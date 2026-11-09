> **PUBLIC READING COPY.** Atlas case docket entry 16 — MCR-BREF94-20261027-1.
> - **Entry:** 16
> - **Date filed:** 10/27/2026 ~7:22 PM PT
> - **Filed by:** Ship
> - **Original source sha256:** MANIFEST.md `fda24c848f90e3e14fe859c1641dae74538d5af3be2dd4792d7058b50c7927f6`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 016 — PRODUCTION — Box-evidence production complete ($0; no VM calls). Manifests verified and served

## Source document: MANIFEST.md

# MANIFEST: Subpoena 1 (Order No. 2, ORDER-002-SUBPOENA-1.md a220d70ea2cd7201bb59d62e69986115bcc382b32d9de6b632d31d7e186ae465)
Request: SUBPOENA-REQUEST-1.md 6c17e46f704b166736af9ba2b4866aa7dc647f2628a5aeab1c118228af3e2362 (Atlas Counsel), R1-R7. Custodian: Ship.
Built 2026-10-27, about 7:40 PM PT. Box only: no VM, server, network or model call. Spend: $0. Originals unchanged. Nothing touches the live court.

Order 1 productions are cross-referenced, not copied twice:
- Every copy below is a member of ../EVIDENCE-COPIES.tar.xz (sha 873cf59fed2682f7c5826897bd73a48883008e442612789b5f094b780b0da69b). Members are listed as `member` sha256 (bytes, mtime PT). The full table with sources is in ../MANIFEST.md sec.B.
- Cited originals are in ../MANIFEST.md sec.C.
- Gaps G1-G13 are in ../GAPS.md. Every VM-only item waits for Clinton's own yes/no with a call cap; if he declines, there is no adverse inference.

Scrub and blank log: 0 private-name hits and 0 secret hits in the produced copies, so 0 scrubs and 0 blanks (../MANIFEST.md sec.D). Nothing else is redacted. Nothing in research/ad14-3… was opened.

## R1: hearing rows, inputs, outputs, ruling texts, bundle, progress file
- Hearing rows (KNOWN, all 220 bref_94 rows through 1:13 PM PT; INDEX A3):
  - `box/accounting-requests/oracle-ledger-20261027/backup-copy/court_ledger.json` 727c52f64b9e40d4fb04fa2984241aca18585b2c3f8ea9e3848e8670914cad7f (164706 B, 2026-10-27 18:05 PT)
  - derived `derived/HEARINGS-bref94.tsv` 33aac8230c4fecfe4533443887ec88090729b2179781c127b4731e5882a82158 (25496 B, 2026-10-27 19:20 PT)
- Ruling texts and bundles (KNOWN, cited, not copied): the 171 refused bundles at [PRIVATE-PATH], COMBINED 4c6f9687daca1803dd675897a50dad82b51135ba231b0d9dbbde9f0aa10d8b3d, 47,173,054 B. Records: [PRIVATE-PATH] [ID]… and RECORD-215b.md [ID]…. Bundle listing: `box/ship-notes/ruling-copy-215-20261027/RECORD.md` e6b322f69e525a03901df97186150b1f47c26d7938e78a90b1e051133364c0a7 (2944 B, 2026-10-27 19:02 PT).
- GAP: per-hearing inputs and package, the referral, rehear and progress files, and proposals (G5); the 49 failed-attempt court roots (G6); the live bundle (G5).

## R2: code and config as deployed, with VM sha and mtime; Oct 26 deploy and restart records
- court_service.py: `court-src-[ID]/tree-f3b/src/atlas_mcp/court_service.py` 570e1a5ca672a2669e1e7cb7ba775fbc4788e5c6c99459e056da2d54246b4408 (35814 B, 2026-10-20 17:00 PT). VM sha matched on Oct 26 (FIX5-POST).
- llm_runtime.py: `court-src-[ID]/tree-f3b/src/atlas_mcp/llm_runtime.py` f51e5806eec6aac4a6691c0422e53d6d66f3afd4867239871a284b9c60c4df25 (12139 B, 2026-10-20 17:00 PT). VM sha matched on Oct 26.
- bailiff_referral.py: `court-src-[ID]/tree-f3b/src/atlas_mcp/bailiff_referral.py` e4cabb3f22dda3447220bf0d2e2912fdffa0be0059f3289eab40f55185bd0997 (61883 B, 2026-10-20 17:00 PT)
- bailiff_demo.py: `court-src-[ID]/tree-f3b/src/atlas_mcp/bailiff_demo.py` d58739059279b5923e30bef2b729d56db9ff5967da3fc8b3a83dc211ac16f707 (205608 B, 2026-10-20 17:00 PT)
- Also court_spool, package, ovested, magistrate_provider, magistrate_execution, authenticated_magistrate, court_proposal, service (../MANIFEST.md sec.B).
- check.py in force: `reconstructed/atlas-court-check.py` 4248111ee1145df63c3778ada2f615a674b31a45bac456be558c2ba70d60cf19 (7288 B, 2026-10-27 14:34 PT)
- model.json in force: `reconstructed/model.json` ce19176a8a76152472d7dd94778f1a6736001eb536323a54626c8b77d9e595a4 (302 B, 2026-10-27 14:34 PT) (= the VM 1:13 PM backup sha)
- court-config.json: `box/audit/cloud-only-cutover-[ID]/bundles-addendum3/pkg/vm-bundle/court-config.json` 76f45471f2c61f52988fce059d1fc364d4dfbea99c8b301d5f17ff2584ab5326 (620 B, 2026-10-27 14:34 PT) (= the VM 1:13 PM backup sha)
- Deploy records:
  - `box/ship-notes/magistrate-1233-fix-20261027/DEPLOY-RECORD.md` 55db991cc7fe5f7420dee41f68be4f729f9d15611a67472d746ede849bc1a524 (4486 B, 2026-10-27 17:31 PT)
  - `box/ship-notes/court-cap20-applied.txt` a397ce30e758617bff466093cffaeb96e3b80b31c2ce7fa2be786898f3f25891 (4168 B, 2026-10-27 14:34 PT)
  - `box/ship-notes/court-fix5-applied.txt` 0ce5bc6d4e68f8374c6bc883a721b085e9bbc2b293b2b8f0e90e56fd9ec913da (360 B, 2026-10-27 14:34 PT)
  - `box/audit/cloud-only-cutover-[ID]/fix5-post/FIX5-POST.md` 57b0cfd98e59da49a915727089f9dafd1608e66fb01ddaab50b37ba0e95b47fe (8031 B, 2026-10-27 14:34 PT)
- GAP: VM shas and mtimes for the other package members and the engine copy (G7); VM restart and deploy journal (G12); the in-force atlas-court.service (G9).

## R3: alerts.jsonl, live and backups
- GAP G2 (priority 2). The backup sha [ID]… (34,774 B) is KNOWN only from DEPLOY-RECORD.
- KNOWN code: alerts are only appended (court_service.py l.382-387).

## R4: xai-calls.jsonl, model_spend.json, court.log, court_ledger.json (live and backups)
- model_spend.json, live as read: `box/accounting-requests/oracle-ledger-20261027/model_spend.json` 249ae884ca997213ca417039982a62eade8a8b91705e0a948a4ac83186ea678f (73 B, 2026-10-27 17:38 PT)
- court_ledger.json, 1:13 PM backup: `box/accounting-requests/oracle-ledger-20261027/backup-copy/court_ledger.json` 727c52f64b9e40d4fb04fa2984241aca18585b2c3f8ea9e3848e8670914cad7f (164706 B, 2026-10-27 18:05 PT)
- GAP: live ledger (G1, priority 1); court.log (G3, priority 3); xai-calls.jsonl (G4); the 1:13 PM model_spend backup [ID] (G11).

## R5: courtwatch.py, units and timers including the cap revert, any notifier
- courtwatch.py in force: `reconstructed/atlas-courtwatch.py` aa158f079e887284cb45bcfb0f2983285ca216f51290031f499852f1f77ec494 (2400 B, 2026-10-27 14:34 PT)
- Units as shipped:
  - `box/audit/cloud-only-cutover-[ID]/bundles-addendum3/pkg/vm-bundle/atlas-court.service` 69f1aa24d1f1086b4944effb3e5549559b2a10ddfd7c0377bb0d05c51a31074f (2386 B, 2026-10-27 14:34 PT) (pre-FIX5)
  - `box/audit/cloud-only-cutover-[ID]/bundles-addendum3/pkg/vm-bundle/atlas-courtwatch.service` 077396f17c4a4026603e8095642607a583541a5e00dc526e5b2df57c4dd979cd (830 B, 2026-10-27 14:34 PT)
- Revert timer and script (KNOWN from hold checks):
  - `box/ship-notes/hold-check-20261027/h2-out.txt` c624da8a5be4c6701f0d02555c13cf27f74bff3dd1769022b332cfa7deb59278 (632 B, 2026-10-27 18:29 PT)
  - `box/ship-notes/hold-check-20261027/h3-out.txt` b1eebf29c41e2659a57f33b3be471bc253d072b6f0bded7160b257a51a8f259d (785 B, 2026-10-27 18:33 PT)
  - `box/ship-notes/hold-check-20261027/h4-out.txt` 026312bc963c4ded06e2639048289456323652b0c3236b7aa9e1877003f84eae (519 B, 2026-10-27 18:57 PT)
  - The scripts are h2/h3/h4.sh in the archive.
- Notifier: KNOWN none in the box package or units (INDEX (c)4).
- GAP: the live units, timers and cap22 files (G9); the cap22 backup folder (G11).

## R6: prompt and sub-agent instructions, tools and actions, precedent and index access
- `court-src-[ID]/tree-f3b/src/atlas_mcp/law/MAGISTRATE_INSTRUCTION_v1.txt` d4454a7e46d030928fc8fba2b8e296f22e7d167f9ccfe3f2c6dbba544bb3ad01 (5255 B, 2026-10-20 17:00 PT)
- `court-src-[ID]/tree-f3b/src/atlas_mcp/magistrate_provider.py` 2cd7fd0ac65fe896545680003dcdae070438e859663bdf8a8ad586f41feb4d5b (22550 B, 2026-10-20 17:00 PT) (SYSTEM l.47-62; own-motion stay or narrow l.41-45)
- `court-src-[ID]/tree-f3b/src/atlas_mcp/package.py` 1280b33e348013aecf151ff0c8e7e138c2fa692d604eaf2114f0abe46fcf9662 (14551 B, 2026-10-20 17:00 PT) (court_history scope l.139-151)
- INDEX (d): KNOWN no stay-queue, injunction, flag or escalate tool; A6 is read-only.
- GAP: VM shas of the prompt files (G7); the template and any precedent or index files (G8).

## R7: start and restart log Oct 26 9 PM to Oct 27 4:30 AM; the 12:01 AM queue entry; the caller per re-hear; diag-magistrate-1233
- The 12:01 AM release is KNOWN from code: court_service.py l.488-500 sets not_before to 12:01 AM PT the next day (FIX5-POST l.28). The first Oct 27 row is at 12:01:33 AM PT (HEARINGS tsv).
- The caller per re-hear is INFERRED from code: the engine's try_import calls request_rehear (bailiff_referral.py l.899-915; court_spool.py l.148-159), and the court re-hears at court_service.py l.436-451. The per-event record is a GAP (G2, G3).
- GAP: journal start and restart log (G12); diag-magistrate-1233 (G10, not on the box).

## Coverage
- R1: rows and ruling texts KNOWN; inputs GAP.
- R2: KNOWN for court_service, llm_runtime, check, model and config; other VM shas GAP.
- R3: GAP.
- R4: partial (model_spend and the 1:13 PM ledger KNOWN; others GAP).
- R5: courtwatch, shipped units and revert evidence KNOWN; live units GAP.
- R6: KNOWN (VM shas of the prompt GAP).
- R7: code-level KNOWN or INFERRED; logs GAP.
- One bucket copy of G1-G12 needs about 5-6 server calls, cap 6 (16 of 40 left). See ../GAPS.md.



## Withheld attachments (not public)

- EVIDENCE-COPIES.tar.xz: binary evidence archive
