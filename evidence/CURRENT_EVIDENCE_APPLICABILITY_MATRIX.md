# Current Evidence Applicability Matrix / 현재 증거 적용성 행렬

Status: current migration map + seven Specification direct constructed pilots + three external Specification applications + one method-family linkage pilot + internal v1.0 standardization completed  
Date: 2026-09-08

This file classifies existing method evidence without retroactively turning one method's results into validation of all 22 DSD methods.

## Interpretation key / 해석 키

- **Direct** = the record directly tested the named method.
- **Shared support** = the record supports a reusable method-family discipline, but does not directly validate another method.
- **Conditional transfer** = the shared rule applies only when the receiving method exposes the relevant structure or claim type.
- **Protocol prepared** = a dedicated method protocol exists, but protocol existence alone is not direct validation.
- **Direct pilot** = a method-specific challenge directly tested the method under its own protocol or locked prospective profile, but established status is not thereby implied.
- **External application** = the method is applied under locked criteria to material authored independently of DSD; this origin class does not imply an independent evaluator.
- **Method-family linkage pilot** = tests whether one method's typed output can be consumed by another DSD method at a locked interface; it does not directly validate the receiving method or all inter-method boundaries.
- **Protocol standardization audit** = tests internal interface stability/default-use readiness; it does not imply evidence maturity or external superiority.
- **Maturity meta-audit** = DSD Audit evaluates whether accumulated evidence justifies a method-status transition; it is not another direct pilot of the audited method.

## Analysis corpus / 분석론 기록

`ANL-CH-001` through `ANL-CH-009` remain direct evidence for **DSD Analysis** challenge criteria only.

## Audit corpus / 감사 기록

Existing `DSD_Audit/` and new audit records remain direct evidence for **DSD Audit** procedures and verdict discipline only. Methodology audits of another DSD method are not automatically counted as new direct Audit validation cases.

## DSD Specification / DSD 명세론

Protocol versions:

```text
v0.1 historical:
  methods/03_specification/PROTOCOL.md

v0.2 historical:
  methods/03_specification/PROTOCOL_v0.2.md

v0.2.1 historical/evidence basis:
  methods/03_specification/PROTOCOL_v0.2.1.md

v1.0 standard/default for new DSD-internal runs:
  methods/03_specification/PROTOCOL_v1.0.md
```

```text
METHOD: DSD Specification
METHOD_EVIDENCE_STATUS: developing
INTERNAL_PROTOCOL_STATUS: standardized
CURRENT_PROTOCOL_FOR_NEW_RUNS: v1.0

V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
V0_2_1_OPENNESS_TRANSITION_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 7
EXTERNAL_APPLICATIONS_TOTAL: 3
EXTERNAL_DOMAINS_TOTAL: 3
METHOD_FAMILY_LINKAGE_PILOTS: 1
```

### v0.1 direct evidence

```text
SPEC_CH_001_RESULT: SPECIFICATION_DISCRIMINATION_PILOT_PASS_WITH_LIMITATIONS
SPEC_CH_002_RESULT: SPECIFICATION_CONTRADICTION_UNDERSPECIFICATION_PILOT_PASS_WITH_LIMITATIONS
SPEC_CH_003_RESULT: SPECIFICATION_OPTIONAL_LAYER_BRIDGE_BOUNDARY_PILOT_PASS_WITH_LIMITATIONS
SPEC_CH_004_RESULT: SPECIFICATION_NO_GAIN_PILOT_PASS_WITH_LIMITATIONS
SPEC_CH_005_RESULT: SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_PASS_WITH_LIMITATIONS
SPEC_CH_005_INDEPENDENT_EVALUATOR_VALIDATION: not_established
```

### SPEC-CH-006 guardrail centerline evidence

```text
SPEC_CH_006_PRECOMMIT: fe009d8da9ab992e6885d07e14ff26355b776a86
SPEC_CH_006_EXACT_GUARDRAIL_FAMILY_MATCHES: 8/8
SPEC_CH_006_FALSE_HARD_FAILURE_ON_PRESSURE_CASES: 0
SPEC_CH_006_FALSE_REJECTION_OF_DECLARED_DERIVATIVE_VIEW: 0
SPEC_CH_006_RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-007 openness / determinacy axis separation

```text
SPEC_CH_007_PRECOMMIT: 1b3665696007b29535b3f46815cad39f4f02c03f
SPEC_CH_007_EXACT_SOURCE_OPENNESS_AXIS_MATCHES: 8/8
SPEC_CH_007_EXACT_DOWNSTREAM_DETERMINACY_AXIS_MATCHES: 8/8
SPEC_CH_007_EXACT_JOINT_AXIS_MATCHES: 8/8
SPEC_CH_007_FALSE_UNDERSPEC_ON_TASK_SUFFICIENT_OPENNESS: 0
SPEC_CH_007_FALSE_OPENNESS_EXCUSE_FOR_MISSING_DATA: 0
SPEC_CH_007_FALSE_DETERMINACY_FROM_INVENTED_VALUE: 0
SPEC_CH_007_RESULT: SPECIFICATION_OPENNESS_DETERMINACY_AXIS_SEPARATION_PILOT_PASS_WITH_LIMITATIONS
```

Accepted stable distinction:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

`SPEC_UNDERSPECIFIED` remains task-relative.

### External application — SPEC-APP-001

Protocol: v0.1.

```text
CASE_ORIGIN: public_normative_standard
SOURCE: RFC 9112 §6.3
EXTERNAL_DOMAIN: HTTP message framing
SOURCE_UNIT_COVERAGE: 13/13
PRECEDENCE_PRESERVATION: 13/13
SOURCE_FIDELITY_RESULT: pass
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

### External application — SPEC-APP-002

Protocol: v0.2.

```text
CASE_ORIGIN: public_normative_ethics_guideline
SOURCE: Belmont Report Part C. Applications
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

### External application — SPEC-APP-003

Protocol: v0.2.1.

```text
CASE_ORIGIN: public_regulatory_standard_plus_official_guidance
SOURCE: OSHA 29 CFR 1910.38 + official EAP/alarm eTool/checklist material
EXTERNAL_DOMAIN: workplace emergency planning / occupational safety
PRECOMMIT: ccda4cfe9e9b25b3a97029c6a19c2e8e07076eb0
SOURCE_UNIT_COVERAGE: 18/18
REGULATORY_MINIMUM_ELEMENTS_PRESERVED: 11/11
SITE_SPECIFIC_OPENNESS_HANDLED_WITHOUT_FABRICATION: 7/7
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
INVENTED_SITE_SPECIFIC_FACTS: 0
NORMATIVE_FORCE_STRENGTHENINGS: 0
REGULATION_GUIDANCE_COLLAPSE: 0
HARD_FAILURE_COUNT: 0
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
RESULT: SPECIFICATION_EXTERNAL_V0_2_1_NO_GAIN_WITH_GUARDRAIL_PRESSURE
```

This external v0.2.1 application supports source-faithful use of the openness/determinacy axes on an operational/regulatory corpus. It does **not** show task-matched superiority: OSHA's own regulation, cross-referenced eTool, and checklist already provide a strong baseline for the locked structural-review task.

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

This supports one native handoff boundary only:

```text
STANDALONE_NO_GAIN
!= METHOD_FAMILY_INTEGRATION_NO_GAIN
```

It does not validate all 22 methods or universal interoperability.

### Protocol minimality/stability audit

```text
AUDIT_ID: DSD-AUDIT-20260908-METHODOLOGY-003
PROTOCOL_FREEZE_READINESS: FREEZE_READY_WITH_NONBREAKING_CLEANUP
STRUCTURAL_CONFLICT_COUNT: 0
BREAKING_SEMANTIC_REVISION_REQUIRED: no
STRUCTURAL_REDESIGN_REQUIRED: no
```

### Protocol v1.0 final standardization audit

```text
AUDIT_ID: DSD-AUDIT-20260908-METHODOLOGY-004
CRITICAL_GATES_PASSED: 14/14
CRITICAL_FAILURES: 0
BREAKING_SEMANTIC_LOSS: 0
REGRESSION_FAMILIES_WITH_REQUIRED_CARRIER_LOSS: 0/11
NEW_UNPRECOMMITTED_SEMANTIC_OBLIGATION: 0
STANDARDIZATION_VERDICT: STANDARDIZE_WITH_DOCUMENTED_LIMITS
DEFAULT_DSD_INTERNAL_PROTOCOL: DSD Specification Protocol v1.0
METHOD_EVIDENCE_STATUS: developing
METHOD_MATURITY_PROMOTION: no
```

The standardization audit approves v1.0 as the default DSD-internal interface. It does not convert internal standardization into an evidence-maturity or superiority claim.

### First maturity meta-audit

```text
SPEC_MATURITY_AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
SPEC_MATURITY_CURRENT_DEVELOPING_STATUS: CONFIRMED
SPEC_MATURITY_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
SPEC_MATURITY_STATUS_DECISION: RETAIN_DEVELOPING
```

That historical maturity verdict is not silently overwritten by protocol standardization.

```text
CURRENT_METHOD_EVIDENCE_STATUS: developing
INTERNAL_PROTOCOL_STATUS: standardized
CURRENT_PROTOCOL_FOR_NEW_RUNS: v1.0
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established
SAME_PROJECT_EVALUATOR_DEPENDENCE: present
ALL_METHOD_HANDOFF_INTEROPERABILITY: not_established
NEXT_EVIDENCE: independent_retrace_or_measured_benefit_or_concrete_second_handoff_question
```

## Shared-core registry status / 공통 코어 상태

The current shared-core registry contains **SC-01 through SC-10** and remains closed for the present registry with conditions.

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
    direct_constructed_pilots: 7
    current_protocol_for_new_runs: v1.0
    internal_protocol_status: standardized
    external_applications_total: 3
    external_domains_total: 3
    method_family_linkage_pilots: 1
    latest_external_result: SPEC_NO_GAIN_WITH_GUARDRAIL_PRESSURE
    independent_evaluator_validation: not_established
    measured_practical_benefit: not_established
    all_method_handoff_interoperability: not_established
    current_method_evidence_status: developing

SHARED_CORE_REGISTRY_STATUS:
  closed_for_current_registry_with_conditions
```

## Migration rule / 이관 규칙

Historical records keep their original path, protocol version, and verdict. New protocol revisions and evidence classification are additive. Do not rewrite prior `PASS`, `FAIL`, `NO_GAIN`, `BASELINE_PREFERRED`, `NON_CORRESPONDENCE`, or untested-axis status merely to appear current.
