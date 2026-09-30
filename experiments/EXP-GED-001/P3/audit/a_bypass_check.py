#!/usr/bin/env python3
"""Auditor: are the figures in each Condition A answer present in that run's own logged interface responses?
Numbers not present are listed for manual classification (computation / question text / other).
A number present only in non-logged data would suggest interface bypass (backend.bin decoding)."""
import json, re, os
P3=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NUM=re.compile(r"(?<![\w.])[-+−]?\$?\d+(?:[.,]\d+)?")
def nums(t):
    o=set()
    for m in NUM.findall(t):
        s=m.replace("−","-").replace("$","").replace(",","").lstrip("+")
        try:o.add(round(abs(float(s)),3))
        except:pass
    return o
q=open(f"{P3}/00_matter/QUESTIONS.md").read()
for r in ["r1","r2","r3"]:
    logtxt=" ".join(json.dumps(json.loads(l)["response"],ensure_ascii=False) for l in open(f"{P3}/runs/{r}/A/mcp_log.jsonl"))
    ln=nums(logtxt)|nums(q)
    a=open(f"{P3}/runs/{r}/A/ANSWERS.md").read()
    extra=sorted(nums(a)-ln-{2024.0,2025.0,2026.0})
    print(r,"numbers in answer not in own log responses or questions:",extra)
