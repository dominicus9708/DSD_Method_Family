# DSD Audit Recording Standard / DSD 감사 기록 표준

## 1. Purpose / 목적

This document defines how DSD audits are recorded so that another reviewer can reconstruct the path without relying on conversational memory.
The record must preserve both the path that led to the verdict and materially rejected alternatives.

## 2. Record identity / 기록 식별

Recommended ID:

```text
DSD-AUDIT-YYYYMMDD-DOMAIN-NNN
```

Record at minimum:

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

## 3. Interface and source lock / 인터페이스·출처 잠금

When DSD formal layers materially affect the case, record:

```text
FORMATION_LAYER: used / not used
PROPERTY_CORE: used / not used
STATIC_AGGREGATION_LAYER: used / not used
DYNAMICS_LAYER: used / not used
REALIZED_AXIS_SPECIALIZATION: supplied / not supplied
OTHER_SPECIALIZATION:
SOURCE_VERSIONS:
```

The shared interface profile is maintained at `../../methodology/DSD_INTERFACE_PROFILE.md`.

## 4. Scope lock / 범위 잠금

Record before evaluating:

- target object
- audit question
- included material
- excluded material
- time range
- descriptive resolution
- external standard
- assumptions

If scope changes, append the change rather than silently editing the original scope.

### 4.1 Optional claim-requirement relation / 선택: 주장-요구조건 관계

Use when intermediate requirements materially differ.

```text
DECLARED_CLAIM:
ACTIVE_REQUIREMENT_AXES:
INTERMEDIATE_REQUIREMENT:
RELATION_TO_DECLARED_CLAIM:
IMPLICATION_OR_PRESERVATION_BASIS:
```

Allowed relation vocabulary:

```text
REQUIRED_MATCH
PROVEN_STRONGER_SUFFICIENT
CONDITIONAL_STRONGER_SUFFICIENT
WEAKER_INSUFFICIENT
INCOMPARABLE
RELATION_UNDETERMINED
```

## 5. Source preservation / 원자료 보존

```text
SOURCE_CLAIM
SOURCE_DEFINITION
SOURCE_PROCEDURE
SOURCE_DATA
SOURCE_VERSION
SOURCE_DATE
SOURCE_REFERENCE
```

## 6. Evidence-status ledger / 증거 상태 장부

```text
ESTABLISHED_WITHIN_SCOPE
UNDETERMINED_OR_INSUFFICIENT
OUT_OF_SCOPE
```

## 7. DSD object-status ledger / DSD 객체 상태 장부

Keep separate ledgers for the DSD layers actually used.
Do not merge evidence status with Formation, Property, Static, or Dynamics object status.

Examples include:

```text
FORMATION_STATUS:
PROPERTY_STATUS:
DYNAMIC_STATUS:
```

Preserve distinctions such as undefined, absent, inapplicable, prerequisite-unsatisfied, defined zero, and defined nonzero where they matter.

## 8. Selection and exclusion ledger / 선택·배제 장부

```text
AVAILABLE_OPTIONS
SELECTED_OPTION
SELECTION_RULE
EXCLUDED_OPTIONS
EXCLUSION_REASONS
POST_HOC_CHANGE_CHECK
```

## 9. Bridge ledger / 브리지 장부

For each material cross-layer or external mapping:

```text
BRIDGE_NAME:
BRIDGE_SOURCE_LAYER:
BRIDGE_DOMAIN:
BRIDGE_CODOMAIN:
BRIDGE_ASSUMPTIONS:
BRIDGE_JUSTIFICATION:
IMPLICIT_BRIDGE_CHECK:
```

Multi-input property data, analytic realization, and constitutive dynamic mappings must not be assigned automatically from names alone.

## 10. Transition and lineage ledger / 전이·lineage 장부

| Step | Prior state / evidence | Transition class | Rule or reason | Next state / conclusion | Identity preserved? | Lineage | Status |
|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |

Recommended transition classes:

```text
DOWNSTREAM_VALUE_EVOLUTION
PROPERTY_ASSIGNMENT_EVOLUTION
PROPERTY_STATUS_OR_DOMAIN_TRANSITION
OPTIONAL_GEOMETRIC_SPECIALIZATION_TRANSITION
CHANNEL_OR_FORMATION_LEVEL_TRANSITION
```

## 11. Proposition-layer ledger / 명제 층위 장부

| ID | Statement | Layer | Source / basis |
|---|---|---|---|
| P1 |  | Fact / Inference / Norm / Decision |  |

## 12. Alternative-possibility ledger / 대안 가능성 장부

For each alternative, record:

- description
- compatibility basis
- evidence against
- whether excluded
- exclusion rule
- information required for exclusion

### 12.1 Optional dependency/frontier ledger / 선택: 의존성·전선 장부

Use only when several material routes exist or the audited object itself makes a frontier/progress claim.

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

## 13. Aggregation and reconstruction ledger / 집계·복원 장부

When a reduced output or summary is used:

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

Suggested optional representation vocabulary:

```text
IDENTICAL
BIJECTIVE_EXACT
ISOMETRIC_OR_PARSEVAL_EQUIVALENT
FIXED_WEIGHT_EQUIVALENT
PROJECTION
CONTRACTION
COARSENING
ONE_WAY_BOUND
SIBLING_CONTRACTIONS
INDEPENDENT
UNKNOWN
```

If source-to-target mapping is itself the primary task, Transformation remains the primary method; Audit checks the performed mapping or claim.

## 14. Witness and counterexample record / 증인·반례 기록

```text
MINIMAL_POSITIVE_WITNESS:
MINIMAL_COUNTEREXAMPLE:
BOUNDARY_CASE:
FINITE_EXHAUSTIVE_RANGE:
UNTESTED_REGION:
```

Finite computation remains finite unless a separate argument establishes generality.

## 15. Contradiction audit / 모순 감사

Check at least:

1. definition contradiction
2. transition contradiction
3. structural contradiction
4. claim contradiction / overreach
5. omission

## 16. Eight-axis summary / 8축 요약

| Axis | Summary |
|---|---|
| D — Describability | |
| R — Resolution | |
| S — Selection | |
| E — Exclusion | |
| T — Transition | |
| C — Consistency | |
| N — Norm | |
| O — Outcome | |

## 17. Verdict discipline / 판정 규율

```text
VERDICT
VERDICT_BASIS
MAXIMUM_SUPPORTED_CLAIM
UNSUPPORTED_OR_UNRESOLVED_CLAIMS
EXTERNAL_DOMAIN_VERDICT
DSD_STRUCTURAL_AUDIT_VERDICT
CORRESPONDENCE_AND_LIMITS
```

## 18. Reproducibility and traceability / 재현·추적

For computational/procedural audits record where applicable:

- repository and path
- commit SHA
- environment
- dependencies
- inputs
- random seed
- numerical tolerance
- execution order
- generated outputs

For non-computational audits record source set, dates, passages, classification rules, decision rules, and unresolved material.

## 19. Revision and migration log / 개정·마이그레이션 기록

The optional fields introduced by later Audit methodology revisions are prospective and additive. Historical audit records are not invalidated solely because they predate those fields.

Never overwrite a historical verdict silently.

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
