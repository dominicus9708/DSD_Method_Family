# DSD Method Family / DSD 방법군

This repository records the development and application of the **DSD Method Family**.
It grew from the existing **DSD Analysis** repository and preserves the established Analysis and Audit paths rather than migrating or rewriting them.

이 저장소는 **DSD 방법군**의 전개와 분야별 적용을 기록합니다.
기존 **DSD 분석론** 저장소에서 확장되었으며, 분석론·감사의 기존 기록과 경로를 이동하거나 소급 재작성하지 않고 새 방법군 구조를 추가합니다.

## Method-family extension / 방법군 확장

The registry is maintained under [`methods/`](methods/).
After refining compound entries and restoring roles omitted by the initial count, the repository now distinguishes **18 registry groups and 22 atomic methods**.
The common framework is maintained at [`methodology/DSD_METHOD_FAMILY_FRAMEWORK.md`](methodology/DSD_METHOD_FAMILY_FRAMEWORK.md).

Compatibility-preserving registry groups:

1. DSD Analysis / DSD 분석론
2. DSD Audit / DSD 감사
3. DSD Specification / DSD 명세론
4. DSD Design / DSD 설계론
5. DSD Synthesis / DSD 합성론
6. DSD Comparison / DSD 비교론
7. DSD Classification / DSD 분류론
8. DSD Transformation / DSD 변환론
9. DSD Provenance-Lineage / DSD 추적·계보론 — split into Provenance and Lineage
10. DSD Aggregation-Compression / DSD 집계·압축론 — split into Aggregation and Compression
11. DSD Measurement / DSD 측정론
12. DSD Computation-Optimization / DSD 계산·최적화론 — split into Computation and Optimization
13. DSD Simulation / DSD 시뮬레이션론
14. DSD Control / DSD 제어론
15. DSD Diagnosis-Reconstruction / DSD 진단·복원론 — split into Diagnosis and Reconstruction
16. DSD Interpretation / DSD 해석론
17. DSD Operation / DSD 운영론
18. DSD Prediction / DSD 예측론

Analysis and Audit are the two most mature current methods.
The remaining entries begin as proposed/developing frameworks and must earn stronger status through protocols, counterexamples, no-gain cases, reproducibility, and cross-domain tests.

## Repository role / 저장소의 역할

The method family selects only the DSD structures needed for the task from the current Formation, General Property, Static Aggregation, Dynamics, and optional specialization interfaces.
Its purpose is not to replace domain-specific proof, validation, interpretation, design, clinical, legal, engineering, artistic, or other professional standards.

DSD 방법군은 Formation, General Property, Static Aggregation, Dynamics 및 선택적 특수화를 하나의 고정 패키지로 강제하지 않습니다.
각 방법과 대상에 필요한 구조만 선택하며, 외부 분야의 고유 용어·검증기준·전문 판단을 DSD로 대체하지 않습니다.

## Existing Analysis and Audit / 기존 분석론·감사

Analysis and audit remain related but distinct.

- **DSD Analysis / DSD 분석론**: decomposes, compares, and reinterprets structures.
- **DSD Audit / DSD 감사**: retraces an analysis, calculation, judgment, or record under explicit scope, interface, evidence, procedure, and verdict rules.

An analysis result is not automatically an audit pass.
Audit methodology, templates, protocols, future algorithmization, and new audit records remain under [`DSD_Audit/`](DSD_Audit/).

The registry wrappers [`methods/01_analysis/`](methods/01_analysis/) and [`methods/02_audit/`](methods/02_audit/) point to these established locations; they are not migrations.

## Shared DSD interface / 공유 DSD 인터페이스

The current paper-facing DSD layer and status interface is maintained at:

- [`methodology/DSD_INTERFACE_PROFILE.md`](methodology/DSD_INTERFACE_PROFILE.md)

The method-family-level operating framework is maintained at:

- [`methodology/DSD_METHOD_FAMILY_FRAMEWORK.md`](methodology/DSD_METHOD_FAMILY_FRAMEWORK.md)

Realized-axis geometry is treated as an optional specialization of the general Property interface rather than as a universal property core.

## Current structure / 현재 구조

```text
DSD_Method_Family/
├─ README.md
├─ methodology/
│  ├─ DSD_INTERFACE_PROFILE.md
│  └─ DSD_METHOD_FAMILY_FRAMEWORK.md
├─ methods/
│  ├─ README.md
│  ├─ 01_analysis/
│  ├─ 02_audit/
│  ├─ 03_specification/
│  ├─ 04_design/
│  ├─ 05_synthesis/
│  ├─ 06_comparison/
│  ├─ 07_classification/
│  ├─ 08_transformation/
│  ├─ 09_provenance_lineage/
│  │  ├─ provenance/
│  │  └─ lineage/
│  ├─ 10_aggregation_compression/
│  │  ├─ aggregation/
│  │  └─ compression/
│  ├─ 11_measurement/
│  ├─ 12_computation_optimization/
│  │  ├─ computation/
│  │  └─ optimization/
│  ├─ 13_simulation/
│  ├─ 14_control/
│  ├─ 15_diagnosis_reconstruction/
│  │  ├─ diagnosis/
│  │  └─ reconstruction/
│  ├─ 16_interpretation/
│  ├─ 17_operation/
│  └─ 18_prediction/
├─ challenges/                        # existing analysis objectivity/consistency challenges
├─ DSD_Audit/                         # established separated audit module
│  ├─ README.md
│  ├─ methodology/
│  ├─ templates/
│  ├─ protocols/
│  └─ audits/
├─ audits/                             # legacy/historical audit records
├─ protocols/                          # existing paths preserved
└─ templates/                          # existing paths preserved
```

Older audit-methodology files and analysis records remain at previous repository paths for historical compatibility.
New method-family definitions are additive.

## Current DSD layer model / 현재 DSD 층위 모델

The shared interface distinguishes:

1. **Formation** — staged structural admission, partial assignment, operational-channel formation, and finite composition after post-Stage-VI term data are supplied.
2. **General Property** — typed property profiles, applicability, contextual prerequisites, and partial property assignments over a fixed Stage-VI formation background.
3. **Static Aggregation** — analytic realization of admitted channels plus an optional, separate typed-property aggregation interface.
4. **Dynamics** — component-resolved trajectories, regular epochs, transition classes, and lineage.
5. **Optional specializations** — realized-axis geometry and other additional structures when explicitly supplied.

These are not a mandatory serial chain.
A case records only the layers it actually uses.

## Method-family operating rules / 방법군 운영 규칙

- Preserve the external field's original terminology and validation standards.
- Do not infer structural identity from terminological similarity.
- Distinguish undefinedness, absence, inapplicability, and defined zero when the selected interface requires it.
- Do not infer a cross-layer bridge merely because names or coordinates resemble one another.
- Do not infer unique support, decomposition, cause, or historical reconstruction from aggregate equality without an applicable reconstruction basis.
- Preserve direct correspondence, partial correspondence, correspondence after explicit encoding, and non-correspondence.
- Record failed mappings, boundary cases, and `NO_GAIN` outcomes rather than collecting only DSD-favorable examples.
- Treat proposed methods as proposed until they have dedicated protocols, failure cases, and reproducible applications.

## Objectivity and consistency challenges / 객관성·일관성 도전

Dedicated adversarial and repeatability-oriented tests for DSD Analysis remain stored in [`challenges/`](challenges/).
These tests allow `PASS`, `FAIL`, `UNDETERMINED`, `NON_CORRESPONDENCE`, and `NO_ANALYTICAL_GAIN` outcomes without treating only DSD-favorable results as successful research.

The challenge corpus remains an important template for later method-family validation: every new method should eventually gain its own negative, boundary, and no-gain cases rather than inheriting validity from DSD Analysis automatically.

## Structural gravity logging / 구조적 중력 로그

Structural-gravity results developed in the project conversation remain recorded as a research-line log rather than being promoted automatically into general DSD Method Family methodology.

Legacy records currently remain under the historical `audits/science/` path.
When a structural-gravity case is newly re-audited, the new audit record should be created under `DSD_Audit/audits/science/` while preserving the legacy source path.

## Where to start / 활용 순서

### DSD Method Family / DSD 방법군

1. Read [`methods/README.md`](methods/README.md).
2. Read [`methodology/DSD_METHOD_FAMILY_FRAMEWORK.md`](methodology/DSD_METHOD_FAMILY_FRAMEWORK.md).
3. Select the task method or explicit combination of methods.
4. Lock the DSD layers and source versions actually used.
5. Supply the external-domain bridge and external standard separately.
6. Record results, losses, unresolved alternatives, and reproducibility information under the selected method.

### DSD Analysis / DSD 분석론

1. Read [`methodology/DSD_INTERFACE_PROFILE.md`](methodology/DSD_INTERFACE_PROFILE.md) when formal DSD layers matter.
2. Fix the analysis target and external-domain terminology.
3. Select only the DSD layers needed for the case.
4. Build structural correspondences without replacing external standards.
5. Preserve non-correspondence, alternatives, counterexamples, and boundary cases.
6. For objectivity/repeatability challenges, use [`challenges/`](challenges/).

### DSD Audit / DSD 감사

Use the separated audit module:

1. [`DSD_Audit/README.md`](DSD_Audit/README.md)
2. [`DSD_Audit/methodology/GENERAL_AUDIT_FRAMEWORK.md`](DSD_Audit/methodology/GENERAL_AUDIT_FRAMEWORK.md)
3. [`DSD_Audit/methodology/AUDIT_RECORDING_STANDARD.md`](DSD_Audit/methodology/AUDIT_RECORDING_STANDARD.md)
4. [`DSD_Audit/templates/AUDIT_CASE_TEMPLATE.md`](DSD_Audit/templates/AUDIT_CASE_TEMPLATE.md)
5. [`DSD_Audit/methodology/AUDIT_ALGORITHMIZATION_ROADMAP.md`](DSD_Audit/methodology/AUDIT_ALGORITHMIZATION_ROADMAP.md) for future software-assisted auditing.

## Historical record policy / 과거 기록 보존 원칙

Expanding DSD Analysis into the DSD Method Family does not retroactively rewrite older analysis or audit records.
Older paths, terminology, interface versions, and verdicts are preserved as historical states.
When a case is re-evaluated under a newer method-family definition, create a new record or explicit migration record and cross-link the previous path.
