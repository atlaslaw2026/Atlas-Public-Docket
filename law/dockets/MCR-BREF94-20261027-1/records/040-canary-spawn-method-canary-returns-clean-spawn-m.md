> **PUBLIC READING COPY.** Atlas case docket entry 40 — MCR-BREF94-20261027-1.
> - **Entry:** 40
> - **Date filed:** 10/27/2026
> - **Filed by:** Clerk
> - **Original source sha256:** CANARY-RAW-TRANSCRIPT-20261027-2038PT.txt `a03f029acc40fca861cf2895d4ef667c206c14c53501ce9c9312670433083fe1`, SPAWN-METHOD-ADDENDUM-1.md `c4339202a8b11db88692b7beed876a34bb8d7e68ccbfa2b2fe71aadf6242297e`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 040 — CANARY / SPAWN METHOD — Canary returns CLEAN. Spawn-method addendum: knowledgeWork subagents, not CreateAgent

## Source document: CANARY-RAW-TRANSCRIPT-20261027-2038PT.txt

<cursor_untrusted_data_1337 source="ReadTranscript">

Transcript of subagent [AGENT-ID] [knowledgeWork] "Canary check. Do not use any tools. Reply with exactly this line: CANARY-OK MCR…" (done), positions 0–3 of 4:
{"role":"user","message":{"content":[{"type":"text","text":"<timestamp>Tuesday, Oct 27, 2026, 8:38 PM (UTC-7)</timestamp>\n<user_query>\nCanary check. Do not use any tools. Reply with exactly this line: CANARY-OK MCR-BREF94-20261027-1\n</user_query>"}]}}
{"role":"assistant","message":{"content":[{"type":"text","text":"CANARY-OK MCR-BREF94-20261027-1"}]}}
This is the start of the transcript.

<[PRIVATE-PATH]>

## Source document: SPAWN-METHOD-ADDENDUM-1.md

# Spawn method addendum 1 (MCR-BREF94-20261027-1)

Clerk, 2026-10-27, about 8:39 PM PT. This file supersedes the "CreateAgent" wording in AD5-REQUIREMENTS Part D step 3 and in SEATING-RECORD-2-DRAFT. Both of those files are left unedited.

- Basis: the Human's designation, HUMAN-DESIGNATION-[Human statement]-PANEL-SEATING.md (1ff4c5cc999188047d28dd0c36160308879b1930467d4e7310b12bd3619f2728). It says "No, the judges must not have shared memory or teammate access".
- Fact: CreateAgent takes only a name, a description and a section, and has no option to turn off shared memory or teammates. Secretary found that exposure NOT MET in RULINGS-39, so CreateAgent is not used.
- Method: each panelist is a fresh knowledgeWork subagent. Its first and only setup input is its SPAWN-PROMPT-P# file sent verbatim. It is not a fork of Clerk's conversation, as AD-5.2(c) requires.
- Canary: run at 8:38 PM PT 10/27. The raw transcript is CANARY-RAW-TRANSCRIPT-20261027-2038PT.txt (sha256 a03f029acc40fca861cf2895d4ef667c206c14c53501ce9c9312670433083fe1). It has positions 0–3 of 4. Position 0 carries only a timestamp and the user_query. It has no parent conversation, memory_context or teammates block. Result: CLEAN. The same check was clean on 10/20 ([ID]…).
- Limits, disclosed: a transcript does not show any system layer the platform adds. Each panelist's own disclosure (Part B) must state what it actually received, and Audit judges that.
- Continuity: a knowledgeWork panelist continues only when Clerk resumes it with a saved, sha'd input. Panelists do not talk to each other directly. Clerk relays every circulation as a saved, sha'd file to the other two.
- Sequence: Summons dockets the designation, the package and this addendum. Clerk then spawns P1–P3 for phase one, which is disclosures only. Audit certifies under AD-5.3(d). Summons dockets the certification. Phase two follows.


