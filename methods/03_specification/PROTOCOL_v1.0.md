# DSD Specification Protocol v1.0 / DSD 명세론 표준 프로토콜 v1.0

Status: **candidate pending final standardization audit**  
Date: 2026-09-08  
Method: **DSD Specification / DSD 명세론**  
Higher field: **II. Criteria & Validation / 기준·검증**

## 0. Standardization boundary / 표준화 경계

This candidate is derived from Protocol v0.2.1 after the minimality/stability audit `DSD-AUDIT-20260908-METHODOLOGY-003`.

The allowed cleanup package is limited to:

```text
C1  make context-dependent fields explicitly conditional
C2  allow atom-level VALIDATION_STANDARD inheritance
C3  separate minimal core output from extended diagnostic ledgers
C4  treat NO_GAIN_STATUS as a derived compatibility view
C5  preserve G1-G4 and openness/determinacy axes without expansion
C6  preserve all v0.x protocols/evidence as historical records
```

This v1.0 candidate does not silently rescore v0.1, v0.2, or v0.2.1 evidence.

Internal protocol standardization does **not** imply independent external validation, superiority over existing specification methods, or perfect/final method maturity.

## 1. Method task / 방법 과제

DSD Specification declares, under a locked source inventory and selected DSD interfaces, what must be present, optional, distinguished, mapped, permitted, prohibited, unresolved, or treated as a violation for a declared target and downstream task.

Compact form:

> 무엇이 어떻게 되어 있어야 하는가를 구조적으로 선언하는 방법.

Specification is distinct from:

```text
Analysis       -> decomposes/re-expresses a target
Audit          -> evaluates work against criteria/evidence/procedure
Design         -> constructs a target satisfying requirements
Specification -> declares requirements and admissibility constraints
```

Specification may provide a typed criterion carrier to other DSD methods, but downstream use does not turn those methods into Specification.

## 2. Core input lock / 핵심 입력 잠금

The following are the minimal core inputs for a standard run:

```text
SPECIFICATION_ID:
TARGET_SCOPE:
REQUIREMENT_SOURCE_SET:
SOURCE_VERSIONS:
DSD_INTERFACE_PROFILE_DATE:
SELECTED_DSD_LAYERS:
REQUIREMENT_INVENTORY:
DECLARED_DOWNSTREAM_TASK:
```

Completeness claims are relative to the locked `REQUIREMENT_INVENTORY` and declared downstream task unless a stronger domain completeness basis is independently supplied.

### Conditional input extensions

Use only when applicable:

```text
EXTERNAL_DOMAIN_IF_ANY:
EXTERNAL_STANDARD_IF_ANY:
```

An inactive conditional field is omitted rather than filled with invented or meaningless boilerplate.

## 3. Source-purpose and derivative-view lock / 원문 목적·파생 관점 잠금

Activate this section when source purpose, priority, audience function, or a derivative DSD viewpoint is material to the claim or use.

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

Allowed source-purpose evidence statuses:

```text
EXPLICITLY_STATED
STRONGLY_SUPPORTED_BY_SOURCE_STRUCTURE
UNDETERMINED
OUT_OF_SCOPE
```

Do not invent authorial intent, purpose, audience, or priority merely to complete the record.

## 4. Specification atom v1.0 / 명세 원자

### Core atom fields

```text
REQUIREMENT_ID:
SOURCE_REFERENCE:
TARGET_ENTITY_OR_CARRIER:
REQUIREMENT_TYPE:
REQUIRED_OR_OPTIONAL:
ACTIVATION_CONDITION:
REQUIRED_STRUCTURE_OR_VALUE:
VIOLATION_CONDITION:
UNRESOLVED_CONDITION:
```

### Conditional atom fields

Activate only when they materially affect the requirement:

```text
PRECEDENCE_OR_PRIORITY:
SOURCE_OPENNESS_STATUS:
DOWNSTREAM_DETERMINACY_STATUS:
ALLOWED_ALTERNATIVES:
PROHIBITED_STATES:
DEPENDENCIES:
VALIDATION_STANDARD:
```

`VALIDATION_STANDARD` inherits the locked specification/domain standard by default. Supply an atom-level value only when the atom requires a narrower, different, or explicitly local standard.

Natural-language labels alone are insufficient where activation, dependency, violation, or unresolved semantics affect downstream use.

## 5. Source openness and downstream determinacy / 원문 개방성·하위 과제 결정가능성

Activate these axes only when openness or determinacy is claim-relevant.

```text
SOURCE_OPENNESS_STATUS:
  SOURCE_DETERMINATE
  SOURCE_INTENTIONAL_OPENNESS
  OPENNESS_INTENT_UNDETERMINED
  NOT_APPLICABLE

DOWNSTREAM_DETERMINACY_STATUS:
  SUFFICIENT_AT_DECLARED_RESOLUTION
  UNDERDETERMINED_FOR_DECLARED_TASK
  NOT_APPLICABLE
```

The axes remain independent:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

A source may intentionally preserve bounded discretion or contextual implementation while still being underdetermined for a stronger downstream task.

`SPEC_UNDERSPECIFIED` is therefore task-relative and does not by itself prove that the source was accidentally defective.

## 6. DSD layer and bridge discipline / DSD 층위·브리지 규율

Use only the DSD interfaces required by the locked task.

```text
FORMATION_LAYER:
  use when formation/admission/channel structure is material

PROPERTY_CORE:
  use when typed property/status/applicability/prerequisite structure is material

STATIC_AGGREGATION_LAYER:
  use only when aggregate/readout/information-loss obligations are material

DYNAMICS_LAYER:
  use only when evolution/transition/lineage obligations are material

OPTIONAL_SPECIALIZATION:
  supply only when claim-dependent
```

Cross-carrier, cross-layer, or cross-domain mappings require explicit bridges when the claim depends on them. Similar names or intuitive correspondence do not create a bridge.

External domain standards remain external validation authorities.

## 7. Guardrail profile / 중심선 가드레일

Guardrails are centerline controls, not automatic discard rules.

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

Activation:

```text
G1 active when a source/requirement corpus is represented
G2 active when source purpose/priority is claim-relevant
G3 active when added detail or representation burden can affect declared use
G4 active when a derivative DSD viewpoint is introduced
```

Guardrail verdicts:

```text
INSIDE_GUARDRAILS
GUARDRAIL_PRESSURE
GUARDRAIL_EXCEEDED_RECOVERABLE
PURPOSE_OR_VIEWPOINT_DISTORTED
UNDETERMINED
```

Extra detail, abstraction, or viewpoint change is not automatically a failure. Undeclared or uncontrolled drift is the concern.

## 8. Hard failures and method outcomes / 경성 실패·방법 결과

Representative hard failures:

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

Method-specific outcomes:

```text
SPEC_CONTRADICTION
SPEC_UNDERSPECIFIED
SPEC_OVERCONSTRAINED
SPEC_WRONG_STANDARD
SPEC_NO_GAIN
```

`SPEC_NO_GAIN` is a valid non-failure result. A competent existing specification may remain preferable for a standalone domain task while the DSD Specification record still has method-family handoff value.

## 9. Construction procedure v1.0 / 구성 절차

```text
STEP 1  lock target, sources, versions, inventory, and downstream task
STEP 2  lock only source purpose/audience/priority supported at the available resolution
STEP 3  lock selected DSD interfaces and required dependencies
STEP 4  declare transformation purpose and derivative viewpoint when active
STEP 5  atomize requirements using the core atom fields
STEP 6  activate only claim-relevant conditional atom fields
STEP 7  preserve type/status/prerequisite/dependency distinctions required by the task
STEP 8  preserve precedence/priority when active
STEP 9  classify source openness and downstream determinacy when active
STEP 10 separate required DSD dependencies from optional interfaces
STEP 11 declare required bridges and external standards
STEP 12 declare aggregate/reconstruction or transition/lineage obligations only when active
STEP 13 run contradiction, omission, hidden-dependency, wrong-standard, and fabrication checks
STEP 14 run active G1-G4 guardrails
STEP 15 record final Specification status separately from diagnostic ledgers
STEP 16 record limits and reproducibility information
STEP 17 hand off the typed record to another DSD method only under an explicit receiving task
```

## 10. Core checks / 핵심 검사

```text
S1  type completeness relative to locked inventory
S2  claim-relevant status distinguishability
S3  dependency explicitness when dependency matters
S4  bridge explicitness when cross-structure transfer matters
S5  violation/unresolved semantics
S6  contradiction detection
S7  optional-interface restraint
S8  external-standard separation
S9  source-purpose evidence restraint when active
S10 precedence/priority preservation when active
S11 derivative-view separation when active
S12 detail proportionality / primary-function preservation when active
S13 source-openness evidence discipline when active
S14 downstream-task determinacy check when active
S15 no fabricated closure of unresolved/open conditions
S16 method-family handoff preserves requirement identity and external-standard boundary
```

## 11. Standard output / 표준 산출물

### Minimal core result

Every standard run records:

```text
SPECIFICATION_RESULT_ID:
SPECIFICATION_PROTOCOL_VERSION: v1.0
TARGET_SCOPE:
DECLARED_DOWNSTREAM_TASK:
LOCKED_REQUIREMENT_INVENTORY:
REQUIREMENT_ATOMS:
SELECTED_DSD_LAYERS:
FINAL_SPEC_STATUS:
  usable
  usable_with_unresolved_items
  contradictory
  underspecified
  no_gain
LIMITS:
REPRODUCIBILITY_RECORD:
```

### Conditional extended ledgers

Include only when active or non-empty:

```text
SOURCE_PURPOSE_LOCK:
TRANSFORMATION_PURPOSE:
STATUS_DISTINCTIONS_REQUIRED:
BRIDGES_REQUIRED:
EXTERNAL_STANDARDS_REQUIRED:
SOURCE_OPENNESS_RECORD:
DOWNSTREAM_DETERMINACY_RECORD:
CONTRADICTIONS_FOUND:
UNDERSPECIFIED_ITEMS:
OVERCONSTRAINTS_FOUND:
HARD_FAILURES:
GUARDRAIL_RECORD:
GUARDRAIL_VERDICT:
```

Compatibility/export systems may expose:

```text
NO_GAIN_STATUS := (FINAL_SPEC_STATUS == no_gain)
```

This is a derived view, not an additional semantic state.

## 12. Reproducibility / 재현성

Record enough information for a later retrace at the declared resolution:

```text
PROTOCOL_VERSION: v1.0
SOURCE_SET_AND_VERSIONS:
REQUIREMENT_INVENTORY_HASH_OR_ID:
DECLARED_DOWNSTREAM_TASK:
INTERFACE_PROFILE_DATE:
ATOMIZATION_RULE_VERSION:
ACTIVE_CONDITIONAL_FIELDS_OR_LEDGERS:
SOURCE_PURPOSE_EVIDENCE_IF_ACTIVE:
SOURCE_OPENNESS_EVIDENCE_IF_ACTIVE:
GUARDRAIL_PROFILE_VERSION: G1-G4/v1.0
ORDER_OF_PROCESSING_IF_RELEVANT:
MANUAL_JUDGMENT_POINTS:
UNRESOLVED_SOURCE_CONFLICTS:
OUTPUT_RECORD_ID:
```

Procedural retraceability is not the same as independent evaluator agreement.

## 13. Validation and scope / 검증·범위

Protocol-level success asks whether the run:

1. faithfully represents the locked source inventory;
2. preserves claim-relevant distinctions and requirements;
3. activates only necessary fields and DSD interfaces;
4. preserves source purpose/priority/viewpoint boundaries when relevant;
5. distinguishes intentional openness from task-relative underdetermination;
6. does not fabricate closure or strengthen normative force;
7. exposes contradiction, underspecification, overconstraint, wrong-standard, and NO_GAIN outcomes when applicable;
8. remains retraceable and handoff-compatible at the declared interface.

It does not replace domain proof, empirical validation, professional judgment, legal/safety authority, interpretive standards, or other receiving-domain validation.

## 14. Historical compatibility / 역사적 호환성

```text
PROTOCOL.md        -> v0.1 historical
PROTOCOL_v0.2.md   -> v0.2 historical
PROTOCOL_v0.2.1.md -> v0.2.1 historical/current evidence basis
PROTOCOL_v1.0.md   -> candidate until final standardization audit passes
```

Historical evidence keeps the protocol version under which it was produced. No automatic rescoring occurs.

## 15. Evidence and maturity restraint / 증거·성숙도 절제

Current evidence before final standardization audit includes:

```text
DIRECT_CONSTRUCTED_PILOTS: 7
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
METHOD_FAMILY_HANDOFF_PILOTS: 1  # Specification -> Audit
```

Still not established:

```text
INDEPENDENT_EVALUATOR_VALIDATION
MEASURED_ENGINEERING_BENEFIT
ALL_METHOD_HANDOFF_INTEROPERABILITY
EXTERNAL_SPECIFICATION_SUPERIORITY
PERFECTION_OR FINALITY
```

Method evidence status remains `developing` unless a separate maturity audit changes it.
