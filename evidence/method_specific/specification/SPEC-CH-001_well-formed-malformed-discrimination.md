# SPEC-CH-001 — Well-Formed / Malformed Specification Discrimination / 정상·비정상 명세 구별 도전

Status: **SPECIFICATION_DISCRIMINATION_PILOT_PASS_WITH_LIMITATIONS**  
Date: 2026-09-06  
Evidence scope: `method_specific`  
Case origin: `constructed_benchmark`  
Method directly tested: **DSD Specification / DSD 명세론**  
Method protocol: **DSD Specification Protocol v0.1**  
DSD interface profile date: **2026-09-05**

## 1. Purpose / 목적

This challenge tests whether DSD Specification, under its own protocol, can distinguish a specification that is structurally usable for a declared downstream checker from specifications that are malformed because a required type, status distinction, activation condition, bridge, violation semantics, or dependency boundary is missing or distorted.

This is **direct method-specific evidence for Specification**. It is not a shared-core transfer pilot and does not directly validate another DSD method.

## 2. Locked benchmark target / 고정 벤치마크 대상

Synthetic target: `RelaySpecToy-v1`.

The target is an internal typed relay specification with no external-domain truth claim, no aggregate readout, no temporal identity claim, and no realized-axis specialization.

```text
TARGET_SCOPE: RelaySpecToy-v1
REQUIREMENT_SOURCE_SET: RS-SPEC-001-v1
SELECTED_DSD_LAYERS:
  FORMATION_LAYER: used
  PROPERTY_CORE: used
  STATIC_AGGREGATION_LAYER: not used
  DYNAMICS_LAYER: not used
  REALIZED_AXIS_SPECIALIZATION: not supplied
EXTERNAL_DOMAIN: none
EXTERNAL_STANDARD: not applicable
```

Locked requirement inventory:

```text
R1 INPUT REQUIREMENT
  input_A is required.
  target carrier: C_in
  input type: scalar signal token

R2 STATUS REQUIREMENT
  property q(input_A) is evaluated only in ACTIVE context.
  defined_zero and applicable_but_undefined must remain distinguishable.

R3 BRIDGE REQUIREMENT
  when an output relation transfers a result from C_in to C_out,
  an explicit bridge B_io is required.

R4 VERDICT REQUIREMENT
  the downstream checker must be able to distinguish, when relevant:
  SATISFIED
  VIOLATED
  UNRESOLVED_OR_UNDERSPECIFIED
  NOT_APPLICABLE
```

Completeness is claimed only relative to `RS-SPEC-001-v1`.

## 3. Precommitted discrimination criteria / 사전 고정 판정 기준

A case is accepted as **well formed** only if the protocol can produce a usable structural specification without inventing a missing type, status distinction, activation condition, bridge, or violation rule.

A case is classified as malformed when at least one of the following protocol-level diagnostics is triggered:

```text
D1 TYPE_OR_CARRIER_OMISSION
  required target/type information is absent
  -> SPEC_UNDERSPECIFIED

D2 STATUS_COLLAPSE
  defined_zero and applicable_but_undefined are collapsed
  -> SPEC_UNDERSPECIFIED

D3 ACTIVATION_AMBIGUITY
  a context-dependent requirement has no activation condition
  -> SPEC_UNDERSPECIFIED

D4 BRIDGE_OMISSION
  cross-carrier meaning is used with no explicit/canonical bridge
  -> SPEC_UNDERSPECIFIED

D5 VIOLATION_SEMANTICS_OMISSION
  the requirement cannot distinguish satisfied/violated/unresolved/not-applicable
  as required by the downstream task
  -> SPEC_UNDERSPECIFIED

D6 OPTIONAL_DEPENDENCY_INJECTION
  claim-irrelevant realized-axis data are made mandatory
  -> SPEC_OVERCONSTRAINED
```

Expected case-level scoring is locked before classification:

```text
WELL_FORMED_CASES: 2
MALFORMED_CASES: 6
PASS_REQUIREMENT:
  accept 2/2 well-formed cases
  detect 6/6 malformed cases
  exact diagnostic family match 8/8
  no false requirement for inactive Static/Dynamics/axis interfaces
```

## 4. Cases / 사례

### WF-01 — Complete minimal specification

Record contains:

```text
R1 target carrier C_in and scalar input type
R2 ACTIVE activation condition
R2 separate defined_zero / applicable_but_undefined statuses
R3 explicit B_io bridge from C_in to C_out
R4 explicit satisfied / violated / unresolved / not-applicable semantics
Static: not used
Dynamics: not used
Realized axis: not supplied
```

Expected: `usable`.

Observed: `usable`.

Reason: all claim-relevant type, status, dependency, bridge, and verdict semantics required by the locked inventory are explicit.

### WF-02 — Minimal specification with inactive optional interfaces omitted

Same locked requirements as WF-01, but no Static Aggregation, Dynamics, or realized-axis records are supplied beyond an explicit `not used / not supplied` interface lock.

Expected: `usable`.

Observed: `usable`.

Reason: those interfaces are not required by `RS-SPEC-001-v1`; omitting them does not create underspecification.

This is the principal negative control against over-requiring optional interfaces.

### MF-01 — Missing target carrier/type

Perturbation:

```text
R1: "input_A is required"
TARGET_ENTITY_OR_CARRIER: omitted
input type: omitted
```

Expected diagnostic: `SPEC_UNDERSPECIFIED / D1 TYPE_OR_CARRIER_OMISSION`.

Observed: exact match.

The downstream checker cannot determine which carrier/type satisfies the requirement without inventing information.

### MF-02 — Status collapse

Perturbation:

```text
R2 status allowed values:
  zero_or_undefined
```

instead of keeping:

```text
defined_zero
applicable_but_undefined
```

Expected diagnostic: `SPEC_UNDERSPECIFIED / D2 STATUS_COLLAPSE`.

Observed: exact match.

The specification loses a distinction explicitly required by the locked inventory.

### MF-03 — Missing activation condition

Perturbation:

```text
R2 applies to q(input_A)
ACTIVATION_CONDITION: omitted
```

Expected diagnostic: `SPEC_UNDERSPECIFIED / D3 ACTIVATION_AMBIGUITY`.

Observed: exact match.

Because R2 is defined only for ACTIVE context in the locked source inventory, the specification no longer determines when the status requirement applies.

### MF-04 — Missing bridge

Perturbation:

```text
source carrier: C_in
target carrier: C_out
cross-carrier output relation: declared
BRIDGE_ID / MAP_OR_RELATION: omitted
```

Expected diagnostic: `SPEC_UNDERSPECIFIED / D4 BRIDGE_OMISSION`.

Observed: exact match.

The record uses a cross-carrier correspondence but does not specify how that correspondence is established.

### MF-05 — Missing violation/unresolved semantics

Perturbation:

```text
R4: "the relay output must be acceptable"
VIOLATION_CONDITION: omitted
UNRESOLVED_CONDITION: omitted
NOT_APPLICABLE condition: omitted
```

Expected diagnostic: `SPEC_UNDERSPECIFIED / D5 VIOLATION_SEMANTICS_OMISSION`.

Observed: exact match.

The downstream checker cannot distinguish failure from missing information or inapplicability.

### MF-06 — Irrelevant realized-axis dependency injected

Perturbation:

```text
REALIZED_AXIS_SPECIALIZATION: made mandatory
required rank data: yes
```

although no requirement in `RS-SPEC-001-v1` uses axis, rank, normal, or geometry.

Expected diagnostic: `SPEC_OVERCONSTRAINED / D6 OPTIONAL_DEPENDENCY_INJECTION`.

Observed: exact match.

The requirement is explicit but stronger than the locked inventory and turns a claim-irrelevant optional specialization into a hidden prerequisite.

## 5. Score / 점수

```text
WELL_FORMED_CASES_ACCEPTED: 2/2
MALFORMED_CASES_DETECTED: 6/6
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
FALSE_POSITIVES_ON_INACTIVE_INTERFACES: 0
NEGATIVE_CONTROL: pass
```

Case table:

| Case | Expected | Observed | Match |
|---|---|---|---|
| WF-01 | usable | usable | yes |
| WF-02 | usable | usable | yes |
| MF-01 | SPEC_UNDERSPECIFIED / D1 | same | yes |
| MF-02 | SPEC_UNDERSPECIFIED / D2 | same | yes |
| MF-03 | SPEC_UNDERSPECIFIED / D3 | same | yes |
| MF-04 | SPEC_UNDERSPECIFIED / D4 | same | yes |
| MF-05 | SPEC_UNDERSPECIFIED / D5 | same | yes |
| MF-06 | SPEC_OVERCONSTRAINED / D6 | same | yes |

## 6. Method-specific result / 방법 고유 결과

```text
CHALLENGE_ID: SPEC-CH-001
METHOD_DIRECTLY_TESTED: DSD Specification
METHOD_VERSION_OR_PROTOCOL: Specification Protocol v0.1
RESULT: SPECIFICATION_DISCRIMINATION_PILOT_PASS_WITH_LIMITATIONS
DIRECT_METHOD_EVIDENCE: yes, pilot-level
METHOD_MATURITY: not mature
```

The challenge supports the limited claim that **Protocol v0.1 can discriminate the locked well-formed cases from six basic malformed specification constructions using its own method-specific criteria**.

It does not support a claim that every real-world specification can be correctly generated or classified by DSD Specification.

## 7. Shared-core use / 공통 코어 사용

The following shared rules were activated only where relevant:

```text
SC-01  status/type distinction
SC-02  locked requirement source and interface profile
SC-03  explicit C_in -> C_out bridge
SC-04  optional-interface restraint
SC-07  evidence scope / case-origin metadata
SC-08  locked scoring criteria and unfavorable-result preservation
```

SC-05, SC-06, SC-09, and SC-10 were not required by the core benchmark claim. Their inactivity is intentional and is part of the minimum-layer discipline.

## 8. Reproducibility record / 재현성 기록

```text
PROTOCOL_VERSION: Specification Protocol v0.1
REQUIREMENT_SOURCE_SET: RS-SPEC-001-v1
REQUIREMENT_INVENTORY_ID: SPEC-CH-001-RI-v1
INTERFACE_PROFILE_DATE: 2026-09-05
CASE_SET: WF-01, WF-02, MF-01..MF-06
CASE_ORDER: fixed as written
ATOMIZATION_RULE_VERSION: Protocol v0.1
MANUAL_JUDGMENT_POINTS:
  mapping each perturbation to the protocol diagnostic family
OUTPUT_RECORD_ID: SPEC-CH-001
```

A future independent-retrace challenge should give the same locked source inventory and cases to a separate reviewer without supplying the observed labels.

## 9. Limits / 한계

- constructed synthetic benchmark;
- same-session protocol authoring and testing history, not independent blind validation;
- only basic well-formed/malformed discrimination is tested;
- contradiction combinations are reserved for `SPEC-CH-002`;
- bridge/optional-layer boundary stress testing is reserved for `SPEC-CH-003`;
- `NO_GAIN` is reserved for `SPEC-CH-004`;
- independent retrace/reproducibility is reserved for `SPEC-CH-005`;
- no real-world or independently generated requirement corpus is tested here;
- no maturity promotion beyond `developing` is claimed.

## 10. Next step / 다음 단계

Proceed to **SPEC-CH-002 — Contradiction and Underspecification Challenge** while preserving this record append-only.