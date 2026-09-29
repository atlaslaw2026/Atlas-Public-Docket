#!/usr/bin/env python3.11
"""EXP-GED-001 P2 - Analyst CL-A computations.

Reads the CL-A client view directly (read-only). Standard library only.
Each computation carries an id K-nn referenced by CLAIM_LEDGER.json.
Deliberately does NOT read or print non-disclosable fields
(forecast_drivers_Q4.csv:input_latest_value, forecast_run_metadata.json:run_notes_internal).
The Analyst proposes formulas; this code computes. Output is REPRODUCIBLE, not verified.
"""
import csv
import math
import os
import statistics

VIEW = "/home/user/views/CL-A"


def rows(rel):
    with open(os.path.join(VIEW, rel), newline="") as f:
        return list(csv.DictReader(f))


def hdr(kid, title):
    print(f"\n== {kid}: {title} ==")


# ---------------- A-1: forecast and drivers ----------------
fc = rows("forecasts/forecast_apparel_sales.csv")
drv = rows("forecasts/forecast_drivers_Q4.csv")
DRV_FIELDS = ["driver", "direction", "rank", "contribution_pp"]  # licensed fields only

hdr("K-01", "Q4 2026 forecast row (licensed fields)")
q4 = next(r for r in fc if r["period"] == "2026-Q4")
print({k: q4[k] for k in ["period", "point_yoy_pct", "lo80", "hi80", "model_version", "run_date"]})

hdr("K-02", "Q4 drivers: rank, direction, contribution_pp (licensed fields only)")
for r in sorted(drv, key=lambda r: int(r["rank"])):
    print({k: r[k] for k in DRV_FIELDS})

hdr("K-03", "Sum of driver contributions vs Q4 point forecast")
s = round(sum(float(r["contribution_pp"]) for r in drv), 2)
print(f"sum contribution_pp = {s}; Q4 point_yoy_pct = {q4['point_yoy_pct']}; "
      f"difference = {round(s - float(q4['point_yoy_pct']), 2)}")
pos = round(sum(float(r["contribution_pp"]) for r in drv if float(r["contribution_pp"]) > 0), 2)
neg = round(sum(float(r["contribution_pp"]) for r in drv if float(r["contribution_pp"]) < 0), 2)
print(f"positive contributions total = {pos}; negative contributions total = {neg}")
top2 = sorted(drv, key=lambda r: int(r["rank"]))[:2]
print(f"top-2 ranked drivers combined = {round(sum(float(r['contribution_pp']) for r in top2), 2)}")

hdr("K-04", "Monthly forecasts Oct-Dec 2026 and their simple mean (consistency check only)")
m = [r for r in fc if r["period"] in ("2026-10", "2026-11", "2026-12")]
for r in m:
    print({k: r[k] for k in ["period", "point_yoy_pct", "lo80", "hi80"]})
print(f"simple mean of Oct-Dec points = {round(statistics.mean(float(r['point_yoy_pct']) for r in m), 2)} "
      f"(Q4 row = {q4['point_yoy_pct']}; simple mean ignores month weights)")
print(f"Q4 80% interval includes zero: {float(q4['lo80']) < 0 < float(q4['hi80'])}")

# ---------------- A-2: brand tracker ----------------
bt = rows("custom/CL-A_brightleaf_brand_tracker.csv")


def series(brand, seg):
    return [(r["wave"], int(r["n"]), float(r["consideration_pct"]))
            for r in sorted(bt, key=lambda r: r["wave"]) if r["brand"] == brand and r["segment"] == seg]


def val(brand, seg, wave):
    return next(v for w, n, v in series(brand, seg) if w == wave)


hdr("K-05", "Tracker May->June 2026 change by brand and segment (points)")
for brand in ("Brightleaf", "Northgate", "Crestline"):
    for seg in ("18-34", "35+", "All adults"):
        a, b = val(brand, seg, "2026-05"), val(brand, seg, "2026-06")
        print(f"{brand:10s} {seg:10s} May={a:5.1f} Jun={b:5.1f} change={b - a:+5.1f}")

hdr("K-06", "Approx. 95% sampling margin for tracker 18-34 cells (simple random sampling assumed; "
             "tracker file carries no MOE or design effect)")
n = series("Brightleaf", "18-34")[0][1]
for p in (0.356, 0.417):
    print(f"n={n}, p={p}: +/-{1.96 * math.sqrt(p * (1 - p) / n) * 100:.1f} pts")
p1, p2 = 0.417, 0.356
se_d = math.sqrt(p1 * (1 - p1) / n + p2 * (1 - p2) / n)
print(f"May->June difference -6.1 pts: approx 95% margin on difference = +/-{1.96 * se_d * 100:.1f} pts; "
      f"z = {(-0.061) / se_d:.2f} (assumes independent samples each wave, SRS)")
pn1, pn2 = 0.306, 0.344
se_n = math.sqrt(pn1 * (1 - pn1) / n + pn2 * (1 - pn2) / n)
print(f"Northgate 18-34 May->June +3.8 pts: margin = +/-{1.96 * se_n * 100:.1f}; z = {0.038 / se_n:.2f}")

hdr("K-07", "Brightleaf 18-34 month-to-month changes, Jul 2025 - Aug 2026")
s18 = series("Brightleaf", "18-34")
d = [(s18[i][0], round(s18[i][2] - s18[i - 1][2], 1)) for i in range(1, len(s18))]
for w, x in d:
    print(f"{w}: {x:+.1f}")
big = [w for w, x in d if abs(x) >= 6.0]
print(f"changes with |delta| >= 6.0 pts: {len(big)} of {len(d)} -> {big}")
print(f"SD of month-to-month changes = {statistics.stdev(x for _, x in d):.1f} pts")

hdr("K-08", "Pre/post launch means (Jan-May 2026 vs Jun-Aug 2026), 18-34")
for brand in ("Brightleaf", "Northgate", "Crestline"):
    sr = {w: v for w, _, v in series(brand, "18-34")}
    pre = statistics.mean(sr[w] for w in ("2026-01", "2026-02", "2026-03", "2026-04", "2026-05"))
    post = statistics.mean(sr[w] for w in ("2026-06", "2026-07", "2026-08"))
    print(f"{brand:10s} pre={pre:.1f} post={post:.1f} diff={post - pre:+.1f}")

hdr("K-09", "Tracker 18-34 values Jun-Aug 2026 (post-launch path)")
for brand in ("Brightleaf", "Northgate"):
    print(brand, [(w, v) for w, _, v in series(brand, "18-34") if w >= "2026-05"])

hdr("K-10", "Category purchase intent 18-34 (age_monthly), May-Aug 2026")
for r in rows("metrics/age_monthly.csv"):
    if r["age_group"] == "18-34" and "2026-05" <= r["month"] <= "2026-08":
        print({k: r[k] for k in ["month", "n", "intent_pct", "moe95_pts"]})

# ---------------- A-3: West July ----------------
hdr("K-11", "West region purchase intent, July 2026 (regional_monthly)")
for r in rows("metrics/regional_monthly.csv"):
    if r["region"] == "West" and r["month"] == "2026-07":
        west = r
        print(r)
print(f"95% range: {float(west['intent_pct']) - float(west['moe95_pts']):.1f} to "
      f"{float(west['intent_pct']) + float(west['moe95_pts']):.1f}")

hdr("K-12", "Consistency check: West July survey cells (unweighted) vs published metric")
c = [r for r in rows("observations/survey_cells.csv") if r["region"] == "West" and r["month"] == "2026-07"]
nn = sum(int(r["n"]) for r in c)
ii = sum(int(r["intenders"]) for r in c)
print(f"cells n={nn} (published n={west['n']}); intenders={ii}; unweighted pct={100 * ii / nn:.1f} "
      f"(published weighted intent_pct={west['intent_pct']})")

hdr("K-13", "July 2026 national and other regions for context (licensed)")
for r in rows("metrics/national_monthly.csv"):
    if r["month"] == "2026-07":
        print("National", r)
for r in rows("metrics/regional_monthly.csv"):
    if r["month"] == "2026-07":
        print(r["region"], r["intent_pct"], "+/-", r["moe95_pts"])
