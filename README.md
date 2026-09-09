# DSD Method Family / DSD 방법군

This repository records the development and application of the **DSD Method Family**.
It grew from the existing DSD Analysis work and preserves established Analysis, Audit, challenge, methodology, protocol, and historical record paths rather than rewriting them for cosmetic consistency.

이 저장소는 **DSD 방법군**의 전개와 분야별 적용을 기록합니다.
기존 DSD 분석론에서 확장되었으며, 분석론·감사·도전·방법론·프로토콜·과거 기록은 외형적 통일을 위해 소급 재작성하지 않습니다.

## Current architecture / 현재 구조

```text
DSD foundational layers
-> 8 higher-level method fields
-> 22 independent methods
-> 10-rule shared core
-> explicit cross-method application cases
```

현재 개념적 정본은 **8개 상위 분야 / 22개 독립 방법 / SC-01~SC-10 공통 코어**입니다.
상위 분야는 분류와 탐색을 위한 조직 단위일 뿐, 소속 방법들을 하나의 방법으로 합치지 않습니다.

- Field index: [`methods/fields/`](methods/fields/)
- Independent-method registry: [`methods/README.md`](methods/README.md)
- Method independence/boundary audit: [`methods/METHOD_BOUNDARY_MATRIX.md`](methods/METHOD_BOUNDARY_MATRIX.md)
- Common framework: [`methodology/DSD_METHOD_FAMILY_FRAMEWORK.md`](methodology/DSD_METHOD_FAMILY_FRAMEWORK.md)
- Shared-core extraction rule: [`methodology/SHARED_CORE_EXTRACTION_RULE.md`](methodology/SHARED_CORE_EXTRACTION_RULE.md)
- Shared-core closure audit: [`evidence/shared/SHARED_CORE_CLOSURE_AUDIT.md`](evidence/shared/SHARED_CORE_CLOSURE_AUDIT.md)
- Current DSD interface profile: [`methodology/DSD_INTERFACE_PROFILE.md`](methodology/DSD_INTERFACE_PROFILE.md)
- Evidence applicability registry: [`evidence/`](evidence/)

## Eight higher-level fields / 8개 상위 분야

1. **Structural Description & Understanding / 구조 기술·이해** — Analysis, Comparison, Classification, Interpretation
2. **Criteria & Validation / 기준·검증** — Specification, Audit
3. **Construction & Transformation / 구성·변환** — Design, Synthesis, Transformation
4. **Evidence & Lineage / 증거·계보** — Measurement, Provenance, Lineage
5. **Reduction & Representation / 축약·표현** — Aggregation, Compression
6. **Inverse Inference & Reconstruction / 역추론·복원** — Diagnosis, Reconstruction
7. **Computation & Selection / 계산·선택** — Computation, Optimization
8. **Dynamics & Action / 동역학·행동** — Simulation, Prediction, Control, Operation

The total remains **22 independent methods**.

## Repository role / 저장소의 역할

The method family selects only the DSD structures required for a task from Formation, General Property, Static Aggregation, Dynamics, and explicit optional specializations.
It does not replace domain-specific proof, empirical validation, interpretation, engineering standards, clinical standards, legal standards, artistic judgment, or other disciplinary methods.

A domain application should be recorded as:

```text
DSD structural layer
+ selected independent method(s)
+ explicit domain bridge
+ domain-specific standard
-> method-specific result(s)
```

The separation between DSD-internal success and the receiving domain's validation standard is now explicitly tested as **SC-10**.

## Existing Analysis and Audit / 기존 분석론·감사

Analysis and Audit remain related but distinct and are currently the two most mature methods.

- **DSD Analysis / DSD 분석론**: decomposes and structurally re-expresses one declared target.
- **DSD Audit / DSD 감사**: retraces analysis, calculation, judgment, evidence, procedure, bridge use, and verdict rules under an explicit scope and standard.

Under the current method-family boundary, cross-target structural comparison is recorded under **DSD Comparison**, criterion-based class assignment under **DSD Classification**, and source/context interpretive reading under **DSD Interpretation**. Historical Analysis records that combine these operations are preserved without retroactive rewriting.

An analysis result is not automatically an audit pass.
The dedicated Audit corpus remains under [`DSD_Audit/`](DSD_Audit/).

## Method independence and shared core / 방법 독립성과 공통 구조

The current duplication audit found **no exact duplicate among the 22 methods** when comparing:

```text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
```

Methods may share DSD layers, status rules, bridge machinery, aggregation/reconstruction checks, transition/lineage checks, evidence discipline, baseline rules, domain-validation boundaries, or recording procedures without becoming the same method.

The shared-core extraction stage is now **closed for the current registry with conditions**. The current core contains SC-01 through SC-10. The closure audit reviewed all 45 unordered shared-rule pairs, found no exact duplicate shared rules, confirmed representative transfer coverage across all eight higher-level fields for every SC, and preserved the separation between shared-rule support and direct method validation.

The specialization-restraint pattern is retained as a derived profile of SC-01/03/04 rather than a duplicate independent shared rule. `REPRODUCIBILITY_RECORD` remains a method/evidence maturity requirement because concrete rerun/retrace obligations differ by method.

## Current repository layout / 현재 저장소 배치

```text
DSD_Method_Family/
├─ README.md
├─ methodology/
│  ├─ DSD_INTERFACE_PROFILE.md
│  ├─ DSD_METHOD_FAMILY_FRAMEWORK.md
│  └─ SHARED_CORE_EXTRACTION_RULE.md
├─ methods/
│  ├─ README.md
│  ├─ METHOD_BOUNDARY_MATRIX.md
│  ├─ fields/
│  │  ├─ README.md
│  │  ├─ 01_structural_understanding/
│  │  ├─ 02_criteria_validation/
│  │  ├─ 03_construction_transformation/
│  │  ├─ 04_evidence_lineage/
│  │  ├─ 05_reduction_representation/
│  │  ├─ 06_inverse_reconstruction/
│  │  ├─ 07_computation_selection/
│  │  └─ 08_dynamics_action/
│  ├─ 01_analysis/
│  ├─ 02_audit/
│  ├─ 03_specification/
│  ├─ 04_design/
│  ├─ 05_synthesis/
│  ├─ 06_comparison/
│  ├─ 07_classification/
│  ├─ 08_transformation/
│  ├─ 09_provenance_lineage/        # legacy wrapper only
│  │  ├─ provenance/                 # independent method
│  │  └─ lineage/                    # independent method
│  ├─ 10_aggregation_compression/    # legacy wrapper only
│  │  ├─ aggregation/                # independent method
│  │  └─ compression/                # independent method
│  ├─ 11_measurement/
│  ├─ 12_computation_optimization/   # legacy wrapper only
│  │  ├─ computation/                # independent method
│  │  └─ optimization/               # independent method
│  ├─ 13_simulation/
│  ├─ 14_control/
│  ├─ 15_diagnosis_reconstruction/   # legacy wrapper only
│  │  ├─ diagnosis/                  # independent method
│  │  └─ reconstruction/             # independent method
│  ├─ 16_interpretation/
│  ├─ 17_operation/
│  └─ 18_prediction/
├─ evidence/
│  ├─ README.md
│  ├─ CURRENT_EVIDENCE_APPLICABILITY_MATRIX.md
│  ├─ shared/
│  │  ├─ SC-01_...md through SC-10_...md
│  │  ├─ SPECIALIZATION_RESTRAINT_DUPLICATION_AUDIT.md
│  │  └─ SHARED_CORE_CLOSURE_AUDIT.md
│  ├─ method_specific/
│  └─ real_world_cases/
├─ challenges/
├─ DSD_Audit/
├─ audits/                            # legacy/historical audit records
├─ protocols/
└─ templates/
```

## Legacy compatibility / 기존 경로 호환성

The combined labels `Provenance-Lineage`, `Aggregation-Compression`, `Computation-Optimization`, and `Diagnosis-Reconstruction` are no longer treated as methods.
Their directories remain only because deleting or renaming them would break existing links and records.

개념적으로는 각각 독립된 방법이며, 기존 복합 경로명은 **호환성용 묶음**으로만 남깁니다.
Numeric and A/B labels are path identifiers rather than claims of theoretical dependence.

## Shared DSD interface / 공유 DSD 인터페이스

The paper-facing DSD layer/status interface is maintained at [`methodology/DSD_INTERFACE_PROFILE.md`](methodology/DSD_INTERFACE_PROFILE.md).
A case records only the layers it actually uses.

Current common layers are:

1. **Formation** — staged admission, partial assignment, operational-channel formation, and composition interface.
2. **General Property** — typed property profiles, applicability, prerequisites, partial assignments, and status distinctions.
3. **Static Aggregation** — analytic channel realization, aggregation, and information-loss/reconstruction conditions.
4. **Dynamics** — component-resolved trajectories, transition classes, regular epochs, and lineage.
5. **Optional specializations** — additional geometric or domain-specific structure when explicitly supplied.

## Method-family operating rules / 방법군 운영 규칙

The current shared-core registry is:

```text
SC-01  preserve claim-relevant DSD status/type distinctions
SC-02  lock claim-relevant source/interface/version semantics
SC-03  make claim-relevant cross-structure mappings explicit
SC-04  use sufficient dependencies without optional-interface overconstraint
SC-05  respect information-loss and reconstruction limits
SC-06  separate regular evolution, transition, and lineage
SC-07  separate evidence applicability from case origin
SC-08  preserve evaluation integrity, failures, NO_GAIN, and precommit boundaries
SC-09  separate evidence/audit status from DSD object/model status
SC-10  keep external-domain validation standards distinct from DSD-internal success
```

These rules are conditionally activated by the task/interface. They do not force unused layers, external standards for purely DSD-internal claims, competitive baselines for purely descriptive work, or lineage for static records.

## Objectivity and consistency challenges / 객관성·일관성 도전

Adversarial and repeatability-oriented tests for DSD Analysis remain under [`challenges/`](challenges/).
Their discipline is also a template for later methods: every method should eventually acquire negative, boundary, no-gain, and reproducibility cases rather than inheriting validity from another method.

## Evidence applicability / 증거 적용성

Validation evidence is separated by **scope** and **case origin**.

- [`evidence/shared/`](evidence/shared/) records support for reusable method-family disciplines. Shared support does not directly validate all 22 methods.
- [`evidence/method_specific/`](evidence/method_specific/) defines direct evidence requirements for each independent method.
- [`evidence/real_world_cases/`](evidence/real_world_cases/) is reserved for actual events, judicial cases, historical incidents, personal cases, empirical datasets, and documented organizational or technical incidents.
- [`evidence/CURRENT_EVIDENCE_APPLICABILITY_MATRIX.md`](evidence/CURRENT_EVIDENCE_APPLICABILITY_MATRIX.md) maps the existing Analysis/Audit corpus into the current method-family scope without retroactive rewriting.

`EVIDENCE_SCOPE_CLASS` and `CASE_ORIGIN` are separate fields. A real-world judicial case, for example, may directly test DSD Audit while only conditionally supporting shared bridge or evidence-status rules.

Existing `ANL-CH-*` records remain direct Analysis evidence. Existing `DSD_Audit/` records remain direct Audit evidence. Lessons extracted from either corpus may support shared rules, but they do not automatically validate another independent method.

## Where to start / 활용 순서

1. Read [`methods/fields/README.md`](methods/fields/README.md) to select a higher-level field.
2. Read [`methods/README.md`](methods/README.md) and [`methods/METHOD_BOUNDARY_MATRIX.md`](methods/METHOD_BOUNDARY_MATRIX.md) to select the independent method or explicit method combination.
3. Lock the DSD source layers and versions actually used.
4. Apply the relevant SC-01 through SC-10 rules only when their activation conditions are present.
5. Supply the domain bridge and external standard separately when an external-domain claim is made.
6. Classify the evidence scope and case origin using [`evidence/`](evidence/).
7. Record method-specific results, information loss, unresolved alternatives, transition/lineage obligations, and reproducibility information.
8. Audit the result separately when an audit claim is needed.

The shared-core extraction stage should be reopened only under the conditions listed in [`evidence/shared/SHARED_CORE_CLOSURE_AUDIT.md`](evidence/shared/SHARED_CORE_CLOSURE_AUDIT.md). Otherwise development should proceed to method-specific protocols, evidence, and real-world cases.

## Historical record policy / 과거 기록 보존 원칙

Reclassification does not retroactively rewrite earlier analysis or audit records.
If an older case is revisited under the current eight-field / 22-method architecture, create a new record or explicit migration note and cross-link the historical path.
