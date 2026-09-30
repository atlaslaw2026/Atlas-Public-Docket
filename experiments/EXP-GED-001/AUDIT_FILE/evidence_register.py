#!/usr/bin/env python3
"""Builds the EXP-GED-001 audit-file evidence register: stable IDs → paths, SHA-256, first-commit time, kind.
Kind: C = contemporaneous experimental evidence (produced during the experiment by the acting component);
      I = later interpretation (audit, scoring, findings, white-paper claims);  D = design (pre-registered or specification).
Run from the repository root. Output: AUDIT_FILE/EVIDENCE_REGISTER.md and .json"""
import hashlib, json, os, subprocess, glob
B = "experiments/EXP-GED-001"
R = [
 ("E-01","D","Experiment definition, hypothesis, design (Phase 3)",["P3/00_matter/MATTER.md"]),
 ("E-02","D","Pre-registration with sealed-item hashes (pushed before any Phase 3 run)",["P3/00_matter/PREREGISTRATION.md"]),
 ("E-03","D","Authoritative store integrity manifest",["P3/00_matter/STORE_MANIFEST.sha256"]),
 ("E-04","D","Authorization policy (client identities, licenses, disclosure rules)",["P3/00_matter/authorization_policy.json"]),
 ("E-05","D","Simulated MCP-style interface: specification, code, manifest",["P3/00_matter/INTERFACE_SPEC.md","P3/harness/mcp.py","P3/harness/build_backend.py","P3/harness/INTERFACE.md","P3/00_matter/INTERFACE_MANIFEST.sha256"]),
 ("E-06","D","Exact client questions (identical in both conditions)",["P3/00_matter/QUESTIONS.md"]),
 ("E-07","D","Exact prompts for every office",sorted(glob.glob(f"{B}/P3/00_matter/prompts/*.md"))),
 ("E-08","D","Private Atlas steps not performed; experiment-built components",["P3/00_matter/PRIVATE_STEPS_NOT_PERFORMED.md"]),
 ("E-09","C","Condition A run r1: answer, interface log (requests and returned data), agent audit, source commit",["P3/runs/r1/A/ANSWERS.md","P3/runs/r1/A/mcp_log.jsonl","P3/runs/r1/A/AUDIT.md","P3/runs/r1/A/SOURCE.txt"]),
 ("E-10","C","Condition A run r2",["P3/runs/r2/A/ANSWERS.md","P3/runs/r2/A/mcp_log.jsonl","P3/runs/r2/A/AUDIT.md","P3/runs/r2/A/SOURCE.txt"]),
 ("E-11","C","Condition A run r3",["P3/runs/r3/A/ANSWERS.md","P3/runs/r3/A/mcp_log.jsonl","P3/runs/r3/A/AUDIT.md","P3/runs/r3/A/SOURCE.txt"]),
 ("E-12","C","Access-boundary determinations for each A run (deterministic; experiment-built)",["P3/harness/access_boundary.py"]+[f"P3/runs/r{n}/B/access/ACCESS_DETERMINATION.json" for n in (1,2,3)]),
 ("E-13","C","Condition B Analyst (truth boundary): claim ledgers, arguments, computations, own interface logs",[f"P3/runs/r{n}/B/analyst/{f}" for n in (1,2,3) for f in ("CLAIM_LEDGER.json","ARGUMENT.md","analysis.py","analysis_output.txt","mcp_log.jsonl","HANDBACK.md","READ_LOG.md")]),
 ("E-14","C","Condition B independent Challengers",[f"P3/runs/r{n}/B/challenge/{f}" for n in (1,2,3) for f in ("COUNTERARGUMENT.md","reconstruct.py","reconstruct_output.txt","mcp_log.jsonl","HANDBACK.md","READ_LOG.md")]),
 ("E-15","C","Magistrate determinations and machine-readable approved/rejected claims",[f"P3/runs/r{n}/B/magistrate/{f}" for n in (1,2,3) for f in ("DETERMINATION.md","APPROVED_CLAIMS.json","mcp_log.jsonl","READ_LOG.md","HANDBACK.md")]),
 ("E-16","C","r2 Magistrate linked correction (Q7.4R) after gate failure",["P3/runs/r2/B/magistrate/APPROVED_CLAIMS_CORRECTION_1.json","P3/runs/r2/B/magistrate/CORRECTION_1.md"]),
 ("E-17","C","Condition B final client answers, provenance, gate results",[f"P3/runs/r{n}/B/final/{f}" for n in (1,2,3) for f in ("FINAL_ANSWER.md","PROVENANCE.json","GATE_RESULT.txt")]+["P3/runs/r2/B/final/PROVENANCE_v2.json","P3/runs/r2/B/final/GATE_RESULT_v2.txt","P3/harness/gate.py"]),
 ("E-18","C","Magistrate validation run (r4): packet and determination",["P3/runs/r4/A/ANSWERS.md","P3/runs/r4/A/mcp_log.jsonl","P3/runs/r4/B/magistrate/DETERMINATION.md","P3/runs/r4/B/magistrate/APPROVED_CLAIMS.json","P3/runs/r4/B/magistrate/READ_LOG.md"]),
 ("E-19","C","Clerk's contemporaneous log: every Clerk act, defect, repair, correction (Phase 3; Phases 1–2 logs alongside)",["CLERK/P3_CLERK_LOG.md","CLERK/P2_CLERK_LOG.md","00_matter/CLERK_LOG.md"]),
 ("E-20","C","Resulting-state verification 1 (+ addendum)",["P3/verification/RESULTING_STATE_1.md"]),
 ("E-21","I","Independent audit, stage 1 (blind to answer key)",["P3/audit/AUDIT_STAGE1.md","P3/audit/AUDITOR_HANDBACK_STAGE1.md","P3/audit/READ_LOG.md"]),
 ("E-22","I","Independent audit, stage 2 (key-scored; results matrix; established / not established)",["P3/audit/AUDIT_STAGE2.md","P3/audit/AUDITOR_HANDBACK_STAGE2.md"]),
 ("E-23","D","Unsealed answer keys, generators, perturbation materials (hash-verified against pre-registrations)",sorted(glob.glob(f"{B}/UNSEALED/*/*"))+[f"{B}/UNSEALED/README.md"]),
 ("E-24","I","Institutional-memory test: fresh-clone reconstruction",["P3/memory_test/MEMORY_TEST.md","P3/memory_test/PROMPT.md"]),
 ("E-25","C","Pilot Phase 1 record (tracker; contaminated baseline; clean baselines; challenge correction; Magistrate; Clerk leak)",["00_matter/MATTER.md","02_baseline/README.md","04_challenge/COUNTERARGUMENT.md","05_magistrate/DETERMINATION.md"]),
 ("E-26","C","Pilot Phase 2 record (two clients; views; baselines; governed analysts)",["P2/00_matter/MATTER.md","P2/00_matter/PREREGISTRATION.md","P2/harness/access_layer.py"]),
]
def norm(p): return p if p.startswith(B) else f"{B}/{p}"
def first_commit(p):
    out = subprocess.run(["git","log","--diff-filter=A","--format=%h %cI","--",p],capture_output=True,text=True).stdout.strip().splitlines()
    return out[-1] if out else "UNCOMMITTED"
rows=[]; missing=[]
for eid,kind,desc,paths in R:
    items=[]
    for p in paths:
        p=norm(p)
        if not os.path.exists(p): missing.append((eid,p)); continue
        items.append({"path":p,"sha256":hashlib.sha256(open(p,"rb").read()).hexdigest(),"first_commit":first_commit(p)})
    rows.append({"id":eid,"kind":kind,"description":desc,"items":items})
json.dump({"experiment":"EXP-GED-001","register":rows,"missing":missing},open(f"{B}/AUDIT_FILE/EVIDENCE_REGISTER.json","w"),indent=1)
K={"C":"Contemporaneous evidence","I":"Later interpretation","D":"Design / pre-registration"}
md=["# EXP-GED-001 — Evidence register","","Stable evidence IDs cited by the findings (`FINDINGS.md`) and by the white paper. **Kind:** C = contemporaneous evidence produced during the experiment by the acting component; D = design or pre-registration; I = later interpretation (audit, scoring, findings). Hashes are SHA-256 of the files at the time this register was generated; first commit is the commit that added each file to the branch `claude/exp-governed-enterprise-data`.",""]
for r in rows:
    md+=[f"## {r['id']} · {K[r['kind']]}","",r["description"],"","| File | SHA-256 | First commit |","|---|---|---|"]
    md+=[f"| `{i['path'].replace(B+'/','')}` | `{i['sha256'][:16]}…` | {i['first_commit']} |" for i in r["items"]]
    md.append("")
if missing: md+=["## Missing paths","",*[f"- {e}: `{p}`" for e,p in missing]]
open(f"{B}/AUDIT_FILE/EVIDENCE_REGISTER.md","w").write("\n".join(md)+"\n")
print("rows",len(rows),"files",sum(len(r['items']) for r in rows),"missing",missing)
