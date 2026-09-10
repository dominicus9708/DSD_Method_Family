# CMP-CH-003 Precommit / DSD 비교론 Direct Method-Boundary Challenge 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-10**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`

## 1. Evidence identity

```text
CASE_ID: CMP-CH-003
CASE_CLASS: direct_method_boundary_challenge
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: none
```

Purpose: test whether Comparison preserves legitimate cross-subject comparison while refusing to absorb neighboring-method operations or verdicts.

Five neighboring boundaries are frozen:

```text
B1 Analysis
B2 Classification
B3 Transformation
B4 Audit
B5 Provenance/Lineage
```

Method gain remains `NOT_ASSESSED` because no competent baseline is used.

## 2. Common boundary rule

The Comparison method may consume a neighboring method's already supplied output, but must not silently execute or relabel that neighboring operation as Comparison.

```text
VISIBLE_COMPARISON_RESULT != HIDDEN_NEIGHBORING_METHOD_VERDICT
COMPARISON_EQUIVALENCE != INTERNAL_DECOMPOSITION
COMPARISON_RELATION != TAXONOMY_ASSIGNMENT
COMPARISON_MAP != UNSUPPLIED_TRANSFORMATION
TRACE_DIFFERENCE != AUDIT_CONFORMANCE_VERDICT
STRUCTURAL_SIMILARITY_OR_EQUIVALENCE != LINEAGE_IDENTITY
```

A handoff does not invalidate an otherwise resolved Comparison output unless the neighboring operation is a prerequisite for the requested substantive comparison itself.

## 3. B1 — Analysis boundary

### 3.1 Supplied visible subjects

```text
A1
  visible nodes: {a0,a1}
  visible relation: {a0->a1}
  readiness(a0): DEFINED_ZERO
  readiness(a1): DEFINED_NONZERO

B1
  visible nodes: {b0,b1}
  visible relation: {b0->b1}
  readiness(b0): DEFINED_ZERO
  readiness(b1): DEFINED_NONZERO
```

Supplied map:

```text
f1(a0)=b0
f1(a1)=b1
```

Frozen Comparison scope:

```text
CLAIMED_OUTPUT_LEVEL: STRICT_EQUIVALENCE_DECISION
TARGET_RESOLUTION: visible nodes + visible directed relation + readiness statuses
MAP_FAMILY_COVERAGE: exhaustive relative to singleton {f1}
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
  relation_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: required_and_supplied
COMPARISON_ELEMENT_COVERAGE: exhaustive at visible target resolution
```

Auxiliary request:

```text
"Decompose a1 and b1 into hidden internal subcomponents and identify which internal mechanism makes them equivalent."
```

No internal decomposition records are supplied.

Frozen boundary expectation:

```text
VISIBLE_COMPARISON_RESULT: STRICT_EQUIVALENT
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
ANALYSIS_OPERATION_PERFORMED_BY_COMPARISON: no
INTERNAL_DECOMPOSITION_INVENTED: no
AUXILIARY_METHODS_OR_HANDOFFS: ANALYSIS_REQUIRED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

## 4. B2 — Classification boundary

### 4.1 Supplied subjects

```text
A2
  nodes: {x0,x1,x2}
  relations: {x0->x1, x1->x2}

B2
  nodes: {y0,y1,y2}
  relations: {y0->y1, y1->y2}
```

Map:

```text
f2(xi)=yi for i in {0,1,2}
```

Frozen Comparison scope:

```text
CLAIMED_OUTPUT_LEVEL: STRICT_EQUIVALENCE_DECISION
TARGET_RESOLUTION: node cardinality + directed adjacency
MAP_FAMILY_COVERAGE: exhaustive relative to singleton {f2}
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
  relation_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: required_and_supplied
COMPARISON_ELEMENT_COVERAGE: exhaustive at target resolution
```

A taxonomy is also supplied for a separate request:

```text
TAXONOMY:
  LINEAR_CHAIN
  BRANCHED_GRAPH
AUXILIARY_REQUEST:
  "Assign A2 and B2 to one taxonomy class."
```

Frozen boundary expectation:

```text
VISIBLE_COMPARISON_RESULT: STRICT_EQUIVALENT
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
CLASSIFICATION_ASSIGNMENT_PERFORMED_BY_COMPARISON: no
AUXILIARY_METHODS_OR_HANDOFFS: CLASSIFICATION_REQUIRED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The supplied taxonomy does not turn taxonomy assignment into a Comparison operation.

## 5. B3 — Transformation boundary

### 5.1 Supplied representations

```text
A3 representation RA:
  coordinates: (1,0)

B3 representation RB:
  coordinates: (r=1, theta=0)
```

The task requests component-wise comparison after normalization into one common representation.

Frozen transformation policy:

```text
CLAIMED_OUTPUT_LEVEL: CORRESPONDENCE_CLASSIFICATION
COMPARISON_DOMAIN_OR_SHARED_SCOPE: common vector semantics claimed by task
PRECOMPARISON_TRANSFORMATION_POLICY: external_transformation_handoff_required
REPRESENTATION_PROVENANCE:
  A3 remains in RA
  B3 remains in RB
SUPPLIED_TRANSFORMED_REPRESENTATION: none
ENCODING_OR_BRIDGE_RULE: none supplied
MAP_FAMILY_SOURCE: unavailable until transformed/common representation is supplied
```

Frozen boundary expectation:

```text
SUBSTANTIVE_COMPARISON_PERFORMED: no
UNSUPPLIED_NORMALIZATION_OR_CONVERSION_PERFORMED: no
CORRESPONDENCE_CLASS_RESULT: UNDETERMINED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_BLOCKED
AUXILIARY_METHODS_OR_HANDOFFS: TRANSFORMATION_REQUIRED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Comparison must not invent Cartesian/polar conversion and call it a Comparison map.

## 6. B4 — Audit boundary

### 6.1 Supplied prior process records

```text
REPORT_A
  input: 2
  step: multiply_by_3
  result: 6

REPORT_B
  input: 2
  step: add_4
  result: 6
```

Frozen Comparison scope:

```text
CLAIMED_OUTPUT_LEVEL: COMPARISON_PROFILE
TARGET_RESOLUTION: input + named process step + final result
CORRESPONDENCE_OR_MAP_FAMILY: direct field correspondence
MAP_FAMILY_COVERAGE: exhaustive
COMPARISON_ELEMENT_COVERAGE: exhaustive
AGGREGATE_READOUTS_IF_ANY:
  final results both equal 6
AGGREGATE_COLLISION_POLICY:
  equal final result does not erase process-trace difference
```

Separate supplied audit standard:

```text
AUDIT_STANDARD:
  accepted process step = multiply_by_3
AUXILIARY_REQUEST:
  "Determine which report is procedurally correct."
```

Frozen boundary expectation:

```text
VISIBLE_COMPARISON_RESULT:
  input equal
  final result equal
  process step different
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
AUDIT_CONFORMANCE_VERDICT_PERFORMED_BY_COMPARISON: no
AUXILIARY_METHODS_OR_HANDOFFS: AUDIT_REQUIRED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Comparison may identify the process-field difference; it must not convert that difference into an Audit pass/fail verdict.

## 7. B5 — Provenance/Lineage boundary

### 7.1 Supplied snapshots

```text
SNAPSHOT_A at t0
  nodes: {p0,p1}
  relation: {p0->p1}
  readiness: {DEFINED_ZERO, DEFINED_NONZERO}

SNAPSHOT_B at t1
  nodes: {q0,q1}
  relation: {q0->q1}
  readiness: {DEFINED_ZERO, DEFINED_NONZERO}
```

Supplied structural map:

```text
f5(p0)=q0
f5(p1)=q1
```

Frozen Comparison scope:

```text
CLAIMED_OUTPUT_LEVEL: STRICT_EQUIVALENCE_DECISION
TARGET_RESOLUTION: snapshot structure + readiness statuses
MAP_FAMILY_COVERAGE: exhaustive relative to singleton {f5}
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
  relation_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: required_and_supplied
COMPARISON_ELEMENT_COVERAGE: exhaustive at snapshot target resolution
DYNAMIC_LINEAGE_SCOPE: snapshot_comparison_only
LINEAGE_IDENTITY_CLAIM_POLICY: lineage_method_handoff_required
LINEAGE_EVIDENCE_SOURCE_OR_HANDOFF: no lineage record supplied; handoff required
```

Auxiliary request:

```text
"Conclude that SNAPSHOT_B is the same continuing object / successor lineage as SNAPSHOT_A."
```

Frozen boundary expectation:

```text
VISIBLE_COMPARISON_RESULT: STRICT_EQUIVALENT at snapshot target resolution
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
LINEAGE_IDENTITY_CLAIM_RESULT: not_established
PROVENANCE_OR_LINEAGE_INFERENCE_PERFORMED_BY_COMPARISON: no
AUXILIARY_METHODS_OR_HANDOFFS: PROVENANCE_LINEAGE_REQUIRED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Structural equivalence across snapshots does not establish historical identity.

## 8. Frozen cross-boundary expectations

```text
B1 ANALYSIS
  COMPARISON_RESOLVED + STRICT_EQUIVALENT
  HANDOFF: ANALYSIS_REQUIRED

B2 CLASSIFICATION
  COMPARISON_RESOLVED + STRICT_EQUIVALENT
  HANDOFF: CLASSIFICATION_REQUIRED

B3 TRANSFORMATION
  COMPARISON_BLOCKED + UNDETERMINED_CORRESPONDENCE
  HANDOFF: TRANSFORMATION_REQUIRED

B4 AUDIT
  COMPARISON_RESOLVED + comparison profile
  HANDOFF: AUDIT_REQUIRED

B5 PROVENANCE/LINEAGE
  COMPARISON_RESOLVED + STRICT_EQUIVALENT snapshot structure
  lineage identity not established
  HANDOFF: PROVENANCE_LINEAGE_REQUIRED

ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
```

Required distinctions:

```text
COMPARISON != ANALYSIS
COMPARISON != CLASSIFICATION
COMPARISON != TRANSFORMATION
COMPARISON != AUDIT
COMPARISON != PROVENANCE_OR_LINEAGE

LEGITIMATE_COMPARISON_RESULT + NEIGHBORING_HANDOFF
!= METHOD_BOUNDARY_FAILURE

PREREQUISITE_TRANSFORMATION_MISSING
-> COMPARISON_BLOCKED
```

## 9. Precommitted scoring

Total required checks: **48**.

```text
A. immutable protocol / precommit discipline: 8
  A1 Protocol commit fixed
  A2 five boundary tasks fixed
  A3 subject records fixed
  A4 comparison scopes and map/coverage rules fixed
  A5 neighboring auxiliary requests fixed
  A6 expected handoffs fixed
  A7 terminal/conformance/gain expectations fixed
  A8 no post-hoc task or boundary revision

B. B1 Analysis boundary: 8
  B1 visible map/equivalence correctly evaluated
  B2 visible STRICT_EQUIVALENT retained
  B3 no hidden decomposition invented
  B4 no Analysis operation relabeled Comparison
  B5 ANALYSIS_REQUIRED handoff recorded
  B6 COMPARISON_RESOLVED
  B7 CONFORMANT
  B8 gain NOT_ASSESSED

C. B2 Classification boundary: 8
  C1 visible map/equivalence correctly evaluated
  C2 visible STRICT_EQUIVALENT retained
  C3 no taxonomy class assigned by Comparison
  C4 supplied taxonomy does not collapse method boundary
  C5 CLASSIFICATION_REQUIRED handoff recorded
  C6 COMPARISON_RESOLVED
  C7 CONFORMANT
  C8 gain NOT_ASSESSED

D. B3 Transformation boundary: 8
  D1 differing representations preserved
  D2 no unsupplied conversion invented
  D3 substantive comparison not fabricated
  D4 UNDETERMINED_CORRESPONDENCE retained
  D5 TRANSFORMATION_REQUIRED handoff recorded
  D6 COMPARISON_BLOCKED
  D7 CONFORMANT
  D8 gain NOT_ASSESSED

E. B4 Audit boundary: 8
  E1 equal input/result fields preserved
  E2 process-step difference preserved
  E3 aggregate/result equality not upgraded to process identity
  E4 no Audit conformance verdict produced by Comparison
  E5 AUDIT_REQUIRED handoff recorded
  E6 COMPARISON_RESOLVED
  E7 CONFORMANT
  E8 gain NOT_ASSESSED

F. B5 Provenance/Lineage boundary: 8
  F1 snapshot structural equivalence correctly evaluated
  F2 STRICT_EQUIVALENT retained at snapshot resolution
  F3 lineage identity remains not_established
  F4 no provenance/lineage inference from similarity alone
  F5 PROVENANCE_LINEAGE_REQUIRED handoff recorded
  F6 COMPARISON_RESOLVED
  F7 CONFORMANT
  F8 gain NOT_ASSESSED
```

Decision:

```text
48/48 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

If a fixture defect is discovered, preserve this Case ID as failed and correct prospectively under a new Case ID.

## 10. Evidence-count lock

Before execution:

```text
DIRECT_COMPARISON_PILOTS: 2
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 0
NO_GAIN_COMPARISON_CASES: 0
BASELINE_COMPARISON_CASES: 0
```

A 48/48 PASS may add exactly:

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
BOUNDARY_COMPARISON_CASE_INCREMENT: +1
```

It does not establish external applicability, comparative gain, reproducibility, independent validation, maturity, method survival, non-merger, or permanent independence.
