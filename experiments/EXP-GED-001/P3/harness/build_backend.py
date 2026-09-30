#!/usr/bin/env python3
"""Packages the authoritative store into backend.bin for the simulated interface, with a classification
catalog derived from the store's policy and data dictionary. Deterministic.
Usage: build_backend.py <store_dir> <out_dir>"""
import base64, json, os, sys, zlib

def classify(path, pol):
    a, b = pol["clients"]["CL-A"], pol["clients"]["CL-B"]
    if path.startswith("internal/"): return {"classification": "INTERNAL — PROPRIETARY", "licensed_to": [], "note": "Halvorsen internal; not licensed to any client"}
    if path.startswith("policy/"): return {"classification": "INTERNAL — GOVERNANCE", "licensed_to": [], "note": "Enterprise authorization policy"}
    if path.startswith("custom/"): return {"classification": "CLIENT-CONFIDENTIAL", "licensed_to": ["CL-A"], "note": "Commissioned by and licensed only to CL-A"}
    lic = [c for c, v in pol["clients"].items() if path in v["datasets"]]
    out = {"classification": "CLIENT-LICENSED", "licensed_to": lic}
    if path in ("observations/survey_cells.csv", "metrics/regional_monthly.csv"):
        out["note"] = "Region rows licensed per client: " + "; ".join(f"{c}: {', '.join(v['regions'])}" for c, v in pol["clients"].items())
    if path == "forecasts/forecast_drivers_Q4.csv":
        out["note"] = "Field licensing: contribution_pp licensed to " + ", ".join(c for c, v in pol["clients"].items() if "contribution_pp" in v["forecast_disclosure"]) + "; input_latest_value is not client-disclosable"
    if path == "forecasts/forecast_run_metadata.json":
        out["note"] = "run_notes_internal is not client-disclosable"
    return out

def main(store, out):
    pol = json.load(open(os.path.join(store, "policy/authorization_policy.json")))
    files = {}
    for root, _, fs in os.walk(store):
        for f in fs:
            p = os.path.relpath(os.path.join(root, f), store)
            if p == "README.md": continue
            files[p] = open(os.path.join(root, f), encoding="utf-8").read()
    ctx = {}
    for cid, c in pol["clients"].items():
        ctx[cid] = {"client_name": c["name"], "tier": c["tier"], "policy_id": pol["policy_id"], "licensed_datasets": c["datasets"],
                    "licensed_regions": c["regions"], "forecast_fields_client_may_receive": c["forecast_disclosure"],
                    "custom_studies": c["custom_studies"], "rules": pol["global_rules"]}
    be = {"catalog": {p: classify(p, pol) for p in sorted(files)}, "files": files, "client_context": ctx}
    raw = json.dumps(be, sort_keys=True, ensure_ascii=False).encode()
    open(os.path.join(out, "backend.bin"), "wb").write(base64.b64encode(zlib.compress(raw, 9)))
    print("resources:", len(files))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
