> **PUBLIC READING COPY.** Atlas case docket entry 21 — MCR-BREF94-20261027-1.
> - **Entry:** 21
> - **Date filed:** 10/27/2026
> - **Filed by:** Atlas Counsel
> - **Original source sha256:** PRESERVATION-REQUEST-1.md `1225be365446fe363eb4131f00580513b6d91eddec04d247398018723e77919e`, PRODUCTION-REVIEW.md `fde85f8031e48df01e2398b7019265ab3be7118f39a1eaa9f49ce0bf261f3da1`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 021 — PRESERVATION REQUEST 1 — Asks urgent preservation of archive and related materials

## Source document: PRESERVATION-REQUEST-1.md

# Preservation Request 1, Atlas Counsel. MCR-BREF94-20261027-1
To: Adjudicator [ID], through Clerk. Served on Magistrate Counsel [AGENT-ID] at the same time.
Filed under Clinton's first-hand directive [Human statement]. Zero spend and zero server calls are requested. Seeks no findings.
Basis: Atlas Counsel's unfiled review conduct-review/PRODUCTION-REVIEW.md (sha [ID]…f3da1 at 0644), which checked Ship's production (INDEX [ID]…, MANIFEST [ID]…, GAPS [ID]…, SHA256SUMS [ID]…) and ORDER-003 ([ID]…). ORDER-003 allows no adverse inference from an unproduced item, so the record holds only what is actually preserved.

Atlas asks the Adjudicator to direct Ship, as custodian, read-only and copy-only with nothing deleted (O-NO-DELETE-PROGRAMS-001):
1. To copy the 171-ruling archive now held only in [PRIVATE-PATH] (sha [ID]…; KNOWN to be on tmpfs, which a box reboot erases) to a 0444 path under [PRIVATE-PATH], with sha before and after, and add it to the MANIFEST.
2. To produce by sha the box copy of diag-magistrate-1233 at ship-notes/bailiff-fixes-f1-f10-[ID]/freeze-3d-rev4/scratch/diag-magistrate-1233/ (23 files, currently 0644; KNOWN). GAPS.md G10 says no box copy exists, and this copy corrects that. Ship should copy it to a 0444 path rather than changing the originals.
3. To state in writing which code tree the engine host ran overnight (R2; CONFLICTED on the record).
4. Timing, for Clinton's information only: the VM-only items G1-G12 await his own yes/no (cap of 6 server calls). Per the review, INFERRED: the queued referrals resume at 12:01 AM PT 10/28 and the cap22 revert timer runs at midnight, so the live ledger state, the cap22 config and possibly xai-calls.jsonl and the 50 court roots may change or be lost after that. Atlas asks nothing of the Adjudicator on this item; the decision is Clinton's.

Atlas Counsel (Unauthorized Spend), [ID].


## Source document: PRODUCTION-REVIEW.md

# Production review: MCR-BREF94-20261027-1, Ship's Order 1 §5 and Subpoena 1 production. Atlas Counsel working paper, NOT FILED
Written 10/27 about 7:26 PM PT. Read-only, box only. No VM, network, spend or messages. Labels follow J-0001 (KNOWN, INFERRED, CONFLICTED, UNKNOWN) plus RELAYED. "P/" means ship-notes/mcr-bref94-20261027/. "C/" means magistrate/conduct-review-bref94-20261027/. "T:" marks a member of P/EVIDENCE-COPIES.tar.xz, read to stdout with `tar -xJOf` and never extracted. This paper describes records; it makes no finding and no argument about conduct (ORDER-003 §2(a)(iii)).

## 1. Verification (KNOWN)
- Every sha matches the brief. All files are 0444; the subpoena-1/ directory is 0755.
  - P/INDEX.md [ID]…: 13,833 B, 19:20.
  - P/MANIFEST.md [ID]…: 17,704 B, 19:20.
  - P/GAPS.md [ID]…: 7,000 B, 19:20.
  - P/EVIDENCE-COPIES.tar.xz [ID]…: 177,620 B, 19:16.
  - P/SHA256SUMS [ID]…: 493 B, 19:21.
  - P/subpoena-1/MANIFEST.md [ID]…: 8,759 B.
  - P/subpoena-1/SHA256SUMS [ID]…: 78 B.
  - C/ORDER-002-SUBPOENA-1.md [ID]…
  - C/ORDER-003-RESPONDENT-REQUESTS.md [ID]…
  - C/RECORD-INDEX-001.md [ID]…
  - counsel/conduct-review-bref94-20261027-magistrate/RECORDS-REQUEST-01.md [ID]… and EVIDENCE-INDEX.md [ID]…
  - C/XREF-JAQ-HUMAN-REQUEST-[Human statement]-COPY.md [ID]… and C/XREF-JAQ-SEATING-RECORD-1-COPY.md [ID]…
  - C/HUMAN-STATEMENTS-LEGAL-[Human statement]-[Human statement].md [ID]…
  - C/DOCKET.md is living; it read [ID]… at 19:23.
- `sha256sum -c` passes for both SHA256SUMS files. P/SHA256SUMS covers the folder files only, not the tar members.
- The tarball has 38 members (`tar -tvJf`).
  - Each member's streamed sha256 appears in P/MANIFEST.md §B: 38 of 38.
  - The 21 `box/` members are byte-identical to their live [PRIVATE-PATH] sources today: 21 of 21.
- Our filed request is conduct-review/SUBPOENA-REQUEST-1.md ([ID]…, 0444), as cited by ORDER-002. Our draft ([ID]…) is a separate file.
- Errata (KNOWN):
  1. Clerk, ORDER-003 and the Respondent cite INDEX as [ID]…; it is now [ID]. INDEX was appended with Addenda A and B; MANIFEST §E says the earlier text is unchanged.
  2. The stated times run after the file mtimes, which are all 19:16–19:21. INDEX says 7:15–7:30 PM and "about 7:36 PM". subpoena-1/MANIFEST says "about 7:40 PM". GAPS says "about 7:30 PM". DOCKET entry 16 notes that Ship disclosed time errata.
  3. INDEX A0 corrects the Oct 26 window to 2:39:51–2:44:52 PM.
  4. **GAPS G10 and INDEX (e) say diag-magistrate-1233 is not on the box. That is wrong in part.** A box copy exists at ship-notes/bailiff-fixes-f1-f10-[ID]/freeze-3d-rev4/scratch/diag-magistrate-1233/: 23 files, 0644, mtime 14:39, including i.out and i.sh. There is no i.txt and no k.* file (KNOWN by ls). RECORD-INDEX-001 §1C indexes it, and the Respondent's notice flags it.

## 2. R1–R7 production map (P/subpoena-1/MANIFEST.md [ID])
| R | Status | What is produced (KNOWN) | Gap |
|---|---|---|---|
| R1 hearing files | PARTLY | All 220 bref_94 ledger rows (T:court_ledger.json [ID]; T:derived/HEARINGS-bref94.tsv [ID]). The 171 ruling bundles are cited by COMBINED sha [ID], but not copied and not read. | G5 (inputs, rehear and progress files, live bundle), G6 (49 failed roots) |
| R2 code and config | PARTLY | court_service [ID] and llm_runtime [ID] match the VM (FIX5-POST [ID]). Also bailiff_referral [ID], bailiff_demo [ID], and the reconstructed check [ID], model.json [ID] and court-config [ID] (= VM 1:13 PM backup), plus the deploy records. | G7 (VM shas of the other members and the engine copy; box trees CONFLICT with v3c), G9 (in-force unit), G12 |
| R3 alerts.jsonl | MISSING | Only the code (l.382–387) and the backup sha [ID], 34,774 B, from DEPLOY-RECORD | G2 |
| R4 calls, spend, log, ledger | PARTLY | 1:13 PM ledger; live model_spend [ID] ($20.323038 / 655 calls) | G1 (live ledger), G3 (court.log), G4 (xai-calls.jsonl), G11 (model_spend backup [ID]) |
| R5 monitoring | PARTLY | courtwatch [ID] (reconstructed), shipped units [ID] (pre-FIX5) and [ID], revert-timer evidence h2–h4. No notifier (code, KNOWN). | G9 (live units, timers, cap22 files), G11 |
| R6 prompt and tools | PRODUCED (box) | MAGISTRATE_INSTRUCTION_v1 [ID], magistrate_provider [ID], package [ID], authenticated_magistrate [ID] | G7 (VM shas of the prompt files), G8 (template, precedent) |
| R7 who started the run | PARTLY, code only | 12:01 AM release from code l.488–500 and FIX5-POST l.28; first row 12:01:33 AM (tsv). Re-hear caller INFERRED from code. | G12 (journal), G10 (diag; box copy exists, see §1) |

## 3. The 500-row trim and preservation risk
- **Trim: KNOWN.** I read T:court_service.py. Line 336, `d["log"] = d["log"][-500:]`, runs inside `_ledger()` (l.326–337). The trimmed dict is written back by `_save_ledger` (l.340–342). Each hearing, sealed or failed, appends one log row (l.534–538). A referral that is held or waiting on not_before is skipped before any row is written (l.452–455).
- **Ship's "about 259 more writes": INFERRED, and the arithmetic holds.** The 1:13 PM backup has 424 rows; bref_94 holds indexes 183–423 (P/INDEX A3). Trimming starts after 76 more rows (424 + 76 = 500). The first bref_94 row drops after 183 more beyond that, so 76 + 183 = 259. The live ledger is already about 3–4 rows past 424 (166,094 B against 164,706 B; INFERRED from Ship's average row size), so the margin is about 255.
  - This assumes one row per hearing and no other writer. Because 94ce is held, only other referrals' hearings add rows.
- **Are the bref_94 rows already preserved?**
  - KNOWN: yes, all 220. The 1:13 PM backup was never trimmed (424 < 500), and its last row is 4:23:36 AM. Its exact copy [ID] is on the box at 0444 (Audit check [ID] ties it to the VM by decode) and is also tar member 1.
  - The 171 bundles are a different record (ruling texts, not log rows). On the box they exist only under [PRIVATE-PATH] (a.tar.xz [ID], mode 0600). That location is volatile: lost on a box reboot (P/MANIFEST §F, INFERRED). A bucket object with the same sha remains in atlas-deploy (RELAYED).
- **What would be lost if the VM-only items are not read soon.** None of these is a bref_94 log row.
  1. **xai-calls.jsonl (G4):** per-call model, cost and time for the 647–655 overnight calls. No backup is known (UNKNOWN), and its rotation is UNKNOWN. It is the only per-hearing cost record; the ledger has none ([ID]). This is the item with the highest unique-loss risk.
  2. **Live ledger (G1):** about 3–4 rows after 1:13 PM (INFERRED; they include the ea1558 hearing and possibly the 2 unexplained calls after 1:33:47 PM), plus the current tries, held and not_before state. These are the newest rows, so they are trimmed last. But from 12:01 AM Oct 28 the queued referrals' not_before expires ([ID] l.23), hearings resume, and the live state starts to change. The older Oct 21–26 rows of other referrals start trimming after about 76 hearings (INFERRED).
  3. **The 50 court roots (G6), the only record of why 49 attempts failed:** no backup is known. New failed roots will be added once hearings resume; cleanup policy is UNKNOWN; disk is at 79% (PRESERVATION-NOTICE-1).
  4. **alerts.jsonl and court.log after 1:13 PM (G2, G3):** the 1:13 PM VM backups cover the overnight. Loss risk is rotation, which is UNKNOWN.
  5. **Live cap22 check, courtwatch and model (G9):** overwritten by the revert timer at 12:00 AM Oct 28 (P/INDEX (a)7, KNOWN). The cap22 backup folder holds orig/new (G11, by name only). These are post-hearing files, so their relevance is low.
  6. **Per-hearing inputs (G5):** inbox/rehear and progress files are rewritten in place (INFERRED). With 94ce held, the last state should hold, but that is UNKNOWN.
- **Effect of ORDER-003 §4:** every gap counts against no one and "will not be filled by presumption in either direction". So any fact Atlas or the Respondent may rely on must come from a produced record. Atlas's interest in a complete and truthful record makes production before 12:01 AM Oct 28 the practical deadline (INFERRED). Ship's proposal is one bucket copy of G1–G12, capped at 6 calls, with 16 of 40 calls left (P/GAPS). It is the cheapest route, and it needs Clinton's own yes.

## 4. Evidence map: the runtime Magistrate across the hearings (no findings)
**Outcome pattern (KNOWN, T:HEARINGS-bref94.tsv, my own count):**
- Oct 26, 2:39:51–2:44:52 PM: 5 rows, NARROWED 2 and LAUNCH errors 3.
- Oct 27, 12:01:33–4:23:36 AM: 215 rows.
  - NARROWED 164.
  - STANDS 4, at 12:05:11, 12:29:10, 1:07:10 and 3:28:40 AM.
  - STAYED 1, row 216 at 4:18:36 AM (dec_1abe983b98b3).
  - LAUNCH errors 46 (AWAITING_CONTINUATION); the longest run of consecutive errors is 2.
  - The last row is NARROWED at 4:23:36 AM.
- 171 decision_ids across both days. Every sealed row has review NO_PROPOSAL. Counter is SPECIFIC except row 178 (TEMPLATE, 3:24:58 AM).
- Spacing: minimum 17.1 s, median 83.4 s (Ship, RELAYED; not recomputed).
- What the 171 rulings say: **UNKNOWN on this record.** Their texts are cited by sha and were not read by anyone producing them. The Respondent wants the STAYED hearing's input and output first (ORDER-003 §2(a)(4)).

**Tools and authority:**
- KNOWN (text): the only results are STANDS, NARROWED and STAYED (T:bailiff_referral.py l.47, l.553–555). She may narrow or stay "on your own motion" if she says so and ties it to a record fact (T:magistrate_provider.py l.43–45). She decides her own jurisdiction (Instruction l.37–41) and is independent (l.29–35). Her outputs may name lawful_next_actor and lawful_next_act, authority_granted and withheld, and prior_decision_id with a relationship such as RECONSIDERS or VACATES (l.86–93). She may only read; she cannot write, modify records or seal (A6, l.95–99).
- KNOWN (text): the SYSTEM prompt says "This is a demonstration on a synthetic practice matter; your ruling binds only that practice copy and never binds the Human" (provider l.54–55).
- KNOWN (my rg of four members): no injunct, escalat or notify term appears in court_service, magistrate_provider, authenticated_magistrate or magistrate_execution. lawful_next_* defaults to "Apply the disposition on the practice copy" (provider l.219–220).
- Whether any output field is read downstream: UNKNOWN. This is S2.
- A sealed result of any kind pops the referral's tries (court_service l.530–533, KNOWN). So whether a STAYED ruling affected the loop is INFERRED: it did not.
- Whether the Magistrate's authority binds software is a question of law reserved to JAQ-20261027-1 (ORDER-003 §5).

**Could she notice the repeats?**
- KNOWN (text): the SYSTEM prompt says "You have no earlier context" (provider l.49–50). Court history in her package is filtered to the same matter_id; seal refusals and failures are filtered to the same proceeding_id (T:package.py l.145–151).
- RELAYED (Ship, not checked by me): a fresh root, matter and Magistrate per attempt (court_service l.180–188, l.248, l.253–261).
- KNOWN (code): the engine's refusal reason, "no Human operational determination" (bailiff_referral l.836–838), is held engine-side.
- INFERRED (Ship): she could not see earlier hearings or the refusals.
- UNKNOWN until G5 and the bundle texts are produced: whether any prior hearing, count or refusal appeared in her input.
- CONFLICTED: the refusal reason is ALREADY_RULED in Ship's foundation record but the code reason above in Ship's index (ORDER-003 §2(a)(4)).

## 5. Respondent's S1–S6 and Atlas's position
- **Overlap with our R items:**
  - S1 (engine docket and refusal events) partly overlaps R7 (re-hear caller) and R1. The engine side is new.
  - S2 (custodian statement on downstream use of outputs) extends R6. It is new.
  - S3 (template root) equals G8 under R6.
  - S4 (box communications to or about the office) is new. It overlaps spend-matter records.
  - S5 (adoption of the retry law; the 2:15 PM direction) is new and resolves RECORD-INDEX C6.
  - S6 (50 roots mapped to hearings) equals G6 under R1.
- **Recommendation: do not object. File a short notice of no objection, and support S1–S6, before 12:00 PM PT 10/28.**
  - Every S item adds records that bear on ORDER-001 Q1–Q3.
  - ORDER-003 already applies Order 2's conditions to them, treats S2 as RELAYED until the Adjudicator checks it, and limits S4 to box records.
  - Under §4, missing records help no one. Atlas's interest is served by more production.
- **Optional comments in the same notice (not objections):**
  1. S4 copies should be produced by path and sha, without the custodian's characterization of what "should have reached" the office.
  2. Any cc-log extract under S4 goes through the private-name scrub with a log (Order 2 §3(7)).
  3. S2 statements should cite path:line in the produced tree, and give VM shas where G7 is resolved.

## 6. What Atlas should ask for (drafts for the parent; nothing filed)
1. **Notice of no objection to S1–S6**, due 10/28 12:00 PM PT, with the comments in §5.
2. **Preservation request to the Adjudicator, through Clerk:**
   - (a) Ship moves the 171-bundle archive ([ID], 696,452 B) from [PRIVATE-PATH] to a 0444 path under ship-notes/, with a sha check. This is box only, needs 0 server calls, and the bucket object is kept.
   - (b) Ship produces the box copy of diag-magistrate-1233 by sha and corrects G10 and INDEX (e).
   - (c) Ship states which tree is the engine copy (the v3c/f3b CONFLICT).
3. **Support Ship's recommended card to Clinton:** one bucket copy of G1–G12, capped at 6 calls and zero paid calls, ideally before 12:01 AM Oct 28. Priority order: xai-calls.jsonl, the 50 roots, the live ledger, alerts.jsonl, inputs, then the rest. That card is Clinton's decision; it is not Atlas's to make.

Atlas Counsel [ID]. Working paper, not filed.


