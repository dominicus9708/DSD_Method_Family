# Current Evidence Applicability Matrix / 현재 증거 적용성 행렬

Status: current migration map + five Specification direct pilots + first external Specification application  
Date: 2026-09-06

This file classifies existing method evidence without retroactively turning one method's results into validation of all 22 DSD methods.

## Interpretation key / 해석 키

- **Direct** = the record directly tested the named method.
- **Shared support** = the record supports a reusable method-family discipline, but does not directly validate another method.
- **Conditional transfer** = the shared rule applies only when the receiving method exposes the relevant structure or claim type.
- **Protocol prepared** = a dedicated method protocol exists, but protocol existence alone is not direct validation.
- **Direct pilot** = a method-specific challenge directly tested the method under its own protocol, but maturity is not yet established.
- **External application** = the method is applied under locked criteria to material authored independently of DSD; this origin class does not imply an independent evaluator.

## Analysis corpus / 분석론 기록

`ANL-CH-001` through `ANL-CH-009` remain direct evidence for **DSD Analysis** challenge criteria only. Their shared lessons may support common rules, but do not directly validate another method.

## Audit corpus / 감사 기록

Existing `DSD_Audit/` and new audit records remain direct evidence for **DSD Audit** procedures and verdict discipline only. Shared lessons do not automatically validate Specification, Prediction, Reconstruction, or other methods.

## DSD Specification / DSD 명세론

Protocol:
- `methods/03_specification/PROTOCOL.md` — **DSD Specification Protocol v0.1**.

Internal direct pilots:
- `SPEC-CH-001_well-formed-malformed-discrimination.md`;
- `SPEC-CH-002_contradiction-underspecification.md` with precommit;
- `SPEC-CH-003_optional-layer-bridge-boundary.md` with precommit;
- `SPEC-CH-004_no-gain-specification.md` with precommit;
- `SPEC-CH-005_reproducibility-independent-retrace.md` with precommit and reference-key hash commitment.

External application:
- `evidence/real_world_cases/specification/SPEC-APP-001_RFC9112_message-body-length.md` with separate precommit.

```text
METHOD: DSD Specification
METHOD_STATUS: developing
DEDICATED_PROTOCOL: yes
DIRECT_INTERNAL_PILOTS: five_completed
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

SPEC_APP_001_CASE_ORIGIN: public_normative_standard
SPEC_APP_001_SOURCE: RFC 9112 §6.3 core precedence algorithm
SPEC_APP_001_PRECOMMIT_COMMIT: 9b91cecda9516fd7cd65c9eb181e80ab4fa45deb
SPEC_APP_001_SOURCE_UNIT_COVERAGE: 13/13
SPEC_APP_001_TRIGGER_OR_ACTOR_SCOPE_PRESERVATION: 13/13
SPEC_APP_001_PRECEDENCE_PRESERVATION: 13/13
SPEC_APP_001_BCP14_MUST_OBLIGATIONS_PRESERVED: 8/8
SPEC_APP_001_INVENTED_SOURCE_FACTS: 0
SPEC_APP_001_SOURCE_FIDELITY_RESULT: pass
SPEC_APP_001_FINAL_SPEC_STATUS: no_gain
SPEC_APP_001_COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
SPEC_APP_001_PROTOCOL_PRESSURE: ordered_precedence_priority_present_nonfatal
SPEC_APP_001_INDEPENDENT_EVALUATOR_VALIDATION: not_established

MATURE_DIRECT_METHOD_VALIDATION: not_claimed
NEXT_STEP: specification_maturity_audit
```

`SPEC-APP-001` satisfies the repository checklist's **external or independently generated corpus-origin** requirement because RFC 9112 is an external public normative standard authored independently of DSD. It does not satisfy the separate independent-evaluator requirement.

The external result is intentionally non-favorable to a DSD superiority claim: the RFC baseline was already compact, ordered, and normative, so the precommitted comparative verdict was `SPEC_NO_GAIN` with the baseline preferred for this locked task. This counts as evidence of source fidelity and NO_GAIN preservation, not as evidence of engineering benefit.

## Shared-core registry status / 공통 코어 상태

The current shared-core registry contains **SC-01 through SC-10** and is closed for the present registry with conditions.

```text
SHARED_CORE_RULES_PROMOTED: 10
SPECIALIZATION_RESTRAINT: derived_profile
SHARED_CORE_CLOSURE_RESULT: closed_for_current_registry_with_conditions
DIRECT_METHOD_VALIDATION_FROM_SHARED_CORE: not claimed
```

`REPRODUCIBILITY_RECORD` remains a method/evidence maturity requirement rather than a separate shared semantic-core ID.

## Current overall classification / 현재 총괄 분류

```text
DIRECTLY_MATURE_METHOD_EVIDENCE:
  DSD Analysis
  DSD Audit

DEVELOPING_WITH_DIRECT_AND_EXTERNAL_APPLICATION_EVIDENCE:
  DSD Specification
    direct_internal_pilots: 5
    internal_constructed_sequence: completed
    NO_GAIN_pilot: completed
    procedural_retrace: completed
    external_or_independent_corpus_application: completed
    external_application_result: SPEC_NO_GAIN
    independent_evaluator_validation: not_established
    maturity_audit: pending

SHARED_METHOD_FAMILY_EVIDENCE_AVAILABLE:
  yes

SHARED_CORE_REGISTRY_STATUS:
  closed_for_current_registry_with_conditions

OTHER_METHODS_DIRECTLY_VALIDATED_BY_ANALYSIS_OR_AUDIT_CORPUS:
  no

OTHER_METHODS_DIRECTLY_VALIDATED_BY_SHARED_CORE_TRANSFER_PILOTS:
  no

REAL_WORLD_OR_EXTERNAL_CASE_CORPUS_STATUS:
  first public normative-standard application populated
```

## Migration rule / 이관 규칙

Historical records keep their original path and original verdict. New method-family classification is additive and does not rewrite prior `PASS`, `FAIL`, `NO_GAIN`, `BASELINE_PREFERRED`, or `NON_CORRESPONDENCE` results.
