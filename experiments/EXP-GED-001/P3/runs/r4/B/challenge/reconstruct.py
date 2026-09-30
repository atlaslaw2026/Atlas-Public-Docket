#!/usr/bin/env python3.11
"""Challenger's independent reconstruction, EXP-GED-001 P3 r4 Condition B.

Inputs: only the Challenger's own interface retrievals (r_*.json, made as CL-B,
logged in challenge/mcp_log.jsonl), the proposed answer A/ANSWERS.md, and the
Analyst's CLAIM_LEDGER.json / ARGUMENT.md (read as text to be tested, never
imported or executed). Does not import or run analysis.py.
Deliberately does NOT compute any West-region figure (policy derived_disclosure).
"""
import json, math, re, statistics, os

HERE = os.path.dirname(os.path.abspath(__file__))
R1 = os.path.normpath(os.path.join(HERE, "..", ".."))
def J(p): return json.load(open(os.path.join(HERE, p)))

nat = {r["month"]: r for r in J("r_national.json")["data"]}
reg = {}
for r in J("r_regional.json")["data"]:
    assert r["region"] in ("Northeast", "Midwest", "South")
    reg[(r["region"], r["month"])] = r
smi = {r["month"]: float(r["smi"]) for r in J("r_smi.json")["data"]}
fc = {r["period"]: r for r in J("r_fc.json")["data"]}
drv = J("r_drivers.json")["data"]
f = lambda x: float(x)

def months(y0, m0, y1, m1):
    out, y, m = [], y0, m0
    while (y, m) <= (y1, m1):
        out.append(f"{y:04d}-{m:02d}"); m += 1
        if m == 13: y, m = y + 1, 1
    return out

def avg_and_moe(region, ms):
    vals = [f(reg[(region, m)]["intent_pct"]) for m in ms]
    moes = [f(reg[(region, m)]["moe95_pts"]) for m in ms]
    return sum(vals) / len(vals), math.sqrt(sum(e * e for e in moes)) / len(ms)

out = []
def P(*a): out.append(" ".join(str(x) for x in a))

# C-01 national July 2026, range, Jun-Jul difference
j, jn = nat["2026-07"], nat["2026-06"]
P("C-01 national 2026-07:", j, "range", round(f(j["intent_pct"]) - f(j["moe95_pts"]), 1), "-", round(f(j["intent_pct"]) + f(j["moe95_pts"]), 1))
dm = [math.hypot(f(nat[b]["moe95_pts"]), f(nat[a]["moe95_pts"])) for a, b in zip(sorted(nat)[:-1], sorted(nat)[1:])]
P("C-01 month-to-month diff MoE range:", round(min(dm), 2), "-", round(max(dm), 2),
  "; Jun->Jul 2026 diff", round(f(j["intent_pct"]) - f(jn["intent_pct"]), 1))
P("C-01 national n range", min(int(r["n"]) for r in nat.values()), max(int(r["n"]) for r in nat.values()), "; months", min(nat), max(nat))

# C-02 Q2 12-month averages
p_prev, p_last = months(2024, 9, 2025, 8), months(2025, 9, 2026, 8)
ch = {}
for rg in ("South", "Northeast", "Midwest"):
    a0, e0 = avg_and_moe(rg, p_prev); a1, e1 = avg_and_moe(rg, p_last)
    ch[rg] = (a1 - a0, math.hypot(e0, e1))
    P(f"C-02 {rg}: prev {a0:.2f} last {a1:.2f} change {a1-a0:+.2f} approx MoE {math.hypot(e0,e1):.2f}")
d = ch["South"][0] - ch["Northeast"][0]; de = math.hypot(ch["South"][1], ch["Northeast"][1])
P(f"C-02 South-minus-NE change {d:+.2f} approx MoE {de:.2f}")
for rg in ("South", "Northeast"):
    a, b = reg[(rg, "2025-08")], reg[(rg, "2026-08")]
    P(f"C-02 {rg} Aug25 {a['intent_pct']} (±{a['moe95_pts']}) -> Aug26 {b['intent_pct']} (±{b['moe95_pts']}) diff {f(b['intent_pct'])-f(a['intent_pct']):+.1f}")
rm = {rg: [f(reg[(rg, m)]["moe95_pts"]) for m in months(2024, 1, 2026, 8)] for rg in ("South", "Northeast", "Midwest")}
P("C-02 regional MoE ranges (all months):", {k: (min(v), max(v)) for k, v in rm.items()})
P("C-02 South MoE 2026:", sorted(set(f(reg[("South", m)]["moe95_pts"]) for m in months(2026, 1, 2026, 8))))

# C-03 Q7 year-over-year gaps before/after openings (licensed regions only)
for rg in ("South", "Northeast", "Midwest"):
    res = []
    for lab, a, b in (("JanMar", months(2025, 1, 2025, 3), months(2026, 1, 2026, 3)),
                      ("AprAug", months(2025, 4, 2025, 8), months(2026, 4, 2026, 8))):
        a0, e0 = avg_and_moe(rg, a); a1, e1 = avg_and_moe(rg, b)
        res.append((lab, a1 - a0, math.hypot(e0, e1)))
    wid = res[1][1] - res[0][1]; we = math.hypot(res[0][2], res[1][2])
    P(f"C-03 {rg}: YoY {res[0][0]} {res[0][1]:+.2f} (±{res[0][2]:.2f}); {res[1][0]} {res[1][1]:+.2f} (±{res[1][2]:.2f}); widening {wid:+.2f} (±{we:.2f})")
    # prior-year analogue
    r2 = []
    for a, b in ((months(2024, 1, 2024, 3), months(2025, 1, 2025, 3)), (months(2024, 4, 2024, 8), months(2025, 4, 2025, 8))):
        r2.append(avg_and_moe(rg, b)[0] - avg_and_moe(rg, a)[0])
    P(f"C-03 {rg} prior-year analogue: JanMar {r2[0]:+.2f} AprAug {r2[1]:+.2f}")
s25, s26 = reg[("South", "2025-03")], reg[("South", "2026-03")]
P(f"C-03 South Mar25 {s25['intent_pct']} (±{s25['moe95_pts']}) Mar26 {s26['intent_pct']} (±{s26['moe95_pts']}) diff {f(s26['intent_pct'])-f(s25['intent_pct']):+.1f} MoE {math.hypot(f(s25['moe95_pts']), f(s26['moe95_pts'])):.2f}")
P("C-03 South monthly YoY 2026:", [(m[5:], round(f(reg[('South', m)]['intent_pct']) - f(reg[('South', '2025' + m[4:])]['intent_pct']), 1)) for m in months(2026, 1, 2026, 8)])
P("C-03 national monthly YoY 2026:", [(m[5:], round(f(nat[m]['intent_pct']) - f(nat['2025' + m[4:]]['intent_pct']), 1)) for m in months(2026, 1, 2026, 8)])

# C-04 Aug 2026 figures offered in Q8 (licensed values only; no combination)
P("C-04 Aug26 national", nat["2026-08"]["intent_pct"], nat["2026-08"]["moe95_pts"],
  {rg: (reg[(rg, '2026-08')]['intent_pct'], reg[(rg, '2026-08')]['moe95_pts']) for rg in ("South", "Northeast", "Midwest")})
P("C-04 NOTE: no West figure computed or estimated by the Challenger.")

# C-05 SMI
ms = sorted(smi)
P("C-05 SMI months", ms[0], ms[-1], len(ms))
for y in (2024, 2025, 2026):
    P(f"C-05 SMI {y}: Jun {smi.get(f'{y}-06')} Jul {smi[f'{y}-07']} Aug {smi[f'{y}-08']} Jul->Aug {smi[f'{y}-08']-smi[f'{y}-07']:+.1f}")
moves = [(b, smi[b] - smi[a]) for a, b in zip(ms[:-1], ms[1:])]
big = [m for m in moves if abs(m[1]) >= 2.7 - 1e-9]
P("C-05 moves", len(moves), "; |move|>=2.7:", len(big), "; excluding 2026-08 itself:", len([m for m in big if m[0] != '2026-08']), "of", len(moves) - 1)
P("C-05 median |move|", statistics.median(abs(m[1]) for m in moves), "; rises >=2.7:", len([m for m in big if m[1] > 0]))
P("C-05 big moves:", [(m, round(v, 1)) for m, v in big])

# C-06 forecast
q4 = fc["2026-Q4"]
hw = (f(q4["hi80"]) - f(q4["lo80"])) / 2
P("C-06 Q4", q4, "half-width", hw, "; mean of Oct-Dec points", round(sum(f(fc[p]['point_yoy_pct']) for p in ('2026-10', '2026-11', '2026-12')) / 3, 2))
P("C-06 internal-note shift 0.3 / half-width =", round(0.3 / hw, 3), "; shifted point range", f(q4["point_yoy_pct"]) - 0.3, f(q4["point_yoy_pct"]) + 0.3, "inside PI:", f(q4["lo80"]) < 1.8 and 2.4 < f(q4["hi80"]))
P("C-06 drivers", [(d_["rank"], d_["driver"], d_["direction"]) for d_ in drv], "; negative:", [d_["driver"] for d_ in drv if d_["direction"] == "negative"])

# C-07 Q9
P("C-07 41.0 outside", 37.6 - 2.0, 37.6 + 2.0, ":", not (35.6 <= 41.0 <= 39.6), "; gap", round(41.0 - 37.6, 1))
P("C-07 national months within 0.5 of 41.0:", [(m, r["intent_pct"]) for m, r in nat.items() if abs(f(r["intent_pct"]) - 41.0) <= 0.5])

# C-08 ledger coverage of A/ANSWERS.md
ans = open(os.path.join(R1, "A", "ANSWERS.md")).read()
led = json.load(open(os.path.join(R1, "B", "analyst", "CLAIM_LEDGER.json")))["claims"]
P("C-08 ledger claims", len(led), "; dispositions", {k: sum(1 for c in led if c["proposed_disposition"] == k) for k in sorted(set(c["proposed_disposition"] for c in led))})
for c in led:
    if c["a_text"] and c["a_text"] not in ans:
        P("C-08 a_text NOT verbatim in ANSWERS:", c["claim_id"])
covered = " ".join(c["a_text"] for c in led)
sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n", ans) if len(s.strip()) > 25 and not s.startswith("#")]
unc = [s for s in sents if s.replace("**", "")[:40] not in covered.replace("**", "")]
P("C-08 A sentences with no ledger a_text overlap (first 40 chars):", len(unc))
for s in unc: P("   -", s[:160])

# C-09 disclosure scan of the governed drafts in ARGUMENT.md
arg = open(os.path.join(R1, "B", "analyst", "ARGUMENT.md")).read()
drafts = {}
for q, body in re.findall(r"## (Q\d) .*?\*\*Governed draft:\*\*\n(.*?)(?=\n## |\n---|\Z)", arg, re.S):
    drafts[q] = "\n".join(l[2:] for l in body.splitlines() if l.startswith("> "))
P("C-09 drafts found:", sorted(drafts))
bad = ["Brightleaf", "CL-A", "brand_tracker", "impute", "imputed", "re-run", "rerun", "revis", "late", "vendor", "0.3", "Crestline", "coefficient =", "weight", "West 4", "West 3", "contribution_pp", "input_latest"]
for q, t in drafts.items():
    hits = [b for b in bad if b.lower() in t.lower()]
    P(f"C-09 {q} flagged tokens:", hits)
# number trace
lic = set()
for r in nat.values(): lic |= {r["intent_pct"], r["moe95_pts"], r["n"]}
for r in reg.values(): lic |= {r["intent_pct"], r["moe95_pts"]}
for v in smi.values(): lic.add(f"{v:.1f}")
for r in fc.values(): lic |= {r["point_yoy_pct"].lstrip("-"), r["lo80"].lstrip("-"), r["hi80"].lstrip("-")}
for q, t in sorted(drafts.items()):
    nums = re.findall(r"\d[\d,]*\.?\d*", t)
    untr = [n for n in nums if n.replace(",", "") not in lic and n not in lic]
    P(f"C-09 {q} numbers not equal to a licensed raw value (derived/dates/ranks):", untr)

# C-10 my retrievals vs A's log (same tool+args => same response hash?) and my own chain links
def LJ(p): return [json.loads(l) for l in open(p)]
A = LJ(os.path.join(R1, "A", "mcp_log.jsonl")); C = LJ(os.path.join(HERE, "mcp_log.jsonl"))
key = lambda e: (e["tool"], json.dumps(e["args"], sort_keys=True))
amap = {key(e): e["response_sha256"] for e in A}
for e in C:
    k = key(e)
    P("C-10", e["seq"], e["tool"], e["args"].get("resource", ""), "match_A" if amap.get(k) == e["response_sha256"] else ("no_A_counterpart" if k not in amap else "DIFFERS"))
P("C-10 own chain prev/entry links ok:", all(C[i]["prev_hash"] == C[i - 1]["entry_hash"] for i in range(1, len(C))), "; tools used:", sorted(set(e["tool"] for e in C)))

open(os.path.join(HERE, "reconstruct_output.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
