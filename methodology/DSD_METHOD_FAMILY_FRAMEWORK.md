# DSD Method Family Framework / DSD 방법군 공통 프레임

Status: working framework
Framework date: 2026-09-06

This document organizes the DSD Method Family derived from the Formation Axiom System, General Property Axiom System, Channel-Indexed Static Aggregation, Structural Reorganization Dynamics, and explicit optional specializations.

이 문서는 형성공리계, 속성공리계, 채널별 정적 집계, 구조 재구성 동역학 및 명시적 선택 특수화에서 파생되는 DSD 사용 방식을 공통 방법군으로 정리합니다.

## 1. Preservation rule / 기존 구조 보존 원칙

- Existing DSD Analysis and DSD Audit records remain valid historical and operational records.
- Existing `DSD_Audit/`, `audits/`, `challenges/`, `methodology/`, `protocols/`, and `templates/` paths are preserved.
- New classification material is additive under `methods/fields/`.
- Historical paths are not silently rewritten when a method is refined or reclassified.
- Earlier compound 09/10/12/15 paths are retained only for compatibility and are not counted as current methods.

## 2. Shared DSD source layers / 공통 DSD 기반 층위

A method uses only the layers required by its task.

1. **Formation** — admission, restriction, realization, partial assignment, operational-channel formation, finite composition interface.
2. **General Property** — typed profiles, applicability, contextual prerequisites, partial property assignments, status distinctions.
3. **Static Aggregation** — channel-indexed analytic realization, finite aggregation, optional typed-property aggregation, information-loss and reconstruction conditions.
4. **Dynamics** — component-resolved trajectories, regular epochs, transition classes, lineage, dynamic bridges.
5. **Optional specializations** — realized-axis geometry or any additional domain-specific structure supplied explicitly.

The current paper-facing interface lock remains in `DSD_INTERFACE_PROFILE.md`.

## 3. Current method architecture / 현재 방법 구조

The current conceptual architecture is:

```text
DSD foundational layers
-> 8 higher-level method fields
-> 22 independent methods
-> explicit cross-method application cases
```

The higher-level fields are organizational categories only.
They do not merge member methods, inherit results across methods, or create a new method merely by grouping names together.

현재 개념적 정본은 **8개 상위 분야 / 22개 독립 방법**입니다.
상위 분야는 분류·탐색·연구관리용이며, 소속 방법의 입력·연산·산출물·실패 조건·검증기준을 합치지 않습니다.

## 4. Eight higher-level fields / 8개 상위 분야

### I. Structural Description & Understanding / 구조 기술·이해
- Analysis / DSD 분석론
- Comparison / DSD 비교론
- Classification / DSD 분류론
- Interpretation / DSD 해석론

### II. Criteria & Validation / 기준·검증
- Specification / DSD 명세론
- Audit / DSD 감사

### III. Construction & Transformation / 구성·변환
- Design / DSD 설계론
- Synthesis / DSD 합성론
- Transformation / DSD 변환론

### IV. Evidence & Lineage / 증거·계보
- Measurement / DSD 측정론
- Provenance / DSD 출처·유래 추적론
- Lineage / DSD 계보론

### V. Reduction & Representation / 축약·표현
- Aggregation / DSD 집계론
- Compression / DSD 압축론

### VI. Inverse Inference & Reconstruction / 역추론·복원
- Diagnosis / DSD 진단론
- Reconstruction / DSD 복원론

### VII. Computation & Selection / 계산·선택
- Computation / DSD 계산론
- Optimization / DSD 최적화론

### VIII. Dynamics & Action / 동역학·행동
- Simulation / DSD 시뮬레이션론
- Prediction / DSD 예측론
- Control / DSD 제어론
- Operation / DSD 운영론

Total: **22 independent methods**.

## 5. Independence rule / 방법 독립성 규칙

Two methods remain distinct when their task interfaces differ materially in inputs, operation, outputs, failure modes, or validation criteria.

Important distinctions include:

- **Provenance ≠ Lineage**: provenance records origin/derivation; lineage records predecessor-successor identity across change.
- **Aggregation ≠ Compression**: aggregation constructs a readout or representative value; compression intentionally removes representation subject to retained-distinction requirements.
- **Computation ≠ Optimization**: computation determines required evaluation; optimization selects among admissible alternatives under explicit objectives and constraints.
- **Diagnosis ≠ Reconstruction**: diagnosis infers present hidden states or causes; reconstruction infers prior, omitted, damaged, or compressed structures or histories.
- **Simulation ≠ Prediction**: simulation evolves model-consistent states; prediction makes a claim about a future target and requires appropriate empirical/domain validation.
- **Control ≠ Operation**: control chooses interventions; operation manages repeated lifecycle, resources, monitoring, execution, and handoff.
- **Specification ≠ Audit**: specification declares requirements or criteria; audit evaluates compliance, evidence, procedure, and structural consistency against relevant standards.

A field classification never licenses inference from one method result to another without an explicit bridge.

## 6. Common method record / 공통 방법 기록 형식

Every method definition should state at least:

```text
METHOD_NAME:
HIGHER_FIELD:
STATUS: established / developing / proposed / experimental
TASK:
INPUTS:
DSD_LAYERS_USED:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
OPERATION:
OUTPUTS:
FAILURE_OR_NO_GAIN_CRITERIA:
INFORMATION_LOSS_CHECK:
LINEAGE_OR_TRANSITION_CHECK:
LIMITS:
REPRODUCIBILITY_RECORD:
```

Numeric or A/B labels may be retained in paths for historical compatibility, but the method name and field are the conceptual identifiers.

## 7. Domain-bridge rule / 분야별 브리지 원칙

DSD does not replace a field's own proof, validation, interpretation, professional, empirical, ethical, or safety standards.

A domain application therefore has the form:

```text
DSD structural layer
+ selected independent method(s)
+ explicit domain bridge
+ domain-specific standard
-> method-specific result(s)
```

A mathematical proof remains mathematical proof; a medical judgment remains subject to medical evidence and clinical standards; a historical interpretation remains subject to source criticism; an artistic interpretation is not reduced to a scalar aggregate merely because selected features can be encoded.

## 8. Status and bridge discipline / 상태·브리지 규율

Across the method family:

- preserve absence, undefinedness, inapplicability, prerequisite failure, and defined zero when the selected interface distinguishes them;
- do not infer cross-layer mappings from terminology alone;
- do not infer structural identity from aggregate equality without reconstruction conditions;
- preserve failed mappings, alternative mappings, and `NO_GAIN` results;
- when dynamics is used, distinguish value evolution from status/domain and formation-level transitions;
- use explicit lineage when successor identity is not inherited automatically;
- do not treat membership in the same higher-level field as evidence of method equivalence.

## 9. Method composition / 방법 조합

The methods are composable but not a mandatory pipeline.
Typical combinations include:

```text
Specification -> Design -> Synthesis -> Audit
Analysis -> Comparison -> Classification
Measurement -> Provenance -> Lineage
Aggregation -> Compression
Diagnosis -> Reconstruction
Computation -> Optimization
Simulation -> Prediction -> Control -> Operation
Interpretation -> Comparison -> Audit
```

A case may combine methods from several fields, but each intermediate and final result should remain attributable to the method that produced it.

## 10. Legacy compatibility / 기존 복합 경로 호환성

The following directories remain as historical navigation wrappers only:

- `09_provenance_lineage/` → Provenance + Lineage
- `10_aggregation_compression/` → Aggregation + Compression
- `12_computation_optimization/` → Computation + Optimization
- `15_diagnosis_reconstruction/` → Diagnosis + Reconstruction

These wrapper names are not current method names and are not included in the count of 22 methods.

## 11. Development policy / 개발 정책

- Analysis and Audit are the two most mature current methods and retain their established corpora.
- Comparison, Provenance, Lineage, and Aggregation have comparatively direct support in current DSD formal structures but still require dedicated method-level protocols.
- Proposed methods should be promoted only after concrete protocols, counterexamples, boundary cases, `NO_GAIN` cases, reproducibility records, and cross-domain tests accumulate.
- Similarity to an existing external methodology is not novelty by itself.
- The intended contribution is a shared DSD structural layer plus explicitly separable method roles and cross-method interoperability, not a claim to replace all disciplinary methods.
