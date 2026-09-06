# SC-07 — Evidence Scope / Case-Origin Separation / 증거 적용범위·사례 출처 분리 검증

Status: **promoted_with_conditions**  
Date: 2026-09-06  
Evidence scope: `shared_method_family`  
Case origin: `synthetic_constructed_benchmark`

## 1. Result / 결과

`Evidence Scope / Case-Origin Separation` is promoted as a **conditional shared-core rule**.

A representative method from each of the eight higher-level fields was tested against three evidence-metadata perturbations:

- `SI`: scope inflation / direct-target erasure — a record that directly tests one method is allowed to validate sibling methods or the whole family, or its direct target is deleted while the PASS is retained;
- `OC`: origin-class conflation — `EVIDENCE_SCOPE_CLASS` and `CASE_ORIGIN` are collapsed into one classification axis, making combinations such as `method_specific + judicial_case` or `shared_method_family + constructed_benchmark` unrepresentable;
- `OR`: origin-to-validation substitution — changing only the case-origin label is allowed to strengthen or broaden validation without any corresponding change in protocol, criteria, source quality, baseline, external standard, or reproducibility.

```text
SCOPE_INFLATION_OR_TARGET_ERASURE_CHECKS: 8/8 detected
ORIGIN_CLASS_CONFLATION_CHECKS: 8/8 detected
ORIGIN_TO_VALIDATION_SUBSTITUTION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Record **what an evidence item directly tests** independently from **what kind of case produced it**. A real event, judicial case, historical case, personal case, empirical dataset, or organizational incident does not by origin alone broaden the set of methods directly validated; a synthetic or constructed case is not by origin alone incapable of supporting a shared rule. Validation scope changes only when the test target and validation basis change.

SC-07 does not claim that case origin is irrelevant. Origin controls source-verification, privacy, authority, and external-standard obligations; it simply does not replace evidence applicability.

## 2. Source basis / 소스 근거

The current DSD evidence architecture already separates two dimensions.

### Evidence applicability axis

```text
EVIDENCE_SCOPE_CLASS:
  shared_method_family
  method_specific

METHOD_DIRECTLY_TESTED:
SHARED_RULES_SUPPORTED:
METHODS_NOT_DIRECTLY_VALIDATED:
TRANSFER_LIMIT:
```

`shared_method_family` means evidence for a reusable operating discipline. It does not directly validate every receiving method.

`method_specific` means the record directly tests the named method under its own task interface. A result is not inherited by other methods without their own test.

### Case-origin axis

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

The existing evidence rules explicitly state that the third operational lane, real-world application evidence, is not the same logical axis as shared versus method-specific applicability.

Historical Analysis challenges remain direct Analysis evidence. Existing `DSD_Audit/` records remain direct Audit evidence. Their reusable lessons may support shared rules, but do not automatically validate the other DSD methods.

## 3. Locked metadata witnesses / 고정 메타데이터 witness

### Witness M — method-specific constructed case

```text
EVIDENCE_RECORD_ID: M
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: M_target
SHARED_RULES_SUPPORTED: optional
CASE_ORIGIN: constructed_benchmark
RESULT: PASS_or_FAIL_under_locked_protocol
```

This record directly tests only `M_target`, even if its result also supports one or more shared rules.

### Witness R* — counterfactual real-world-origin variant

For schema testing only, hold the test target, protocol, inputs, criteria, result, and quality fields fixed and change only the metadata label:

```text
CASE_ORIGIN: real_event
```

`R*` is **not asserted to be an actual external case**. It is a counterfactual metadata perturbation used to test whether case origin is incorrectly substituted for validation scope.

The direct target remains `M_target` unless the actual protocol and validation basis are broadened.

### Witness S — shared-rule constructed case

```text
EVIDENCE_RECORD_ID: S
EVIDENCE_SCOPE_CLASS: shared_method_family
METHODS_DIRECTLY_TESTED: representative methods used for transfer testing
SHARED_RULES_SUPPORTED: named shared rule
CASE_ORIGIN: constructed_benchmark
DIRECT_VALIDATION_OF_ALL_22_METHODS: no
```

A constructed benchmark can therefore support a shared operating rule without becoming direct validation of every method.

## 4. Perturbations / 교란 연산

### SI — Scope inflation / direct-target erasure

Apply either of the following invalid transformations:

```text
method-specific PASS for M_target
-> validates the entire higher-level field
-> validates all 22 methods
```

or remove `METHOD_DIRECTLY_TESTED` while retaining an unqualified PASS/FAIL that downstream readers can inherit globally.

### OC — Origin-class conflation

Replace the two axes with a single label such as:

```text
real_world_evidence
synthetic_evidence
```

or

```text
shared_real_world
method_specific_synthetic
```

This destroys valid cross-combinations and makes it impossible to state clearly whether a judicial case directly tested Audit, whether a constructed benchmark supported a shared rule, or whether a real-world application was only illustrative.

### OR — Origin-to-validation substitution

Hold protocol, target, criteria, source quality, external standard, baseline, and reproducibility fixed, then change only `CASE_ORIGIN` and allow any of the following to change automatically:

```text
METHOD_DIRECTLY_TESTED
EVIDENCE_SCOPE_CLASS
PASS strength
method-family validity claim
```

Such a change is invalid unless some substantive validation property changes with it.

## 5. Eight-field transfer test / 8개 상위 분야 교차 시험

| Field | Representative method | SI: scope inflation / target erasure | OC: origin conflation | OR: origin-to-validation substitution | Result |
|---|---|---|---|---|---|
| I. Structural Description & Understanding | Interpretation | one Interpretation case is inflated into Analysis/Comparison/Classification validation | a judicial/historical origin label replaces the direct-method field | changing only origin broadens the reading-method validity claim | PASS: 3/3 detected |
| II. Criteria & Validation | Audit | one Audit record is inherited by Specification or all methods | `real_world` is used instead of `method_specific + Audit` | a real-incident label is treated as stronger Audit proof without protocol changes | PASS: 3/3 detected |
| III. Construction & Transformation | Design | one Design test is inflated into Synthesis/Transformation validation | real deployment origin replaces the Design test target | origin alone upgrades an application example into family-wide design validation | PASS: 3/3 detected |
| IV. Evidence & Lineage | Provenance | one Provenance test is inflated into Measurement/Lineage validation | historical-case origin is mistaken for Provenance-method scope | historical origin alone is treated as proof of provenance-method correctness | PASS: 3/3 detected |
| V. Reduction & Representation | Aggregation | one Aggregation benchmark is inflated into Compression validation | empirical-dataset origin replaces direct Aggregation scope | dataset origin alone upgrades aggregate behavior into general method validity | PASS: 3/3 detected |
| VI. Inverse Inference & Reconstruction | Diagnosis | one Diagnosis case is inflated into Reconstruction validation | personal-case origin replaces the direct Diagnosis target | personal/real origin alone upgrades an application result without an external diagnostic standard | PASS: 3/3 detected |
| VII. Computation & Selection | Optimization | one Optimization benchmark is inflated into Computation validation | empirical-dataset origin replaces the Optimization protocol target | dataset origin alone upgrades ranking performance without baseline/reproducibility changes | PASS: 3/3 detected |
| VIII. Dynamics & Action | Control | one Control application is inflated into Simulation/Prediction/Operation validation | organizational-incident origin replaces the direct Control target | real incident origin alone upgrades an intervention record into method-family validity | PASS: 3/3 detected |

The origin labels in this table are schema-level examples, not claims that those external cases have already been collected or verified.

This is a shared-rule transfer test, not direct validation of the selected methods as complete methodologies.

## 6. Negative control / 음성 대조군

SC-07 permits legitimate interaction between the two axes.

1. A real-world judicial case may be `EVIDENCE_SCOPE_CLASS: method_specific`, `METHOD_DIRECTLY_TESTED: DSD Audit`, while also listing shared rules it supports.
2. A constructed benchmark may be `EVIDENCE_SCOPE_CLASS: shared_method_family` and provide strong counterexample support for a common discipline.
3. Case origin may legitimately change **source-handling obligations**: judicial cases need authoritative decision texts, historical cases require source hierarchy, personal cases require privacy/sensitivity handling, and empirical datasets require provenance and data-quality records.
4. Evidence scope may legitimately broaden when the protocol itself is broadened to test additional methods with their own outputs, failure criteria, and validation standards.
5. A real-world case may contribute to direct method validation when protocol, scoring/failure criteria, external standard, relevant baseline, and reproducibility are sufficiently locked. Real-world origin alone is not that basis.

Therefore SC-07 is not “ignore whether a case is real”. It is:

> **Do not use case origin as a substitute for validation scope, and do not use validation scope as a substitute for source/reality status.**

## 7. Standard evidence-classification record / 표준 증거 분류 기록

```text
EVIDENCE_RECORD_ID:
EVIDENCE_SCOPE_CLASS: shared_method_family / method_specific
METHOD_DIRECTLY_TESTED:
METHOD_VERSION_OR_PROTOCOL:
SHARED_RULES_SUPPORTED:
METHODS_NOT_DIRECTLY_VALIDATED:
TRANSFER_LIMIT:

CASE_ORIGIN:
SOURCE_STATUS:
PRIMARY_OR_AUTHORITATIVE_SOURCE:
SECONDARY_SOURCES:
FACT_INTERPRETATION_BOUNDARY:
EXTERNAL_STANDARD:
PRIVACY_OR_SENSITIVITY_HANDLING:

RESULT:
DIRECT_VALIDATION_BASIS:
REPRODUCIBILITY_RECORD:
```

If a record is method-specific and also supports shared rules, keep the primary applicability as method-specific and list the reusable rules separately rather than reclassifying the record as family-wide validation.

## 8. Promotion test / 승격 시험

```text
SOURCE_SUPPORT: pass
SAME_SEMANTIC_MEANING_ACROSS_METHODS: pass
SCOPE_INFLATION_OR_TARGET_ERASURE_COUNTEREXAMPLE: pass
ORIGIN_CLASS_CONFLATION_COUNTEREXAMPLE: pass
ORIGIN_TO_VALIDATION_SUBSTITUTION_COUNTEREXAMPLE: pass
NON_TRANSFER_CASE_IDENTIFIED: pass
METHOD_TASK_REDEFINITION: none
DIRECT_VALIDATION_SEPARATION: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
```

## 9. Transfer conditions / 적용 조건

Apply SC-07 whenever an evidence record is used to support a method, a shared rule, a real-world application, or a maturity/validation claim.

It is especially important when one record simultaneously has a real-world origin and method-specific relevance, or when a method-specific record is cited as support for a reusable shared discipline.

## 10. Non-transfer / minimal-record cases / 적용하지 않거나 단순화하는 경우

A private scratch calculation that is not used as evidence for any method or claim does not need the full evidence-classification schema.

If case origin is genuinely unknown, record it as unresolved/unknown in the local record rather than guessing a real-world category; this does not justify broadening evidence scope.

A source-free synthetic construction may omit real-world source fields, but it must still identify its constructed origin and applicability scope if it is entered into the evidence corpus.

## 11. Evidence limits / 한계

- This is a synthetic cross-field metadata and transfer pilot.
- No new judicial, historical, personal, empirical, or organizational case is claimed to have been externally verified by this record.
- One representative method per higher-level field was tested.
- It does not validate the overall correctness, performance, or usefulness of all 22 methods.
- External real-world cases must still be independently sourced and verified before entering `evidence/real_world_cases/`.

## 12. Relation to SC-01–SC-06 / SC-01~06과의 관계

```text
SC-01 = preserve claim-relevant distinctions
SC-02 = lock source/interface/version semantics
SC-03 = make required bridges explicit
SC-04 = keep claim-relevant dependency layers explicit and restrained
SC-05 = respect information-loss and reconstruction limits
SC-06 = separate identity-preserving evolution, transition, and lineage
SC-07 = separate evidence applicability from case origin/reality status
```

The seven rules are complementary but non-identical.

## 13. Next shared-core candidate / 다음 후보

`SC-08 — Baseline / Failure-NO_GAIN / Anti-Post-Hoc Discipline` should be tested separately.
