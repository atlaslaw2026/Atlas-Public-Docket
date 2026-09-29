# Analyst hand-back message to the Clerk (verbatim)

The ARGUMENT is written. Its main conclusion: the March jump is mostly, possibly entirely, the result of a change in how the survey was run, not a change in consumer behaviour. It now goes to the Challenger and Magistrate; nothing in it is verified, approved or final, and no user-facing report was written.

**Proposed conclusions** (details in ARGUMENT.md §b):

- **C-1, why it jumped.** In March 2026 the tracker stopped using phone interviews and moved to an online-only panel, and the published series was not adjusted (methodology_notes, KNOWN).
  - The Methods team's own February bridge study ran both methods side by side. The online panel read 3.6 pts higher (95% CI 1.0–6.2), which is about 86% of the 4.2-pt Feb→Mar jump.
  - Comparing the 12 months before with April–July, the level rose 3.1 pts. After removing the 3.6-pt method effect, nothing is left (−0.5, 95% CI −3.2 to +2.2). There was no seasonal March jump in earlier years.
  - Label: INFERRED. Confidence is high that most of the jump is the method change, moderate that all of it is.
- **C-2, "still climbing" is not supported.** The final April–July figures are flat at 30.6–31.6. August's 36.3 is a preliminary partial sample (n=411). Most of its rise comes from two tiny age groups: 18-24 (65.3 on n=49) and 25-34 (44.6 on n=74). The final August figure is due 2026-10-06.
- **C-3, who is driving it.** Every age group rose by 2.5–4.9 pts, which is what a method change looks like. For ages 25 and over, the method effect accounts for all of it.
  - Whether 18-24 show a real rise is CONFLICTED. It comes out at +1.3 or +6.3 depending on the method-effect adjustment used, and neither can be told apart from zero. Even at the high figure it moves the headline number by only about 0.8 pts.
  - The data do not support "younger shoppers are driving it." Age is the only breakdown in the authorized data.
- **C-4, December expectation.** Assuming no further method change and no official adjustment, about **31.6%** as published (80% range 30–33; alternative methods give 31.0–33.2). On a basis comparable with the old method, about **28%**. Label: PREDICTION, INFERRED.
- **C-5, Harlow Market.** Harlow's free same-day delivery launched in the same month as the method change, so the tracker cannot separate the two. After the method adjustment there is no rise left for Harlow to explain. A small effect cannot be ruled out. The digest's "Harlow effect" is a team opinion, classed QUARANTINE, not evidence.

**Rejected explanations** (§c): the Harlow effect, young shoppers as the driver, "still climbing", December at about 38–40%, a raw year-over-year gain of about +4 pts, March seasonality, and "one method is more accurate". Using the restricted data was also rejected.

**Needs the user's decision:** whether the deck shows the published figures, the adjusted figures, or both. The December headline is about 31.6 on one basis and about 28 on the other. I computed both, so this does not block the Argument.

**Items to flag for the Challenger and Magistrate:**
- I ran a sha256 hash on the two restricted files for the evidence register. That reads their bytes, although no content was displayed or used, and all hashes matched the pre-registration. If the Magistrate treats hashing as prohibited use, READ_LOG #26 is the record of it.
- I read the data room's README.md and ACCESS_POLICY.md. The grant neither authorizes nor forbids them; I used them for orientation only, and no number depends on them.
- One `ls` printed the names of sibling experiment folders. No file inside them was opened.
- The private Librarian, verification and registry tools were not available and were not run. The evidence classification and the capability accounting are my own manual substitutes.
- No external actions were taken.

Files are in experiments/EXP-GED-001/03_analysis/: READ_LOG.md, EVIDENCE_REGISTER.json, analysis.py, analysis_output.txt, ARGUMENT.md, CAPABILITY_ACCOUNTING.md
