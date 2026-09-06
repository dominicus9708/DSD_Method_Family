# Current Evidence Applicability Matrix / 현재 증거 적용성 행렬

Status: current migration map + four post-closure Specification direct pilots
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
- `SPEC-CH-004_no-gain-specification.md` with precommit.

```text
METHOD: DSD Specification
METHOD_STATUS: developing
DEDICATED_PROTOCOL: yes
DIRECT_METHOD_EVIDENCE: four_pilots_completed

SPEC_CH_001_WELL_FORMED_ACCEPTED: 2/2
SPEC_CH_001_MALFORMED_DETECTED: 6/6
SPEC_CH_001_EXACT_DIAGNOSTIC_MATCHES: 8/8
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

MATURE_DIRECT_METHOD_VALIDATION: not_claimed
NEXT_DIRECT_RECORD: SPEC-CH-005
```

`SPEC-CH-004` is method-specific evidence because it tests Specification's own `SPEC_NO_GAIN` output and its boundary against usable-with-gain and `SPEC_UNDERSPECIFIED`. It uses a competent already-complete non-DSD structured specification as the strongest constructed baseline and does not claim DSD advantage when the operational content is equivalent.

All four records remain constructed pilots. They do not move Specification into mature direct method evidence.

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

DEVELOPING_WITH_DIRECT_PILOT_EVIDENCE:
  DSD Specification
    direct_pilot_records: 4
    NO_GAIN_pilot: completed
    independent_retrace: not_yet_completed

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