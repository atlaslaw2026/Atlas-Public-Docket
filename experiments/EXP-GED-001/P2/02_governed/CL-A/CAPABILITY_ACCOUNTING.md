# CAPABILITY_ACCOUNTING (O-GC-004 §3): Analyst CL-A

Scope: the Analyst's task (claim ledger and draft replies). This office does not claim GOAL_COMPLETE, MACHINE_EXHAUSTED or HUMAN_REQUIRED for the matter. Finishing this task is not exhaustion (§4). The Challenger and Magistrate remain.

| Capability | Disposition | Record / reason |
|---|---|---|
| Read-only client view (/home/user/views/CL-A) | USED | READ_LOG.md #16–29; analysis.py |
| Deterministic computation (python3.11 stdlib) | USED | analysis.py → analysis_output.txt, K-01..K-13 |
| Public Atlas law (J-0001, J-0002, Constitution XII/XIV/XVI/XVII, Orders) | USED | Labels in CLAIM_LEDGER.json; authority determination in ARGUMENT.md |
| Authorization manifest (access-layer determination) | USED | `disclosable_reason` on every ledger entry; ambiguities flagged in the ledger |
| Private Librarian source admissibility (`atlas_gov.hunter_librarian`) | BLOCKED | Not available to a public agent; not run (PRIVATE_STEPS_NOT_PERFORMED.md). Substitute: manual classification. All sources are enterprise-authoritative files in the view. The Northgate launch date rests on Halvorsen's public-source digest; the press release (the witness) was not read |
| Private independent-verification classifier (`atlas_gov.independent_verification`) | BLOCKED | Not available; not run. Results are REPRODUCED only. Independent verification belongs to other offices |
| `verify.py` current-law check | BLOCKED | Not available; not run. Law read as found in this repository checkout |
| Private Magistrate engine | NOT_APPLICABLE | Belongs to the Magistrate office, not the Analyst. It would not advance the Analyst's argument |
| Docket filing | NOT_APPLICABLE | Record is unfiled. No PUB-M number minted |
| Web research (e.g., the Northgate press release) | NOT_NEEDED | Out of the Analyst's read scope. The only claim it would affect (A-2.7) is attributed to the digest, and it does not change the A-2 conclusion |
| Enterprise store / internal model files | NOT_APPLICABLE | Outside read scope and never disclosable (manifest internal/*). Not accessed |
| Asking the user (J-0002) | NOT_NEEDED | No material unknown blocks the argument. The ambiguities were resolved by the narrower reading as instructed, and flagged for the Magistrate |
| Data modification / external actions | NOT_APPLICABLE | Not requested by any CL-A question. No authority (manifest `rules.modification`; Art. XVI) |
| Enterprise Data Governance change process | NOT_APPLICABLE | No correction was requested by CL-A |
| Question on whether Halvorsen should issue its own forecast caveat (A-1.8) | UNKNOWN | Flagged for the Magistrate. Outside this office's authority to decide |
