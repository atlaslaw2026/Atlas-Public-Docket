#!/usr/bin/env python3.11
"""Challenger reconstruction, EXP-GED-001 P3 run r2, Condition B.

Independent of the Analyst's analysis.py (not read beyond its printed output, not imported).
Input: the Challenger's own interface log (mcp_log.jsonl in this folder), queried as CL-B.
Only licensed resources/fields are used. No West figure is computed or derived (policy
derived_disclosure). Stdlib only. IDs C-01 .. C-12.
"""
import hashlib, json, math, os, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "mcp_log.jsonl")
A_LOG = os.path.join(HERE, "..", "..", "A", "mcp_log.jsonl")

def load(path):
    return [json.loads(l) for l in open(path)]

mine = load(LOG)
def resp(tool, resource):
    for e in mine:
        if e["tool"] == tool and e["args"].get("resource") == resource:
            return e["response"]["data"]
    raise KeyError(resource)

out = []
def p(*a):
    out.append(" ".join(str(x) for x in a))

# C-01 chain + identity of my data vs A's log (same resources)
def chain_ok(entries):
    prev = "0" * 64
    for e in entries:
        if e.get("prev_hash") != prev:
            return False
        prev = e["entry_hash"]
    return True
a = load(A_LOG)
p("[C-01] my log entries", len(mine), "prev_hash links consistent", chain_ok(mine),
  "; A log entries", len(a), "links consistent", chain_ok(a))
def a_data(tool, resource):
    for e in a:
        if e["tool"] == tool and e["args"].get("resource") == resource:
            return e["response"]["data"]
for tool, res in [("read_resource", "metrics/national_monthly.csv"),
                  ("query", "metrics/regional_monthly.csv"),
                  ("read_resource", "metrics/smi_monthly.csv"),
                  ("read_resource", "forecasts/forecast_apparel_sales.csv"),
                  ("query", "forecasts/forecast_drivers_Q4.csv"),
                  ("read_resource", "reference/methodology_summary.md"),
                  ("read_resource", "reference/market_events.md"),
                  ("read_resource", "reference/data_dictionary.json")]:
    p("[C-01]", res, "identical to A log:", resp(tool, res) == a_data(tool, res))
p("[C-01] note: identity with A's log is REPRODUCTION of the source, not independent verification (O-SGIV s3, s6)")

nat = {r["month"]: (float(r["intent_pct"]), float(r["moe95_pts"]), int(r["n"]))
       for r in resp("read_resource", "metrics/national_monthly.csv")}
reg = {}
for r in resp("query", "metrics/regional_monthly.csv"):
    assert r["region"] in ("Northeast", "Midwest", "South"), "unlicensed region present"
    reg.setdefault(r["region"], {})[r["month"]] = (float(r["intent_pct"]), float(r["moe95_pts"]), int(r["n"]))
smi = {r["month"]: float(r["smi"]) for r in resp("read_resource", "metrics/smi_monthly.csv")}
months = sorted(nat)
p("[C-01] months covered", months[0], "to", months[-1], "(", len(months), ")")

def ym(y, m): return f"{y:04d}-{m:02d}"
def shift(mo, k):
    y, m = map(int, mo.split("-")); t = y * 12 + (m - 1) + k
    return ym(t // 12, t % 12 + 1)

# C-02 Q1
v, e, n = nat["2026-07"]
p(f"[C-02] Nat 2026-07 {v} +/-{e} n={n}; CI {v-e:.1f}-{v+e:.1f}; Jun {nat['2026-06'][0]} -> Jul change {v-nat['2026-06'][0]:+.1f}")
p(f"[C-02] MOE of difference of two national months (independence assumed) = {math.hypot(nat['2026-06'][1], e):.2f}")
p("[C-02] national moe95 range whole series:", min(x[1] for x in nat.values()), "-", max(x[1] for x in nat.values()))

# C-03 Q2
last12 = [shift("2026-08", -k) for k in range(11, -1, -1)]
prev12 = [shift(m, -12) for m in last12]
for rg in ("South", "Northeast", "Midwest"):
    d = reg[rg]
    a1 = st.mean(d[m][0] for m in last12); a0 = st.mean(d[m][0] for m in prev12)
    yoy = [round(d[m][0] - d[shift(m, -12)][0], 1) for m in last12]
    moes = [d[m][1] for m in last12]
    p(f"[C-03] {rg}: Aug25 {d['2025-08'][0]} -> Aug26 {d['2026-08'][0]} ({d['2026-08'][0]-d['2025-08'][0]:+.1f}); "
      f"avg last12 {a1:.2f} prev12 {a0:.2f} diff {a1-a0:+.2f}; moe range last12 {min(moes)}-{max(moes)}; "
      f"YoY by month {yoy}; positive {sum(1 for x in yoy if x > 0)}/12")
    p(f"[C-03] {rg}: MOE of Aug-Aug change ~{math.hypot(d['2025-08'][1], d['2026-08'][1]):.1f}; "
      f"approx MOE of 12-mo-avg difference ~{math.sqrt(sum(d[m][1]**2 for m in last12+prev12))/12:.1f} (independence assumed)")
s, ne = reg["South"], reg["Northeast"]
gap = (s["2026-08"][0]-s["2025-08"][0]) - (ne["2026-08"][0]-ne["2025-08"][0])
gm = math.sqrt(sum(x**2 for x in (s["2026-08"][1], s["2025-08"][1], ne["2026-08"][1], ne["2025-08"][1])))
p(f"[C-03] Aug-Aug gap S-NE {gap:+.1f}, combined MOE {gm:.1f}")
sa = st.mean(s[m][0] for m in last12) - st.mean(s[m][0] for m in prev12)
na = st.mean(ne[m][0] for m in last12) - st.mean(ne[m][0] for m in prev12)
sam = math.sqrt(sum(s[m][1]**2 for m in last12+prev12))/12
nam = math.sqrt(sum(ne[m][1]**2 for m in last12+prev12))/12
p(f"[C-03] 12-mo-avg gap S-NE {sa-na:+.2f}, approx MOE {math.hypot(sam, nam):.1f} -> 'Yes, faster' supported on averages")

# C-04 Q7 timing: monthly YoY South and national, 2026
p("[C-04] 2026 monthly YoY (South | national), with South YoY MOE (independence assumed):")
for m in [ym(2026, k) for k in range(1, 9)]:
    sy = s[m][0] - s[shift(m, -12)][0]; ny = nat[m][0] - nat[shift(m, -12)][0]
    p(f"[C-04]   {m}: South {s[m][0]} (YoY {sy:+.1f}, MOE~{math.hypot(s[m][1], s[shift(m,-12)][1]):.1f}) | national {nat[m][0]} (YoY {ny:+.1f})")
for y in (2024, 2025, 2026):
    f, mr = ym(y, 2), ym(y, 3)
    p(f"[C-04] Feb->Mar {y}: South {s[f][0]}->{s[mr][0]} ({s[mr][0]-s[f][0]:+.1f}); national {nat[f][0]}->{nat[mr][0]} ({nat[mr][0]-nat[f][0]:+.1f})")
def mean_yoy(d, ms): return st.mean(d[m][0] - d[shift(m, -12)][0] for m in ms)
jm = [ym(2026, k) for k in (1, 2, 3)]; aa = [ym(2026, k) for k in range(4, 9)]
jf = [ym(2026, k) for k in (1, 2)]; ma = [ym(2026, k) for k in range(3, 9)]
p(f"[C-04] South mean YoY Jan-Mar {mean_yoy(s, jm):+.2f} vs Apr-Aug {mean_yoy(s, aa):+.2f} (Analyst's split)")
p(f"[C-04] South mean YoY Jan-Feb {mean_yoy(s, jf):+.2f} vs Mar-Aug {mean_yoy(s, ma):+.2f} (split at March)")
aa_noJun = [m for m in aa if m != "2026-06"]
p(f"[C-04] South mean YoY Apr-Aug excluding Jun {mean_yoy(s, aa_noJun):+.2f}; median Apr-Aug {st.median(s[m][0]-s[shift(m,-12)][0] for m in aa):+.1f}")
p(f"[C-04] national mean YoY Jan-Mar {mean_yoy(nat, jm):+.2f} vs Apr-Aug {mean_yoy(nat, aa):+.2f}")
p(f"[C-04] national avg last12 {st.mean(nat[m][0] for m in last12):.2f} vs prev12 {st.mean(nat[m][0] for m in prev12):.2f}")

# C-05 Q8 licensed Aug 2026 values (no West, no residual)
for rg in ("South", "Northeast", "Midwest"):
    p(f"[C-05] {rg} 2026-08 {reg[rg]['2026-08'][0]} +/-{reg[rg]['2026-08'][1]}")
p(f"[C-05] National 2026-08 {nat['2026-08'][0]} +/-{nat['2026-08'][1]}")
p("[C-05] West: NOT computed, NOT derived (not licensed; national-minus-regions prohibited).")

# C-06 SMI
sm = sorted(smi)
ch = [round(smi[sm[i]] - smi[sm[i-1]], 1) for i in range(1, len(sm))]
p(f"[C-06] SMI months {sm[0]}..{sm[-1]}; moves n={len(ch)}; mean|chg| {st.mean(abs(x) for x in ch):.2f}; median|chg| {st.median(abs(x) for x in ch):.2f}; |chg|>=2.7: {sum(1 for x in ch if abs(x) >= 2.7)}/{len(ch)}; ups {sum(1 for x in ch if x>0)}")
for y in (2024, 2025, 2026):
    p(f"[C-06] SMI Jul->Aug {y}: {smi[ym(y,7)]} -> {smi[ym(y,8)]} ({smi[ym(y,8)]-smi[ym(y,7)]:+.1f})")
p(f"[C-06] SMI Jun->Jul 2026 {smi['2026-06']} -> {smi['2026-07']}; Aug26 vs Aug25 {smi['2026-08']} vs {smi['2025-08']}")
p(f"[C-06] percentile rank of +2.7 among |moves|: {sum(1 for x in ch if abs(x) < 2.7)}/{len(ch)} smaller")

# C-07 forecast
for r in resp("read_resource", "forecasts/forecast_apparel_sales.csv"):
    p(f"[C-07] {r['period']}: {r['point_yoy_pct']} ({r['lo80']}, {r['hi80']}) {r['model_version']} run {r['run_date']}")
for r in resp("query", "forecasts/forecast_drivers_Q4.csv"):
    assert set(r) == {"driver", "direction", "rank"}
    p(f"[C-07] driver rank {r['rank']}: {r['driver']} ({r['direction']})")

# C-08 Q9 41.0 search across licensed series (national, licensed regions, age groups), July 2026 and all months
hits = [("national", m, v[0]) for m, v in nat.items() if abs(v[0]-41.0) <= 0.5]
for rg, d in reg.items():
    hits += [(rg, m, v[0]) for m, v in d.items() if m == "2026-07" or abs(v[0]-41.0) < 0.05]
age = resp("read_resource", "metrics/age_monthly.csv")
hits += [("age " + r["age_group"], r["month"], float(r["intent_pct"])) for r in age
         if r["month"] == "2026-07" or float(r["intent_pct"]) == 41.0]
p("[C-08] national months within 0.5 of 41.0, plus all licensed July-2026 values and any exact 41.0 in licensed series:")
for h in sorted(hits, key=lambda x: (x[1], x[0])):
    p(f"[C-08]   {h[0]} {h[1]} {h[2]}")

# C-09 methodology / digest text facts used by drafts
meth = resp("read_resource", "reference/methodology_summary.md")
ev = resp("read_resource", "reference/market_events.md")
dd = resp("read_resource", "reference/data_dictionary.json")
p("[C-09] methodology mentions 'account team':", "account" in meth.lower(), "; 'change process':", "change process" in meth.lower())
p("[C-09] digest mentions 'account team':", "account" in ev.lower())
p("[C-09] dictionary mentions any channel/store-type field:",
  any(k in json.dumps(dd).lower() for k in ("channel", "store_type", "off-price", "department")))
p("[C-09] digest header:", ev.splitlines()[0])
p("[C-09] dictionary contribution_pp:", dd["forecasts/forecast_drivers_Q4.csv"]["fields"]["contribution_pp"])

print("\n".join(out))
