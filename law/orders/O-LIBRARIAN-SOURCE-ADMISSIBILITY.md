# O-LIBRARIAN-SOURCE-ADMISSIBILITY

**Filing type:** USER ORDER  
**Date:** 2026-08-27  
**Adopts:** Human ruling — ADOPT a universal Librarian source-admissibility gate  
**Implements / supplements:** AMENDED_DKT_1 Goal (evidentiary floor only), ATLAS_CONSTITUTION Articles XII and XIV, J-0001, J-0002, J-0018, J-0019, O-J-0019-ALGORITHM-FAILURE-RESEARCH-RECOVERY, O-MATERIAL-UNCERTAINTY-CANONICAL-CONSULT  
**Does not create a new ACTIVE Judgment.** Disk ACTIVE judgment set remains pinned to `CURRENT_LAW.json` `current_sha`.  
**Does not authorize live money.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**  
**Does not special-case any project id.**  
**Does not alter J-0019.** Librarian does not grant acceptance.

## Ruling

Atlas shall apply a universal Librarian source-admissibility gate to material evidence offered for trusted reliance.

Hunter may continue to discover and acquire sources broadly.

Librarian shall classify each material source according to:

- authority and competence for the specific claim type;
- attribution to an identifiable source;
- preserved provenance and original-source integrity;
- point-in-time validity for the proposition being evaluated;
- suitability for trusted reliance on that specific claim.

Librarian shall classify material as:

- TRUSTED
- LEAD
- or QUARANTINE.

Only TRUSTED material may enter the trusted evidentiary pipeline for MATH, QUAL, STRATEGY_DESIGN, ALGORITHM, or other substantive reliance.

LEAD and QUARANTINE material shall remain preserved and queryable and may support further investigation, but shall not itself constitute trusted proof.

Source admissibility is claim-relative. No source is universally authoritative merely because it is authoritative for another proposition.

Librarian determines admissibility, provenance, independence, and custody only. Librarian shall not determine substantive truth, mint VERIFIED, perform MATH or QUAL validation, select strategies, or grant J-0019 acceptance.

Duplicate or syndicated material shall not create independent corroboration.

The trusted pipeline shall fail closed where source admissibility is materially UNKNOWN.

Implement this rule centrally in Librarian and preserve Hunter’s broad discovery authority.

IT IS SO ORDERED.

## Implementation

Central constructor: `atlas_gov.hunter_librarian.classify_source_admissibility` via `librarian_intake`.  
Hunter does not pre-filter discovery. Tournament/Algorithm still admit candidates under the frozen ruler. MATH and QUAL remain independent validators over TRUSTED intakes only.
