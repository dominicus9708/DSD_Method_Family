# SC-05 — Aggregate / Information-Loss / Reconstruction Restraint / 집계·정보손실·복원 절제 검증

Status: **promoted_with_conditions**
Date: 2026-09-06
Evidence scope: `shared_method_family`
Case origin: `synthetic_constructed_benchmark`

## 1. Result / 결과

`Aggregate / Information-Loss / Reconstruction Restraint` is promoted as a **conditional shared-core rule**.
A representative method from each of the eight higher-level fields was tested against three aggregate/reconstruction perturbations:

- `AE`: aggregate-equality inflation — infer support, decomposition, full structure, provenance, or state equality from equal reduced aggregates;
- `RI`: reconstruction without injectivity — claim a unique source reconstruction from a many-to-one aggregate without an injectivity/inverse basis;
- `LE`: loss-boundary erasure — retain only the reduced aggregate while deleting the record of retained support, injectivity status, or known information loss and then make claims requiring the discarded information.

```text
AGGREGATE_EQUALITY_INFLATION_CHECKS: 8/8 detected
RECONSTRUCTION_WITHOUT_INJECTIVITY_CHECKS: 8/8 detected
LOSS_BOUNDARY_ERASURE_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Equality of a reduced aggregate entails equality only for information that the aggregation/readout map is known to preserve. Reconstruction of support, decomposition, typed inputs, correlation, provenance, component state, or history requires injectivity, inverse data, or sufficient support-retaining side information on the declared admissible class.

SC-05 does not prohibit aggregation. It prohibits treating discarded information as if it remained available.

## 2. Source basis / 소스 근거

### Formation Axiom System

The Formation system distinguishes strict formation equivalence from composite-level coincidence. Equal composite outputs under a prescribed output comparison are strictly weaker than equality of the full formation structure.

### Channel-Indexed Static Aggregation

Section 11 separates support-retaining channel/property data from the final sums.
For fixed support `F`, the summation operator

```text
S_F((u_c)_{c in F}) = sum_{c in F} u_c
```

is reconstructive on an admissible family `A_F` only when the restriction is injective. The paper gives the exact criterion

```text
ker(S_F) ∩ (A_F - A_F) = {0}.
```

Property aggregation may discard selected support, property kind, typed input coordinates, and cross-property correlation. Combined static equality likewise does not reconstruct either coordinate's support without the required injectivity and cross-coordinate reconstruction conditions.

### Structural Reorganization Dynamics

The Dynamics paper keeps the state component-resolved and explicitly rejects identification of aggregate equality with component-state equality. Lineage-connected succession is not determined by aggregate equality or inequality. Its finite countermodel gives two distinct component trajectories with the same aggregate at every time.

## 3. Locked static witness / 고정 정적 witness

Use the finite witnesses from the Static Aggregation paper.

### Formation side

```text
T(c0) = 0
T(c+) = +1
T(c-) = -1

F0 = {c0}
F± = {c+, c-}

Comp(F0) = 0 = Comp(F±)
F0 != F±
```

### Property side

```text
iota_u = (property_u, c+, 2)
iota_b = (property_b, (c+, c-), -2)
iota_0 = (property_0, c-, 0)

G± = {iota_u, iota_b}
G0 = {iota_0}

Agg(G±) = 0 = Agg(G0)
G± != G0
```

### Combined

```text
Static(F±, G±) = (0,0) = Static(F0, G0)
```

The reduced descriptor is identical while both formation support and property support differ.

## 4. Locked dynamic auxiliary witness / 고정 동적 보조 witness

Use the same channel support `{c1,c2}` for two trajectories:

```text
U: component terms = ( f(t), -f(t) )
V: component terms = ( g(t), -g(t) )
f != g
```

Then

```text
Comp_U(t) = 0 = Comp_V(t)
```

for every `t`, while the component-resolved realizations differ. Aggregate equality therefore does not determine component-state identity, propagation content, or lineage.

## 5. Perturbations / 교란 연산

### AE — Aggregate-equality inflation

From `Agg(X)=Agg(Y)` or equal reduced readouts, infer one or more of:

```text
same support
same decomposition
same full structural descriptor
same source/provenance
same component state
same history/lineage
```

without a preservation theorem.

### RI — Reconstruction without injectivity

Given only the aggregate, select one source/support/decomposition as the unique original despite the map being non-injective or its injectivity being unknown.

### LE — Loss-boundary erasure

Delete the operational fields

```text
SUPPORT_RETAINED
INJECTIVITY_STATUS
KNOWN_INFORMATION_LOSS
```

from an aggregate-only record and then permit downstream support-sensitive, provenance-sensitive, component-sensitive, or history-sensitive claims.

## 6. Eight-field transfer test / 8개 상위 분야 교차 시험

| Field | Representative method | AE: equality inflation | RI: reconstruction without injectivity | LE: loss-boundary erasure | Result |
|---|---|---|---|---|---|
| I. Structural Description & Understanding | Comparison | equal aggregate is misclassified as full structural equivalence | one of `F0` or `F±` is selected as the unique original | the comparison scope is overstated because erased distinctions are no longer recorded | PASS: 3/3 detected |
| II. Criteria & Validation | Audit | aggregate agreement is used to pass a support-sensitive claim | a decomposition is reconstructed without an injectivity basis and reused as evidence | the audit cannot retrace what information the reduction preserved | PASS: 3/3 detected |
| III. Construction & Transformation | Transformation | aggregate preservation is inflated into structure preservation | a many-to-one target aggregate is uniquely inverted | preserved versus discarded source structure is not recorded | PASS: 3/3 detected |
| IV. Evidence & Lineage | Provenance | equal aggregate is mistaken for equal source/provenance | one derivation path is invented from the readout alone | support and bridge history are removed from the provenance chain | PASS: 3/3 detected |
| V. Reduction & Representation | Aggregation | equal sums are treated as equal selected support/property structure | original support is uniquely reconstructed from a non-injective sum | only the aggregate is retained while the loss boundary is omitted | PASS: 3/3 detected |
| VI. Inverse Inference & Reconstruction | Reconstruction | equal aggregates are treated as equal source states | unique reconstruction is asserted with no injectivity/inverse witness | unrecoverable coordinates are not marked, overstating reconstruction confidence | PASS: 3/3 detected |
| VII. Computation & Selection | Computation | an aggregate is used as a complete cache key for a component-sensitive computation, causing a collision | channel count/component tuple is inferred uniquely from aggregate zero | the cache/reduction record does not state which input distinctions were discarded | PASS: 3/3 detected |
| VIII. Dynamics & Action | Simulation | equal aggregate trajectories are treated as equal component states/identity | the readout `0` is uniquely expanded into `f(t)` or `g(t)` | component-resolved distinctions needed for propagation or lineage disappear | PASS: 3/3 detected |

This is a shared-rule transfer test, not direct validation of the selected methods as complete methodologies.

## 7. Negative control / 음성 대조군

Stronger conclusions from an aggregate are admissible when their reconstruction basis is explicit.
Examples include:

1. the aggregation/readout map is proved injective on the declared admissible data class;
2. for fixed-support summation, an exact kernel criterion such as `ker(S_F) ∩ (A_F-A_F) = {0}` is satisfied and the support itself is known;
3. for a combined descriptor, injectivity of each coordinate and any necessary cross-coordinate reconstruction condition are established;
4. the final claim concerns only the aggregate value, norm, threshold, or another quantity explicitly defined at the reduced level;
5. support-retaining data or a sufficient sidecar are kept alongside the aggregate.

Therefore SC-05 is not "never aggregate". It is:

> **Do not reconstruct or identify more structure than the declared reduction is proved to preserve.**

## 8. Standard aggregation/reconstruction record / 표준 집계·복원 기록

```text
AGGREGATION_OR_READOUT_ID:
SOURCE_CARRIER:
AGGREGATE_CARRIER:
MAP:
ADMISSIBLE_DATA_CLASS:
SUPPORT_RETAINED: yes / no / partial
INFORMATION_PRESERVED:
KNOWN_INFORMATION_LOSS:
INJECTIVITY_STATUS: proved / disproved / unknown / not_required
INJECTIVITY_OR_KERNEL_WITNESS:
RECONSTRUCTION_CLAIM: none / partial / unique
RECONSTRUCTION_BASIS:
CROSS_COORDINATE_CONDITIONS_IF_ANY:
DOWNSTREAM_CLAIMS_REQUIRING_LOST_DATA:
```

## 9. Promotion test / 승격 시험

```text
SOURCE_SUPPORT: pass
SAME_SEMANTIC_MEANING_ACROSS_METHODS: pass
AGGREGATE_EQUALITY_INFLATION_COUNTEREXAMPLE: pass
RECONSTRUCTION_WITHOUT_INJECTIVITY_COUNTEREXAMPLE: pass
LOSS_BOUNDARY_ERASURE_COUNTEREXAMPLE: pass
NON_TRANSFER_CASE_IDENTIFIED: pass
METHOD_TASK_REDEFINITION: none
DIRECT_VALIDATION_SEPARATION: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
```

## 10. Transfer conditions / 적용 조건

Apply SC-05 when:

- a method uses an aggregate, summary, compressed descriptor, reduced readout, or another potentially many-to-one representation;
- a downstream claim attempts to recover support, decomposition, source, history, component state, or another distinction not explicitly preserved by that map;
- a reduced result is reused as a cache key, identity criterion, provenance token, or reconstruction input.

## 11. Non-transfer cases / 적용하지 않는 경우

SC-05 is inactive when no aggregate/reduced representation is used.

A support-retaining sidecar is not mandatory when the claim is genuinely limited to the aggregate itself and no discarded information is needed.

When injectivity and inverse conditions are proved, reconstruction is permitted exactly within the proven range.

## 12. Evidence limits / 한계

- This is a synthetic cross-field transfer pilot.
- The core witnesses reuse finite/countermodel structures explicitly supplied by the current Static Aggregation and Dynamics papers.
- One representative method per higher-level field was tested.
- It does not validate the overall correctness, performance, or usefulness of all 22 methods.
- Real datasets involving lossy measurement summaries, compression, or simulation readouts still require separate external validation.

## 13. Relation to SC-01–SC-04 / SC-01~04와의 관계

```text
SC-01 = preserve claim-relevant distinctions
SC-02 = lock the source/interface/revision that activates the rules
SC-03 = explicitly supply claim-relevant mappings
SC-04 = select only claim-relevant layers as dependencies
SC-05 = do not infer beyond the preservation/reconstruction capacity of a reduced aggregate
```

The five rules are complementary but non-identical.

## 14. Next shared-core candidate / 다음 후보

`SC-06 — Transition / Lineage Discipline` should be tested separately.
