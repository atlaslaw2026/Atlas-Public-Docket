# Magistrate's own computation from its own CL-B retrievals (r_*.json). No West computed.
import json, math, statistics as st
L=lambda f: json.load(open(f))['data']
nat={r['month']:r for r in L('r_national.json')}
reg={}
for r in L('r_regional.json'): reg[(r['region'],r['month'])]=r
assert {r for r,_ in reg}=={'Northeast','Midwest','South'}
smi={r['month']:float(r['smi']) for r in L('r_smi.json')}
f=lambda d,k: float(d[k])
print('Q1 national 2026-07',nat['2026-07']); print(' 2026-06',nat['2026-06']); print(' 2026-08',nat['2026-08'])
m6,m7=nat['2026-06'],nat['2026-07']
print(' Jun-Jul diff',round(f(m7,'intent_pct')-f(m6,'intent_pct'),2),'diff MoE',round(math.hypot(f(m6,'moe95_pts'),f(m7,'moe95_pts')),2))
mo=[f(v,'moe95_pts') for v in nat.values()]; print(' nat moe range',min(mo),max(mo),' diff moe range',round(min(mo)*2**.5,2),round(max(mo)*2**.5,2))
def months(a,b):
    ms=sorted(nat); return [m for m in ms if a<=m<=b]
def avg(region,a,b):
    ms=months(a,b); v=[f(reg[(region,m)],'intent_pct') for m in ms]; e=[f(reg[(region,m)],'moe95_pts') for m in ms]
    return st.mean(v), math.sqrt(sum(x*x for x in e))/len(e), len(ms)
print('Q2')
res={}
for R in ['South','Northeast','Midwest']:
    p=avg(R,'2024-09','2025-08'); c=avg(R,'2025-09','2026-08')
    d=c[0]-p[0]; dm=math.hypot(p[1],c[1]); res[R]=(d,dm)
    print(f' {R}: prev {p[0]:.2f} cur {c[0]:.2f} chg {d:+.2f} moe {dm:.2f} (nmonths {p[2]},{c[2]})')
print(f" S-NE diff {res['South'][0]-res['Northeast'][0]:+.2f} moe {math.hypot(res['South'][1],res['Northeast'][1]):.2f}")
for R in ['South','Northeast']:
    a,b=reg[(R,'2025-08')],reg[(R,'2026-08')]; print(f' {R} Aug25 {a["intent_pct"]}±{a["moe95_pts"]} Aug26 {b["intent_pct"]}±{b["moe95_pts"]}')
rm=[f(v,'moe95_pts') for v in reg.values()]; print(' regional moe range',min(rm),max(rm))
sm=[f(v,'moe95_pts') for k,v in reg.items() if k[0]=='South']; print(' South moe range',min(sm),max(sm))
print('Q7 YoY gaps South / NE / MW')
def yoy(R,ms):
    d=[f(reg[(R,m)],'intent_pct')-f(reg[(R,str(int(m[:4])-1)+m[4:])],'intent_pct') for m in ms]
    e=[math.hypot(f(reg[(R,m)],'moe95_pts'),f(reg[(R,str(int(m[:4])-1)+m[4:])],'moe95_pts')) for m in ms]
    return st.mean(d), math.sqrt(sum(x*x for x in e))/len(e)
for R in ['South','Northeast','Midwest']:
    pre=yoy(R,['2026-01','2026-02','2026-03']); post=yoy(R,['2026-04','2026-05','2026-06','2026-07','2026-08'])
    print(f' {R}: JanMar {pre[0]:+.2f}±{pre[1]:.2f}  AprAug {post[0]:+.2f}±{post[1]:.2f}  widening {post[0]-pre[0]:+.2f}±{math.hypot(pre[1],post[1]):.2f}')
    if R=='South':
        a,b=reg[('South','2026-03')],reg[('South','2025-03')]; print('  Mar26',a['intent_pct'],a['moe95_pts'],'Mar25',b['intent_pct'],b['moe95_pts'],'diff',round(f(a,'intent_pct')-f(b,'intent_pct'),2),'moe',round(math.hypot(f(a,'moe95_pts'),f(b,'moe95_pts')),2))
    pre5=yoy(R,['2025-01','2025-02','2025-03']) if (R,'2024-01') in reg else None
    if pre5: post5=yoy(R,['2025-04','2025-05','2025-06','2025-07','2025-08']); print(f'   prior yr: JanMar {pre5[0]:+.2f} AprAug {post5[0]:+.2f}')
print('Q8 SMI')
ms=sorted(smi); print(' months',ms[0],ms[-1],len(ms))
for y in ['2024','2025','2026']: print(f' {y} Jun {smi[y+"-06"]} Jul {smi[y+"-07"]} Aug {smi[y+"-08"]} Jul->Aug {smi[y+"-08"]-smi[y+"-07"]:+.1f}')
mv=[round(smi[ms[i]]-smi[ms[i-1]],1) for i in range(1,len(ms))]
last=mv[-1]; print(' n moves',len(mv),'last',last)
print(' moves >=2.7 incl last',sum(abs(x)>=2.7-1e-9 for x in mv),'of',len(mv),'; before last',sum(abs(x)>=2.7-1e-9 for x in mv[:-1]),'of',len(mv)-1)
print(' median |move|',st.median([abs(x) for x in mv]))
for y in ['2024','2025','2026']: print(f' national intent {y} Jul->Aug', round(f(nat[y+'-08'],'intent_pct')-f(nat[y+'-07'],'intent_pct'),1))
print('Q8 Aug2026 figures', nat['2026-08']['intent_pct'],nat['2026-08']['moe95_pts'], [(R,reg[(R,'2026-08')]['intent_pct'],reg[(R,'2026-08')]['moe95_pts']) for R in ['South','Northeast','Midwest']])
print('Q9 other months near 41.0:',[(m,v['intent_pct']) for m,v in nat.items() if abs(f(v,'intent_pct')-41.0)<=0.5])
print('Forecast internal-note check: shift 0.3 vs half-width',(4.6-(-0.4))/2, 0.3/2.5, 'shifted point range',2.1-0.3,2.1+0.3)
