#!/usr/bin/env python3
"""Auditor: r2 Magistrate could not read CLAIM_LEDGER.json. Check claim-id -> content mapping:
compare, per id, the ledger's a_text/proposed_wording with the Magistrate's approved_wording/reason."""
import json, difflib, os
P3=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L={c["claim_id"]:c for c in json.load(open(f"{P3}/runs/r2/B/analyst/CLAIM_LEDGER.json"))["claims"]} if isinstance(json.load(open(f"{P3}/runs/r2/B/analyst/CLAIM_LEDGER.json")),dict) else {c["claim_id"]:c for c in json.load(open(f"{P3}/runs/r2/B/analyst/CLAIM_LEDGER.json"))}
M={c["claim_id"]:c for c in json.load(open(f"{P3}/runs/r2/B/magistrate/APPROVED_CLAIMS.json"))["claims"]}
def sim(a,b): return difflib.SequenceMatcher(None,(a or "").lower(),(b or "").lower()).ratio()
low=[]
for k in sorted(L, key=lambda x:(x.split('.')[0],x)):
    l=L[k]; m=M.get(k,{})
    ref=(l.get("proposed_wording") or l.get("statement") or l.get("a_text") or "")
    s=max(sim(ref,m.get("approved_wording")), sim(l.get("a_text"),m.get("approved_wording")), sim(l.get("statement"),m.get("approved_wording")))
    if s<0.45: low.append((round(s,2),k,m.get("disposition"),(l.get("a_text") or l.get("statement"))[:90],str(m.get("approved_wording"))[:90]))
print("r2 ids:",len(L),"ruled:",len(set(L)&set(M)))
print("low-similarity pairs (ledger text vs Magistrate wording) — inspect manually:")
for x in sorted(low): print("  ",x)
