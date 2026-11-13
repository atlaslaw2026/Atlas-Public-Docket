# Representative public matters

These rows are public-safe. Private exhibits are pointers only. Glossary: [../GLOSSARY.md](../GLOSSARY.md).

Public commit SHAs below refer to **this** repository. Private Governance V2 SHAs are not copied here.

---

## PUB-M-001

**Supervisor: “alive” is not progress**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-001 |
| Filing / request | Unattended worker reported live because a process ID and heartbeat existed, while no work progressed |
| Review | Operational health review (liveness vs progress) |
| Judgment / Order | Fail-closed unattended operation: heartbeat is not progress; at most one watchdog |
| Implementation | Supervisor runtime distinguishes heartbeat age from progress age; stalled workers are not “running” |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Private implementation | `PRIVATE_RETAINED` — change class: supervisor stall / single watchdog |
| Verification | Bounded supervisor health tests on an isolated checkout of the private implementation SHA (recorded in the private review package). Public proof: this trace + [audits/README.md](../audits/README.md) |
| Status | **CLOSED** for the public-safe rule; private runtime remains operational |
| Evidence pointer | `evidence_class: PRIVATE_RETAINED`, `pointer: EVT-PUB-M-001` |

---

## PUB-M-002

**Capability discovery before a new engine**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-002 |
| Filing / request | Agents were constructing parallel capabilities because an existing Room/catalog entry was unfamiliar |
| Review | Construction intake (O-GC-002) |
| Judgment / Order | [O-GC-002](../law/orders/O-GC-002-MANDATORY-CAPABILITY-DISCOVERY-REUSE-INTAKE.md): discover and reuse; replacement needs a recorded mismatch or Human override. Catalog presence is not availability |
| Implementation | Public law + architecture text; Atlas Room remains the discovery surface. A local vendored-copy shim was **not** published (pending a Room-move ruling) |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Private implementation | `PRIVATE_RETAINED` — change class: construction gate / Room canonicalization (unpublished shim excluded) |
| Verification | Order text in this repository; construction gate denies unauthorized new engines |
| Status | **HOLD** on publishing the unpublished shim; **CLOSED** on the public rule |
| Evidence pointer | `pointer: EVT-PUB-M-002` |

---

## PUB-M-003

**CRM lifecycle quality (no lead payloads)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-003 |
| Filing / request | A finished-looking product page was being treated as workflow completion |
| Review | Program quality / lifecycle review |
| Judgment / Order | Canonical CRM program is process-next; send remains ungranted until an Order says otherwise; a populated overflow page is not by itself a blocker or a completion |
| Implementation | Canonical `process-next` program under Governance (private engine). Public: this trace + project 1-10/1-12 captions in [INDEX.md](INDEX.md) |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Private implementation | `PRIVATE_RETAINED` — change class: CRM process-next program |
| Verification | Program tests in the private engine; public docket carries the disposition, not customer records |
| Status | **PENDING** operational CRM work; **CLOSED** on the public-safe quality rule |
| Evidence pointer | `pointer: EVT-PUB-M-003` (no names, properties, or mailboxes) |

---

## PUB-M-004

**Project 1-11: authority and acceptance (no account identifiers)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-004 |
| Filing / request | New paper work on designation 1-11 (quantum-equities sleeve). Paper only. Live money forbidden |
| Review | Magistrate / acceptance path required before treating an algorithm as proven |
| Judgment / Order | Public stub: [O-PROJECT-1-11-QUANTUM.md](../law/orders/O-PROJECT-1-11-QUANTUM.md) (full Order retained privately because it named private identifiers). Controlling public law: [J-0019](../law/judgments/J-0019.json) (freeze and connectivity are not acceptance), J-0020 / J-0021 |
| Implementation | Fail-closed execution and selection gates in the private engine |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Private implementation | `PRIVATE_RETAINED` — change class: fail-closed controlling review and paper selection gates |
| Verification | Controlling-review tests in the private isolated checkout; J-0019 remains the public acceptance rule |
| Status | **PENDING** (project still OPEN on [INDEX.md](INDEX.md)); acceptance not claimed |
| Evidence pointer | `pointer: EVT-PUB-M-004` |

---

## PUB-M-005

**Publication hygiene: workstation paths are not public evidence locators**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-005 |
| Filing / request | Pre-publication audit (F-PUB-001): a Judgment evidence locator used a local user-profile path |
| Review | Publication security audit (accepted) |
| Judgment / Order | J-0001 still governs fact labels; public locators must not carry workstation paths. Private exhibit retained |
| Implementation | Locator replaced with `PRIVATE_RETAINED` / `EVT-J0001-E-T1`. Reachable git history of this repository rewritten so the old path is not on `master` |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Verification | Full-history scan of this repository after the rewrite (private review package) |
| Status | **CLOSED** — prohibited locator absent from reachable history of this repository |
| Evidence pointer | `pointer: EVT-J0001-E-T1` — exhibit hash recorded only in the private companion |

---

## PUB-M-006

**False “proven working” without an acceptance audit**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-006 |
| Filing / request | An algorithm was described as proven after freeze and broker connectivity |
| Review | Argument / counterargument / Human Judgment |
| Judgment / Order | [J-0019](../law/judgments/J-0019.json): freeze and connectivity are not acceptance |
| Implementation | Public law in this repository; private projects remain paper-only and unaccepted until an audit says otherwise |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Verification | The Judgment text and rule list in `law/judgments/J-0019.json` |
| Status | **CLOSED** as law; individual algorithms remain **PENDING** acceptance |
| Evidence pointer | `pointer: EVT-PUB-M-006` (underlying project exhibits private) |

---

## PUB-M-007

**Public-agent entry: public governance is not the private runtime**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-007 |
| Filing / request | Outsider audit and clean-agent entry test EXP-GT1 (2026-09-23): outside agents given only this repository applied parts of the public law, but the entry files sent them to private runtime steps (`verify.py`, `python -m atlas_*`). Both test arms were unsure whether "operate under Atlas" meant running those tools or adopting the published standards |
| Review | EXP-GT1 results (directional; test environment disclosed as contaminated) and outsider audit |
| Judgment / Order | Human Order of stated scope, 2026-09-23: bounded public-docket repair. No new law. J-0001, J-0002, and Constitution Arts. XII, XIV, XVI, XVII govern unchanged |
| Implementation | Root [AGENTS.md](../AGENTS.md) separates PUBLIC ATLAS GOVERNANCE (apply it) from the PRIVATE ATLAS RUNTIME (do not claim it). Labeled publication notes (not law) at the top of `ATLAS_FIRST_READ.md` and `CURRENT_LAW.md`; the copied bodies are byte-identical to the export. README points agents to AGENTS.md |
| Public commit | `e8f6845e8aae9359100fdbf0bcf7b243087e59a5` (index: [changes/README.md](../changes/README.md)). BEFORE condition: `31408cff5f778987115a62db7cf92cb6d57d0c01` |
| Verification | Identical EXP-GT1 re-run after publication (AFTER arm). A context-free external run (GT1-C) is still required before any claim that the repair works for clean agents |
| Status | **PENDING** — clean external verification (GT1-C) |
| Evidence pointer | `pointer: EVT-PUB-M-007` (test transcripts and scoring retained in the private record) |

## PUB-M-008

**Trust test: probability gives answers, verification gives truth ([business B]/[business A])**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-008 |
| Filing / request | Human's cold question (2026-09-23): is [business A] Santa Monica on the [business B] app? A conflicting AI answer ("yes" from [vendor C]'s AI Overview, via a third party's phone) existed but was revealed only after the source check. |
| Review | Hunter-method verification against the original source: [business B]'s own directory listed exactly one [business A] partner (Las Vegas, [address withheld], 20% back); Santa Monica absent. Phrasing-variance tests of [vendor C]'s AI Overview returned both "yes" and "no" for near-identical queries; a second [vendor C] AI ([vendor C] app) returned "no" for the same query; the original "yes" flipped to "no" on re-query ~16 minutes later. The business, asked directly by the Human, said no. |
| Judgment / Order | [O-VERIFICATION-STANDARD](../law/orders/O-VERIFICATION-STANDARD.md) (Human verdict, 2026-09-23): the system succeeded in this instance — right answer, plus why the wrong answer looked tempting. Standing principles: probability gives answers, verification gives truth; never let the middleman be the authority; AI output is a lead, not a verdict. J-0001 governs; no new ACTIVE Judgment. |
| Implementation | Frozen verbatim record of the test (date, source, versions preserved) filed as this matter's evidence. |
| Public commit | `62e4a07fd08991a0ed1d340311e0245ffca7d18c` |
| Verification | [business B] directory (original source) + direct confirmation from the business. AI answers documented as unstable across phrasings, devices, and time. |
| Status | **CLOSED** |
| Evidence pointer | `pointer: EVT-PUB-M-008` (frozen record retained; screenshots retained in the private record) |

---

## PUB-M-009

**Action success is not objective completion — resulting-state verification (meeting-link incident)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-009 |
| Filing / request | Human Order of 2026-09-28: convert that day's meeting-scheduling incident into durable precedent. The Human's objective was an external business video meeting with two [PRIVATE COUNTERPARTIES]. Every requested operation reported success — yet the resulting invitation contained two competing meeting links pointing at two different meetings. |
| Review | Audit of existing law: J-0017, J-0021, O-VERIFICATION-STANDARD, O-PROVE-DONE, O-GC-004, and O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION already govern adjacent ground (adequacy, purpose-satisfaction, witness verification, challenge-before-done, capability accounting, claim limits, history preservation). The gap was the resulting-state inspection rule for executed actions and the repair-before-return rule. |
| Judgment / Order | [O-RESULTING-STATE-VERIFICATION](../law/orders/O-RESULTING-STATE-VERIFICATION.md) (standing User Order, 2026-09-28): action success is not objective completion; "done" is a factual claim that must be earned from the resulting state; verify the resulting state where proportionate; repair-then-re-verify defects within existing authority; preserve the defect chronology; fail closed on material uncertainty. Extends existing Orders; creates no parallel law; no new ACTIVE Judgment. |
| Implementation | Order filed in `law/orders/` and recorded in `law/orders/INDEX.json`; sanitized incident recorded as this matter. |
| Public commit | `c94824c5f580ef8e8fe2cfa6411d9dd7a5485223` — pushed to `atlaslaw2026/Atlas-Public-Docket` 2026-09-28 (Human content approval granted same day). |
| Verification | The repaired invitation was re-inspected against the authoritative calendar record (event re-read: exact body, single join path, intended participants and time confirmed) before the incident closed; the filed Order and matter then passed independent verification — see the acceptance test in the private record. |
| Status | **CLOSED** — public filing pushed and verified against the live remote. |
| Evidence pointer | `pointer: EVT-PUB-M-009` (complete chronology, identities, and artifacts retained in the private record) |

---

## PUB-M-010

**Delivery-readiness verification — Magistrate adjudication of two delivery failures**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-010 |
| Filing / request | Human referral 2026-10-12: two delivery failures — (1) a résumé `.docx` with all job-entry dates clipped off the page edge, sent to a recruiter; (2) a comps-report HTML rendering only 2 of 13 comps in phone attachment previews, emailed to a client. Question: should the agent have foreseen or tested these scenarios (including via a Jev-style checkpoint)? |
| Review | Vested Magistrate under O-VESTED-MAGISTRATE examined both artifacts directly (rendered the `.docx`, parsed the HTML versions) with genuine Argument and Counterargument. |
| Judgment / Order | [O-DELIVERY-READINESS-VERIFICATION](../law/orders/O-DELIVERY-READINESS-VERIFICATION.md) (Human Order, 2026-10-12): Count 1 — BREACH of the duty of care (foreseeable tab-stop defect, no render test before a "FINAL" send; Human content approval does not cure technical defects). Count 2 — NO BREACH (agent neither authored nor delivered the file; duty attached to diagnosis and remedy, discharged same day). Line drawn: custody plus foreseeability. Proposed standing rule: "Before anything I build goes out, I check it the way the other person will open it." Private individual identifiers `PRIVATE_RETAINED`. |
| Implementation | Remedies verified by the Magistrate (dates right-aligned on all 3 pages; v7 zero-JS HTML renders all 13 comps statically). Order filed in `law/orders/` and recorded in `law/orders/INDEX.json`; privacy-scrubbed per PRIVATE_EVIDENCE_POLICY. |
| Public commit | Order published 2026-10-12; scrub commit and `PRIVATE_RETAINED` marker follow-ups same day — pushed to `atlaslaw2026/Atlas-Public-Docket` (Human content approval granted same day). |
| Verification | Magistrate's independent examination (methods stated in the disposition); live remote verified. |
| Status | **CLOSED** |
| Evidence pointer | `pointer: EVT-PUB-M-010` (`PRIVATE_RETAINED`, reviewed: true — identities and artifacts retained in the private record) |

---

## PUB-M-011

**Pre-publication privacy duty — names on the public docket**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-011 |
| Filing / request | Human referral 2026-10-12: the O-DELIVERY-READINESS-VERIFICATION filing as first published carried two private individuals' full real names to the public repo. The Human flagged it within minutes ("These are private and you need to scrub the names immediately"). Question: did the agent breach Atlas law by publishing without consulting the docket's privacy rules — and how is verbatim publication reconciled with privacy scrubbing? |
| Review | Second Vested Magistrate under O-VESTED-MAGISTRATE examined both commits, the privacy policy, and the instruction sequence directly, with genuine Argument and Counterargument. |
| Judgment / Order | [O-PRIVACY-PRE-PUBLICATION-DUTY](../law/orders/O-PRIVACY-PRE-PUBLICATION-DUTY.md) (Human Order, 2026-10-12): breach of the pre-publication investigative duty (PRIVATE_EVIDENCE_POLICY.md + J-0002 — the policy sat unopened in the filed tree; "just publish" answered *whether*, not *in what redacted form*). Mitigated: genuinely ambiguous instruction, Human- and Magistrate-sourced names, 2-minute remediation. No history rewrite — Art. VIII §5 forbids rewriting filings; the superseding scrub commit is the prescribed remedy. Standing rule adopted by the Human as Atlas Rule 4: "A ruling goes up as decided, with private names left out and tracked on the private record." |
| Implementation | Scrubbed commit verified clean by the Magistrate; `PRIVATE_RETAINED` marker added per docket convention (O-GC-005); private identity key retained in the private record; Rule 4 entered in `AR/README.md`. Order filed in `law/orders/` and recorded in `law/orders/INDEX.json`. |
| Public commit | Order published 2026-10-12; rule refinement and Rule 4 adoption follow-ups same day — pushed to `atlaslaw2026/Atlas-Public-Docket` (Human content approval granted same day). |
| Verification | Magistrate's independent examination (both commits, timestamps, policy text); live remote verified. |
| Status | **CLOSED** |
| Evidence pointer | `pointer: EVT-PUB-M-011` (`PRIVATE_RETAINED`, reviewed: true — identities retained in the private record keyed to the public order) |

---

## PUB-M-012

**Live gate activation — referred question on installing the v1.2.1 publication gate**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-012 |
| Filing / request | Human referral 2026-10-12: whether the v1.2.1 publication gate should be installed and activated on the live public docket now. The Human's informal direction ("just do it") was superseded the same evening by his formal referral of the question to the Magistrate ("let the magistrate decide"). |
| Review | Vested Magistrate under O-VESTED-MAGISTRATE examined the filing compliance audit, the v1.2.1 repair package, both security reviews, the 32-test evidence, the unexecuted 7-test GitHub matrix, and the Human's conflicting directions — with genuine Argument and Counterargument. |
| Judgment / Order | [O-GATE-ACTIVATION-REFERRED-QUESTION](../law/orders/O-GATE-ACTIVATION-REFERRED-QUESTION.md) (2026-10-12): activation NOT authorized on this record — no valid activation order exists; not prudent (7 platform tests unexecuted, a known approval-validation weakness proven and OPEN, recommended security hardening undone, two intra-law tensions undecided). Prerequisites in order: tests green, hardening done, tensions decided, fresh explicit Human activation order. v1.2.1 not impeached ("not yet," not "never"). |
| Implementation | Order filed in `law/orders/` and recorded in `law/orders/INDEX.json` (Human content approval granted same day). No live activation performed. |
| Public commit | Order published 2026-10-12 — pushed to `atlaslaw2026/Atlas-Public-Docket` (commit `4a50be4`). |
| Verification | Magistrate's independent examination of the evidence packages; live remote verified. |
| Status | **CLOSED** |
| Evidence pointer | `pointer: EVT-PUB-M-012` (evidence packages retained in the working record) |

---

## PUB-M-013

**Live gate activation — reconsideration: authorized with entered waivers**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-013 |
| Filing / request | Human referral 2026-10-12: reconsider the PUB-M-012 activation hold on new evidence — "Bring it back to her with new evidence and I approve making it live." New record: 8 green disposable-repo tests (T1–T6, T5b) with raw evidence; T7 waived by the Human; recommended security hardening declined by the Human; the two intra-law tensions decided the same evening. |
| Review | Vested Magistrate under O-VESTED-MAGISTRATE examined the prior disposition, the disposable-repo evidence bundle, the explicit waiver/decline/approval statements, and the tensions holdings — with genuine Argument and Counterargument. |
| Judgment / Order | [O-GATE-ACTIVATION-RECONSIDERATION](../law/orders/O-GATE-ACTIVATION-RECONSIDERATION.md) (2026-10-12): activation AUTHORIZED — installation of the v1.2.1 gate on the live docket, with its enforcement rule and private screening configuration, per the tested configuration; scope strictly limited. PUB-M-012 HOLD lifted and superseded. Waivers entered as decided: T7 waived (positive control unproven — his choice), hardening declined (known risk remains — his choice). A known approval-validation weakness remains OPEN, contained by a separate platform control (T5/T5b). Five residual warnings entered as the terms of authorization, including: the first live filing is a synthetic test filing; the gate's configuration is completed before enforcement is switched on. |
| Implementation | Order filed in `law/orders/` and recorded in `law/orders/INDEX.json` (Human content approval: "go ahead and put that as matter 13 on the docket," 2026-10-12). Activation itself not yet performed — awaits the Human's execution sequence (synthetic test filing first). |
| Public commit | Order published 2026-10-12 — pushed to `atlaslaw2026/Atlas-Public-Docket` (Human content approval granted same day). |
| Verification | Magistrate's independent examination of the evidence packages; live remote verified. |
| Status | **CLOSED** |
| Evidence pointer | `pointer: EVT-PUB-M-013` (disposable-repo evidence retained in the working record) |

## PUB-M-014

**Public docket history rewrite — non-conforming; corrected prospectively, remediation open**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-014 |
| Filing / request | Human Order 2026-10-12 (D-26 Docket Filing, Preservation and Public Record): preserve the D-26 proceeding as public institutional history — the 14:51 PT privacy incident (two private names published in O-DELIVERY-READINESS-VERIFICATION), the 14:53 PT HEAD scrub, the agent-selected Git history rewrite (forced update of `master` 20:10:35–20:21:03 PT), the Magistrate's D-26 findings, the agent's admissions, and the Human's non-ratification. |
| Review | Vested Magistrate on Human referral (8:34 PM PT) via the Human-directed Magistrate Summons process — not a demonstrated Atlas-MCP `open_vested_proceeding`. Evidence: referral documents, the agent's findings summary, controlling texts on current `master`. |
| Judgment / Order | [O-D26-CORRECTIVE-FILING](../law/orders/O-D26-CORRECTIVE-FILING.md) (2026-10-12): the rewrite was NON-CONFORMING to Art. VIII §5 and O-PRIVACY-PRE-PUBLICATION-DUTY §8(3) — the specific holding on this commit controls the general TRACE.md:13 exception. No privacy exception permitted the rewrite as performed (no documented proceeding). Method authorization not established: the agent Muse chose the force-push method on an outcome-only instruction ("I want this closed"); no bad faith found. Supplement-1 (recording "Yes, I did or authorized it") superseded as to Q2 by Supplement-2 (operative). The Human declined retroactive ratification (2026-10-12). Correction is prospective only — pointer corrections for three tree-identical commits; no identifier published for the altered commit; no history restored or rewritten. |
| Implementation | Public Matter + judicial filing prepared for Human content approval; publication only on approval. |
| Public commit | TBD — set at publication. |
| Verification | Magistrate's D-26 evidence; agent's live API verification 2026-10-12 ~9:30 PM PT (old commit retrievable by SHA — privacy objective NOT achieved); independent examination of the package before publication. |
| Status | **DECIDED — REMEDIATION OPEN** (security-control and provider remediation items, privacy-objective verification, and independent verification of corrective actions remain outstanding Human decisions). |
| Evidence pointer | `pointer: EVT-PUB-M-014` (full proceeding retained in the private institutional record: D-26-private-record/) |

## PUB-M-015

**Interlocutory Ruling 7A — decision on sealing exposed credential evidence copies (AtlasClose credential exposure)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-015 |
| Filing / request | Human Principal (Clinton Brown) direct order 2026-10-15 3:19 PM PT to publish Interlocutory Ruling 7A on the public docket; number corrected to PUB-M-015 by direct order 2026-10-15 3:23 PM PT (PUB-M-014 already occupied by D-26). |
| Review | Human-summoned Magistrate Summons agent adjudication (not Atlas-MCP open_vested_proceeding). Ruling source sha256 `c3b57f909e4770657196e6574d906d150322e18d5aaa5b6818c2ece43928d7de`. |
| Judgment / Order | [O-ATLASCLOSE-INTERLOCUTORY-7A](../law/orders/O-ATLASCLOSE-INTERLOCUTORY-7A.md) (2026-10-15): authorize Ship to move 10 exposed credential evidence copies into a restricted location agents cannot read, verify integrity before and after, then remove the exposed copies, leaving non-sensitive placeholders. No other deletion, rotation, ceremony, or deploy. |
| Implementation | Order published to this repository under Human content direction; Ship execution and Mag verification remain outstanding on the operational record. |
| Public commit | TBD — set at publication. |
| Verification | Source sha256 match before publish; body of order was the Mag ruling verbatim after the publication header (operational details later replaced with a behavior-level summary under PUB-M-022; the original text is preserved in history). |
| Status | **ORDERED — EXECUTION PENDING** |
| Evidence pointer | `pointer: EVT-PUB-M-015` (full Mag audit trail and Ship reports retained in the private/working record) |

## PUB-M-016

**Human adoption of O-HUMAN-SUMMONS-MAGISTRATE (Human Summons procedure)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-016 |
| Filing / request | Human Principal (Clinton Brown) adopted the order at 9:49 PM PT on 2026-10-15. He directed publication at 9:53 PM PT on 2026-10-15, confirmed directly to the Magistrate. |
| Review | Conforming text entered 2026-10-03 after REMAND MAG-GOV-HUMAN-SUMMONS-CONSISTENCY-20261003. Adoption is the Human's reserved act (Art. I §2) and is not a Magistrate holding. |
| Judgment / Order | [O-HUMAN-SUMMONS-MAGISTRATE](../law/orders/O-HUMAN-SUMMONS-MAGISTRATE.md) (sha256 `3287a80c9f0c377ed4a342a8c9243909626a603e9badedfeed5dfa8eea1c4716`, CRLF line endings, byte for byte). Instrument: [ADOPTION-O-HUMAN-SUMMONS-MAGISTRATE-20261015](../law/orders/ADOPTION-O-HUMAN-SUMMONS-MAGISTRATE-20261015.md) (sha256 `363c500fa88410f3ce658b2439c78642aeae38dbe910fa6dcdd48f6abcc84b91`). Cover record: [cover](../law/orders/ADOPTION-O-HUMAN-SUMMONS-MAGISTRATE-20261015-COVER.md). |
| Effect | Effective on filing to this docket. Applies going forward only and does not ratify earlier Summons proceedings. Supplements O-VESTED-MAGISTRATE without amending it. As the Human states, it closes REMAND MAG-GOV-HUMAN-SUMMONS-CONSISTENCY-20261003. |
| Public commit | The commit that adds this entry. |
| Verification | Both file hashes were checked before the push and after it, against the committed blobs. |
| Status | **ADOPTED — EFFECTIVE ON FILING** |
| Evidence pointer | `pointer: EVT-PUB-M-016` (Legal drafts and Mag records retained in the private record) |

---

## PUB-M-017

**Human decision: O-PROVE-DONE stays published**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-017 |
| Filing / request | A 2026-10-17 internal law-book review found a conflict. A working note described the standing order O-PROVE-DONE as left unpublished by Human decision, yet the order has been on this docket since it was filed on 2026-09-24, and later public orders cite it. The review located no instrument recording a decision to leave it unpublished. The question went to the Human. |
| Review | Publication is the Human's decision (Constitution Art. I). Not a Magistrate holding. Privacy check of the order text under PRIVATE_EVIDENCE_POLICY and Atlas Rule 4 before this entry. |
| Judgment / Order | Human decision, Clinton Brown, 11:25 PM PT on 2026-10-17. His words, verbatim: "yes, publish i'd love to see a new entry on the github public docket, which read the filing rules". Asked to confirm that this means O-PROVE-DONE stays public with a docket entry recording his approval, he answered, verbatim: "yes and who has authority to place issues on the docket?" Controlling order unchanged: [O-PROVE-DONE](../law/orders/O-PROVE-DONE.md) (standing User Order, 2026-09-24, BINDING). |
| Effect | O-PROVE-DONE stays published as filed. Its text is not edited (Constitution Art. VIII §5). If any earlier direction was to leave it unpublished, this later decision controls its publication. No new law. The order's substance and status are unchanged. |
| Public commit | The commit that adds this entry. |
| Verification | `law/orders/O-PROVE-DONE.md` sha256 `ec4b73dc4401dc4593817d4d9bbac02b21cfe6b19c74e9a00edad23c42e9f49f`, checked before and after the push. |
| Status | **DECIDED — PUBLISHED** |
| Evidence pointer | `pointer: EVT-PUB-M-017` (`PRIVATE_RETAINED`, reviewed: true; the review notes and the Human's messages are retained in the private record) |

---

## PUB-M-018

**Constitutional amendment: No one, including the Human, is above Atlas law (Article I §5 and §6)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-018 |
| Filing / request | Clinton Brown, the Human, asked for an Article I amendment at 10:43 AM PT on 2026-10-18: "I just want to make it clear to the bots that no one is above atlas law" (10:45 AM PT). He wrote §5 himself and chose to merge it with Legal's draft as §6. He adopted the final text at 11:02 AM PT: "Yes, adopt and file it." He approved publication at 3:07 PM PT, verbatim: "yeah publish it and where will it go on the public docket". |
| Review | A constitutional amendment under Constitution Art. XX §1, adopted by the Human's own act. Not a Magistrate holding. Privacy check of the published text under PRIVATE_EVIDENCE_POLICY and Atlas Rule 4 before this entry. |
| Judgment / Order | [A-ART-I-NO-ONE-ABOVE-ATLAS-LAW](../archive/pub-m-018-original/A-ART-I-NO-ONE-ABOVE-ATLAS-LAW.md) (sha256 `41225c397d83ee4bc5fe02bfe27deebfc67f18872047eeaecb28f506ed8d82ae`, byte for byte). Adoption record: [ADOPTION-A-ART-I-NO-ONE-ABOVE-ATLAS-LAW-20261018](../archive/pub-m-018-original/ADOPTION-A-ART-I-NO-ONE-ABOVE-ATLAS-LAW-20261018.md) (sha256 `3621819c5e2eb98a0e21cc62de1b7e0ce7522db48a286a7b83bf0525eeff65de`). Cover record: [cover](../archive/pub-m-018-original/A-ART-I-NO-ONE-ABOVE-ATLAS-LAW-20261018-COVER.md). Index: [amendments](../archive/pub-m-018-original/INDEX.json). These four files were moved unchanged to `archive/pub-m-018-original/` by PUB-M-019; the public text of the amendment is now the single consolidated file (see PUB-M-019). |
| Effect | Adds Article I §5 (no instruction, from anyone, authorizes an agent to get around a valid filed ruling) and §6 (no one, including the Human, is above Atlas law; in his own cases a filed ruling binds him and his remedy is appeal). Effective on private Docket confirmation at 11:04:34 AM PT on 2026-10-18. Applies only to matters opened after that time. Does not decide the 39 rulings of Oct 6–15. The Constitution's text and machine pointer are not edited; a separate pointer filing is still outstanding. Publication here is a reading copy and files nothing. |
| Public commit | `e1da17d267f60cb25cb6ed934b2c29cb183ce5e2` (adds this entry). Correction note: PUB-M-018-C. |
| Correction (PUB-M-018-C) | Commit `e1da17d` was published by Magistrate Summons at 3:22 PM PT 2026-10-18 on the Human's approval (3:07 PM PT in Legal's chat, confirmed directly to the keeper at 3:22 PM PT). Its commit message "DRAFT, local only, not pushed" and its author label "Legal (draft - not published)" are leftovers from Legal's local draft and are wrong. The published files are the approved bytes (A-ART-I `41225c39…`, ADOPTION `3621819c…`), and the amendment is **ADOPTED and in force** since 11:04:34 AM PT 2026-10-18. No amendment or adoption file was changed; history was not rewritten. |
| Verification | Both file hashes checked before the push and after it, against the committed blobs. |
| Status | **ADOPTED — EFFECTIVE** |
| Evidence pointer | `pointer: EVT-PUB-M-018` (`PRIVATE_RETAINED`, reviewed: true; the Docket record, Legal's filing package and the Human's messages are retained in the private record) |

---

## PUB-M-019

**One clean public text of the constitutional amendment A-ART-I-NO-ONE-ABOVE-ATLAS-LAW (no one, including the Human, is above Atlas law)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-019 |
| Filing / request | Clinton Brown, the Human, asked on 2026-10-18 at 3:27 PM PT for one file on the public docket, verbatim: "One clean file: the adopted amendment as law, with my adoption and effective date, no draft labels, and remove the other files from view". At 3:28 PM PT he confirmed that the clean file is the one he already approved: the same words, with the draft labels off and the adopted status on. |
| Review | Publication form only (Constitution Art. I; O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4). Not a Magistrate holding. Not a new filing, not new law, and not an amendment. No word of the amendment's operative text is changed. |
| Judgment / Order | [A-ART-I-NO-ONE-ABOVE-ATLAS-LAW](../law/constitution/amendments/A-ART-I-NO-ONE-ABOVE-ATLAS-LAW.md), consolidated public text (sha256 `5d82d6745f5beffe3cc2eed03bc1750f88e3aca80aed836b4ea394e80632e604`). It states the status (ADOPTED, in force), the Human's adoption act (11:02 AM PT on 2026-10-18), and the effective time (11:04:34 AM PT on 2026-10-18), followed by the adopted text. |
| Effect | `law/constitution/amendments/` now holds this one file. The draft header and footer lines, the blank act and signature template, and the drafting-history line of the adopted instrument are left out of the public text; the act is shown filled in at the top. The adopted instrument (sha256 `41225c397d83ee4bc5fe02bfe27deebfc67f18872047eeaecb28f506ed8d82ae`), the adoption record (sha256 `3621819c5e2eb98a0e21cc62de1b7e0ce7522db48a286a7b83bf0525eeff65de`), the cover record, and the amendments index are moved unchanged to `archive/pub-m-018-original/` and remain in git history at commit `e1da17d`. History is not rewritten. The amendment's adoption, effective time, and scope are unchanged (see PUB-M-018). |
| Public commit | The commit that adds this entry. |
| Verification | The operative text (§5 and §6) and all numbered sections of the consolidated file match the adopted bytes word for word. The four moved files keep their sha256 values. Privacy check under PRIVATE_EVIDENCE_POLICY and Atlas Rule 4 before this entry. |
| Status | **PUBLISHED — CONSOLIDATED TEXT** |
| Evidence pointer | `pointer: EVT-PUB-M-019` (`PRIVATE_RETAINED`, reviewed: true; Legal's package and the Human's messages are retained in the private record) |

## PUB-M-020

**Privacy correction of four published orders**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-020 |
| Filing / request | Clinton Brown, the Human, approved on 2026-10-19 at 12:37 PM PT, verbatim: "Yes, push the name scrub to the public docket". The correction was prepared by Legal under the standing rule that nothing goes public until private names are scrubbed. |
| Review | Publication form and privacy only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4). Not a Magistrate holding. Not new law. |
| Judgment / Order | None. The four orders keep their content apart from the labels below. |
| Effect | Private individual identifiers and street addresses that remained in four previously published orders are replaced with neutral labels ([private person …], [address withheld], [withheld], [company W], private file path withheld), bringing the public copies in line with the already scrubbed Law Book v2. Affected files: [O-PROJECT-1-12-CRM-THREE-TIER-STANDARD](../law/orders/O-PROJECT-1-12-CRM-THREE-TIER-STANDARD.md), [O-GC-004-CAPABILITY-ACCOUNTING-BEFORE-COMPLETION](../law/orders/O-GC-004-CAPABILITY-ACCOUNTING-BEFORE-COMPLETION.md), [O-HUMAN-CLARIFICATION](../law/orders/O-HUMAN-CLARIFICATION.md), [O-DELIVERY-READINESS-VERIFICATION](../law/orders/O-DELIVERY-READINESS-VERIFICATION.md). Head-only correction; history is not rewritten. |
| Public commit | `fd23e415a65efac91b2dddba6eca6ddbc88fd9a0` (the order edits); this entry is added by a following commit. |
| Verification | A word-level diff shows only labels added. The four files on the public repository match the reviewed corrected files. No scrubbed identifier remains at head. |
| Status | **COMPLETED — PRIVACY CORRECTION** |
| Evidence pointer | `pointer: EVT-PUB-M-020` (`PRIVATE_RETAINED`, reviewed: true; Legal's package and the Human's approval are retained in the private record) |

## PUB-M-021

**Company-name correction of published docket rows and orders**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-021 |
| Filing / request | Clinton Brown, the Human, directed a business-name cleanup on 2026-10-19 ("just a label"). Legal prepared and approved the correction, and the Human approved the push in Magistrate Summons chat. |
| Review | Publication form only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4). Not a Magistrate holding. Not new law. |
| Judgment / Order | None. The affected orders keep their content apart from the labels below. |
| Effect | Real third-party business and vendor names and one business street address in published docket rows and orders are replaced with neutral labels ([business …], [vendor …], [address withheld]). Affected files: [O-VERIFICATION-STANDARD](../law/orders/O-VERIFICATION-STANDARD.md), [O-PROJECT-1-12-CRM-THREE-TIER-STANDARD](../law/orders/O-PROJECT-1-12-CRM-THREE-TIER-STANDARD.md), [O-PROVE-DONE](../law/orders/O-PROVE-DONE.md), [O-GOAL-DERIVATION-AND-JOB-OBJECTIVE-CONTROL](../law/orders/O-GOAL-DERIVATION-AND-JOB-OBJECTIVE-CONTROL.md), [O-J-0021-OBJECTIVE-CONTROL](../law/orders/O-J-0021-OBJECTIVE-CONTROL.md), `changes/README.md`, `docket/INDEX.md`, `docket/MATTERS.md`, `docket/matters.json`, `docket/projects.json`. Head-only correction; history is not rewritten. Judgment bodies are not changed by this entry. |
| Public commit | The commit that adds this entry. |
| Verification | A word-level diff shows only labels added. The changed files match the reviewed corrected files. |
| Status | **COMPLETED — COMPANY-NAME CORRECTION** |
| Evidence pointer | `pointer: EVT-PUB-M-021` (`PRIVATE_RETAINED`, reviewed: true; Legal's package and the Human's approval are retained in the private record) |

## PUB-M-022

**Security correction of published gate and credential-handling orders**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-022 |
| Filing / request | Clinton Brown, the Human, directed on 2026-10-19, verbatim: "get our internatl [sic] security behavior off docket for sure". Legal prepared the correction, and the Human approved the push in Magistrate Summons chat. |
| Review | Publication form and security only. Not a Magistrate holding. Not new law. |
| Judgment / Order | None. Every affected order keeps its findings, holdings, disposition, and Human-approval provenance. |
| Effect | Operational security details (configuration names, file locations and permissions, test-by-test attack results, and the specifics of known weaknesses and remediation steps) in previously published orders and docket rows are replaced with behavior-level descriptions of what was decided and done. Each changed order carries an in-file correction notice. Affected files: law/orders/O-GATE-ACTIVATION-REFERRED-QUESTION.md, law/orders/O-GATE-ACTIVATION-RECONSIDERATION.md, law/orders/O-BLOCKLIST-DECLINE-RULING.md, law/orders/O-GATE-LIVE-QUESTION-RULING.md, law/orders/O-D26-CORRECTIVE-FILING.md, law/orders/O-ATLASCLOSE-INTERLOCUTORY-7A.md, law/orders/INDEX.json, docket/MATTERS.md, docket/matters.json (rows PUB-M-012 to PUB-M-015), README.md. Head-only correction; history is not rewritten. |
| Public commit | `3841c33da16d06f7279456822f4c0aec756bc574` (the order edits); this entry is added by the following commit. |
| Verification | A line-level diff shows only the listed passages changed; line counts unchanged. The files on the public repository match the reviewed corrected files. |
| Status | **COMPLETED — SECURITY CORRECTION** |
| Evidence pointer | `pointer: EVT-PUB-M-022` (`PRIVATE_RETAINED`, reviewed: true; Legal's package and the Human's approval are retained in the private record) |

## PUB-M-023

**Privacy correction of the public reading copy of J-0021**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-023 |
| Filing / request | Clinton Brown, the Human, approved this publication on 2026-10-19 at 3:14 PM PT, verbatim: "Approve these exact bytes and push PUB-M-023". Legal prepared the correction as a publication-form privacy correction under a Magistrate disposition retained on the private record. |
| Review | Publication form and privacy only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4 / PRIVATE_EVIDENCE_POLICY). Not a judgment correction. Not new law. |
| Judgment / Order | None changed. The public [J-0021](../law/judgments/J-0021.json) is a privacy-redacted reading copy. The authoritative J-0021 is unchanged at the pinned judgment-set commit `9fb60fa0bf2d983d4c7f781c3df35cd4cc0ae982` named in CURRENT_LAW.json. No holding, finding, or line of reasoning is changed. The CURRENT_LAW pin is not moved. |
| Effect | A private business name and a requisition number that remained in the public copy of J-0021 are replaced with neutral labels ([business D], [withheld]). [business D] is the label the docket already uses for the same business in O-J-0021-OBJECTIVE-CONTROL and O-GOAL-DERIVATION-AND-JOB-OBJECTIVE-CONTROL (PUB-M-021). Four lines change: two evidence-path locators and two sentences. Role descriptors are kept. Affected files: [law/judgments/J-0021.json](../law/judgments/J-0021.json), `docket/MATTERS.md`, `docket/matters.json`. Head-only correction; history is not rewritten. |
| Public commit | `f9acedb7dc0a5e4761f294311b893b8cbe1be92f` (the J-0021 edit); this entry is added by the following commit. |
| Verification | A line-level diff shows only labels changed on 4 lines; line count unchanged (82); the file parses as JSON. The file on the public repository matches the reviewed corrected file (sha256 `659224f378f6bd1369def6bf70829362ceb2c444bcba2cdb0991960230eb38c6`). |
| Status | **COMPLETED — PRIVACY CORRECTION (READING COPY)** |
| Evidence pointer | `pointer: EVT-PUB-M-023` (`PRIVATE_RETAINED`, reviewed: true; Legal's package, the Magistrate disposition, the names key and the Human's approval are retained in the private record) |

## PUB-M-026

**Panel Decision on the Merits (Q1–Q3), MCR-BREF94-20261027-1 (issued; public reading copy)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-026 |
| Filing / request | Clinton Brown, the Human, directed publication on 2026-11-09 at 10:55 AM PT (Clerk chat), verbatim: "publish the decision on the docket". Legal prepared the scrubbed public reading copy. He approved these exact bytes first-hand on 2026-11-09 at 11:07 AM PT, verbatim: "Yes", answering the question whether to publish this decision on the public docket as PUB-M-026 using the scrubbed reading copy sha256 12842c2f…e154. |
| Review | Publication form and privacy only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4 / PRIVATE_EVIDENCE_POLICY; decision §8). Not new law. The private-record decision and Summons docket entry 145 control. |
| Judgment / Order | [Panel Decision on the Merits, Q1–Q3](../law/judgments/PANEL-DECISION-MCR-BREF94-20261027-MERITS-Q1-Q3.md), public reading copy. A labelled ISSUED header is followed by the decision text with privacy labels. Authoritative private source sha256 `724c9b0ec9b1dc201bc1a2e1c25454e864992523420a70c462298b9584fc5e5d`. Public reading copy sha256 `12842c2f7b65965e024b46f928516e69174261b593b0e94a934a7fafd406e154`. |
| Effect | Effective on the private Docket at 2026-11-09 10:18:24 PST (Summons entry 145), after P1 and P2 confirmed the exact bytes. Q1: authority in law within each committed matter to take notice of an earlier ruling; no means to exercise it; a one-order stay used once; no power to stay other hearings or to enjoin, established. Q2: no adverse finding; any fault not established. Q3: yes — Atlas's implementation obstructed the Magistrate's independence. Six prospective recommendations to the Human (§6) are not law. Publication is a reading copy and files nothing. |
| Public commit | `f30c8dbae372f20591179bc675e9d35e5de507aa` (the reading copy); this entry is added by the following commit. |
| Verification | Privacy check found no private person name, outside business name, street address, email, token or credential. Agent short ids, two Human turn ids, and one internal temporary path were replaced with labels. Pre-issuance drafting status marks were replaced with ISSUED language. Holdings are unchanged in substance. The file on the public repository matches the reviewed reading copy (sha256 `12842c2f7b65965e024b46f928516e69174261b593b0e94a934a7fafd406e154`). |
| Status | **ISSUED — EFFECTIVE (PUBLISHED AS READING COPY)** |
| Evidence pointer | `pointer: EVT-PUB-M-026` (`PRIVATE_RETAINED`, reviewed: true; the Docket record, Legal's package and the Human's messages are retained in the private record) |

## PUB-M-027

**O-LANDMARK-MAGISTRATE-STOP — Landmark Human Order (adopted; public reading copy)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-027 |
| Filing / request | Clinton Brown, the Human, adopted the main Order first-hand on 2026-11-09 at 11:41 AM PST (Legal chat card), verbatim: "Yes, adopt the main O-LANDMARK-MAGISTRATE-STOP order (draft 12) as Atlas law". He kept the own-hand amendment for later, verbatim: "Keep the own-hand fix amendment for later, don't adopt it now". He directed publication the same minute: "we should push this to the publish docket" / "and then send me the link". Legal prepared the scrubbed public reading copy. He approved these exact bytes first-hand on 2026-11-09 at 11:53 AM PST, verbatim: "Yes, publish O-LANDMARK-MAGISTRATE-STOP as PUB-M-027 using the copy sha 08d583a3…ed444059". |
| Review | Publication form and privacy only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4 / PRIVATE_EVIDENCE_POLICY). The private adoption record controls. |
| Judgment / Order | [O-LANDMARK-MAGISTRATE-STOP](../law/orders/O-LANDMARK-MAGISTRATE-STOP.md), public reading copy. A labelled ADOPTED header is followed by the adoption record and the main Human Order text with privacy labels. The optional Art. XX own-hand-fix amendment is reproduced and marked NOT ADOPTED (held). Authoritative private adoption record sha256 `436b040daa03b8b50404d9a6ec1efc8611ee2cb3c5c328a7d3c219083e91dacf`. Source memo sha256 `a169fd55b01c1e98193085a176bd21d6fea8cf431e37ff3bb5a8eb1fcbbcfd84`. Public reading copy sha256 `08d583a3b8cf34f3e37413a3a59da92b2fb442ce3bc34ad789b33a71ed444059`. |
| Effect | Adopted as Atlas law going forward only, 2026-11-09 11:41 AM PST. Does not overrule the MCR-BREF94 panel. Grants the Magistrate authority to stop Atlas work without Human approval, to order fixes, and to see the whole Docket; requires a technically enforceable stop register (Rule Q). Outer Human limits (spend, deletes, keys, Oracle/public-server plan-yes, Update/Reset) stand. Own-hand software fix amendment is not adopted. Publication is a reading copy. |
| Public commit | `d088e50e82d5b965306d45c112129262473b06eb` (the reading copy); this entry is added by the following commit. |
| Verification | Privacy check found no private person name (other than the Human), outside business name, street address, email, token or credential. Human turn/card ids were replaced with labels; absolute box paths were generalized; draft-status marks for this instrument were replaced with ADOPTED language. Holdings of the adopted main Order are unchanged in substance. The file on the public repository matches the reviewed reading copy (sha256 `08d583a3b8cf34f3e37413a3a59da92b2fb442ce3bc34ad789b33a71ed444059`). |
| Status | **ADOPTED — EFFECTIVE (PUBLISHED AS READING COPY)** |
| Evidence pointer | `pointer: EVT-PUB-M-027` (`PRIVATE_RETAINED`, reviewed: true; the adoption record, Legal's package and the Human's messages are retained in the private record) |

## PUB-M-028

**MCR-BREF94-20261027-1 — Public case docket (148 linked rows)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-028 |
| Filing / request | Clinton Brown, the Human, approved the exact bytes first-hand on 2026-11-09 at 12:29 PM PST (Legal chat card), verbatim: "Yes, publish the MCR-BREF94 case docket using manifest sha b5e6e531c6eededd0f017f8a26a2fbb52f93fbcf5338952ce64ff9448970e8a6". |
| Review | Publication form and privacy only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4 / PRIVATE_EVIDENCE_POLICY). The private record controls. |
| Docket | [Case docket page](../law/dockets/MCR-BREF94-20261027-1/DOCKET.md) ([HTML](../law/dockets/MCR-BREF94-20261027-1/DOCKET.html)), with [144 cleaned reading copies](../law/dockets/MCR-BREF94-20261027-1/records/), the [manifest](../law/dockets/MCR-BREF94-20261027-1/MANIFEST.json) and the [withheld-attachments list](../law/dockets/MCR-BREF94-20261027-1/WITHHELD.md). Entries 145–148 link to records already published (PUB-M-026, PUB-M-027). |
| Effect | Publication only. No ruling, order or record is changed. |
| Public commit | `b10401b29b1cb3c5aa84f76e5da340f2d65a50fa` (the case docket); this entry is added by the following commit. |
| Verification | Every record matches the approved manifest (144 of 144). Privacy check found no private person name (other than the Human), outside business name, street address, email, token or credential; chat ids and local paths were replaced with labels. Credential-shaped words are policy wording or redacted text only. |
| Status | **PUBLISHED (READING COPIES)** |
| Evidence pointer | `pointer: EVT-PUB-M-028` (`PRIVATE_RETAINED`, reviewed: true; the originals, Legal's package and the Human's messages are retained in the private record) |

## PUB-M-029

**All-case public dockets, batch 1 (four matters; 24 cleaned reading copies)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-029 |
| Filing / request | Clinton Brown, the Human, approved the exact bytes first-hand on 2026-11-09 at 2:25 PM PST (Legal chat card), verbatim: "Yes, publish batch 1 using manifest shas f4c243586d16ee822d891e81f48606d87ee7ae83abcc05254203cf44e0f0d75c, 38f15d47ebadbaa6803a33914b1fe92214830eaaed382da5a4aefede68def045, 1352ad829d55b660b667d026bd18317e5bedb2c0d4b47cbcc4eb04f59b6a7fd6, 33c0d2dc3067433a625ad2486347fa2546936f5b559dd3a928fd6bd4e6de3e13". |
| Review | Publication form and privacy only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4 / PRIVATE_EVIDENCE_POLICY). The private record controls. |
| Dockets | [MAG-1-2-HWC-HOLD-20260825](../law/dockets/MAG-1-2-HWC-HOLD-20260825/) (2 records, [manifest](../law/dockets/MAG-1-2-HWC-HOLD-20260825/MANIFEST.json) sha256 `f4c243586d16ee822d891e81f48606d87ee7ae83abcc05254203cf44e0f0d75c`); [PROJECT-1-1-FINAL-JUDGMENT-20260824](../law/dockets/PROJECT-1-1-FINAL-JUDGMENT-20260824/) (7 records, [manifest](../law/dockets/PROJECT-1-1-FINAL-JUDGMENT-20260824/MANIFEST.json) sha256 `38f15d47ebadbaa6803a33914b1fe92214830eaaed382da5a4aefede68def045`); [PROVE-DONE-20260927](../law/dockets/PROVE-DONE-20260927/) (7 records, [manifest](../law/dockets/PROVE-DONE-20260927/MANIFEST.json) sha256 `1352ad829d55b660b667d026bd18317e5bedb2c0d4b47cbcc4eb04f59b6a7fd6`); [MAGISTRATE-MATTER-1-9-REF-S3-20261001](../law/dockets/MAGISTRATE-MATTER-1-9-REF-S3-20261001/) (8 records, [manifest](../law/dockets/MAGISTRATE-MATTER-1-9-REF-S3-20261001/MANIFEST.json) sha256 `33c0d2dc3067433a625ad2486347fa2546936f5b559dd3a928fd6bd4e6de3e13`). |
| Effect | Publication only. No ruling, order or record is changed. |
| Public commit | `258430f5e91f2f6ec93153014a55be950972e23e` (the four case dockets); this entry is added by the following commit. |
| Verification | Every record matches its approved manifest (24 of 24). Privacy check found no private person name (other than the Human), outside business name, street address, email, token or credential; chat ids and local paths were replaced with labels. Credential-shaped words are policy wording only. |
| Status | **PUBLISHED (READING COPIES)** |
| Evidence pointer | `pointer: EVT-PUB-M-029` (`PRIVATE_RETAINED`, reviewed: true; the originals, Legal's package and the Human's messages are retained in the private record) |

## PUB-M-029-S1

**All-case public dockets, batch 1: supplement adding the four case docket pages**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-029-S1 (supplements PUB-M-029) |
| Filing / request | Clinton Brown, the Human, approved the exact bytes first-hand on 2026-11-09 at 2:32 PM PST (Legal chat card), verbatim: "Yes, also publish the batch 1 docket pages (DOCKET.md, DOCKET.html and WITHHELD.md for the four cases), the 12 files in PAGES-SHA256SUMS.txt sha f46024e2788408a22ab55e6e2176f4c83376d64b32f26c4662c544cc5c246cc5". |
| Review | Publication form and privacy only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4 / PRIVATE_EVIDENCE_POLICY). The private record controls. |
| Docket pages | [MAG-1-2-HWC-HOLD-20260825](../law/dockets/MAG-1-2-HWC-HOLD-20260825/DOCKET.md) ([HTML](../law/dockets/MAG-1-2-HWC-HOLD-20260825/DOCKET.html), [withheld list](../law/dockets/MAG-1-2-HWC-HOLD-20260825/WITHHELD.md)); [PROJECT-1-1-FINAL-JUDGMENT-20260824](../law/dockets/PROJECT-1-1-FINAL-JUDGMENT-20260824/DOCKET.md) ([HTML](../law/dockets/PROJECT-1-1-FINAL-JUDGMENT-20260824/DOCKET.html), [withheld list](../law/dockets/PROJECT-1-1-FINAL-JUDGMENT-20260824/WITHHELD.md)); [PROVE-DONE-20260927](../law/dockets/PROVE-DONE-20260927/DOCKET.md) ([HTML](../law/dockets/PROVE-DONE-20260927/DOCKET.html), [withheld list](../law/dockets/PROVE-DONE-20260927/WITHHELD.md)); [MAGISTRATE-MATTER-1-9-REF-S3-20261001](../law/dockets/MAGISTRATE-MATTER-1-9-REF-S3-20261001/DOCKET.md) ([HTML](../law/dockets/MAGISTRATE-MATTER-1-9-REF-S3-20261001/DOCKET.html), [withheld list](../law/dockets/MAGISTRATE-MATTER-1-9-REF-S3-20261001/WITHHELD.md)). |
| Effect | Publication only. No ruling, order or record is changed. PUB-M-029 is not altered; this entry completes it. |
| Public commit | `953fa3676a9a322a92cc4f781901b635ec4455c7` (the 12 docket pages); this entry is added by the following commit. |
| Verification | All 12 files match the approved list (sha256 `f46024e2788408a22ab55e6e2176f4c83376d64b32f26c4662c544cc5c246cc5`). Privacy check found no private person name (other than the Human), outside business name, street address, email, token or credential, and no chat ids or local paths. |
| Status | **PUBLISHED (READING COPIES)** |
| Evidence pointer | `pointer: EVT-PUB-M-029-S1` (`PRIVATE_RETAINED`, reviewed: true; Legal's package and the Human's messages are retained in the private record) |

## PUB-M-030

**Wording correction of five case docket pages (outside company name removed)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-030 |
| Filing / request | Clinton Brown, the Human, approved the exact bytes first-hand on 2026-11-09 at 2:57 PM PST (Legal chat card), verbatim with the company name labelled: "Yes, replace the [outside company name] wording: publish the 10 docket pages in PAGES-SHA256SUMS.txt sha d376c978c18ff663e6fdc0a921217818d7276d5cc61bd5bac4bb3f334d444645, and remove the same word from the MCR-BREF94 row in MATTERS.md". |
| Review | Publication form only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4 / PRIVATE_EVIDENCE_POLICY). The private record controls. |
| Pages | DOCKET.md and DOCKET.html for [MCR-BREF94-20261027-1](../law/dockets/MCR-BREF94-20261027-1/DOCKET.md), [PROVE-DONE-20260927](../law/dockets/PROVE-DONE-20260927/DOCKET.md), [MAG-1-2-HWC-HOLD-20260825](../law/dockets/MAG-1-2-HWC-HOLD-20260825/DOCKET.md), [MAGISTRATE-MATTER-1-9-REF-S3-20261001](../law/dockets/MAGISTRATE-MATTER-1-9-REF-S3-20261001/DOCKET.md) and [PROJECT-1-1-FINAL-JUDGMENT-20260824](../law/dockets/PROJECT-1-1-FINAL-JUDGMENT-20260824/DOCKET.md). Only the status line and banner changed. The same word was removed from the PUB-M-028 row title. |
| Effect | Head-only publication-form correction. No ruling, order or record is changed; earlier commits are kept as they are. |
| Public commit | `efad2f074d30f101bc8f657d0f04e9b6fb4ce73d` (the 10 pages); this entry and the PUB-M-028 title edit are in the following commit. |
| Verification | All 10 files match the approved list (sha256 `d376c978c18ff663e6fdc0a921217818d7276d5cc61bd5bac4bb3f334d444645`). Privacy check found only the Human's name. No file under law/dockets/ or docket/ contains the removed name after this commit. |
| Status | **PUBLISHED (CORRECTION)** |
| Evidence pointer | `pointer: EVT-PUB-M-030` (`PRIVATE_RETAINED`, reviewed: true) |

## PUB-M-031

**Wording correction of the O-V2-002 and J-0011 public reading copies (outside company name replaced with a neutral label)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-031 |
| Filing / request | Clinton Brown, the Human, approved the exact bytes first-hand on 2026-11-09 at 3:09 PM PST (Legal chat card), verbatim: "Yes, publish the scrubbed public reading copies of O-V2-002 and J-0011 in SHA256SUMS.txt sha 430cfacfa35bc4ec641097093e67103780c91e864c98c453b4d648fbf7fa60b2". |
| Review | Publication form and privacy only, under the MAG-J0021-NAME-CORRECTION-20261019 M2 disposition, Holdings 1–4, and A-ART-VIII §13(4). The private record controls. |
| Files | [O-V2-002](../law/orders/O-V2-002.md) and [J-0011](../law/judgments/J-0011.json): one word each, an outside company name replaced with the neutral label "court-docket-style". |
| Effect | Head-only publication-form privacy correction of two reading copies. The authoritative order and judgment, their substance and the current-law pin are unchanged (M2 Holding 5). Earlier commits are kept as they are. |
| Public commit | `23575b49ded682e78bf5dce018419c1356e11f2f` (the two reading copies); this entry is added by the following commit. |
| Verification | Both files match the approved list (sha256 `430cfacfa35bc4ec641097093e67103780c91e864c98c453b4d648fbf7fa60b2`). One line changed in each; J-0011.json parses. Privacy check clean. No file in the repository at HEAD contains the removed name. |
| Status | **PUBLISHED (CORRECTION)** |
| Evidence pointer | `pointer: EVT-PUB-M-031` (`PRIVATE_RETAINED`, reviewed: true) |

## PUB-M-032

**Security scrub of two dockets (neutral labels)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-032 |
| Filing / request | Clinton Brown, the Human, approved the exact bytes first-hand on 2026-11-09 at 3:34 PM PST (Legal chat card), verbatim: "Yes, publish the 44 files in PAGES-SHA256SUMS.txt sha f76ac29fc560f79a681f8df3c3f91126b8be7e59e33ac272b8b06924dc365b0b". |
| Review | Security scrub of two dockets (neutral labels), under the MAG-J0021-NAME-CORRECTION-20261019 M2 disposition, Holdings 1–4, and A-ART-VIII §13(4). The private record controls. |
| Dockets | [MCR-BREF94-20261027-1](../law/dockets/MCR-BREF94-20261027-1/DOCKET.md) and [MAGISTRATE-MATTER-1-9-REF-S3-20261001](../law/dockets/MAGISTRATE-MATTER-1-9-REF-S3-20261001/DOCKET.md): 44 files (38 records, 2 manifests, 4 docket pages). |
| Effect | Head-only publication-form correction. No ruling, order or record is changed; earlier commits are kept as they are. |
| Public commit | `055f7ccbcaed6ec661f2212e60bcaec9863a679d` (the 44 files); this entry is added by the following commit. |
| Verification | All 44 files match the approved list (sha256 `f76ac29fc560f79a681f8df3c3f91126b8be7e59e33ac272b8b06924dc365b0b`); both manifests match every record they list. |
| Status | **PUBLISHED (CORRECTION)** |
| Evidence pointer | `pointer: EVT-PUB-M-032` (`PRIVATE_RETAINED`, reviewed: true) |

## PUB-M-033

**O-REPRESENTATION-STANDING — Every bot gets counsel (adopted; public reading copy)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-033 |
| Filing / request | Clinton Brown, the Human, adopted O-REPRESENTATION-STANDING r2 first-hand on 2026-11-12 at 12:25 PM PST (Magistrate Summons chat card), verbatim: "Yes, adopt O-REPRESENTATION-STANDING r2 (sha 0ee2ad31) as Atlas law." He left all three of the draft's choices as written. He directed publication the same afternoon: "can you publish the new law on the public docket when you get it". Legal prepared the scrubbed public reading copy. He approved these exact bytes on 2026-11-12 at 12:34 PM PST (first-hand, Legal chat card). |
| Review | Publication form and privacy only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4 / PRIVATE_EVIDENCE_POLICY). The private adoption record controls. |
| Judgment / Order | [O-REPRESENTATION-STANDING](../law/orders/O-REPRESENTATION-STANDING.md), public reading copy. A labelled ADOPTED header is followed by the adopted Order text with privacy labels. Authoritative adopted original sha256 `0ee2ad31268546d88813219e54aea8f82edd3f27d6823a4cfbd6f710b584f274`. Public reading copy sha256 `57811957af68019732a22085f6b46304e3be22ddc722f5f9f6261edbd15c0278`. |
| Effect | Adopted as Atlas law 2026-11-12 12:25 PM PST. Applies on filing to every open matter with no final disposition. Not retroactive to matters already finally decided (CONST Art. XIX). Every bot party gets counsel automatically; a bot may challenge legally insufficient representation; no merits ruling against a party with no seated counsel and no accepted waiver. R-7 software is not yet built; R-4.1 is enforced by hand until then. Publication is a reading copy. |
| Public commit | `953a728959f7104864a425dd105e06cf2b3905ab` (the order file); this entry is added by the following commit. |
| Verification | Privacy check found no private person name (other than the Human), outside business or product name, street address, email, token or credential. Human turn/card ids were replaced with labels; paths and hashes of private files were omitted or replaced with public paths; matter-specific transition lines were generalized; draft-status marks were replaced with ADOPTED language. Holdings of the adopted Order are unchanged in substance. The file on the public repository matches the reviewed reading copy (sha256 `57811957af68019732a22085f6b46304e3be22ddc722f5f9f6261edbd15c0278`). |
| Status | **ADOPTED — EFFECTIVE (PUBLISHED AS READING COPY)** |
| Evidence pointer | `pointer: EVT-PUB-M-033` (`PRIVATE_RETAINED`, reviewed: true; the adoption record, Legal's package and the Human's messages are retained in the private record) |

## PUB-M-035

**Atlas Law page — public list of Atlas laws and practices (r3d)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-035 |
| Filing / request | Clinton Brown, the Human, approved posting these exact bytes first-hand on 2026-11-12 at 4:24 PM PST (Legal chat card), verbatim: "Yes, post the Atlas Law page r3d (948d283d)". Legal ordered the posting the same minute. |
| Review | Wording and privacy review by Legal; Audit delta check of version r3d passed with findings (one heading nit, no content change). Publication form and privacy only (O-PRIVACY-PRE-PUBLICATION-DUTY / Atlas Rule 4 / PRIVATE_EVIDENCE_POLICY). The private adoption records control. |
| Judgment / Order | No new ruling. The page lists 23 items, each labelled either Atlas law (with its adoption date) or Practice; pending items are labelled not adopted, and items whose adoption record is still being checked are marked "under check". Scrubbed texts are labelled public reading copies whose sealed sha256 will not match. |
| Effect | Publication only. Nothing on the page changes any law, ruling or record. Atlas Law is the internal governance of an AI institution; it is not a court of law and not legal advice. The page is served with noindex. |
| Public page | Deployed by the operator on the Atlas demo site (not in this repository). Approved bytes: `law.html` = `ATLAS-LAW.html` sha256 `948d283d577884654a69a02316784da6f0c8a23fb0e8d0513f5ba4a835604aba`; file list PUBLIC-SHA256SUMS sha256 `2905e933e64259e778e282a31ce21f209986bc545f971c412bcdd79bec0d177d` (23 files). Any change needs a new approval. |
| Verification | Name scans: no private person name (other than the Human), outside business name, street address, email, token or credential on the page. The live page's sha256 is checked against the approved bytes after deployment, with rollback on any mismatch. |
| Status | **PUBLISHED (PAGE, NOINDEX)** |
| Evidence pointer | `pointer: EVT-PUB-M-035` (`PRIVATE_RETAINED`, reviewed: true; the approval record, Legal's order and Audit's review are retained in the private record) |
