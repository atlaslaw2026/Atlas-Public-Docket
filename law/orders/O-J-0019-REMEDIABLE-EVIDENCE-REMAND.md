# O-J-0019-REMEDIABLE-EVIDENCE-REMAND

**Filing type:** USER ORDER  
**Date:** 2026-08-26  
**Implements / supplements:** J-0019, J-0020, O-J-0019-NOT-ACCEPTED-RESEARCH-REMAND, O-J-0019-REMAINING-GAP-ROOMS  
**Does not authorize live money.**  
**Does not create execution authority from a remand.**  
**Does not consume viewer/docket/INDEX.json next_docket_no 88.**

## Rule

When a governed room or validator reaches a nonterminal UNKNOWN because of a specific remediable evidence gap, Atlas shall convert that gap into canonical NEXT_REQUIRED work instead of stopping.

The originating room or validator shall identify: the missing proposition; why it is required; whether it is reasonably obtainable; and the appropriate evidence-producing room. Atlas shall route only that missing proposition to that room, validate the returned evidence through the existing validation path, and resume the interrupted dependency from the point of remand.

Do not hardcode HUNTER for every UNKNOWN. HUNTER is a lawful destination when it is the correct evidence-producing room (including Strategy Design research insufficiency that requires empirical comparative evidence).

Preserve UNKNOWN and stop when the gap is unavailable, unknowable, unauthorized, non-remediable, or outside scope. Do not reopen already PROVEN work unless new evidence materially requires reevaluation. Block repeated identical remands from looping.

Does not route EXECUTE, PAPER_FORWARD, broker, or fill while J-0019 is NOT_ACCEPTED.
