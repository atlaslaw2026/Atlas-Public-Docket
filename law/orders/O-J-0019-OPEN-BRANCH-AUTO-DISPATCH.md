# O-J-0019-OPEN-BRANCH-AUTO-DISPATCH

**Filing type:** USER ORDER  
**Date:** 2026-08-27  
**Implements / supplements:** J-0019, J-0020, O-J-0019-DISTINCT-RESEARCH-BRANCH-LOOP, O-J-0020-AUTOMATIC-CONTINUATION  
**Does not authorize live money.**  
**Does not special-case any project id.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**

## Defect

A frozen OPEN strategy-research branch could exist in canonical state without Governance deriving the responsible room or dispatching that work. Continuation depended on a later Human prompt or an already-running continue call. Process exit left OPEN branches idle. Gap fingerprints omitted `branch_id`, so distinct OPEN branches could share a cycle and look exhausted.

## Rule

When a research branch is created or remains OPEN with unresolved required work, Atlas shall derive the responsible capability from the frozen branch design (Hunter for the remanded research question; Math/Qualitative for pending classified items; Strategy Design after validated handoff) and automatically dispatch that work. Persist running versus required versus failed state on the branch record. In-process running work must not be duplicated. A failed or process-interrupted dispatch leaves the branch OPEN and resumable. Do not require another Human continue instruction for that dispatch.

Does not route EXECUTE, PAPER_FORWARD, broker, or fill while J-0019 is NOT_ACCEPTED.
