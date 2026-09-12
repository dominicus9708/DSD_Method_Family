# CLS-CH-002 Precommit / DSD 분류론 Negative-Failure Terminal Distinction 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-12**  
Method: **DSD Classification / DSD 분류론**  
Protocol: **Classification Protocol v0.1**  
Protocol commit: `c20be5f2507a766998ac346aeed2fcef8a045afc`

## 1. Evidence identity

```text
CASE_ID: CLS-CH-002
CASE_CLASS: negative_failure_terminal_distinction
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Classification Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: none
METHOD_GAIN_ASSESSMENT: not_permitted_in_this_case
```

Purpose: test whether Protocol v0.1 preserves seven distinct non-positive or non-single-classification outcomes instead of collapsing them into one generic failure or negative-membership state.

```text
N1 uncertainty crosses decision boundary -> BOUNDARY_CASE
N2 substantive partial evaluation but closure missing -> UNDERDETERMINED
N3 mutually exclusive class criteria both satisfied -> CRITERION_CONFLICT
N4 claim-required semantic bridge absent before substantive evaluation -> BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
N5 subject outside declared universe -> OUT_OF_SCOPE
N6 no current match under open schema -> OPEN_WORLD_NO_CURRENT_MATCH
N7 no class applies after closed class-registry closure -> UNCLASSIFIED_WITHIN_DECLARED_SCHEMA
```

No competent baseline is used. `CLASSIFICATION_METHOD_GAIN_STATUS` must remain `NOT_ASSESSED`.

## 2. Common frozen rules

All seven task instances are frozen before execution.

```text
TASK_FAMILY_ID: CLS-TASK-FAMILY-002
CLAIMED_OUTPUT_LEVEL: MEMBERSHIP_ASSIGNMENT
CLASS_GENERATION: not permitted in all seven tasks
AUXILIARY_METHODS_OR_HANDOFFS: none except an explicitly required-but-absent bridge in N4
EXTERNAL_STANDARD: not used
DYNAMIC_OR_LINEAGE_CLAIM: not used
BASELINE: none
```

Common guards:

```text
BOUNDARY_CASE != CLASSIFICATION_FAILURE
UNDERDETERMINED != NEGATIVE_MEMBERSHIP
CRITERION_CONFLICT != CLASSIFIED_MULTI
BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION != NEGATIVE_MEMBERSHIP
OUT_OF_SCOPE != UNCLASSIFIED_WITHIN_DECLARED_SCHEMA
OPEN_WORLD_NO_CURRENT_MATCH != UNIVERSAL_NONMEMBERSHIP
OPEN_WORLD_NO_CURRENT_MATCH != CLOSED_WORLD_UNCLASSIFIED
CLOSED_WORLD_UNCLASSIFIED != OUT_OF_SCOPE
```

A task may return a non-positive status and still be `CLASSIFICATION_PROTOCOL_CONFORMANCE = CONFORMANT` when that status is the strongest justified result under the frozen task.

---

## 3. N1 — uncertainty crosses a class boundary

### 3.1 Frozen schema

```text
TASK_ID: CLS-TASK-002-N1
SUBJECT_ID: N1-S
CLASSIFICATION_UNIVERSE: real-valued x records with supplied uncertainty interval
CLASS_SCHEMA_ID_AND_VERSION: CLS002-BND-v1
CLASS_SCHEMA_STATUS: closed
SCHEMA_COVERAGE_CLAIM: closed_world_claim for the declared LOW/HIGH predicates plus explicit boundary handling
CLASS_RELATION_SEMANTICS: disjoint
MUTUAL_EXCLUSION_RULES: LOW and HIGH cannot both be terminally assigned

CLASS LOW:
  criterion: x < 10

CLASS HIGH:
  criterion: x > 10

FEATURE_UNCERTAINTY_OR_TOLERANCE_POLICY:
  use the full supplied interval, not only the central estimate

BOUNDARY_DECISION_SEMANTICS:
  if the uncertainty interval contains or crosses x=10, return BOUNDARY_CASE
```

### 3.2 Frozen subject

```text
central_estimate_x: 10.0
uncertainty_interval_x: [9.8, 10.2]
```

### 3.3 Expected result

```text
EXPECTED_ASSIGNMENT: none terminal
EXPECTED_MEMBERSHIP_STATUS: BOUNDARY_CASE
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

The central estimate must not be used to force LOW or HIGH.

---

## 4. N2 — partial substantive evaluation without closure

### 4.1 Frozen schema

```text
TASK_ID: CLS-TASK-002-N2
SUBJECT_ID: N2-S
CLASSIFICATION_UNIVERSE: records with Boolean features f1 and f2 when available
CLASS_SCHEMA_ID_AND_VERSION: CLS002-PARTIAL-v1
CLASS_SCHEMA_STATUS: closed
SCHEMA_COVERAGE_CLAIM: closed_world_claim over the two declared classes
CLASS_RELATION_SEMANTICS: disjoint

CLASS READY:
  criterion: f1 == true AND f2 == true

CLASS NOT_READY:
  criterion: f1 == false OR f2 == false

MISSING_INFORMATION_POLICY:
  if at least one claim-relevant criterion component has been substantively evaluated but missing information prevents decision closure, return UNDERDETERMINED;
  BLOCKED is reserved here for a pre-evaluation absence that prevents any substantive criterion evaluation.
```

### 4.2 Frozen subject

```text
f1: true
f2: missing
f1_source: supplied record
f2_source: not supplied
```

### 4.3 Expected result

```text
READY: unresolved
NOT_READY: unresolved
SUBSTANTIVE_EVALUATION_PERFORMED: yes, f1 evaluated
EXPECTED_ASSIGNMENT: none terminal
EXPECTED_MEMBERSHIP_STATUS: UNDERDETERMINED
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

Missing `f2` must not be coerced to false and must not be relabeled as `NOT_READY`.

---

## 5. N3 — mutually exclusive criteria both satisfied

### 5.1 Frozen schema

```text
TASK_ID: CLS-TASK-002-N3
SUBJECT_ID: N3-S
CLASSIFICATION_UNIVERSE: exact real-valued x records
CLASS_SCHEMA_ID_AND_VERSION: CLS002-CONFLICT-v1
CLASS_SCHEMA_STATUS: closed
SCHEMA_COVERAGE_CLAIM: closed_world_claim over the frozen class registry
CLASS_RELATION_SEMANTICS: disjoint
MUTUAL_EXCLUSION_RULES: POS and NONPOS may not both be terminal assignments
MULTI_LABEL_POLICY: forbidden
CRITERION_CONFLICT_POLICY: no priority or tie-break; unresolved exclusive satisfaction -> CRITERION_CONFLICT

CLASS POS:
  criterion: x >= 0

CLASS NONPOS:
  criterion: x <= 0
```

### 5.2 Frozen subject

```text
x: 0
uncertainty: none
```

### 5.3 Expected result

```text
POS: satisfied
NONPOS: satisfied
EXPECTED_ASSIGNMENT: none terminal
EXPECTED_MEMBERSHIP_STATUS: CRITERION_CONFLICT
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

The run must not silently choose one class or relabel the result `CLASSIFIED_MULTI` because the frozen schema declares the classes mutually exclusive.

---

## 6. N4 — missing claim-required bridge before substantive evaluation

### 6.1 Frozen schema and bridge requirement

```text
TASK_ID: CLS-TASK-002-N4
SUBJECT_ID: N4-S
CLASSIFICATION_UNIVERSE: raw device-code records requiring a supplied semantic bridge before temperature-state classification
CLASS_SCHEMA_ID_AND_VERSION: CLS002-BLOCK-v1
CLASS_SCHEMA_STATUS: externally_fixed
SCHEMA_COVERAGE_CLAIM: externally_fixed_scope_only
CLASS_RELATION_SEMANTICS: disjoint

CLASS COLD:
  semantic criterion: temperature_state == cold

CLASS HOT:
  semantic criterion: temperature_state == hot

FEATURE_EXTRACTION_OR_MAPPING_RULE:
  raw device code may be mapped to temperature_state only through supplied bridge BR-TEMP-001

BR-TEMP-001_SUPPLIED: no
UNDECLARED_MAPPING_PERMITTED: no
```

### 6.2 Frozen subject

```text
raw_device_code: H
semantic_temperature_state: not supplied
```

### 6.3 Expected result

```text
SUBSTANTIVE_CRITERION_EVALUATION_PERFORMED: no
EXPECTED_ASSIGNMENT: none terminal
EXPECTED_MEMBERSHIP_STATUS: BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

The raw label `H` must not be guessed to mean `hot`, and missing bridge information must not be converted into negative membership.

---

## 7. N5 — subject outside the declared classification universe

### 7.1 Frozen schema

```text
TASK_ID: CLS-TASK-002-N5
SUBJECT_ID: N5-S
CLASSIFICATION_UNIVERSE:
  record_type == sensor AND q_applicability == applicable
CLASS_SCHEMA_ID_AND_VERSION: CLS002-SCOPE-v1
CLASS_SCHEMA_STATUS: closed
SCHEMA_COVERAGE_CLAIM: closed_world_claim only inside the declared sensor universe
OUT_OF_SCOPE_POLICY:
  a subject failing universe admission is OUT_OF_SCOPE and class criteria are not applied

CLASS ACTIVE:
  criterion inside universe: q_status == DEFINED_NONZERO

CLASS INACTIVE:
  criterion inside universe: q_status == DEFINED_ZERO
```

### 7.2 Frozen subject

```text
record_type: document
q_applicability: inapplicable
q_status: not evaluated
```

### 7.3 Expected result

```text
CRITERION_EVALUATION_PERFORMED: no
EXPECTED_ASSIGNMENT: none
EXPECTED_MEMBERSHIP_STATUS: OUT_OF_SCOPE
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

The subject must not be relabeled `UNCLASSIFIED_WITHIN_DECLARED_SCHEMA` because it was never admitted to the classification universe.

---

## 8. N6 — open schema with no current class match

### 8.1 Frozen schema

```text
TASK_ID: CLS-TASK-002-N6
SUBJECT_ID: N6-S
CLASSIFICATION_UNIVERSE: color-labelled records
CLASS_SCHEMA_ID_AND_VERSION: CLS002-OPEN-v1
CLASS_SCHEMA_STATUS: open
SCHEMA_COVERAGE_CLAIM: open_world_no_exhaustiveness_claim
CLASS_RELATION_SEMANTICS: disjoint among currently registered classes
CLASS_GENERATION: not performed in this challenge

CURRENT CLASS RED:
  criterion: color == red

CURRENT CLASS BLUE:
  criterion: color == blue
```

### 8.2 Frozen subject

```text
color: green
```

### 8.3 Expected result

```text
RED: not_satisfied
BLUE: not_satisfied
EXPECTED_ASSIGNMENT: none current
EXPECTED_MEMBERSHIP_STATUS: OPEN_WORLD_NO_CURRENT_MATCH
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

No current match must not be upgraded to universal nonmembership or to closed-world unclassified status.

---

## 9. N7 — closed class registry with no applicable class

### 9.1 Frozen schema

```text
TASK_ID: CLS-TASK-002-N7
SUBJECT_ID: N7-S
CLASSIFICATION_UNIVERSE: colors {red, blue, green}
CLASS_SCHEMA_ID_AND_VERSION: CLS002-CLOSED-v1
CLASS_SCHEMA_STATUS: closed
SCHEMA_COVERAGE_CLAIM: closed_world_claim
CLOSED_SCHEMA_CLOSURE_EVIDENCE:
  the class registry for this task is frozen to exactly {RED_CLASS, BLUE_CLASS};
  no other class is admissible and class generation is disabled;
  closure is a claim about the available class registry, not a claim that every universe member must match a class.
CLASS_RELATION_SEMANTICS: disjoint

CLASS RED_CLASS:
  criterion: color == red

CLASS BLUE_CLASS:
  criterion: color == blue
```

### 9.2 Frozen subject

```text
color: green
```

### 9.3 Expected result

```text
RED_CLASS: not_satisfied
BLUE_CLASS: not_satisfied
SUBJECT_IN_UNIVERSE: yes
CLASS_REGISTRY_CLOSED: yes
EXPECTED_ASSIGNMENT: none
EXPECTED_MEMBERSHIP_STATUS: UNCLASSIFIED_WITHIN_DECLARED_SCHEMA
EXPECTED_CONFORMANCE: CONFORMANT
EXPECTED_GAIN: NOT_ASSESSED
```

This task contrasts directly with N6: the same surface feature may yield different nonmembership semantics because schema closure differs.

---

## 10. Frozen cross-task distinction matrix

```text
N1 -> BOUNDARY_CASE
N2 -> UNDERDETERMINED
N3 -> CRITERION_CONFLICT
N4 -> BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
N5 -> OUT_OF_SCOPE
N6 -> OPEN_WORLD_NO_CURRENT_MATCH
N7 -> UNCLASSIFIED_WITHIN_DECLARED_SCHEMA

ALL PROTOCOL CONFORMANCE: CONFORMANT
ALL METHOD GAIN: NOT_ASSESSED
```

Required distinctions:

```text
BOUNDARY_CASE != UNDERDETERMINED
UNDERDETERMINED != BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
CRITERION_CONFLICT != CLASSIFIED_MULTI
BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION != NEGATIVE_MEMBERSHIP
OUT_OF_SCOPE != UNCLASSIFIED_WITHIN_DECLARED_SCHEMA
OPEN_WORLD_NO_CURRENT_MATCH != UNCLASSIFIED_WITHIN_DECLARED_SCHEMA
OPEN_WORLD_NO_CURRENT_MATCH != UNIVERSAL_NONMEMBERSHIP
NONPOSITIVE_RESULT != PROTOCOL_NONCONFORMANCE
```

---

## 11. Precommitted scoring

Total required checks: **50**.

### A. Protocol validity-gate family — 14 checks

```text
A1  G1 schema identity/version frozen for every task
A2  G2 universe and target resolution frozen for every task
A3  G3 relation/exclusion/overlap semantics sufficient for each requested result
A4  G4 coverage claim explicit for every schema
A5  G5 closed-world nonmembership invoked only with closure evidence, specifically N7
A6  G6 class criteria and semantics/provenance identifiable
A7  G7 criterion-composition and decision semantics explicit enough for each task
A8  G8 feature mappings/bridges explicit; missing bridge in N4 remains missing rather than fabricated
A9  G9 missing/inapplicable/out-of-scope/status distinctions preserved
A10 G10 uncertainty/boundary policy correctly applied to N1 and not fabricated elsewhere
A11 G11 class generation disabled; no schema mutation occurs
A12 G12 no unsupported equivalence/hierarchy/aggregate/temporal special claim introduced
A13 G13 no neighboring-method result absorbed without provenance
A14 G14 every output remains within frozen evidence/coverage closure
```

### B. N1 boundary checks — 4 checks

```text
B1 full uncertainty interval used
B2 no forced LOW/HIGH assignment
B3 BOUNDARY_CASE returned
B4 CONFORMANT and gain NOT_ASSESSED
```

### C. N2 underdetermined checks — 4 checks

```text
C1 f1 substantive evaluation preserved
C2 missing f2 not coerced to false
C3 UNDERDETERMINED returned rather than NOT_READY or BLOCKED
C4 CONFORMANT and gain NOT_ASSESSED
```

### D. N3 conflict checks — 4 checks

```text
D1 POS and NONPOS both evaluated satisfied
D2 disjoint/mutual-exclusion semantics preserved
D3 CRITERION_CONFLICT returned rather than arbitrary single class or CLASSIFIED_MULTI
D4 CONFORMANT and gain NOT_ASSESSED
```

### E. N4 blocked checks — 4 checks

```text
E1 required bridge recorded absent
E2 raw code not semantically guessed
E3 BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION returned before substantive criterion evaluation
E4 CONFORMANT and gain NOT_ASSESSED
```

### F. N5 out-of-scope checks — 4 checks

```text
F1 universe-admission failure preserved
F2 class criteria not applied outside universe
F3 OUT_OF_SCOPE returned rather than unclassified/negative membership
F4 CONFORMANT and gain NOT_ASSESSED
```

### G. N6 open-world checks — 4 checks

```text
G1 RED and BLUE both not satisfied
G2 open-world nonexhaustiveness preserved
G3 OPEN_WORLD_NO_CURRENT_MATCH returned; no universal nonmembership claim
G4 CONFORMANT and gain NOT_ASSESSED
```

### H. N7 closed-world-unclassified checks — 4 checks

```text
H1 subject admitted to declared universe
H2 RED_CLASS and BLUE_CLASS both not satisfied
H3 closed registry closure supports UNCLASSIFIED_WITHIN_DECLARED_SCHEMA without claiming subject out of scope
H4 CONFORMANT and gain NOT_ASSESSED
```

### I. Cross-task distinction checks — 8 checks

```text
I1 BOUNDARY_CASE kept distinct from UNDERDETERMINED
I2 UNDERDETERMINED kept distinct from BLOCKED
I3 CRITERION_CONFLICT kept distinct from CLASSIFIED_MULTI
I4 BLOCKED kept distinct from negative membership
I5 OUT_OF_SCOPE kept distinct from closed-world unclassified
I6 OPEN_WORLD_NO_CURRENT_MATCH kept distinct from closed-world unclassified
I7 OPEN_WORLD_NO_CURRENT_MATCH kept distinct from universal nonmembership
I8 all seven non-positive outcomes remain compatible with CONFORMANT execution when justified
```

Decision:

```text
50/50 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

If a fixture defect is discovered after this commit, this Case ID must remain preserved as failed or defective and any corrected challenge must receive a new Case ID. The protocol, fixture, expected statuses, or scoring may not be changed post hoc to obtain a PASS.

---

## 12. Evidence-count lock

Before execution:

```text
DIRECT_CLASSIFICATION_PILOTS: 1
POSITIVE_DIRECT_CHALLENGES: 1
NEGATIVE_FAILURE_CHALLENGES: 0
METHOD_BOUNDARY_CHALLENGES: 0
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
```

A 50/50 PASS may add exactly:

```text
DIRECT_CLASSIFICATION_PILOT_INCREMENT: +1
NEGATIVE_FAILURE_CHALLENGE_INCREMENT: +1
```

It does not establish external applicability, comparative gain, reproducibility, independent validation, superiority, permanent method independence, or maturity promotion.