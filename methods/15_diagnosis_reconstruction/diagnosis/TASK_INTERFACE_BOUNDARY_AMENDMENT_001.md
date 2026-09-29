# DSD Diagnosis Task Interface Boundary Amendment 001

Status: **PROSPECTIVE AMENDMENT ESTABLISHED**  
Date: **2026-09-29**  
Method: **Diagnosis / DSD 진단론**

Frozen historical basis:

~~~text
SOURCE_REGISTRY_COMMIT:
  63ccc25d5bc8ddadadabfe698852d846e5671f15

SOURCE_REGISTRY_BLOB:
  1152759be5b56462156c83ecd3c508c73f1755f7

TASK_INTERFACE_COMMIT:
  e2c636eb0751878423a35d6848f7ef5a8fe81cc3

TASK_INTERFACE_BLOB:
  8cc12899c9b3f7a5f78d0e1893c5aa3a3824d444

BOUNDARY_ATTACK_COMMIT:
  f930b29b1422f4306fa38e8063edd9a8a3ed8118

BOUNDARY_ATTACK_BLOB:
  50de1b4ccb64264cf100a573f3831b8e2d1c7057
~~~

The historical Task Interface and boundary-attack record are not rewritten.

This Amendment prospectively binds the five nonbreaking refinements forced by the 18 pre-protocol boundary attacks.

## 1. Amendment result

~~~text
BOUNDARY_AMENDMENT_001:
  established

REFINEMENT_GROUPS_ADOPTED:
  5/5

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

DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  0

EXTERNAL_APPLICATION:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 2. R1 — evidence-set coherence and conflict semantics

Before candidate elimination is interpreted as a Diagnosis result, Protocol v0.1 must evaluate the coherence of the frozen claim-relevant evidence set.

Required record:

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
  the supplied claim-relevant evidence records can be jointly interpreted
  under the frozen schema, time, regime, resolution, and precedence rules

CONFLICTING:
  mutually incompatible applicable evidence records exist under the same
  frozen semantics and no frozen resolver or precedence rule resolves them

UNDERDETERMINED:
  multiple admissible evidence-set interpretations yield different
  claim-relevant candidate outcomes and no frozen resolver exists

BLOCKED:
  coherence cannot be evaluated because a required schema, timestamp,
  provenance, calibration, decoder, or other required evidence interface
  is unavailable

OUT_OF_SCOPE:
  the evidence packet lies outside the frozen Diagnosis task scope
~~~

A conflicting evidence packet may not be silently converted into:

~~~text
DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
~~~

merely because every candidate fails at least one mutually incompatible observation.

Required guards:

~~~text
EVIDENCE_CONFLICT
  !=
CANDIDATE_EXCLUSION_BY_DEFAULT

NONE_COMPATIBLE_IN_DECLARED_CLASS
  !=
EVIDENCE_SET_CONFLICTING

MUTUALLY_INCOMPATIBLE_OBSERVATIONS
  !=
NO_REAL_STATE_EXISTS
~~~

When evidence-set conflict is claim-relevant and unresolved:

~~~text
overall Diagnosis primary status:
  DIAGNOSIS_CONFLICTING

task terminal:
  DIAGNOSIS_TASK_CONFLICTING
~~~

unless a higher-priority frozen out-of-scope condition applies.

Evidence conflict remains visible even if some subordinate candidate evaluations are individually possible.

## 3. R2 — bridge-rule conflict and pair-conflict semantics

The Task Interface already permits deterministic maps, relation-valued compatibility rules, set-valued prediction, residual criteria, transition relations, and other supplied bridges.

Protocol v0.1 must distinguish:

~~~text
bridge unavailable
from
bridge semantics underdetermined
from
bridge rules mutually conflicting
~~~

Required bridge-level status:

~~~text
BRIDGE_RELATION_AVAILABLE

BRIDGE_RELATION_UNAVAILABLE

BRIDGE_RELATION_CONFLICTING

BRIDGE_RELATION_UNDERDETERMINED

BRIDGE_RELATION_OUT_OF_SCOPE
~~~

Required pair-level disposition family:

~~~text
PAIR_COMPATIBLE

PAIR_INCOMPATIBLE

PAIR_BLOCKED

PAIR_CONFLICTING

PAIR_OUT_OF_SCOPE

PAIR_UNDERDETERMINED
~~~

Semantics:

~~~text
PAIR_CONFLICTING:
  two or more applicable bridge records under the same frozen
  candidate/evidence identity, scope, version semantics, and precedence
  assert mutually incompatible pair outcomes and no frozen resolver applies

PAIR_UNDERDETERMINED:
  multiple admissible bridge interpretations remain, but the supplied records
  are not themselves mutually contradictory under one frozen interpretation

PAIR_BLOCKED:
  a required bridge relation or prerequisite is unavailable
~~~

Required guards:

~~~text
CONFLICTING != UNDERDETERMINED

UNAVAILABLE != CONFLICTING

PAIR_INCOMPATIBLE != PAIR_CONFLICTING
~~~

A claim-relevant unresolved pair conflict propagates to:

~~~text
DIAGNOSIS_CONFLICTING
~~~

and remains separately recorded in the pair ledger.

## 4. R3 — required Diagnosis interface availability and BLOCKED semantics

Protocol v0.1 must maintain an explicit availability status for every required claim-relevant interface that is not already represented by the evidence-set or bridge status families.

Required generic record:

~~~text
REQUIRED_DIAGNOSIS_INTERFACE_ID
REQUIRED_DIAGNOSIS_INTERFACE_ROLE
REQUIRED_DIAGNOSIS_INTERFACE_VERSION_OR_DEFINITION
REQUIRED_DIAGNOSIS_INTERFACE_STATUS
REQUIRED_DIAGNOSIS_INTERFACE_PROVENANCE
~~~

Status family:

~~~text
REQUIRED_DIAGNOSIS_INTERFACE_AVAILABLE

REQUIRED_DIAGNOSIS_INTERFACE_UNAVAILABLE

REQUIRED_DIAGNOSIS_INTERFACE_CONFLICTING

REQUIRED_DIAGNOSIS_INTERFACE_UNDERDETERMINED

REQUIRED_DIAGNOSIS_INTERFACE_OUT_OF_SCOPE
~~~

The generic interface family includes, when claim-relevant:

~~~text
Formation status handoff
Property status handoff
Measurement handoff
support-retention sidecar
Aggregation/Compression loss record
injectivity/collision record
residual target/carrier/rule
transition relation
dynamic-support handoff
candidate-class completeness handoff
causal bridge
decoder/schema
other declared domain interface
~~~

Binding consequences:

~~~text
required interface unavailable:
  -> candidate / claim evaluation BLOCKED

required interface conflicting:
  -> CONFLICTING if claim-relevant and unresolved

required interface underdetermined:
  -> UNDERDETERMINED if alternative admissible interface semantics
     change the requested claim

required interface out of scope:
  -> OUT_OF_SCOPE for the dependent claim
~~~

An unavailable required sidecar may not be converted into:

~~~text
candidate exclusion
negative evidence
defined zero
ordinary evaluable NOT_ESTABLISHED
~~~

Required guards:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
EVALUABLE_INCOMPATIBILITY

BLOCKED
  !=
NOT_ESTABLISHED

MISSING_STATUS_OR_SUPPORT_SIDECAR
  !=
NEGATIVE_EVIDENCE
~~~

## 5. R4 — inference-mode scope: deterministic compatibility versus explicit probability

Diagnosis Protocol v0.1 must freeze:

~~~text
INFERENCE_MODE
~~~

Allowed modes for v0.1:

~~~text
DETERMINISTIC_COMPATIBILITY

PROBABILISTIC_IF_EXPLICITLY_SUPPLIED
~~~

Default:

~~~text
INFERENCE_MODE:
  DETERMINISTIC_COMPATIBILITY
~~~

### 5.1 Deterministic compatibility mode

This mode supports:

~~~text
candidate compatibility filtering
candidate exclusion
candidate-set multiplicity
declared-class uniqueness
blocked/conflicting/underdetermined states
cause compatibility
bounded cause identification only if an explicit causal bridge is supplied
~~~

It does not manufacture:

~~~text
prior probabilities
likelihoods
posterior probabilities
Bayes factors
ranking scores
decision losses
expected utility
optimal candidate choice
~~~

### 5.2 Probabilistic-if-explicitly-supplied mode

A probabilistic Diagnosis request is in scope only when the task freezes at least the probabilistic objects required by that claim.

Depending on the requested result, this may include:

~~~text
PROBABILISTIC_MODEL_ID
PROBABILISTIC_MODEL_VERSION
PRIOR_OR_BASE_MEASURE
LIKELIHOOD_OR_OBSERVATION_MODEL
NORMALIZATION_DOMAIN
POSTERIOR_SEMANTICS
RANKING_RULE
DECISION_LOSS_OR_UTILITY_IF_DECISION_IS_REQUESTED
PROBABILISTIC_SCOPE
~~~

Protocol v0.1 does not define universal priors, likelihoods, or losses.

If a ranking/posterior claim is requested without its required explicit probabilistic interface:

~~~text
ranking/posterior claim:
  DIAGNOSIS_TASK_OUT_OF_SCOPE
~~~

The deterministic compatibility subtask may remain independently established if it was separately frozen.

Required guards:

~~~text
PROBABILITY != COMPATIBILITY

CANDIDATE_RANKING != CANDIDATE_ELIMINATION

NO_PROBABILISTIC_INTERFACE
  !=
PERMISSION_TO_INVENT_PRIOR

MOST_PROBABLE
  !=
ONLY_COMPATIBLE
~~~

A future dedicated probabilistic extension may broaden this interface prospectively.

## 6. R5 — task-terminal precedence and PARTIAL semantics

Diagnosis Protocol v0.1 must emit exactly one task-level terminal:

~~~text
DIAGNOSIS_TASK_ESTABLISHED

DIAGNOSIS_TASK_PARTIAL

DIAGNOSIS_TASK_NOT_ESTABLISHED

DIAGNOSIS_TASK_BLOCKED

DIAGNOSIS_TASK_CONFLICTING

DIAGNOSIS_TASK_OUT_OF_SCOPE

DIAGNOSIS_TASK_UNDERDETERMINED
~~~

Binding terminal precedence:

~~~text
DIAGNOSIS_TASK_OUT_OF_SCOPE
>
DIAGNOSIS_TASK_CONFLICTING
>
DIAGNOSIS_TASK_UNDERDETERMINED
>
DIAGNOSIS_TASK_BLOCKED
>
DIAGNOSIS_TASK_ESTABLISHED /
DIAGNOSIS_TASK_PARTIAL /
DIAGNOSIS_TASK_NOT_ESTABLISHED
~~~

Semantics:

~~~text
OUT_OF_SCOPE:
  the requested operation, inference mode, candidate class, bridge role,
  or claim lies outside the frozen Diagnosis task

CONFLICTING:
  mutually incompatible applicable claim-relevant evidence, bridge,
  interface, rule, or scope records exist under the same frozen semantics
  and no frozen resolver applies

UNDERDETERMINED:
  multiple admissible claim-relevant interpretations of candidate class,
  evidence semantics, bridge semantics, resolution, scope, or other frozen
  interface produce different task outcomes and no resolver exists

BLOCKED:
  one or more required in-scope evidence/bridge/interface/prerequisite
  records are unavailable, preventing completion of a required obligation

ESTABLISHED:
  the requested frozen claim level is supported after all required
  candidate/evidence obligations are validly evaluated

PARTIAL:
  the frozen task contains multiple independently required in-scope
  Diagnosis obligations;
  at least one obligation is established;
  at least one other evaluable obligation is not established;
  and no OUT_OF_SCOPE / CONFLICTING / UNDERDETERMINED / BLOCKED state
  dominates the run

NOT_ESTABLISHED:
  the requested in-scope claim is evaluable under all required interfaces
  but the requested claim level fails
~~~

PARTIAL may not be used:

~~~text
to rescue one failed atomic claim

to hide a blocked required interface

to hide a conflict

to hide underdetermined semantics

to combine an out-of-scope claim with an in-scope claim
and call the run partly successful
~~~

The terminal summarizes the run only.

It does not erase:

~~~text
evidence-set status
bridge status
pair dispositions
candidate dispositions
candidate-set outcome
identifiability scope
cause-claim record
additional-observation handoff
subordinate obligation results
~~~

## 7. Candidate-set outcome remains separate from task terminal

Boundary attack D1-D3 confirms that candidate-set multiplicity is a Diagnosis result, not a failure-state family.

Protocol v0.1 must preserve:

~~~text
DIAGNOSIS_SET_MULTIPLE_COMPATIBLE

DIAGNOSIS_SET_UNIQUE_WITHIN_DECLARED_CLASS

DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS

DIAGNOSIS_SET_PARTIALLY_EVALUATED

DIAGNOSIS_SET_UNDERDETERMINED
~~~

with guards:

~~~text
MULTIPLE_COMPATIBLE
  !=
TASK_UNDERDETERMINED

UNIQUE_WITHIN_DECLARED_CLASS
  !=
GLOBAL_UNIQUE_DIAGNOSIS

NONE_COMPATIBLE_IN_DECLARED_CLASS
  !=
NO_REAL_STATE_EXISTS
~~~

Example:

~~~text
primary claim:
  CANDIDATE_COMPATIBILITY_SET

result:
  two compatible candidates remain

overall primary status:
  DIAGNOSIS_ESTABLISHED

task terminal:
  DIAGNOSIS_TASK_ESTABLISHED

candidate-set outcome:
  DIAGNOSIS_SET_MULTIPLE_COMPATIBLE
~~~

## 8. Candidate-class completeness discipline

Protocol v0.1 must freeze:

~~~text
CANDIDATE_CLASS_ID
CANDIDATE_CLASS_VERSION_OR_DEFINITION
CANDIDATE_CLASS_COMPLETENESS_STATUS
CANDIDATE_CLASS_COMPLETENESS_PROVENANCE
~~~

Status family:

~~~text
CANDIDATE_CLASS_DECLARED_BOUNDED

CANDIDATE_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE

CANDIDATE_CLASS_COMPLETENESS_UNDERDETERMINED

CANDIDATE_CLASS_COMPLETENESS_NOT_CLAIMED
~~~

A unique surviving candidate may support:

~~~text
UNIQUE_WITHIN_DECLARED_CANDIDATE_CLASS
~~~

without supporting:

~~~text
GLOBAL_UNIQUE_DIAGNOSIS
~~~

A completeness claim is supplied evidence/handoff and must not be manufactured by Diagnosis.

## 9. Cause-claim discipline remains binding

The boundary attack does not change the Task Interface cause distinction.

Protocol v0.1 must preserve:

~~~text
CAUSE_NOT_CLAIMED

CAUSE_COMPATIBILITY_ONLY

CAUSE_BRIDGE_BLOCKED

CAUSE_BRIDGE_UNDERDETERMINED

CAUSE_IDENTIFICATION_ESTABLISHED_ON_DECLARED_MODEL

CAUSE_IDENTIFICATION_NOT_ESTABLISHED
~~~

and guards:

~~~text
DIAGNOSTIC_COMPATIBILITY != CAUSAL_PROOF

CORRELATION != CAUSAL_BRIDGE

RESIDUAL_MATCH != CAUSAL_BRIDGE

TEMPORAL_PRECEDENCE != CAUSAL_BRIDGE

CAUSE_IDENTIFICATION_ON_DECLARED_MODEL
  !=
UNRESTRICTED_REAL_WORLD_CAUSAL_CERTAINTY
~~~

## 10. Readout / residual / transition discipline remains binding

The Amendment retains the historical Task Interface rules:

~~~text
EQUAL_AGGREGATE != EQUAL_CURRENT_STATE

PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY

REDUCED_READOUT != COMPLETE_DIAGNOSTIC_CLASSIFIER

LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY

NONINJECTIVE_FORWARD_MAP
  !=
LICENSE_TO_SELECT_ONE_PREIMAGE

RESIDUAL_ZERO != SOURCE_STATE_IDENTITY

RESIDUAL_MATCH != CAUSE_ESTABLISHED

TRANSITION_COMPATIBILITY != UNIQUE_SUCCESSOR

CURRENT_STATE_DIAGNOSIS
  !=
PAST_HISTORY_RECONSTRUCTION
~~~

A relation-valued transition may legitimately leave several current candidates compatible.

## 11. Neighboring-method non-substitution remains binding

Diagnosis may consume typed handoffs from neighboring methods, but no handoff silently substitutes for Diagnosis.

Protocol v0.1 must preserve at least:

~~~text
MEASUREMENT_SUFFICIENCY != DIAGNOSIS

CLASSIFICATION_RESULT != DIAGNOSIS_RESULT

COMPARISON_SIMILARITY != DIAGNOSIS_RESULT

RECONSTRUCTION_CANDIDATE != CURRENT_DIAGNOSIS

PREDICTION_OUTPUT != CURRENT_DIAGNOSIS

SIMULATION_TRAJECTORY != OBSERVED_STATE

AUDIT_PASS != DIAGNOSIS_RESULT

NEED_FOR_ADDITIONAL_OBSERVATION
  !=
OPTIMAL_MEASUREMENT_SELECTED

DIAGNOSIS_DISCRIMINATOR_REQUIREMENT
  !=
MEASUREMENT_PLAN_EXECUTION
~~~

If Optimization is invoked to select an observation, that is a separate handed-off task.

## 12. Maximum-supported-claim discipline

A conformant Diagnosis result may assert only what the frozen candidate class, evidence set, bridge scope, inference mode, and claim level support.

Protocol v0.1 may not silently upgrade:

~~~text
candidate compatibility
  -> truth

declared-class uniqueness
  -> global uniqueness

cause compatibility
  -> causal certainty

model-scoped cause identification
  -> unrestricted causal proof

current-state diagnosis
  -> unique past history

measurement sufficiency
  -> diagnosis

readout equality
  -> hidden-state identity

deterministic compatibility
  -> posterior probability

additional observation requirement
  -> optimal action
~~~

## 13. Prospective Protocol v0.1 obligations

Diagnosis Protocol v0.1 must contain, at minimum:

~~~text
task identity / version / claim-level lock

candidate-class ID/version/completeness lock

evidence register
evidence status/provenance/time/regime
EVIDENCE_SET_COHERENCE_STATUS

bridge register
BRIDGE_RELATION_STATUS
pair disposition including PAIR_CONFLICTING

REQUIRED_DIAGNOSIS_INTERFACE_STATUS

inference-mode lock
probabilistic-interface gate when requested

resolution/equivalence/threshold semantics

Formation / Property / Measurement /
support-retention / reduction-loss handoffs

residual target/carrier/rule gate when used

transition / dynamic-support gate when used

candidate disposition ledger

compatible / excluded / blocked /
conflicting / unresolved candidate ledgers

candidate-set outcome
identifiability scope

cause-claim gate

additional-observation handoff

task-terminal precedence and PARTIAL semantics

neighboring-method non-substitution ledger

protocol-conformance record
method-gain record
maximum-supported-claim record
~~~

The Protocol must distinguish source-derived constraints from prospective methodology rules.

## 14. Amendment interpretation lock

~~~text
BOUNDARY_AMENDMENT
  !=
PROTOCOL_VALIDATION

PROTOCOL_FREEZE_AUTHORIZED
  !=
PROTOCOL_INTERNALLY_STANDARDIZED

NO_BOUNDARY_COLLAPSE
  !=
PERMANENT_METHOD_IRREDUCIBILITY

METHOD_IDENTITY_PRESERVED
  !=
METHOD_SUPERIORITY

DETERMINISTIC_DEFAULT
  !=
PROBABILITY_REJECTED_IN_PRINCIPLE
~~~

The probabilistic interface is scoped, not prohibited in principle.

## 15. Post-amendment state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 historical draft preserved

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

PRESERVED_NO_REFINEMENT:
  13

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  5

BOUNDARY_AMENDMENT_001:
  established

REFINEMENT_GROUPS_ADOPTED:
  5/5

METHOD_IDENTITY_CHANGED:
  no

TASK_INTERFACE_CORE_REOPENED:
  no

DEDICATED_DIAGNOSIS_PROTOCOL:
  not established

PROTOCOL_FREEZE_AUTHORIZED:
  yes

DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  0

BASELINE_DIAGNOSIS_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_DIAGNOSIS_APPLICATIONS:
  0

INDEPENDENT_DIAGNOSIS_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

DIAGNOSIS_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_DIAGNOSIS_EVIDENCE_STATUS:
  boundary_amendment_complete

PROTOCOL_REVISION_REQUIRED:
  not applicable pre-protocol

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 16. Next

Freeze executable Diagnosis Protocol v0.1 from:

~~~text
historical Task Interface v0.1
+
Boundary Amendment 001
+
recovered source registry
~~~

Do not rewrite the historical Task Interface or boundary-attack record during Protocol construction.
