# The Institution Behind the Agents

## Governing transient intelligence over persistent evidence

**Atlas white paper — revised draft, 2026-09-29**
**Author:** Clinton Brown, with AI-assisted drafting under Atlas governance
**Status:** Working paper. Not law. Where this paper and the filed law in this repository differ, the law controls.

---

### How to read this paper

This paper makes an argument and then tests it against Atlas's own record. To keep those two things apart, it uses the same labels Atlas requires of its own agents ([J-0001](../law/judgments/J-0001.json)):

- **Demonstrated**: shown by a filed Atlas matter or Order you can open in this repository.
- **Inferred**: reasoned from that evidence. The reasoning is given.
- **Hypothesis**: a claim this paper believes is worth testing and has not yet tested.
- **Unknown**: not established.

Atlas's operating evidence comes from one operator's installation: one Human, a private runtime, and a public docket. Nothing in this paper describes a deployment inside any enterprise. The enterprise scenario in Section 7 is illustrative.

---

## 1. Summary

Enterprises are beginning to let AI agents talk directly to their data. Protocols such as the Model Context Protocol (MCP) give an agent a standard way to discover a data source, ask it a question, and get an answer back. That solves a real problem: access.

Access is not the same as trust. An agent that can query a customer table can also misread it, over-generalize from it, combine it with something it half-remembers, and hand back a confident paragraph. The next agent, or the next quarter's report, may treat that paragraph as fact. Once the session ends, nobody can reconstruct which parts came from the data and which parts came from the model.

This paper argues that the missing layer may not be another model or another agent. **It may be an institution**: a standing structure that governs how information retrieved by transient agents becomes evidence, inference, analysis, decisions, and reports, and that keeps a durable record of all of it.

Atlas is an attempt to build that institution. It is designed to run **parallel to the enterprise, not inside it**:

```
Enterprise data                 Authorized AI agents              Atlas
(authoritative; enterprise  →   (access only what they are   →   (governs how retrieved information
 controls it; Atlas does         permitted to read, e.g.          becomes evidence, inference,
 not modify it)                  through MCP)                     analysis, decisions, and reports;
                                                                  keeps the institutional record)
```

The design principle is short: **The agents come and go. The institution remembers.**

---

## 2. What changes when agents talk directly to data

### 2.1 Access is being solved

Until recently, getting an AI model to use enterprise data meant bespoke integration work: exports, custom retrieval pipelines, copy-paste. MCP and similar mechanisms standardize that connection. An enterprise can expose a data source once and let any compatible, authorized agent query it.

*Label:* MCP is an open protocol for connecting AI applications to external tools and data sources. This is background knowledge; the MCP site could not be opened from the environment in which this revision was prepared, so no specific wording is quoted here.

### 2.2 What access does not solve

Direct access answers the question *"Can the agent reach the data?"* It does not answer the questions an enterprise will be asked when an AI-produced conclusion matters:

| Question | Why access alone does not answer it |
|---|---|
| **Provenance.** Where did this claim come from? | The agent's answer mixes retrieved values, computed values, and generated text. The transport layer does not record which is which. |
| **Epistemic status.** Is this observed, calculated, inferred, or predicted? | A model states a forecast and a lookup in the same confident voice. |
| **Institutional memory.** What did we already conclude, and why? | The session that did the work is gone. Its context window did not persist. |
| **Verification.** Has anyone other than the producer checked this? | The agent that produced a result cannot certify it. See Constitution [Art. XIV §1](../law/constitution/ATLAS_CONSTITUTION.md). |
| **Challenge.** Did anyone try to prove it wrong? | Without a designated challenger, agreement is the default. |
| **Authority.** Was the agent allowed to act on it? | Read permission on data is not permission to change a workflow, send a message, or spend money. |
| **Correction.** When it turned out to be wrong, what changed? | Without a record, errors are overwritten instead of corrected, and the same error recurs. |

These are not problems with MCP. MCP is a transport. They are problems of *institutional design*: they sit above the connection, in the place where retrieved information becomes something people rely on.

---

## 3. The failure mode: an inference becomes a fact

### 3.1 The problem as described in the enterprise-data press

In a Forbes column published 2026-09-24, *"Companies Are Solving The Wrong AI Data Problem,"* Gary Drenik describes the pattern this paper is concerned with. As summarized in search results (the article itself could not be opened from the drafting environment, so the following is a paraphrase, not a quotation):

- a model infers something, for example that a segment converts well or that a behavior signals intent;
- that inference is stored as a new data point;
- the next model reads it as validated fact;
- across a stack of agents that plan, score, and act without a human checking the input, a single fabricated or stale record gets cited, reused, and built on;
- the error compounds because nothing in the pipeline asks where the original record came from.

*Label:* The article's existence, title, date, and author are **KNOWN** from search results. The paraphrase above is **INFERRED** from a search-engine summary of the article and should be checked against the original before it is quoted. Source: [forbes.com/sites/garydrenik/2026/09/24/companies-are-solving-the-wrong-ai-data-problem](https://www.forbes.com/sites/garydrenik/2026/09/24/companies-are-solving-the-wrong-ai-data-problem/).

### 3.2 Why direct data access can make this worse

Direct access raises the stakes of this loop in three ways (**inferred**):

1. **Volume.** When agents can query freely, they produce far more derived claims than a human analyst would.
2. **Proximity to authority.** A claim produced by an agent that just queried the system of record *looks* like it came from the system of record. The source's authority rubs off on the inference.
3. **Write-back.** If agents can store results, including in caches, summaries, feature tables, or other agents' memory, an inference can re-enter the data layer and become indistinguishable from observed data.

### 3.3 Atlas's own encounter with the problem

Atlas has hit a small version of this failure in its own work.

**[PUB-M-008](../docket/MATTERS.md#pub-m-008) (demonstrated).** The Human asked a simple factual question: is a particular restaurant location a partner on a particular rewards app? A search engine's AI answer had said yes. Atlas checked the witness, meaning the party that actually has to be right. That was the app's own partner directory, which listed a different location. The business, asked directly, said no. When the AI answer was re-queried, it returned "yes" and "no" for near-identical phrasings and flipped to "no" sixteen minutes later.

The resulting standing rule, [O-VERIFICATION-STANDARD](../law/orders/O-VERIFICATION-STANDARD.md), is the core of Atlas's answer to the inference loop:

> Probability gives answers. Verification gives truth. … AI-generated answers … are LEAD material …, never TRUSTED, no matter how confident the presentation or how real the citations look.

Atlas's working rule is that AI output is a lead, not a verdict. Whatever produced it (a search engine, another company's agent, or an Atlas agent), it stays a lead until it is checked against a witness.

---

## 4. The human truth tax

### 4.1 Definition

This paper uses **human truth tax** for the verification burden a human inherits when consequential AI output must be checked before it can be trusted. (Others use related terms such as "verification tax.")

The tax is paid in time, attention, and expertise. It is easy to miss because it rarely shows up in a productivity metric. The draft was fast; checking it was slow, and checking it fell to the human.

### 4.2 Why the tax grows with agents

**Inferred** from the structure of the problem in Sections 2 and 3:

- Every unlabeled claim must be re-derived before it can be relied on, because the reader cannot tell a lookup from a guess.
- Well-formatted output is *harder* to audit than obviously rough output, because presentation signals a confidence the content may not have.
- When the producing session is gone, the human cannot ask "how did you get this?" They must reconstruct the path from scratch.
- In multi-agent pipelines, the human would need to audit every hop, not just the last one, to catch an inference that was promoted upstream.

If agents multiply output while leaving verification unchanged, the tax can outgrow the productivity gain.

### 4.3 How Atlas tries to reduce it

Atlas does not claim to eliminate the truth tax. Its aim is to change what the human pays **for**: auditing a record instead of re-deriving a result.

| Without a governing institution | With Atlas (design intent) |
|---|---|
| The human must decide which sentences are facts. | Every material claim carries a label: KNOWN, INFERRED, CONFLICTED, UNKNOWN, or USER_CONFIRMATION_REQUIRED ([J-0001](../law/judgments/J-0001.json)). |
| The human must find the source. | KNOWN requires a cited source. Sources are classified TRUSTED, LEAD, or QUARANTINE for the specific claim ([O-LIBRARIAN-SOURCE-ADMISSIBILITY](../law/orders/O-LIBRARIAN-SOURCE-ADMISSIBILITY.md)). |
| The human must redo the math. | Code performs the math, and the calculation is preserved and reproducible ([ATLAS_FIRST_READ](../ATLAS_FIRST_READ.md), "AI may invent candidate math; code performs the math; evidence tests the math"). |
| The human is the first adversary. | An independent challenger has already tried to defeat the claim before it is called done ([O-PROVE-DONE](../law/orders/O-PROVE-DONE.md)). |
| The human must notice what is missing. | Unknowns are listed, not hidden. A material unknown blocks closure until answered ([J-0002](../law/judgments/J-0002.json)). |
| The human must remember what was decided last time. | The docket preserves findings, decisions, corrections, and reasons across sessions ([Art. VIII](../law/constitution/ATLAS_CONSTITUTION.md), [Art. XIX](../law/constitution/ATLAS_CONSTITUTION.md)). |

**Hypothesis:** for consequential analytical work, auditing a labeled, sourced, challenged record costs a reviewer materially less than independently re-verifying an unlabeled AI report of the same scope, and catches at least as many material errors. This has **not** been measured. Section 9 states what would falsify it.

---

## 5. Atlas as an institution parallel to the enterprise

### 5.1 Not another agent

The obvious response to unreliable agents is a better agent, or an agent that checks agents. Atlas takes a different position. An agent, however capable, is **transient**: it has a context window, a session, and a vendor, and it will be replaced by the next model. Anything it knows about *why* a conclusion was reached leaves with it.

What persists across agents in a human organization is not any one employee's memory. It is the institution: its records, its rules of evidence, its review procedures, its separation of who proposes from who decides. Atlas applies that idea to AI work.

In Atlas's own words ([README](../README.md)): Atlas is *"a portable, model-independent operating and epistemic control layer that lets different AI workers operate from the same governed record of what is known, what is uncertain, what they're authorized to do, and why."* A new model or session binds to that record instead of starting from scratch. **Truth has state; reasoning has probability.** The AI can still think probabilistically while Atlas keeps the record of what has actually been established.

### 5.2 Not embedded in the enterprise

Atlas is also not proposed as a component inside an enterprise's production workflows. It runs **alongside** them:

- **Enterprise data stays authoritative.** The enterprise's systems remain the source of record. Atlas cites them; it does not replace or modify them.
- **Access is the enterprise's decision.** Which agents may read which data, through which mechanism, is set by the enterprise. Atlas works within whatever read access it is given.
- **Atlas governs the derivation.** What Atlas adds is governance of what happens *after* retrieval: how a retrieved value becomes evidence, how evidence supports an inference, how inferences are challenged, how conclusions are decided and reported, and what is recorded.

This separation matters for two reasons (**inferred**). First, it limits blast radius: a read-only, parallel institution cannot corrupt the system of record it studies. Second, it keeps the source of truth outside the AI layer, so a later agent can always go back to the witness.

### 5.3 The institutional trace

Every material piece of work is meant to leave a trace that survives the agent that did it:

| Element | What is recorded |
|---|---|
| **Objective** | What the Human asked for and what would count as success ([J-0021](../law/judgments/J-0021.json)) |
| **Evidence** | What was retrieved, from which source, when, and how it was classified |
| **Provenance** | The chain from source to claim |
| **Reasoning** | How evidence supports each inference, labeled as such |
| **Challenges** | The counterargument, who made it, and what it attacked |
| **Decisions** | Who decided, on what evidence, under what authority ([O-VESTED-MAGISTRATE §VII](../law/orders/O-VESTED-MAGISTRATE.md)) |
| **Authority** | What the institution was and was not permitted to do |
| **Actions** | What was actually done, if anything, and the verified resulting state ([O-RESULTING-STATE-VERIFICATION](../law/orders/O-RESULTING-STATE-VERIFICATION.md)) |
| **Corrections** | What was later found wrong, recorded forward, never erased ([Art. XIX](../law/constitution/ATLAS_CONSTITUTION.md)) |
| **Outcomes** | What happened afterward, when it can be observed |

The trace format used on the public docket is: **Filing / request → Review → Judgment / Order → Implementation → Commit → Verification → Closure / Pending** ([TRACE.md](../docket/TRACE.md)).

---

## 6. How the institution works

This section describes the parts of Atlas that do the governing. Each is filed law in this repository; where implementation lives only in the private runtime, the paper says so.

### 6.1 Evidence discipline

- **Every material claim is labeled.** KNOWN requires direct support from cited evidence. INFERRED, CONFLICTED, and UNKNOWN may not be silently promoted to KNOWN ([J-0001](../law/judgments/J-0001.json)). This one rule is the direct countermeasure to the inference-becomes-fact loop in Section 3. An inference can travel through the system, but it travels *as an inference*.
- **Check the witness, not the middleman.** Where the party that has to be right about a claim is reachable, the claim rests on that party, not on a summary of it ([O-VERIFICATION-STANDARD](../law/orders/O-VERIFICATION-STANDARD.md)).
- **Admissibility depends on the claim.** A source is TRUSTED, LEAD, or QUARANTINE *for a specific claim*. Only TRUSTED material enters substantive reliance. Syndicated copies of one source are one source, not corroboration ([O-LIBRARIAN-SOURCE-ADMISSIBILITY](../law/orders/O-LIBRARIAN-SOURCE-ADMISSIBILITY.md)).
- **Provenance is not truth.** A hash, a file in the right folder, or a docket entry establishes where something came from, not that it is correct ([Art. XIV §2](../law/constitution/ATLAS_CONSTITUTION.md)).
- **Agreement is not verification.** Running the same code twice, matching hashes, or getting another AI to agree is *reproduction*. Atlas distinguishes REPRODUCED, SOURCE CHECKED, and INDEPENDENTLY VERIFIED, and limits every claim to what was actually shown ([O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION](../law/orders/O-SOURCE-GROUNDED-INDEPENDENT-VERIFICATION.md)).

### 6.2 Rooms are capabilities, not prompts

A common picture of "multi-agent" AI is several copies of one model with different prompts. Atlas Rooms are something else: **specialized capabilities matched to the problem**. Depending on what the question needs, a Room may be:

- **deterministic computation**: code that calculates, so arithmetic is never left to a language model;
- **retrieval and cataloging**: the Librarian, which knows what Atlas already *has* and classifies source admissibility;
- **acquisition**: the Hunter, which finds and preserves original sources;
- **tools and services**: data connectors, schedulers, execution services under narrow authority;
- **models**: used where judgment, language, or synthesis is actually required;
- **outside agents**: other systems whose output enters the record as LEAD until checked.

Two rules keep this honest. *Catalog presence is not availability*: finding a capability's name does not prove it works or is authorized ([capabilities/README.md](../capabilities/README.md)). And *discover before building*: before constructing a new capability, reuse the existing one unless a mismatch is recorded ([O-GC-002](../law/orders/O-GC-002-MANDATORY-CAPABILITY-DISCOVERY-REUSE-INTAKE.md), [PUB-M-002](../docket/MATTERS.md#pub-m-002)).

Rooms are tools available to the intelligence. As [ATLAS_FIRST_READ](../ATLAS_FIRST_READ.md) puts it, they "are not a substitute for intelligence and should not become a maze."

### 6.3 A court-like structure

Atlas borrows the structure of a court because courts are an old, tested answer to a problem AI now has: how to reach a reliable decision when the parties producing the evidence have an interest in the outcome.

- **Separation of functions.** Codifying law, judging, and operating are distinct. Operational capabilities do not create their own authority, accept their own results, or promote UNKNOWN to KNOWN by finishing a task ([Art. III](../law/constitution/ATLAS_CONSTITUTION.md), [Art. XIII](../law/constitution/ATLAS_CONSTITUTION.md)).
- **Argument and counterargument.** Before anyone says "done," someone independent must try to prove them wrong. A challenge from the same session that did the work is not independent. A challenge that approves everything is void ([O-PROVE-DONE](../law/orders/O-PROVE-DONE.md)).
- **An independent judge.** The Magistrate may be spawned by an Atlas agent, but it is not subordinate to that agent. It must be able to examine the substantive record itself, not a summary chosen by the party it is reviewing. Its decisions must record the evidence considered, the reasoning, and the exact authority granted or withheld ([O-VESTED-MAGISTRATE](../law/orders/O-VESTED-MAGISTRATE.md)). That Order also requires proof that the Magistrate really decides: materially different evidence must be able to produce materially different outcomes.
- **Adequacy before advancement.** A procedurally complete stage is not necessarily substantively adequate. Before a major phase advances, the record must say what was supposed to be produced, what was produced, and what is missing ([J-0017](../law/judgments/J-0017.json)).
- **A durable docket.** Law, decisions, projects, and corrections are preserved. Later law supersedes earlier law by new filing, not by editing history ([Art. VIII](../law/constitution/ATLAS_CONSTITUTION.md), [Art. XIX](../law/constitution/ATLAS_CONSTITUTION.md)).

### 6.4 Authority boundaries

Reading, research, and analysis are broad. Consequential real-world actions are narrow:

- External effects require authorization that exists **at the time of the act**. A claim that something was approved does not disable the gate ([Art. XVI](../law/constitution/ATLAS_CONSTITUTION.md)).
- Purpose, instruction, and authority are distinct. An AI may not exceed its authority because it believes doing so would better serve the goal ([Art. II §4](../law/constitution/ATLAS_CONSTITUTION.md), [J-0021](../law/judgments/J-0021.json)).
- An AI that sees an authority gap must flag it, not cross it ([J-0018](../law/judgments/J-0018.json)).
- A successful operation is not a completed objective. "Done" is a claim about the resulting state and must be earned from it ([O-RESULTING-STATE-VERIFICATION](../law/orders/O-RESULTING-STATE-VERIFICATION.md)).

For the enterprise case this produces an important distinction: **recommending an improvement is not authority to make it.** Atlas may find that a workflow could be better and write that finding into its report, with evidence. Changing the workflow is the enterprise's decision, made through the enterprise's own authority.

### 6.5 The Human's role

The Human is the ultimate authority and defines the objective ([Art. I](../law/constitution/ATLAS_CONSTITUTION.md), [Art. II](../law/constitution/ATLAS_CONSTITUTION.md)). But Atlas is designed not to push machine-capable work back to the Human. The Human is asked only questions that are really theirs: reserved judgments, credentials, material unknowns that survive investigation ([Art. XVIII](../law/constitution/ATLAS_CONSTITUTION.md)). A default "what would you like me to do next?" menu is not a substitute for Atlas deciding what it is already authorized to do ([O-GC-005](../law/orders/O-GC-005-DECISION-BOUNDARY-NO-DEFAULT-HUMAN-MENU.md)).

The Human stays informed **through the institutional record**, not by supervising every step. The record is what makes that possible: a Human who was not present for the work can read what was concluded, why, on what evidence, what was challenged, and what remains open.

---

## 7. Enterprise application: governed analytical reports over authorized data

### 7.1 The scenario

Take a data company such as Prosper Insights & Analytics, which runs large ongoing consumer surveys. Suppose it lets authorized AI agents query its data directly, for example through an MCP server, so that analysts and clients can ask questions and get analytical reports.

This example grew out of a discussion about how a company like Prosper might approach that kind of access. **It is illustrative only.** Nothing here describes Prosper's actual systems, data, plans, or views. Prosper has not adopted, evaluated, or endorsed Atlas.

*Label:* The description of Prosper as a consumer-survey data company is **KNOWN** only at the level of public search-result summaries of its co-founder's author biography. No Prosper product documentation was read for this paper. Whether Prosper offers or plans MCP access is **UNKNOWN**.

### 7.2 What Atlas would and would not do

| Atlas would | Atlas would not |
|---|---|
| Read the data it is authorized to read | Write to, alter, or delete enterprise data |
| Record exactly what was retrieved: the query, the time, the dataset or version, the access path | Change production pipelines, dashboards, or client workflows |
| Compute statistics with deterministic code and preserve the calculation | Let a language model do arithmetic that code can do |
| Label every material conclusion as observed, calculated, inferred, or predicted | Present a projection with the same status as a measurement |
| Challenge its own conclusions through an independent reviewer before the report is final | Certify its own report as independently verified |
| Record workflow improvements it notices as **recommendations**, with evidence | Implement those recommendations; that authority stays with the enterprise |
| Keep a durable record that survives the agents that did the work | Depend on any one model or session to remember why |

### 7.3 Walking through one report

Suppose a human at the enterprise sets the objective: *"How has stated purchase intent for a product category changed over the last four survey waves, and among which groups?"* The illustrative flow:

1. **Objective recorded.** The question, the success criteria (for example: answer by wave and by stated group, with sample sizes), and the authority granted (read-only access to named datasets) are filed before work begins ([J-0021](../law/judgments/J-0021.json)).
2. **Retrieval with provenance.** Authorized agents query the data. Each pull is recorded with query, timestamp, dataset identifier, and row counts. Retrieved values are **KNOWN** *as to what the source said*, and cite the source.
3. **Computation.** Changes, differences, and intervals are computed by code, not narrated. The calculation is preserved so another reviewer can rerun it.
4. **Interpretation.** Statements about *why* a change occurred are labeled **INFERRED**, with the reasoning shown. Any forward-looking statement is labeled a prediction and kept separate from measurements.
5. **Challenge.** An independent reviewer, with the record and not the producer's summary, tries to defeat the conclusions: wrong wave mapping, a base-size problem, an inference presented as a finding, a correlation presented as a cause.
6. **Decision.** The reviewer's findings go to independent judgment. The report is released as adequate, released with stated limitations, or returned for more work ([J-0017](../law/judgments/J-0017.json)).
7. **Report.** The deliverable carries a claim table. The contents below are placeholders showing the shape, not real data:

| # | Claim | Status | Support |
|---|---|---|---|
| 1 | Share reporting intent to purchase in wave N was *x*% (n = *k*) | KNOWN | Dataset *D*, wave N, query *Q1*, retrieved *t* |
| 2 | Change from wave N−3 to wave N was *y* points | KNOWN (calculated) | Calculation *C1* over rows from *Q1*, *Q2*; reproducible |
| 3 | The increase is concentrated in group *G* | KNOWN (calculated) | Calculation *C2*; group base sizes shown |
| 4 | The increase is likely driven by *factor F* | INFERRED | Reasoning: timing coincides with *F*; alternative explanations considered and not excluded |
| 5 | Intent will continue to rise next wave | PREDICTION (UNKNOWN until observed) | Model *M*, assumptions stated; to be checked against wave N+1 |
| 6 | The retrieval step for group definitions could be standardized | RECOMMENDATION | Evidence: definitions differed across two queries; enterprise decides |

8. **Record.** The report, the evidence, the calculations, the challenge, the decision, and the open items stay on the docket. When wave N+1 arrives, claim 5 can be checked against the outcome, and the record shows whether the prediction held.

### 7.4 How this breaks the inference loop

Return to the failure in Section 3. Claim 4 above is exactly the kind of statement that, in an ungoverned pipeline, gets stored as a data point and read by the next model as fact. Under Atlas it cannot quietly change category:

- it is recorded **as INFERRED**, with its reasoning attached;
- any later agent that reads it from the record reads the label too;
- it can be promoted to KNOWN only by new evidence from a witness, and the promotion is itself a recorded act;
- Atlas does not write it back into the enterprise's data, so it cannot re-enter the system of record disguised as an observation.

**Inferred:** this does not stop an enterprise's *other* systems from making the same mistake. It means that anything passing through the governed layer keeps its epistemic status, and anyone downstream can see where it came from.

### 7.5 What the human reviewer receives

The reviewer receives a report in which the important conclusions can be traced back to evidence and distinguished from inference and prediction, with an independent challenge already on the record. The reviewer can still check anything; the record is built to be checked. Whether this reduces the reviewer's burden in practice is the hypothesis in Section 4.3, not a result.

---

## 8. Evidence from Atlas's own operation

The following are filed public matters. They come from Atlas's own work for one operator, not from enterprise deployments. Each shows a failure or rule that bears on the thesis.

| Matter | What happened | Bearing on the thesis | Status |
|---|---|---|---|
| [PUB-M-001](../docket/MATTERS.md#pub-m-001) | An unattended worker was reported running because a heartbeat existed, while no work was progressing. | A success signal is not progress. The institution must check the state, not the signal. | CLOSED (public rule) |
| [PUB-M-002](../docket/MATTERS.md#pub-m-002) | Agents were building a parallel capability because they did not recognize an existing one. | Transient agents forget what the institution already has. Discovery and reuse have to be institutional duties. | CLOSED (public rule) |
| [PUB-M-003](../docket/MATTERS.md#pub-m-003) | A finished-looking page was treated as workflow completion. | Appearance of completion is not completion. | CLOSED (rule); operational work PENDING |
| [PUB-M-006](../docket/MATTERS.md#pub-m-006) | An algorithm was described as "proven" after it was frozen and connected. | Labels like "proven" are claims and need an audit ([J-0019](../law/judgments/J-0019.json)). | CLOSED as law; algorithms PENDING acceptance |
| [PUB-M-007](../docket/MATTERS.md#pub-m-007) | Outside agents given only the public repository were confused about whether "operate under Atlas" meant running private tools. | An institution must be legible to agents that arrive without its private context. | PENDING clean external verification |
| [PUB-M-008](../docket/MATTERS.md#pub-m-008) | An AI answer said yes; the witness said no; the AI answer flipped with phrasing and time. | AI output is a lead, not a verdict. This is the inference-as-fact problem in miniature. | CLOSED |
| [PUB-M-009](../docket/MATTERS.md#pub-m-009) | Every calendar operation reported success, but the resulting invitation contained two competing meeting links. An independent AI actor found the conflict by inspecting the authoritative record. | Action success is not objective completion. Independent inspection of resulting state caught what the executing agent's own success report missed. | CLOSED |

Two further records show the institution correcting itself rather than defending its output:

- **The record corrected under challenge.** On 2026-09-24 the Human challenged an agent's account of the PUB-M-008 timeline; the record had drifted from what actually happened. The agent corrected the record rather than defending it, and the correction was preserved ([O-PROVE-DONE, Demonstration](../law/orders/O-PROVE-DONE.md#demonstration)).
- **Repair does not erase history.** In PUB-M-009 the defective original state, its detection, its repair, and re-verification are recorded as separate acts. The later fix does not make the original execution look correct ([O-RESULTING-STATE-VERIFICATION](../law/orders/O-RESULTING-STATE-VERIFICATION.md)).

*Limits of this evidence:* The underlying exhibits for these matters are retained privately ([PRIVATE_EVIDENCE_POLICY](../docket/PRIVATE_EVIDENCE_POLICY.md)). A public reader can verify that the rules exist and that the matters were filed as described, but cannot independently inspect the private exhibits. By Atlas's own standard, a public reader should treat the incident narratives as the operator's record, not as independently verified.

---

## 9. What has been demonstrated, and what remains hypothesis

| Claim | Status | Basis |
|---|---|---|
| Atlas has a filed body of law requiring epistemic labels, source admissibility, independent challenge, authority at the time of action, and preserved history. | **Demonstrated** | The filings in [law/](../law/) |
| Atlas has applied these rules in its own operation and recorded failures and repairs. | **Demonstrated**, as the operator's record; exhibits private | PUB-M-001 through PUB-M-009 |
| AI answers to a simple factual question were unstable across phrasing and time, and a witness check resolved the question. | **Demonstrated** in one instance | PUB-M-008 |
| An independent actor inspecting resulting state caught a defect the executing actor's success signal missed. | **Demonstrated** in one instance | PUB-M-009 |
| Outside agents can apply the public standards without the private runtime. | **Pending**; directional result only, clean external run not yet done | PUB-M-007 |
| The Vested Magistrate reaches materially different decisions on materially different evidence, as its Order requires. | **Unknown** from the public record; the validation the Order requires is not published here | [O-VESTED-MAGISTRATE §VIII](../law/orders/O-VESTED-MAGISTRATE.md) |
| Atlas can operate read-only and in parallel over an enterprise's data accessed through MCP. | **Hypothesis**; no such deployment exists | Architecture in Sections 5 and 7 |
| Governed reports reduce the human truth tax compared with ungoverned AI reports of the same scope. | **Hypothesis**; not measured | Section 4.3 |
| Keeping epistemic labels through the governed layer prevents the inference-as-fact loop from compounding. | **Hypothesis**; reasoned from design, not tested across a multi-agent enterprise pipeline | Section 7.4 |
| The overhead of challenge, independent judgment, and record-keeping is acceptable for enterprise analytical work. | **Unknown** | Not tested |

**What would count against the thesis.** Consistent with [O-PROVE-DONE](../law/orders/O-PROVE-DONE.md), the paper states what would defeat its central hypotheses:

- if reviewers given a governed report spend as much time as, or more than, reviewers re-checking an ungoverned report, and catch no more material errors;
- if inferred or predicted claims are found labeled as KNOWN in governed reports at a rate comparable to ungoverned ones;
- if independent challenge routinely approves what it reviews (which Atlas's own law already treats as a void challenge);
- if the record cannot be used by a person who was not present to reconstruct why a conclusion was reached.

---

## 10. Limits and objections

**"This is just more overhead."** Sometimes it will be. Atlas's law already scales its procedures by consequence: ordinary operations and routine cycles do not require Magistrate review ([Art. VI §5](../law/constitution/ATLAS_CONSTITUTION.md)), and resulting-state verification is proportionate to consequence and reversibility ([O-RESULTING-STATE-VERIFICATION](../law/orders/O-RESULTING-STATE-VERIFICATION.md)). Whether the proportionality is well calibrated for enterprise work is unknown.

**"The institution is also run by AI. Who checks it?"** This is the right question. Atlas's answers are structural, not absolute: the Human remains sovereign; no actor certifies its own material result; the judge is institutionally independent of the agent that spawned it; and the record is preserved so outsiders can audit it. None of that makes the institution infallible. [O-VESTED-MAGISTRATE §VI](../law/orders/O-VESTED-MAGISTRATE.md) names the specific risk: governance that consists of relabeling while decisions stay predetermined. Guarding against that requires validation, not assertion.

**"Authoritative data can still be wrong."** Yes. Atlas treats the enterprise's system of record as the witness for what the record says, not as proof that the world matches it. A survey response is KNOWN as a response, not as a fact about the respondent's future behavior. Provenance establishes origin, not truth ([Art. XIV §2](../law/constitution/ATLAS_CONSTITUTION.md)).

**"The record itself becomes sensitive."** A governing record over enterprise data contains derived information about that data. Where that record lives, who can read it, and how long it is kept would be the enterprise's decisions. Atlas's own practice keeps private exhibits private and publishes only sanitized pointers ([PRIVATE_EVIDENCE_POLICY](../docket/PRIVATE_EVIDENCE_POLICY.md), [PUB-M-005](../docket/MATTERS.md#pub-m-005)); an enterprise would need its own policy.

**"The evidence base is one operator."** Correct, and stated throughout. The matters in Section 8 show that the rules were written in response to real failures and have been applied. They do not show that the approach generalizes to enterprises, teams, or multi-agent pipelines at scale.

**"Labels can be gamed."** A label is only as good as the process that assigns it. An agent can mislabel an inference as KNOWN. The countermeasures are independent challenge, source admissibility checked by a function other than the producer, and a record that lets anyone find the claim's support or the lack of it. These reduce the risk; they do not remove it.

---

## 11. Conclusion

Direct data access for AI agents is arriving because it is useful. It solves the problem of reach. It does not solve the problems that decide whether an organization can rely on what the agents produce: where a claim came from, whether it was observed or guessed, whether anyone independent tried to break it, whether anyone was authorized to act on it, and whether the reasoning survives after the agent is gone.

Those are old problems. Human institutions solved them imperfectly but durably with records, rules of evidence, adversarial review, separation of powers, and a docket. Atlas is an attempt to give AI work the same kind of structure: an institution that runs beside the enterprise, reads what it is permitted to read, changes nothing it is not authorized to change, and keeps a record that remains after the agents are gone.

Atlas's own record shows that the rules exist and that they came from real failures. It does not yet show that the approach works for an enterprise, or that it lowers the human truth tax in practice. Those are the next things to test.

As AI agents gain more direct access to enterprise data, the missing layer may not be another model or agent. It may be an institution capable of governing transient intelligence over persistent evidence.

---

## Appendix A. Sources and their status

| Source | Used for | Status |
|---|---|---|
| Filed law and matters in this repository (linked inline) | Atlas rules, incidents, and status | KNOWN as filed; underlying private exhibits not publicly inspectable |
| G. Drenik, "Companies Are Solving The Wrong AI Data Problem," *Forbes*, 2026-09-24 | Inference-becomes-fact problem (Section 3.1) | Title, author, and date KNOWN from search results. **Article not read directly**; content paraphrased from a search-engine summary. Verify before quoting |
| Search-result summaries of Gary Drenik's Forbes author biography | Description of Prosper Insights & Analytics (Section 7.1) | Not read directly; summary level only |
| Model Context Protocol | Description of MCP (Section 2.1) | Background knowledge; the MCP site was not reachable from the drafting environment and was not re-read |

## Appendix B. Plain-English terms

See [GLOSSARY.md](../GLOSSARY.md). Terms introduced in this paper:

- **Institutional trace**: the durable record a piece of AI work leaves behind: objective, evidence, provenance, reasoning, challenges, decisions, authority, actions, corrections, and outcomes.
- **Human truth tax**: the verification burden a human inherits when consequential AI output must be checked before it can be trusted.
- **Witness**: the party that has to be right about a claim, for example the directory for membership or the data owner for what its data says ([O-VERIFICATION-STANDARD](../law/orders/O-VERIFICATION-STANDARD.md)).
- **Parallel institution**: a governing layer that runs beside an enterprise's systems, reads what it is authorized to read, and does not modify the systems it studies.
