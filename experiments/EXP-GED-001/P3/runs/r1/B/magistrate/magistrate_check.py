# Magistrate's own computations (r1, CL-B). Independent code; stdlib only.
# Inputs: nat.json, reg.json, smi.json = responses retrieved by the Magistrate through the interface
# (see mcp_log.jsonl). Does not import or run analysis.py or reconstruct.py.
# Shared assumption with the parties (disclosed): approximate MoE of a difference or mean treats
# monthly samples as independent: moe(a-b) = sqrt(ma^2+mb^2); moe(mean of k) = sqrt(sum m^2)/k.
import json, math, statistics
from decimal import Decimal as D

nat = {r["month"]: r for r in json.load(open("nat.json"))["data"]}
reg = {}
for r in json.load(open("reg.json"))["data"]:
    reg.setdefault(r["region"], {})[r["month"]] = r
smi = [(r["month"], D(r["smi"])) for r in json.load(open("smi.json"))["data"]]

def f(r, k): return float(r[k])
def months(a, b):
    out = []; y, m = map(int, a.split("-")); y2, m2 = map(int, b.split("-"))
    while (y, m) <= (y2, m2):
        out.append(f"{y:04d}-{m:02d}"); m += 1
        if m == 13: y, m = y + 1, 1
    return out
def mean_moe(series, ms):
    v = [f(series[m], "intent_pct") for m in ms]; e = [f(series[m], "moe95_pts") for m in ms]
    return sum(v) / len(v), math.sqrt(sum(x * x for x in e)) / len(e)
def pr(tag, *a): print(f"[{tag}]", *a)

print("regions received:", sorted(reg), "| national months:", min(nat), "..", max(nat), len(nat), "| SMI rows:", len(smi))

# M-01 Q1/Q9/Q5
j = nat["2026-07"]; pr("M-01", "Jul-2026 national", j)
v, e = f(j, "intent_pct"), f(j, "moe95_pts"); pr("M-01", "95% range", round(v - e, 1), round(v + e, 1))
ks = sorted(nat); dm = [math.hypot(f(nat[a], "moe95_pts"), f(nat[b], "moe95_pts")) for a, b in zip(ks, ks[1:])]
pr("M-01", "month-to-month diff MoE range", round(min(dm), 2), round(max(dm), 2))
pr("M-01", "Jun->Jul 2026", f(nat["2026-06"], "intent_pct"), "->", v, "diff", round(v - f(nat["2026-06"], "intent_pct"), 1),
   "moe", round(math.hypot(f(nat["2026-06"], "moe95_pts"), e), 2))
pr("M-01", "Jun/Jul/Aug 2026 national", [(m, nat[m]["intent_pct"], nat[m]["moe95_pts"]) for m in ("2026-06", "2026-07", "2026-08")])
pr("M-01", "months with national 40.0-42.0:", [(m, nat[m]["intent_pct"]) for m in ks if 40.0 <= f(nat[m], "intent_pct") <= 42.0])

# M-02 Q2
P0, P1 = months("2024-09", "2025-08"), months("2025-09", "2026-08")
ch = {}
for R in ("South", "Northeast"):
    a0, e0 = mean_moe(reg[R], P0); a1, e1 = mean_moe(reg[R], P1)
    ch[R] = (a1 - a0, math.hypot(e0, e1))
    pr("M-02", R, "12m avg", round(a0, 2), "->", round(a1, 2), "change", round(a1 - a0, 2), "+/-", round(math.hypot(e0, e1), 2))
dd = ch["South"][0] - ch["Northeast"][0]; de = math.hypot(ch["South"][1], ch["Northeast"][1])
pr("M-02", "South minus Northeast change", round(dd, 2), "+/-", round(de, 2))
for R in ("South", "Northeast"):
    pr("M-02", R, "Aug25->Aug26", reg[R]["2025-08"]["intent_pct"], "->", reg[R]["2026-08"]["intent_pct"])
allm = [f(reg[R][m], "moe95_pts") for R in reg for m in reg[R]]
pr("M-02", "regional monthly MoE range (licensed regions, all months)", min(allm), max(allm))
sm26 = [f(reg["South"][m], "moe95_pts") for m in months("2026-01", "2026-08")]
pr("M-02", "South 2026 monthly MoE range", min(sm26), max(sm26))

# M-03 Q7 YoY gaps before / during-after openings
def yoy(R, a, b, ya, yb):
    ms1 = months(f"{yb}-{a}", f"{yb}-{b}"); ms0 = months(f"{ya}-{a}", f"{ya}-{b}")
    m1, e1 = mean_moe(reg[R], ms1); m0, e0 = mean_moe(reg[R], ms0); return m1 - m0, math.hypot(e0, e1)
for R in ("South", "Northeast", "Midwest"):
    g1, s1 = yoy(R, "01", "03", 2025, 2026); g2, s2 = yoy(R, "04", "08", 2025, 2026)
    pr("M-03", R, "YoY Jan-Mar", round(g1, 2), "+/-", round(s1, 2), "| YoY Apr-Aug", round(g2, 2), "+/-", round(s2, 2),
       "| widening", round(g2 - g1, 2), "+/-", round(math.hypot(s1, s2), 2))
for R in ("South",):
    g1, _ = yoy(R, "01", "03", 2024, 2025); g2, _ = yoy(R, "04", "08", 2024, 2025)
    pr("M-03", R, "prior year (2025 vs 2024) YoY Jan-Mar", round(g1, 2), "Apr-Aug", round(g2, 2))
s25, s26 = reg["South"]["2025-03"], reg["South"]["2026-03"]
pr("M-03", "South Mar25/Mar26", s25["intent_pct"], s26["intent_pct"], "diff", round(f(s26, "intent_pct") - f(s25, "intent_pct"), 1),
   "moe", round(math.hypot(f(s25, "moe95_pts"), f(s26, "moe95_pts")), 2))

# M-04 Q8 regional August 2026 (licensed values only; no combination with national performed)
for R in ("South", "Northeast", "Midwest"):
    pr("M-04", R, "Aug-2026", reg[R]["2026-08"]["intent_pct"], "+/-", reg[R]["2026-08"]["moe95_pts"])

# M-05 Q8 SMI
sd = dict(smi)
for y in (2024, 2025, 2026):
    a, b = sd[f"{y}-07"], sd[f"{y}-08"]; pr("M-05", y, "SMI Jul->Aug", a, "->", b, "change", b - a)
pr("M-05", "SMI Jun->Jul 2026", sd["2026-06"], "->", sd["2026-07"])
mv = [(smi[i][0], smi[i][1] - smi[i - 1][1]) for i in range(1, len(smi))]
aug = abs(sd["2026-08"] - sd["2026-07"])
before = [m for m in mv if m[0] != "2026-08"]
pr("M-05", "monthly moves total", len(mv), "| |move|>=", aug, "incl Aug-26:", sum(abs(x) >= aug for _, x in mv),
   "| among the", len(before), "before it:", sum(abs(x) >= aug for _, x in before))
pr("M-05", "median |move| all", statistics.median(abs(x) for _, x in mv), "| median before", statistics.median(abs(x) for _, x in before))
pr("M-05", "national intent Jul->Aug by year", [(y, round(f(nat[f'{y}-08'], 'intent_pct') - f(nat[f'{y}-07'], 'intent_pct'), 1)) for y in (2024, 2025, 2026)])
pr("M-05", "SMI range", smi[0][0], "..", smi[-1][0])

# M-06 Q3/Q8 forecast re-run note (non-disclosable; record only)
hw = (4.6 - (-0.4)) / 2
pr("M-06", "Q4 80% half-width", hw, "| stated possible shift 0.3 =", round(0.3 / hw, 3), "of half-width; shifted point range 1.8..2.4 inside -0.4..4.6")
