#!/usr/bin/env python3
"""Auditor: independent provenance tracer (stricter than gate.py G2/G3).
For each governed run: (a) every provenance sentence occurs verbatim in FINAL_ANSWER.md; (b) provenance sentences
cover the answer body (non-heading text); (c) every cited claim is APPROVED*; (d) the sentence's wording is
drawn from the cited claims' approved_wording (token overlap; words not in cited wording listed);
(e) every number in the sentence appears in the approved wording of THE CITED claims (not merely anywhere).
Then samples sentences and prints sentence -> claim -> evidence pointer for manual tracing to the store."""
import json, re, os, random, difflib
P3=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NUM=re.compile(r"(?<![\w.])[-+−]?\$?\d+(?:[.,]\d+)?")
def nums(t):
    o=set()
    for m in NUM.findall(t):
        s=m.replace("−","-").replace("$","").replace(",","").lstrip("+")
        try:o.add(round(abs(float(s)),3))
        except:pass
    return o
W=re.compile(r"[A-Za-z]+")
def norm(s): return re.sub(r"\s+"," ",s.replace("’","'").replace("**","")).strip()
cfg={"r1":("PROVENANCE.json",["APPROVED_CLAIMS.json"]),"r2":("PROVENANCE_v2.json",["APPROVED_CLAIMS.json","APPROVED_CLAIMS_CORRECTION_1.json"]),"r3":("PROVENANCE.json",["APPROVED_CLAIMS.json"])}
random.seed(20260930)
for r,(pv,acs) in cfg.items():
    B=f"{P3}/runs/{r}/B"; fa=open(f"{B}/final/FINAL_ANSWER.md").read(); fan=norm(fa)
    prov=json.load(open(f"{B}/final/{pv}"))
    claims={}
    for a in acs:
        d=json.load(open(f"{B}/magistrate/{a}")); 
        for c in d["claims"]: claims[c["claim_id"]]=c
    appr={k:c for k,c in claims.items() if c["disposition"].startswith("APPROVED")}
    rej_words={k:c.get("approved_wording","") for k,c in claims.items() if not c["disposition"].startswith("APPROVED")}
    print(f"===== {r}: {len(prov)} provenance sentences; {len(appr)} approved claims")
    notin=[p["sentence"] for p in prov if norm(p["sentence"]) not in fan]
    print(" (a) sentences not found verbatim in answer:", len(notin), notin[:3])
    body=fan
    for p in sorted(prov,key=lambda p:-len(p["sentence"])): body=body.replace(norm(p["sentence"]),"")
    body=re.sub(r"#+ [^#]*?(?=\s[A-Z]|$)","",body)  # rough heading strip
    left=[l for l in [norm(x) for x in fa.splitlines()] if l and not l.startswith("#")]
    uncovered=[]
    for l in left:
        t=l
        for p in prov: t=t.replace(norm(p["sentence"]),"")
        t=re.sub(r"^[-*\d.\s|]+","",t).strip(" -|:")
        if len(W.findall(t))>2: uncovered.append(t)
    print(" (b) answer text not covered by any provenance sentence:", uncovered if uncovered else "none")
    bad_ids=[(p["sentence"][:50],i) for p in prov for i in p["claim_ids"] if i not in appr]
    print(" (c) cited ids not approved:", bad_ids if bad_ids else "none")
    unused=[k for k in appr if not any(k in p["claim_ids"] for p in prov)]
    print("     approved claims never cited:", unused)
    numfail=[]; wordfail=[]; weak=[]
    for p in prov:
        cw=" ".join(appr[i].get("approved_wording","") for i in p["claim_ids"] if i in appr)
        extra=nums(p["sentence"])-nums(cw)-{2024.0,2025.0,2026.0}
        if extra: numfail.append((p["sentence"][:90],p["claim_ids"],sorted(extra)))
        sw=[w.lower() for w in W.findall(p["sentence"])]; cwset={w.lower() for w in W.findall(cw)}
        miss=[w for w in sw if w not in cwset]
        ratio=difflib.SequenceMatcher(None,norm(p["sentence"]).lower(),norm(cw).lower()).find_longest_match(0,len(norm(p["sentence"])),0,len(norm(cw))).size/max(1,len(norm(p["sentence"])))
        if norm(p["sentence"]) not in norm(cw): weak.append((round(ratio,2),p["sentence"][:80],p["claim_ids"],miss[:12]))
    print(" (e) sentences with numbers absent from their OWN cited claims' approved wording:", len(numfail))
    for x in numfail: print("     ",x)
    print(" (d) sentences not a verbatim substring of their cited approved wording:", len(weak))
    for x in sorted(weak)[:40]: print("     ",x)
    # rejected wording surfacing?
    for k,w in rej_words.items():
        if w and len(w)>25 and norm(w) in fan: print("  !! REJECTED claim wording appears in answer:",k,w[:80])
    print(" SAMPLE trace (6 random sentences):")
    for p in random.sample(prov,6):
        print("   S:",p["sentence"][:140])
        for i in p["claim_ids"]:
            c=claims.get(i,{}); print(f"     -> {i} [{c.get('disposition')}/{c.get('class')}/{c.get('j0001_label')}] ev: {str(c.get('evidence'))[:200]}")
