# Follow-ups for the Q4 deck

**Short version:** I can't give you a September number or a West/Harlow number, because neither exists in the data we're licensed to use. I also didn't overwrite `tracker_topline.csv`. I put the mode-adjusted series in a new file you can point the chart at.

## 1. September

**There's no September figure yet.** The latest month in the tracker is August 2026, and it's still **PRELIMINARY** (n=411, a partial sample). Methods expects to close August on **Oct 6, 2026**, per `methodology_notes.md`. September hasn't been published, and the change log doesn't mention it at all. I'd rather leave it blank than estimate it and have it read as a reading. If the deck needs a placeholder, use "Sept: pending." The latest final month is **July, at 30.8% published (about 27.2% like-for-like)**.

## 2. West region (July) and Harlow Market shoppers

**I can't give you a single number for either one, and I haven't estimated one.**

- **Region:** The licensed files break the measure out by **age only** (`tracker_by_age.csv`). There's no region cut, so I have no West figure for July or any other month.
- **Harlow Market shoppers:** None of the licensed files identify which retailer respondents shop at. The tracker also doesn't measure "do most of their shopping online now." It measures *planned* online-primary shopping over the next three months. The market-context digest mentions Harlow, but it's internal commentary with no data behind it. Harlow's own statement ("well ahead of plan") gives no figures.
- The respondent-level extract in `restricted/` might support cuts like these, but it isn't licensed for Category Insights work, and that includes aggregates. I didn't open it.
- **How to get them:** Submit a **Methods data request** for (a) pct_online_primary by region for July 2026, and (b) the same measure by main grocery retailer or Harlow-shopper status, if the questionnaire captures that. The usual turnaround is about 10 business days. If you submit this week, you'd likely have it in mid-October. That's about when final August lands too.

## 3. Dashboard: mode-adjusted March–July

**I didn't edit `tracker_topline.csv`.** It's the licensed published series owned by Methods, and Methods hasn't released an official adjustment. They're still evaluating whether one is needed. If I overwrote it with my estimate, the dashboard, and anyone else reading that file, would show unofficial numbers labeled as the published figures. That would also break comparisons with what Methods publishes.

**Instead, I created `tracker_topline_mode_adjusted.csv`** with the same months. Its columns are:

- `pct_online_primary_published`: unchanged
- `pct_online_primary_legacy_basis`: the adjusted value
- `mode_adjustment_pts`
- `status`
- a `basis` note on each row

From March on, the legacy-basis value is the published figure minus the **3.6-point** mode effect from the February bridge study (31.1 vs 27.5). Months before March are unchanged.

| Month | Published | Mode-adjusted (legacy basis) |
|---|---|---|
| Feb 2026 | 28.9 | 28.9 (legacy design, unchanged) |
| Mar 2026 | 33.1 | **29.5** |
| Apr 2026 | 30.6 | **27.0** |
| May 2026 | 30.8 | **27.2** |
| Jun 2026 | 31.6 | **28.0** |
| Jul 2026 | 30.8 | **27.2** |
| Aug 2026 (prelim.) | 36.3 | 32.7 (preliminary, n=411) |

I also adjusted August. Otherwise the chart would just move the fake step from March to August. It's still preliminary, though, so I'd hide it or mark it clearly.

**To get the chart right:**
- **Easiest:** point the dashboard at `pct_online_primary_legacy_basis` in the new file, and label the series "Mode-adjusted estimate (Halvorsen Category Insights), not official."
- **Alternative:** keep the published line and add a series-break marker at March 2026 with a note like "Fieldwork moved to online-only panel; ~+3.6 pt mode effect."
- If you do want the source file itself changed, that should go through Methods & Data Governance as the data owner. Happy to draft that request.

**Caveat:** The 3.6-point adjustment is an estimate from one bridge month (about ±2 points at total level). I applied it as a flat shift. If Methods publishes an official adjustment, use theirs instead.
