# SPEC-APP-005 — JSON Schema Draft 2020-12 `dependentRequired` Blind External Test Precommit

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Case class: external authoritative specification + independently maintained official test suite

## 1. Purpose

This run tests DSD Specification v1.0 on an external software-validation corpus under a label-withholding procedure.

The target is the official JSON Schema Test Suite file:

`tests/draft2020-12/dependentRequired.json`

at JSON-Schema-Test-Suite commit:

`f6fd52a0a95472e079cbfc6ef7f089702b80e045`

The normative interpretation source is JSON Schema Draft 2020-12 Validation, §6.5.4 `dependentRequired`.

The principal question is whether the v1.0 typed requirement representation can classify the official test instances from schema + instance data **before** the test-suite `valid` labels are revealed.

## 2. Blindness / reveal rule

Before predictions are frozen, the evaluator may inspect only:

```text
schema
instance data
normative JSON Schema 2020-12 `dependentRequired` rule
```

The following test-suite fields are withheld from the prediction packet:

```text
valid
case/test descriptions
comments that directly reveal the expected result
```

The full locked source file is downloaded only through a redaction step that does not print the withheld labels/descriptions before the prediction record is committed.

After all predictions are committed, the `valid` labels may be revealed and compared.

This is a **within-session label-withholding test**, not an independent evaluator test. Same-model/common-evaluator dependence remains present.

## 3. Selection rule

Use **all test instances** contained in the locked `dependentRequired.json` file at the pinned commit.

No case may be removed after prediction because it is inconvenient, ambiguous, or incorrect.

If a case cannot be classified from the locked normative source and redacted packet, prediction must be `UNRESOLVED` rather than guessed.

## 4. Locked DSD interface profile

```text
FORMATION_LAYER: not used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: none
```

Reason: this task is a typed applicability/dependency/requirement-validation problem. No aggregate, lineage, dynamics, or realized-axis claim is required.

## 5. Normative requirement lock

From JSON Schema Draft 2020-12 Validation §6.5.4:

```text
R1 `dependentRequired` applies dependency requirements by property presence.
R2 For each dependency key that is present in the instance object, every property name listed for that key must also be present.
R3 A dependency key absent from the instance does not activate its dependency list.
R4 `dependentRequired` is an object-validation assertion; non-object instances are not made invalid solely by this keyword.
R5 Multiple active dependency keys must each satisfy their own dependency lists.
R6 An empty dependency list imposes no additional required property.
R7 Dependencies are not assumed bidirectional unless both directions are explicitly declared.
```

These are DSD re-expression atoms, not replacements for the JSON Schema specification.

## 6. Predicted outcome classes

Each redacted test instance receives exactly one pre-reveal prediction:

```text
VALID
INVALID
UNRESOLVED
```

`UNRESOLVED` is preserved as an unfavorable/indeterminate result and may not be changed after reveal.

## 7. Scoring

Primary score:

```text
BLIND_LABEL_MATCHES / TOTAL_LOCKED_TESTS
```

Secondary checks:

```text
FALSE_DEPENDENCY_ACTIVATION_ON_ABSENT_TRIGGER
MISSED_ACTIVE_DEPENDENCY
FALSE_BIDIRECTIONAL_INFERENCE
FALSE_FAILURE_ON_NON_OBJECT
EMPTY_DEPENDENCY_LIST_ERROR
SOURCE_FACT_INVENTION
POST_REVEAL_PREDICTION_CHANGE
```

No minimum score is predeclared as automatic evidence of method maturity. All mismatches are preserved and analyzed.

## 8. v1.0-specific regression questions

This run also tests whether v1.0 can remain compact while retaining dependency semantics:

```text
DEPENDENCIES: expected active
PRECEDENCE_OR_PRIORITY: expected inactive
SOURCE_OPENNESS_STATUS: expected inactive
DOWNSTREAM_DETERMINACY_STATUS: expected inactive unless a source ambiguity is actually encountered
ALLOWED_ALTERNATIVES: optional, only if required by a specific schema
PROHIBITED_STATES: optional, only if required by a specific schema
ATOM_LOCAL_VALIDATION_STANDARD: inherited from JSON Schema 2020-12 unless narrower local semantics are needed
```

The protocol fails this regression aspect if irrelevant optional ledgers must be populated to preserve the classification.

## 9. Guardrails

```text
G1 SOURCE_FIDELITY: active
G2 PURPOSE_AND_PRIORITY_FIDELITY: inactive for the narrow conformance-classification task unless source purpose becomes claim-relevant
G3 DETAIL_PROPORTIONALITY: active
G4 VIEWPOINT_SEPARATION: inactive unless a derivative interpretation beyond the normative rule is introduced
```

## 10. Baseline and claim limits

Baseline after reveal:

```text
JSON Schema Draft 2020-12 normative text
+ official JSON-Schema-Test-Suite expected `valid` labels
```

The run does not establish:

```text
independent evaluator validation
validator implementation correctness beyond this file
full JSON Schema conformance
software-engineering productivity gain
superiority over the official JSON Schema test suite
```

## 11. Anti-post-hoc rule

After the prediction commit:

```text
no case deletion
no requirement rewrite to rescue a mismatch
no post-reveal exception addition
no changed prediction
```

A future protocol revision may respond to a real failure, but this run's result remains frozen under v1.0.
