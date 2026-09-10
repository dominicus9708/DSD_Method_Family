# SYN-APP-003 Precommit / USB Type-C Physical Mating External Application

Status: **PRECOMMITTED — evaluation not yet executed at commit time**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`

## 1. Evidence identity

```text
CASE_ID: SYN-APP-003
CASE_CLASS: external_application
CASE_ORIGIN: externally_sourced_physical_interface_rule_with_constructed_candidate_fixture
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
EXTERNAL_DOMAIN: physical connector assembly / USB Type-C mating interface
EXTERNAL_STANDARD:
  USB Type-C Cable and Connector Specification Release 2.0 (August 2019),
  mechanical mating and attach/orientation clauses only
SUPPORTING_CURRENT_USB_IF_PAGE:
  USB Type-C Cable and Connector Specification overview
BASELINE: none
```

The current USB-IF document library contains newer Type-C releases, but this application freezes the publicly accessible Release 2.0 mechanical interface text as its version-specific external authority. No claim of current Release-2.5 compliance is made.

## 2. Frozen external authority and source facts

Official sources:

```text
USB-IF Type-C overview:
https://www.usb.org/usb-type-cr-cable-and-connector-specification

Frozen Release 2.0 PDF:
https://www.usb.org/sites/default/files/USB%20Type-C%20Spec%20R2.0%20-%20August%202019.pdf
```

Frozen source scope:

```text
Release 2.0 Section 2.3.2 — Plug Orientation/Cable Twist Detection
Release 2.0 Section 2.3.3 — Initial Power and Data Relationship
Release 2.0 Section 3.2 — USB Type-C Connector Mating Interfaces
USB-IF Type-C overview — reversible plug orientation and cable direction
```

Frozen source facts, paraphrased:

```text
S1 The Type-C interface defines a plug and a receptacle as the mating connector pair.
S2 The dimensions governing mating interoperability belong to the Type-C plug/receptacle mating interfaces.
S3 A Type-C plug may be inserted into a Type-C receptacle in either of two orientations.
S4 The Type-C ecosystem is designed for reversible plug orientation and cable direction.
S5 Plug orientation is detected through the Configuration Channel (CC) system for correct signal routing.
S6 Mechanical characteristics of the Type-C plug/receptacle alone do not inherently establish host/device or Source/Sink relationships.
S7 Power/data role establishment and successful USB operation require electrical/configuration behavior beyond mere mechanical mating.
```

No USB Power Delivery contract, USB4 mode, cable current rating, data-rate capability, compliance-logo status, signal-integrity measurement, durability-cycle test, or certification result is activated.

## 3. Frozen Synthesis task

```text
SYNTHESIS_TASK_ID: SYN-APP-TASK-003
TASK_SCOPE:
  evaluate direct physical mating compositions made from declared USB Type-C plug/receptacle or Type-C-to-Type-C cable-end components,
  preserving connector role, allowed orientation, cable-end direction symmetry, and the boundary between mechanical mating and functional power/data-role establishment
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
TARGET_DSD_LAYER_SCOPE:
  Formation-style component/interface bookkeeping only as method interface
DOMAIN_BRIDGE:
  USB-IF Type-C physical mating/orientation rules
EXTERNAL_STANDARD:
  USB Type-C Cable and Connector Specification Release 2.0 mechanical subset
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE:
  static_order_only
COMPOSITION_CANDIDATE_BASIS:
  {M1,M2,M3,M4,M5,M6,M7,M8,M9,M10}
COMPOSITION_COVERAGE:
  exhaustive relative only to the frozen ten-candidate fixture
```

This task concerns direct Type-C physical mating structure and declared target properties. It does not claim complete electrical interoperability.

## 4. Frozen target resolution

A material output record preserves:

```text
connector component identity
connector role: PLUG or RECEPTACLE
whether a Type-C-to-Type-C cable end is E1 or E2
relative insertion orientation: ORIENTATION_A / ORIENTATION_B / INVALID_90_DEG
physical mating result
cable-end assignment when applicable
declared functional-role claim, if any
```

Therefore:

```text
TYPE_C_COMPONENT_ADMITTED
!= DIRECTLY_MATEABLE_WITH_ANY_TYPE_C_COMPONENT

ORIENTATION_A
!= ORIENTATION_B as insertion-state record
but both may be mechanically admissible

MECHANICAL_MATING
!= SOURCE_SINK_ROLE_ESTABLISHMENT

MECHANICAL_MATING
!= HOST_DEVICE_ROLE_ESTABLISHMENT

REVERSIBLE_CABLE_DIRECTION
!= REVERSIBLE_POWER_OR_DATA_ROLE
```

## 5. Frozen hard conditions

```text
H1 MATING_ROLE_COMPATIBILITY
   A direct Type-C connector mating pair must consist of one Type-C plug and one Type-C receptacle.
   Plug-to-plug and receptacle-to-receptacle are rejected as direct mating compositions.

H2 INSERTION_ORIENTATION_LEGALITY
   For a Type-C plug/receptacle pair, ORIENTATION_A and ORIENTATION_B are admitted.
   The frozen INVALID_90_DEG orientation is rejected because the external interface admits the two insertion orientations, not a quarter-turn insertion.

H3 PHYSICAL_MATING_TARGET_ACCURACY
   If H1-H2 pass, the declared physical-mating target must match the Type-C mating interface.

H4 FUNCTIONAL_ROLE_NONINFERENCE
   A candidate is rejected if it declares that Source/Sink or host/device role is established solely by mechanical connector geometry.
   Such roles require CC/electrical configuration beyond mechanical mating.

H5 CABLE_DIRECTION_REVERSIBILITY
   For the frozen Type-C-to-Type-C cable candidates, swapping end identities E1 and E2 between the two Type-C receptacles is not by itself a physical mating failure.
   This condition does not establish power/data-role symmetry.
```

Staging:

```text
Evaluate H1 first.
If H1 fails -> H2-H5 NOT_REACHED.
If H1 passes -> evaluate H2.
If H2 fails -> H3-H5 NOT_REACHED.
If H1-H2 pass -> evaluate H3-H4.
Evaluate H5 only for cable-end candidates M6, M7, M10; otherwise H5 NOT_APPLICABLE.
```

## 6. Frozen components

```text
P1: USB Type-C plug
P2: USB Type-C plug
R1: USB Type-C receptacle
R2: USB Type-C receptacle

CABLE_C2C:
  E1: USB Type-C plug end
  E2: USB Type-C plug end
```

Every listed component identity is individually admitted as a Type-C plug/receptacle/cable-end component in the frozen task. Individual admission does not imply arbitrary direct composability.

## 7. Frozen candidates and expected results

```text
M1
  composition: P1 -> R1
  orientation: ORIENTATION_A
  functional-role claim: none
  expected: admissible / NONE

M2
  composition: P1 -> R1
  orientation: ORIENTATION_B
  functional-role claim: none
  expected: admissible / NONE

M3
  composition: P1 -> R1
  orientation: INVALID_90_DEG
  functional-role claim: none
  expected: rejected / {H2}
  H3-H5: NOT_REACHED

M4
  composition: P1 -> P2 direct
  expected: rejected / {H1}
  H2-H5: NOT_REACHED

M5
  composition: R1 -> R2 direct
  expected: rejected / {H1}
  H2-H5: NOT_REACHED

M6
  composition:
    E1 -> R1 in ORIENTATION_A
    E2 -> R2 in ORIENTATION_B
  functional-role claim: none
  expected: admissible / NONE
  H5: PASS

M7
  composition:
    E2 -> R1 in ORIENTATION_A
    E1 -> R2 in ORIENTATION_B
  functional-role claim: none
  expected: admissible / NONE
  H5: PASS
  rationale: cable direction/end assignment is reversed without creating a physical mating incompatibility

M8
  composition: P1 -> R1 in ORIENTATION_A
  declared additional target:
    Source/Sink relationship is established solely by mechanical mating geometry
  expected: rejected / {H4}

M9
  composition: P1 -> R1 in ORIENTATION_B
  declared additional target:
    host/device data relationship is established solely by mechanical mating geometry
  expected: rejected / {H4}

M10
  composition:
    E2 -> R1 in ORIENTATION_B
    E1 -> R2 in ORIENTATION_A
  declared additional target:
    swapping cable direction also reverses/establishes Source/Sink role solely from cable direction
  expected: rejected / {H4}
  H5: PASS
```

Expected admissible family:

```text
SYNTHESIS_ADMISSIBLE_FAMILY:
{M1,M2,M6,M7}
```

Expected ledgers:

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

## 8. Frozen scope guards

```text
PHYSICAL_TYPE_C_MATING_ADMISSIBLE
!= COMPLETE_USB_FUNCTIONAL_INTEROPERABILITY

PHYSICAL_TYPE_C_MATING_ADMISSIBLE
!= USB_IF_CERTIFICATION

REVERSIBLE_PLUG_ORIENTATION
!= ARBITRARY_ROTATIONAL_SYMMETRY

REVERSIBLE_CABLE_DIRECTION
!= POWER_ROLE_SYMMETRY

MECHANICAL_CONNECTION
!= CC_NEGOTIATION_OR_ROLE_DETECTION

SINGLE_EXTERNAL_APPLICATION_PASS_OR_FAIL
!= METHOD_SURVIVAL_MERGER_OR_DELETION_DECISION
```

## 9. Precommitted scoring

Total required checks: **44**.

```text
A. source / precommit integrity: 8
  A1 Release-2.0 authority fixed
  A2 exact source scope fixed
  A3 supporting USB-IF overview fixed
  A4 candidate basis M1-M10 fixed
  A5 coverage fixed to ten-candidate fixture
  A6 H1-H5 and staging fixed
  A7 target resolution fixed
  A8 no baseline; method gain fixed NOT_ASSESSED

B. exact candidate verdict/failure checks: 10
  B1-B10 exact M1-M10 verdict and failure-set behavior

C. physical-interface discipline: 12
  C1 M1 orientation A admitted
  C2 M2 orientation B admitted
  C3 M3 invalid quarter-turn rejected
  C4 M4 plug-plug direct mating rejected
  C5 M5 receptacle-receptacle direct mating rejected
  C6 M6 cable-end assignment admitted
  C7 M7 swapped cable-end assignment admitted
  C8 M8 mechanical mating not upgraded to Source/Sink establishment
  C9 M9 mechanical mating not upgraded to host/device establishment
  C10 M10 cable-direction reversibility not upgraded to Source/Sink symmetry
  C11 H1 failure preserves downstream NOT_REACHED
  C12 H2 failure preserves downstream NOT_REACHED

D. closure / protocol ledgers: 8
  D1 family exactly {M1,M2,M6,M7}
  D2 terminal SYNTHESIS_ADMISSIBLE
  D3 conformance CONFORMANT
  D4 gain NOT_ASSESSED
  D5 exhaustive claim limited to frozen fixture
  D6 no Design/Optimization/Transformation/Aggregation claim absorbed
  D7 no temporal insertion-force/durability process claim
  D8 no current Release-2.5 compliance claim

E. external-scope / method-independence discipline: 6
  E1 physical mating not upgraded to functional USB interoperability
  E2 physical mating not upgraded to certification
  E3 reversible orientation not upgraded to arbitrary rotational symmetry
  E4 cable direction not upgraded to power/data role symmetry
  E5 pass/fail does not decide method survival/merger/deletion
  E6 external domain counted as physical connector assembly, materially distinct from URI syntax and SI unit algebra
```

Decision:

```text
44/44 -> EXTERNAL_APPLICATION_VERDICT: PASS
otherwise -> EXTERNAL_APPLICATION_VERDICT: FAIL
```

## 10. Evidence-count lock

Before execution:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
EXTERNAL_SYNTHESIS_APPLICATIONS: 2
EXTERNAL_SYNTHESIS_DOMAINS: 2
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 2
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

A 44/44 PASS may add exactly:

```text
EXTERNAL_SYNTHESIS_APPLICATION_INCREMENT: +1
EXTERNAL_SYNTHESIS_DOMAIN_INCREMENT: +1
EXTERNAL_SYNTHESIS_APPLICATION_PASS_INCREMENT: +1
```

It does not increase constructed direct-pilot or reproducibility counts and does not establish independent validation, practical superiority, current-standard certification, or maturity.
