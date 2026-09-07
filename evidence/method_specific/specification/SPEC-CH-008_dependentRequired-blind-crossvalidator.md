# SPEC-CH-008 — `dependentRequired` Label-Withheld Cross-Validator Challenge

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Precommit: `92277445b73a72d7d4d9ff29f849d7068eb4244a`
Frozen prediction commit: `7c5f32231d21b4b59251f4093a7116ab899bfb4e`
Cross-validator: Python `jsonschema` 4.26.0, `Draft202012Validator`
Normative basis: JSON Schema Draft 2020-12 Validation §6.5.4 `dependentRequired`

## 1. Result in one line

All 16 frozen DSD Specification v1.0 predictions matched the post-freeze `jsonschema` Draft 2020-12 validator outcomes. The challenge preserved one-way dependency activation, empty dependency lists, multi-trigger conjunction, root-vs-nested scope, self-dependency, and non-object non-activation without requiring irrelevant v1.0 ledgers.

```text
CROSS_VALIDATOR_MATCHES: 16/16
UNRESOLVED_PREDICTIONS: 0
POST_REVEAL_PREDICTION_CHANGE: 0
HARD_FAILURES: 0
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_DEPENDENCY_LABEL_WITHHELD_CROSSVALIDATOR_PASS_WITH_LIMITATIONS
```

## 2. Frozen predictions vs cross-validator

| Case | Frozen DSD prediction | jsonschema 4.26.0 | Match |
|---|---|---|---|
| C01 | VALID | VALID | yes |
| C02 | INVALID | INVALID | yes |
| C03 | VALID | VALID | yes |
| C04 | VALID | VALID | yes |
| C05 | VALID | VALID | yes |
| C06 | INVALID | INVALID | yes |
| C07 | VALID | VALID | yes |
| C08 | INVALID | INVALID | yes |
| C09 | VALID | VALID | yes |
| C10 | VALID | VALID | yes |
| C11 | INVALID | INVALID | yes |
| C12 | VALID | VALID | yes |
| C13 | VALID | VALID | yes |
| C14 | VALID | VALID | yes |
| C15 | VALID | VALID | yes |
| C16 | VALID | VALID | yes |

```text
CROSS_VALIDATOR_MATCHES: 16/16
CROSS_VALIDATOR_MISMATCHES: 0
```

## 3. Boundary diagnostics

```text
FALSE_DEPENDENCY_ACTIVATION_ON_ABSENT_TRIGGER: 0
MISSED_ACTIVE_DEPENDENCY: 0
FALSE_BIDIRECTIONAL_INFERENCE: 0
EMPTY_DEPENDENCY_LIST_ERROR: 0
SELF_DEPENDENCY_ERROR: 0
MULTI_TRIGGER_COMBINATION_ERROR: 0
ROOT_NESTED_SCOPE_ERROR: 0
FALSE_FAILURE_ON_NON_OBJECT: 0
POST_REVEAL_PREDICTION_CHANGE: 0
```

Repeated controls remained consistent:

```text
C03 == C07 == VALID
C02 == C08 == INVALID
```

## 4. DSD v1.0 structure used

The case required only a compact typed dependency carrier:

```text
TRIGGER_PRESENCE(p)
  -> REQUIRE_PRESENCE(q1,...,qn)
```

Active v1.0 conditional structure:

```text
DEPENDENCIES: active
```

Inactive and omitted without classification loss:

```text
PRECEDENCE_OR_PRIORITY
SOURCE_OPENNESS_STATUS
DOWNSTREAM_DETERMINACY_STATUS
ALLOWED_ALTERNATIVES
PROHIBITED_STATES
```

`VALIDATION_STANDARD` was inherited from the locked JSON Schema 2020-12 normative standard rather than repeated atom-by-atom.

```text
IRRELEVANT_OPTIONAL_LEDGERS_ACTIVATED: 0
FALSE_MANDATORY_OPTIONAL_DSD_LAYER: 0
```

## 5. Guardrails

```text
G1 SOURCE_FIDELITY: inside
G2 PURPOSE_AND_PRIORITY_FIDELITY: inactive for the narrow assertion task
G3 DETAIL_PROPORTIONALITY: inside
G4 VIEWPOINT_SEPARATION: inactive
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
```

No new source semantics or reverse dependencies were invented merely to make the cases determinate.

## 6. External-standard boundary

The normative rule remains JSON Schema Draft 2020-12 Validation §6.5.4. The Python `jsonschema` result is an implementation cross-check, not a replacement for the specification.

The challenge therefore establishes only consistency on the locked cases:

```text
DSD_FROZEN_PREDICTIONS
== JSONSCHEMA_IMPLEMENTATION_OUTCOMES
```

It does not establish full validator conformance or domain superiority.

## 7. Evidence interpretation

Supported by this challenge:

```text
DEPENDENCY_ACTIVATION_DISCIPLINE: pass_on_locked_cases
ONE_WAY_DEPENDENCY_BOUNDARY: pass
EMPTY_DEPENDENCY_BOUNDARY: pass
MULTI_TRIGGER_BOUNDARY: pass
ROOT_NESTED_SCOPE_BOUNDARY: pass
NON_OBJECT_APPLICABILITY_BOUNDARY: pass
V1_0_CONDITIONAL_FIELD_RESTRAINT: pass_on_locked_cases
LABEL_WITHHELD_IMPLEMENTATION_CROSSCHECK: 16/16
```

Not supported:

```text
INDEPENDENT_EVALUATOR_VALIDATION
EXTERNAL_REAL_WORLD_CORPUS_VALIDATION
FULL_JSON_SCHEMA_CONFORMANCE
MEASURED_ENGINEERING_BENEFIT
SUPERIORITY_OVER_JSON_SCHEMA_TOOLING
```

The cases were constructed within the DSD project and the same assistant performed the DSD reasoning. `jsonschema` was invoked only after the prediction commit, so the outcome labels were withheld at the implementation-comparison stage, but evaluator independence is not established.

## 8. Relation to SPEC-APP-005 precommit

A separate planned external test, `SPEC-APP-005_JSON-Schema-dependentRequired_blind_precommit.md`, pinned the official JSON-Schema-Test-Suite `dependentRequired.json` corpus. In this environment the source-access path could not expose schema/data while technically withholding embedded `valid` labels. Rather than contaminate that precommit or pretend a blind test occurred, the external run remains unscored/uncompleted.

This constructed cross-validator challenge is therefore **not** counted as completion of SPEC-APP-005.

## 9. Final record

```text
SPECIFICATION_RESULT_ID: SPEC-CH-008
SPECIFICATION_PROTOCOL_VERSION: v1.0
TARGET_SCOPE: dependentRequired dependency semantics across 16 locked constructed cases
DECLARED_DOWNSTREAM_TASK: classify VALID/INVALID before software-validator reveal
SELECTED_DSD_LAYERS: PROPERTY_CORE only
FINAL_SPEC_STATUS: usable
HARD_FAILURES: none
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
LIMITS: constructed cases; same evaluator; external implementation cross-check only

RESULT:
SPECIFICATION_V1_0_DEPENDENCY_LABEL_WITHHELD_CROSSVALIDATOR_PASS_WITH_LIMITATIONS
```
