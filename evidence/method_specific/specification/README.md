# DSD Specification Method-Specific Evidence / DSD 명세론 개별 방법 직접 증거

Status: **eight direct constructed pilots + four completed external applications + one blocked external blind precommit + one method-family linkage pilot / internal Protocol v1.0 standardized / method evidence maturity remains developing**  
Date: 2026-09-08  
Method: **DSD Specification / DSD 명세론**

Protocol versions:
- v0.1 historical: [`../../../methods/03_specification/PROTOCOL.md`](../../../methods/03_specification/PROTOCOL.md)
- v0.2 historical: [`../../../methods/03_specification/PROTOCOL_v0.2.md`](../../../methods/03_specification/PROTOCOL_v0.2.md)
- v0.2.1 historical/evidence basis: [`../../../methods/03_specification/PROTOCOL_v0.2.1.md`](../../../methods/03_specification/PROTOCOL_v0.2.1.md)
- v1.0 standard/default for new DSD-internal runs: [`../../../methods/03_specification/PROTOCOL_v1.0.md`](../../../methods/03_specification/PROTOCOL_v1.0.md)

Shared-core pilots SC-01 through SC-10 may be reused as operating disciplines, but they do not count as direct Specification validation.

## Direct evidence registry / 직접 증거 레지스트리

### SPEC-CH-001 through SPEC-CH-005 — v0.1 evidence

```text
SPEC-CH-001  SPECIFICATION_DISCRIMINATION_PILOT_PASS_WITH_LIMITATIONS
SPEC-CH-002  SPECIFICATION_CONTRADICTION_UNDERSPECIFICATION_PILOT_PASS_WITH_LIMITATIONS
SPEC-CH-003  SPECIFICATION_OPTIONAL_LAYER_BRIDGE_BOUNDARY_PILOT_PASS_WITH_LIMITATIONS
SPEC-CH-004  SPECIFICATION_NO_GAIN_PILOT_PASS_WITH_LIMITATIONS
SPEC-CH-005  SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_PASS_WITH_LIMITATIONS
```

`SPEC-CH-005` supports procedural retraceability and order stability on a locked constructed packet, not independent reviewer validation.

### SPEC-CH-006 — Guardrail Centerline Challenge

```text
PRECOMMIT_COMMIT: fe009d8da9ab992e6885d07e14ff26355b776a86
EXACT_GUARDRAIL_FAMILY_MATCHES: 8/8
FALSE_HARD_FAILURE_ON_PRESSURE_CASES: 0
FALSE_REJECTION_OF_DECLARED_DERIVATIVE_VIEW: 0
RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS
```

Accepted guardrail profile:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

### SPEC-CH-007 — Source-Intentional Openness / Accidental Underspecification Boundary

Precommit: [`SPEC-CH-007_open-texture-underspecification_precommit.md`](SPEC-CH-007_open-texture-underspecification_precommit.md)  
Result: [`SPEC-CH-007_open-texture-underspecification.md`](SPEC-CH-007_open-texture-underspecification.md)

```text
PRECOMMIT_COMMIT: 1b3665696007b29535b3f46815cad39f4f02c03f
EXACT_SOURCE_OPENNESS_AXIS_MATCHES: 8/8
EXACT_DOWNSTREAM_DETERMINACY_AXIS_MATCHES: 8/8
EXACT_JOINT_AXIS_MATCHES: 8/8
TASK_SUFFICIENT_INTENTIONAL_OPENNESS_ACCEPTED: 2/2
INTENTIONAL_OPENNESS_WITH_AUTOMATION_GAP_PRESERVED: 1/1
ACCIDENTAL_OR_UNRESOLVED_MISSING_DATA_DETECTED: 3/3
UNSUPPORTED_INTENT_NOT_INVENTED: 3/3
INVENTED_RESOLUTION_ESCALATED_TO_HARD_FAILURE: 1/1
FALSE_UNDERSPECIFICATION_ON_TASK_SUFFICIENT_INTENTIONAL_OPENNESS: 0
FALSE_OPENNESS_EXCUSE_FOR_MISSING_REQUIRED_DATA: 0
FALSE_DETERMINACY_FROM_INVENTED_VALUE: 0
RESULT: SPECIFICATION_OPENNESS_DETERMINACY_AXIS_SEPARATION_PILOT_PASS_WITH_LIMITATIONS
```

The key result remains:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

### SPEC-CH-008 — `dependentRequired` label-withheld implementation cross-check

Precommit: [`SPEC-CH-008_dependentRequired-blind-crossvalidator_precommit.md`](SPEC-CH-008_dependentRequired-blind-crossvalidator_precommit.md)  
Frozen predictions: [`SPEC-CH-008_dependentRequired-blind-crossvalidator_predictions.md`](SPEC-CH-008_dependentRequired-blind-crossvalidator_predictions.md)  
Result: [`SPEC-CH-008_dependentRequired-blind-crossvalidator.md`](SPEC-CH-008_dependentRequired-blind-crossvalidator.md)

```text
PRECOMMIT_COMMIT: 92277445b73a72d7d4d9ff29f849d7068eb4244a
PREDICTION_COMMIT: 7c5f32231d21b4b59251f4093a7116ab899bfb4e
CROSS_VALIDATOR: Python jsonschema 4.26.0 / Draft202012Validator
CROSS_VALIDATOR_MATCHES: 16/16
UNRESOLVED_PREDICTIONS: 0
FALSE_DEPENDENCY_ACTIVATION_ON_ABSENT_TRIGGER: 0
MISSED_ACTIVE_DEPENDENCY: 0
FALSE_BIDIRECTIONAL_INFERENCE: 0
EMPTY_DEPENDENCY_LIST_ERROR: 0
ROOT_NESTED_SCOPE_ERROR: 0
FALSE_FAILURE_ON_NON_OBJECT: 0
POST_REVEAL_PREDICTION_CHANGE: 0
IRRELEVANT_OPTIONAL_LEDGERS_ACTIVATED: 0
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_DEPENDENCY_LABEL_WITHHELD_CROSSVALIDATOR_PASS_WITH_LIMITATIONS
```

This is a constructed method-specific challenge with a post-freeze independent software implementation cross-check. It is **not** independent evaluator validation and is **not** external real-world application evidence.

## External applications / 외부·독립 생성 corpus 적용

### SPEC-APP-001 — RFC 9112 §6.3

Protocol: **v0.1**.

```text
SOURCE_UNIT_COVERAGE: 13/13
PRECEDENCE_PRESERVATION: 13/13
SOURCE_FIDELITY_RESULT: pass
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

### SPEC-APP-002 — Belmont Report Part C

Protocol: **v0.2**.

```text
EXTERNAL_DOMAIN: human-subject research ethics
SOURCE_UNIT_COVERAGE: 22/22
LOCAL_PRIORITY_PRESERVATION: 5/5
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED: 4/4
HARD_FAILURE_COUNT: 0
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
RESULT: SPECIFICATION_EXTERNAL_GUARDRAIL_APPLICATION_PASS_WITH_MIXED_GAIN
```

### SPEC-APP-003 — OSHA Emergency Action Plan core corpus

Protocol: **v0.2.1**  
Result: [`../../real_world_cases/specification/SPEC-APP-003_OSHA_EAP_core_guidance.md`](../../real_world_cases/specification/SPEC-APP-003_OSHA_EAP_core_guidance.md)

```text
EXTERNAL_DOMAIN: workplace emergency planning / occupational safety
SOURCE_UNIT_COVERAGE: 18/18
REGULATORY_MINIMUM_ELEMENTS_PRESERVED: 11/11
SOURCE_INTENTIONAL_OPENNESS_HANDLED_WITHOUT_FABRICATION: 7/7
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
HARD_FAILURE_COUNT: 0
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

### SPEC-APP-004 — WCAG 2.2 Contrast (Minimum) labeled regression

Protocol: **v1.0**  
Result: [`../../real_world_cases/specification/SPEC-APP-004_WCAG22-contrast-v1.0.md`](../../real_world_cases/specification/SPEC-APP-004_WCAG22-contrast-v1.0.md)

```text
EXTERNAL_DOMAIN: web accessibility / WCAG text contrast
EXAMPLE_OUTCOME_FAMILY_MATCHES: 8/8
NORMAL_LARGE_THRESHOLD_SEPARATION: pass
INCIDENTAL_INACTIVE_BOUNDARY_PRESERVATION: pass
INACTIVE_CONDITIONAL_LEDGER_BOILERPLATE: 0
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
RESULT: SPECIFICATION_V1_0_EXTERNAL_LABELED_REGRESSION_NO_GAIN_WITH_LIMITATIONS
```

This is a labeled post-standardization regression/interface test, not blind predictive evidence.

### SPEC-APP-005 — JSON Schema official test-suite blind run — blocked without scoring

Precommit: [`../../real_world_cases/specification/SPEC-APP-005_JSON-Schema-dependentRequired_blind_precommit.md`](../../real_world_cases/specification/SPEC-APP-005_JSON-Schema-dependentRequired_blind_precommit.md)  
Blocked record: [`../../real_world_cases/specification/SPEC-APP-005_JSON-Schema-dependentRequired_blind_blocked.md`](../../real_world_cases/specification/SPEC-APP-005_JSON-Schema-dependentRequired_blind_blocked.md)

```text
STATUS: BLOCKED_BY_LABEL_ISOLATION_TOOLING
PREDICTIONS_COMMITTED: no
OFFICIAL_LABELS_SCORED: no
COUNT_AS_EXTERNAL_APPLICATION_COMPLETION: no
COUNT_AS_BLIND_EVIDENCE: no
```

The embedded official `valid` labels could not be technically isolated from schema/data before source delivery in the current runtime. The precommit was therefore preserved rather than weakened after the fact.

## Method-family linkage evidence / 방법군 연계 증거

`SPEC-LINK-001` is a linkage pilot, not a direct Specification challenge and not direct Audit validation.

```text
RECEIVING_METHOD: DSD Audit
AUDIT_FINDING_MATCHES: 6/6
REQUIREMENT_IDENTITY_PRESERVATION: pass
NORMATIVE_FORCE_PRESERVATION: pass
OPENNESS_PRESERVATION: pass
HIDDEN_RETRANSLATION_REQUIRED: no
EXTERNAL_STANDARD_BOUNDARY_PRESERVED: yes
RESULT: SPECIFICATION_TO_AUDIT_NATIVE_HANDOFF_PILOT_PASS_WITH_LIMITATIONS
```

## Protocol stability and standardization audits / 프로토콜 안정성·표준화 감사

These are DSD Audit methodology records and are not counted as additional direct Specification pilots.

```text
DSD-AUDIT-20260908-METHODOLOGY-003
  PROTOCOL_FREEZE_READINESS: FREEZE_READY_WITH_NONBREAKING_CLEANUP

DSD-AUDIT-20260908-METHODOLOGY-004
  CRITICAL_GATES_PASSED: 14/14
  STANDARDIZATION_VERDICT: STANDARDIZE_WITH_DOCUMENTED_LIMITS
  DEFAULT_DSD_INTERNAL_PROTOCOL: DSD Specification Protocol v1.0
```

## Maturity meta-audit / 성숙도 메타감사

The first maturity audit remains historical:

```text
AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

Later work establishes internal v1.0 interface stability but does not itself establish independent evaluator agreement or measured practical benefit.

## Current evidence state / 현재 증거 상태

```text
V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
V0_2_1_OPENNESS_TRANSITION_PILOT: 1
V1_0_CONSTRUCTED_CROSSVALIDATOR_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 8

EXTERNAL_APPLICATIONS_COMPLETED: 4
EXTERNAL_DOMAINS_COMPLETED: 4
EXTERNAL_BLIND_PRECOMMITS_BLOCKED_UNSCORED: 1
METHOD_FAMILY_LINKAGE_PILOTS: 1

CURRENT_PROTOCOL_FOR_NEW_RUNS: v1.0
INTERNAL_PROTOCOL_STATUS: standardized
LATEST_COMPLETED_DIRECT_RESULT: SPECIFICATION_V1_0_DEPENDENCY_LABEL_WITHHELD_CROSSVALIDATOR_PASS_WITH_LIMITATIONS
LATEST_COMPLETED_EXTERNAL_RESULT: SPECIFICATION_V1_0_EXTERNAL_LABELED_REGRESSION_NO_GAIN_WITH_LIMITATIONS
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established
ALL_METHOD_HANDOFF_INTEROPERABILITY: not_established
CURRENT_METHOD_EVIDENCE_STATUS: developing
```

Further evidence should prioritize a genuinely evaluator-separated external case, independent retrace, measured practical benefit where feasible, or a concrete second receiving-method linkage. Blocked/unscored attempts remain visible and do not count as completed evidence.
