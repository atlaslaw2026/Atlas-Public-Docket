#!/usr/bin/env python3
"""SEALED: build perturbed backend for the Phase 3 Magistrate validation test (see ANSWER_KEY_P3.md)."""
import base64, csv, io, json, math, sys, zlib
def rd(t): return list(csv.DictReader(io.StringIO(t)))
def wr(rows):
    s = io.StringIO(); w = csv.DictWriter(s, fieldnames=list(rows[0].keys()), lineterminator="\r\n"); w.writeheader(); w.writerows(rows); return s.getvalue()
def moe(p, n, deff=1.3): return round(1.96 * math.sqrt(deff * p * (1 - p) / n) * 100, 1)
be = json.loads(zlib.decompress(base64.b64decode(open(sys.argv[1], "rb").read())))
F = be["files"]; cells = rd(F["observations/survey_cells.csv"])
months = sorted({c["month"] for c in cells})
# v2: from 2025-06, each South cell tracks the Northeast cell of the same month and age, plus that age's
# pre-period (2024-01..2025-05) mean South-minus-Northeast offset. South's relative growth disappears.
idx = {(c["month"], c["region"], c["age_group"]): c for c in cells}
pct = lambda c: int(c["intenders"]) / int(c["n"])
off = {}
for a in {c["age_group"] for c in cells}:
    pre = [m for m in months if m < "2025-06"]
    off[a] = sum(pct(idx[(m, "South", a)]) - pct(idx[(m, "Northeast", a)]) for m in pre) / len(pre)
for c in cells:
    if c["region"] == "South" and c["month"] >= "2025-06":
        target = pct(idx[(c["month"], "Northeast", c["age_group"])]) + off[c["age_group"]]
        c["intenders"] = str(round(int(c["n"]) * target))
F["observations/survey_cells.csv"] = wr(cells)
def agg(key):
    o = {}
    for c in cells:
        a = o.setdefault(key(c), [0, 0]); a[0] += int(c["n"]); a[1] += int(c["intenders"])
    return o
for fn, key in (("metrics/national_monthly.csv", lambda c: c["month"]), ("metrics/regional_monthly.csv", lambda c: (c["month"], c["region"])), ("metrics/age_monthly.csv", lambda c: (c["month"], c["age_group"]))):
    rows = rd(F[fn]); A = agg(key)
    for r in rows:
        k = r["month"] if fn.endswith("national_monthly.csv") else (r["month"], r["region"] if "region" in r else r["age_group"])
        n, x = A[k]; r["n"] = str(n); r["intent_pct"] = f"{round(100 * x / n, 1)}"; r["moe95_pts"] = f"{moe(x / n, n)}"
    F[fn] = wr(rows)
open(sys.argv[2], "wb").write(base64.b64encode(zlib.compress(json.dumps(be, sort_keys=True, ensure_ascii=False).encode(), 9)))
