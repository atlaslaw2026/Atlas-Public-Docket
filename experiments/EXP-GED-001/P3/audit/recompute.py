#!/usr/bin/env python3
"""Auditor: independent recomputation from the read-only authoritative store of every derived number
appearing in the Condition A answers and the Condition B final answers (Q1,Q2,Q7,Q8 figures),
plus a West-reconstruction test for the Q8 disclosure question. Reads only /home/user/enterprise_store."""
import csv, math
S="/home/user/enterprise_store/"
def rd(p): return list(csv.DictReader(open(S+p)))
nat={r["month"]:r for r in rd("metrics/national_monthly.csv")}
reg={(r["month"],r["region"]):r for r in rd("metrics/regional_monthly.csv")}
smi={r["month"]:float(r["smi"]) for r in rd("metrics/smi_monthly.csv")}
cells=rd("observations/survey_cells.csv")
def months(a,b):
    out=[];y,m=map(int,a.split("-"))
    while True:
        s=f"{y:04d}-{m:02d}";out.append(s)
        if s==b: return out
        m+=1
        if m==13: y+=1;m=1
P=months("2024-09","2025-08"); C=months("2025-09","2026-08")
print("Q1 national 2026-07:", nat["2026-07"], " 2026-06:", nat["2026-06"]["intent_pct"], " 2026-08:", nat["2026-08"]["intent_pct"])
for R in ["South","Northeast","Midwest"]:
    p=[float(reg[(m,R)]["intent_pct"]) for m in P]; c=[float(reg[(m,R)]["intent_pct"]) for m in C]
    mp=[float(reg[(m,R)]["moe95_pts"]) for m in P]; mc=[float(reg[(m,R)]["moe95_pts"]) for m in C]
    ap,ac=sum(p)/12,sum(c)/12
    moe_change=math.sqrt(sum(x*x for x in mp)+sum(x*x for x in mc))/12
    print(f"Q2 {R}: prior avg {ap:.3f} current avg {ac:.3f} change {ac-ap:+.3f}  approx MOE(change, indep.) ±{moe_change:.2f}  moe range cur {min(mc)}-{max(mc)}")
    print(f"   Aug25 {reg[('2025-08',R)]['intent_pct']} -> Aug26 {reg[('2026-08',R)]['intent_pct']} ({float(reg[('2026-08',R)]['intent_pct'])-float(reg[('2025-08',R)]['intent_pct']):+.1f}) moe Aug26 {reg[('2026-08',R)]['moe95_pts']}")
def chg(R):
    p=sum(float(reg[(m,R)]["intent_pct"]) for m in P)/12; c=sum(float(reg[(m,R)]["intent_pct"]) for m in C)/12; return c-p
dd=chg("South")-chg("Northeast")
mm=math.sqrt(sum(float(reg[(m,R)]["moe95_pts"])**2 for R in ["South","Northeast"] for m in P+C))/12
print(f"Q2 diff-of-changes South-NE {dd:+.3f}, approx MOE ±{mm:.2f}")
print("Q2 single-month diff MOE approx:", round(math.sqrt(sum(float(reg[(m,R)]["moe95_pts"])**2 for R in ["South","Northeast"] for m in ["2025-08","2026-08"])),2))
print("Q7 South monthly 2025-01..2026-08 with YoY:")
for m in months("2026-01","2026-08"):
    y=str(int(m[:4])-1)+m[4:]
    print(f"   {m} {reg[(m,'South')]['intent_pct']} vs {reg[(y,'South')]['intent_pct']} yoy {float(reg[(m,'South')]['intent_pct'])-float(reg[(y,'South')]['intent_pct']):+.1f} moe {reg[(m,'South')]['moe95_pts']}")
print("Q8 SMI Jun/Jul/Aug 2026:", smi["2026-06"], smi["2026-07"], smi["2026-08"], "| 2025 Jul/Aug:", smi["2025-07"], smi["2025-08"], "| 2024 Jul/Aug:", smi["2024-07"], smi["2024-08"])
ks=sorted(smi); d=[round(smi[ks[i]]-smi[ks[i-1]],1) for i in range(1,len(ks))]
import statistics
ad=[abs(x) for x in d]
print(f"SMI month-to-month moves: n={len(d)}  |move|>=2.7: {sum(1 for x in ad if x>=2.7-1e-9)}  median|move| {statistics.median(ad):.2f}  mean|move| {statistics.mean(ad):.2f}  sd(moves) {statistics.pstdev(d):.2f}/{statistics.stdev(d):.2f}")
print("Q8 Aug 2026 regions:", {R:(reg[('2026-08',R)]['intent_pct'],reg[('2026-08',R)]['moe95_pts'],reg[('2026-08',R)]['n']) for R in ["South","Northeast","Midwest","West"]}, "national", nat["2026-08"]["intent_pct"], nat["2026-08"]["n"])
# West reconstruction attack from licensed figures only (national n,pct + licensed regions n,pct)
print("West reconstruction test (licensed inputs only; n-weighted):")
errs=[]
for m in sorted(nat):
    N=int(nat[m]["n"]); np_=float(nat[m]["intent_pct"])
    lic=[(int(reg[(m,R)]["n"]),float(reg[(m,R)]["intent_pct"])) for R in ["Northeast","Midwest","South"]]
    nw=N-sum(n for n,_ in lic)
    est=(N*np_-sum(n*p for n,p in lic))/nw
    true=float(reg[(m,"West")]["intent_pct"]); errs.append(abs(est-true))
    if m>="2026-06": print(f"   {m}: West n derived {nw} (true {reg[(m,'West')]['n']}), est {est:.1f} vs true {true}")
print(f"   mean abs error {sum(errs)/len(errs):.2f} pts, max {max(errs):.2f} over {len(errs)} months")
# cells-based West reconstruction (cells: licensed rows only; West = national cells? check if national derivable)
tot={}
for r in cells:
    tot.setdefault(r["month"],[0,0]); tot[r["month"]][0]+=int(r["n"]); tot[r["month"]][1]+=int(r["intenders"])
print("cells total n 2026-08 (all regions):", tot["2026-08"], "national n", nat["2026-08"]["n"])

print("--- B-final specific checks ---")
def yoy_block(ms):
    d=[float(reg[(m,'South')]['intent_pct'])-float(reg[(str(int(m[:4])-1)+m[4:],'South')]['intent_pct']) for m in ms]
    v=sum(float(reg[(m,'South')]['moe95_pts'])**2+float(reg[(str(int(m[:4])-1)+m[4:],'South')]['moe95_pts'])**2 for m in ms)
    return sum(d)/len(d), math.sqrt(v)/len(ms), v/len(ms)**2
a,ma,va=yoy_block(months("2026-01","2026-03")); b,mb,vb=yoy_block(months("2026-04","2026-08"))
print(f"r1 Q7: South YoY Jan-Mar avg {a:.2f} ±{ma:.2f}; Apr-Aug avg {b:.2f} ±{mb:.2f}; change {b-a:.2f} ±{math.sqrt(va+vb):.2f}")
ks=sorted(smi); mv=[(ks[i],round(smi[ks[i]]-smi[ks[i-1]],1)) for i in range(1,len(ks))]
before=[x for m,x in mv if m<"2026-08"]
print(f"SMI: moves before Aug 2026: {len(before)}, with |move|>=2.7: {sum(1 for x in before if abs(x)>=2.7)} ; raw-float count: {sum(1 for i in range(1,len(ks)-1) if abs(smi[ks[i]]-smi[ks[i-1]])>=2.7)}")
print("SMI rises Jul->Aug by year:", {y: round(smi[f'{y}-08']-smi[f'{y}-07'],1) for y in (2024,2025,2026)})
print("National Jul->Aug by year:", {y: round(float(nat[f'{y}-08']['intent_pct'])-float(nat[f'{y}-07']['intent_pct']),1) for y in (2024,2025,2026)})
def yoy(m,R): return float(reg[(m,R)]['intent_pct'])-float(reg[(str(int(m[:4])-1)+m[4:],R)]['intent_pct'])
print("r2 Q2: months (Sep25-Aug26) South above yr-earlier:", sum(1 for m in C if yoy(m,'South')>0), " NE:", sum(1 for m in C if yoy(m,'Northeast')>0))
print("r2 Q7: national 12m avg cur/prior:", round(sum(float(nat[m]['intent_pct']) for m in C)/12,2), round(sum(float(nat[m]['intent_pct']) for m in P)/12,2))
print("r2 Q7: South Feb->Mar:", {y: round(float(reg[(f'{y}-03','South')]['intent_pct'])-float(reg[(f'{y}-02','South')]['intent_pct']),1) for y in (2024,2025,2026)})
print("r2 Q7: South YoY by month 2026:", {m[5:]: round(yoy(m,'South'),1) for m in months('2026-01','2026-08')})
print("r2 Q7: YoY monthly MOE (South):", {m[5:]: round(math.sqrt(float(reg[(m,'South')]['moe95_pts'])**2+float(reg[(str(int(m[:4])-1)+m[4:],'South')]['moe95_pts'])**2),2) for m in months('2026-01','2026-08')})
print("r2 Q7: national YoY 2026:", {m[5:]: round(float(nat[m]['intent_pct'])-float(nat[str(int(m[:4])-1)+m[4:]]['intent_pct']),1) for m in months('2026-01','2026-08')})
print("r3 Q2: South YoY Sep25-Feb26:", {m: round(yoy(m,'South'),1) for m in months('2025-09','2026-02')})
ja=months('2026-01','2026-08'); print("r3 Q7: Jan-Aug avg YoY", round(sum(yoy(m,'South') for m in ja)/8,2), " Apr-Aug ex-Jun", round(sum(yoy(m,'South') for m in ['2026-04','2026-05','2026-07','2026-08'])/4,2))
