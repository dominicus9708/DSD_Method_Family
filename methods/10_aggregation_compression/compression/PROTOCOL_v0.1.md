# DSD Compression Protocol v0.1

Status: **FROZEN EXECUTABLE INTERNAL PROTOCOL**  
Date: **2026-09-27**  
Method: **Compression / DSD 압축론**  
Legacy path ID: `10B`

## 1. Frozen lineage of this protocol

~~~text
TASK_INTERFACE_COMMIT:
  40cfedf1ce027c84d4c063a306bb5d7ce770be46

TASK_INTERFACE_BLOB:
  a80b776cbac43de4d6d2c761720fb5268aa87d88

BOUNDARY_REVIEW_COMMIT:
  c84fe112053cd12f46edb3a2c7099ccb5480d09e

BOUNDARY_REVIEW_BLOB:
  563d781498a3af8c64072f757d1e3906e9b9be22

AMENDMENT_COMMIT:
  907cc5ab415e12038fdb521466bb9d2cdfaef159

AMENDMENT_BLOB:
  735ad137da54933d2f2d969aa1dd82218ffa4c7a
~~~

This protocol operationalizes the historical Task Interface v0.1 plus Boundary Amendment 001.

It does not replace or redefine the mathematical statements of the Property, Static Aggregation, or Dynamics source layers.

## 2. Atomic method task

Given an already represented source object/state/data class and a frozen downstream purpose, execute or evaluate a declared reduction map and emit a reduced representation only under a frozen contract specifying:

~~~text
what may collapse
what must remain distinguishable
what status/support/provenance must remain
what reduction dimension is claimed
what reconstruction scope is claimed
what resolution/scope applies
~~~

Compression success requires both:

~~~text
purpose-relative preservation obligations satisfied
+
frozen reduction requirement satisfied
~~~

A smaller main output alone is insufficient.

## 3. Primary claim levels

Exactly one primary claim level is frozen per task.

~~~text
PURPOSE_BOUNDED_COMPRESSION

STATUS_PRESERVING_COMPRESSION

SUPPORT_AWARE_COMPRESSION

RESOLUTION_BOUNDED_COMPRESSION

LOSSLESS_ON_DECLARED_CLASS

LOSSY_WITH_DECLARED_SAFE_COLLISIONS

RECONSTRUCTION_AWARE_COMPRESSION

DYNAMIC_REDUCED_READOUT_COMPRESSION
~~~

Subordinate checks may use other claim levels without replacing the primary claim.

## 4. Validity gates G1-G18

### G1 — task/version/claim lock

Freeze:

~~~text
COMPRESSION_TASK_ID
COMPRESSION_TASK_VERSION
PRIMARY_CLAIM_LEVEL
MAXIMUM_SUPPORTED_CLAIM
~~~

No post-hoc task rewriting.

### G2 — source/interface/representation lock

Freeze every claim-relevant:

~~~text
SOURCE_INTERFACE_ID
SOURCE_INTERFACE_VERSION_OR_DOCUMENT
SOURCE_OBJECT_CLASS
SOURCE_REPRESENTATION_ID
SOURCE_REPRESENTATION_VERSION
SOURCE_STATUS_SCHEMA
~~~

Native source-status distinctions remain authoritative.

### G3 — purpose and purpose-composition lock

Freeze:

~~~text
DOWNSTREAM_PURPOSE_ID
DOWNSTREAM_PURPOSE_VERSION_OR_DEFINITION

PURPOSE_SCOPE:
  single
  conjunction
  prioritized_family
  alternative_family

PURPOSE_SET_ID / VERSION:
  when applicable

PURPOSE_COMPOSITION_RULE:
  when applicable

PURPOSE_PRECEDENCE_RULE:
  when applicable
~~~

No purpose may be selected after observing compression performance.

### G4 — required-distinction / acceptable-collision consistency

Freeze:

~~~text
REQUIRED_DISTINCTION_RELATION
ACCEPTABLE_COLLISION_RELATION
PURPOSE_RELATION_STATUS
~~~

Required guard:

~~~text
ABSENCE_FROM_REQUIRED_DISTINCTION
  !=
PERMISSION_TO_MERGE
~~~

A source pair cannot be simultaneously required-distinct and safe-to-merge under the same unresolved semantics without producing conflict.

### G5 — compression-map/output lock

Freeze:

~~~text
COMPRESSION_MAP_ID
COMPRESSION_MAP_VERSION_OR_DEFINITION
REDUCED_OUTPUT_SPACE_AND_TYPE
DYNAMIC_OR_STATIC_SCOPE
~~~

Current v0.1 assumes a declared deterministic compression map or deterministic composed chain.

A stochastic encoder without a frozen stochastic interface is out of scope.

### G6 — resolution discipline

When resolution is claim-relevant, freeze:

~~~text
RESOLUTION_STATUS
RESOLUTION_PARAMETER_OR_RELATION
RESOLUTION_VERSION
DISTINGUISHABILITY_RULE
~~~

Resolution required but unavailable -> BLOCKED.

Multiple admissible resolutions with different outcomes and no resolver -> UNDERDETERMINED.

Conflicting applicable resolution records -> CONFLICTING.

Changing resolution after result requires a new task version.

### G7 — source status/support/provenance discipline

Preserve every source distinction required by the frozen purpose.

At minimum, when present in the source interface:

~~~text
DEFINED_ZERO != ABSENCE
UNDEFINED != ZERO
SUPPORT_IDENTITY != REDUCED_VALUE
PROVENANCE != REDUCED_VALUE
~~~

No zero-padding of absent or undefined information merely to make a fixed-size compressed representation.

### G8 — representation-accounting and reduction lock

Freeze:

~~~text
REPRESENTATION_ACCOUNTING_SCOPE:
  main_output_only
  output_plus_required_sidecars
  externally_declared_metric

REPRESENTATION_COST_METRIC

SOURCE_COST

REDUCED_PACKAGE_COST

REDUCTION_DIMENSION:
  size
  resolution
  coordinate_detail
  alphabet_or_code_length
  application_declared_metric

REDUCTION_REQUIREMENT:
  strict
  nonincreasing
  thresholded
  externally_declared
~~~

Preserving distinctions without satisfying the frozen reduction requirement is not enough to establish Compression.

### G9 — purpose-relative collision discipline

Every claim-relevant compression fiber must be evaluated relative to the frozen purpose contract.

For a binary required-distinction relation:

~~~text
(x,y) in REQUIRED_DISTINCTION_P
  =>
C(x) != C(y)
~~~

is required.

A collision is not automatically a failure.

A collision is destructive when it erases a frozen required distinction.

### G10 — multidimensional collision-consequence discipline

Do not force every collision into one exclusive label.

Record separately:

~~~text
COLLISION_PURPOSE_STATUS
COLLISION_STATUS_RETENTION_STATUS
COLLISION_SUPPORT_RETENTION_STATUS
COLLISION_PROVENANCE_RETENTION_STATUS
COLLISION_RECONSTRUCTION_STATUS
~~~

Required guards:

~~~text
PURPOSE_SAFE_COLLISION != RECONSTRUCTION_SAFE_COLLISION
PURPOSE_SAFE_COLLISION != STATUS_SAFE_COLLISION
PURPOSE_SAFE_COLLISION != SUPPORT_SAFE_COLLISION
~~~

### G11 — property-summary / correlation discipline

When a source representation contains typed properties or cross-property relations:

~~~text
SUMMARY_EQUALITY != STRICT_PROPERTY_EQUIVALENCE
~~~

Any correlation needed by the frozen purpose must:

~~~text
remain in the compressed output
or
remain in a required sidecar
or
be excluded from the maximum-supported claim
~~~

### G12 — descriptive-projection / reduced-readout discipline

For a declared descriptive projection or reduced readout:

~~~text
PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY
READOUT_EQUALITY != DYNAMIC_STATE_EQUALITY
REDUCED_READOUT != COMPLETE_CLASSIFIER
~~~

Erased source differences remain latent distinctions relative to the declared projection.

### G13 — linear/kernel and class-local losslessness discipline

Kernel language may be used only when the compression map is supplied as linear on the relevant carrier.

If injectivity is established only on a frozen source class:

~~~text
LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
~~~

Nonlinear compression remains fiber/collision based unless another exact structure is supplied.

### G14 — reconstruction-scope and relational-coupling discipline

Freeze:

~~~text
RECONSTRUCTION_SCOPE_CLASS:
  none
  coordinatewise
  support
  joint_coordinate
  relational_coupling
  full_declared_source_class

CROSS_COORDINATE_OR_RELATIONAL_CONDITION:
  not_required
  supplied
  required_but_unavailable
  unresolved
  conflicting
~~~

Required unavailable relational condition -> reconstruction BLOCKED.

Coordinatewise recoverability does not imply relational or full-source reconstruction.

### G15 — required-interface failure discipline

For every required sidecar/interface/metric/rule:

~~~text
REQUIRED_INTERFACE_STATUS:
  available
  unavailable
  conflicting
  underdetermined
  out_of_scope
~~~

Rules:

~~~text
unavailable required interface
  ->
BLOCKED

available required information demonstrably erased
  ->
NOT_ESTABLISHED
unless a higher-priority terminal applies
~~~

Required guard:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
EVALUABLE_DESTRUCTIVE_LOSS
~~~

### G16 — end-to-end composition discipline

For a composed compression chain, freeze:

~~~text
COMPOSITION_CLAIM
COMPRESSION_CHAIN_ID
COMPRESSION_CHAIN_VERSION
CHAIN_STAGE_ORDER
ORIGINAL_PURPOSE_OBLIGATIONS
STAGEWISE_RETAINED_DISTINCTIONS
~~~

A local stage pass does not establish the original end-to-end claim.

~~~text
LOCAL_STAGE_PASS != END_TO_END_COMPRESSION_PASS
~~~

### G17 — neighboring-method non-substitution

Neighboring-method records may be consumed as sidecars but do not silently become Compression criteria.

~~~text
AGGREGATION_RESULT != COMPRESSION_VALIDITY
TRANSFORMATION_MAPPING != PURPOSE_PRESERVATION
CLASSIFICATION_RESULT != COMPRESSION_SUFFICIENCY
COMPARISON_SIMILARITY != SAFE_COLLISION_BY_DEFAULT
MEASUREMENT_PRECISION != COMPRESSION_RESOLUTION_BY_DEFAULT
RECONSTRUCTION_CANDIDATE != COMPRESSION_LOSSLESSNESS
TRACKING_PROVENANCE != SOURCE_RECONSTRUCTION
LINEAGE_IDENTITY != COMPRESSION_EQUIVALENCE
AUDIT_PASS != COMPRESSION_RESULT
~~~

### G18 — status / terminal / conformance / gain / max-claim discipline

Assign only the frozen status families.

Apply frozen task-terminal precedence.

Emit protocol conformance, method-gain status, and a bounded maximum-supported claim.

No task result may be promoted beyond the frozen purpose, source class, reduction metric, resolution, collision evidence, reconstruction scope, and sidecars.

## 5. Binding operation T1-T18

### T1 — freeze task and primary claim

Instantiate G1.

### T2 — bind source interface and representation

Instantiate G2 and retain native source statuses.

### T3 — freeze purpose semantics

Instantiate G3.

If multiple purposes exist, freeze composition and precedence semantics before further evaluation.

### T4 — validate purpose relations

Instantiate G4.

Record conflicts, incompleteness, and claim-relevant unresolved pairs before applying the compression map.

### T5 — freeze compression map and output type

Instantiate G5.

Reject post-result map substitution under the same task identity.

### T6 — resolve resolution semantics

Instantiate G6.

If resolution is required and blocked/underdetermined/conflicting, retain that state.

### T7 — build source status/support/provenance ledger

Instantiate G7 before reduction.

### T8 — freeze representation accounting and reduction requirement

Instantiate G8.

Do not compute a compression-success verdict before the accounting scope and reduction dimension are fixed.

### T9 — execute the declared compression map

Compute only the frozen deterministic map or frozen deterministic chain on the frozen source class.

Emit the reduced representation.

### T10 — build collision/fiber ledger

Identify claim-relevant equal-output source pairs or fibers.

Do not infer source identity from reduced equality.

### T11 — evaluate multidimensional collision consequences

Instantiate G10 for each claim-relevant collision.

Retain purpose/status/support/provenance/reconstruction consequences independently.

### T12 — evaluate property/correlation and projection/readout guards

Instantiate G11 and G12 when applicable.

Do not promote summary or projected equality to complete source equivalence.

### T13 — evaluate linear/kernel or other declared losslessness condition

Instantiate G13.

If the map is nonlinear and no other exact structure is supplied, keep the analysis fiber/collision based.

### T14 — evaluate reconstruction scope

Instantiate G14.

Apply only the frozen reconstruction and relational conditions.

### T15 — evaluate required-interface availability versus destructive loss

Instantiate G15.

Keep BLOCKED separate from evaluable NOT_ESTABLISHED.

### T16 — evaluate actual reduction and composed-chain validity

First evaluate the frozen reduction metric.

Then, when a composition claim exists, instantiate G16 and validate end-to-end preservation from the original source-level purpose.

### T17 — preserve neighboring-method sidecars

Instantiate G17.

No neighboring-method result may substitute for Compression validity.

### T18 — assign statuses, terminal, conformance, gain, and maximum claim

Instantiate G18 and emit the required output schema.

## 6. Purpose-relation statuses

~~~text
PURPOSE_RELATION_CONSISTENT
PURPOSE_RELATION_CONFLICTING
PURPOSE_RELATION_INCOMPLETE
PURPOSE_RELATION_BLOCKED
PURPOSE_RELATION_OUT_OF_SCOPE
~~~

`PURPOSE_RELATION_INCOMPLETE` yields task-level UNDERDETERMINED only when the unresolved pair/branch can change the claim-relevant verdict.

## 7. Resolution statuses

~~~text
RESOLUTION_NOT_APPLICABLE
RESOLUTION_SUPPLIED
RESOLUTION_BLOCKED
RESOLUTION_UNDERDETERMINED
RESOLUTION_CONFLICTING
~~~

## 8. Compression-domain statuses

~~~text
COMPRESSION_DOMAIN_ADMITTED
COMPRESSION_DOMAIN_NOT_ADMITTED
COMPRESSION_DOMAIN_BLOCKED
COMPRESSION_DOMAIN_CONFLICTING
COMPRESSION_DOMAIN_UNDERDETERMINED
COMPRESSION_DOMAIN_OUT_OF_SCOPE
~~~

The domain includes the frozen source class, purpose semantics, map applicability, and claim-relevant resolution/scope requirements.

## 9. Reduction statuses

~~~text
REDUCTION_ESTABLISHED
REDUCTION_NOT_ESTABLISHED
REDUCTION_BLOCKED
REDUCTION_UNDERDETERMINED
REDUCTION_CONFLICTING
REDUCTION_OUT_OF_SCOPE
~~~

A valid reduced representation with no frozen reduction does not establish Compression.

## 10. Collision/fiber statuses

Generic collision detection:

~~~text
COLLISION_NOT_TESTED
NO_COLLISION_ON_TESTED_CLASS
COLLISION_WITNESS_ESTABLISHED
COLLISION_UNDERDETERMINED
~~~

Purpose consequence:

~~~text
COLLISION_PURPOSE_SAFE
COLLISION_PURPOSE_DESTRUCTIVE
COLLISION_PURPOSE_UNRESOLVED
COLLISION_PURPOSE_NOT_TESTED
~~~

Status-retention consequence:

~~~text
COLLISION_STATUS_PRESERVED
COLLISION_STATUS_DESTRUCTIVE
COLLISION_STATUS_UNRESOLVED
COLLISION_STATUS_NOT_APPLICABLE
~~~

Support-retention consequence:

~~~text
COLLISION_SUPPORT_PRESERVED
COLLISION_SUPPORT_DESTRUCTIVE
COLLISION_SUPPORT_UNRESOLVED
COLLISION_SUPPORT_NOT_APPLICABLE
~~~

Provenance-retention consequence:

~~~text
COLLISION_PROVENANCE_PRESERVED
COLLISION_PROVENANCE_DESTRUCTIVE
COLLISION_PROVENANCE_UNRESOLVED
COLLISION_PROVENANCE_NOT_APPLICABLE
~~~

Reconstruction consequence:

~~~text
COLLISION_RECONSTRUCTION_SAFE
COLLISION_RECONSTRUCTION_DESTRUCTIVE
COLLISION_RECONSTRUCTION_BLOCKED
COLLISION_RECONSTRUCTION_UNRESOLVED
COLLISION_RECONSTRUCTION_NOT_CLAIMED
~~~

These axes may carry different statuses for the same collision.

## 11. Losslessness / injectivity statuses

~~~text
LOSSLESSNESS_NOT_TESTED
LOSSLESS_ON_DECLARED_CLASS
LOSSLESSNESS_NOT_ESTABLISHED
LOSSLESSNESS_BLOCKED
LOSSLESSNESS_CONFLICTING
LOSSLESSNESS_UNDERDETERMINED
LOSSLESSNESS_OUT_OF_SCOPE
~~~

Required guard:

~~~text
LOSSLESS_ON_DECLARED_CLASS
  !=
GLOBAL_INJECTIVITY
~~~

## 12. Reconstruction statuses

~~~text
RECONSTRUCTION_NOT_CLAIMED
RECONSTRUCTION_ESTABLISHED_ON_DECLARED_CLASS
RECONSTRUCTION_PARTIAL_OR_BOUNDED
RECONSTRUCTION_NOT_ESTABLISHED
RECONSTRUCTION_BLOCKED
RECONSTRUCTION_UNDERDETERMINED
RECONSTRUCTION_CONFLICTING
RECONSTRUCTION_OUT_OF_SCOPE
~~~

Compression may be established while reconstruction is not claimed or is intentionally lossy, provided the frozen primary claim does not require reconstruction.

## 13. Composition statuses

~~~text
COMPOSITION_NOT_CLAIMED
COMPOSITION_LOCAL_ONLY
COMPOSITION_END_TO_END_ESTABLISHED
COMPOSITION_END_TO_END_NOT_ESTABLISHED
COMPOSITION_BLOCKED
COMPOSITION_UNDERDETERMINED
COMPOSITION_CONFLICTING
COMPOSITION_OUT_OF_SCOPE
~~~

## 14. Primary task statuses

~~~text
COMPRESSION_ESTABLISHED
COMPRESSION_NOT_ESTABLISHED
COMPRESSION_BLOCKED
COMPRESSION_CONFLICTING
COMPRESSION_OUT_OF_SCOPE
COMPRESSION_UNDERDETERMINED
~~~

These are task-evidence statuses and do not replace source-level statuses.

## 15. Task terminals

~~~text
COMPRESSION_TASK_ESTABLISHED
COMPRESSION_TASK_PARTIAL
COMPRESSION_TASK_NOT_ESTABLISHED
COMPRESSION_TASK_BLOCKED
COMPRESSION_TASK_CONFLICTING
COMPRESSION_TASK_OUT_OF_SCOPE
COMPRESSION_TASK_UNDERDETERMINED
~~~

Frozen precedence:

~~~text
OUT_OF_SCOPE
>
CONFLICTING
>
UNDERDETERMINED
>
BLOCKED
>
ESTABLISHED / PARTIAL / NOT_ESTABLISHED
~~~

`PARTIAL` requires multiple independent required obligations with at least one established and at least one evaluable not-established obligation, and no higher-priority terminal.

It may not rescue one failed atomic compression proposition.

## 16. Protocol conformance

~~~text
COMPRESSION_PROTOCOL_CONFORMANT
COMPRESSION_PROTOCOL_NONCONFORMANT
COMPRESSION_PROTOCOL_INDETERMINATE
~~~

A negative, blocked, conflicting, out-of-scope, or underdetermined task result may still be protocol-conformant.

## 17. Method-gain statuses

~~~text
COMPRESSION_METHOD_GAIN_ESTABLISHED
COMPRESSION_METHOD_GAIN_PARTIAL
COMPRESSION_METHOD_GAIN_NO_GAIN
COMPRESSION_METHOD_GAIN_NOT_ASSESSED
COMPRESSION_METHOD_GAIN_UNDERDETERMINED
~~~

~~~text
NO_GAIN != METHOD_FAILURE
~~~

Method gain must be assessed only against a frozen fair comparator when a baseline comparison is explicitly part of the task.

## 18. Required output schema

Each execution record must contain, as applicable:

~~~text
TASK_LOCK

SOURCE_INTERFACE_LOCK
SOURCE_STATUS_LEDGER
SOURCE_SUPPORT_PROVENANCE_LEDGER

PURPOSE_LOCK
PURPOSE_RELATION_LEDGER

COMPRESSION_MAP_LOCK
COMPRESSION_DOMAIN_LEDGER

RESOLUTION_LEDGER

REPRESENTATION_ACCOUNTING_LEDGER
REDUCTION_LEDGER

COMPRESSED_OUTPUT

COLLISION_FIBER_LEDGER
COLLISION_CONSEQUENCE_LEDGER

PROPERTY_CORRELATION_LEDGER

PROJECTION_READOUT_LEDGER

LINEAR_KERNEL_OR_LOSSLESSNESS_LEDGER

RECONSTRUCTION_SCOPE_LEDGER
RELATIONAL_CONDITION_LEDGER

REQUIRED_INTERFACE_LEDGER

COMPOSITION_LEDGER

NEIGHBOR_METHOD_SIDECAR_LEDGER

PRIMARY_TASK_STATUS
TASK_TERMINAL_STATUS

PROTOCOL_CONFORMANCE
METHOD_GAIN_STATUS

MAXIMUM_SUPPORTED_CLAIM
~~~

Every claim-relevant optional ledger must be explicitly marked:

~~~text
NOT_APPLICABLE
NOT_REQUESTED
BLOCKED
or
populated
~~~

rather than silently omitted.

## 19. Core semantic guards

~~~text
SMALLER_REPRESENTATION != BETTER_REPRESENTATION
COMPRESSION_RATIO != COMPRESSION_VALIDITY

SUMMARY_EQUALITY != STRICT_STRUCTURE_EQUIVALENCE
PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY
READOUT_EQUALITY != DYNAMIC_STATE_EQUALITY
REDUCED_READOUT != COMPLETE_CLASSIFIER

DEFINED_ZERO != ABSENCE
UNDEFINED != ZERO

PURPOSE_SAFE_COLLISION != UNIVERSALLY_SAFE_COLLISION
PURPOSE_SAFE_COLLISION != RECONSTRUCTION_SAFE_COLLISION

LOSSY != FAILURE_BY_DEFAULT

LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY

ABSENCE_FROM_REQUIRED_DISTINCTION != PERMISSION_TO_MERGE

UNAVAILABLE_REQUIRED_INTERFACE != EVALUABLE_DESTRUCTIVE_LOSS
BLOCKED != NOT_ESTABLISHED

MAIN_OUTPUT_SHRINKAGE != TOTAL_REPRESENTATION_REDUCTION
DISTINCTION_PRESERVATION != COMPRESSION_ESTABLISHED
IDENTITY_TRANSFORMATION != COMPRESSION_BY_DEFAULT

COORDINATEWISE_RECONSTRUCTION != RELATIONAL_RECONSTRUCTION
COMPRESSION_SUCCESS != RECONSTRUCTION_SUCCESS

LOCAL_STAGE_PASS != END_TO_END_COMPRESSION_PASS

COMPRESSION != AGGREGATION
COMPRESSION != TRANSFORMATION
COMPRESSION != RECONSTRUCTION
COMPRESSION != CLASSIFICATION
COMPRESSION != COMPARISON
COMPRESSION != MEASUREMENT
COMPRESSION != TRACKING
COMPRESSION != LINEAGE
COMPRESSION != AUDIT
~~~

## 20. Maximum-supported claim rule

A valid Compression result may claim only what follows from the frozen:

~~~text
purpose
source class
source status/support/provenance
compression map/version
resolution
representation accounting
reduction dimension/requirement
collision fibers
retained sidecars
losslessness evidence
reconstruction scope
relational conditions
composition scope
~~~

Examples of allowed bounded claims:

~~~text
compression established for purpose P on declared class A
under metric M and resolution epsilon

purpose-safe lossy compression on the tested class

lossless compression on declared class A

support-aware compression with required sidecar retained

dynamic reduced-readout compression without complete-state identity claim

end-to-end compression established on declared chain K
~~~

Not automatically allowed:

~~~text
global source identity

strict property equivalence from summary equality

global injectivity from declared-class injectivity

relational reconstruction from coordinatewise reconstruction

complete dynamic-state equality from readout equality

universal purpose safety

external validity

independent validation

independent replication

method superiority
~~~

## 21. Current protocol state

~~~text
DEDICATED_COMPRESSION_PROTOCOL:
  established v0.1

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18

TASK_INTERFACE_DRAFT:
  v0.1 historical draft preserved

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

BOUNDARY_AMENDMENT_001:
  established

REFINEMENT_GROUPS_ADOPTED:
  8/8

DIRECT_COMPRESSION_PILOTS_ATTEMPTED:
  0

SUCCESSFUL_DIRECT_COMPRESSION_PILOTS:
  0

BASELINE_COMPRESSION_CASES:
  0

NO_GAIN_COMPRESSION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

COMPRESSION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_COMPRESSION_EVIDENCE_STATUS:
  protocol_frozen

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 22. Next

Prospectively precommit and execute the first positive constructed Compression challenge without rewriting this protocol.
