# O-ALG1-V1-PAPER-FORWARD-GITHUB — ORDER

FILING TYPE: ORDER  
DATE: 2026-08-24  
AUTHORITY: Explicit user instruction to run ALG1-V1-PAPER-FORWARD unattended from GitHub, laptop independent, paper only. Binds `JOB_ALG1_V1_PAPER_FORWARD` only. Adopts the Proposed Order after Argument and Counterargument.

## Authorization (entire chain; nothing more)

**GITHUB → ALG1-V1-PAPER-FORWARD → ALPACA PAPER ONLY**

GitHub Actions may submit Alpaca orders **only** when all of the following are true:

1. Workflow is the dedicated ALG1-V1 paper-forward workflow (not the harvest/track cycle).
2. Job identity is `JOB_ALG1_V1_PAPER_FORWARD` / `ALG1-V1-PAPER-FORWARD`.
3. Endpoint is `https://paper-api.alpaca.markets`.
4. Live endpoint `https://api.alpaca.markets` is rejected.
5. Credentials are the paper account keys.
6. Returned Alpaca account matches the expected paper account (hash/id check); otherwise abort.
7. Frozen ALG1-V1 `HOLD_PASSIVE_SLEEVES` cadence applies (month-end equal-weight; inherited-book first session was HOLD).
8. Duplicate session cycles do not submit again.

## Preserve

- `alpaca_execution.py` GITHUB_ACTIONS kill-switch for V1 harvest / general trading.
- `ALPACA_ORDERS_ENABLED` default off on harvest workflows.
- Live trading hard-blocked at multiple layers.
- Task 7, Task 8, Task 11 historical artifacts untouched.
- ALG1-V1 logic is not redesigned because the scheduler moved.

## Does not authorize

- GITHUB → ALPACA LIVE
- General GitHub trading permission
- Local Windows Task Scheduler as production scheduler
