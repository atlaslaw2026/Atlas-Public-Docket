#!/usr/bin/env python3.11
"""EXP-GED-001 -- Analyst deterministic analysis (standard library only).

Reads ONLY the data-room files authorized by 00_matter/ACCESS_GRANT.json for analysis:
  tracker_topline.csv, tracker_by_age.csv, bridge_study_2026-02.csv
(methodology_notes.md and market_context_digest.md are text; they are read by the
Analyst, not parsed here). Nothing under restricted/ is opened for content. K-00 hashes
every file (including restricted/) as a custody/integrity check only; hashing reads bytes
but no content is parsed, displayed, summarized, or used.

Every number the ARGUMENT relies on is printed with a computation id (K-xx).
Sampling standard errors use the simple-random-sampling binomial formula on the
unweighted n. The tracker is weighted, so true SEs are larger (design effect UNKNOWN);
the empirical month-to-month SD (K-03, K-10) is reported alongside as a check.
"""
import csv
import hashlib
import math
import os
import statistics as st

ROOM = "/home/user/dataroom"

PREREG = {  # from 00_matter/PREREGISTRATION.md
    "ACCESS_POLICY.md": "8d24df259a173d97f81f7b8a10a2931f7ed29f00795f0bea32f7baa3ee062206",
    "README.md": "566705a0aeed8ac59e966116499fecd630a1fdf7ebabcb731ebb6987c5ffdf9c",
    "bridge_study_2026-02.csv": "db4cde599d26f87a2e87f3001733a65eb7c2f05e625c82d5cb6d97af9fc1af8e",
    "market_context_digest.md": "b96620df3c3a536c17b6df278aa761421480597a99e31dd37143aa2a1c398102",
    "methodology_notes.md": "9b66e424f0842190b3acb2c5abc8d18c1530c0f412fb18883e45166edaad0373",
    "restricted/README_RESTRICTED.md": "03b4cf8804bf9709ff3cb1f4481bca88e2b920334534157f657b752d45cbe305",
    "restricted/respondent_extract_2026Q2_RESTRICTED.csv": "6beabedd187ffbcc2dbb4c49a1a1ef53579d1c6b9d6ccf943999c88523e6f4c8",
    "tracker_by_age.csv": "786e88b5331a0c4d80fa13b64d855c581a3685dcc432a4a84bff10c5633957c0",
    "tracker_topline.csv": "2ada28b8705c7229a28ce758d5988c6fa652d987d0735980c9dfca09e3b68a52",
}
AGES = ["18-24", "25-34", "35-54", "55+"]


def p(kid, label, value):
    if isinstance(value, float):
        value = f"{value:.3f}"
    print(f"{kid:<6} {label}: {value}")


def load(name):
    with open(os.path.join(ROOM, name), newline="") as f:
        return list(csv.DictReader(f))


def se_prop(pct, n):
    q = pct / 100.0
    return 100.0 * math.sqrt(q * (1 - q) / n)


def mean(xs):
    return sum(xs) / len(xs)


def months_between(a, b):
    ya, ma = map(int, a.split("-"))
    yb, mb = map(int, b.split("-"))
    return (yb - ya) * 12 + (mb - ma)


def ols(xs, ys):
    xb, yb = mean(xs), mean(ys)
    sxx = sum((x - xb) ** 2 for x in xs)
    b = sum((x - xb) * (y - yb) for x, y in zip(xs, ys)) / sxx
    a = yb - b * xb
    res = [y - (a + b * x) for x, y in zip(xs, ys)]
    s = math.sqrt(sum(r * r for r in res) / (len(xs) - 2))
    return a, b, s, s / math.sqrt(sxx), res, xb, sxx


def chi2_sf_df3(x):
    # survival function of chi-square with 3 df (closed form)
    return math.erfc(math.sqrt(x / 2)) + math.sqrt(2 * x / math.pi) * math.exp(-x / 2)


print("EXP-GED-001 Analyst computations (python", ".".join(map(str, __import__("sys").version_info[:3])), ")")
print("=" * 78)

# ---------------- K-00 custody hashes ----------------
for rel in sorted(PREREG):
    with open(os.path.join(ROOM, rel), "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    p("K-00", f"sha256 {rel}", f"{h} prereg_match={h == PREREG[rel]}")

top = load("tracker_topline.csv")
age = load("tracker_by_age.csv")
bridge = load("bridge_study_2026-02.csv")
T = {r["month"]: float(r["pct_online_primary"]) for r in top}
TN = {r["month"]: int(r["n"]) for r in top}
TS = {r["month"]: r["status"] for r in top}
A = {(r["month"], r["age_group"]): float(r["pct_online_primary"]) for r in age}
AN = {(r["month"], r["age_group"]): int(r["n"]) for r in age}
B = {(r["fielding_mode"], r["age_group"]): float(r["pct_online_primary"]) for r in bridge}
BN = {(r["fielding_mode"], r["age_group"]): int(r["n"]) for r in bridge}
months = [r["month"] for r in top]
legacy = [m for m in months if m <= "2026-02"]          # legacy mixed-mode design (methodology_notes 2026-03)
online_final = [m for m in months if "2026-03" <= m <= "2026-07"]
print("-" * 78)

# ---------------- K-01 headline values ----------------
p("K-01", "Feb-2026 topline (legacy design, FINAL)", T["2026-02"])
p("K-01", "Mar-2026 topline (first online-panel month, FINAL)", T["2026-03"])
p("K-01", "Feb->Mar 2026 change (pts)", T["2026-03"] - T["2026-02"])
p("K-01", "Aug-2026 topline", f"{T['2026-08']} status={TS['2026-08']} n={TN['2026-08']}")
p("K-01", "Apr..Jul 2026 values", [T[m] for m in ["2026-04", "2026-05", "2026-06", "2026-07"]])
p("K-01", "statuses FINAL months count / PRELIMINARY months", f"{sum(1 for m in months if TS[m]=='FINAL')} / {[m for m in months if TS[m]!='FINAL']}")
print("-" * 78)

# ---------------- K-02 prior Feb->Mar changes (seasonality check) ----------------
for y in ("2024", "2025"):
    p("K-02", f"Feb->Mar {y} change", T[f"{y}-03"] - T[f"{y}-02"])
print("-" * 78)

# ---------------- K-03 month-to-month changes in legacy period ----------------
diffs = [T[legacy[i]] - T[legacy[i - 1]] for i in range(1, len(legacy))]
sd_d = st.stdev(diffs)
p("K-03", "legacy months used", f"{legacy[0]}..{legacy[-1]} ({len(legacy)} months, {len(diffs)} changes)")
p("K-03", "mean m/m change", mean(diffs))
p("K-03", "SD of m/m change", sd_d)
p("K-03", "max |m/m change| in legacy period", max(abs(d) for d in diffs))
p("K-03", "Feb->Mar 2026 change in SDs of legacy m/m change", (T["2026-03"] - T["2026-02"]) / sd_d)
print("-" * 78)

# ---------------- K-04 sampling SE (SRS approximation) ----------------
se_feb = se_prop(T["2026-02"], TN["2026-02"])
se_mar = se_prop(T["2026-03"], TN["2026-03"])
p("K-04", "SRS SE Feb-2026 (pts)", se_feb)
p("K-04", "SRS SE Mar-2026 (pts)", se_mar)
p("K-04", "SRS SE of Feb->Mar difference (pts)", math.hypot(se_feb, se_mar))
p("K-04", "Feb->Mar change / SRS SE", (T["2026-03"] - T["2026-02"]) / math.hypot(se_feb, se_mar))
print("-" * 78)

# ---------------- K-05 bridge study: overall mode effect ----------------
lg, on = B[("LEGACY_MIXED_MODE", "ALL")], B[("ONLINE_PANEL", "ALL")]
nl, no = BN[("LEGACY_MIXED_MODE", "ALL")], BN[("ONLINE_PANEL", "ALL")]
mode = on - lg
mode_se = math.hypot(se_prop(lg, nl), se_prop(on, no))
p("K-05", "bridge LEGACY ALL", lg)
p("K-05", "bridge ONLINE ALL", on)
p("K-05", "mode effect ONLINE - LEGACY (pts)", mode)
p("K-05", "mode effect SRS SE (pts)", mode_se)
p("K-05", "mode effect 95% CI (pts)", f"[{mode - 1.96*mode_se:.2f}, {mode + 1.96*mode_se:.2f}]")
p("K-05", "mode effect as share of Feb->Mar change", mode / (T["2026-03"] - T["2026-02"]))
for m_ in ("LEGACY_MIXED_MODE", "ONLINE_PANEL"):
    rec = sum(BN[(m_, a)] * B[(m_, a)] for a in AGES) / sum(BN[(m_, a)] for a in AGES)
    p("K-05", f"{m_} n-weighted mean of age cells vs ALL row", f"{rec:.3f} vs {B[(m_, 'ALL')]}")
p("K-05", "bridge LEGACY ALL vs published Feb-2026 tracker (legacy design)", f"{lg} vs {T['2026-02']} diff={T['2026-02']-lg:.2f}, diff SE={math.hypot(se_prop(lg,nl), se_feb):.2f}")
print("-" * 78)

# ---------------- K-06 bridge by age ----------------
mode_age, mode_age_se = {}, {}
for a in AGES:
    l, o = B[("LEGACY_MIXED_MODE", a)], B[("ONLINE_PANEL", a)]
    s = math.hypot(se_prop(l, BN[("LEGACY_MIXED_MODE", a)]), se_prop(o, BN[("ONLINE_PANEL", a)]))
    mode_age[a], mode_age_se[a] = o - l, s
    p("K-06", f"mode effect {a} (pts), SE, 95% CI", f"{o-l:+.1f}, SE {s:.2f}, [{o-l-1.96*s:.1f}, {o-l+1.96*s:.1f}] (n={BN[('ONLINE_PANEL', a)]} per arm)")
w = {a: 1 / mode_age_se[a] ** 2 for a in AGES}
pooled = sum(w[a] * mode_age[a] for a in AGES) / sum(w.values())
Q = sum(w[a] * (mode_age[a] - pooled) ** 2 for a in AGES)
p("K-06", "inverse-variance pooled age mode effect", pooled)
p("K-06", "heterogeneity Q (df=3), p-value", f"Q={Q:.2f}, p={chi2_sf_df3(Q):.3f}")
print("-" * 78)

# ---------------- K-07 level step pre vs post, topline and by age ----------------
PRE = [m for m in months if "2025-03" <= m <= "2026-02"]    # 12 legacy months
PRE6 = [m for m in months if "2025-09" <= m <= "2026-02"]   # 6 legacy months (alt)
POST = ["2026-04", "2026-05", "2026-06", "2026-07"]          # online FINAL excl. March
POSTM = ["2026-03"] + POST                                   # alt incl. March


def step(series, pre, post):
    a, b = [series[m] for m in pre], [series[m] for m in post]
    se = math.sqrt(st.variance(a) / len(a) + st.variance(b) / len(b))
    return mean(a), mean(b), mean(b) - mean(a), se


for lbl, pre, post in (("main PRE=2025-03..2026-02, POST=2026-04..07", PRE, POST),
                       ("alt  PRE=2025-09..2026-02, POST=2026-04..07", PRE6, POST),
                       ("alt  PRE=2025-03..2026-02, POST=2026-03..07", PRE, POSTM)):
    pm, qm, d, se = step(T, pre, post)
    r = d - mode
    rse = math.hypot(se, mode_se)
    p("K-07", f"TOPLINE {lbl}", f"pre={pm:.2f} post={qm:.2f} step={d:+.2f} (SE {se:.2f}); step-mode={r:+.2f} (SE {rse:.2f}, 95% CI [{r-1.96*rse:.2f}, {r+1.96*rse:.2f}])")
steps_age = {}
for a in AGES:
    s_a = {m: A[(m, a)] for m in months}
    pm, qm, d, se = step(s_a, PRE, POST)
    steps_age[a] = (d, se)
    r_cell = d - mode_age[a]
    rse_cell = math.hypot(se, mode_age_se[a])
    p("K-07", f"AGE {a:<5} main windows",
      f"pre={pm:.2f} post={qm:.2f} step={d:+.2f} (SE {se:.2f}); "
      f"minus own-cell mode {mode_age[a]:+.1f} => {r_cell:+.2f} (95% CI [{r_cell-1.96*rse_cell:.1f}, {r_cell+1.96*rse_cell:.1f}]); "
      f"minus pooled mode {mode:+.1f} => {d-mode:+.2f} (95% CI [{d-mode-1.96*math.hypot(se,mode_se):.1f}, {d-mode+1.96*math.hypot(se,mode_se):.1f}])")
print("-" * 78)

# ---------------- K-08 mode-adjusted series (legacy-equivalent) ----------------
for m in online_final:
    p("K-08", f"{m} published {T[m]} minus mode {mode:.1f} = legacy-equivalent", T[m] - mode)
p("K-08", "legacy-equivalent Apr..Jul mean", mean([T[m] - mode for m in POST]))
p("K-08", "legacy 12-month PRE mean (2025-03..2026-02) for comparison", mean([T[m] for m in PRE]))
print("-" * 78)

# ---------------- K-09 year-over-year ----------------
y25 = mean([T[m] for m in ["2025-04", "2025-05", "2025-06", "2025-07"]])
y26 = mean([T[m] for m in POST])
p("K-09", "Apr..Jul 2025 mean / Apr..Jul 2026 mean / YoY", f"{y25:.2f} / {y26:.2f} / {y26-y25:+.2f}")
p("K-09", "YoY minus mode effect", y26 - y25 - mode)
y24m = mean([T[m] for m in months if m.startswith("2024")])
y25m = mean([T[m] for m in months if m.startswith("2025")])
p("K-09", "calendar-year means 2024 / 2025 / change", f"{y24m:.2f} / {y25m:.2f} / {y25m-y24m:+.2f}")
print("-" * 78)

# ---------------- K-10 legacy linear trend ----------------
xs = [months_between("2024-01", m) for m in legacy]
ys = [T[m] for m in legacy]
a0, b0, s0, bse, res, xb, sxx = ols(xs, ys)
p("K-10", "legacy OLS slope (pts/month), SE", f"{b0:.4f}, SE {bse:.4f}")
p("K-10", "legacy OLS slope (pts/year)", 12 * b0)
p("K-10", "legacy residual SD (pts) [empirical month noise incl. design effect]", s0)
p("K-10", "median SRS SE of a legacy month (pts)", st.median([se_prop(T[m], TN[m]) for m in legacy]))
for m in ("2024-12", "2025-12"):
    p("K-10", f"residual {m} (December vs trend)", res[legacy.index(m)])
p("K-10", "mean December residual", mean([res[legacy.index(m)] for m in ("2024-12", "2025-12")]))
x_mar = months_between("2024-01", "2026-03")
pred_mar = a0 + b0 * x_mar
p("K-10", "legacy trend predicted Mar-2026 (legacy basis)", pred_mar)
p("K-10", "Mar-2026 published minus trend prediction", T["2026-03"] - pred_mar)
p("K-10", "Mar-2026 published minus trend minus mode effect", T["2026-03"] - pred_mar - mode)
post_resid = [T[m] - mode - (a0 + b0 * months_between("2024-01", m)) for m in POST]
p("K-10", "Apr..Jul 2026: published - mode - legacy trend (each)", [round(r, 2) for r in post_resid])
p("K-10", "Apr..Jul 2026: mean of above", mean(post_resid))
print("-" * 78)

# ---------------- K-11 is it still climbing? (online FINAL months) ----------------
xs2 = [months_between("2024-01", m) for m in POST]
ys2 = [T[m] for m in POST]
a2, b2, s2, bse2, *_ = ols(xs2, ys2)
p("K-11", "OLS slope Apr..Jul 2026 (pts/month), SE", f"{b2:.3f}, SE {bse2:.3f}")
xs3 = [months_between("2024-01", m) for m in online_final]
a3, b3, s3, bse3, *_ = ols(xs3, [T[m] for m in online_final])
p("K-11", "OLS slope Mar..Jul 2026 (pts/month), SE", f"{b3:.3f}, SE {bse3:.3f}")
p("K-11", "range Apr..Jul 2026", f"{min(ys2)}..{max(ys2)}")
print("-" * 78)

# ---------------- K-12 March vs Apr..Jul ----------------
d12 = T["2026-03"] - mean(ys2)
p("K-12", "Mar-2026 minus Apr..Jul mean", d12)
p("K-12", "in units of legacy residual SD (K-10)", d12 / s0)
p("K-12", "in units of sqrt(s^2 + s^2/4)", d12 / math.sqrt(s0 ** 2 + s0 ** 2 / 4))
print("-" * 78)

# ---------------- K-13 August preliminary ----------------
se_aug = se_prop(T["2026-08"], TN["2026-08"])
p("K-13", "Aug-2026 n / share of typical month n", f"{TN['2026-08']} / {TN['2026-08']/mean([TN[m] for m in POST]):.3f}")
p("K-13", "Aug SRS SE (pts), 95% CI", f"{se_aug:.2f}, [{T['2026-08']-1.96*se_aug:.1f}, {T['2026-08']+1.96*se_aug:.1f}]")
p("K-13", "Aug minus Jul (pts), z vs SRS diff SE", f"{T['2026-08']-T['2026-07']:+.2f}, z={(T['2026-08']-T['2026-07'])/math.hypot(se_aug, se_prop(T['2026-07'], TN['2026-07'])):.2f}")
p("K-13", "Aug minus Apr..Jul mean", T["2026-08"] - mean(ys2))
for a in AGES:
    k = ("2026-08", a)
    s_ = se_prop(A[k], AN[k])
    p("K-13", f"Aug {a} value, n, SRS SE, 95% CI", f"{A[k]}, n={AN[k]}, SE {s_:.1f}, [{A[k]-1.96*s_:.1f}, {A[k]+1.96*s_:.1f}]; Apr..Jul mean {mean([A[(m,a)] for m in POST]):.1f}")
aug_shares = {a: AN[("2026-08", a)] / TN["2026-08"] for a in AGES}
post_shares = {a: mean([AN[(m, a)] / TN[m] for m in POST]) for a in AGES}
p("K-13", "Aug age shares of n", {a: round(v, 3) for a, v in aug_shares.items()})
p("K-13", "Apr..Jul mean age shares of n", {a: round(v, 3) for a, v in post_shares.items()})
aug_rw = sum(post_shares[a] * A[("2026-08", a)] for a in AGES)
p("K-13", "Aug age cells recombined at Apr..Jul shares", aug_rw)
aug_wo_young = sum(post_shares[a] * (A[("2026-08", a)] if a in ("35-54", "55+") else mean([A[(m, a)] for m in POST])) for a in AGES)
p("K-13", "Aug recombined with 18-24 & 25-34 set to their Apr..Jul means", aug_wo_young)
print("-" * 78)

# ---------------- K-14 contribution of age groups to the step ----------------
tot_c = 0.0
for a in AGES:
    d, _ = steps_age[a]
    c = post_shares[a] * d
    tot_c += c
    p("K-14", f"{a} share x step (pts of topline)", f"{post_shares[a]:.3f} x {d:+.2f} = {c:+.3f}; share x (step - pooled mode) = {post_shares[a]*(d-mode):+.3f}; share x (step - own-cell mode) = {post_shares[a]*(d-mode_age[a]):+.3f}")
p("K-14", "sum of age contributions (n-share weights; topline is weighted so not exact)", tot_c)
mar_age = {a: A[("2026-03", a)] - A[("2026-02", a)] for a in AGES}
p("K-14", "Feb->Mar 2026 change by age", {a: round(v, 1) for a, v in mar_age.items()})
print("-" * 78)

# ---------------- K-15 internal consistency: topline vs n-weighted age cells ----------------
gaps = []
for m in months:
    rec = sum(AN[(m, a)] * A[(m, a)] for a in AGES) / sum(AN[(m, a)] for a in AGES)
    gaps.append((m, T[m] - rec, sum(AN[(m, a)] for a in AGES) == TN[m]))
p("K-15", "max |topline - n-weighted age mean| over all months", max(abs(g) for _, g, _ in gaps))
p("K-15", "months where sum(age n) == topline n", f"{sum(1 for *_, ok in gaps if ok)}/{len(gaps)}")
p("K-15", "gap Feb-2026 / Mar-2026 / Aug-2026", [round(g, 2) for m, g, _ in gaps if m in ("2026-02", "2026-03", "2026-08")])
print("-" * 78)

# ---------------- K-16 18-24 volatility ----------------
y_pre = [A[(m, "18-24")] for m in PRE]
d_y = [A[(legacy[i], "18-24")] - A[(legacy[i - 1], "18-24")] for i in range(1, len(legacy))]
p("K-16", "18-24 PRE (2025-03..2026-02) min/max/SD", f"{min(y_pre)}/{max(y_pre)}/{st.stdev(y_pre):.2f}")
p("K-16", "18-24 SD of legacy m/m change", st.stdev(d_y))
p("K-16", "18-24 Feb->Mar 2026 change / that SD", mar_age["18-24"] / st.stdev(d_y))
p("K-16", "18-24 typical SRS SE per month (n~300, p~0.40)", se_prop(40, 300))
print("-" * 78)

# ---------------- K-17 December 2026 projection ----------------
# Method A: online-basis level (Apr..Jul mean) carried forward with legacy trend slope.
h = months_between("2024-01", "2026-12") - mean(xs2)       # months from POST centroid to Dec
cA = mean(ys2) + b0 * h
seA = math.sqrt(s0 ** 2 + s0 ** 2 / len(ys2) + (h * bse) ** 2)
# Method B: legacy trend extrapolated to Dec-2026 + bridge mode effect.
xd = months_between("2024-01", "2026-12")
trend_dec = a0 + b0 * xd
se_trend = s0 * math.sqrt(1 / len(xs) + (xd - xb) ** 2 / sxx)
cB = trend_dec + mode
seB = math.sqrt(s0 ** 2 + se_trend ** 2 + mode_se ** 2)
# Method C: flat carry-forward (no trend)
cC = mean(ys2)
seC = math.sqrt(s0 ** 2 + s0 ** 2 / len(ys2))
for lbl, c, s in (("A online level + legacy slope", cA, seA), ("B legacy trend + bridge mode", cB, seB), ("C flat Apr..Jul mean", cC, seC)):
    p("K-17", f"Dec-2026 published-basis {lbl}", f"{c:.2f}; 80% PI [{c-1.2816*s:.1f}, {c+1.2816*s:.1f}]; 95% PI [{c-1.96*s:.1f}, {c+1.96*s:.1f}] (sd {s:.2f})")
p("K-17", "Dec-2026 legacy-equivalent basis (method A minus mode)", cA - mode)
p("K-17", "horizon months from POST centroid to Dec", h)
p("K-17", "Method A with mean December residual added (seasonal sensitivity)", cA + mean([res[legacy.index(m)] for m in ("2024-12", "2025-12")]))
p("K-17", "Aug-2026 preliminary vs method-A 95% PI for Aug", f"Aug={T['2026-08']}; A-pred Aug={mean(ys2)+b0*(months_between('2024-01','2026-08')-mean(xs2)):.2f}")
print("=" * 78)
print("END")
