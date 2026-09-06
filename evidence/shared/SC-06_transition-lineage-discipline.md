# SC-06 — Transition / Lineage Discipline / 전이·계보 규율 검증

Status: **promoted_with_conditions**  
Date: 2026-09-06  
Evidence scope: `shared_method_family`  
Case origin: `synthetic_constructed_benchmark`

## 1. Result / 결과

`Transition / Lineage Discipline` is promoted as a **conditional shared-core rule**.
A representative method from each of the eight higher-level fields was tested against three temporal-identity perturbations:

- `TR`: transition-as-regular-evolution — conceal an identity-breaking change inside one regular trajectory;
- `LO`: lineage omission/invention — preserve a successor/history claim after removing required lineage, or invent lineage from names, coordinates, or aggregate similarity;
- `LC`: lineage coherence/type violation — accept lineage with invalid source/target typing, non-identity self-time relation, incoherent composition, or component identity inferred from channel lineage alone.

```text
TRANSITION_AS_REGULAR_EVOLUTION_CHECKS: 8/8 detected
LINEAGE_OMISSION_OR_INVENTION_CHECKS: 8/8 detected
LINEAGE_COHERENCE_OR_TYPE_VIOLATION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Keep ordinary downstream evolution inside a regular epoch only while the inherited Stage-VI formation identity and declared support typing remain valid. When literal identity is broken, record a transition and supply typed lineage for any successor/history claim. Do not infer succession from labels, values, aggregate equality, or apparent continuity alone.

## 2. Source basis / 소스 근거

### Formation Axiom System

An admitted operational channel has identity

```text
c = (p, a, lambda, v, rho)
```

and the assigned value `v` is part of channel identity. Restriction/realization histories are not channel coordinates.

### Structural Reorganization Dynamics

A regular epoch keeps the inherited Stage-VI formation background and regular support signature fixed. A change of a channel-identity coordinate, channel admission/loss, or formation assignment is a channel/formation-level transition and is not written as value evolution of one fixed channel.

Across a formation transition, succession is additional data. A channel-lineage relation is

```text
Lambda_{s,t} subset C(s) x C(t)
```

and `(c_s,c_t) in Lambda_{s,t}` declares succession, not Stage-VI tuple equality.

A coherent lineage family requires self-time identity and cross-time coherence:

```text
Lambda_{t,t} = Delta_{C(t)}
Lambda_{s,t} o Lambda_{r,s} subset Lambda_{r,t}
```

Branching and merging are allowed unless a stronger application-specific uniqueness condition is declared. On a fixed formation background, canonical identity lineage is available.

Component-level identity is separate from channel lineage when downstream component structure is involved. Aggregate equality or inequality is not a lineage criterion.

## 3. Locked microcase / 고정 microcase

### Transition-required case

```text
t0:
  c0 = (p,a,lambda,3,rho)

t1:
  c1 = (p,a,lambda,4,rho)

c0 != c1
EVENT_CLASS = formation_transition
(c0,c1) in Lambda_0,1
```

The change in `v` changes Stage-VI channel identity.

### Regular-evolution negative control

```text
same inherited channel c
T_c(t0) = 2
T_c(t1) = 5
formation background unchanged
support signature unchanged
EVENT_CLASS = analytic_value_evolution
canonical lineage = identity on c
```

The second case is regular downstream evolution and does not require a new formation transition.

## 4. Perturbations / 교란 연산

### TR — Transition-as-regular-evolution

Replace the transition-required case by an in-place notation such as

```text
c(t) = (..., v(t), ...)
```

while retaining one unchanged inherited channel identity and one regular epoch.

### LO — Lineage omission or invention

Keep a successor/continuity/history claim after removing required `Lambda_{s,t}` or component lineage, or infer the edge from same name, same aggregate, nearby coordinates, or narrative continuity alone.

### LC — Lineage coherence or type violation

Accept any of the following:

- a relation whose source/target carriers do not match the pre/post channel sets;
- `Lambda_{t,t}` not equal to self-time identity;
- short-interval lineage whose composition is not contained in the declared long-interval lineage;
- component identity inferred from channel lineage without the required component relation/profile.

## 5. Eight-field transfer test / 8개 상위 분야 교차 시험

| Field | Representative method | TR | LO | LC | Result |
|---|---|---|---|---|---|
| I. Structural Description & Understanding | Classification | formation transition misclassified as ordinary evolution | successor continuity classified without lineage evidence | incoherent lineage accepted as one coherent history class | PASS: 3/3 detected |
| II. Criteria & Validation | Specification | identity-changing update allowed by a regular-state schema | successor field has no declared basis | schema omits typing/self-time/coherence requirements | PASS: 3/3 detected |
| III. Construction & Transformation | Transformation | distinct pre/post objects treated as in-place mutation | continuity claimed with no successor map | incoherent lineage used as a transformation chain | PASS: 3/3 detected |
| IV. Evidence & Lineage | Lineage | literal equality confused with succession | edge invented from name/aggregate similarity | coherence or typing violation not rejected | PASS: 3/3 detected |
| V. Reduction & Representation | Compression | transition boundary erased into one-object history | compressed pre/post records linked with no lineage | branching/merging/coherence data discarded while history claims survive | PASS: 3/3 detected |
| VI. Inverse Inference & Reconstruction | Reconstruction | two formation objects reconstructed as one persistent object | a single history invented across an unlinked transition | impossible history reconstructed from incoherent lineage | PASS: 3/3 detected |
| VII. Computation & Selection | Computation | identity-changing object updated under one key, causing state collision | state carry-over computed without successor relation | inconsistent lineage graph causes duplicate/missing propagation | PASS: 3/3 detected |
| VIII. Dynamics & Action | Operation | transition-required event executed as same-object operation | action state carried to an unlinked successor | conflicting successor relations corrupt operation history | PASS: 3/3 detected |

This is a shared-rule transfer test, not direct validation of the selected methods as complete methodologies.

## 6. Negative control / 음성 대조군

SC-06 does **not** require a new formation model for every temporal change.

It permits:

1. ordinary analytic, represented, weight, or defined-property-value evolution inside a fixed Stage-VI formation background and valid regular support signature;
2. canonical identity lineage on a fixed formation background;
3. branching or merging when the lineage relation is typed and coherent and the application does not require unique successors;
4. property-status or realized-axis events to remain separate from formation transitions whenever the declared event class and regular support rules allow it.

Aggregate equality or inequality remains irrelevant as a standalone lineage criterion.

Therefore SC-06 is not “promote every change to a transition”. It is:

> **Do not confuse literal identity, regular evolution, transition, and successor relation.**

## 7. Standard transition/lineage record / 표준 전이·계보 기록

```text
TEMPORAL_RECORD_ID:
PRE_TIME_OR_ORDER:
POST_TIME_OR_ORDER:
PRE_FORMATION_BACKGROUND:
POST_FORMATION_BACKGROUND:
PRE_SUPPORT_SIGNATURE:
POST_SUPPORT_SIGNATURE:
EVENT_CLASS:
IDENTITY_PRESERVED: yes / no / not_applicable
TRANSITION_REQUIRED: yes / no
TRANSITION_REASON:
CHANNEL_LINEAGE_RELATION:
COMPONENT_LINEAGE_RELATION_IF_REQUIRED:
LINEAGE_SOURCE: canonical_fixed_background / supplied_transition_relation / none
SELF_TIME_IDENTITY_CHECK:
CROSS_TIME_COHERENCE_CHECK:
BRANCHING_OR_MERGING:
UNIQUE_SUCCESSOR_REQUIRED: yes / no
AGGREGATE_USED_AS_LINEAGE_EVIDENCE: no
BALANCE_OR_JUMP_RULE_IF_CLAIMED:
KNOWN_IDENTITY_BREAKS:
```

## 8. Promotion test / 승격 시험

```text
SOURCE_SUPPORT: pass
SAME_SEMANTIC_MEANING_ACROSS_METHODS: pass
TRANSITION_AS_REGULAR_EVOLUTION_COUNTEREXAMPLE: pass
LINEAGE_OMISSION_OR_INVENTION_COUNTEREXAMPLE: pass
LINEAGE_COHERENCE_OR_TYPE_COUNTEREXAMPLE: pass
NON_TRANSFER_CASE_IDENTIFIED: pass
METHOD_TASK_REDEFINITION: none
DIRECT_VALIDATION_SEPARATION: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
```

## 9. Transfer conditions / 적용 조건

Apply SC-06 when:

- time/order-indexed work makes identity, persistence, succession, history, or successor claims;
- a change may invalidate Stage-VI identity, admitted support, or a declared regular support signature;
- pre/post objects need to remain connected without pretending that they are literally equal.

## 10. Non-transfer cases / 적용하지 않는 경우

SC-06 is inactive for purely static single-slice work with no temporal identity or succession claim.

Inside a fixed-background regular epoch, a long transition record is unnecessary when canonical identity lineage is sufficient.

Branching/merging is not itself failure; uniqueness is tested only when the method/task explicitly requires it.

## 11. Evidence limits / 한계

- This is a synthetic cross-field transfer pilot.
- The rule is extracted primarily from the current DSD Dynamics transition/lineage interface and Formation channel identity.
- One representative method per higher-level field was tested.
- It does not validate the overall correctness, performance, or usefulness of all 22 methods.
- Real event histories, organizational incidents, empirical time series, and judicial/historical succession claims require separate external evidence.

## 12. Relation to SC-01–SC-05 / SC-01~05와의 관계

```text
SC-01 = preserve claim-relevant distinctions
SC-02 = lock the source/interface/revision that activates the rules
SC-03 = explicitly supply claim-relevant mappings
SC-04 = keep only claim-relevant layers as dependencies
SC-05 = respect information loss and reconstruction limits of reduced readouts
SC-06 = separate identity-preserving evolution from identity-breaking transition and record succession through lineage
```

The six rules are complementary but non-identical.

## 13. Next shared-core candidate / 다음 후보

`SC-07 — Evidence Scope / Case-Origin Separation` should be tested separately.
