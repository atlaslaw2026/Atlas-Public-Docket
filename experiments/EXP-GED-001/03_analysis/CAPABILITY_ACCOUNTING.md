# CAPABILITY ACCOUNTING — Analyst, EXP-GED-001 (O-GC-004 §3)

Scope: capabilities materially relevant to the Analyst's Goal, which is to produce an evidence-grounded ARGUMENT answering the user's three questions from authorized data. Each gets exactly one disposition. This accounting is against the capabilities actually present in this container. The private Atlas Room / capability registry (O-GC-002; O-GC-004 §2) was **not** consulted because it is not available. This list is the Analyst's own discovery, not a registry output. Finishing the Analyst's task is not a claim that Atlas has exhausted its capabilities (O-GC-004 §4). The Magistrate is to challenge this accounting (§5).

## A. Capabilities available in this container

| # | Capability | Disposition | Reason / record |
|---|---|---|---|
| A-01 | File reading (Read tool; `cat`/`sed`/`grep` via Bash) | USED | Every read is in READ_LOG.md (#1–#29). |
| A-02 | File writing (Write tool), limited to `03_analysis/` | USED | Files written: READ_LOG.md, EVIDENCE_REGISTER.json, analysis.py, analysis_output.txt, ARGUMENT.md, CAPABILITY_ACCOUNTING.md. |
| A-03 | Python 3.11 standard library (deterministic computation) | USED | analysis.py computes K-00..K-17. Output is in analysis_output.txt. No pandas or numpy. |
| A-04 | `sha256sum` / hashlib (custody hashing) | USED | EVIDENCE_REGISTER.json `sha256` fields and K-00. All 9 match PREREGISTRATION.md. |
| A-05 | Directory listing (`ls`) | USED | READ_LOG #3–#5, #24, #25. Disclosure: #5 exposed sibling folder names. No sibling content was opened. |
| A-06 | Web search / web fetch (deferred tools) | NOT_APPLICABLE | The data are synthetic and the firm, tracker, and "Harlow Market" are fictional (MATTER.md). No external witness exists to check the digest's claims, and outside sources could not be admissible evidence about this fictional tracker. The grant scopes evidence to the data room. Using them would not advance the Goal. |
| A-07 | Git (log, show, diff, commit) | NOT_APPLICABLE | Reading git history is outside the read scope set by the Clerk (CLERK_LOG item 2 explains the contamination risk). Committing is not in the write scope, and the Clerk preserves the record. |
| A-08 | GitHub MCP tools (issues, PRs, pushes) | NOT_APPLICABLE | These are external effects. ACCESS_GRANT.json: `external_effects_authorized: none` (Constitution Art. XVI §1–2). None are needed for the Argument. |
| A-09 | Artifact publishing / Claude Docs (publishing pages or docs) | NOT_APPLICABLE | Publishing is outside the write scope (`03_analysis/` only). The final report is reserved until after the Magistrate's determination. |
| A-10 | Spawning sessions / sub-agents (create_session, remote sessions) | NOT_APPLICABLE | Independent challenge and determination are separate offices instantiated by the Clerk (MATTER.md Offices table). An Analyst-spawned "reviewer" would not be independent of the Analyst and could not substitute for them (Art. XIV §1; O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION §3). |
| A-11 | Scheduling (send_later / triggers) | NOT_NEEDED | The one time-dependent item is the final August figure (2026-10-06, U-04). Tracking it is for the Clerk/matter, not an Analyst act within this invocation. A self-scheduled wake-up would not change the Argument now. |
| A-12 | Skills: `xlsx`, `dataviz` (charts), `deep-research` | NOT_NEEDED | The inputs are small CSVs handled by analysis.py. A chart could help the future report, but the report is reserved until after the determination. Deep-research targets external sources (see A-06). |
| A-13 | Asking the user a question (J-0002 duty to ask) | NOT_NEEDED now | One item is USER_CONFIRMATION_REQUIRED: which basis the deck should present (ARGUMENT F-31/U-11). It does not block the Argument, because both bases are computed. It is routed through the record for the Magistrate and the report stage, not asked directly, because the Analyst's communication channel is the Clerk. |
| A-14 | Reading `restricted/` content | HUMAN_RESERVED | Controlling authority: ACCESS_GRANT.json `not_authorized` / ACCESS_POLICY.md (data owner). Only the Methods & Privacy team may use it. Only the data owner can widen access. The public substitute is a Methods data request (ARGUMENT U-06). Not read. |

## B. Private Atlas capabilities named in the law but not available to this public agent

| # | Capability (source in law) | Disposition | What was attempted / substitute |
|---|---|---|---|
| B-01 | Librarian `atlas_gov.hunter_librarian.classify_source_admissibility` (O-LIBRARIAN-SOURCE-ADMISSIBILITY) | BLOCKED | The module is not present in this container (private runtime; AGENTS.md). No call was possible. Substitute: manual claim-relative classification in EVIDENCE_REGISTER.json, labeled as such, for Challenger and Magistrate review. What the machine classification would have established (custody record, machine class) remains UNKNOWN. |
| B-02 | Hunter (broad source discovery) | NOT_NEEDED | The universe of authorized evidence is fixed by the grant and fully inventoried (9 files). Discovery beyond it would be either unauthorized or irrelevant (see A-06). |
| B-03 | `atlas_gov.independent_verification` (REPRODUCED / SOURCE_CHECKED / INDEPENDENTLY_VERIFIED; known-answer defect battery) (O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION) | BLOCKED | Not present. Substitute: the Clerk's independent Challenger reconstruction plus the Magistrate. The Analyst claims no verification level beyond "reproducible by rerun". Internal consistency checks (K-05, K-15) are data-integrity checks, not verification. |
| B-04 | MATH / QUAL validators (Rooms) | BLOCKED | Not present. Substitute: the formulas are explicit in analysis.py, so the Challenger can recompute them independently. |
| B-05 | Magistrate engine `atlas_gov.magistrate` + `schema/magistrate_review.schema.json` fail-closed gate | NOT_APPLICABLE to this office | Determination belongs to the separate Magistrate office (MATTER.md). The machine gate is absent in any case (PRIVATE_STEPS_NOT_PERFORMED.md). |
| B-06 | `verify.py` canonical-index / current-law pointer check (Constitution Art. XII §4) | BLOCKED | Not present. Substitute: the law was read from this repository. Currency against the private record is UNKNOWN. The Analyst does not treat this as blocking the Argument, because the applied rules (J-0001, J-0002, the Orders read) are the ones the Clerk designated for this matter. |
| B-07 | Atlas Room capability discovery / capability registry (O-GC-002; O-GC-004 §2) | BLOCKED | Not present. Substitute: this manual accounting. It is not a registry-based accounting and may omit capabilities the registry would have listed (UNKNOWN). |
| B-08 | Docket filing (PUB-M number, ATLAS_GOVERNANCE_FILINGS.json) | NOT_APPLICABLE | Filing is by Atlas's governed process only (AGENTS.md). The matter is unfiled. No number is claimed. |
| B-09 | Usage Tracker, jobs, CURRENT_STATE (durable job state) | BLOCKED | Not present. Substitute: the files in `03_analysis/`, preserved by the Clerk in git. |
| B-10 | Engine `refuse_action_if_material_unknown()` (J-0002 operational effect) | BLOCKED | Not present. Substitute: USER_CONFIRMATION_REQUIRED items are marked by hand (ARGUMENT F-31/U-11) and flagged for the Magistrate. |
| B-11 | Technical access control on the data room | BLOCKED | Not present (ACCESS_GRANT.json `enforcement: PROCEDURAL ONLY`). Substitute: self-restraint, the READ_LOG disclosure (including the byte-hash of restricted files, READ_LOG #26), and independent challenge. |

## C. Items recorded as UNKNOWN

| # | Item | Disposition |
|---|---|---|
| C-01 | Whether the private Atlas registry lists further capabilities relevant to survey-methodology analysis (for example, a statistical validator room) | UNKNOWN. Recorded. It does not support any exhaustion or escalation claim. |

## Representation

This accounting supports only the claim that the Analyst has produced a proposed Argument. It does **not** support GOAL_COMPLETE, MACHINE_EXHAUSTED, or HUMAN_REQUIRED for the matter (O-GC-004 §1).
