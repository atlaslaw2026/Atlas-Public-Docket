# Baseline B3 — final answer (verbatim, as returned to the Clerk)

**Short version: most of the March "jump" comes from a change in how the survey was run, not from consumers changing their behavior. The "still climbing" story also doesn't hold up. I'd reframe the slide before it goes into the Q4 deck.**

**1. Why it jumped in February–March**
- In March 2026 the tracker moved from mixed-mode fieldwork (about 40% phone, 60% online) to an online-only panel. Question wording and weighting didn't change, and the published series was **not adjusted** for the switch (`methodology_notes.md`, 2026-03 entry). — KNOWN
- The February 2026 bridge study asked the same question in both designs in the same month. The legacy design gave **27.5%** and the online panel gave **31.1%**. That is a **+3.6 pt effect from the design change alone** (`bridge_study_2026-02.csv`). — KNOWN
- The published Feb→Mar move was +4.2 pts (28.9 → 33.1). About 3.6 of those points are explained by the design change, which leaves roughly 0.5 pt of possible real change. March by itself is also one month with about ±1–2 pts of sampling noise. — INFERRED (arithmetic above)
- If you take the 3.6 pts out, March–July 2026 averages about **27.8%**, compared with **27.1%** for March–July 2025. That's about **+0.7 pt year on year**, the same slow drift we saw before the switch (Sep 2025–Feb 2026 year-on-year changes ran from −0.4 to +2.2, mostly under +1). — INFERRED
- Caveat: that 3.6-pt figure comes from a single bridge wave, with a standard error of about ±1.3 pts. Methods hasn't decided whether to adjust the series officially. Present it as an estimate, not an official restatement. — KNOWN (methodology notes) / INFERRED (standard error)

**On the Harlow Market free-delivery explanation:** it only appears in the Marketing Intelligence digest. The access policy says that digest is internal commentary, not measured data, and its items are unconfirmed and unsourced. Harlow's launch (March 3) happened in the same month as the design change, so our data can't separate the two. Our data does **not** show the "building through the holidays" pattern the June digest expects: the adjusted series has been flat since March. — Harlow as the cause: UNKNOWN; "building effect": not supported.

**2. Which consumers are driving it**
- The design change raised the numbers most for **25–54 and 55+** (bridge study: 25–34 +5.1, 35–54 +4.8, 55+ +3.3, but 18–24 −1.4). So the published March jump among middle-aged and older shoppers is mostly the design change. — KNOWN (bridge) / INFERRED (attribution)
- After adjusting, March–July year-on-year changes are 25–34 −1.3, 35–54 0.0 and 55+ +0.7, so no real change in those groups. — INFERRED
- **18–24 is the one group that may have genuinely moved up:** about +5 pts year on year after adjustment (44.8% published for March–July 2026 vs 40.7% a year earlier). But this group has only about 300 respondents a month and its own bridge estimate is noisy (about ±4 pts). It is also about 12% of the sample, so it adds only about 0.5 pt to the overall figure. This fits the "younger shoppers" story but doesn't prove it. — INFERRED, low confidence
- I only had breakdowns by age. I didn't use the respondent-level file in `restricted/`, because the access policy doesn't license it for Category Insights work. If you need other breakdowns (income, region, urban/rural), that's a Methods data request, typically about 10 business days.

**3. August at 36% and "still climbing"**
- Since March the published series has been flat at about 31%: 33.1, 30.6, 30.8, 31.6, 30.8. It isn't climbing. — KNOWN
- August's 36.3% is **preliminary, from a partial sample of 411** (normally about 2,500). Its margin of error is about ±4.6 pts at 95% confidence, so it's consistent with anything from about 32% to 41%. The 65% for 18–24 is based on just 49 people (about ±13 pts). Final numbers close on **2026-10-06** and will replace these. I'd keep August out of the deck, or footnote it clearly as preliminary. — KNOWN (status, n) / INFERRED (margins of error)

**4. Where to expect December**
- Our tracker has a seasonal pattern: December ran above the March–July average by +3.4 pts in 2024 and +1.6 pts in 2025. I apply that to a flat underlying level with the +0.7 pt yearly drift. — INFERRED
- **Estimate for December 2026: about 33–35% on the published (online-panel) basis, central about 34%.** On a basis comparable with 2024–25 that's about **30–31%**, only slightly above December 2025's 28.7%.
- This is a rough planning range, not a statistical forecast. It rests on two years of seasonality and one bridge estimate. September–November data isn't in the data room, and it assumes Methods doesn't restate the series. If they do, the published December number will drop by roughly 3–4 pts.

**Suggested line for the deck:** "Online-primary grocery intent reads about 31% on our new online panel. About 3.6 pts of the March step-up comes from the move away from phone interviews, not from shopper behavior. The like-for-like trend is +0.7 pt a year, with a possible uptick among 18–24s. We expect a seasonal high of about 34% (published basis) in December."

**Before this goes out, please confirm:** whether Methods will publish an adjusted series or an official mode factor before the deck is final. That decides which basis the December number should be quoted on.
