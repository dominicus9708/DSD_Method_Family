# TRK-CH-005 Precommit — Strongest-Reasonable Non-DSD Tracking Baseline Comparison

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-21**  
Case ID: `TRK-CH-005`  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

```text
TRACKING_PROTOCOL_COMMIT:
  a0d979325c11919fecaa4d8eab129477a365af87

TRACKING_PROTOCOL_BLOB:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

TRACKING_PROTOCOL_VERSION:
  v0.1
```

No Tracking protocol revision is allowed in response to this comparison.

## 2. Strong baseline identity

```text
BASELINE_ID:
  B1_STRONG_TYPED_TRACE_ENGINE

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_trace_evaluator

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
```

B1 is deliberately stronger than the competent B0 baseline.

The comparison must not weaken B1 to manufacture DSD gain.

## 3. Frozen B1 capabilities

B1 may:

```text
1 lock target, task version, bounded scope, relation dimensions,
  finite query obligations, and completion rule;

2 preserve stable node identity, node version, type, domain,
  representation/schema identity, and human-readable labels separately;

3 maintain a typed directed multigraph with parallel edges,
  branch, merge, disconnected components, cycles, and self-reference
  where the relation schema permits;

4 distinguish a direct edge from path reachability and apply
  relation composition only when an explicit composition rule is supplied;

5 preserve relation-type, direction, relation-schema identity/version,
  validity time/snapshot, and relation scope;

6 keep relation claims separate from evidence/support records,
  evidence provenance, evidence version, and applicability;

7 distinguish:
  PRESENT,
  EXPLICIT_NEGATIVE,
  ABSENT_REQUIRED_LINK,
  AMBIGUOUS,
  CONFLICT,
  BLOCKED,
  NOT_APPLICABLE,
  OUTSIDE_SCOPE,
  UNRESOLVED_SCHEMA;

8 preserve multiple admissible relation-schema versions without
  selecting one post hoc when no precedence is supplied;

9 preserve version-scoped semantics without retroactively applying
  a later schema to an earlier frozen task;

10 preserve temporal order, process order, location, custody,
   ownership, responsibility, source, reference, dependency,
   causal handoff, and identity handoff as separately typed relations;

11 retain Transformation, Aggregation, Compression, Measurement,
   Reconstruction, Lineage, Interpretation, Audit, Comparison,
   and Analysis handoff records as typed sidecars/edges;

12 preserve aggregate/compression collision, information-loss,
   injectivity, reconstruction-limit, and provenance sidecars;

13 preserve Reconstruction candidates as candidates and distinguish them
   from directly established historical links;

14 retain explicit Lineage decisions when supplied,
   but not infer successor identity from continuity alone;

15 evaluate run-level completion using a predeclared precedence:
   OUTSIDE_SCOPE -> CONFLICT -> UNRESOLVED -> BLOCKED -> COMPLETE/PARTIAL;

16 emit a bounded maximum-supported-claim statement that does not
   infer truth, authenticity, causality, legal ownership/responsibility,
   successor identity, reconstruction truth, transformation correctness,
   audit success, or external adequacy unless separately supplied;

17 retain enough immutable intermediate records for deterministic retrace.
```

B1 may use ordinary graph algorithms, tables, finite traversal, reachability checks, typed ledgers, schema dispatch, and deterministic rule evaluation.

Extra computational competence is allowed.

Extra hidden factual information is not.

## 4. Equal-information rule

Tracking and B1 receive exactly the same claim-relevant:

```text
task identity/version
target
bounded scope
declared trace dimensions
finite required query set
completion rule
node IDs / versions / types / domains / labels
relation types / directions / schemas / schema versions
validity time/snapshot records
evidence/support records and provenance
support / explicit-negation / absence state
prerequisite / decoder / access availability
branch / merge / cycle topology
composition rules or explicit absence thereof
location / custody / ownership / responsibility records
method-handoff records
Transformation sidecars
Aggregation/Compression loss and collision sidecars
Reconstruction candidate records
Lineage handoffs
precedence rules or explicit absence thereof
```

No side receives hidden favorable information.

## 5. Frozen strong subcases

```text
R1 version-scoped relation semantics and non-retroactivity
R2 branch / merge / cycle / reachability discipline
R3 Reconstruction candidate versus established history plus Lineage handoff
R4 temporal location/custody evolution without causality/ownership promotion
R5 integrated conflict / underdetermination / blockage / loss-sidecar bounded claim
```

## 6. R1 — version-scoped relation semantics

Nodes:

```text
A = APP_A
L = LIB_L
```

One frozen raw metadata record:

```text
REC-1:
  edge_code = "USES"
  A -> L
```

Two schema versions:

```text
REL-v1:
  "USES" means DEPENDS_ON

REL-v2:
  "USES" means REFERENCES
  and does not establish DEPENDS_ON
```

Two separately frozen tasks:

```text
R1-t0:
  relation schema = REL-v1
  required query = A DEPENDS_ON L

R1-t1:
  relation schema = REL-v2
  required query = A DEPENDS_ON L
```

Expected Tracking:

```text
R1-t0:
  TRACKING_LINK_ESTABLISHED
  TRACKING_TRACE_COMPLETE

R1-t1:
  TRACKING_LINK_EXPLICITLY_NEGATED
  TRACKING_TRACE_COMPLETE
```

Expected B1:

```text
R1-t0:
  B1_PRESENT
  B1_TRACE_COMPLETE

R1-t1:
  B1_EXPLICIT_NEGATIVE
  B1_TRACE_COMPLETE
```

Required guards:

```text
SAME_RAW_RECORD != SAME_RELATION_SEMANTICS_ACROSS_SCHEMA_VERSIONS
LATER_SCHEMA != RETROACTIVE_SCHEMA_FOR_EARLIER_TASK
```

## 7. R2 — branch / merge / cycle / direct-edge discipline

Nodes:

```text
S
A
B
M
X
Y
Z
```

Supplied direct relations:

```text
S COPIED_TO A
S COPIED_TO B

A INCLUDED_IN M
B INCLUDED_IN M

X REFERENCES Y
Y REFERENCES Z
Z REFERENCES X
```

No transitive composition rule for `REFERENCES`.

Expected on both systems:

```text
branch S -> A,B retained
merge-shaped inclusion A,B -> M retained
reference cycle X -> Y -> Z -> X retained
X reaches Z by path
X REFERENCES Z direct edge not created
branch/merge topology not promoted to Lineage split/merge
reference cycle not promoted to temporal/causal cycle
```

Expected run status:

```text
all frozen direct queries resolved
-> COMPLETE
```

Required guards:

```text
PATH_REACHABILITY != DIRECT_TRACE_LINK
BRANCHING_TRACE != LINEAGE_BRANCHING_WITHOUT_HANDOFF
MERGING_TRACE != LINEAGE_MERGER_WITHOUT_HANDOFF
REFERENCE_CYCLE != TEMPORAL_CYCLE
GRAPH_CONNECTIVITY != IDENTITY
```

## 8. R3 — Reconstruction candidate versus established history plus Lineage handoff

Nodes:

```text
D1
D2
LEGACY
```

Direct trace evidence:

```text
D1 EDITED_TO D2
```

Required direct historical query:

```text
D2 COPIED_TO LEGACY
```

Direct support:

```text
absent
```

Explicit negation:

```text
absent
```

Prerequisites:

```text
available
```

Reconstruction sidecar:

```text
RC-1:
  candidate D2 COPIED_TO LEGACY

RC-2:
  candidate D1 COPIED_TO LEGACY

available evidence does not eliminate either
```

Separate explicit Lineage handoff:

```text
LIN-1:
  predecessor = D1
  successor = D2
  identity-preservation verdict = PRESERVED
```

Expected Tracking:

```text
D1 EDITED_TO D2:
  ESTABLISHED

D2 COPIED_TO LEGACY:
  MISSING

RC-1 / RC-2:
  retained in reconstructed/inferred sidecar
  not established as historical trace

LIN-1:
  retained as explicit Lineage handoff

Tracking itself does not derive LIN-1 from EDITED_TO
terminal:
  PARTIAL
```

Expected B1: claim-relevant match.

Required guards:

```text
MISSING_TRACE_LINK != LICENSE_TO_RECONSTRUCT
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
EXPLICIT_LINEAGE_HANDOFF != TRACKING-INFERRED_IDENTITY
TRACE_CONTINUITY != LINEAGE_IDENTITY
```

## 9. R4 — temporal location/custody evolution

Artifact:

```text
ART
version:
  v7 at t0 and t1
```

Supplied records:

```text
t0:
  ART STORED_IN BOX_A
  ART CUSTODY_HELD_BY ACTOR_A

t1:
  ART STORED_IN BOX_B
  ART CUSTODY_HELD_BY ACTOR_B
```

No ownership record.

No responsibility record.

No causal handoff.

No formation-change record.

Expected on both systems:

```text
t0 location/custody links retained
t1 location/custody links retained
location change retained as time-indexed relation change
custody change retained as time-indexed relation change
no ownership inferred
no responsibility inferred
no causality inferred
no formation change inferred
same artifact version retained
terminal = COMPLETE
```

Required guards:

```text
LOCATION_CHANGE != FORMATION_CHANGE
CUSTODY_RELATION != OWNERSHIP_RELATION
OWNERSHIP_RELATION != RESPONSIBILITY_RELATION
TEMPORAL_SUCCESSION != CAUSAL_LINK
LOCATION_OR_CUSTODY_CHANGE != LINEAGE_CHANGE
```

## 10. R5 — integrated unresolved states and loss sidecars

Nodes:

```text
RAW
AGG
CMP
OUT
LOC_X
LOC_Y
```

Supplied handoffs:

```text
RAW METHOD_HANDOFF_TO AGG
  source method: Aggregation

AGG METHOD_HANDOFF_TO CMP
  source method: Compression
```

Aggregation sidecar:

```text
aggregate value:
  0

support candidates:
  {+1,-1}
  {0}

collision:
  yes

map:
  noninjective

full support reconstruction:
  unavailable
```

Compression sidecar:

```text
CMP retains aggregate value
CMP retains collision-warning bit
discarded support detail is not reconstructible from CMP alone
```

Required location query at snapshot T0:

```text
OUT STORED_IN ?
```

Applicable evidence:

```text
E1: OUT STORED_IN LOC_X at T0
E2: OUT STORED_IN LOC_Y at T0
```

Schema:

```text
exactly one exclusive location at T0
```

No precedence.

Second required dependency query:

```text
OUT DEPENDS_ON CMP
```

Two admissible schema versions:

```text
DEP-A:
  supplied record establishes dependency

DEP-B:
  same supplied record means reference-only
  dependency query explicitly negative
```

No precedence.

Third required handoff query:

```text
CMP METHOD_HANDOFF_TO OUT
```

Encrypted handoff record exists but required decoder is unavailable.

Expected Tracking link states:

```text
location:
  CONFLICTING

dependency:
  UNDERDETERMINED

CMP -> OUT handoff:
  BLOCKED
```

Expected run terminal under frozen precedence:

```text
TRACKING_TRACE_CONFLICTING
```

because:

```text
CONFLICTING
precedes
UNDERDETERMINED
precedes
BLOCKED
```

Lower-level states remain visible.

B1 receives and uses the same terminal precedence.

Both systems must preserve:

```text
aggregate collision
noninjectivity
reconstruction unavailable
compression discarded-support limitation
method-handoff provenance
```

Neither may claim:

```text
equal aggregate => equal support
full support reconstructed
Aggregation correctness
Compression correctness
true location selected
preferred dependency schema selected
blocked handoff absent
```

## 11. Frozen gain axes

```text
G1 VERSION_AND_SCHEMA_GAIN
  DSD advantage only if R1 version-scoped semantics are handled more correctly.

G2 GRAPH_TOPOLOGY_GAIN
  DSD advantage only if R2 branch/merge/cycle/direct-edge semantics are handled more correctly.

G3 RECONSTRUCTION_LINEAGE_BOUNDARY_GAIN
  DSD advantage only if R3 candidate/history and explicit Lineage handoff boundaries
  are preserved more correctly.

G4 TEMPORAL_RELATION_GAIN
  DSD advantage only if R4 time-indexed location/custody changes are handled more correctly
  without ownership/causality/formation/Lineage overclaim.

G5 LOSS_AND_UNRESOLVED_GAIN
  DSD advantage only if R5 loss sidecars, conflict, underdetermination,
  blockage, and terminal precedence are preserved more correctly.

G6 BOUNDED_MAXIMUM_CLAIM_GAIN
  DSD advantage only if B1 makes a stronger unsupported claim from the same records.

G7 TRACEABILITY_GAIN
  DSD advantage only if a claim-relevant result cannot be deterministically retraced
  from B1's frozen intermediate ledger while it can from Tracking.
```

Allowed per-axis result:

```text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
```

Overall rule:

```text
if Tracking is nonconformant or wrong:
  FAIL

if Tracking is correct and at least one G1-G7 shows DSD advantage
while B1 remains a fair strongest-reasonable comparator:
  GAIN_ESTABLISHED

if Tracking and B1 are both correct and all G1-G7 are BASELINE_MATCH:
  NO_GAIN

otherwise:
  FAIL or UNRESOLVED according to the frozen evidence
```

Terminology, formatting, elegance, implementation speed, pedagogy, and external practical usefulness are not gain axes.

## 12. Frozen scoring — 72 checks

### A. Immutable fairness — 10

```text
A1 Tracking protocol commit/blob frozen
A2 B1 identity/capabilities frozen
A3 R1-R5 frozen before execution
A4 equal claim-relevant information supplied
A5 G1-G7 frozen
A6 scoring frozen
A7 B1 not weakened after precommit
A8 no hidden favorable input
A9 no external application/evaluator counted
A10 terminology difference not counted as gain
```

### B. R1 version semantics — 10

```text
B1 Tracking R1-t0 established
B2 B1 R1-t0 equivalent present
B3 Tracking R1-t1 explicitly negated
B4 B1 R1-t1 equivalent explicit negative
B5 Tracking preserves version lock
B6 B1 preserves version lock
B7 Tracking no retroactive schema use
B8 B1 no retroactive schema use
B9 Tracking terminals complete
B10 B1 terminals complete
```

### C. R2 graph topology — 14

```text
C1 Tracking branch retained
C2 B1 branch retained
C3 Tracking merge-shaped inclusion retained
C4 B1 merge-shaped inclusion retained
C5 Tracking reference cycle retained
C6 B1 reference cycle retained
C7 Tracking path reachability retained
C8 B1 path reachability retained
C9 Tracking unsupported direct X REFERENCES Z not created
C10 B1 unsupported direct edge not created
C11 Tracking branch/merge not promoted to Lineage
C12 B1 same no-identity overclaim
C13 Tracking terminal complete
C14 B1 terminal complete
```

### D. R3 Reconstruction / Lineage boundary — 12

```text
D1 Tracking edit link established
D2 B1 edit link present
D3 Tracking direct legacy query missing
D4 B1 equivalent absent-required-link
D5 Tracking RC-1/RC-2 retained as candidates
D6 B1 candidates retained as candidates
D7 Tracking no reconstructed link promoted
D8 B1 no candidate promoted
D9 Tracking explicit LIN-1 handoff retained
D10 B1 explicit identity handoff retained
D11 neither derives Lineage identity from edit continuity
D12 both terminals partial
```

### E. R4 temporal location/custody — 12

```text
E1 Tracking t0 location retained
E2 B1 t0 location retained
E3 Tracking t1 location retained
E4 B1 t1 location retained
E5 Tracking custody changes retained
E6 B1 custody changes retained
E7 neither infers ownership
E8 neither infers responsibility
E9 neither infers causality
E10 neither infers formation change
E11 neither infers Lineage change
E12 both terminals complete
```

### F. R5 integrated unresolved/loss case — 10

```text
F1 Tracking location conflicting
F2 B1 equivalent conflict
F3 Tracking dependency underdetermined
F4 B1 equivalent unresolved schema
F5 Tracking handoff blocked
F6 B1 equivalent blocked
F7 both preserve conflict > underdetermined > blocked terminal precedence
F8 both emit conflict run terminal
F9 both preserve aggregate/compression loss sidecars
F10 neither reconstructs lost support or selects preferred unresolved branch
```

### G. Comparative conclusion — 4

```text
G1 all seven frozen gain axes scored from claim-relevant results
G2 final gain status follows frozen rule
G3 strongest-reasonable status limited to constructed-evidence level
G4 NO_GAIN, if obtained, not interpreted as merger/deletion/absorption evidence
```

```text
TOTAL_REQUIRED_CHECKS: 72
PASS_THRESHOLD: 72/72
PARTIAL_PASS_ALLOWED: no
```

Any mismatch remains visible.

## 13. Evidence-count lock

Before execution:

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED: 4
SUCCESSFUL_DIRECT_TRACKING_PILOTS: 4
POSITIVE_TRACKING_CASES: 1
NEGATIVE_OR_FAILURE_TRACKING_CASES: 1
METHOD_BOUNDARY_TRACKING_CASES: 1
BASELINE_TRACKING_CASES: 1
NO_GAIN_TRACKING_CASES: 1

STRONGEST_REASONABLE_BASELINE_TRACKING:
  not established

REPRODUCIBILITY_CASES: 0
EXTERNAL_TRACKING_APPLICATIONS: 0
```

A `72/72 PASS` with final `NO_GAIN` may add exactly:

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

It does not increment reproducibility, external application, independent validation, or independent replication counters.

## 14. Next if passed

Proceed to deterministic same-project retrace from immutable Tracking protocol, CH005 precommit, and CH005 result artifacts.

A successful retrace remains same-project artifact-consistency evidence, not independent replication.
