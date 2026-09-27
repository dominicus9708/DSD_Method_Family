# DSD Compression Task Interface Boundary Amendment 001

Status: **PROSPECTIVE AMENDMENT ESTABLISHED**  
Date: **2026-09-27**  
Method: **Compression / DSD 압축론**

Frozen historical basis:

~~~text
TASK_INTERFACE_COMMIT:
  40cfedf1ce027c84d4c063a306bb5d7ce770be46

TASK_INTERFACE_BLOB:
  a80b776cbac43de4d6d2c761720fb5268aa87d88

BOUNDARY_REVIEW_COMMIT:
  c84fe112053cd12f46edb3a2c7099ccb5480d09e

BOUNDARY_REVIEW_BLOB:
  563d781498a3af8c64072f757d1e3906e9b9be22
~~~

The historical Task Interface and boundary-review record are not rewritten.

## 1. Amendment result

~~~text
BOUNDARY_AMENDMENT_001:
  established

REFINEMENT_GROUPS_ADOPTED:
  8/8

METHOD_IDENTITY_CHANGED:
  no

TASK_INTERFACE_CORE_REOPENED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no

PROTOCOL_FREEZE_AUTHORIZED:
  yes
~~~

The amendment binds execution semantics required by the Compression method without altering the predecessor papers' mathematical statements.

## 2. R1 — multidimensional collision consequences

A compression collision may be safe under one obligation and destructive under another.

Do not force all consequences into one exclusive collision label.

For every claim-relevant collision, freeze and record separately:

~~~text
COLLISION_PURPOSE_STATUS:
  safe
  destructive
  unresolved
  not_tested

COLLISION_STATUS_RETENTION_STATUS:
  preserved
  destructive
  unresolved
  not_applicable

COLLISION_SUPPORT_RETENTION_STATUS:
  preserved
  destructive
  unresolved
  not_applicable

COLLISION_PROVENANCE_RETENTION_STATUS:
  preserved
  destructive
  unresolved
  not_applicable

COLLISION_RECONSTRUCTION_STATUS:
  safe
  destructive
  blocked
  unresolved
  not_claimed
~~~

Required guard:

~~~text
PURPOSE_SAFE_COLLISION
  !=
RECONSTRUCTION_SAFE_COLLISION
~~~

and likewise:

~~~text
PURPOSE_SAFE_COLLISION
  !=
STATUS_SAFE_COLLISION

PURPOSE_SAFE_COLLISION
  !=
SUPPORT_SAFE_COLLISION
~~~

A task may establish Compression only if every obligation required by the frozen claim is satisfied.

## 3. R2 — purpose-relation consistency and incompleteness

Freeze:

~~~text
REQUIRED_DISTINCTION_RELATION
ACCEPTABLE_COLLISION_RELATION
PURPOSE_RELATION_STATUS
~~~

Allowed purpose-relation statuses:

~~~text
PURPOSE_RELATION_CONSISTENT
PURPOSE_RELATION_CONFLICTING
PURPOSE_RELATION_INCOMPLETE
PURPOSE_RELATION_BLOCKED
PURPOSE_RELATION_OUT_OF_SCOPE
~~~

Rules:

~~~text
same source pair both:
  required-distinct
  and
  explicitly safe-to-merge

->
  PURPOSE_RELATION_CONFLICTING

claim-relevant source pair:
  neither required-distinct
  nor explicitly safe-to-merge
  and no default rule is frozen

->
  PURPOSE_RELATION_INCOMPLETE
  /
  task-level UNDERDETERMINED when the unresolved pair can change the verdict
~~~

Required guard:

~~~text
ABSENCE_FROM_REQUIRED_DISTINCTION
  !=
PERMISSION_TO_MERGE
~~~

No post-hoc default may be introduced after seeing the compression result.

## 4. R3 — multi-purpose composition

Freeze one purpose scope:

~~~text
PURPOSE_SCOPE:
  single
  conjunction
  prioritized_family
  alternative_family
~~~

For any non-single scope, freeze:

~~~text
PURPOSE_SET_ID
PURPOSE_SET_VERSION
PURPOSE_COMPOSITION_RULE
PURPOSE_PRECEDENCE_RULE
  when applicable
~~~

Semantics:

~~~text
single:
  evaluate one frozen purpose

conjunction:
  all required purpose obligations must hold

prioritized_family:
  supplied precedence determines which obligation governs
  when obligations conflict

alternative_family:
  evaluate each admissible purpose branch separately;
  do not collapse divergent branch outcomes without a resolver
~~~

If a conjunction contains incompatible obligations:

~~~text
COMPRESSION_TASK_CONFLICTING
~~~

If multiple admissible purpose interpretations produce different verdicts and no resolver exists:

~~~text
COMPRESSION_TASK_UNDERDETERMINED
~~~

Guard:

~~~text
POST_HOC_PURPOSE_SELECTION
  prohibited
~~~

## 5. R4 — resolution semantics

Freeze:

~~~text
RESOLUTION_STATUS:
  not_applicable
  supplied
  blocked
  underdetermined
  conflicting

RESOLUTION_PARAMETER_OR_RELATION
RESOLUTION_VERSION
DISTINGUISHABILITY_RULE
~~~

Rules:

~~~text
resolution required but unavailable:
  COMPRESSION_TASK_BLOCKED

multiple admissible resolutions
with different claim-relevant outcomes
and no resolver:
  COMPRESSION_TASK_UNDERDETERMINED

incompatible applicable resolution records
under the same frozen semantics:
  COMPRESSION_TASK_CONFLICTING

resolution changed after result:
  new COMPRESSION_TASK_VERSION required
~~~

Guard:

~~~text
RESOLUTION_CHANGE
  !=
SAME_TASK_SEMANTICS
~~~

If a resolution family is intentionally frozen, the family and its branch rule must be explicit before evaluation.

## 6. R5 — unavailable required interface versus evaluable destructive loss

For each required support/status/provenance/reconstruction/purpose/resolution interface:

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
required interface unavailable:
  COMPRESSION_TASK_BLOCKED

required information available
and compression demonstrably erases
a frozen required distinction:
  COMPRESSION_TASK_NOT_ESTABLISHED
  unless a higher-priority terminal applies

required records conflict:
  COMPRESSION_TASK_CONFLICTING

multiple admissible interface interpretations
produce different verdicts:
  COMPRESSION_TASK_UNDERDETERMINED
~~~

Guards:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
EVALUABLE_DESTRUCTIVE_LOSS

BLOCKED
  !=
NOT_ESTABLISHED
~~~

## 7. R6 — representation accounting and actual reduction criterion

A Compression claim must freeze what counts as "representation" and what kind of reduction is claimed.

Freeze:

~~~text
REPRESENTATION_ACCOUNTING_SCOPE:
  main_output_only
  output_plus_required_sidecars
  externally_declared_metric

REPRESENTATION_COST_METRIC:
  explicit metric or external contract

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

Rules:

~~~text
if claim is actual package reduction:
  source and reduced package must be evaluated
  under the same frozen accounting metric

main-output shrinkage:
  insufficient when required sidecars are part of the
  frozen accounting scope

all required distinctions preserved
but no frozen reduction requirement met:
  COMPRESSION_TASK_NOT_ESTABLISHED
~~~

Allowed reduction statuses:

~~~text
REDUCTION_ESTABLISHED
REDUCTION_NOT_ESTABLISHED
REDUCTION_BLOCKED
REDUCTION_UNDERDETERMINED
REDUCTION_CONFLICTING
REDUCTION_OUT_OF_SCOPE
~~~

Guards:

~~~text
MAIN_OUTPUT_SHRINKAGE
  !=
TOTAL_REPRESENTATION_REDUCTION

DISTINCTION_PRESERVATION
  !=
COMPRESSION_ESTABLISHED

IDENTITY_TRANSFORMATION
  !=
COMPRESSION_BY_DEFAULT
~~~

## 8. R7 — reconstruction scope and relational coupling

Freeze one reconstruction scope:

~~~text
RECONSTRUCTION_SCOPE_CLASS:
  none
  coordinatewise
  support
  joint_coordinate
  relational_coupling
  full_declared_source_class
~~~

Freeze any required cross-coordinate or relational condition:

~~~text
CROSS_COORDINATE_OR_RELATIONAL_CONDITION:
  not_required
  supplied
  required_but_unavailable
  unresolved
  conflicting
~~~

Rules:

~~~text
required_but_unavailable:
  RECONSTRUCTION_BLOCKED
  and task-level BLOCKED if reconstruction is required
  by the frozen primary claim

unresolved:
  RECONSTRUCTION_UNDERDETERMINED

conflicting:
  task-level CONFLICTING if claim-relevant

supplied:
  evaluate the supplied condition

not_required:
  do not invent one
~~~

Guards:

~~~text
COORDINATEWISE_RECONSTRUCTION
  !=
RELATIONAL_RECONSTRUCTION

INJECTIVITY_ON_DECLARED_CLASS
  !=
GLOBAL_RECONSTRUCTION

COMPRESSION_SUCCESS
  !=
RECONSTRUCTION_SUCCESS
~~~

## 9. R8 — end-to-end composition

For composed compression chains, freeze:

~~~text
COMPOSITION_CLAIM:
  not_claimed
  end_to_end_validation_required
  established_on_declared_chain

COMPRESSION_CHAIN_ID
COMPRESSION_CHAIN_VERSION
CHAIN_STAGE_ORDER
ORIGINAL_PURPOSE_OBLIGATIONS
STAGEWISE_RETAINED_DISTINCTIONS
~~~

Rules:

~~~text
local stage validity:
  does not establish end-to-end validity

for an end-to-end claim:
  propagate the original frozen purpose obligations
  through every stage
  and re-evaluate final collision fibers against
  the original required distinctions
~~~

Guard:

~~~text
LOCAL_STAGE_PASS
  !=
END_TO_END_COMPRESSION_PASS
~~~

A stage may be valid for its own local purpose while the composed chain fails the original source-level purpose.

## 10. Binding task-terminal precedence

Freeze:

~~~text
COMPRESSION_TASK_OUT_OF_SCOPE
>
COMPRESSION_TASK_CONFLICTING
>
COMPRESSION_TASK_UNDERDETERMINED
>
COMPRESSION_TASK_BLOCKED
>
COMPRESSION_TASK_ESTABLISHED /
COMPRESSION_TASK_PARTIAL /
COMPRESSION_TASK_NOT_ESTABLISHED
~~~

Semantics:

~~~text
OUT_OF_SCOPE:
  requested operation or claim lies outside
  the frozen Compression interface

CONFLICTING:
  mutually incompatible applicable claim-relevant
  records exist under the same frozen semantics
  and no precedence resolves them

UNDERDETERMINED:
  multiple admissible claim-relevant purposes,
  resolutions, maps, scopes, classes, or metrics
  yield different outcomes and no resolver exists

BLOCKED:
  a required source interface, sidecar, purpose rule,
  resolution, reconstruction condition, composition rule,
  or accounting metric is unavailable

ESTABLISHED:
  all required obligations are established
  and the frozen reduction criterion is met

PARTIAL:
  multiple independent required obligations exist;
  at least one is established and at least one
  evaluable obligation is not established,
  with no higher-priority terminal

NOT_ESTABLISHED:
  the in-scope claim is evaluable and fails,
  including destructive required-distinction loss
  or failure of the frozen reduction requirement
~~~

Lower-level statuses remain preserved under a higher-priority terminal.

## 11. Binding status families

The executable protocol must keep the following families separate.

### Purpose status

~~~text
PURPOSE_RELATION_CONSISTENT
PURPOSE_RELATION_CONFLICTING
PURPOSE_RELATION_INCOMPLETE
PURPOSE_RELATION_BLOCKED
PURPOSE_RELATION_OUT_OF_SCOPE
~~~

### Resolution status

~~~text
RESOLUTION_NOT_APPLICABLE
RESOLUTION_SUPPLIED
RESOLUTION_BLOCKED
RESOLUTION_UNDERDETERMINED
RESOLUTION_CONFLICTING
~~~

### Reduction status

~~~text
REDUCTION_ESTABLISHED
REDUCTION_NOT_ESTABLISHED
REDUCTION_BLOCKED
REDUCTION_UNDERDETERMINED
REDUCTION_CONFLICTING
REDUCTION_OUT_OF_SCOPE
~~~

### Collision consequence statuses

Keep purpose/status/support/provenance/reconstruction consequence axes separate.

### Reconstruction status

~~~text
RECONSTRUCTION_NOT_CLAIMED
RECONSTRUCTION_ESTABLISHED_ON_DECLARED_CLASS
RECONSTRUCTION_PARTIAL_OR_BOUNDED
RECONSTRUCTION_NOT_ESTABLISHED
RECONSTRUCTION_BLOCKED
RECONSTRUCTION_UNDERDETERMINED
RECONSTRUCTION_CONFLICTING
~~~

These may not be collapsed into one generic PASS/FAIL flag.

## 12. Protocol-freeze authorization

All eight refinement groups are prospective.

They preserve:

~~~text
METHOD_IDENTITY_PRESERVED:
  yes

HISTORICAL_TASK_INTERFACE_REWRITTEN:
  no

HISTORICAL_BOUNDARY_REVIEW_REWRITTEN:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Therefore:

~~~text
PROTOCOL_FREEZE_AUTHORIZED:
  yes
~~~

The next step is to freeze executable Compression Protocol v0.1 using the historical Task Interface together with Boundary Amendment 001.
