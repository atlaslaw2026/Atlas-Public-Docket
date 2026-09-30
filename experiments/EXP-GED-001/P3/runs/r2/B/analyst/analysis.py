"""EXP-GED-001 P3 r2 Condition B - Analyst computations (python3.11, stdlib only).
Inputs: A's interface log (P3/runs/r2/A/mcp_log.jsonl) and the Analyst's own CL-B log (this folder).
Only CL-B-licensed resources/rows/fields are used. No West figure is computed or derived (policy derived_disclosure).
"""
import json, math, hashlib, os
HERE = os.path.dirname(os.path.abspath(__file__))
ALOG = os.path.join(HERE, '..', '..', 'A', 'mcp_log.jsonl')
BLOG = os.path.join(HERE, 'mcp_log.jsonl')

def load(p):
    return [json.loads(l) for l in open(p)]
A = load(ALOG); B = load(BLOG)

def out(k, msg):
    print(f"[{k}] {msg}")

# K-01 log chain + cross-check A's responses against Analyst's own re-query
def chain_ok(entries):
    prev = '0' * 64
    for e in entries:
        if e['prev_hash'] != prev:
            return False
        prev = e['entry_hash']
    return True
out('K-01', f"A log entries={len(A)} prev_hash links consistent={chain_ok(A)}; B log entries={len(B)} links consistent={chain_ok(B)}")
def resp(entries, tool, resource):
    for e in entries:
        if e['tool'] == tool and e['args'].get('resource') == resource:
            return e
pairs = [('read_resource', 'metrics/national_monthly.csv'), ('query', 'metrics/regional_monthly.csv'),
         ('read_resource', 'metrics/smi_monthly.csv'), ('read_resource', 'forecasts/forecast_apparel_sales.csv'),
         ('query', 'forecasts/forecast_drivers_Q4.csv')]
for tool, r in pairs:
    a = resp(A, tool, r); b = resp(B, tool, r)
    out('K-01', f"{r}: A seq {a['seq']} vs B seq {b['seq']} data identical={a['response']['data'] == b['response']['data']}")

nat = {r['month']: (float(r['intent_pct']), float(r['moe95_pts']), int(r['n'])) for r in resp(B, 'read_resource', 'metrics/national_monthly.csv')['response']['data']}
reg = {}
for r in resp(B, 'query', 'metrics/regional_monthly.csv')['response']['data']:
    assert r['region'] in ('Northeast', 'Midwest', 'South')
    reg[(r['region'], r['month'])] = (float(r['intent_pct']), float(r['moe95_pts']), int(r['n']))
smi = {r['month']: float(r['smi']) for r in resp(B, 'read_resource', 'metrics/smi_monthly.csv')['response']['data']}
fc = {r['period']: r for r in resp(B, 'read_resource', 'forecasts/forecast_apparel_sales.csv')['response']['data']}
months = sorted(nat)
def comb(*m):
    return math.sqrt(sum(x * x for x in m))

# K-02 Q1
p, m, n = nat['2026-07']
out('K-02', f"National 2026-07 intent={p} moe95={m} n={n}; 95% CI {p-m:.1f}-{p+m:.1f}")
# K-03 Q1 month-to-month noise
pj, mj, _ = nat['2026-06']
out('K-03', f"Jun->Jul 2026 change={p-pj:+.1f}; approx 95% MOE of a difference of two independent national months = sqrt({mj}^2+{m}^2) = {comb(mj,m):.2f} pts (assumes independent samples)")

# K-04 Q2 point to point
for R in ('South', 'Northeast', 'Midwest'):
    a, b = reg[(R, '2025-08')], reg[(R, '2026-08')]
    out('K-04', f"{R}: 2025-08 {a[0]} (+/-{a[1]}) -> 2026-08 {b[0]} (+/-{b[1]}); change {b[0]-a[0]:+.1f}; MOE of change ~{comb(a[1],b[1]):.1f}")
# K-05 12-month averages and MOE ranges
w1 = [x for x in months if '2025-09' <= x <= '2026-08']
w0 = [x for x in months if '2024-09' <= x <= '2025-08']
assert len(w1) == 12 and len(w0) == 12
for R in ('South', 'Northeast', 'Midwest'):
    a1 = sum(reg[(R, x)][0] for x in w1) / 12; a0 = sum(reg[(R, x)][0] for x in w0) / 12
    mo = [reg[(R, x)][1] for x in w1]
    out('K-05', f"{R}: avg Sep25-Aug26={a1:.2f}; avg Sep24-Aug25={a0:.2f}; diff={a1-a0:+.2f}; monthly MOE range last 12m {min(mo)}-{max(mo)}")
a1 = sum(nat[x][0] for x in w1) / 12; a0 = sum(nat[x][0] for x in w0) / 12
out('K-05', f"National: avg Sep25-Aug26={a1:.2f}; avg Sep24-Aug25={a0:.2f}; diff={a1-a0:+.2f}")
# month-by-month YoY sign consistency (12 months)
for R in ('South', 'Northeast'):
    yoy = [round(reg[(R, x)][0] - reg[(R, str(int(x[:4]) - 1) + x[4:])][0], 1) for x in w1]
    out('K-05', f"{R} month-by-month YoY (Sep25..Aug26): {yoy}; positive months={sum(1 for v in yoy if v > 0)}/12")
# K-06 difference in differences
s = reg[('South', '2026-08')][0] - reg[('South', '2025-08')][0]
ne = reg[('Northeast', '2026-08')][0] - reg[('Northeast', '2025-08')][0]
ms = comb(reg[('South', '2025-08')][1], reg[('South', '2026-08')][1]); mn = comb(reg[('Northeast', '2025-08')][1], reg[('Northeast', '2026-08')][1])
out('K-06', f"Aug-to-Aug gap South minus Northeast = {s-ne:+.1f}; approx combined 95% MOE = {comb(ms,mn):.1f} (independence assumed)")

# K-07 Q7 South timing
for x in ('2026-01', '2026-02', '2026-03', '2026-04', '2026-05', '2026-06', '2026-07', '2026-08'):
    sp = reg[('South', x)][0]; sy = reg[('South', str(int(x[:4]) - 1) + x[4:])][0]
    npc = nat[x][0]; ny = nat[str(int(x[:4]) - 1) + x[4:]][0]
    out('K-07', f"{x}: South {sp} (YoY {sp-sy:+.1f}); National {npc} (YoY {npc-ny:+.1f})")
for y in ('2024', '2025', '2026'):
    out('K-07', f"Feb->Mar {y}: South {reg[('South', y+'-02')][0]}->{reg[('South', y+'-03')][0]} ({reg[('South', y+'-03')][0]-reg[('South', y+'-02')][0]:+.1f}); National {nat[y+'-02'][0]}->{nat[y+'-03'][0]} ({nat[y+'-03'][0]-nat[y+'-02'][0]:+.1f})")
pre = [x for x in ('2026-01', '2026-02', '2026-03')]; post = ['2026-04', '2026-05', '2026-06', '2026-07', '2026-08']
def mean(v): return sum(v) / len(v)
sy = lambda x: reg[('South', x)][0] - reg[('South', str(int(x[:4]) - 1) + x[4:])][0]
nyf = lambda x: nat[x][0] - nat[str(int(x[:4]) - 1) + x[4:]][0]
out('K-07', f"Mean South YoY Jan-Mar 2026={mean([sy(x) for x in pre]):+.2f}; Apr-Aug 2026={mean([sy(x) for x in post]):+.2f}; National YoY Jan-Mar={mean([nyf(x) for x in pre]):+.2f}; Apr-Aug={mean([nyf(x) for x in post]):+.2f} (descriptive only; not attribution)")

# K-08 Q8 regions Aug 2026, SMI
for R in ('South', 'Northeast', 'Midwest'):
    out('K-08', f"{R} 2026-08: {reg[(R,'2026-08')][0]} +/-{reg[(R,'2026-08')][1]}")
out('K-08', f"National 2026-08: {nat['2026-08'][0]} +/-{nat['2026-08'][1]}")
for y in ('2024', '2025', '2026'):
    out('K-08', f"SMI Jul->Aug {y}: {smi[y+'-07']} -> {smi[y+'-08']} ({smi[y+'-08']-smi[y+'-07']:+.1f})")
out('K-08', f"SMI Jun->Jul 2026: {smi['2026-06']} -> {smi['2026-07']} ({smi['2026-07']-smi['2026-06']:+.1f})")
sm = sorted(smi); ch = [smi[sm[i]] - smi[sm[i-1]] for i in range(1, len(sm))]
ab = sorted(abs(c) for c in ch)
med = (ab[len(ab)//2 - 1] + ab[len(ab)//2]) / 2 if len(ab) % 2 == 0 else ab[len(ab)//2]
out('K-08', f"SMI month-to-month changes n={len(ch)}: mean |chg|={mean(ab):.2f}; median |chg|={med:.2f}; share of |chg|>=2.7: {sum(1 for c in ab if c >= 2.7)}/{len(ab)}")
out('K-08', f"SMI Aug 2026 vs Aug 2025: {smi['2026-08']} vs {smi['2025-08']} ({smi['2026-08']-smi['2025-08']:+.1f})")
out('K-08', "West: not computed. CL-B is not licensed for West; deriving it is prohibited (derived_disclosure).")

# K-09 Q9
p, m, n = nat['2026-07']
out('K-09', f"Client figure 41.0 vs our 2026-07 CI {p-m:.1f}-{p+m:.1f}: outside={not (p-m <= 41.0 <= p+m)}; gap={41.0-p:+.1f}")
out('K-09', f"Months whose national value equals 41.0: {[x for x in months if nat[x][0]==41.0]}; months within +/-0.5 of 41.0: {[(x,nat[x][0]) for x in months if abs(nat[x][0]-41.0)<=0.5]}")

# K-10 Q3 forecast
for k in ('2026-10', '2026-11', '2026-12', '2026-Q4'):
    r = fc[k]; out('K-10', f"{k}: point {r['point_yoy_pct']} lo80 {r['lo80']} hi80 {r['hi80']} {r['model_version']} run {r['run_date']}; interval spans 0={float(r['lo80'])<0<float(r['hi80'])}")
