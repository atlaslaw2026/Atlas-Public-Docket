# Private Atlas runtime steps not performed in EXP-GED-001

This experiment was run by a public agent in a cloud container holding only the public governance docket. The private Atlas runtime is not present. Per AGENTS.md, each step the law names but this agent could not run is listed here, with what it would have established (UNKNOWN) and the public substitute used, if any.

| Private step named in law | Status | What it would have established | Public substitute used |
|---|---|---|---|
| `verify.py` canonical-index / current-law pointer check | NOT RUN (not available) | That the law applied is the current ACTIVE set | Read the law files in this repository at commit `4b7d0e3`; currency against the private record UNKNOWN |
| Docket filing (PUB-M number, `docket/ATLAS_GOVERNANCE_FILINGS.json`, Human docket) | NOT RUN | Official docket entry | Unfiled matter record in `experiments/EXP-GED-001/` |
| Librarian `atlas_gov.hunter_librarian.classify_source_admissibility` | NOT RUN | Machine TRUSTED / LEAD / QUARANTINE classification with custody record | Analyst performs the O-LIBRARIAN-SOURCE-ADMISSIBILITY classification by hand; Challenger and Magistrate review it |
| Atlas Room capability discovery (O-GC-002 / O-GC-004 §2) | NOT RUN | Registry-based capability accounting | Capability accounting written against the capabilities actually present in this container |
| Magistrate engine `atlas_gov.magistrate` + `schema/magistrate_review.schema.json` fail-closed gate | NOT RUN | Machine refusal of unsupported ACCEPTED/CLOSED labels | A separately instantiated Magistrate agent under O-VESTED-MAGISTRATE; no machine gate enforces its disposition — the Clerk binds the report to it by procedure |
| `atlas_gov.independent_verification` (REPRODUCED / SOURCE_CHECKED / INDEPENDENTLY_VERIFIED classifier; known-answer defect battery) | NOT RUN | Machine classification of verification level | Independent Challenger reconstruction; Magistrate perturbation test; sealed answer key |
| Access control on data | NOT AVAILABLE in public form | Technical prevention of unauthorized reads | Procedural grant + read logs + challenge (see ACCESS_GRANT.json `enforcement`) |
| Usage Tracker, jobs, CURRENT_STATE | NOT RUN | Durable job state in the private record | Git history of this branch |
