#!/usr/bin/env python3.11
"""Challenger (Condition B, r3) independent reconstruction.

Reads ONLY this office's own interface log (challenge/mcp_log.jsonl, CL-B,
read-only calls). Does not import or run the Analyst's analysis.py.
Outputs C-nn computations to stdout (saved as reconstruct_output.txt).
"""
import hashlib, json, math, os, re, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "mcp_log.jsonl")

entries = [json.loads(l) for l in open(LOG)]

# C-00 chain check on own log
print("C-00 own log: entries=%d" % len(entries))
prev = None
ok = True
for e in entries:
    if prev is not None and e.get("prev_hash") != prev:
        ok = False
    prev = e.get("entry_hash")
print("  prev_hash links consistent:", ok)
for e in entries:
    print("  seq%-2s %-18s %s" % (e["seq"], e["tool"], json.dumps(e["args"], sort_keys=True)[:90]))


def resp(tool, **match):
    for e in entries:
        if e["tool"] != tool:
            continue
        if all(e["args"].get(k) == v for k, v in match.items()):
            return e["response"]
    raise KeyError((tool, match))


nat = {r["month"]: r for r in resp("read_resource", resource="metrics/national_monthly.csv")["data"]}
reg_rows = resp("query", resource="metrics/regional_monthly.csv")["data"]
regions_seen = sorted({r["region"] for r in reg_rows})
reg = {}
for r in reg_rows:
    reg.setdefault(r["region"], {})[r["month"]] = r
smi = {r["month"]: float(r["smi"]) for r in resp("read_resource", resource="metrics/smi_monthly.csv")["data"]}
fc = resp("read_resource", resource="forecasts/forecast_apparel_sales.csv")["data"]

f = lambda r, k: float(r[k])


def months(y0, m0, y1, m1):
    out = []
    y, m = y0, m0
    while (y, m) <= (y1, m1):
        out.append("%04d-%02d" % (y, m))
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return out

print()
print("C-01 regions returned by own regional query:", regions_seen, "(West absent: %s)" % ("West" not in regions_seen))

print()
print("C-02 Q1/Q9 national")
for mth in ("2026-06", "2026-07", "2026-08"):
    r = nat[mth]
    print("  %s intent=%s moe=%s n=%s range=%.1f..%.1f" % (mth, r["intent_pct"], r["moe95_pts"], r["n"],
          f(r, "intent_pct") - f(r, "moe95_pts"), f(r, "intent_pct") + f(r, "moe95_pts")))
d = f(nat["2026-07"], "intent_pct") - f(nat["2026-06"], "intent_pct")
md = math.hypot(f(nat["2026-07"], "moe95_pts"), f(nat["2026-06"], "moe95_pts"))
print("  Jun->Jul diff=%+.1f  moe(diff, independent samples)=%.2f" % (d, md))
print("  client 41.0 - Jul 37.6 = %+.1f ; 41.0 in Aug range 39.4..43.4: %s" % (41.0 - 37.6, 39.4 <= 41.0 <= 43.4))

print()
print("C-03 Q2/Q8 12-month averages (licensed regions)")
cur = months(2025, 9, 2026, 8)
pri = months(2024, 9, 2025, 8)
chg = {}
for rg in ("South", "Northeast", "Midwest"):
    a = statistics.mean(f(reg[rg][m], "intent_pct") for m in cur)
    b = statistics.mean(f(reg[rg][m], "intent_pct") for m in pri)
    # moe of avg change: sqrt(sum moe^2)/12 for each window, combined
    ma = math.sqrt(sum(f(reg[rg][m], "moe95_pts") ** 2 for m in cur)) / 12
    mb = math.sqrt(sum(f(reg[rg][m], "moe95_pts") ** 2 for m in pri)) / 12
    chg[rg] = (a - b, math.hypot(ma, mb))
    moes = [f(reg[rg][m], "moe95_pts") for m in cur]
    print("  %-9s cur=%.2f prior=%.2f change=%+.2f moe~%.2f  moe range(12m)=%.1f..%.1f" % (rg, a, b, a - b, math.hypot(ma, mb), min(moes), max(moes)))
dd = chg["South"][0] - chg["Northeast"][0]
print("  South-NE difference=%+.2f moe~%.2f" % (dd, math.hypot(chg["South"][1], chg["Northeast"][1])))

print()
print("C-04 Q2/Q7 year-over-year by month")
for rg in ("South", "Northeast", "Midwest"):
    ys = []
    for m in cur:
        pm = "%04d-%s" % (int(m[:4]) - 1, m[5:])
        ys.append((m, f(reg[rg][m], "intent_pct") - f(reg[rg][pm], "intent_pct")))
    print("  %-9s " % rg + " ".join("%s:%+.1f" % (m[2:], v) for m, v in ys))
    if rg == "South":
        early = [v for m, v in ys if m < "2026-03"]
        late = [v for m, v in ys if m >= "2026-03"]
        print("    South Sep25-Feb26 yoy min=%+.1f max=%+.1f ; Mar-Aug26 min=%+.1f" % (min(early), max(early), min(late)))

print()
print("C-05 Q7 windows (South and comparators)")
for rg in ("South", "Northeast", "Midwest"):
    def win(y, a, b):
        return statistics.mean(f(reg[rg]["%d-%02d" % (y, k)], "intent_pct") for k in range(a, b + 1))
    print("  %-9s Jan-Aug %+.2f | Jan-Mar %+.2f | Apr-Aug %+.2f" % (rg, win(2026, 1, 8) - win(2025, 1, 8), win(2026, 1, 3) - win(2025, 1, 3), win(2026, 4, 8) - win(2025, 4, 8)))
# noise on the South widening (Apr-Aug gap minus Jan-Mar gap), independent months assumed
def mo(rg, y, a, b):
    ks = range(a, b + 1)
    return math.sqrt(sum(f(reg[rg]["%d-%02d" % (y, k)], "moe95_pts") ** 2 for k in ks)) / len(ks)
g1 = math.hypot(mo("South", 2026, 1, 3), mo("South", 2025, 1, 3))
g2 = math.hypot(mo("South", 2026, 4, 8), mo("South", 2025, 4, 8))
print("  South widening moe~%.2f (gap moe Jan-Mar %.2f, Apr-Aug %.2f)" % (math.hypot(g1, g2), g1, g2))
s = reg["South"]
xjun = [f(s["2026-%02d" % k], "intent_pct") - f(s["2025-%02d" % k], "intent_pct") for k in (4, 5, 7, 8)]
print("  South Apr-Aug gap excluding June = %+.2f" % statistics.mean(xjun))

print()
print("C-06 Q8 August 2026 table values")
for rg in ("South", "Northeast", "Midwest"):
    r = reg[rg]["2026-08"]
    print("  %-9s %s ±%s" % (rg, r["intent_pct"], r["moe95_pts"]))
print("  National  %s ±%s" % (nat["2026-08"]["intent_pct"], nat["2026-08"]["moe95_pts"]))

print()
print("C-07 Q8 SMI")
ks = sorted(smi)
print("  range %s..%s" % (ks[0], ks[-1]))
for y in (2024, 2025, 2026):
    print("  %d Jul=%.1f Aug=%.1f chg=%+.1f" % (y, smi["%d-07" % y], smi["%d-08" % y], smi["%d-08" % y] - smi["%d-07" % y]))
ch = [smi[ks[i]] - smi[ks[i - 1]] for i in range(1, len(ks))]
absch = [abs(c) for c in ch]
print("  n changes=%d sd=%.2f mean|chg|=%.2f median|chg|=%.2f share |chg|>=2.7: %d/%d" % (
    len(ch), statistics.stdev(ch), statistics.mean(absch), statistics.median(absch), sum(a >= 2.7 for a in absch), len(ch)))
print("  Jun26=%.1f Jul26=%.1f Aug26=%.1f Aug25=%.1f" % (smi["2026-06"], smi["2026-07"], smi["2026-08"], smi["2025-08"]))

print()
print("C-08 Q3/Q8 forecast rows (authorized fields)")
for r in fc:
    print("  %(period)s point=%(point_yoy_pct)s lo80=%(lo80)s hi80=%(hi80)s %(model_version)s %(run_date)s" % r)

print()
print("C-09 Q8 reconstruction test (challenge only; NOT for the client).")
print("  Tests whether the governed Q8 table + Q9 national figure let a reader back out the West.")
# using publicly known approximate adult population shares (US Census regions) as an external weight
shares = {"Northeast": 0.17, "Midwest": 0.21, "South": 0.38}
west_share = 1 - sum(shares.values())
aug = {rg: f(reg[rg]["2026-08"], "intent_pct") for rg in shares}
nat_aug = f(nat["2026-08"], "intent_pct")
w = (nat_aug - sum(shares[rg] * aug[rg] for rg in shares)) / west_share
print("  With approximate public Census adult shares (NE .17, MW .21, S .38): implied West level is computable (value withheld here: %s)" % ("yes" if not math.isnan(w) else "no"))
print("  Tolerance: an error of ±0.1 in the national figure moves the implied West by ±%.2f pts" % (0.1 / west_share))
