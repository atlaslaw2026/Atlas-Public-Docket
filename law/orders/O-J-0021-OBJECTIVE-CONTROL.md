# O-J-0021-OBJECTIVE-CONTROL

**Filing type:** IMPLEMENTING ORDER  
**Implements:** J-0021 (ACTIVE)  
**Date:** 2026-08-25  
**Job:** JOB_GOV_GOAL_DERIVATION  
**Does not rewrite G-60 / G-67 / G-68 / G-69 / G-70.**  
**Does not rewrite UNSEEN_FIRST_PASS letters.**  
**Does not authorize employer send or live trading.**  
**Does not expand J-0020 into mid-draft editing.**

## Commands

1. Canonical schema: `schema/objective.schema.json`.

2. Shared module: `atlas_gov.objective`. Material tasks call `require_material_task` (or inherit via `inherit_routine`) **before** generative execution. Fail closed on `OBJECTIVE_GAP`. Log `OBJECTIVE_LOADED_AT_EXECUTION` from the context actually handed to the executor.

3. Every material governed job SHALL carry `job_objective` on the job JSON: `{id, text, project_id, project_goal_ref, controlling_authority, not}`.

4. TASK_PURPOSE and SUCCESS_CRITERIA MAY be derived from JOB_OBJECTIVE + `task_kind`. Do not require the Human to author them per task.

5. Evaluate results against JOB_OBJECTIVE / TASK_PURPOSE. Detect named proxies in `atlas_gov.objective.PROXIES`. Record evaluations as JSON. Do not treat pack-compliance as purpose-satisfaction.

6. Magistrate uses `atlas_gov.magistrate.inspect_goal_drift` at material supervisory points. Remand competent-wrong-objective work. Do not draft task objectives or edit drafts.

7. Routine HOLD / frozen-spec cycles inherit; no new G-n to restate purpose.

8. Do not append `viewer/docket/INDEX.json` (next_docket_no remains 88). Record J-0021 and this Order on `docket/ATLAS_GOVERNANCE_FILINGS.json`.

9. Implementation evidence: `findings/F-J-0021-IMPLEMENTATION.md`. Required test: `validation/test_j0021_objective.py`.

10. Project 1-2: set JOB_OBJECTIVE on `JOB_PROJECT_1_2_GOVERNED_JOB_SEARCH`. Outreach composition task_kind `COMPOSE_EMPLOYER_LETTER` derives the commercial TASK_PURPOSE stated in J-0021. Do not overwrite Natera first-pass.
