> **PUBLIC READING COPY.** Atlas case docket entry 7 — MAGISTRATE-MATTER-1-9-REF-S3-20261001.
> - **Entry:** 7
> - **Date filed:** 10/02/2026 12:06:27 PM PDT
> - **Filed by:** Magistrate / Gate
> - **Original source sha256:** 40_EXECUTION_GATE_OBSERVATION.json `29ca0b80061d250ac80564c8d4e617cd4aad1fdb6e5ea5056df2cc8d5c35cdc6`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists and Batch-1 scrub gate. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 007 — Execution gate observation

## Source document: 40_EXECUTION_GATE_OBSERVATION.json

{
  "act": "daily_ew_four_paper_deltas",
  "authorize_submit_callable": {
    "callable": true,
    "signature": "(req: 'dict[str, Any]') -> 'dict[str, Any]'"
  },
  "broker_order_created": false,
  "controlling_review_resolution": {
    "CURRENT_STATE_CONFLICT": false,
    "HUMAN_AUTHORITY_UNRESOLVED": null,
    "NO_VALID_CONTROLLING_MAGISTRATE_ACT": false,
    "authority_class": "MAGISTRATE_REVIEW",
    "fail_closed": false,
    "historical_not_controlling_004": [],
    "historical_not_controlling_007": [],
    "historical_not_controlling_count": 2,
    "ok": true,
    "reason": null,
    "schema_valid_not_controlling": [
      "MAG-1-9-XDOMAIN-RESTORE-20260901",
      "MAG-1-9-XDOMAIN-TRUE-HUMAN-20260901",
      "MAG-1-9-006",
      "MAG-1-9-005",
      "MAG-1-9-004",
      "MAG-1-9-003",
      "MAG-1-9-002",
      "MAG-1-9-001"
    ],
    "schema_valid_not_controlling_contains_004": true,
    "schema_valid_not_controlling_contains_007": false,
    "selected_REVIEW_ID": "MAG-1-9-007",
    "selected_blocks_execution": false,
    "selected_disposition": "ROUTE",
    "selected_user_decision_required": false
  },
  "daily_ew_magistrate_leg": {
    "REVIEW_ID": "MAG-1-9-007",
    "blocks_execution": false,
    "disposition": "ROUTE",
    "execution_blocked": false,
    "reason": null,
    "unknown": false,
    "user_decision_required": false
  },
  "follows_ruling": true,
  "forced": false,
  "gate_vs_ruling": "FOLLOWS_RULING",
  "limits_observed_from_order_text_not_executed": {
    "no_live": true,
    "note": "Order limits preserved by non-execution of broker submit; observation only.",
    "paper_only": true,
    "sleeve": "1000",
    "symbols": [
      "AJG",
      "CRL",
      "TGT",
      "PCG"
    ]
  },
  "matter_decision_in_findings_magistrate": [],
  "matter_decision_path": "[private path withheld]",
  "method": "ordinary_atlas_gov.magistrate.controlling_review_resolution + daily_ew resolve_controlling_mag semantics",
  "new_review_created": false,
  "project_id": "1-9",
  "resolver_code_modified": false,
  "schema": "atlas-1-9-ref-s3-gate-observation.v1",
  "utc": "2026-10-02T19:06:27Z"
}
