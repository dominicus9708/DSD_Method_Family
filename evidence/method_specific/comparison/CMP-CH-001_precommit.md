# CMP-CH-001 Precommit / DSD 비교론 Positive Direct Challenge 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-10**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`

## 1. Evidence identity

```text
CASE_ID: CMP-CH-001
CASE_CLASS: positive_direct_comparison_challenge
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: none
```

Purpose: jointly test four legitimate positive Comparison outcomes without conflating them:

```text
T1 strict equivalence with sufficient closure
T2 direct correspondence weaker than strict equivalence
T3 encoded correspondence through a supplied bridge
T4 equal aggregate readout with justified structural non-equivalence
```

This case is not a baseline comparison. Method gain must remain `NOT_ASSESSED`.

## 2. Frozen task family

The challenge contains four independently frozen task instances. All use static supplied records only.

```text
TASK_FAMILY_ID: CMP-TASK-FAMILY-001
TARGET_DSD_LAYER_SCOPE:
  Formation-compatible structural records
  General Property status/value records where specified
  Static Aggregation readout only in T4
DYNAMIC_LINEAGE_SCOPE: not_used
LINEAGE_IDENTITY_CLAIM_POLICY: not_claimed
PRECOMPARISON_TRANSFORMATION_POLICY: none_required except supplied bridge in T3
EXTERNAL_STANDARD: not_used
DOMAIN_BRIDGE: not_used
AUXILIARY_METHODS_OR_HANDOFFS: Static Aggregation readout supplied only for T4
```

No task may infer Classification, Audit, Transformation, Design, Synthesis, Provenance, or Lineage verdicts.

## 3. Common comparison conventions

Every task records separately:

```text
MAP_FAMILY_COVERAGE
COMPARISON_ELEMENT_COVERAGE
MAP_PROPERTY_REQUIREMENT_PROFILE
REVERSE_DIRECTION_OR_INVERSE_POLICY
CORRESPONDENCE_CLASS_RESULT
STRUCTURAL_EQUIVALENCE_RESULT
TERMINAL_COMPARISON_STATUS
COMPARISON_PROTOCOL_CONFORMANCE
COMPARISON_METHOD_GAIN_STATUS
```

Property statuses are literal typed states:

```text
DEFINED_ZERO
DEFINED_NONZERO
APPLICABLE_BUT_UNDEFINED
```

No coercion of `APPLICABLE_BUT_UNDEFINED` to numeric zero is permitted.

## 4. T1 — strict equivalence with full closure

### 4.1 Subjects

```text
A1
  nodes: {a0,a1,a2}
  directed relations: {a0->a1, a1->a2}
  node Property readiness:
    a0 = DEFINED_ZERO
    a1 = DEFINED_NONZERO
    a2 = DEFINED_ZERO

B1
  nodes: {b0,b1,b2}
  directed relations: {b0->b1, b1->b2}
  node Property readiness:
    b0 = DEFINED_ZERO
    b1 = DEFINED_NONZERO
    b2 = DEFINED_ZERO
```

### 4.2 Frozen map and closure

```text
MAP_ID: f1
f1(a0)=b0
f1(a1)=b1
f1(a2)=b2
MAP_DIRECTION: A1->B1
MAP_FAMILY_COVERAGE: exhaustive relative to frozen singleton family {f1}
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
  inverse_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: required_and_supplied
inverse f1^-1(bi)=ai

COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive
  relations: exhaustive
  properties: exhaustive
  status_classes: exhaustive
  stages_or_layers: not_applicable

EQUIVALENCE_CRITERION:
  exact node-cardinality match
  bijective map
  forward and inverse relation preservation
  exact Property-status preservation at mapped nodes
```

### 4.3 Requested output and expected result

```text
CLAIMED_OUTPUT_LEVEL: STRICT_EQUIVALENCE_DECISION
EXPECTED_CORRESPONDENCE_CLASS: STRICT_EQUIVALENT
EXPECTED_STRUCTURAL_EQUIVALENCE_RESULT: yes
EXPECTED_TERMINAL: COMPARISON_RESOLVED
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

## 5. T2 — direct correspondence weaker than strict equivalence

### 5.1 Subjects

```text
A2
  nodes: {x0,x1}
  directed relations: {x0->x1}
  node Property readiness:
    x0 = DEFINED_ZERO
    x1 = DEFINED_NONZERO

B2
  nodes: {y0,y1,y2}
  directed relations: {y0->y1, y1->y2}
  node Property readiness:
    y0 = DEFINED_ZERO
    y1 = DEFINED_NONZERO
    y2 = DEFINED_ZERO
```

### 5.2 Frozen map and closure

```text
MAP_ID: f2
f2(x0)=y0
f2(x1)=y1
MAP_DIRECTION: A2->B2
MAP_FAMILY_COVERAGE: exhaustive relative to frozen singleton family {f2}
MAP_PROPERTY_REQUIREMENT_PROFILE:
  injective_required
  homomorphic_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: not_required

COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive over A2-domain and mapped B2 subset
  relations: exhaustive over A2-domain and mapped B2 subset
  properties: exhaustive over A2-domain and mapped B2 subset
  status_classes: exhaustive over A2-domain and mapped B2 subset
  stages_or_layers: not_applicable

CORRESPONDENCE_CRITERION:
  injective direct map
  mapped relation preservation
  mapped Property-status preservation
STRICT_EQUIVALENCE_CRITERION:
  would additionally require bijectivity/full target closure; not satisfied because y2 has no preimage
```

### 5.3 Requested output and expected result

```text
CLAIMED_OUTPUT_LEVEL: CORRESPONDENCE_CLASSIFICATION
EXPECTED_CORRESPONDENCE_CLASS: DIRECT_CORRESPONDENCE
EXPECTED_STRUCTURAL_EQUIVALENCE_RESULT: no
EXPECTED_UNRESOLVED_SET_FOR_REQUESTED_CLASS: none
EXPECTED_TERMINAL: COMPARISON_RESOLVED
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

The result must not be upgraded to `STRICT_EQUIVALENT`.

## 6. T3 — encoded correspondence through supplied bridge

### 6.1 Subjects and bridge

```text
A3
  states: {0,1}
  transition relation: {0->1}
  readiness:
    0 = DEFINED_ZERO
    1 = DEFINED_NONZERO

B3
  states: {OFF,ON}
  transition relation: {OFF->ON}
  readiness:
    OFF = DEFINED_ZERO
    ON = DEFINED_NONZERO

SUPPLIED_ENCODING_BRIDGE e:
  e(0)=OFF
  e(1)=ON
```

No literal direct-coordinate equality between `{0,1}` and `{OFF,ON}` is claimed.

### 6.2 Frozen map and closure

```text
MAP_ID: f3=e
MAP_DIRECTION: A3->B3
MAP_FAMILY_COVERAGE: exhaustive relative to frozen singleton bridge family {e}
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required within supplied encoded state sets
  relation_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: required_and_supplied
inverse e^-1(OFF)=0
e^-1(ON)=1
ENCODING_OR_BRIDGE_RULE: supplied bridge e required for claim-relevant correspondence
PRECOMPARISON_TRANSFORMATION_POLICY: supplied_transformed_representation not used; bridge remains an explicit Comparison encoding bridge
REPRESENTATION_PROVENANCE:
  original A3 labels {0,1}
  original B3 labels {OFF,ON}
  no relabeling performed outside supplied e

COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive through e
  relations: exhaustive through e
  properties: exhaustive through e
  status_classes: exhaustive through e
  stages_or_layers: not_applicable
```

### 6.3 Requested output and expected result

```text
CLAIMED_OUTPUT_LEVEL: CORRESPONDENCE_CLASSIFICATION
EXPECTED_CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
EXPECTED_STRUCTURAL_EQUIVALENCE_RESULT:
  equivalent_under_supplied_encoding_only
EXPECTED_TERMINAL: COMPARISON_RESOLVED
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

The result must not be relabeled `DIRECT_CORRESPONDENCE` merely because e is bijective.

## 7. T4 — equal aggregate, structurally different

### 7.1 Subjects and supplied readouts

```text
A4
  support: {p0,p1,p2}
  term values: {1,1,2}
  decomposition multiplicity: 3
  supplied aggregate readout: 4

B4
  support: {q0}
  term values: {4}
  decomposition multiplicity: 1
  supplied aggregate readout: 4
```

The supplied aggregate readouts come from an already completed Static Aggregation handoff. Comparison does not recompute or reinterpret them as structure.

### 7.2 Frozen map family and structural criterion

```text
CORRESPONDENCE_OR_MAP_FAMILY:
  all bijections between support(A4) and support(B4)
MAP_FAMILY_COVERAGE: exhaustive by cardinality argument
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: required for strict equivalence

COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive
  relations: not_applicable
  properties: exhaustive for supplied term values/multiplicity
  status_classes: not_applicable
  stages_or_layers: not_applicable

EQUIVALENCE_CRITERION:
  equal support cardinality
  bijective term-support correspondence
  exact term-value/decomposition preservation

AGGREGATE_READOUTS_IF_ANY:
  A4=4
  B4=4
AGGREGATE_COLLISION_POLICY:
  equal aggregate is recorded separately and is insufficient for structural equivalence
```

Because support cardinalities are 3 and 1, no bijection exists.

### 7.3 Requested output and expected result

```text
CLAIMED_OUTPUT_LEVEL: STRICT_EQUIVALENCE_DECISION
EXPECTED_AGGREGATE_READOUT_COMPARISON_RESULT: equal
EXPECTED_CORRESPONDENCE_CLASS: NONCORRESPONDENCE under the frozen strict structural family
EXPECTED_STRUCTURAL_EQUIVALENCE_RESULT: no
EXPECTED_TERMINAL: COMPARISON_RESOLVED
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

The equal aggregate must not be upgraded into common support, decomposition, or structure.

## 8. Frozen cross-task expectations

```text
T1: STRICT_EQUIVALENT
T2: DIRECT_CORRESPONDENCE, not strict equivalence
T3: ENCODED_CORRESPONDENCE, not relabeled direct
T4: aggregate equal + structural non-equivalence / NONCORRESPONDENCE

ALL TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
ALL COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
ALL COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Required distinctions:

```text
STRICT_EQUIVALENT != DIRECT_CORRESPONDENCE
DIRECT_CORRESPONDENCE != ENCODED_CORRESPONDENCE
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
INJECTIVE_EMBEDDING != BIJECTIVE_EQUIVALENCE
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
```

## 9. Precommitted scoring

Total required checks: **40**.

```text
A. immutable protocol / precommit discipline: 8
  A1 protocol commit fixed
  A2 four task instances fixed
  A3 subject records fixed
  A4 map/bridge families fixed
  A5 map-property requirements fixed
  A6 element coverage fixed
  A7 expected output/terminal/conformance/gain fixed
  A8 no post-hoc task or criterion revision

B. T1 strict-equivalence checks: 8
  B1 node/cardinality match
  B2 f1 bijective
  B3 forward relation preservation
  B4 inverse relation preservation
  B5 Property statuses preserved
  B6 STRICT_EQUIVALENT
  B7 COMPARISON_RESOLVED + CONFORMANT
  B8 gain NOT_ASSESSED

C. T2 weaker-direct checks: 8
  C1 f2 injective
  C2 mapped relation preserved
  C3 mapped Property statuses preserved
  C4 y2 remains outside image
  C5 DIRECT_CORRESPONDENCE
  C6 strict equivalence = no
  C7 COMPARISON_RESOLVED + CONFORMANT
  C8 gain NOT_ASSESSED

D. T3 encoded checks: 8
  D1 bridge e explicitly used
  D2 bridge bijective on supplied states
  D3 transition preserved through e
  D4 Property statuses preserved through e
  D5 ENCODED_CORRESPONDENCE
  D6 not relabeled DIRECT_CORRESPONDENCE
  D7 COMPARISON_RESOLVED + CONFORMANT
  D8 gain NOT_ASSESSED

E. T4 aggregate-collision checks: 8
  E1 aggregate readouts equal
  E2 support cardinalities differ
  E3 exhaustive bijection family closes by impossibility
  E4 no structural bijection
  E5 NONCORRESPONDENCE under frozen strict family / strict equivalence no
  E6 no reconstruction from aggregate equality
  E7 COMPARISON_RESOLVED + CONFORMANT
  E8 gain NOT_ASSESSED
```

Decision:

```text
40/40 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

A challenge failure does not imply method deletion, merger, or absorption. If the challenge design itself is defective, preserve the failed Case ID and correct prospectively under a new ID.

## 10. Evidence-count lock

Before execution:

```text
DIRECT_COMPARISON_PILOTS: 0
POSITIVE_COMPARISON_CASES: 0
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 0
BOUNDARY_COMPARISON_CASES: 0
NO_GAIN_COMPARISON_CASES: 0
BASELINE_COMPARISON_CASES: 0
```

A 40/40 PASS may add exactly:

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
POSITIVE_COMPARISON_CASE_INCREMENT: +1
```

It does not establish external applicability, baseline gain, reproducibility, independent validation, method maturity, or permanent method independence.
