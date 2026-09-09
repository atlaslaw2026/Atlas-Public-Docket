# O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION

**Filing type:** USER ORDER  
**Date:** 2026-09-05  
**Identifier:** `O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION`  
**Adopts:** Human ruling — source-grounded and independent verification  
**Implements / supplements:** J-0001, J-0011, J-0018, J-0019, J-0020  
**Does not create a new ACTIVE Judgment.** Disk ACTIVE judgment set remains pinned to `CURRENT_LAW.json` `current_sha`.  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**  
**Does not accept a strategy, authorize trading, permit purchases, change frozen research thresholds, or erase historical findings.**

IT IS SO ORDERED.

## Ruling

Repeated agreement does not establish correctness. Running the same code twice, reproducing its output, matching hashes, or obtaining agreement from another AI is insufficient to label a result VERIFIED, VALIDATED, CORRECT, or PASS.

This rule applies to Atlas verification claims across projects.

This Order is the adopting instrument. It is not itself a Judgment. It does not rewrite G-n history.

## 1. Verify against source evidence

Every material claim must be traceable to preserved source evidence. Verify its origin, identity, timestamps, units, coverage, and applicability to the claim. A hash establishes file integrity, not factual accuracy.

For trading research, verify the actual contract, dated instrument mapping, expiration, strike, right, multiplier, quote, and information available at the decision time. Never assume an identifier is stable across sessions.

## 2. Verify the method as well as the data

Real source data does not make an incorrect calculation valid. Independently check formulas, assumptions, timing, sizing, cash accounting, costs, and economic meaning.

Reconcile starting cash, transactions, remaining cash, positions, and marked equity. Do not compound fixed-size trade profits as though positions were proportionally resized.

## 3. Require independent reconstruction

The verifier must derive expected results from source evidence and the specification without relying on the producer’s summaries or reusing the disputed calculation and mapping logic.

A different agent running the same evaluator is reproduction, not independent mathematical verification. Disclose shared code, dependencies, and assumptions.

## 4. Test whether the verifier can detect errors

Use independently calculated cases with known answers and deliberate defects. For Project 1-11, include wrong-contract mappings, reused identifiers, negative fills, future information, incorrect multipliers, and incorrect compounding.

A verification process that cannot detect those defects cannot certify the affected calculations.

## 5. Reconstruct the complete affected path

If a defect changes signals, exits, sizing, or subsequent decisions, rerun the complete affected sequence. Repricing trades at exit dates selected by faulty logic is diagnostic only, not a corrected backtest.

Previously viewed data remains viewed after repairs.

## 6. Limit claims to what was proven

Distinguish:

- **REPRODUCED** — the output can be generated again.
- **SOURCE CHECKED** — the inputs and their interpretation were checked.
- **INDEPENDENTLY VERIFIED** — source evidence and an independent method support the result.

State the exact scope, coverage, tolerances, and limitations. Sampling cannot certify unexamined results. Missing or contradictory evidence requires **NOT PROVEN**; a demonstrated material defect requires **FAIL**.

## 7. Preserve history and resolve contradictions

Preserve original reports and add linked corrections. Mark affected claims as unreliable pending reconstruction.

For Project 1-11, reconcile the conflicting V13 completion and missing-data reports using exact commits, paths, timestamps, and artifact hashes. Do not select whichever report is more favorable.

## 8. Implementation and authority

Register this order under this identifier. Implement it in the applicable verification procedures and acceptance checks, with tests proving unsupported success claims are blocked.

This order does not accept a strategy, authorize trading, permit purchases, change frozen research thresholds, or erase historical findings.

Saving this file is not compliance.

## Operating module

`atlas_gov.independent_verification`

- `evaluate_verification_packet` classifies REPRODUCED / SOURCE_CHECKED / INDEPENDENTLY_VERIFIED / NOT_PROVEN / FAIL.
- `may_claim_verification` fail-closes VERIFIED / VALIDATED / CORRECT / PASS / INDEPENDENTLY_VERIFIED unless the packet class is INDEPENDENTLY_VERIFIED.
- `known_answer_defect_battery` must detect the six Project 1-11 defect classes.
- Wired into `atlas_gov.acceptance.may_represent`, `atlas_gov.acceptance.compute_acceptance`, and `atlas_gov.rooms.validators.math_validator`.

Schema: `schema/independent_verification.schema.json`.  
Required test: `validation/test_o_source_grounded_independent_verification.py`.  
Implementation evidence: `findings/F-O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION-IMPLEMENTATION.md`.

Do not append `viewer/docket/INDEX.json`. Record this Order on `docket/ATLAS_GOVERNANCE_FILINGS.json`.
