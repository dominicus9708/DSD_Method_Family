# DSD Specification Protocol v0.2.1 / DSD 명세론 전용 프로토콜 v0.2.1

Status: **developing / current protocol for new runs**  
Date: 2026-09-07  
Method: **DSD Specification / DSD 명세론**  
Higher field: **II. Criteria & Validation / 기준·검증**

## 0. Revision boundary / 개정 경계

Protocol v0.2.1 is a prospective minor revision of v0.2.

It does **not** rewrite or rescore:

```text
SPEC-CH-001 through SPEC-CH-005      # v0.1-era
SPEC-APP-001                         # v0.1
SPEC-CH-006                          # v0.2 guardrail-transition evidence
SPEC-APP-002                         # v0.2 external Belmont application
DSD-AUDIT-20260907-METHODOLOGY-001   # first maturity audit
```

Historical protocols remain:

```text
PROTOCOL.md        -> v0.1
PROTOCOL_v0.2.md   -> v0.2
```

v0.2.1 adds only the distinction validated prospectively by `SPEC-CH-007`:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

No shared-core rule is added.

## 1. Method task / 방법 과제

DSD Specification declares what entities, statuses, inputs, prerequisites, dependencies, bridges, outputs, transitions, admissible alternatives, and violation/unresolved conditions a target must preserve under a locked source inventory and selected DSD interfaces.

It also preserves the boundary between:

- source content and DSD-added structure;
- source purpose and derivative DSD purpose;
- source-supported priority and DSD presentation;
- intentional source openness and accidental missing information;
- source resolution and downstream-task determinacy.

Specification remains distinct from Audit, Design, and Analysis.

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
DECLARED_DOWNSTREAM_TASK:
```

Completeness is relative to the locked requirement inventory and declared downstream task unless a stronger domain completeness basis is supplied.

## 3. Source purpose / viewpoint lock / 원문 목적·관점 잠금

```text
SOURCE_PRIMARY_PURPOSE:
SOURCE_PURPOSE_EVIDENCE:
SOURCE_TARGET_USER_OR_ACTOR:
SOURCE_PRIMARY_ACTION_OR_DECISION:
SOURCE_PRIORITY_HIERARCHY:
SOURCE_COMMUNICATION_OR_USE_FUNCTION:

TRANSFORMATION_PURPOSE:
VIEWPOINT_CHANGE_DECLARED: yes / no
DSD_ADDED_STRUCTURE:
DSD_ADDED_DETAIL:
DERIVATIVE_VIEW_LABEL:
```

Allowed purpose-evidence statuses include:

```text
EXPLICITLY_STATED
STRONGLY_SUPPORTED_BY_SOURCE_STRUCTURE
UNDETERMINED
OUT_OF_SCOPE
```

Do not invent authorial intent, source purpose, or audience merely to fill a field.

## 4. Source openness axis / 원문 개방성 축

This axis asks **what the source itself supports** about determinacy, discretion, and openness.

```text
SOURCE_OPENNESS_STATUS:
  SOURCE_DETERMINATE
  SOURCE_INTENTIONAL_OPENNESS
  OPENNESS_INTENT_UNDETERMINED
  NOT_APPLICABLE
```

### SOURCE_DETERMINATE

The source supplies a determinate value, rule, admissible set, selector, or procedure at the resolution relevant to the claim.

A range or finite set can be fully determinate when the source intentionally defines the whole set as admissible.

### SOURCE_INTENTIONAL_OPENNESS

Use only when source evidence supports that contextual judgment, bounded discretion, balancing, professional judgment, or an open choice is intentionally preserved.

Intentional openness must not be inferred merely from missing information.

### OPENNESS_INTENT_UNDETERMINED

The source leaves a point unresolved but available evidence does not justify classifying the gap as either deliberate openness or accidental omission.

Preserve this state rather than inventing source intent.

## 5. Downstream determinacy axis / 하위 과제 결정가능성 축

This axis asks whether the locked source resolution is **sufficient for the declared downstream task**.

```text
DOWNSTREAM_DETERMINACY_STATUS:
  SUFFICIENT_AT_DECLARED_RESOLUTION
  UNDERDETERMINED_FOR_DECLARED_TASK
  NOT_APPLICABLE
```

The two axes are independent.

A valid joint state is:

```text
SOURCE_OPENNESS_STATUS: SOURCE_INTENTIONAL_OPENNESS
DOWNSTREAM_DETERMINACY_STATUS: UNDERDETERMINED_FOR_DECLARED_TASK
```

For example, a source may intentionally delegate bounded professional judgment while an attempted fully automated downstream task demands a unique answer that the source does not provide.

## 6. Relation to `SPEC_UNDERSPECIFIED` / 미명세 판정과의 관계

`SPEC_UNDERSPECIFIED` remains a **task-relative Specification outcome**.

It activates when the declared downstream task requires a target/type/status/dependency/bridge/selector/actor/threshold/violation condition that is not sufficiently determined at the locked source resolution.

Therefore:

```text
SOURCE_INTENTIONAL_OPENNESS
!= immunity from SPEC_UNDERSPECIFIED
```

and:

```text
SPEC_UNDERSPECIFIED
!= proof that the source accidentally failed
```

An intentionally open source can be sufficient for a human judgment/review task and insufficient for a stronger deterministic automation task.

## 7. Specification atom v0.2.1 / 명세 원자

```text
REQUIREMENT_ID:
SOURCE_REFERENCE:
TARGET_ENTITY_OR_CARRIER:
REQUIREMENT_TYPE:
REQUIRED_OR_OPTIONAL:
ACTIVATION_CONDITION:
PRECEDENCE_OR_PRIORITY: optional
SOURCE_OPENNESS_STATUS: optional_when_claim_relevant
DOWNSTREAM_DETERMINACY_STATUS: optional_when_claim_relevant
REQUIRED_STRUCTURE_OR_VALUE:
ALLOWED_ALTERNATIVES:
PROHIBITED_STATES:
DEPENDENCIES:
VALIDATION_STANDARD:
VIOLATION_CONDITION:
UNRESOLVED_CONDITION:
```

The new fields are activated only when openness/determinacy is material to the claim or downstream task.

## 8. DSD layer and bridge discipline / 층위·브리지 규율

Use only required DSD interfaces.

```text
FORMATION_LAYER: used when formation structure is material
PROPERTY_CORE: used when typed property/status structure is material
STATIC_AGGREGATION_LAYER: used only for aggregate/readout obligations
DYNAMICS_LAYER: used only for evolution/transition/lineage obligations
OPTIONAL_SPECIALIZATION: supplied only when claim-dependent
```

Cross-carrier/layer/domain mappings require explicit bridges. Names or intuitive similarity do not create mappings.

## 9. Guardrail ledger / 중심선 가드레일

The v0.2 guardrails remain unchanged:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

Guardrail verdicts remain separate from hard failure:

```text
INSIDE_GUARDRAILS
GUARDRAIL_PRESSURE
GUARDRAIL_EXCEEDED_RECOVERABLE
PURPOSE_OR_VIEWPOINT_DISTORTED
UNDETERMINED
```

Extra detail or derivative viewpoint change is not automatically failure.

## 10. Hard failures / 경성 실패

Representative hard failures remain:

```text
SOURCE_FACT_INVENTION
SILENT_REQUIRED_SOURCE_OMISSION
NORMATIVE_FORCE_STRENGTHENING
SPEC_CONTRADICTION
REQUIRED_BRIDGE_OMISSION
SPEC_WRONG_STANDARD
CLAIM_RELEVANT_STATUS_COLLAPSE
FABRICATED_DETERMINACY
```

`FABRICATED_DETERMINACY` records a case where a missing/open source value is silently filled and then counted as if the downstream task had become source-supported.

It is normally accompanied by `SOURCE_FACT_INVENTION` when the fabricated value is attributed to the source.

## 11. Construction procedure v0.2.1 / 구성 절차

```text
STEP 1  lock target scope, source inventory, and declared downstream task
STEP 2  lock source purpose / audience / priority only to supported resolution
STEP 3  lock DSD source/interface/version dependencies
STEP 4  declare DSD transformation purpose and viewpoint change
STEP 5  atomize requirements
STEP 6  type entities, statuses, prerequisites, domains, and actors
STEP 7  preserve precedence/priority when active
STEP 8  classify SOURCE_OPENNESS_STATUS when claim-relevant
STEP 9  classify DOWNSTREAM_DETERMINACY_STATUS relative to the declared task
STEP 10 separate required dependencies from optional interfaces
STEP 11 declare bridges and external standards when needed
STEP 12 declare aggregate/reconstruction and transition/lineage obligations when active
STEP 13 declare allowed/prohibited/violation/unresolved conditions
STEP 14 run contradiction, omission, hidden-dependency, wrong-standard, and fabrication checks
STEP 15 run G1-G4 guardrail checks
STEP 16 record final Specification outcome separately from openness/determinacy and guardrail ledgers
STEP 17 record reproducibility trace
```

## 12. Core checks / 핵심 검사

```text
S1  type completeness relative to locked inventory
S2  status distinguishability
S3  dependency explicitness
S4  bridge explicitness
S5  violation semantics
S6  contradiction detection
S7  optional-interface restraint
S8  external-standard separation
S9  source-purpose evidence lock
S10 precedence/priority preservation when active
S11 declared viewpoint-change separation
S12 detail proportionality / primary-function preservation
S13 source-openness evidence discipline
S14 downstream-task determinacy check
S15 no fabricated closure of unresolved/open source conditions
```

## 13. Method-specific outcomes / 방법 고유 결과

```text
SPEC_CONTRADICTION
SPEC_UNDERSPECIFIED
SPEC_OVERCONSTRAINED
SPEC_WRONG_STANDARD
SPEC_NO_GAIN
```

The two new axes do not replace these outcomes.

`SPEC_NO_GAIN` remains a valid non-failure result.

## 14. Output record v0.2.1 / 산출 기록

```text
SPECIFICATION_RESULT_ID:
SPECIFICATION_PROTOCOL_VERSION: v0.2.1
TARGET_SCOPE:
DECLARED_DOWNSTREAM_TASK:
LOCKED_REQUIREMENT_INVENTORY:
SOURCE_PURPOSE_LOCK:
TRANSFORMATION_PURPOSE:
REQUIREMENT_ATOMS:
SELECTED_DSD_LAYERS:
STATUS_DISTINCTIONS_REQUIRED:
BRIDGES_REQUIRED:
EXTERNAL_STANDARDS_REQUIRED:
SOURCE_OPENNESS_RECORD:
DOWNSTREAM_DETERMINACY_RECORD:
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
LIMITS:
REPRODUCIBILITY_RECORD:
```

## 15. Validation standard / 검증 기준

Protocol-level validation asks whether the output:

1. faithfully represents the locked source inventory;
2. preserves claim-relevant type/status/dependency/bridge structure;
3. preserves source purpose, priority, and viewpoint boundaries;
4. distinguishes source-supported intentional openness from unsupported intent attribution;
5. separately evaluates whether source resolution is sufficient for the declared downstream task;
6. does not invent closure merely to satisfy a stronger task;
7. preserves detail/representation burden as a guardrail concern;
8. remains retraceable.

External-domain correctness and competent professional judgment remain external standards.

## 16. Reproducibility / 재현성

```text
PROTOCOL_VERSION: v0.2.1
SOURCE_SET_AND_VERSIONS:
REQUIREMENT_INVENTORY_HASH_OR_ID:
DECLARED_DOWNSTREAM_TASK:
SOURCE_PURPOSE_EVIDENCE:
SOURCE_OPENNESS_EVIDENCE:
INTERFACE_PROFILE_DATE:
ATOMIZATION_RULE_VERSION:
GUARDRAIL_PROFILE_VERSION: G1-G4/v0.2
ORDER_OF_PROCESSING_IF_RELEVANT:
MANUAL_JUDGMENT_POINTS:
UNRESOLVED_SOURCE_CONFLICTS:
OUTPUT_RECORD_ID:
```

## 17. Evidence state / 증거 상태

```text
v0.1:
  SPEC-CH-001 through SPEC-CH-005
  SPEC-APP-001

v0.2:
  SPEC-CH-006
  SPEC-APP-002

v0.2.1 transition evidence:
  SPEC-CH-007
    EXACT_SOURCE_OPENNESS_AXIS_MATCHES: 8/8
    EXACT_DOWNSTREAM_DETERMINACY_AXIS_MATCHES: 8/8
    EXACT_JOINT_AXIS_MATCHES: 8/8
    RESULT: SPECIFICATION_OPENNESS_DETERMINACY_AXIS_SEPARATION_PILOT_PASS_WITH_LIMITATIONS

v0.2.1 external applications:
  0

METHOD_STATUS:
  developing
```

## 18. Promotion restraint / 승격 절제

Protocol v0.2.1 is a prospective method-specific refinement only.

It does not establish:
- independent evaluator agreement;
- broad cross-domain superiority;
- improved professional judgment;
- practical time/defect reduction;
- a new shared-core rule;
- `established` method status.

The strongest next evidence is a genuinely independent retrace of an existing locked application, or a new external application under v0.2.1 followed by a separate maturity re-audit.
