#!/bin/sh
# Auditor: independent hash recomputation (store, interface copies, harness, pre-registered served files)
set -u
P3=/home/user/Atlas-Public-Docket/experiments/EXP-GED-001/P3
echo "== store vs STORE_MANIFEST =="
cd /home/user/enterprise_store && sha256sum -c $P3/00_matter/STORE_MANIFEST.sha256
echo "== store: files not in manifest =="
find . -type f | sort > /tmp/_st; awk '{print $2}' $P3/00_matter/STORE_MANIFEST.sha256 | sort | diff - /tmp/_st && echo none
ls -la --time-style=full-iso -R /home/user/enterprise_store | head -60
echo "== harness vs INTERFACE_MANIFEST =="
cd $P3/harness && sha256sum -c $P3/00_matter/INTERFACE_MANIFEST.sha256
for d in /home/user/p3_iface_r1 /home/user/p3_iface_r2 /home/user/p3_iface_r3 /home/user/p3_iface_r4; do
  echo "== $d =="; ls -la $d; (cd $d && sha256sum *)
done
echo "== pre-registered served files =="
cd $P3/00_matter && sha256sum STORE_MANIFEST.sha256 INTERFACE_MANIFEST.sha256 QUESTIONS.md authorization_policy.json MATTER.md INTERFACE_SPEC.md prompts/*.md
