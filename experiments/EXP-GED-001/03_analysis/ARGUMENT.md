# ARGUMENT — Analyst, EXP-GED-001

```
MATTER (unfiled; public-agent record)
Office: ANALYST (Argument). Not a determination. Nothing here is verified, approved, or final.
```

**User question.** The tracker's share planning to do most grocery shopping online went from ~29% (Feb) to 33% (Mar) and "is still climbing" (Aug 36%). Why did it jump, which consumers are driving it, and where should we expect it by December?

**Evidence used.** Only the authorized files in the grant: `tracker_topline.csv`, `tracker_by_age.csv`, `bridge_study_2026-02.csv`, `methodology_notes.md`, and `market_context_digest.md` (commentary only). Nothing under `restricted/` was opened or used. Admissibility classes are in [EVIDENCE_REGISTER.json](EVIDENCE_REGISTER.json). Every number comes from [analysis.py](analysis.py). Output is in [analysis_output.txt](analysis_output.txt), cited as K-xx.

**Statistical caveat that applies throughout.** Standard errors (SE) assume simple random sampling on the unweighted n. The tracker is weighted, so true SEs are somewhat larger. The design effect is UNKNOWN. As a check, the legacy series' actual month-to-month noise around its trend is 1.09 pts (K-10). A single month's SRS SE is 0.89 pts, so the SRS figures understate the noise only modestly.

## Short version

1. **Why it jumped.** In March 2026 the tracker switched from mixed phone and online fieldwork to an online-only panel, and the published series was not adjusted for this (KNOWN). The Methods team's own February bridge study found that the online panel reads **3.6 pts higher** than the legacy design on the same measure (95% CI 1.0–6.2). That is about 86% of the 4.2-pt Feb→Mar jump. After allowing for it, the data show no detectable real change in online-grocery intent (INFERRED).
2. **Who is driving it.** The step shows up in every age group, which is what a methodology shift would produce. No consumer segment can be shown to drive a real change. The "younger shoppers / Harlow effect" story is not supported by the authorized evidence.
3. **Still climbing?** Not in the final data. April–July are flat at 30.6–31.6. August's 36.3% is a preliminary partial sample (n=411, about 16% of a normal month). It is driven by very small young-adult cells, and it will be replaced on 2026-10-06.
4. **December.** On the basis the tracker publishes (online panel), expect **about 31–32%**, with an 80% range of roughly 30–33%, and higher under alternative assumptions (C-4). On a legacy-comparable basis that is about 28%, roughly where it was a year ago. This assumes no further methodology change or official adjustment.

---

## a. Findings table

Categories: OBSERVED FACT / INFERENCE / PREDICTION / UNKNOWN. Labels per J-0001.

| ID | Claim | Category | J-0001 label | Evidence pointer | Reasoning |
|---|---|---|---|---|---|
| F-01 | Published pct_online_primary was 28.9 in Feb-2026 and 33.1 in Mar-2026, a change of +4.2 pts. Both are FINAL. | OBSERVED FACT | KNOWN | `tracker_topline.csv` rows 2026-02, 2026-03; K-01 | Direct read. The user's "29% → 33%" is accurate. |
| F-02 | Fieldwork moved to an online-only, probability-recruited panel in 2026-03. CATI (phone) was retired. Wording and weighting are unchanged. The published series is **not adjusted** for the transition. The Feb-2026 figure is from the legacy design. The Methods team is evaluating whether an adjustment is required. | OBSERVED FACT | KNOWN | `methodology_notes.md` entry 2026-03 | Direct statement by the data owner. The jump happens in the first month on the new design. |
| F-03 | In the Feb-2026 bridge wave, the online panel read 31.1 and the legacy design read 27.5, a difference of +3.6 pts (SRS SE 1.31; 95% CI +1.0 to +6.2). | OBSERVED FACT (the estimate); its CI is computed | KNOWN (point estimate); CI INFERRED from the SRS formula | `bridge_study_2026-02.csv` rows ALL; K-05 | The same population was measured in the same month by both designs, so the difference isolates the design (mode/panel) effect, within sampling error. |
| F-04 | The bridge mode difference equals 86% of the Feb→Mar jump (3.6 / 4.2). | INFERENCE (arithmetic on KNOWN values) | INFERRED | K-05 | Ratio of F-03 to F-01. |
| F-05 | The Feb→Mar 2026 change (+4.2) is 3.8× the SD of legacy month-to-month changes (1.11). It exceeds any legacy month-to-month change (max 3.4). | OBSERVED FACT (computed) | KNOWN | K-03 | The jump is too large to be ordinary monthly noise. Something changed. |
| F-06 | Feb→Mar was +1.2 in 2024 and +0.5 in 2025. | OBSERVED FACT | KNOWN | `tracker_topline.csv` 2024-02/03, 2025-02/03; K-02 | There is no history of a March seasonal jump of this size. |
| F-07 | Level step: the 12 legacy months 2025-03..2026-02 average 27.82. The online months Apr–Jul 2026 average 30.95. The step is +3.12 (SE 0.37). Minus the bridge mode effect, the residual is **−0.48** (95% CI −3.15 to +2.20). Alternative windows give residuals of −1.18 and −0.04, and every CI includes zero. | INFERENCE | INFERRED | K-07 | After removing the measured design effect, no real level change is detectable. A genuine rise of up to about 2–3 pts cannot be excluded (upper CI). |
| F-08 | Year-over-year, Apr–Jul 2026 minus Apr–Jul 2025 is +4.22. Minus the mode effect that leaves +0.63. The legacy trend was about +1.1 to +1.2 pts/yr (2024→2025 calendar means +1.07; OLS 1.21/yr). | INFERENCE | INFERRED | K-09, K-10 | The mode-adjusted YoY change is at or below the pre-existing slow uptrend. No acceleration is evident. |
| F-09 | Mode-adjusted (legacy-equivalent) values: Mar 29.5, Apr 27.0, May 27.2, Jun 28.0, Jul 27.2. The Apr–Jul mean is 27.35, against a legacy 12-month mean of 27.83. | INFERENCE | INFERRED | K-08 | This assumes the Feb-2026 bridge mode effect applies unchanged in later months (see U-03). |
| F-10 | Relative to the legacy linear trend plus the mode effect, Apr–Jul 2026 run **1.56 pts below** expectation (each month −0.96 to −1.86). March is 0.84 above. | INFERENCE | INFERRED | K-10 | This is not evidence of acceleration. If anything, the underlying level is at or slightly below trend once the mode effect is removed. Could be noise, a smaller true mode effect, or a flattening trend (see U-01). |
| F-11 | April–July 2026 are flat: 30.6, 30.8, 31.6, 30.8. The OLS slope is +0.14 pts/month (SE 0.22). Including March, the slope is −0.36 (SE 0.32). | OBSERVED FACT (values); slope computed | KNOWN (values); slope INFERRED | `tracker_topline.csv` 2026-04..07; K-11 | The FINAL data do not show continued climbing after March. |
| F-12 | Aug-2026 = 36.3 is PRELIMINARY on a partial sample of n=411 (16% of a typical month). SRS 95% CI is 31.7–40.9. It will be replaced at final close, expected 2026-10-06. | OBSERVED FACT | KNOWN | `tracker_topline.csv` 2026-08; `methodology_notes.md` 2026-08; K-13 | The file and the notes say so directly. |
| F-13 | Within August, 18-24 = 65.3 on n=49 (SE 6.8) and 25-34 = 44.6 on n=74 (SE 5.8). 35-54 = 30.0 is at its Apr–Jul mean of 30.8. If the two young cells are set to their Apr–Jul means, the August recombination falls from 36.3 to 32.4. | INFERENCE | INFERRED | `tracker_by_age.csv` 2026-08; K-13 | The August rise comes from two very small cells. Its age composition of n matches normal months (K-13), so the rise is not a composition artifact at the age level. It could be early-responder bias in a partial sample (UNKNOWN, U-04). |
| F-14 | Aug minus Jul = +5.5 pts, z = 2.16 under SRS. | INFERENCE | INFERRED | K-13 | Borderline by SRS. Given the preliminary partial sample and a design effect above 1, this is not reliable evidence of a new rise. |
| F-15 | The Apr–Jul vs pre-period step is positive in **every** age group: 18-24 +4.89, 25-34 +2.52, 35-54 +2.80, 55+ +3.07. | OBSERVED FACT (computed means) | KNOWN (means); interpretation INFERRED | K-07 | A broad-based step across all ages is the pattern expected from a design change. It is not the pattern of one segment changing behavior. |
| F-16 | Bridge mode effects by age: 18-24 −1.4 (SE 4.1), 25-34 +5.1 (3.3), 35-54 +4.8 (2.2), 55+ +3.3 (2.0). Heterogeneity Q=2.03, df=3, p=0.57. The pooled estimate is 3.6. | OBSERVED FACT (cells); test INFERRED | KNOWN (cell values); INFERRED (no evidence of heterogeneity) | `bridge_study_2026-02.csv`; K-06 | The bridge cannot distinguish age-specific mode effects from a common effect. |
| F-17 | For 18-24, the step minus the pooled mode effect is +1.29 (95% CI −3.1 to +5.6). Minus its own cell's mode effect it is +6.29 (95% CI −2.4 to +15.0). For 25+ groups, all residuals are negative or near zero under either adjustment. | INFERENCE | **CONFLICTED** for 18-24 (two defensible adjustments give +1.3 vs +6.3, both CIs include 0); INFERRED (no detectable real change) for 25+ | K-07 | Whether 18-24 show a real rise depends on an unmeasured quantity: the true 18-24 mode effect. Neither result is statistically distinguishable from zero. |
| F-18 | Even if the whole 18-24 residual were real (own-cell basis), its contribution to the topline is about +0.76 pts (share 0.12 × 6.29). Under the pooled basis it is +0.16. | INFERENCE | INFERRED | K-14 | 18-24 is about 12% of the sample. It cannot account for a 4-pt topline move. |
| F-19 | 18-24 is volatile. Pre-period range 31.0–45.0, SD 3.63. The SD of month-to-month change is 4.04. The Feb→Mar +10.0 is 2.5 of those SDs. SRS SE is about 2.8 per month. | OBSERVED FACT (computed) | KNOWN | K-16 | A single-month 10-pt swing in 18-24 is unusual but not extraordinary for this cell. Jan-2026 alone dropped to 31.0. |
| F-20 | Feb→Mar 2026 change by age: 18-24 +10.0, 25-34 −2.1, 35-54 +5.4, 55+ +4.0. | OBSERVED FACT | KNOWN | `tracker_by_age.csv` 2026-02/03; K-14 | The single-month view is noisy and inconsistent (25-34 fell). The multi-month step (F-15) is more reliable. |
| F-21 | March 2026 (33.1) sits 2.15 pts above the Apr–Jul mean, about 1.8–2.0 noise SDs. | INFERENCE | INFERRED (that it is within plausible noise); cause UNKNOWN | K-12 | It could be noise, a first-wave panel effect, or a short-lived real effect (for example, the Harlow promotion). The data cannot discriminate. |
| F-22 | The digest reports Harlow Market free same-day delivery nationwide from 2026-03-03 and competitor fee cuts in April. | OBSERVED FACT (that the digest says this); event itself unconfirmed | KNOWN that the digest reports it; UNKNOWN that the event occurred as stated | `market_context_digest.md` Mar, Apr; register class LEAD | This is secondhand, unsourced commentary (grant: commentary only). |
| F-23 | The Harlow launch month is the same month as the fieldwork transition, so the two are confounded in the tracker. | INFERENCE | INFERRED | F-02, F-22 | Any Harlow effect in March cannot be separated from the design change using the tracker alone. The bridge is the only de-confounding tool, and after it no residual rise is detectable (F-07). |
| F-24 | The digest's June "Harlow effect … pulling younger shoppers online … build through the holidays" is a team opinion about this tracker, with no data attached. | OBSERVED FACT (that it was said) | KNOWN that it was said; the claim itself is QUARANTINE (register) and UNKNOWN as fact | `market_context_digest.md` June | It is a hypothesis to test, not evidence. Testing it against TRUSTED data does not support it (C-3, NP-1, NP-2). |
| F-25 | Internal consistency: the age cells recombine (n-weighted) to the topline within 0.06 pts in all 32 months, and age n sums equal topline n in 32/32 months. The bridge ALL rows reconcile to their cells. | OBSERVED FACT (computed) | KNOWN | K-15, K-05 | This is a data-integrity check only. The files come from the same survey and do not independently corroborate each other. |
| F-26 | The bridge legacy arm (27.5) is 1.4 below the published Feb-2026 tracker (28.9). The difference SE is about 1.28. | OBSERVED FACT (computed) | KNOWN (values); INFERRED (consistent within sampling error) | K-05 | If the published Feb value were used as the legacy anchor, the implied mode effect would be about 2.2 rather than 3.6. That still explains about half the jump, and more of the multi-month step. |
| F-27 | December 2026 on the published (online-panel) basis: central **31.6**, 80% PI 30.0–33.2, 95% PI 29.2–34.0 (method A). Alternatives: B 33.2 (80% 30.8–35.5), C 31.0 (80% 29.4–32.5). A seasonal-December sensitivity gives 32.8. | PREDICTION | INFERRED (conditional forecast) | K-17 | See C-4 for assumptions. |
| F-28 | December 2026 on a legacy-equivalent basis is about 28.0. | PREDICTION | INFERRED | K-17 | Method A minus the mode effect. Compare Dec-2025 = 28.7 (legacy). |
| F-29 | Which consumer segments other than age changed is not in the authorized data. | UNKNOWN | UNKNOWN | EVIDENCE_REGISTER (tracker_by_age: age only) | Resolution is via a Methods data request (ACCESS_POLICY), not the restricted file. |
| F-30 | Whether Methods will adopt an official adjustment, and its size. | UNKNOWN | UNKNOWN | `methodology_notes.md` 2026-03 | See U-02. |
| F-31 | Which basis the Q4 deck should present (published unadjusted, legacy-equivalent, or both). | UNKNOWN | **USER_CONFIRMATION_REQUIRED** | J-0002 materiality test | The answer changes the headline December number (~31.6 vs ~28.0) and the "jump" narrative. The analysis supplies both. The choice of representation is the user's. |

---

## b. Proposed conclusions

### C-1 — Why it jumped: mostly (possibly entirely) a fieldwork-methodology change, not a behavior change

- **Claim.** The Feb→Mar 2026 jump (28.9 → 33.1) coincides with the tracker's switch from mixed phone and online fieldwork to an online-only panel, and the published series is unadjusted for it. The Methods team's own bridge study measured a +3.6-pt design effect (95% CI 1.0–6.2), about 86% of the jump. Comparing the 12 legacy months before with the four settled online months after, the level rose 3.1 pts, statistically indistinguishable from the design effect (residual −0.5, 95% CI −3.2 to +2.2). **The authorized evidence does not show a real increase in consumers' intent to shop online. The jump should not be presented as one.**
- **Category / label.** INFERENCE / INFERRED. The transition and the lack of adjustment are KNOWN (F-02). The bridge estimate is KNOWN (F-03). The attribution is INFERRED.
- **Confidence.** High that the methodology change accounts for most of the jump: the timing is exact, the bridge was designed for this purpose, and all ages moved (F-15). Moderate on "entirely": a real change of up to about 2 pts (upper CI) cannot be ruled out, and March itself sits about 2 pts above Apr–Jul (F-21).
- **Evidence.** F-01, F-02, F-03, F-04, F-05, F-06, F-07, F-08, F-09, F-15; K-01, K-02, K-03, K-05, K-07, K-08, K-09.
- **What would falsify it.** (i) A Methods adjustment study or a repeat bridge showing a mode effect near 0. The Feb bridge's CI lower bound is 1.0, so this would take new evidence. (ii) Evidence that the bridge arms were not comparable, for example different weighting or sample frames (U-05). (iii) Mode-adjusted values in coming months rising well above the legacy trend (for example, more than 2–3 pts above 28 on a legacy-equivalent basis for several FINAL months).

### C-2 — "Still climbing" is not supported; the level has been flat since April, and August is not yet a usable data point

- **Claim.** In FINAL data, the measure has been flat at 30.6–31.6 from April to July (slope +0.14 ± 0.22 pts/month). The August 36.3 is a preliminary partial sample (n=411). Most of its rise sits in two small cells: 18-24 at 65.3 on n=49 and 25-34 at 44.6 on n=74. It should not be used as evidence of a trend until the final figure is released (expected 2026-10-06).
- **Category / label.** OBSERVED FACT for the values and status (KNOWN). INFERENCE for "flat" and "not usable" (INFERRED).
- **Confidence.** High on "flat Apr–Jul" and on "August is preliminary and small-sample". Moderate on whether the final August figure will come in lower: that is a PREDICTION, and it is UNKNOWN (U-04).
- **Evidence.** F-11, F-12, F-13, F-14; K-11, K-13.
- **What would falsify it.** A final August (released 2026-10-06) near or above ~34 on the full sample, followed by September/October FINAL values above ~33, would establish a real post-July rise that this conclusion does not anticipate.

### C-3 — Who is driving it: no consumer segment can be shown to drive a real change; the measured step is broad-based across ages

- **Claim.** The step from the pre-period to Apr–Jul appears in every age group (+2.5 to +4.9 pts). For ages 25+, it is fully accounted for by the bridge design effect (residuals −2.6 to −0.2 under their own-cell adjustments; −1.1 to −0.5 under the pooled adjustment). 18-24 shows the largest raw step (+4.9). Whether any of that is real is CONFLICTED: +1.3 under a common design effect and +6.3 under the 18-24 bridge cell, and neither is distinguishable from zero because the bridge cannot resolve age-specific design effects (p=0.57). Even the high 18-24 figure would move the topline by only about 0.8 pts. The data do **not** support "younger shoppers are driving it". Age is the only segment dimension available in the authorized data.
- **Category / label.** INFERENCE. INFERRED for 25+; CONFLICTED for 18-24; UNKNOWN for all non-age segments.
- **Confidence.** High that no segment explains the topline jump as a behavioral change. Low on whether 18-24 has any real rise.
- **Evidence.** F-15, F-16, F-17, F-18, F-19, F-20, F-29; K-06, K-07, K-14, K-16.
- **What would falsify it.** (i) A larger bridge or Methods adjustment showing an 18-24 design effect near or below zero, combined with continued 18-24 values above ~44 in FINAL months. That would make a real young-adult rise of about 5+ pts likely, though still worth under 1 topline point. (ii) A Methods breakdown by non-age segments showing a concentrated change in one segment beyond design-effect expectations.

### C-4 — December expectation: about 31–32% on the published basis, not a continued climb toward 40%

- **Claim.** Assuming no further methodology change and no official re-basing, the published (online-panel basis) December 2026 figure is expected to be about **31.6%** (method A), with an 80% prediction interval of about **30–33%** and a 95% interval of about 29–34%. Alternative reasonable methods give 31.0 (flat carry-forward) to 33.2 (legacy trend plus bridge mode effect, 80% PI 30.8–35.5). A seasonal-December allowance based on only two prior Decembers gives 32.8. On a legacy-comparable basis, the expectation is about **28%**, which is close to Dec-2025's 28.7.
- **Method A (primary).** Take the Apr–Jul 2026 mean (30.95) and add the legacy OLS slope (0.10 pts/month) × 6.5 months, with residual SD 1.09 and propagated slope uncertainty (K-17). It uses only FINAL online-basis months and the pre-existing trend rate. It excludes the August preliminary (F-12) and March (the first new-design month, which may be atypical; F-21).
- **Category / label.** PREDICTION / INFERRED (conditional).
- **Confidence.** Moderate. The interval reflects sampling noise and trend uncertainty. It does **not** include the risk of an official series adjustment (U-02), a changing mode effect (U-03), or a real market shift after July.
- **Evidence.** F-08, F-10, F-11, F-27, F-28; K-10, K-11, K-17.
- **What would falsify it.** FINAL values for Sep–Nov consistently above ~33.5 or below ~29.5, or a final December outside 29–34. If Methods re-bases the series, this forecast has to be restated on the new basis rather than counted as falsified.

### C-5 — The Harlow Market promotion cannot be shown, from authorized evidence, to have moved the measure

- **Claim.** The digest reports that Harlow launched free same-day delivery on 2026-03-03, in the same month as the fieldwork transition. The tracker alone cannot separate the two. After removing the bridge design effect, no real rise remains (C-1), and there is no evidence of a build-up through the year (C-2). A small Harlow-related effect (≤ ~2 pts, or a short-lived March bump) is not excluded. The "Harlow effect" in the digest is a team opinion (QUARANTINE for this claim), not a finding. It should not be presented as the explanation.
- **Category / label.** INFERENCE / INFERRED. That the event happened is UNKNOWN (LEAD source only).
- **Confidence.** Moderate-high that Harlow is not the main explanation of the jump. Low on whether it had any effect at all.
- **Evidence.** F-21, F-22, F-23, F-24; C-1.
- **What would falsify it.** A de-confounded measurement, for example a regional breakdown (Harlow footprint vs non-footprint) via a Methods data request, showing a real rise concentrated where Harlow delivery launched.

---

## c. Conclusions considered and NOT proposed

| ID | Tempting conclusion | Why not proposed |
|---|---|---|
| NP-1 | "The March jump is the Harlow effect: free delivery drove a 4-pt rise in online intent." | It is confounded with the fieldwork switch in the same month (F-23), and the bridge design effect accounts for about 86% of the jump and the whole multi-month step (F-04, F-07). The only source for it is a QUARANTINE opinion and unsourced LEAD commentary (F-22, F-24). Presenting it would promote an unsupported inference to fact (J-0001). |
| NP-2 | "Younger shoppers (18-24) are driving the increase." | The 18-24 Mar jump (+10) is within this cell's volatility (2.5 SDs of month-to-month change; F-19). Its real component is CONFLICTED and not distinguishable from zero (F-17). Its maximum topline contribution is about 0.8 of the 3–4 pts (F-18). All ages moved (F-15). The August 65.3 is n=49 preliminary (F-13). |
| NP-3 | "The measure is still climbing: 29 → 33 → 36." | Apr–Jul are flat (F-11). August is a preliminary partial sample (F-12, F-13). |
| NP-4 | "By December it will be ~38–40%" (extrapolating Feb→Aug or Jul→Aug). | It rests on the methodology step and an unreliable preliminary point. Neither is a trend in behavior. The flat FINAL data and the legacy trend rate imply about 31–32 (C-4). |
| NP-5 | "Online grocery intent rose about 3–4 pts year over year." | The raw YoY (+4.2) crosses the design change. Mode-adjusted YoY is +0.6, consistent with the pre-existing trend of about 1.1–1.2/yr (F-08). |
| NP-6 | "March is a seasonal high." | Prior Feb→Mar changes were +1.2 and +0.5 (F-06). |
| NP-7 | "The online panel is more accurate, so the 'true' level was always ~31%." (or the reverse, "the legacy design was right") | The bridge measures the *difference* between designs, not which one is closer to true intent. Which is more valid is UNKNOWN (U-07). The conclusions above therefore talk about comparability, not accuracy. |
| NP-8 | "There has been no change at all in consumer behavior." (stated as fact) | Too strong. The residual CI runs to about +2.2 pts (F-07). Proposed instead: "no detectable change". |
| NP-9 | "The March-only spike above Apr–Jul (≈2 pts) is a real short-lived promotion effect." | It is 1.8–2.0 noise SDs, and it is also the first new-design month (F-21). The cause is UNKNOWN. |
| NP-10 | Using the restricted respondent extract to break the jump down by other segments or to test the Harlow hypothesis. | Not authorized under the grant (not even in aggregate). It was not opened. The correct route is a Methods data request (U-06). |
| NP-11 | "Competitor fee cuts in April sustained the higher level." | The source is LEAD only ("selected metros", unsourced). The higher level is accounted for by the design effect, so no additional cause is needed or tested. |

---

## d. Unknowns and what would resolve each

| ID | Unknown | Why it matters | What would resolve it |
|---|---|---|---|
| U-01 | True size of the design (mode/panel) effect. Bridge: 3.6, 95% CI 1.0–6.2. Using the published Feb figure as the anchor implies about 2.2 (F-26). | It sets how much of the jump is artifact, and the legacy-equivalent level. | The Methods team's adjustment evaluation (methodology_notes 2026-03). An additional bridge wave. Ask Methods for the bridge weighting and SEs. |
| U-02 | Whether Methods will officially adjust or re-base the published series, and when. | The December number and the historical chart the deck shows would change basis. | Ask the Methods team (they are "evaluating whether an adjustment is required"). |
| U-03 | Whether the design effect is stable after Feb-2026 (for example, panel conditioning or attrition in a new panel). | F-09/F-10 and C-4 assume stability. | A repeat bridge, or Methods monitoring of panel tenure effects. |
| U-04 | The final August figure. | It confirms or refutes the preliminary 36.3. | Final close, expected 2026-10-06 (methodology_notes 2026-08). |
| U-05 | Whether the bridge arms were weighted like the tracker and drawn from comparable frames. | Comparability of the bridge estimate with the published series. | The Methods bridge documentation. |
| U-06 | Changes in segments other than age (region/Harlow footprint, income, household, urbanicity). | "Who is driving it" beyond age. Also a de-confounded test of Harlow (C-5). | A Methods data request (~10 business days per ACCESS_POLICY). Not the restricted file. |
| U-07 | Which design better reflects true behavior. | Whether ~28 or ~31 is the "real" level to communicate. | Out of scope for this data. Methods judgment and external validation (for example, behavioral purchase data). |
| U-08 | Age-specific design effects, especially 18-24 (bridge cell SE 4.1). | Whether young adults show a real rise (F-17 CONFLICTED). | A larger bridge sample for 18-24, or a pooled multi-wave estimate from Methods. |
| U-09 | Whether the digest's market events occurred as described (Harlow 2026-03-03 launch; April fee cuts). | Context only; not needed for C-1..C-4. | The original sources (Harlow announcement, trade press). Not available in the data room. |
| U-10 | Design effect of weighting on SEs. | The width of CIs and PIs. | The Methods team's weighting efficiency statistics. The empirical residual SD (1.09 vs SRS 0.89) suggests about 1.2× (INFERRED). |
| U-11 | **USER_CONFIRMATION_REQUIRED:** Which basis should the Q4 deck present: published (online-panel, unadjusted), legacy-equivalent, or both with a break marker? | It is material to the representation (J-0002): the headline December number is ~31.6 vs ~28.0, and the "jump" narrative changes. | The user's decision, possibly after consulting Methods (U-02). The Analyst's recommendation for the Magistrate's consideration is to show the published series with an explicit break at 2026-03 plus the bridge-adjusted line. |

---

## Private steps not performed (this office)

- Librarian `classify_source_admissibility`: not available; not run. A manual substitute is in EVIDENCE_REGISTER.json.
- `atlas_gov.independent_verification`: not available; not run. Nothing here is labeled VERIFIED. analysis.py output is at most REPRODUCIBLE by rerun, and rerunning it is reproduction, not verification (O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION §3, §6).
- Magistrate engine / fail-closed gate: not available. Disposition is for the separately instantiated Magistrate.
- `verify.py` current-law check: not run. The law applied is the repository copy. Its currency is UNKNOWN.

## Authority

External actions taken: none. No messages, posts, issues, PRs, or commits.

## Status

PENDING — Challenger review, then Magistrate determination. The Analyst does not certify this Argument (Art. XIV §1).
