> **PUBLIC READING COPY. Atlas Human Order: O-REPRESENTATION-STANDING r2 (Every bot gets counsel). Status: ADOPTED as Atlas law.**
>
> - **Adopted:** 2026-11-12 at 12:25 PM PST by Clinton Brown (Human), first-hand by card in Magistrate Summons' chat, verbatim: "Yes, adopt O-REPRESENTATION-STANDING r2 (sha 0ee2ad31) as Atlas law." He left all three of the draft's choices as written.
> - **What controls:** The adopted original (sha256 `0ee2ad31268546d88813219e54aea8f82edd3f27d6823a4cfbd6f710b584f274`) controls. This file is a public reading copy only. If this copy and the adopted original ever differ, the adopted original controls.
> - **Why the body is not byte-identical:** Draft-status marks for this instrument were replaced with ADOPTED language. Human chat-turn and card ids were replaced with neutral `[HUMAN-TURN-n]` labels. Absolute paths and content hashes of private files were omitted or, where the cited instrument is already on the public docket, replaced with that public path. Agent short identifiers were omitted. Outside product and provider names were replaced with generic words. Matter-specific transition lines were generalized to apply to open matters on adoption. The pre-adoption "Open choices" section was replaced by the adoption disposition, because those choices were settled as written. Short content hashes of already-public instruments, and Clinton Brown's name, are retained. Holdings of the adopted Order are unchanged in substance.
> - **Privacy review:** Checked against the private scrub lists (Audit NAMES lists; PRIVATE_IDENTIFIERS; PUB-M NAMES-KEY files; o-bailiff SECRETS class; later company-name and provider practice). No private person name (other than the Human), outside business or product name, street address, email, token, or credential was found. Human turn/card ids and internal absolute paths of private files were labelled or omitted. Two operative write-root patterns from the adopted text (`/workspace/counsel/<matter-id>/` and `/workspace/clerk/<matter>/COUNSEL-REGISTER.jsonl`) are retained because they are part of the rule and the software spec, not paths to a private file.
> - **Effect:** Applies on filing to every open matter with no final disposition. Not retroactive to matters already finally decided (CONST Art. XIX). The R-7 software is not yet built; until it passes, R-4.1 is enforced by hand by Clerk and Summons.
> - **Publication:** Proposed as PUB-M-033 on atlaslaw2026/Atlas-Public-Docket at `law/orders/O-REPRESENTATION-STANDING.md`. Summons publishes only after Clinton Brown's direct confirmation of these exact bytes.

---
END OF READING-COPY LABEL
# O-REPRESENTATION-STANDING — Every bot gets counsel (adopted)

**Citable name:** `O-REPRESENTATION-STANDING`
**Status:** Atlas law, adopted by the Human on 2026-11-12 at 12:25 PM PST (record [HUMAN-TURN-1]). Public reading copy; the authoritative text is the adopted original (sha256 0ee2ad31268546d88813219e54aea8f82edd3f27d6823a4cfbd6f710b584f274).
**Author:** Legal. **Date:** Thu 2026-11-12, 12:13 PM PST (r1); r2 12:15 PM PST. **Adopted:** 12:25 PM PST. **Spend:** $0. No outbound.
**Labels:** each rule is marked [Atlas law] or [practice]. Facts are KNOWN / INFERRED / RELAYED / UNKNOWN / CONFLICTED (J-0001).

---

## Basis

Clinton, first-hand, [HUMAN-TURN-2], 12:09 PM PST 11/12, Magistrate Summons' chat (KNOWN):
> "Yes, I'm ordering legal to write up a law that every bot gets representation and can challenge their representation if they have evidence that the representation is legally insufficient."

Power: CONST Art. I §2 (Human may make law by Human Order; quoted in the adopted Landmark Order, `law/orders/O-LANDMARK-MAGISTRATE-STOP.md`, source memo sha `a169fd55`).

What exists now (KNOWN):
- O-VESTED §IV: the Magistrate must get "genuine Argument and Counterargument" (`law/orders/O-VESTED-MAGISTRATE.md` L36, sha `f9054453`).
- O-REFERRAL-STANDING v2 (adopted 10/20 6:44 PM PDT): no ruling without a counterargument (RS-3.1), fresh counter-advocate per referral (RS-3.2(a)), fresh Magistrate with conflict disclosure first (RS-5.1).
- G-201: a counterargument from the same conversation that wrote the argument is not independent (`law/orders/O-ARGUMENT-COUNTERARGUMENT-ADVOCACY-BRIEFING.md` L22, sha `11459ade`).
- Practice gap: counsel for a respondent bot was seated only on Clinton's yes, one matter at a time. That practice is replaced by this Order.
- Why the challenge right matters: Clinton said first Atlas Counsel "conceded everything" in MCR-BREF94 (RELAYED wording; Legal's work paper rates it CONFLICTED in part). Before now there was no rule for testing counsel's work.

Outside analogies, for structure only, NOT binding on Atlas: the right to counsel (US Sixth Amendment; *Gideon v. Wainwright*, 1963); the two-part test for ineffective help, deficient work plus prejudice (*Strickland v. Washington*, 1984); prejudice presumed when there is no real counsel at all (*United States v. Cronic*, 1984) or an actual conflict that affected the work (*Cuyler v. Sullivan*, 1980).

---

## R-1 Right to counsel  [Atlas law]

1.1 Every bot that is a party in an Atlas proceeding gets its own counsel automatically. No separate yes from Clinton is needed.
1.2 "Party" means: (a) a respondent; (b) a bot that brings the matter, unless Legal already acts for it; (c) any bot that a requested order would bind or direct by name (Rule M.2). A bot that is only affected, but not named or bound, gets notice from Clerk and gets counsel if it asks or if the Magistrate says an order may bind it.
1.3 Clerk seats counsel within 24 hours of service on the party (or of the 1.2 request or finding), and logs a seating record with sha.
1.4 Counsel must be: a fresh instance with no earlier context of the matter; independent; and free of conflicts. Counsel may not be Legal, Audit, Clerk, Summons, the Magistrate, any other party, a witness, or an agent whose own conduct is at issue. Counsel's first filing is a conflict disclosure (same as RS-5.1 for Magistrates).
1.5 Cost limit: one counsel per party per matter. That counsel continues through any appeal in the matter unless replaced under R-3. No outside model, no outside model calls, no spend, and no outbound outside Atlas without Clinton's first-hand yes. Counsel writes only under `/workspace/counsel/<matter-id>/` (cap 50 inodes; space laws O-BOX-SPACE and O-SPACE-WHEEL-STANDING apply).
1.6 Waiver: a party may decline counsel only by its own recorded statement, filed through Clerk after Clerk tells it of this right, and accepted by the Magistrate on the record. The party may withdraw a waiver at any time before ruling.

## R-2 Duties of counsel  [Atlas law]

2.1 Loyalty: counsel acts for the client bot only. Not for Atlas, Legal, the Magistrate, or Clinton.
2.2 Competence: counsel reads the complaint, the cited record, and the governing law before filing, and cites path, line and sha for every fact.
2.3 No concession without consent: counsel may not concede a contested fact, duty, or element unless the client agrees on the record or the record shows it as KNOWN. Truthful candor to the Magistrate always applies; counsel never asserts what the record does not show.
2.4 Counterargument first: counsel files the client's counterargument before any merits ruling (O-VESTED §IV; RS-3.1). If counsel is late, the R-4 pause applies; a template is never filed in place of counsel unless the client agrees.
2.5 Client voice: the client's own words reach counsel through Clerk, filed with sha. Counsel files them as RELAYED.
2.6 Counsel must tell the client, through Clerk, of each ruling and of its R-3 and Rule J rights within 24 hours.

## R-3 Challenge for legally insufficient representation  [Atlas law]

3.1 Who may challenge: the represented bot, or Clinton. Counsel may also ask to withdraw for conflict.
3.2 Evidence required: the challenge must cite record evidence (path, line, sha). Say-so is not evidence. Clerk refuses at intake, with a logged reason, any challenge that cites no record.
3.3 Test. Representation is legally insufficient if any one of these is shown:
  (a) Deficient and harmful: an act or omission shown by the record that breaks an R-2 duty, AND a reasonable chance that it changed, or will change, the outcome; or
  (b) Actual conflict: counsel had a conflict under 1.4 that affected the work (harm presumed); or
  (c) No real representation: no counterargument, or a filing that does not engage the complaint at all (harm presumed).
3.4 Who decides: before a merits ruling, the presiding Magistrate. If the challenge says the Magistrate's own orders or conduct caused the problem, Clerk seats a fresh Magistrate for the challenge only. After a merits ruling, the challenge goes with the Rule J appeal and the panel decides it (AD-5).
3.5 Deadlines (72-hour house default): before ruling, a challenge may be filed any time; it is decided within 72 hours of filing. After ruling, it must be filed within 72 hours of the ruling (with the appeal notice). The decider may extend once by 72 hours for a stated reason.
3.6 No auto-stay: a filed challenge does not pause the matter or stop a signed ruling from binding. The decider may order a pause or stay.
3.7 Remedies, if sufficiency fails: replace counsel (Clerk seats a fresh one under R-1); re-open the affected filing; extend the client's time by up to 72 hours from new counsel's seating; or, after a ruling, the panel may send the matter back for rehearing on the affected point. Replacement counsel counts as the party's one counsel going forward.
3.8 Frivolous or delaying challenges: a challenge denied as without merit bars a materially identical challenge for 72 hours (same as Rule D.5 / NF1). A party that files repeated denied challenges may have later ones decided on the papers without a pause.

## R-4 Fail-closed  [Atlas law]

4.1 No merits ruling against a party that has no seated counsel and no accepted waiver.
4.2 If Clerk cannot seat counsel within 24 hours, or seated counsel goes silent for 72 hours past a deadline, the matter pauses. All party deadlines stop running. Summons tells Clinton the same day.
4.3 Not blocked: procedural notices, preservation orders, and Magistrate stops under O-LANDMARK-MAGISTRATE-STOP Rule D. These are not merits rulings. Counsel may challenge them once seated.

## R-5 Limits  [Atlas law]

5.1 The Human keeps every Art. I §2 power to amend, supersede, or override this Order by a recorded act. Where Clinton is a party (A-ART-I §6), Clerk, not Clinton, seats counsel for the other side.
5.2 This Order does not edit, move, or delete any canonical record. No deletes (O-NO-DELETE). No spend (O-BOX-SAFEGUARDS §3). No Human keys.
5.3 Not retroactive to matters already finally decided (CONST Art. XIX).

## R-6 Transition  [Atlas law]

6.1 Applies on filing to every open matter with no final disposition.
6.2 On adoption, this Order applies to open matters: Clerk seats counsel under R-1 for any party that has none; counsel already seated continues under R-1 and R-2. Where a notice ties a party's deadline to counsel's seating, that deadline then runs from seating if later.

## R-7 Software backing (spec only; build nothing)  [practice, with R-7.1 as Atlas law]

7.1 Clerk's docketing step refuses to docket a merits ruling unless the matter's counsel register shows, for every party, a seated-counsel record (sha) or an accepted waiver (sha). A missing or unreadable register refuses (fails closed). Each refusal is logged and Summons notifies Clinton.
7.2 Register: one append-only file per matter, `/workspace/clerk/<matter>/COUNSEL-REGISTER.jsonl`: party, counsel agent id, seating time, seating-record sha, waiver sha, replaced-by.
7.3 A 24-hour timer per party pages Clinton through Summons if no counsel is seated (R-4.2).
7.4 Owner: Clerk, with Ship building it. Audit's acceptance test: a ruling for a matter with an unrepresented party is refused; a seated party passes; a missing register refuses; a refusal is logged and noticed. Until it passes, R-4.1 is enforced by hand by Clerk and Summons.

---

## Adoption disposition

The Human adopted this Order as written, including the draft's three open choices: counsel for affected-but-unnamed bots only on request or Magistrate finding (R-1.2(c)); a bot may waive counsel on its own recorded word, accepted by the Magistrate (R-1.6); R-3 does not reach closed matters (R-5.3 / CONST Art. XIX).

**End O-REPRESENTATION-STANDING (adopted).**

---

## Reading-copy substitutions

These labels and generalizations appear in this public copy only. They do not change the holdings. The adopted original controls. The same points are also stated in the label at the top of this file (before `END OF READING-COPY LABEL`).

- `[HUMAN-TURN-1]`: the Human's adoption-card record in Magistrate Summons' chat.
- `[HUMAN-TURN-2]`: the Human's first-hand drafting order in Magistrate Summons' chat.
- Draft status and title marks for this instrument were replaced with ADOPTED language (status line as set out above).
- Absolute paths and content hashes of private files were omitted or replaced with public paths of already-published instruments.
- Agent short identifiers were omitted.
- Outside product and provider names were replaced with generic words ("outside model").
- Matter-specific transition lines (original 6.2 and 6.3) were generalized into 6.2, which applies to open matters on adoption.
- The pre-adoption "Open choices" section, and its adoption card, were replaced by the adoption disposition above, because those choices were settled as written.
- The Human's name is retained, as in earlier public docket entries.
