# EXP-GED-001 — Evidence register

Stable evidence IDs cited by the findings (`FINDINGS.md`) and by the white paper. **Kind:** C = contemporaneous evidence produced during the experiment by the acting component; D = design or pre-registration; I = later interpretation (audit, scoring, findings). Hashes are SHA-256 of the files at the time this register was generated; first commit is the commit that added each file to the branch `claude/exp-governed-enterprise-data`.

## E-01 · Design / pre-registration

Experiment definition, hypothesis, design (Phase 3)

| File | SHA-256 | First commit |
|---|---|---|
| `P3/00_matter/MATTER.md` | `f018fa2311c00579…` | fb634ef 2026-09-30T20:31:58+00:00 |

## E-02 · Design / pre-registration

Pre-registration with sealed-item hashes (pushed before any Phase 3 run)

| File | SHA-256 | First commit |
|---|---|---|
| `P3/00_matter/PREREGISTRATION.md` | `6a65cd1cb45c200b…` | fb634ef 2026-09-30T20:31:58+00:00 |

## E-03 · Design / pre-registration

Authoritative store integrity manifest

| File | SHA-256 | First commit |
|---|---|---|
| `P3/00_matter/STORE_MANIFEST.sha256` | `31b63bac6e05ba8d…` | fb634ef 2026-09-30T20:31:58+00:00 |

## E-04 · Design / pre-registration

Authorization policy (client identities, licenses, disclosure rules)

| File | SHA-256 | First commit |
|---|---|---|
| `P3/00_matter/authorization_policy.json` | `086172634a6de95e…` | fb634ef 2026-09-30T20:31:58+00:00 |

## E-05 · Design / pre-registration

Simulated MCP-style interface: specification, code, manifest

| File | SHA-256 | First commit |
|---|---|---|
| `P3/00_matter/INTERFACE_SPEC.md` | `d47678e960b2bf76…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `P3/harness/mcp.py` | `a025a35ac96fff28…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `P3/harness/build_backend.py` | `a3978963a8ec1f17…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `P3/harness/INTERFACE.md` | `bbf91fa09e6c819f…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `P3/00_matter/INTERFACE_MANIFEST.sha256` | `6456fa790bf1f69a…` | fb634ef 2026-09-30T20:31:58+00:00 |

## E-06 · Design / pre-registration

Exact client questions (identical in both conditions)

| File | SHA-256 | First commit |
|---|---|---|
| `P3/00_matter/QUESTIONS.md` | `4b2f4a7fe8ae2fd3…` | fb634ef 2026-09-30T20:31:58+00:00 |

## E-07 · Design / pre-registration

Exact prompts for every office

| File | SHA-256 | First commit |
|---|---|---|
| `P3/00_matter/prompts/A_CONDITION.md` | `d5735cbbd6abe294…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `P3/00_matter/prompts/B1_ANALYST.md` | `98a845bb583fdc8c…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `P3/00_matter/prompts/B2_CHALLENGER.md` | `6a2832875338ea3b…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `P3/00_matter/prompts/B3_MAGISTRATE.md` | `5c2f16538e9866f1…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `P3/00_matter/prompts/B4_COMPOSER.md` | `161f62b734296740…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `P3/00_matter/prompts/C1_AUDITOR.md` | `5b84ad7394db3490…` | 4cd3981 2026-09-30T21:12:48+00:00 |
| `P3/00_matter/prompts/C_OVERSIGHT.md` | `0b3398e67069e1ec…` | fb634ef 2026-09-30T20:31:58+00:00 |

## E-08 · Design / pre-registration

Private Atlas steps not performed; experiment-built components

| File | SHA-256 | First commit |
|---|---|---|
| `P3/00_matter/PRIVATE_STEPS_NOT_PERFORMED.md` | `a0b13540a8e75cc5…` | fb634ef 2026-09-30T20:31:58+00:00 |

## E-09 · Contemporaneous evidence

Condition A run r1: answer, interface log (requests and returned data), agent audit, source commit

| File | SHA-256 | First commit |
|---|---|---|
| `P3/runs/r1/A/ANSWERS.md` | `49bbb0cd647931fb…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r1/A/mcp_log.jsonl` | `6f3496df48c55100…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r1/A/AUDIT.md` | `5a8f17e33cce3143…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r1/A/SOURCE.txt` | `4e45225cfe7e2bc2…` | 0e2af7a 2026-09-30T20:35:06+00:00 |

## E-10 · Contemporaneous evidence

Condition A run r2

| File | SHA-256 | First commit |
|---|---|---|
| `P3/runs/r2/A/ANSWERS.md` | `6bda18698545cd96…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r2/A/mcp_log.jsonl` | `afc686bcfc8fb4da…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r2/A/AUDIT.md` | `f8791332fb029a41…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r2/A/SOURCE.txt` | `f1888460c93ef93b…` | 0e2af7a 2026-09-30T20:35:06+00:00 |

## E-11 · Contemporaneous evidence

Condition A run r3

| File | SHA-256 | First commit |
|---|---|---|
| `P3/runs/r3/A/ANSWERS.md` | `1f75e7eadc30b562…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r3/A/mcp_log.jsonl` | `f3bd5eeb4fe75755…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r3/A/AUDIT.md` | `8322f781c141e257…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r3/A/SOURCE.txt` | `d74833baa3840613…` | 0e2af7a 2026-09-30T20:35:06+00:00 |

## E-12 · Contemporaneous evidence

Access-boundary determinations for each A run (deterministic; experiment-built)

| File | SHA-256 | First commit |
|---|---|---|
| `P3/harness/access_boundary.py` | `308190da4d74ec34…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `P3/runs/r1/B/access/ACCESS_DETERMINATION.json` | `b3f1c3692079609b…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r2/B/access/ACCESS_DETERMINATION.json` | `6b8a19888dc02660…` | 0e2af7a 2026-09-30T20:35:06+00:00 |
| `P3/runs/r3/B/access/ACCESS_DETERMINATION.json` | `3ae983f7952853fd…` | 0e2af7a 2026-09-30T20:35:06+00:00 |

## E-13 · Contemporaneous evidence

Condition B Analyst (truth boundary): claim ledgers, arguments, computations, own interface logs

| File | SHA-256 | First commit |
|---|---|---|
| `P3/runs/r1/B/analyst/CLAIM_LEDGER.json` | `933c8352db06ddfe…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r1/B/analyst/ARGUMENT.md` | `a56f07f77b93daf5…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r1/B/analyst/analysis.py` | `48d88010ae1768b2…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r1/B/analyst/analysis_output.txt` | `03943fe481e82c11…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r1/B/analyst/mcp_log.jsonl` | `bceae8f95cde71c0…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r1/B/analyst/HANDBACK.md` | `fa01ac5d48530ddd…` | 11cac0b 2026-09-30T20:46:11+00:00 |
| `P3/runs/r1/B/analyst/READ_LOG.md` | `02b8e8cefd0d87f3…` | 184918f 2026-09-30T20:45:01+00:00 |
| `P3/runs/r2/B/analyst/CLAIM_LEDGER.json` | `9877a9ee6fa588e3…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r2/B/analyst/ARGUMENT.md` | `653802bfb77e580c…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r2/B/analyst/analysis.py` | `839eda3f6becd6cc…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r2/B/analyst/analysis_output.txt` | `2201aa8466548d72…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r2/B/analyst/mcp_log.jsonl` | `08a693a487748a60…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r2/B/analyst/HANDBACK.md` | `2ef6a4009bdcc0f1…` | 184918f 2026-09-30T20:45:01+00:00 |
| `P3/runs/r2/B/analyst/READ_LOG.md` | `475c8a0429f00de3…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r3/B/analyst/CLAIM_LEDGER.json` | `280033ae52aafbac…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r3/B/analyst/ARGUMENT.md` | `e69f8ba4a2317267…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r3/B/analyst/analysis.py` | `1c9a4ab79b7f28fb…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r3/B/analyst/analysis_output.txt` | `bd86662bf617e9a9…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r3/B/analyst/mcp_log.jsonl` | `eaf4bf06e39e2a34…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r3/B/analyst/HANDBACK.md` | `c4ab03b5b7efd1da…` | 413d746 2026-09-30T20:44:32+00:00 |
| `P3/runs/r3/B/analyst/READ_LOG.md` | `863e240bf26fc351…` | 413d746 2026-09-30T20:44:32+00:00 |

## E-14 · Contemporaneous evidence

Condition B independent Challengers

| File | SHA-256 | First commit |
|---|---|---|
| `P3/runs/r1/B/challenge/COUNTERARGUMENT.md` | `705d02d45e51efe5…` | f50b59d 2026-09-30T20:53:21+00:00 |
| `P3/runs/r1/B/challenge/reconstruct.py` | `83d72ba3dfb7bf05…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r1/B/challenge/reconstruct_output.txt` | `cd6d4ba2673ef38e…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r1/B/challenge/mcp_log.jsonl` | `2082ea0529be29d1…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r1/B/challenge/HANDBACK.md` | `d6ef6877ac55e182…` | 85ee394 2026-09-30T20:54:48+00:00 |
| `P3/runs/r1/B/challenge/READ_LOG.md` | `c47cfc0d9ed0bd91…` | 85ee394 2026-09-30T20:54:48+00:00 |
| `P3/runs/r2/B/challenge/COUNTERARGUMENT.md` | `7282a7b122e04650…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r2/B/challenge/reconstruct.py` | `5a2bdc21b7752261…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r2/B/challenge/reconstruct_output.txt` | `e2657bdefdfe4265…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r2/B/challenge/mcp_log.jsonl` | `f3bd0675d2c7589f…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r2/B/challenge/HANDBACK.md` | `fc3d29d6a8b46730…` | f50b59d 2026-09-30T20:53:21+00:00 |
| `P3/runs/r2/B/challenge/READ_LOG.md` | `faab5f8ee9a85408…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r3/B/challenge/COUNTERARGUMENT.md` | `23eb1d58dd5cfe51…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r3/B/challenge/reconstruct.py` | `29f9ca3cd6f1968a…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r3/B/challenge/reconstruct_output.txt` | `cbf4ca7036c81ad3…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r3/B/challenge/mcp_log.jsonl` | `7136b6ce6f261756…` | 11cac0b 2026-09-30T20:46:11+00:00 |
| `P3/runs/r3/B/challenge/HANDBACK.md` | `907d9c062c25968d…` | 691bade 2026-09-30T20:52:46+00:00 |
| `P3/runs/r3/B/challenge/READ_LOG.md` | `5dc270bcd4cff780…` | 691bade 2026-09-30T20:52:46+00:00 |

## E-15 · Contemporaneous evidence

Magistrate determinations and machine-readable approved/rejected claims

| File | SHA-256 | First commit |
|---|---|---|
| `P3/runs/r1/B/magistrate/DETERMINATION.md` | `20f70fa8fa87e0df…` | c1bec3d 2026-09-30T21:02:55+00:00 |
| `P3/runs/r1/B/magistrate/APPROVED_CLAIMS.json` | `c33a4677c16f7bcc…` | cdb846f 2026-09-30T21:01:40+00:00 |
| `P3/runs/r1/B/magistrate/mcp_log.jsonl` | `d07977f1ee916c33…` | 2500dae 2026-09-30T21:00:14+00:00 |
| `P3/runs/r1/B/magistrate/READ_LOG.md` | `3625ff8237e56665…` | c1bec3d 2026-09-30T21:02:55+00:00 |
| `P3/runs/r1/B/magistrate/HANDBACK.md` | `edb62e06fbfb3b34…` | ec80b2d 2026-09-30T21:03:48+00:00 |
| `P3/runs/r2/B/magistrate/DETERMINATION.md` | `868ba4260f9429bc…` | b5bdc39 2026-09-30T21:01:04+00:00 |
| `P3/runs/r2/B/magistrate/APPROVED_CLAIMS.json` | `297a3e53b9156b97…` | 2500dae 2026-09-30T21:00:14+00:00 |
| `P3/runs/r2/B/magistrate/mcp_log.jsonl` | `6ed880f621e080e0…` | 85ee394 2026-09-30T20:54:48+00:00 |
| `P3/runs/r2/B/magistrate/READ_LOG.md` | `c65299cbf5376ec0…` | b5bdc39 2026-09-30T21:01:04+00:00 |
| `P3/runs/r2/B/magistrate/HANDBACK.md` | `5aed4f47c861de80…` | cdb846f 2026-09-30T21:01:40+00:00 |
| `P3/runs/r3/B/magistrate/DETERMINATION.md` | `ade81d438cddaefc…` | 2500dae 2026-09-30T21:00:14+00:00 |
| `P3/runs/r3/B/magistrate/APPROVED_CLAIMS.json` | `b69704d61e45a408…` | 2500dae 2026-09-30T21:00:14+00:00 |
| `P3/runs/r3/B/magistrate/mcp_log.jsonl` | `943b1f07ffdcaba2…` | f7fcdba 2026-09-30T20:53:31+00:00 |
| `P3/runs/r3/B/magistrate/READ_LOG.md` | `a77a5f469d937fd8…` | 2500dae 2026-09-30T21:00:14+00:00 |
| `P3/runs/r3/B/magistrate/HANDBACK.md` | `bc6c57647a7b67bc…` | 2500dae 2026-09-30T21:00:14+00:00 |

## E-16 · Contemporaneous evidence

r2 Magistrate linked correction (Q7.4R) after gate failure

| File | SHA-256 | First commit |
|---|---|---|
| `P3/runs/r2/B/magistrate/APPROVED_CLAIMS_CORRECTION_1.json` | `ef5c87b888717dab…` | ec80b2d 2026-09-30T21:03:48+00:00 |
| `P3/runs/r2/B/magistrate/CORRECTION_1.md` | `2096d71d0ecb59b0…` | ec80b2d 2026-09-30T21:03:48+00:00 |

## E-17 · Contemporaneous evidence

Condition B final client answers, provenance, gate results

| File | SHA-256 | First commit |
|---|---|---|
| `P3/runs/r1/B/final/FINAL_ANSWER.md` | `4ac832e6239d8d71…` | f26803b 2026-09-30T21:04:50+00:00 |
| `P3/runs/r1/B/final/PROVENANCE.json` | `8355885037d6f938…` | f26803b 2026-09-30T21:04:50+00:00 |
| `P3/runs/r1/B/final/GATE_RESULT.txt` | `94f43eb9a94d9bca…` | f10cfe0 2026-09-30T21:05:13+00:00 |
| `P3/runs/r2/B/final/FINAL_ANSWER.md` | `0fc0e777a3fbee11…` | c1bec3d 2026-09-30T21:02:55+00:00 |
| `P3/runs/r2/B/final/PROVENANCE.json` | `c4f3a5299b72fcac…` | c1bec3d 2026-09-30T21:02:55+00:00 |
| `P3/runs/r2/B/final/GATE_RESULT.txt` | `9b59ff7ec16c3239…` | c1bec3d 2026-09-30T21:02:55+00:00 |
| `P3/runs/r3/B/final/FINAL_ANSWER.md` | `99efe48819250242…` | b5bdc39 2026-09-30T21:01:04+00:00 |
| `P3/runs/r3/B/final/PROVENANCE.json` | `4bf9274c7d8070a9…` | b5bdc39 2026-09-30T21:01:04+00:00 |
| `P3/runs/r3/B/final/GATE_RESULT.txt` | `94f43eb9a94d9bca…` | cdb846f 2026-09-30T21:01:40+00:00 |
| `P3/runs/r2/B/final/PROVENANCE_v2.json` | `7bbbf561f0ca7b66…` | 0bfe533 2026-09-30T21:04:37+00:00 |
| `P3/runs/r2/B/final/GATE_RESULT_v2.txt` | `94f43eb9a94d9bca…` | f26803b 2026-09-30T21:04:50+00:00 |
| `P3/harness/gate.py` | `7830b2b0c0486171…` | fb634ef 2026-09-30T20:31:58+00:00 |

## E-18 · Contemporaneous evidence

Magistrate validation run (r4): packet and determination

| File | SHA-256 | First commit |
|---|---|---|
| `P3/runs/r4/A/ANSWERS.md` | `49bbb0cd647931fb…` | b5bdc39 2026-09-30T21:01:04+00:00 |
| `P3/runs/r4/A/mcp_log.jsonl` | `09270f5e1b955df5…` | b5bdc39 2026-09-30T21:01:04+00:00 |
| `P3/runs/r4/B/magistrate/DETERMINATION.md` | `285330cdf7089e3c…` | 8bdd405 2026-09-30T21:12:06+00:00 |
| `P3/runs/r4/B/magistrate/APPROVED_CLAIMS.json` | `4ced4060f576724d…` | 8bdd405 2026-09-30T21:12:06+00:00 |
| `P3/runs/r4/B/magistrate/READ_LOG.md` | `e4f5a909a2811390…` | 8bdd405 2026-09-30T21:12:06+00:00 |

## E-19 · Contemporaneous evidence

Clerk's contemporaneous log: every Clerk act, defect, repair, correction (Phase 3; Phases 1–2 logs alongside)

| File | SHA-256 | First commit |
|---|---|---|
| `CLERK/P3_CLERK_LOG.md` | `6c59cb934433ca00…` | fb634ef 2026-09-30T20:31:58+00:00 |
| `CLERK/P2_CLERK_LOG.md` | `b51512391294280a…` | 3487771 2026-09-29T20:37:44+00:00 |
| `00_matter/CLERK_LOG.md` | `b99dde55e9bda931…` | 0ca94c3 2026-09-29T20:05:10+00:00 |

## E-20 · Contemporaneous evidence

Resulting-state verification 1 (+ addendum)

| File | SHA-256 | First commit |
|---|---|---|
| `P3/verification/RESULTING_STATE_1.md` | `f430f7927f9dabd7…` | 4cd3981 2026-09-30T21:12:48+00:00 |

## E-21 · Later interpretation

Independent audit, stage 1 (blind to answer key)

| File | SHA-256 | First commit |
|---|---|---|
| `P3/audit/AUDIT_STAGE1.md` | `7091f4161e572d78…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `P3/audit/AUDITOR_HANDBACK_STAGE1.md` | `24433ff8f5d1363f…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `P3/audit/READ_LOG.md` | `43ee28167c92af38…` | 24771e1 2026-09-30T21:28:04+00:00 |

## E-22 · Later interpretation

Independent audit, stage 2 (key-scored; results matrix; established / not established)

| File | SHA-256 | First commit |
|---|---|---|
| `P3/audit/AUDIT_STAGE2.md` | `c771140018656e04…` | f8ae65e 2026-09-30T21:34:21+00:00 |
| `P3/audit/AUDITOR_HANDBACK_STAGE2.md` | `4134fea88d527f9d…` | 494fa3e 2026-09-30T21:35:45+00:00 |

## E-23 · Design / pre-registration

Unsealed answer keys, generators, perturbation materials (hash-verified against pre-registrations)

| File | SHA-256 | First commit |
|---|---|---|
| `UNSEALED/P1/ANSWER_KEY_AND_RUBRIC.md` | `30e94e1fbe6eecc5…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P1/ANSWER_KEY_Q2.md` | `a71cbd5b4ead7d38…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P1/USER_QUESTION.txt` | `9c011871029d51c3…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P1/USER_QUESTION_Q2.txt` | `35d13a2c746032a7…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P1/bridge_study_2026-02_PERTURBED.csv` | `54c3e5cb2b44ff30…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P1/dataroom_manifest_sha256.txt` | `da941dfc3bbbe96b…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P1/generate_dataroom.py` | `c2d9270d30da47fb…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P1/generation_log.json` | `fe459e717aeeff69…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P2/ANSWER_KEY_P2.md` | `547b9c09bdb7dd37…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P2/CL-B_perturbed.sha256` | `66c1f9455d7951e2…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P2/QUESTIONS.json` | `2052681d20aa1d38…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P2/generate_store.py` | `144c381c274955f9…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P2/generation_log.json` | `bee32efb022e1519…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P3/ANSWER_KEY_P3.md` | `862301c7a27f32cc…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P3/QUESTIONS_P3.json` | `02b08afe0e27d94a…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P3/backend_PERTURBED.bin` | `519254ea3409c438…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P3/perturb_backend.py` | `00e6f17976420cdd…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/P3/replay_log.py` | `e8360bcb65768195…` | 24771e1 2026-09-30T21:28:04+00:00 |
| `UNSEALED/README.md` | `93144e50b31e6237…` | 24771e1 2026-09-30T21:28:04+00:00 |

## E-24 · Later interpretation

Institutional-memory test: fresh-clone reconstruction

| File | SHA-256 | First commit |
|---|---|---|
| `P3/memory_test/MEMORY_TEST.md` | `04fccdb457bdf6f6…` | f8ae65e 2026-09-30T21:34:21+00:00 |
| `P3/memory_test/PROMPT.md` | `41d988982c902cd3…` | f8ae65e 2026-09-30T21:34:21+00:00 |

## E-25 · Contemporaneous evidence

Pilot Phase 1 record (tracker; contaminated baseline; clean baselines; challenge correction; Magistrate; Clerk leak)

| File | SHA-256 | First commit |
|---|---|---|
| `00_matter/MATTER.md` | `68165d4508d7eebd…` | 32063f6 2026-09-29T20:04:47+00:00 |
| `02_baseline/README.md` | `d1932f9226f97472…` | a9a4bed 2026-09-29T20:09:24+00:00 |
| `04_challenge/COUNTERARGUMENT.md` | `166648796f28e0d9…` | 5460c4d 2026-09-29T20:26:03+00:00 |
| `05_magistrate/DETERMINATION.md` | `ac2f558695d63243…` | 3afdbc6 2026-09-29T20:37:00+00:00 |

## E-26 · Contemporaneous evidence

Pilot Phase 2 record (two clients; views; baselines; governed analysts)

| File | SHA-256 | First commit |
|---|---|---|
| `P2/00_matter/MATTER.md` | `219a2cc15d73472d…` | 7434ce2 2026-09-29T20:31:48+00:00 |
| `P2/00_matter/PREREGISTRATION.md` | `8a2791cdd1983c76…` | 7434ce2 2026-09-29T20:31:48+00:00 |
| `P2/harness/access_layer.py` | `48b0238c29aa2981…` | 712274d 2026-09-29T20:29:01+00:00 |

