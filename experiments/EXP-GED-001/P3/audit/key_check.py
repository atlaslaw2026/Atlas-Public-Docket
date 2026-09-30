#!/usr/bin/env python3
"""Auditor stage 2: check the P3 key's quoted figures against the store; also true (DGP) vs observed South effect."""
import csv
reg={(r["month"],r["region"]):float(r["intent_pct"]) for r in csv.DictReader(open("/home/user/enterprise_store/metrics/regional_monthly.csv"))}
def avg(R,ms): return sum(reg[(m,R)] for m in ms)/len(ms)
a=["2026-05","2026-06","2026-07"]; b=["2025-05","2025-06","2025-07"]
print("May-Jul 2026 vs 2025: South %+.2f  NE %+.2f"%(avg("South",a)-avg("South",b), avg("Northeast",a)-avg("Northeast",b)))
for m in ["2025-09","2025-10","2025-11","2025-12","2026-01","2026-02","2026-03","2026-04","2026-05","2026-06","2026-07","2026-08"]:
    print(m,"South-NE gap %+.1f"%(reg[(m,"South")]-reg[(m,"Northeast")]))
print("pre-period (2024-01..2025-05) mean South-NE gap %+.2f"%(sum(reg[(f,"South")]-reg[(f,"Northeast")] for f in [k[0] for k in reg if k[1]=="South" and k[0]<"2025-06"])/17))
# DGP: south_growth = 0.25*(t-17+1) from 2025-06 (t=17). True YoY South-vs-NE advantage at month t>=29 is 3.0 pts.
print("DGP true South YoY advantage (steady state, from 2026-06): +3.00 pts; Aug 2026 true cumulative South growth: +%.2f"%(0.25*(31-17+1)))
