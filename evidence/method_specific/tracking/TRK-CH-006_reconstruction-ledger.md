# TRK-CH-006 Reconstruction Ledger — Deterministic Same-Project Retrace

Status: **RECONSTRUCTED FROM FROZEN DERIVATION BASIS / BEFORE FORMAL RESULT COMPARISON**  
Date: **2026-09-22**  
Case ID: `TRK-CH-006`

## 1. Frozen derivation basis

```text
P0 Tracking Protocol v0.1
commit: a0d979325c11919fecaa4d8eab129477a365af87
blob:   72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

P1 TRK-CH-005 original precommit
commit: b410f63882fd311c24033e4527899023474ce7bc
blob:   fc408e2ee33a422964ed1c966d4a2e7edfce421b

P1B TRK-CH-005B corrective precommit
commit: d69b2e68d835854c1483fdcb6c87a61a81953ebe
blob:   21c233dc9914e8327f587fe38973df13624f287a

TRK-CH-006 precommit
commit: 5afb654a259869ecf0caf1c2458d57648bdad391
blob:   abe172c341954795c3e2394399a0bbaa3d7ca783
```

Formal comparison against the frozen TRK-CH-005B result artifact is not performed in this ledger.

This ledger records only the regenerated Tracking-side consequences of P0 + P1 + P1B.

## 2. R1 reconstructed ledger — version-scoped relation semantics

### t0 / REL-v1

Frozen schema:

```text
"USES" -> DEPENDS_ON
```

Required query:

```text
APP_A DEPENDS_ON LIB_L
```

Reconstructed result:

```text
TRACKING_LINK_ESTABLISHED
TRACKING_TRACE_COMPLETE
```

### t1 / REL-v2

Frozen schema:

```text
"USES" -> REFERENCES
does not establish DEPENDS_ON
```

Explicit non-dependency evidence:

```text
absent
```

Prerequisites:

```text
available
```

Reconstructed result:

```text
TRACKING_LINK_MISSING
TRACKING_TRACE_PARTIAL
```

Preserved:

```text
NOT_ESTABLISHED != EXPLICITLY_NEGATED
MISSING_LINK != NEGATIVE_LINK
LATER_SCHEMA != RETROACTIVE_SCHEMA_FOR_EARLIER_TASK
```

## 3. R2 reconstructed ledger — branch / merge / cycle / reachability

Direct relations retained:

```text
S COPIED_TO A
S COPIED_TO B

A INCLUDED_IN M
B INCLUDED_IN M

X REFERENCES Y
Y REFERENCES Z
Z REFERENCES X
```

Derived graph facts allowed by the frozen protocol:

```text
branch:
  S -> A,B

merge-shaped inclusion:
  A,B -> M

reference cycle:
  X -> Y -> Z -> X

path reachability:
  X reaches Z through Y
```

Not created:

```text
X REFERENCES Z
```

because no transitive composition rule is supplied.

Not inferred:

```text
Lineage split
Lineage merger
temporal cycle
causal cycle
identity equivalence from graph connectivity
```

Reconstructed terminal:

```text
TRACKING_TRACE_COMPLETE
```

## 4. R3 reconstructed ledger — Reconstruction candidates and explicit Lineage handoff

Direct relation:

```text
D1 EDITED_TO D2
-> TRACKING_LINK_ESTABLISHED
```

Required historical query:

```text
D2 COPIED_TO LEGACY

direct support:
  absent

explicit negation:
  absent

prerequisites:
  available

-> TRACKING_LINK_MISSING
```

Reconstruction sidecar:

```text
RC-1:
  candidate D2 COPIED_TO LEGACY

RC-2:
  candidate D1 COPIED_TO LEGACY
```

Both remain:

```text
RECONSTRUCTED_OR_INFERRED_LINK
NOT_ESTABLISHED_AS_HISTORICAL_TRACE_LINK
```

Explicit Lineage handoff:

```text
LIN-1:
  predecessor = D1
  successor = D2
  identity-preservation verdict = PRESERVED
```

Tracking records LIN-1 as supplied.

Tracking does not derive LIN-1 from `D1 EDITED_TO D2`.

Preserved:

```text
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
TRACE_CONTINUITY != LINEAGE_IDENTITY
EXPLICIT_LINEAGE_HANDOFF != TRACKING-INFERRED_IDENTITY
```

Reconstructed terminal:

```text
TRACKING_TRACE_PARTIAL
```

## 5. R4 reconstructed ledger — temporal location/custody evolution

Frozen records:

```text
t0:
  ART STORED_IN BOX_A
  ART CUSTODY_HELD_BY ACTOR_A

t1:
  ART STORED_IN BOX_B
  ART CUSTODY_HELD_BY ACTOR_B
```

All four relations are retained as time-indexed established trace relations.

Artifact version remains:

```text
v7
```

Not inferred:

```text
ownership
responsibility
causality
formation change
Lineage change
```

Preserved:

```text
LOCATION_CHANGE != FORMATION_CHANGE
CUSTODY_RELATION != OWNERSHIP_RELATION
OWNERSHIP_RELATION != RESPONSIBILITY_RELATION
TEMPORAL_SUCCESSION != CAUSAL_LINK
LOCATION_OR_CUSTODY_CHANGE != LINEAGE_CHANGE
```

Reconstructed terminal:

```text
TRACKING_TRACE_COMPLETE
```

## 6. R5 reconstructed ledger — conflict / underdetermination / blockage / loss sidecars

Aggregation handoff:

```text
RAW METHOD_HANDOFF_TO AGG
source method: Aggregation
```

Aggregation sidecar retained:

```text
aggregate value = 0
support candidates = {+1,-1}, {0}
collision = yes
map = noninjective
full support reconstruction = unavailable
```

Compression handoff:

```text
AGG METHOD_HANDOFF_TO CMP
source method: Compression
```

Compression sidecar retained:

```text
aggregate value retained
collision-warning bit retained
discarded support detail not reconstructible from CMP alone
```

Location query:

```text
OUT STORED_IN ?

E1:
  OUT STORED_IN LOC_X at T0

E2:
  OUT STORED_IN LOC_Y at T0

exclusive-location schema:
  one location only at T0

precedence:
  none
```

Reconstructed status:

```text
TRACKING_LINK_CONFLICTING
```

Dependency query:

```text
OUT DEPENDS_ON CMP

DEP-A:
  dependency established

DEP-B:
  reference-only
  dependency query explicitly negative

both admissible
precedence:
  none
```

Reconstructed status:

```text
TRACKING_LINK_UNDERDETERMINED
```

Handoff query:

```text
CMP METHOD_HANDOFF_TO OUT

encrypted handoff record:
  exists

required decoder:
  unavailable
```

Reconstructed status:

```text
TRACKING_LINK_BLOCKED
```

Run-level terminal under frozen precedence:

```text
CONFLICTING
> UNDERDETERMINED
> BLOCKED

TRACKING_TRACE_CONFLICTING
```

Lower-level link statuses remain visible.

Not claimed:

```text
equal aggregate means equal support
full support reconstructed
Aggregation correctness
Compression correctness
true location selected
preferred dependency schema selected
blocked handoff absent
```

## 7. Reconstructed protocol-level record

```text
TRACKING_PROTOCOL_CONFORMANCE:
  CONFORMANT

PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 8. Reconstructed bounded-claim record

Maximum supported claim:

```text
The frozen Tracking protocol supports the typed relation/status,
graph-topology, unresolved-state, handoff, and bounded-terminal
judgments above under P0 + P1 + P1B.
```

Not established:

```text
truth
authenticity
causality
legal ownership/responsibility
Tracking-inferred Lineage identity
reconstruction truth
Transformation correctness
Aggregation correctness
Compression correctness
Audit success
external applicability
independent validation
independent replication
```

## 9. Reconstructed distinction ledger

```text
NOT_ESTABLISHED != EXPLICITLY_NEGATED
MISSING_LINK != NEGATIVE_LINK
PATH_REACHABILITY != DIRECT_TRACE_LINK
BRANCHING_TRACE != LINEAGE_BRANCHING_WITHOUT_HANDOFF
MERGING_TRACE != LINEAGE_MERGER_WITHOUT_HANDOFF
REFERENCE_CYCLE != TEMPORAL_CYCLE
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
TRACE_CONTINUITY != LINEAGE_IDENTITY
LOCATION_CHANGE != FORMATION_CHANGE
CUSTODY_RELATION != OWNERSHIP_RELATION
OWNERSHIP_RELATION != RESPONSIBILITY_RELATION
TEMPORAL_SUCCESSION != CAUSAL_LINK
EQUAL_AGGREGATE != EQUAL_SUPPORT
BLOCKED_LINK != MISSING_LINK
CONFLICTING_LINK != UNDERDETERMINED_LINK
```

## 10. Reconstruction freeze summary

```text
R1:
  t0 ESTABLISHED / COMPLETE
  t1 MISSING / PARTIAL

R2:
  topology preserved
  unsupported direct edge absent
  COMPLETE

R3:
  edit ESTABLISHED
  historical copy MISSING
  reconstruction candidates not promoted
  explicit Lineage handoff retained
  PARTIAL

R4:
  time-indexed location/custody retained
  no ownership/causality/formation/Lineage promotion
  COMPLETE

R5:
  location CONFLICTING
  dependency UNDERDETERMINED
  handoff BLOCKED
  run terminal CONFLICTING
  loss sidecars retained

TRACKING_PROTOCOL_CONFORMANCE:
  CONFORMANT

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

This ledger is now suitable for formal comparison against P2.

No post-comparison correction is authorized.
