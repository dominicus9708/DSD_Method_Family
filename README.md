# DSD Method Family / DSD 방법군

This repository records the development and application of the **DSD Method Family**.
It grew from the existing DSD Analysis work and preserves established Analysis, Audit, challenge, methodology, protocol, and historical record paths rather than rewriting them for cosmetic consistency.

이 저장소는 **DSD 방법군**의 전개와 분야별 적용을 기록합니다.
기존 DSD 분석론에서 확장되었으며, 분석론·감사·도전·방법론·프로토콜·과거 기록은 외형적 통일을 위해 소급 재작성하지 않습니다.

## Current architecture / 현재 구조

The current conceptual registry is:

```text
DSD foundational layers
-> 8 higher-level method fields
-> 22 independent methods
-> explicit cross-method application cases
```

현재 개념적 정본은 **8개 상위 분야 / 22개 독립 방법**입니다.
상위 분야는 분류와 탐색을 위한 조직 단위일 뿐, 소속 방법들을 하나의 방법으로 합치지 않습니다.

- Field index: [`methods/fields/`](methods/fields/)
- Independent-method registry: [`methods/README.md`](methods/README.md)
- Common framework: [`methodology/DSD_METHOD_FAMILY_FRAMEWORK.md`](methodology/DSD_METHOD_FAMILY_FRAMEWORK.md)
- Current DSD interface profile: [`methodology/DSD_INTERFACE_PROFILE.md`](methodology/DSD_INTERFACE_PROFILE.md)

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

## Existing Analysis and Audit / 기존 분석론·감사

Analysis and Audit remain related but distinct and are currently the two most mature methods.

- **DSD Analysis / DSD 분석론**: decomposes, compares, and structurally re-expresses a target.
- **DSD Audit / DSD 감사**: retraces analysis, calculation, judgment, evidence, procedure, bridge use, and verdict rules under an explicit scope and standard.

An analysis result is not automatically an audit pass.
The dedicated Audit corpus remains under [`DSD_Audit/`](DSD_Audit/).

## Current repository layout / 현재 저장소 배치

```text
DSD_Method_Family/
├─ README.md
├─ methodology/
│  ├─ DSD_INTERFACE_PROFILE.md
│  └─ DSD_METHOD_FAMILY_FRAMEWORK.md
├─ methods/
│  ├─ README.md
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

- Preserve the external field's original terminology and validation standards.
- Do not infer structural identity from terminological similarity.
- Distinguish undefinedness, absence, inapplicability, prerequisite failure, and defined zero when the selected interface requires it.
- Do not infer a cross-layer bridge from names alone.
- Do not infer support, decomposition, cause, or unique reconstruction from aggregate equality without an applicable reconstruction basis.
- Preserve failed mappings, boundary cases, alternatives, and `NO_GAIN` outcomes.
- Do not infer method equivalence merely because two methods belong to the same higher-level field.
- Treat proposed methods as proposed until they have dedicated protocols, failure cases, and reproducible applications.

## Objectivity and consistency challenges / 객관성·일관성 도전

Adversarial and repeatability-oriented tests for DSD Analysis remain under [`challenges/`](challenges/).
Their discipline is also a template for later methods: every method should eventually acquire negative, boundary, no-gain, and reproducibility cases rather than inheriting validity from another method.

## Where to start / 활용 순서

1. Read [`methods/fields/README.md`](methods/fields/README.md) to select a higher-level field.
2. Read [`methods/README.md`](methods/README.md) and select the independent method or explicit method combination.
3. Lock the DSD source layers and versions actually used.
4. Supply the domain bridge and external standard separately.
5. Record method-specific results, information loss, unresolved alternatives, transition/lineage obligations, and reproducibility information.
6. Audit the result separately when an audit claim is needed.

## Historical record policy / 과거 기록 보존 원칙

Reclassification does not retroactively rewrite earlier analysis or audit records.
If an older case is revisited under the current eight-field / 22-method architecture, create a new record or explicit migration note and cross-link the historical path.
