# DSD Method Family Registry / DSD 방법군 레지스트리

The current conceptual registry contains **22 independent methods classified into eight higher-level fields**.
The fields are organizational categories only and do not merge their member methods.

현재 개념적 정본은 **8개 상위 분야 / 22개 독립 방법**입니다.
상위 분야는 분류·탐색·연구관리용이며, 소속 방법의 입력·연산·출력·검증 기준을 합치지 않습니다.

See [`fields/`](fields/) for the field indexes.

## Eight fields and 22 independent methods / 8개 상위 분야와 22개 독립 방법

### I. Structural Description & Understanding / 구조 기술·이해
- **Analysis / DSD 분석론** — [`01_analysis/`](01_analysis/)
- **Comparison / DSD 비교론** — [`06_comparison/`](06_comparison/)
- **Classification / DSD 분류론** — [`07_classification/`](07_classification/)
- **Interpretation / DSD 해석론** — [`16_interpretation/`](16_interpretation/)

### II. Criteria & Validation / 기준·검증
- **Specification / DSD 명세론** — [`03_specification/`](03_specification/)
- **Audit / DSD 감사** — [`02_audit/`](02_audit/)

### III. Construction & Transformation / 구성·변환
- **Design / DSD 설계론** — [`04_design/`](04_design/)
- **Synthesis / DSD 합성론** — [`05_synthesis/`](05_synthesis/)
- **Transformation / DSD 변환론** — [`08_transformation/`](08_transformation/)

### IV. Evidence & Lineage / 증거·계보
- **Measurement / DSD 측정론** — [`11_measurement/`](11_measurement/)
- **Provenance / DSD 출처·유래 추적론** — [`09_provenance_lineage/provenance/`](09_provenance_lineage/provenance/)
- **Lineage / DSD 계보론** — [`09_provenance_lineage/lineage/`](09_provenance_lineage/lineage/)

### V. Reduction & Representation / 축약·표현
- **Aggregation / DSD 집계론** — [`10_aggregation_compression/aggregation/`](10_aggregation_compression/aggregation/)
- **Compression / DSD 압축론** — [`10_aggregation_compression/compression/`](10_aggregation_compression/compression/)

### VI. Inverse Inference & Reconstruction / 역추론·복원
- **Diagnosis / DSD 진단론** — [`15_diagnosis_reconstruction/diagnosis/`](15_diagnosis_reconstruction/diagnosis/)
- **Reconstruction / DSD 복원론** — [`15_diagnosis_reconstruction/reconstruction/`](15_diagnosis_reconstruction/reconstruction/)

### VII. Computation & Selection / 계산·선택
- **Computation / DSD 계산론** — [`12_computation_optimization/computation/`](12_computation_optimization/computation/)
- **Optimization / DSD 최적화론** — [`12_computation_optimization/optimization/`](12_computation_optimization/optimization/)

### VIII. Dynamics & Action / 동역학·행동
- **Simulation / DSD 시뮬레이션론** — [`13_simulation/`](13_simulation/)
- **Prediction / DSD 예측론** — [`18_prediction/`](18_prediction/)
- **Control / DSD 제어론** — [`14_control/`](14_control/)
- **Operation / DSD 운영론** — [`17_operation/`](17_operation/)

## Classification rule / 분류 원칙

A higher-level field is not a method by itself.
For example, Aggregation and Compression are both in Reduction & Representation, but an aggregation result is not automatically a compression result.
Likewise Simulation, Prediction, Control, and Operation remain separate even when one application uses all four.

상위 분야는 하나의 합성 방법이 아닙니다.
세분화·독립성의 기준은 이름이 아니라 **입력, 수행 연산, 산출물, 실패 조건, 검증 기준이 독립적으로 달라지는가**입니다.

A case may combine methods from several fields, but every method result must remain separately identifiable and auditable.

## Legacy path compatibility / 기존 경로 호환성

The earlier 01–18 path layout is preserved so that existing links and records do not break.
The following compound directories are **legacy compatibility wrappers only and are not counted as methods**:

- `09_provenance_lineage/` → Provenance + Lineage
- `10_aggregation_compression/` → Aggregation + Compression
- `12_computation_optimization/` → Computation + Optimization
- `15_diagnosis_reconstruction/` → Diagnosis + Reconstruction

Their nested method directories are the independent methods.
The historical numeric/A-B labels remain path identifiers, not a claim that paired methods form one methodology.

## Existing-path policy / 기존 구조 보존

- `01_analysis/` remains a registry wrapper for the historically established DSD Analysis corpus.
- `02_audit/` remains the registry entry for the dedicated `../DSD_Audit/` module.
- Existing audit, challenge, methodology, protocol, and template paths are not migrated merely to match the new classification.
- New field indexes are additive under [`fields/`](fields/).
- Proposed methods remain proposed until they acquire dedicated protocols, counterexamples, no-gain cases, reproducibility records, and cross-domain tests.

The shared framework is [`../methodology/DSD_METHOD_FAMILY_FRAMEWORK.md`](../methodology/DSD_METHOD_FAMILY_FRAMEWORK.md), and the current paper-facing layer lock remains [`../methodology/DSD_INTERFACE_PROFILE.md`](../methodology/DSD_INTERFACE_PROFILE.md).
