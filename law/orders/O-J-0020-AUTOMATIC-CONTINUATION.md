# O-J-0020-AUTOMATIC-CONTINUATION

**Filing type:** USER ORDER  
**Date:** 2026-08-26  
**Implements / supplements:** J-0020, O-J-0020-MAGISTRATE  
**Does not authorize live money.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**

## Defect

Magistrate reviews recorded machine-authorized NEXT_REQUIRED (user_decision_required false) but `file_review` did not dispatch rooms, and the supervisor cycle was not invoked by the review constructor. NEXT was therefore recorded without automatic execution. A Human “continue” was being used as a substitute for that missing dispatch.

## Rule

Whenever Governance determines a next action is machine-authorized and no Human-reserved boundary exists, the Magistrate/supervisor mechanism shall automatically dispatch and continue the governed workflow. Do not require a separate Human continue instruction for that work.

Does not perform broker or live execution. Does not treat MAG `blocks_execution` as a stop on research-room dispatch. Does not special-case any project id.
