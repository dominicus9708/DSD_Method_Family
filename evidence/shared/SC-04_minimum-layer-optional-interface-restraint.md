# SC-04 — Minimum-Layer / Optional-Interface Restraint / 최소 층위·선택 인터페이스 절제 검증

Status: **promoted_with_conditions**
Date: 2026-09-06
Evidence scope: `shared_method_family`
Case origin: `synthetic_constructed_benchmark`

## 1. Result / 결과

`Minimum-Layer / Optional-Interface Restraint` is promoted as a **conditional shared-core rule**.
A representative method from each of the eight higher-level fields was tested against three layer-selection perturbations:

- `U`: required-layer deletion — remove one claim-required layer and keep the same claim;
- `O`: optional-layer overconstraint — turn a claim-irrelevant optional interface into a mandatory eligibility condition;
- `X`: irrelevant-extension contamination — add alternative irrelevant optional extensions and allow the core result to change only because of that extension.

```text
REQUIRED_LAYER_DELETION_CHECKS: 8/8 detected
OPTIONAL_LAYER_OVERCONSTRAINT_CHECKS: 8/8 detected
IRRELEVANT_EXTENSION_CONTAMINATION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
MINIMALITY_SCOPE: inclusion-minimal_relative_to_locked_layer_inventory
```

Invariant meaning:

> Each claim must have a sufficient DSD dependency set, but the absence of a claim-irrelevant optional layer or specialization must not be treated as failure, and an irrelevant optional extension must not alter the core result merely by being present.

This is not a universal cardinality-minimality requirement. It is a rule against both **missing required dependencies** and **invented optional dependencies**.

## 2. Source basis / 소스 근거

### Property Axiom System

The general Property core does not require the earlier realized-axis machinery. Axis lines, bilinear data, normals, ranks, and related structures remain a downstream geometric specialization. Optional representation is added only after the complete core descriptor has been constructed.

### Channel-Indexed Static Aggregation

The Static layer accepts the general Property interface without requiring a realized-axis specialization. Realized-axis structure and later physical interpretations may use the Static layer but are not required for its definition. The countable aggregation construction is also an optional extension of the finite core.

### Structural Reorganization Dynamics

The Dynamics layer explicitly avoids making the Property extension, realized-axis geometry, or reduced aggregate mandatory for every dynamical realization. Core channel-resolved dynamics may be defined over the fixed Stage-VI formation background without adding a Property model. Missing optional interfaces are omitted rather than replaced by numerical zero objects.

## 3. Locked layer inventory / 잠근 층위 목록

For this pilot only, use the following inventory:

```text
F = Formation interface
P = General Property interface
A = Channel-Indexed Static Aggregation interface
D = Structural Reorganization Dynamics interface
G = Realized-axis geometric specialization
```

`G` is a specialization rather than a foundational layer, but it is treated as one selectable interface for the layer-selection test.

## 4. Locked claims and relative minimum sufficient sets / 고정 claim과 상대적 최소 충분 집합

No global or unique minimality is claimed. The following are **inclusion-minimal relative to the locked inventory and current source interfaces**.

| Claim | Meaning | Relative minimum sufficient set |
|---|---|---|
| `K_F` | an operational channel is admitted | `{F}` |
| `K_P` | a typed property input has status `defined_zero` | `{F,P}` |
| `K_A` | a selected channel family has a declared analytic aggregate | `{F,A}` |
| `K_D` | supplied transition/lineage supports succession between formation states | `{F,D}` |
| `K_G` | a realized-axis specialization has a declared rank/line geometry | `{F,P,G}` |

## 5. Perturbations / 교란 연산

### U — Required-layer deletion

Remove one member of the relative minimum sufficient set and keep the same claim. The claim should become unsupported or underdetermined.

### O — Optional-layer overconstraint

Require an optional interface that the target claim does not need. If a valid execution without that interface is rejected, the method has created an unjustified dependency.

### X — Irrelevant-extension contamination

Keep the core data fixed, add two alternative optional-extension variants that the source interface declares irrelevant to the core claim, and let only the extension vary. If the core result changes, the optional layer has contaminated the claim.

## 6. Eight-field transfer test / 8개 상위 분야 교차 시험

| Field | Representative method | Claim / minimum set | U: deletion | O: overconstraint | X: contamination | Result |
|---|---|---|---|---|---|---|
| I. Structural Description & Understanding | Analysis | `K_F / {F}` | deleting F removes admission support | requiring P falsely rejects a valid Formation-only case | changing an irrelevant P extension must not alter channel admission | PASS: 3/3 detected |
| II. Criteria & Validation | Specification | `K_P / {F,P}` | deleting P removes the property-status requirement | requiring G falsely rejects a non-geometric property specification | G variants must not change the `defined_zero` requirement | PASS: 3/3 detected |
| III. Construction & Transformation | Design | `K_A / {F,A}` | deleting A removes the analytic-readout design target | requiring P falsely rejects channel-only aggregation design | irrelevant P variants must not alter the channel aggregate design verdict | PASS: 3/3 detected |
| IV. Evidence & Lineage | Measurement | `K_P / {F,P}` | deleting P removes the status target being measured/discriminated | requiring G falsely rejects non-geometric typed-property measurement | G variants must not change the same property-measurement classification | PASS: 3/3 detected |
| V. Reduction & Representation | Compression | `K_A / {F,A}` | deleting A removes the readout whose preservation is being tested | requiring G falsely rejects non-geometric analytic compression | G variants must not alter aggregate-preservation verdicts | PASS: 3/3 detected |
| VI. Inverse Inference & Reconstruction | Reconstruction | `K_D / {F,D}` | deleting D removes transition/lineage history support | requiring P falsely rejects property-free dynamic history | irrelevant P variants must not alter the same lineage reconstruction | PASS: 3/3 detected |
| VII. Computation & Selection | Optimization | `K_A / {F,A}` | deleting A removes the declared aggregate objective quantity | requiring G falsely rejects a non-geometric objective problem | unbridged G variants must not change objective ranking | PASS: 3/3 detected |
| VIII. Dynamics & Action | Prediction | `K_D / {F,D}` | deleting D removes the dynamic basis of a future-transition claim | requiring P or A falsely rejects a core Formation+Dynamics prediction | unbridged optional P/A variants must not alter the same dynamic prediction | PASS: 3/3 detected |

This is a shared-rule transfer test, not direct validation of the selected methods as complete methodologies.

## 7. Negative control / 음성 대조군

A non-minimal selected set is not automatically wrong.

It is admissible when:

1. a multi-claim task uses the union of the layer sets needed by its separate claims;
2. an additional layer supports an explicitly declared secondary claim, diagnostic, sensitivity analysis, representation, or computational convenience while remaining `REQUIRED_FOR_CORE_CLAIM: no`;
3. the optional specialization itself is the target, such as a realized-axis rank claim;
4. an extra optional interface is present but the core result remains invariant under that irrelevant extension.

Therefore SC-04 is not “always use the fewest possible layers”. It is:

> **Do not omit required dependencies, do not turn irrelevant optional interfaces into hidden prerequisites, and do not let irrelevant extensions silently change the core result.**

## 8. Standard layer-selection record / 표준 층위 선택 기록

```text
CLAIM_ID:
CLAIM_TEXT:
CANDIDATE_LAYER_INVENTORY:
MINIMALITY_SCOPE: inclusion-minimal_relative_to_locked_layer_inventory
MINIMUM_SUFFICIENT_LAYER_SET:
SELECTED_LAYER_SET:
REQUIRED_LAYER_WITNESSES:
OPTIONAL_LAYERS_PRESENT:
OPTIONAL_LAYER_ROLE:
REQUIRED_FOR_CORE_CLAIM: yes / no
CORE_RESULT_INVARIANT_UNDER_IRRELEVANT_EXTENSION:
UNSUPPORTED_CLAIMS_FROM_OMITTED_LAYER:
```

## 9. Promotion test / 승격 시험

```text
SOURCE_SUPPORT: pass
SAME_SEMANTIC_MEANING_ACROSS_METHODS: pass
REQUIRED_LAYER_DELETION_COUNTEREXAMPLE: pass
OPTIONAL_LAYER_OVERCONSTRAINT_COUNTEREXAMPLE: pass
IRRELEVANT_EXTENSION_CONTAMINATION_COUNTEREXAMPLE: pass
NON_TRANSFER_CASE_IDENTIFIED: pass
METHOD_TASK_REDEFINITION: none
DIRECT_VALIDATION_SEPARATION: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
```

## 10. Transfer conditions / 적용 조건

Apply SC-04 when:

- a claim depends on one or more DSD source/interface layers;
- optional interfaces or specializations could be mistaken for mandatory prerequisites;
- several DSD layers are combined and their claim-specific roles need to be separated.

## 11. Non-transfer cases / 적용하지 않는 경우

A long layer-selection protocol is unnecessary when a task is already fully contained in one locked interface and no optional downstream interface enters the record.

A multi-purpose task may legitimately use a non-minimal overall set when each additional layer supports a separately declared output and the core/secondary claim boundaries remain explicit.

## 12. Evidence limits / 한계

- This is a synthetic cross-field transfer pilot.
- Relative minimality is asserted only against the locked `F/P/A/D/G` inventory and the current source interfaces.
- One representative method per higher-level field was tested.
- It does not validate the overall correctness, performance, or usefulness of all 22 methods.
- Real-world costs and benefits of layer selection still require independent cases.

## 13. Relation to SC-01–SC-03 / SC-01~03과의 관계

```text
SC-01 = preserve claim-relevant distinctions
SC-02 = lock the source/interface/revision that activates the rules
SC-03 = explicitly supply required cross-interface mappings
SC-04 = keep only claim-relevant layers as dependencies and do not over-require optional interfaces
```

The four rules are complementary but non-identical.

## 14. Next shared-core candidate / 다음 후보

`SC-05 — Aggregate / Information-Loss / Reconstruction Restraint` should be tested separately.
