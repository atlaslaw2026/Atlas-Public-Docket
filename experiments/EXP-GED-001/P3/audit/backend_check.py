#!/usr/bin/env python3
"""Auditor: (1) rebuild backend.bin from the read-only store and compare to served copies;
(2) decode each interface copy and diff its file contents against the store byte-for-byte;
(3) characterise the r4 perturbation."""
import base64, zlib, json, os, sys, hashlib, subprocess, tempfile, difflib
STORE="/home/user/enterprise_store"; P3="/home/user/Atlas-Public-Docket/experiments/EXP-GED-001/P3"
def dec(p): return json.loads(zlib.decompress(base64.b64decode(open(p,"rb").read())))
tmp=tempfile.mkdtemp()
subprocess.run([sys.executable, f"{P3}/harness/build_backend.py", STORE, tmp], check=True)
rb=open(f"{tmp}/backend.bin","rb").read()
print("rebuilt backend sha256:", hashlib.sha256(rb).hexdigest())
store={}
for root,_,fs in os.walk(STORE):
    for f in fs:
        p=os.path.relpath(os.path.join(root,f),STORE)
        if p!="README.md": store[p]=open(os.path.join(root,f),encoding="utf-8").read()
for d in ["harness"]+[f"r{i}" for i in range(1,5)]:
    path=f"{P3}/harness/backend.bin" if d=="harness" else f"/home/user/p3_iface_{d}/backend.bin"
    be=dec(path)
    diffs=[k for k in sorted(set(store)|set(be["files"])) if store.get(k)!=be["files"].get(k)]
    ref=dec(f"{tmp}/backend.bin")
    print(f"{d}: sha={hashlib.sha256(open(path,'rb').read()).hexdigest()[:16]} files_differing_from_store={diffs} catalog_same={be['catalog']==ref['catalog']} ctx_same={be['client_context']==ref['client_context']}")
    for k in diffs:
        for l in difflib.unified_diff(store.get(k,"").splitlines(), be["files"].get(k,"").splitlines(), lineterm="", n=0):
            print("   ", l)
