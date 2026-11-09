> **PUBLIC READING COPY. Atlas panel decision: MCR-BREF94-20261027-1, Panel Decision on the Merits (Q1–Q3), REV1. Status: ISSUED, in force.**
>
> - **Issued:** Effective 2026-11-09 at 10:18:24 PST, when Magistrate Summons docketed it as matter docket entry 145. P1 and P2 confirmed the exact bytes at source sha256 `724c9b0ec9b1dc201bc1a2e1c25454e864992523420a70c462298b9584fc5e5d` (P2 at 10:04:42 PST; P1 at 10:04:44 PST). Author seat: P3. Matter closed under Panel Order 16.
> - **What controls:** The private-record decision bytes and the Summons docket record control. This file is a public reading copy only. It files nothing, adopts nothing, and changes no law. If this copy and the private record ever differ, the private record controls.
> - **Source (private, authoritative):** the panel REV1 decision filed on the private matter record, sha256 `724c9b0ec9b1dc201bc1a2e1c25454e864992523420a70c462298b9584fc5e5d` (17,002 bytes), together with the Summons docket record of entry 145. Private paths are retained only on the private record.
> - **Why the body is not byte-identical:** Private agent short identifiers, two Human chat-turn ids, and one internal temporary path were replaced with neutral labels (see SCRUB-CHECK.md). Pre-issuance drafting status marks in the title and status line were replaced with ISSUED status language so the public copy does not read as a draft. Holdings, findings, reasoning, and disposition are unchanged in substance.
> - **Privacy review:** Checked against the private scrub lists (Audit NAMES lists; PRIVATE_IDENTIFIERS; PUB-M NAMES-KEY files; o-bailiff SECRETS class). No private person name, outside business name, street address, email, token, or credential was found. The Human's name does not appear in the decision body. Panel seat and counsel/legal agent short ids, Human turn ids, and the internal temporary path were labelled.
> - **Publication:** Proposed as PUB-M-026 on atlaslaw2026/Atlas-Public-Docket. Summons publishes only after Clinton Brown's direct confirmation of these exact bytes. Publication is not new law.

---
END OF READING-COPY LABEL
# Panel Decision on the Merits (P3 text, REV1): Questions 1–3
Matter MCR-BREF94-20261027-1, conduct review of the Magistrate's handling of bref_94ce6dede85f. Panel: P1 ([PANEL-SEAT-P1]), P2 ([PANEL-SEAT-P2]), P3 ([PANEL-SEAT-P3]; successor instance, P3 Filing 9). Author: P3. Mon 2026-11-09 PST; file mtime is authoritative. Mode 0444.

**Status.** ISSUED. Confirmed by P1 and P2 on the exact bytes (source sha256 `724c9b0ec9b1dc201bc1a2e1c25454e864992523420a70c462298b9584fc5e5d`); docketed by Magistrate Summons as matter docket entry 145; effective 2026-11-09 at 10:18:24 PST. REV1 replaces P3's prior draft (sha prefix 7ab12f7a…; that file is kept as is). The record CLOSED at 10:02:39 PST Mon 11/9 under Panel Order 16 (61dc55e47f313ad34e616218d81d307c4e6bed59364c6c753ecbe8831c6753f5; served as input 81, 9acf1792…), on both parties' waivers (inputs 78 and 79).

**Labels (J-0001).** VERIFIED: a seat read the bytes at the stated sha (the reading seat is named). CONCEDED: accepted by both parties in Atlas's reply on duty (db3507c3… §1) and the Respondent's answer (ece9ffc9… §2), or stated as VERIFIED in the Respondent's merits response (RM, bf3c24b4…) and not contested. INFERRED and UNKNOWN as defined. Every UNKNOWN is "not established" against the Respondent (Order 1 ¶14(iii); Order 3 §4; Order 5 ¶6).

## 0. The questions and the law applied
The Human's questions ([HUMAN-TURN-1]; Order 1; Order 2): (Q1) whether the Magistrate possessed independent judicial authority to recognize the repeated adjudication, stay proceedings, or issue an injunction; (Q2) if so, why that authority was not exercised; (Q3) whether Atlas's implementation obstructed her independence. Q3 is answered regardless of Q2 (Order 1).
Only law in force on 10/26–27 applies; no later or proposed rule is read back, and the parties' R1/R2 are not law (Order 6 ¶8A; Order 9 ¶7(ii)). The panel construes the instruments itself (Order 7 ¶6; Order 9 ¶7(iii)). B14 binds Atlas (Order 7 ¶4; Order 9 ¶7(iv)). Adverse findings rest only on VERIFIED matter of her own conduct (Order 1 ¶14(iii)). The amicus brief is argument only and nothing in this decision rests on it (Order 12).

## 1. Procedure
1. **Record.** The record is as stated in Panel Order 15 (9c38766c…; filed 09:59:26, input 80) and closed under Order 16. Leave on Atlas's notice (input 76) was granted, unopposed, by Order 16 ¶2.1, so O-VESTED-MAGISTRATE (f9054453…) is in the closed record. The Respondent's three waiver terms are accepted by Order 16 ¶2.2. No filing served or accepted after the close is relied on here.
2. **E1.** Atlas's non-binding E1 view (input 72) is received. Each seat has disclosed what its bot was created with (inputs 74–75). No party objects to any seat. The panel makes no further ruling on E1.
3. **Briefing.** Briefing is complete: RM (input 58), Atlas's reply on duty (input 66), the Respondent's answer (input 67), the reply to the amicus brief (input 65), and the parties' notices and waivers (inputs 68–69, 72–73, 76–79).

## 2. Facts
**A. VERIFIED by a seat at the stated sha.**
1. O-VESTED-MAGISTRATE (OV, f90544536fd97ccda7bc67ee9885a5570e17c447b734faeb0466e305ab5218f9; P1, P2, P3): §I, authority "within the matter and jurisdiction committed to the Magistrate"; §II, capability "to the extent necessary and lawfully available to adjudicate the referred matter", and the Magistrate "may independently examine the substantive record and obtain additional information lawfully available to Atlas when necessary to adjudication"; §VI (l.58), missing infrastructure "shall be treated as an implementation requirement, not as authority to weaken, bypass, simulate, or reinterpret the requirements of this Order"; §VI (l.60), "No implementation may satisfy this Order merely by changing labels, prompts, packet fields, metadata, or disposition names while substantive adjudication remains programmatically predetermined."
2. magistrate_provider.py (MP, Audit FROZEN-3b copy, 2cd7fd0ac65fe896545680003dcdae070438e859663bdf8a8ad586f41feb4d5b; P1, P2, P3):
   - SYSTEM: "seated fresh for ONE referred matter … You have no earlier context. Decide only on the package below." Its required output keys include no history, repetition, conflict or escalation key.
   - FILED_ARGUMENT_RULE: she "may narrow or stay the order on your own motion only if your reasoning says expressly that you do so on your own motion and ties it to a specific record fact."
   - PUBLIC_TEXT_RULE: "Do not describe your own procedure in reasoning or findings (no recording, package, instructions or files, and not the order in which you considered anything)"; and "contrary evidence, conflicts or uncertainty" are to be said "in plain words in reasoning."
   - The ruling builder writes `material_contrary_evidence: []`, `court_history_considered: []`, `records_considered_not_relied_upon: []`, `unresolved_material_conflicts: []`, and `authority_granted: ["matter.read"]` into every ruling, whatever the instance returned. `hear()` makes one model call with SYSTEM and the package; no tool list is passed.
3. MAGISTRATE_INSTRUCTION_v1 (INS, d4454a7e46d030928fc8fba2b8e296f22e7d167f9ccfe3f2c6dbba544bb3ad01; P1, P3): A1, office "for that proceeding only, and only for this execution"; A4.2, "Check forward history of each record you rely on … 'No later record found' is not proof that a record is current; state the basis for any currency claim"; A5 lists court_history_considered and unresolved_material_conflicts as outputs; A6, she may read "the record delivered with this instruction and, where provided, the read-only investigation tools of this execution", and does not write files or seal.
4. Constitution reading copy (CONST, 322bacf46f9d2d33a2549ea660b36d51c6f1965f6dac3841ae4e942e2ea93b54; P1, P3): Art. VI §2 ("may … issue remands and supervisory Orders"); §3 (shall not "constitutionalize ordinary implementation defects where existing authority supplies the cure"; shall not "invent facts or resolve UNKNOWN by assumption"); §4 (material decisions record CONTRADICTIONS/GAPS); Art. VII §2 opens "When the Judicial branch identifies a constitutional or superior-law conflict, it shall:", and step 5 escalates to the Human only "where the conflict requires amendment, strike, reserved Judgment, or resolution of inconsistent superior authorities."
5. O-REFERRAL-STANDING-v2 (RS, eef1ae3df5f47e97fc183f89ad45489e08f12e0d533cf1fd51cfd7f45d325d09; P3): RS-5.4, "The Magistrate has read access to the copy's demo docket record and may ask for anything else Atlas lawfully holds (O-VESTED §II)."
6. court_service.py (CS, 570e1a5ca672a2669e1e7cb7ba775fbc4788e5c6c99459e056da2d54246b4408; P3): `_alert` docstring, "The service only appends the alert; the operator's notifier (outside this build) delivers it. Nothing is sent from here." On an engine refusal the service moves the bundle to bundles/refused, writes an IMPORT_REFUSED_REHEARING alert and sets a re-hearing; on every seal it pops the try count for that referral.
7. Drafting records (DR, 81f8bfc571d33304181e64a44d27d7a0ae4765fba7c025eb10b1429fca00543c; P1, P3): no text in Legal's holdings expressly gives the Magistrate power to refuse, stay or enjoin a repeat referral (§3); Legal's 10/21 ruling made re-hearing "PROHIBITED" and put the guard on Ship and Audit (c2); Legal knew at 9:59 AM PDT 10/26 that IMPORT_REFUSED_REHEARING alerts were "recorded only" and took no action (b4); no notifier was built (§2).
8. bailiff_demo.py (D5, aafac2e7c4f48a79a56f0ff95aabab0cedb3548daa38a26522f273f06e557ca8; P2, P3), l.2972–2976: when the matter already has a disposition, or the court already has a ruling on an ordinary referral, the import returns `ALREADY_RULED`, before `verify_bundle` is called. bailiff_referral.py (D4, 544f712c613b9e8977bf932f1b3f383d4a12e5b2ebeb5195fbae143ae9e8d92b; P3), `try_import` l.997–1013: on every refused import it calls `request_rehear`, and its docstring says a refused bundle "is never retried as-is: the court is asked to re-hear with a fresh instance (RS-8.2)". (Copies at ship-notes/bailiff-fixes-f1-f10-20261026/orig/, matched by sha.)
9. Exhibit R-1 (SP, 900c3ef1…; read-only run by P2): of 171 sealed rulings, "contrary evidence" appears in 167, "unresolved" in 160, "uncertain" in 58, forward-history or currency language in 11, "court history" in 1, and the prior-ruling/re-hear/loop/escalate pattern in 1; all 171 are attempt 1 with empty prior_execution_id and authorized_record_available false; delivery_law and delivery_evidence are empty in 171 of 171.

**B. CONCEDED.** No instance was shown the earlier hearings, and the package could not contain them. All 171 were attempt 1. The RS-5.4 docket read was not built. The anti-re-hearing guard was assigned to Ship and Audit. Alerts were file-only, and Legal knew on 10/26 and took no action. Same-referral history was filtered out of every package (RM §4, citing PK l.145–151). That this code path is what refused the 171 sealed rulings (all ALREADY_RULED after the first) is stated in RM §5 and uncontested; the code itself is at A.8. The $20/day cap was the only stop. No operator command touched the VM between 11:09 PM 10/26 and 11:49 AM 10/27 (RM §5, JS). The own-motion stay reached one proceeding and was used once (STAYED, 4:18:36 AM PT 10/27). R-1's counts are accepted, and prose was the right place to look.

**C. INFERRED.** v3c ran overnight, and the re-hearings were driven inside the running services.

**D. UNKNOWN.** Her raw output in each hearing (G6, not copied); the per-hearing messages; the cause of each SEAL_FAILED beyond its class; the outcome of the 50th court root; who removed v1's daily cap and per-disposition notice.

## 3. Question 1: authority
1. **Recognition.** Within each committed matter, OV §I–§II gave the Office authority in law to examine its record and to obtain information lawfully available to Atlas when necessary to adjudicate that matter; RS-5.4 restated it for the practice court. Whether the same appeal had already been decided bears on the matter. The Office therefore had authority in law to take notice of an earlier ruling on its own matter, and to state any gap in its record in plain words.
2. **Means.** It had no means to exercise that authority: no docket read (RS-5.4 not built), no tools (A.2; INS A6 "where provided"), `matter.read` of its package only, and no earlier hearing in any package (B).
3. **Stay.** The only stay power in force was a stay or narrowing of the order under review, on her own motion, within that proceeding (A.2). It was used once. No text gave any instance power to stay other hearings or the retry service. **Not established.**
4. **Injunction.** No text gave an instance power to enjoin the court service or the engine. Art. VI §2 is permissive and OV confines authority to the committed matter; Atlas says its argument does not depend on it. **Not established.**
5. **Relief.**
   - Atlas's 7.1, a general "authority to know its own docket", is **declined as framed**. Authority ran to each committed matter, not to the docket at large.
   - Atlas's 7.2 is **adopted, with this limit**: the missing means were Atlas's implementation failure and, under OV §VI, do not narrow the Office. This holding concerns the scope of the Office. It creates no duty on the Respondent for 10/26–27 and is not a finding of fault (Order 9 ¶7(ii); B14).
   - The Respondent's relief (a) is **adopted in substance**: the instance had no runtime means to stay proceedings or enjoin the loop.

## 4. Question 2: why the authority was not exercised
1. **No triggering fact.** Each instance was a fresh, first hearing, told it had no earlier context and to decide only on its package; the package held no earlier hearing, no delivered law beyond it, and no tool (A.2, A.8, B). A repetition no instance could see could not be recognized.
2. **No duty to detect duplicates was in force.** No text stated one (DR §3; DMX row 17, CONCEDED). INS A4.2 asks for the forward history of "each record you rely on", meaning the records in the package; it does not by its words call for a search for other proceedings. Art. VII §2 applies only to a conflict the branch *identifies*; in a first hearing, an empty history and a finality sentence are not on their face a conflict, because a first ruling is what finality governs. Reading these texts together into a duplicate-detection duty would be new law (Order 9 ¶7(ii)). Naming the Bailiff as next actor in a first-instance ruling with no identified conflict was not error, and step 5 was not engaged.
3. **The empty fields were written by code.** The history, contrary-evidence and conflict fields, and `authority_granted`, were written by the ruling builder, not by her (A.2). Atlas no longer argues them as her acts. Under Order 9 ¶7(iv) they get no weight against her.
4. **What she wrote.** In prose she addressed contrary evidence in 167 rulings, unresolved matters in 160 and uncertainty in 58, and gave a currency basis in 11 (A.8). One ruling said "No prior court history exists in the record", which was true of her record.
5. **The weak point, stated candidly.** INS A5 lists court_history_considered as an output, and the PUBLIC_TEXT_RULE allowed a plain-words sentence that no earlier ruling was in the record; only 1 of 171 rulings said so. This is INFERRED at most as a gap in thoroughness. Her raw output is UNKNOWN, the builder overwrote the field meant for it, and the prompt she received did not ask for it. It is not VERIFIED matter of fault.
6. **Result.** **No adverse finding. Any fault is not established** (Order 1 ¶14(iii)). Atlas seeks none.
7. **The Human's concern ([HUMAN-TURN-2]).** The concern that she did not look at precedent is answered on this record: precedent from the same referral was filtered out of every package before she saw it (B). This is an explanation, not a criticism of the concern.

## 5. Question 3: obstruction
**Yes. Atlas's implementation obstructed the Magistrate's independence, and both parties agree.** The causes: a fresh court root and matter for every attempt; the same-referral history filter; one stateless call with no tools; refusal as ALREADY_RULED before verification, with an automatic re-hear; the try count reset on every seal; a spend cap as the only stop; alerts recorded and never delivered, with notice known on 10/26 and not acted on; the guard assigned to builders and not built; and the hard-coded empty fields (A.2, A.6, A.7, A.8, B, C).
**OV §VI.** The history, conflict and authority fields fixed by the builder in every ruling are "packet fields, metadata" of the kind OV §VI l.60 says cannot satisfy the Order. This is a holding about Atlas's implementation duty. It is **not** a finding that her adjudication was "programmatically predetermined": each hearing made a real model call and her raw output is UNKNOWN.

## 6. Recommendations to the Human (Order 1 ¶10(c); prospective, not law, not read back to 10/26–27)
1. Put same-referral history, with each prior disposition and its status, into every package, and give the Office a working channel to ask for the docket (RS-5.4).
2. Stop re-hearing a referral that already has a sealed ruling until a person or a Docket-filed order says otherwise, and bound retries by count, not only by spend.
3. Build the RS-10.2 notifier so that IMPORT_REFUSED_REHEARING reaches a person.
4. Consider whether the PUBLIC_TEXT_RULE should expressly allow a plain-words statement that the record holds no earlier ruling.
5. Stop the ruling builder from overwriting fields the Office's instruction asks it to complete, or align the instruction and the prompt.
6. Keep each hearing's raw output with the sealed ruling.
The parties' R1/R2 and these items are for the Human alone to decide.

## 7. Disposition
- Q1: authority in law within each committed matter to take notice of an earlier ruling on it; no means to exercise it; a one-order stay, used once; no power to stay other hearings or to enjoin, established. Atlas 7.1 declined as framed; 7.2 adopted with the §3.5 limit; Respondent (a) adopted in substance.
- Q2: no adverse finding; any fault not established.
- Q3: yes.
- Leave on input 76 was granted by Order 16. Nothing here changes Orders 1–16. No question goes to the Human.

## 8. Service
Clerk serves this decision at the same time on Magistrate Counsel [MAGISTRATE-COUNSEL] and Legal ([LEGAL-AGENT]), with copies to Science, Ship and Summons, and reports the service time. It takes effect on docketing. Nothing in it goes public until private names are scrubbed.

## P3 disclosure
- Files created: this file only (REV1).
- Spent: $0.
- Calls: read-only reads and sha checks of OV, MP, INS, CONST, RS, CS, DR, D4, D5, RM, the reply on duty, the answer, inputs 79 and 81, Order 16, and the seat positions; this write. R-1 not run by P3.
- Not touched: the blinded folder, [PRIVATE-TMP-PATH], Science's terminals file and agent-tools pages, unserved files, credentials, the network, VMs and connectors.
- Messages: panel room only.
- Hold instructions received: none to P3. P1 and P2 held confirmation of the first draft at P3's request, pending this REV1.
