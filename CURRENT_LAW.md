# CURRENT LAW

**Machine pointer:** `CURRENT_LAW.json`  
**Template for new Judgments:** `law/JUDGMENT_TEMPLATE.md`  
**This file is the single human answer to: what governs Atlas right now?**

**Cutover recorded 2026-08-23** in `D:\atlas\ATLAS_RECORD\CURRENT_LAW.md`. Universal current law is this private repository at GitHub `main`. At the opening of JOB-J0012-USAGE-ACCOUNTING that SHA was `a11a6c8870164ee7d3e8a3808264289c2c2f5eff` (then matching ATLAS_RECORD / HEAD). **Pointer correction 2026-08-29 (`JOB_GOV_ARGUMENT_COUNTERARGUMENT_ADVOCACY`):** `CURRENT_LAW.json` `current_sha` is `9fb60fa0bf2d983d4c7f781c3df35cd4cc0ae982`, the judgment-set commit that contains ACTIVE J-0022. SHA `e20a5cd8116aa32910a61a5dca700fb895fd9507` remains an ancestor and is not competing law. Disk `law/judgments` and `git show {current_sha}:law/judgments` must resolve the same ACTIVE ids (fail closed). A later HEAD may be a pointer-hygiene descendant; it is not a second law.

**Entrypoint (O-GC-003 then J-0010 / `STARTUP.md`):** a fresh agent completing GitHub entry verifies the live canonical index with the existing `verify.py` first. If that verification fails: UNKNOWN — do not infer the active project from this file. After VERIFIED, every new agent finds ATLAS_RECORD, reads `CURRENT_LAW.md`, resolves this V2 repository, **loads the operative Constitution** (`law/constitution/CURRENT_OPERATIVE_CONSTITUTION.json`), loads Judgments and standing gates, binds a job, then loads the project's derived CURRENT_STATE (`docket/derived/CURRENT_STATE/`). Ordinary current **operational memory** is that derived packet. CURRENT_STATE is not law (Constitution Art. X). `current_sha` remains the judgment-set commit and does not contain the Constitution (C-1). If the pointer cannot be resolved: UNKNOWN or USER_CONFIRMATION_REQUIRED — no silent fallback to historical Governance.

**Human endpoint (J-0011 / J-0013):** `viewer/` is the offline Flask lens. The **active public Human docket** is the canonical DOCKET identity `docket/CURRENT_DOCKET.json` (command `python -m atlas_gov docket`). Do not treat `viewer/site` as that host. `docket/CURRENT_PUBLICATION.json` is an alias, not a second live host. AI docket at `/` (`viewer/docket/INDEX.json`); My docket at `/human` is rebuilt from that INDEX (same Dkt. numbers, captions not law). HUMAN DOCKET at `/human-docket` is a derived reading copy. The Viewer is a lens over this record, not a second pointer or second repository of law. **CURRENT_ATLAS_DOCKET** Dkt. 1 is the Goal (`docket/ATLAS_DOCKET.json`). **LEGACY_GOVERNANCE_INDEX** Dkt. 1 remains O-V2-001 (`viewer/docket/INDEX.json`, not rewritten). Unqualified Dkt. 1 means the Goal (Constitution Art. VIII). INDEX citations must still be verified against INDEX before KNOWN (J-0013). J-0014 remains PROPOSED. Run `python viewer/run.py` (loopback).

## Authority stack (one hierarchy)

**Operative from 2026-08-27T14:50:00-07:00** (`O-ATLAS-CONSTITUTION-RATIFICATION`; Constitution Schedule A). Lower yields to higher. CURRENT_STATE and NEXT_ACT are not in this list.

1. **Atlas Constitution** — `law/constitution/ATLAS_CONSTITUTION.md` (pointer `law/constitution/CURRENT_OPERATIVE_CONSTITUTION.json`).
2. **Human constitutional acts and other explicit superior Human authority** — ratification, amendment, reserved Judgment, Code strike, Human Orders of stated scope. Cannot silently amend the Constitution.
3. **Operative Goal** — purpose and objective selection only. Does not by itself repeal or create procedural authority (`AMENDED_DKT_1`; Art. II).
4. **Atlas Code / general statutes** — Code when distilled; until then incorporated standing user gates in `law/incorporated/STANDING_USER_GATES.md` (historical statute SHA256 prefix `4f3a5cade6964649`). Consult Code/gates before reconstructing raw precedent when they clearly resolve a general issue.
5. **Uncodified ACTIVE Judgments, general implementing Orders, and controlling judicial precedent** — `law/judgments/` status ACTIVE; `law/orders/`. Apply where Code/gates are silent, ambiguous, remanded, or under review.
6. **Project-specific authority** — 1-x Orders and jobs. A project Human Order is level 2 for its stated scope.

**Pre-ratification stack (historical, not deleted):** User Orders → ACTIVE Judgments → standing gates → schemas. That list governed until the Constitution’s effective moment. Jobs answer `governing_law_at_time` from their job record.

**Schemas** in `schema/` remain how work is recorded. They are not a grant of power.

There is **no second active JUDGMENT.md**. Historical files remain historical:

- `D:\atlas\Atlas-Governance\statute\JUDGMENT.md` — superseded as universal current law after cutover; retained as historical statute + source of incorporated gates.
- `D:\atlas\Atlas_Governance_Docket\JUDGMENT.md` — never current GitHub law (Task 3); remains cabinet text.
- Watcher overlay Clerk/Magistrate — **WATCHER-ONLY** (`watcher/README.md`).

## Active Judgments (V2)

| ID | Title |
|---|---|
| J-0001 | Facts before Judgment; epistemic statuses |
| J-0002 | Material unknown — duty to ask |
| J-0003 | Heightened protection for operational systems |
| J-0004 | Regression / “what changed?” |
| J-0005 | User operational knowledge is evidence |
| J-0006 | Universal Atlas job lifecycle |
| J-0007 | Watcher governance is not universal Atlas law |
| J-0008 | Activity/usage integration; never invent MEASURED |
| J-0009 | Law Viewer incident as governance case (no Law Viewer code change) |
| J-0010 | Universal Governance entrypoint — ATLAS_RECORD first |
| J-0011 | Governance Viewer is a lens, not a source of law |
| J-0012 | Universal AI Usage Accounting and Job Attribution |
| J-0013 | Docket is Dkt. 1..N with no gaps and matching timestamps; citations must be verified; redocket authorized if the sequence breaks |
| J-0015 | Capital-at-risk rule — TARGET_STRATEGIC_CASH = 0% for the next AI challenger; AI-ALG2-V1 remains frozen |
| J-0016 | Project 1-1 Final Judgment — substantive design phase closed; forward experiment continues |
| J-0017 | Narrow major-phase substantive adequacy gate — procedurally complete is not substantively adequate to advance |
| J-0018 | Duty to identify and flag potential Governance issues — AI must not silently cross an authority gap |
| J-0019 | Algorithm Acceptance Audit — freeze and connectivity are not acceptance |
| J-0020 | Atlas Magistrate — continuing three-dimensional Goal custodian |
| J-0021 | Goal derivation and objective control — purpose must control material AI execution |
| J-0022 | Automatic briefing trigger — material governance-sensitive self-repair |

## Constitution (operative)

Ratified Draft 2 is controlling constitutional law. Proposed drafting record remains in `law/constitution/proposed/`. J-0019 is unchanged. Legacy INDEX Dkt. 1 remains O-V2-001. No operative Code book is created by ratification. Article IV delegated codification may proceed later, subject to Article V. Conformity conflicts: `findings/F-CONSTITUTION-CONFORMITY-CONFLICTS.md`.

## What this law does not do

- J-0022 requires automatic Argument / independent Counterargument / Magistrate review only before a proposed software repair that would materially alter governance execution, institutional authority, routing, NEXT_ACT, room eligibility, or institutional behavior. It does **not** adopt a universal A/CA trigger for ordinary defects, research disagreements, uncertainty, investigation, diagnosis, testing, failed approaches, remands, or routine software repairs. It does **not** add Magistrate dispositions, rewrite MAG-1-9, implement the 1-9 chooser/DEF repair, authorize live trading, or treat authorized repair as Goal completion or as authority to rewrite governing law.
- J-0021 requires typed JOB_OBJECTIVE / TASK_PURPOSE / SUCCESS_CRITERIA on material execution. It does **not** authorize the Magistrate to draft every task, approve every output, or edit mid-draft. It does **not** mint a new G-n for each HOLD cycle. It does **not** rewrite UNSEEN_FIRST_PASS letters. Prompt decoration is not the implementation. G-60 and G-67–G-70 remain the preserved briefing record.
- O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION requires source-grounded independent reconstruction before VERIFIED / VALIDATED / CORRECT / PASS. Reproduction, hash match, and AI agreement are not independent verification. It does **not** add an ACTIVE Judgment (pinned SHA unchanged). It does **not** accept a strategy, authorize trading, permit purchases, change frozen research thresholds, or erase historical findings. Saving the Order is not compliance.
- O-MATERIAL-UNCERTAINTY-CANONICAL-CONSULT requires a central consult of canonical authority on material uncertainty, feeding NEXT_ACT. It does **not** add an ACTIVE Judgment (pinned SHA unchanged). It does **not** make Human Docket/Viewer authority. It does **not** treat MAX_OUTER or tool/search limits as governance exhaustion. It does **not** replace the Magistrate or compute_next_act.
- J-0020 activates the Atlas Magistrate as a continuing Goal-custodian and cross-layer coherence function (`JOB_GOV_ORCHESTRATOR_MAGISTRATE` RUNNING). It does **not** rename Orchestrator classes, collapse specialist rooms, or treat the Watcher overlay Magistrate as universal law (J-0007). G-5–G-8 remain preserved historical briefing.
- J-0018 duty to flag does **not** authorize AI to open a Judgment proceeding, file Argument/Counterargument, or make law.
- J-0019: candidate selection, freeze, broker connectivity, and a HOLD/invocation are not algorithm acceptance. ACCEPTED / OPERATIVE / PAPER_READY / PRODUCTION_READY / PROVEN_WORKING (or equivalent) require an Algorithm Acceptance Audit. P13-ALG-V1 is preserved and not accepted as a proven forward-operating algorithm.
- O-SHARED-AI-REASSESSMENT-DELIBERATION (G-198) makes shared AI reassessment/deliberation available to authorized rooms as advisory intelligence. It does **not** expand room authority, choose NEXT_ACT, amend the Goal/Constitution/Judgments/MAG, complete general-deliberation construction by itself, or authorize trading, communications, or other external execution.
- Does not authorize employer/external email.
- Does not authorize Alpaca **live** orders.
- Does not authorize general GitHub broker-order permission, and does not lift the V1 harvest `GITHUB_ACTIONS` kill-switch.
- Narrow user Order `O-ALG1-V1-PAPER-FORWARD-GITHUB` (2026-08-24) permits GitHub Actions to submit Alpaca **paper** orders solely for `JOB_ALG1_V1_PAPER_FORWARD` / `ALG1-V1-PAPER-FORWARD` at `https://paper-api.alpaca.markets`. It does not imply GITHUB → ALPACA LIVE.
- Does not authorize deletion of historical Governance.
- Does not authorize modifying Law Viewer, Hunter, or trading algorithms as part of Governance work.

## Supersession

See `migration/LEDGER.md`. After cutover, agents answer “what law applied to an old job?” from the job record’s `governing_law` pointer, not by rewriting history.
