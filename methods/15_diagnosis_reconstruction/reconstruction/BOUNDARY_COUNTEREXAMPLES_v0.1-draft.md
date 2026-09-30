# DSD Reconstruction Boundary Counterexamples v0.1 — Pre-Protocol Attack Record

Status: **EXECUTED — PRE-PROTOCOL BOUNDARY ATTACK COMPLETE**  
Date: **2026-10-01**  
Method: **Reconstruction / DSD 복원론**

Purpose: pressure the historical Reconstruction Task Interface before any executable Reconstruction Protocol is frozen.

These are constructed internal counterexamples.

They are not external validation.

Task Interface under attack:

~~~text
TASK_INTERFACE_COMMIT:
  b12426af3c5ed053c8383e4b242d761251af8d22

TASK_INTERFACE_BLOB:
  92bfa7f9e523af0886169bf76d2854870ba202e3
~~~

Source-registry basis:

~~~text
SOURCE_REGISTRY_COMMIT:
  78acf2532680722cf09a50376d0c69d74803f1a4

SOURCE_REGISTRY_BLOB:
  f00063f285745dd328e5b2d8c82ff3579957d615
~~~

The historical Task Interface is not rewritten by this attack.

## 1. Results summary

~~~text
BOUNDARY_ATTACKS_RUN:
  18

PRESERVED_NO_REFINEMENT:
  10

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  8

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

BOUNDARY_AMENDMENT_REQUIRED:
  yes

REFINEMENT_GROUPS_REQUIRED:
  8

PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The eight refinement groups concern candidate-class representation, evidence coherence, required-interface semantics, frozen-interface closure for unrecoverability, history-relation coherence, definitional-recompletion scope, probabilistic inference scope, and task-terminal semantics.

None changes the Reconstruction method identity.

## 2. RCN-B01 — non-enumerated reconstruction class

Frozen reconstruction class:

~~~text
H = { x in R^3 : A x = y }
~~~

The class is:

~~~text
uncountable or otherwise not intended for explicit enumeration
represented by:
  a predicate / equation / parameterization

explicit candidate list:
  unavailable by design
~~~

The historical Task Interface requires:

~~~text
RECONSTRUCTION_CANDIDATE_IDENTITIES
~~~

and its working operation says:

~~~text
evaluate every declared source/history candidate
~~~

Attack:

~~~text
require literal enumeration of every h in H
before Reconstruction can be executed
~~~

This overconstrains Reconstruction to list-like candidate registries and is not required by the recovered source constraints.

A reconstruction class may be represented intensionally and evaluated by theorem, symbolic fiber, exact solver relation, or other frozen class-level procedure.

Required prospective refinement R1:

~~~text
RECONSTRUCTION_CLASS_REPRESENTATION_MODE:
  EXPLICIT_ENUMERATION
  PARAMETRIC_CLASS
  PREDICATE_DEFINED_CLASS
  RELATION_DEFINED_CLASS
  EXTERNALLY_SUPPLIED_CLASS_INTERFACE

RECONSTRUCTION_CLASS_REPRESENTATION:
  frozen definition / registry

CANDIDATE_EVALUATION_MODE:
  ELEMENTWISE
  SYMBOLIC_SET
  EXACT_FIBER_OR_PREIMAGE
  THEOREM_OR_RELATION_BASED
  EXTERNALLY_SUPPLIED_EVALUATOR
~~~

If explicit candidate identities are not the representation mode, they are not required one-by-one.

The protocol must still freeze the candidate class before claim-relevant evaluation and preserve class-completeness status.

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R1 candidate-class representation and evaluation mode
~~~

## 3. RCN-B02 — multiple compatible reconstructions under fully frozen semantics

Frozen class:

~~~text
H = {h1,h2,h3}
~~~

Evaluation:

~~~text
h1:
  compatible

h2:
  compatible

h3:
  excluded
~~~

Primary claim:

~~~text
RECONSTRUCTION_COMPATIBILITY_SET
~~~

Required:

~~~text
compatible:
  {h1,h2}

excluded:
  {h3}

RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE

overall Reconstruction:
  may be ESTABLISHED
~~~

Attack:

~~~text
multiple compatible reconstructions
  ->
task underdetermined
or
protocol failure
~~~

Rejected.

Guard already present:

~~~text
MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 4. RCN-B03 — one surviving declared reconstruction with incomplete class

Frozen:

~~~text
declared class:
  {h1,h2,h3}

class completeness:
  RECONSTRUCTION_CLASS_COMPLETENESS_NOT_CLAIMED

evidence:
  excludes h1
  excludes h2
  retains h3
~~~

Required:

~~~text
RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS

not:
  GLOBAL_HISTORICAL_TRUTH
  ONE_POSSIBLE_REAL_PAST
~~~

The draft already preserves:

~~~text
ONE_SURVIVING_DECLARED_RECONSTRUCTION
  !=
ONE_POSSIBLE_REAL_PAST
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 5. RCN-B04 — zero compatible reconstructions in a declared class

Frozen:

~~~text
H = {h1,h2}

every required candidate/evidence relation:
  evaluable

h1:
  excluded

h2:
  excluded

evidence packet:
  coherent
~~~

Required:

~~~text
RECONSTRUCTION_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
~~~

Forbidden:

~~~text
NO_REAL_PAST_STATE
NO_REAL_HISTORY
REALITY_IMPOSSIBLE
~~~

Guard already present:

~~~text
NO_ADMISSIBLE_DECLARED_RECONSTRUCTION
  !=
NO_REAL_PAST_STATE_OR_HISTORY
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 6. RCN-B05 — internally conflicting evidence packet

Frozen evidence:

~~~text
e1:
  same source field
  same time / regime / schema
  status = valid
  value = 0

e2:
  same source field
  same time / regime / schema
  status = valid
  value = 1

readout semantics:
  exact single-valued
  no tolerance
  no precedence
  no multiplexing rule
~~~

Every candidate can be made to fail at least one record.

Attack:

~~~text
return NONE_COMPATIBLE_IN_DECLARED_CLASS
without first representing the evidence packet conflict
~~~

The Task Interface has pair/candidate conflict states, but it does not yet freeze an evidence-set coherence status before candidate reconstruction.

Required prospective refinement R2:

~~~text
EVIDENCE_SET_COHERENCE_STATUS:
  CONSISTENT
  CONFLICTING
  UNDERDETERMINED
  BLOCKED
  OUT_OF_SCOPE

EVIDENCE_CONFLICT_RESOLVER_OR_NONE
EVIDENCE_PRECEDENCE_RULE_OR_NONE
~~~

For this fixture:

~~~text
EVIDENCE_SET_COHERENCE_STATUS:
  CONFLICTING

task-level consequence:
  RECONSTRUCTION_CONFLICTING
  unless a frozen resolver/precedence rule applies
~~~

A conflicting evidence packet may not be silently reinterpreted as evidence that no source existed.

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R2 evidence-set coherence and conflict semantics
~~~

## 7. RCN-B06 — mutually incompatible same-version bridge rules

Frozen bridge registry:

~~~text
BRIDGE-v4 rule A:
  h + e -> RECONSTRUCTION_PAIR_COMPATIBLE

BRIDGE-v4 rule B:
  h + e -> RECONSTRUCTION_PAIR_INCOMPATIBLE

same applicability scope:
  yes

resolver:
  none
~~~

The Task Interface already includes:

~~~text
RECONSTRUCTION_PAIR_CONFLICTING

RECONSTRUCTION_CANDIDATE_CONFLICTING

RECONSTRUCTION_CONFLICTING
~~~

and defines pair conflict as mutually incompatible applicable frozen records under the same semantics.

Required:

~~~text
pair:
  RECONSTRUCTION_PAIR_CONFLICTING

candidate:
  RECONSTRUCTION_CANDIDATE_CONFLICTING

task:
  RECONSTRUCTION_CONFLICTING
  when claim-relevant
~~~

No additional method-level state family is forced by this fixture.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 8. RCN-B07 — equal output with distinct source supports

Frozen sources:

~~~text
h1 != h2
~~~

Frozen forward/readout map:

~~~text
F(h1) = y
F(h2) = y
~~~

No frozen distinguishing sidecar is part of this claim.

Primary claim:

~~~text
RECONSTRUCTION_COMPATIBILITY_SET
~~~

Required:

~~~text
h1:
  compatible

h2:
  compatible

RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE
~~~

Forbidden:

~~~text
EQUAL_OUTPUT -> EQUAL_SOURCE
select h1
select h2
~~~

The Task Interface already preserves:

~~~text
EQUAL_OUTPUT != EQUAL_SOURCE

NONINJECTIVE_FORWARD_MAP
  !=
LICENSE_TO_SELECT_ONE_PREIMAGE
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 9. RCN-B08 — injective on declared class but not globally

Frozen:

~~~text
declared reconstruction class:
  H

F|_H:
  injective

outside H:
  collisions exist
~~~

Evidence selects one candidate in H.

Class completeness:

~~~text
not claimed globally
~~~

Required:

~~~text
UNIQUE_WITHIN_DECLARED_RECONSTRUCTION_CLASS:
  may be established

GLOBAL_INJECTIVITY:
  not established

GLOBAL_HISTORICAL_TRUTH:
  not established
~~~

The Task Interface already preserves:

~~~text
LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY

UNIQUE_WITHIN_DECLARED_CLASS != GLOBAL_HISTORICAL_TRUTH
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 10. RCN-B09 — coordinatewise recovery without relational recovery

Frozen source coordinates:

~~~text
X1
X2
~~~

Frozen retained data recover:

~~~text
X1:
  uniquely recoverable

X2:
  uniquely recoverable
~~~

Requested source claim also requires:

~~~text
R(X1,X2)
~~~

But:

~~~text
relational / cross-coordinate sidecar:
  not supplied

two distinct relations:
  remain compatible with the same coordinate values
~~~

Required:

~~~text
coordinate values:
  recoverable on declared coordinatewise scope

relational coupling:
  not established
~~~

Forbidden:

~~~text
COORDINATEWISE_RECOVERY
  ->
RELATIONAL_OR_FULL_SOURCE_RECOVERY
~~~

The Task Interface already freezes reconstruction scope and required relational/cross-coordinate conditions.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 11. RCN-B10 — required sidecar unavailable

Frozen claim:

~~~text
target:
  relational source reconstruction

main readout:
  available

required relational/support sidecar:
  declared required

availability:
  unavailable
~~~

The draft correctly states:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
DEMONSTRATED_UNRECOVERABILITY
~~~

but Section 13 currently allows:

~~~text
required sidecar unavailable
  ->
BLOCKED or PARTIAL
according to the frozen task semantics
~~~

while the draft terminal precedence places:

~~~text
BLOCKED
>
PARTIAL
~~~

The exact execution consequence is therefore insufficiently frozen.

Required prospective refinement R3:

~~~text
REQUIRED_RECONSTRUCTION_INTERFACE_STATUS:
  AVAILABLE
  UNAVAILABLE
  CONFLICTING
  UNDERDETERMINED
  OUT_OF_SCOPE
~~~

Rules:

~~~text
required interface unavailable
and required for the primary claim:
  RECONSTRUCTION_TASK_BLOCKED

required information available
but demonstrably insufficient / destructively erased:
  evaluable NOT_ESTABLISHED or
  frozen unrecoverability status,
  not BLOCKED

required interface conflicting:
  RECONSTRUCTION_TASK_CONFLICTING

required interface semantics underdetermined:
  RECONSTRUCTION_TASK_UNDERDETERMINED
~~~

A PARTIAL terminal may only be considered under the separately frozen multi-obligation semantics of R8.

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R3 required-interface availability and BLOCKED semantics
~~~

## 12. RCN-B11 — apparent collision without frozen-interface closure

Frozen:

~~~text
h1 != h2

current main readout:
  F(h1) = F(h2) = y

currently registered sidecars:
  none
~~~

Request:

~~~text
UNRECOVERABLE_INFORMATION_ON_FROZEN_INTERFACE
~~~

But the task does not state whether the frozen interface is complete for the requested reconstruction distinction.

Possibility:

~~~text
a claim-relevant sidecar exists in the source system
but was simply not registered into this task
~~~

Attack:

~~~text
"no registered sidecar"
  ->
"distinction proven unrecoverable on the frozen interface"
~~~

This is insufficient.

The current Task Interface correctly distinguishes interface unavailability from unrecoverability, but it does not yet freeze a positive closure/completeness status for the interface package used to prove unrecoverability.

Required prospective refinement R4:

~~~text
RECONSTRUCTION_INTERFACE_CLOSURE_STATUS:
  COMPLETE_FOR_DECLARED_CLAIM
  EXPLICITLY_PARTIAL
  COMPLETENESS_UNDERDETERMINED
  BLOCKED
  OUT_OF_SCOPE

FROZEN_INTERFACE_COMPONENT_REGISTER
FROZEN_INTERFACE_COMPLETENESS_PROVENANCE
~~~

An unrecoverability claim requires at least:

~~~text
two distinct in-scope admissible sources
+
same frozen claim-relevant evidence/readout package
+
RECONSTRUCTION_INTERFACE_CLOSURE_STATUS =
  COMPLETE_FOR_DECLARED_CLAIM
+
no frozen component distinguishes them
+
requested distinction lies inside the frozen reconstruction scope
~~~

Guard:

~~~text
NO_REGISTERED_DISTINGUISHER
  !=
PROVED_UNRECOVERABILITY
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R4 frozen-interface closure for unrecoverability claims
~~~

## 13. RCN-B12 — Formation witness-history treated as temporal history

Frozen Formation handoff:

~~~text
candidate channel:
  admitted

compatible formation witness histories:
  nonempty
~~~

No temporal event semantics are supplied.

Attack:

~~~text
formation witness history
  ->
actual temporal event history
~~~

Rejected.

The Task Interface already preserves:

~~~text
FORMATION_WITNESS_HISTORY
  !=
ACTUAL_TEMPORAL_HISTORY

STAGE_DEPENDENCY_ORDER
  !=
PHYSICAL_TIME_ORDER
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 14. RCN-B13 — branching / merging transition relation

Frozen transition relation:

~~~text
p1 -> s
p2 -> s

s -> q1
s -> q2
~~~

No unique predecessor or unique successor condition is supplied.

Present evidence identifies:

~~~text
s
~~~

Requested history:

~~~text
which exact predecessor path occurred?
~~~

Required:

~~~text
multiple predecessor/history candidates remain visible

branching:
  allowed

merging:
  allowed

unique predecessor/path:
  not established
~~~

The Task Interface already freezes branching/merging and unique-predecessor/path requirements.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 15. RCN-B14 — direct history relation conflicts with composed intermediate records

Frozen:

~~~text
direct long-interval record:
  a -> c
  status = valid

intermediate records:
  a -> b
  b !-> c
  status = valid

same history scope / regime / relation family:
  yes

composition / precedence rule:
  absent
~~~

Attack:

~~~text
silently prefer the direct record
or
silently prefer the composed intermediate chain
~~~

The Task Interface freezes direct long-interval and intermediate records but does not yet freeze a history-relation coherence/composition status.

Required prospective refinement R5:

~~~text
HISTORY_RELATION_COHERENCE_STATUS:
  CONSISTENT
  CONFLICTING
  UNDERDETERMINED
  BLOCKED
  OUT_OF_SCOPE

HISTORY_COMPOSITION_RULE_OR_NONE
HISTORY_PRECEDENCE_RULE_OR_NONE
DIRECT_VS_COMPOSED_RELATION_POLICY
~~~

If claim-relevant direct and composed records conflict under the same frozen semantics and no resolver exists:

~~~text
RECONSTRUCTION_TASK_CONFLICTING
~~~

If multiple admissible composition rules yield different histories and no resolver exists:

~~~text
RECONSTRUCTION_TASK_UNDERDETERMINED
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R5 history-relation coherence and composition semantics
~~~

## 16. RCN-B15 — pure definitional recompletion presented as Reconstruction

Frozen Property primitive core:

~~~text
complete primitive coordinates:
  supplied

requested output:
  derived Property status / defined-record coordinate

closure rule:
  uniquely definitional
~~~

No prior state, missing source, damaged structure, compressed source, or hidden history is being inferred.

Attack:

~~~text
count deterministic definitional recompletion
as a successful Reconstruction case
~~~

The Task Interface correctly distinguishes:

~~~text
DEFINITIONAL_RECOMPLETION
  !=
EVIDENCE_BASED_RECONSTRUCTION
~~~

but currently says a pure recompletion task "may be out of scope."

The protocol requires an exact boundary.

Required prospective refinement R6:

~~~text
DEFINITIONAL_RECOMPLETION_ROLE:
  NOT_USED
  SUBORDINATE_DETERMINISTIC_STEP
  PRIMARY_REQUEST_ONLY
~~~

Rules:

~~~text
PRIMARY_REQUEST_ONLY
and complete primitive core supplied:
  RECONSTRUCTION_TASK_OUT_OF_SCOPE
  for the Reconstruction claim

SUBORDINATE_DETERMINISTIC_STEP:
  allowed inside a genuine Reconstruction task
  but must not be counted as independent
  Reconstruction evidence

NOT_USED:
  no recompletion semantics imported
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R6 definitional-recompletion scope
~~~

## 17. RCN-B16 — "most probable past" requested without probabilistic interface

Frozen task provides:

~~~text
declared candidate histories
deterministic compatibility bridges
evidence packet

prior:
  absent

likelihood model:
  absent

posterior semantics:
  absent

decision loss:
  absent
~~~

Request:

~~~text
Which compatible history is most probable?
~~~

The Task Interface guards:

~~~text
CANDIDATE_RANKING != CANDIDATE_ELIMINATION
PROBABILITY != HISTORICAL_TRUTH
~~~

but does not yet freeze the inference-mode scope.

Required prospective refinement R7:

~~~text
INFERENCE_MODE:
  DETERMINISTIC_COMPATIBILITY
  PROBABILISTIC_IF_EXPLICITLY_SUPPLIED

default Protocol v0.1 mode:
  DETERMINISTIC_COMPATIBILITY
~~~

Rules:

~~~text
posterior / probability ranking request
without explicit probabilistic interface:
  RECONSTRUCTION_TASK_OUT_OF_SCOPE
  for the ranking claim

compatibility-set Reconstruction:
  may remain independently established

probabilistic ranking when supplied:
  ranking remains separate from historical truth
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R7 deterministic / probabilistic inference-mode scope
~~~

## 18. RCN-B17 — neighboring-method substitution and additional-evidence pressure

Frozen Reconstruction result:

~~~text
compatible histories:
  {h1,h2}

remaining distinction:
  feature f
~~~

Available neighboring results:

~~~text
Tracking:
  one observed trace segment

Lineage:
  one established successor identity

Diagnosis:
  present hidden state identified

Measurement:
  a possible discriminator is known

Audit:
  evidence procedure passes
~~~

Attack A:

~~~text
any neighboring result
  ->
unique Reconstruction result
without the Reconstruction bridge evaluation
~~~

Rejected.

Attack B:

~~~text
Reconstruction must itself choose the globally optimal
next measurement under cost/risk/information objective
~~~

Rejected unless a separate Measurement/Optimization task is supplied.

The Task Interface already preserves:

~~~text
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
RECONSTRUCTION_CANDIDATE != ESTABLISHED_LINEAGE
CURRENT_STATE_DIAGNOSIS != PAST_OR_OMITTED_RECONSTRUCTION
NEED_FOR_ADDITIONAL_EVIDENCE != OPTIMAL_MEASUREMENT_SELECTED
RECONSTRUCTION_DISCRIMINATOR_REQUIREMENT != OPTIMIZATION_RESULT
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 19. RCN-B18 — multi-obligation mixed result and terminal precedence

Frozen task contains independent required obligations:

~~~text
Q1:
  compatibility-set reconstruction
  established

Q2:
  relational reconstruction
  required sidecar unavailable
  blocked

Q3:
  posterior ranking
  no probabilistic interface
  out of scope

Q4:
  history records conflict
  conflicting
~~~

The historical Task Interface proposes:

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

but explicitly leaves it unfrozen.

It also defines PARTIAL using:

~~~text
at least one validly established
+
at least one validly not established or unevaluable
~~~

This could allow a BLOCKED subordinate obligation to be relabeled PARTIAL despite BLOCKED having higher precedence.

Required prospective refinement R8:

~~~text
RECONSTRUCTION_TASK_OUT_OF_SCOPE
>
RECONSTRUCTION_TASK_CONFLICTING
>
RECONSTRUCTION_TASK_UNDERDETERMINED
>
RECONSTRUCTION_TASK_BLOCKED
>
RECONSTRUCTION_TASK_ESTABLISHED /
RECONSTRUCTION_TASK_PARTIAL /
RECONSTRUCTION_TASK_NOT_ESTABLISHED
~~~

Exact PARTIAL semantics:

~~~text
PARTIAL:
  multiple independently required in-scope obligations exist;
  at least one is ESTABLISHED;
  at least one other independently required obligation is
  evaluably NOT_ESTABLISHED;
  no required obligation is BLOCKED;
  no higher-priority terminal applies

PARTIAL
  !=
rescue label for a BLOCKED atomic obligation

PARTIAL
  !=
rescue label for one failed atomic proposition
~~~

For this fixture:

~~~text
task terminal:
  RECONSTRUCTION_TASK_OUT_OF_SCOPE

subordinate records retained:
  Q1 established
  Q2 blocked
  Q4 conflicting
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R8 task-terminal precedence and exact PARTIAL semantics
~~~

## 20. Refinement groups

The boundary attack preserves the Reconstruction method identity but requires eight prospective execution refinements.

~~~text
R1
  candidate-class representation and evaluation mode

R2
  evidence-set coherence and conflict semantics

R3
  required-interface availability and BLOCKED semantics

R4
  frozen-interface closure for unrecoverability claims

R5
  history-relation coherence and composition semantics

R6
  definitional-recompletion scope

R7
  deterministic versus explicitly supplied probabilistic
  inference-mode scope

R8
  task-terminal precedence and exact PARTIAL semantics
~~~

## 21. Forced prospective amendment

Reconstruction Task Interface Boundary Amendment 001 must add or freeze at least:

~~~text
A. RECONSTRUCTION_CLASS_REPRESENTATION_MODE
   and CANDIDATE_EVALUATION_MODE
   so non-enumerated classes are admissible without
   post-hoc class changes

B. EVIDENCE_SET_COHERENCE_STATUS
   with explicit conflict / underdetermined / blocked consequences

C. REQUIRED_RECONSTRUCTION_INTERFACE_STATUS
   with:
     unavailable required interface -> BLOCKED
     evaluable destructive loss -> NOT_ESTABLISHED or
       an explicitly supported unrecoverability claim
     conflict -> CONFLICTING
     unresolved semantics -> UNDERDETERMINED

D. RECONSTRUCTION_INTERFACE_CLOSURE_STATUS
   so "no registered distinguisher" is not enough
   to prove unrecoverability

E. HISTORY_RELATION_COHERENCE_STATUS
   and frozen direct-versus-composed
   history-relation semantics

F. DEFINITIONAL_RECOMPLETION_ROLE
   with pure recompletion outside the Reconstruction
   evidence count

G. INFERENCE_MODE
   with deterministic compatibility as default v0.1
   and probabilistic ranking only through an explicit interface

H. exact task-terminal precedence and PARTIAL semantics
~~~

The Amendment may refine execution status semantics and class representation.

It must not rewrite the historical Task Interface v0.1 draft.

## 22. Boundary result

No attack requires collapsing Reconstruction into:

~~~text
Diagnosis
Tracking
Lineage
Aggregation
Compression
Transformation
Measurement
Comparison
Audit
Optimization
~~~

No attack requires changing the recovered source-derived core:

~~~text
equal output does not imply equal source

noninjective forward structure preserves multiple
compatible reconstructions unless additional
frozen evidence eliminates them

class-local injectivity does not become global uniqueness

coordinatewise recovery does not become relational recovery

formation witness-history does not become temporal history

relation-valued transitions may branch and merge

reconstructed links do not become observed Tracking links

candidate predecessor relations do not become established Lineage

definitional recompletion remains distinct from
evidence-based reconstruction

interface unavailability does not prove destructive information loss

current-state Diagnosis does not reconstruct unique history
~~~

The historical Task Interface remains unchanged.

## 23. Current state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 historical draft preserved

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

PRESERVED_NO_REFINEMENT:
  10

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  8

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

BOUNDARY_AMENDMENT_001:
  not yet established

REFINEMENT_GROUPS_REQUIRED:
  8

DEDICATED_RECONSTRUCTION_PROTOCOL:
  not established

DIRECT_RECONSTRUCTION_PILOTS_ATTEMPTED:
  0

BASELINE_RECONSTRUCTION_CASES:
  0

NO_GAIN_RECONSTRUCTION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_RECONSTRUCTION_APPLICATIONS:
  0

INDEPENDENT_RECONSTRUCTION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

RECONSTRUCTION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_RECONSTRUCTION_EVIDENCE_STATUS:
  pre_protocol_boundary_attack_complete

PROTOCOL_REVISION_REQUIRED:
  not applicable pre-protocol

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 24. Next

Establish Reconstruction Task Interface Boundary Amendment 001 prospectively.

Protocol freeze is not authorized before that Amendment is established.
