# Current Evidence Applicability Matrix / 현재 증거 적용성 행렬

Status: current migration map + eight Specification direct constructed pilots + five completed external Specification applications + one blocked unscored external blind precommit + one method-family linkage pilot + internal v1.0 standardization completed  
Date: 2026-09-08

This file classifies existing method evidence without retroactively turning one method's results into validation of all 22 DSD methods.

## Interpretation key / 해석 키

- **Direct** = the record directly tested the named method.
- **Shared support** = reusable method-family discipline, not direct validation of another method.
- **Direct pilot** = method-specific challenge under its own locked protocol/profile.
- **External application** = application to material authored independently of DSD; external origin does not imply independent evaluator.
- **Blocked/unscored precommit** = planned evidence whose locked test condition could not be satisfied; it remains visible but is not counted as completed evidence.
- **Resolution-artifact-withheld external application** = a real-world source is used to freeze an acceptance prediction before comments/patches/closing resolution are exposed; stronger than a labeled regression, but not equivalent to independent-evaluator or full-blind validation.
- **Method-family linkage pilot** = tests one locked inter-method handoff boundary only.
- **Protocol standardization audit** = tests internal interface stability/default-use readiness, not external maturity.
- **Maturity meta-audit** = evaluates whether accumulated evidence justifies a method-status transition.

## Analysis corpus / 분석론 기록

`ANL-CH-001` through `ANL-CH-009` remain direct evidence for **DSD Analysis** challenge criteria only.

## Audit corpus / 감사 기록

Existing `DSD_Audit/` and new audit records remain direct evidence for **DSD Audit** procedures and verdict discipline only. Methodology audits of another DSD method are not automatically counted as new direct Audit validation cases.

## DSD Specification / DSD 명세론

```text
METHOD: DSD Specification
METHOD_EVIDENCE_STATUS: developing
INTERNAL_PROTOCOL_STATUS: standardized
CURRENT_PROTOCOL_FOR_NEW_RUNS: v1.0

V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
V0_2_1_OPENNESS_TRANSITION_PILOT: 1
V1_0_CONSTRUCTED_CROSSVALIDATOR_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 8

EXTERNAL_APPLICATIONS_COMPLETED: 5
EXTERNAL_DOMAINS_COMPLETED: 5
EXTERNAL_BLIND_PRECOMMITS_BLOCKED_UNSCORED: 1
RESOLUTION_WITHHELD_REAL_WORLD_APPLICATIONS: 1
V1_0_EXTERNAL_APPLICATIONS_COMPLETED: 2
METHOD_FAMILY_LINKAGE_PILOTS: 1
```

### Stable v1.0 distinctions

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION

SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS

HARD_FAILURE
!= GUARDRAIL_PRESSURE
```

### Direct pilots SPEC-CH-001~007

Historical direct results remain under the protocol version in which they were produced:

```text
SPEC-CH-001 discrimination
SPEC-CH-002 contradiction / underspecification
SPEC-CH-003 optional-layer / bridge boundary
SPEC-CH-004 NO_GAIN
SPEC-CH-005 procedural retrace / order stability
SPEC-CH-006 guardrail centerline
SPEC-CH-007 source openness / downstream determinacy
```

None is silently rescored under v1.0.

### SPEC-CH-008 — v1.0 dependency label-withheld cross-validator

```text
CASE_ORIGIN: constructed_method_specific_challenge
NORMATIVE_BASIS: JSON Schema Draft 2020-12 Validation §6.5.4
PRECOMMIT: 92277445b73a72d7d4d9ff29f849d7068eb4244a
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

This supports v1.0 dependency and conditional-field behavior on the locked cases. It is not independent evaluator validation because the cases and DSD reasoning were produced within the same project/model environment. The software implementation was invoked only after predictions were frozen.

### Completed external applications

```text
SPEC-APP-001 — RFC 9112 §6.3
  protocol: v0.1
  result: SPEC_NO_GAIN / baseline preferred

SPEC-APP-002 — Belmont Report Part C
  protocol: v0.2
  result: usable / mixed gain with guardrail pressure

SPEC-APP-003 — OSHA EAP core corpus
  protocol: v0.2.1
  result: SPEC_NO_GAIN / guardrail pressure / baseline preferred

SPEC-APP-004 — WCAG 2.2 SC 1.4.3 + official ACT examples
  protocol: v1.0
  external domain: web accessibility
  official example family matches: 8/8
  inactive conditional ledger boilerplate: 0
  result: SPECIFICATION_V1_0_EXTERNAL_LABELED_REGRESSION_NO_GAIN_WITH_LIMITATIONS

SPEC-APP-006 — python-jsonschema ErrorTree issue #1328
  protocol: v1.0
  external domain: Python library API behavior / error-structure semantics
  resolution artifacts withheld until after prediction: yes
  actual closing commit: 7fa1acc948b34ab6283b3621ecbdc4360a717ba7
  primary axes matched: 5/5
  implementation overprediction: 0
  post-reveal prediction change: 0
  final status: usable
  result: SPECIFICATION_V1_0_REAL_WORLD_RESOLUTION_WITHHELD_ACCEPTANCE_MATCH_WITH_LIMITATIONS
```

`SPEC-APP-004` is a labeled regression/interface check because expected ACT labels were visible before DSD mapping. It is not blind prediction evidence.

`SPEC-APP-006` is the first completed real-world case where the actual maintainer resolution was naturally separated and withheld until after the DSD acceptance contract was frozen. It supports case-level resolution alignment but does not establish independent evaluator validation, full blindness, or measured engineering benefit.

### Blocked external blind attempt — SPEC-APP-005

```text
SOURCE: JSON-Schema-Test-Suite dependentRequired.json
PINNED_COMMIT: f6fd52a0a95472e079cbfc6ef7f089702b80e045
PRECOMMIT: 154af0ae57e1cc6bc78bdefdcfb83faf1ba71a9c
STATUS: BLOCKED_BY_LABEL_ISOLATION_TOOLING
PREDICTIONS_COMMITTED: no
OFFICIAL_LABELS_SCORED: no
COUNT_AS_EXTERNAL_APPLICATION_COMPLETION: no
COUNT_AS_BLIND_EVIDENCE: no
```

The locked official source combines input and expected labels in one file, and the current delivery path could not redact expected labels before evaluator exposure. The precommit was preserved rather than weakened after the tooling constraint appeared.

### Method-family linkage — SPEC-LINK-001

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

This supports one native handoff boundary only and does not validate universal interoperability.

### Protocol audits

```text
DSD-AUDIT-20260908-METHODOLOGY-003
  PROTOCOL_FREEZE_READINESS: FREEZE_READY_WITH_NONBREAKING_CLEANUP

DSD-AUDIT-20260908-METHODOLOGY-004
  CRITICAL_GATES_PASSED: 14/14
  BREAKING_SEMANTIC_LOSS: 0
  REGRESSION_FAMILIES_WITH_REQUIRED_CARRIER_LOSS: 0/11
  STANDARDIZATION_VERDICT: STANDARDIZE_WITH_DOCUMENTED_LIMITS
  DEFAULT_DSD_INTERNAL_PROTOCOL: DSD Specification Protocol v1.0
```

### Maturity boundary

```text
FIRST_MATURITY_AUDIT: DSD-AUDIT-20260907-METHODOLOGY-001
HISTORICAL_PROMOTION_VERDICT: INSUFFICIENT_BASIS
CURRENT_METHOD_EVIDENCE_STATUS: developing
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established
SAME_PROJECT_EVALUATOR_DEPENDENCE: present
ALL_METHOD_HANDOFF_INTEROPERABILITY: not_established
```

## Shared-core registry status / 공통 코어 상태

```text
SHARED_CORE_RULES_PROMOTED: 10
SHARED_CORE_CLOSURE_RESULT: closed_for_current_registry_with_conditions
DIRECT_METHOD_VALIDATION_FROM_SHARED_CORE: not claimed
SPECIFICATION_GUARDRAIL_PROFILE_PROMOTED_TO_SHARED_CORE: no
SPECIFICATION_OPENNESS_DETERMINACY_AXES_PROMOTED_TO_SHARED_CORE: no
```

## Current overall classification / 현재 총괄 분류

```text
DIRECTLY_MATURE_METHOD_EVIDENCE:
  DSD Analysis
  DSD Audit

INTERNALLY_STANDARDIZED_BUT_EVIDENCE_DEVELOPING:
  DSD Specification
    direct_constructed_pilots: 8
    current_protocol_for_new_runs: v1.0
    internal_protocol_status: standardized
    completed_external_applications: 5
    completed_external_domains: 5
    blocked_unscored_external_blind_precommits: 1
    resolution_withheld_real_world_applications: 1
    method_family_linkage_pilots: 1
    independent_evaluator_validation: not_established
    measured_practical_benefit: not_established
    all_method_handoff_interoperability: not_established
    current_method_evidence_status: developing

SHARED_CORE_REGISTRY_STATUS:
  closed_for_current_registry_with_conditions
```

## Migration rule / 이관 규칙

Historical records keep their original path, protocol version, and verdict. New protocol revisions and evidence classification are additive. Do not rewrite prior `PASS`, `FAIL`, `NO_GAIN`, `BASELINE_PREFERRED`, `NON_CORRESPONDENCE`, blocked/unscored status, or untested-axis status merely to appear current.
