# DSD Method Family Registry / DSD 방법군 레지스트리

This directory adds the sixteen-method registry while preserving the repository's established Analysis and Audit paths.

| ID | Method | Korean | Status | Primary role |
|---|---|---|---|---|
| 01 | Analysis | DSD 분석론 | established | decompose and compare an existing target |
| 02 | Audit | DSD 감사 | established | retrace and evaluate procedure, evidence, and structural consistency |
| 03 | Specification | DSD 명세론 | proposed | state what must be declared, distinguished, and constrained |
| 04 | Design | DSD 설계론 | proposed | construct a target structure under explicit requirements |
| 05 | Synthesis | DSD 합성론 | proposed | compose admissible parts into candidate or realized wholes |
| 06 | Comparison | DSD 비교론 | developing | determine preserved structure and first branching |
| 07 | Classification | DSD 분류론 | proposed | classify structures by preserved distinctions and equivalence conditions |
| 08 | Transformation | DSD 변환론 | proposed | transform representations while recording what is preserved or lost |
| 09 | Provenance-Lineage | DSD 추적·계보론 | developing | track origin, succession, and evidence or object lineage |
| 10 | Aggregation-Compression | DSD 집계·압축론 | developing | reduce data while auditing support and reconstruction loss |
| 11 | Measurement | DSD 측정론 | proposed | design observations that distinguish relevant structural alternatives |
| 12 | Computation-Optimization | DSD 계산·최적화론 | proposed | prune unnecessary computation and allocate resources by structural relevance |
| 13 | Simulation | DSD 시뮬레이션론 | proposed | evolve admissible state trajectories and transitions |
| 14 | Control | DSD 제어론 | proposed | choose interventions that move a system toward declared target states |
| 15 | Diagnosis-Reconstruction | DSD 진단·복원론 | proposed | infer admissible hidden or prior structures from present evidence |
| 16 | Interpretation | DSD 해석론 | proposed | separate source, interpretive bridge, and resulting reading |

## Existing-path policy

- `01_analysis/` is a registry wrapper; the existing DSD Analysis corpus is not moved.
- `02_audit/` points to `../DSD_Audit/`; the dedicated audit module remains canonical.
- The other method directories begin as method definitions and roadmaps, not claims of mature standalone disciplines.
- The shared framework is [`../methodology/DSD_METHOD_FAMILY_FRAMEWORK.md`](../methodology/DSD_METHOD_FAMILY_FRAMEWORK.md).
- The current paper-facing layer lock remains [`../methodology/DSD_INTERFACE_PROFILE.md`](../methodology/DSD_INTERFACE_PROFILE.md).
