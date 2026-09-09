# Atlas — public governance docket

Atlas is a **governed AI/agent operating system**: a work framework that requires evidence, explicit authority, persistent state, an audit trail, and fail-closed execution. It is not a chat log and not a pile of scripts.

This repository is the **public procedural record and portfolio**. It is not a backup of the private operational tree, not a second live docket host, and not a dump of private evidence.

## Start here (about 10 minutes)

1. This README — what Atlas is, what Clinton directed, how it responds to real failure modes
2. [GLOSSARY.md](GLOSSARY.md) — plain English for Atlas terms
3. [docket/MATTERS.md](docket/MATTERS.md) — representative traces you can follow end to end
4. [PORTFOLIO.md](PORTFOLIO.md) — what this record is meant to prove
5. [CURRENT_LAW.md](CURRENT_LAW.md) and [architecture/README.md](architecture/README.md) if you want the rules and the loop

**Representative matters**

| Matter | What it shows |
|---|---|
| [PUB-M-001](docket/MATTERS.md#pub-m-001) | Unattended process looked alive but was stalled — heartbeat is not progress |
| [PUB-M-002](docket/MATTERS.md#pub-m-002) | Duplicate construction blocked; discover and reuse before building |
| [PUB-M-003](docket/MATTERS.md#pub-m-003) | CRM lifecycle quality: a finished-looking page is not done |
| [PUB-M-004](docket/MATTERS.md#pub-m-004) | Paper trading: freeze and connectivity are not acceptance |
| [PUB-M-005](docket/MATTERS.md#pub-m-005) | Publication hygiene: private paths do not belong on a public docket |

## What Clinton did

Clinton Brown is the Human whose system this is. He **designed, directed, tested, audited, and governed** Atlas and its AI-assisted implementation: Goal and Orders, what must remain private, what counts as done, and when execution must stop.

This portfolio does **not** claim he personally hand-coded every module. The record shows directed construction, review, and fail-closed rules, with implementation performed by authorized agents under that governance.

## What problem Atlas addresses

Ordinary agent setups fail in predictable ways:

- **Lost state** — the next session cannot reconstruct what was already decided
- **False completion** — a heartbeat, a UI, or a passing vibe is treated as the Goal
- **Unauthorized execution** — send, trade, or build without a recorded grant
- **Weak evidence** — claims without sources, hashes, or labels
- **Duplicate / parallel work** — a second engine because the first was unfamiliar
- **Tool-routing failures** — catalog mention treated as a working capability
- **Unreliable unattended operation** — a process is “running” but making no progress
- **No reconstructable why** — nobody can show filing → ruling → commit → verification

## How Atlas responds

| Failure mode | Atlas response |
|---|---|
| Lost state | Durable docket, jobs, and derived current-state packets (operational memory, not law) |
| False completion | Explicit closure rules; Magistrate review; mechanical PASS is not Human Goal completion |
| Unauthorized execution | Fail-closed gates; paper vs live; send remains ungranted until an Order says otherwise |
| Weak evidence | J-0001 labels (known / inferred / unknown); evidence pointers; private exhibits stay private |
| Duplicate construction | O-GC-002: discover and reuse; replacement needs a recorded mismatch or Human override |
| Tool-routing theater | Catalog presence is not availability; discovery does not grant execution |
| Unattended stall | Liveness ≠ progress; watchdog; bounded workers |
| Unreconstructable action | Trace: filing → review → judgment/order → implementation → commit → verification → closure |

Governing law for agents now: [CURRENT_LAW.md](CURRENT_LAW.md). How to read an Order or Judgment: [law/README.md](law/README.md).

## Public vs private

| Public (this repo) | Private (not here) |
|---|---|
| Governance V2 law, Constitution, Judgments | Secrets, API keys, tokens, vaults |
| Public-safe Orders (some bodies stubbed) | Mailbox, broker account IDs, credential metadata |
| Sanitized docket / traces | Customer/lead records, CRM payloads |
| Architecture and capability documentation | PERSONAL_CONTEXT corpus |
| This git history | Entra-protected Human docket viewer |

CRCR (Clinton Rules of Computational Procedure) is a **working name** and **not adopted**. Slot: [crcr/README.md](crcr/README.md).

Related public work: [atlas-portable-index](https://github.com/atlaslaw2026/atlas-portable-index) (bootstrap), [Atlas-Law-Viewer](https://github.com/atlaslaw2026/Atlas-Law-Viewer) (product demo).

See [SECURITY.md](SECURITY.md). If you find a secret or lead-level record here, treat it as an incident.
