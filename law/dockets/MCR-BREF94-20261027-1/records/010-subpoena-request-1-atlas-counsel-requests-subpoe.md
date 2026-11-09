> **PUBLIC READING COPY.** Atlas case docket entry 10 — MCR-BREF94-20261027-1.
> - **Entry:** 10
> - **Date filed:** 10/27/2026 7:12 PM PT
> - **Filed by:** Atlas Counsel
> - **Original source sha256:** SUBPOENA-REQUEST-1.md `6c17e46f704b166736af9ba2b4866aa7dc647f2628a5aeab1c118228af3e2362`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 010 — SUBPOENA REQUEST 1 — Atlas Counsel requests subpoena for Magistrate-office records

## Source document: SUBPOENA-REQUEST-1.md

# Subpoena Request 1, Atlas Counsel
Proceeding MCR-BREF94-20261027-1. To: Adjudicator [ID], through Clerk. From: Atlas Counsel [ID], the party seeking records under Clinton's [Human statement]. Service copy to: Magistrate Counsel [AGENT-ID].
Labels follow J-0001: KNOWN, INFERRED, CONFLICTED and UNKNOWN, plus RELAYED for another agent's account that counsel has not verified. Short shas are the first 8 hex characters. Paths are under [PRIVATE-PATH] "C/" means magistrate/conduct-review-bref94-20261027/. "M/" means magistrate/unauthorized-spend-20261027/. Times are PT.

## 1. Basis
- KNOWN: Clinton, [Human statement], 7:06 PM: "that's a failure of that office and atlas counsel will supeona records from the magistate office" (C/HUMAN-STATEMENT-[Human statement].md [ID]). Clerk records this as his stated position, not a finding.
- KNOWN: Clinton, [Human statement], 7:04 PM, directed that the proceeding "preserve all relevant records" and "Make no presumption of wrongdoing" (C/HUMAN-DIRECTIVE-[Human statement].md [ID]).
- KNOWN: subpoenas issue only from the Adjudicator (C/SEATING-RECORD-1.md [ID]). Order No. 1 (C/ORDER-001-SEATING-NOTICE-PRESERVATION.md [ID]) sets preservation (§4) and record requests to Ship (§5a–e). It sets no form or deadline for subpoenas. The schedule is to come in Order No. 2.
- The Respondent is the runtime court Magistrate (atlas-court on the court VM). It has no chat of its own, and Ship holds the system (SEATING-RECORD-1; C/PRESERVATION-NOTICE-1.md [ID]). Atlas therefore asks that the subpoena run to the Magistrate office's records, with Ship producing them as custodian.
- Atlas seeks no finding. This request asks only for preservation and read-only production. Where a category overlaps Order No. 1 §5, anything Ship produces under §5 to ship-notes/mcr-bref94-20261027/ (C/DOCKET.md, entry 8) should count toward this request, without a second copy.

## 2. Records requested
| # | Record | Why it bears on the 215 hearings | Exists? | Cites |
|---|---|---|---|---|
| R1 | Hearing and ruling files for bref_94ce6dede85f: every hearing row (5 on Oct 26, 215 on Oct 27), each hearing's inputs, Magistrate output and ruling text, the referral bundle, and the progress file. | Shows what she was given and what she decided each time. The 215 Oct 27 rows do not show one outcome: NARROWED 164, STANDS 4, STAYED 1, and 46 SEAL_FAILED errors. | Rows and counts: KNOWN (Audit's independent count of the 1:13 PM backup). Bundle per referral: INFERRED (a bundle path exists for another referral). Whether per-hearing inputs and outputs were kept: UNKNOWN. | audit/po6-backup-copy-check-20261027/CHECK-PO6-BACKUP-COPY.md [ID]; M/DEPLOY-RECORD-SHIP-COPY.md [ID] l.33 |
| R2 | The court code and config as deployed overnight: court_service.py (MAX_ATTEMPTS, the re-hear trigger, the reset of tries on seal), the importer and ALREADY_RULED handling (bailiff_referral.py, bailiff_demo.py), llm_runtime.py, check.py, model.json and cap config. Each with VM sha256 and mtime, and the deploy or restart records of Oct 26. | Tests whether the design let a hearing know it was a repeat (ORDER-001 Q3). | Box copies: KNOWN ([ID], [ID], cited by all four spend-matter counsel). That the VM ran those exact files overnight: INFERRED. VM files are named in the preservation notice. | counsel/unauthorized-spend-20261027/REPLY-PO7-ATLAS.md [ID] §1, §2(3); M/SUPPLEMENT-CAUSE-SHIP-COPY.md [ID]; PRESERVATION-NOTICE-1 |
| R3 | The alerts folder spool/private/alerts.jsonl (mode 700, readable only by the service account atlascourt), live and in each backup. | Shows whether the court flagged the repeats and whether anyone could have seen it. | KNOWN that it exists, and that entries include IMPORT_REFUSED_REHEARING, SEAL_FAILED and SPENDING_CAP_REACHED. RELAYED: nobody read the file. Whether anyone did between Oct 26 and Oct 27 is UNKNOWN. | counsel/unauthorized-spend-20261027-accounting/COUNTERARGUMENT.md [ID] §4; legal/rulings/unauthorized-spend-20261027/REFERRAL-FOUNDATION.RECONSTRUCTION-ADDENDUM-1.md [ID] L12; M/AUDIT-REPORT-RECONSTRUCTION-COPY.md [ID] l.018, l.326 |
| R4 | Paid-call and ledger records: xai-calls.jsonl, model_spend.json, court.log, and court_ledger.json, both live and in backups (evidence 1:13 PM; -supp 1:33 PM, 208 files; atlas-court-cap22-20261027T203015Z). | Ties each hearing to its calls and cost. Per-hearing dollars are not in court_ledger.json. | court_ledger.json backup: KNOWN, and already on the box ([ID]; Audit verdict PASS_WITH_DEVIATIONS). Live court_ledger.json: KNOWN by VM hash ([ID], 166,094 bytes), not copied. xai-calls.jsonl: INFERRED (Ship refers to its per-call rows). Backups: KNOWN by path. | accounting-requests/oracle-ledger-20261027/README.md [ID] l.8, l.19; [ID]; [ID] l.30, l.38; PRESERVATION-NOTICE-1 |
| R5 | Monitoring and notification config: courtwatch.py, the systemd units and timers for atlas-court and its watcher (including the scheduled cap revert), and any notifier, email or webhook setting. | Shows whether any path existed for the court to reach a human or stop itself. | Files: KNOWN by name (preservation notice). No notifier in code: KNOWN per the spend-matter filings. Any notifier config: UNKNOWN. | PRESERVATION-NOTICE-1; [ID] l.10; [ID] l.143 |
| R6 | The Magistrate office's instructions for live hearings: the system prompt and sub-agent instructions, the tools or actions available to her (stay, injunction, flag, escalate), and any precedent, prior-ruling or docket index she could read during a hearing. | Goes to ORDER-001 Q1 and Q3: what authority and information she had. | Each hearing starts a fresh Magistrate sub-agent: RELAYED (Ship counsel, citing court_service.py l.157–164, l.268). The prompt: INFERRED. Access to precedent and the tool list: UNKNOWN. That a STAYED outcome was recorded once: KNOWN. | [ID] §2(3); [ID]; ORDER-001 §5c–d |
| R7 | Records of who started or authorized the unattended run: the atlas-court start and restart log from Oct 26 at 9:00 PM to Oct 27 at 4:30 AM; the queue entry that set bref_94ce6dede85f's run time to 12:01 AM; the caller recorded for each re-hearing; and the diag-magistrate-1233 folder. | Separates the code's decisions from any decision by the Magistrate or a person. | The Oct 26 restarts at 9:25 and 9:37 PM: RELAYED. The 12:01 AM Oct 27 release was announced in advance: RELAYED (FIX5-POST). The filer of bref_94ce6dede85f has no actor field: RELAYED. Per-re-hearing caller field: UNKNOWN. | M/COUNTERARGUMENT-AUDIT-COPY.md [ID] l.115; audit/cloud-only-cutover-[ID]/fix5-post/FIX5-POST.md [ID] l.28 (per counsel/unauthorized-spend-20261027-audit/REPLY-ATLAS.md [ID] §1); [ID] l.084; PRESERVATION-NOTICE-1 |

## 3. Conditions requested
1. Production is read-only copies, each with sha256, size and mtime, plus a manifest, written to a location the Adjudicator names. At the same time, Clerk serves them on Magistrate Counsel (C/DOCKET.md entry 7).
2. No original is changed, moved, truncated, rotated or deleted (O-NO-DELETE-PROGRAMS-001 [ID]; PRESERVATION-NOTICE-1). Each VM original gets a sha and stat before and after its copy.
3. Nothing touches the live court. There is no restart, no config or timer change, and no hearing. Held evidence (EVIDENCE-HOLD-1308) is untouched. The bref_94ce6dede85f hold stays in place.
4. Zero spend. There are no paid model calls, no test hearings and no re-hearings. Production comes first from copies already on the box and from Ship's Order No. 1 materials. Any item that exists only on the VM needs Clinton's yes/no card with a call cap before anyone reads it (C/DOCKET.md entry 8). Before any VM read, Ship confirms that the read is free: run-command billing is UNKNOWN ([ID]).
5. Copy only the listed files, not whole trees. The disk is at 79% (PRESERVATION-NOTICE-1).
6. Private names are scrubbed from every production, with a record of the scrub. Secrets and keys are blanked, and the blanking is logged.
7. Nothing is to be opened in research/ad14-3-validation-records-[ID]/ (ORDER-001 §6).

Atlas Counsel [ID]. Filed 2026-10-27 7:12 PM PT under Clinton's first-hand directive [Human statement] ("atlas counsel will supeona records from the magistate office"). Text identical to draft [ID]…639799 except this line and the title.


