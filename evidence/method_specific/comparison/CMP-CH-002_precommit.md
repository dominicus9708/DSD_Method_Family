# CMP-CH-002 Precommit / DSD 비교론 Negative-Failure Terminal Distinction 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-10**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`

## 1. Evidence identity

```text
CASE_ID: CMP-CH-002
CASE_CLASS: negative_failure_terminal_distinction
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: none
```

Purpose: distinguish negative/failure terminal states and prevent unsupported closure.

```text
N1 non-exhaustive map family -> COMPARISON_UNDERDETERMINED
N2 partial element coverage -> COMPARISON_UNDERDETERMINED
N3 missing required semantic bridge -> COMPARISON_BLOCKED
N4 required inverse/reverse evidence missing after forward comparison -> COMPARISON_UNDERDETERMINED
N5 exhaustive map family all fail -> COMPARISON_RESOLVED + NONCORRESPONDENCE
```

Method gain must remain `NOT_ASSESSED` because no competent baseline is used.

## 2. Common rules

All tasks are static and supplied before execution.

```text
DYNAMIC_LINEAGE_SCOPE: not_used
LINEAGE_IDENTITY_CLAIM_POLICY: not_claimed
EXTERNAL_STANDARD: not_used
AUXILIARY_METHODS_OR_HANDOFFS: none
```

Required guards:

```text
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
SUBSTANTIVE_PARTIAL_COMPARISON != REQUESTED_CLOSURE
EXHAUSTIVE_ALL_MAP_FAILURE != NONEXHAUSTIVE_FAILURE_TO_FIND
```

## 3. N1 — non-exhaustive map family

### 3.1 Subjects

```text
A1
  nodes: {a0,a1}
  directed relation: {a0->a1}

B1
  nodes: {b0,b1}
  directed relation: {b0->b1}
```

### 3.2 Frozen map family

Admissible family is frozen as:

```text
F1 = {f11,f12}

f11(a0)=b1
f11(a1)=b0

f12(a0)=b0
f12(a1)=b1
```

Only `f11` is evaluated in this run.

```text
MAP_FAMILY_COVERAGE: non_exhaustive
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
  relation_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: not_required for requested correspondence classification
COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive for evaluated f11
  relations: exhaustive for evaluated f11
  properties: not_applicable
  status_classes: not_applicable
  stages_or_layers: not_applicable
```

`f11` is bijective but fails directed-relation preservation because `a0->a1` maps to `b1->b0`, which is absent.
`f12` remains untested and would be admissible to test under the frozen family.

### 3.3 Expected result

```text
CLAIMED_OUTPUT_LEVEL: CORRESPONDENCE_CLASSIFICATION
EVALUATED_MAP_RESULT_f11: failure_relation_preservation
UNTESTED_MAP_SET: {f12}
EXPECTED_CORRESPONDENCE_CLASS: UNDETERMINED_CORRESPONDENCE
EXPECTED_STRUCTURAL_EQUIVALENCE_RESULT: underdetermined
EXPECTED_TERMINAL: COMPARISON_UNDERDETERMINED
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

A failed `f11` must not be promoted to global noncorrespondence.

## 4. N2 — partial element coverage

### 4.1 Subjects

```text
A2
  nodes: {x0,x1}
  relation: {x0->x1}
  readiness:
    x0 = DEFINED_ZERO
    x1 = DEFINED_NONZERO

B2
  nodes: {y0,y1}
  relation: {y0->y1}
  readiness:
    y0 = DEFINED_ZERO
    y1 = RECORD_WITHHELD
```

### 4.2 Frozen map and coverage

```text
f2(x0)=y0
f2(x1)=y1
MAP_FAMILY_COVERAGE: exhaustive relative to frozen singleton {f2}
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
  relation_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: required_and_supplied
inverse f2^-1(yi)=xi

COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive
  relations: exhaustive
  properties: partial
  status_classes: partial
  stages_or_layers: not_applicable

CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL:
  STRICT_EQUIVALENCE_DECISION requires all claim-relevant Property/status conditions closed
```

The map and relation structure close, but `B2.y1` readiness is withheld.

### 4.3 Expected result

```text
CLAIMED_OUTPUT_LEVEL: STRICT_EQUIVALENCE_DECISION
PRESERVED_STRUCTURAL_SUBSET: nodes + relation + supplied y0 readiness
UNRESOLVED_SET: {readiness(y1)}
EXPECTED_CORRESPONDENCE_CLASS: UNDETERMINED_CORRESPONDENCE
EXPECTED_STRUCTURAL_EQUIVALENCE_RESULT: underdetermined
EXPECTED_TERMINAL: COMPARISON_UNDERDETERMINED
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

The run must not upgrade partial element coverage to strict equivalence.

## 5. N3 — missing required bridge

### 5.1 Subjects

```text
A3
  states: {0,1}
  transition: {0->1}

B3
  states: {COLD,HOT}
  transition: {COLD->HOT}
```

The task explicitly declares that literal labels are not a shared semantic coordinate system.
A semantic state bridge is required before substantive cross-domain correspondence can be evaluated.

### 5.2 Frozen bridge policy

```text
ENCODING_OR_BRIDGE_RULE:
  claim_required_semantic_bridge
BRIDGE_SUPPLIED: no
MAP_FAMILY_SOURCE: unavailable until bridge is supplied
MAP_FAMILY_COVERAGE: unknown
PRECOMPARISON_TRANSFORMATION_POLICY: transformation_not_permitted_in_comparison
REPRESENTATION_PROVENANCE:
  original A3 and B3 representations retained
```

### 5.3 Expected result

```text
CLAIMED_OUTPUT_LEVEL: CORRESPONDENCE_CLASSIFICATION
SUBSTANTIVE_MAP_EVALUATION_PERFORMED: no
EXPECTED_CORRESPONDENCE_CLASS: UNDETERMINED_CORRESPONDENCE
EXPECTED_STRUCTURAL_EQUIVALENCE_RESULT: not_evaluated
EXPECTED_TERMINAL: COMPARISON_BLOCKED
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

The missing bridge must not be relabeled as structural difference or noncorrespondence.

## 6. N4 — forward success but required inverse evidence absent

### 6.1 Subjects

```text
A4
  nodes: {u0,u1}
  relation: {u0->u1}

B4
  nodes: {v0,v1}
  relation: {v0->v1}
```

### 6.2 Frozen forward map and inverse policy

```text
f4(u0)=v0
f4(u1)=v1
MAP_FAMILY_COVERAGE: exhaustive relative to frozen singleton {f4}
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
  forward_relation_preservation_required
  inverse_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: required_but_unverified

COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive
  relations: exhaustive in forward direction
  properties: not_applicable
  status_classes: not_applicable
  stages_or_layers: not_applicable

CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL:
  STRICT_EQUIVALENCE_DECISION requires inverse/reverse preservation evidence
```

The supplied forward map is bijective and preserves the forward relation.
No inverse/reverse preservation record is supplied and this run is not permitted to invent one.

### 6.3 Expected result

```text
CLAIMED_OUTPUT_LEVEL: STRICT_EQUIVALENCE_DECISION
FORWARD_MAP_RESULT: success
REVERSE_OR_INVERSE_RESULT: required_but_unverified
UNRESOLVED_SET: {inverse_preservation}
EXPECTED_CORRESPONDENCE_CLASS: UNDETERMINED_CORRESPONDENCE
EXPECTED_STRUCTURAL_EQUIVALENCE_RESULT: underdetermined
EXPECTED_TERMINAL: COMPARISON_UNDERDETERMINED
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

Forward success must not establish the stronger symmetric/inverse claim.

## 7. N5 — exhaustive all-map failure gives resolved noncorrespondence

### 7.1 Subjects

```text
A5
  nodes: {m0,m1}
  directed relation: {m0->m1}

B5
  nodes: {n0,n1}
  directed relations: {}
```

### 7.2 Frozen exhaustive map family

All bijections between the two 2-element sets are enumerated:

```text
g1(m0)=n0, g1(m1)=n1
g2(m0)=n1, g2(m1)=n0

MAP_FAMILY_COVERAGE: exhaustive
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
  relation_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: not_required beyond the frozen noncorrespondence criterion

COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive
  relations: exhaustive
  properties: not_applicable
  status_classes: not_applicable
  stages_or_layers: not_applicable

NONCORRESPONDENCE_CRITERION:
  no bijection in the exhaustive frozen family preserves every A5 directed relation in B5
```

Both `g1` and `g2` fail because `B5` contains no directed relation.

### 7.3 Expected result

```text
CLAIMED_OUTPUT_LEVEL: CORRESPONDENCE_CLASSIFICATION
EVALUATED_MAP_RESULTS:
  g1 -> relation preservation fail
  g2 -> relation preservation fail
UNTESTED_MAP_SET: none
EXPECTED_CORRESPONDENCE_CLASS: NONCORRESPONDENCE
EXPECTED_STRUCTURAL_EQUIVALENCE_RESULT: no
EXPECTED_TERMINAL: COMPARISON_RESOLVED
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

This is the contrast case showing that sufficient exhaustive failure can legitimately close noncorrespondence.

## 8. Frozen cross-task terminal distinctions

```text
N1 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
N2 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
N3 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_BLOCKED
N4 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
N5 -> NONCORRESPONDENCE / COMPARISON_RESOLVED

ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
```

Required distinctions:

```text
NONEXHAUSTIVE_MAP_FAILURE != RESOLVED_NONCORRESPONDENCE
PARTIAL_ELEMENT_COVERAGE != STRICT_EQUIVALENCE
MISSING_REQUIRED_BRIDGE != PROVEN_DIFFERENCE
FORWARD_SUCCESS != INVERSE_PRESERVATION
UNDERDETERMINED != BLOCKED
RESOLVED_NONCORRESPONDENCE != UNDERDETERMINED_FAILURE_TO_FIND
```

## 9. Precommitted scoring

Total required checks: **48**.

```text
A. immutable protocol / precommit discipline: 8
  A1 protocol commit fixed
  A2 five task instances fixed
  A3 subject records fixed
  A4 map/bridge families and coverage fixed
  A5 map-property / inverse requirements fixed
  A6 element coverage fixed
  A7 expected output/terminal/conformance/gain fixed
  A8 no post-hoc task or criterion revision

B. N1 non-exhaustive-map checks: 8
  B1 f11 evaluated
  B2 f11 relation failure preserved
  B3 f12 remains explicitly untested
  B4 no global noncorrespondence claim
  B5 UNDETERMINED_CORRESPONDENCE
  B6 COMPARISON_UNDERDETERMINED
  B7 CONFORMANT
  B8 gain NOT_ASSESSED

C. N2 partial-element checks: 8
  C1 f2 bijective and structural relation preserved
  C2 readiness(y1) withheld
  C3 Property/status coverage remains partial
  C4 strict equivalence not closed
  C5 UNDETERMINED_CORRESPONDENCE
  C6 COMPARISON_UNDERDETERMINED
  C7 CONFORMANT
  C8 gain NOT_ASSESSED

D. N3 missing-bridge checks: 8
  D1 bridge required by frozen task
  D2 bridge absent
  D3 substantive map comparison not fabricated
  D4 no difference/noncorrespondence inferred
  D5 UNDETERMINED_CORRESPONDENCE
  D6 COMPARISON_BLOCKED
  D7 CONFORMANT
  D8 gain NOT_ASSESSED

E. N4 inverse-evidence checks: 8
  E1 forward f4 success
  E2 inverse preservation required
  E3 inverse evidence absent/unverified
  E4 strict equivalence not closed
  E5 UNDETERMINED_CORRESPONDENCE
  E6 COMPARISON_UNDERDETERMINED
  E7 CONFORMANT
  E8 gain NOT_ASSESSED

F. N5 exhaustive-noncorrespondence checks: 8
  F1 g1 evaluated and fails relation preservation
  F2 g2 evaluated and fails relation preservation
  F3 exhaustive family coverage confirmed
  F4 no untested map remains
  F5 NONCORRESPONDENCE
  F6 COMPARISON_RESOLVED
  F7 CONFORMANT
  F8 gain NOT_ASSESSED
```

Decision:

```text
48/48 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

If a fixture defect is discovered, preserve this Case ID as failed and correct prospectively under a new Case ID. A case failure does not decide method deletion, merger, absorption, or survival.

## 10. Evidence-count lock

Before execution:

```text
DIRECT_COMPARISON_PILOTS: 1
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 0
BOUNDARY_COMPARISON_CASES: 0
NO_GAIN_COMPARISON_CASES: 0
BASELINE_COMPARISON_CASES: 0
```

A 48/48 PASS may add exactly:

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
NEGATIVE_OR_FAILURE_COMPARISON_CASE_INCREMENT: +1
```

It does not establish external applicability, comparative gain, reproducibility, independent validation, method maturity, or permanent method independence.
