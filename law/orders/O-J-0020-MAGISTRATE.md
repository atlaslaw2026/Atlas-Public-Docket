# O-J-0020-MAGISTRATE

**Filing type:** IMPLEMENTING ORDER  
**Implements:** J-0020 (ACTIVE)  
**Date:** 2026-08-25  
**Job:** JOB_GOV_ORCHESTRATOR_MAGISTRATE  
**Does not rename Orchestrator classes.**  
**Does not treat Watcher overlay Magistrate as universal law (J-0007).**  
**Does not disturb J-0016 / J-0017 / J-0018 / J-0019.**  
**Does not authorize live trading.**

## Commands

1. Canonical Magistrate-review schema is `schema/magistrate_review.schema.json`.

2. `atlas_gov.magistrate` is the shared reader. Claiming ACCEPTED, OPERATIVE, WORKING, PROVEN_WORKING, PAPER_READY, PRODUCTION_READY, SCHEDULER_PROVEN, FORWARD_OPERATION_PROVEN, MONITORING, SUBSTANTIVELY_COMPLETE, CLOSED, or equivalent **fails closed** unless a matching Magistrate review record exists and that review's disposition permits the claimed label. Ordinary HOLD/trade/test/trivial-implementation labels remain ungated by this module.

3. `JOB_GOV_ORCHESTRATOR_MAGISTRATE` is UNBLOCKED and remains **RUNNING** as the standing Magistrate function. Proceeding status: RESOLVED — JUDGMENT ENTERED — MAGISTRATE ACTIVATED. Do not rewrite G-5–G-8.

4. Project 1-3 is the first continuing application. Preserve G-31 as historical review. File `MAG-1-3-001` against **current** 1-3 posture. Do not redo V2 research. Do not treat AAA-002 `SCHEDULER_PROVEN` as project-level remote autonomous scheduling.

5. If NEXT_REQUIRED is authorized machine work Atlas can perform, route it. Do not return 1-3 to the Human solely for a continue instruction. External GitHub login or missing hosted secrets remain USER_RESERVED.

6. Do not append `viewer/docket/INDEX.json` (next_docket_no remains 88). Record J-0020 on `docket/ATLAS_GOVERNANCE_FILINGS.json`.

7. Implementation evidence: `findings/F-J-0020-IMPLEMENTATION.md`. Required test: `validation/test_j0020_magistrate.py`.
