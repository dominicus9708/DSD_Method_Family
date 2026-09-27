# DSD Compression Task Interface v0.1 Draft

Status: **HISTORICAL DRAFT — PRE-PROTOCOL**
Date: **2026-09-27**
Method: **Compression / DSD 압축론**
Legacy path ID: 10B

## 1. Atomic task

Given an already represented source object/state/data class and a declared downstream purpose, construct or evaluate a reduced representation that removes representation detail only within the collision classes that the frozen purpose permits, while preserving every distinction and sidecar required by that purpose.

Compression does not by itself establish source reconstruction, classification sufficiency, identity, or external validity.

## 2. Claim levels

Every task freezes exactly one primary claim level:

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

## 3. Required task lock

Before evaluation, freeze:

~~~text
COMPRESSION_TASK_ID
COMPRESSION_TASK_VERSION
PRIMARY_CLAIM_LEVEL
SOURCE_INTERFACE_ID
SOURCE_INTERFACE_VERSION_OR_DOCUMENT
SOURCE_OBJECT_CLASS
SOURCE_REPRESENTATION_ID
SOURCE_REPRESENTATION_VERSION
DOWNSTREAM_PURPOSE_ID
DOWNSTREAM_PURPOSE_VERSION_OR_DEFINITION
COMPRESSION_MAP_ID
COMPRESSION_MAP_VERSION_OR_DEFINITION
REDUCED_OUTPUT_SPACE_AND_TYPE
REQUIRED_DISTINCTION_RELATION
ACCEPTABLE_COLLISION_RELATION
STATUS_RETENTION_POLICY
SUPPORT_RETENTION_POLICY
PROVENANCE_RETENTION_POLICY
RESOLUTION_OR_THRESHOLD
RECONSTRUCTION_CLAIM
DYNAMIC_OR_STATIC_SCOPE
MAXIMUM_SUPPORTED_CLAIM
~~~

Changing a claim-relevant lock after seeing the result requires a new task version.

## 4. Source representation interface

Record the source class and the claim-relevant structure that exists before reduction.

Possible source-side records include typed property records, channel-resolved component terms, support-retaining descriptors, component-resolved dynamic states, declared descriptive states, and already-constructed aggregate/readout records.

Do not treat absent or undefined source information as numerical zero merely to obtain a fixed-size compressed representation.

## 5. Compression map

Let the frozen source task class be X_task and reduced output carrier be Z_C.

~~~text
C:
  X_task -> Z_C
~~~

No linearity, orthogonality, injectivity, surjectivity, continuity, or losslessness is inferred unless separately supplied.

## 6. Purpose-relative required distinctions

A downstream purpose may declare source states that are safe to merge and source pairs that must remain distinct.

For a simple binary relation interface:

~~~text
(x,y) in REQUIRED_DISTINCTION_P
  =>
C(x) != C(y)
~~~

is a necessary purpose-preservation condition.

Equivalently, every compression fiber must remain inside a purpose-allowed collision class.

This is a prospective method-interface condition, not a theorem attributed to the predecessor papers.

## 7. Compression fibers and collision ledger

For each compressed output z relevant to the task, record the fiber C^{-1}(z).

Collision classes:

~~~text
purpose_safe
purpose_destructive
reconstruction_destructive
status_destructive
support_destructive
unresolved
not_tested
~~~

A collision is not automatically a failure.

It is a failure only when it erases a distinction required by the frozen task.

## 8. Property-summary guard

~~~text
SUMMARY_EQUALITY != STRICT_PROPERTY_EQUIVALENCE
~~~

When the downstream purpose depends on cross-property correlations among typed input locations, those correlations must remain in the compressed output, remain in an explicitly retained sidecar, or be excluded from the maximum claim.

## 9. Support and status retention

If the frozen purpose requires them, retain:

~~~text
support identity
typed input identity
property kind
defined-zero / undefined / absent distinctions
negative status information
source provenance
~~~

Required guards:

~~~text
DEFINED_ZERO != ABSENCE
UNDEFINED != ZERO
SUPPORT_RETAINING_DESCRIPTOR != REDUCED_VALUE
~~~

## 10. Resolution interface

When compression is resolution-sensitive, freeze a declared distinguishability threshold or relation.

~~~text
RESOLUTION_PARAMETER:
  epsilon

DISTINGUISHABILITY_RULE:
  supplied by the task
~~~

Changing the resolution changes task semantics unless a resolution family is frozen in advance.

## 11. Descriptive projection specialization

For a declared descriptive projection Pi_O:

~~~text
Pi_O(U) = Pi_O(V)
  does not imply
U = V
~~~

When U != V but Pi_O(U)=Pi_O(V), record a projection-relative erased distinction.

## 12. Linear/kernel specialization

If C is linear, kernel analysis may characterize erased linear distinctions.

Injectivity of C restricted to a declared class may support a class-local lossless claim.

~~~text
INJECTIVE_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
~~~

## 13. Reconstruction interface

Compression and reconstruction remain separate tasks.

Freeze reconstruction scope, required sidecars, injectivity or other reconstruction conditions, source class, and cross-coordinate conditions before making reconstruction claims.

Unavailable required reconstruction interfaces produce blockage, not a fabricated negative result.

## 14. Dynamic reduced-readout specialization

A dynamic reduced readout may serve as a compressed representation only after the component-resolved state is specified.

~~~text
REDUCED_READOUT != COMPONENT_RESOLVED_STATE
READOUT_EQUALITY != DYNAMIC_STATE_EQUALITY
READOUT != COMPLETE_CLASSIFIER
~~~

No converse reconstruction is inferred without injectivity or another reconstruction condition.

## 15. Neighboring-method non-substitution

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

## 16. Primary result statuses

~~~text
COMPRESSION_ESTABLISHED
COMPRESSION_NOT_ESTABLISHED
COMPRESSION_BLOCKED
COMPRESSION_CONFLICTING
COMPRESSION_OUT_OF_SCOPE
COMPRESSION_UNDERDETERMINED
~~~

## 17. Collision / retention statuses

~~~text
COLLISION_NOT_TESTED
NO_COLLISION_ON_TESTED_CLASS
PURPOSE_SAFE_COLLISION_ESTABLISHED
PURPOSE_DESTRUCTIVE_COLLISION_ESTABLISHED
STATUS_DESTRUCTIVE_COLLISION_ESTABLISHED
SUPPORT_DESTRUCTIVE_COLLISION_ESTABLISHED
RECONSTRUCTION_DESTRUCTIVE_COLLISION_ESTABLISHED
COLLISION_UNDERDETERMINED
~~~

A purpose-safe collision is not universally harmless.

## 18. Reconstruction statuses

~~~text
RECONSTRUCTION_NOT_CLAIMED
RECONSTRUCTION_ESTABLISHED_ON_DECLARED_CLASS
RECONSTRUCTION_PARTIAL_OR_BOUNDED
RECONSTRUCTION_NOT_ESTABLISHED
RECONSTRUCTION_BLOCKED
RECONSTRUCTION_UNDERDETERMINED
~~~

Compression success does not require reconstruction unless the frozen purpose requires it.

## 19. Task terminals

~~~text
COMPRESSION_TASK_ESTABLISHED
COMPRESSION_TASK_PARTIAL
COMPRESSION_TASK_NOT_ESTABLISHED
COMPRESSION_TASK_BLOCKED
COMPRESSION_TASK_CONFLICTING
COMPRESSION_TASK_OUT_OF_SCOPE
COMPRESSION_TASK_UNDERDETERMINED
~~~

Terminal precedence is intentionally not frozen in this draft.

## 20. Five-interface method identity

### INPUTS

~~~text
already represented source object/state/data class
+
declared downstream purpose
+
declared reduction map or mechanism
+
retained-distinction / acceptable-collision contract
+
optional sidecar, resolution, reconstruction requirements
~~~

### OPERATION

~~~text
apply or evaluate the reduction
and compare claim-relevant collisions/erasures
against the frozen purpose contract
~~~

### OUTPUTS

~~~text
reduced representation
collision/fiber ledger
retained-distinction verdict
retained support/status/provenance sidecars
reconstruction limits
bounded maximum-supported claim
~~~

### FAILURE_OR_NO_GAIN_CRITERIA

~~~text
required distinction erased
required status/support/provenance erased
required reconstruction prerequisite unavailable
destructive collision
purpose/resolution semantics unresolved
no declared representation reduction
no claim-relevant advantage over a fair baseline
~~~

### VALIDATION_STANDARD

~~~text
purpose-relative retained distinctions preserved
required sidecars present
destructive collisions absent or explicitly bounded
reconstruction claims satisfy frozen conditions
resolution/scope respected
historical loss and NO_GAIN records preserved
~~~

## 21. Initial semantic guards

~~~text
SMALLER_REPRESENTATION != BETTER_REPRESENTATION
COMPRESSION_RATIO != COMPRESSION_VALIDITY
SUMMARY_EQUALITY != STRICT_STRUCTURE_EQUIVALENCE
PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY
PURPOSE_SAFE_COLLISION != UNIVERSALLY_SAFE_COLLISION
LOSSY != FAILURE_BY_DEFAULT
LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
REDUCED_READOUT != COMPLETE_CLASSIFIER
COMPRESSION != RECONSTRUCTION
COMPRESSION != AGGREGATION
COMPRESSION != TRANSFORMATION
COMPRESSION != CLASSIFICATION
~~~

## 22. Pre-protocol attack targets

~~~text
purpose equivalence / required-distinction duality
multi-purpose compression with incompatible retained distinctions
unknown or changing resolution
status-preserving versus support-preserving compression
compression map version changes
acceptable collision versus reconstructibility
lossless claims on bounded versus variable source classes
nonlinear projection where kernel language is unavailable
sidecar-heavy compression that reduces main output but not total representation size
compression that preserves all distinctions and therefore achieves no reduction
two compressed coordinates individually sufficient but jointly insufficient for reconstruction
dynamic readout equality across distinct component states
neighbor-method substitution pressure
NO_GAIN against competent non-DSD compression baselines
~~~

The draft remains historical once the boundary attack begins.
