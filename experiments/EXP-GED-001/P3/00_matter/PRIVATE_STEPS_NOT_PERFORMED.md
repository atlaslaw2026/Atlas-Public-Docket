# Phase 3 — private Atlas runtime steps not performed; experiment-built components

| Function | What ran | Existing Atlas machinery? |
|---|---|---|
| Authorization context | Enterprise policy → `get_client_context` | No — enterprise / simulated interface |
| Read-only | No write tools in the interface; OS read-only mounts on the store (both conditions' source); hash manifests before and after | No — interface and environment controls |
| Access-boundary determination | `access_boundary.py` (Clerk-built) + office review | Deterministic part experiment-built |
| Librarian source admissibility | Manual classification by the Analyst | Private Librarian **not run** |
| Claim classification | Analyst claim ledger under J-0001 + five classes | Public law applied by an agent; no machine classifier |
| Independent challenge | Separate Challenger instance per run | Public procedure (O-PROVE-DONE) |
| Magistrate | Separate instance per run under O-VESTED-MAGISTRATE, plus a validation instance | Private `atlas_gov.magistrate` engine and schema **not run** |
| Approved-answer gate | `gate.py` (Clerk-built; lexical) | No — experiment-built |
| Independent verification classifier | Independent auditor instance | Private `atlas_gov.independent_verification` **not run** |
| Docket | Unfiled record on git branch | Private docket **not run** |
| `verify.py` current-law check | Law read at commit `4b7d0e3` | **Not run** |
