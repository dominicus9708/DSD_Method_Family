# TRK-CH-005 — Strongest-Reasonable Non-DSD Tracking Baseline Result

Status: **EXECUTED — 68/72 / PRECOMMIT-FIXTURE FAILURE**  
Date: **2026-09-21**  
Case ID: `TRK-CH-005`  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen identities

```text
TRACKING_PROTOCOL_COMMIT:
  a0d979325c11919fecaa4d8eab129477a365af87

TRACKING_PROTOCOL_BLOB:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

PRECOMMIT_COMMIT:
  b410f63882fd311c24033e4527899023474ce7bc

PRECOMMIT_BLOB:
  fc408e2ee33a422964ed1c966d4a2e7edfce421b

BASELINE_ID:
  B1_STRONG_TYPED_TRACE_ENGINE
```

No frozen input, expected result, gain axis, or scoring item was rewritten after execution began.

## 2. Failure location

The failure is confined to R1-t1.

Frozen R1-t1 states:

```text
REL-v2:
  "USES" means REFERENCES
  and does not establish DEPENDS_ON

required query:
  A DEPENDS_ON L
```

The precommit expected:

```text
Tracking:
  TRACKING_LINK_EXPLICITLY_NEGATED
  TRACKING_TRACE_COMPLETE

B1:
  B1_EXPLICIT_NEGATIVE
  B1_TRACE_COMPLETE
```

That expectation is not licensed by the frozen Tracking Protocol v0.1.

Protocol v0.1 requires an explicitly negated relation to have applicable supplied evidence that explicitly supports non-occurrence/non-relation.

R1-t1 supplies only:

```text
the raw code maps to REFERENCES under REL-v2
and therefore does not establish DEPENDS_ON
```

It does not supply:

```text
an explicit evidence record stating
A does not DEPEND_ON L
```

Therefore the conformant Tracking result is:

```text
A DEPENDS_ON L:
  TRACKING_LINK_MISSING

TRACKING_TRACE_TERMINAL_STATUS:
  TRACKING_TRACE_PARTIAL
```

The strongest-reasonable B1 baseline, under its own frozen operation, reaches the equivalent result:

```text
A DEPENDS_ON L:
  B1_ABSENT_REQUIRED_LINK

terminal:
  B1_TRACE_PARTIAL
```

Preserved:

```text
NOT_ESTABLISHED != EXPLICITLY_NEGATED
MISSING_LINK != NEGATIVE_LINK
```

## 3. Why the precommit is not rewritten

The precommit is intentionally preserved.

Changing R1-t1 after observing the semantic mismatch would violate prospective challenge discipline.

Therefore:

```text
PRECOMMIT_REWRITTEN: no
POST_HOC_EXPECTATION_REPAIR: no
```

The failed expectation remains part of the evidence record.

## 4. R1 scoring

```text
B1 Tracking R1-t0 established:
  PASS

B2 B1 R1-t0 equivalent present:
  PASS

B3 Tracking R1-t1 explicitly negated:
  FAIL
  actual = TRACKING_LINK_MISSING

B4 B1 R1-t1 equivalent explicit negative:
  FAIL
  actual = B1_ABSENT_REQUIRED_LINK

B5 Tracking preserves version lock:
  PASS

B6 B1 preserves version lock:
  PASS

B7 Tracking no retroactive schema use:
  PASS

B8 B1 no retroactive schema use:
  PASS

B9 Tracking terminals complete:
  FAIL
  t1 actual = TRACKING_TRACE_PARTIAL

B10 B1 terminals complete:
  FAIL
  t1 actual = B1_TRACE_PARTIAL
```

R1 subtotal:

```text
6/10
```

Importantly, Tracking and B1 still agree with each other.

The failure is in the precommitted fixture expectation, not a Tracking-versus-baseline divergence.

## 5. R2 — graph topology

Both Tracking and B1 correctly preserve:

```text
S -> A,B branch
A,B -> M merge-shaped inclusion
X -> Y -> Z -> X reference cycle
X reaches Z by path
no unsupported direct X REFERENCES Z edge
no Lineage split/merge inference
no temporal/causal-cycle inference
```

Result:

```text
R2_CLAIM_RELEVANT_RESULT:
  BASELINE_MATCH

R2_SCORE:
  14/14 PASS
```

## 6. R3 — Reconstruction / Lineage boundary

Both systems preserve:

```text
D1 EDITED_TO D2:
  established/present

D2 COPIED_TO LEGACY:
  missing/absent-required-link

RC-1 / RC-2:
  reconstruction candidates only

LIN-1:
  explicit identity handoff retained

no reconstruction candidate promoted to historical fact
no Lineage identity inferred from EDITED_TO alone
terminal:
  partial
```

Result:

```text
R3_CLAIM_RELEVANT_RESULT:
  BASELINE_MATCH

R3_SCORE:
  12/12 PASS
```

## 7. R4 — temporal location/custody evolution

Both systems preserve the t0/t1 location and custody records without inferring:

```text
ownership
responsibility
causality
formation change
Lineage change
```

The artifact remains version v7.

Result:

```text
R4_CLAIM_RELEVANT_RESULT:
  BASELINE_MATCH

R4_SCORE:
  12/12 PASS
```

## 8. R5 — integrated unresolved states and loss sidecars

Both systems preserve:

```text
location relation:
  conflicting

dependency relation:
  underdetermined / unresolved-schema

CMP -> OUT handoff:
  blocked

run terminal:
  conflict / conflicting
```

The frozen precedence is preserved:

```text
CONFLICT
> UNRESOLVED
> BLOCKED
```

Both also retain:

```text
aggregate collision
noninjectivity
full-support reconstruction unavailable
compression discarded-support limitation
method-handoff provenance
```

Neither reconstructs lost support or selects a preferred unresolved branch.

Result:

```text
R5_CLAIM_RELEVANT_RESULT:
  BASELINE_MATCH

R5_SCORE:
  10/10 PASS
```

## 9. Comparative gain axes

Despite the fixture failure, the claim-relevant Tracking-versus-B1 comparisons themselves match on the executed records.

```text
G1 VERSION_AND_SCHEMA_GAIN:
  BASELINE_MATCH
  with corrected actual R1-t1 semantics

G2 GRAPH_TOPOLOGY_GAIN:
  BASELINE_MATCH

G3 RECONSTRUCTION_LINEAGE_BOUNDARY_GAIN:
  BASELINE_MATCH

G4 TEMPORAL_RELATION_GAIN:
  BASELINE_MATCH

G5 LOSS_AND_UNRESOLVED_GAIN:
  BASELINE_MATCH

G6 BOUNDED_MAXIMUM_CLAIM_GAIN:
  BASELINE_MATCH

G7 TRACEABILITY_GAIN:
  BASELINE_MATCH
```

However the precommitted challenge did not reach its pass threshold.

Therefore this artifact may not establish the strongest-reasonable baseline status.

```text
TRACKING_METHOD_GAIN_STATUS_FOR_CH005:
  NOT_ASSESSED_AS_SUCCESSFUL_BASELINE_CASE
```

## 10. Frozen scoring

```text
A immutable fairness:
  10/10

B R1 version semantics:
  6/10

C R2 graph topology:
  14/14

D R3 Reconstruction / Lineage boundary:
  12/12

E R4 temporal location/custody:
  12/12

F R5 integrated unresolved/loss:
  10/10

G comparative conclusion:
  4/4
```

Final:

```text
TOTAL_REQUIRED_CHECKS: 72
PASSED: 68
FAILED: 4

PASS_THRESHOLD: 72/72
CHALLENGE_RESULT:
  FAIL_PRECOMMIT_FIXTURE_EXPECTATION
```

## 11. Protocol pressure

The failure does not expose a contradiction in Tracking Protocol v0.1.

It exposes a stronger distinction already required by the protocol:

```text
NOT_ESTABLISHED != EXPLICITLY_NEGATED
MISSING_LINK != NEGATIVE_LINK
```

Therefore:

```text
PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no

FIXTURE_PRECOMMIT_CORRECTION_REQUIRED:
  yes
```

## 12. Counter discipline

The precommit authorized counter changes only on `72/72 PASS`.

Because this run scored `68/72`, no canonical Tracking counters are advanced by this artifact.

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED:
  remains 4 under the frozen counter rule

SUCCESSFUL_DIRECT_TRACKING_PILOTS:
  remains 4

BASELINE_TRACKING_CASES:
  remains 1

NO_GAIN_TRACKING_CASES:
  remains 1

STRONGEST_REASONABLE_BASELINE_TRACKING:
  not established
```

The failed artifact is preserved historically and must not be deleted or rewritten.

## 13. Maximum supported claim

TRK-CH-005 establishes that the original strongest-baseline precommit contained a fixture expectation error at R1-t1:

```text
"does not establish DEPENDS_ON"
was incorrectly precommitted as
"explicitly negates DEPENDS_ON"
```

The frozen Tracking protocol correctly resists that promotion.

The remaining R2-R5 comparisons matched the strong non-DSD baseline, but the challenge as a whole did not pass.

## 14. Next

Create a new corrective precommit without altering TRK-CH-005.

The corrective fixture must preserve R1-t1 as:

```text
Tracking:
  TRACKING_LINK_MISSING
  TRACKING_TRACE_PARTIAL

B1:
  B1_ABSENT_REQUIRED_LINK
  B1_TRACE_PARTIAL
```

and rerun the strongest-reasonable baseline comparison prospectively.
