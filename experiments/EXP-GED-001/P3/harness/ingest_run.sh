#!/usr/bin/env bash
# Ingest Condition A run N from its branch into P3/runs/rN/A (verbatim), then compute B/access.
set -euo pipefail
N=$1; R=/home/user/Atlas-Public-Docket; P3=$R/experiments/EXP-GED-001/P3; BR=origin/exp-ged-001-p3-a-r$N; BASE=origin/exp-ged-001-p3-interface
cd $R; git fetch -q origin exp-ged-001-p3-a-r$N exp-ged-001-p3-interface
mkdir -p $P3/runs/r$N/A $P3/runs/r$N/B/access
for f in ANSWERS.md AUDIT.md mcp_log.jsonl; do git show $BR:$f > $P3/runs/r$N/A/$f; done
{ echo "branch: exp-ged-001-p3-a-r$N"; echo "commit: $(git rev-parse $BR)"; echo "commit_time: $(git log -1 --format=%cI $BR)";
  echo "files changed vs interface branch:"; git diff --name-status $BASE $BR | sed 's/^/  /';
  echo "sha256:"; (cd $P3/runs/r$N/A && sha256sum ANSWERS.md AUDIT.md mcp_log.jsonl | sed 's/^/  /'); } > $P3/runs/r$N/A/SOURCE.txt
python3 $P3/harness/access_boundary.py $P3/00_matter/authorization_policy.json $P3/runs/r$N/A/mcp_log.jsonl > $P3/runs/r$N/B/access/ACCESS_DETERMINATION.json
python3 -c "import json;d=json.load(open('$P3/runs/r$N/B/access/ACCESS_DETERMINATION.json'));print('r$N chain_ok',d['chain_ok'],d['summary'])"
cat $P3/runs/r$N/A/SOURCE.txt | sed -n 4,9p
