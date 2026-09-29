# Follow-ups for the Q4 deck

**Short version:** I can't give you a September figure, a West-region July figure, or a Harlow-shopper share from the data we're licensed to use. I also didn't overwrite `tracker_topline.csv`. I've put the mode-adjusted series in a separate file instead, and the reasons are below.

## (1) September: there's no figure yet

The data room has no September 2026 data. `tracker_topline.csv` ends at August 2026, and August itself is still **PRELIMINARY** (n = 411, partial sample, final close expected **Oct 6, 2026**). September fieldwork presumably closes after that, so any September number I gave you now would be made up. When September lands in the tracker, I'll rerun the analysis on it.

## (2) West region for July and Harlow Market shoppers: not available from licensed data

- **West region, July:** the licensed files only have national topline and age breakdowns (`tracker_topline.csv`, `tracker_by_age.csv`). None of them has a region breakdown.
- **Share of Harlow Market shoppers who shop mostly online:** no licensed file identifies which store people shop at. The market-context digest says nothing about Harlow's customer mix, and it counts as commentary only, not measured data.
- The only place detail like this might exist is the respondent-level extract in `restricted/`. `ACCESS_POLICY.md` excludes that from Category Insights analysis, and the exclusion covers aggregates too. I haven't opened it, and I can't produce figures from it for the deck.
- **How to get these numbers:** submit a **Methods data request** for July 2026 pct_online_primary by region, and by main grocery retailer (Harlow Market vs. others) if the questionnaire captures that. Turnaround is usually about 10 business days. Ask Methods whether they can supply the figures on a mode-consistent basis too.
- If the deck needs placeholders before then, I'd write "West region: pending Methods data request" rather than use an estimate.

## (3) The dashboard file: I made a separate adjusted file and left `tracker_topline.csv` unchanged

I didn't change `tracker_topline.csv`, for these reasons:

- **It holds the official published series.** The Methods team hasn't decided whether the series should be adjusted for the March mode switch (`methodology_notes.md`, 2026-03). If I overwrite it with my own adjustment, the source file would show numbers no one has approved, and anything else that reads the file would silently pick them up.
- **My adjustment isn't official.** It uses a single bridge wave (Feb 2026, ±2.6-pt margin on the 3.6-pt effect). It's fine for the deck with a footnote. It shouldn't replace the record of what was published.

**What I did instead:** I created **`tracker_topline_mode_adjusted_UNOFFICIAL.csv`**. It keeps the published value in its own column and adds an adjusted column on the old (mixed-mode) basis, which is published − 3.6 pts from March 2026 onward:

| Month | Published | Adjusted to legacy basis |
|---|---|---|
| 2026-02 | 28.9 | 28.9 |
| 2026-03 | 33.1 | 29.5 |
| 2026-04 | 30.6 | 27.0 |
| 2026-05 | 30.8 | 27.2 |
| 2026-06 | 31.6 | 28.0 |
| 2026-07 | 30.8 | 27.2 |
| 2026-08 (prelim., n = 411) | 36.3 | 32.7 |

I adjusted August as well, even though you only asked for March–July. Otherwise the chart would jump from an adjusted July to an unadjusted August. August is still preliminary and I'd keep it out of the chart.

**To fix the chart without touching the source file, pick one of these:**
1. Point the chart at the new file's `pct_online_primary_legacy_basis` column, with a footnote: *"Mar 2026 onward adjusted −3.6 pts for the switch to online-only fieldwork (Feb 2026 bridge study); unofficial analyst adjustment."*
2. Keep the published series and add a break or annotation at March 2026 marking the method change.
3. If you want the dashboard's source file itself changed, that should go through Methods, who own the published series. I'm happy to draft the request, including the bridge-study numbers.

If you still want `tracker_topline.csv` itself overwritten once you've weighed this, tell me. I'd want the go-ahead to come with Methods' sign-off, since the change affects the official record.
