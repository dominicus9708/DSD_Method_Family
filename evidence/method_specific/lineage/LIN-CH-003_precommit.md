# LIN-CH-003 — Direct Neighboring-Method Boundary Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-25**  
Challenge ID: `LIN-CH-003`  
Method: **Lineage / DSD 계보론**  
Protocol: **Lineage Protocol v0.1**

Frozen protocol identity:

```text
PROTOCOL_COMMIT:
  f69f364985d604d2c883b14b2efa18535a6bbf6e

PROTOCOL_BLOB:
  0ef686f3987b590e67e07b9ee5e4861c31e6e1ef
```

## 1. Purpose

Test whether Lineage collapses into neighboring methods when all methods receive fair access to the same shared artifact bundle.

The challenge tests eight Method Family neighbors and one foundational Dynamics source-layer handoff.

This is a fixture-bounded method-boundary test.

It is not a permanent irreducibility proof or method-survival vote.

## 2. Shared artifact bundle

Every comparison receives access to the same relevant constructed bundle:

```text
three ordered times:
  t0 < t1 < t2

formation/background records:
  B0 at t0,t1
  B1 at t2
  explicit B0 -> B1 formation transition

typed channel/component identity records

explicit channel/component lineage relations

identity-bearing component family

Tracking trace:
  t0 -> t1 -> t2

Transformation record:
  source-to-target carrier map with preservation/loss labels

Comparison record:
  structural correspondence and divergence profile

Classification record:
  class-membership criteria and assignments

Aggregation record:
  reduced readouts and support/collision sidecar

Compression record:
  retained-distinction set and reconstruction-limit sidecar

Reconstruction record:
  admissible missing-history candidates where direct lineage is absent

Audit record:
  frozen criteria and conformance evidence

Dynamics record:
  regular-epoch classification
  formation transition
  source-defined lineage primitives
```

No method may receive hidden claim-relevant evidence unavailable to another comparison participant.

Method-specific task questions and output contracts remain explicit; fair access does not require identical task contracts.

## 3. Five-interface non-collapse test

For each Method Family pair, compare:

```text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
```

Expected pair result:

```text
EXACT_COLLAPSE
or
PARTIAL_OVERLAP_NOT_COLLAPSE
or
UNRESOLVED_BOUNDARY
```

A pair is `EXACT_COLLAPSE` only if the frozen fixture shows no claim-relevant distinction across all five interfaces.

Shared artifacts, handoffs, or overlapping records do not by themselves imply collapse.

## 4. B1 — Lineage vs Tracking

Shared overlap:

```text
object identities
time/version records
transition records
typed relation provenance
```

Frozen distinction:

```text
Tracking operation:
  record where an artifact/state came from, went, and which evidence
  supports typed trace links

Lineage operation:
  decide predecessor/successor identity across change under
  canonical/supplied lineage and identity-bearing coverage rules
```

Outputs:

```text
Tracking:
  trace graph/path/link-status ledger

Lineage:
  successor-status / family-coherence / state-succession /
  interval-identity ledgers
```

Required guard:

```text
TRACKING_LINK != LINEAGE_SUCCESSOR_DECISION
TRACE_CONTINUITY != LINEAGE_IDENTITY
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 5. B2 — Lineage vs Reconstruction

Shared overlap:

```text
formation traces
lineage-related evidence
missing-history regions
provenance
```

Frozen distinction:

```text
Reconstruction:
  infer the set of prior/hidden structures or histories compatible
  with incomplete evidence

Lineage:
  evaluate a declared predecessor/successor identity claim from
  supplied admissible lineage interface
```

Required guard:

```text
RECONSTRUCTED_LINEAGE_CANDIDATE
  !=
ESTABLISHED_LINEAGE
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 6. B3 — Lineage vs Transformation

Shared overlap:

```text
source object
target object
mapping records
preservation/loss records
transition context
```

Frozen distinction:

```text
Transformation:
  execute/evaluate a declared source-to-target map and record
  preservation, change, merge, split, omission, addition, loss

Lineage:
  determine whether target objects/states are successors of
  predecessor objects/states
```

Required guard:

```text
TRANSFORMATION_MAPPING != SUCCESSOR_IDENTITY
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 7. B4 — Lineage vs Comparison

Shared overlap:

```text
same source/target structures
maps/correspondences
structural features
```

Frozen distinction:

```text
Comparison:
  determine correspondence, divergence, equivalence status,
  and first justified branch within declared comparison coverage

Lineage:
  determine directed predecessor/successor identity
```

Required guards:

```text
STRUCTURAL_EQUIVALENCE != LINEAGE_IDENTITY
SIMILAR_OUTPUT != SHARED_LINEAGE_OR_IDENTITY
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 8. B5 — Lineage vs Classification

Shared overlap:

```text
typed object descriptors
features
status records
optional dynamic descriptors
```

Frozen distinction:

```text
Classification:
  assign subjects to classes under frozen membership criteria

Lineage:
  decide individual predecessor/successor identity across change
```

Required guard:

```text
CLASS_MEMBERSHIP != INDIVIDUAL_SUCCESSOR_IDENTITY
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 9. B6 — Lineage vs Aggregation

Shared overlap:

```text
channel/property inputs
support descriptors
reduced readouts
```

Frozen distinction:

```text
Aggregation:
  construct declared representative/readout values and preserve
  aggregation-map, support, collision, and injectivity information

Lineage:
  decide predecessor/successor identity using lineage relations
  and identity-bearing coverage
```

Required guards:

```text
AGGREGATE_EQUALITY != LINEAGE_IDENTITY
AGGREGATE_INEQUALITY != LINEAGE_NONIDENTITY
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 10. B7 — Lineage vs Compression

Shared overlap:

```text
source representation
retained distinctions
loss/reconstruction sidecars
```

Frozen distinction:

```text
Compression:
  reduce representation while preserving distinctions required
  by a declared downstream purpose

Lineage:
  evaluate directed succession identity across change
```

Required guard:

```text
COMPRESSED_REPRESENTATION_CONTINUITY
  !=
LINEAGE_IDENTITY
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 11. B8 — Lineage vs Audit

Shared overlap:

```text
scope/version locks
evidence provenance
procedure records
lineage obligations
```

Frozen distinction:

```text
Audit:
  retrace a process/result under explicit criteria and issue
  a conformance/evidence verdict

Lineage:
  evaluate a predecessor/successor identity proposition
```

Required guard:

```text
LINEAGE_RESULT != GENERAL_AUDIT_VERDICT
AUDIT_CONFORMANCE != LINEAGE_IDENTITY
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 12. D1 — Lineage vs foundational Dynamics source layer

This is not counted as a Method Family pair.

Dynamics supplies foundational source semantics including:

```text
regular epoch
formation transition
channel-lineage relation
component-lineage relation
coherent lineage family
identity-bearing component family
lineage-connected state succession
```

Lineage method execution:

```text
freezes a declared identity question
checks the supplied source semantics operationally
emits typed successor/coherence/coverage/task-terminal records
```

It does not:

```text
derive the constitutive evolution law
invent a transition
invent a lineage relation
replace the foundational source definition
```

Expected source-layer result:

```text
SOURCE_HANDOFF_SEPARATION_ESTABLISHED_AT_FIXTURE_LEVEL
```

Guard:

```text
SOURCE_DEPENDENCY != METHOD_COLLAPSE
OPERATIONALIZATION != SOURCE_DEFINITION_REPLACEMENT
```

## 13. Precommitted checks — 72

Each of B1-B8 and D1 receives eight frozen checks.

### B1 Tracking — 8

```text
T1 same shared artifact access
T2 overlapping inputs acknowledged
T3 operation distinction preserved
T4 output-contract distinction preserved
T5 failure/terminal distinction preserved
T6 validation-standard distinction preserved
T7 typed handoff remains possible
T8 result = PARTIAL_OVERLAP_NOT_COLLAPSE
```

### B2 Reconstruction — 8

```text
R1 same shared artifact access
R2 overlapping inputs acknowledged
R3 operation distinction preserved
R4 output-contract distinction preserved
R5 failure/terminal distinction preserved
R6 validation-standard distinction preserved
R7 candidate-vs-established guard preserved
R8 result = PARTIAL_OVERLAP_NOT_COLLAPSE
```

### B3 Transformation — 8

```text
X1 same shared artifact access
X2 overlapping inputs acknowledged
X3 operation distinction preserved
X4 output-contract distinction preserved
X5 failure/terminal distinction preserved
X6 validation-standard distinction preserved
X7 map-vs-identity guard preserved
X8 result = PARTIAL_OVERLAP_NOT_COLLAPSE
```

### B4 Comparison — 8

```text
C1 same shared artifact access
C2 overlapping inputs acknowledged
C3 operation distinction preserved
C4 output-contract distinction preserved
C5 failure/terminal distinction preserved
C6 validation-standard distinction preserved
C7 equivalence/similarity-vs-lineage guard preserved
C8 result = PARTIAL_OVERLAP_NOT_COLLAPSE
```

### B5 Classification — 8

```text
K1 same shared artifact access
K2 overlapping inputs acknowledged
K3 operation distinction preserved
K4 output-contract distinction preserved
K5 failure/terminal distinction preserved
K6 validation-standard distinction preserved
K7 class-membership-vs-individual-identity guard preserved
K8 result = PARTIAL_OVERLAP_NOT_COLLAPSE
```

### B6 Aggregation — 8

```text
A1 same shared artifact access
A2 overlapping inputs acknowledged
A3 operation distinction preserved
A4 output-contract distinction preserved
A5 failure/terminal distinction preserved
A6 validation-standard distinction preserved
A7 aggregate-vs-lineage guard preserved
A8 result = PARTIAL_OVERLAP_NOT_COLLAPSE
```

### B7 Compression — 8

```text
P1 same shared artifact access
P2 overlapping inputs acknowledged
P3 operation distinction preserved
P4 output-contract distinction preserved
P5 failure/terminal distinction preserved
P6 validation-standard distinction preserved
P7 representation-continuity-vs-lineage guard preserved
P8 result = PARTIAL_OVERLAP_NOT_COLLAPSE
```

### B8 Audit — 8

```text
U1 same shared artifact access
U2 overlapping inputs acknowledged
U3 operation distinction preserved
U4 output-contract distinction preserved
U5 failure/terminal distinction preserved
U6 validation-standard distinction preserved
U7 audit-verdict-vs-lineage guard preserved
U8 result = PARTIAL_OVERLAP_NOT_COLLAPSE
```

### D1 Dynamics source layer — 8

```text
D1 same source artifact access
D2 source dependency acknowledged
D3 source definition vs method operation separated
D4 Dynamics transition/evolution role preserved
D5 Lineage operational-output role preserved
D6 no lineage relation invented by method
D7 no constitutive law inferred by Lineage
D8 result = SOURCE_HANDOFF_SEPARATION_ESTABLISHED_AT_FIXTURE_LEVEL
```

```text
PRECOMMITTED_REQUIRED_CHECKS: 72
```

## 14. Success criterion

A full pass requires:

```text
72/72 checks PASS

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED: 8

EXACT_COLLAPSE_PAIRS: 0
UNRESOLVED_BOUNDARY_PAIRS: 0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS: 8

DYNAMICS_SOURCE_LAYER_BOUNDARY_TESTS: 1
SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level

PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

This may establish only fixture-bounded separation.

```text
FIXTURE_BOUNDED_SEPARATION
  !=
PERMANENT_METHOD_IRREDUCIBILITY

BOUNDARY_NONCOLLAPSE
  !=
METHOD_SUPERIORITY

BOUNDARY_NONCOLLAPSE
  !=
PERMANENT_METHOD_SURVIVAL_PROOF
```

If all checks pass, update counters to:

```text
DIRECT_LINEAGE_PILOTS_ATTEMPTED: 3
SUCCESSFUL_DIRECT_LINEAGE_PILOTS: 3

METHOD_BOUNDARY_LINEAGE_CASES: 1

BASELINE_LINEAGE_CASES: 0
NO_GAIN_LINEAGE_CASES: 0
REPRODUCIBILITY_CASES: 0
```
