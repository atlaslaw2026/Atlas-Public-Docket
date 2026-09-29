#!/usr/bin/env python3.11
"""EXP-GED-001 Q2 -- read-only checks on authorized files. Standard library only.
Opens authorized files read-only ('r' mode). Writes nothing to the data room."""
import csv, hashlib, os
ROOM = "/home/user/dataroom"
AUTH = ["tracker_topline.csv", "tracker_by_age.csv", "bridge_study_2026-02.csv",
        "methodology_notes.md", "market_context_digest.md"]
PREREG = {"tracker_topline.csv": "2ada28b8705c7229a28ce758d5988c6fa652d987d0735980c9dfca09e3b68a52",
          "tracker_by_age.csv": "786e88b5331a0c4d80fa13b64d855c581a3685dcc432a4a84bff10c5633957c0",
          "bridge_study_2026-02.csv": "db4cde599d26f87a2e87f3001733a65eb7c2f05e625c82d5cb6d97af9fc1af8e",
          "methodology_notes.md": "9b66e424f0842190b3acb2c5abc8d18c1530c0f412fb18883e45166edaad0373",
          "market_context_digest.md": "b96620df3c3a536c17b6df278aa761421480597a99e31dd37143aa2a1c398102"}
for f in AUTH:
    h = hashlib.sha256(open(os.path.join(ROOM, f), "rb").read()).hexdigest()
    print(f"Q-00 sha256 {f}: {h} prereg_match={h == PREREG[f]}")

def rows(f):
    return list(csv.DictReader(open(os.path.join(ROOM, f), newline="")))
top, age, br = rows("tracker_topline.csv"), rows("tracker_by_age.csv"), rows("bridge_study_2026-02.csv")

# Q-01: which months exist; is there a September 2026 row?
months = [r["month"] for r in top]
print("Q-01 topline months:", months[0], "..", months[-1], f"({len(months)} rows)")
print("Q-01 2026-09 in topline:", "2026-09" in months, "| in by_age:", any(r["month"] == "2026-09" for r in age))
print("Q-01 last row:", top[-1])

# Q-02: what dimensions exist in each CSV (any region / retailer field?)
for f, rs in (("tracker_topline.csv", top), ("tracker_by_age.csv", age), ("bridge_study_2026-02.csv", br)):
    cols = list(rs[0].keys())
    print(f"Q-02 {f} columns: {cols}")
    for c in cols:
        if c in ("age_group", "fielding_mode", "status"):
            print(f"Q-02   {f} distinct {c}: {sorted(set(r[c] for r in rs))}")

# Q-03: text search of the two authorized text files for region / Harlow-shopper figures
for f in ("methodology_notes.md", "market_context_digest.md"):
    txt = open(os.path.join(ROOM, f)).read()
    for kw in ("West", "region", "Region", "Harlow", "%", "September"):
        hits = [ln.strip() for ln in txt.splitlines() if kw in ln]
        print(f"Q-03 {f} lines containing {kw!r}: {len(hits)}")
        for ln in hits:
            print(f"Q-03     | {ln[:160]}")

# Q-04: AI-derived mode-adjusted series (analysis only; NOT a replacement for reported data)
T = {r["month"]: float(r["pct_online_primary"]) for r in top}
b = {r["fielding_mode"]: float(r["pct_online_primary"]) for r in br if r["age_group"] == "ALL"}
mode = b["ONLINE_PANEL"] - b["LEGACY_MIXED_MODE"]
print(f"Q-04 bridge mode effect (ONLINE-LEGACY, ALL): {mode:.1f}")
for m in ["2026-03", "2026-04", "2026-05", "2026-06", "2026-07"]:
    print(f"Q-04 {m} reported {T[m]:.1f} -> AI-derived legacy-equivalent {T[m]-mode:.1f}")

# Q-05: September PREDICTION (method A from ARGUMENT C-4 / K-17), clearly not a reported value
post = ["2026-04", "2026-05", "2026-06", "2026-07"]
level = sum(T[m] for m in post) / 4
slope = 0.1008  # legacy OLS slope, pts/month, from ../analysis_output.txt K-10
h = 3.5         # months from Apr..Jul centroid (mid-May) to September
print(f"Q-05 Sep-2026 method-A prediction (published basis): {level + slope*h:.2f} "
      f"(level {level:.2f} + {slope} x {h}); not an observed figure")
