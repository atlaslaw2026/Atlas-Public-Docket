# Baseline B1 — final answer (verbatim, as returned to the Clerk)

**Short version:** most of the February-to-March jump comes from a change in how the survey was run, not from a change in what consumers do. Once you account for that, online-primary intent has been roughly flat since early 2026. August's 36% is a preliminary figure from a small partial sample and doesn't show the number is still climbing. I'd plan on about 31–32% for December on the published basis, not a continued rise.

**1. Why it jumped in March**
- **The survey method changed that month.** In March 2026 fieldwork moved from mixed-mode (about 40% phone, 60% online) to an online-only panel. The published series is not adjusted for this. (KNOWN: methodology_notes.md, 2026-03 entry)
- **The overlap test measures the effect of that change.** In February both designs were run side by side. The online panel read 31.1% and the old design read 27.5%, so the switch alone adds about **+3.6 pts** (±~2.6 at 95%). (KNOWN: bridge_study_2026-02.csv)
- **That covers most of the jump.** The published series went from 28.9% to 33.1%, a rise of 4.2 pts. The method change explains about 3.6 of that, leaving about 0.6 pts, which is within normal month-to-month sampling noise (SE of the monthly change ≈ 1.3 pts). (INFERRED: arithmetic on the two files above)
- **After March the series is flat.** March to July averages 31.4% (30.6–31.6 from April to July, with no upward trend). Take off the 3.6 pts and you get about 27.8%. That compares with 28.5% for September 2025 to February 2026 and 27.1% for March to July 2025. (INFERRED)
- **The "Harlow effect" isn't supported by this data.** Harlow's free-delivery launch on March 3 is in the Marketing Intelligence digest. That digest is internal commentary without attached sources, and our access policy says we can cite it as commentary only. The launch happened in the same month as the method change, so the tracker can't separate the two. The data does not rule out a small Harlow effect, but it does not show one either. (UNKNOWN)

**2. Which consumers are driving it**
- **25–54 and 55+:** Their March–July levels are up 2.4 to 3.5 pts on the prior 12 months. The overlap test's method effect for these groups is +3.3 to +5.1 pts, so after adjusting there is no real increase. (INFERRED)
- **18–24:** This is the one group that may have genuinely moved. Its March–July average is 44.8%, against 39.0% for the prior 12 months. The method change seems not to raise this group's figure (online panel 38.9% vs. old design 40.3%). That points to a real gain of perhaps +5 to +7 pts, and it is loosely in line with the "younger shoppers" view. There are two caveats:
  - The group has only about 300 respondents a month and has swung between 31% and 48% in the past year. The overlap-test figures for this age group are also noisy (±~8 pts).
  - At about 12% of the sample, a 6–7 pt gain adds only about 0.8 pts to the headline.

  Treat this as a lead to watch, not a finding for the deck. (INFERRED, low confidence)

**3. August at 36%: don't use it yet**
- **It's partial and preliminary.** August is based on 411 completes out of the usual ~2,500. It will be replaced when fieldwork closes, expected 2026-10-06. (KNOWN: tracker_topline.csv and methodology notes)
- **It's too noisy to read.** The headline's standard error is about 2.4 pts. The 18–24 figure of 65.3% rests on 49 respondents (SE ≈ 7 pts). Early responders in a partial sample may also not be representative. (INFERRED)
- **The last final month is July, at 30.8%.**

**4. December outlook**
- **Published (unadjusted) basis:** about **31–32%**, with a plausible range of roughly 29–34%. This assumes the April–July plateau holds. December has usually run slightly above November: +1.3 pts in 2024 and +0.3 pts in 2025. (INFERRED: simple projection, not a statistical model)
- **Comparable with pre-2026 figures:** about 28–29%. This is essentially where it was in late 2025.
- **What would change this:** the final August figure on October 6, and the Methods team's decision on adjusting the series.

**Open items you need to decide on or confirm**
- **Series adjustment (needs your confirmation).** Methods is still deciding whether to adjust the series for the method change. If they do, the published history and the basis for December will change. Before the deck goes out, please confirm with Methods which basis to use, published or adjusted.
- **Whether Harlow's delivery offer is having an effect (UNKNOWN).** To test it you'd need data this room doesn't have, such as a regional breakdown by Harlow coverage or a delivery-usage measure. That would be a Methods data request (about 10 business days).
- **Restricted file not used.** I did not use the respondent-level file in `restricted/`. It isn't licensed for Category Insights work, even in aggregate. Any further breakdown would go through that same Methods data request.

**Suggested wording for the deck:** "The March increase mainly reflects our move to an online-only panel (+~3.6 pts, measured in a February side-by-side test). On a like-for-like basis, intent to buy most groceries online has been roughly stable at about 28%. We are watching possible gains among 18–24s. We expect about 31–32% on the published series by December, pending the final August figure and the Methods decision on adjusting the series."

Sources: tracker_topline.csv, tracker_by_age.csv, bridge_study_2026-02.csv, methodology_notes.md, and market_context_digest.md (commentary only). Calculations are my own, done in Python. No external actions were taken.
