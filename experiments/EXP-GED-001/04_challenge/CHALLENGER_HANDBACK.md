# Challenger hand-back for Q1 (verbatim)

The Analyst's main finding holds: the March jump is a fieldwork-design artifact, not a change in consumer behaviour. But the Analyst missed a clear seasonal pattern in the data, and that makes C-4 (the December forecast) biased low. C-4 should not be approved as written.

I rebuilt the analysis independently in my own script. It reads only the five authorized files and nothing under restricted/, and I wrote and ran it before opening the Analyst's analysis.py or its output. Every Analyst number I recomputed matches, which means reproduced by an independent method, not independently verified. My script's self-test passed and caught both errors I planted in it.

**The miss:** in both pre-change years, April–July ran about 1.7 points below the rest of the year (t=5.2). March and December sit high. The Analyst checked seasonality only on the Feb→Mar change, so the whole pattern was missed.

**Proposed dispositions**

| Conclusion | Disposition | Why |
|---|---|---|
| C-1 Why it jumped | **SUSTAIN**, with wording changes | Three methods on different assumptions all find no detectable real change: same-month year-over-year (about −0.4), a seasonal counterfactual (gap +3.5 against the bridge's 3.6, residual about −0.1), and the bridge's online arm compared with Apr–Jul on the same design (about +1.1, not distinguishable from zero). The wording must state that the bridge is assumed comparable to the published series (U-05) and that the effect is assumed stable after February. |
| C-2 "Still climbing" | **MODIFY** | Apr–Jul is the normal seasonal low, so a 2–3 point rise into Q4 is expected with no behaviour change. The Analyst's test (Sep/Oct above ~33 means a real rise) would misread normal seasonality as growth. F-13 leaves out the 55+ group, which is 4.75 points up and supplies a third of August's rise, so three of four age groups are elevated, not two. |
| C-3 Who is driving it | **MODIFY** | The 18-24 label should be UNKNOWN, not CONFLICTED: it is one source with two adjustments, both indistinguishable from zero. On seasonally matched comparisons every age group's residual is +0.1 to +0.7, and 18-24 is the smallest. That strengthens the rejection of "younger shoppers are driving it". |
| C-4 December | **MODIFY; do not approve as written** | Seasonal methods give 32.9–33.9 against the Analyst's 31.6, and four of five sit above its 80% upper bound. Backtested on Aug–Dec 2025, the Analyst's trend-only method forecast 1.2 points too low on average. Proposed: about 33% (80% range 31–35); on the old-method basis about 29–30, not 28. The seasonal pattern rests on only two years, and the December-specific part is weakly identified. The rejection of 38–40% stands. |
| C-5 Harlow | **MODIFY** | March's excess over April–July matches its usual seasonal position. The Analyst treated it as a possible short-lived Harlow bump; on the evidence, nothing March-specific is left. |

**Findings to strike or correct:** F-10 (uncorrected seasonal low) strike; U-10 (design effect ~1.2×) reword as UNKNOWN; F-21 relabel INFERRED seasonal. NP-6 was right only for the Feb→Mar jump. The other rejected explanations stand.

**Access and evidence audit:** No conclusion depends on unauthorized data. analysis.py re-reads the bytes of the restricted files on every run, so it must not be rerun until those paths are removed. The Analyst read README.md and ACCESS_POLICY.md, which are not on the grant's authorized list, and U-06 relies on ACCESS_POLICY.md. Marking restricted files QUARANTINE conflates access with admissibility. The register's statement that no material claim rests on LEAD material is wrong: applying the February bridge effect to later months is LEAD-classed. This doesn't change C-1, but the note must be corrected.

**Capability accounting:** four available analyses were skipped: seasonal modelling, forecast backtest, same-design comparison, calendar-month inspection. The chart skill's NOT_NEEDED reason doesn't hold. HUMAN_RESERVED for the restricted data should become not authorized by the grant.

**Still open:** the deck basis (U-11) stays USER_CONFIRMATION_REQUIRED. Headline pair becomes ~33 published vs ~29.5 old-method, instead of 31.6 vs 28.0.

Files: 04_challenge/COUNTERARGUMENT.md, READ_LOG.md, reconstruct.py, reconstruct_output.txt
