> **PUBLIC READING COPY.** Atlas case docket entry 4 — MAGISTRATE-MATTER-1-9-REF-S3-20261001.
> - **Entry:** 4
> - **Date filed:** 10/02/2026
> - **Filed by:** Spawning actor / Constitution
> - **Original source sha256:** 02_MAGISTRATE_INSTANCE_CONSTITUTION.md `ccf519a528a9ca7f53c4f3b3ae93f8351ecf845f2e64f88640b9c102306427e9`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists and Batch-1 scrub gate. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 004 — Instance constitution (decision pack)

## Source document: 02_MAGISTRATE_INSTANCE_CONSTITUTION.md

# Magistrate Instance Constitution

| Field | Value |
|---|---|
| Magistrate instance ID | `[magistrate instance id withheld]` |
| Matter | `1-9` |
| Referral | `REF-1-9-S3-DIVERGENCE-20261001` |
| Spawning authority | Human instruction to finish the open referral under the standing rule that the filing actor supplies the matter and the record, and the Magistrate retrieves her own governing authorities. Filing standing for an unresolved Magistrate-jurisdiction question: `HO-MAGISTRATE-FILING-REFERRAL-STANDING-20260927`. |
| Spawning actor | Cursor session that located the open referral. That actor summarized prior decisions before this constitution. It does not control this disposition. |
| Adjudicator | A separately constituted computational agent. Not `magistrate_vested.py`. Not `atlas_gov.magistrate_independent.conduct_independent_review`. |

## Record supplied

The referral record, and only that record, is supplied by path:

- `[private path withheld]
- `[private path withheld]

No governing order, judgment, sealed review, or prior holding is copied into this constitution.

## Limits on the spawning actor

The spawning actor may establish this instance and point at the referral record. It may not state a proposed disposition, select between reviews, change resolver selection, submit an order, or rewrite a sealed review.

## Output (form only)

Write both files under `[private path withheld]

1. `30_MAGISTRATE_DECISION.json` — magistrate_instance_id; matter; referral_id; spawning_authority; governing authorities actually retrieved (path and hash); evidence actually read (path and hash); prior decisions cited; disposition; whether original; binding effect and its limits; what the execution gate is to do; reasoning tied to evidence; what is proven, strongly supported, and unproven; timestamps.
2. `31_STATEMENT_OF_REASONS.md` — the same reasons in readable form.

Do not modify sealed files under `findings\magistrate\`. Do not change resolver code. Do not trade.
