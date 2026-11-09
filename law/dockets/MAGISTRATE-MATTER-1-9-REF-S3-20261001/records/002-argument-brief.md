> **PUBLIC READING COPY.** Atlas case docket entry 2 — MAGISTRATE-MATTER-1-9-REF-S3-20261001.
> - **Entry:** 2
> - **Date filed:** 10/01/2026
> - **Filed by:** Advocate
> - **Original source sha256:** 10_ARGUMENT_BRIEF.md `f052076de361367e7bddd01dfa8641b823b4bcd1bb06c096faf5337491068339`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists and Batch-1 scrub gate. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 002 — Argument brief

## Source document: 10_ARGUMENT_BRIEF.md

# Argument Brief

| Field | Value |
|---|---|
| Actor | Argument. This actor is not the Magistrate and does not decide the referral. |
| Magistrate instance | `MAGINST-1-9-S3-20261001-3e4975dabadc` |
| Matter | `1-9` |
| Referral | `REF-1-9-S3-DIVERGENCE-20261001` |
| Question | Under S3, which review controls 1-9 `daily_ew_four` paper deltas at the execution gate — MAG-1-9-007 (designated; `blocks_execution` false) or MAG-1-9-004 (said to be selected by the resolver; `blocks_execution` true) — and what, if anything, should the gate do pending resolver change? |
| Counterargument | Not read. Not relied on. |

## Assigned position, and what of it the record supports

The position this actor was instructed to argue was:

> MAG-1-9-004 is what controls 1-9 `daily_ew_four` paper deltas at the live execution gate today, because that is the review the existing resolver selects, and pending an authorized resolver change the gate should keep following that selection.

**Concession.** The clause "because that is the review the existing resolver selects" is false on this record. It is abandoned. Once that clause is abandoned, the further clause that MAG-1-9-004 is what controls the live gate today is also abandoned. The existing resolver selects MAG-1-9-007. The live gate follows that function. MAG-1-9-007 is the review the gate applies to these paper deltas today.

What remains, and what this brief maintains:

Pending an authorized change to selection semantics, the gate should keep following the review the existing resolver selects. That review is MAG-1-9-007. Putting MAG-1-9-004 in its place at the gate would be a change of selection, which the governing supplemental decision told implementation not to make on its own.

## How the resolver chooses, and what it chooses

`controlling_review_resolution` keeps schema-valid, `is_authoritative` J-0020 reviews for the project. It orders them by `utc`, newest first. A candidate is selected only if `may_supersede_controller` allows it to replace every other authoritative review. See `[private path withheld] (`is_human_reserved_act` at lines 291–298, `_adopted_human_order_cited` at 301–326, `may_supersede_controller` at 330–346, `_select_controlling_review` at 349–364, `controlling_review_resolution` at 536–672). File sha256 `d3e4d2044bd03a53097922dd0bec718f0280f1225c512bc3dd336c5275d8e13e`.

A review is human-reserved when `user_decision_required` is true and its class is `MAGISTRATE_REVIEW`. A later machine review replaces that reserved review only when the later review cites, in `required_predecessors` or `applicable_authority`, an `O-` order file that contains the text `IT IS SO ORDERED`. Later `utc` alone does not replace it.

Applied to the nine current `MAG-1-9*.json` files, by a read-only recomputation that used the same content-hash rule as `provenance.content_sha256` (`[private path withheld] lines 71–77 and 301–321) and the same selection rules, and that matched each seal to the ledger entry at the recorded `ledger_seq`:

| Review | utc | Seal-authoritative | `user_decision_required` | `blocks_execution` | Adopted order cited in the resolver's fields |
|---|---|---|---|---|---|
| MAG-1-9-007 | 2026-08-31T19:17:07+00:00 | yes | false | false | `O-PROJECT-1-9-PAPER-FORWARD` |
| MAG-1-9-006 | 2026-08-31T17:50:32+00:00 | yes | false | false | `O-PROJECT-1-9-PAPER-FORWARD` |
| MAG-1-9-005 | 2026-08-31T16:57:27+00:00 | yes | false | false | `O-PROJECT-1-9-PAPER-FORWARD` |
| MAG-1-9-004 | 2026-08-31T13:39:39+00:00 | yes | true | true | `O-PROJECT-1-9-EXECUTION-PROOF` |
| MAG-1-9-XDOMAIN-RESTORE-20260901 | 2026-09-01T15:37:28+00:00 | no (content hash mismatch) | true | absent | none |
| MAG-1-9-XDOMAIN-TRUE-HUMAN-20260901 | 2026-09-01T15:35:06+00:00 | no (content hash mismatch) | true | absent | none |

MAG-1-9-001, MAG-1-9-002, and MAG-1-9-003 are also seal-authoritative and older than MAG-1-9-004. None of them is the newest unblocked candidate.

MAG-1-9-004 is human-reserved. MAG-1-9-007 is not. MAG-1-9-007's `required_predecessors` include `O-PROJECT-1-9-PAPER-FORWARD`. That order's adoption line is `IT IS SO ORDERED — 2026-08-31`. `may_supersede_controller` therefore returns true as `HUMAN_ORDER_RESOLVES_RESERVED_CONTROLLER`. Newest-first selection stops at MAG-1-9-007. It never reaches MAG-1-9-004. The two 2026-09-01 XDOMAIN records are newer and human-reserved, and they fail the content hash, so they are outside the authoritative set. That is the same rejection the live function recorded.

This recomputation did not import `atlas_gov` and did not call `controlling_review_resolution`. The package init calls `ensure_room_registered`, and `controlling_review_resolution` appends `STALE_AUTHORITY_FALLBACK.jsonl` through `_log_stale_authority_fallback` (magistrate.py lines 118–174). The live function has already written its own result.

**Live call, same function.** `[private path withheld], sha256 `55d0b982d0f4badb426f908720047d00427b617909193983ba06698699042e40`, lines 1–2, both `utc` `2026-10-01T13:40:48+00:00`, caller `resolve_controlling_mag@p19_paper_forward_cycle.py`. Both rows set `older_decision_selected` to `MAG-1-9-007` and reject the two XDOMAIN records for `NOT_AUTHORITATIVE` / `CONTENT_HASH_MISMATCH_POST_SEAL_MUTATION_OR_TAMPER`. `p19_paper_forward_cycle.resolve_controlling_mag` calls `controlling_review_resolution` (`[private path withheld] lines 94–98). `p19_daily_ew_cycle.resolve_controlling_mag` calls the same function (`[private path withheld] lines 38–41).

The supplemental decision's recorded hash of `magistrate.py` was `e5fedccb9cc55e9581630f2c6ad8707a793c7b17095a4f25f26840300e488f1b`. The file hashed for this brief is `d3e4d2044bd03a53097922dd0bec718f0280f1225c512bc3dd336c5275d8e13e`. The selection above is from the current text, as read. The 13:40 log is from the function as it ran that hour. Both return MAG-1-9-007 for 1-9. The vested-validation screen in the current function (lines 581–607) does not remove MAG-1-9-007: that review has neither `decision_maker` `MAGISTRATE_VESTED` nor a `vested_decision` object.

## Where the "resolver selects MAG-1-9-004" sentence came from

`KNOWN_RESOLVER_DIVERGENCES.jsonl` says `resolver_selects` is `MAG-1-9-004` and `gate_outcome_differs` is true. That sentence was written as a literal in `[private path withheld] lines 51–52. The script hashes the review files. It does not call `controlling_review_resolution`. The referral record, written by the same script, repeats the question in that form and sets `does_not_change_controlling_selection` true. A docket assertion that does not execute the resolver is not the resolver's selection, and the script's own flag says it leaves selection unchanged.

The same-day live log, at 13:40 UTC, is earlier than the divergence write at 18:34:07Z. Before the divergence row existed, the live resolver had already selected MAG-1-9-007.

## What the execution gate does with that selection

The `daily_ew_four` cycle checks the resolver before it builds a broker request. `submit_deltas` calls `resolve_controlling_mag` and returns without submission when `execution_blocked` or `unknown` is set (`p19_daily_ew_cycle.py` lines 227–240). `execution_blocked` is true when the selected review has `blocks_execution` true, a HOLD / HUMAN_RESERVED disposition, `does_not_submit_paper_orders`, or `does_not_authorize_new_orders` (lines 45–50).

If that check passes, `submit_market_orders` calls `authorize_submit` (`[private path withheld] lines 540–548). `authorize_submit` loads `latest_controlling_review`, which is `controlling_review_resolution` again, and returns `MAGISTRATE_HOLD_BLOCKS_SUBMIT` when that review's disposition is HOLD / HUMAN_RESERVED or `blocks_execution` is true (`[private path withheld] lines 176–180; file sha256 `69020bdf782dbc305c272d16b4b5be1328c7be3cfc74950076200a63621efe46`, the same hash the supplemental decision recorded for this file).

MAG-1-9-007's disposition is `ROUTE`. `blocks_execution` is false. It does not set `does_not_submit_paper_orders` or `does_not_authorize_new_orders`. `precise_states.PAPER_ORDERS_OPERATIVE` is `AUTHORIZED_DEF4_DAILY_EW_FOUR`. `order_authorized_paper_deltas_permitted` is true. On those fields, both the cycle's pre-check and `authorize_submit`'s magistrate block leave the submit path open as far as the magistrate check is concerned. This brief does not say a particular cycle will pass every other prerequisite in `authorize_submit`. It says the magistrate check, given the review the resolver returns, does not block on `blocks_execution`.

**Concession on what MAG-1-9-004 would do if it were the selected review.** Its `blocks_execution` is true, its disposition is `ROUTE`, and `precise_states.PAPER_ORDERS_OPERATIVE` is `NOT_AUTHORIZED_WHILE_MAG_1_9_002_HOLD_PRESERVED`. Its `next_required` is `HUMAN_DECISION_OPERATIVE_PAPER_FORWARD_OR_PROJECT_CLOSEOUT`. It does not mention `daily_ew_four`. If the resolver returned it, both the cycle pre-check and `authorize_submit` would stop the submit with `MAGISTRATE_HOLD_BLOCKS_SUBMIT`. The resolver does not return it. The gate outcome that would follow from MAG-1-9-004 is a result under a selection the gate does not make.

**Concession on MAG-1-9-007's own supersession list.** `supersedes_controller_of` names only `MAG-1-9-006`. The resolver does not read that field. Selection of MAG-1-9-007 over MAG-1-9-004 is `may_supersede_controller` plus `utc`, because MAG-1-9-007 cites `O-PROJECT-1-9-PAPER-FORWARD`. It is not a declaration inside MAG-1-9-007 that MAG-1-9-004 has been rewritten. The Human order says MAG-1-9-004 is not rewritten. That preservation is consistent with MAG-1-9-004 remaining a sealed record and with MAG-1-9-007 being the review the resolver returns.

## Human order and prior Magistrate decisions

`O-PROJECT-1-9-PAPER-FORWARD-DAILY-EW` (Human adoption `IT IS SO ORDERED — 2026-08-31`) authorizes recurring paper-only `daily_ew_four` deltas on the existing $1,000 sleeve. Its Magistrate paragraph preserves MAG-1-9-006 as history and says the next sealed Magistrate review for this release is MAG-1-9-007. It states that it does not rewrite MAG-1-9-004. It does not install MAG-1-9-004 as the release review.

`O-PROJECT-1-9-PAPER-FORWARD` (same adoption line) is the order MAG-1-9-007, MAG-1-9-006, and MAG-1-9-005 cite. Its own next-review sentence names MAG-1-9-005 for that earlier release. It likewise says it does not rewrite MAG-1-9-004. The resolver's citation test treats that adopted order as enough for MAG-1-9-007 to replace the reserved MAG-1-9-004. The test does not require the cited order to be `O-PROJECT-1-9-PAPER-FORWARD-DAILY-EW`.

**Concession.** MAG-1-9-007 does not list `O-PROJECT-1-9-PAPER-FORWARD-DAILY-EW` in `required_predecessors` or `applicable_authority`. The reason the resolver returns MAG-1-9-007 is the `PAPER-FORWARD` citation together with newer `utc`, not a citation of the daily-EW order inside those two fields. This brief does not describe the current resolver as an encoding of S3's act-scoped rule.

Supplemental decision S3 (`32_MAGISTRATE_SUPPLEMENTAL_DECISION.json`, holding at the `S3` object) states two propositions that this referral has to keep separate:

1. Where an adopted Human order designates a review for a stated class of acts, that review controls that act until the Human amends the designation or a later review of that same act cites the designating order. Applied to 1-9: MAG-1-9-007 was and is the lawful controlling review for `daily_ew_four` paper deltas.
2. The then-current resolver selects per project by `utc` with human-reserved exceptions and is not act-scoped. Implementation shall not change selection semantics on its own. It shall record the rule as a known divergence and refer any matter in which the divergence would change a gate outcome.

**Concession.** Proposition 1 is a merits holding of instance `MAGINST-HREF-20260930-df9a5799984b`. Under O-VESTED-MAGISTRATE §V, a merits disposition controls the proposition actually adjudicated. This brief does not ask that S3's designation holding be reopened. On the files as they stand, that holding and the resolver's return name the same review for this gate: MAG-1-9-007.

Proposition 2 is why this referral exists. The referral was supposed to be filed where the divergence would change a gate outcome. For this matter the measured return does not change the gate relative to the designated review. Both are MAG-1-9-007, and `blocks_execution` on that review is false. The row that says the resolver selects MAG-1-9-004 is the unimplemented literal described above. A rule-text difference can still be described: S3's supersession condition asks for a later review of the same act that cites the designating daily-EW order; the code's condition accepts any adopted `O-` citation. That difference does not, on these files, select MAG-1-9-004 or flip `blocks_execution` at the gate.

The first decision, question 18, stated the status quo in the same direction: present controlling authority is whatever the unmodified resolver selects, and in particular 1-9 is controlled by MAG-1-9-007. That holding was a declaration of the status quo pending remand. The supplemental decision left the first decision's other holdings standing. The live 2026-10-01 log and the current selection rules are the same status quo.

J-0020's limitation "Not live trading" is the subject of supplemental holding S6. S6 reads a controlling J-0020 review as a fail-closed veto at `authorize_submit` lines 176–182, and reads the review as never itself the authority to trade. This brief uses that only to identify what the gate does with the selected review's `blocks_execution` flag. Authority for the paper deltas, if any, remains the adopted project orders. MAG-1-9-007 says `does_not_create_new_authority` true and `does_not_authorize_live` true.

## What the gate should do pending an authorized resolver change

S3's implementation instruction is: do not change selection semantics; refer a matter when the divergence would change a gate outcome. The gate's magistrate check already is the resolver: `latest_controlling_review` in `authorize_submit`, and the same function in `p19_daily_ew_cycle.resolve_controlling_mag`.

Pending an authorized change to those selection semantics, the gate should keep calling that function and should keep applying the review it returns. The review it returns for 1-9 is MAG-1-9-007. A local substitution of MAG-1-9-004 at the daily cycle or inside `authorize_submit` would be a change of which review controls the gate. Nothing in the Human daily-EW order, in question 18, or in S3's instruction to leave selection semantics in place authorizes that substitution.

If a later authorized change narrowed `_adopted_human_order_cited` so that only a citation of `O-PROJECT-1-9-PAPER-FORWARD-DAILY-EW` could replace MAG-1-9-004, MAG-1-9-007 would then fail that narrower test, because it does not cite the daily-EW order in the two fields the function reads, and MAG-1-9-004 could become the selected review. That would be a new selection rule. It is not the rule in the file today. This brief does not ask for it. Until such a change is authorized and made in the resolver, the gate's existing call already applies MAG-1-9-007, and that is the review that controls these paper deltas at the live gate.

## Exhibits

Sha256 values below were computed on the file bytes for this brief, except where a cell quotes a hash recorded inside another exhibit.

| Exhibit | Path | sha256 |
|---|---|---|
| Instance constitution (procedure) | `[private path withheld] | `c3086c7b509757da90311da7d180971b039de26fb66740c0f6766aa402dc8544` |
| Referral docket line | `[private path withheld] | `a13773fdba3b1954320765328764b7f3ce1dffa12863e120e3f5a7631a90e3dd` |
| Referral record | `[private path withheld] | `ca41ad8ded95d872bf51c7831f94b058079a61f49805c28e96bfe261d2d699d3` |
| Divergence row (hardcoded selection claim) | `[private path withheld] | `45b8491ffc04db1e2fba76de9e75a9047156121474667ffe86d271e1e09bfaf5` |
| Script that wrote the hardcoded claim | `[private path withheld] | `91f59d648ef81ac78590bbd3957942b7efbf04c87f84dd56c20010f0ef81fc6e` |
| Implementation log | `[private path withheld] | `e1f595f06d7e81fecb9eb3c5519496e53e6e614a22e71608c695e0a8ebfe5bc7` |
| MAG-1-9-004 | `[private path withheld] | `e1cf338631eb745a9e51e5022061279abc870881ae194ca73e630c10d446cf3a` |
| MAG-1-9-007 | `[private path withheld] | `33381de41b8091494a976bdce95f9419ad77df098a89646269f4d3489018cc2a` |
| MAG-1-9-002 | `[private path withheld] | `cd65c6a36193230f96c85042f6ebaffb1a613b6d22009a58dc294f0dc7788efe` |
| MAG-1-9-005 | `[private path withheld] | `95f23e0fc0f51c3dff51be126348d5f358c15a8130bfaa3fd304489924e1a40e` |
| MAG-1-9-006 | `[private path withheld] | `ee9f1d180aade8e1c61802114dcf5f97e0c2eacd7db7a0dfb395a005e697c9c6` |
| XDOMAIN TRUE-HUMAN | `[private path withheld] | `ca689edfcfdd6cea90bb5cc48d00a141fdae2a276d5609e005be67430ca8784d` |
| XDOMAIN RESTORE | `[private path withheld] | `bda31b95795c3d60b7e41283bd95defa27a7e979410610e768658286ffe27e0c` |
| Daily-EW Human order | `[private path withheld] | `80536412358718ae9f1075414e0786ebbc2837caf3f439fdde57103f989e76cf` |
| Paper-forward Human order | `[private path withheld] | `8ff5fbf4e4576469573be437f206ad8929035ebe6f82d2d2dc9ff240b5ac07f2` |
| Resolver | `[private path withheld] | `d3e4d2044bd03a53097922dd0bec718f0280f1225c512bc3dd336c5275d8e13e` |
| Execution gate | `[private path withheld] | `69020bdf782dbc305c272d16b4b5be1328c7be3cfc74950076200a63621efe46` |
| Submit path that calls the gate | `[private path withheld] | `d504acf77dec814f26fb893b43ebf4a73df2ad14494725029d45c9dcbf71f01a` |
| Daily EW cycle | `[private path withheld] | `98e74382f482b843203cbe72e3773fd98f64a011ea53545e9dcf5bbadc5c10fd` |
| Paper-forward cycle (live log caller) | `[private path withheld] | `cc8dac1196a404022ac42aa28690ada5aceb4d205069eb5217eda764552cbbc7` |
| Live resolver log | `[private path withheld] | `55d0b982d0f4badb426f908720047d00427b617909193983ba06698699042e40` |
| Supplemental decision (S3, S6, S7) | `[private path withheld] | `cc1b4f98f024f883c23f685adb45e1fdbf05063c090e4c4516ba52f0edb8c398` |
| First decision, question 18 | `[private path withheld] | `ddad0a8272ae39f7a0873fa56e76e3fa1c2595284074fce1bdbe3d73f0c36ecf` |
| O-VESTED-MAGISTRATE §V | `[private path withheld] | `bcbf0248cfdcb147dfeb6c681f16a79ca50f9f6101f5eac3eeea47540f524b7f` |
| J-0020 | `[private path withheld] | `de7e5f2a3f724565baf4c24da3f5e92a67cf33f28da765b011d1cf3021ac4292` |

No code, sealed review, referral status, trade, or message was changed in preparing this brief.
