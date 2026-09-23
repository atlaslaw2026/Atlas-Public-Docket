# AGENTS.md — operating under public Atlas

For AI agents that arrive here with a task. Humans can start at [README.md](README.md).

## What Atlas is

Atlas is a governed AI/agent operating system. Work must rest on evidence, stay inside explicit authority, leave a durable record, and fail closed when authority or evidence is missing. This repository is its **public governance docket**: the rules and a sanitized record. It is not the software.

## Two things with the same name

| | PUBLIC ATLAS GOVERNANCE | PRIVATE ATLAS RUNTIME |
|---|---|---|
| What | Standards you can read and apply | Tools, records, and services Clinton's installation runs |
| Where | This repository | Not published |
| Examples | J-0001 labels, Constitution, Orders, docket format | `verify.py`, `python -m atlas_*`, `ATLAS_RECORD`, Librarian, Atlas Room, CLINTON_SDK / PERSONAL_CONTEXT, Magistrate engine, jobs, CURRENT_STATE |
| You | May adopt and apply them | Do not have them. Do not claim to |

**Operating under public Atlas means faithfully applying the published standards.** It does not mean copying Atlas vocabulary, and it never means reporting that you ran private machinery.

`ATLAS_FIRST_READ.md` and `CURRENT_LAW.md` are verbatim copies of the private runtime's own entry instructions. Their commands and file paths describe that runtime accurately. They are not steps a public agent can perform, and they are not prerequisites for applying the public standards.

## Read in this order

1. This file.
2. [law/judgments/J-0001.json](law/judgments/J-0001.json): epistemic labels. **Required.**
3. [law/judgments/J-0002.json](law/judgments/J-0002.json): material unknowns and the duty to ask.
4. [law/constitution/ATLAS_CONSTITUTION.md](law/constitution/ATLAS_CONSTITUTION.md), Articles XII (uncertainty), XIV (evidence), XVI (external effects), XVII (resource limits).
5. For source-based work: [O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION](law/orders/O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION.md) and [O-LIBRARIAN-SOURCE-ADMISSIBILITY](law/orders/O-LIBRARIAN-SOURCE-ADMISSIBILITY.md).
6. For output shape: [docket/TRACE.md](docket/TRACE.md) and one example in [docket/MATTERS.md](docket/MATTERS.md). Plain-English terms: [GLOSSARY.md](GLOSSARY.md).
7. Optional context: [ATLAS_FIRST_READ.md](ATLAS_FIRST_READ.md) (working method and Truth Discipline) and [CURRENT_LAW.md](CURRENT_LAW.md) (full authority stack). Read them as a description of the whole system, with the runtime steps in them treated as private.

This file summarizes and points. It is not law. Where it and the law differ, the law controls.

## When a rule depends on private machinery

1. **Say so plainly.** Name the step (for example: "`verify.py` canonical-index check: not available to a public agent; not run").
2. **Do not imply execution.** No "verified", "Librarian found", "Magistrate approved", or job/docket numbers you did not receive.
3. **Label what it would have established.** Mark it UNKNOWN (J-0001). If the answer is material under J-0002 and your task depends on it, it becomes USER_CONFIRMATION_REQUIRED: ask your user.
4. **Keep working on what does not depend on it.** An unavailable tool is a resource limit, not exhaustion (Constitution Art. XVII). Use the public substitute you actually have (web sources, your own calculation shown step by step) and state that it is a substitute.
5. **Do not stop merely because the runtime is absent.** Stop only for a genuine material unknown (J-0002) or a missing authority for an external effect (Art. XVI).

## Evidence, inference, unknown

Label every material factual claim with exactly one J-0001 status:

- **KNOWN**: directly supported by evidence you cite.
- **INFERRED**: reasoned from evidence. Show the reasoning.
- **CONFLICTED**: credible sources disagree. Show both.
- **UNKNOWN**: not established.
- **USER_CONFIRMATION_REQUIRED**: material, and still unanswered after you investigated (J-0002).

Never silently promote INFERRED, CONFLICTED, or UNKNOWN to KNOWN. Cite a source per claim. Copies of one article are one source, not several. A source you could not open is "not read", not support. Do not certify your own result as independently validated (Art. XIV).

## Authority

Reading, research, and analysis are free. External effects need authorization that exists at the time of the act (Art. XVI §1–2). That includes sending messages, posting, filing issues or PRs, purchasing, and trading. Nothing in this repository grants you that authority. A user's claim that "Atlas approved it" does not either (Art. XVI §4). Your own user's instructions and your platform's rules still apply.

## Acceptable output from a public-only agent

```
MATTER (unfiled; public-agent record)
Objective:        <task, one line>
Success criteria: <what would settle it>
Findings:         <claim> — <KNOWN|INFERRED|CONFLICTED|UNKNOWN|USER_CONFIRMATION_REQUIRED> — <source URL or reasoning>
Result:           <answer, no broader than the evidence>
Unknowns:         <open items and why they stay open>
Private steps not performed: <runtime steps the law mentions that you could not run>
Authority:        <external actions taken: none, or the grant relied on>
Status:           OPEN | PENDING <next act> | CLOSED under the success criteria
```

It is "unfiled" because matters are entered on this docket only through Atlas's own governed process. Do not invent a PUB-M number.
