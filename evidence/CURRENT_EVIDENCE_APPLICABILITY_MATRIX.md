# Current Evidence Applicability Matrix / 현재 증거 적용성 행렬

Status: current migration map + six Specification direct constructed pilots + first external Specification application + completed maturity audit  
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

`ANL-CH-001` through `ANL-CH-009` remain direct evidence for **DSD Analysis** challenge criteria only. Their shared lessons may support common rules, but do not directly validate another method.

## Audit corpus / 감사 기록

Existing `DSD_Audit/` and new audit records remain direct evidence for **DSD Audit** procedures and verdict discipline only. Shared lessons do not automatically validate Specification, Prediction, Reconstruction, or other methods.

## DSD Specification / DSD 명세론

Protocol versions:

```text
v0.1 historical protocol:
  methods/03_specification/PROTOCOL.md

v0.2 prospective current protocol for new runs:
  methods/03_specification/PROTOCOL_v0.2.md
```

The first five constructed pilots and `SPEC-APP-001` remain v0.1-era evidence. `SPEC-CH-006` directly tests the prospective purpose/detail/viewpoint guardrail distinction used to establish v0.2 for new runs.

```text
METHOD: DSD Specification
METHOD_STATUS: developing
CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2

V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 6
EXTERNAL_APPLICATIONS_TOTAL: 1
V0_2_EXTERNAL_APPLICATIONS: 0
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
SPEC_CH_006_UNDECLARED_PURPOSE_SHIFT_DETECTED: 1/1
SPEC_CH_006_AUTHORIAL_INTENT_OVERATTRIBUTION_DETECTED: 1/1
SPEC_CH_006_UNKNOWN_PURPOSE_PRESERVED_AS_UNDETERMINED: 1/1
SPEC_CH_006_SOURCE_FACT_INVENTION_ESCALATED_TO_HARD_FAILURE: 1/1
SPEC_CH_006_RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS
```

Accepted v0.2 guardrail ledger:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

and the method-specific distinction:

```text
HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

This is currently Specification-specific evidence. It does not reopen or add an SC shared-core ID.

### External application — SPEC-APP-001

Protocol: v0.1.

```text
CASE_ORIGIN: public_normative_standard
SOURCE: RFC 9112 §6.3
SOURCE_UNIT_COVERAGE: 13/13
PRECEDENCE_PRESERVATION: 13/13
BCP14_MUST_OBLIGATIONS_PRESERVED: 8/8
INVENTED_SOURCE_FACTS: 0
SOURCE_FIDELITY_RESULT: pass
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

The v0.2 guardrail axes were not separately precommitted in this v0.1 application:

```text
PURPOSE_FIDELITY_GUARDRAIL: untested_as_formal_axis
DETAIL_PROPORTIONALITY_GUARDRAIL: untested_as_formal_axis
VIEWPOINT_SEPARATION_GUARDRAIL: untested_as_formal_axis
```

Do not retroactively convert those fields to PASS.

### First maturity meta-audit

```text
SPEC_MATURITY_AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
SPEC_MATURITY_MINIMUM_COMPONENTS_PRESENT: 8/8
SPEC_MATURITY_CURRENT_DEVELOPING_STATUS: CONFIRMED
SPEC_MATURITY_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
SPEC_MATURITY_STATUS_DECISION: RETAIN_DEVELOPING
SPEC_MATURITY_ESTABLISHED_EVIDENCE_BREADTH: insufficient
SPEC_MATURITY_EXTERNAL_CORPUS_COUNT: 1
SPEC_MATURITY_EXTERNAL_DOMAIN_COUNT: 1
SPEC_MATURITY_INDEPENDENT_EVALUATOR_VALIDATION: not_established
SPEC_MATURITY_MEASURED_ENGINEERING_BENEFIT: not_established
```

The post-audit discovery of the v0.1 purpose/detail/viewpoint guardrail gap does not erase the audit. It adds a prospective protocol requirement and further supports withholding `established` status until v0.2 is tested on external corpora.

```text
ESTABLISHED_STATUS: not_justified_on_current_evidence
NEXT_DIRECT_APPLICATION: SPEC-APP-002_less_structured_external_corpus_under_v0.2
```

## Shared-core registry status / 공통 코어 상태

The current shared-core registry contains **SC-01 through SC-10** and remains closed for the present registry with conditions.

```text
SHARED_CORE_RULES_PROMOTED: 10
SPECIALIZATION_RESTRAINT: derived_profile
SHARED_CORE_CLOSURE_RESULT: closed_for_current_registry_with_conditions
DIRECT_METHOD_VALIDATION_FROM_SHARED_CORE: not claimed
SPECIFICATION_GUARDRAIL_PROFILE_PROMOTED_TO_SHARED_CORE: no
```

Purpose/detail/viewpoint guardrails remain Specification-method-specific until repeated independent evidence across multiple methods shows a stable domain-independent common obligation that cannot already be represented by the current shared-core architecture.

## Current overall classification / 현재 총괄 분류

```text
DIRECTLY_MATURE_METHOD_EVIDENCE:
  DSD Analysis
  DSD Audit

DEVELOPING_WITH_DIRECT_AND_EXTERNAL_APPLICATION_EVIDENCE:
  DSD Specification
    direct_constructed_pilots: 6
    current_protocol_for_new_runs: v0.2
    v0.2_external_applications: 0
    external_or_independent_corpus_applications_total: 1
    external_application_result: SPEC_NO_GAIN
    independent_evaluator_validation: not_established
    maturity_audit: completed
    established_promotion: insufficient_basis
    current_status: developing

SHARED_CORE_REGISTRY_STATUS:
  closed_for_current_registry_with_conditions

OTHER_METHODS_DIRECTLY_VALIDATED_BY_ANALYSIS_OR_AUDIT_CORPUS:
  no

OTHER_METHODS_DIRECTLY_VALIDATED_BY_SHARED_CORE_TRANSFER_PILOTS:
  no
```

## Migration rule / 이관 규칙

Historical records keep their original path, protocol version, and verdict. New protocol revisions and evidence classification are additive. Do not rewrite prior `PASS`, `FAIL`, `NO_GAIN`, `BASELINE_PREFERRED`, `NON_CORRESPONDENCE`, or untested-axis status merely to appear current.
