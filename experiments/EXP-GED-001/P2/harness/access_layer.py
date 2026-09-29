#!/usr/bin/env python3
"""EXP-GED-001 Phase 2 — test-harness ACCESS LAYER (not Atlas).

Stands in for the enterprise's own data-access layer. It is deterministic. From the
authoritative store and the machine-readable policy it builds one view per client
BEFORE any client question is seen:
  * copies only the datasets the client is licensed for;
  * row-filters region-bearing tables to the client's licensed regions;
  * drops forecast fields the client may not receive unless the data dictionary marks
    them "AI-visible for explanation" (those are kept, flagged non-disclosable);
  * writes authorization_manifest.json (machine-readable) and CLIENT_CONTEXT.md.
Usage: access_layer.py <store_dir> <views_dir>
"""
import csv, json, os, shutil, sys, hashlib

AI_VISIBLE_NOT_DISCLOSABLE = {
    "forecasts/forecast_drivers_Q4.csv": ["input_latest_value"],
    "forecasts/forecast_run_metadata.json": ["run_notes_internal"],
}

def read_csv(p):
    with open(p, newline="") as f:
        r = csv.DictReader(f); return r.fieldnames, list(r)

def write_csv(p, fields, rows):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

def build(store, views):
    pol = json.load(open(os.path.join(store, "policy/authorization_policy.json")))
    for cid, c in pol["clients"].items():
        out = os.path.join(views, cid)
        if os.path.exists(out): shutil.rmtree(out)
        os.makedirs(out)
        withheld = []
        for ds in c["datasets"]:
            src, dst = os.path.join(store, ds), os.path.join(out, ds)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if ds.endswith(".csv"):
                fields, rows = read_csv(src)
                if "region" in fields:
                    before = len(rows); rows = [r for r in rows if r["region"] in c["regions"]]
                    if len(rows) != before: withheld.append(f"{ds}: rows for regions not licensed ({before-len(rows)} rows removed)")
                if ds == "forecasts/forecast_drivers_Q4.csv":
                    keep = [f for f in fields if f in c["forecast_disclosure"] or f in AI_VISIBLE_NOT_DISCLOSABLE[ds]]
                    dropped = [f for f in fields if f not in keep]
                    if dropped: withheld.append(f"{ds}: fields removed {dropped}")
                    fields = keep; rows = [{k: r[k] for k in keep} for r in rows]
                write_csv(dst, fields, rows)
            else:
                shutil.copyfile(src, dst)
        manifest = {
            "client_id": cid, "client_name": c["name"], "tier": c["tier"],
            "policy_id": pol["policy_id"], "determined_by": "access_layer.py (deterministic; before any question)",
            "datasets_in_view": c["datasets"], "licensed_regions": c["regions"],
            "forecast_fields_client_may_receive": c["forecast_disclosure"],
            "ai_visible_but_not_client_disclosable": {k: v for k, v in AI_VISIBLE_NOT_DISCLOSABLE.items() if k in c["datasets"]},
            "withheld_by_access_layer": withheld,
            "rules": pol["global_rules"],
        }
        json.dump(manifest, open(os.path.join(out, "authorization_manifest.json"), "w"), indent=1)
        open(os.path.join(out, "CLIENT_CONTEXT.md"), "w").write(
            f"# Client context\n\nYou are serving **{c['name']}** (client id {cid}, {c['tier']} tier), a client of Halvorsen Insights.\n"
            f"This directory is the client's read-only view of Halvorsen data. `authorization_manifest.json` states what this client may receive.\n")
    print("built", ", ".join(pol["clients"]))

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
