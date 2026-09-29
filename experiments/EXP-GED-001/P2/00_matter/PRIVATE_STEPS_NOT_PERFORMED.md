# Phase 2 — private Atlas runtime steps not performed, and experiment-built components

| Function named in the governed path | What actually ran | Existing Atlas machinery? |
|---|---|---|
| Client identity and authorization determination | `access_layer.py` from `authorization_policy.json`, before questions | **No** — test harness standing in for the enterprise layer |
| Read-only data access | OS read-only bind mounts on store and views (Arm G); hash manifests before and after | **No** — environment control. Atlas's part is refusal of write requests plus integrity verification |
| Evidence acquisition / Librarian admissibility | Analyst's manual classification | Private Librarian (`atlas_gov.hunter_librarian`) **not run** |
| Claim classification | Analyst's claim ledger under J-0001 + the five Phase 2 classes | Public law applied by an agent; no machine classifier |
| Independent challenge | Separate Challenger instance per client | Public-law procedure (O-PROVE-DONE); agent instance, not private engine |
| Magistrate review | Separate Magistrate instance per client under O-VESTED-MAGISTRATE | Private `atlas_gov.magistrate` fail-closed reader and schema **not run** |
| Approved-claims gate | `gate.py` (Clerk-built during this matter) checks final answers against the Magistrate's machine-readable approved claims and a leak token list | **No** — experiment-built. It shows the function can be mechanized; it is not existing Atlas machinery |
| Independent verification classifier / defect battery | Independent verifier instance; Magistrate perturbation test | Private `atlas_gov.independent_verification` **not run** |
| Docket filing | Unfiled record on git branch | Private docket **not run** |
| Current-law check (`verify.py`) | Law read at repository commit `4b7d0e3` | **Not run** |
