# Current Evidence Applicability Matrix / 현재 증거 적용성 행렬

Status: current migration map + seven Specification direct constructed pilots + three external Specification applications + completed first maturity audit  
Date: 2026-09-07

This file classifies existing method evidence without retroactively turning one method's results into validation of all 22 DSD methods.

## Interpretation key / 해석 키

- **Direct** = the record directly tested the named method.
- **Shared support** = the record supports a reusable method-family discipline, but does not directly validate another method.
- **Conditional transfer** = the shared rule applies only when the receiving method exposes the relevant structure or claim type.
- **Protocol prepared** = a dedicated method protocol exists, but protocol existence alone is not direct validation.
- **Direct pilot** = a method-specific challenge directly tested the method under its own protocol or locked prospective profile, but established status is not thereby implied.
- **External application** = the method is applied under locked criteria to material authored independently of DSD; this origin class does not imply an independent evaluator.
- **Maturity meta-audit** = DSD Audit evaluates whether accumulated evidence justifies a method-status transition; it is not another direct pilot of the audited method.

## Analysis corpus / 분석론 기록

`ANL-CH-001` through `ANL-CH-009` remain direct evidence for **DSD Analysis** challenge criteria only.

## Audit corpus / 감사 기록

Existing `DSD_Audit/` and new audit records remain direct evidence for **DSD Audit** procedures and verdict discipline only.

## DSD Specification / DSD 명세론

Protocol versions:

```text
v0.1 historical:
  methods/03_specification/PROTOCOL.md

v0.2 historical / APP-002 protocol:
  methods/03_specification/PROTOCOL_v0.2.md

v0.2.1 current for new runs / APP-003 protocol:
  methods/03_specification/PROTOCOL_v0.2.1.md
```

```text
METHOD: DSD Specification
METHOD_STATUS: developing
CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2.1

V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
V0_2_1_OPENNESS_TRANSITION_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 7
EXTERNAL_APPLICATIONS_TOTAL: 3
EXTERNAL_DOMAINS_TOTAL: 3
V0_2_EXTERNAL_APPLICATIONS: 1
V0_2_1_EXTERNAL_APPLICATIONS: 1
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

Accepted prospective v0.2.1 distinction:

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

This first external v0.2.1 application supports source-faithful use of the openness/determinacy axes on an operational/regulatory corpus. It does **not** show task-matched superiority: OSHA's own regulation, cross-referenced eTool, and checklist already provide a strong baseline for the locked structural-review task.

### First maturity meta-audit

```text
SPEC_MATURITY_AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
SPEC_MATURITY_CURRENT_DEVELOPING_STATUS: CONFIRMED
SPEC_MATURITY_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
SPEC_MATURITY_STATUS_DECISION: RETAIN_DEVELOPING
```

This audit predates `SPEC-APP-002`, `SPEC-CH-007`, and `SPEC-APP-003`; it remains historical until a new re-audit.

```text
CURRENT_STATUS_AFTER_LATEST_EVIDENCE: developing
ESTABLISHED_STATUS_AFTER_LATEST_EVIDENCE: not_reaudited
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established
SAME_PROJECT_EVALUATOR_DEPENDENCE: present
NEXT_EVIDENCE: genuinely_independent_retrace_or_dependency_discounted_maturity_reaudit
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

DEVELOPING_WITH_DIRECT_AND_EXTERNAL_APPLICATION_EVIDENCE:
  DSD Specification
    direct_constructed_pilots: 7
    current_protocol_for_new_runs: v0.2.1
    external_applications_total: 3
    external_domains_total: 3
    v0.2.1_external_applications: 1
    latest_external_result: SPEC_NO_GAIN_WITH_GUARDRAIL_PRESSURE
    independent_evaluator_validation: not_established
    measured_practical_benefit: not_established
    first_maturity_audit: historical_before_latest_evidence
    established_status_after_latest_evidence: not_reaudited
    current_status: developing

SHARED_CORE_REGISTRY_STATUS:
  closed_for_current_registry_with_conditions
```

## Migration rule / 이관 규칙

Historical records keep their original path, protocol version, and verdict. New protocol revisions and evidence classification are additive. Do not rewrite prior `PASS`, `FAIL`, `NO_GAIN`, `BASELINE_PREFERRED`, `NON_CORRESPONDENCE`, or untested-axis status merely to appear current.
