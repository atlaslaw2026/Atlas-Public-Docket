# O-GC-002 — Mandatory Capability Discovery and Reuse Intake

**Filing type:** USER ORDER (standing)  
**Status:** BINDING  
**Date:** 2026-09-05  
**Order id:** `O-GC-002`  
**Caption:** ORDER GC 002  
**Job:** `JOB_PROGRAM_PORTFOLIO_CHAPTER_ASSET_RECOVERY`  
**Human source:** Cursor conversation proposing the Order text (2026-09-05)  
**Does not independently authorize:** paid generation, external communication, manuscript modification, deployment, dangerous operations, or live trading.

## 1. Rule

No Atlas agent, script, room, cloud worker, SDK consumer, launcher task, or other authorized machine actor may create, generate, scaffold, replace, substantially duplicate, or commission a new program, engine, workflow, service, agent, or reusable capability unless the proposed construction has first passed Atlas capability discovery and reuse intake.

## 2. Required Intake

Before construction begins, the actor must submit the intended capability by purpose and required behavior, not merely by proposed filename, implementation, or product name, through the authorized Atlas discovery and intake mechanism.

The intake must determine whether Atlas already possesses a capability that could satisfy or materially contribute to the requested work.

## 3. Existing Capability Found

If discovery identifies an existing capability that appears capable of satisfying the requested purpose, the actor must reuse, invoke, extend, compose with, or test that capability before constructing a replacement.

Discovery of an existing capability does not establish that the capability works. Its verification class must remain visible: FOUND, STATUS_CHECKED, END_TO_END_VERIFIED.

An actor may test an existing capability to establish whether it actually satisfies the present requirement.

## 4. Replacement Requires Concrete Mismatch

A new capability may be constructed despite an existing candidate only after the actor records a concrete mismatch between the required behavior and the existing capability.

A concrete mismatch must identify what the existing capability cannot do, why composition or bounded extension is insufficient, and what new capability is actually required.

Statements such as “a new version would be better,” “this is easier to rebuild,” “the existing system is unfamiliar,” or “the agent prefers another architecture” do not establish a concrete mismatch.

## 5. Duplicate and Ambiguous Capabilities

Discovery must not silently choose between ambiguous or duplicate capabilities.

Where multiple candidates exist, Atlas must preserve and expose them and identify any established canonical or successor relationship from existing evidence.

Canonical status may not be inferred solely from filename, modification date, size, apparent sophistication, or model preference.

## 6. Enforcement

`intake_before_build` or its governed successor becomes a required authorization gate for Atlas construction.

Any Atlas controlled construction path that can create a reusable capability must either invoke the intake gate directly before construction, or receive a valid prior intake decision associated with the proposed capability.

A construction path that cannot demonstrate a valid intake decision has no Atlas authority to construct.

## 7. Bypass

Failure to load a Cursor rule, startup document, Room interface, launcher catalog, or other orientation material does not waive this Order.

The obligation attaches to the construction action itself, not to a particular user interface or agent session.

## 8. Human Authority

The Human may expressly authorize construction without reuse when desired.

Such authorization must be recorded as a Human override and does not alter the underlying discovery record or establish that the existing capability was defective.

## 9. Evidence

Every intake decision must preserve enough evidence to determine: the requested purpose; the capabilities discovered; their verification classes; the reuse or mismatch determination; the selected capability or proposed construction; and any Human override.

Existing `ATLAS_RECORD/ATLAS_ROOM/reuse_decisions.jsonl` may serve as the decision record unless a governed successor is established.

## 10. Non Expansion of Authority

This Order authorizes discovery, inspection, status checking, and intake necessary to determine reuse.

It does not independently authorize paid generation, external communication, manuscript modification, deployment, execution of dangerous operations, or any other action requiring separate authority.

## 11. Implementation

Atlas shall identify every Atlas controlled path capable of constructing reusable capabilities and bind this Order to those paths.

Implementation should modify the smallest necessary enforcement surfaces.

Existing engines must not be rewritten merely to comply with this Order.

## 12. Acceptance Test

This Order is not fully implemented merely because catalogs, rules, or documentation mention it.

Implementation is demonstrated only when:

A. A fresh actor requesting an already existing capability is prevented from constructing a replacement without intake.

B. Discovery returns the existing capability by purpose.

C. A replacement attempt without a concrete mismatch is denied.

D. A replacement with a recorded concrete mismatch, or an explicit Human override, can proceed when otherwise authorized.

E. At least one construction route outside the Cursor orientation rule is tested, establishing that enforcement is attached to construction rather than merely agent instruction.
