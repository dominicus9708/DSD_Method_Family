# DSD Evidence Applicability / DSD 증거 적용성 분류

This directory separates **what an evidence record directly validates** from **what kind of case produced the record**.

이 디렉터리는 DSD 방법군의 검증 증거를 다음 세 기록군으로 분리합니다.

1. **Shared method-family evidence / 방법군 공통 규율 증거**
2. **Method-specific evidence / 개별 방법 직접 증거**
3. **Real-world application evidence / 외부 실제사례 적용 증거**

The third category is intentionally not treated as the same logical axis as the first two. A real-world case may directly test one method while also supporting one or more shared rules.

## Core rule / 핵심 규칙

A record must never move from

```text
works in DSD Analysis
```

to

```text
validates all DSD methods
```

without a method-specific test.

Likewise, a real event, judicial case, historical case, personal case, or empirical dataset is not automatically validation of the whole method family merely because DSD can be applied to it.

The separation between evidence applicability and case origin has been cross-field tested as shared-core rule **SC-07**. See [`shared/SC-07_evidence-scope-case-origin-separation.md`](shared/SC-07_evidence-scope-case-origin-separation.md).

Evaluation integrity across baseline choice, unfavorable/null outcome preservation, and post-reveal criterion changes has also been cross-field tested as **SC-08**. See [`shared/SC-08_baseline-failure-no-gain-anti-post-hoc-discipline.md`](shared/SC-08_baseline-failure-no-gain-anti-post-hoc-discipline.md). The baseline clause is conditional on a comparative/gain/performance claim; purely descriptive tasks do not require a competitor merely to be valid.

The separation between **evidence/audit status** and **DSD object/model status** has been cross-field tested as **SC-09**. See [`shared/SC-09_evidence-status-object-status-separation.md`](shared/SC-09_evidence-status-object-status-separation.md). An object may be `applicable_but_undefined` while that status is fully confirmed by the available evidence, or may be `defined_zero` while evidence for applying the formal model to an external target remains insufficient.

The separation between **DSD-internal success** and the **receiving domain's validation standard** has been cross-field tested as **SC-10**. See [`shared/SC-10_external-standard-domain-validation-separation.md`](shared/SC-10_external-standard-domain-validation-separation.md). An explicit domain bridge does not by itself replace mathematical proof, empirical validation, professional/interpretive authority, legal standards, or other task-relevant external validation requirements.

The current shared-core extraction stage has been closed for the present registry with conditions. See [`shared/SHARED_CORE_CLOSURE_AUDIT.md`](shared/SHARED_CORE_CLOSURE_AUDIT.md). This closure covers shared-rule extraction only; it is not direct validation of all 22 methods.

## Required scope fields / 적용 범위 필드

```text
EVIDENCE_SCOPE_CLASS:
  shared_method_family
  method_specific

METHOD_DIRECTLY_TESTED:
SHARED_RULES_SUPPORTED:
METHODS_NOT_DIRECTLY_VALIDATED:
TRANSFER_LIMIT:
```

Case origin is recorded separately:

```text
CASE_ORIGIN:
  synthetic_toy
  constructed_benchmark
  real_event
  judicial_case
  historical_case
  personal_case
  empirical_dataset
  organizational_or_technical_incident
```

`CASE_ORIGIN` may change source-verification, authority, privacy, provenance, or external-standard obligations. It does **not** by itself change `METHOD_DIRECTLY_TESTED` or expand a record from method-specific evidence to whole-family validation.

When a record contains both a DSD object/model status and an evidence/audit judgment, preserve them separately:

```text
DSD_OBJECT_STATUS:
DSD_OBJECT_STATUS_BASIS:
EVIDENCE_STATUS:
EVIDENCE_BASIS:
CLAIM_ABOUT_OBJECT_STATUS:
CLAIM_STATUS_RELATION:
```

`unknown`, `insufficient`, or `out of scope` on the evidence side must not be silently converted into `undefined`, `inapplicable`, `absent`, or `zero` on the object side, and the reverse conversion is likewise invalid without an explicit rule.

When a DSD result is used for an external-domain claim, preserve the domain-validation boundary:

```text
DSD_METHOD_OUTPUT:
DOMAIN_CLAIM:
DOMAIN_BRIDGE:
EXTERNAL_DOMAIN:
EXTERNAL_STANDARD:
DSD_INTERNAL_VALIDATION_RESULT:
DOMAIN_VALIDATION_RESULT:
```

For confirmatory/comparative evidence that activates SC-08, additionally preserve the strongest reasonable baseline when applicable, locked pass/failure/no-gain criteria, unfavorable/null outcomes, precommit status, and any post-reveal revisions as new versions rather than silent rewrites.

`REPRODUCIBILITY_RECORD` remains a method/evidence maturity requirement. The current closure audit does not promote one universal reproducibility semantics because concrete rerun/retrace obligations differ by method.

## Directory map / 폴더 구조

```text
evidence/
├─ README.md
├─ CURRENT_EVIDENCE_APPLICABILITY_MATRIX.md
├─ shared/
│  ├─ README.md
│  ├─ SC-01_...md through SC-10_...md
│  ├─ SPECIALIZATION_RESTRAINT_DUPLICATION_AUDIT.md
│  └─ SHARED_CORE_CLOSURE_AUDIT.md
├─ method_specific/
│  └─ README.md
└─ real_world_cases/
   └─ README.md
```

Historical Analysis and Audit records remain in their established paths. This directory cross-references them; it does not retroactively rename, move, or rewrite their verdicts.
