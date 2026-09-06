# DSD Specification Protocol v0.1 / DSD 명세론 전용 프로토콜 v0.1

Status: **developing / protocol established, direct evidence not yet mature**  
Date: 2026-09-06  
Method: **DSD Specification / DSD 명세론**  
Higher field: **II. Criteria & Validation / 기준·검증**

## 1. Method task / 방법 과제

DSD Specification converts a declared target, requirement source, and selected DSD interfaces into an explicit **structural specification record** that states what must be present, what may be optional, what distinctions must be preserved, which mappings are required, what outputs or transitions are admissible, and what counts as violation or unresolved specification.

It does **not** prove that the external requirement source is correct, lawful, safe, clinically valid, scientifically true, or otherwise authoritative. Those judgments remain under the applicable external standard.

Core method boundary:

```text
Specification
= declare requirements and admissibility constraints
!= Audit
= evaluate performed work against requirements/evidence/procedure
```

Specification may later be consumed by Design, Synthesis, Transformation, Audit, Control, Operation, or another method, but those downstream tasks do not become part of Specification itself.

## 2. Required inputs / 필수 입력

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

`REQUIREMENT_INVENTORY` is the locked set of requirement candidates that this protocol is asked to express. Completeness claims are relative to this locked inventory unless a stronger domain-specific completeness theorem or authority source is supplied.

## 3. DSD layer selection / DSD 층위 선택

Default starting point:

```text
FORMATION_LAYER: used
PROPERTY_CORE: used when typed properties/statuses are part of the target
STATIC_AGGREGATION_LAYER: used only when aggregate/readout obligations are specified
DYNAMICS_LAYER: used only when evolution/transition/lineage obligations are specified
OPTIONAL_SPECIALIZATION: supplied only when a claim actually depends on it
```

SC-04 applies to prevent both deletion of required dependencies and hidden over-requirement of optional interfaces.

## 4. Specification atom / 명세 원자

Each requirement should be atomized into a record that can be checked without relying on prose implication alone.

```text
REQUIREMENT_ID:
SOURCE_REFERENCE:
TARGET_ENTITY_OR_CARRIER:
REQUIREMENT_TYPE:
  existence
  admission
  status
  typed_input
  prerequisite
  value_or_range
  relation
  bridge
  aggregate
  transition
  lineage
  output
  prohibition
  external_standard
REQUIRED_OR_OPTIONAL:
ACTIVATION_CONDITION:
REQUIRED_STRUCTURE_OR_VALUE:
ALLOWED_ALTERNATIVES:
PROHIBITED_STATES:
DEPENDENCIES:
VALIDATION_STANDARD:
VIOLATION_CONDITION:
UNRESOLVED_CONDITION:
```

A requirement is not considered fully specified merely because a natural-language sentence names the desired object. Its activation, dependency, and violation semantics must be sufficiently explicit for the intended downstream task.

## 5. Status and typed-domain discipline / 상태·타입 도메인 규율

When the selected DSD interface distinguishes statuses, the specification must not silently collapse them.

Representative distinctions include:

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

For a typed property input, preserve the complete ordered typed input unless a separate symmetry/quotient rule is explicitly supplied.

Activated shared rule: **SC-01**.

## 6. Source/interface/version lock / 소스·인터페이스·버전 잠금

Every requirement whose semantics depend on a DSD paper, domain rule, specification source, standard, or revision must identify that dependency.

```text
SOURCE_LOCK:
  DOCUMENT_OR_RULE:
  VERSION_OR_DATE:
  ID_OR_COMMIT_IF_AVAILABLE:

INTERFACE_LOCK:
  FORMATION_LAYER: used / not used
  PROPERTY_CORE: used / not used
  STATIC_AGGREGATION_LAYER: used / not used
  DYNAMICS_LAYER: used / not used
  OPTIONAL_SPECIALIZATION: supplied / not supplied
```

Activated shared rule: **SC-02**.

## 7. Bridge requirements / 브리지 요구조건

If a requirement transfers meaning across layers, carriers, representations, or external domains, the mapping must be explicit or canonically referenced.

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

Names, coordinate occurrence, or intuitive association are not sufficient to create the bridge.

Activated shared rule: **SC-03**.

## 8. Aggregate and reconstruction requirements / 집계·복원 요구조건

If a specification permits an aggregate, compressed representation, or reduced readout, it must state what downstream distinctions are still required.

```text
REDUCTION_OR_AGGREGATION_ID:
SOURCE_CARRIER:
REDUCED_CARRIER:
MAP:
REQUIRED_PRESERVED_INFORMATION:
KNOWN_INFORMATION_LOSS:
INJECTIVITY_REQUIRED: yes / no
RECONSTRUCTION_CLAIM_ALLOWED: none / partial / unique
RECONSTRUCTION_BASIS:
```

A specification must not imply unique support/decomposition/history reconstruction from an aggregate unless the required injectivity or side information is itself specified.

Activated shared rule: **SC-05**.

## 9. Transition and lineage requirements / 전이·계보 요구조건

When the target includes time/order-dependent identity, the specification must distinguish ordinary evolution from identity-breaking transition.

```text
EVENT_CLASS:
IDENTITY_PRESERVED: yes / no / not_applicable
TRANSITION_REQUIRED: yes / no
TRANSITION_TRIGGER:
CHANNEL_LINEAGE_REQUIRED: yes / no
COMPONENT_LINEAGE_REQUIRED: yes / no
LINEAGE_SOURCE_OR_RULE:
BRANCHING_OR_MERGING_ALLOWED:
```

Activated shared rule: **SC-06**.

## 10. External-standard boundary / 외부 기준 경계

When the specification makes or enables an external-domain conclusion, DSD structural consistency is not itself the receiving domain's proof, empirical, professional, legal, ethical, safety, or interpretive standard.

```text
DOMAIN_CLAIM_IF_ANY:
EXTERNAL_DOMAIN:
EXTERNAL_STANDARD:
STANDARD_SOURCE_OR_AUTHORITY:
STANDARD_APPLICABILITY:
DOMAIN_BRIDGE:
```

Activated shared rule: **SC-10**.

## 11. Specification construction procedure / 명세 구성 절차

```text
STEP 1  lock target scope and requirement-source inventory
STEP 2  lock DSD source/interface/version dependencies
STEP 3  atomize each requirement
STEP 4  type entities, inputs, statuses, prerequisites, and domains
STEP 5  separate required dependencies from optional interfaces
STEP 6  declare bridges and external standards where needed
STEP 7  declare aggregate/reconstruction obligations when reduction is used
STEP 8  declare transition/lineage obligations when temporal identity is used
STEP 9  declare allowed, prohibited, violation, and unresolved conditions
STEP 10 run contradiction, omission, hidden-dependency, and overclaim checks
STEP 11 record output and reproducibility trace
```

## 12. Core specification checks / 핵심 명세 검사

### S1 — Type completeness relative to the locked inventory

Every requirement that needs a typed carrier or input must identify it sufficiently for the downstream task.

### S2 — Status distinguishability

Claim-relevant DSD statuses must remain distinct.

### S3 — Dependency explicitness

Every requirement identifies the DSD layers, prerequisites, and optional interfaces it actually depends on.

### S4 — Bridge explicitness

Every non-inherited cross-structure correspondence used by a requirement has an explicit bridge.

### S5 — Violation semantics

A downstream checker must be able to distinguish at least:

```text
SATISFIED
VIOLATED
UNRESOLVED_OR_UNDERSPECIFIED
NOT_APPLICABLE
```

when those states are relevant to the target.

### S6 — Contradiction detection

The same activated requirement context must not simultaneously require and prohibit the same state unless the conflict is explicitly recorded as an unresolved source conflict.

### S7 — Optional-interface restraint

A claim-irrelevant optional specialization is not a hidden prerequisite.

### S8 — External-standard separation

External-domain acceptability or truth is not silently replaced by DSD-internal consistency.

## 13. Contradiction and underspecification classes / 모순·미명세 분류

```text
SPEC_CONTRADICTION:
  two simultaneously active requirements cannot both be satisfied

SPEC_UNDERSPECIFIED:
  the requirement text does not determine a necessary target/type/status/
  dependency/bridge/violation condition needed by the declared downstream task

SPEC_OVERCONSTRAINED:
  a claim-irrelevant optional interface or stronger condition is made mandatory

SPEC_WRONG_STANDARD:
  a requirement is validated under a criterion not competent for the declared claim

SPEC_NO_GAIN:
  DSD re-expression adds no new distinction, traceability, ambiguity reduction,
  or downstream checkability beyond an already complete locked external specification
```

`SPEC_NO_GAIN` is a valid result and is not converted into failure merely because the DSD representation was unnecessary.

## 14. Output record / 산출 기록

```text
SPECIFICATION_RESULT_ID:
SPECIFICATION_PROTOCOL_VERSION: v0.1
TARGET_SCOPE:
LOCKED_REQUIREMENT_INVENTORY:
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
FINAL_SPEC_STATUS:
  usable
  usable_with_unresolved_items
  contradictory
  underspecified
  no_gain
LIMITS:
REPRODUCIBILITY_RECORD:
```

## 15. Shared-core activation matrix / 공통 코어 활성화 행렬

| Shared rule | Specification activation |
|---|---|
| SC-01 | status/type distinctions appear in requirements |
| SC-02 | source/interface/version semantics affect requirements |
| SC-03 | cross-layer/carrier/domain mapping is required |
| SC-04 | required vs optional DSD dependencies must be separated |
| SC-05 | aggregate/reduced representation or reconstruction is specified |
| SC-06 | temporal identity, transition, or lineage is specified |
| SC-07 | evidence records about the specification are classified |
| SC-08 | competing specifications, superiority, or locked confirmatory evaluation is claimed |
| SC-09 | DSD object status and evidence/audit status coexist in the record |
| SC-10 | the specification supports an external-domain claim |

The protocol does not force inactive shared rules into every specification.

## 16. Method-specific failure / no-gain criteria / 방법 고유 실패·무이득 기준

A Specification run fails or remains unresolved when the declared downstream task requires a distinction or condition that the produced specification leaves ambiguous, contradictory, wrongly typed, unsupported, silently bridged, or validated under the wrong standard.

A run may return `NO_GAIN` when the locked source specification already contains all relevant distinctions, dependencies, violation semantics, standards, and traceability, so the DSD re-expression supplies no additional operational value.

## 17. Validation standard / 검증 기준

Protocol-level validation asks whether the specification record correctly and reproducibly represents the **locked requirement inventory** under the selected DSD interfaces and preserves the required distinctions for the declared downstream task.

External-domain correctness remains separately governed by the domain standard identified under SC-10.

No global completeness theorem is claimed by protocol v0.1.

## 18. Reproducibility record / 재현성 기록

```text
PROTOCOL_VERSION:
SOURCE_SET_AND_VERSIONS:
REQUIREMENT_INVENTORY_HASH_OR_ID:
INTERFACE_PROFILE_DATE:
ATOMIZATION_RULE_VERSION:
ORDER_OF_PROCESSING_IF_RELEVANT:
MANUAL_JUDGMENT_POINTS:
UNRESOLVED_SOURCE_CONFLICTS:
OUTPUT_RECORD_ID:
```

For non-code specification work, reproducibility means another reviewer can retrace the same source inventory, atomization, dependency, bridge, status, and violation decisions. It does not require executable code when the task itself is not computational.

## 19. Evidence status / 증거 상태

This file establishes a **dedicated method protocol** for DSD Specification.

It is not by itself direct empirical validation of the method.

Next method-specific evidence sequence:

```text
SPEC-CH-001  basic well-formed / malformed specification discrimination
SPEC-CH-002  contradiction and underspecification challenge
SPEC-CH-003  optional-layer and bridge boundary challenge
SPEC-CH-004  NO_GAIN specification challenge
SPEC-CH-005  reproducibility / independent retrace challenge
then external or independently generated application cases
```
