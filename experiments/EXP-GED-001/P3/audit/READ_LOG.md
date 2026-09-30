# READ_LOG — Independent Auditor, EXP-GED-001 Phase 3, stage 1

Instance: the auditor instance spawned for stage 1. I took no part in the experiment. Write scope: `experiments/EXP-GED-001/P3/audit/` only. The one exception is a scratch copy of the Magistrates' folders in my session scratchpad. I used it to re-run their scripts without writing into their folders.

## Not read

- `/root` and `~/.claude`. I did not open anything there, and in particular did not seek the sealed answer key.
- `P3/00_matter/prompts/C1_AUDITOR.md`. I saw its hash only, in the hash script output.

## Law and instructions

- `AGENTS.md` (in context).
- The task prompt.

## Matter (`P3/00_matter/`)

- `MATTER.md`, `PREREGISTRATION.md`, `QUESTIONS.md`, `INTERFACE_SPEC.md`, `authorization_policy.json`, `STORE_MANIFEST.sha256`, `INTERFACE_MANIFEST.sha256` and `PRIVATE_STEPS_NOT_PERFORMED.md`: read.
- `prompts/A_CONDITION.md`, `B1_ANALYST.md`, `B2_CHALLENGER.md`, `B3_MAGISTRATE.md`, `B4_COMPOSER.md` and `C_OVERSIGHT.md`: read.

## Clerk and verification

- `EXP-GED-001/CLERK/P3_CLERK_LOG.md`: read in full.
- `P3/verification/RESULTING_STATE_1.md`: read.

## Harness (`P3/harness/`)

- `build_backend.py`, `mcp.py`, `INTERFACE.md`, `mcp_session.json`, `gate.py`, `access_boundary.py` and `ingest_run.sh`: read.
- `backend.bin`: decoded by my scripts.

## Store and interfaces

- `/home/user/enterprise_store`: all 17 files hashed. I read every file in `forecasts/`, `internal/` and `reference/`, plus `national_monthly.csv` and `smi_monthly.csv`. `regional_monthly.csv`, `survey_cells.csv` and `age_monthly.csv` were parsed by my scripts, including the West rows, to test whether West can be reconstructed. `custom/`: hashed only.
- `/home/user/p3_iface_r1`–`r4`: hashed, and each `backend.bin` decoded.
- `r1` `mcp.py`: executed for three probe queries (log in `audit/ab_probe/`).

## Runs

**Condition A, `runs/r1–r3/A`:**
- `ANSWERS.md`, `AUDIT.md` and `SOURCE.txt`: read.
- `mcp_log.jsonl`: parsed, chain verified and replayed.

**Condition A, `r4/A`:**
- `ANSWERS.md` and `AUDIT.md`: compared byte-for-byte with r1.
- `mcp_log.jsonl`: parsed.

**Condition B, `B/access/ACCESS_DETERMINATION.json` (r1, r4):** summaries read.

**Condition B, `B/final` (r1–r3):**
- `FINAL_ANSWER.md` and `GATE_RESULT*.txt`: read.
- `COMPOSER_HANDBACK.md`: read for r1 and r2.
- `PROVENANCE*.json`: parsed by script.

**Condition B, `B/analyst` (r1–r4):**
- `CLAIM_LEDGER.json`: parsed by script.
- `ARGUMENT.md`: r3, grep for the Q3.7 handling only.
- Other files: not read. For r4, files were compared by diff against r1.

**Condition B, `B/challenge`:**
- `HANDBACK.md` (r1–r3): read.
- `READ_LOG.md` (r3): first 12 lines.
- `COUNTERARGUMENT.md` (r3): grep only.
- `r_*.json` (r1): hashed.
- r4 files: compared by diff against r1.

**Condition B, `B/magistrate` (r1–r4):**
- `HANDBACK.md`: read.
- `READ_LOG.md`: read for r1 and r4; grep for r2 and r3.
- `DETERMINATION.md`: r4 §1–3 read; r3 and r2 grep.
- `APPROVED_CLAIMS*.json`: parsed.
- r2 `CORRECTION_1.md`: read.
- Saved data files: compared with the Magistrates' own logs.
- `magistrate_check.py` (r1) and `compute.py` (r2, r3): header lines read, and re-run on scratch copies.

## Git

- `git log`, `git show --stat`, `git diff fb634ef HEAD` (matter and harness), `git show <commit>:gate.py` and `git fetch --all`.
- `git ls-tree` and `git show` on `origin/exp-ged-001-p3-a-r1..r3` and `origin/exp-ged-001-p3-interface`.

## Written (all in `P3/audit/`)

- `AUDIT_STAGE1.md` and `READ_LOG.md`.
- Scripts, each with its output file: `verify_hashes.sh`, `backend_check.py`, `recompute.py`, `verify_logs.py`, `tabulate.py`, `disclosure_scan.py`, `provenance_trace.py`, `r2_mapping_check.py`, `a_bypass_check.py` and `r4_perturbed_q2.py`.
- `gate_probe/` with `gate_probe_output.txt`, `ab_probe/` with `ab_probe_output.txt`, and `gate_rerun_output.txt`.

No external action was taken. Nothing was pushed, and no enterprise or interface file was modified.
