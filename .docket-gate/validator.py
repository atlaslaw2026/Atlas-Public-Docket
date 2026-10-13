#!/usr/bin/env python3
"""Atlas Public Docket - publication gate validator (v1.2.1).

v1.2.1 changes vs v1.1.0: blocklisted-name echoes redacted from all emitted
output (findings, detail lines, verdict JSON). Detection conditions,
severities, waiver behavior, and exit codes are unchanged; only the emitted
`matched` text for blocklist-derived categories is replaced with a
non-reversible marker plus a withheld-match count.

Validates a proposed public-docket filing BEFORE it may be published.
Implements section III (publication gate) + section V (filing-type validation)
of the HUMAN ORDER "PUBLIC DOCKET MECHANICAL ENFORCEMENT REPAIR".

Usage:
    validator.py --repo <repo-root> --manifest <publication-manifest.json>
                 --changed-files-file <file> [--blocklist <file>]
                 [--allow-no-git] [--types <filing-types.json>] [--output <verdict.json>]

Exit codes: 0 = PASS (publishable), 2 = BLOCK (not publishable),
            1 = usage / validator-internal error.

Fail-closed design: any check that cannot be performed (missing blocklist,
unresolvable authority reference, unrecognized citation, git history
unavailable without --allow-no-git) BLOCKS the filing and routes it to
human review. The validator never auto-passes on uncertainty.

The privacy scan is a SAFEGUARD, not proof of cleanliness: it catches known
patterns (blocklisted names, emails, phone numbers, credential-like tokens,
private absolute paths). A PASS means "no known pattern found", not "this
text is proven clean". Material uncertainty always routes to the Human.

What the validator CANNOT do (documented, not hidden):
  * It cannot cryptographically prove Clinton Brown typed the authorization
    receipt. It verifies the receipt exists, names him, and its content hash
    matches the exact filed bytes. The real assurance is Clinton's own PR
    review plus the ruleset (PR + required check + publishing identity).
  * It cannot know private names Clinton never told it about. The blocklist
    is only as complete as its maintenance. Single-token hits are ambiguous
    by nature and therefore BLOCK to human review rather than auto-pass.
"""

import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

VERSION = "1.1.0"
HUMAN_NAME = "Clinton Brown"

# Check-result severity ladder. "review" and "fail" both BLOCK the filing:
# "review" means a human must decide; "fail" means a known rule was broken.
BLOCKING = {"review", "fail"}

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(
    r"(?<!\d)(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}(?!\d)"
)
PRIVATE_PATH_RE = re.compile(
    r"(?i)(?:/home/|/users/|%userprofile%|%homepath%|\b[a-z]:[\\/]|~/workspace)"
)
CREDENTIAL_PREFIX_RE = re.compile(
    r"(?i)\b(?:ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|ghu_[A-Za-z0-9]{20,}|"
    r"ghs_[A-Za-z0-9]{20,}|ghr_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
    r"sk-(?:live|test)-[A-Za-z0-9]{16,}|xox[baprs]-[A-Za-z0-9-]{10,}|"
    r"AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)"
)
CREDENTIAL_ASSIGN_RE = re.compile(
    r"(?i)\b(api[_-]?key|api[_-]?secret|client[_-]?secret|secret|token|"
    r"password|passwd|bearer)\b\s*[:=]\s*[\"']?[^\s\"'`]{8,}"
)
HIGH_ENTROPY_TOKEN_RE = re.compile(r"[A-Za-z0-9+/=_-]{24,}")
ENTROPY_THRESHOLD = 4.6  # above the max entropy of hex (4.0); catches base64-ish secrets

# Citation patterns extracted from filing text (unioned with manifest refs).
ORDER_REF_RE = re.compile(r"\bO-[A-Z0-9][A-Z0-9-]{2,}\b")
JUDGMENT_REF_RE = re.compile(r"\bJ-\d{3,4}\b")
RULE_REF_RE = re.compile(r"(?i)\bRule (\d+)\b")
MATTER_REF_RE = re.compile(r"\bPUB-M-\d+\b")
G_REF_RE = re.compile(r"\bG-\d+\b")
DKT_REF_RE = re.compile(r"\bDkt\.?\s*\d+\b", re.IGNORECASE)

PRIVATE_ONLY_PATH_RES = [
    re.compile(r"^docket/ATLAS_"),
    re.compile(r"^private/"),
    re.compile(r"^jobs/"),
    re.compile(r"(?i)\.env$"),
    re.compile(r"(?i)^secrets?/"),
]


def shannon_entropy(s):
    if not s:
        return 0.0
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in freq.values())


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def utcnow_iso():
    return datetime.now(timezone.utc).isoformat()


class Validator:
    def __init__(self, repo, manifest, changed_files, blocklist_names,
                 types, allow_no_git=False, base_ref="origin/master"):
        self.repo = os.path.abspath(repo)
        self.manifest = manifest
        self.manifest_path = None
        self.changed_files = set(changed_files)
        self.blocklist = blocklist_names  # None => fail closed
        self.types = types
        self.allow_no_git = allow_no_git
        # Uniqueness / non-duplication are evaluated against the BASE ref
        # (the branch being merged into), NOT the PR head: the PR head already
        # contains the PR's own new rows/blobs, so head-evaluation denies every
        # compliant filing. v1.1.0 fix.
        self.base_ref = base_ref
        self.checks = []
        self.block_reasons = []
        self.findings = []  # privacy findings
        self.file_hashes = {}  # repo-rel path -> sha256

    # -- plumbing -----------------------------------------------------
    def check(self, name, result, detail):
        self.checks.append({"name": name, "result": result, "detail": detail})
        if result in BLOCKING:
            self.block_reasons.append(f"[{name}] {detail}")

    def repo_path(self, rel):
        return os.path.join(self.repo, rel)

    def git(self, *args):
        return subprocess.run(
            ["git", "-C", self.repo] + list(args),
            capture_output=True, timeout=120,
        )

    def is_git_repo(self):
        p = self.git("rev-parse", "--git-dir")
        return p.returncode == 0

    def base_ref_ok(self):
        p = self.git("rev-parse", "--verify", "--quiet", self.base_ref + "^{commit}")
        return p.returncode == 0

    def base_show(self, rel):
        """Bytes of rel at the base ref, or None if absent/unresolvable."""
        p = self.git("show", f"{self.base_ref}:{rel}")
        if p.returncode != 0:
            return None
        return p.stdout

    def base_path_exists(self, rel):
        p = self.git("cat-file", "-e", f"{self.base_ref}:{rel}")
        return p.returncode == 0

    # -- check 1: manifest schema / mandatory fields ------------------
    def check_manifest_schema(self):
        m = self.manifest
        rtype = m.get("record_type")
        tdef = self.types["record_types"].get(rtype)
        if tdef is None:
            self.check("manifest-schema", "fail",
                       f"Unknown record_type {rtype!r}. Known types: "
                       f"{sorted(self.types['record_types'])}.")
            return None
        missing = [f for f in tdef["required_fields"] if f not in m or m[f] in (None, "")]
        if missing:
            self.check("manifest-schema", "fail",
                       f"record_type {rtype!r} missing mandatory fields: {missing}.")
            return None
        rid = m.get("record_id", "")
        if not re.match(tdef["record_id_pattern"] + r"\Z", rid):
            self.check("manifest-schema", "fail",
                       f"record_id {rid!r} does not match required pattern "
                       f"{tdef['record_id_pattern']!r} for type {rtype!r}.")
            return None
        files = m.get("files", [])
        if not files or not any(f.get("role") == "primary" for f in files):
            self.check("manifest-schema", "fail",
                       "files[] must be non-empty and designate one primary file.")
            return None
        primaries = [f for f in files if f.get("role") == "primary"]
        if len(primaries) != 1:
            self.check("manifest-schema", "fail",
                       f"Exactly one primary file required; found {len(primaries)}.")
            return None
        primary = primaries[0]["path"]
        if not re.match(tdef["primary_destination_pattern"] + r"\Z", primary):
            self.check("manifest-schema", "fail",
                       f"Primary destination {primary!r} does not match required pattern "
                       f"{tdef['primary_destination_pattern']!r} for type {rtype!r}.")
            return None
        if not isinstance(m.get("authority_refs", []), list):
            self.check("manifest-schema", "fail", "authority_refs must be a list.")
            return None
        self.check("manifest-schema", "pass",
                   f"record_type={rtype}, record_id={rid}, primary={primary}.")
        return tdef

    # -- check 2: record id uniqueness --------------------------------
    def check_record_id_unique(self, tdef):
        # Evaluated against the BASE ref: the PR head already contains this
        # PR's own new rows/files, so head-evaluation would deny every filing.
        rtype, rid = self.manifest["record_type"], self.manifest["record_id"]
        if not self.is_git_repo() or not self.base_ref_ok():
            if self.allow_no_git:
                self.check("record-id-unique", "skipped",
                           "--allow-no-git and no resolvable base ref: uniqueness not "
                           "checked. CI must run with full history.")
                return
            self.check("record-id-unique", "review",
                       f"Base ref {self.base_ref!r} not resolvable: cannot prove id "
                       f"uniqueness. Human review required, or run with full history.")
            return
        if rtype in ("order", "standing-order", "correction"):
            raw = self.base_show("law/orders/INDEX.json")
            if raw is None:
                self.check("record-id-unique", "pass",
                           f"record_id {rid!r}: no law/orders/INDEX.json at base; "
                           f"treated as empty.")
                return
            try:
                rows = json.loads(raw.decode("utf-8"))
                ids = {r.get("id") for r in rows} if isinstance(rows, list) \
                    else {r.get("id") for r in rows.get("rows", [])}
            except Exception as e:
                self.check("record-id-unique", "review",
                           f"Could not parse base law/orders/INDEX.json ({e}); cannot "
                           f"prove id uniqueness. Human review required.")
                return
            if rid in ids:
                self.check("record-id-unique", "fail",
                           f"record_id {rid!r} is already filed (present in base "
                           f"law/orders/INDEX.json). New filings need new identities.")
            else:
                self.check("record-id-unique", "pass",
                           f"record_id {rid!r} not present in base law/orders/INDEX.json.")
        elif rtype == "judgment":
            if self.base_path_exists(f"law/judgments/{rid}.json"):
                self.check("record-id-unique", "fail",
                           f"law/judgments/{rid}.json already exists at base.")
            else:
                self.check("record-id-unique", "pass",
                           f"law/judgments/{rid}.json does not exist at base.")
        elif rtype == "matter-row":
            found = self._matter_row_exists_base(rid)
            if found is None:
                self.check("record-id-unique", "pass",
                           f"No matters.json/MATTERS.md at base; treated as empty.")
            elif found:
                self.check("record-id-unique", "fail",
                           f"matter {rid!r} already has a public row at base.")
            else:
                self.check("record-id-unique", "pass",
                           f"matter {rid!r} has no public row at base.")
        elif rtype == "receipt":
            if self.base_path_exists(f"docket/receipts/{rid}.json"):
                self.check("record-id-unique", "fail",
                           f"docket/receipts/{rid}.json already exists at base.")
            else:
                self.check("record-id-unique", "pass",
                           f"docket/receipts/{rid}.json does not exist at base.")

    def _matter_row_exists_base(self, rid):
        raw = self.base_show("docket/matters.json")
        if raw is not None:
            try:
                data = json.loads(raw.decode("utf-8"))
                rows = data if isinstance(data, list) else data.get("rows", data.get("matters", []))
                return any(r.get("id") == rid or r.get("matter_id") == rid for r in rows)
            except Exception:
                return None
        raw = self.base_show("docket/MATTERS.md")
        if raw is not None:
            return rid in raw.decode("utf-8", errors="replace")
        return None

    # -- check 3: destination allowed ---------------------------------
    def check_destination_allowed(self):
        bad = []
        for f in self.manifest["files"]:
            p = f["path"]
            if ".." in p or p.startswith("/") or "\\" in p:
                bad.append(f"{p}: path traversal / absolute path not allowed")
                continue
            for rx in PRIVATE_ONLY_PATH_RES:
                if rx.search(p):
                    bad.append(f"{p}: targets a private-canonical path; private records "
                               f"must never be filed to the public repo")
        if bad:
            self.check("destination-allowed", "fail", "; ".join(bad))
        else:
            self.check("destination-allowed", "pass",
                       "All destinations are public-repo paths, no traversal.")

    # -- check 4: classification --------------------------------------
    def check_classification(self, tdef):
        cls = self.manifest.get("classification")
        if cls not in tdef["allowed_classifications"]:
            self.check("classification-consistent", "fail",
                       f"classification {cls!r} not allowed for type "
                       f"{self.manifest['record_type']!r} (allowed: "
                       f"{tdef['allowed_classifications']}).")
            return
        if cls == "private":
            # Belt and braces: the type table never allows private here, but if
            # it ever did, this validator still refuses the public repo.
            self.check("classification-consistent", "fail",
                       "classification 'private' can never be filed to the public repo. "
                       "File it on the private canonical docket instead.")
            return
        self.check("classification-consistent", "pass",
                   f"classification={cls!r} allowed for this type and consistent with "
                   f"a public-repo destination.")

    # -- check 5: authority references resolve -------------------------
    def _resolve_ref(self, ref):
        """Returns (ok: bool|None, detail). None = cannot verify from public tree."""
        if re.fullmatch(r"O-[A-Z0-9][A-Z0-9-]*", ref):
            p = self.repo_path(f"law/orders/{ref}.md")
            if os.path.exists(p):
                return True, f"{ref} -> law/orders/{ref}.md"
            idx = self.repo_path("law/orders/INDEX.json")
            if os.path.exists(idx):
                try:
                    rows = json.load(open(idx, encoding="utf-8"))
                    ids = {r.get("id") for r in (rows if isinstance(rows, list)
                                                 else rows.get("rows", []))}
                    if ref in ids:
                        return True, f"{ref} -> row in law/orders/INDEX.json (body not in tree)"
                except Exception:
                    pass
            return False, f"{ref}: no law/orders/{ref}.md and no INDEX.json row"
        if re.fullmatch(r"J-\d+", ref):
            p = self.repo_path(f"law/judgments/{ref}.json")
            return (True, f"{ref} -> law/judgments/{ref}.json") if os.path.exists(p) \
                else (False, f"{ref}: law/judgments/{ref}.json not found")
        m = re.fullmatch(r"(?i)Rule (\d+)", ref)
        if m:
            arp = self.repo_path("AR/README.md")
            if not os.path.exists(arp):
                return False, f"{ref}: AR/README.md not in tree"
            text = open(arp, encoding="utf-8", errors="replace").read()
            if re.search(r"(?i)\bRule " + m.group(1) + r"\b", text):
                return True, f"{ref} -> AR/README.md"
            return False, f"{ref}: no 'Rule {m.group(1)}' in AR/README.md"
        if re.fullmatch(r"PUB-M-\d+", ref):
            mj = self.repo_path("docket/matters.json")
            mm = self.repo_path("docket/MATTERS.md")
            hit = False
            if os.path.exists(mj):
                try:
                    data = json.load(open(mj, encoding="utf-8"))
                    rows = data if isinstance(data, list) else data.get("rows", data.get("matters", []))
                    hit = any(r.get("id") == ref or r.get("matter_id") == ref for r in rows)
                except Exception:
                    pass
            if not hit and os.path.exists(mm):
                hit = ref in open(mm, encoding="utf-8", errors="replace").read()
            return (True, f"{ref} -> public matter row") if hit \
                else (False, f"{ref}: no public matter row found")
        if re.fullmatch(r"G-\d+", ref):
            return None, (f"{ref}: G-n records live on the private canonical docket "
                          f"(ATLAS_GOVERNANCE_FILINGS.json), which is not in the public "
                          f"tree. Cannot verify from here - human must confirm on the "
                          f"private record.")
        if re.fullmatch(r"(?i)Dkt\.?\s*\d+", ref):
            lp = self.repo_path("viewer/docket/INDEX.json")
            if os.path.exists(lp) and ref.split()[-1] in open(lp, encoding="utf-8", errors="replace").read():
                return True, f"{ref} -> viewer/docket/INDEX.json (legacy series)"
            return False, f"{ref}: not found in viewer/docket/INDEX.json"
        if ref in ("Constitution", "CURRENT_LAW.md", "AGENTS.md", "AR/README.md"):
            p = self.repo_path(ref if ref.endswith(".md") else "constitution.md")
            alt = {"Constitution": ["constitution.md", "CONSTITUTION.md",
                                    "law/constitution.md"]}.get(ref, [p])
            for cand in alt:
                if os.path.exists(self.repo_path(cand)):
                    return True, f"{ref} -> {cand}"
            return False, f"{ref}: not present in this tree"
        return None, (f"{ref}: unrecognized citation format. The validator only resolves "
                      f"O-*, J-*, Rule n, PUB-M-*, G-*, Dkt. n and named law files. "
                      f"Human review required.")

    def _extract_refs_from_text(self, text, self_id):
        refs = set()
        for rx in (ORDER_REF_RE, JUDGMENT_REF_RE, MATTER_REF_RE, G_REF_RE):
            refs.update(rx.findall(text))
        for m in RULE_REF_RE.finditer(text):
            refs.add(f"Rule {m.group(1)}")
        refs.update(m.group(0) for m in DKT_REF_RE.finditer(text))
        refs.discard(self_id)
        return refs

    def check_authority_refs(self):
        manifest_refs = list(dict.fromkeys(self.manifest.get("authority_refs", [])))
        # Union with citations extracted from the primary file's text.
        primary = next(f["path"] for f in self.manifest["files"] if f.get("role") == "primary")
        text = open(self.repo_path(primary), encoding="utf-8", errors="replace").read()
        text_refs = self._extract_refs_from_text(text, self.manifest["record_id"])
        all_refs = list(dict.fromkeys(manifest_refs + sorted(text_refs)))
        if not all_refs:
            self.check("authority-refs-resolve", "review",
                       "No authority references found in manifest or filing text. A public "
                       "filing with no cited authority is a material uncertainty - human "
                       "review required.")
            return
        ok, failed, unverifiable = [], [], []
        for ref in all_refs:
            status, detail = self._resolve_ref(ref)
            if status is True:
                ok.append(ref)
            elif status is False:
                failed.append(detail)
            else:
                unverifiable.append(detail)
        detail = (f"resolved: {ok}; unresolvable: {failed}; "
                  f"not verifiable from public tree: {unverifiable}")
        if failed or unverifiable:
            self.check("authority-refs-resolve", "review" if not failed else "fail",
                       detail + " - every cited authority must resolve; unresolvable or "
                       "unverifiable citations block publication pending human confirmation.")
        else:
            self.check("authority-refs-resolve", "pass", detail)

    # -- check 6: Order-vs-Matter rules (2026-10-12 clarifications) -----
    def check_order_matter_rules(self):
        rtype = self.manifest["record_type"]
        linkage = self.manifest.get("matter_linkage")
        if rtype == "standing-order":
            if linkage:
                self.check("order-matter-rules", "review",
                           f"Standing orders stand alone with authority + provenance (HC1); "
                           f"matter_linkage={linkage!r} looks like an artificial matter "
                           f"number. Confirm with the Human that a real proceeding requires it.")
            else:
                self.check("order-matter-rules", "pass",
                           "Standing order carries no matter number, per HC1.")
            return
        if rtype == "matter-row":
            if linkage and linkage != self.manifest["record_id"]:
                self.check("order-matter-rules", "fail",
                           "A matter-row's linkage must be null or its own id.")
            else:
                self.check("order-matter-rules", "pass",
                           "Matter row linkage self-consistent.")
            return
        # order / judgment / correction / receipt
        if not linkage:
            self.check("order-matter-rules", "pass",
                       "No matter linkage. Per the 2026-10-12 clarifications (HC2): Orders "
                       "are NOT Matters; an unlinked Order is not a defect. No linkage "
                       "required, none invented.")
            return
        status, detail = self._resolve_ref(linkage)
        if status is True:
            self.check("order-matter-rules", "pass",
                       f"matter_linkage {linkage!r} resolves: {detail}.")
        elif status is False:
            self.check("order-matter-rules", "fail",
                       f"matter_linkage {linkage!r} does not resolve: {detail}.")
        else:
            self.check("order-matter-rules", "review",
                       f"matter_linkage {linkage!r} not verifiable from the public tree: "
                       f"{detail} Human must confirm on the private record.")

    # -- check 7: authorization receipt --------------------------------
    def check_authorization_receipt(self):
        primary = next(f["path"] for f in self.manifest["files"] if f.get("role") == "primary")
        content_hash = sha256_file(self.repo_path(primary))
        self.file_hashes[primary] = content_hash
        rec = self.manifest.get("authorization_receipt")
        if not isinstance(rec, dict):
            self.check("authorization-receipt", "fail",
                       "No authorization receipt in manifest. Publication requires a "
                       "recorded authorization: who authorized, under what authority, "
                       "hash of the exact content authorized. No receipt = no publication.")
            return
        problems = []
        if rec.get("authorized_by") != HUMAN_NAME:
            problems.append(f"authorized_by must be exactly {HUMAN_NAME!r} (the Human); "
                            f"got {rec.get('authorized_by')!r}")
        if not rec.get("authority"):
            problems.append("authority field empty: the receipt must state under what "
                            "authority the Human authorized this (e.g. 'Human level-2 "
                            "direct order 2026-10-12' or 'standing authorization O-PROVE-DONE')")
        if not rec.get("authorized_at"):
            problems.append("authorized_at missing (ISO timestamp required)")
        else:
            try:
                ts = datetime.fromisoformat(rec["authorized_at"])
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
                if ts > datetime.now(timezone.utc):
                    problems.append("authorized_at is in the future")
            except Exception:
                problems.append("authorized_at is not a parseable ISO timestamp")
        if rec.get("content_sha256") != content_hash:
            problems.append(f"content_sha256 {rec.get('content_sha256')!r} does not match "
                            f"the filed bytes ({content_hash}). The authorization must "
                            f"cover the EXACT content being published; any byte difference "
                            f"voids it.")
        if problems:
            self.check("authorization-receipt", "fail",
                       "Authorization receipt defective: " + "; ".join(problems))
        else:
            self.check("authorization-receipt", "pass",
                       f"Receipt names {HUMAN_NAME}, authority stated, timestamp valid, "
                       f"content hash matches filed bytes ({content_hash[:16]}...). "
                       f"NOTE: the validator verifies the receipt's presence and hash, not "
                       f"that the Human truly typed it - that assurance is Clinton's PR "
                       f"review plus the ruleset.")
        self.auth_receipt_hash = hashlib.sha256(
            canonical_json(rec).encode("utf-8")).hexdigest()
        self.auth_authority = rec.get("authority", "")

    # -- check 8: privacy scan (SAFEGUARD) ------------------------------
    def _waivers(self):
        return self.manifest.get("privacy_waivers", []) or []

    def _is_waived(self, matched_text, category):
        for w in self._waivers():
            if not isinstance(w, dict):
                continue
            if w.get("approved_by") != HUMAN_NAME or not w.get("justification"):
                continue
            needle = str(w.get("match", ""))
            if needle and needle.lower() in matched_text.lower():
                return True, w
        return False, None

    # v1.2.1: categories whose `matched` text derives from the blocklist itself.
    # Emitting the matched name would leak the blocklist one finding at a time
    # (blocklist oracle). The waiver check above runs on the true matched text
    # BEFORE redaction, so waiver behavior is unchanged; only emitted text is
    # redacted. Detection conditions, severities, and exit codes are untouched.
    REDACTED_CATEGORIES = frozenset({"private-name", "ambiguous-name-token"})
    REDACTED_MARKER = "[blocklisted name withheld]"

    def _add_finding(self, category, matched, location, severity):
        waived, waiver = self._is_waived(matched, category)
        emitted = (self.REDACTED_MARKER
                   if category in self.REDACTED_CATEGORIES
                   else matched[:120])
        self.findings.append({
            "category": category,
            "matched": emitted,
            "location": location,
            "severity": severity,           # "fail" or "review"
            "waived": waived,
            "waiver_justification": (waiver or {}).get("justification") if waived else None,
        })

    def _scan_text(self, text, location):
        # 1. blocklisted names
        if self.blocklist is None:
            self._add_finding("blocklist-unavailable",
                              "no blocklist supplied", location, "review")
        else:
            for name in self.blocklist:
                if " " in name.strip():
                    if re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", text,
                                 re.IGNORECASE):
                        self._add_finding("private-name", name, location, "fail")
                else:
                    if re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", text,
                                 re.IGNORECASE):
                        self._add_finding("ambiguous-name-token", name, location, "review")
        # 2. emails
        for m in EMAIL_RE.finditer(text):
            self._add_finding("email", m.group(0), location, "fail")
        # 3. phones
        for m in PHONE_RE.finditer(text):
            self._add_finding("phone", m.group(0), location, "review")
        # 4. credential-like
        for m in CREDENTIAL_PREFIX_RE.finditer(text):
            self._add_finding("credential-token", m.group(0)[:40] + "...", location, "fail")
        for m in CREDENTIAL_ASSIGN_RE.finditer(text):
            self._add_finding("credential-assignment", m.group(0)[:80], location, "fail")
        for m in HIGH_ENTROPY_TOKEN_RE.finditer(text):
            tok = m.group(0)
            if shannon_entropy(tok) >= ENTROPY_THRESHOLD and not tok.startswith("http"):
                self._add_finding("high-entropy-string", tok[:40] + "...", location, "review")
        # 5. private absolute paths
        for m in PRIVATE_PATH_RE.finditer(text):
            self._add_finding("private-path", m.group(0), location, "fail")

    def check_privacy_scan(self):
        if self.blocklist is None:
            self.check("privacy-scan", "review",
                       "No name blocklist available (no --blocklist file and no "
                       "DOCKET_NAME_BLOCKLIST env). The name check cannot run, so the "
                       "filing cannot be proven name-clean. Supply the blocklist.")
            # still run the pattern scans below
        for f in self.manifest["files"]:
            p = f["path"]
            full = self.repo_path(p)
            if p not in self.changed_files:
                self._add_finding("manifest-mismatch",
                                  f"{p} listed in manifest but not in the PR's changed files",
                                  "manifest", "fail")
                continue
            if not os.path.exists(full):
                self._add_finding("missing-file", f"{p} not found in working tree",
                                  "manifest", "fail")
                continue
            if p not in self.file_hashes:
                self.file_hashes[p] = sha256_file(full)
            try:
                text = open(full, encoding="utf-8", errors="replace").read()
            except Exception as e:
                self._add_finding("unreadable-file", f"{p}: {e}", "manifest", "review")
                continue
            self._scan_text(text, p)
        # Manifest-level free text also merges to master with the PR (the
        # manifest file itself is committed), so scan it too. v1.1.0 fix:
        # `notes` previously merged unscanned.
        free_texts = []
        _notes = self.manifest.get("notes")
        if isinstance(_notes, str) and _notes.strip():
            free_texts.append((_notes, "manifest:notes"))
        _rec = self.manifest.get("authorization_receipt") or {}
        _auth = _rec.get("authority")
        if isinstance(_auth, str) and _auth.strip():
            free_texts.append((_auth, "manifest:authorization_receipt.authority"))
        for _i, _w in enumerate(self._waivers()):
            _j = _w.get("justification") if isinstance(_w, dict) else None
            if isinstance(_j, str) and _j.strip():
                free_texts.append((_j, f"manifest:privacy_waivers[{_i}].justification"))
        for _text, _loc in free_texts:
            self._scan_text(_text, _loc)
        active = [x for x in self.findings if not x["waived"]]
        waived = [x for x in self.findings if x["waived"]]
        # invalid waivers (wrong approver / empty justification) are themselves a flag
        bad_waivers = [w for w in self._waivers()
                       if not isinstance(w, dict) or w.get("approved_by") != HUMAN_NAME
                       or not w.get("justification")]
        detail_lines = []
        for x in active:
            detail_lines.append(f"{x['severity'].upper()} {x['category']} @ {x['location']}: "
                                f"{x['matched']!r}")
        for x in waived:
            detail_lines.append(f"WAIVED {x['category']} @ {x['location']}: {x['matched']!r} "
                                f"(justification: {x['waiver_justification']!r})")
        # v1.2.1: report how many blocklisted-name matches were withheld so the
        # reviewer knows the count without learning the names. Locations above
        # are file paths, not secret content.
        n_withheld = sum(1 for x in active
                         if x["category"] in self.REDACTED_CATEGORIES)
        if n_withheld:
            detail_lines.append(
                f"NOTE: {n_withheld} blocklisted-name match(es) withheld from "
                f"output (see locations above).")
        for w in bad_waivers:
            detail_lines.append(f"INVALID WAIVER IGNORED: {str(w)[:100]!r} (waivers must be "
                                f"approved_by {HUMAN_NAME!r} with a non-empty justification)")
        header = ("SAFEGUARD scan, not proof of cleanliness. A PASS means no known "
                  "pattern was found; it does not prove the text is clean. ")
        if bad_waivers:
            self.check("privacy-scan", "fail", header +
                       "Invalid waiver entries present (wrong approver or empty "
                       "justification); they were ignored. " + " | ".join(detail_lines))
        elif any(x["severity"] == "fail" for x in active):
            self.check("privacy-scan", "fail", header + " | ".join(detail_lines))
        elif any(x["severity"] == "review" for x in active):
            self.check("privacy-scan", "review", header +
                       "Ambiguous findings require human judgment; nothing here auto-passes. "
                       + " | ".join(detail_lines))
        else:
            tail = (" | ".join(detail_lines) if detail_lines
                    else "no findings in any category")
            self.check("privacy-scan", "pass", header + tail)

    # -- check 9: no-op / duplicate blob -------------------------------
    def _base_blob_hashes(self):
        """Map sha256(content) -> list of git blob sha1s, for blobs reachable
        from the BASE ref only. Blobs introduced by the PR itself are NOT
        reachable from base, so the PR's own new files can never self-match.
        (v1.1.0 fix: the old all-history enumeration matched the PR's own
        blobs and denied every filing.)"""
        rl = self.git("rev-list", "--objects", self.base_ref)
        if rl.returncode != 0:
            return None
        obj_ids = [l.split()[0] for l in rl.stdout.decode("utf-8", "replace").splitlines()
                   if l.strip()]
        if not obj_ids:
            return {}
        chk = subprocess.run(
            ["git", "-C", self.repo, "cat-file", "--batch-check"],
            input="\n".join(obj_ids).encode(), capture_output=True, timeout=180)
        if chk.returncode != 0:
            return None
        blob_ids = []
        for line in chk.stdout.split(b"\n"):
            parts = line.split()
            if len(parts) >= 2 and parts[1] == b"blob":
                blob_ids.append(parts[0])
        if not blob_ids:
            return {}
        # Stream all blob contents through one `git cat-file --batch` call.
        proc = subprocess.run(
            ["git", "-C", self.repo, "cat-file", "--batch"],
            input=b"\n".join(blob_ids), capture_output=True, timeout=300)
        if proc.returncode != 0:
            return None
        out, pos, result = proc.stdout, 0, {}
        idx = 0
        while pos < len(out) and idx < len(blob_ids):
            nl = out.find(b"\n", pos)
            if nl == -1:
                break
            header = out[pos:nl].split()
            pos = nl + 1
            if len(header) < 3:
                break
            try:
                size = int(header[2])
            except ValueError:
                break
            content = out[pos:pos + size]
            pos += size
            if pos < len(out) and out[pos:pos + 1] == b"\n":
                pos += 1
            result.setdefault(hashlib.sha256(content).hexdigest(), []).append(
                blob_ids[idx].decode())
            idx += 1
        return result

    def check_no_duplicate(self):
        if not self.is_git_repo() or not self.base_ref_ok():
            if self.allow_no_git:
                self.check("no-duplicate-blob", "skipped",
                           "--allow-no-git and no resolvable base ref: history "
                           "comparison skipped. CI must run with full history.")
                return
            self.check("no-duplicate-blob", "review",
                       f"Base ref {self.base_ref!r} not resolvable: cannot prove this "
                       f"blob was not already filed. Human review required, or run "
                       f"with full history.")
            return
        blob_map = self._base_blob_hashes()
        if blob_map is None:
            self.check("no-duplicate-blob", "review",
                       "Could not enumerate base blobs; cannot prove non-duplication. "
                       "Human review required.")
            return
        dupes = []
        for f in self.manifest["files"]:
            p = f["path"]
            h = self.file_hashes.get(p) or (
                sha256_file(self.repo_path(p)) if os.path.exists(self.repo_path(p)) else None)
            if h and h in blob_map:
                log = self.git("log", self.base_ref, "--find-object=" + blob_map[h][0],
                               "--format=%H %ci %s")
                commits = log.stdout.decode("utf-8", "replace").strip().split("\n")[:3]
                dupes.append(f"{p} (sha256 {h[:16]}...) already filed at base; e.g. "
                             "commit(s): " + " | ".join(commits))
        if dupes:
            self.check("no-duplicate-blob", "fail",
                       "Identical blob already filed (no-op / duplicate filing): "
                       + "; ".join(dupes))
        else:
            self.check("no-duplicate-blob", "pass",
                       f"None of the {len(self.manifest['files'])} filed blob(s) matches any "
                       f"blob reachable from base {self.base_ref} "
                       f"({len(blob_map)} distinct content hashes).")

    # -- check 10: index coverage --------------------------------------
    def check_index_coverage(self):
        rtype = self.manifest["record_type"]
        tdef = self.types["record_types"][rtype]
        cov = tdef.get("index_coverage", "")
        if not cov or cov.startswith("none"):
            self.check("index-coverage", "pass",
                       f"No index coverage mandated for type {rtype!r} by controlling law.")
            return
        changed = self.changed_files
        missing = []
        if "INDEX.json" in cov and "law/orders/INDEX.json" not in changed:
            # only required if the index exists in this tree
            if os.path.exists(self.repo_path("law/orders/INDEX.json")):
                missing.append("law/orders/INDEX.json (the HC1 discoverability row)")
        if "AR/README.md" in cov and "AR/README.md" not in changed:
            missing.append("AR/README.md (the one-sentence rule entry)")
        if "matters.json or docket/MATTERS.md" in cov and not (
                "docket/matters.json" in changed or "docket/MATTERS.md" in changed):
            missing.append("docket/matters.json or docket/MATTERS.md (the public row)")
        if "CURRENT_LAW.md" in cov and "CURRENT_LAW.md" not in changed:
            missing.append("CURRENT_LAW.md (Active Judgments table)")
        # correction: superseded file must NOT be among changed files
        if rtype == "correction":
            sup = self.manifest.get("supersedes", "")
            m = re.fullmatch(r"O-[A-Z0-9][A-Z0-9-]*", sup or "")
            if m:
                sup_path = f"law/orders/{sup}.md"
                if sup_path in changed:
                    self.check("index-coverage", "fail",
                               f"Correction {self.manifest['record_id']} edits the superseded "
                               f"file {sup_path} in place. Corrections take a NEW identity; "
                               f"the superseded text is never edited (Art. VIII section 5).")
                    return
            j = re.fullmatch(r"J-\d+", sup or "")
            if j and f"law/judgments/{sup}.json" in changed:
                self.check("index-coverage", "fail",
                           f"Correction edits the superseded judgment file in place - "
                           f"forbidden (Art. VIII section 5).")
                return
        if missing:
            self.check("index-coverage", "fail",
                       "Controlling law requires these to be filed with the record, but "
                       "they are not in the PR's changed files: " + "; ".join(missing))
        else:
            self.check("index-coverage", "pass",
                       f"Required companion filing(s) present: {cov}.")

    # -- run -----------------------------------------------------------
    def run(self):
        tdef = self.check_manifest_schema()
        if tdef is None:
            return self.verdict()
        # hash primary early (needed by several checks); authorization check
        # re-verifies the hash itself.
        primary = next(f["path"] for f in self.manifest["files"] if f.get("role") == "primary")
        if os.path.exists(self.repo_path(primary)):
            self.file_hashes[primary] = sha256_file(self.repo_path(primary))
        self.check_record_id_unique(tdef)
        self.check_destination_allowed()
        self.check_classification(tdef)
        self.check_authority_refs()
        self.check_order_matter_rules()
        self.check_authorization_receipt()
        self.check_privacy_scan()
        self.check_no_duplicate()
        self.check_index_coverage()
        return self.verdict()

    def verdict(self):
        blocked = any(c["result"] in BLOCKING for c in self.checks)
        primary = None
        try:
            primary = next(f["path"] for f in self.manifest["files"]
                           if f.get("role") == "primary")
        except Exception:
            pass
        return {
            "verdict": "block" if blocked else "pass",
            "validator": f"atlas-publication-gate/{VERSION}",
            "record_type": self.manifest.get("record_type"),
            "record_id": self.manifest.get("record_id"),
            "classification": self.manifest.get("classification"),
            "primary_file": primary,
            "content_sha256": self.file_hashes.get(primary),
            "repo": self.repo,
            "checked_at": utcnow_iso(),
            "checks": self.checks,
            "block_reasons": self.block_reasons,
            "receipt": {
                "authorization_receipt_hash": getattr(self, "auth_receipt_hash", None),
                "authorization_authority": getattr(self, "auth_authority", None),
            },
        }


def load_blocklist(path, env_value):
    names = []
    if path and os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    names.append(line)
        return names
    if env_value:
        return [l.strip() for l in env_value.splitlines()
                if l.strip() and not l.strip().startswith("#")]
    return None  # fail closed: validator blocks without a blocklist


def main(argv=None):
    ap = argparse.ArgumentParser(description="Atlas public-docket publication gate validator.")
    ap.add_argument("--repo", required=True, help="Repo working tree (PR head checkout).")
    ap.add_argument("--manifest", required=True, help="publication-manifest.json path.")
    ap.add_argument("--changed-files", nargs="*", default=[],
                    help="Repo-relative paths changed by this PR.")
    ap.add_argument("--changed-files-file", default=None,
                    help="File listing changed paths, one per line.")
    ap.add_argument("--blocklist", default=None,
                    help="Path to person-names.blocklist. NEVER commit this file to the "
                         "public repo; in CI it is materialized from a secret.")
    ap.add_argument("--types", default=None,
                    help="filing-types.json path (default: alongside validator.py).")
    ap.add_argument("--allow-no-git", action="store_true",
                    help="Allow the duplicate-blob check to skip when git history is "
                         "unavailable (local pre-checks only; CI must not use this).")
    ap.add_argument("--base-ref", default="origin/master",
                    help="Git ref uniqueness/non-duplication are evaluated against "
                         "(default: origin/master). The PR head already contains the "
                         "PR's own rows/blobs, so head-evaluation would deny every "
                         "compliant filing.")
    ap.add_argument("--output", default=None, help="Write verdict JSON to this path.")
    args = ap.parse_args(argv)

    types_path = args.types or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                            "filing-types.json")
    try:
        with open(types_path, encoding="utf-8") as f:
            types = json.load(f)
    except Exception as e:
        print(json.dumps({"verdict": "block", "error": f"cannot load filing-types: {e}"}))
        return 1
    try:
        with open(args.manifest, encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as e:
        print(json.dumps({"verdict": "block", "error": f"cannot load manifest: {e}"}))
        return 1

    changed = list(args.changed_files)
    if args.changed_files_file:
        try:
            with open(args.changed_files_file, encoding="utf-8") as f:
                changed += [l.strip() for l in f if l.strip()]
        except Exception as e:
            print(json.dumps({"verdict": "block", "error": f"cannot read changed-files: {e}"}))
            return 1

    blocklist = load_blocklist(args.blocklist, os.environ.get("DOCKET_NAME_BLOCKLIST"))

    v = Validator(args.repo, manifest, changed, blocklist, types,
                  allow_no_git=args.allow_no_git, base_ref=args.base_ref)
    v.manifest_path = args.manifest
    verdict = v.run()
    out = json.dumps(verdict, indent=2, ensure_ascii=False)
    print(out)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(out)
    return 2 if verdict["verdict"] == "block" else 0


if __name__ == "__main__":
    sys.exit(main())
