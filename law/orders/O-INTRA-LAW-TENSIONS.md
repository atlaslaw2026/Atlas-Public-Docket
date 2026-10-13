# MAGISTRATE DISPOSITION — The Two Intra-Law Tensions

**Magistrate:** Vested Magistrate under O-VESTED-MAGISTRATE (2026-09-28), on the Human's referral of 2026-10-12 ("She's the judge, have her rule").
**Questions referred:** (1) TRACE.md:13's rewrite exception vs. PUB-M-011's no-rewrite holding — which controls; (2) the scope of the no-rewrite rule going forward.
**Status:** Filed 2026-10-12 on the Human's direction ("these need to go in orders not matters"). Content approved by the Human for filing.
## Evidence examined directly

- `docket/TRACE.md` in full — line 13: "Do not rewrite authentic history merely to make a timeline prettier. The exception is a documented secret/PII incident (see PUB-M-005)."
- Constitution Art. VIII §5, full text: "Historical filings shall not be rewritten **to make later doctrine appear as though it always existed**. Supersession is by later filing and pointer, not by editing the superseded text."
- `law/orders/O-PRIVACY-PRE-PUBLICATION-DUTY.md` in full, including §8(3) ("NO history rewrite is ordered — and Atlas law forbids it... the superseding scrub commit is the constitutionally prescribed remedy"), §9 (the no-rewrite holding binds "within this matter's scope"), and the Human's SO ORDERED action.
- `docket/MATTERS.md` PUB-M-005 row: "Reachable git history of this repository rewritten so the old path is not on `master`" — a history rewrite actually performed, closed, verified.
- `docket/MATTERS.md` PUB-M-011 row and the O-GATE-ACTIVATION-REFERRED-QUESTION disposition (procedural posture: these tensions left for separate determination).
- Git examination, this session **(KNOWN):** commit `4a9ca21` — the PUB-M-011 offending commit carrying the two private full names — **is an ancestor of master**. The scrub commit remediated the working tree at HEAD only; the names remain in the public repo's reachable history and downloadable by anyone who clones it.

## QUESTION 1 — the rewrite exception

**Argument (TRACE.md:13's exception controls).** The constitutional text is narrower than PUB-M-011's reading of it: it forbids rewriting *to make later doctrine appear as though it always existed* — the evil named is falsification, not remediation. A documented PII purge falsifies nothing. Precedent exists and stands: PUB-M-005 rewrote reachable history and closed verified, and TRACE.md:13 states the exception as docket practice. And the supersession-only remedy is technically hollow for secrets — KNOWN, the names are still in the public object store today. A rule that forbids the only effective remedy makes the docket's own privacy law (Rule 4, PRIVATE_EVIDENCE_POLICY) unenforceable against the history everyone downloads. Clinton's "amended, never erased" principle governs wrong *entries* — doctrine and findings — not exposure incidents, which are a different category.

**Counterargument (PUB-M-011's no-rewrite holding controls).** Hierarchy: PUB-M-011 is a Human Order, SO ORDERED — it outranks docket guidance (TRACE.md) and a single matter's implementation row (PUB-M-005). The docket-of-mistakes principle depends on the flawed filing remaining examinable: PUB-M-011's breach finding *requires* `4a9ca21` to exist as filed; purging it erases the evidence of the breach itself. A docket that rewrites its embarrassments is a brochure. Rewrite is also unreliable — public clones may already exist — so purging buys false assurance at the price of the evidentiary record. And PUB-M-005 is distinguishable: a workstation path was never authentic doctrinal history; the filed order body was.

**Resolution.** The constitutional text is the tiebreaker, and it decides the question: the prohibition targets *falsifying* rewrites. Both precedents survive under it. PUB-M-005's rewrite falsified nothing — it was openly recorded in the matter row, and a local file path is not doctrine. PUB-M-011 correctly refused to purge *filed decisional substance* — the order as rendered, breach included — because the docket's integrity depends on the flawed filing remaining examinable; its own §9 scopes that holding to the matter. What the constitutional text does not support is extending PUB-M-011's refusal into a blanket ban on purging secrets from the object store: the text doesn't say that, PUB-M-005 did the opposite and stands, and the KNOWN continued exposure shows a ban would leave privacy law with no effective remedy. The two authorities are therefore reconciled, not ranked: falsifying rewrite is forbidden; documented remediation is permitted.

## QUESTION 2 — scope of the no-rewrite rule

**Argument (broad: binds both records, all commits).** Anti-falsification is classified a foundational principle; the private canonical record is the authoritative one, so silently falsifying it would be worse, not more permissible. Clinton's "recall in kind" fallback — rebuild from the verbatim record of what was actually said — depends on the record being verbatim.

**Counterargument (narrow: public repo only).** TRACE.md explicitly scopes its history rule to "this repository" and distinguishes it from "the private operational git history." The Human is the sole authority over his private record, and no referred text extends Art. VIII §5's mechanism to private git history.

**Resolution.** The public docket repo's entire git history is bound — initial filing commits, follow-up commits, and corrective supersessions alike. Each is authentic history; the chain must remain examinable end to end, so a correction is itself corrected only by further supersession, never by editing. The anti-falsification principle extends to the private canonical record as a foundational matter — the authoritative record must not be silently falsified — but the private record's amendment *procedure* is not supplied by the referred record. Until the Human defines it, the safe posture is the same supersession discipline, and no silent rewrite of either record.

## HOLDINGS

**1.** Art. VIII §5 forbids rewriting history *in a way that falsifies the record* — doctrine, findings, judgments, and the fact of what was filed may not be made to appear otherwise than they were. **TRACE.md:13's exception stands**, conditioned as follows: a purge of secrets/PII from the git object store is permitted when (a) it is openly entered in the docket record — what was purged, why, when, by whose authority, on the PUB-M-005 model; (b) it alters no finding, holding, or the fact of what was filed; (c) it is limited to the secret/PII material itself; and (d) it has the Human's per-incident content approval — the agent may never purge unilaterally (Art. XVI; audit D-privacy-audit recommendation). **PUB-M-011's no-rewrite holding stands** for filed decisional substance within its matter's scope: a filed order, including the breach it evidences, may not be purged to make the breach appear never to have happened. The superseding commit remains the required remedy for the docket's working state and for all doctrinal corrections.

**2.** The no-rewrite rule, as conditioned in Holding 1, binds the whole of the public docket repo's git history — initial filings, follow-ups, and corrective supersessions. The anti-falsification principle extends to the private canonical record; its amendment procedure is the Human's to define, and until he does, supersession discipline applies there too, with no silent rewrites of either record.

## WHAT REMAINS UNDECIDED, AND WHOSE IT IS

1. **Whether to apply the conditioned purge to the still-exposed PUB-M-011 names.** KNOWN: the two private names remain in the public repo's reachable history today. The supersession-only remedy the Human approved stands and the matter is closed; this disposition does not reopen it. Any purge is the Human's per-incident decision under Holding 1(d).
2. **The private canonical record's amendment procedure.** The Human's to define.
3. **Gate activation.** Not decided here — still held pending the Count 3 prerequisites in O-GATE-ACTIVATION-REFERRED-QUESTION.

*Rendered by the Vested Magistrate, 2026-10-12, on the Human's referral. Argument and Counterargument heard on each question; evidence examined directly; J-0001 discipline applied. This is the adjudication ordered, not a simulation. Filed 2026-10-12 on the Human's direction.*
