# Magistrate's own computation from its own interface responses (r_*.json). Uses decimal arithmetic to avoid float artefacts.
import json
from decimal import Decimal as D
L=lambda f: json.load(open(f))['data']
nat=L('r_metrics_national_monthly_csv.json'); reg=L('r_regional.json'); smi=L('r_metrics_smi_monthly_csv.json')
print('national months', nat[0]['month'], '->', nat[-1]['month'], len(nat))
N={r['month']:(D(r['intent_pct']),int(r['n']),D(r['moe95_pts'])) for r in nat}
print('M1 Jul26', N['2026-07'], 'Jun26', N['2026-06'], 'Aug26', N['2026-08'])
print('M1 range', N['2026-07'][0]-N['2026-07'][2], N['2026-07'][0]+N['2026-07'][2])
print('M1 moe range national', min(v[2] for v in N.values()), max(v[2] for v in N.values()))
m=N['2026-07'][2]; md=N['2026-06'][2]
print('M1 diff moe jun-jul', float((m*m+md*md).sqrt()))
R={}
for r in reg: R.setdefault(r['region'],{})[r['month']]=(D(r['intent_pct']),int(r['n']),D(r['moe95_pts']))
months=sorted(N)
last12=months[-12:]; prev12=months[-24:-12]
print('last12',last12[0],last12[-1],'prev12',prev12[0],prev12[-1])
def avg(d,ms): return sum(d[x][0] for x in ms)/len(ms)
for reg_ in ['South','Northeast','Midwest']:
    d=R[reg_]
    a1,a0=avg(d,last12),avg(d,prev12)
    print('M2',reg_,'avg last12 %.2f prev12 %.2f diff %.2f'%(a1,a0,a1-a0),'Aug25',d['2025-08'][0],'Aug26',d['2026-08'][0],'chg',d['2026-08'][0]-d['2025-08'][0],
      'moe range last12',min(d[x][2] for x in last12),max(d[x][2] for x in last12),
      'months above yr-earlier', sum(1 for x in last12 if d[x][0]>d[prev12[last12.index(x)]][0]))
a1,a0=avg({k:v for k,v in N.items()},last12),avg(N,prev12); print('M2 national avg %.2f %.2f'%(a1,a0))
S=R['South'];NE=R['Northeast']
def dm(d,a,b): return float((d[a][2]**2+d[b][2]**2).sqrt())
print('M2 South aug-aug moe',dm(S,'2026-08','2025-08'),'NE',dm(NE,'2026-08','2025-08'))
gap=(S['2026-08'][0]-S['2025-08'][0])-(NE['2026-08'][0]-NE['2025-08'][0])
print('M2 gap aug-aug',gap,'combined moe', (sum(x**2 for x in [S['2026-08'][2],S['2025-08'][2],NE['2026-08'][2],NE['2025-08'][2]]).sqrt()))
# averages: moe of mean of 12 independent months approx sqrt(sum moe^2)/12
import math
def moe_avg(d,ms): return math.sqrt(sum(float(d[x][2])**2 for x in ms))/len(ms)
gS=float(avg(S,last12)-avg(S,prev12)); gN=float(avg(NE,last12)-avg(NE,prev12))
mS=math.hypot(moe_avg(S,last12),moe_avg(S,prev12)); mN=math.hypot(moe_avg(NE,last12),moe_avg(NE,prev12))
print('M2 avg-change South %.2f +-%.2f ; NE %.2f +-%.2f ; gap %.2f +-%.2f'%(gS,mS,gN,mN,gS-gN,math.hypot(mS,mN)))
# Q7 seasonality and YoY
for y in ['2024','2025','2026']:
    print('M3 South Feb->Mar',y,S[y+'-03'][0]-S[y+'-02'][0],' national',N[y+'-03'][0]-N[y+'-02'][0])
print('M3 South YoY 2026 by month:')
for mm in ['01','02','03','04','05','06','07','08']:
    a='2026-'+mm;b='2025-'+mm
    print('  ',a,'South',S[a][0],'yoy',S[a][0]-S[b][0],'moe %.2f'%dm(S,a,b),' national yoy',N[a][0]-N[b][0])
# SMI
sm=[(r['month'],D(r['smi'])) for r in smi]
print('SMI months',sm[0][0],'->',sm[-1][0],len(sm))
mv=[(sm[i][0],sm[i][1]-sm[i-1][1]) for i in range(1,len(sm))]
print('M4 n moves',len(mv),'Jul->Aug26',[v for k,v in mv if k=='2026-08'])
print('M4 moves |>=2.7| incl this', sum(1 for k,v in mv if abs(v)>=D('2.7')),' excl this', sum(1 for k,v in mv if abs(v)>=D('2.7') and k!='2026-08'))
absv=sorted(abs(v) for k,v in mv); print('M4 mean abs',float(sum(absv)/len(absv)),'median',absv[len(absv)//2] if len(absv)%2 else (absv[len(absv)//2-1]+absv[len(absv)//2])/2)
SM=dict(sm)
for y in ['2024','2025','2026']: print('M4 SMI',y,'Jun',SM.get(y+'-06'),'Jul',SM.get(y+'-07'),'Aug',SM.get(y+'-08'))
# Q9 near 41.0
print('M5 national months within 0.5 of 41.0',[(k,str(v[0])) for k,v in N.items() if abs(v[0]-D('41.0'))<=D('0.5')], 'any ==41.0', [k for k,v in N.items() if v[0]==D('41.0')])
print('M5 South/NE/MW Jul26',S['2026-07'][0],NE['2026-07'][0],R['Midwest']['2026-07'][0])
print('M6 Aug26 regional', {k:(str(R[k]['2026-08'][0]),str(R[k]['2026-08'][2])) for k in R}, 'national', str(N['2026-08'][0]), str(N['2026-08'][2]))
print('M6 regions returned', sorted(R))
nyJ=[N['2026-%s'%m][0]-N['2025-%s'%m][0] for m in ['01','02','03']]; nyA=[N['2026-%s'%m][0]-N['2025-%s'%m][0] for m in ['04','05','06','07','08']]
print('M3 national yoy Jan-Mar avg %.2f Apr-Aug avg %.2f'%(sum(nyJ)/3,sum(nyA)/5))
