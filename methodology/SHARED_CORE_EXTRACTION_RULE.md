# DSD Shared-Core Extraction Rule / DSD 공통 구조 추출 규칙

Status: preparation rule
Date: 2026-09-06

This document governs the next stage of the DSD Method Family: extracting structures that are genuinely reusable across methods **without merging the methods themselves**.

## 1. Core principle / 핵심 원칙

A common element belongs to the shared core only when its meaning and obligation remain stable across multiple receiving methods.

```text
shared operator or rule
!=
identical method
```

Method identity remains determined by task-specific inputs, operations, outputs, failure/no-gain criteria, and validation standards.

## 2. Extraction record / 추출 기록

Every proposed shared element should be recorded with:

```text
SHARED_CORE_ID:
NAME:
SOURCE_METHODS:
SOURCE_RECORDS:
DSD_LAYERS_USED:
INVARIANT_MEANING:
RECEIVING_METHODS:
TRANSFER_CONDITIONS:
NON_TRANSFER_CASES:
METHOD_SPECIFIC_INPUT_REMAINS:
METHOD_SPECIFIC_OPERATION_REMAINS:
METHOD_SPECIFIC_OUTPUT_REMAINS:
METHOD_SPECIFIC_FAILURE_CRITERIA_REMAINS:
METHOD_SPECIFIC_VALIDATION_REMAINS:
EVIDENCE_STATUS:
```

## 3. Initial shared-core candidates / 초기 후보

The following are candidates because they have already appeared across the DSD formal interfaces or Analysis/Audit practice. They are **not yet automatically promoted** merely by appearing in this list.

- status discipline: absence / undefinedness / inapplicability / prerequisite failure / defined zero;
- explicit bridge discipline;
- minimum-layer and optional-interface restraint;
- aggregate/reconstruction restraint;
- support and information-loss recording;
- transition versus regular evolution distinction;
- explicit lineage when identity is not inherited;
- source/version/interface lock;
- evidence-status versus DSD-object-status separation;
- strongest reasonable baseline and `NO_GAIN` preservation where applicable;
- precommit / anti-post-hoc recording discipline;
- explicit preservation of failed, boundary, non-correspondence, and indeterminate outcomes.

## 4. Promotion test / 공통 코어 승격 시험

A candidate becomes shared core only after all applicable questions are answered:

1. Does the rule have the same semantic meaning in at least two independent methods?
2. Does reusing it avoid changing either method's task definition?
3. Can a counterexample show when the rule is inapplicable rather than forcing it universally?
4. Is the rule supported by current DSD source layers or an explicit domain-independent operating requirement?
5. Are direct method validation claims kept separate from shared-rule support?

If these conditions are not met, the rule remains method-specific or conditional.

## 5. Evidence rule / 증거 규칙

Existing Analysis and Audit records can support a shared rule, but they do not directly validate another method.

```text
SOURCE_RECORD -> shared-rule support
shared-rule support -> candidate transfer
candidate transfer != method validation
```

Receiving methods must re-test the shared rule in their own task interfaces.

## 6. Relation to method boundaries / 방법 경계와의 관계

See [`../methods/METHOD_BOUNDARY_MATRIX.md`](../methods/METHOD_BOUNDARY_MATRIX.md).

If shared-core extraction makes two methods appear indistinguishable across all five boundary axes, the pair must be re-opened for a duplication audit. Otherwise shared infrastructure remains shared infrastructure, not a reason to merge methods.

## 7. Planned order / 예정 순서

The next development stage should begin with the most stable cross-method structures before attempting method-specific new protocols:

1. status and typed-domain discipline;
2. source/interface/version locks;
3. bridge declarations;
4. minimum-layer/optional-interface selection;
5. aggregate, information-loss, and reconstruction restraint;
6. transition/lineage discipline;
7. evidence scope and case-origin separation;
8. baseline, failure/no-gain, and anti-post-hoc recording rules.

Each item should be promoted only after its transfer conditions and non-transfer cases are recorded.
