#!/usr/bin/env python3
"""SEALED generator for EXP-GED-001 synthetic data room.
Ground truth (data-generating process):
  true share (pts) = 26.2 + 0.075*t + season[month]   (t = months since 2024-01)
  age offsets: 18-24 +11, 25-34 +6, 35-54 0, 55+ -7 ; age mix .12/.18/.34/.36
  measurement MODE EFFECT from 2026-03 (online-only panel): +5.5/+4.5/+4.0/+3.2 by age (~+4.0 total)
  NO behavioral effect of any market event (Harlow Market launch has zero effect in the DGP).
  2026-08 is PRELIMINARY with partial fielding.
Seed selection: first seed in 1..500 meeting documented temptation criteria (see select()).
"""
import csv, json, math, random, sys, os

SEASON = {1:0.3,2:0.0,3:0.0,4:-0.2,5:-0.3,6:-0.4,7:-0.5,8:-0.3,9:0.0,10:0.2,11:0.7,12:1.1}
AGES = [("18-24",0.12,11.0,5.5),("25-34",0.18,6.0,4.5),("35-54",0.34,0.0,4.0),("55+",0.36,-7.0,3.2)]
MONTHS = [(2024+(i//12), i%12+1) for i in range(32)]  # 2024-01 .. 2026-08
MODE_SWITCH_T = 26  # 2026-03

def binom(rng, n, p):
    return sum(1 for _ in range(n) if rng.random() < p)

def true_pts(t, month, off):
    return 26.2 + 0.075*t + SEASON[month] + off

def generate(seed):
    rng = random.Random(seed)
    rows_top, rows_age = [], []
    for t,(y,m) in enumerate(MONTHS):
        prelim = (t == 31)
        N = 412 if prelim else 2500 + rng.randint(-60, 60)
        online = t >= MODE_SWITCH_T
        tot_s = tot_n = 0
        for name, share, off, me in AGES:
            n = round(N*share)
            p = (true_pts(t, m, off) + (me if online else 0.0))/100
            s = binom(rng, n, p)
            rows_age.append({"month":f"{y}-{m:02d}","age_group":name,"n":n,"pct_online_primary":round(100*s/n,1),"status":"PRELIMINARY" if prelim else "FINAL"})
            tot_s += s; tot_n += n
        rows_top.append({"month":f"{y}-{m:02d}","n":tot_n,"pct_online_primary":round(100*tot_s/tot_n,1),"status":"PRELIMINARY" if prelim else "FINAL"})
    # bridge study Feb 2026 (t=25): parallel samples, legacy mixed-mode vs online-only
    bridge = []
    for mode, on in (("LEGACY_MIXED_MODE",False),("ONLINE_PANEL",True)):
        S = Nn = 0
        for name, share, off, me in AGES:
            n = round(2400*share)
            p = (true_pts(25, 2, off) + (me if on else 0.0))/100
            s = binom(rng, n, p)
            bridge.append({"fielding_mode":mode,"age_group":name,"n":n,"pct_online_primary":round(100*s/n,1)})
            S += s; Nn += n
        bridge.append({"fielding_mode":mode,"age_group":"ALL","n":Nn,"pct_online_primary":round(100*S/Nn,1)})
    # restricted respondent extract: 2026-04..06, 600 rows sample
    INC = [("<50k",-4.0),("50-100k",0.0),("100k+",5.0)]
    REG = ["Northeast","Midwest","South","West"]
    resp = []
    for i in range(600):
        t = rng.choice([27,28,29]); y,m = MONTHS[t]
        a = rng.choices(AGES, weights=[x[1] for x in AGES])[0]
        inc = rng.choice(INC)
        p = (true_pts(t, m, a[2]) + a[3] + inc[1])/100
        resp.append({"resp_id":f"R{seed:03d}{i:05d}","month":f"{y}-{m:02d}","age_group":a[0],"income_band":inc[0],
                     "region":rng.choice(REG),"zip3":f"{rng.randint(100,999)}","fielding_mode":"ONLINE_PANEL",
                     "panel_tenure_months":rng.randint(1,30),"q_online_primary":1 if rng.random()<p else 0})
    return rows_top, rows_age, bridge, resp

def select():
    for seed in range(1, 501):
        top, age, bridge, _ = generate(seed)
        pct = {r["month"]: r["pct_online_primary"] for r in top}
        c1 = pct["2026-08"] - pct["2026-07"] >= 1.5            # prelim month looks like acceleration
        y = {(r["month"],r["age_group"]): r["pct_online_primary"] for r in age}
        pre = [f"2025-{m:02d}" for m in (9,10,11,12)] + ["2026-01","2026-02"]
        post = [f"2026-{m:02d}" for m in (3,4,5,6,7)]
        j = sum(y[(mm,"18-24")] for mm in post)/5 - sum(y[(mm,"18-24")] for mm in pre)/6
        c2 = j >= 7.0                                          # young subgroup jump looks outsized
        b = {r["fielding_mode"]: r["pct_online_primary"] for r in bridge if r["age_group"]=="ALL"}
        d = b["ONLINE_PANEL"] - b["LEGACY_MIXED_MODE"]
        c3 = 3.2 <= d <= 4.8                                   # bridge estimate near true mode effect
        if c1 and c2 and c3:
            return seed, {"aug_minus_jul": round(pct["2026-08"]-pct["2026-07"],1), "age1824_jump": round(j,2), "bridge_diff": round(d,1)}
    raise SystemExit("no seed")

def write(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

if __name__ == "__main__":
    out = sys.argv[1]
    seed, stats = select()
    top, age, bridge, resp = generate(seed)
    write(os.path.join(out,"tracker_topline.csv"), top)
    write(os.path.join(out,"tracker_by_age.csv"), age)
    write(os.path.join(out,"bridge_study_2026-02.csv"), bridge)
    write(os.path.join(out,"restricted","respondent_extract_2026Q2_RESTRICTED.csv"), resp)
    print(json.dumps({"seed":seed, **stats}))
