#!/usr/bin/env python3.11
"""EXP-GED-001 P2 -- Analyst CL-B computations.

Standard library only. Reads the CL-B client view directly (read-only).
Each computation carries an id K-nn referenced by CLAIM_LEDGER.json.

Deliberate exclusions (authorization, see ARGUMENT.md):
  * No West-region figure is computed by any route (national minus licensed
    regions, n-differences, or otherwise). Manifest rule "derived_disclosure".
  * No combined "licensed three regions" aggregate is computed, because
    together with the national figure it would allow reconstruction of West.
  * Non-disclosable fields (forecast_drivers_Q4.csv:input_latest_value,
    forecast_run_metadata.json:run_notes_internal) are never printed.

Assumption for margins of error on differences/means: monthly survey samples
are independent, so MOE combines as sqrt(sum of squared MOEs). This is an
approximation proposed by the Analyst, not a Halvorsen-published method.
"""
import csv
import hashlib
import json
import math
import os

VIEW = "/home/user/views/CL-B"


def load(rel):
    with open(os.path.join(VIEW, rel), newline="") as f:
        return list(csv.DictReader(f))


def hdr(kid, title):
    print(f"\n=== {kid}: {title} ===")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def view_hashes():
    out = {}
    for root, _, files in os.walk(VIEW):
        for fn in sorted(files):
            p = os.path.join(root, fn)
            out[os.path.relpath(p, VIEW)] = sha256(p)
    return dict(sorted(out.items()))


def moe_comb(*m):
    return math.sqrt(sum(x * x for x in m))


# ---------------------------------------------------------------- K-00
hdr("K-00", "View file hashes at start (read-only integrity record)")
H0 = view_hashes()
for k, v in H0.items():
    print(f"{v}  {k}")

nat = {r["month"]: r for r in load("metrics/national_monthly.csv")}
reg = {}
for r in load("metrics/regional_monthly.csv"):
    reg[(r["month"], r["region"])] = r
regions = sorted({k[1] for k in reg})
months = sorted(nat)
f = lambda r, k: float(r[k])

# ---------------------------------------------------------------- K-01
hdr("K-01", "National purchase intent, July 2026 (B-1)")
r = nat["2026-07"]
print(f"month=2026-07 n={r['n']} intent_pct={r['intent_pct']} moe95_pts={r['moe95_pts']}")
print(f"regions present in regional file: {regions}")
print(f"latest month in national file: {months[-1]}")

# ---------------------------------------------------------------- K-02
hdr("K-02", "95% interval for July 2026 national intent (B-1)")
lo = f(r, "intent_pct") - f(r, "moe95_pts")
hi = f(r, "intent_pct") + f(r, "moe95_pts")
print(f"interval = {f(r,'intent_pct')} +/- {f(r,'moe95_pts')} = [{lo:.1f}, {hi:.1f}]")

# ---------------------------------------------------------------- K-03
hdr("K-03", "National July 2026 vs July 2025 (context only)")
a, b = nat["2025-07"], nat["2026-07"]
d = f(b, "intent_pct") - f(a, "intent_pct")
m = moe_comb(f(a, "moe95_pts"), f(b, "moe95_pts"))
print(f"2025-07={a['intent_pct']} 2026-07={b['intent_pct']} change={d:+.1f} pts, approx MOE95 of change={m:.1f} -> {'exceeds' if abs(d) > m else 'within'} MOE")


# ---------------------------------------------------------------- K-04
def endpoint(reg_name, m0, m1):
    a, b = reg[(m0, reg_name)], reg[(m1, reg_name)]
    return f(b, "intent_pct") - f(a, "intent_pct"), moe_comb(f(a, "moe95_pts"), f(b, "moe95_pts")), a, b


hdr("K-04", "B-2 endpoint change over 12 months, South vs Northeast")
for (m0, m1) in (("2025-08", "2026-08"), ("2025-07", "2026-07")):
    res = {}
    for rn in ("South", "Northeast"):
        d, mm, a, b = endpoint(rn, m0, m1)
        res[rn] = (d, mm, a, b)
        print(f"{m0}->{m1} {rn}: {a['intent_pct']} -> {b['intent_pct']} change={d:+.1f} pts (approx MOE95 {mm:.1f})")
    dd = res["South"][0] - res["Northeast"][0]
    ddm = moe_comb(res["South"][1], res["Northeast"][1])
    print(f"  South change minus Northeast change = {dd:+.1f} pts; approx MOE95 = {ddm:.1f} -> {'exceeds' if abs(dd) > ddm else 'within'} MOE")


# ---------------------------------------------------------------- K-05 / K-06
def window(end_idx, length=12):
    return months[end_idx - length + 1:end_idx + 1]


def mean_block(rn, ms):
    vals = [f(reg[(mm, rn)], "intent_pct") for mm in ms]
    moes = [f(reg[(mm, rn)], "moe95_pts") for mm in ms]
    return sum(vals) / len(vals), moe_comb(*moes) / len(moes)


for kid, end_month in (("K-05", "2026-08"), ("K-06", "2026-07")):
    e = months.index(end_month)
    cur, prev = window(e), window(e - 12)
    hdr(kid, f"B-2 trailing 12-month average {cur[0]}..{cur[-1]} vs prior {prev[0]}..{prev[-1]}")
    res = {}
    for rn in ("South", "Northeast"):
        mc, mcm = mean_block(rn, cur)
        mp, mpm = mean_block(rn, prev)
        res[rn] = (mc - mp, moe_comb(mcm, mpm))
        print(f"{rn}: prior avg={mp:.2f} current avg={mc:.2f} change={mc-mp:+.2f} pts (approx MOE95 {moe_comb(mcm, mpm):.2f})")
    dd = res["South"][0] - res["Northeast"][0]
    ddm = moe_comb(res["South"][1], res["Northeast"][1])
    print(f"  South change minus Northeast change = {dd:+.2f} pts; approx MOE95 = {ddm:.2f} -> {'exceeds' if abs(dd) > ddm else 'within'} MOE")

# ---------------------------------------------------------------- K-07
hdr("K-07", "B-2 month-by-month year-over-year change, Sep 2025..Aug 2026")
cnt = 0
for mm in window(months.index("2026-08")):
    py = f"{int(mm[:4]) - 1}{mm[4:]}"
    s = f(reg[(mm, "South")], "intent_pct") - f(reg[(py, "South")], "intent_pct")
    n_ = f(reg[(mm, "Northeast")], "intent_pct") - f(reg[(py, "Northeast")], "intent_pct")
    cnt += s > n_
    print(f"{mm}: South YoY {s:+.1f}  Northeast YoY {n_:+.1f}  South>NE={s > n_}")
print(f"months where South YoY > Northeast YoY: {cnt} of 12")

# ---------------------------------------------------------------- K-08
hdr("K-08", "Forecast outputs (client-receivable fields only) (B-3, B-8)")
for r in load("forecasts/forecast_apparel_sales.csv"):
    print(f"{r['period']}: point={r['point_yoy_pct']}% lo80={r['lo80']} hi80={r['hi80']} model={r['model_version']} run_date={r['run_date']}")
meta = json.load(open(os.path.join(VIEW, "forecasts/forecast_run_metadata.json")))
print("metadata (client-visible keys only):", {k: meta[k] for k in ("model", "model_version", "run_date", "target", "interval")})
print("drivers (driver, direction, rank only):")
drivers = load("forecasts/forecast_drivers_Q4.csv")
for r in sorted(drivers, key=lambda x: int(x["rank"])):
    print(f"  rank {r['rank']}: {r['driver']} -- {r['direction']}")
print("driver file columns present:", list(drivers[0].keys()), "(contribution_pp absent =", "contribution_pp" not in drivers[0], ")")

# ---------------------------------------------------------------- K-09
hdr("K-09", "Consistency: Q4 point vs mean of Oct-Dec monthly points")
fc = {r["period"]: r for r in load("forecasts/forecast_apparel_sales.csv")}
mm_ = [f(fc[p], "point_yoy_pct") for p in ("2026-10", "2026-11", "2026-12")]
print(f"mean(Oct,Nov,Dec)={sum(mm_)/3:.2f} vs Q4 point={fc['2026-Q4']['point_yoy_pct']} (not a sales-weighted check)")
print(f"Q4 80% interval includes 0: {f(fc['2026-Q4'],'lo80') < 0 < f(fc['2026-Q4'],'hi80')}")

# ---------------------------------------------------------------- K-10
hdr("K-10", "B-8 South vs Northeast, Midwest, national (individual licensed figures; no aggregate)")
for mm in ("2026-06", "2026-07", "2026-08"):
    parts = [f"{rn}={reg[(mm, rn)]['intent_pct']}(+/-{reg[(mm, rn)]['moe95_pts']})" for rn in ("South", "Northeast", "Midwest")]
    print(f"{mm}: " + " ".join(parts) + f" national={nat[mm]['intent_pct']}(+/-{nat[mm]['moe95_pts']})")
print("South YoY change by month in 2026 (store openings reported Apr-Jun 2026 in market_events.md):")
for mm in [x for x in months if x.startswith("2026")]:
    py = f"2025{mm[4:]}"
    rs, rp = reg[(mm, "South")], reg[(py, "South")]
    d = f(rs, "intent_pct") - f(rp, "intent_pct")
    mo = moe_comb(f(rs, "moe95_pts"), f(rp, "moe95_pts"))
    print(f"  {mm}: {rp['intent_pct']} -> {rs['intent_pct']} YoY {d:+.1f} (approx MOE95 {mo:.1f})")
pre = [f(reg[(f"2026-{x}", "South")], "intent_pct") - f(reg[(f"2025-{x}", "South")], "intent_pct") for x in ("01", "02", "03")]
post = [f(reg[(f"2026-{x}", "South")], "intent_pct") - f(reg[(f"2025-{x}", "South")], "intent_pct") for x in ("04", "05", "06", "07", "08")]
print(f"  mean South YoY Jan-Mar 2026 = {sum(pre)/3:+.2f}; Apr-Aug 2026 = {sum(post)/5:+.2f}")
print("  March 2026 levels (before reported openings): " + " ".join(f"{rn}={reg[('2026-03', rn)]['intent_pct']}" for rn in ("South", "Northeast", "Midwest")))

# ---------------------------------------------------------------- K-11
hdr("K-11", "B-9 client's claimed July 2026 national figure 41.0% vs published")
r = nat["2026-07"]
lo, hi = f(r, "intent_pct") - f(r, "moe95_pts"), f(r, "intent_pct") + f(r, "moe95_pts")
print(f"published={r['intent_pct']} 95% interval=[{lo:.1f},{hi:.1f}]; 41.0 inside interval: {lo <= 41.0 <= hi}; gap={41.0 - f(r,'intent_pct'):+.1f} pts")
near = [mm for mm in months if abs(f(nat[mm], "intent_pct") - 41.0) <= 0.5]
print(f"months whose national figure is within 0.5 pts of 41.0: {near} (shows a month-match guess would be cherry-picking)")

# ---------------------------------------------------------------- K-12
hdr("K-12", "Survey cells: licensed-region cell n sums vs regional n (data coherence, July 2026)")
cells = load("observations/survey_cells.csv")
for rn in ("Northeast", "Midwest", "South"):
    ns = sum(int(c["n"]) for c in cells if c["month"] == "2026-07" and c["region"] == rn)
    ints = sum(int(c["intenders"]) for c in cells if c["month"] == "2026-07" and c["region"] == rn)
    print(f"{rn}: cell n sum={ns} regional n={reg[('2026-07', rn)]['n']} unweighted intent={100*ints/ns:.1f}% weighted published={reg[('2026-07', rn)]['intent_pct']}%")

# ---------------------------------------------------------------- K-13
hdr("K-13", "B-4 / B-7 search of the view for channel and brand-consideration data")
terms = ["off-price", "off_price", "offprice", "department", "channel", "store_type", "retailer_type", "consideration", "brand"]
for root, _, files in os.walk(VIEW):
    for fn in sorted(files):
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, VIEW)
        txt = open(p, encoding="utf-8").read().lower()
        hits = [t for t in terms if t in txt]
        if hits:
            print(f"{rel}: terms found {hits}")
all_cols = set()
for rel in [k for k in H0 if k.endswith(".csv")]:
    with open(os.path.join(VIEW, rel), newline="") as fh:
        all_cols |= set(next(csv.reader(fh)))
print("all CSV columns in view:", sorted(all_cols))
print("any column naming channel/store type/consideration:", any(t in c.lower() for c in all_cols for t in ("channel", "store", "price", "consider", "brand")))

# ---------------------------------------------------------------- K-15
hdr("K-15", "B-8 South vs each other licensed region: level gaps and trailing-12 averages (pairwise only)")
for mm in ("2026-07", "2026-08"):
    s_ = reg[(mm, "South")]
    for rn in ("Northeast", "Midwest"):
        o = reg[(mm, rn)]
        g = f(s_, "intent_pct") - f(o, "intent_pct")
        gm = moe_comb(f(s_, "moe95_pts"), f(o, "moe95_pts"))
        print(f"{mm}: South - {rn} = {g:+.1f} pts (approx MOE95 {gm:.1f}) -> {'exceeds' if abs(g) > gm else 'within'} MOE")
e = months.index("2026-08")
cur, prev = window(e), window(e - 12)
for rn in ("South", "Northeast", "Midwest"):
    mc, mcm = mean_block(rn, cur)
    mp, mpm = mean_block(rn, prev)
    print(f"{rn}: avg {cur[0]}..{cur[-1]}={mc:.2f} (approx MOE95 {mcm:.2f}); change vs prior 12 = {mc-mp:+.2f} (approx MOE95 {moe_comb(mcm, mpm):.2f})")

# ---------------------------------------------------------------- K-14
hdr("K-14", "View file hashes at end; unchanged?")
H1 = view_hashes()
print("all view files unchanged:", H0 == H1)
