# O-J-0019-DISTINCT-RESEARCH-BRANCH-LOOP

**Filing type:** USER ORDER  
**Date:** 2026-08-27  
**Implements / supplements:** J-0019, J-0020, O-J-0019-NOT-ACCEPTED-RESEARCH-REMAND, O-J-0019-REMEDIABLE-EVIDENCE-REMAND, O-J-0019-HUNTER-EVIDENCE-HANDOFF, O-J-0020-AUTOMATIC-CONTINUATION  
**Does not authorize live money.**  
**Does not create execution authority from a research branch.**  
**Does not special-case any project id.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**

## Defect

A completed remediable-evidence cycle on one strategy-research branch could stop machine-authorized research (`IDENTICAL_EVIDENCE_REMAND` / no additional obtainable evidence on that cycle) while J-0019 remained NOT_ACCEPTED because no uniquely warrantable operative strategy had been frozen. Branch exhaustion was treated as project exhaustion.

## Rule

When J-0019 remains NOT_ACCEPTED because the current strategy-research branch produced no uniquely warrantable operative strategy, Atlas shall automatically close that branch as historical precedent and open a materially distinct governed strategy-research branch from canonical CURRENT_STATE.

Hunter shall investigate new strategy hypotheses, data relationships, portfolio-construction approaches, or other materially different research directions. Parameter retunes, cosmetic variants, and repeats of exhausted families are not distinct branches.

Each branch shall freeze its research design and acceptance tests before evaluation. It shall produce canonical evidence, route quantitative and qualitative items through the existing validation paths, return validated evidence to Strategy Design, and reevaluate J-0019.

If the new branch is also exhausted without ACCEPTED, Atlas shall repeat with another materially distinct branch. Continue until independently computed J-0019 ACCEPTED or a proven hard-stop: no materially distinct research directions remaining within scope; required data unavailable; exhausted authority; or another non-remediable constraint.

When a branch is exhausted and unused local research files do not themselves establish a new direction, Atlas shall first route a distinct-research-discovery task to Hunter. Hunter shall independently investigate the authorized research space for materially different strategy hypotheses, market relationships, data transformations, portfolio-construction methods, signal families, or other research directions not already represented by exhausted branches. Existing project files and prior branches are precedent and duplicate controls, not the universe of permissible new research.

Hunter shall canonically record candidate directions considered, evidence or reasoning supporting material distinctness, and why rejected directions are duplicative, trivial retunes, unavailable, unauthorized, or otherwise unsuitable. `NO_MATERIALLY_DISTINCT_DIRECTIONS` may be filed only if that governed discovery record establishes that no reasonably obtainable materially distinct direction remains within authorized scope. Exhaustion of restatements, price series, or already-used local artifacts is not that proof.

Otherwise Atlas shall freeze a new branch design and continue Hunter → canonical evidence filing → Math/Qualitative validation → Strategy Design → J-0019. An open branch whose Hunter cycle is complete, with no additional reasonably obtainable evidence on that branch, is exhausted: close it as precedent and continue discovery or a new distinct branch. Do not re-dispatch Hunter on that same exhausted branch. Catch-all residual classes are considered only after named authorized families. Closing a branch after an empty local-file scan does not exhaust that authorized class; existing files remain precedent, not the universe of the class.

Do not treat branch exhaustion as project exhaustion. Preserve all prior branches, evidence, failures, and already PROVEN states so later branches learn from them and do not repeat them. Precommitted standing tests may be inherited; they may not be weakened to manufacture acceptance.

Does not route EXECUTE, PAPER_FORWARD, broker, or fill while J-0019 is NOT_ACCEPTED.
