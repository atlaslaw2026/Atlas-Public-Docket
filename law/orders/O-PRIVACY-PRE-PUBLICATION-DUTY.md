# O-PRIVACY-PRE-PUBLICATION-DUTY

**Filing type:** HUMAN ORDER (on Magistrate disposition)
**Status:** BINDING (Human-approved 2026-10-12; privacy-scrubbed per PRIVATE_EVIDENCE_POLICY)
**Date:** 2026-10-12
**Title:** Order on the Pre-Publication Privacy Duty

**Privacy:** Private individual identifiers in this matter are `PRIVATE_RETAINED` — reviewed by the Magistrate, not published here. Role descriptors ("a recruiter," "a client") are used throughout.

## I. REFERRAL

On 2026-10-12 the Human referred to the Vested Magistrate (O-VESTED-MAGISTRATE, 2026-09-28, BINDING) the question whether the invoking agent breached Atlas law by publishing two private individuals' full real names to the public docket (order O-DELIVERY-READINESS-VERIFICATION, commit 4a9ca21) without first consulting the docket's privacy rules — and how the tension between verbatim publication of Magistrate rulings and privacy scrubbing is to be resolved.

## II. DISPOSITION (VERBATIM)

The Magistrate's ruling is published as rendered. No authority exists to alter it before publication.

---

# MAGISTRATE DISPOSITION — Vested Magistrate under O-VESTED-MAGISTRATE (second matter)

**Magistrate instance:** Subagent session `593610c9-515b-4f15-a4c1-1b7ed825c346`, instantiated 2026-10-12 as Magistrate for this matter, which is distinct from the 2026-10-12 delivery-readiness adjudication (closed). This decision was made by this instance on the evidence below, not by the invoking agent and not by deterministic code.

## 1. Matter adjudicated

Whether the invoking agent breached Atlas law by publishing two private individuals' full real names to the PUBLIC docket (order O-DELIVERY-READINESS-VERIFICATION, commit 4a9ca21, 2026-10-12 14:51 PDT) without first consulting the docket's own privacy rules — and how the tension between verbatim publication of Magistrate rulings and privacy scrubbing is to be resolved going forward.

## 2. Propositions decided

(a) Was the initial publication with real names a breach of Atlas law, and if so, of what specifically?
(b) How is the verbatim-publication vs. privacy-scrubbing tension resolved going forward — and is a standing rule warranted?
(c) Any further disposition warranted.

## 3. Evidence actually considered

I examined the following directly; I did not rely on the referral's summaries alone:

- **`~/workspace/atlas-docket/law/orders/O-VESTED-MAGISTRATE.md`** — read in full. My vesting authority; §§ I–IV, VII, IX applied.
- **`~/workspace/atlas-docket/docket/PRIVATE_EVIDENCE_POLICY.md`** — read in full. The operative prohibition: the public docket "must not carry... customer/client identifiers beyond what an Order deliberately publishes as public-safe caption."
- **`~/workspace/atlas-docket/AGENTS.md`** — read; the ordered reading list (J-0001 required, J-0002, Constitution) and the J-0001 labeling duty.
- **`~/workspace/atlas-docket/law/judgments/J-0001.json`** and **`J-0002.json`** — read in full. J-0001: label every material claim; never promote INFERRED to KNOWN. J-0002: an agent must not convert a material unanswered question into an implementation assumption; investigate first, ask if still unknown.
- **Constitution, `~/workspace/atlas-docket/law/constitution/ATLAS_CONSTITUTION.md`** — Art. VIII §5 (no rewriting of historical filings; supersession by later filing and pointer), Art. XII (uncertainty), Art. XIV (evidence; "it ran" is not "it worked"), Art. XVI (external effects need operative authority at the time of the act).
- **The published order at commit `4a9ca21`** — examined via `git show`: contained two private full names ×2 each in the order body, including inside the carried Magistrate disposition. **KNOWN.**
- **The scrubbed order at HEAD (`3927f6b`)** — examined via grep: zero hits for either name; role-based descriptors ("a recruiter," "a client") plus one `[REDACTED]` filename. **KNOWN.**
- **Commit timestamps** — `4a9ca21` at 14:51:00 PDT, scrub commit `3927f6b` at 14:53:01 PDT: remediation within 2 minutes. **KNOWN.**
- **The Human's instructions and the agent's sequence** (approval "Just publish"; the Human's "no authority to change the ruling" statement; the agent reading the privacy policy only after the Human's flag "These are private and you need to scrub the names immediately"): **INFERRED from the undisputed referral record** — I did not independently verify chat timestamps; neither party disputes the sequence.
- **Whether any third party viewed or copied the names during the ~2-minute exposure window:** **UNKNOWN** — no evidence either way; the repo is public, so exposure was possible but unproven.

## 4. Governing authorities actually applied

- **PRIVATE_EVIDENCE_POLICY.md** — the direct prohibition, applied as the primary substantive law.
- **J-0002** — the investigative duty: the privacy policy was available evidence bearing directly on the publication act, in the same docket tree the agent was filing into; the agent did not consult it before acting.
- **O-VESTED-MAGISTRATE** (§§ I–IV, VII, IX) — jurisdiction, independence, provenance; notably, it vests the Magistrate superior to the *invoking agent*, not superior to the Human's standing docket law.
- **Art. XVI** — the push itself was Human-authorized ("Just publish"); no execution-authority breach.
- **Art. VIII §5** — decisive for the history question (see §8).
- **Art. XIV §3 / J-0001** — labeling discipline applied throughout this disposition.

## 5. Material Argument and Counterargument, and the weight given

**Argument (breach):** The agent published real private names to a public repository without ever opening the docket's own privacy policy — which exists precisely for this and sits in the same directory tree being filed into. A governed agent checks publication rules before publishing, especially where the Human's approval went to the order's substance ("I want to see the order online to read it"), not to a waiver of privacy law. The agent had the means and the duty and used neither until the Human caught the violation. "Publish verbatim" cannot excuse it: verbatim holdings and privacy scrubbing are reconcilable, and standing policy outranks filing convenience.

**Counterargument (no breach):** The agent executed the Human's explicit, specific instruction to publish the Magistrate's ruling unaltered — the Human himself declared he had "no authority to change the ruling before it is published," and the agent had just been told the ruling "publishes as the Magistrate wrote it, not as anyone prefers it." The names arrived via the Human's own referral and the Magistrate's own disposition; the agent introduced no private fact the record didn't already contain. Remediation came within minutes of the flag, before any evidence of downstream harm. The conflict was between two genuine duties, resolved correctly once surfaced.

**Weight given:** The Argument prevails on the core question, but the Counterargument carries real mitigating weight. The decisive point: the conflict the agent faced was genuine, but it was *resolvable before publication* — and Atlas law (J-0002) prescribes exactly how: when a material question ("does standing privacy law permit these identifiers on the public docket?") cannot be answered from the instructions alone, investigate, then ask. The agent did neither; it converted the question into the assumption that "publish unaltered" covered identifiers too. That is the same J-0002 failure pattern the prior Magistrate found in the delivery-readiness matter — an unasked material question silently assumed away.

Against full culpability: the Human's instruction was genuinely ambiguous on identifiers, the names were Human- and Magistrate-sourced (the agent originated nothing private), the push itself was authorized, and remediation took 2 minutes. This was a diligence failure under a conflicting instruction, not a willful publication.

One correction to the Counterargument's framing that matters for (b): the Human's "no authority to change the ruling" was the Human's own legal conclusion, and it spoke to the ruling's *substance* — its holdings, findings, and reasoning. Scrubbing identifiers alters none of that. O-VESTED-MAGISTRATE makes the Magistrate superior to the *invoking agent*; it does not strip the Human of authority over his own docket's standing privacy law, nor does "verbatim" reasonably mean character-identical reproduction of private identifiers. The two duties were reconcilable all along — which is why the failure to even check is the breach.

## 6. Findings

- **Breach — narrow and specific: breach of the pre-publication investigative duty.** **KNOWN** (by direct examination of both commits): the order as pushed at 14:51 carried two private full names to a public repo, in violation of PRIVATE_EVIDENCE_POLICY.md's explicit prohibition. **INFERRED** (from the undisputed record): the agent never consulted the policy before publishing. Under J-0002, the policy was available, directly applicable evidence; the material question of whether the "publish verbatim" instruction overrode it was never investigated and never asked. The Human's approval authorized the *act* of publishing, not the *content violation* — no privacy waiver was stated or implied, and a waiver of standing docket law would require an explicit one.
- **Not a breach of:** the verbatim-publication instruction (the ruling's substance was preserved intact); Art. XVI (execution authority was operative via the Human's approval); any duty to the data subjects beyond the policy itself (downstream viewing is UNKNOWN, and the agent originated no private fact).
- **Mitigation (material):** (1) genuinely conflicting Human instruction, ambiguous on identifiers; (2) names sourced from the Human's referral and the Magistrate's disposition, not introduced by the agent; (3) remediation in 2 minutes, before any evidence of downstream harm; (4) the agent's scrub (role-based descriptors + one `[REDACTED]` filename) was exactly the policy-correct remedy and is verified clean.
- **On (b):** the tension dissolves on inspection. "Publish the ruling as decided" and "carry no private identifiers" were never in conflict — scrubbing preserves every holding, finding, and line of reasoning. The standing rule is warranted, in the Human's short-and-sweet style, one sentence: **"A ruling goes up as decided — with private names left out."**

## 7. Reasoning

Publication is the publisher's act, and the publisher bears the duty to know the publication law. The docket's privacy policy is not obscure machinery — it is a short file in the very tree being filed into, and J-0002's investigative duty points straight at it. The agent's error was not malice and not disobedience; it was the familiar failure mode of this docket's recent history: treating an instruction's silence on a point as an answer to it. "Just publish" answered *whether* to publish, not *in what redacted form* — and the privacy policy already answered the second question for anyone who opened it. That said, culpability is bounded: the Human wrote the names into the record twice over (referral and approval of a disposition containing them) and ordered the ruling published unaltered, so the agent's wrong reading of an ambiguous instruction was not unreasonable on its face — it was merely unasked-about, and Atlas does not permit unasked material questions. Two minutes to remediation, with the constitutionally correct remedy (a superseding commit, not a rewrite), keeps this a diligence finding rather than a conduct one.

## 8. Disposition

1. **Breach found**, scoped as above: breach of the pre-publication investigative duty (PRIVATE_EVIDENCE_POLICY.md + J-0002). No broader breach.
2. **Remedy already executed and verified** — the scrubbed commit `3927f6b` is clean by direct examination. No further corrective act required of the invoking agent on the live files.
3. **On the lingering history question: NO history rewrite is ordered — and Atlas law forbids it.** Art. VIII §5: "Historical filings shall not be rewritten... Supersession is by later filing and pointer, not by editing the superseded text." A force-push purge of commit `4a9ca21` would itself violate the Constitution's no-rewrite principle. The superseding scrub commit is the constitutionally prescribed remedy, and it is already in place. The ~2-minute exposure window's actual viewership is UNKNOWN; the law does not authorize destroying the historical record to chase an unproven exposure.
4. **Standing rule proposed** (for the Human's content approval; takes effect only upon it), one sentence: **"A ruling goes up as decided — with private names left out."**
5. **Practice note (no new authority):** the invoking agent should fold a privacy check into pre-publication practice for docket filings — open PRIVATE_EVIDENCE_POLICY.md before any push to the public repo — just as the delivery-readiness rule now requires render-verification for generated artifacts.
6. No sanction beyond the finding itself; remediated in 2 minutes with the correct remedy, and the underlying ambiguity was genuine.

## 9. Authority granted or withheld

This Magistrate **grants no new standing authority** and **enacts no rule**. The proposed rule in §8(4) takes effect, if at all, only upon the Human's content approval through the normal order process. The invoking agent is **bound** by the breach finding and the Art. VIII §5 no-rewrite holding within this matter's scope, and is **withheld** from filing or pushing any order or docket entry on this matter — and from any force-push or history rewrite of the public repo — without the Human's content approval.

## 10. Lawful next actor and act

The **invoking agent** shall draft the order memorializing this disposition (including the proposed one-sentence rule) and seek the **Human's** content approval before any filing. No docket push, no repo commit, no history rewrite, and no external communication is authorized by this disposition.

**Labels on this disposition's own material claims:** the commit examinations, timestamps, and policy quotations are KNOWN (directly performed, methods stated); the Human's instructions, the agent's pre-publication sequence, and the absence of downstream harm are INFERRED from the undisputed referral record; any third-party viewing during the exposure window is UNKNOWN; the proposed rule's future effectiveness is UNKNOWN pending Human approval.

---

## III. HUMAN ACTION

The disposition above stands as rendered. The Human's authority on this filing is limited to: (a) approving or declining publication of the disposition as filed; (b) approving or declining the proposed standing rule in §8(4), which the Magistrate expressly left to the Human's content approval and which takes effect only upon that approval. The Magistrate further holds, under Art. VIII §5, that no history rewrite of the public repo is permitted — the superseding scrub commit stands as the constitutionally prescribed remedy.

**Human refinement of the proposed rule (2026-10-12):** the rule as proposed does not track the redacted identities. Refined text, in the Human's short-and-sweet style, one sentence: **"A ruling goes up as decided, with private names left out and tracked on the private record."** The private record retains the real identities keyed to the public order id, per PRIVATE_EVIDENCE_POLICY (`PRIVATE_RETAINED`).

SO ORDERED.
