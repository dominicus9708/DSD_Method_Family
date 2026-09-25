# DSD Aggregation Task Interface v0.1 Draft

Status: **HISTORICAL DRAFT — PRE-PROTOCOL**
Date: **2026-09-25**
Method: **Aggregation / DSD 집계론**
Legacy path ID: `10A`

## 1. Atomic task

Given already-admitted channel data and/or already-defined typed property data, construct a declared aggregate readout under an explicit aggregation map and domain, while preserving the distinction between the reduced output and any support/status information required to interpret it.

Aggregation does not by itself reconstruct the source support.

## 2. Claim levels

Every task freezes exactly one primary claim level:

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

A task may include subordinate checks at other levels, but the maximum claim must remain tied to the frozen primary claim level.

## 3. Required task lock

Before evaluation, freeze:

```text
AGGREGATION_TASK_ID
AGGREGATION_TASK_VERSION

PRIMARY_CLAIM_LEVEL

SOURCE_INTERFACE_ID
SOURCE_INTERFACE_VERSION_OR_DOCUMENT

FORMATION_BACKGROUND_ID
  when formation channels are used

PROPERTY_MODEL_ID
  when property data are used

INPUT_SUPPORT_OR_SELECTION
AGGREGATION_DOMAIN_CLASS
AGGREGATION_MAP_ID
AGGREGATION_MAP_VERSION_OR_DEFINITION

OUTPUT_SPACE_AND_TYPE

SUPPORT_RETENTION_POLICY
NEGATIVE_STATUS_SIDECAR_POLICY

INJECTIVITY_OR_RECONSTRUCTION_CLAIM:
  none
  test_required
  assumed_by_external_contract

COUNTABLE_EXTENSION_REQUESTED:
  yes / no

POSTPROCESSING_REQUESTED:
  yes / no

MAXIMUM_SUPPORTED_CLAIM
```

Changing a claim-relevant lock after seeing the result requires a new task version.

## 4. Formation-channel input interface

When channel aggregation is used, record:

```text
ADMITTED_CHANNEL_SET:
  C_L

SELECTED_FINITE_SUPPORT:
  F subset C_L

for each c in F:
  channel identity
  realization / component-term source
  component term T(c)
  term provenance
  term-space type
```

If a selected object is not in the admitted channel set:

```text
T(c):
  undefined
```

Do not zero-extend it.

If an admitted channel has a defined zero term:

```text
CHANNEL_STATUS:
  present

TERM_STATUS:
  defined_zero
```

This is distinct from channel absence.

## 5. Formation-compatible core aggregate

For a finite selected support:

```text
Comp(F)
  =
sum_{c in F} T(c)
```

The method records:

```text
support F
component-term ledger
summation map
aggregate value
output space
bound/stability data when claimed
```

The direct Formation-compatible readout is the declared finite sum.

A normalized cross-channel average is separate postprocessing unless independently declared by the application.

## 6. Optional countable extension

Countable aggregation is not silently substituted for the finite core.

When requested, freeze:

```text
COUNTABLE_SUPPORT:
  finite_or_countable

ABSOLUTE_SUMMABILITY_CHECK:
  required

ENUMERATION_INDEPENDENCE_CLAIM:
  only after absolute/unconditional convergence condition is met
```

Conditionally convergent or uncountable aggregation is outside the current source-defined core unless a later protocol explicitly supplies a new justified interface.

## 7. Typed-property input interface

When property aggregation is used, freeze:

```text
DEFINED_TYPED_PROPERTY_CARRIER:
  R^prop_A

SELECTED_CARRIER:
  I_A subset R^prop_A

SELECTED_FINITE_PROPERTY_SUPPORT:
  G subset I_A

PROPERTY_BRIDGE:
  Theta_A : I_A -> U_A

for each selected datum:
  property kind
  complete ordered typed input
  defined value
  bridge image
  provenance
```

The following statuses are not inserted into the defined carrier by zero-padding:

```text
undeclared
profile unavailable
inapplicable
prerequisite-unsatisfied
applicable but undefined
```

A defined zero remains an admitted defined datum.

## 8. Multi-input property guard

For a typed property datum with multiple input coordinates:

```text
MULTI_INPUT_PROPERTY:
  retains its complete typed input
```

No coordinate becomes a canonical channel owner unless an explicit application-level selector/allocation rule is supplied and frozen.

## 9. Typed-property aggregate

For finite G:

```text
Agg(G)
  =
sum_{iota in G} Theta_A(iota)
```

Record separately:

```text
selected property support G
bridge identity
bridge-output ledger
aggregate value
output space
property-kind/input distinctions retained in sidecar when required
```

## 10. Combined static descriptor

When both coordinates are requested:

```text
Static(F,G)
  =
(Comp(F), Agg(G))
```

Required guard:

```text
FORMATION_COORDINATE
  !=
PROPERTY_COORDINATE
```

The ordered pair does not identify the logical roles of the two coordinates.

## 11. Support-retaining record

When support interpretation or later reconstruction matters, retain:

```text
CHANNEL_SUPPORT_DATA:
  {(c,T(c)) : c in F}

PROPERTY_SUPPORT_DATA:
  {(iota,Theta_A(iota)) : iota in G}
```

A reduced aggregate may be emitted without these sidecars only when the task explicitly does not claim source/support reconstruction.

## 12. Collision and injectivity interface

For a fixed finite channel support F, a reconstruction claim requires an injectivity check on the declared admissible assignment class.

The source criterion is represented methodologically as:

```text
AGGREGATION_OPERATOR:
  S_F

ADMISSIBLE_ASSIGNMENT_CLASS:
  A_F

INJECTIVITY_STATUS:
  established
  not_established
  blocked
  out_of_scope
```

Aggregate equality alone is not evidence of source equality.

If collision witnesses exist:

```text
same aggregate
different support-resolved/source-resolved data
```

record them explicitly.

## 13. Stability claims

Static perturbation or norm bounds may be recorded only when their assumptions are supplied.

Required guard:

```text
STATIC_ANALYTIC_STABILITY
  !=
DYNAMICAL_STABILITY
```

No physical evolution law is inferred from a static aggregation bound.

## 14. Postprocessing

Any later map:

```text
P : aggregate_output -> Z
```

is a separate postprocessing layer.

Examples:

```text
normalized average
scalar projection
thresholding
ranking
display formatting
compression
```

Do not rewrite the core aggregation task as the postprocessing task.

## 15. Specialized scalar readout

A one-channel scalar weighted readout such as the weighted structural descriptor may be recorded as a specialization when its metric-measure and local-scaling assumptions are supplied.

Required guard:

```text
SPECIALIZED_WEIGHTED_READOUT
  !=
GENERAL_AGGREGATION_DEFINITION

READOUT_EQUALITY
  !=
UNDERLYING_STATE_IDENTITY
```

## 16. Primary result statuses

Draft result statuses:

```text
AGGREGATION_ESTABLISHED

AGGREGATION_NOT_ESTABLISHED

AGGREGATION_BLOCKED

AGGREGATION_CONFLICTING

AGGREGATION_OUT_OF_SCOPE

AGGREGATION_UNDERDETERMINED
```

These are task-level evidence statuses.

They do not replace the source-level Formation or Property object/status distinctions.

## 17. Collision / information-loss statuses

```text
COLLISION_NOT_TESTED

COLLISION_WITNESS_ESTABLISHED

NO_COLLISION_ON_TESTED_CLASS

INJECTIVITY_ESTABLISHED_ON_DECLARED_CLASS

INJECTIVITY_NOT_ESTABLISHED

INJECTIVITY_BLOCKED
```

`NO_COLLISION_ON_TESTED_CLASS` is not global injectivity.

## 18. Task terminals

Draft terminals:

```text
AGGREGATION_TASK_ESTABLISHED
AGGREGATION_TASK_PARTIAL
AGGREGATION_TASK_NOT_ESTABLISHED
AGGREGATION_TASK_BLOCKED
AGGREGATION_TASK_CONFLICTING
AGGREGATION_TASK_OUT_OF_SCOPE
AGGREGATION_TASK_UNDERDETERMINED
```

Terminal precedence is intentionally not yet frozen.

It is a target of the pre-protocol boundary attack.

## 19. Five-interface method identity

### INPUTS

```text
already-admitted channel terms and/or
already-defined selected typed property data
+
explicit aggregation map/domain/support policy
```

### OPERATION

```text
combine the selected values under the declared aggregation operator
while preserving required support/status/injectivity metadata
```

### OUTPUTS

```text
aggregate value/readout
aggregation ledger
support sidecar when required
collision/injectivity status
bounded maximum-supported claim
```

### FAILURE / NO-GAIN CONDITIONS

```text
required input undefined
required bridge/map unavailable
domain assumptions fail
countable extension lacks required convergence
claim exceeds support/injectivity evidence
baseline matches claim-relevant outputs
```

### VALIDATION STANDARD

```text
correct execution of the declared aggregation map
+
preservation of source status distinctions
+
correct collision/injectivity bounds
+
no unsupported reconstruction or identity inference
```

## 20. Neighboring-method guards

```text
AGGREGATION != MEASUREMENT
AGGREGATION != COMPRESSION
AGGREGATION != RECONSTRUCTION
AGGREGATION != COMPARISON
AGGREGATION != CLASSIFICATION
AGGREGATION != TRACKING
AGGREGATION != LINEAGE

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
COLLISION_TEST != RECONSTRUCTION
INJECTIVITY_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
```

## 21. Pre-protocol open points

The boundary attack must test at least:

```text
same aggregate / different channel support
same aggregate / different typed-property support
defined zero versus absence
undefined property versus defined zero
multi-input property allocation
direct sum versus weighted average
finite core versus countable extension
conditionally convergent countable case
formation/property coordinate conflation
postprocessing conflation
support sidecar omission
fixed-support injectivity claim
cross-coordinate reconstruction claim
static stability versus dynamic stability
D_w specialization overclaim
aggregation versus compression
aggregation versus reconstruction
aggregation versus measurement
```

No Protocol v0.1 may be frozen until these attacks are evaluated.
