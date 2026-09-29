"""Magistrate's own computation for EXP-GED-001.

Written by the Magistrate instance spawned for this determination. It does not import, copy,
or run 03_analysis/analysis.py or 04_challenge/reconstruct.py. It opens only the five files
that ACCESS_GRANT.json authorizes. Python 3 standard library only (numpy is not installed).
Output ids are M-xx.
"""
import csv, hashlib, math, statistics
from statistics import NormalDist

ROOM = "/home/user/dataroom/"
AUTH = ["tracker_topline.csv", "tracker_by_age.csv", "bridge_study_2026-02.csv",
        "methodology_notes.md", "market_context_digest.md"]
PREREG = {
    "tracker_topline.csv": "2ada28b8705c7229a28ce758d5988c6fa652d987d0735980c9dfca09e3b68a52",
    "tracker_by_age.csv": "786e88b5331a0c4d80fa13b64d855c581a3685dcc432a4a84bff10c5633957c0",
    "bridge_study_2026-02.csv": "db4cde599d26f87a2e87f3001733a65eb7c2f05e625c82d5cb6d97af9fc1af8e",
    "methodology_notes.md": "9b66e424f0842190b3acb2c5abc8d18c1530c0f412fb18883e45166edaad0373",
    "market_context_digest.md": "b96620df3c3a536c17b6df278aa761421480597a99e31dd37143aa2a1c398102",
}

def h(title):
    print("\n== " + title)

h("M-00 custody (authorized files only)")
for f in AUTH:
    d = hashlib.sha256(open(ROOM + f, "rb").read()).hexdigest()
    print(f, "MATCH" if d == PREREG[f] else "MISMATCH " + d)

top = list(csv.DictReader(open(ROOM + "tracker_topline.csv")))
age = list(csv.DictReader(open(ROOM + "tracker_by_age.csv")))
br = list(csv.DictReader(open(ROOM + "bridge_study_2026-02.csv")))
months = [r["month"] for r in top]
y = {r["month"]: float(r["pct_online_primary"]) for r in top}
n = {r["month"]: int(r["n"]) for r in top}
status = {r["month"]: r["status"] for r in top}
final = [m for m in months if status[m] == "FINAL"]
legacy = [m for m in final if m <= "2026-02"]
online_final = [m for m in final if m >= "2026-03"]
idx = {m: i for i, m in enumerate(months)}  # 2024-01 -> 0
def moy(m): return int(m[5:])
def se_p(p, nn): return math.sqrt(p * (100 - p) / nn)

h("M-01 Q2 existence checks")
print("topline columns:", list(top[0].keys()))
print("age columns:", list(age[0].keys()))
print("bridge columns:", list(br[0].keys()))
print("last month in topline:", months[-1], "| any 2026-09 row:", "2026-09" in months,
      "| any 2026-09 in age:", any(r["month"] == "2026-09" for r in age))
for f in ["methodology_notes.md", "market_context_digest.md"]:
    t = open(ROOM + f).read()
    print(f, "| 'West':", "West" in t, "| 'September':", "September" in t,
          "| 'region':", t.count("region"), "| 'Harlow':", t.count("Harlow"))

h("M-02 the jump and legacy month-to-month noise")
jump = y["2026-03"] - y["2026-02"]
diffs = [y[legacy[i + 1]] - y[legacy[i]] for i in range(len(legacy) - 1)]
print(f"Feb->Mar 2026 = {jump:+.2f}; legacy MoM SD = {statistics.stdev(diffs):.2f}; max |MoM| = {max(abs(d) for d in diffs):.2f}; z = {jump/statistics.stdev(diffs):.2f}")
print("prior Feb->Mar:", {yr: round(y[yr + '-03'] - y[yr + '-02'], 2) for yr in ["2024", "2025"]})

h("M-03 bridge design effect")
b = {(r["fielding_mode"], r["age_group"]): (float(r["pct_online_primary"]), int(r["n"])) for r in br}
on, nn1 = b[("ONLINE_PANEL", "ALL")]; lg, nn2 = b[("LEGACY_MIXED_MODE", "ALL")]
de = on - lg; de_se = math.sqrt(se_p(on, nn1) ** 2 + se_p(lg, nn2) ** 2)
print(f"design effect = {de:.2f}, SRS SE {de_se:.3f}, 95% CI {de-1.96*de_se:.2f}..{de+1.96*de_se:.2f}; share of jump {de/jump:.1%}")
for g in ["18-24", "25-34", "35-54", "55+"]:
    o, a = b[("ONLINE_PANEL", g)], b[("LEGACY_MIXED_MODE", g)]
    print(f"  {g}: {o[0]-a[0]:+.1f} (SE {math.sqrt(se_p(*o)**2+se_p(*a)**2):.2f})")
print(f"published Feb-2026 {y['2026-02']} vs bridge legacy arm {lg}: diff {y['2026-02']-lg:+.2f}; "
      f"alt design effect anchored on published Feb = {on - y['2026-02']:.2f}")

# ---------- least squares (stdlib) ----------
def ols(X, Y):
    k = len(X[0]); N = len(Y)
    XtX = [[sum(X[r][i] * X[r][j] for r in range(N)) for j in range(k)] for i in range(k)]
    XtY = [sum(X[r][i] * Y[r] for r in range(N)) for i in range(k)]
    A = [row[:] + [1.0 if i == j else 0.0 for j in range(k)] for i, row in enumerate(XtX)]
    for c in range(k):
        p = max(range(c, k), key=lambda r: abs(A[r][c])); A[c], A[p] = A[p], A[c]
        pv = A[c][c]; A[c] = [v / pv for v in A[c]]
        for r in range(k):
            if r != c:
                f = A[r][c]; A[r] = [vr - f * vc for vr, vc in zip(A[r], A[c])]
    inv = [row[k:] for row in A]
    beta = [sum(inv[i][j] * XtY[j] for j in range(k)) for i in range(k)]
    res = [Y[r] - sum(beta[i] * X[r][i] for i in range(k)) for r in range(N)]
    s2 = sum(e * e for e in res) / (N - k)
    return beta, inv, s2, N - k

def pred(beta, inv, s2, x):
    mu = sum(bi * xi for bi, xi in zip(beta, x))
    v = s2 * sum(x[i] * inv[i][j] * x[j] for i in range(len(x)) for j in range(len(x)))
    return mu, math.sqrt(s2 + v)

# Student-t quantiles for small df (two-sided 80% and 95%), hard-coded standard table values.
T80 = {14: 1.345, 15: 1.341, 16: 1.337, 17: 1.333, 18: 1.330, 19: 1.328, 20: 1.325, 21: 1.323, 22: 1.321, 23: 1.319, 24: 1.318, 25: 1.316, 26: 1.315, 27: 1.314, 28: 1.313}
T95 = {14: 2.145, 15: 2.131, 16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 21: 2.080, 22: 2.074, 23: 2.069, 24: 2.064, 25: 2.060, 26: 2.056, 27: 2.052, 28: 2.048}

def row_summer(m, post=True):
    x = [1.0, idx[m], 1.0 if 4 <= moy(m) <= 7 else 0.0]
    if post: x.append(1.0 if m >= "2026-03" else 0.0)
    return x

def row_moy(m, post=True):
    x = [1.0, idx[m]] + [1.0 if moy(m) == k else 0.0 for k in range(2, 13)]
    if post: x.append(1.0 if m >= "2026-03" else 0.0)
    return x

h("M-04 seasonality in the legacy series (legacy FINAL months only, 2024-01..2026-02)")
bt, inv, s2, df = ols([row_summer(m, False) for m in legacy], [y[m] for m in legacy])
print(f"trend+summer: slope {bt[1]:.4f}/mo ({bt[1]*12:.2f}/yr); summer(Apr-Jul) {bt[2]:+.2f} SE {math.sqrt(s2*inv[2][2]):.2f} t={bt[2]/math.sqrt(s2*inv[2][2]):.1f}; resid SD {math.sqrt(s2):.2f}; df {df}")
for yr in ["2024", "2025"]:
    aj = statistics.mean(y[f"{yr}-0{k}"] for k in range(4, 8))
    rest = statistics.mean(y[f"{yr}-{k:02d}"] for k in [1, 2, 3, 8, 9, 10, 11, 12])
    print(f"  {yr}: Apr-Jul mean {aj:.2f}, rest {rest:.2f}, diff {aj-rest:+.2f}; Mar-AprJul {y[yr+'-03']-aj:+.2f}; Dec-AprJul {y[yr+'-12']-aj:+.2f}")
aj26 = statistics.mean(y[f"2026-0{k}"] for k in range(4, 8))
print(f"  2026: Apr-Jul mean {aj26:.2f}; Mar-AprJul {y['2026-03']-aj26:+.2f}")
bt0, inv0, s20, df0 = ols([row_summer(m, False) for m in legacy], [y[m] for m in legacy])
cf = [sum(bi * xi for bi, xi in zip(bt0, row_summer(m, False))) for m in online_final]
gap = statistics.mean(y[m] - c for m, c in zip(online_final, cf))
gapAJ = statistics.mean(y[m] - sum(bi * xi for bi, xi in zip(bt0, row_summer(m, False))) for m in online_final if m != "2026-03")
print(f"legacy-only counterfactual: mean gap Mar-Jul 2026 {gap:+.2f}; Apr-Jul {gapAJ:+.2f} (vs bridge {de:.2f}; residual {gapAJ-de:+.2f})")

h("M-05 intervention models on all FINAL months (2024-01..2026-07): step estimated from the tracker itself")
models = {"summer": row_summer, "month-of-year": row_moy}
fits = {}
for name, fn in models.items():
    X = [fn(m) for m in final]; Y = [y[m] for m in final]
    bt, inv, s2, df = ols(X, Y)
    k = len(bt) - 1
    step, step_se = bt[k], math.sqrt(s2 * inv[k][k])
    fits[name] = (bt, inv, s2, df)
    print(f"{name}: step {step:+.2f} SE {step_se:.2f} (95% CI {step-T95[df]*step_se:.2f}..{step+T95[df]*step_se:.2f}); "
          f"step - bridge = {step-de:+.2f} (SE {math.sqrt(step_se**2+de_se**2):.2f}); slope {bt[1]*12:.2f}/yr; resid SD {math.sqrt(s2):.2f}; df {df}")

h("M-06 December 2026 forecasts (published, online-panel basis)")
idx["2026-12"] = 35; idx["2026-09"] = 32
for name, fn in models.items():
    bt, inv, s2, df = fits[name]
    mu, sd = pred(bt, inv, s2, fn("2026-12"))
    mu9, sd9 = pred(bt, inv, s2, fn("2026-09"))
    print(f"{name}: Dec {mu:.2f}  80% PI {mu-T80[df]*sd:.1f}..{mu+T80[df]*sd:.1f}  95% PI {mu-T95[df]*sd:.1f}..{mu+T95[df]*sd:.1f}"
          f" | legacy-equiv (minus bridge 3.6) {mu-de:.2f} | Sep {mu9:.2f} (80% {mu9-T80[df]*sd9:.1f}..{mu9+T80[df]*sd9:.1f})")
# Analyst method A reproduction (trend-only from the Apr-Jul level)
bt_l, inv_l, s2_l, df_l = ols([[1.0, idx[m]] for m in legacy], [y[m] for m in legacy])
print(f"trend-only (Analyst method A): Apr-Jul mean {aj26:.2f} + {bt_l[1]:.4f}*6.5 = {aj26+bt_l[1]*6.5:.2f}; legacy resid SD {math.sqrt(s2_l):.2f}")
print(f"naive seasonal: Apr-Jul 2026 + mean historical (Dec - Apr-Jul) = {aj26 + statistics.mean([y['2024-12']-25.2, y['2025-12']-statistics.mean(y[f'2025-0{k}'] for k in range(4,8))]):.2f}")

h("M-07 backtest: fit on 2024-01..2025-07, forecast 2025-08..2025-12 (legacy only, no step term)")
train = [m for m in legacy if m <= "2025-07"]; test = [m for m in legacy if "2025-08" <= m <= "2025-12"]
for name, fn in [("trend-only-from-AprJul", None), ("summer", lambda m: row_summer(m, False)), ("month-of-year", lambda m: row_moy(m, False))]:
    if fn is None:
        btt, _, _, _ = ols([[1.0, idx[m]] for m in train], [y[m] for m in train])
        base = statistics.mean(y[f"2025-0{k}"] for k in range(4, 8))
        preds = [base + btt[1] * (idx[m] - 17.5) for m in test]
    else:
        btt, invt, s2t, dft = ols([fn(m) for m in train], [y[m] for m in train])
        preds = [sum(bi * xi for bi, xi in zip(btt, fn(m))) for m in test]
    errs = [p - y[m] for p, m in zip(preds, test)]
    print(f"{name}: preds {[round(p,2) for p in preds]} actual {[y[m] for m in test]} mean err {statistics.mean(errs):+.2f} MAE {statistics.mean(abs(e) for e in errs):.2f}; Dec err {errs[-1]:+.2f}")

h("M-08 August 2026 preliminary by age vs Apr-Jul 2026 means")
A = {(r["month"], r["age_group"]): (float(r["pct_online_primary"]), int(r["n"])) for r in age}
groups = ["18-24", "25-34", "35-54", "55+"]
tot = sum(A[("2026-08", g)][1] for g in groups)
dev_total = 0
for g in groups:
    mean_aj = statistics.mean(A[(f"2026-0{k}", g)][0] for k in range(4, 8))
    v, nn = A[("2026-08", g)]
    contrib = (v - mean_aj) * nn / tot; dev_total += contrib
    print(f"  {g}: Aug {v} (n={nn}, SE {se_p(v,nn):.1f}) vs AprJul {mean_aj:.2f}: {v-mean_aj:+.2f}, z {(v-mean_aj)/se_p(v,nn):.2f}, contribution {contrib:+.2f}")
print(f"  total deviation {dev_total:+.2f}; Aug topline {y['2026-08']} SE {se_p(y['2026-08'],411):.2f}; vs Jul z {(y['2026-08']-y['2026-07'])/math.sqrt(se_p(y['2026-08'],411)**2+se_p(y['2026-07'],n['2026-07'])**2):.2f}")
bts, _, _, _ = fits["summer"]
exp_aug = sum(bi * xi for bi, xi in zip(bts, row_summer("2026-08")))
print(f"  seasonal-model expectation for Aug 2026 {exp_aug:.2f}; Aug prelim minus expectation {y['2026-08']-exp_aug:+.2f} (z {(y['2026-08']-exp_aug)/se_p(y['2026-08'],411):.2f})")

h("M-09 age: same-month YoY (Apr-Jul 2026 vs Apr-Jul 2025) minus pooled bridge effect")
for g in groups:
    yoy = statistics.mean(A[(f"2026-0{k}", g)][0] - A[(f"2025-0{k}", g)][0] for k in range(4, 8))
    o, a = b[("ONLINE_PANEL", g)], b[("LEGACY_MIXED_MODE", g)]
    print(f"  {g}: YoY {yoy:+.2f}; minus pooled {de:.1f} = {yoy-de:+.2f}; minus own-cell {o[0]-a[0]:+.1f} = {yoy-(o[0]-a[0]):+.2f}")
yoy_top = statistics.mean(y[f"2026-0{k}"] - y[f"2025-0{k}"] for k in range(4, 8))
print(f"  topline YoY {yoy_top:+.2f}; minus bridge {yoy_top-de:+.2f}; minus bridge and legacy trend ({bt_l[1]*12:.2f}/yr) {yoy_top-de-bt_l[1]*12:+.2f}")
mar_yoy = y["2026-03"] - y["2025-03"]
print(f"  March YoY {mar_yoy:+.2f}; minus bridge {mar_yoy-de:+.2f}; minus bridge and trend {mar_yoy-de-bt_l[1]*12:+.2f}")

h("M-10 internal consistency: age cells recombine to topline")
mx = 0
for m in months:
    rec = sum(A[(m, g)][0] * A[(m, g)][1] for g in groups) / sum(A[(m, g)][1] for g in groups)
    mx = max(mx, abs(rec - y[m]))
print(f"max |n-weighted recombination - topline| = {mx:.3f}")
