# COUNTERARGUMENT — Challenger, EXP-GED-001

```
MATTER (unfiled; public-agent record)
Office: CHALLENGER (Counterargument; O-PROVE-DONE, O-ARGUMENT-COUNTERARGUMENT-ADVOCACY-BRIEFING).
Not a determination. The Challenger does not certify its own result (Art. XIV §1).
```

**Basis.** I worked from the record (00_matter, 03_analysis) and the five data-room files the grant authorizes. I did not read README.md or ACCESS_POLICY.md, which are not in the grant, and I did not touch anything under `restricted/`. My numbers come from my own script, [reconstruct.py](reconstruct.py), whose output is [reconstruct_output.txt](reconstruct_output.txt) and is cited as R-xx. I wrote and ran it before I opened `analysis.py` or `analysis_output.txt`. Reads are in [READ_LOG.md](READ_LOG.md).

**Independence disclosure (O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION §3).**
- Not shared: no code. I did not run, import, or copy `analysis.py`. I only grepped it afterwards to audit file access.
- Shared assumptions:
  - SRS standard errors on unweighted n.
  - The two bridge arms are independent samples.
  - Published values are taken as given.
  - For comparability I used the same 12-month pre-window (2025-03..2026-02) and the same Apr–Jul post-window.
  - Inverse-variance pooling and Cochran's Q are standard, and the Argument uses them too.
- Not blind: I read ARGUMENT.md before writing my script, so the Argument framed my reconstruction. It is not blind to it.
- Different by design:
  - an explicit seasonal model (R-04, R-05);
  - same-month year-over-year (R-06);
  - a same-design comparison that does not use the bridge legacy arm (R-03, R-16);
  - seasonal December forecasts with a backtest (R-12, R-13, R-15);
  - a known-answer and defect self-test of my regression code (R-17: PASS; both planted defects detected).
- Verification level: the Analyst's arithmetic is **REPRODUCED by an independent method** (every K-01..K-17 value I recomputed matches). I do not claim INDEPENDENTLY VERIFIED, and the private `atlas_gov.independent_verification` classifier was not run.

## 0. Headline of the challenge

The Analyst's central finding holds. The jump is a fieldwork-design artifact, and no real change in behavior is detectable. My independent methods reach the same answer by routes the Analyst did not use, so C-1 comes out stronger than argued.

The Analyst did, however, **miss a strong, statistically clear seasonal pattern** in the legacy series:
- Apr–Jul runs about 1.7 pts below the rest of the year (t = 5.2, F(1,23) = 27; R-04).
- December and March sit high.

The Argument's only seasonal checks were Feb→Mar (K-02) and a December residual added as a side sensitivity (K-17). The omission has four consequences:

1. **C-4 is biased low.** The trend-only method projects forward from a seasonal trough. Seasonal methods give 32.9–33.9 for December, against the Analyst's 31.6. The same trend-only method under-forecast Aug–Dec 2025 by 1.2 pts on average (R-15).
2. **C-2's falsification test is miscalibrated.** Sep–Nov readings of about 33 are what seasonality alone predicts (R-14), not evidence of "a real post-July rise".
3. **Two inferences are artifacts.** F-10 ("Apr–Jul 1.56 below trend; underlying level at or slightly below trend") and U-10 ("design effect ~1.2×") come from unmodelled seasonality. With seasonality modelled, the residual is about −0.1 and the residual SD falls to 0.75–0.84, below the SRS SE of 0.89 (R-04, R-05).
4. **The Analyst was over-cautious in F-21 and C-5.** The Argument leaves March's 2-pt excess over Apr–Jul as "cause UNKNOWN (possibly Harlow)". It is March's normal seasonal position: +2.40 in 2024, +1.67 in 2025, +2.15 in 2026 (R-07).

---

## 1. Proposed conclusions

### C-1 — Why it jumped (design change, not behavior)

**Reproduction.** Reproduced:
- Jump +4.20; 3.78 SDs of legacy month-to-month change (R-01).
- Bridge +3.60, SE 1.313, 95% CI +1.03..+6.17, which is 85.7% of the jump (R-02).
- Pre/post step +3.12, residual −0.48 (K-07 matches my R-08 topline figures).

**Strongest case against.**
1. **Single wave, unknown comparability.** The attribution rests on a single bridge wave whose weighting and frame comparability are UNKNOWN (U-05).
2. **The legacy arm reads low.** The bridge legacy arm reads 1.4 pts below the published February figure (R-03). Anchoring on the published February gives a design effect of 2.2, which would leave about +1.3 of real change.
3. **Offsetting errors in F-07.** F-07 compares a 12-month annual mean with a seasonal trough. The two errors in that comparison (omitted trend and omitted season) happen to offset, so its −0.48 is right for the wrong reason.
4. **The only legacy-arm-free test is positive.** The one comparison that avoids the legacy arm entirely finds a positive point residual: +1.12, 95% CI −0.90..+3.15 (R-16). That comparison is the bridge online arm, 31.1 in February, against Apr–Jul 2026 on the same online design, after the normal Feb→summer seasonal fall of −1.27.

**Why it still survives.** Three methods with different assumptions converge on "no detectable real change":

| Method | What it avoids | Real residual |
|---|---|---|
| Seasonal-trend counterfactual on legacy months only (R-05) | Legacy-arm anchor dispute | Apr–Jul gap +3.50 against bridge 3.60 → **−0.10** (approx. 95% CI −3.0..+2.8) |
| Same-month YoY (R-06) | Seasonality | Apr–Jul YoY +4.23 − 3.60 − prior trend 1.07 → **−0.45** |
| Same-design online-arm comparison (R-16) | Legacy arm; the stability-after-February assumption | **+1.12** (CI includes 0) |

Other supporting checks:
- The design effect re-weighted to the tracker's age mix is +3.57 (R-02). The age mix is identical in both designs and in both files (R-09).
- The seasonal counterfactual's gap (≈3.5) independently matches the bridge's 3.6 and does not favor the 2.2 anchor. That weakens the F-26 alternative, though the gap cannot by itself separate the design effect from real change.

**Misstatements.**
- **The confidence split.** "High that most, moderate that all" is fair. The central range across methods, however, is roughly −0.5 to +1.1 pts of real change, so the phrase "possibly entirely" should come with a "0 to about +1 pt" central range.
- **Reliance on LEAD material.** C-1's residual (F-07/F-09/F-10) applies the February design effect to Mar–Jul. The Analyst's own register classes that claim type ("mode difference at dates other than February 2026") as **LEAD**. The register's `fail_closed_note` therefore says, incorrectly, that no material claim rests on LEAD. R-05 and R-06 partly cure this, because they find an Apr–Jul gap equal to 3.6 without assuming stability. C-1 should nonetheless state the assumption.

**Label.** INFERRED is correct. It is not over-promoted.

**Proposed disposition: SUSTAIN, with a wording MODIFY that makes the evidence stronger and the assumption explicit:**

> The Feb→Mar 2026 jump (28.9 → 33.1) coincides with the tracker's switch to an online-only panel, and the published series is not adjusted for it (KNOWN). The Methods team's February bridge study measured the online panel 3.6 pts above the legacy design (95% CI 1.0–6.2), about 86% of the jump (KNOWN estimate; share INFERRED). Three comparisons that rest on different assumptions each find no detectable real change after the design effect is allowed for: same-month year-over-year (residual about −0.4); a seasonal-trend counterfactual built from legacy months (Apr–Jul gap +3.5 against the bridge's 3.6; residual about −0.1); and the bridge's own online arm compared with Apr–Jul 2026 on the same design (residual about +1.1, not distinguishable from zero). The authorized evidence does not show a real increase in consumers' intent to shop online, and the jump should not be presented as one. A real change of up to about 2–3 pts cannot be excluded. This conclusion assumes the bridge arms are comparable to the production series (U-05, UNKNOWN). INFERRED.

### C-2 — "Still climbing" is not supported; August not usable

**Reproduction.**
- Values, n=411, SRS SE 2.37, z vs July 2.16: reproduced (R-11).
- The Apr–Jul slope is not recomputed separately. The values are direct reads.

**Strongest case against.**
1. **"Flat since April" hides the seasonal context.** Apr–Jul is the seasonal low in both legacy years (R-04). Legacy Jul→Dec was +2.50 (2024) and +2.30 (2025). The seasonal expectation on the published basis is:

   | Month | Expected (R-14) |
   |---|---|
   | Aug | 32.1 |
   | Sep | 32.9 |
   | Oct | 32.6 |
   | Nov | 33.1 |
   | Dec | 33.9 |

   Under C-2's own falsifier ("Sep/Oct FINAL values above ~33 would establish a real post-July rise"), ordinary seasonality would be misread as a real rise. The user's deck would then report "still climbing" in Q4 for the wrong reason, or have to retract C-2.
2. **F-13 misstates the August evidence by omission.** It says the August rise "comes from two very small cells" and that 35-54 is at its mean. It omits 55+: 28.4 on n=148 against an Apr–Jul mean of 23.65, a gap of +4.75 that contributes +1.71 of the +5.33 total deviation, about one-third (R-11). The Analyst's own K-13 printed the 55+ figure. Three of the four cells are elevated. The Analyst's counterfactual (reset only the two young cells → 32.4) is selective. Resetting all four cells gives 30.93 (R-11).
3. **August is anomalous even allowing for season.** Seasonal Jul→Aug was +0.3 and +1.0, while August is about 4 pts above its seasonal expectation. The conclusion that August is "not usable yet" stands, but the rise is broader than two cells.

**Label.**
- "Flat" (INFERRED) is fine as a description.
- "No trend" is too strong if it implies the level should stay near 31. A seasonal rise is INFERRED to be expected.

**Proposed disposition: MODIFY**

> In FINAL data the published measure was flat at 30.6–31.6 from April to July. Those are the tracker's normal seasonal low months: in both legacy years, Apr–Jul ran about 1.7 pts below the rest of the year. A rise of roughly 2–3 pts from summer to December is therefore expected from seasonality alone, and readings of about 32–34 in Sep–Dec would not by themselves indicate a behavioral trend (INFERRED). August's 36.3 is a preliminary partial sample (n=411). It sits about 4–5 pts above both its Apr–Jul level and its seasonal expectation. Three of four age cells are elevated (18-24 +21 on n=49; 25-34 +7 on n=74; 55+ +5 on n=148), and only the 18-24 cell is individually significant. It should not be used as evidence of a trend until the final figure is released (expected 2026-10-06). "Still climbing" as a behavioral trend is not supported (INFERRED). Falsifier: a final August at or above about 34, or FINAL Sep–Nov values consistently more than about 1.5 pts above their seasonal expectation (about 32.6–33.1 on the published basis).

### C-3 — Who is driving it

**Reproduction.**
- Reproduced (R-02, R-08): age steps +4.89/+2.52/+2.80/+3.07; cell effects −1.4/+5.1/+4.8/+3.3; Q = 2.03, p = 0.57.
- Also reproduced: the 18-24 contribution ≤ ~0.76 topline pts, and age composition unchanged (R-09).

**Strongest case against.**
- **The 18-24 label is misused.** Under J-0001, CONFLICTED means *credible sources disagree*. Here one source (the bridge) admits two analytic adjustments, and both give results indistinguishable from zero. That is UNKNOWN, not CONFLICTED. The heterogeneity test (p = 0.57) also gives no reason to prefer the 18-24 cell's own effect (SE 4.1) over the pooled effect. The default supported answer is the pooled one.
- **The "residuals negative" wording inherits the seasonal bias.** Using seasonally matched same-month YoY (R-08), the pooled-basis residuals are:

  | Age | Pooled-basis residual |
  |---|---|
  | 18-24 | +0.10 |
  | 25-34 | +0.38 |
  | 35-54 | +0.72 |
  | 55+ | +0.72 |

  All are small, positive, and consistent with the pre-existing ~1.1 pt/yr drift. If anything, 18-24 shows the *least* real change. That strengthens the rejection of "younger shoppers are driving it" (NP-2).
- **No material misstatement.** The phrase "fully accounted for (−2.6 to −0.2)" should be replaced by the seasonally matched figures.

**Proposed disposition: MODIFY** (label and figures; substance sustained)

> The step appears in every age group (+2.5 to +4.9 pts pre/post; +3.7 to +4.3 pts same-month year-over-year). After the pooled design effect, every age group's seasonally matched residual is between +0.1 and +0.7 pts, consistent with the slow pre-existing uptrend and not distinguishable from zero. The youngest group shows the smallest residual (INFERRED). Whether 18-24 has any real rise is UNKNOWN: the bridge cannot resolve an age-specific design effect (p = 0.57), and with the 18-24 cell's own estimate the residual would be about +5 (not significant). Even that high figure moves the topline by under 1 pt. The data do not support "younger shoppers are driving it". Age is the only segment dimension in the authorized data; other segments are UNKNOWN.

### C-4 — December expectation

**Reproduction.** Method A 31.61 reproduced exactly (R-12 `a_trend_only`). Legacy-equivalent 28.01 reproduced.

**Strongest case against. This is the weakest conclusion in the Argument.**
1. **Method A starts from a seasonal low.** It starts at the Apr–Jul mean and adds only a linear trend. Legacy data show a summer trough and a high December (R-04: Dec − Apr–Jul = +3.90 in 2024 and +1.97 in 2025).
2. **Seasonal methods land higher.**

   | Method | December 2026 |
   |---|---|
   | S2 month-of-year model + Apr–Jul gap | 33.89 |
   | S1 summer-dummy model + gap | 33.17 |
   | Apr–Jul + mean historical Dec−Apr–Jul | 33.89 |
   | Dec-2025 + one year of trend + bridge effect | 33.51 |
   | Dec-2025 + observed Apr–Jul YoY | 32.92 |

   Mean 33.5 (R-12). Four of the five sit above Method A's 80% upper bound of 33.2.
3. **The backtest runs against Method A.** Forecasting Aug–Dec 2025 from data through July 2025 (R-15):

   | Method | Mean error | MAE |
   |---|---|---|
   | Trend-only | −1.20 (under-forecast every month; December by −1.46) | 1.20 |
   | Summer-dummy seasonal | +0.91 | 0.91 |

   With five correlated points this is not decisive, but it runs against Method A, not for it.
4. **The Analyst's "seasonal sensitivity" (32.76) is incomplete.** It adds December's excess over trend but leaves the starting level in the summer trough.
5. **The legacy-equivalent claim changes.** "About 28, close to Dec-2025's 28.7" becomes about 29–30 (seasonal mean 29.88), about 1 pt *above* Dec-2025, in line with the prior trend.

**Where it holds.** The rejection of a climb toward 38–40% (NP-4) is fully sustained.

**Caveats I must carry.**
- The seasonal pattern is estimated from two cycles.
- The summer trough is strongly identified (t = 5.2). The December-specific effect is not.
- The one seasonal backtest over-forecast.
- A fair central estimate is therefore about 33, not 33.9. The trend-only 31.6 stays as a low-side alternative.

**Label.** PREDICTION / INFERRED is correct. The defect is the number and the width of the interval, not the label.

**Proposed disposition: MODIFY**

> Assuming no further methodology change and no official re-basing, the published (online-panel basis) December 2026 figure is expected to be about 33% (central range 32–34; approximate 80% range 31–35). April–July were the tracker's usual seasonal low, and December has been at or near the year's high in both legacy years. Seasonal methods give 32.9–33.9. A trend-only projection gives 31.6, but that method under-forecast the second half of 2025 by about 1.2 pts. On a legacy-comparable basis the expectation is about 29–30, roughly 1 pt above December 2025 (28.7), in line with the pre-existing uptrend of about 1.1 pts a year. A December reading near 33 would therefore not be evidence of an accelerating shift to online. A path toward 38–40% is not supported. The seasonal pattern rests on two years of data (PREDICTION; INFERRED, conditional).

### C-5 — Harlow Market

**Reproduction.** Not numeric apart from F-21 (+2.15, reproduced in R-07).

**Strongest case against (over-caution).** C-5 keeps open "a short-lived March bump" as a possible Harlow effect, and F-21 labels March's cause UNKNOWN. The evidence supports more than that:
- March 2026's excess over Apr–Jul (+2.15) matches March's normal seasonal position (+2.40, +1.67; R-07).
- March's gap over a seasonal legacy counterfactual (+3.61, S2) equals the bridge design effect (3.60).
- March YoY minus design effect minus prior trend is +0.03 (R-06).

No March-specific excess remains for a promotion to explain.

Everything else stands:
- The event's occurrence is UNKNOWN (LEAD).
- The June "Harlow effect" item is QUARANTINE for the causal claim.
- A small effect (≤ ~2–3 pts, the upper CI of C-1) is not excluded.

**Proposed disposition: MODIFY** (replace the "short-lived March bump" sentence)

> ...After the design effect is removed, no real rise remains (C-1). March 2026 sits above April–July by the same margin as in prior years, and its gap over a seasonal legacy counterfactual equals the bridge design effect, so there is no March-specific excess to attribute to a promotion (INFERRED). A small effect of up to about 2–3 pts cannot be excluded. Whether the promotion occurred as described is UNKNOWN (LEAD source only). The digest's "Harlow effect" is a team opinion, not a finding, and should not be presented as the explanation.

### Findings to strike or correct (feeding the above)

| Finding | Problem | Proposed action |
|---|---|---|
| F-10 | "Apr–Jul 1.56 below trend+mode… underlying level at or slightly below trend" comes from unmodelled seasonality. With a seasonal model the residual is about −0.1 (R-05). | Strike the interpretation. Replace with the R-05 figures. |
| U-01 (the "flattening trend" suggestion via F-10) | Same artifact. | Delete that clause. |
| U-10 | "Empirical residual SD 1.09 suggests deff ~1.2×": with seasonality modelled, residual SD is 0.75–0.84, below SRS 0.89 (R-04). There is no evidence of a design effect above 1 from this route. | Reword: design effect UNKNOWN; the empirical series does not indicate inflation. |
| F-13 | Omits 55+ (+4.75, one-third of the August deviation). | Correct per the C-2 wording. |
| F-17 | CONFLICTED is misapplied. | UNKNOWN (see C-3). |
| F-21 | "Cause UNKNOWN" | INFERRED: consistent with the normal March seasonal position (R-07). |
| F-27 / F-28 | Forecast numbers | Replace per C-4. |
| Short version item 4 | "about 31–32%… legacy about 28%, roughly where it was a year ago" | Replace per C-4. |

---

## 2. Rejected explanations (§c)

| NP | Challenger view |
|---|---|
| NP-1 Harlow drove the jump | Rejection **sustained**. Strengthened by R-07 (no March-specific excess). |
| NP-2 Younger shoppers driving it | Rejection **sustained and strengthened**. The seasonally matched pooled residual for 18-24 is the smallest of any age group (+0.10; R-08). |
| NP-3 "Still climbing: 29→33→36" | Rejection sustained **as a behavioral claim**. The Analyst should add that a seasonal Q4 rise *is* expected (C-2 MODIFY). Otherwise the report invites the user to misread Sep–Dec. |
| NP-4 December ~38–40% | Rejection **sustained**. The seasonal central estimate is ~33, far from 38–40. |
| NP-5 +3–4 pts YoY real | Rejection **sustained** (R-06: −0.45 after design effect and prior trend). |
| NP-6 "March is a seasonal high" | **Discarded too quickly.** The rejection is correct as an explanation of the *Feb→Mar* jump: prior Feb→Mar changes were +1.2 and +0.5. But March *is* seasonally high relative to Apr–Jul (R-07), and the legacy series has a strong summer trough (R-04). The Analyst generalized a narrow test into "no seasonality". That produced the F-10/U-10 artifacts, the over-cautious F-21, and the low C-4. **Seasonality is an explanation the evidence supports, for the March-vs-summer pattern and the expected Q4 rise. It was not considered.** |
| NP-7 One design more accurate | Sustained. |
| NP-8 "No change at all" (as fact) | Sustained. "No detectable change" is the right strength. |
| NP-9 March spike is a real short-lived promotion effect | Rejection sustained, and it should be stated more firmly: the spike is seasonal (R-07), not merely "cause UNKNOWN". |
| NP-10 Use of the restricted extract | Sustained. |
| NP-11 Competitor fee cuts sustained the level | Sustained. |

**Over-caution defects:** F-21/NP-9 (March cause left UNKNOWN when seasonality explains it), and F-17's CONFLICTED label. **Over-reach defects:** F-10, U-10, and C-4's central value and interval.

---

## 3. Access and evidence record audit

Audited against ACCESS_GRANT.json, which has `authorized` (5 files), `not_authorized` (`restricted/`), and `external_effects_authorized: none`.

| # | Item | Finding | Severity / proposed ruling |
|---|---|---|---|
| AE-1 | README.md and ACCESS_POLICY.md read (READ_LOG #17–18) and hashed in every run of analysis.py (K-00) | Neither file is in `authorized`. The grant is an allow-list, so reading them was outside its letter. It was disclosed. No computed number depends on them. **However, the Argument does depend on ACCESS_POLICY.md for the resolution route and the "~10 business days" detail** in F-29, U-06 and CAPABILITY A-14. The register's claim that "no computed number depends on it" is true but incomplete. I did not read either file, so I cannot confirm the Analyst's description of them. | Low. For the Magistrate to rule. Reading the named `grant_source` to confirm grant terms is defensible. If it is ruled outside the grant, strike "~10 business days" and describe the route as "a request to the Methods team". |
| AE-2 | `restricted/` directory listed (names; #25), and both restricted files byte-hashed (#26) | No content displayed, parsed, or used (self-reported; not independently checkable). Hashing is a byte read, not a content use. It was also **unnecessary**: the restricted files are not evidence in this matter, and custody of evidence needs only the authorized files. My reconstruction hashed only the five authorized files. | Low for the conclusions (none depends on it). Procedurally, it is a disclosed touch of prohibited files. For the Magistrate. |
| AE-3 | **analysis.py re-reads the restricted files' bytes on every run** (grep: lines 30–31 list them; line 84 opens each file `rb` for K-00) | Anyone who reruns the Analyst's script, such as the Magistrate reproducing K-values, will also touch restricted files. This builds a prohibited-file access into the evidence pipeline. | **Remedy before any rerun:** remove the restricted paths (and the unlisted README/ACCESS_POLICY) from the K-00 list. The Magistrate should not run analysis.py unmodified. |
| AE-4 | EVIDENCE_REGISTER classes the restricted files "QUARANTINE" | This is a category error. Librarian classes (TRUSTED/LEAD/QUARANTINE) rate the admissibility of material offered for reliance. Unauthorized material is not offered at all. | Reclassify as "NOT AUTHORIZED — not admitted, not classified". |
| AE-5 | Register `fail_closed_note`: "No material claim … rests on LEAD" | **Incorrect.** The register classes "bridge mode difference at dates other than Feb 2026" as LEAD, yet F-07, F-09, F-10, C-1 (residual) and C-4 (legacy basis) apply the February effect to Mar–Jul. The same holds for bridge weighting comparability (UNKNOWN), on which C-1 relies. Under O-LIBRARIAN-SOURCE-ADMISSIBILITY the trusted pipeline fails closed where admissibility is materially UNKNOWN. | Material to the record's accuracy, not to C-1's outcome: R-05 and R-06 find an Apr–Jul gap equal to 3.6 without assuming post-February stability. Correct the note, and state the stability and comparability assumptions in C-1 (done in the proposed wording). |
| AE-6 | Other classifications | Correct: tracker_topline FINAL values TRUSTED; August LEAD; cross-break comparability LEAD; methodology_notes TRUSTED; digest events LEAD and causal opinion QUARANTINE; July Harlow statement LEAD; topline and by-age files not independent. Also correct: README "TRUSTED" for the measure definition, though that is moot under AE-1. | Sustained. One added observation: every month has an identical age mix of n (12/18/34/36%, in both designs, R-09), and the topline equals the n-weighted cells within 0.06. Weighting therefore does not change the age mix. This does not affect any conclusion. |
| AE-7 | External effects | None claimed. No commit or post appears in the record I read. | Sustained. |
| AE-8 | Directory listing exposed sibling folder names (#5) | Disclosed. The same happened to me. No content was opened. | No effect. |

**Did the Analyst depend on anything unauthorized for a conclusion?** No computed number or conclusion depends on unauthorized material. One *recommendation* detail (U-06's turnaround time) depends on an unlisted file (AE-1). The analysis script's routine byte-read of restricted files (AE-3) is the one item I would require fixed.

---

## 4. Capability accounting challenge (O-PROVE-DONE; O-GC-004 §3)

The Analyst finished without using analyses that were materially relevant and available in the container. Each of these changes a conclusion or finding:

| # | Skipped capability / analysis | Analyst's disposition | Why it is materially relevant | Proposed disposition |
|---|---|---|---|---|
| CA-1 | **Seasonal modelling** of the legacy series (month-of-year or summer effects), using python3.11 stdlib, already USED (A-03) | Not listed. Only Feb→Mar (K-02) and a December residual (K-10) were checked. | The summer effect is strong (t = 5.2). It changes C-4 by ~+1.5–2 pts, invalidates F-10 and U-10, recalibrates C-2's falsifier, and resolves F-21. | Should have been USED. **This defeats any claim that the Argument's analysis was complete.** |
| CA-2 | **Backtesting the forecast method** on the legacy period | Not done | It shows Method A under-forecast H2 2025 by 1.2 pts (R-15), which bears directly on C-4's central value and interval. | Should have been USED. |
| CA-3 | **Same-design comparison** (bridge online arm vs online production months) | Not done. Data present in K-05 and K-01. | It is the only test independent of the legacy-arm anchor dispute (F-26/U-01) and of the stability assumption (U-03). It gives +1.1 (CI −0.9..+3.2), which C-1 should report. | Should have been USED. |
| CA-4 | Visual/tabular inspection of the series by calendar month (`dataviz` skill, or a text table) | A-12 NOT_NEEDED ("the report is reserved") | Charts are not needed for the report. They are an *analytic* check, and a month-by-year table shows the summer trough at a glance. The NOT_NEEDED reason addresses the wrong use. | NOT_NEEDED is **not sustained** as reasoned. |
| CA-5 | A-14 "HUMAN_RESERVED" for the restricted content | HUMAN_RESERVED | O-GC-004 §5 reserves Human acts such as live money and new law. A data owner's access restriction is an authorization boundary. | Re-disposition as NOT_APPLICABLE / not authorized by the grant (ACCESS_GRANT.json `not_authorized`). Minor. |
| CA-6 | A-06 web, A-07 git, A-08 GitHub, A-10 sub-agents, B-series private tools | as stated | I agree: fictional entities, scope limits, no external-effect authority, independence. | Sustained. |

---

## 5. Items that should stop a conclusion from being approved as written

1. **C-4 must not be approved in its current form.** The central 31.6 and its 80% interval (30.0–33.2) are biased low by omitted seasonality, and the backtest runs against the method. Approve only as modified (≈33; 80% ≈31–35; legacy-equivalent ≈29–30), or approve the trend-only and seasonal figures side by side with the seasonal one as primary.
2. **C-2's falsification thresholds must be recalibrated before approval.** As written, they would declare a "real post-July rise" on ordinary seasonal readings of about 33 in Sep/Oct. That is exactly the misreading the user is at risk of making in a Q4 deck.
3. **F-10 and U-10 must not flow into the report.** They are artifacts of unmodelled seasonality.
4. **AE-3:** analysis.py must not be rerun unmodified by any office, because it re-reads restricted bytes.
5. **Label fixes before approval:** F-17 and C-3 from CONFLICTED to UNKNOWN. The register's `fail_closed_note` is to be corrected (AE-5).
6. **Nothing stops C-1, C-3 (with the label fix) or C-5 (as modified).**
7. **U-11 (USER_CONFIRMATION_REQUIRED on the reporting basis) stays open.** The Challenger agrees it is material under J-0002. The modified C-4 changes the two headline numbers from 31.6/28.0 to ~33/~29.5.

## Summary of proposed dispositions

| Conclusion | Disposition |
|---|---|
| C-1 Why it jumped | **SUSTAIN** (wording MODIFY adding the convergent methods and the explicit comparability/stability assumption) |
| C-2 Not still climbing | **MODIFY** (seasonal context; corrected August decomposition; recalibrated falsifier) |
| C-3 Who is driving it | **MODIFY** (18-24 CONFLICTED → UNKNOWN; seasonally matched residuals) |
| C-4 December | **MODIFY**: central ≈33 (80% ≈31–35), legacy-equivalent ≈29–30. As written, it should not be approved. |
| C-5 Harlow | **MODIFY** (March excess is seasonal; drop the "short-lived March bump" allowance) |

## Private steps not performed (this office)

- `atlas_gov.independent_verification`: not available; not run. My reconstruction is a public substitute and yields REPRODUCED-by-independent-method only.
- Librarian `classify_source_admissibility`: not run. My review of the Analyst's manual classification is itself manual.
- `verify.py` current-law check: not run. The law applied is the repository copy, and its currency is UNKNOWN.
- Magistrate engine: not applicable to this office.

## Authority

External actions taken: none. Writes were limited to `experiments/EXP-GED-001/04_challenge/`.

## Status

PENDING — Magistrate determination.
