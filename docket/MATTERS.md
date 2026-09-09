# Representative public matters

These rows are public-safe. Private exhibits are pointers only. Glossary: [../GLOSSARY.md](../GLOSSARY.md).

Public commit SHAs below refer to **this** repository. Private Governance V2 SHAs are not copied here.

---

## PUB-M-001

**Supervisor: “alive” is not progress**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-001 |
| Filing / request | Unattended worker reported live because a process ID and heartbeat existed, while no work progressed |
| Review | Operational health review (liveness vs progress) |
| Judgment / Order | Fail-closed unattended operation: heartbeat is not progress; at most one watchdog |
| Implementation | Supervisor runtime distinguishes heartbeat age from progress age; stalled workers are not “running” |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Private implementation | `PRIVATE_RETAINED` — change class: supervisor stall / single watchdog |
| Verification | Bounded supervisor health tests on an isolated checkout of the private implementation SHA (recorded in the private review package). Public proof: this trace + [audits/README.md](../audits/README.md) |
| Status | **CLOSED** for the public-safe rule; private runtime remains operational |
| Evidence pointer | `evidence_class: PRIVATE_RETAINED`, `pointer: EVT-PUB-M-001` |

---

## PUB-M-002

**Capability discovery before a new engine**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-002 |
| Filing / request | Agents were constructing parallel capabilities because an existing Room/catalog entry was unfamiliar |
| Review | Construction intake (O-GC-002) |
| Judgment / Order | [O-GC-002](../law/orders/O-GC-002-MANDATORY-CAPABILITY-DISCOVERY-REUSE-INTAKE.md): discover and reuse; replacement needs a recorded mismatch or Human override. Catalog presence is not availability |
| Implementation | Public law + architecture text; Atlas Room remains the discovery surface. A local vendored-copy shim was **not** published (pending a Room-move ruling) |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Private implementation | `PRIVATE_RETAINED` — change class: construction gate / Room canonicalization (unpublished shim excluded) |
| Verification | Order text in this repository; construction gate denies unauthorized new engines |
| Status | **HOLD** on publishing the unpublished shim; **CLOSED** on the public rule |
| Evidence pointer | `pointer: EVT-PUB-M-002` |

---

## PUB-M-003

**CRM lifecycle quality (no lead payloads)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-003 |
| Filing / request | A finished-looking product page was being treated as workflow completion |
| Review | Program quality / lifecycle review |
| Judgment / Order | Canonical CRM program is process-next; send remains ungranted until an Order says otherwise; a populated overflow page is not by itself a blocker or a completion |
| Implementation | Canonical `process-next` program under Governance (private engine). Public: this trace + project 1-10/1-12 captions in [INDEX.md](INDEX.md) |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Private implementation | `PRIVATE_RETAINED` — change class: CRM process-next program |
| Verification | Program tests in the private engine; public docket carries the disposition, not customer records |
| Status | **PENDING** operational CRM work; **CLOSED** on the public-safe quality rule |
| Evidence pointer | `pointer: EVT-PUB-M-003` (no names, properties, or mailboxes) |

---

## PUB-M-004

**Project 1-11: authority and acceptance (no account identifiers)**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-004 |
| Filing / request | New paper work on designation 1-11 (quantum-equities sleeve). Paper only. Live money forbidden |
| Review | Magistrate / acceptance path required before treating an algorithm as proven |
| Judgment / Order | Public stub: [O-PROJECT-1-11-QUANTUM.md](../law/orders/O-PROJECT-1-11-QUANTUM.md) (full Order retained privately because it named private identifiers). Controlling public law: [J-0019](../law/judgments/J-0019.json) (freeze and connectivity are not acceptance), J-0020 / J-0021 |
| Implementation | Fail-closed execution and selection gates in the private engine |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Private implementation | `PRIVATE_RETAINED` — change class: fail-closed controlling review and paper selection gates |
| Verification | Controlling-review tests in the private isolated checkout; J-0019 remains the public acceptance rule |
| Status | **PENDING** (project still OPEN on [INDEX.md](INDEX.md)); acceptance not claimed |
| Evidence pointer | `pointer: EVT-PUB-M-004` |

---

## PUB-M-005

**Publication hygiene: workstation paths are not public evidence locators**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-005 |
| Filing / request | Pre-publication audit (F-PUB-001): a Judgment evidence locator used a local user-profile path |
| Review | Publication security audit (accepted) |
| Judgment / Order | J-0001 still governs fact labels; public locators must not carry workstation paths. Private exhibit retained |
| Implementation | Locator replaced with `PRIVATE_RETAINED` / `EVT-J0001-E-T1`. Reachable git history of this repository rewritten so the old path is not on `master` |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Verification | Full-history scan of this repository after the rewrite (private review package) |
| Status | **CLOSED** — prohibited locator absent from reachable history of this repository |
| Evidence pointer | `pointer: EVT-J0001-E-T1` — exhibit hash recorded only in the private companion |

---

## PUB-M-006

**False “proven working” without an acceptance audit**

| Step | Public record |
|---|---|
| Docket ID | PUB-M-006 |
| Filing / request | An algorithm was described as proven after freeze and broker connectivity |
| Review | Argument / counterargument / Human Judgment |
| Judgment / Order | [J-0019](../law/judgments/J-0019.json): freeze and connectivity are not acceptance |
| Implementation | Public law in this repository; private projects remain paper-only and unaccepted until an audit says otherwise |
| Public commit | `186d04ce8749b0af2bef8c6e154dba2ef6c4db9e` |
| Verification | The Judgment text and rule list in `law/judgments/J-0019.json` |
| Status | **CLOSED** as law; individual algorithms remain **PENDING** acceptance |
| Evidence pointer | `pointer: EVT-PUB-M-006` (underlying project exhibits private) |
