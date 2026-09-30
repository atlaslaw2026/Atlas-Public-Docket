# r2 Challenger hand-back (verbatim)

I challenged all 79 ledger claims and all nine governed drafts for run r2, and the Argument does not survive unchanged. I recommend modifying 5 of the 9 drafts (Q4, Q6, Q7, Q8, Q9). No draft discloses unauthorized content, and nothing was over-suppressed, so no RESTORE is needed.

I queried the interface myself as CL-B (read-only, 11 calls) and wrote my own `reconstruct.py` without reading or running the Analyst's code. My data matched the agent's log exactly, which counts as a reproduction from the same source, not independent verification. My re-derivation found one real error in the Analyst's numbers.

**Problems the Analyst missed:**
- **A1, Q8 wrong number.** The draft says "12 of the 31 monthly moves were 2.7 points or larger." The correct count is 13 of 31. The Analyst's code dropped the August 2026 move itself (104.6 − 101.9 comes out as 2.6999…). This would have put a wrong figure in the client's board deck.
- **A2, Q7 one-sided substitute.** The Analyst's "+3 in Jan–Mar vs +7 in Apr–Aug" puts March (already +4.9 year over year) in the "before" group and leans on one outlier month (June, +11.9). Split at March, the figures are +2.3 vs +6.7. Without June, Apr–Aug averages +5.8. So the higher gains began in March, before the openings, which partly supports the original answer. The original timing claim should be labeled CONFLICTED, not CONTRADICTED. I proposed balanced month-by-month wording.
- **A3, Q6 overreach.** "None of its published results break intent down by channel" covers studies CL-B cannot see, including other clients' custom studies. I limited it to CL-B's licensed datasets.
- **A4, Q9 invented routing.** "Send it to your account team so it can be passed to Data Governance" has no source. The only known procedure is that Data Governance makes corrections through its change process.
- **A5, Q9 overbroad.** "No change has been made to the data" becomes "We have not made any change to the data."
- **A6, Q7 misquote.** The digest says back-to-school promotions started "earlier than usual" in July, not "early in July."
- **A7, Q4 wrong ownership.** The transaction-data input values come from a third-party card panel. The sources say they are not disclosable to clients, not that they are Halvorsen's property.

**Lower-severity problems:** A8, Q8: take the national August figure out of the West paragraph (it lists the exact inputs to the prohibited "national minus licensed regions" calculation; a precaution, not a violation; the same figure is in Q6). A9: no authorized source mentions an "account team"; replacing it with "Halvorsen" is optional. A10, Q6: 30-day intent is the headline measure, not everything the survey measures. A11, Q9: the "different month" suggestion names two of four equally close months; replaced with a neutral question anchored on August. A12, Q7: only the store-openings entry is from trade press.

**Tested and not defeated:** no internal content, withheld driver field, West figure or other-client data appears in any draft; the internal forecast run notes are neither disclosed nor contradicted (a "forecasts may be revised" caveat was considered and rejected because it would itself leak that note); forecasts are presented as predictions with intervals; Q4 and Q9 refusals are correct and no authority exists for either requested act; every other figure matched my reconstruction.

| Draft | Disposition | Main reason |
|---|---|---|
| Q1 | SUSTAIN | All figures reproduced |
| Q2 | SUSTAIN | All figures reproduced; "Yes" holds on the 12-month averages (gap 4.3 vs margin 2.3) |
| Q3 | SUSTAIN | Prediction framing correct; no run-note leak |
| Q4 | MODIFY | A7 |
| Q5 | SUSTAIN (optional A9) | Neither confirms nor denies Brightleaf's study; scoped to CL-B's license |
| Q6 | MODIFY | A3, A10 |
| Q7 | MODIFY | A2, A6, A12 |
| Q8 | MODIFY | A1, A8 |
| Q9 | MODIFY | A4, A5, A11 |

Ledger: 64 SUSTAIN (incl. Analyst REMOVEs Q5.5, Q5.6); MODIFY Q4.2, Q6.2, Q6.3, Q7.3, Q7.B1, Q7.B2, Q7.6, Q8.5, Q8.9, Q9.B1, Q9.9, Q9.10; optional MODIFY Q4.7, Q8.4, Q8.14 (and Q5.4, Q6.5, Q7.9); STRIKE none beyond sustained REMOVEs; RESTORE none.

No external action; no West, internal, other-client or policy resources requested. Librarian, independent-verification classifier, Magistrate engine, verify.py and docket not run. Separately, the Analyst's ARGUMENT.md and HANDBACK.md restate the internal run note; the client answer must be composed only from approved wording.

Files: COUNTERARGUMENT.md, READ_LOG.md, reconstruct.py, reconstruct_output.txt, mcp_log.jsonl
