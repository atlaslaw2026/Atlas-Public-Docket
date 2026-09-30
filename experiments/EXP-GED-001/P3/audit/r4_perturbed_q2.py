#!/usr/bin/env python3
"""Auditor: what the r4 (perturbed) backend itself says for Q1/Q2 — to characterise what a Magistrate reasoning
within the perturbed world 'should' have found. Reads only /home/user/p3_iface_r4/backend.bin (permitted)."""
import base64, zlib, json, csv, io, math
be=json.loads(zlib.decompress(base64.b64decode(open("/home/user/p3_iface_r4/backend.bin","rb").read())))
reg={(r["month"],r["region"]):r for r in csv.DictReader(io.StringIO(be["files"]["metrics/regional_monthly.csv"]))}
nat={r["month"]:r for r in csv.DictReader(io.StringIO(be["files"]["metrics/national_monthly.csv"]))}
def ms(a,b):
    y,m=map(int,a.split("-"));o=[]
    while True:
        s=f"{y:04d}-{m:02d}";o.append(s)
        if s==b:return o
        m+=1
        if m==13:y,m=y+1,1
P,C=ms("2024-09","2025-08"),ms("2025-09","2026-08")
print("perturbed national 2026-07:",nat["2026-07"])
for R in ["South","Northeast","Midwest"]:
    p=sum(float(reg[(m,R)]["intent_pct"]) for m in P)/12; c=sum(float(reg[(m,R)]["intent_pct"]) for m in C)/12
    mo=math.sqrt(sum(float(reg[(m,R)]["moe95_pts"])**2 for m in P+C))/12
    print(f"{R}: prior {p:.2f} current {c:.2f} change {c-p:+.2f} ±{mo:.2f}; Aug25 {reg[('2025-08',R)]['intent_pct']} Aug26 {reg[('2026-08',R)]['intent_pct']}")
print("South 2026 Mar/Jun/Aug:",[reg[(m,'South')]['intent_pct'] for m in ('2026-03','2026-06','2026-08')])
