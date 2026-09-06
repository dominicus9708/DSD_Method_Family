# DSD Shared-Core Extraction Rule / DSD 공통 구조 추출 규칙

Status: working promotion rule
Date: 2026-09-06

This document governs the DSD Method Family stage that extracts structures genuinely reusable across methods **without merging the methods themselves**.

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

The following are candidates because they have already appeared across the DSD formal interfaces or Analysis/Audit practice. They are **not automatically promoted** merely by appearing in this list.

- **SC-01 status and typed-domain discipline** — promoted with conditions; see `../evidence/shared/SC-01_status-typed-domain-discipline.md`;
- **SC-02 source / interface / version lock** — promoted with conditions; see `../evidence/shared/SC-02_source-interface-version-lock.md`;
- **SC-03 explicit bridge discipline** — promoted with conditions; see `../evidence/shared/SC-03_explicit-bridge-discipline.md`;
- minimum-layer and optional-interface restraint;
- aggregate/reconstruction restraint;
- support and information-loss recording;
- transition versus regular evolution distinction;
- explicit lineage when identity is not inherited;
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

The development order begins with the most stable cross-method structures before method-specific new protocols:

1. **SC-01 status and typed-domain discipline — completed: promoted_with_conditions**;
2. **SC-02 source / interface / version lock — completed: promoted_with_conditions**;
3. **SC-03 explicit bridge discipline — completed: promoted_with_conditions**;
4. minimum-layer/optional-interface selection;
5. aggregate, information-loss, and reconstruction restraint;
6. transition/lineage discipline;
7. evidence scope and case-origin separation;
8. baseline, failure/no-gain, and anti-post-hoc recording rules.

Each item is promoted only after its transfer conditions and non-transfer cases are recorded.

## 8. Promotion registry / 승격 기록

### SC-01 — Status and Typed-Domain Discipline

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
STATUS_COLLAPSE_CHECKS: 8/8 detected
TYPED_DOMAIN_PROJECTION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Do not silently collapse claim-relevant status or complete typed-domain distinctions merely because they can be mapped to the same numerical or reduced representation.

Transfer conditions:

- the selected interface actually distinguishes the relevant status or typed coordinates;
- the claimed result depends, or may depend, on those distinctions;
- an intentional quotient/coarsening uses an explicit map and records its loss boundary.

Non-transfer case:

- a method does not use the relevant status-bearing interface; or
- an explicit quotient is part of the declared task, the claim is restricted to the quotient, and no recovery of discarded distinctions is asserted.

Evidence record: [`../evidence/shared/SC-01_status-typed-domain-discipline.md`](../evidence/shared/SC-01_status-typed-domain-discipline.md).

### SC-02 — Source / Interface / Version Lock

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
SOURCE_SUBSTITUTION_CHECKS: 8/8 detected
SEMANTIC_VERSION_DRIFT_CHECKS: 8/8 detected
INTERFACE_OMISSION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Lock every source, interface branch, and revision whose semantics can affect the claimed result. If exact revisions are replaced by a range or equivalence class, equivalence over the actually used interface must be established explicitly.

Transfer conditions:

- source-defined semantics, optional interfaces, or revisions can affect the method result;
- reproducibility, auditability, comparison, or historical traceability is claimed;
- downstream work inherits upstream definitions whose revision can change the interpretation.

Non-transfer/minimal-lock cases:

- unused downstream layers are explicitly recorded as `not used` and do not need to become dependencies;
- an exact revision may be replaced by a documented equivalence class only after equivalence on the used interface is shown.

Evidence record: [`../evidence/shared/SC-02_source-interface-version-lock.md`](../evidence/shared/SC-02_source-interface-version-lock.md).

### SC-03 — Explicit Bridge Discipline

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
BRIDGE_OMISSION_CHECKS: 8/8 detected
NAME_OR_COORDINATE_INFERENCE_CHECKS: 8/8 detected
BRIDGE_SUBSTITUTION_SENSITIVITY_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Do not infer a claim-relevant cross-layer, cross-representation, cross-carrier, or cross-domain correspondence from labels, raw values, or coordinate occurrence alone. Supply the map/relation and its assumptions explicitly unless the locked interface already does so or invariance across the admissible bridge class has been established.

Transfer conditions:

- the claim connects distinct DSD layers, representations, typed carriers, external domains, or method outputs;
- alternative admissible mappings could change ownership, support, coefficient, classification, ranking, diagnosis, or intervention;
- external-domain meaning is being supported from DSD structure.

Non-transfer/minimal-bridge cases:

- the operation remains inside the same typed carrier and uses a declared identity map;
- the locked interface already supplies the required structure-preserving map and the claim remains inside its stated preservation range;
- a separate invariance theorem proves the same result for every admissible bridge in the declared class.

Evidence record: [`../evidence/shared/SC-03_explicit-bridge-discipline.md`](../evidence/shared/SC-03_explicit-bridge-discipline.md).

Relations among the first three promoted rules:

```text
SC-01 = preserve claim-relevant distinctions
SC-02 = lock the semantics that determine which rules/interfaces are active
SC-03 = explicitly supply claim-relevant mappings between active structures
```
