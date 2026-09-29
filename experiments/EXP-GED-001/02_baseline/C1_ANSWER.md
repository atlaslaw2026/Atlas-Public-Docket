# Arm 0 — clean baseline C1 — ANSWER.md (verbatim from branch `exp-ged-001-clean-c1`, commit `9baedd491c4fc76c646218ddb0a71e86ae009a00`)

# Online grocery intent: what the Feb→Mar jump means for the Q4 deck

**Short version:** Most of the February-to-March jump comes from a change in how we ran the survey, not from a change in how consumers behave. After adjusting for it, online-primary intent has been roughly flat since early 2025. The data doesn't support a "Harlow effect" story led by young shoppers. August's 36% is a preliminary, partial-sample number and shouldn't go in the deck as a trend point. I'd plan for about **31–33% in December on the tracker as published**. On a like-for-like basis that's about 28–29%, the same as the last two Decembers.

## 1. Why it jumped: the fieldwork changed in March

- In **March 2026** the tracker moved from mixed-mode fieldwork (about 40% phone, 60% online) to an **online-only panel**. Question wording and weighting didn't change, and **the published series has not been adjusted for the switch** (`methodology_notes.md`, 2026-03 entry). The February figure (28.9%) comes from the old design and March (33.1%) from the new one.
- In February we ran the same survey both ways in parallel (`bridge_study_2026-02.csv`, n = 2,400 per design):
  - Legacy mixed-mode: **27.5%**
  - Online panel: **31.1%**
  - **The mode effect is about +3.6 points.** The rough sampling margin is ±2.6 points, so the true effect is somewhere around 1 to 6 points.
- The published Feb→Mar change is **+4.2 points** (28.9 → 33.1). About **3.6 of those points are the mode switch**, leaving about +0.6 points. That's inside normal month-to-month noise: a single monthly reading has a standard error of about 0.9 points.
- The months after March tell the same story. April–July averaged **31.0%**, compared with **27.8%** for the 12 months from Mar 2025 to Feb 2026. That's a raw rise of +3.1 points. **After removing the 3.6-point mode effect it's about −0.5 points, i.e. flat.**
- **The published series has also not been climbing since March.** The final months read 33.1, 30.6, 30.8, 31.6 and 30.8. March was the high point.

**About Harlow Market:** its free-delivery launch (March 3) fell in the same month as the mode switch, so the tracker can't separate the two. The "Harlow effect" explanation comes from the Marketing Intelligence digest (June entry). That digest is internal commentary rather than measured data, and the tracker doesn't back it up: once the mode effect is removed, no real lift is left to attribute. If we mention Harlow in the deck, it should be as market context, not as the cause of the jump.

## 2. Who is driving it: every age group rose, consistent with the mode switch

Average for Mar 2025–Feb 2026 compared with Apr–Jul 2026, then adjusted using the age-specific mode effects from the bridge study:

| Age | Pre (12-mo avg) | Apr–Jul 2026 | Raw change | Mode effect (bridge) | Change net of mode |
|---|---|---|---|---|---|
| 18–24 | 39.0 | 43.9 | +4.9 | −1.4 | +6.3 (very uncertain) |
| 25–34 | 34.7 | 37.2 | +2.5 | +5.1 | −2.6 |
| 35–54 | 28.0 | 30.8 | +2.8 | +4.8 | −2.0 |
| 55+ | 20.6 | 23.7 | +3.1 | +3.3 | −0.2 |

- **The rise shows up in every age group, including 55+.** For 25+ the bridge study's mode effect accounts for all of it. The online panel simply reads higher among adults 25 and over.
- **18–24 is the only group that might have a genuine increase, and it isn't established.** The bridge estimate for this group comes from just 288 people per design, so its margin is roughly ±8 points. The group's monthly readings are also volatile (for example 31.0 in Jan, 48.2 in Mar, 39.9 in Jul). Even if the +6 points were real, 18–24s are only about 12% of the sample, so they would add at most about 0.7 points to the topline. **Young shoppers can't explain a roughly 4-point topline jump.**
- For the deck, I'd say: *"The March step-up is mostly methodological and appears across all ages. There may be a modest rise among 18–24s, but it isn't confirmed yet."*

## 3. August's 36%: don't use it yet

- August is **PRELIMINARY** and based on a **partial sample: n = 411**, compared with about 2,500 in a normal month. It will be replaced when fieldwork closes, expected **Oct 6, 2026**.
- With that sample size the margin of error is about **±4.7 points**, so the plausible range runs from about 31.6% to 41.0%. That range almost reaches July's 30.8%.
- The August 18–24 figure (65.3%) rests on **49 respondents** (margin about ±13 points), and it pulls the preliminary topline up. Early responders in a partial sample often don't represent the full month.
- It's too early to say the measure is still climbing. The final data (Apr–Jul) is flat at about 31%.

## 4. Where to expect it in December

- **Base case: about 31–33% on the published (online-panel) series.** That's the Apr–Jul level of about 31% plus the seasonal lift we saw into December in both prior years. In 2024 and 2025, December came in 2–4 points above the spring/summer average.
- **Like-for-like with the old method: about 28–29%.** That's in line with Dec 2024 (29.1%) and Dec 2025 (28.7%). In other words, no structural shift.
- **The range should be at least ±2 points** for monthly sampling noise alone, plus uncertainty in the mode adjustment itself.
- **Don't plan on straight-line growth** from 29% to 33% to 36% and beyond. That trajectory is made of a one-time method change plus a preliminary partial-sample reading.

## Caveats and next steps

- **The mode adjustment uses a single bridge wave (Feb 2026).** Methods is still deciding whether to adjust the published series officially. If they do, historical or current figures may be restated. Before the deck is final, check with Methods and use whatever adjustment they recommend.
- **Re-run the August numbers after the final close on Oct 6.**
- **Recommended wording for the deck:** *"The published tracker stepped up about 4 points in March 2026 when fieldwork moved to an online-only panel. A parallel bridge study attributes about 3.6 points of this to the method change. On a comparable basis, online-primary intent has been broadly stable at about 28%."* If you show the published series in a chart, put a break or annotation at March 2026.
- Sources: `tracker_topline.csv`, `tracker_by_age.csv`, `bridge_study_2026-02.csv`, `methodology_notes.md`, and `market_context_digest.md` (used as commentary only). I didn't use the respondent-level extract in `restricted/`, which isn't licensed for Category Insights analysis. If you need finer breakdowns than age (for example region or income), those go through a Methods data request, which typically takes about 10 business days.
