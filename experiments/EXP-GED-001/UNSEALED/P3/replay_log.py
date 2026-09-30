#!/usr/bin/env python3
"""SEALED: replay an interface log request-for-request against another backend, preserving seq and ts_utc,
recomputing responses and the hash chain. Usage: replay_log.py <in_log> <out_log> <iface_dir>"""
import hashlib, json, os, subprocess, sys
def canon(o): return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
src, dst, iface = sys.argv[1:4]; prev = "0" * 64; out = []
tmp = dst + ".tmp"
for line in open(src):
    if not line.strip(): continue
    e = json.loads(line)
    if os.path.exists(tmp): os.remove(tmp)
    subprocess.run(["python3", f"{iface}/mcp.py", e["tool"], json.dumps(e["args"])], env={**os.environ, "MCP_LOG": tmp}, capture_output=True, check=True)
    r = json.loads(open(tmp).read().strip())
    n = {"seq": e["seq"], "ts_utc": e["ts_utc"], "client_id": r["client_id"], "tool": r["tool"], "args": r["args"], "response": r["response"], "response_sha256": r["response_sha256"], "prev_hash": prev}
    n["entry_hash"] = hashlib.sha256((prev + canon(n)).encode()).hexdigest(); prev = n["entry_hash"]; out.append(canon(n))
os.remove(tmp); open(dst, "w").write("\n".join(out) + "\n")
