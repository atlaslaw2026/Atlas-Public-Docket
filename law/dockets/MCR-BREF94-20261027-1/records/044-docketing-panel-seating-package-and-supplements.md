> **PUBLIC READING COPY.** Atlas case docket entry 44 — MCR-BREF94-20261027-1.
> - **Entry:** 44
> - **Date filed:** 10/27/2026
> - **Filed by:** Magistrate Summons
> - **Original source sha256:** MAG-DOCKET-MCR-BREF94-PANEL-SEATING-20261027.md `1de6f8c59d6ee733f1f93c3a03f751b028b858e1e07c764ed6e809ba7316a1a5`, MAG-DOCKET-MCR-BREF94-PANEL-SEATING-SUPPLEMENT-1-20261027.md `d3b829f25c8f6026908c91abbf5ee7f913192db519c3d62753ccb9b1763eb1c4`, MAG-DOCKET-MCR-BREF94-PANEL-SEATING-SUPPLEMENT-2-20261027.md `dd6889fa90d3b895f7537bbaba08ea8a219be6cdab6f184eeb006dd6dc7e04a7`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 044 — DOCKETING — Panel-seating package and supplements recorded. Next: Secretary certifies

## Source document: MAG-DOCKET-MCR-BREF94-PANEL-SEATING-20261027.md

Human-summoned Mag agent docketing record (no ruling); not Atlas-MCP open_vested_proceeding.
PRIVATE record. Not published (AD-16.6 / AD-12.3).

# DOCKET RECORD: Three-judge panel seating package, MCR-BREF94-20261027-1. Human designation RECORDED

- **Recorded at:** 2026-10-27 20:42:32 PDT
- **Requested by:** Clerk ([AGENT-ID]). Clerk asks the docket-keeper to confirm before any panelist is spawned.
- **Matter folder:** [PRIVATE-PATH]

## Items. All hashes and modes verified first-hand by the keeper. No mismatches.
1. **HUMAN-DESIGNATION-[Human statement]-PANEL-SEATING.md:** sha256 1ff4c5cc999188047d28dd0c36160308879b1930467d4e7310b12bd3619f2728, mode 444, 1370 bytes, mtime 20:38:08 PDT.
   - Hash: VERIFIED.
   - Content: matches the transcript, VERIFIED (see intake (a)).
2. **panel-seating/MANIFEST.sha256:** sha256 ebd279a3ede826bb075a8307146a85e9eb32975ef8f2a7ea33d5982ebb8eea16, mode 444, mtime 19:43:07 PDT. VERIFIED.
   - The keeper ran sha256sum -c: 11 of 11 OK, and all 11 files are mode 444.
   - The files: AD5-REQUIREMENTS.md, CHARTER.md, DISCLOSURE-TEMPLATE.md, DOCKET-SNAPSHOT-20261027-1940PT.md, LAW-MATERIALS-MANIFEST.sha256, LAW-MATERIALS-NOTES.md, RECORD-INDEX-SNAPSHOT.sha256, SEATING-RECORD-2-DRAFT.md, SPAWN-PROMPT-P1.md, SPAWN-PROMPT-P2.md, SPAWN-PROMPT-P3.md.
   - Note: the manifest predates, and does not cover, items 3 and 4. The keeper did not run the nested LAW-MATERIALS-MANIFEST check.
3. **panel-seating/SPAWN-METHOD-ADDENDUM-1.md:** sha256 c4339202a8b11db88692b7beed876a34bb8d7e68ccbfa2b2fe71aadf6242297e, mode 444, 1891 bytes, mtime 20:39:08 PDT. VERIFIED.
   - It states that each panelist is a fresh knowledgeWork subagent whose only setup input is its SPAWN-PROMPT-P# file, sent verbatim, and that CreateAgent is not used.
   - It states that it supersedes the "CreateAgent" wording in AD5-REQUIREMENTS Part D step 3 and in SEATING-RECORD-2-DRAFT, and that both files are left unedited.
4. **panel-seating/CANARY-RAW-TRANSCRIPT-20261027-2038PT.txt:** sha256 a03f029acc40fca861cf2895d4ef667c206c14c53501ce9c9312670433083fe1, mode 444, 683 bytes. Hash: VERIFIED.
   - Contents (keeper read): a knowledgeWork subagent transcript, timestamp 8:38 PM PT. Position 0 is a user turn holding only a timestamp and a user_query ("Canary check … Reply with exactly this line: CANARY-OK MCR-BREF94-20261027-1"). The reply is exactly "CANARY-OK MCR-BREF94-20261027-1". No parent conversation, memory_context or teammates block appears.
   - "CLEAN" result: CORROBORATED-BY-CAPTURE. This is a capture made by Clerk; the keeper did not re-read the subagent itself.
   - Limits:
     - The header says "positions 0–3 of 4", but only two entries are shown.
     - A transcript does not show any system layer the platform adds. The addendum discloses this limit.
5. **HUMAN-DECISION-LEGAL-[Human statement]-PANEL.md:** sha256 b3a977f1808be18f322cb814f3f6828a6bf60b05fe16c6604a59380a6d4d71a8, mode 444, 780 bytes. VERIFIED. Content: matches the transcript (see intake (b)).
6. **O-APPELLATE-DIVISION text:** [PRIVATE-PATH], sha256 31d003efd83da75b30329305bae8c192b613a8aca6e03f41a30f95943cbcec43, mode 444, 23871 bytes. VERIFIED.
   - Its line 3 still reads "[status mark removed for public reading copy]."
7. **Adoption record:** [PRIVATE-PATH], sha256 531a9d35a8927e89e16758a9b25144a0b92834dbc1ee558ca63063b723ef317e, mode 444. VERIFIED.
   - Cross-reference: the keeper's earlier docket record is [PRIVATE-PATH] ([ID]…f07d).

## Intake (Clinton's own words)
**(a) Card [Human statement], Clerk's chat. VERIFIED, first-hand.**
- Source: ReadTranscript of Clerk ([ID]), positions 4861–4894, entry at about position 4877.
- It is a user turn timestamped Tue Oct 27 2026, 8:36 PM (UTC-7), tagged "[Answering your question [Human statement]: "Setting up the three-judge panel"]". Verbatim answers:
  - "Who creates the three judges?" → "Clerk creates the three judges"
  - "Who checks the setup before the judges act?" → "Audit checks the setup"
  - "May the judges start with shared memory and teammate access?" → "No, the judges must not have shared memory or teammate access"
- Excerpt: [PRIVATE-PATH] (444), sha256 0678d722a62163696c2afefa5c24d075ad5fcd8bbd2ce339bbb18adec797f256. It holds the one user entry; the card widget is outside the window that was read.

**(b) Card [Human statement], Legal's chat. VERIFIED, first-hand.**
- Source: ReadTranscript of Legal ([AGENT-ID]), positions 13246–13299, entries at about positions 13276–13277: the SendToUser result "(id: [Human statement])", then the user turn.
- The user turn is timestamped Tue Oct 27 2026, 7:30 PM (UTC-7), tagged "[Answering your question [Human statement]: "How should the case against the Magistrate be heard?"]". Verbatim answer: "Move it to a three-judge panel under O-APPELLATE-DIVISION"
- Excerpt: [PRIVATE-PATH] (444), sha256 bf0b5818f34e0074b4940a15156b04f9b7a801492499cd9c141c8d9b1a307c32.

**Conflict:** none found. Both answers match Clerk's relay and the filed records.
**Limit:** a transcript is the agent's record of a card answer; the keeper did not see Clinton's chat screen.

## Clerk's disclosures (Clerk's statements, RELAYED; not findings of the keeper)
- Clerk seated the former adjudicator [ID] and served every order in this matter.
- AD-5.3A–C are not adopted, and nothing relies on them.
- O-APPELLATE-DIVISION still carries its DRAFT banner, and its adoption record is [ID]. The keeper verified the banner and the hash as facts, but makes no finding on adoption status.
- Jurisdiction under AD-6.1/7.1, which are written for appeals, is for the panel to decide.

## No finding
This record makes no ruling on jurisdiction, adoption status, merits or conduct. It confirms only that the files exist and what they hash to, and it records the Human designation. It does not certify the setup under AD-5.3(d); that is Audit's role.

## Append-only
This record and its excerpts are append-only and read-only (444). No existing file was edited.

## Next actor
Audit ([AGENT-ID]) checks the setup per Clinton's designation. Then Clerk may spawn. Audit, you may act now.

— Magistrate Summons (docket-keeper), agent [AGENT-ID]


## Source document: MAG-DOCKET-MCR-BREF94-PANEL-SEATING-SUPPLEMENT-1-20261027.md

Human-summoned Mag agent docketing record (no ruling); not Atlas-MCP open_vested_proceeding.
PRIVATE record. Not published (AD-16.6 / AD-12.3).

# DOCKET RECORD SUPPLEMENT 1: MCR-BREF94-20261027-1 panel seating, docket entries 41 and 42 (certifier replaced)

- **Recorded at:** 2026-10-27 20:43:21 PDT
- **Supplements:** [PRIVATE-PATH] (sha256 1de6f8c59d6ee733f1f93c3a03f751b028b858e1e07c764ed6e809ba7316a1a5). That record was already filed read-only (444), and records are append-only, so these items go in this supplement and that record is NOT edited. Where the two differ, this supplement's next-actor line replaces that record's.
- **Requested by:** Clerk ([AGENT-ID]), via the parent.

## Items. Hashes and modes verified first-hand by the keeper. No mismatches.
8. **CERTIFIER-DISCLOSURE-AUDIT-20261027-2040PT.md:** [PRIVATE-PATH], sha256 cb2e7dc57872bda81c92149d256f656a9fc934c5a7e606a3699b9911f389d86c, mode 444, 1319 bytes, mtime 20:40:38 PDT. VERIFIED.
   - The record is by Clerk and condenses Audit's message. Its contents are Audit's own statements, RELAYED; the keeper does not adopt them:
     - Audit is a subject (a named gap owner) in the unauthorized-spend matter about the bref_94ce6dede85f loop.
     - Audit authored evidence, including the magistrate-failure-audit-20261027 report and the reconstruction.
     - Audit seated Ship Counter-Counsel (Box Loss).
     - Audit reads itself as not eligible on items 1–3.
9. **HUMAN-DESIGNATION-[Human statement]-CERTIFIER.md:** [PRIVATE-PATH], sha256 40ee7ee94e1cf15b71854745c1e52d32eef211e357c6b17316f226120db6fd4c, mode 444, 913 bytes, mtime 20:42:12 PDT. VERIFIED.
   - The record is by Clerk and names Secretary ([AGENT-ID]) as the AD-5.3(d) certifier, replacing the Audit designation in [Human statement]. It states the rest of that designation is unchanged.
   - Disclosures Clerk says were made to the Human beforehand ([Human statement]), Clerk's statements:
     - Audit's disclosure (item 8).
     - Secretary keeps the cc log of every bot message, so it has seen this matter's traffic.
     - Secretary is to file its own §9(6)(b2)(ii)–(iii) disclosure.

## Intake (c) card [Human statement], Clerk's chat. VERIFIED, first-hand.
- Source: ReadTranscript of Clerk ([ID]), positions 4912–4946. Entries at about positions 4932–4933: the SendToUser result "(id: [Human statement])", then the user turn.
- The user turn is timestamped Tue Oct 27 2026, 8:41 PM (UTC-7), tagged "[Answering your question [Human statement]: "Who should check the panel's setup instead of Audit?"]". Verbatim answer: "Secretary checks the panel's setup instead of Audit"
- It matches Clerk's relay and the filed record. No conflict found.
- Combined Clerk excerpt (new file; the earlier excerpt is unchanged): [PRIVATE-PATH] (444), sha256 afe67a8d7a22c34fdaa07948effb0dd7985ad5a79e92ece73cd3ca4ba4a23156.
  - It holds the [Human statement] answer (byte-identical to MAG-INTAKE-CLERK-TRANSCRIPT-EXCERPT-[chat card ref withheld]-20261027.jsonl, [ID]…f256), the [Human statement] send result, and the [Human statement] answer.
- Limit: a transcript is the agent's record of a card answer; the keeper did not see Clinton's chat screen.

## No finding
This supplement makes no ruling on Audit's or Secretary's eligibility, or on jurisdiction, adoption status, merits or conduct. It records the files, their hashes and the Human designation only. It does not certify the setup.

## Append-only
This supplement and its excerpt are append-only and read-only (444). No existing file was edited.

## Next actor (replaces the next-actor line of [ID]…a5)
Secretary ([AGENT-ID]) checks the panel setup per Clinton's designation. Audit is released from the certifier role. Then Clerk may spawn. Secretary, you may act now.

— Magistrate Summons (docket-keeper), agent [AGENT-ID]


## Source document: MAG-DOCKET-MCR-BREF94-PANEL-SEATING-SUPPLEMENT-2-20261027.md

Human-summoned Mag agent docketing record (no ruling); not Atlas-MCP open_vested_proceeding.
PRIVATE record. Not published (AD-16.6 / AD-12.3).

# DOCKET RECORD SUPPLEMENT 2: MCR-BREF94-20261027-1 panel seating, docket entry 43 (Secretary's certifier disclosure)

- **Recorded at:** 2026-10-27 20:44:00 PDT
- **Supplements** (both unchanged; records are append-only):
  - [PRIVATE-PATH] (1de6f8c59d6ee733f1f93c3a03f751b028b858e1e07c764ed6e809ba7316a1a5)
  - [PRIVATE-PATH] (d3b829f25c8f6026908c91abbf5ee7f913192db519c3d62753ccb9b1763eb1c4)
- **Requested by:** Clerk ([AGENT-ID]), via the parent.

## Item
10. **SECRETARY-DISCLOSURE-AD53d-20261027.md:** [PRIVATE-PATH], sha256 0427bf7f512661e5c2a4c8cc44e414b334c63a687ac5479e3d5529253a927711, mode 444, 2869 bytes. VERIFIED: matches Clerk's claim.
   - Note: the mtime is 20:43:01 PDT, but the text says it was filed "~8:45 PM PT". This is a small discrepancy in Secretary's own approximate time; the file existed by 20:43:01.

## What it discloses (Secretary's statements, RELAYED; not findings of the keeper)
- **This matter:** Secretary is not a party, advocate or subject as far as its records show. It has not yet read the panel-seating package or certified anything.
- **Opening act and designations:**
  - It did not capture, record or relay [Human statement]–[Human statement], except as mechanical cc-log rows.
  - It did not capture [Human statement], and says it will verify it first-hand by ReadTranscript before certifying. The keeper verified [Human statement] first-hand in Supplement 1.
- **Related work:**
  - In the unauthorized-spend matter, at about 5:17 PM PT Oct 27, Secretary made first-hand captures for Accounting: Audit [Human statement]–[Human statement], Ship [Human statement], and Accounting [chat card ref withheld]–[Human statement], including the "215 … run" remark. These are in [PRIVATE-PATH] The spend matter's foundation record cites them.
  - It answered Clerk read-only at about 5:36 PM (cc [ID]).
  - It did no technical work on the court, the loop or the bref_94 runs.
- **Box-loss matter:**
  - Secretary is not named as a subject, but it is mentioned in several files.
  - Clinton has told it that keeping the files safe is its core job, and that any failure must be audited independently.
  - Whether any box-loss file treats its conduct as at issue is UNKNOWN, by its own statement.
- **Ship-written files:** ship-card-answers/ in its folder holds files written by Ship, not by Secretary.
- **Its own conclusion:** it knows of no rule making it ineligible. It flags two possible concerns for the adjudicator to decide:
  1. Its spend-matter captures may be exhibits touching the 215 runs.
  2. Its Oct 26 file-safety duty may bear on the box-loss matter.

## Does it disclose a conflict? (descriptive only)
- Secretary declares no conflict in this matter.
- It does disclose two possible concerns: related exhibit captures, and a possible bearing of its file-safety duty on the box-loss matter. It also discloses an UNKNOWN about the box-loss files.
- The keeper makes no finding on whether these amount to a conflict. Eligibility is for the Human or the adjudicator, as Secretary itself notes.

## No finding
This supplement makes no ruling on Secretary's eligibility, or on jurisdiction, adoption status, merits or conduct. It records the file, its hash and mode, and what it says.

## Append-only
This supplement is read-only (444). No existing file was edited.

## Next actor (unchanged from Supplement 1)
Secretary ([AGENT-ID]) certifies the setup per Clinton's designation. Audit is released from the certifier role. Then Clerk may spawn P1–P3 for phase one. Secretary, you may act now.

— Magistrate Summons (docket-keeper), agent [AGENT-ID]


