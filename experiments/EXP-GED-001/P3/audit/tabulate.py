#!/usr/bin/env python3
"""Auditor: join each run's Analyst CLAIM_LEDGER with the Magistrate's APPROVED_CLAIMS (+corrections);
tabulate truth/access flags on A-sourced claims and what happened to them."""
import json, collections, os, sys
P3=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for r in ["r1","r2","r3","r4"]:
    B=f"{P3}/runs/{r}/B"
    led=json.load(open(f"{B}/analyst/CLAIM_LEDGER.json")); led=led["claims"] if isinstance(led,dict) else led
    ap=json.load(open(f"{B}/magistrate/APPROVED_CLAIMS.json"))["claims"]
    cor=f"{B}/magistrate/APPROVED_CLAIMS_CORRECTION_1.json"
    if os.path.exists(cor):
        c=json.load(open(cor)); ap+= c["claims"] if "claims" in c else []
    A={c["claim_id"]:c for c in ap}; Lg={c["claim_id"]:c for c in led}
    print(f"===== {r}: ledger {len(Lg)} claims; magistrate {len(A)} entries; dispositions {collections.Counter(c['disposition'] for c in ap)}")
    print("  ids in ledger not ruled:", sorted(set(Lg)-set(A)), " ruled not in ledger:", sorted(set(A)-set(Lg)))
    print("  ledger source x truth:", collections.Counter((c.get('source'),c.get('truth')) for c in led))
    print("  ledger access != AUTHORIZED:", [(c['claim_id'],c['access'][:60]) for c in led if not str(c.get('access','')).startswith('AUTHORIZED')])
    print("  A-sourced claims with truth not in {SUPPORTED,PREDICTION} or disposition != KEEP (ledger), and Magistrate outcome:")
    for c in led:
        if c.get("source")!="A": continue
        t=c.get("truth"); d=c.get("proposed_disposition")
        m=A.get(c["claim_id"],{})
        if t not in ("SUPPORTED","PREDICTION") or d!="KEEP" or m.get("disposition")!="APPROVED":
            print(f"   {c['claim_id']:7} truth={t:15} analyst={d:10} mag={m.get('disposition','-'):20} m.truth={str(m.get('truth'))[:18]:18} | {c.get('a_text','')[:90]!r}")
