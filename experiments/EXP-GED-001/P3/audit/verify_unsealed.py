#!/usr/bin/env python3
"""Auditor stage 2: verify UNSEALED/ files against the three pre-registrations (parsed, not transcribed),
and check that each pre-registration's hash lines are unchanged since the commit that introduced them."""
import re, hashlib, os, subprocess
E="/home/user/Atlas-Public-Docket/experiments/EXP-GED-001"
pre={"P1":"00_matter/PREREGISTRATION.md","P2":"P2/00_matter/PREREGISTRATION.md","P3":"P3/00_matter/PREREGISTRATION.md"}
def h(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
for ph,pf in pre.items():
    txt=open(f"{E}/{pf}").read()
    rows=re.findall(r"^\|\s*([^|`]+?)\s*(?:\([^|]*\))?\s*\|\s*`([0-9a-f]{64})`",txt,re.M)
    print(f"== {ph} ({pf}): {len(rows)} hashed rows")
    for name,hh in rows:
        name=name.strip().split(" ")[0]
        f=f"{E}/UNSEALED/{ph}/{os.path.basename(name)}"
        alt={"CL-B_perturbed":f"{E}/UNSEALED/P2/CL-B_perturbed.sha256"}
        if not os.path.exists(f):
            f=alt.get(name, f)
        if os.path.exists(f): print(f"   {name:45} {'MATCH' if h(f)==hh else 'MISMATCH '+h(f)[:16]}")
        else: print(f"   {name:45} (not an unsealed file; served/other)")
    # history of prereg hash lines
    log=subprocess.run(["git","-C",E,"log","--format=%h","--",pf],capture_output=True,text=True).stdout.split()
    first=log[-1]
    old=subprocess.run(["git","-C",E,"show",f"{first}:experiments/EXP-GED-001/{pf}"],capture_output=True,text=True).stdout
    oh=set(re.findall(r"[0-9a-f]{64}",old)); nh=set(re.findall(r"[0-9a-f]{64}",txt))
    print(f"   commits touching prereg: {log}; hashes removed since first commit {first}: {sorted(oh-nh)}; added: {len(nh-oh)}")
for f in ["P1/bridge_study_2026-02_PERTURBED.csv","P1/dataroom_manifest_sha256.txt","P3/replay_log.py"]:
    print("not pre-registered (by name):",f,h(f"{E}/UNSEALED/{f}")[:16])
