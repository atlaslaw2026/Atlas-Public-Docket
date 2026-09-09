# O-MATERIAL-UNCERTAINTY-CANONICAL-CONSULT

**Filing type:** USER ORDER  
**Date:** 2026-08-27  
**Adopts:** Human ruling on the docket-first uncertainty briefing (adopt with limits)  
**Implements / supplements:** J-0001, J-0002, J-0010, J-0011, J-0018, J-0019, J-0020, J-0021, O-J-0020-AUTOMATIC-CONTINUATION, O-J-0019-REMEDIABLE-EVIDENCE-REMAND, O-J-0019-INVOCATION-BOUND-NOT-PROJECT-STOP  
**Does not create a new ACTIVE Judgment.** Disk ACTIVE judgment set remains pinned to `CURRENT_LAW.json` `current_sha`.  
**Does not authorize live money.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**  
**Does not special-case any project id.**

## Ruling

Adopt a universal material-uncertainty canonical-authority consultation rule, implemented centrally and feeding the existing NEXT_ACT control plane, with the Human Docket/Viewer remaining non-authoritative and ordinary resource/tool limits excluded from governance escalation.

This Order is the adopting instrument. It is not itself a Judgment. It does not rewrite G-n history.

## Rule

When Atlas encounters **material** uncertainty affecting authority, operative state, evidence reliance, routing, continuation, acceptance, execution, termination, or whether Human action is required, Atlas SHALL consult canonical authority through `atlas_gov.consult.consult_canonical_authority` **before** acting, stopping, escalating, or inferring authority.

Consultation is a **lookup**. It SHALL feed `atlas_gov.rooms.runtime.compute_next_act`. It SHALL NOT become a second Magistrate, a second NEXT_ACT chooser, or a runtime god-object that re-walks G-n history. Ordinary current authority remains derived CURRENT_STATE compiled from canonical sources.

**Material** uses the J-0002 test. Non-material drafting and ordinary investigation SHALL NOT trigger this consult as an authority gap (J-0018).

## Canonical sources (precedence)

1. Binding User Orders  
2. ACTIVE Judgments at the pinned current_sha (disk and SHA sets must match)  
3. Incorporated standing gates  
4. Canonical docket filings (`docket/ATLAS_DOCKET.json`, `docket/ATLAS_GOVERNANCE_FILINGS.json`, original filings)  
5. Latest Magistrate review and RUNNING/AUTHORIZED job  
6. Derived CURRENT_STATE — operational memory, not law (J-0011)

## Forbidden as authority

Human Docket (`HUMAN_DOCKET.json`), Governance Viewer, Azure live URL, `viewer/docket/INDEX.json`, `ATLAS_RECORD/ATLAS_NEXT_ACTION.json`, historical cabinet papers, Watcher overlay Magistrate, prompt text, and chat memory SHALL NOT be consulted for authority. Identity pointer `docket/CURRENT_DOCKET.json` is not itself law.

## Implementation ceilings (not governance exhaustion)

`MAX_OUTER`, search limits, local file exhaustion, tool unavailability, source unavailability, and equivalent implementation ceilings MAY end one invocation. They SHALL NOT be treated as UNKNOWN law, HUMAN_RESERVED, or AUTHORITY_EXHAUSTED. Persist continuation under O-J-0019-INVOCATION-BOUND-NOT-PROJECT-STOP.

## Preserve / Human

UNKNOWN, AMBIGUOUS, and CONFLICTED SHALL NOT be silently promoted to KNOWN (J-0001). CURRENT_STATE_CONFLICT fail-closes to the existing Magistrate path. Remediable evidence UNKNOWN remains room remand (O-J-0019-REMEDIABLE-EVIDENCE-REMAND), not Human continue. Human escalation remains J-0002 (after investigation), J-0018 flags, and J-0020 reserved Judgment / genuine credentials / non-remediable evidence / act beyond authority.

## Audit

Constraining consults (block, conflict, forbidden source, or implementation ceiling) MAY file a `CANONICAL_AUTHORITY_CONSULT` docket event. Do not mint a new G-n per consult. Do not append INDEX 88.
