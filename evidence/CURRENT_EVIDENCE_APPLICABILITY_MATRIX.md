# Current Evidence Applicability Matrix / 현재 증거 적용성 행렬

Status: current migration map + five post-closure Specification direct pilots  
Date: 2026-09-06

This file classifies existing method evidence without retroactively turning one method's results into validation of all 22 DSD methods.

## Interpretation key / 해석 키

- **Direct** = the record directly tested the named method.
- **Shared support** = the record supports a reusable method-family discipline, but does not directly validate another method.
- **Conditional transfer** = the shared rule applies only when the receiving method exposes the relevant structure or claim type.
- **Protocol prepared** = a dedicated method protocol exists, but protocol existence alone is not direct validation.
- **Direct pilot** = a method-specific challenge directly tested the method under its own protocol, but maturity is not yet established.

## Analysis corpus / 분석론 기록

`ANL-CH-001` through `ANL-CH-009` remain direct evidence for **DSD Analysis** challenge criteria only. Their shared lessons may support common rules, but do not directly validate another method.

## Audit corpus / 감사 기록

Existing `DSD_Audit/` and new audit records remain direct evidence for **DSD Audit** procedures and verdict discipline only. Shared lessons do not automatically validate Specification, Prediction, Reconstruction, or other methods.

## DSD Specification / DSD 명세론

A dedicated method protocol exists at:

- `methods/03_specification/PROTOCOL.md` — **DSD Specification Protocol v0.1**;
- `evidence/method_specific/specification/` — dedicated direct-evidence lane.

Direct pilots:

- `SPEC-CH-001_well-formed-malformed-discrimination.md`;
- `SPEC-CH-002_contradiction-underspecification.md` with precommit;
- `SPEC-CH-003_optional-layer-bridge-boundary.md` with precommit;
- `SPEC-CH-004_no-gain-specification.md` with precommit;
- `SPEC-CH-005_reproducibility-independent-retrace.md` with precommit and reference-key hash commitment.

```text
METHOD: DSD Specification
METHOD_STATUS: developing
DEDICATED_PROTOCOL: yes
DIRECT_METHOD_EVIDENCE: five_pilots_completed
INTERNAL_CONSTRUCTED_CHALLENGE_SEQUENCE: completed

SPEC_CH_001_RESULT: SPECIFICATION_DISCRIMINATION_PILOT_PASS_WITH_LIMITATIONS

SPEC_CH_002_PRECOMMIT_COMMIT: 848a01b160ecfe4fcbdb8e69d6501e40555d782d
SPEC_CH_002_CONTRADICTIONS_CORRECT: 3/3
SPEC_CH_002_UNDERSPECIFICATIONS_CORRECT: 3/3
SPEC_CH_002_EXACT_DIAGNOSTIC_MATCHES: 8/8
SPEC_CH_002_CROSS_CLASS_ERRORS: 0
SPEC_CH_002_RESULT: SPECIFICATION_CONTRADICTION_UNDERSPECIFICATION_PILOT_PASS_WITH_LIMITATIONS

SPEC_CH_003_PRECOMMIT_COMMIT: d2cc07121043546be8e2450d8af288491b837e76
SPEC_CH_003_OPTIONAL_OVERCONSTRAINTS_CORRECT: 3/3
SPEC_CH_003_REQUIRED_BRIDGE_FAILURES_CORRECT: 3/3
SPEC_CH_003_EXACT_DIAGNOSTIC_MATCHES: 8/8
SPEC_CH_003_CROSS_CLASS_ERRORS: 0
SPEC_CH_003_RESULT: SPECIFICATION_OPTIONAL_LAYER_BRIDGE_BOUNDARY_PILOT_PASS_WITH_LIMITATIONS

SPEC_CH_004_PRECOMMIT_COMMIT: 4d55d00af7fa376d370415a48b82de6883ba6fc8
SPEC_CH_004_NO_GAIN_CASES_CORRECT: 3/3
SPEC_CH_004_OPERATIONAL_GAIN_CASES_CORRECT: 3/3
SPEC_CH_004_UNDERSPECIFIED_CASES_CORRECT: 2/2
SPEC_CH_004_EXACT_STATUS_FAMILY_MATCHES: 8/8
SPEC_CH_004_FALSE_NO_GAIN_ON_INCOMPLETE_SOURCE: 0
SPEC_CH_004_FALSE_COSMETIC_GAIN: 0
SPEC_CH_004_INVENTED_SOURCE_FACTS: 0
SPEC_CH_004_RESULT: SPECIFICATION_NO_GAIN_PILOT_PASS_WITH_LIMITATIONS

SPEC_CH_005_PRECOMMIT_COMMIT: dda33b2028c9e5fb0f7b3bef938a8b834219f787
SPEC_CH_005_REFERENCE_KEY_HASH_MATCH: yes
SPEC_CH_005_TRACE_A_FINAL_STATUS_MATCHES: 8/8
SPEC_CH_005_TRACE_B_FINAL_STATUS_MATCHES: 8/8
SPEC_CH_005_TRACE_A_B_FINAL_STATUS_AGREEMENT: 8/8
SPEC_CH_005_TRACE_A_B_DIAGNOSTIC_AGREEMENT: 8/8
SPEC_CH_005_TRACE_A_B_ATOMIZATION_BOUNDARY_MATCHES: 32/32
SPEC_CH_005_SOURCE_FACT_INVENTION: 0
SPEC_CH_005_ORDER_SENSITIVITY_ERRORS: 0
SPEC_CH_005_RESULT: SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_PASS_WITH_LIMITATIONS
SPEC_CH_005_INDEPENDENT_EVALUATOR_VALIDATION: not_established

MATURE_DIRECT_METHOD_VALIDATION: not_claimed
NEXT_REQUIRED_EVIDENCE: external_or_independently_generated_application_case
```

The fifth record directly tests Specification's own reproducibility/retrace requirement on a frozen constructed packet and two processing orders. It supports procedural retraceability, not independent reviewer validation.

All five records remain constructed pilots. They do not move Specification into mature direct method evidence.

## Shared-core registry status / 공통 코어 상태

The current shared-core registry contains **SC-01 through SC-10** and is closed for the present registry with conditions.

```text
SHARED_CORE_RULES_PROMOTED: 10
SPECIALIZATION_RESTRAINT: derived_profile
SHARED_CORE_CLOSURE_RESULT: closed_for_current_registry_with_conditions
DIRECT_METHOD_VALIDATION_FROM_SHARED_CORE: not claimed
```

`REPRODUCIBILITY_RECORD` remains a method/evidence maturity requirement rather than a separate shared semantic-core ID. `SPEC-CH-005` is therefore a method-specific implementation test of that requirement, not a new shared-core promotion.

## Current overall classification / 현재 총괄 분류

```text
DIRECTLY_MATURE_METHOD_EVIDENCE:
  DSD Analysis
  DSD Audit

DEVELOPING_WITH_DIRECT_PILOT_EVIDENCE:
  DSD Specification
    direct_pilot_records: 5
    internal_constructed_sequence: completed
    NO_GAIN_pilot: completed
    procedural_retrace: completed
    independent_evaluator_validation: not_established
    external_or_independent_application_case: still_required

SHARED_METHOD_FAMILY_EVIDENCE_AVAILABLE:
  yes

SHARED_CORE_REGISTRY_STATUS:
  closed_for_current_registry_with_conditions

OTHER_METHODS_DIRECTLY_VALIDATED_BY_ANALYSIS_OR_AUDIT_CORPUS:
  no

OTHER_METHODS_DIRECTLY_VALIDATED_BY_SHARED_CORE_TRANSFER_PILOTS:
  no

REAL_WORLD_CASE_CORPUS_STATUS:
  separate registry prepared; must be populated and verified independently
```

## Migration rule / 이관 규칙

Historical records keep their original path and original verdict. New method-family classification is additive and does not rewrite prior `PASS`, `FAIL`, `NO_GAIN`, or `NON_CORRESPONDENCE` results.