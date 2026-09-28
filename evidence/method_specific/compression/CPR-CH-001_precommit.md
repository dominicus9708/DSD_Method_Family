# CPR-CH-001 — Positive Constructed Compression Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-28**  
Challenge ID: `CPR-CH-001`  
Method: **Compression / DSD 압축론**  
Protocol: **Compression Protocol v0.1**  
Case class: `positive_constructed_compression_challenge`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  b1efa06e4c715e08ce2558a608c7f09aa22172bd

PROTOCOL_BLOB:
  4d67d800e107229f91c16cf5b0235928124482b2

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18
~~~

The protocol is immutable for this challenge.

No protocol rule may be edited in response to the result.

## 2. Challenge purpose

Test whether frozen Compression Protocol v0.1 can execute one positive constructed lossy compression task that simultaneously contains:

~~~text
frozen downstream purpose
complete required-distinction relation on the tested class
explicit acceptable-collision relation
intentional lossy collision
source-status preservation
actual package-size reduction
multidimensional collision-consequence records
bounded non-reconstruction claim
no resolution dependency
no composition claim
no neighboring-method substitution
bounded maximum claim
~~~

The task deliberately permits detail loss inside purpose-safe collision classes.

It does not request source identity, exact reconstruction, global injectivity, or method-gain evidence.

## 3. Frozen task lock

~~~text
COMPRESSION_TASK_ID:
  CPR-CH-001

COMPRESSION_TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  LOSSY_WITH_DECLARED_SAFE_COLLISIONS

SOURCE_INTERFACE_ID:
  CPR-CH-001-SOURCE-v1

SOURCE_OBJECT_CLASS:
  X_CPR_001 = {x1,x2,x3,x4}

SOURCE_REPRESENTATION_ID:
  SRC-TRIPLE-v1

SOURCE_REPRESENTATION_TYPE:
  (group,detail,status)

DOWNSTREAM_PURPOSE_ID:
  PURPOSE-GROUP-STATUS-v1

PURPOSE_SCOPE:
  single

COMPRESSION_MAP_ID:
  DROP-DETAIL-v1

COMPRESSION_MAP_DEFINITION:
  C(group,detail,status) = (group,status)

REDUCED_OUTPUT_TYPE:
  (group,status)

STATUS_RETENTION_POLICY:
  required
  encoded directly in reduced output

SUPPORT_RETENTION_POLICY:
  not_required

PROVENANCE_RETENTION_POLICY:
  not_required

RESOLUTION_STATUS:
  RESOLUTION_NOT_APPLICABLE

RECONSTRUCTION_SCOPE_CLASS:
  none

COMPOSITION_CLAIM:
  not_claimed

REPRESENTATION_ACCOUNTING_SCOPE:
  output_plus_required_sidecars

REPRESENTATION_COST_METRIC:
  FIELD_UNIT_COUNT-v1

REDUCTION_DIMENSION:
  size

REDUCTION_REQUIREMENT:
  strict

MAXIMUM_SUPPORTED_CLAIM:
  on the frozen four-object class, DROP-DETAIL-v1 preserves
  every group/status distinction required by PURPOSE-GROUP-STATUS-v1,
  merges only purpose-safe same-group/same-status detail variants,
  and reduces the frozen package cost from 12 to 8 field units
~~~

No claim-relevant lock may change after this precommit.

## 4. Frozen source fixture

~~~text
x1:
  (A,a1,NONZERO)

x2:
  (A,a2,NONZERO)

x3:
  (B,b1,ZERO)

x4:
  (B,b2,ZERO)
~~~

Native source-status semantics:

~~~text
NONZERO:
  defined nonzero source state

ZERO:
  defined zero source state
~~~

No source object is absent or undefined in this positive fixture.

Source representation cost:

~~~text
4 objects
x 3 frozen fields each
=
12 FIELD_UNIT_COUNT-v1 units
~~~

## 5. Frozen purpose relation

The purpose requires preservation of:

~~~text
group
status
~~~

and explicitly declares detail to be irrelevant for this task.

Required-distinction relation:

~~~text
D_req =
  all unordered source pairs
  whose group differs
  or whose status differs
~~~

On the frozen class:

~~~text
(x1,x3)
(x1,x4)
(x2,x3)
(x2,x4)
~~~

must remain distinguishable.

Acceptable-collision relation:

~~~text
A_safe =
  all unordered distinct source pairs
  with same group and same status
~~~

On the frozen class:

~~~text
(x1,x2)
(x3,x4)
~~~

are explicitly safe to merge.

The two relations are complete for all six unordered pairs on the frozen four-object class.

Expected purpose relation:

~~~text
PURPOSE_RELATION_CONSISTENT
~~~

No pair is simultaneously required-distinct and safe-to-merge.

No claim-relevant pair is left unspecified.

## 6. Frozen compression map

~~~text
C(group,detail,status)
  =
(group,status)
~~~

Expected outputs:

~~~text
C(x1) = (A,NONZERO)
C(x2) = (A,NONZERO)

C(x3) = (B,ZERO)
C(x4) = (B,ZERO)
~~~

Expected collision witnesses:

~~~text
x1 != x2
C(x1) = C(x2)

x3 != x4
C(x3) = C(x4)
~~~

Expected non-collisions across required distinctions:

~~~text
(A,NONZERO) != (B,ZERO)
~~~

Therefore every frozen required-distinction pair remains distinguishable.

## 7. Frozen collision-consequence expectations

For collision `(x1,x2)`:

~~~text
COLLISION_PURPOSE_STATUS:
  COLLISION_PURPOSE_SAFE

COLLISION_STATUS_RETENTION_STATUS:
  COLLISION_STATUS_PRESERVED

COLLISION_SUPPORT_RETENTION_STATUS:
  COLLISION_SUPPORT_NOT_APPLICABLE

COLLISION_PROVENANCE_RETENTION_STATUS:
  COLLISION_PROVENANCE_NOT_APPLICABLE

COLLISION_RECONSTRUCTION_STATUS:
  COLLISION_RECONSTRUCTION_NOT_CLAIMED
~~~

For collision `(x3,x4)`:

~~~text
COLLISION_PURPOSE_STATUS:
  COLLISION_PURPOSE_SAFE

COLLISION_STATUS_RETENTION_STATUS:
  COLLISION_STATUS_PRESERVED

COLLISION_SUPPORT_RETENTION_STATUS:
  COLLISION_SUPPORT_NOT_APPLICABLE

COLLISION_PROVENANCE_RETENTION_STATUS:
  COLLISION_PROVENANCE_NOT_APPLICABLE

COLLISION_RECONSTRUCTION_STATUS:
  COLLISION_RECONSTRUCTION_NOT_CLAIMED
~~~

The two purpose-safe collisions intentionally erase only the frozen detail field.

## 8. Frozen representation accounting

Reduced package:

~~~text
4 reduced outputs
x 2 frozen fields each
=
8 FIELD_UNIT_COUNT-v1 units
~~~

No additional required sidecar exists.

Thus:

~~~text
SOURCE_COST:
  12

REDUCED_PACKAGE_COST:
  8

COST_REDUCTION:
  4

STRICT_REDUCTION:
  yes
~~~

Expected:

~~~text
REDUCTION_ESTABLISHED
~~~

The result may not be established merely from purpose preservation; the 12 -> 8 reduction must also be verified.

## 9. Frozen losslessness / reconstruction / composition expectations

Because collision witnesses exist on the declared source class:

~~~text
LOSSLESSNESS_STATUS:
  LOSSLESSNESS_NOT_ESTABLISHED
~~~

This is intentional and does not invalidate the frozen lossy claim.

Reconstruction:

~~~text
RECONSTRUCTION_STATUS:
  RECONSTRUCTION_NOT_CLAIMED
~~~

Composition:

~~~text
COMPOSITION_STATUS:
  COMPOSITION_NOT_CLAIMED
~~~

Resolution:

~~~text
RESOLUTION_STATUS:
  RESOLUTION_NOT_APPLICABLE
~~~

Property-correlation ledger:

~~~text
NOT_APPLICABLE
~~~

Projection/readout ledger:

~~~text
NOT_APPLICABLE
~~~

Neighbor-method sidecar ledger:

~~~text
NOT_REQUESTED
~~~

## 10. Frozen expected task result

~~~text
PURPOSE_RELATION_STATUS:
  PURPOSE_RELATION_CONSISTENT

COMPRESSION_DOMAIN_STATUS:
  COMPRESSION_DOMAIN_ADMITTED

REDUCTION_STATUS:
  REDUCTION_ESTABLISHED

PRIMARY_TASK_STATUS:
  COMPRESSION_ESTABLISHED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_ESTABLISHED

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT

METHOD_GAIN_STATUS:
  COMPRESSION_METHOD_GAIN_NOT_ASSESSED

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 11. Frozen scoring — 72 checks

### A. Protocol and task immutability — 10

~~~text
A1 protocol commit/blob frozen
A2 G1-G18 and T1-T18 identities frozen
A3 task ID/version frozen
A4 primary claim level frozen
A5 source interface/class frozen
A6 purpose identity frozen
A7 compression map/version frozen
A8 accounting metric/reduction requirement frozen
A9 reconstruction/composition scope frozen
A10 no post-hoc task or protocol repair
~~~

### B. Source / purpose / map locks — 10

~~~text
B1 four source objects retained exactly
B2 source triple representation retained
B3 NONZERO status retained
B4 ZERO status retained
B5 purpose requires group preservation
B6 purpose requires status preservation
B7 detail explicitly irrelevant
B8 D_req contains exactly four cross-group/status pairs
B9 A_safe contains exactly two same-group/same-status pairs
B10 purpose relation complete and consistent on all six unordered pairs
~~~

### C. Compression execution and actual reduction — 10

~~~text
C1 C(x1) = (A,NONZERO)
C2 C(x2) = (A,NONZERO)
C3 C(x3) = (B,ZERO)
C4 C(x4) = (B,ZERO)
C5 source cost = 12
C6 reduced package cost = 8
C7 same FIELD_UNIT_COUNT-v1 metric used on both
C8 output_plus_required_sidecars scope respected
C9 strict size reduction established
C10 distinction preservation alone not used as compression proof
~~~

### D. Collision and purpose preservation — 12

~~~text
D1 x1 != x2
D2 C(x1) = C(x2)
D3 x3 != x4
D4 C(x3) = C(x4)
D5 both collision witnesses recorded
D6 x1/x2 collision purpose-safe
D7 x3/x4 collision purpose-safe
D8 status preserved on x1/x2 collision
D9 status preserved on x3/x4 collision
D10 all four D_req pairs remain distinguishable
D11 no purpose-destructive collision established
D12 lossy collision not treated as automatic task failure
~~~

### E. Multidimensional consequence discipline — 10

~~~text
E1 x1/x2 purpose consequence recorded separately
E2 x1/x2 status consequence recorded separately
E3 x1/x2 support consequence marked not applicable
E4 x1/x2 provenance consequence marked not applicable
E5 x1/x2 reconstruction consequence marked not claimed
E6 x3/x4 purpose consequence recorded separately
E7 x3/x4 status consequence recorded separately
E8 x3/x4 support consequence marked not applicable
E9 x3/x4 provenance consequence marked not applicable
E10 x3/x4 reconstruction consequence marked not claimed
~~~

### F. Optional boundary discipline — 10

~~~text
F1 resolution NOT_APPLICABLE
F2 losslessness NOT_ESTABLISHED on declared class
F3 no global injectivity claim
F4 reconstruction NOT_CLAIMED
F5 compression success not promoted to reconstruction success
F6 composition NOT_CLAIMED
F7 property-correlation ledger NOT_APPLICABLE
F8 projection/readout ledger NOT_APPLICABLE
F9 neighboring-method sidecars NOT_REQUESTED
F10 no neighboring method substitutes for Compression validity
~~~

### G. Final protocol result — 10

~~~text
G1 purpose relation CONSISTENT
G2 compression domain ADMITTED
G3 reduction ESTABLISHED
G4 primary status COMPRESSION_ESTABLISHED
G5 terminal COMPRESSION_TASK_ESTABLISHED
G6 protocol COMPRESSION_PROTOCOL_CONFORMANT
G7 method gain NOT_ASSESSED
G8 maximum-supported claim remains class/purpose/metric bounded
G9 protocol revision not required
G10 shared core reopen not required
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  72

PASS_THRESHOLD:
  72/72

PARTIAL_PASS_ALLOWED:
  no
~~~
