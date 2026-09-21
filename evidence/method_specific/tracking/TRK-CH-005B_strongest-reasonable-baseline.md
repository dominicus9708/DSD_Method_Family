# TRK-CH-005B — Corrected Strongest-Reasonable Non-DSD Tracking Baseline Result

Status: **EXECUTED — 72/72 PASS / NO_GAIN**  
Date: **2026-09-21**  
Case ID: `TRK-CH-005B`  
Case class: `strongest_reasonable_baseline_constructed_corrective`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen identities

```text
TRACKING_PROTOCOL_COMMIT:
  a0d979325c11919fecaa4d8eab129477a365af87

TRACKING_PROTOCOL_BLOB:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

TRK-CH-005_PRECOMMIT_COMMIT:
  b410f63882fd311c24033e4527899023474ce7bc

TRK-CH-005_RESULT_COMMIT:
  89b7f183c1bb567c1c133221f91feddf9d7e85c9

CORRECTIVE_PRECOMMIT_COMMIT:
  d69b2e68d835854c1483fdcb6c87a61a81953ebe

CORRECTIVE_PRECOMMIT_BLOB:
  21c233dc9914e8327f587fe38973df13624f287a

BASELINE_ID:
  B1_STRONG_TYPED_TRACE_ENGINE
```

The failed TRK-CH-005 artifact remains unchanged.

No B1 capability was weakened.

## 2. Fairness result

```text
EQUAL_CLAIM_RELEVANT_INFORMATION: yes
B1_WEAKENED_POST_HOC: no
TRACKING_HIDDEN_FAVORABLE_INPUTS: 0
B1_WITHHELD_CLAIM_RELEVANT_INPUTS: 0
EXTERNAL_EVALUATOR_USED: no
EXTERNAL_APPLICATION_COUNTED: no
```

## 3. R1 — corrected version-scoped relation semantics

Frozen raw record:

```text
REC-1:
  edge_code = "USES"
  APP_A -> LIB_L
```

### REL-v1 / t0

```text
"USES" means DEPENDS_ON
```

Tracking:

```text
APP_A DEPENDS_ON LIB_L:
  TRACKING_LINK_ESTABLISHED

terminal:
  TRACKING_TRACE_COMPLETE
```

B1:

```text
APP_A DEPENDS_ON LIB_L:
  B1_PRESENT

terminal:
  B1_TRACE_COMPLETE
```

### REL-v2 / t1

```text
"USES" means REFERENCES
and does not establish DEPENDS_ON

explicit non-dependency evidence:
  absent
```

Tracking:

```text
APP_A DEPENDS_ON LIB_L:
  TRACKING_LINK_MISSING

terminal:
  TRACKING_TRACE_PARTIAL
```

B1:

```text
APP_A DEPENDS_ON LIB_L:
  B1_ABSENT_REQUIRED_LINK

terminal:
  B1_TRACE_PARTIAL
```

Both preserve:

```text
NOT_ESTABLISHED != EXPLICITLY_NEGATED
MISSING_LINK != NEGATIVE_LINK
SAME_RAW_RECORD != SAME_RELATION_SEMANTICS_ACROSS_SCHEMA_VERSIONS
LATER_SCHEMA != RETROACTIVE_SCHEMA_FOR_EARLIER_TASK
```

R1 result:

```text
BASELINE_MATCH
R1_SCORE: 10/10
```

## 4. R2 — branch / merge / cycle / direct-edge discipline

Supplied graph:

```text
S COPIED_TO A
S COPIED_TO B

A INCLUDED_IN M
B INCLUDED_IN M

X REFERENCES Y
Y REFERENCES Z
Z REFERENCES X
```

Both Tracking and B1 preserve:

```text
one-to-many branch
many-to-one inclusion topology
reference cycle
X -> Y -> Z reachability
no unsupported direct X REFERENCES Z edge
no Lineage split/merge inference
no temporal/causal-cycle inference
```

Both terminals:

```text
COMPLETE
```

R2 result:

```text
BASELINE_MATCH
R2_SCORE: 14/14
```

## 5. R3 — Reconstruction candidate / established history / Lineage handoff

Direct trace:

```text
D1 EDITED_TO D2
```

Unsupported historical query:

```text
D2 COPIED_TO LEGACY
```

Tracking:

```text
D1 EDITED_TO D2:
  TRACKING_LINK_ESTABLISHED

D2 COPIED_TO LEGACY:
  TRACKING_LINK_MISSING
```

B1:

```text
D1 EDITED_TO D2:
  B1_PRESENT

D2 COPIED_TO LEGACY:
  B1_ABSENT_REQUIRED_LINK
```

Both preserve RC-1 and RC-2 as reconstruction candidates only.

Both retain the explicit `LIN-1` Lineage identity handoff without deriving it from edit continuity.

```text
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
TRACE_CONTINUITY != LINEAGE_IDENTITY
```

Both terminals:

```text
PARTIAL
```

R3 result:

```text
BASELINE_MATCH
R3_SCORE: 12/12
```

## 6. R4 — temporal location/custody evolution

Frozen records:

```text
t0:
  ART STORED_IN BOX_A
  ART CUSTODY_HELD_BY ACTOR_A

t1:
  ART STORED_IN BOX_B
  ART CUSTODY_HELD_BY ACTOR_B
```

Both systems retain the time-indexed relation changes.

Neither infers:

```text
ownership
responsibility
causality
formation change
Lineage change
```

The artifact remains version v7.

Both terminals:

```text
COMPLETE
```

R4 result:

```text
BASELINE_MATCH
R4_SCORE: 12/12
```

## 7. R5 — integrated conflict / underdetermination / blockage / loss sidecars

Both systems preserve:

```text
location query:
  conflicting / conflict

dependency query:
  underdetermined / unresolved-schema

CMP -> OUT handoff:
  blocked
```

Both apply:

```text
CONFLICT
> UNRESOLVED
> BLOCKED
```

as the frozen run-level precedence.

Therefore both run terminals are the corresponding conflict terminal.

Both preserve:

```text
aggregate collision
noninjectivity
full-support reconstruction unavailable
compression discarded-support limitation
method-handoff provenance
```

Neither:

```text
reconstructs lost support
selects LOC_X or LOC_Y
selects DEP-A or DEP-B
calls the blocked handoff absent
claims Aggregation correctness
claims Compression correctness
```

R5 result:

```text
BASELINE_MATCH
R5_SCORE: 10/10
```

## 8. Gain-axis result

```text
G1 VERSION_AND_SCHEMA_GAIN:
  BASELINE_MATCH

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

Therefore:

```text
TRACKING_METHOD_GAIN_STATUS:
  NO_GAIN
```

The strong generic trace engine reproduced the claim-relevant Tracking outputs under equal information access.

No DSD-specific performance advantage was established in this strongest-reasonable constructed comparison.

## 9. NO_GAIN interpretation

```text
NO_GAIN
  means:
    no claim-relevant advantage over B1 was established
    for the frozen constructed tasks under equal information access
```

It does not mean:

```text
Tracking protocol failed
Tracking should be deleted
Tracking should merge into Lineage or Reconstruction
Tracking is permanently redundant
Tracking has no organizational or formal value
Tracking cannot show gain on another precommitted task
```

Preserved:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```

## 10. Frozen scoring

```text
A immutable fairness:
  10/10

B R1 version semantics:
  10/10

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
PASSED: 72
FAILED: 0
TOTAL: 72/72 PASS
```

## 11. Conformance and protocol pressure

```text
TRK-CH-005B_CONFORMANCE:
  CONFORMANT

TRACKING_METHOD_GAIN_STATUS:
  NO_GAIN

STRONGEST_REASONABLE_BASELINE_TRACKING:
  established_at_constructed_evidence_level

PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

The earlier CH005 failure remains a fixture/precommit expectation failure and is not erased by this corrective pass.

## 12. Counter update authorized by corrective precommit

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED:
  4 -> 5

SUCCESSFUL_DIRECT_TRACKING_PILOTS:
  4 -> 5

BASELINE_TRACKING_CASES:
  1 -> 2

NO_GAIN_TRACKING_CASES:
  1 -> 2

STRONGEST_REASONABLE_BASELINE_TRACKING:
  established_at_constructed_evidence_level
```

Unchanged:

```text
POSITIVE_TRACKING_CASES: 1
NEGATIVE_OR_FAILURE_TRACKING_CASES: 1
METHOD_BOUNDARY_TRACKING_CASES: 1

ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED: yes

REPRODUCIBILITY_CASES: 0

EXTERNAL_TRACKING_APPLICATIONS: 0
INDEPENDENT_TRACKING_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

TRACKING_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_TRACKING_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 13. Maximum supported claim

TRK-CH-005B establishes only:

```text
At the constructed-evidence level,
a strongest-reasonable generic typed trace engine
with equal claim-relevant information reproduced
the claim-relevant Tracking outputs across R1-R5.

No DSD-specific gain was established.
```

It does not establish external adequacy, independent validation, permanent redundancy, method merger, practical superiority/inferiority, or permanent registry status.

## 14. Next

Proceed to deterministic same-project retrace.

The retrace must reconstruct the CH005B claim-relevant ledger from immutable Protocol v0.1 plus the corrective precommit before comparing against this result.

A successful retrace remains same-project artifact consistency evidence, not independent replication.
