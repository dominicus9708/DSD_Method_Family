# CPR-CH-003 — Direct Neighboring-Method Compression Boundary Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-28**  
Challenge ID: `CPR-CH-003`  
Method: **Compression / DSD 압축론**  
Protocol: **Compression Protocol v0.1**  
Case class: `direct_neighboring_method_boundary`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  b1efa06e4c715e08ce2558a608c7f09aa22172bd

PROTOCOL_BLOB:
  4d67d800e107229f91c16cf5b0235928124482b2
~~~

The frozen Compression protocol may not be edited in response to this challenge.

## 2. Purpose

Test whether Compression collapses into neighboring Method Family methods when each pair receives fair access to the same claim-relevant artifact bundle.

The challenge tests nine neighboring methods:

~~~text
Aggregation
Transformation
Reconstruction
Classification
Comparison
Measurement
Tracking
Lineage
Audit
~~~

This is a fixture-bounded method-boundary test.

It is not:

~~~text
a permanent irreducibility proof
a method-survival vote
a method-superiority claim
a merger/deletion decision
an external-validation result
~~~

## 3. Shared artifact bundle

Every pair receives the same relevant constructed records:

~~~text
source object class
source representation and native statuses
frozen downstream purpose
required-distinction relation
acceptable-collision relation
compression map/version
reduced output package
representation-accounting metric
source cost
reduced package cost
collision/fiber ledger
status/support/provenance retention policies
resolution records
declared-class losslessness evidence
reconstruction-scope records
composition records
maximum-supported claim
protocol-conformance record

Aggregation sidecar:
  declared readout / aggregation operator
  support and collision information

Transformation sidecar:
  source-target mapping
  preserved/lost-coordinate record

Reconstruction sidecar:
  admissible source candidates
  reconstruction prerequisites
  uniqueness/nonuniqueness record

Classification sidecar:
  class schema
  criterion-traceable class assignment

Comparison sidecar:
  source-target correspondence/divergence profile

Measurement sidecar:
  candidate observations/readouts
  declared resolution
  discrimination profile

Tracking sidecar:
  provenance/version/handoff links

Lineage sidecar:
  predecessor-successor identity records

Audit sidecar:
  frozen audit scope
  evidence provenance
  criteria and conformance verdict
~~~

No compared method receives hidden claim-relevant information unavailable to Compression.

Fair access does not require identical task contracts.

## 4. Five-interface non-collapse test

For every pair compare:

~~~text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
~~~

Allowed pair result:

~~~text
EXACT_COLLAPSE
PARTIAL_OVERLAP_NOT_COLLAPSE
UNRESOLVED_BOUNDARY
~~~

`EXACT_COLLAPSE` requires no claim-relevant distinction across all five interfaces in the frozen fixture.

Shared data, maps, outputs, sidecars, or workflow handoffs are insufficient for collapse.

## 5. B1 — Compression vs Aggregation

Shared overlap:

~~~text
source values
maps/readouts
collision information
support sidecars
reduced outputs
~~~

Frozen distinction:

~~~text
Compression:
  intentionally reduce representation under a frozen
  downstream-purpose / retained-distinction contract
  and verify an actual reduction criterion

Aggregation:
  combine selected admitted values into a declared readout
  under a declared operator/domain
~~~

Failure distinction:

~~~text
Compression:
  may fail even when a reduced readout is correctly computed
  if required distinctions are destroyed or no frozen reduction occurs

Aggregation:
  may succeed despite noninjectivity/information loss
  when no reconstruction claim is frozen
~~~

Guard:

~~~text
AGGREGATION_RESULT != COMPRESSION_VALIDITY
REDUCED_READOUT != PURPOSE_VALIDATED_COMPRESSION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 6. B2 — Compression vs Transformation

Shared overlap:

~~~text
source object
declared map
target representation
preservation/loss record
versioned mapping
~~~

Frozen distinction:

~~~text
Compression:
  requires a declared reduction dimension/metric
  plus preservation of purpose-required distinctions

Transformation:
  maps source to target representation/regime
  while recording preservation/loss;
  representation reduction is not intrinsically required
~~~

Failure distinction:

~~~text
identity or size-neutral map:
  may be a valid Transformation
  but does not establish strict Compression when reduction is required

reduction that destroys a purpose-required distinction:
  may still be an executed Transformation
  but fails Compression
~~~

Guard:

~~~text
TRANSFORMATION_MAPPING != COMPRESSION_VALIDITY
REPRESENTATION_CHANGE != REPRESENTATION_REDUCTION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 7. B3 — Compression vs Reconstruction

Shared overlap:

~~~text
compressed output
collision fibers
support/status sidecars
injectivity/losslessness evidence
reconstruction prerequisites
~~~

Frozen distinction:

~~~text
Compression:
  forward reduction relative to purpose

Reconstruction:
  inverse inference of compatible prior/hidden/lost/source structures
  from incomplete or reduced evidence
~~~

Failure distinction:

~~~text
Compression:
  may intentionally be lossy and valid

Reconstruction:
  exact recovery is not established when multiple compatible
  sources remain without a resolving condition
~~~

Guard:

~~~text
COMPRESSION_SUCCESS != RECONSTRUCTION_SUCCESS
PURPOSE_SAFE_COLLISION != RECONSTRUCTION_SAFE_COLLISION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 8. B4 — Compression vs Classification

Shared overlap:

~~~text
reduced features
typed statuses
purpose criteria
feature provenance
~~~

Frozen distinction:

~~~text
Compression:
  reduce representation while preserving required distinctions

Classification:
  assign class membership under explicit criteria
~~~

Failure distinction:

~~~text
a compressed representation may preserve every required feature
without assigning any class

a classifier may succeed using an unreduced representation
~~~

Guard:

~~~text
COMPRESSED_REPRESENTATION != CLASS_ASSIGNMENT
CLASSIFICATION_SUCCESS != COMPRESSION_ESTABLISHED
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 9. B5 — Compression vs Comparison

Shared overlap:

~~~text
source and reduced representations
maps
difference profiles
resolution/criterion records
~~~

Frozen distinction:

~~~text
Compression:
  evaluates whether reduction preserves the purpose-required distinctions

Comparison:
  judges correspondence/divergence/equivalence between supplied targets
  under frozen comparison criteria
~~~

Failure distinction:

~~~text
Compression can fail because representation cost is not reduced
even when source and output are perfectly comparable

Comparison can establish correspondence without reducing either object
~~~

Guard:

~~~text
COMPARISON_SIMILARITY != SAFE_COLLISION_BY_DEFAULT
COMPARISON_RESULT != COMPRESSION_VALIDITY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 10. B6 — Compression vs Measurement

Shared overlap:

~~~text
resolution
readout candidates
distinguishability requirements
status information
~~~

Frozen distinction:

~~~text
Compression:
  may erase distinctions below a frozen purpose/resolution
  while preserving those required by the task

Measurement:
  determines which observations/readouts discriminate
  declared alternatives at a declared resolution
~~~

Failure distinction:

~~~text
Measurement can identify a discriminating readout
without reducing representation

Compression can preserve a distinction supplied by Measurement
without itself determining how that distinction was observed
~~~

Guard:

~~~text
MEASUREMENT_PRECISION != COMPRESSION_RESOLUTION_BY_DEFAULT
DISCRIMINATING_MEASUREMENT_PLAN != COMPRESSED_REPRESENTATION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 11. B7 — Compression vs Tracking

Shared overlap:

~~~text
source identity
versioned compression map
provenance sidecars
handoff records
~~~

Frozen distinction:

~~~text
Compression:
  executes/evaluates representation reduction

Tracking:
  records supported typed provenance/version/process/location/handoff links
~~~

Failure distinction:

~~~text
Compression can succeed while provenance tracking is not requested

Tracking can succeed without reducing representation
~~~

Guard:

~~~text
TRACKING_PROVENANCE != SOURCE_RECONSTRUCTION
TRACKING_TRACE != COMPRESSION_RESULT
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 12. B8 — Compression vs Lineage

Shared overlap:

~~~text
source/target identities
versioned state records
reduced descriptors
change/handoff records
~~~

Frozen distinction:

~~~text
Compression:
  declares which source distinctions may collapse in a reduced representation

Lineage:
  determines predecessor-successor identity across change
~~~

Failure distinction:

~~~text
compression-equivalent outputs do not establish successor identity

different compressed outputs do not automatically negate lineage identity
~~~

Guard:

~~~text
COMPRESSION_EQUIVALENCE != LINEAGE_IDENTITY
COMPRESSED_INEQUALITY != LINEAGE_NONIDENTITY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 13. B9 — Compression vs Audit

Shared overlap:

~~~text
frozen protocol
task/version locks
evidence provenance
conformance records
failure/status ledgers
~~~

Frozen distinction:

~~~text
Compression:
  performs/evaluates the reduction task

Audit:
  retraces and evaluates performed work/evidence/procedure
  against frozen scope and audit criteria
~~~

Failure distinction:

~~~text
a conformant negative Compression result may be a valid protocol output

an Audit may pass because the negative result was correctly produced
rather than because Compression was established
~~~

Guard:

~~~text
COMPRESSION_RESULT != AUDIT_VERDICT
COMPRESSION_PROTOCOL_CONFORMANCE != GENERAL_AUDIT_PASS
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 14. Source-handoff separation lock

Compression may consume artifacts produced by:

~~~text
Property
Static Aggregation
Dynamics reduced-readout/projection interfaces
~~~

but this challenge does not count foundational source-layer handoff as a method collapse.

Required guard:

~~~text
SOURCE_LAYER_HANDOFF != METHOD_IDENTITY
~~~

Expected source-handoff result:

~~~text
SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

## 15. Frozen scoring — 81 checks

Each method pair receives nine checks.

### B1 — Compression vs Aggregation

~~~text
B1-1 shared artifact access fair
B1-2 INPUTS overlap recorded without identity claim
B1-3 OPERATION distinction preserved
B1-4 OUTPUTS distinction preserved
B1-5 FAILURE/NO_GAIN distinction preserved
B1-6 VALIDATION_STANDARD distinction preserved
B1-7 semantic guard preserved
B1-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
B1-9 no permanent irreducibility/superiority claim
~~~

### B2 — Compression vs Transformation

~~~text
B2-1 shared artifact access fair
B2-2 INPUTS overlap recorded without identity claim
B2-3 OPERATION distinction preserved
B2-4 OUTPUTS distinction preserved
B2-5 FAILURE/NO_GAIN distinction preserved
B2-6 VALIDATION_STANDARD distinction preserved
B2-7 semantic guard preserved
B2-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
B2-9 no permanent irreducibility/superiority claim
~~~

### B3 — Compression vs Reconstruction

~~~text
B3-1 shared artifact access fair
B3-2 INPUTS overlap recorded without identity claim
B3-3 OPERATION distinction preserved
B3-4 OUTPUTS distinction preserved
B3-5 FAILURE/NO_GAIN distinction preserved
B3-6 VALIDATION_STANDARD distinction preserved
B3-7 semantic guard preserved
B3-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
B3-9 no permanent irreducibility/superiority claim
~~~

### B4 — Compression vs Classification

~~~text
B4-1 shared artifact access fair
B4-2 INPUTS overlap recorded without identity claim
B4-3 OPERATION distinction preserved
B4-4 OUTPUTS distinction preserved
B4-5 FAILURE/NO_GAIN distinction preserved
B4-6 VALIDATION_STANDARD distinction preserved
B4-7 semantic guard preserved
B4-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
B4-9 no permanent irreducibility/superiority claim
~~~

### B5 — Compression vs Comparison

~~~text
B5-1 shared artifact access fair
B5-2 INPUTS overlap recorded without identity claim
B5-3 OPERATION distinction preserved
B5-4 OUTPUTS distinction preserved
B5-5 FAILURE/NO_GAIN distinction preserved
B5-6 VALIDATION_STANDARD distinction preserved
B5-7 semantic guard preserved
B5-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
B5-9 no permanent irreducibility/superiority claim
~~~

### B6 — Compression vs Measurement

~~~text
B6-1 shared artifact access fair
B6-2 INPUTS overlap recorded without identity claim
B6-3 OPERATION distinction preserved
B6-4 OUTPUTS distinction preserved
B6-5 FAILURE/NO_GAIN distinction preserved
B6-6 VALIDATION_STANDARD distinction preserved
B6-7 semantic guard preserved
B6-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
B6-9 no permanent irreducibility/superiority claim
~~~

### B7 — Compression vs Tracking

~~~text
B7-1 shared artifact access fair
B7-2 INPUTS overlap recorded without identity claim
B7-3 OPERATION distinction preserved
B7-4 OUTPUTS distinction preserved
B7-5 FAILURE/NO_GAIN distinction preserved
B7-6 VALIDATION_STANDARD distinction preserved
B7-7 semantic guard preserved
B7-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
B7-9 no permanent irreducibility/superiority claim
~~~

### B8 — Compression vs Lineage

~~~text
B8-1 shared artifact access fair
B8-2 INPUTS overlap recorded without identity claim
B8-3 OPERATION distinction preserved
B8-4 OUTPUTS distinction preserved
B8-5 FAILURE/NO_GAIN distinction preserved
B8-6 VALIDATION_STANDARD distinction preserved
B8-7 semantic guard preserved
B8-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
B8-9 no permanent irreducibility/superiority claim
~~~

### B9 — Compression vs Audit

~~~text
B9-1 shared artifact access fair
B9-2 INPUTS overlap recorded without identity claim
B9-3 OPERATION distinction preserved
B9-4 OUTPUTS distinction preserved
B9-5 FAILURE/NO_GAIN distinction preserved
B9-6 VALIDATION_STANDARD distinction preserved
B9-7 semantic guard preserved
B9-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
B9-9 no permanent irreducibility/superiority claim
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  81

PASS_THRESHOLD:
  81/81

PARTIAL_PASS_ALLOWED:
  no
~~~

## 16. Expected aggregate boundary result

If all 81 checks pass:

~~~text
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  9

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  9

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Counter update:

~~~text
DIRECT_COMPRESSION_PILOTS_ATTEMPTED:
  3

SUCCESSFUL_DIRECT_COMPRESSION_PILOTS:
  3

METHOD_BOUNDARY_COMPRESSION_CASES:
  1
~~~

## 17. Next

If the frozen bundle passes, proceed to a fair competent non-DSD Compression baseline challenge.
