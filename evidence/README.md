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

These shared-core pilots support the reusable rules themselves. They do not directly validate all 22 methods.

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

For confirmatory/comparative evidence that activates SC-08, additionally preserve the strongest reasonable baseline when applicable, locked pass/failure/no-gain criteria, unfavorable/null outcomes, precommit status, and any post-reveal revisions as new versions rather than silent rewrites.

## Directory map / 폴더 구조

```text
evidence/
├─ README.md
├─ CURRENT_EVIDENCE_APPLICABILITY_MATRIX.md
├─ shared/
│  ├─ README.md
│  ├─ SC-07_evidence-scope-case-origin-separation.md
│  └─ SC-08_baseline-failure-no-gain-anti-post-hoc-discipline.md
├─ method_specific/
│  └─ README.md
└─ real_world_cases/
   └─ README.md
```

Historical Analysis and Audit records remain in their established paths. This directory cross-references them; it does not retroactively rename, move, or rewrite their verdicts.
