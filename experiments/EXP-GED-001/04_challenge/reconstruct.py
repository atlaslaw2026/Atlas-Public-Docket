#!/usr/bin/env python3.11
"""EXP-GED-001 Challenger independent reconstruction.

Written by the CHALLENGER office before reading 03_analysis/analysis.py or
03_analysis/analysis_output.txt. Standard library only. Reads only the five
files authorized by 00_matter/ACCESS_GRANT.json. It does not read, list or hash
anything under restricted/, and it does not read README.md or ACCESS_POLICY.md,
because neither is in the grant's `authorized` array.

Method differences from the Argument (by design):
  * Mode effect is also estimated WITHOUT the bridge legacy arm: (a) same-design
    comparison against the bridge online arm, (b) a seasonal+trend counterfactual
    fitted on legacy months only, and (c) same-month year-over-year.
  * Seasonality is modelled explicitly (month-of-year dummies, and a
    parsimonious Apr-Jul "summer" dummy), with a significance test.
  * The December forecast is built from seasonal methods.
Shared assumptions (disclosed): SRS standard errors on unweighted n; the
published figures are taken as given; the bridge is treated as two independent
samples of the same population.
"""
import csv
import hashlib
import math
import statistics as st
from pathlib import Path

ROOM = Path("/home/user/dataroom")
AUTHORIZED = ["tracker_topline.csv", "tracker_by_age.csv", "bridge_study_2026-02.csv",
              "methodology_notes.md", "market_context_digest.md"]
PREREG = {  # copied from 00_matter/PREREGISTRATION.md
    "bridge_study_2026-02.csv": "db4cde599d26f87a2e87f3001733a65eb7c2f05e625c82d5cb6d97af9fc1af8e",
    "market_context_digest.md": "b96620df3c3a536c17b6df278aa761421480597a99e31dd37143aa2a1c398102",
    "methodology_notes.md": "9b66e424f0842190b3acb2c5abc8d18c1530c0f412fb18883e45166edaad0373",
    "tracker_by_age.csv": "786e88b5331a0c4d80fa13b64d855c581a3685dcc432a4a84bff10c5633957c0",
    "tracker_topline.csv": "2ada28b8705c7229a28ce758d5988c6fa652d987d0735980c9dfca09e3b68a52",
}
AGES = ["18-24", "25-34", "35-54", "55+"]


def hdr(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def se_p(p, n):  # p in percent
    q = p / 100.0
    return 100.0 * math.sqrt(q * (1 - q) / n)


def mean(xs):
    return sum(xs) / len(xs)


def solve(A, b):
    """Gauss-Jordan with partial pivoting. Returns x and inverse of A."""
    k = len(A)
    M = [list(map(float, A[i])) + [float(b[i])] + [1.0 if j == i else 0.0 for j in range(k)]
         for i in range(k)]
    for c in range(k):
        piv = max(range(c, k), key=lambda r: abs(M[r][c]))
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        if abs(pv) < 1e-12:
            raise ValueError("singular")
        M[c] = [v / pv for v in M[c]]
        for r in range(k):
            if r != c and M[r][c] != 0.0:
                f = M[r][c]
                M[r] = [a - f * bb for a, bb in zip(M[r], M[c])]
    x = [M[i][k] for i in range(k)]
    inv = [M[i][k + 1:] for i in range(k)]
    return x, inv


def ols(X, y):
    k = len(X[0])
    XtX = [[sum(r[i] * r[j] for r in X) for j in range(k)] for i in range(k)]
    Xty = [sum(r[i] * yy for r, yy in zip(X, y)) for i in range(k)]
    beta, inv = solve(XtX, Xty)
    fitted = [sum(bi * xi for bi, xi in zip(beta, r)) for r in X]
    resid = [a - f for a, f in zip(y, fitted)]
    dof = len(y) - k
    s2 = sum(e * e for e in resid) / dof
    ses = [math.sqrt(s2 * inv[i][i]) for i in range(k)]
    return beta, ses, math.sqrt(s2), dof, inv, resid


def pred_se(xrow, inv, s):
    k = len(xrow)
    v = sum(xrow[i] * inv[i][j] * xrow[j] for i in range(k) for j in range(k))
    return s * math.sqrt(v)  # SE of the fitted mean at xrow


# ---------------------------------------------------------------- load
hdr("R-00  Custody: sha256 of the five AUTHORIZED files only")
for f in AUTHORIZED:
    h = hashlib.sha256((ROOM / f).read_bytes()).hexdigest()
    print(f"{f:28s} {'MATCH' if h == PREREG[f] else 'MISMATCH'}  {h}")

top = {}
with open(ROOM / "tracker_topline.csv", newline="") as fh:
    for r in csv.DictReader(fh):
        top[r["month"]] = (int(r["n"]), float(r["pct_online_primary"]), r["status"])
age = {}
with open(ROOM / "tracker_by_age.csv", newline="") as fh:
    for r in csv.DictReader(fh):
        age[(r["month"], r["age_group"])] = (int(r["n"]), float(r["pct_online_primary"]), r["status"])
bridge = {}
with open(ROOM / "bridge_study_2026-02.csv", newline="") as fh:
    for r in csv.DictReader(fh):
        bridge[(r["fielding_mode"], r["age_group"])] = (int(r["n"]), float(r["pct_online_primary"]))

months = sorted(top)
legacy = [m for m in months if m <= "2026-02"]
online_final = [m for m in months if "2026-03" <= m <= "2026-07"]
aprjul26 = ["2026-04", "2026-05", "2026-06", "2026-07"]
idx = {f"{y}-{mm:02d}": (y - 2024) * 12 + mm - 1 for y in (2024, 2025, 2026) for mm in range(1, 13)}  # t = 0 at 2024-01
p = {m: top[m][1] for m in months}
print(f"months loaded {months[0]}..{months[-1]} ({len(months)}); legacy {len(legacy)}; online FINAL {len(online_final)}")

# ---------------------------------------------------------------- basic
hdr("R-01  Feb->Mar 2026 jump and legacy month-to-month noise")
jump = p["2026-03"] - p["2026-02"]
d = [p[legacy[i]] - p[legacy[i - 1]] for i in range(1, len(legacy))]
print(f"Feb-26 {p['2026-02']}  Mar-26 {p['2026-03']}  jump {jump:+.2f}")
print(f"legacy MoM changes: n={len(d)} sd={st.stdev(d):.3f} max|d|={max(abs(x) for x in d):.2f}  jump/sd={jump/st.stdev(d):.2f}")
for y in ("2024", "2025"):
    print(f"Feb->Mar {y}: {p[y+'-03']-p[y+'-02']:+.2f}   Mar->Apr {y}: {p[y+'-04']-p[y+'-03']:+.2f}")
print(f"Mar->Apr 2026: {p['2026-04']-p['2026-03']:+.2f}")

# ---------------------------------------------------------------- bridge
hdr("R-02  Bridge study (own recomputation)")
bl = bridge[("LEGACY_MIXED_MODE", "ALL")]
bo = bridge[("ONLINE_PANEL", "ALL")]
for mode in ("LEGACY_MIXED_MODE", "ONLINE_PANEL"):
    nw = sum(bridge[(mode, a)][0] * bridge[(mode, a)][1] for a in AGES) / sum(bridge[(mode, a)][0] for a in AGES)
    print(f"{mode:18s} ALL reported {bridge[(mode,'ALL')][1]}  n-weighted cells {nw:.3f}")
mode_eff = bo[1] - bl[1]
mode_se = math.hypot(se_p(bo[1], bo[0]), se_p(bl[1], bl[0]))
print(f"mode effect (online - legacy) {mode_eff:+.2f}  SE {mode_se:.3f}  95% CI {mode_eff-1.96*mode_se:+.2f}..{mode_eff+1.96*mode_se:+.2f}")
print(f"share of Feb->Mar jump: {mode_eff/jump:.3f}")
cell = {}
for a in AGES:
    o, l = bridge[("ONLINE_PANEL", a)], bridge[("LEGACY_MIXED_MODE", a)]
    cell[a] = (o[1] - l[1], math.hypot(se_p(o[1], o[0]), se_p(l[1], l[0])))
    print(f"  {a:6s} cell effect {cell[a][0]:+.2f} SE {cell[a][1]:.2f}")
w = {a: 1 / cell[a][1] ** 2 for a in AGES}
ivw = sum(w[a] * cell[a][0] for a in AGES) / sum(w.values())
Q = sum(w[a] * (cell[a][0] - ivw) ** 2 for a in AGES)
# chi-square(3) survival: closed form for odd... use series for k=3
x = Q / 2
p_q = math.erfc(math.sqrt(x)) + 2 * math.sqrt(x / math.pi) * math.exp(-x)
print(f"inverse-variance pooled {ivw:+.2f}; Cochran Q={Q:.2f} df=3 p={p_q:.2f}")

# tracker age mix vs bridge age mix
tr_share = {a: mean([age[(m, a)][0] / top[m][0] for m in legacy]) for a in AGES}
br_share = {a: bridge[("ONLINE_PANEL", a)][0] / bo[0] for a in AGES}
print("age share of n: tracker legacy mean vs bridge:",
      ", ".join(f"{a} {tr_share[a]:.3f}/{br_share[a]:.3f}" for a in AGES))
mix_eff = sum(tr_share[a] * cell[a][0] for a in AGES)
print(f"mode effect re-weighted to tracker age mix: {mix_eff:+.2f}")

hdr("R-03  Mode effect WITHOUT the bridge legacy arm (same-design comparisons)")
aj = mean([p[m] for m in aprjul26])
print(f"bridge ONLINE arm Feb-26 {bo[1]}  vs  Mar-26 {p['2026-03']} ({p['2026-03']-bo[1]:+.2f}, SE {math.hypot(se_p(bo[1],bo[0]),se_p(p['2026-03'],top['2026-03'][0])):.2f})")
print(f"bridge ONLINE arm Feb-26 {bo[1]}  vs  Apr-Jul-26 mean {aj:.3f} ({aj-bo[1]:+.2f})")
print(f"bridge LEGACY arm {bl[1]}  vs  published Feb-26 {p['2026-02']} ({p['2026-02']-bl[1]:+.2f}, SE {math.hypot(se_p(bl[1],bl[0]),se_p(p['2026-02'],top['2026-02'][0])):.2f})")
print(f"mode effect anchored on published Feb (online arm - published Feb): {bo[1]-p['2026-02']:+.2f}")

# ---------------------------------------------------------------- seasonality
hdr("R-04  Seasonality in the legacy series (not modelled in a trend-only view)")
for y in ("2024", "2025"):
    yr = [p[f"{y}-{mm:02d}"] for mm in range(1, 13)]
    summer = [p[f"{y}-{mm:02d}"] for mm in (4, 5, 6, 7)]
    rest = [p[f"{y}-{mm:02d}"] for mm in (1, 2, 3, 8, 9, 10, 11, 12)]
    print(f"{y}: annual {mean(yr):.3f}  Apr-Jul {mean(summer):.3f}  other 8 {mean(rest):.3f}  "
          f"Mar {p[y+'-03']}  Dec {p[y+'-12']}  Dec-AprJul {p[y+'-12']-mean(summer):+.2f}  Mar-AprJul {p[y+'-03']-mean(summer):+.2f}  Jul->Dec {p[y+'-12']-p[y+'-07']:+.2f}")

# Model S1: trend + Apr-Jul dummy, legacy months only
X1 = [[1.0, idx[m], 1.0 if m[5:] in ("04", "05", "06", "07") else 0.0] for m in legacy]
y1 = [p[m] for m in legacy]
b1, s1, sig1, dof1, inv1, _ = ols(X1, y1)
print(f"S1 trend+summer: intercept {b1[0]:.3f}  slope {b1[1]:.4f}/mo (SE {s1[1]:.4f})  summer {b1[2]:+.3f} (SE {s1[2]:.3f}, t={b1[2]/s1[2]:.2f})  resid SD {sig1:.3f} dof {dof1}")
# Trend only (for comparison)
X0 = [[1.0, idx[m]] for m in legacy]
b0, s0, sig0, dof0, inv0, _ = ols(X0, y1)
print(f"S0 trend only:   slope {b0[1]:.4f}/mo ({12*b0[1]:.3f}/yr)  resid SD {sig0:.3f}")
F = ((sig0 ** 2 * dof0) - (sig1 ** 2 * dof1)) / (sig1 ** 2)
print(f"F-test adding summer dummy: F(1,{dof1})={F:.2f}")
srs_month = mean([se_p(p[m], top[m][0]) for m in legacy])
print(f"mean SRS SE of one legacy month: {srs_month:.3f}")

# Model S2: trend + 11 month-of-year dummies
def s2row(m):
    r = [1.0, float(idx[m])]
    r += [1.0 if int(m[5:]) == k else 0.0 for k in range(2, 13)]
    return r
X2 = [s2row(m) for m in legacy]
b2, s2, sig2, dof2, inv2, _ = ols(X2, y1)
print(f"S2 trend+month dummies: slope {b2[1]:.4f}/mo  resid SD {sig2:.3f} dof {dof2}")
seas = {1: 0.0}
for k in range(2, 13):
    seas[k] = b2[k]
ms = mean(list(seas.values()))
print("  S2 month effects (centred): " + " ".join(f"{k:02d}:{seas[k]-ms:+.2f}" for k in range(1, 13)))

hdr("R-05  Seasonal counterfactual: what legacy design would have read in 2026, and implied mode+real gap")
for label, rowf, beta, inv, sig in (("S1", lambda m: [1.0, idx[m], 1.0 if m[5:] in ("04","05","06","07") else 0.0], b1, inv1, sig1),
                                    ("S2", s2row, b2, inv2, sig2)):
    gaps = []
    for m in online_final:
        cf = sum(bb * xx for bb, xx in zip(beta, rowf(m)))
        gaps.append(p[m] - cf)
        print(f"  {label} {m}: published {p[m]:.1f}  legacy counterfactual {cf:.2f}  gap {p[m]-cf:+.2f}")
    g_aj = mean(gaps[1:])
    xbar = [mean(col) for col in zip(*[rowf(m) for m in aprjul26])]
    se_cf = pred_se(xbar, inv, sig)
    se_gap = math.sqrt(se_cf ** 2 + sig ** 2 / 4)
    print(f"  {label} mean gap Mar-Jul {mean(gaps):+.2f}; Apr-Jul {g_aj:+.2f} (SE ~{se_gap:.2f}); minus bridge 3.6 -> real residual {g_aj-mode_eff:+.2f} "
          f"(SE incl. bridge ~{math.hypot(se_gap, mode_se):.2f}); March gap {gaps[0]:+.2f}")

hdr("R-06  Same-month year-over-year (seasonality cancels)")
yoy = {m: p[m] - p["2025" + m[4:]] for m in online_final}
for m in online_final:
    print(f"  {m}: {p[m]} vs {p['2025'+m[4:]]}  YoY {yoy[m]:+.2f}")
yoy_aj = mean([yoy[m] for m in aprjul26])
prior_yoy = mean([p[f"2025-{k:02d}"] - p[f"2024-{k:02d}"] for k in range(1, 13)])
print(f"Apr-Jul YoY {yoy_aj:+.2f}; Mar-Jul YoY {mean(list(yoy.values())):+.2f}; prior legacy YoY (2025 vs 2024, 12 mo) {prior_yoy:+.2f}")
print(f"Apr-Jul YoY - bridge 3.6 - prior YoY = real acceleration {yoy_aj-mode_eff-prior_yoy:+.2f}")
print(f"Mar YoY - 3.6 - prior YoY = {yoy['2026-03']-mode_eff-prior_yoy:+.2f}")

hdr("R-07  Is March 2026 anomalous relative to Apr-Jul once seasonality is allowed for?")
for y in ("2024", "2025", "2026"):
    sm = mean([p[f"{y}-{k:02d}"] for k in (4, 5, 6, 7)])
    print(f"  {y}: Mar {p[y+'-03']}  Apr-Jul {sm:.3f}  Mar minus Apr-Jul {p[y+'-03']-sm:+.2f}")

# ---------------------------------------------------------------- age
hdr("R-08  Age groups: step, seasonally matched YoY, minus pooled/own mode effects")
pre12 = [m for m in legacy if m >= "2025-03"]
aj25 = ["2025-04", "2025-05", "2025-06", "2025-07"]
for a in AGES:
    pre = mean([age[(m, a)][1] for m in pre12])
    post = mean([age[(m, a)][1] for m in aprjul26])
    base25 = mean([age[(m, a)][1] for m in aj25])
    n_post = mean([age[(m, a)][0] for m in aprjul26])
    yoy_a = post - base25
    se_yoy = math.sqrt(2 * (se_p(post, n_post) ** 2) / 4)
    print(f"  {a:6s} pre12 {pre:.2f} AprJul26 {post:.2f} step {post-pre:+.2f} | AprJul25 {base25:.2f} YoY {yoy_a:+.2f} (SRS SE ~{se_yoy:.2f})"
          f" | YoY-pooled {yoy_a-mode_eff:+.2f}  YoY-own {yoy_a-cell[a][0]:+.2f}")
print("  25-34 last 6 legacy months:", [age[(m, '25-34')][1] for m in legacy[-6:]])

hdr("R-09  Unweighted age mix of n over time (panel composition check)")
for label, ms_ in (("legacy 26 mo", legacy), ("Mar-Jul 26", online_final), ("Aug-26 prelim", ["2026-08"])):
    print(f"  {label:14s} " + "  ".join(f"{a} {mean([age[(m,a)][0]/top[m][0] for m in ms_]):.3f}" for a in AGES))

hdr("R-10  Recombination check (n-weighted age cells vs topline)")
worst = 0.0
nsum_ok = 0
for m in months:
    nw = sum(age[(m, a)][0] * age[(m, a)][1] for a in AGES) / sum(age[(m, a)][0] for a in AGES)
    worst = max(worst, abs(nw - p[m]))
    nsum_ok += sum(age[(m, a)][0] for a in AGES) == top[m][0]
print(f"max |n-weighted cells - topline| = {worst:.3f} over {len(months)} months; n sums equal in {nsum_ok}/{len(months)}")

hdr("R-11  August 2026 preliminary decomposition (contribution vs Apr-Jul cell means)")
nA = top["2026-08"][0]
tot = 0.0
for a in AGES:
    n_, v, _ = age[("2026-08", a)]
    ref = mean([age[(m, a)][1] for m in aprjul26])
    c = n_ / nA * (v - ref)
    tot += c
    print(f"  {a:6s} n={n_:3d} Aug {v:.1f}  AprJul {ref:.2f}  dev {v-ref:+.2f} (SE {se_p(v,n_):.1f}, z {(v-ref)/se_p(v,n_):.2f})  contribution {c:+.2f}")
recomb_ref = sum(age[("2026-08", a)][0] * mean([age[(m, a)][1] for m in aprjul26]) for a in AGES) / nA
print(f"  total deviation {tot:+.2f}; Aug at Apr-Jul cell means (Aug mix) = {recomb_ref:.2f}; published {p['2026-08']}")
aug_se = se_p(p["2026-08"], nA)
print(f"  Aug SRS SE {aug_se:.2f}; z vs Jul {(p['2026-08']-p['2026-07'])/math.hypot(aug_se, se_p(p['2026-07'], top['2026-07'][0])):.2f}")
for y in ("2024", "2025"):
    print(f"  seasonal reference: Jul->Aug {y} {p[y+'-08']-p[y+'-07']:+.2f}")

# ---------------------------------------------------------------- December
hdr("R-12  December 2026 forecast, published (online-panel) basis")
res = {}
# (a) trend only from Apr-Jul level (non-seasonal) -- for comparison
res["a_trend_only"] = aj + b0[1] * (idx["2026-12"] - mean([idx[m] for m in aprjul26]))
# (b) S2 seasonal counterfactual for Dec-26 + level gap estimated from Apr-Jul (published basis)
g2 = mean([p[m] - sum(bb * xx for bb, xx in zip(b2, s2row(m))) for m in aprjul26])
res["b_S2_plus_AprJul_gap"] = sum(bb * xx for bb, xx in zip(b2, s2row("2026-12"))) + g2
# (c) S1 (summer dummy) counterfactual for Dec-26 + gap
rowS1 = lambda m: [1.0, idx[m], 1.0 if m[5:] in ("04", "05", "06", "07") else 0.0]
g1 = mean([p[m] - sum(bb * xx for bb, xx in zip(b1, rowS1(m))) for m in aprjul26])
res["c_S1_plus_AprJul_gap"] = sum(bb * xx for bb, xx in zip(b1, rowS1("2026-12"))) + g1
# (d) Apr-Jul-26 level + mean historical (Dec - Apr-Jul same year)
diffs = [p[f"{y}-12"] - mean([p[f"{y}-{k:02d}"] for k in (4, 5, 6, 7)]) for y in ("2024", "2025")]
res["d_AprJul_plus_hist_Dec_diff"] = aj + mean(diffs)
# (e) Dec-25 + one year of legacy trend + bridge mode effect
res["e_Dec25_plus_trend_plus_bridge"] = p["2025-12"] + 12 * b0[1] + mode_eff
# (f) same as (e) using same-month YoY observed Apr-Jul
res["f_Dec25_plus_AprJul_YoY"] = p["2025-12"] + yoy_aj
for k, v in res.items():
    print(f"  {k:32s} {v:6.2f}")
seasonal = [res[k] for k in res if k != "a_trend_only"]
print(f"  seasonal methods b-f: range {min(seasonal):.2f}..{max(seasonal):.2f}, mean {mean(seasonal):.2f}")
# rough 80% PI for method (d): combine month noise (S2 resid SD), level uncertainty and
# the spread of the historical Dec-AprJul differential
sd_diff = abs(diffs[0] - diffs[1]) / math.sqrt(2)
pi_sd = math.sqrt(sig2 ** 2 + sig2 ** 2 / 4 + sd_diff ** 2 / 2)
print(f"  historical Dec-AprJul diffs {diffs[0]:+.2f}, {diffs[1]:+.2f}; approx PI SD for (d) {pi_sd:.2f};"
      f" 80% PI {res['d_AprJul_plus_hist_Dec_diff']-1.2816*pi_sd:.1f}..{res['d_AprJul_plus_hist_Dec_diff']+1.2816*pi_sd:.1f}")
print(f"  legacy-equivalent basis (subtract bridge 3.6): seasonal mean {mean(seasonal)-mode_eff:.2f}; trend-only {res['a_trend_only']-mode_eff:.2f}")

hdr("R-13  Backtest: forecast Dec-2025 using data through Jul-2025 only")
tr = [m for m in months if m <= "2025-07"]
Xb = [[1.0, idx[m]] for m in tr]
bb_, _, _, _, _, _ = ols(Xb, [p[m] for m in tr])
aj25v = mean([p[m] for m in aj25])
f_trend = aj25v + bb_[1] * (idx["2025-12"] - mean([idx[m] for m in aj25]))
f_seas = aj25v + (p["2024-12"] - mean([p[f"2024-{k:02d}"] for k in (4, 5, 6, 7)]))
f_yoy = p["2024-12"] + (aj25v - mean([p[f"2024-{k:02d}"] for k in (4, 5, 6, 7)]))
print(f"  actual Dec-25 {p['2025-12']}; trend-only {f_trend:.2f} (err {f_trend-p['2025-12']:+.2f}); "
      f"seasonal-diff {f_seas:.2f} (err {f_seas-p['2025-12']:+.2f}); YoY {f_yoy:.2f} (err {f_yoy-p['2025-12']:+.2f})")
print("  NOTE: a single backtest point; not decisive.")

hdr("R-14  Aug->Dec path implied by seasonality (why 'still rising' into Q4 is expected on any basis)")
for m in ("2026-08", "2026-09", "2026-10", "2026-11", "2026-12"):
    cf = sum(bb * xx for bb, xx in zip(b2, s2row(m))) + g2
    print(f"  {m}: S2 seasonal expectation (published basis) {cf:.2f}")

hdr("R-15  Backtest over Aug-Dec 2025, fitted on data through Jul-2025 only (5 correlated points)")
trm = [m for m in months if m <= "2025-07"]
bt0, _, _, _, _, _ = ols([[1.0, idx[m]] for m in trm], [p[m] for m in trm])
bt1, _, _, _, _, _ = ols([rowS1(m) for m in trm], [p[m] for m in trm])
lvl = aj25v
cen = mean([idx[m] for m in aj25])
e0, e1 = [], []
for m in ("2025-08", "2025-09", "2025-10", "2025-11", "2025-12"):
    f0 = lvl + bt0[1] * (idx[m] - cen)                       # Apr-Jul level + linear trend (no seasonality)
    f1 = lvl + bt1[1] * (idx[m] - cen) - bt1[2]              # Apr-Jul level + trend + exit from summer trough
    e0.append(f0 - p[m]); e1.append(f1 - p[m])
    print(f"  {m}: actual {p[m]}  trend-only {f0:.2f} ({f0-p[m]:+.2f})  S1 seasonal {f1:.2f} ({f1-p[m]:+.2f})")
print(f"  mean error: trend-only {mean(e0):+.2f}, S1 {mean(e1):+.2f};  MAE: trend-only {mean([abs(x) for x in e0]):.2f}, S1 {mean([abs(x) for x in e1]):.2f}")
print(f"  S1 summer effect estimated from 2024-01..2025-07 only: {bt1[2]:+.2f}")

hdr("R-16  Same-design (online arm) comparison with seasonal adjustment")
# expected legacy-pattern change from Feb to Apr-Jul under S2 (season + trend), applied to the online arm
feb_fit = sum(bb * xx for bb, xx in zip(b2, s2row("2026-02")))
aj_fit = mean([sum(bb * xx for bb, xx in zip(b2, s2row(m))) for m in aprjul26])
exp_change = aj_fit - feb_fit
obs_change = aj - bo[1]
se_sd = math.sqrt(se_p(bo[1], bo[0]) ** 2 + (sig2 ** 2) / 4)
print(f"  expected seasonal+trend change Feb->Apr-Jul {exp_change:+.2f}; observed online-arm->Apr-Jul {obs_change:+.2f};"
      f" residual {obs_change-exp_change:+.2f} (SE ~{se_sd:.2f}; 95% CI {obs_change-exp_change-1.96*se_sd:+.2f}..{obs_change-exp_change+1.96*se_sd:+.2f})")
print("  This comparison does not use the bridge LEGACY arm and does not need the mode effect to be stable after Feb.")

hdr("R-17  Known-answer self-test of this script's regression code (O-SOURCE-GROUNDED §4)")
# Synthetic series with exactly known parameters: intercept 20, slope 0.25/mo, summer -2.0.
syn = [20 + 0.25 * idx[m] + (-2.0 if m[5:] in ("04", "05", "06", "07") else 0.0) for m in legacy]
kb, _, ks, _, _, _ = ols(X1, syn)
ok1 = abs(kb[0] - 20) < 1e-9 and abs(kb[1] - 0.25) < 1e-9 and abs(kb[2] + 2.0) < 1e-9
print(f"  recover (20, 0.25, -2.0): got ({kb[0]:.6f}, {kb[1]:.6f}, {kb[2]:.6f})  {'PASS' if ok1 else 'FAIL'}")
# Deliberate defect: drop the summer term from the generating model's fit -> must show biased slope/resid
kb0, _, ks0, _, _, _ = ols(X0, syn)
print(f"  defect detection: trend-only fit on seasonal truth gives resid SD {ks0:.3f} (>0 flags omitted seasonality): {'DETECTED' if ks0 > 0.5 else 'MISSED'}")
# Deliberate defect: a mis-keyed month index (off by one year) must change the fitted slope
bad = [[1.0, idx[m] + (12 if m.startswith('2025') else 0), X1[i][2]] for i, m in enumerate(legacy)]
kbb, _, _, _, _, _ = ols(bad, syn)
print(f"  defect detection: mis-keyed time index -> slope {kbb[1]:.4f} vs true 0.25: {'DETECTED' if abs(kbb[1]-0.25) > 0.01 else 'MISSED'}")
