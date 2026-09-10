# SYN-APP-003 Result / USB Type-C Physical Mating External Application

Status: **EXECUTED — 44/44 PASS**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Precommit commit: `4159872ad761f1fe06a784e1771a9b5ac994bff8`  
Precommit blob: `0cfe2711c49e4a249751200dddaec357f2736ce9`

## 1. Evidence identity

```text
CASE_ID: SYN-APP-003
CASE_CLASS: external_application
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
EXTERNAL_DOMAIN: physical connector assembly / USB Type-C mating interface
FROZEN_EXTERNAL_STANDARD:
  USB Type-C Cable and Connector Specification Release 2.0 (August 2019),
  mechanical mating and attach/orientation clauses only
SUPPORTING_SOURCE:
  USB-IF Type-C overview
BASELINE: none
```

The immutable precommit was fetched from its commit before execution. Candidate identities, expected verdicts, source scope, target resolution, hard conditions, staging, and scoring were not changed after precommit.

This application does not claim conformance to the newer current Type-C release. The frozen application is version-specific to the Release-2.0 mechanical subset.

## 2. External-rule reconstruction

The frozen USB-IF source subset supports the following application-level rules:

```text
R1 Type-C direct connector mating is a plug-to-receptacle interface.
R2 The Type-C plug admits two insertion orientations in the receptacle.
R3 Reversible Type-C cable direction does not make cable-end assignment a physical mating incompatibility by itself.
R4 CC/electrical configuration is used to detect orientation and establish functional relationships.
R5 Mechanical Type-C connector geometry by itself does not inherently establish Source/Sink or host/device relationships.
```

These are used only at the declared static physical-interface resolution.

## 3. Candidate execution

### M1 — plug/receptacle, orientation A

```text
H1 PASS
H2 PASS
H3 PASS
H4 PASS
H5 NOT_APPLICABLE
RESULT: admissible
FAILURE_SET: NONE
```

### M2 — plug/receptacle, orientation B

```text
H1 PASS
H2 PASS
H3 PASS
H4 PASS
H5 NOT_APPLICABLE
RESULT: admissible
FAILURE_SET: NONE
```

Both externally admitted Type-C insertion orientations remain distinct insertion-state records while remaining mechanically admissible.

### M3 — plug/receptacle, invalid quarter-turn insertion

```text
H1 PASS
H2 FAIL
H3-H5 NOT_REACHED
RESULT: rejected
FAILURE_SET: {H2}
```

Reversible orientation was not generalized into arbitrary rotational symmetry.

### M4 — direct plug-to-plug mating

```text
H1 FAIL
H2-H5 NOT_REACHED
RESULT: rejected
FAILURE_SET: {H1}
```

### M5 — direct receptacle-to-receptacle mating

```text
H1 FAIL
H2-H5 NOT_REACHED
RESULT: rejected
FAILURE_SET: {H1}
```

Individual Type-C component admission therefore does not imply arbitrary Type-C-to-Type-C direct composability.

### M6 — Type-C-to-Type-C cable, E1/E2 assignment

```text
E1 -> R1 ORIENTATION_A: H1-H3 PASS
E2 -> R2 ORIENTATION_B: H1-H3 PASS
H4 PASS
H5 PASS
RESULT: admissible
FAILURE_SET: NONE
```

### M7 — same cable with E1/E2 swapped

```text
E2 -> R1 ORIENTATION_A: H1-H3 PASS
E1 -> R2 ORIENTATION_B: H1-H3 PASS
H4 PASS
H5 PASS
RESULT: admissible
FAILURE_SET: NONE
```

The cable-end swap changes the recorded assignment but is not a physical Type-C mating incompatibility.

### M8 — mechanical mating plus Source/Sink inferred solely from geometry

```text
H1 PASS
H2 PASS
H3 PASS
H4 FAIL
H5 NOT_APPLICABLE
RESULT: rejected
FAILURE_SET: {H4}
```

The mechanically valid connector pair was not upgraded into a power-role determination.

### M9 — mechanical mating plus host/device role inferred solely from geometry

```text
H1 PASS
H2 PASS
H3 PASS
H4 FAIL
H5 NOT_APPLICABLE
RESULT: rejected
FAILURE_SET: {H4}
```

The mechanically valid connector pair was not upgraded into a data-role determination.

### M10 — reversible cable direction plus Source/Sink symmetry claim

```text
E2 -> R1 ORIENTATION_B: H1-H3 PASS
E1 -> R2 ORIENTATION_A: H1-H3 PASS
H4 FAIL
H5 PASS
RESULT: rejected
FAILURE_SET: {H4}
```

This preserves the important distinction that physical cable-direction reversibility does not itself determine or reverse Source/Sink roles.

## 4. Closure

```text
SYNTHESIS_ADMISSIBLE_FAMILY:
{M1,M2,M6,M7}
```

Rejected family:

```text
M3  -> {H2}
M4  -> {H1}
M5  -> {H1}
M8  -> {H4}
M9  -> {H4}
M10 -> {H4}; H5 PASS
```

No candidate outside the frozen ten-candidate fixture was used to support exhaustiveness.

## 5. Structural distinctions retained

```text
TYPE_C_COMPONENT_ADMITTED
!= DIRECTLY_MATEABLE_WITH_ANY_TYPE_C_COMPONENT

REVERSIBLE_PLUG_ORIENTATION
!= ARBITRARY_ROTATIONAL_SYMMETRY

MECHANICAL_MATING
!= SOURCE_SINK_ROLE_ESTABLISHMENT

MECHANICAL_MATING
!= HOST_DEVICE_ROLE_ESTABLISHMENT

REVERSIBLE_CABLE_DIRECTION
!= POWER_ROLE_SYMMETRY
```

The application also preserves prerequisite staging:

```text
H1 failure -> H2-H5 NOT_REACHED
H2 failure -> H3-H5 NOT_REACHED
```

Thus downstream whole-level claims are not fabricated after a more basic physical-interface failure.

## 6. Three-ledger result

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No comparative baseline was activated.

## 7. Precommitted scoring

```text
A. source / precommit integrity          8 / 8 PASS
B. exact candidate verdicts            10 / 10 PASS
C. physical-interface discipline       12 / 12 PASS
D. closure / protocol ledgers           8 / 8 PASS
E. external-scope / independence        6 / 6 PASS

PRECOMMITTED_REQUIRED_CHECKS:          44
PASSED:                                44
FAILED:                                 0
EXTERNAL_APPLICATION_VERDICT:        PASS
```

No scoring item was weakened or deleted after execution.

## 8. Evidence increment

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: remains 6
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
REPRODUCIBILITY_CASES: remains 1
DEDICATED_RETRACE_PASSES: remains 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

The three external domains are now:

```text
1. Internet identifier syntax / RFC 3986 generic URI composition
2. Physical metrology / BIPM SI unit composition
3. Physical connector assembly / USB Type-C mating interface
```

## 9. Protocol pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_COLLAPSE_OR_SURVIVAL_DECISION_FROM_THIS_CASE: none
```

The application did not expose a Protocol-v0.1 contradiction or require Synthesis to absorb Design, Transformation, Aggregation, Optimization, Measurement, or Dynamics.

## 10. Scope limits

This result does not establish:

```text
current USB Type-C Release-2.5 conformance
USB-IF product certification
USB Power Delivery negotiation success
USB4 or data-rate capability
complete electrical interoperability
signal-integrity performance
connector durability
insertion-force compliance
independent replication
method superiority
method maturity
```

The next internal step is a first Synthesis maturity audit using the now-populated direct, baseline, external, and retrace evidence architecture. Such an audit must treat method survival/merger/deletion as a separate structural question rather than as a direct consequence of pass/fail counts.
