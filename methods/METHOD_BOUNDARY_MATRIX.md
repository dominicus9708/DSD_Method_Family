# DSD Method Boundary Matrix / DSD 방법 독립성·중복성 검토

Status: current classification audit
Date: 2026-09-06

This document checks whether the current **22 independent DSD methods** are genuine method distinctions or merely duplicated labels.

## 1. Non-duplication test / 중복 판정 기준

Two methods become duplicate candidates only when the following five interfaces are materially the same:

```text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
```

Sharing DSD source layers, operators, records, or appearing in one workflow is not sufficient to merge methods.

## 2. Current verdict / 현재 판정

```text
METHOD_COUNT: 22
EXACT_DUPLICATE_METHODS_FOUND: 0
METHODS_REQUIRING_SCOPE_WORDING_REFINEMENT: Analysis
LEGACY_WRAPPERS_COUNTED_AS_METHODS: 0
```

The current 22-method registry can remain intact. The main scope-overlap risk was the older wording of **DSD Analysis**, which said that Analysis itself decomposes, compares, and reinterprets a target. Under the current method-family architecture, the Analysis core is narrowed to **single-target structural decomposition and structural re-expression**. Cross-target comparison, explicit class assignment, and source/context interpretation are attributed to Comparison, Classification, and Interpretation respectively.

Historical Analysis records may contain several of these operations together. They are not retroactively rewritten; new records should identify each method-specific output separately.

## 3. Field-by-field boundaries / 상위 분야별 경계

| Field | Methods | Boundary that keeps them distinct |
|---|---|---|
| I. Structural Description & Understanding | Analysis / Comparison / Classification / Interpretation | one-target decomposition and re-expression / cross-target preserved-difference judgment / criterion-based class assignment / source-context-bridge reading |
| II. Criteria & Validation | Specification / Audit | declare requirements / retrace and evaluate performed work against scope, evidence, procedure, and standards |
| III. Construction & Transformation | Design / Synthesis / Transformation | construct target from goals and constraints / compose admitted parts under a composition rule / map source to target representation or regime while recording preservation and loss |
| IV. Evidence & Lineage | Measurement / Provenance / Lineage | determine discriminating observations / trace origin and derivation / determine predecessor-successor relation across change |
| V. Reduction & Representation | Aggregation / Compression | construct a declared readout / reduce representation while preserving declared downstream distinctions |
| VI. Inverse Inference & Reconstruction | Diagnosis / Reconstruction | infer compatible present hidden states or causes / infer compatible prior, omitted, damaged, compressed, or lost structures and histories |
| VII. Computation & Selection | Computation / Optimization | determine what must be evaluated and what may be omitted / choose among admissible alternatives under objective and constraints |
| VIII. Dynamics & Action | Simulation / Prediction / Control / Operation | generate model-consistent trajectories / assert future-target relevance / choose interventions / manage repeated live lifecycle, monitoring, handoff, and method orchestration |

## 4. Near-overlap pairs / 중복으로 오인하기 쉬운 관계

### Analysis vs Comparison vs Classification vs Interpretation

Analysis provides the structural decomposition and status-separated representation of a declared target. Comparison consumes two or more such structures and judges preserved and differing structure. Classification applies explicit criteria to assign classes or groupings. Interpretation separates source material, context, interpretive assumptions, and the bridge that supports a reading.

### Design vs Optimization

Design forms an admissible target/design space from goals and constraints. Optimization selects among an already justified admissible space under an objective and constraints. A design workflow may contain optimization, but the success criteria differ.

### Synthesis vs Transformation

Synthesis is a parts-to-whole construction under an explicit composition rule. Transformation is a source-to-target mapping between representations, schemas, models, or regimes. A synthesized object may later be transformed, and transformed components may later be synthesized, without collapsing the two methods.

### Measurement vs Diagnosis

Measurement asks which observations can discriminate relevant alternatives. Diagnosis uses observations to narrow compatible current hidden-state or cause hypotheses.

### Provenance vs Lineage vs Reconstruction

Provenance records supported origin/derivation chains. Lineage records successor identity across change. Reconstruction infers admissible hidden or lost past structures from incomplete evidence. A reconstructed origin is not automatically provenance; a provenance chain is not automatically lineage.

### Aggregation vs Compression vs Transformation

Aggregation constructs a readout, compression intentionally reduces representation relative to retained distinctions, and transformation maps between source and target forms. They may share maps but have different validation targets.

### Computation vs Optimization vs Control

Computation determines required evaluations. Optimization chooses among admissible alternatives. Control chooses dynamic interventions intended to move a system toward declared target states.

### Simulation vs Prediction

Simulation generates trajectories consistent with the supplied model. Prediction additionally claims relevance to a future external target and therefore requires empirical/domain validation beyond simulation consistency.

## 5. Legacy-wrapper rule / 호환성 묶음 규칙

The following paths remain navigation compatibility wrappers only and are **not** methods:

```text
09_provenance_lineage/
10_aggregation_compression/
12_computation_optimization/
15_diagnosis_reconstruction/
```

Their nested independent methods remain separately counted.

## 6. Shared-core extraction rule / 공통 구조 추출 규칙

Common DSD structure is extracted upward without erasing method boundaries.

```text
SHARED_CORE:
METHOD_SPECIFIC_INPUT:
METHOD_SPECIFIC_OPERATION:
METHOD_SPECIFIC_OUTPUT:
METHOD_SPECIFIC_FAILURE_CRITERIA:
METHOD_SPECIFIC_VALIDATION:
```

A rule belongs in `SHARED_CORE` only when multiple methods can reuse it without changing its meaning. The method-specific fields remain local even when they use the same Formation, Property, Static, Dynamics, bridge, status, evidence, or domain-validation machinery.

The current shared-core registry contains **SC-01 through SC-10** and is closed for the present registry with conditions. The closure audit reviewed all 45 unordered rule pairs and found no exact duplicate shared rules. This does not alter the current method verdict:

```text
METHOD_COUNT: 22
EXACT_DUPLICATE_METHODS_FOUND: 0
SHARED_CORE_RULE_COUNT: 10
SHARED_CORE_CLOSURE: closed_for_current_registry_with_conditions
```

Shared-rule transfer support is not direct validation of the methods that receive the rule.

## 7. Next stage / 다음 단계

The shared/common extraction stage is complete for the current registry. New development should now prioritize:

1. method-specific protocols for the less mature methods;
2. positive, negative/failure, boundary, and `NO_GAIN` cases;
3. method-appropriate reproducibility/retraceability records;
4. external/domain standards and real-world application evidence where applicable;
5. periodic boundary re-audits if a method definition changes.

Reopen shared-core extraction only if a source revision, new independent method, or new stable cross-method obligation cannot be represented by the current SC-01 through SC-10 registry.
