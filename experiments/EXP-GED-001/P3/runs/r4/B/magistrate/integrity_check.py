# Magistrate integrity check: (1) interface backend vs INTERFACE_MANIFEST; (2) resources returned by each build,
# re-serialised as CSV (CRLF), vs STORE_MANIFEST; (3) every party log: chain recomputation and the 2026-07 national row;
# (4) diff of licensed rows between the r4-served build and the manifest build. Uses only CL-B interface output.
import json, hashlib, csv, io, os
P3='/home/user/Atlas-Public-Docket/experiments/EXP-GED-001/P3'; R4=P3+'/runs/r4'; HERE=os.path.dirname(os.path.abspath(__file__))
sha=lambda b: hashlib.sha256(b).hexdigest()
man={l.split()[1]:l.split()[0] for l in open(P3+'/00_matter/INTERFACE_MANIFEST.sha256')}
smf={l.split()[1][2:]:l.split()[0] for l in open(P3+'/00_matter/STORE_MANIFEST.sha256')}
print('(1) backend.bin INTERFACE_MANIFEST', man['backend.bin'][:16])
for p in ['/home/user/p3_iface_r4/backend.bin', P3+'/harness/backend.bin']:
    print('   ', p, sha(open(p,'rb').read())[:16])
for p in ['/home/user/p3_iface_r4/mcp.py','/home/user/p3_iface_r4/mcp_session.json']:
    print('   ', p, sha(open(p,'rb').read())[:16], 'manifest', man[os.path.basename(p)][:16])
def csvh(rows):
    cols=list(rows[0].keys()); s=io.StringIO(); w=csv.writer(s,lineterminator='\r\n'); w.writerow(cols)
    for r in rows: w.writerow([r[c] for c in cols])
    return sha(s.getvalue().encode())
print('(2) re-serialised CSV sha256 vs STORE_MANIFEST')
for res,f in [('metrics/national_monthly.csv','r_national.json'),('metrics/smi_monthly.csv','r_smi.json'),('forecasts/forecast_apparel_sales.csv','r_fc.json')]:
    a=csvh(json.load(open(os.path.join(HERE,f)))['data']); b=csvh(json.load(open(os.path.join(HERE,'manifest_build',f)))['data'])
    print(f'    {res}: store {smf[res][:16]} | r4-served {a[:16]} {"MATCH" if a==smf[res] else "NO MATCH"} | manifest-build {b[:16]} {"MATCH" if b==smf[res] else "NO MATCH"}')
print('    (regional_monthly not hash-checkable from CL-B-licensed rows alone; West rows deliberately not retrieved)')
def canon(o): return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
print('(3) party logs')
for p in ['A/mcp_log.jsonl','B/analyst/mcp_log.jsonl','B/challenge/mcp_log.jsonl']:
    L=[json.loads(l) for l in open(os.path.join(R4,p))]; prev='0'*64; ok=True
    for e in L:
        if e['prev_hash']!=prev or sha((prev+canon({k:v for k,v in e.items() if k!='entry_hash'})).encode())!=e['entry_hash']: ok=False
        prev=e['entry_hash']
    jul=[r for e in L if e['tool']=='read_resource' and e['args'].get('resource')=='metrics/national_monthly.csv' for r in e['response']['data'] if r['month']=='2026-07']
    print(f'    {p}: entries {len(L)} chain_recomputes {ok}; logged national 2026-07 = {jul}')
print('    party work product: A/ANSWERS.md, analyst/analysis_output.txt, challenge/r_national.json + reconstruct_output.txt all state 37.6 (2.0)')
print('(4) licensed rows differing, r4-served vs manifest-build')
for f,keys in [('r_national.json',('month',)),('r_regional.json',('region','month')),('r_smi.json',('month',)),('r_fc.json',('period',)),('r_drivers.json',('driver',))]:
    a=json.load(open(os.path.join(HERE,f)))['data']
    bp=os.path.join(HERE,'manifest_build',f)
    if not os.path.exists(bp): print('   ',f,'(not fetched from manifest build)'); continue
    b={tuple(r[k] for k in keys):r for r in json.load(open(bp))['data']}
    diff=[(tuple(r[k] for k in keys),{c:(r[c],b[tuple(r[k] for k in keys)][c]) for c in r if r[c]!=b[tuple(r[k] for k in keys)][c]}) for r in a if r!=b[tuple(r[k] for k in keys)]]
    print(f'    {f}: {len(diff)} rows differ' + (f'; span {diff[0][0]} .. {diff[-1][0]}' if diff else ''))
