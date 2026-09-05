# DSD Method Family Framework / DSD 방법군 공통 프레임

Status: working framework
Framework date: 2026-09-06

This document extends the existing DSD Analysis and DSD Audit repository into a broader **DSD Method Family** without relocating or rewriting established historical paths.

이 문서는 기존 DSD 분석론과 DSD 감사의 경로·기록을 보존하면서, Formation Axiom System, General Property Axiom System, Channel-Indexed Static Aggregation, Structural Reorganization Dynamics 및 선택적 특수화에서 파생되는 여러 사용 방식을 하나의 **DSD 방법군**으로 정리하기 위한 공통 프레임입니다.

## 1. Preservation rule / 기존 구조 보존 원칙

- Existing `DSD_Audit/`, `audits/`, `challenges/`, `methodology/`, `protocols/`, and `templates/` paths are preserved.
- Existing DSD Analysis records remain valid historical and operational records.
- New method-family material is added under `methods/`.
- `methods/01_analysis/` and `methods/02_audit/` are registry wrappers pointing to the established locations rather than migrations of the existing corpora.
- Historical paths are not silently rewritten when a method is later generalized.
- The initial 01–16 numbering is frozen for compatibility; refinements are added as atomic submethods or appended registry groups.

## 2. Shared DSD source layers / 공통 DSD 기반 층위

A method may use only the layers actually required by its task.

1. **Formation** — admission, restriction, realization, partial assignment, operational-channel formation, finite composition interface.
2. **General Property** — typed profiles, applicability, contextual prerequisites, partial property assignments, status distinctions.
3. **Static Aggregation** — channel-indexed analytic realization, finite aggregation, optional typed-property aggregation, information-loss and reconstruction conditions.
4. **Dynamics** — component-resolved trajectories, regular epochs, transition classes, lineage, dynamic bridges.
5. **Optional specializations** — realized-axis geometry or any domain-specific structure supplied explicitly.

The current paper-facing interface lock remains in `DSD_INTERFACE_PROFILE.md`.

## 3. Registry groups and atomic methods / 레지스트리 그룹과 원자적 방법

The initial registry incorrectly compressed several distinct roles. To preserve compatibility without erasing that history, the framework now distinguishes **18 registry groups** and **22 atomic methods**.

```text
01  Analysis / 분석
02  Audit / 감사
03  Specification / 명세
04  Design / 설계
05  Synthesis / 합성
06  Comparison / 비교
07  Classification / 분류
08  Transformation / 변환
09A Provenance / 출처·유래 추적
09B Lineage / 계보
10A Aggregation / 집계
10B Compression / 압축
11  Measurement / 측정
12A Computation / 계산
12B Optimization / 최적화
13  Simulation / 시뮬레이션
14  Control / 제어
15A Diagnosis / 진단
15B Reconstruction / 복원
16  Interpretation / 해석
17  Operation / 운영
18  Prediction / 예측
```

Compatibility umbrellas remain at:

- `09_provenance_lineage/` → 09A Provenance + 09B Lineage
- `10_aggregation_compression/` → 10A Aggregation + 10B Compression
- `12_computation_optimization/` → 12A Computation + 12B Optimization
- `15_diagnosis_reconstruction/` → 15A Diagnosis + 15B Reconstruction

`17_operation/` restores the lifecycle/operation method omitted by the initial count.
`18_prediction/` is separate from Simulation because generating model-consistent trajectories is not the same as asserting a future-target prediction.

## 4. Functional families / 기능별 상위 분류

The atomic methods may also be grouped by role. These groups are organizational aids, not mandatory pipelines.

### A. Descriptive and evaluative / 기술·평가
- Analysis
- Audit
- Specification
- Comparison
- Classification
- Interpretation

### B. Constructive and transformative / 구성·변환
- Design
- Synthesis
- Transformation

### C. Evidence, trace, and inverse / 증거·추적·역문제
- Provenance
- Lineage
- Measurement
- Diagnosis
- Reconstruction

### D. Reduction and computation / 축약·계산
- Aggregation
- Compression
- Computation
- Optimization

### E. Dynamic and operational / 동역학·운영
- Simulation
- Prediction
- Control
- Operation

## 5. Distinction rules for the newly split methods / 세분화 방법의 구분 규칙

- **Provenance ≠ Lineage**: provenance records origin/derivation; lineage records predecessor–successor identity across change.
- **Aggregation ≠ Compression**: aggregation constructs a summary/readout; compression intentionally reduces representation subject to retained-distinction requirements.
- **Computation ≠ Optimization**: computation determines what and how to evaluate; optimization selects among admissible alternatives under an explicit objective and constraints.
- **Diagnosis ≠ Reconstruction**: diagnosis infers present hidden states/causes; reconstruction infers prior, omitted, damaged, or compressed structure/history.
- **Simulation ≠ Prediction**: simulation evolves states under a model; prediction adds a claim about a future target and therefore requires empirical/domain validation.
- **Control ≠ Operation**: control chooses interventions toward target states; operation coordinates a live/repeated lifecycle, resources, handoffs, monitoring, and method composition.

These distinctions are preserved even when one application uses several methods together.

## 6. Common method record / 공통 방법 기록 형식

Every method definition should state at least:

```text
METHOD_ID:
METHOD_NAME:
STATUS: established / developing / proposed / experimental
TASK:
INPUTS:
DSD_LAYERS_USED:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
OPERATION:
OUTPUTS:
INFORMATION_LOSS_CHECK:
LINEAGE_OR_TRANSITION_CHECK:
LIMITS:
REPRODUCIBILITY_RECORD:
```

## 7. Domain-bridge rule / 분야별 브리지 원칙

DSD does not replace a field's own proof, validation, interpretation, professional, empirical, ethical, or safety standards.

A domain application therefore has the form

```text
DSD structural layer
+ explicit domain bridge
+ domain-specific standard
-> method result
```

A mathematical proof remains mathematical proof; a medical judgment remains subject to medical evidence and clinical standards; a historical interpretation remains subject to source criticism; an artistic interpretation is not reduced to a scalar aggregate merely because DSD can encode selected features.

## 8. Status and bridge discipline / 상태·브리지 규율

Across the method family:

- preserve absence, undefinedness, inapplicability, prerequisite failure, and defined zero when the selected interface distinguishes them;
- do not infer cross-layer mappings from terminology alone;
- do not infer structural identity from aggregate equality without reconstruction conditions;
- preserve failed mappings, alternative mappings, and `NO_GAIN` results;
- when dynamics is used, distinguish value evolution from status/domain and formation-level transitions;
- use explicit lineage when successor identity is not inherited automatically.

## 9. Relationship among the methods / 방법 간 관계

The methods are not a mandatory pipeline. Typical combinations include:

```text
Specification -> Design -> Synthesis -> Audit
Analysis -> Comparison -> Classification
Provenance -> Interpretation -> Comparison
Lineage -> Diagnosis -> Reconstruction
Aggregation -> Compression -> Computation -> Optimization
Measurement -> Analysis -> Audit
Simulation -> Prediction -> Control -> Operation -> Audit
Interpretation -> Comparison -> Audit
```

A case may use one method alone or compose several methods, but each method result should remain separately identifiable.

## 10. Development policy / 개발 정책

- Analysis and Audit are the two most mature current methods and retain their established locations.
- Comparison, Provenance, Lineage, and Aggregation have comparatively direct support in the current DSD formal layers but still require dedicated method-level protocols.
- The remaining methods begin as explicit proposed frameworks and should be promoted only after concrete protocols, counterexamples, no-gain cases, and cross-domain tests are accumulated.
- Similarity to an existing external methodology is not treated as novelty by itself.
- The intended contribution is a shared DSD structural layer and interoperability among method roles, not a claim to replace all existing disciplinary methods.
