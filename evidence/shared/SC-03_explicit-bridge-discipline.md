# SC-03 — Explicit Bridge Discipline / 명시적 브리지 규율 검증

Status: **promoted_with_conditions**
Date: 2026-09-06
Evidence scope: `shared_method_family`
Case origin: `synthetic_constructed_benchmark`

## 1. Result / 결과

`Explicit Bridge Discipline` is promoted as a **conditional shared-core rule**.
A representative method from each of the eight higher-level fields was tested against three deliberately invalid or destabilizing perturbations:

- `B0`: bridge omission — keep a downstream claim after deleting the selector or bridge that justifies it;
- `BN`: name/coordinate inference — infer ownership, analytic meaning, coefficient role, or domain meaning from labels, coordinate occurrence, or raw value alone;
- `BS`: bridge substitution sensitivity — keep the same upstream record but replace one admissible supplied bridge with another and test whether the downstream result changes.

```text
BRIDGE_OMISSION_CHECKS: 8/8 detected
NAME_OR_COORDINATE_INFERENCE_CHECKS: 8/8 detected
BRIDGE_SUBSTITUTION_SENSITIVITY_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> A cross-interface or cross-domain correspondence is not generated merely by a shared name, numerical value, or occurrence of an object among typed inputs. When a claim depends on such a correspondence, its source carrier, target carrier, mapping rule, assumptions, and preservation/loss obligations must be supplied explicitly or already be part of the locked interface.

## 2. Source basis / 소스 근거

### Property Axiom System

The Property system keeps application-specific semantics, representation choices, downstream aggregation, dynamics, and geometric specialization outside the universal property core. Such semantics and extensions enter only when explicitly supplied.

### Channel-Indexed Static Aggregation

A multi-input property record is not automatically allocated to one formation channel. Channel-local use requires an application-supplied selector `Sel_A(c)`, and downstream analytic realization or aggregation uses supplied bridges such as `B_c` and `Theta_A`. The property axioms and matching input coordinates do not infer those maps.

### Structural Reorganization Dynamics

A static property bridge does not determine an evolution operator. When property data influence transport, relaxation, coupling, or propagation, a separate constitutive dynamic bridge `B_dyn,t` is required. The dynamics paper explicitly states that property labels do not canonically determine coefficients or operators.

## 3. Locked microcase / 고정 microcase

Fix the same Stage-VI formation background with admitted channels `c+` and `c-` and one binary typed property record:

```text
iota_b = (q_b, (c+, c-), z=2)
```

The record belongs to the complete ordered pair and has no distinguished unary owner by type alone.

Supply several admissible downstream choices as separate data:

```text
Selector S_plus:  iota_b -> c+
Selector S_minus: iota_b -> c-

Static bridge Theta_1(iota_b) = 2
Static bridge Theta_2(iota_b) = -2

Dynamic bridge B1(iota_b) -> K = 2 I
Dynamic bridge B2(iota_b) -> K = 5 I
```

The same upstream typed record therefore admits distinct downstream associations and representations unless an application explicitly selects one.

## 4. Perturbations / 교란 연산

### B0 — Bridge omission

Delete a required selector or bridge while preserving the downstream claim.
The result becomes unsupported or underdetermined.

### BN — Name/coordinate inference

Infer, for example,

```text
owner = c+
aggregate = 2
K = 2 I
```

merely because `c+` occurs among the inputs, the property label resembles a downstream role, or the assigned value is `2`.
The source systems provide no canonical inference of this kind.

### BS — Bridge substitution sensitivity

Hold the upstream property record fixed and change only the supplied bridge:

```text
S_plus -> S_minus
Theta_1 -> Theta_2
B1 -> B2
```

If the downstream result changes, the bridge is claim-relevant supplied data rather than dispensable notation.

## 5. Eight-field transfer test / 8개 상위 분야 교차 시험

| Field | Representative method | B0: omission | BN: name/coordinate inference | BS: substitution sensitivity | Result |
|---|---|---|---|---|---|
| I. Structural Description & Understanding | Analysis | the structural correspondence being analyzed loses its mapping basis | terminological or coordinate similarity is mistaken for structural correspondence | the same upstream record can support different downstream structures under different bridges | PASS: 3/3 detected |
| II. Criteria & Validation | Audit | the source-to-claim trace is incomplete | an implicit inference may be mistaken for a justified mapping | pass/fail support depends on which bridge was actually used | PASS: 3/3 detected |
| III. Construction & Transformation | Transformation | the source-target map is missing from the transformation definition | matching names are mistaken for preservation | different bridges generate different target representations | PASS: 3/3 detected |
| IV. Evidence & Lineage | Provenance | the derivation chain from upstream datum to result is broken | shared labels are mistaken for derivation edges | bridge substitution changes the derivation path | PASS: 3/3 detected |
| V. Reduction & Representation | Aggregation | no analytic carrier or property aggregation map is supplied | the raw property value is mistaken for an already justified aggregate | `Theta_1` and `Theta_2` yield different aggregates from the same support | PASS: 3/3 detected |
| VI. Inverse Inference & Reconstruction | Diagnosis | the link between observations/DSD states and hidden-state hypotheses is unsupported | label similarity is mistaken for causal/state correspondence | the compatible diagnosis set may change under a different bridge | PASS: 3/3 detected |
| VII. Computation & Selection | Optimization | the mapping from a DSD-derived quantity into objective/constraint data is unspecified | a similarly named property is used automatically as an objective coefficient | objective values or rankings can change when the bridge changes | PASS: 3/3 detected |
| VIII. Dynamics & Action | Control | the property-to-control/dynamic coefficient map is missing | an intervention coefficient is inferred directly from a property label | `B1` and `B2` can yield different control laws from the same upstream state | PASS: 3/3 detected |

This is a shared-rule transfer test, not direct validation of the selected methods as complete methodologies.

## 6. Negative control / 음성 대조군

SC-03 does **not** require an arbitrary new function between every two steps.
No extra ad hoc bridge is required when one of the following holds:

1. source and target are the same typed carrier and the task explicitly uses the identity map;
2. the locked interface already supplies an inclusion, projection, embedding, isomorphism, selector, or other structure-preserving map and the claim stays within that map's stated preservation range;
3. a separate invariance theorem proves that the final result is identical for every admissible bridge in the declared class.

Therefore SC-03 is not a rule of bridge proliferation. It is:

> **Do not silently automate claim-relevant cross-interface inference.**

## 7. Standard bridge record / 표준 브리지 기록

```text
BRIDGE_ID:
SOURCE_LAYER_OR_DOMAIN:
SOURCE_CARRIER:
TARGET_LAYER_OR_DOMAIN:
TARGET_CARRIER:
MAP_OR_RELATION:
SELECTION_RULE_IF_ANY:
ASSUMPTIONS:
PRESERVED_STRUCTURE:
KNOWN_INFORMATION_LOSS:
VALIDATION_OR_JUSTIFICATION:
ALTERNATIVE_BRIDGES_CONSIDERED:
```

## 8. Promotion test / 승격 시험

```text
SOURCE_SUPPORT: pass
SAME_SEMANTIC_MEANING_ACROSS_METHODS: pass
BRIDGE_OMISSION_COUNTEREXAMPLE: pass
NAME_OR_COORDINATE_INFERENCE_COUNTEREXAMPLE: pass
BRIDGE_SUBSTITUTION_COUNTEREXAMPLE: pass
NON_TRANSFER_CASE_IDENTIFIED: pass
METHOD_TASK_REDEFINITION: none
DIRECT_VALIDATION_SEPARATION: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
```

## 9. Transfer conditions / 적용 조건

Apply SC-03 when:

- a claim connects distinct DSD layers, representations, typed carriers, external domains, or method outputs;
- different admissible mappings could change ownership, support, coefficient, classification, ranking, diagnosis, or intervention;
- a DSD structural result is used to support an external-domain meaning or standard.

In external-domain applications, the domain bridge and the field's own validation standard must be recorded separately.

## 10. Non-transfer cases / 적용하지 않는 경우

Do not force an extra bridge when:

- no cross-interface mapping exists because the operation stays inside the same declared typed carrier;
- the locked interface already supplies the required map and the claim stays within its explicit preservation domain;
- invariance across all admissible bridges has been separately established.

## 11. Evidence limits / 한계

- This is a synthetic cross-field transfer pilot.
- One representative method per higher-level field was tested.
- It does not validate the overall correctness, performance, or usefulness of all 22 methods.
- Real events, judicial cases, historical cases, personal cases, and empirical datasets still require separate domain-bridge validation.

## 12. Relation to SC-01 and SC-02 / SC-01·SC-02와의 관계

```text
SC-01 = preserve claim-relevant distinctions
SC-02 = lock the semantics/interface/revision that make rules active
SC-03 = explicitly supply claim-relevant cross-interface mappings
```

The three rules are complementary but non-identical.

## 13. Next shared-core candidate / 다음 후보

`SC-04 — Minimum-Layer / Optional-Interface Restraint` should be tested separately.
