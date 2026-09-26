# DSD Audit Case Template / DSD 감사 실행 템플릿

> Copy this file for each individual audit. Unknown fields must remain `UNDETERMINED` or `OUT_OF_SCOPE` rather than being forced into a positive or negative result.

---

## 0. Identity / 식별

```text
AUDIT_ID:
TITLE:
DOMAIN:
DATE:
AUDITOR_OR_AGENT:
RELATED_SOURCE_OR_CASE:
METHODOLOGY_VERSION:
DSD_INTERFACE_PROFILE_DATE:
```

## 1. DSD interface lock / DSD 인터페이스 잠금

```text
FORMATION_LAYER: used / not used
PROPERTY_CORE: used / not used
STATIC_AGGREGATION_LAYER: used / not used
DYNAMICS_LAYER: used / not used
REALIZED_AXIS_SPECIALIZATION: supplied / not supplied
OTHER_SPECIALIZATION:
SOURCE_VERSIONS:
```

## 2. Audit question / 감사 질문

```text
PRIMARY_QUESTION:
QUESTIONS_NOT_BEING_DECIDED:
```

## 3. Scope / 범위

```text
TARGET_SCOPE:
TIME_SCOPE:
DESCRIPTIVE_RESOLUTION:
INCLUDED_MATERIAL:
EXCLUDED_MATERIAL:
EXTERNAL_STANDARD:
ASSUMPTIONS:
```

## 3A. Optional claim-requirement relation / 선택: 주장-요구조건 관계

Use only when intermediate requirement strength is material.

```text
DECLARED_CLAIM:
ACTIVE_REQUIREMENT_AXES:
INTERMEDIATE_REQUIREMENT:
RELATION_TO_DECLARED_CLAIM:
IMPLICATION_OR_PRESERVATION_BASIS:
```

## 4. Original source preservation / 원자료 보존

```text
SOURCE_CLAIM:
SOURCE_DEFINITION:
SOURCE_PROCEDURE:
SOURCE_DATA_OR_EVIDENCE:
SOURCE_VERSION:
SOURCE_DATE:
SOURCE_REFERENCE:
```

## 5. Evidence status / 증거 상태

### Established within scope / 범위 내 확인
- 

### Undetermined or insufficient / 미정·불충분
- 

### Out of scope / 범위 밖
- 

## 6. DSD object status / DSD 객체 상태

```text
FORMATION_STATUS:
PROPERTY_STATUS:
STATIC_ANALYTIC_STATUS:
DYNAMIC_STATUS:
STATUS_SIDE_INFORMATION:
```

## 7. Selection and exclusion / 선택·배제

```text
AVAILABLE_OPTIONS:
SELECTED_OPTION:
SELECTION_RULE:
EXCLUDED_OPTIONS:
EXCLUSION_REASONS:
POST_HOC_CHANGE_CHECK:
```

## 8. Bridge declarations / 브리지 선언

```text
BRIDGE_NAME:
BRIDGE_SOURCE_LAYER:
BRIDGE_DOMAIN:
BRIDGE_CODOMAIN:
BRIDGE_ASSUMPTIONS:
BRIDGE_JUSTIFICATION:
IMPLICIT_BRIDGE_CHECK:
```

Add more bridge blocks as needed.

## 9. Proposition layers / 명제 층위

### Fact
- 

### Inference
- 

### Norm
- 

### Decision
- 

## 10. Transition and lineage audit / 전이·lineage 감사

| Step | Prior state/evidence | Transition class | Rule/reason | Next state/conclusion | Identity preserved? | Lineage | Status |
|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |

Suggested status values:

```text
JUSTIFIED
CONDITIONALLY_JUSTIFIED
UNSUPPORTED
CONTRADICTED
UNDETERMINED
```

## 11. Alternative describabilities / 대안 기술가능성

```text
ALTERNATIVE_1:
COMPATIBILITY_BASIS:
EVIDENCE_AGAINST:
EXCLUDED?:
EXCLUSION_BASIS:
ADDITIONAL_INFORMATION_NEEDED:
```

## 11A. Optional dependency/frontier ledger / 선택: 의존성·전선 장부

Use only when several material routes exist or a frontier/progress claim is audited.

```text
AND_PREREQUISITES:
OR_SUFFICIENT_ROUTES:
COMMON_MANDATORY_GATES:
MINIMAL_FRONTIER_FAMILIES:
ATTACK_METHODS:
SUPPORTING_WORK:
FROZEN_BRANCHES:
REOPEN_CONDITIONS:
```

## 12. Aggregation and reconstruction / 집계·복원

```text
OUTPUT_EQUALITY_CHECK:
SUPPORT_EQUALITY_CHECK:
DECOMPOSITION_RETENTION_CHECK:
INJECTIVITY_ESTABLISHED:
COLLISION_WITNESS:
KERNEL_OR_INFORMATION_LOSS_CHECK:
RECONSTRUCTION_CLAIM:
REPRESENTATION_RELATION:
REPRESENTATION_PRESERVATION_BASIS:
CLAIM_STRENGTH_ESCALATION:
ESCALATION_BASIS:
CLAIM_RELEVANT_INFORMATION_LOSS:
MERGE_OR_DEDUPLICATION_BASIS:
```

## 13. Witnesses and counterexamples / 증인·반례

```text
MINIMAL_POSITIVE_WITNESS:
MINIMAL_COUNTEREXAMPLE:
BOUNDARY_CASE:
FINITE_EXHAUSTIVE_RANGE:
UNTESTED_REGION:
```

## 14. Contradiction audit / 모순 감사

```text
DEFINITION_CONTRADICTION:
TRANSITION_CONTRADICTION:
STRUCTURAL_CONTRADICTION:
CLAIM_CONTRADICTION_OR_OVERREACH:
OMISSION:
```

## 15. Eight-axis summary / 8축 요약

| Axis | Audit result / 감사 결과 |
|---|---|
| D — Describability | |
| R — Resolution | |
| S — Selection | |
| E — Exclusion | |
| T — Transition | |
| C — Consistency | |
| N — Norm | |
| O — Outcome | |

## 16. Final verdict / 최종 판정

```text
VERDICT:
VERDICT_BASIS:
MAXIMUM_SUPPORTED_CLAIM:
UNSUPPORTED_OR_UNRESOLVED_CLAIMS:
EXTERNAL_DOMAIN_VERDICT:
DSD_STRUCTURAL_AUDIT_VERDICT:
CORRESPONDENCE_AND_LIMITS:
```

Default verdict vocabulary:

```text
CONFIRMED
CONDITIONALLY_CONFIRMED
PARTIALLY_CONFIRMED
UNDETERMINED
INSUFFICIENT_BASIS
EXCLUSION_ERROR
TRANSITION_ERROR
NORM_CONFLATION
CONTRADICTION
OVERCLAIM
```

## 17. Reproducibility and traceability / 재현·추적

```text
REQUIRED_SOURCES:
REVIEW_OR_EXECUTION_ORDER:
REPOSITORY_AND_PATH:
COMMIT_SHA:
ENVIRONMENT:
DEPENDENCIES:
INPUTS:
RANDOM_SEED:
TOLERANCE:
GENERATED_OUTPUTS:
RELATED_NOTION_PAGE:
```

## 18. Follow-up / 후속

- [ ] Obtain additional material
- [ ] Independent review
- [ ] Expand counterexample search
- [ ] Compare with domain protocol
- [ ] Reflect in synthesis or paper preparation

## 19. Revision and migration log / 개정·마이그레이션

```text
REVISION_DATE:
PREVIOUS_DSD_INTERFACE_PROFILE:
CURRENT_DSD_INTERFACE_PROFILE:
CHANGED_SCOPE:
NEW_SOURCE:
MIGRATION_STATUS:
LEGACY_TERMINOLOGY:
CHANGED_VERDICT:
REASON:
```
