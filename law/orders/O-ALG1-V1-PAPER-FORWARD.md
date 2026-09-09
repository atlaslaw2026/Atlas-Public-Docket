# O-ALG1-V1-PAPER-FORWARD — ORDER

FILING TYPE: ORDER  
DATE: 2026-08-24  
AUTHORITY: Explicit user instruction to activate frozen ALG1-V1 as the autonomous Alpaca **paper** trading baseline. Binds `JOB_ALG1_V1_PAPER_FORWARD` only.

## Identity

- Forward identity: `ALG1-V1-PAPER-FORWARD`
- Frozen policy: `ALG1-V1` / `CAND-001` `HOLD_PASSIVE_SLEEVES`
- Job: `JOB_ALG1_V1_PAPER_FORWARD`
- Venue: Alpaca paper trading only

## ORDERS

1. Activate the existing locked ALG1-V1 policy as the current forward paper-trading baseline. Task 11 (`ALG1-V1-CA-REPLAY`) remains historical validation evidence only. Do not convert the replay into a trading algorithm. Do not rewrite ALG1-V1, Task 7, Task 8, or Task 11 artifacts.

2. Current paper account state is the starting state. Do not treat this as a new $100,000 experiment. Do not liquidate to restart.

3. ALG1 may operate autonomously on its existing locked cadence (month-end equal-weight rebalance of the authorized ten-name eligible basket). Ordinary rebalance/orders authorized by that frozen policy do not require a new per-trade human approval.

4. If a basket name has a zero position: determine why before any buy. If it remains eligible and no Judgment, Order, risk gate, or exclusion blocks re-entry, treat it as an underweight sleeve at the next authorized ALG1 rebalance. If it is ineligible or blocked, do not buy merely to restore equal weight.

5. PAPER TRADING ONLY. Hard-block live-trading endpoints and live credentials. Every submitted order must route to Alpaca paper trading. Do not enable the historical V1 filing-harvest order path.

6. Record decisions, proposed vs submitted orders, fills, cash, equity, positions, and Governance authority. J-0012 usage accounting applies; missing tokens are UNKNOWN, never invented MEASURED zero.

## Does not authorize

- Live (real-money) Alpaca orders
- Redesign of ALG1, new signals, Task 10 qualitative inputs, new thresholds, or a silent cadence change
- Modification of Task 7 / Task 8 / Task 11 historical artifacts
