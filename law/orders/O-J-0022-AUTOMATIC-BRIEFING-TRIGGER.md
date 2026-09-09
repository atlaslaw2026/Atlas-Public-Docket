# O-J-0022-AUTOMATIC-BRIEFING-TRIGGER

**Filing type:** IMPLEMENTING ORDER  
**Implements:** J-0022 (ACTIVE)  
**Date:** 2026-08-29  
**Job:** JOB_GOV_ARGUMENT_COUNTERARGUMENT_ADVOCACY  
**Does not rewrite G-213–G-218 or MAG-GOV-G213-001.**  
**Does not modify J-0018, J-0019, or J-0020 text.**  
**Does not authorize live trading.**  
**Does not implement the 1-9 chooser/DEF repair.**

## Commands

1. Canonical schema: `schema/j0022_self_repair.schema.json`.

2. Shared module: `atlas_gov.j0022_briefing_trigger`. Before implementing a proposed self-repair, call `evaluate_proposed_self_repair`. Fail closed on `GOVERNANCE_SENSITIVE_REPAIR_BLOCKED` and `HUMAN_RESERVED`.

3. If the proposal would materially alter governance execution, institutional authority, routing, NEXT_ACT, room eligibility, or institutional behavior, classify `GOVERNANCE_SENSITIVE_SELF_REPAIR` and automatically require: DEFECT → DIAGNOSIS → AI ARGUMENT → INDEPENDENT AI COUNTERARGUMENT → MAGISTRATE REVIEW → bounded repair only if MAG authorizes using an **existing** disposition → independent verification → resume original Goal.

4. Do **not** auto-open Argument/Counterargument for ordinary defects, research disagreements, uncertainty, investigation, diagnosis, testing, failed approaches, remands, or routine software repairs.

5. Argument and Counterargument on this path must be substantive (evidence-supported case; independent attacks on facts, necessity, scope, authority, consequences, alternatives). Room stampers are not sufficient. Independent Counterargument requires a different `run_session_identity` than the Argument.

6. Magistrate intake for a completed qualifying briefing on this class uses existing `atlas_gov.magistrate.file_review`. No new MAG disposition enum. `suppress_auto_continue` unless MAG ROUTE of already-authorized machine work is the disposition.

7. Human-reserved proposals (new/amended governing law, enlarged authority, live money, acts beyond machine authority) fail closed to Human Judgment. Briefing does not replace that Human act.

8. Verification before marking repair complete: defect corrected; in authorized scope; regressions pass; unrelated governance unchanged. Repair is not Goal completion.

9. Do not append `viewer/docket/INDEX.json` (next_docket_no remains 88). Record J-0022 and this Order on `docket/ATLAS_GOVERNANCE_FILINGS.json`.

10. Implementation evidence: `findings/F-J-0022-IMPLEMENTATION.md`. Required test: `validation/test_j0022_automatic_briefing_trigger.py`.
