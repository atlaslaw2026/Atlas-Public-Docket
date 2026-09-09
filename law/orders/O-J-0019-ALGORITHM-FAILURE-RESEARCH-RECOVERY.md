# O-J-0019-ALGORITHM-FAILURE-RESEARCH-RECOVERY

**Filing type:** USER ORDER  
**Date:** 2026-08-27  
**Implements / supplements:** J-0019, J-0020, O-J-0019-HUNTER-EVIDENCE-HANDOFF, O-J-0019-NOT-ACCEPTED-RESEARCH-REMAND, O-J-0019-DISTINCT-RESEARCH-BRANCH-LOOP  
**Does not authorize live money.**  
**Does not special-case any project id.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**

## Defect

Strategy Tournament / ALGORITHM failure outcomes (`NO_CANDIDATE_ADEQUATE` and kin) were recorded as tournament artifacts (`next_governance=DISTINCT_RESEARCH`) that `compute_next_act` did not consume. MATH/QUAL validator rejection returned `DISPATCH_FAILED` or allowed the algorithm chain to continue. J-0019 remand could send Hunter-acquired evidence to MATH/QUAL or Strategy Design without LIBRARIAN custody.

## Rule

Remediable ALGORITHM, Strategy Tournament, Strategy Design, MATH, QUAL, J-0019, and exhausted-branch failures shall be filed as typed deficiencies (`origin_stage`, `deficiency_class`, `required_evidence_or_research`, `remediable`, `source_artifact`, `lineage_parent`, `resume_stage`). The sole NEXT_ACT chooser is `atlas_gov.rooms.runtime.compute_next_act`; it shall consume the open deficiency and dispatch the recovery chain. New investigation routes HUNTER, then necessarily LIBRARIAN, then MATH/QUAL as required, then resume of the exact originating stage. Do not WAIT, silently continue, substitute stale packets, mint synthetic downstream success, require Human CONTINUE, or route EXECUTE/PAPER_FORWARD while J-0019 is NOT_ACCEPTED.
