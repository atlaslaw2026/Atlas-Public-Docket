# O-J-0019-INVOCATION-BOUND-NOT-PROJECT-STOP

**Filing type:** USER ORDER  
**Date:** 2026-08-27  
**Implements / supplements:** J-0019, J-0020, O-J-0020-AUTOMATIC-CONTINUATION, O-J-0019-NOT-ACCEPTED-PROJECT-CONTINUATION  
**Does not authorize live money.**  
**Does not special-case any project id.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**

## Defect

`MAX_OUTER` bounded a single `continue_machine_authorized_project` call and was recorded as `stopped`, after which the project loop idled until another Human continue. That treated a runtime invocation limit as a project-level terminal while J-0019 remained NOT_ACCEPTED and the Human objective remained active.

## Rule

`MAX_OUTER` (and equivalent per-invocation step budgets) may end one process invocation to bound recursion and resource use. They are not Governance terminal dispositions and shall not stop the project loop.

When a bounded continuation reaches `MAX_OUTER` and the classifier remains machine-authorized CONTINUE, Atlas shall persist canonical continuation state (`invocation_bound`, not `project_terminal`) and immediately schedule or dispatch the next governed continuation cycle from that state without another Human prompt. Later invocations shall not re-dispatch already-completed room work, shall not erase branch history or independently PROVEN research states, and shall remain fail-closed for EXECUTE / PAPER_FORWARD / broker / fill while J-0019 is NOT_ACCEPTED.

Stop the project loop only on J-0019 ACCEPTED, an authorized project-level terminal ruling, Human-reserved NEXT, or legitimate operational HOLD that is not execution.
