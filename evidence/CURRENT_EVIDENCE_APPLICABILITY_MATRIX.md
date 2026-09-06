# Current Evidence Applicability Matrix / 현재 증거 적용성 행렬

Status: current migration map + first post-closure method-protocol preparation
Date: 2026-09-06

This file classifies existing Analysis challenge evidence without retroactively turning it into validation of all 22 DSD methods.

## Interpretation key / 해석 키

- **Direct** = the record directly tested the named method.
- **Shared support** = the record supports a reusable method-family discipline, but does not directly validate another method.
- **Conditional transfer** = the shared rule applies only when the receiving method exposes the relevant structure or claim type.
- **Protocol prepared** = a dedicated method protocol exists, but direct method evidence has not yet been accumulated.

## ANL-CH-001 through ANL-CH-009

| Record | Direct method evidence | Shared method-family support | Transfer limit |
|---|---|---|---|
| ANL-CH-001 Blind + Twin | Analysis | relabeling invariance, discrimination, status discipline | other methods must re-test these under their own task outputs |
| ANL-CH-002 Symmetric Case | Analysis | invariance/equivariance separation, symmetry discipline | conditional on an explicitly declared symmetry action |
| ANL-CH-003 DSD Null / No-Gain | Analysis | baseline sufficiency, `NO_GAIN` preservation | does not establish usefulness or no-gain for another method |
| ANL-CH-004 Forced Non-Correspondence | Analysis | essential-structure preservation, encoding is not direct correspondence | receiving method must define its own target-preservation criterion |
| ANL-CH-005 Layer Restraint | Analysis | minimum-layer selection, optional-interface restraint | does not identify the minimum layers for a different method automatically |
| ANL-CH-006 Specialization Removal | Analysis | specialization-dependent/core partition, unavailable is not false/zero | reusable portion is now classified as the derived specialization profile over SC-01/03/04 |
| ANL-CH-007 Competing Explanation | Analysis | strongest reasonable baseline, anti-strawman discipline | each method requires a task-matched competent baseline |
| ANL-CH-008 Unseen-Problem Transfer | Analysis | rule-lock transfer, post-reveal drift prohibition, holdout-level honesty | same-session pseudo-unseen result is not independent transfer validation |
| ANL-CH-009 Reverse Prediction | Analysis | prediction-only precommit, no post-reveal rescue, miss preservation | does not directly validate the independent DSD Prediction method |

## Audit corpus / 감사 기록

Existing `DSD_Audit/` and new audit records remain **direct evidence for DSD Audit**.
They may also support shared disciplines such as source lock, interface lock, evidence-status separation, bridge checks, alternative/witness preservation, contradiction checks, and maximum-supported-claim discipline.

Those shared lessons do not automatically validate Analysis, Specification, Prediction, Reconstruction, or other methods.

## DSD Specification / DSD 명세론

A dedicated method protocol now exists at:

- `methods/03_specification/PROTOCOL.md` — **DSD Specification Protocol v0.1**;
- `evidence/method_specific/specification/` — dedicated direct-evidence lane.

Current classification:

```text
METHOD: DSD Specification
METHOD_STATUS: developing
DEDICATED_PROTOCOL: yes
DIRECT_METHOD_CHALLENGE_CORPUS: not_yet_accumulated
DIRECT_METHOD_VALIDATION: not_claimed
NEXT_DIRECT_RECORD: SPEC-CH-001
```

Protocol preparation is a maturity step, not a PASS result. Specification remains outside `DIRECTLY_MATURE_METHOD_EVIDENCE` until method-specific challenge and application evidence accumulate.

## Shared-core registry status / 공통 코어 상태

The current shared-core registry contains **SC-01 through SC-10** and is closed for the present registry with conditions.

```text
SHARED_CORE_RULES_PROMOTED: 10
SPECIALIZATION_RESTRAINT: derived_profile
SHARED_CORE_CLOSURE_RESULT: closed_for_current_registry_with_conditions
DIRECT_METHOD_VALIDATION_FROM_SHARED_CORE: not claimed
```

The closure audit found one additional framework-level semantic gap after SC-01 through SC-09: external-domain validation standards were not yet independently protected from DSD-internal success. This gap was tested across all eight higher-level fields and promoted as **SC-10 External-Standard / Domain-Validation Separation**.

`REPRODUCIBILITY_RECORD` remains a method/evidence maturity requirement rather than a new shared semantic-core ID in the current closure version.

## Current overall classification / 현재 총괄 분류

```text
DIRECTLY_MATURE_METHOD_EVIDENCE:
  DSD Analysis
  DSD Audit

DEVELOPING_WITH_DEDICATED_PROTOCOL_BUT_NOT_DIRECTLY_VALIDATED:
  DSD Specification

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

Historical records keep their original path and original verdict.
New method-family classification is additive:

```text
original historical record
+ EVIDENCE_SCOPE_CLASS
+ METHOD_DIRECTLY_TESTED
+ SHARED_RULES_SUPPORTED
+ CASE_ORIGIN when applicable
-> current applicability record
```

No historical `PASS`, `FAIL`, `NO_GAIN`, or `NON_CORRESPONDENCE` result is rewritten merely to fit the method-family taxonomy.
