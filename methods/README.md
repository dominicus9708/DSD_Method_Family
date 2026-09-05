# DSD Method Family Registry / DSD 방법군 레지스트리

This directory preserves the initial 01–16 registry while refining compound entries into atomic methods and restoring method roles that were omitted by the initial count.

현재 구조는 **18개 registry group / 22개 atomic method**로 관리합니다.
기존 01–16 경로는 호환성을 위해 유지하고, 복합 항목은 하위 방법으로 세분화합니다.

## Registry groups / 레지스트리 그룹

| ID | Registry group | Korean | Status | Atomic structure |
|---|---|---|---|---|
| 01 | Analysis | DSD 분석론 | established | 01 Analysis |
| 02 | Audit | DSD 감사 | established | 02 Audit |
| 03 | Specification | DSD 명세론 | proposed | 03 Specification |
| 04 | Design | DSD 설계론 | proposed | 04 Design |
| 05 | Synthesis | DSD 합성론 | proposed | 05 Synthesis |
| 06 | Comparison | DSD 비교론 | developing | 06 Comparison |
| 07 | Classification | DSD 분류론 | proposed | 07 Classification |
| 08 | Transformation | DSD 변환론 | proposed | 08 Transformation |
| 09 | Provenance-Lineage | DSD 추적·계보론 | developing umbrella | 09A Provenance + 09B Lineage |
| 10 | Aggregation-Compression | DSD 집계·압축론 | developing umbrella | 10A Aggregation + 10B Compression |
| 11 | Measurement | DSD 측정론 | proposed | 11 Measurement |
| 12 | Computation-Optimization | DSD 계산·최적화론 | proposed umbrella | 12A Computation + 12B Optimization |
| 13 | Simulation | DSD 시뮬레이션론 | proposed | 13 Simulation |
| 14 | Control | DSD 제어론 | proposed | 14 Control |
| 15 | Diagnosis-Reconstruction | DSD 진단·복원론 | proposed umbrella | 15A Diagnosis + 15B Reconstruction |
| 16 | Interpretation | DSD 해석론 | proposed | 16 Interpretation |
| 17 | Operation | DSD 운영론 | proposed | 17 Operation |
| 18 | Prediction | DSD 예측론 | proposed | 18 Prediction |

## Atomic method count / 원자적 방법 22개

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

## Functional families / 기능별 상위 분류

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

## Existing-path policy / 기존 경로 보존

- `01_analysis/` is a registry wrapper; the existing DSD Analysis corpus is not moved.
- `02_audit/` points to `../DSD_Audit/`; the dedicated audit module remains canonical.
- Compound paths `09_provenance_lineage/`, `10_aggregation_compression/`, `12_computation_optimization/`, and `15_diagnosis_reconstruction/` remain as compatibility umbrellas and now contain atomic submethods.
- `17_operation/` restores the operation/lifecycle method that was omitted from the initial count.
- `18_prediction/` separates prediction from simulation because a model-consistent trajectory is not automatically an empirically relevant forecast.
- Proposed methods are definitions and roadmaps, not claims of mature standalone disciplines.
- The shared framework is [`../methodology/DSD_METHOD_FAMILY_FRAMEWORK.md`](../methodology/DSD_METHOD_FAMILY_FRAMEWORK.md).
- The current paper-facing layer lock remains [`../methodology/DSD_INTERFACE_PROFILE.md`](../methodology/DSD_INTERFACE_PROFILE.md).

## Representative navigation policy / 대표 바로가기 정책

- **DSD Analysis** and **DSD Audit** are retained as the two representative entry points because they are the most mature and historically established methods.
- Their compatibility/navigation wrappers remain explicit under `01_analysis/` and `02_audit/`.
- No equivalent shortcut or duplicate compatibility entry is added for methods 03–18 merely for symmetry.
- Newer methods are discovered through this registry and their canonical method directories, avoiding unnecessary duplicate navigation paths.
