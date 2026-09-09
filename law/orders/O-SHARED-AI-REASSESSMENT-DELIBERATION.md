# O-SHARED-AI-REASSESSMENT-DELIBERATION

**Filing type:** USER ORDER  
**Date:** 2026-08-28  
**Adopts:** Human Order — shared Atlas AI reassessment and deliberation capability  
**Canonical id:** G-198  
**Implements / supplements:** AMENDED_DKT_1 (purpose and evidentiary floor only; Goal does not create this procedure), ATLAS_CONSTITUTION Articles I, II, III, XII, XIII, XIV, XVI, XVII, XVIII and Schedule A, J-0001, J-0018, J-0021  
**Does not create a new ACTIVE Judgment.** Disk ACTIVE judgment set remains pinned to `CURRENT_LAW.json` `current_sha`.  
**Does not authorize live money.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**  
**Does not special-case any project id.**  
**Does not alter J-0019.** Shared AI advice is not algorithm acceptance.  
**Does not choose NEXT_ACT.** NEXT_ACT remains `atlas_gov.rooms.runtime.compute_next_act`.  
**Does not expand room authority.** Advisory intelligence only.

## I. PURPOSE

Atlas is an AI research system intended to pursue a Goal by discovering and verifying information, developing and challenging possible solutions, testing its work, preserving what it learns, and continuing until it produces an auditable result.

The purpose of this Order is to ensure that every authorized Atlas room has access to shared AI intelligence when performing its assigned work, rather than being limited to a predetermined method, query, source, calculation, or approach.

A room's access to intelligence does not enlarge that room's authority.

## II. SHARED CAPABILITY

Every authorized Atlas room may invoke the shared Atlas AI reassessment and deliberation capability in furtherance of its assigned work.

A room may invoke the capability whenever additional reasoning may reasonably assist the room, including when:

the current approach has failed or been exhausted;
available evidence is incomplete, conflicting, ambiguous, or insufficient;
the room is uncertain how best to proceed;
an expected source, method, calculation, or test does not produce the expected result;
the room identifies a weakness, counterargument, alternative explanation, or unresolved question;
additional information may materially improve the work;
the room has completed an apparent task but reasonably questions whether the assigned work or Goal has actually been advanced; or
another reasonable approach may exist.

Invocation is not limited to failure conditions. A room may use the capability whenever additional intelligence would reasonably improve its work.

## III. SCOPE OF DELIBERATION

The shared AI capability may think broadly about how the calling room can better perform its assigned work.

It may, among other things:

formulate or challenge hypotheses;
identify alternative explanations;
propose different sources or information;
formulate searches or queries;
identify additional evidence that would be useful;
propose alternative retrieval or research methods;
propose calculations, mathematical models, comparisons, simulations, or tests;
identify weaknesses in existing reasoning or evidence;
identify assumptions and unknowns;
propose methods for testing or falsifying a conclusion;
reconsider an unsuccessful approach;
identify other available Atlas capabilities that may be useful;
compare competing approaches;
recommend that existing work be affirmed, revised, rejected, or investigated further; and
propose another legitimate means of accomplishing the calling room's assigned work.

Prior evidence and prior AI conclusions are inherited information, not boundaries on further inquiry.

This implements the research-cell principle that AI may retrieve, test, reconsider, and challenge existing work rather than automatically stopping when the first approach fails.

## IV. ROOM AUTHORITY IS NOT EXPANDED

The shared AI capability is advisory intelligence, not independent authority.

Neither invocation of the capability nor its output expands the authority of the calling room.

A room may act upon AI advice only when the proposed activity falls within that room's existing authority.

Accordingly, this Order alone does not authorize the AI capability or a calling room to:

amend or replace the Goal;
create, amend, disregard, or supersede law;
modify an operative Judgment or Order;
alter MAG authority or an operative MAG determination;
change routing or NEXT_ACT;
transfer authority between rooms;
change a substantive evidence requirement merely because satisfying it is difficult;
represent a hypothesis or unsupported inference as fact;
manufacture evidence;
bypass an applicable legal, regulatory, risk, integrity, or execution control; or
undertake consequential real-world action for which authority has not otherwise been granted.

The governing principle is:

Every room has access to intelligence. Each room retains only its existing authority.

## V. FREEDOM OF INTELLECTUAL INQUIRY

Within those authority boundaries, Atlas shall not unnecessarily prescribe the intellectual path by which AI performs the assigned work.

AI may search, compare, calculate, hypothesize, challenge, test, retrieve additional information, reconsider prior work, and try another legitimate approach.

Governance controls the boundary around the work; it does not prescribe every intellectual move occurring inside it. This is consistent with Atlas's Black-Globe operating model.

## VI. FAILURE OF AN APPROACH

Failure of a particular source, query, calculation, hypothesis, acquisition method, research path, or other approach does not by itself establish that the assigned work cannot be completed.

Where the assigned work remains incomplete, the calling room may use the shared AI capability to determine whether another reasonable approach exists within its authority.

A room should not repeatedly perform the same failed action merely to appear active.

Instead, it may reconsider the problem, investigate legitimate alternatives, and continue through another reasonable authorized path.

The existence of uncertainty is not itself a reason to stop.

A genuine governed blocker may be recognized where reasonable authorized inquiry has been undertaken and no legitimate path remains available within the room's authority.

## VII. TRUTH AND EVIDENCE DISCIPLINE

Intellectual freedom does not authorize factual invention.

When AI relies upon or produces material information, Atlas shall distinguish, as applicable:

source fact; calculation; empirical result; inference; assumption; hypothesis; and unknown.

Material factual claims must remain traceable to identifiable evidence.

Material numerical claims should be performed or reproducible through deterministic calculation where practical.

Hypotheses may be created freely but must remain identified as hypotheses until supported.

Unknown information shall remain unknown rather than being manufactured.

The governing principle is:

Think freely. Work toward the Goal. When you claim something is true, prove it.

This reflects Atlas's requirement that evidence, provenance, and the evolving work product survive when intelligence crosses back through the governance shell.

## VIII. PERSISTENCE AND AUDITABILITY

A material invocation of the shared AI capability shall leave an observable record sufficient to establish:

the calling room and assigned work; the problem or question presented; material information supplied to the capability; significant alternatives proposed; material new sources, calculations, tests, hypotheses, assumptions, or evidence introduced; the recommendation produced; what the calling room did with that recommendation; and the resulting outcome.

Atlas need not preserve private chain-of-thought.

It shall preserve the observable work, evidence, provenance, decisions, results, and useful learning necessary for another AI or the user to inspect and challenge the work.

## IX. RELATIONSHIP TO THE GOAL

The shared capability exists to help rooms perform their bounded assignments in service of the larger Atlas Goal.

Completion of an internal process, room, schema, retrieval attempt, calculation, or other intermediate step shall not by itself be confused with accomplishment of the underlying Goal.

Every Atlas AI should understand why its work exists while receiving only the information reasonably necessary for its assignment and retaining access to additional information when needed.

## X. EFFECT OF THIS ORDER

This Order makes the shared Atlas AI reassessment and deliberation capability available to every authorized Atlas room.

It does not replace Hunter, Librarian, Math, Watcher, Magistrate, consultation, evidence, execution, or other existing owners or capabilities.

It does not itself alter the substantive authority assigned to those components.

It instead establishes that specialized Atlas components may have access to intelligence while performing their respective jobs, subject to their existing authority and the applicable governance boundary.

The software implementation shall provide a common reusable interface rather than creating separate room-specific reasoning systems where the shared capability can reasonably serve the same function.

Nothing in this Order itself authorizes trading, financial execution, legal conclusions, communications, external actions, or other consequential conduct beyond authority otherwise granted.

IT IS SO ORDERED.

## Implementation

Common reusable interface: `atlas_gov.sdk.reassess` / `atlas_gov.sdk.deliberate` (`atlas_gov/sdk/advise.py`). Output is advisory, not authority. Persistence of advice records is `findings/sdk/advice/` when `persist=True`.

Capability-state findings G-194 and G-197 remain evidence that the callable is a packet-grounded prototype, not completed general deliberation. This Order authorizes invocation; it does not rewrite those findings and does not by itself complete remaining construction.
