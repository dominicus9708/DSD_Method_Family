# DSD Reconstruction Task Interface Boundary Amendment 001

Status: **PROSPECTIVE AMENDMENT ESTABLISHED**  
Date: **2026-10-01**  
Method: **Reconstruction / DSD 복원론**

Frozen historical basis:

~~~text
SOURCE_REGISTRY_COMMIT:
  78acf2532680722cf09a50376d0c69d74803f1a4

SOURCE_REGISTRY_BLOB:
  f00063f285745dd328e5b2d8c82ff3579957d615

TASK_INTERFACE_COMMIT:
  b12426af3c5ed053c8383e4b242d761251af8d22

TASK_INTERFACE_BLOB:
  92bfa7f9e523af0886169bf76d2854870ba202e3

BOUNDARY_ATTACK_COMMIT:
  27d0ead2e3a95b0ce8eb08169a3c56714384f1d6

BOUNDARY_ATTACK_BLOB:
  01b083199069477d0b8aec6518709eba735dc893
~~~

The historical Task Interface and boundary-attack record are not rewritten.

This Amendment prospectively binds the eight nonbreaking refinements forced by the 18 pre-protocol Reconstruction boundary attacks.

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

HISTORICAL_TASK_INTERFACE_REWRITTEN:
  no

HISTORICAL_BOUNDARY_ATTACK_RECORD_REWRITTEN:
  no

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

PROTOCOL_FREEZE_AUTHORIZED:
  yes

DIRECT_RECONSTRUCTION_PILOTS_ATTEMPTED:
  0

EXTERNAL_APPLICATION:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 2. R1 — reconstruction-class representation and evaluation mode

The historical Task Interface can be read too narrowly if `RECONSTRUCTION_CANDIDATE_IDENTITIES` is interpreted as requiring explicit enumeration.

Protocol v0.1 must support both extensional and intensional reconstruction classes.

Freeze:

~~~text
RECONSTRUCTION_CLASS_ID
RECONSTRUCTION_CLASS_VERSION_OR_DEFINITION
RECONSTRUCTION_CLASS_REPRESENTATION_MODE
RECONSTRUCTION_CLASS_REPRESENTATION
CANDIDATE_EVALUATION_MODE
RECONSTRUCTION_CLASS_COMPLETENESS_STATUS
~~~

Allowed representation modes:

~~~text
EXPLICIT_ENUMERATION
PARAMETRIC_CLASS
PREDICATE_DEFINED_CLASS
RELATION_DEFINED_CLASS
EXTERNALLY_SUPPLIED_CLASS_INTERFACE
~~~

Allowed evaluation modes:

~~~text
ELEMENTWISE
SYMBOLIC_SET
EXACT_FIBER_OR_PREIMAGE
THEOREM_OR_RELATION_BASED
EXTERNALLY_SUPPLIED_EVALUATOR
~~~

Rules:

~~~text
EXPLICIT_ENUMERATION:
  explicit candidate identities are required

PARAMETRIC_CLASS /
PREDICATE_DEFINED_CLASS /
RELATION_DEFINED_CLASS:
  the frozen class definition is the candidate-class identity
  and literal enumeration is not required

EXACT_FIBER_OR_PREIMAGE:
  a complete exact symbolic fiber/preimage may stand
  for candidate-by-candidate listing when the class semantics support it

THEOREM_OR_RELATION_BASED:
  a frozen theorem or relation may establish class-level
  compatibility, exclusion, multiplicity, or uniqueness claims
  without enumerating every element
~~~

Required guards:

~~~text
NON_ENUMERATED_CLASS
  !=
UNDECLARED_CLASS

INTENSIONAL_CLASS_DEFINITION
  !=
POST_HOC_CANDIDATE_EXPANSION

SYMBOLIC_CLASS_RESULT
  !=
GLOBAL_COMPLETENESS_BY_DEFAULT
~~~

Changing the representation/evaluation mode after claim-relevant results are known opens a new task version.

## 3. R2 — evidence-set coherence and conflict semantics

Before reconstruction-candidate elimination is interpreted as a source/history result, Protocol v0.1 must evaluate coherence of the frozen claim-relevant evidence set.

Freeze:

~~~text
EVIDENCE_SET_ID
EVIDENCE_SET_VERSION
EVIDENCE_SET_SCOPE
EVIDENCE_SET_COHERENCE_STATUS
EVIDENCE_CONFLICT_RESOLVER_OR_NONE
EVIDENCE_PRECEDENCE_RULE_OR_NONE
~~~

Status family:

~~~text
EVIDENCE_SET_CONSISTENT
EVIDENCE_SET_CONFLICTING
EVIDENCE_SET_UNDERDETERMINED
EVIDENCE_SET_BLOCKED
EVIDENCE_SET_OUT_OF_SCOPE
~~~

Semantics:

~~~text
CONSISTENT:
  the supplied claim-relevant evidence records can be jointly
  interpreted under the frozen schema, time, regime,
  resolution, and precedence semantics

CONFLICTING:
  mutually incompatible applicable evidence records exist
  under the same frozen semantics and no frozen resolver
  or precedence rule resolves them

UNDERDETERMINED:
  multiple admissible evidence-set interpretations remain
  and produce different claim-relevant reconstruction outcomes

BLOCKED:
  coherence cannot be evaluated because a required
  evidence-interface dependency is unavailable

OUT_OF_SCOPE:
  the evidence packet lies outside the frozen Reconstruction task
~~~

Required guards:

~~~text
EVIDENCE_SET_CONFLICTING
  !=
RECONSTRUCTION_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS

EVIDENCE_CONFLICT
  !=
SOURCE_NONEXISTENCE

MUTUALLY_INCOMPATIBLE_OBSERVATIONS
  !=
NO_REAL_PAST_STATE_OR_HISTORY
~~~

Unresolved claim-relevant evidence conflict yields:

~~~text
RECONSTRUCTION_CONFLICTING
RECONSTRUCTION_TASK_CONFLICTING
~~~

unless a higher-priority frozen out-of-scope condition applies.

## 4. R3 — required Reconstruction interface availability and BLOCKED semantics

Protocol v0.1 must maintain an explicit status for every required claim-relevant interface not already fully represented by evidence-set or bridge status.

Freeze:

~~~text
REQUIRED_RECONSTRUCTION_INTERFACE_ID
REQUIRED_RECONSTRUCTION_INTERFACE_ROLE
REQUIRED_RECONSTRUCTION_INTERFACE_VERSION_OR_DEFINITION
REQUIRED_RECONSTRUCTION_INTERFACE_STATUS
REQUIRED_RECONSTRUCTION_INTERFACE_PROVENANCE
~~~

Status family:

~~~text
REQUIRED_RECONSTRUCTION_INTERFACE_AVAILABLE
REQUIRED_RECONSTRUCTION_INTERFACE_UNAVAILABLE
REQUIRED_RECONSTRUCTION_INTERFACE_CONFLICTING
REQUIRED_RECONSTRUCTION_INTERFACE_UNDERDETERMINED
REQUIRED_RECONSTRUCTION_INTERFACE_OUT_OF_SCOPE
~~~

This family includes, when claim-relevant:

~~~text
Formation status / witness-history handoff
Property status / typed-input handoff
Aggregation map / support sidecar
Compression map / reduction sidecar
Transformation map
collision / fiber / kernel record
injectivity record
cross-coordinate / relational condition
Tracking handoff
Lineage handoff
transition relation
Measurement handoff
decoder / schema
other declared domain interface
~~~

Binding consequences:

~~~text
required interface unavailable:
  -> dependent claim BLOCKED

required interface conflicting:
  -> CONFLICTING if claim-relevant and unresolved

required interface underdetermined:
  -> UNDERDETERMINED if alternative admissible interface
     semantics change the requested result

required interface out of scope:
  -> OUT_OF_SCOPE for the dependent claim
~~~

If the required information is available and evaluably shows destructive loss or non-identifiability:

~~~text
result:
  NOT_ESTABLISHED
  or
  an explicitly supported frozen-interface
  unrecoverability claim
~~~

but not BLOCKED.

Required guards:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
EVALUABLE_DESTRUCTIVE_INFORMATION_LOSS

BLOCKED
  !=
NOT_ESTABLISHED

MISSING_REQUIRED_SIDECAR
  !=
NEGATIVE_EVIDENCE
~~~

## 5. R4 — frozen-interface closure for unrecoverability claims

A claim of:

~~~text
UNRECOVERABLE_INFORMATION_ON_FROZEN_INTERFACE
~~~

requires a positive closure statement about the interface package relevant to the requested distinction.

Freeze:

~~~text
RECONSTRUCTION_INTERFACE_CLOSURE_STATUS
FROZEN_INTERFACE_COMPONENT_REGISTER
FROZEN_INTERFACE_SCOPE
FROZEN_INTERFACE_COMPLETENESS_PROVENANCE
~~~

Status family:

~~~text
INTERFACE_COMPLETE_FOR_DECLARED_CLAIM
INTERFACE_EXPLICITLY_PARTIAL
INTERFACE_COMPLETENESS_UNDERDETERMINED
INTERFACE_CLOSURE_BLOCKED
INTERFACE_CLOSURE_OUT_OF_SCOPE
~~~

Binding requirement for:

~~~text
UNRECOVERABLE_DISTINCTION_ESTABLISHED_ON_FROZEN_INTERFACE
~~~

At minimum:

~~~text
two distinct in-scope admissible source/history candidates

+
same complete frozen claim-relevant evidence/readout package

+
RECONSTRUCTION_INTERFACE_CLOSURE_STATUS =
  INTERFACE_COMPLETE_FOR_DECLARED_CLAIM

+
no frozen interface component distinguishes the candidates

+
the requested distinction lies inside the frozen
reconstruction scope
~~~

When the interface is only explicitly partial:

~~~text
do not claim unrecoverability

possible result:
  multiple compatible
  blocked
  partial reconstruction
  or
  unresolved,
depending on the frozen task
~~~

Required guards:

~~~text
NO_REGISTERED_DISTINGUISHER
  !=
PROVED_UNRECOVERABILITY

UNRECOVERABLE_ON_FROZEN_INTERFACE
  !=
ABSOLUTELY_UNRECOVERABLE_BY_ANY_FUTURE_EVIDENCE

INTERFACE_CLOSURE_COMPLETE_FOR_CLAIM
  !=
GLOBAL_INFORMATION_COMPLETENESS
~~~

## 6. R5 — history-relation coherence and composition semantics

A historical Reconstruction task may contain both direct long-interval relation records and composed intermediate relation records.

Protocol v0.1 must freeze their interaction.

Freeze:

~~~text
HISTORY_RELATION_FAMILY_ID
HISTORY_RELATION_FAMILY_VERSION
HISTORY_RELATION_COHERENCE_STATUS
HISTORY_COMPOSITION_RULE_OR_NONE
HISTORY_PRECEDENCE_RULE_OR_NONE
DIRECT_VS_COMPOSED_RELATION_POLICY
~~~

Status family:

~~~text
HISTORY_RELATION_CONSISTENT
HISTORY_RELATION_CONFLICTING
HISTORY_RELATION_UNDERDETERMINED
HISTORY_RELATION_BLOCKED
HISTORY_RELATION_OUT_OF_SCOPE
~~~

Semantics:

~~~text
CONSISTENT:
  direct and composed claim-relevant history records
  agree under the frozen relation/composition semantics

CONFLICTING:
  applicable direct and composed records make mutually
  incompatible claims under the same frozen semantics
  and no resolver applies

UNDERDETERMINED:
  multiple admissible composition/precedence semantics
  yield different history outcomes and no resolver exists

BLOCKED:
  a required intermediate relation, composition rule,
  timestamp, regime record, or decoder is unavailable

OUT_OF_SCOPE:
  the requested historical relation lies outside the
  frozen history-relation family or scope
~~~

Binding consequences:

~~~text
claim-relevant unresolved history conflict:
  -> RECONSTRUCTION_TASK_CONFLICTING

multiple admissible composition rules with different results:
  -> RECONSTRUCTION_TASK_UNDERDETERMINED

required history relation unavailable:
  -> RECONSTRUCTION_TASK_BLOCKED
~~~

Required guards:

~~~text
DIRECT_LONG_INTERVAL_RECORD
  !=
COMPOSED_INTERMEDIATE_CHAIN_BY_DEFAULT

TEMPORAL_ADJACENCY
  !=
HISTORICAL_LINK

TRANSITION_COMPATIBILITY
  !=
UNIQUE_HISTORY

BRANCHING_OR_MERGING
  !=
PROTOCOL_FAILURE
~~~

## 7. R6 — definitional-recompletion scope

Protocol v0.1 must explicitly classify definitional recompletion.

Freeze:

~~~text
DEFINITIONAL_RECOMPLETION_ROLE
~~~

Allowed roles:

~~~text
DEFINITIONAL_RECOMPLETION_NOT_USED

DEFINITIONAL_RECOMPLETION_SUBORDINATE_DETERMINISTIC_STEP

DEFINITIONAL_RECOMPLETION_PRIMARY_REQUEST_ONLY
~~~

Binding rules:

~~~text
PRIMARY_REQUEST_ONLY
and
complete primitive core supplied
and
requested output follows uniquely by the frozen definition:
  -> RECONSTRUCTION_TASK_OUT_OF_SCOPE
     for the Reconstruction claim

SUBORDINATE_DETERMINISTIC_STEP:
  may be used inside a genuine Reconstruction task
  but must remain separately typed and
  must not be counted as independent Reconstruction evidence

NOT_USED:
  no definitional-recompletion semantics imported
~~~

Required guards:

~~~text
DEFINITIONAL_RECOMPLETION
  !=
EVIDENCE_BASED_RECONSTRUCTION

DETERMINISTIC_REEVALUATION_FROM_COMPLETE_PRIMITIVES
  !=
RECOVERY_OF_MISSING_HISTORICAL_SOURCE
~~~

## 8. R7 — inference-mode scope

Protocol v0.1 must freeze:

~~~text
INFERENCE_MODE
~~~

Allowed modes:

~~~text
DETERMINISTIC_COMPATIBILITY

PROBABILISTIC_IF_EXPLICITLY_SUPPLIED
~~~

Default:

~~~text
INFERENCE_MODE:
  DETERMINISTIC_COMPATIBILITY
~~~

### 8.1 Deterministic compatibility mode

Supports:

~~~text
candidate compatibility filtering
candidate exclusion
multiple-compatible source/history sets
declared-class uniqueness
collision/fiber reasoning
blocked/conflicting/underdetermined states
class-bounded reconstruction
frozen-interface unrecoverability
~~~

Does not manufacture:

~~~text
priors
likelihoods
posterior probabilities
Bayes factors
ranking scores
decision losses
expected utility
historical truth probabilities
~~~

### 8.2 Probabilistic-if-explicitly-supplied mode

A probabilistic Reconstruction request is in scope only when the required probabilistic interface is frozen.

Depending on the requested claim, this may include:

~~~text
PROBABILISTIC_MODEL_ID
PROBABILISTIC_MODEL_VERSION
PRIOR_OR_BASE_MEASURE
LIKELIHOOD_OR_HISTORY_OBSERVATION_MODEL
NORMALIZATION_DOMAIN
POSTERIOR_SEMANTICS
RANKING_RULE
DECISION_LOSS_OR_UTILITY_IF_DECISION_IS_REQUESTED
PROBABILISTIC_SCOPE
~~~

If a posterior/ranking claim is requested without the explicit required interface:

~~~text
ranking/posterior claim:
  RECONSTRUCTION_TASK_OUT_OF_SCOPE
~~~

A separately frozen deterministic compatibility-set subtask may remain established.

Required guards:

~~~text
PROBABILITY
  !=
HISTORICAL_TRUTH

CANDIDATE_RANKING
  !=
CANDIDATE_ELIMINATION

MOST_PROBABLE_HISTORY
  !=
ONLY_COMPATIBLE_HISTORY

NO_PROBABILISTIC_INTERFACE
  !=
PERMISSION_TO_INVENT_PRIOR
~~~

## 9. R8 — task-terminal precedence and exact PARTIAL semantics

Protocol v0.1 must emit exactly one task-level terminal:

~~~text
RECONSTRUCTION_TASK_ESTABLISHED

RECONSTRUCTION_TASK_PARTIAL

RECONSTRUCTION_TASK_NOT_ESTABLISHED

RECONSTRUCTION_TASK_BLOCKED

RECONSTRUCTION_TASK_CONFLICTING

RECONSTRUCTION_TASK_OUT_OF_SCOPE

RECONSTRUCTION_TASK_UNDERDETERMINED
~~~

Binding terminal precedence:

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

Semantics:

~~~text
OUT_OF_SCOPE:
  requested target, claim, inference mode, class representation,
  history relation, bridge role, or operation lies outside
  the frozen Reconstruction interface

CONFLICTING:
  mutually incompatible applicable claim-relevant evidence,
  bridge, history relation, interface, rule, or scope records
  exist under the same frozen semantics and no resolver applies

UNDERDETERMINED:
  multiple admissible claim-relevant class, evidence,
  bridge, history, resolution, or interface semantics
  produce different task outcomes and no resolver exists

BLOCKED:
  one or more required in-scope evidence, bridge,
  sidecar, relation, decoder, or prerequisite records
  are unavailable and prevent completion of a required obligation

ESTABLISHED:
  the requested frozen claim level is supported after all
  required obligations are validly evaluated

PARTIAL:
  multiple independently required in-scope Reconstruction
  obligations exist;
  at least one is ESTABLISHED;
  at least one other independently required obligation is
  evaluably NOT_ESTABLISHED;
  no required obligation is BLOCKED;
  and no OUT_OF_SCOPE / CONFLICTING / UNDERDETERMINED
  terminal dominates the task

NOT_ESTABLISHED:
  the requested in-scope claim is evaluable under all required
  interfaces but the requested claim level fails
~~~

PARTIAL may not be used:

~~~text
to rescue one failed atomic claim

to hide a blocked required interface

to hide evidence conflict

to hide history-relation conflict

to hide underdetermined semantics

to combine an out-of-scope claim with an in-scope claim
and call the whole task partly successful
~~~

The terminal summarizes the run only.

It does not erase subordinate:

~~~text
evidence-set coherence
required-interface status
pair disposition
candidate disposition
candidate-set outcome
injectivity/collision record
unrecoverability record
history-relation status
Tracking/Lineage handoff
additional-evidence handoff
~~~

## 10. Candidate-set outcome remains separate from task terminal

Protocol v0.1 must preserve at least:

~~~text
RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE

RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS

RECONSTRUCTION_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS

RECONSTRUCTION_SET_PARTIALLY_EVALUATED

RECONSTRUCTION_SET_CONFLICTING

RECONSTRUCTION_SET_UNDERDETERMINED
~~~

with guards:

~~~text
MULTIPLE_COMPATIBLE
  !=
TASK_UNDERDETERMINED

UNIQUE_WITHIN_DECLARED_CLASS
  !=
GLOBAL_HISTORICAL_TRUTH

NONE_COMPATIBLE_IN_DECLARED_CLASS
  !=
NO_REAL_PAST_STATE_OR_HISTORY
~~~

Example:

~~~text
primary claim:
  RECONSTRUCTION_COMPATIBILITY_SET

result:
  multiple compatible histories remain

overall primary status:
  RECONSTRUCTION_ESTABLISHED

task terminal:
  RECONSTRUCTION_TASK_ESTABLISHED

candidate-set outcome:
  RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE
~~~

## 11. Required protocol additions

Reconstruction Protocol v0.1 must incorporate the historical Task Interface plus this Amendment.

At minimum, the executable protocol must bind:

~~~text
A. class representation mode
B. candidate evaluation mode
C. class completeness status

D. evidence-set coherence status
E. evidence conflict resolver / precedence

F. required-interface status family

G. frozen-interface closure status
H. frozen-interface component register
I. completeness provenance

J. history-relation coherence status
K. composition rule
L. direct-vs-composed relation policy

M. definitional-recompletion role

N. inference mode
O. explicit probabilistic interface when used

P. exact terminal precedence
Q. exact PARTIAL semantics
~~~

## 12. Protocol-freeze authorization

All eight refinement groups are prospective and preserve:

~~~text
METHOD_IDENTITY_PRESERVED:
  yes

HISTORICAL_TASK_INTERFACE_REWRITTEN:
  no

HISTORICAL_BOUNDARY_ATTACK_RECORD_REWRITTEN:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Therefore:

~~~text
PROTOCOL_FREEZE_AUTHORIZED:
  yes
~~~

The next canonical step is to freeze executable Reconstruction Protocol v0.1 using:

~~~text
SOURCE_REGISTRY_v0.1

+

historical Task Interface v0.1 Draft

+

Boundary Counterexamples v0.1

+

Task Interface Boundary Amendment 001
~~~
