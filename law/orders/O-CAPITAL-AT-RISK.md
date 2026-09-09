# O-CAPITAL-AT-RISK — ORDER: Capital-at-risk; TARGET_STRATEGIC_CASH = 0% for the next AI challenger

FILING TYPE: ORDER  
DATE: 2026-08-24  
ISSUER: User  
STATUS: ACTIVE  
JOB: JOB_CAPITAL_AT_RISK_RULE  
AUTHORITY: Explicit user instruction to make a rule that experiment capital is at risk, so strategic cash shall be 0%, and not to apply that rule retroactively to AI-ALG2-V1.

## Identity

- Rule name: `CAPITAL_AT_RISK`
- Machine target: `TARGET_STRATEGIC_CASH = 0%`
- Binds: the next authorized AI challenger after frozen `AI-ALG2-V1` (including any later AI-ALG2-V2 / ALG3 / successor identity the user later authorizes)
- Does not bind: `AI-ALG2-V1`, `AI-ALG2-V1-CA-REPLAY`, Task 8, Task 12 replay artifacts, or `ALG1-V1` / `ALG1-V1-CA-REPLAY` / `ALG1-V1-PAPER-FORWARD`

This Order does not create, code, or authorize that next challenger. It states the cash rule that challenger must obey if and when it is separately authorized.

## CAPITAL-AT-RISK RULE

The AI challenger shall target 100% deployment of experiment capital among currently eligible securities.

`TARGET_STRATEGIC_CASH = 0%`

Cash is not an investment decision and may not be used merely because the AI is uncertain, cautious, or prefers lower volatility.

If the AI reduces or exits one eligible position, the released capital must be reallocated among other eligible positions according to its judgment.

Temporary cash caused by order settlement, fills, market closure, rounding, or other execution mechanics is permitted but must not be treated as a strategic allocation.

If Governance or a risk rule makes every available investment ineligible, cash may be held as an operational necessity and the reason must be recorded.

The purpose of the experiment is to determine how well AI allocates capital at risk, not how well it avoids allocating capital.

## Frozen ALG2 result

Do not apply this rule retroactively to ALG2.

`AI-ALG2-V1` stays frozen, including the corrected-ruler ending cash weight **0.2909 (29.09%)** / **$1,097.56** cash on `AI-ALG2-V1-CA-REPLAY`. That cash result is evidence of why the frozen protocol failed the experiment. It is not a defect to be patched in place.

Task 8 published endings remain **$14,624.71 / $14,624.71 / $6,609.16**. Task 12 corrected-ruler endings remain Passive **$5,444.07**, ALG1 **$5,831.35**, AI **$3,772.87**. Verdicts `AI_ALG2_BEATS_NEITHER` and `AI_ALG2_CA_REPLAY_BEATS_NEITHER` remain historical.

## Does not authorize

- Rewrite of `AI-ALG2-V1` source, prompts, gates, `CASH_FLOOR`, `CASH_CAP`, or `DEFENSIVE_CASH`
- Creation or implementation of ALG3 / AI-ALG2-V2 in this job
- Alpaca live orders, or any broker orders
- Using Task 10 qualitative corpus as point-in-time knowledge
- Changing ALG1-V1 paper-forward operations
- Closing or altering `JOB_TASK_13_AI_ALG2_FORENSIC_AUDIT`
