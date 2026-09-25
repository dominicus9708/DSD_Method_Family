# DSD Aggregation Protocol v0.1

Status: **FROZEN EXECUTABLE INTERNAL PROTOCOL**  
Date: **2026-09-25**  
Method: **Aggregation / DSD 집계론**  
Legacy path ID: `10A`

## 1. Frozen lineage of this protocol

```text
TASK_INTERFACE_COMMIT:
  58287d8b4d200c55860c5029281699de0750a5d4
TASK_INTERFACE_BLOB:
  0eb42ab35703b4ac684ddd0fa477289dd944a3f0

BOUNDARY_ATTACK_COMMIT:
  59eefe5347b8509c097ee69ec488fcfe808849e9
BOUNDARY_ATTACK_BLOB:
  5deb99c973c8c89b4aead5d588d88b525daa534c

AMENDMENT_COMMIT:
  a327688f71e336cd458490dda1c6a786ee59be4c
AMENDMENT_BLOB:
  7bbbb7837de21d4628e9b4bf36f6ac725198ddab
```

This protocol operationalizes the frozen Task Interface plus Boundary Amendment 001.

It does not replace or redefine the mathematical source layer.

## 2. Atomic method task

Given already-admitted channel data and/or already-defined typed property data, execute a declared aggregation operation on a frozen domain and emit:

```text
aggregate/readout value
aggregation-domain ledger
support/status sidecar when required
collision/injectivity status
reconstruction-scope status when claimed
protocol-conformance status
method-gain status
maximum-supported claim
```

Aggregation is not source reconstruction by default.

## 3. Claim levels

```text
FORMATION_CHANNEL_AGGREGATE
PROPERTY_AGGREGATE
COMBINED_STATIC_DESCRIPTOR
COUNTABLE_ANALYTIC_EXTENSION
SPECIALIZED_SCALAR_READOUT
AGGREGATE_INJECTIVITY
AGGREGATE_STABILITY
POSTPROCESSED_READOUT
```

Exactly one primary claim level is frozen per task.

## 4. Validity gates G1-G16

### G1 — task/version/claim lock

Freeze:

```text
task ID
task version
primary claim level
maximum-supported claim
```

No post-hoc task rewriting.

### G2 — source/interface lock

Freeze every claim-relevant source interface, document/version, formation background, property model, bridge, selector, and postprocessing map.

### G3 — input-status discipline

Preserve source status distinctions.

```text
ABSENT_CHANNEL != ADMITTED_DEFINED_ZERO_TERM
UNDEFINED_PROPERTY != DEFINED_ZERO_PROPERTY
```

No zero-padding of undefined data.

### G4 — aggregation-domain/map lock

Freeze:

```text
selected support/selection
domain class
aggregation operator
output space/type
```

The direct source-defined finite channel aggregate is the unnormalized finite sum.

### G5 — formation finite-core discipline

For `FORMATION_CHANNEL_AGGREGATE`, every selected channel must be admitted and every required component term must be defined.

A normalized average is not silently substituted for the direct finite sum.

### G6 — property aggregation discipline

Only explicitly selected defined typed property data may enter the property aggregate.

Complete typed inputs remain attached to each selected datum.

### G7 — multi-input allocation discipline

A multi-input property datum has no canonical single-channel owner unless an explicit frozen selector/allocation rule is supplied.

### G8 — countable-extension discipline

A countable extension is allowed only when explicitly requested and its source-defined convergence condition is established.

The finite core is not silently redefined.

### G9 — coordinate-separation discipline

For a combined static descriptor:

```text
FORMATION_COORDINATE != PROPERTY_COORDINATE
```

Equal numerical values do not identify their logical roles.

### G10 — support-retention discipline

If a frozen claim needs source/support identification, required support/status sidecars must be available.

Required unavailable sidecar:

```text
-> BLOCKED
```

### G11 — collision/injectivity discipline

Freeze:

```text
support
summation/aggregation operator
admissible assignment class
injectivity claim level
```

No local/no-collision test may be promoted to global injectivity.

### G12 — reconstruction-scope discipline

Freeze:

```text
not_claimed
fixed_support
variable_support
combined_coordinate
```

Fixed-support injectivity does not imply variable-support reconstruction.

### G13 — cross-coordinate reconstruction discipline

For combined reconstruction, freeze whether a cross-coordinate condition is:

```text
not_required
supplied
required_but_unavailable
unresolved
```

### G14 — stability/postprocessing discipline

Static analytic perturbation bounds remain static.

Any downstream reduction/average/projection/ranking/compression is separately identified as postprocessing.

### G15 — specialized-readout discipline

A weighted scalar readout such as `D_w` is a specialization under its own assumptions.

```text
READOUT_EQUALITY != SOURCE_IDENTITY
SPECIALIZED_READOUT != GENERAL_AGGREGATION_DEFINITION
```

### G16 — status/terminal/max-claim discipline

Apply exact task statuses, frozen terminal precedence, protocol-conformance rules, and bounded maximum-supported claims.

No neighboring-method result is silently promoted to an Aggregation result.

## 5. Binding operation T1-T16

### T1 — freeze task

Instantiate G1.

### T2 — bind sources and interfaces

Instantiate G2.

### T3 — build source-status ledger

Record absent/undefined/defined-zero/defined-nonzero distinctions before aggregation.

### T4 — freeze domain and operator

Record selected support/selection, operator, output type, and direct/postprocessed distinction.

### T5 — evaluate formation-side inputs

For channel aggregation:

```text
admitted channel?
component term defined?
term provenance available?
```

### T6 — evaluate property-side inputs

For property aggregation:

```text
datum is defined typed property data?
complete typed input retained?
bridge image defined?
```

### T7 — evaluate selector/allocation claims

Reject implicit ownership of multi-input data.

### T8 — evaluate finite/countable domain

For countable claims, verify the required absolute/unconditional convergence condition.

### T9 — compute declared aggregate

Compute only the frozen operator on the frozen domain.

### T10 — emit support/status sidecar

Retain support-resolved data when required by the frozen claim.

### T11 — evaluate collision/injectivity

If requested, evaluate the frozen declared class.

Record collision witnesses without upgrading absence of a witnessed collision to global injectivity.

### T12 — evaluate reconstruction scope

Keep fixed-support, variable-support, and combined-coordinate claims separate.

### T13 — evaluate cross-coordinate condition

For combined reconstruction, apply only the frozen condition.

### T14 — evaluate stability/postprocessing/specialization

Keep static bounds, postprocessing, and scalar specializations separated from core aggregation.

### T15 — assign statuses and terminal

Apply the status families and frozen terminal precedence.

### T16 — emit conformance/gain/max claim

Emit protocol conformance, method-gain status, and bounded maximum-supported claim.

## 6. Source-status ledger

Allowed source-input statuses include:

```text
CHANNEL_ABSENT
CHANNEL_PRESENT_TERM_DEFINED_ZERO
CHANNEL_PRESENT_TERM_DEFINED_NONZERO
CHANNEL_TERM_UNDEFINED

PROPERTY_UNDECLARED
PROPERTY_PROFILE_UNAVAILABLE
PROPERTY_INAPPLICABLE
PROPERTY_PREREQUISITE_UNSATISFIED
PROPERTY_APPLICABLE_UNDEFINED
PROPERTY_DEFINED_ZERO
PROPERTY_DEFINED_NONZERO
```

These are source/object statuses, not task-terminal labels.

## 7. Aggregation-domain statuses

```text
AGGREGATION_DOMAIN_ADMITTED
AGGREGATION_DOMAIN_NOT_ADMITTED
AGGREGATION_DOMAIN_BLOCKED
AGGREGATION_DOMAIN_CONFLICTING
AGGREGATION_DOMAIN_UNDERDETERMINED
AGGREGATION_DOMAIN_OUT_OF_SCOPE
```

## 8. Collision statuses

```text
COLLISION_NOT_TESTED
COLLISION_WITNESS_ESTABLISHED
NO_COLLISION_ON_TESTED_CLASS
```

Required guard:

```text
NO_COLLISION_ON_TESTED_CLASS
  !=
GLOBAL_INJECTIVITY
```

## 9. Injectivity statuses

```text
INJECTIVITY_NOT_TESTED
INJECTIVITY_ESTABLISHED_ON_DECLARED_CLASS
INJECTIVITY_NOT_ESTABLISHED
INJECTIVITY_BLOCKED
INJECTIVITY_CONFLICTING
INJECTIVITY_UNDERDETERMINED
INJECTIVITY_OUT_OF_SCOPE
```

## 10. Reconstruction-scope statuses

```text
RECONSTRUCTION_NOT_CLAIMED
RECONSTRUCTION_FIXED_SUPPORT
RECONSTRUCTION_VARIABLE_SUPPORT
RECONSTRUCTION_COMBINED_COORDINATE
```

A reconstruction-scope label is not itself a reconstruction success result.

## 11. Primary task statuses

```text
AGGREGATION_ESTABLISHED
AGGREGATION_NOT_ESTABLISHED
AGGREGATION_BLOCKED
AGGREGATION_CONFLICTING
AGGREGATION_OUT_OF_SCOPE
AGGREGATION_UNDERDETERMINED
```

## 12. Task terminals

```text
AGGREGATION_TASK_ESTABLISHED
AGGREGATION_TASK_PARTIAL
AGGREGATION_TASK_NOT_ESTABLISHED
AGGREGATION_TASK_BLOCKED
AGGREGATION_TASK_CONFLICTING
AGGREGATION_TASK_OUT_OF_SCOPE
AGGREGATION_TASK_UNDERDETERMINED
```

Frozen precedence:

```text
OUT_OF_SCOPE
>
CONFLICTING
>
UNDERDETERMINED
>
BLOCKED
>
ESTABLISHED / PARTIAL / NOT_ESTABLISHED
```

`PARTIAL` requires multiple independent required obligations.

It may not rescue one failed atomic aggregation proposition.

## 13. Protocol conformance

```text
AGGREGATION_PROTOCOL_CONFORMANT

AGGREGATION_PROTOCOL_NONCONFORMANT

AGGREGATION_PROTOCOL_INDETERMINATE
```

A negative, blocked, conflicting, out-of-scope, or underdetermined task result may still be protocol-conformant.

## 14. Method-gain statuses

```text
AGGREGATION_METHOD_GAIN_ESTABLISHED
AGGREGATION_METHOD_GAIN_PARTIAL
AGGREGATION_METHOD_GAIN_NO_GAIN
AGGREGATION_METHOD_GAIN_NOT_ASSESSED
AGGREGATION_METHOD_GAIN_UNDERDETERMINED
```

```text
NO_GAIN != METHOD_FAILURE
```

## 15. Required output schema

Each execution record must contain, as applicable:

```text
TASK_LOCK

SOURCE_INTERFACE_LOCK

SOURCE_STATUS_LEDGER

AGGREGATION_DOMAIN_LEDGER

CHANNEL_TERM_LEDGER

PROPERTY_DATA_LEDGER

SELECTOR_ALLOCATION_LEDGER

AGGREGATION_OPERATOR

DIRECT_AGGREGATE_OUTPUT

COUNTABLE_EXTENSION_LEDGER

COMBINED_COORDINATE_LEDGER

SUPPORT_STATUS_SIDECAR

COLLISION_LEDGER

INJECTIVITY_LEDGER

RECONSTRUCTION_SCOPE_LEDGER

CROSS_COORDINATE_CONDITION_LEDGER

STABILITY_LEDGER

POSTPROCESSING_LEDGER

SPECIALIZED_READOUT_LEDGER

PRIMARY_TASK_STATUS

TASK_TERMINAL_STATUS

PROTOCOL_CONFORMANCE

METHOD_GAIN_STATUS

MAXIMUM_SUPPORTED_CLAIM
```

Not every optional ledger must be populated, but every omitted optional ledger must be marked `NOT_APPLICABLE` or `NOT_REQUESTED` rather than silently absent if it is claim-relevant.

## 16. Core guards

```text
AGGREGATE_EQUALITY != SOURCE_IDENTITY
AGGREGATE_EQUALITY != SUPPORT_EQUALITY
AGGREGATE_INEQUALITY != AUTOMATIC_SOURCE_NONIDENTITY

DEFINED_ZERO != ABSENCE
UNDEFINED != ZERO

PROPERTY_AGGREGATE != FORMATION_COMPOSITE
MULTI_INPUT_PROPERTY != SINGLE_CHANNEL_OWNERSHIP

DIRECT_FINITE_SUM != NORMALIZED_AVERAGE
FINITE_CORE != COUNTABLE_EXTENSION

SUPPORT_RETENTION != REDUCED_AGGREGATE

FIXED_SUPPORT_INJECTIVITY != VARIABLE_SUPPORT_RECONSTRUCTION
COORDINATEWISE_INJECTIVITY != AUTOMATIC_CROSS_COORDINATE_RECONSTRUCTION

STATIC_ANALYTIC_STABILITY != DYNAMICAL_STABILITY

SPECIALIZED_WEIGHTED_READOUT != GENERAL_AGGREGATION_DEFINITION
READOUT_EQUALITY != UNDERLYING_STATE_IDENTITY

AGGREGATION != MEASUREMENT
AGGREGATION != COMPRESSION
AGGREGATION != RECONSTRUCTION
AGGREGATION != COMPARISON
AGGREGATION != CLASSIFICATION
AGGREGATION != TRACKING
AGGREGATION != LINEAGE
```

## 17. Maximum-supported claim rule

A valid output may claim only what follows from the frozen domain/operator/status/support/injectivity/reconstruction data.

Examples:

```text
allowed:
  aggregate value on declared support
  static norm/stability bound under declared assumptions
  collision witness on declared fixture
  injectivity on declared admissible class

not automatically allowed:
  unique source support
  source identity
  hidden negative-property status recovery
  dynamical stability
  physical constitutive law
  global injectivity
  independent validation
```

## 18. Current protocol state

```text
DEDICATED_AGGREGATION_PROTOCOL:
  established v0.1

VALIDITY_GATES:
  G1-G16

BINDING_OPERATION:
  T1-T16

DIRECT_AGGREGATION_PILOTS_ATTEMPTED:
  0

SUCCESSFUL_DIRECT_AGGREGATION_PILOTS:
  0

AGGREGATION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_AGGREGATION_EVIDENCE_STATUS:
  protocol_frozen

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 19. Next

Prospectively precommit and execute the first positive constructed Aggregation challenge without rewriting this protocol.
