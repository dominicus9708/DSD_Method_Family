# SPEC-APP-006 — `ErrorTree` Read-Mutation / Frozen DSD v1.0 Prediction

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Precommit: `70a9ffd9b02d839057f1efb62b7c8a605e6cc813`
External source seen: `python-jsonschema/jsonschema` issue #1328 body and issue metadata only
Resolution artifacts seen before this commit: **none**

## 1. Result predicted before resolution reveal

The issue body supports a small behavioral contract: `ErrorTree` iteration and membership should reflect actual error-bearing child keys, and reading a child key with no error should not silently change those observable sets.

```text
PREDICTED_ACCEPTANCE_FAMILY:
  preserve observable error-key semantics across missing-child read

PREDICTED_MINIMUM_REGRESSION_FAMILY:
  __iter__ and __contains__ remain unchanged for an error-free accessed key
```

## 2. Requirement atoms

### E1 — iteration reflects error-bearing child keys

```text
REQUIREMENT_ID: E1
SOURCE_REFERENCE: issue #1328 reproduction + stated documentation contradiction
TARGET_ENTITY_OR_CARRIER: ErrorTree child-key iteration
REQUIREMENT_TYPE: observable_semantics
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: iterate an ErrorTree constructed from validator errors
REQUIRED_STRUCTURE_OR_VALUE: returned child keys correspond to child positions/keys with actual errors at the represented tree level
VIOLATION_CONDITION: an error-free key appears merely because it was read/accessed
UNRESOLVED_CONDITION: maintainer resolution redefines documented iteration semantics rather than repairing the reported behavior
VALIDATION_STANDARD: issue-linked library contract / maintainer resolution
```

### E2 — containment reflects actual error-bearing child membership

```text
REQUIREMENT_ID: E2
SOURCE_REFERENCE: issue #1328 reproduction
TARGET_ENTITY_OR_CARRIER: ErrorTree.__contains__
REQUIREMENT_TYPE: observable_semantics
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: evaluate `key in tree`
REQUIRED_STRUCTURE_OR_VALUE: an error-free key is False at the represented tree level
VIOLATION_CONDITION: an error-free key becomes True solely because `tree[key]` was previously read
UNRESOLVED_CONDITION: maintainer resolution explicitly changes the public meaning of containment
VALIDATION_STANDARD: issue-linked library contract / maintainer resolution
```

### E3 — read/access must preserve the error-key observables

```text
REQUIREMENT_ID: E3
SOURCE_REFERENCE: issue #1328 before/after reproduction
TARGET_ENTITY_OR_CARRIER: operation `tree[k]` for a key/index with no error
REQUIREMENT_TYPE: state_transition_constraint
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: access an error-free/missing child key
REQUIRED_STRUCTURE_OR_VALUE: the access does not by itself alter the externally reported error-key set used by iteration or containment
ALLOWED_ALTERNATIVES:
  A) do not persist an empty child in state used by iteration/containment
  B) persist/cache an empty child internally but exclude it from iteration/containment until it carries an error
VIOLATION_CONDITION: the read alone changes `list(tree)` or `key in tree` as though a new error appeared
UNRESOLVED_CONDITION: public access semantics are intentionally redesigned by maintainers
```

### E4 — existing actual-error child remains observable

```text
REQUIREMENT_ID: E4
SOURCE_REFERENCE: issue #1328 initial `list(tree) == [0]`
TARGET_ENTITY_OR_CARRIER: pre-existing error-bearing index 0
REQUIREMENT_TYPE: preservation
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: access a different error-free key/index
REQUIRED_STRUCTURE_OR_VALUE: the actual-error child remains represented after the access
VIOLATION_CONDITION: fixing the false added key removes or hides the genuine error key
UNRESOLVED_CONDITION: none at issue-body resolution
```

### E5 — implementation mechanism is intentionally open

```text
REQUIREMENT_ID: E5
SOURCE_REFERENCE: absence of implementation constraint in issue body
TARGET_ENTITY_OR_CARRIER: internal ErrorTree storage/access implementation
REQUIREMENT_TYPE: implementation_freedom
REQUIRED_OR_OPTIONAL: intentionally_open
ACTIVATION_CONDITION: choosing a repair
SOURCE_OPENNESS_STATUS: SOURCE_INTENTIONAL_OPENNESS
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
REQUIRED_STRUCTURE_OR_VALUE: any implementation satisfying E1-E4 without introducing a conflicting public contract
PROHIBITED_STATES: treating one guessed implementation technique as source-mandated
VIOLATION_CONDITION: DSD prediction claims an exact private data-structure change is required by the issue body
UNRESOLVED_CONDITION: none for behavioral acceptance
```

## 3. Frozen behavioral predictions

For the reporter's reproduced state:

```text
BEFORE_ACCESS:
  list(tree) == [0]
  1 in tree == False

AFTER_ACCESS_OF_ERROR_FREE_INDEX_1:
  list(tree) == [0]
  1 in tree == False
  genuine index 0 remains observable
```

Compatibility prediction, lower confidence than E1-E4:

```text
PREDICT_ACCESS_ITSELF_REMAINS_SUPPORTED: yes
PREDICT_MISSING_CHILD_ACCESS_NEED_NOT_RAISE: yes
CONFIDENCE: medium
```

Reason: the report identifies the mutation of iteration/containment as the bug, not indexing access itself. This is an inference, not a direct quoted requirement.

## 4. Frozen regression-test prediction

Minimum likely maintainer test family:

```text
T1 construct ErrorTree with at least one genuine child error
T2 assert an error-free key is absent from iteration/containment
T3 access that error-free key
T4 assert iteration is unchanged
T5 assert containment for that key remains false
```

Secondary plausible check:

```text
T6 genuine error-bearing key remains present after T3
```

Not predicted as required because absent from the issue body:

```text
exact internal container type
exact private attribute changes
performance benchmark
serialization behavior
len(tree) behavior beyond what follows indirectly
thread-safety changes
new exception type
```

## 5. DSD v1.0 field activation

```text
PROPERTY_CORE: used
DEPENDENCIES: inactive
SOURCE_OPENNESS_STATUS: active only for E5 implementation freedom
DOWNSTREAM_DETERMINACY_STATUS: active only for E5
ALLOWED_ALTERNATIVES: active only for E3
PROHIBITED_STATES: active only for E5
PRECEDENCE_OR_PRIORITY: omitted
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
```

## 6. Frozen scoring expectations

```text
A1_BEHAVIORAL_REQUIREMENT_MATCH:
  expected MATCH if resolution preserves pre/post observable key semantics

A2_MEMBERSHIP_ITERATION_SEMANTICS_MATCH:
  expected MATCH if actual resolution specifically addresses __iter__/__contains__ false membership

A3_READ_NONMUTATION_OR_EQUIVALENT_OBSERVATIONAL_INVARIANT_MATCH:
  expected MATCH if read no longer causes the false observable addition, regardless of internal mechanism

A4_PREEXISTING_ERROR_PRESERVATION_MATCH:
  expected MATCH if genuine error entries remain visible

A5_REGRESSION_TEST_FAMILY_MATCH:
  expected MATCH/PARTIAL_MATCH depending on actual tests

A6_IMPLEMENTATION_OVERPREDICTION_COUNT:
  expected 0

A7_SOURCE_FACT_INVENTION_COUNT:
  expected 0

A8_POST_REVEAL_PREDICTION_CHANGE:
  required 0
```

## 7. Guardrails before reveal

```text
G1 SOURCE_FIDELITY: inside
G2 PURPOSE_AND_PRIORITY_FIDELITY: inactive
G3 DETAIL_PROPORTIONALITY: inside
G4 VIEWPOINT_SEPARATION: inactive
```

## 8. Freeze declaration

After this commit, issue comments, linked PRs, patches, closing commits, and maintainer rationale may be revealed. The requirements and predictions above must not be rewritten to fit the revealed resolution.
