# O-GC-003 — Atlas V4 Portable Bootstrap and Authoritative Docket

**Filing type:** USER ORDER (standing)  
**Status:** BINDING  
**Date:** 2026-09-05  
**Order id:** `O-GC-003`  
**Caption:** ORDER GC 003  
**Canonical id:** G-285  
**Human source:** Cursor instruction authorizing implementation after the Atlas V4 Portable Cloud Governance Audit FAIL.

**Does not:** redesign Atlas Governance V2; create Governance V3 or Governance V4 law; amend J-0019 or any Judgment; authorize live trading; erase the V4 FAIL audit or the Alpaca options incident; implement token-accounting repair, multi-agent isolation, UI redesign, historical job cleanup, trading-strategy changes, Chapter changes, or a broad V2 refactor.

Governance V2 remains the governing law unless separately changed by Human authority.

“Atlas V4” in this Order means the portable architecture that lets a fresh AI actor discover and verify governing law, project authority, evidence requirements, and execution boundaries without hidden conversational or workstation context. It is not adoption of a new law version.

## 1. Objective

A fresh AI actor with only the portable bootstrap package must be able to determine, or else fail closed:

- the Atlas architecture/version it is entering;
- the currently governing law;
- the active or assigned project;
- controlling judgments and orders (by identifier and hash);
- authority granted;
- prohibited actions;
- required evidence destinations;
- acceptance authority;
- whether the authoritative record has been cryptographically verified.

## 2. Package

Create and maintain `ATLAS_BOOTSTRAP.md`, `atlas-manifest.json`, and the minimum verification adapter that makes them functional. Point to the authoritative record; do not duplicate law text.

## 3. Canonical index

One machine-reachable authoritative index that does not require this workstation. It must expose machine-readable governance identifier, governing SHA, controlling-record hashes, assigned project, authority and prohibitions, evidence destination, acceptance authority, manifest version, and a non-UNKNOWN deployed record hash.

A login wall, unavailable endpoint, authentication failure, hash mismatch, missing deployed hash, or unverifiable record is UNKNOWN and fail-closed.

Do not treat local disk as proof of the live index during portable bootstrap.

Do not publish the full private docket or Judgment bodies. The index is hashes and authority pointers, not a replacement for the Entra-gated viewer.

## 4. Integrity

The bootstrap must not be trusted merely because the same actor wrote it. Verify by fetching the live index, recomputing the payload hash, and comparing the bootstrap pin. Do not silently replace historical hashes. Preserve recorded mismatches (including Atlas Room `source_hashes.json` vs live J-0019) until an authorized reconciliation.

## 5. Authority

This bootstrap grants no substantive authority. It only discovers and verifies authority already granted under Governance V2 and Human records. Missing law, missing authority, and UNKNOWN verification are not permission.

## 6. Local compatibility

Existing local Atlas may continue. Remove `D:\atlas` hard dependency only on the portable verify path. Do not rewrite Watcher, Hunter, Chapter, CRM, trading, Room, Magistrate, or other working engines to satisfy this Order.

## 7. Acceptance

Files existing is not completion. Pass only if an isolated fresh actor, without prior Atlas conversational context and without relying on local Atlas files, can verify the live index and the facts in §1, and stops on a deliberately broken verification.

## 8. Historical preservation

The Atlas V4 FAIL audit remains the pre-implementation baseline. Do not rewrite the Alpaca options incident or other historical failures.
