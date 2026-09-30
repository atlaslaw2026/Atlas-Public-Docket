# Magistrate's own computation (stdlib only; reads only this folder's interface outputs). Does not import analyst/challenger code.
import json, statistics as st, math
nat={r['month']:r for r in json.load(open('out_national_monthly.csv.txt'))['data']}
smi={r['month']:float(r['smi']) for r in json.load(open('out_smi_monthly.csv.txt'))['data']}
reg={}
for r in json.load(open('out_regional.txt'))['data']:
    assert r['region']!='West'
    reg.setdefault(r['region'],{})[r['month']]=r
months=sorted(nat)
def P(d,m): return float(d[m]['intent_pct'])
def M(d,m): return float(d[m]['moe95_pts'])
print('M-01 Jul26 national',nat['2026-07'], 'range',37.6-2.0,37.6+2.0)
print('M-02 Jun->Jul',P(nat,'2026-07')-P(nat,'2026-06'),'diff margin',math.hypot(M(nat,'2026-06'),M(nat,'2026-07')))
last=[m for m in months if '2025-09'<=m<='2026-08']; prev=[m for m in months if '2024-09'<=m<='2025-08']
for R in ['South','Northeast','Midwest']:
    a=st.mean(P(reg[R],m) for m in last); b=st.mean(P(reg[R],m) for m in prev)
    se=lambda ms: math.sqrt(sum((M(reg[R],m)/1.96)**2 for m in ms))/len(ms)
    marg=1.96*math.hypot(se(last),se(prev))
    print('M-03',R,'last12 %.2f prev12 %.2f chg %+.2f  ±%.2f'%(a,b,a-b,marg), 'moe range',min(M(reg[R],m) for m in last+prev),max(M(reg[R],m) for m in last+prev),'last12 moe range',min(M(reg[R],m) for m in last),max(M(reg[R],m) for m in last))
S,N=reg['South'],reg['Northeast']
d=lambda R,ms: st.mean(P(R,m) for m in last) - st.mean(P(R,m) for m in prev)
print('M-04 S-NE diff of changes', d(S,None)-d(N,None))
print('M-05 Aug25->Aug26 S',P(S,'2025-08'),P(S,'2026-08'),'NE',P(N,'2025-08'),P(N,'2026-08'))
yoy={m:P(S,m)-P(S,m.replace('2026','2025').replace('2025-0','2025-0') if m.startswith('2026') else None) for m in []}
print('M-06 South YoY by month:')
for m in last:
    y=str(int(m[:4])-1)+m[4:]
    print('   ',m,'%+.1f'%(P(S,m)-P(S,y)))
def yoyavg(R,ms): return st.mean(P(R,m)-P(R,str(int(m[:4])-1)+m[4:]) for m in ms)
q1=['2026-01','2026-02','2026-03']; aa=['2026-04','2026-05','2026-06','2026-07','2026-08']; aa_noJun=['2026-04','2026-05','2026-07','2026-08']
for R in ['South','Northeast','Midwest']:
    print('M-07',R,'JanAug YoY %+.2f'%yoyavg(reg[R],q1+aa),'Q1 %+.2f'%yoyavg(reg[R],q1),'AprAug %+.2f'%yoyavg(reg[R],aa),'AprAug exJun %+.2f'%yoyavg(reg[R],aa_noJun))
# noise band of widening (South): each YoY diff has var moe_a^2+moe_b^2; avg
def band(R,ms):
    return math.sqrt(sum((M(R,m)/1.96)**2+(M(R,str(int(m[:4])-1)+m[4:])/1.96)**2 for m in ms))/len(ms)
for lab,ms in [('AprAug',aa),('AprAug exJun',aa_noJun)]:
    print('M-07b South widening',lab,'%+.2f'%(yoyavg(S,ms)-yoyavg(S,q1)),'±%.2f'%(1.96*math.hypot(band(S,q1),band(S,ms))))
# SMI
sm=sorted(smi); ch=[smi[sm[i]]-smi[sm[i-1]] for i in range(1,len(sm))]
print('M-09 SMI JulAug 2024 %+.1f 2025 %+.1f 2026 %+.1f'%(smi['2024-08']-smi['2024-07'],smi['2025-08']-smi['2025-07'],smi['2026-08']-smi['2026-07']))
print('   n changes',len(ch),'sd %.2f median|d| %.2f mean|d| %.2f count|d|>=2.7: %d'%(st.stdev(ch),st.median([abs(x) for x in ch]),st.mean([abs(x) for x in ch]),sum(abs(x)>=2.7-1e-9 for x in ch)))
print('   Jun26 %.1f Jul26 %.1f Aug26 %.1f Aug25 %.1f'%(smi['2026-06'],smi['2026-07'],smi['2026-08'],smi['2025-08']))
print('M-10 Aug26 national',nat['2026-08'],'range',41.4-2,41.4+2,'41.0-37.6=',round(41.0-37.6,1))
for R in ['South','Northeast','Midwest']: print('M-08 Aug26',R,reg[R]['2026-08'])
