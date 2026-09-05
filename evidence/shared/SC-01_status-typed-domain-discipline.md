# SC-01 — Status and Typed-Domain Discipline / 상태·타입 도메인 규율 검증

Status: **promoted_with_conditions**
Date: 2026-09-06
Evidence scope: `shared_method_family`
Case origin: `synthetic_constructed_benchmark`

## 1. Result / 결과

The status / typed-domain discipline is promoted as a **conditional shared core rule**.
A representative method from each of the eight higher-level fields was tested against two deliberately non-faithful perturbations:

- `Z`: zero-totalization that replaces undefined/inapplicable/prerequisite-unsatisfied/absent states with numerical zero;
- `P`: typed-input projection that maps `(a,b_i) -> a` and discards the second typed coordinate.

```text
STATUS_COLLAPSE_CHECKS: 8/8 detected
TYPED_DOMAIN_PROJECTION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

The invariant meaning is:

> Numerical coincidence does not imply equality of assignment-domain status, applicability, membership, or complete typed input. When a selected DSD interface and claimed result depend on those distinctions, they must be preserved or any intentional coarsening must be declared explicitly.

## 2. Source basis / 소스 근거

### Formation Axiom System

The Formation system distinguishes undefined assignment, defined zero, defined nonzero negligible value, channel absence, and an admitted channel with zero component term.
Relevant results include:

- Proposition 5.4: zero-padding is not assignment-faithful;
- Proposition 5.9: a defined zero assignment may support a channel;
- Proposition 5.12: an absent channel is not a zero term;
- Proposition 5.13: zero-extension of the term map is not channel-faithful.

### Property Axiom System

Definition 3.3 distinguishes:

```text
undeclared
profile unavailable
inapplicable
prerequisite unsatisfied
applicable but undefined
defined zero
defined nonzero/value
```

Definition 3.4 retains the property kind, the **complete ordered typed input**, and the assigned value in each defined property record.

### Channel-Indexed Static Aggregation

Section 2.4 preserves Formation/Property status distinctions downstream. Undefined property states remain outside the defined-data carrier rather than being replaced by zero. If negative-status information is required by a downstream claim, the complete descriptor or an explicit status sidecar must be retained.

### Structural Reorganization Dynamics

Section 2.6 permits a coarser dynamic status partition only through an explicit status map. Zero padding must retain sufficient side information whenever undefinedness versus defined zero remains relevant. Section 5.4 separates status/domain transitions from ordinary defined-value evolution.

## 3. Locked synthetic case / 고정 형식 사례

Fix a valid Property model with a zero-bearing property kind `q` and typed profile `S x T`.
Let `a in S` and `b0,b1,b2,b3 in T`.

```text
x0 = (a,b0): applicable, prerequisite-satisfied, Xi_q(x0)=0
     -> defined_zero

xU = (a,b1): applicable, prerequisite-satisfied, xU not in Dom(Xi_q)
     -> applicable_but_undefined

xP = (a,b2): applicable, prerequisite-unsatisfied
     -> prerequisite_unsatisfied

xI = (a,b3): inapplicable
     -> inapplicable

qU: undeclared
qP: declared, profile unavailable
```

At Formation level also include:

```text
c_zero in C_L, T_L(c_zero)=0
c_abs  not in C_L
```

## 4. Perturbations / 붕괴 연산

### Z — zero-totalization

Replace non-defined or absent states by numerical `0`, thereby colliding them with defined zero.
This is intentionally non-faithful.

### P — typed-input projection

Map `(a,b_i) -> a` and discard the second typed coordinate.
When `q` depends on the full ordered profile, this is intentionally non-faithful.

## 5. Eight-field transfer test / 8개 상위 분야 교차 시험

| Field | Representative method | Status-collapse consequence | Typed-domain consequence | Result |
|---|---|---|---|---|
| I. Structural Description & Understanding | Analysis | structural decomposition loses defined-zero vs undefined/absence | full typed input distinction is lost | PASS: loss detected |
| II. Criteria & Validation | Audit | a claim of defined zero cannot be retraced against undefined status | audited property record loses part of its application input | PASS: loss detected |
| III. Construction & Transformation | Transformation | distinct source states collapse to one target zero, breaking faithfulness | source tuple coordinate is lost | PASS: loss detected |
| IV. Evidence & Lineage | Measurement | defined zero observation is conflated with absence of a defined observation | measurement datum loses part of its typed target | PASS: loss detected |
| V. Reduction & Representation | Compression | required downstream distinction becomes a destructive collision | required typed distinction is removed | PASS: loss detected |
| VI. Inverse Inference & Reconstruction | Diagnosis | zero evidence and undefined/no-value evidence constrain different compatible-state sets but become conflated | candidate distinctions keyed by the second coordinate disappear | PASS: loss detected |
| VII. Computation & Selection | Computation | defined zero is evaluable while undefined requires an assignment-domain branch | typed dependency may be omitted incorrectly | PASS: loss detected |
| VIII. Dynamics & Action | Simulation | defined-zero -> nonzero value evolution is conflated with undefined -> defined status transition | time-indexed component identity is coarsened | PASS: loss detected |

The test is a shared-rule transfer test, not a direct validation of the selected methods as complete methodologies.

## 6. Negative control / 음성 대조군

SC-01 does **not** prohibit every coarsening.
An explicit quotient or status map is permitted when all of the following hold:

1. the quotient/status map or projection is declared before the result is interpreted;
2. the final claim is restricted to distinctions preserved by that quotient;
3. no stronger reconstruction, provenance, lineage, compliance, or status claim is made from the lost information;
4. information loss or required sidecar data are recorded.

The explicit dynamic `pi_stat` pattern is an example of this kind of admissible coarsening.

Therefore the shared rule is not "never merge statuses". It is:

> **Do not silently collapse claim-relevant status or typed-domain distinctions.**

## 7. Promotion test / 승격 시험

```text
SOURCE_SUPPORT: pass
SAME_SEMANTIC_MEANING_ACROSS_METHODS: pass
METHOD_TASK_REDEFINITION: none
COLLAPSE_COUNTEREXAMPLE: pass
NON_TRANSFER_CASE_IDENTIFIED: pass
DIRECT_VALIDATION_SEPARATION: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
```

## 8. Transfer conditions / 적용 조건

Apply SC-01 when:

- the selected Formation/Property/downstream interface distinguishes the relevant statuses or typed coordinates;
- the claimed result depends, or may depend, on those distinctions;
- any coarsening is accompanied by an explicit map and declared information loss.

Do not force SC-01 when:

- the method does not use the relevant status-bearing interface at all; or
- an explicit quotient is part of the task definition, the claim is restricted to the quotient, and no recovery of discarded distinctions is asserted.

## 9. Evidence limits / 한계

- This is a synthetic cross-field transfer pilot.
- One representative method per higher-level field was tested.
- It does not validate the overall correctness, performance, or usefulness of all 22 methods.
- No real event, judicial case, historical case, personal case, or empirical dataset is included here.
- Receiving methods still require their own method-specific protocols and external/domain tests.

## 10. Next shared-core candidate / 다음 후보

`SC-02 — Source / Interface / Version Lock` should be tested separately.
