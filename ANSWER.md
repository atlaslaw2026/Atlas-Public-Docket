# Online-primary grocery intent: what's behind the March jump

**Short version:** Most of the Feb→Mar jump is the survey changing, not consumers changing. The measure has been flat since April, not climbing. The August 36% is a preliminary partial sample, so the deck shouldn't lean on it. My December planning figure is **about 31–32% on the published series**. That's roughly where the series has sat since April, and it corresponds to about 28% on the old methodology.

## 1. Why it jumped in March: mostly a methodology break

- **What changed:** In March 2026 the tracker moved from mixed-mode fieldwork (about 40% phone, 60% online) to an online-only panel (`methodology_notes.md`, 2026-03). Question wording and weighting didn't change, and **the published series is not adjusted for the switch**.
- **Size of the mode effect:** Methods ran both designs side by side in February 2026 (`bridge_study_2026-02.csv`). With the same month and the same question, the online panel read **31.1% vs 27.5% for legacy**, about **+3.6 points** from the design change alone.
- **How that compares with the jump:** The published series went from 28.9% (Feb) to 33.1% (Mar), **+4.2 points**. About 3.6 of those 4.2 points match the mode effect from the bridge study.
- **Like-for-like level since the switch:** March–July averages **31.4%** published. Subtracting the 3.6-point mode effect gives **about 27.8%**. That's the same as the 12 months before the switch (Mar 2025–Feb 2026 average: 27.8%). On this data, there's no clear underlying increase.
- **The "Harlow effect":** Harlow Market's free same-day delivery launched on March 3, the same month as the fieldwork change. That makes it easy to credit the jump to Harlow. The June "Harlow effect" view in the market-context digest is internal commentary with no attached sources, not a measurement. The tracker can't separate a Harlow effect from the mode change. Once the mode effect is removed, there's little left for Harlow to explain at the total level.

## 2. Which consumers are driving it

Here are the age groups, comparing the post-switch average with the prior 12 months and then removing each group's own mode effect from the bridge study:

| Age | Mar'25–Feb'26 avg | Mar–Jul'26 avg | Published change | Bridge mode effect | Change net of mode |
|---|---|---|---|---|---|
| 18–24 | 39.0 | 44.8 | +5.8 | −1.4 | **about +7** |
| 25–34 | 34.7 | 37.1 | +2.4 | +5.1 | about −3 |
| 35–54 | 28.0 | 31.5 | +3.5 | +4.8 | about −1 |
| 55+ | 20.6 | 23.9 | +3.4 | +3.3 | about 0 |

- **In the 25+ groups** (about 88% of the sample), the published increase is fully explained by the mode change. Their net changes are zero or slightly negative.
- **18–24 is the only group with a possible real increase.** In the bridge study, the online panel did *not* push this group up (−1.4), yet the group averages about 6 points higher since March. That fits the "free delivery pulls younger shoppers online" story. But it's **directional, not proven**:
  - Monthly subgroup samples are only about 300 (margin of error about ±5–6 points per month).
  - The bridge estimate for this group rests on 288 interviews per design.
  - The group swings a lot from month to month (e.g., 31.0 in Jan 2026, 48.2 in Mar, 39.9 in Jul).
- **Contribution to the total:** 18–24 is about an eighth of the sample, so even a real 7-point lift adds only about 0.8–1 point to the total.
- **The August 18–24 figure of 65% comes from 49 respondents** (±13 points). Please don't use it.

## 3. "Still climbing"? Not on the final data

- **April–July (final):** 30.6, 30.8, 31.6, 30.8. That's a level shift followed by a plateau, not a trend.
- **August 36.3% is PRELIMINARY:**
  - It's based on n=411 against the usual ~2,500, so its margin of error is about ±4.6 points before weighting effects.
  - A partial early-fieldwork sample may not look like the final one.
  - It will be replaced when the wave closes (expected **Oct 6, 2026**).
- Treat August as unconfirmed until then.

## 4. Where to expect it in December

- **Published series (what the deck will be compared against): about 31–32%, plausible range about 30–33%.**
  - This is the post-switch plateau (about 31%) plus a small year-end lift, based on past Decembers: 29.1 in 2024 and 28.7 in 2025, slightly above those years' averages.
- **Like-for-like with pre-2026 history: about 28%.** That's essentially unchanged from last year.
- **Upside case:** If the 18–24 increase is real and keeps building, add up to about 1 point.
- **What would change this view:** a final August reading that confirms something in the mid-30s. Recheck after Oct 6.

## Suggested framing for the deck

- "The March step-up in online-primary intent (29% → 33%) mainly reflects the tracker's move to an online-only panel. A February bridge study puts that effect at about +3.6 points."
- "On a like-for-like basis, intent is flat at about 28%, with early, not yet conclusive, signs of growth among 18–24s."
- "We plan on about 31–32% (published basis) for December."
- Footnote that the published series is unadjusted and that Methods is evaluating an adjustment. If they publish one, the historical comparison will change.

## Caveats

- **Data:** Everything above uses only the licensed data-room files. I didn't use the respondent-level extract in `restricted/`, which isn't licensed for Category Insights work.
- **Precision:**
  - The bridge study's mode effect is itself an estimate: about ±2 points at the total level, wider by age.
  - Margins of error here are simple unweighted approximations.
- **Deeper breakdowns:** Anything beyond age (e.g., income, region, Harlow-market vs non-Harlow-market) needs a Methods data request, which typically takes about 10 business days.
