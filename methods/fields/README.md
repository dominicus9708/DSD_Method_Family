# DSD Method Fields / DSD 방법 상위 분야

This directory classifies the **22 independent DSD methods** into eight higher-level fields.
The fields are navigation and research-organization categories only: they do **not** merge their member methods into a single method.

이 디렉터리는 **22개 독립 DSD 방법**을 8개 상위 분야로 분류합니다.
상위 분야는 탐색·연구관리용 분류이며, 소속 방법들을 하나의 합성 방법으로 취급하지 않습니다.

1. [`01_structural_understanding/`](01_structural_understanding/) — Structural Description & Understanding / 구조 기술·이해
2. [`02_criteria_validation/`](02_criteria_validation/) — Criteria & Validation / 기준·검증
3. [`03_construction_transformation/`](03_construction_transformation/) — Construction & Transformation / 구성·변환
4. [`04_evidence_lineage/`](04_evidence_lineage/) — Evidence & Lineage / 증거·계보
5. [`05_reduction_representation/`](05_reduction_representation/) — Reduction & Representation / 축약·표현
6. [`06_inverse_reconstruction/`](06_inverse_reconstruction/) — Inverse Inference & Reconstruction / 역추론·복원
7. [`07_computation_selection/`](07_computation_selection/) — Computation & Selection / 계산·선택
8. [`08_dynamics_action/`](08_dynamics_action/) — Dynamics & Action / 동역학·행동

## Boundary rule / 방법 경계 규칙

A single case may compose methods from multiple fields, but each method keeps its own inputs, operation, outputs, failure/no-gain criteria, validation standard, and audit record.

The current non-duplication audit is maintained at [`../METHOD_BOUNDARY_MATRIX.md`](../METHOD_BOUNDARY_MATRIX.md). It currently finds **0 exact duplicate methods** among the 22 definitions.

Common status, bridge, layer-selection, evidence, reconstruction, transition/lineage, baseline, and recording rules may later be extracted into shared infrastructure. Shared infrastructure does not merge the methods or validate them automatically. See [`../../methodology/SHARED_CORE_EXTRACTION_RULE.md`](../../methodology/SHARED_CORE_EXTRACTION_RULE.md).
