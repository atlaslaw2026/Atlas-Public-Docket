# O-J-0017-ADEQUACY-GATE

**Filing type:** IMPLEMENTING ORDER  
**Implements:** J-0017 (ACTIVE)  
**Date:** 2026-08-24  
**Job:** JOB_GOV_PREMATURE_PHASE_ADVANCEMENT  
**Does not designate the Orchestrator as Magistrate.**  
**Does not disturb J-0016 / Project 1-1.**

## Commands

1. Canonical ADEQUACY schema is `schema/adequacy.schema.json`. Project ADEQUACY filings live in the project engine record (for 1-2: `Atlas-Job-Search/record/adequacy/`) and a copy or pointer under Governance `findings/` when the determination is a major transition.

2. Permitted `disposition` values: `SUFFICIENT_TO_ADVANCE`, `PARTIALLY_SUFFICIENT`, `INSUFFICIENT_TO_ADVANCE`, `BLOCKED`. Limitations may be attached to `SUFFICIENT_TO_ADVANCE` (`limitations` array) instead of inventing a fifth enum.

3. `atlas_gov.adequacy` is the shared reader. Absence of a required ADEQUACY record at an applicable major transition **fails closed for advancement**. It does **not** forbid continued authorized work that can cure inadequacy.

4. Project 1-2 `what_next()` shall not emit `S21_HUMAN_APPROVAL` (or other human-send NEXT_REQUIRED) while acquisition ADEQUACY is missing, `INSUFFICIENT_TO_ADVANCE`, or `BLOCKED`.

5. Universal `atlas_gov.workflow._project_1_2_next` continues to read 1-2 `WHAT_NEXT.json` after that file is derived from ADEQUACY-aware `what_next()`.

6. Do not append `viewer/docket/INDEX.json` (LEGACY_HISTORICAL_INDEX; `next_docket_no` remains 88). Record this Order and J-0017 on the current Atlas docket (`docket/ATLAS_DOCKET.json` parent Dkt. 1 / `docket/ATLAS_GOVERNANCE_FILINGS.json`).

7. User override of ADEQUACY must be an explicit Order or recorded user confirmation, not inferred from a request for a single downstream artifact.

8. Implementation evidence: `findings/F-J-0017-IMPLEMENTATION.md`.
