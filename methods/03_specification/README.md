# 03. DSD Specification / DSD 명세론

Status: **internally standardized at Protocol v1.0 / method evidence maturity remains developing** — v0.1/v0.2/v0.2.1 records remain historical evidence under their original protocols. `DSD-AUDIT-20260908-METHODOLOGY-004` passed all 14 critical standardization gates and approved v1.0 as the default DSD-internal Specification protocol for new runs. This is an interface-standardization judgment, not independent external validation or superiority over existing specification methods.

Task: state explicitly what entities, statuses, inputs, prerequisites, outputs, transitions, and distinctions a system or study must preserve **without silently replacing the source's original purpose, priority, audience function, viewpoint, intentionally open judgment boundary, or site-specific implementation freedom with DSD-imposed structure**.

Primary DSD sources: Formation + General Property; Static Aggregation and Dynamics when output, reduction, or transition specifications matter.

Typical outputs include typed requirement/status records, explicit bridges, external-standard boundaries, violation/unresolved conditions, guardrail records, and—when relevant—separate source-openness and downstream-determinacy records.

Boundary: DSD Specification organizes structural requirements; it does not replace domain-specific requirements engineering, standards, law, safety rules, clinical standards, scientific definitions, professional judgment, or other competent validation authorities.

## Protocol versions / 프로토콜 버전

- [`PROTOCOL.md`](PROTOCOL.md) — **v0.1 historical**, used for `SPEC-CH-001~005`, `SPEC-APP-001`, and first maturity-audit-era records.
- [`PROTOCOL_v0.2.md`](PROTOCOL_v0.2.md) — **v0.2 historical**, used for `SPEC-CH-006` and `SPEC-APP-002`.
- [`PROTOCOL_v0.2.1.md`](PROTOCOL_v0.2.1.md) — **v0.2.1 historical/evidence basis**, used for `SPEC-CH-007`, `SPEC-APP-003`, and `SPEC-LINK-001`.
- [`PROTOCOL_v1.0.md`](PROTOCOL_v1.0.md) — **standard / default DSD-internal protocol for new Specification runs** after final standardization audit.

v1.0 preserves the stable v0.2.1 semantics while applying only the audited non-breaking cleanup package:

```text
C1 explicit conditionality for context-dependent fields
C2 atom-level VALIDATION_STANDARD inheritance
C3 minimal-core / extended-ledger output separation
C4 NO_GAIN_STATUS as a derived compatibility view
C5 G1-G4 and openness/determinacy preserved without expansion
C6 v0.x protocol/evidence history preserved
```

## Stable v1.0 semantic core / 안정화된 v1.0 핵심

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION

SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS

HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

Conditional fields and ledgers are activated only when material to the declared task. Static Aggregation, Dynamics, and optional specializations are not forced into inactive cases.

## Direct method evidence / 개별 방법 직접 증거

Evidence lane: [`../../evidence/method_specific/specification/`](../../evidence/method_specific/specification/)

```text
SPEC-CH-001~005  v0.1 direct pilots
SPEC-CH-006      guardrail centerline challenge
SPEC-CH-007      source-openness / downstream-determinacy boundary challenge
SPEC-CH-008      v1.0 dependentRequired label-withheld software cross-validator challenge
```

### SPEC-CH-006

```text
EXACT_GUARDRAIL_FAMILY_MATCHES: 8/8
FALSE_HARD_FAILURE_ON_PRESSURE_CASES: 0
RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-007

```text
EXACT_SOURCE_OPENNESS_AXIS_MATCHES: 8/8
EXACT_DOWNSTREAM_DETERMINACY_AXIS_MATCHES: 8/8
EXACT_JOINT_AXIS_MATCHES: 8/8
RESULT: SPECIFICATION_OPENNESS_DETERMINACY_AXIS_SEPARATION_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-008

```text
PRECOMMIT: 92277445b73a72d7d4d9ff29f849d7068eb4244a
PREDICTION_COMMIT: 7c5f32231d21b4b59251f4093a7116ab899bfb4e
CROSS_VALIDATOR: Python jsonschema 4.26.0 / Draft202012Validator
CROSS_VALIDATOR_MATCHES: 16/16
POST_REVEAL_PREDICTION_CHANGE: 0
FALSE_BIDIRECTIONAL_INFERENCE: 0
FALSE_FAILURE_ON_NON_OBJECT: 0
IRRELEVANT_OPTIONAL_LEDGERS_ACTIVATED: 0
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_DEPENDENCY_LABEL_WITHHELD_CROSSVALIDATOR_PASS_WITH_LIMITATIONS
```

This is a constructed direct pilot with post-freeze software-validator comparison. It is not independent evaluator validation or an external real-world application.

## External applications / 외부 적용

External evidence lane: [`../../evidence/real_world_cases/specification/`](../../evidence/real_world_cases/specification/)

### SPEC-APP-001 — RFC 9112 §6.3
Protocol: **v0.1**.
```text
SOURCE_UNIT_COVERAGE: 13/13
PRECEDENCE_PRESERVATION: 13/13
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

### SPEC-APP-002 — Belmont Report Part C
Protocol: **v0.2**.
```text
SOURCE_UNIT_COVERAGE: 22/22
LOCAL_PRIORITY_PRESERVATION: 5/5
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED: 4/4
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
```

### SPEC-APP-003 — OSHA Emergency Action Plan core corpus
Protocol: **v0.2.1**.
```text
SOURCE_UNIT_COVERAGE: 18/18
REGULATORY_MINIMUM_ELEMENTS_PRESERVED: 11/11
SITE_SPECIFIC_OPENNESS_HANDLED_WITHOUT_FABRICATION: 7/7
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

### SPEC-APP-004 — WCAG 2.2 Contrast (Minimum) + official ACT examples
Protocol: **v1.0**.

```text
EXTERNAL_DOMAIN: web accessibility / WCAG text contrast
SELECTED_OFFICIAL_EXAMPLES: 8
EXAMPLE_OUTCOME_FAMILY_MATCHES: 8/8
NORMAL_LARGE_THRESHOLD_SEPARATION: pass
INCIDENTAL_INACTIVE_BOUNDARY_PRESERVATION: pass
INACTIVE_CONDITIONAL_LEDGER_BOILERPLATE: 0
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
RESULT: SPECIFICATION_V1_0_EXTERNAL_LABELED_REGRESSION_NO_GAIN_WITH_LIMITATIONS
```

Because the official W3C ACT outcome labels were visible before mapping, `SPEC-APP-004` is a labeled regression/interface check rather than blind predictive evidence.

### SPEC-APP-005 — JSON Schema official test-suite blind attempt

```text
PRECOMMIT: 154af0ae57e1cc6bc78bdefdcfb83faf1ba71a9c
STATUS: BLOCKED_BY_LABEL_ISOLATION_TOOLING
COUNT_AS_EXTERNAL_APPLICATION_COMPLETION: no
COUNT_AS_BLIND_EVIDENCE: no
```

The official test file embeds expected `valid` labels alongside schema/data, and the current source-delivery path could not redact those labels before evaluator exposure. The precommit was preserved rather than weakened. `SPEC-CH-008` is separately classified and does not substitute for completion of this external application.

### SPEC-APP-006 — python-jsonschema `ErrorTree` issue #1328

Protocol: **v1.0**.

```text
PRECOMMIT: 70a9ffd9b02d839057f1efb62b7c8a605e6cc813
FROZEN_PREDICTION: cbabc9d6533da1643588a1b934d5a41da2be6022
ACTUAL_CLOSING_COMMIT: 7fa1acc948b34ab6283b3621ecbdc4360a717ba7
CASE_ORIGIN: organizational_or_technical_incident
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
PRIMARY_AXES_MATCHED: 5/5
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
SOURCE_FACT_INVENTION_COUNT: 0
POST_REVEAL_PREDICTION_CHANGE: 0
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_REAL_WORLD_RESOLUTION_WITHHELD_ACCEPTANCE_MATCH_WITH_LIMITATIONS
```

The issue body was used to freeze the repair acceptance semantics before maintainer comments, candidate PRs, and the actual closing commit were read. The closing implementation matched the predicted non-mutating iteration/containment behavior, preserved the genuine error child, kept valid error-free child access supported, and added the predicted regression-test family. Adjacent lookup-error improvements were not retroactively added to the prediction.

This is a **resolution-artifact-withheld real-world comparison**, stronger than a labeled regression but still not a fully blind or independent-evaluator validation.

### SPEC-APP-007 — Flask `stream_with_context` issue #5804

Protocol: **v1.0**.

```text
PRECOMMIT: f6bca91ec8b5e6db5d88be603f57f865567a2f12
FROZEN_PREDICTION: 09ea2055c9fedce578f7e993003287ee5f327d60
MAINTAINER_RESOLUTION_PR: pallets/flask#5812
CASE_ORIGIN: organizational_or_technical_incident
EXTERNAL_DOMAIN: Python web framework / streamed-response request-context lifecycle
SELECTED_DSD_LAYERS: PROPERTY_CORE + DYNAMICS_LAYER
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
FULL_MATCH_AXES: 5/6
PARTIAL_MATCH_AXES: 1/6
NON_MATCH_AXES: 0/6
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
POST_REVEAL_PREDICTION_CHANGE: 0
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_REAL_WORLD_LIFECYCLE_RESOLUTION_WITHHELD_MATCH_WITH_ONE_TEST_COVERAGE_PARTIAL
```

The behavior-level lifecycle contract matched the actual merged-context / push-count repair on five axes. The sixth precommitted axis remained only partial because PR #5812 preserved/adapted general stream-context retention tests but did not add a dedicated issue-#5804 teardown timing/count regression reproduction. This unfavorable partial is preserved rather than promoted to a full match.

`SPEC-APP-007` also gives the first completed v1.0 external Specification case in the current evidence sequence where `DYNAMICS_LAYER` was materially selected for transition ordering instead of being forced as boilerplate.

## Method-family linkage / 방법군 연계

`SPEC-LINK-001` tested the first direct DSD-native receiving-method boundary:

```text
external OSHA source
-> DSD Specification v0.2.1
-> DSD Audit
```

```text
AUDIT_FINDING_MATCHES: 6/6
REQUIREMENT_IDENTITY_PRESERVATION: pass
NORMATIVE_FORCE_PRESERVATION: pass
OPENNESS_PRESERVATION: pass
HIDDEN_RETRANSLATION_REQUIRED: no
EXTERNAL_STANDARD_BOUNDARY_PRESERVED: yes
RESULT: SPECIFICATION_TO_AUDIT_NATIVE_HANDOFF_PILOT_PASS_WITH_LIMITATIONS
```

This supports:

```text
STANDALONE_NO_GAIN
!= METHOD_FAMILY_INTEGRATION_NO_GAIN
```

## Protocol audits / 프로토콜 감사

```text
DSD-AUDIT-20260908-METHODOLOGY-003
  PROTOCOL_FREEZE_READINESS: FREEZE_READY_WITH_NONBREAKING_CLEANUP

DSD-AUDIT-20260908-METHODOLOGY-004
  CRITICAL_GATES_PASSED: 14/14
  REGRESSION_FAMILIES_WITH_REQUIRED_CARRIER_LOSS: 0/11
  STANDARDIZATION_VERDICT: STANDARDIZE_WITH_DOCUMENTED_LIMITS
  DEFAULT_DSD_INTERNAL_PROTOCOL: DSD Specification Protocol v1.0
```

Protocol standardization remains separate from evidence maturity.

## Maturity audit / 성숙도 감사

The first maturity audit remains historical:

```text
AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

## Evidence state / 증거 상태

```text
V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
V0_2_1_OPENNESS_TRANSITION_PILOT: 1
V1_0_CONSTRUCTED_CROSSVALIDATOR_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 8

EXTERNAL_APPLICATIONS_COMPLETED: 6
EXTERNAL_DOMAINS_COMPLETED: 6
EXTERNAL_BLIND_PRECOMMITS_BLOCKED_UNSCORED: 1
RESOLUTION_WITHHELD_REAL_WORLD_APPLICATIONS: 2
V1_0_EXTERNAL_APPLICATIONS_COMPLETED: 3
METHOD_FAMILY_LINKAGE_PILOTS: 1

CURRENT_PROTOCOL_FOR_NEW_RUNS: v1.0
INTERNAL_PROTOCOL_STATUS: standardized
LATEST_DIRECT_RESULT: SPECIFICATION_V1_0_DEPENDENCY_LABEL_WITHHELD_CROSSVALIDATOR_PASS_WITH_LIMITATIONS
LATEST_EXTERNAL_RESULT: SPECIFICATION_V1_0_REAL_WORLD_LIFECYCLE_RESOLUTION_WITHHELD_MATCH_WITH_ONE_TEST_COVERAGE_PARTIAL
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established
ALL_METHOD_HANDOFF_INTEROPERABILITY: not_established
METHOD_EVIDENCE_STATUS: developing
```

## Next evidence priority / 다음 증거 우선순위

v1.0 remains the internal default. Further protocol revision should require a concrete defect or new stable obligation rather than routine expansion.

After two resolution-withheld real-world cases, the highest-value next evidence is no longer merely another software issue. Priority should move toward independent evaluator retrace, measured practical benefit where feasible, or a real-world application from a materially different non-software domain with naturally separated input and later outcome. Additional receiving-method linkage should be added only when it answers a concrete interoperability question. Blocked/unscored tests remain visible rather than being converted into apparent successes.
