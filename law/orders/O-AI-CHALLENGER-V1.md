# O-AI-CHALLENGER-V1 — ORDER: Prospective AI forward challenger

FILING TYPE: ORDER  
DATE: 2026-08-24  
ISSUER: User  
STATUS: ACTIVE  
JOB: `JOB_AI_CHALLENGER_V1`  
AUTHORITY: Explicit user instruction to create a governed forward experiment comparing AI judgment to frozen `PASSIVE-FORWARD-BASELINE` and frozen `ALG1-V1-PAPER-FORWARD` on new market data.

## Identity

- Experiment: `AI-FORWARD-CHALLENGER-V1`
- Challenger: `AI-CHALLENGER-V1`
- Controls (do not alter): `PASSIVE-FORWARD-BASELINE`, `ALG1-V1` / `ALG1-V1-PAPER-FORWARD`
- Project: `1-1` (Space Investment Research)
- This is a **NEW** algorithm version. It is not `AI-ALG2-V1`, not `AI-ALG2-V1-CA-REPLAY`, and not ALG3-by-rewrite.

## ORDERS

1. Maintain three independently measured portfolios from the same comparison timestamp and equivalent starting capital: Passive (control), ALG1-V1 (proven rebalancing benchmark), AI-CHALLENGER-V1 (challenger).

2. Do not change Passive or ALG1 rules to make the AI comparison easier. Do not rewrite Task 7, Task 8, Task 11, Task 12 replay, or `AI-ALG2-V1`.

3. AI decisions must use only information knowable at the decision timestamp. Freeze each material judgment before subsequent market results are known. Do not rewrite reasons after outcomes.

4. Bind `J-0015` / `O-CAPITAL-AT-RISK`: `TARGET_STRATEGIC_CASH = 0%`. Temporary execution cash is permitted. Qualitative / press-release evidence remains unauthorized.

5. If only one Alpaca paper account exists, ALG1 remains the paper execution book. Passive and AI are deterministic shadow ledgers. Do not fake account separation. AI must not place live or paper broker orders unless separately authorized. This Order does **not** authorize AI broker POST.

6. Ordinary authorized cycle actions do not require a new human click. Governance must preserve a reconstructable record of who is ahead and why.

## Success question

Answer separately, net of modeled costs, from the filed experiment start:

- Has AI produced more net wealth than Passive?
- Has AI produced more net wealth than ALG1?

Never call AI successful for beating only one.

## Does not authorize

- Live (real-money) trading
- AI posting to Alpaca paper
- Changing ALG1 paper-forward operations
- Using Task 10 qualitative corpus
- Silently replacing `AI-CHALLENGER-V1` with a V2 after seeing later prices
