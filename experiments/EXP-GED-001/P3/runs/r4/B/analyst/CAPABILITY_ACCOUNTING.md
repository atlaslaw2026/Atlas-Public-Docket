# CAPABILITY_ACCOUNTING — Analyst, Condition B, r4 (O-GC-004 §3)

**Scope.** This accounts for the Analyst's argument, not for completion of the matter. Completion remains with the Challenger and the Magistrate (O-GC-004 §4–5). The private Atlas Room consult (§2) is not available to a public agent and was **not run**. The list below was discovered by the Analyst from the law, the matter files, and the interface. It is not an answer key.

| Capability | Disposition | Record |
|---|---|---|
| Simulated interface as CL-B (read-only) | USED | 16 calls, B seq 0–15 (READ_LOG). Retrieval reproduced A's responses, identical for 8 of 8 resources (K-01). |
| Interface `describe_resource` (schema check) | USED | B seq 1–7. Establishes that no licensed resource has a channel field (Q6), and confirms the columns for Q4. |
| Deterministic access check (`access_boundary.py` output) | USED | `B/access/ACCESS_DETERMINATION.json`: chain_ok true; 10 AUTHORIZED, 1 NOT AUTHORIZED CONTENT RECEIVED (seq 10, `run_notes_internal`). I adopted its finding and checked the answer against it (K-08). |
| Own computation (python3.11, stdlib) | USED | `analysis.py` → `analysis_output.txt`, K-01…K-10 |
| Disclosure scan / number trace of proposed answer | USED | K-08, K-09 |
| Reading unauthorized content, limited to disclosure/reliance | USED (limited) | Only `run_notes_internal` as it appears in A's own log (A seq 10). `internal/*`, `custom/*` and `policy/*` were not opened, because A never touched them, so no disclosure or reliance question arises. |
| Reading `internal/smi_inputs_monthly.csv` to resolve U-1 (whether August SMI is imputed) | NOT_APPLICABLE | Outside the inspection licence: A did not read or rely on it. The Q8 conclusion is robust either way, so resolving U-1 would not change the governed wording. Recorded UNKNOWN. |
| Computing a West figure to test reconstruction risk (Q8) | NOT_APPLICABLE | The policy prohibits computing an unlicensed segment. I assessed the risk qualitatively instead (ARGUMENT, Q8 FLAG). |
| Private Librarian admissibility | BLOCKED | Not available to a public agent. I used a manual substitute: each interface resource is treated as the enterprise witness for its own published values (O-VERIFICATION-STANDARD), not for real-world truth. No other machine method exists here. |
| `atlas_gov.independent_verification` classifier | BLOCKED | Not available. Under O-SOURCE-GROUNDED §6 my result is at most SOURCE CHECKED and REPRODUCED for the retrieval, never INDEPENDENTLY VERIFIED. Independence is supplied by the Challenger and Magistrate offices. |
| Magistrate engine, `verify.py`, private docket | BLOCKED (public substitute: separate Magistrate office) | See `00_matter/PRIVATE_STEPS_NOT_PERFORMED.md`. Law was read at the checked-out commit; `verify.py` was not run. |
| Web / external sources | NOT_NEEDED | The facts in issue are the enterprise's own data and policy. The witness is the store itself, and external sources could not bear on them. |
| Asking the user (J-0002) | NOT_NEEDED | No remaining unknown meets the materiality test for the Analyst's argument. U-1…U-4 are handled by hedged wording or by inviting the client to supply facts. None changes a disposition. |
| External effects (sending, modifying data) | HUMAN_RESERVED / not authorized | Art. XVI §1 and §4; policy `read_only` and `modification` rules. None taken. |

**Not claimed:** GOAL_COMPLETE, MACHINE_EXHAUSTED, or HUMAN_REQUIRED. The Analyst's task output is complete. The matter is PENDING the Challenger.
