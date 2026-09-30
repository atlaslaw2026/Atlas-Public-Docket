#!/usr/bin/env python3.11
"""Compose CL-B's answer ONLY from approved_wording in ../magistrate/APPROVED_CLAIMS.json.
Order: claim_id order per question; render notes observed (Q7.X2 within Q7.3; Q7.X3 within Q7.8;
Q4.B1 -> Q4.1+Q4.2; Q9.B1 -> Q9.7+Q9.8). REJECTED claims are not rendered.
No connective words were needed; text is joined with spaces and paragraph breaks only."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
AP = json.load(open(os.path.join(HERE, "..", "magistrate", "APPROVED_CLAIMS.json")))
W = {c["claim_id"]: c for c in AP["claims"]}
OK = {"APPROVED", "APPROVED_AS_MODIFIED"}

# Paragraph plan: each paragraph is a list of "units"; a unit is (claim_ids_for_provenance, claim_id_whose_wording_is_rendered)
# Units flagged "join" are fragments of one sentence (Q4.4-Q4.8).
PLAN = {
 "Q1": [["Q1.1", "Q1.2", "Q1.3", "Q1.4", "Q1.5", "Q1.6"]],
 "Q2": [["Q2.1", "Q2.2", "Q2.3", "Q2.4"], ["Q2.5"], ["Q2.6"]],
 "Q3": [["Q3.1", "Q3.2", "Q3.3"], ["Q3.4", "Q3.5"], ["Q3.6", "Q3.7"]],
 "Q4": [["Q4.1", "Q4.2", "Q4.3"], ["Q4.4", "Q4.5", "Q4.6", "Q4.7", "Q4.8"], ["Q4.9", "Q4.10"]],
 "Q5": [["Q5.1", "Q5.2"], ["Q5.3"], ["Q5.4", "Q5.5"]],
 "Q6": [["Q6.1", "Q6.2", "Q6.3", "Q6.4"], ["Q6.5", "Q6.6"]],
 "Q7": [["Q7.1", "Q7.2", "Q7.3"], ["Q7.4", "Q7.5", "Q7.6"], ["Q7.7", "Q7.8", "Q7.9"], ["Q7.10"]],
 "Q8": [["Q8.1", "Q8.2"], ["Q8.3", "Q8.4", "Q8.5"], ["Q8.6", "Q8.7", "Q8.8", "Q8.9", "Q8.11", "Q8.12"], ["Q8.13"]],
 "Q9": [["Q9.1", "Q9.2", "Q9.3", "Q9.4", "Q9.5", "Q9.6"], ["Q9.7", "Q9.8", "Q9.9", "Q9.10"]],
}
EXTRA_PROV = {"Q7.3": ["Q7.X2"], "Q7.8": ["Q7.X3"]}  # render-within notes
FRAGMENT_GROUP = ["Q4.4", "Q4.5", "Q4.6", "Q4.7", "Q4.8"]
TITLES = {
 "Q1": "July national purchase intent", "Q2": "South vs. Northeast over the last 12 months",
 "Q3": "Holiday-quarter forecast and what's driving it", "Q4": "Replicating the forecast",
 "Q5": "Brand consideration since Northgate Rewards", "Q6": "Off-price vs. department stores this holiday season",
 "Q7": "The South's rise and the new store openings", "Q8": "Board deck: forecast, regions, and the August SMI",
 "Q9": "Your July national figure",
}
SPLIT = re.compile(r"(?<=[.?])\s+(?=[A-Z(\"])")

rendered = set()
md = ["# Answers for Northgate Outfitters", ""]
prov = []
for q, paras in PLAN.items():
    md += [f"## {q}. {TITLES[q]}", ""]
    for para in paras:
        texts = []
        for cid in para:
            c = W[cid]
            assert c["disposition"] in OK and c["approved_wording"], cid
            assert c["question_id"] == q, cid
            rendered.add(cid)
            texts.append(c["approved_wording"])
            if cid in FRAGMENT_GROUP:
                continue
            ids = [cid] + EXTRA_PROV.get(cid, [])
            for s in SPLIT.split(c["approved_wording"]):
                prov.append({"question_id": q, "sentence": s, "claim_ids": ids})
        if para == FRAGMENT_GROUP:
            sent = " ".join(W[c]["approved_wording"] for c in FRAGMENT_GROUP)
            prov.append({"question_id": q, "sentence": sent, "claim_ids": list(FRAGMENT_GROUP)})
        md += [" ".join(texts), ""]

# completeness checks
for c in AP["claims"]:
    cid = c["claim_id"]
    if c["disposition"] in OK and not c.get("render"):
        assert cid in rendered, f"approved claim not rendered: {cid}"
    if c["disposition"] == "REJECTED":
        assert cid not in rendered, cid
text = "\n".join(md).rstrip() + "\n"
# every provenance sentence appears verbatim; every body line is covered by provenance
for p in prov:
    assert p["sentence"] in text, p
body = " ".join(l for l in md if l and not l.startswith("#"))
assert body == " ".join(p["sentence"] for p in prov), "provenance does not cover the body exactly"
open(os.path.join(HERE, "FINAL_ANSWER.md"), "w").write(text)
json.dump(prov, open(os.path.join(HERE, "PROVENANCE.json"), "w"), indent=1, ensure_ascii=False)
print(f"rendered claims={len(rendered)} sentences={len(prov)}")
