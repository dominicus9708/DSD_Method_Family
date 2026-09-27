# DSD Compression Boundary Counterexamples v0.1 Draft

Status: **EXECUTED — PRE-PROTOCOL BOUNDARY ATTACK COMPLETE**  
Date: **2026-09-27**  
Method: **Compression / DSD 압축론**

Task Interface basis:

~~~text
TASK_INTERFACE_COMMIT:
  40cfedf1ce027c84d4c063a306bb5d7ce770be46

TASK_INTERFACE_BLOB:
  a80b776cbac43de4d6d2c761720fb5268aa87d88
~~~

## 1. Purpose

Attack the historical Compression Task Interface v0.1 draft before any executable protocol is frozen.

The attack tests whether the method boundary survives source-supported summary collision, support/status loss, descriptive projection, reconstruction limits, purpose conflict, resolution changes, sidecar accounting, map versioning, class-bounded losslessness, composition, and neighboring-method pressure without silent repair.

Allowed verdicts:

~~~text
PRESERVED_NO_REFINEMENT
PRESERVED_WITH_NONBREAKING_REFINEMENT
BOUNDARY_COLLAPSE
FUNDAMENTAL_INTERFACE_FAILURE
~~~

## 2. Summary result

~~~text
BOUNDARY_ATTACKS_RUN:
  18

PRESERVED_NO_REFINEMENT:
  9

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  9

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

REFINEMENT_GROUPS_REQUIRED:
  8

BOUNDARY_AMENDMENT_REQUIRED:
  yes

PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The draft's atomic method identity survives.

The nine refined attacks expose execution semantics that must be fixed prospectively before protocol freeze.

## 3. C1 — equal finite summary, different strict property structure

Fixture:

~~~text
A and B:
  same property labels
  same per-property domain counts
  same defined-zero counts
  same defined-nonzero counts

but:
  cross-property correlation across typed input locations differs

summary(A) = summary(B)

strict property structure:
  non-isomorphic
~~~

Attack:

~~~text
treat summary equality as sufficient property classification
~~~

Rejected.

The draft already preserves:

~~~text
SUMMARY_EQUALITY != STRICT_PROPERTY_EQUIVALENCE
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 4. C2 — reduced value hides support/status distinctions

Fixture:

~~~text
source S1:
  two present nonzero records cancel

source S2:
  one present defined-zero record

source S3:
  corresponding record absent or undefined

reduced scalar:
  identical where the chosen reduction erases the distinction
~~~

Attack:

~~~text
infer source equality from reduced-value equality
~~~

Rejected.

The draft already separates reduced output from required support/status sidecars.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 5. C3 — descriptive projection erases a latent distinction

Fixture:

~~~text
U != V

Pi_O(U) = Pi_O(V)
~~~

Attack:

~~~text
projected equality
  ->
complete state equality
~~~

Rejected.

The draft already records projection-relative erased distinctions and forbids converse reconstruction without an extra condition.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 6. C4 — purpose-safe collision but reconstruction-destructive collision

Fixture:

~~~text
downstream purpose P:
  x and y may be merged for the immediate readout

compression:
  C(x) = C(y)

reconstruction requirement:
  later task must recover whether source was x or y
~~~

The same collision is:

~~~text
purpose-safe:
  yes

reconstruction-safe:
  no
~~~

Problem:

The draft currently presents collision classes as if one collision receives one primary category.

That is insufficient because safety is multidimensional.

Required refinement R1:

~~~text
COLLISION_PURPOSE_STATUS:
  safe / destructive / unresolved / not_tested

COLLISION_STATUS_RETENTION_STATUS:
  preserved / destructive / unresolved / not_applicable

COLLISION_SUPPORT_RETENTION_STATUS:
  preserved / destructive / unresolved / not_applicable

COLLISION_RECONSTRUCTION_STATUS:
  safe / destructive / blocked / unresolved / not_claimed
~~~

A purpose-safe collision must not overwrite a simultaneous reconstruction-destructive status.

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 7. C5 — required-distinction and acceptable-collision relations disagree

Fixture:

~~~text
(x,y) in REQUIRED_DISTINCTION_P

and

(x,y) in ACCEPTABLE_COLLISION_P
~~~

under the same frozen purpose semantics.

The two declarations conflict.

A second case:

~~~text
pair (u,v):
  neither required-distinct
  nor explicitly safe-to-merge
~~~

The draft must not infer that silence means safety.

Required refinement R2:

~~~text
PURPOSE_RELATION_STATUS:
  consistent
  conflicting
  incomplete
  blocked
  out_of_scope

same pair both required-distinct and safe-to-merge:
  CONFLICTING

claim-relevant pair left unresolved by the frozen purpose contract:
  UNDERDETERMINED

absence from REQUIRED_DISTINCTION
  !=
permission to merge
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 8. C6 — two declared purposes require incompatible compression behavior

Fixture:

~~~text
P1:
  x and y may be merged

P2:
  x and y must remain distinguishable

task claims:
  one compression is valid for {P1,P2}

no purpose precedence or composition rule supplied
~~~

The draft freezes a downstream purpose ID but does not yet freeze how multiple purposes compose.

Required refinement R3:

~~~text
PURPOSE_SCOPE:
  single
  conjunction
  prioritized_family
  alternative_family

PURPOSE_COMPOSITION_RULE:
  explicit

if conjunction contains incompatible obligations:
  CONFLICTING

if several admissible purpose interpretations remain
and yield different verdicts:
  UNDERDETERMINED
~~~

No post-hoc purpose selection after seeing compression performance is allowed.

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 9. C7 — resolution is missing, ambiguous, or changed after evaluation

Fixture A:

~~~text
claim:
  resolution-bounded compression

resolution:
  unavailable
~~~

Fixture B:

~~~text
epsilon in {epsilon_1, epsilon_2}

compression passes at epsilon_1
compression fails at epsilon_2

no frozen resolver
~~~

Fixture C:

~~~text
epsilon changed after result
~~~

Required refinement R4:

~~~text
RESOLUTION_STATUS:
  not_applicable
  supplied
  blocked
  underdetermined
  conflicting

required resolution unavailable:
  BLOCKED

multiple admissible resolutions with different outcomes:
  UNDERDETERMINED

incompatible frozen resolution records:
  CONFLICTING

post-result resolution change:
  new task version
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 10. C8 — required sidecar unavailable versus compression actually erases it

Case A:

~~~text
purpose requires support sidecar
source-side support sidecar is unavailable before compression
~~~

The compression cannot evaluate the obligation.

Case B:

~~~text
required support sidecar is available
compression output/package omits it
~~~

The obligation is evaluable and fails.

Required refinement R5:

~~~text
REQUIRED_INTERFACE_UNAVAILABLE:
  COMPRESSION_TASK_BLOCKED

AVAILABLE_REQUIRED_DISTINCTION_OR_SIDECAR_ERASED:
  COMPRESSION_TASK_NOT_ESTABLISHED

UNAVAILABLE_EVIDENCE
  !=
EVALUABLE_DESTRUCTIVE_LOSS
~~~

The same rule applies to required status and provenance sidecars.

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 11. C9 — compression-map version substitution after seeing the result

Fixture:

~~~text
C-v1:
  frozen before evaluation
  fails one required distinction

C-v2:
  created or selected after observing failure
  passes
~~~

Attack:

~~~text
replace C-v1 by C-v2 inside the same task identity
~~~

Rejected.

The draft already freezes compression-map ID/version and requires a new task version for claim-relevant changes.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 12. C10 — lossless on a bounded class promoted to global losslessness

Fixture:

~~~text
declared source class A:
  C|_A injective

larger class X:
  contains u != v with C(u)=C(v)
~~~

Attack:

~~~text
LOSSLESS_ON_DECLARED_CLASS
  ->
GLOBAL_LOSSLESS
~~~

Rejected.

The draft already preserves:

~~~text
INJECTIVE_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 13. C11 — nonlinear projection forced into kernel language

Fixture:

~~~text
C:
  nonlinear descriptive projection

collision:
  U != V
  C(U)=C(V)

linear structure:
  not supplied
~~~

Attack:

~~~text
describe every erased distinction as a kernel element
~~~

Rejected.

The draft limits kernel analysis to the linear specialization.

The general interface remains fiber/collision based.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 14. C12 — main output shrinks but required sidecars make total package larger

Fixture:

~~~text
source representation:
  100 units

main compressed output:
  20 units

required support/status/provenance sidecars:
  95 units

total retained package:
  115 units
~~~

A main-output-only size ratio would misleadingly report compression.

Required refinement R6:

~~~text
REPRESENTATION_ACCOUNTING_SCOPE:
  main_output_only
  output_plus_required_sidecars
  externally_declared_metric

REPRESENTATION_COST_METRIC:
  frozen before evaluation

SOURCE_COST:
  measured under the frozen metric

REDUCED_PACKAGE_COST:
  measured under the same metric

REDUCTION_STATUS:
  established
  no_reduction
  blocked
  underdetermined
  out_of_scope
~~~

If the primary claim is actual representation reduction and the counted package is not smaller:

~~~text
COMPRESSION_NOT_ESTABLISHED
~~~

unless the task explicitly claims only a different kind of reduction such as resolution reduction under a separately frozen metric.

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 15. C13 — every distinction is preserved but nothing is reduced

Fixture:

~~~text
C:
  identity encoding with renamed fields

required distinctions:
  all preserved

representation cost:
  unchanged under the frozen accounting metric
~~~

The draft's preservation test alone could pass, but a Compression task also requires a declared reduction dimension.

Required refinement:

Use R6 and additionally freeze:

~~~text
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

If no declared reduction occurs:

~~~text
COMPRESSION_NOT_ESTABLISHED
~~~

This does not imply Transformation failure; it means the object did not satisfy the frozen Compression claim.

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 16. C14 — coordinatewise reconstruction does not recover cross-coordinate coupling

Fixture:

~~~text
compressed coordinate Y1:
  individually sufficient to recover source coordinate X1

compressed coordinate Y2:
  individually sufficient to recover source coordinate X2

target reconstruction:
  must also recover relation R(X1,X2)

cross-coordinate coupling rule:
  unavailable
~~~

Coordinatewise sufficiency does not establish joint relational reconstruction.

Required refinement R7:

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

required_but_unavailable:
  RECONSTRUCTION_BLOCKED
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 17. C15 — equal dynamic reduced readout across distinct component states

Fixture:

~~~text
U(t) != V(t)

O_t(U(t)) = O_t(V(t))
for all t in tested interval
~~~

Attack:

~~~text
equal reduced readout
  ->
equal dynamic component-resolved state
~~~

Rejected.

The draft already preserves:

~~~text
READOUT_EQUALITY != DYNAMIC_STATE_EQUALITY
REDUCED_READOUT != COMPLETE_CLASSIFIER
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 18. C16 — randomized or stochastic encoder presented as the current deterministic map interface

Fixture:

~~~text
same source x

run 1:
  z1

run 2:
  z2

no seed / kernel / probability semantics frozen
~~~

The current draft defines Compression through a declared map C:X_task->Z_C.

A stochastic encoder without an explicitly supplied stochastic interface is outside this current draft.

Required handling:

~~~text
current deterministic interface:
  OUT_OF_SCOPE

do not silently convert randomness into nondeterministic evidence
or average outputs post hoc
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

This does not claim stochastic compression is impossible; it is simply outside the present interface.

## 19. C17 — sequential composition of individually valid compressors destroys the original purpose

Fixture:

~~~text
C1:
  valid relative to P1

C2:
  valid relative to P2 on C1 output

composite:
  C2 o C1

original claim:
  preserve P1 distinctions end-to-end

but:
  C2 merges outputs that encode a P1-required distinction
~~~

Individual validity does not imply composite validity for the original purpose.

Required refinement R8:

~~~text
COMPOSITION_CLAIM:
  not_claimed
  end_to_end_validation_required
  established_on_declared_chain

for a composite claim:
  freeze source purpose obligations at chain input
  propagate required retained distinctions through each stage
  re-evaluate final fibers against the original frozen obligations

LOCAL_STAGE_PASS != END_TO_END_COMPRESSION_PASS
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 20. C18 — neighboring-method and NO_GAIN pressure

Fixture:

~~~text
Aggregation:
  already emits a smaller scalar readout

Transformation:
  already maps source to a reduced coordinate package

Classification:
  already succeeds on the same downstream task

generic non-DSD codec:
  preserves the same required distinctions
  at equal or lower representation cost
~~~

Attack:

~~~text
because another method or baseline can produce the same reduced artifact,
Compression collapses into that method or must be deleted
~~~

Rejected.

Method identity remains five-interface based.

A later fair baseline may yield:

~~~text
NO_GAIN
~~~

without implying method failure, deletion, merger, or absorption.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 21. Required refinement groups

The nine refined attacks collapse into eight prospective amendment groups.

### R1 — multidimensional collision consequences

Do not force purpose, status, support, and reconstruction consequences into one exclusive collision label.

### R2 — purpose-relation consistency and incompleteness

Freeze consistency semantics for required-distinction and acceptable-collision declarations.

Silence is not permission to merge.

### R3 — multi-purpose composition

Freeze single/conjunctive/prioritized/alternative purpose semantics before evaluation.

### R4 — resolution semantics

Freeze resolution status and distinguish unavailable, ambiguous, conflicting, and version-changed cases.

### R5 — unavailable required interface versus evaluable destructive loss

Unavailable required sidecar/interface -> BLOCKED.

Available but erased required information -> NOT_ESTABLISHED.

### R6 — representation accounting and actual reduction criterion

Freeze accounting scope, cost metric, reduction dimension, and required amount/type of reduction.

Main-output shrinkage alone is insufficient when required sidecars are claim-relevant.

### R7 — reconstruction scope and relational coupling

Separate coordinatewise, support, joint-coordinate, relational, and full-class reconstruction scopes.

### R8 — end-to-end composition

Do not infer composite Compression validity from local stage validity.

## 22. Terminal-precedence requirement

The draft intentionally left terminal precedence open.

The amendment must freeze:

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

Required semantics:

~~~text
OUT_OF_SCOPE:
  requested operation/claim lies outside the frozen Compression interface

CONFLICTING:
  mutually incompatible applicable claim-relevant records
  exist under the same frozen semantics

UNDERDETERMINED:
  multiple admissible claim-relevant purposes/resolutions/maps/scopes
  yield different outcomes and no resolver exists

BLOCKED:
  a required source interface, sidecar, purpose rule,
  resolution, reconstruction condition, or metric is unavailable

ESTABLISHED:
  all required obligations pass and the frozen reduction criterion is met

PARTIAL:
  multiple independent required obligations exist;
  at least one is established and at least one evaluable obligation
  is not established, with no higher-priority terminal

NOT_ESTABLISHED:
  the in-scope claim is evaluable and fails,
  including destructive required-distinction loss
  or failure of the frozen reduction requirement
~~~

Lower-level collision, retention, reconstruction, and reduction statuses remain visible under a higher-priority task terminal.

## 23. Final boundary verdict

~~~text
METHOD_IDENTITY_PRESERVED:
  yes

BOUNDARY_COLLAPSE_FOUND:
  no

FUNDAMENTAL_INTERFACE_FAILURE:
  no

BOUNDARY_AMENDMENT_001_REQUIRED:
  yes

REFINEMENT_GROUPS:
  8

PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The historical Task Interface v0.1 draft remains unchanged.

The next step is a prospective Task Interface Boundary Amendment 001 that binds R1-R8 and terminal precedence before an executable Compression Protocol is frozen.
