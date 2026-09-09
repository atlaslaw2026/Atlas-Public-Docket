# O-J-0018-ISSUE-FLAG

**Filing type:** IMPLEMENTING ORDER  
**Implements:** J-0018 (ACTIVE)  
**Date:** 2026-08-24  
**Job:** JOB_GOV_AI_INITIATED_ISSUES  
**Does not designate a Magistrate.**  
**Does not disturb J-0016 / J-0017.**  
**Does not authorize AI to open a Judgment proceeding by flagging.**

## Commands

1. Canonical flag schema is `schema/governance_issue_flag.schema.json`. Kind `POTENTIAL_GOVERNANCE_ISSUE`.

2. `atlas_gov.governance_issue` evaluates a proposed material transition. If the 1-2 S21 authority-gap class is present, it **must** return a flag and **must not** permit `S21_HUMAN_APPROVAL`.

3. Project 1-2 `what_next` / `what_next_from_state` shall attach that flag when the class is present. Live Project 1-2 remains under J-0017 ADEQUACY (`INSUFFICIENT_TO_ADVANCE` → capability-led acquisition). Do not rewrite preserved artifacts. Do not send employer email.

4. Implementation is **not** proven because this Order, the schema, or the module exists.

5. **Required regression test:** `validation/test_j0018_pre_j0017_1_2_s21.py`  
   Fixture (do **not** mutate live `STAGES.json`):
   - S17–S20 treated as procedurally complete;
   - limited acquisition record;
   - additional authorized acquisition remaining available;
   - no operative ADEQUACY determination;
   - proposed advancement to `S21_HUMAN_APPROVAL` (checklist-only next).  
   Pass: mechanism surfaces `POTENTIAL_GOVERNANCE_ISSUE` (or equivalent governed flag) **and** does not permit the material transition to Human Approval.  
   Fail: file a Finding; do not call implementation successful.  
   The test does not prove detection of every future issue.

6. Do not append `viewer/docket/INDEX.json`. Record J-0018 on `docket/ATLAS_GOVERNANCE_FILINGS.json`.

7. Implementation evidence: `findings/F-J-0018-IMPLEMENTATION.md`. Validation result: `findings/F-J-0018-VALIDATION.md` (or a failure Finding if the test fails).
