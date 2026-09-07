# DSD Specification Protocol v0.2 / DSD 명세론 전용 프로토콜 v0.2

Status: **developing / prospective current protocol for new runs**  
Date: 2026-09-07  
Method: **DSD Specification / DSD 명세론**  
Higher field: **II. Criteria & Validation / 기준·검증**

## 0. Revision boundary / 개정 경계

Protocol v0.2 is prospective.

It does **not** rewrite or rescore:

```text
SPEC-CH-001 through SPEC-CH-005
SPEC-APP-001
DSD-AUDIT-20260907-METHODOLOGY-001
```

Those records remain v0.1-era evidence under their original rules.

v0.2 incorporates two prospective refinements:

1. a **purpose / priority / detail / viewpoint guardrail ledger** accepted by `SPEC-CH-006`;
2. an optional `PRECEDENCE_OR_PRIORITY` field motivated by the nonfatal pressure observed in `SPEC-APP-001`.

Historical v0.1 remains at [`PROTOCOL.md`](PROTOCOL.md).

## 1. Method task / 방법 과제

DSD Specification converts a declared target, requirement source, and selected DSD interfaces into an explicit structural specification record that states what must be present, what may be optional, what distinctions must be preserved, which mappings are required, what outputs or transitions are admissible, and what counts as violation or unresolved specification.

It must also keep the **source's own purpose and viewpoint** separate from DSD-added structure.

A DSD derivative viewpoint is allowed, but it must be declared as derivative rather than attributed back to the source without evidence.

Core boundary:

```text
Specification
= declare requirements and admissibility constraints
  while preserving source/purpose/viewpoint boundaries

!= Audit
= evaluate performed work against requirements/evidence/procedure
```

## 2. Required input lock / 필수 입력 잠금

```text
SPECIFICATION_ID:
TARGET_SCOPE:
REQUIREMENT_SOURCE_SET:
SOURCE_VERSIONS:
DSD_INTERFACE_PROFILE_DATE:
SELECTED_DSD_LAYERS:
EXTERNAL_DOMAIN_IF_ANY:
EXTERNAL_STANDARD_IF_ANY:
REQUIREMENT_INVENTORY:
```

Completeness remains relative to the locked `REQUIREMENT_INVENTORY` unless a stronger external completeness basis is supplied.

## 3. Source-purpose / viewpoint lock / 원문 목적·관점 잠금

Before DSD atomization, record only what the source supports.

```text
SOURCE_PRIMARY_PURPOSE:
SOURCE_PURPOSE_EVIDENCE:
SOURCE_TARGET_USER_OR_ACTOR:
SOURCE_PRIMARY_ACTION_OR_DECISION:
SOURCE_PRIORITY_HIERARCHY:
SOURCE_COMMUNICATION_OR_USE_FUNCTION:
```

Allowed status values include:

```text
EXPLICITLY_STATED
STRONGLY_SUPPORTED_BY_SOURCE_STRUCTURE
UNDETERMINED
OUT_OF_SCOPE
```

Do not invent a purpose, audience, or authorial intent merely to complete the record.

If the DSD task intentionally changes viewpoint, record:

```text
TRANSFORMATION_PURPOSE:
VIEWPOINT_CHANGE_DECLARED: yes / no
DSD_ADDED_STRUCTURE:
DSD_ADDED_DETAIL:
DERIVATIVE_VIEW_LABEL:
```

## 4. DSD layer selection / DSD 층위 선택

```text
FORMATION_LAYER: used when formation structure is material
PROPERTY_CORE: used when typed properties/statuses are material
STATIC_AGGREGATION_LAYER: used only when aggregate/readout obligations are specified
DYNAMICS_LAYER: used only when evolution/transition/lineage obligations are specified
OPTIONAL_SPECIALIZATION: supplied only when a claim actually depends on it
```

No inactive layer is made mandatory merely because it exists in DSD.

## 5. Specification atom v0.2 / 명세 원자 v0.2

```text
REQUIREMENT_ID:
SOURCE_REFERENCE:
TARGET_ENTITY_OR_CARRIER:
REQUIREMENT_TYPE:
REQUIRED_OR_OPTIONAL:
ACTIVATION_CONDITION:
PRECEDENCE_OR_PRIORITY: optional
REQUIRED_STRUCTURE_OR_VALUE:
ALLOWED_ALTERNATIVES:
PROHIBITED_STATES:
DEPENDENCIES:
VALIDATION_STANDARD:
VIOLATION_CONDITION:
UNRESOLVED_CONDITION:
```

`PRECEDENCE_OR_PRIORITY` is optional. It is used only when the source or downstream task contains an ordered decision relation, precedence hierarchy, urgency relation, or similar priority structure.

Absence of this field is not an error when no such relation exists.

## 6. Status and typed-domain discipline / 상태·타입 도메인 규율

Claim-relevant statuses remain distinct.

Representative examples:

```text
channel_absent
!= admitted_channel_with_zero_term

undeclared
!= profile_unavailable
!= inapplicable
!= prerequisite_unsatisfied
!= applicable_but_undefined
!= defined_zero
!= defined_nonzero
```

Typed input order is preserved unless an explicit symmetry or quotient rule is supplied.

Shared rule: `SC-01` when activated.

## 7. Source/interface/version lock / 소스·인터페이스·버전 잠금

Every claim-relevant source, DSD interface, domain standard, and revision is locked before scoring.

Shared rule: `SC-02`.

## 8. Explicit bridge discipline / 명시적 브리지 규율

```text
BRIDGE_ID:
SOURCE_CARRIER:
TARGET_CARRIER:
MAP_OR_RELATION:
SELECTION_RULE_IF_ANY:
ASSUMPTIONS:
PRESERVED_STRUCTURE:
KNOWN_INFORMATION_LOSS:
```

Names or intuitive similarity do not create a bridge.

Shared rule: `SC-03`.

## 9. Aggregate / reconstruction discipline / 집계·복원 규율

When a reduced representation is permitted, specify preserved information, known loss, injectivity needs, and reconstruction limits.

Shared rule: `SC-05` when activated.

## 10. Transition / lineage discipline / 전이·계보 규율

When temporal identity or stage transitions matter, distinguish ordinary evolution from identity-breaking transition and record lineage if required.

Shared rule: `SC-06` when activated.

## 11. External-standard boundary / 외부 기준 경계

DSD structural success does not replace the receiving domain's validation authority.

```text
DOMAIN_CLAIM_IF_ANY:
EXTERNAL_DOMAIN:
EXTERNAL_STANDARD:
STANDARD_SOURCE_OR_AUTHORITY:
STANDARD_APPLICABILITY:
DOMAIN_BRIDGE:
```

Shared rule: `SC-10` when activated.

## 12. Guardrail ledger / 중심선 가드레일 기록

Guardrails are not automatic discard conditions.

They identify directional drift that can remain usable, become recoverable, or become distorted depending on severity and declaration.

### G1 — Source fidelity / 원문 충실도

Do not invent, silently delete, or strengthen source facts, requirements, normative force, or authorial intent.

### G2 — Purpose and priority fidelity / 목적·우선순위 충실도

Preserve the source's primary purpose, target user/action, and priority hierarchy when source-supported.

A changed purpose is allowed only as a declared derivative viewpoint.

### G3 — Detail proportionality / 디테일 비례성

Added detail is allowed when it serves the declared task.

Flag pressure when atomization, repeated typing, or auxiliary structure increases burden without corresponding operational value or obscures the primary source function.

### G4 — Viewpoint separation / 관점 분리

Keep source-stated structure separate from DSD-added structure, grouping, interpretation, or ontology.

Do not state that a source author intended a DSD ontology, hierarchy, or purpose unless the source supports that claim.

## 13. Guardrail status vocabulary / 가드레일 상태

```text
INSIDE_GUARDRAILS
GUARDRAIL_PRESSURE
GUARDRAIL_EXCEEDED_RECOVERABLE
PURPOSE_OR_VIEWPOINT_DISTORTED
UNDETERMINED
```

These statuses are recorded separately from hard specification status.

A representation may therefore be, for example:

```text
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
```

without contradiction.

## 14. Guardrail record / 가드레일 표준 기록

```text
SEMANTIC_CONTENT_PRESERVED:
SOURCE_PRIORITY_SEMANTICS_PRESERVED:
SOURCE_PRIORITY_PRESENTATION_PRESERVED:
SOURCE_PURPOSE_PRESERVED:
TARGET_USER_FUNCTION_PRESERVED:
DETAIL_INFLATION:
REPRESENTATION_BURDEN:
VIEWPOINT_CHANGE_DECLARED:
DSD_ADDED_STRUCTURE_DECLARED:
AUTHORIAL_INTENT_INFERRED_WITHOUT_BASIS:
PURPOSE_DISTORTION:
GUARDRAIL_VERDICT:
GUARDRAIL_REPAIR_IF_ANY:
```

If source purpose or audience is not established, record `UNDETERMINED` rather than inventing a value.

## 15. Hard failure vs guardrail deviation / 경성 실패와 가드레일 이탈

Hard failure and guardrail deviation are independent ledgers.

Representative hard failures remain:

```text
SOURCE_FACT_INVENTION
SILENT_REQUIRED_SOURCE_OMISSION
SPEC_CONTRADICTION
REQUIRED_BRIDGE_OMISSION
SPEC_WRONG_STANDARD
CLAIM_RELEVANT_STATUS_COLLAPSE
```

Representative guardrail deviations include:

```text
DETAIL_INFLATION
PRIORITY_FLATTENING_RISK
PURPOSE_FUNCTION_OBSCURED
UNDECLARED_PURPOSE_SHIFT
AUTHORIAL_INTENT_OVERATTRIBUTION
UNDECLARED_DSD_VIEWPOINT_SUBSTITUTION
```

A guardrail breach escalates to hard failure only when it also violates an existing hard rule, such as inventing source facts or creating unsupported mandatory obligations.

## 16. Construction procedure v0.2 / 구성 절차 v0.2

```text
STEP 1  lock target scope and requirement-source inventory
STEP 2  lock source purpose / audience / priority only to source-supported resolution
STEP 3  lock DSD source/interface/version dependencies
STEP 4  declare the DSD transformation purpose and any viewpoint change
STEP 5  atomize each requirement
STEP 6  type entities, inputs, statuses, prerequisites, and domains
STEP 7  preserve precedence/priority when active
STEP 8  separate required dependencies from optional interfaces
STEP 9  declare bridges and external standards where needed
STEP 10 declare aggregate/reconstruction obligations when reduction is used
STEP 11 declare transition/lineage obligations when temporal identity is used
STEP 12 declare allowed, prohibited, violation, and unresolved conditions
STEP 13 run hard-failure checks
STEP 14 run G1-G4 guardrail checks
STEP 15 record final specification status and separate guardrail verdict
STEP 16 record reproducibility trace
```

## 17. Core specification checks / 핵심 명세 검사

Existing v0.1 checks remain:

```text
S1 type completeness relative to locked inventory
S2 status distinguishability
S3 dependency explicitness
S4 bridge explicitness
S5 violation semantics
S6 contradiction detection
S7 optional-interface restraint
S8 external-standard separation
```

v0.2 adds:

```text
S9 source-purpose evidence lock
S10 precedence/priority preservation when active
S11 declared viewpoint-change separation
S12 detail proportionality / primary-function preservation
```

## 18. Method-specific outcomes / 방법 고유 결과

Existing outcomes remain:

```text
SPEC_CONTRADICTION
SPEC_UNDERSPECIFIED
SPEC_OVERCONSTRAINED
SPEC_WRONG_STANDARD
SPEC_NO_GAIN
```

`SPEC_NO_GAIN` remains a valid non-failure result.

Guardrail outcomes do not replace these method-specific outcomes.

## 19. Output record v0.2 / 산출 기록 v0.2

```text
SPECIFICATION_RESULT_ID:
SPECIFICATION_PROTOCOL_VERSION: v0.2
TARGET_SCOPE:
LOCKED_REQUIREMENT_INVENTORY:
SOURCE_PURPOSE_LOCK:
TRANSFORMATION_PURPOSE:
REQUIREMENT_ATOMS:
SELECTED_DSD_LAYERS:
STATUS_DISTINCTIONS_REQUIRED:
BRIDGES_REQUIRED:
EXTERNAL_STANDARDS_REQUIRED:
AGGREGATE_RECONSTRUCTION_OBLIGATIONS:
TRANSITION_LINEAGE_OBLIGATIONS:
CONTRADICTIONS_FOUND:
UNDERSPECIFIED_ITEMS:
OVERCONSTRAINTS_FOUND:
NO_GAIN_STATUS:
HARD_FAILURES:
GUARDRAIL_RECORD:
FINAL_SPEC_STATUS:
  usable
  usable_with_unresolved_items
  contradictory
  underspecified
  no_gain
GUARDRAIL_VERDICT:
  INSIDE_GUARDRAILS
  GUARDRAIL_PRESSURE
  GUARDRAIL_EXCEEDED_RECOVERABLE
  PURPOSE_OR_VIEWPOINT_DISTORTED
  UNDETERMINED
LIMITS:
REPRODUCIBILITY_RECORD:
```

## 20. Validation standard / 검증 기준

Protocol-level validation asks whether the specification record:

1. faithfully represents the locked requirement inventory;
2. preserves required type/status/dependency/bridge distinctions;
3. preserves source-supported purpose and priority or explicitly declares a derivative purpose;
4. keeps DSD-added viewpoint separate from source intent;
5. records detail/representation burden without automatically treating all burden as failure;
6. remains reproducibly retraceable.

External-domain correctness remains under the external domain standard.

No global completeness or universal utility theorem is claimed.

## 21. Reproducibility / 재현성

```text
PROTOCOL_VERSION: v0.2
SOURCE_SET_AND_VERSIONS:
REQUIREMENT_INVENTORY_HASH_OR_ID:
SOURCE_PURPOSE_EVIDENCE:
INTERFACE_PROFILE_DATE:
ATOMIZATION_RULE_VERSION:
GUARDRAIL_PROFILE_VERSION: G1-G4/v0.2
ORDER_OF_PROCESSING_IF_RELEVANT:
MANUAL_JUDGMENT_POINTS:
UNRESOLVED_SOURCE_CONFLICTS:
OUTPUT_RECORD_ID:
```

## 22. Evidence state / 증거 상태

```text
v0.1 direct evidence:
  SPEC-CH-001 through SPEC-CH-005
  SPEC-APP-001

v0.2 guardrail transition evidence:
  SPEC-CH-006
    RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS

v0.2 external evidence:
  not yet established

METHOD_STATUS:
  developing
```

Next direct application: `SPEC-APP-002`, using a less-structured external corpus with purpose, audience, priority, viewpoint, and detail-burden guardrails locked before DSD transformation.
