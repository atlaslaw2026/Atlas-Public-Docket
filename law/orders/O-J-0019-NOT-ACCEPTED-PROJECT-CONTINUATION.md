# O-J-0019-NOT-ACCEPTED-PROJECT-CONTINUATION

**Filing type:** USER ORDER  
**Date:** 2026-08-27  
**Implements / supplements:** J-0019, J-0020, O-J-0019-NOT-ACCEPTED-RESEARCH-REMAND, O-J-0019-DISTINCT-RESEARCH-BRANCH-LOOP, O-J-0019-OPEN-BRANCH-AUTO-DISPATCH, O-J-0020-AUTOMATIC-CONTINUATION  
**Does not authorize live money.**  
**Does not special-case any project id.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**

## Defect

A J-0019 NOT_ACCEPTED filing could stop machine-authorized work at remaining named gaps (`REMAINING_GAPS_AFTER_TARGETED_WORK`) or at process bounds without classifying the current research branch, closing it where exhausted, discovering a materially distinct direction, opening that branch, and auto-dispatching required work. A Human continue was substituting for that project-level continuation. Remaining SPEC/TARGETS UNKNOWN after targeted work is not a project-level terminal ruling.

## Rule

When independently computed J-0019 is NOT_ACCEPTED, Atlas shall automatically continue, without another Human continue instruction:

1. Classify the current research branch as still active, exhausted, or otherwise incomplete.
2. Close it as precedent where warranted.
3. Route distinct-research discovery if unused local files do not themselves establish a new direction.
4. Freeze and open the next materially distinct branch.
5. Auto-dispatch required work from the frozen design through Hunter → evidence filing → Math/Qualitative validation → Strategy Design → J-0019.

Stop only on J-0019 ACCEPTED, a proven project-level hard-stop (no materially distinct directions remaining after governed discovery; required data unavailable; exhausted authority; other non-remediable constraint), Human-reserved NEXT, or operational HOLD that is not execution. Remaining remediable gaps after targeted work are not that terminal. Filing NOT_ACCEPTED itself shall start this continuation when a continue loop is not already running.

Does not route EXECUTE, PAPER_FORWARD, broker, or fill while J-0019 is NOT_ACCEPTED. Does not weaken standing acceptance tests. Does not treat NOT_ACCEPTED as proof that no adequate strategy exists.
