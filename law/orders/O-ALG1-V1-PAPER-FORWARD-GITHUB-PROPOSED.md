# O-ALG1-V1-PAPER-FORWARD-GITHUB — PROPOSED ORDER

FILING TYPE: PROPOSED ORDER  
DATE: 2026-08-24  
JOB: JOB_ALG1_V1_PAPER_FORWARD  
STATUS: SUPERSEDED BY ORDER (same-day user instruction adopted the text below)  
This Proposed Order is not law.

## Proposed authorization

Permit GitHub Actions to invoke the existing frozen ALG1-V1 paper-forward adapter unattended, with this exact chain and no other:

**GITHUB → ALG1-V1-PAPER-FORWARD → ALPACA PAPER ONLY**

## Proposed limits

- Paper host `https://paper-api.alpaca.markets` only.
- Reject Alpaca live host `https://api.alpaca.markets`.
- Do not set `ALPACA_ORDERS_ENABLED` for the V1 filing-harvest path.
- Do not authorize `GITHUB → ALPACA LIVE`.
- Laptop/local Task Scheduler is not the production scheduler.
