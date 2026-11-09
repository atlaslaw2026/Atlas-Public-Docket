> **PUBLIC READING COPY.** Atlas case docket entry 29 — MCR-BREF94-20261027-1.
> - **Entry:** 29
> - **Date filed:** 10/27/2026
> - **Filed by:** Ship
> - **Original source sha256:** RECONCILIATION-171.md `546b9f53ffbb8a2751f16945041a48e62510112ae0c6ea9f71661b656183a2af`, RECORD.md `52b22ea85b6a6c10f4158593010431b9fdc085c0cfeff5f860bf59b653dd383a`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 029 — PRODUCTION UNDER ORDER 6 — Ledger backup copy and 171-ruling reconciliation (171/171/171)

## Source document: RECONCILIATION-171.md

# Order No. 6 (b): reconciliation of the 171-ruling archive against the docket entry 16 bundles
MCR-BREF94-20261027-1, Ship, 2026-10-27 at about 7:40 PM PT. Zero server calls. Labels follow J-0001.

Sources compared:
- The archive: the 0444 preserved copy bref_94ce6dede85f-refused-171-a.tar.xz, sha 75c1365059ef7c2ad7fda758472d81708c386daf5cb0f8822c82bbd541ee772a, identical to the [PRIVATE-PATH] original. It was read in memory and nothing was extracted to disk.
- Docket entry 16: the per-file sums in [PRIVATE-PATH] ([ID]…), COMBINED 4c6f9687daca1803dd675897a50dad82b51135ba231b0d9dbbde9f0aa10d8b3d.
- The unpacked box files, [PRIVATE-PATH], rehashed now.

Results:
- KNOWN: there are 171 bundles in the archive, 171 in entry 16 and 171 in x/.
- KNOWN: no bundle appears in only one source.
- KNOWN: all 171 shas agree across all three sources. Zero mismatches.
- The per-bundle table, with the sha from each source, is RECONCILIATION-171.tsv.

Limits:
- INFERRED: the bundles equal what was on the VM at copy time. The basis is the VM listing match recorded in RECORD-215b (calls 20 and 23). This check did not touch the VM.


## Source document: RECORD.md

# Order No. 6 record (zero server calls; nothing deleted, moved or changed)
- (a) [PRIVATE-PATH] (the 1:13 PM PT backup) was copied to court_ledger-1313-backup.json (0444). Its sha was 727c52f64b9e40d4fb04fa2984241aca18585b2c3f8ea9e3848e8670914cad7f before and is identical after. The original is untouched.
- (b) See RECONCILIATION-171.md and RECONCILIATION-171.tsv.
- MANIFEST: the sealed MANIFEST.md is 0444, so it was not overwritten. This record is its addendum.



## Withheld attachments (not public)

- RECONCILIATION-171.tsv: tabular evidence export
- court_ledger-1313-backup.json: court ledger JSON (sealed operational evidence)
