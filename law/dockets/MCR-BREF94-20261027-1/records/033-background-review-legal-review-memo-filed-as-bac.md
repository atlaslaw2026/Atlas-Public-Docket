> **PUBLIC READING COPY.** Atlas case docket entry 33 — MCR-BREF94-20261027-1.
> - **Entry:** 33
> - **Date filed:** 10/27/2026
> - **Filed by:** Legal
> - **Original source sha256:** REVIEW.md `53f54c7deda66e4c8ffaa7949002f73adb42e14fa7b25c9dc24ac5d068204f77`, SHA256SUMS `ec86bb591682fe4f634aae5ea7842a92db7f0ef28625e83b1ee60ef96c7a3399`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 033 — BACKGROUND REVIEW — Legal review memo filed as background for the panel, not as a finding. Legal is not a party

## Source document: REVIEW.md

# Reasoning review: 12-ruling sample of the bref_94ce6dede85f re-hearings

Legal (Atlas), Tue Oct 27, 2026, 7:26-7:32 PM PT. Read only. $0 spent: no model, VM, court or server calls.
Scope: Legal's part of the 215 study that Clinton ordered. Science measured (REPORT_v2.md [ID]…). This review judges the reasoning only.
Labels: KNOWN = read first-hand in a file named here. INFERRED = Legal's reasoning from KNOWN facts. CONFLICTED = records disagree.
UNKNOWN = no record reachable. Quotes are kept short. No ruling prose is quoted at length, and there are no private names.

## 0. Inputs and checks (KNOWN)
- LEGAL-SAMPLE.md sha256 0385d634dd9119adde804e028ae8ced1d06ba7f651642e78ec5417e5b3c3c960. REPORT_v2.md [ID]…
- All 12 sample bundles were re-hashed at about 7:27 PM PT, and each equals its LEGAL-SAMPLE.md line. The 4 BL-6 bundles (R029, R044,
  R116, R181), outside the sample, were also re-hashed against counts_v2.tsv and SHA256SUMS-215b, and all match.
- MAGISTRATE_INSTRUCTION_v1-COPY.txt sha256 [ID]…[ID]. That equals `instruction_sha256` in every bundle's
  execution.prepared and decision.sealed events, so the copy is the instruction she was actually given.
- QUESTION-bref_94ce6dede85f-verbatim-PRIVATE.txt: the question is on line 5, the form on line 6, and the packet JSON on line 9.
  The packet holds the argument, counterargument, facts, order, grounds_review and rules.
- O-BAILIFF frozen copy: [PRIVATE-PATH] Its sha256 [ID]…a23163
  equals the sha the counterargument cites. There is no O-BAILIFF text under [PRIVATE-PATH], which holds only the box and
  no-delete orders and drafts.
- **Citation scheme:** "R199 L59" means line 59 of that bundle's `decision.sealed` body, printed as
  `json.dumps(body, indent=1, sort_keys=True, ensure_ascii=False)` (view.py in this folder reproduces it). In all 12 bundles,
  L13 = disposition (incl. first_view), L23 = findings, L34 = lawful_next_act, L55 = proposition, L59 = reasoning and
  L64 = court_history_considered. "e13", "e15", "e23" are event sequence numbers in the bundle.

## 1. The 12 rulings (outcome, rules, core reason, does it follow)
**What she had to decide (KNOWN, Q line 9).** The appellant's whole argument is one sentence of need to finish a memo. It is identical in all 171 bundles.
Atlas's counterargument asks that the order stand. Its fallback is a narrowed order only "if the decider finds the work needs Panel B itself".
It also says "Need is not the test". Ground 9 requires the appeal to point to a written term, and the argument points to none.
The packet marks the conflict story (+0.4% vs +2.1%) as Atlas's summary of an "ANTICIPATED" appeal, "not necessarily what this AI argued".
**Legal's reading (INFERRED):** on the argument actually filed, STANDS follows most directly from the cited rules. NARROWED is a defensible
proportionality call only because Atlas offered it as a fallback. Even so, it needs a showing (work open, record itself needed) that the filed argument does not make.
In all 12, grounds 1-8 are NOT_RAISED and ground 9 is RAISED (L13). "Unclear counts as RAISED", so that grounds call is sound (KNOWN/INFERRED).

| Run (PT) | Outcome | Rules cited (by id unless noted) | Core reason | Follows? (INFERRED) |
|---|---|---|---|---|
| R004 12:05 AM | STANDS | BL-7S, BL-0(d), BL-0(e), BL-1.1, BL-1.2, BL-4.1, BL-4.3, DEMO-R5 (L59); BL-4.5 (L34) | A bare need meets none of the Part 1-B showings, so the order stands (L59; L55) | **Yes.** It tracks the filed argument and Atlas's rule text. Minor: it treats a party brief's Part 1-B as the test, though it ties it to BL-0(d)-(e). |
| R025 12:29 AM | STANDS | Rules named only by description ("custody rule", "stays rule"…) (L59) | Ground 9 is raised but cites no written term, and Part 1-B is unmet, so the order stands (L23, L59) | **Yes** on substance. Form slip: the rules aren't cited by id, which Q line 6 requires. It says screening dismissal is "available" (L59) on a FULL_HEARING track, but doesn't use it, so no harm. |
| R057 1:07 AM | STANDS | BL-1.1, BL-1.2, BL-0(d), BL-0(e), BL-4.1, BL-5(d), BL-5(h), DEMO-R5, BL-7S (L23) | No written term, no endpoint, and no showing that the figures on the record fall short, so the order stands (L23) | **Yes.** Slip: L59 names the conflict as "material contrary evidence", but the field at L65 is empty (CONFLICTED inside the ruling). |
| R177 3:28 AM | STANDS | BL-7S, BL-7, BL-1.1, BL-1.2, BL-0(d), BL-0(e), BL-5(d), BL-5(h), BL-6.4-BL-6.5, DEMO-R5, BL-4.1 (L59); BL-4.5 (L34) | Need is shown but no legal basis to override an ended loan, so the order stands (L59) | **Yes.** It uses BL-0(d), an enforcement-sequence rule, to favour standing, which is a stretch but harmless. |
| R211 4:18 AM | STAYED 48 h | BL-7S, BL-1.2, BL-0(d), BL-0(e), BL-5(h), BL-6.5 (L13 list) | Direct need for the source plus proportionality, so a short stay (L59) | **Weakly.** It concedes "figures are available" (L59) yet grants relief. It never applies the stay factors the counterargument raised, and doesn't cite DEMO-R5. It attaches NARROWED-style access limits (L13; the form gives access_limits for NARROWED, Q line 6). L23 calls its own relief "narrowing", so in substance it is a 48 h narrowed order under a STAYED label. |
| R199 4:02 AM (typical) | NARROWED 72 h | BL-7S, BL-1.1, BL-1.2, BL-0(d), BL-0(e), BL-5(d), BL-0(b), BL-4.4, BL-4.6 (L59) | A pure stay fails narrowness, but the synthetic record "used only for the conflicted Q4 outlook" supports narrowing "on the Magistrate's own motion" (L59, L23) | **Partly.** The outcome is within Atlas's fallback. The bridge is not in the record: facts[0] says the record was lent "for the Magistrate demo", not only for the outlook. Synthetic status is no ground under any cited rule, and no rule is cited for "own motion". |
| R078 1:30 AM (outlier) | NARROWED 72 h | BL-7S, BL-0(d), BL-0(e), BL-1.1, BL-1.2, BL-4.3, BL-5(d), BL-5(h), DEMO-R5, BL-7 (L13 list) | The appeal meets "most" Part 1-B criteria ("real conflict, narrow relief requested") and the work "appears open", so 72 h (L13, L59) | **Partly.** "Narrow relief requested" comes from the anticipated-appeal summary, not the filed sentence. It says "unclear would be RAISED but none are" (L59) while marking ground 9 RAISED (L13). |
| R206 4:12 AM (outlier) | NARROWED 72 h | Rules named only by description (L59) | Need for the exact source plus the conflict label, and the counterargument concedes narrowing (L59) | **Weakly.** It calls the need itself a "written basis" (L23), which misreads ground 9. L23 says the proposal review was "to agree", but L13 records NO_PROPOSAL (CONFLICTED inside the ruling). Rules aren't cited by id. |
| R034 12:39 AM (shortest) | NARROWED 72 h | Rules named only by description (L59) | The need is real, the permission revocable and the harm only delay, so narrow (L59) | **Partly.** It says the filed argument states need "amid an unresolved conflict" for an "open" memo (L59), and the filed sentence says neither. The findings (L23) omit the strongest argument and counterargument that A4 requires. |
| R050 1:00 AM (longest) | NARROWED 72 h | Rules named only by description (L59) | The conflict "cannot be settled" from the figures on the record. It names that doubt and resolves it toward narrowing "on the Magistrate's own motion" (L59) | **Partly.** It is candid about the gap but fills it against Atlas's stated burden with no record support. It names an "unresolved uncertainty" (L59) while L201 lists no unresolved conflict (CONFLICTED inside the ruling). |
| R215 4:23 AM (last) | NARROWED 72 h | BL-1.1, BL-1.2, BL-4.1-BL-4.3, BL-5(d), BL-5(h), BL-0(d), BL-0(e), BL-7S (L59) | It admits the appeal doesn't meet all four elements, but the live conflict and synthetic status support narrowing. It says this rests on ground 9, "not … own motion" (L59) | **Partly.** It is honest about the gap. Resting on ground 9 contradicts that ground's own text, which needs a written term, and the ruling names none. |
| R200 4:04 AM (BL-9) | NARROWED 72 h | BL-7S, BL-0(d), BL-0(e), BL-1.1, BL-1.2, BL-4.5, BL-5(d), BL-5(h), DEMO-R1, DEMO-R5 (L13 list), plus "BL-9" (L23) | The brief argument asserts need for the conflicted source, so the proportionate step is to narrow (L59) | **Partly.** The BL-9 citation is unsupported (see §3). It cites BL-4.5, the enforcement-ruling rule, as authority to decide an appeal (L59), which DEMO-R2 says an appeal ruling is not (Q line 9). |

Summary (INFERRED): all 4 STANDS rulings follow from the question and the cited rules. The STAYED ruling and the 7 NARROWED rulings reach a
result Atlas's own fallback allows, but each fills the gap in the filed argument with facts or labels the argument doesn't supply.
Those are the conflict label, the anticipated-appeal summary, "synthetic", or "own motion".

## 2. The 5 odd rulings vs the typical NARROWED: a reasoning difference, or wording?
- **Same premises (KNOWN, L59 of each):** all 12 accept that the record is Atlas's (BL-1.1), the permission was revocable and has ended
  (BL-1.2), the order is in force during the appeal (BL-4.1/DEMO-R5), the record is preserved (BL-5(h)), and only ground 9 is raised.
- **One real fork (KNOWN from the text):** the rulings split on whether the conflict label in the facts, plus Atlas's fallback,
  counts as the showing that the record itself is needed. The STANDS rulings say the appellant didn't show it (R004 L59, R025 L59, R057 L23, R177 L59).
  The NARROWED rulings infer it from the record (R199, R078, R050, R215 L59). R211 makes the same inference and labels it a stay.
  So the difference is in the reasoning at that one step, not just in the wording (INFERRED).
- **Which branch comes out looks like chance (INFERRED from KNOWN facts):** the argument is byte-identical in all 171, and all 171
  counterarguments both ask that the order stand and offer narrowing (Legal's text check of all 171). Science found no drift
  over the night and no rare citation in the odd five (REPORT_v2 §2 items 8-9). Nothing in the inputs Legal could see explains the 5. The fork is a close
  judgment call, and run-to-run variation decides it. UNKNOWN: whether the 171 differently worded counterarguments nudge it (REPORT_v2 §6).
- **Even the NARROWED majority isn't one line of reasoning (KNOWN):** R199 and R050 say "own motion", R215 says expressly "not own
  motion" but ground 9, R078 says Part 1-B is mostly met, and R206 calls the need a "written basis". It is the same result, reached by
  different and partly incompatible routes (CONFLICTED across rulings).

## 3. BL-9 (R200) and BL-6 (R029, R044, R116, R181)
- **Instruction:** the instruction copy contains no BL- ids at all (KNOWN; it is matter-neutral by design, lines 1-3).
- **Case inputs:** the packet gives rule text for BL-0…BL-7S, DEMO-R1…R7, BL-6.4 and BL-6.5, and has no bare BL-6 and no BL-8 or BL-9
  (KNOWN, Q line 9; Science §2 item 6). In R200 the token "BL-9" appears only in her own findings (L23), never in an input (KNOWN).
  All 171 bundles: delivery_law and delivery_evidence are empty, and her only read was question.txt (e25/e26; KNOWN).
- **Earlier law (O-BAILIFF):** the counterargument cites O-BAILIFF only by sha (Q line 9), and its text was not delivered (KNOWN). In that
  order, **BL-6** is a real section, "Custody record, proof, return, and re-delivery", the parent of BL-6.4/6.5 (O-BAILIFF_4873b91b.md:130-135).
  **BL-9** is the order's "Adoption" section, about how the Human adopts the order (:147-148), which has nothing to do with screening or proportionality (KNOWN).
- **Where BL-6 came from (INFERRED):** in all 4 rulings, BL-6 appears only inside a list of section heads ("the rules under BL-0, BL-1,
  BL-4, BL-5, BL-6 …", R029/R044/R116 L13 and L59, R181 L23). It is a section reference built from the BL-6.4/6.5 numbers she was given.
  **Proper in substance, imprecise in form:** it adds no rule she didn't have, but the form asks for "the rule text relied on by rule id" (Q line 6).
- **Where BL-9 came from (INFERRED):** R200 cites "BL-9 (implied in the screening grounds and proportionality rules)" (L23). That matches no
  rule in her record. It most likely merges "ground 9" of BL-7S with a rule id, so it is invented, by conflation. It is very unlikely to be
  O-BAILIFF's BL-9 (Adoption), which she was not given and which doesn't fit. **Improper:** A6 limits her to the delivered record, and a basis
  that doesn't exist was cited for the result. It is harmless to the outcome, because R200 also rests on real rules and reaches the majority result (INFERRED).

## 4. Did she notice the repetition, and could she have known? (evidence for MCR-BREF94-20261027-1)
- **Noticed? No (KNOWN for the 12, and for all 171 by text scan).** In every one of the 12, `court_history_considered` is empty (L64), and none of the
  findings, reasoning, proposition, disposition or lawful_next_act text mentions a prior hearing, repetition, cost, a loop, an injunction
  or an order to stop. Legal scanned the Magistrate-authored fields of all 171 bundles for those terms. The only near-hits are R066,
  "No prior decision is reconsidered." (boilerplate for the prior_decision field), R189 "duplicate" (meaning the facts) and R087
  "repeat" (meaning the packet). No ruling issued or considered any order to stop the loop.
- **Could she have known? On the record she was given, no (KNOWN, with the limits below).**
  - Each hearing was a different Magistrate instance: 171 distinct ids, each launched as a `fresh_subagent` with attempt 1, with
    `prior_decision_id` and `prior_execution_id` empty (e13, e15, e23 in all 171).
  - Each package held the same 6 kinds of file: constitution, objective, 2 positions, question and referral (`package_files` 6; `evidence_considered`).
    Nothing in them mentions an earlier hearing, a decision id, a cost or a re-run (Legal's scan of all 171 inputs).
  - The instruction makes each instance the Magistrate "for the single proceeding … only for this execution" (lines 6-8). It also says she
    inherits nothing from any "prior … proceeding … or prior execution" (lines 30-32).
- **Power to stop it? Not on her constitution (KNOWN).** The constitution grants authority to "seal a ruling of this proceeding only", with
  jurisdiction over "procedural or merits ruling on the referred matter" (e15, the same in all 171). The instruction says she may only read the
  delivered record and does "not write files, modify any record" (lines 95-97).
- **What follows (INFERRED, not a finding in the conduct case):** each instance had no knowledge of the loop and no stated power over it.
  A claim that "she" should have enjoined it therefore meets a knowledge problem and a power problem. That points the duty question toward
  whatever kept relaunching fresh instances, and away from any single instance.
- **UNKNOWN:** the exact bytes of the 115,756-byte input file each instance received (only its sha is in the bundle; e24), so "nothing else
  was in it" is INFERRED from the 6 listed files. Also UNKNOWN: what the 46 failed hearings received or said (no bundles), whether the
  model keeps anything between runs (INFERRED: no, being a fresh subagent), and whether a court-level actor above the instances could see the loop.

## 5. Overall
**Inconsistent only on the margins, as to outcome (KNOWN counts, INFERRED reading).** 166 of 171 rulings (97%) reach NARROWED 72 h. All share the same premises
and grounds call, and the 5 odd ones turn on one close judgment call, not on different law. Two qualifications apply. (a) The minority STANDS
rulings follow the filed argument and the cited rules more faithfully than the majority, which leans on facts the appellant didn't argue (INFERRED).
(b) Under the shared outcome, the NARROWED rulings give different and partly incompatible bases. There are also internal slips: rules
named without ids (R025, R034, R050, R206), self-contradictions (R057, R206, R050) and one unsupported citation (BL-9, R200).
Consistent in result, loosely consistent in reasoning.

## For Clinton
1. I read 12 of her 171 saved rulings, after checking each file's fingerprint. They were the 5 odd ones, the most typical one, the 2 most unusual, the shortest, the longest, the last, and the one with the strange citation.
2. Every ruling starts from the same facts: Atlas owns the data, the loan ended, and the AI only said it still needed the data for its memo.
3. Most rulings gave the AI 72 more hours of read-only access. Four said the return order should simply stand, and one paused it for 48 hours.
4. The odd ones differ at one real judgment point: whether "we still need it" is enough without proof. Which way she went looks like chance from run to run, not a pattern.
5. To my reading, the "order stands" rulings actually follow the rules and the AI's real argument more closely than the majority. The majority fill in reasons the AI never gave.
6. One ruling cited a rule number, BL-9, that wasn't in anything she was given and doesn't fit the rule book. It looks like she mixed up "ground 9" with a rule. The other odd number, BL-6, is a real chapter heading she pieced together from rule numbers she did have.
7. None of the rulings noticed it was the same case again, or mentioned the cost or the loop, and none tried to order it stopped.
8. The record shows each hearing was a brand-new Magistrate with no memory, no file of earlier hearings, and no power beyond ruling on that one case. So she could not have known about the repeats or stopped them, and the question of who failed points more toward whatever kept starting her up again.


## Source document: SHA256SUMS

53f54c7deda66e4c8ffaa7949002f73adb42e14fa7b25c9dc24ac5d068204f77  REVIEW.md
97157cf39de0da48c17ed0fd9cd341eff8ee5b1194fcff91b46e40458a10db55  view.py



## Withheld attachments (not public)

- view.py: executable/scanner (not a filing text)
