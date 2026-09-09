# O-J-0019-NOT-ACCEPTED-RESEARCH-REMAND

**Filing type:** USER ORDER  
**Date:** 2026-08-26  
**Implements / supplements:** J-0019, O-J-0019-ALGORITHM-ACCEPTANCE  
**Does not disturb** J-0016. **Does not authorize live money.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**

## Defect repaired

A J-0019 **NOT_ACCEPTED** disposition had no enforceable machine return into HUNTER, ATLAS_MATH, QUALITATIVE, ARGUMENT, COUNTERARGUMENT, and STRATEGY_DESIGN. `allowed_next` was not dispatched. Failed acceptance must not be routed to broker, fill, or execution work.

## Rule

When an independently computed Acceptance Audit is **NOT_ACCEPTED** and at least one failed criterion is **research-remediable**, Atlas shall remand the affected project into the governed research workflow. The remand packet shall carry the audit id, failed conditions, UNKNOWN states, tests evaluated, and evidence evaluated. The next cycle shall address those deficiencies and shall not blindly repeat prior work.

Research-remediable states: `RESEARCH_REPRODUCED`, `SPEC_CODE_MATCHED`, `SIGNAL_COMPUTED`, `TARGETS_GENERATED`.

Operational-readiness states (`BROKER_CONNECTED`, `ORDER_PATH_PROVEN`, `FILL_PATH_PROVEN`, `SCHEDULER_PROVEN`, `FORWARD_OPERATION_PROVEN`) do not by themselves authorize execution. They also do not prove that no adequate strategy exists.

**NOT_ACCEPTED is not proof that no adequate strategy exists.**

Continue cycling until independently computed J-0019 **ACCEPTED**, a substantive evidence-based no-adequate-strategy conclusion, or a genuine Human-reserved boundary.

Project 1-7 existing evidence, filings, findings, and paper state are preserved. Paper only. Live UNPROVEN.
