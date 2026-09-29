# DSD Diagnosis Protocol v0.1

Status: **FROZEN EXECUTABLE INTERNAL PROTOCOL**  
Date: **2026-09-29**  
Method: **Diagnosis / DSD 진단론**  
Legacy path ID: `15A`

## 1. Frozen lineage of this protocol

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

AMENDMENT_COMMIT:
  eb51b70765a69277aeabe4152260431c970b95e5

AMENDMENT_BLOB:
  c5b9fde42828d67f77a7e92d3a588cb6a7aeca2d
~~~

This protocol operationalizes the recovered Diagnosis source registry, the historical Task Interface v0.1, and Boundary Amendment 001.

It does not rewrite the source papers, historical Task Interface, boundary attack, or Amendment.

Source-derived constraints and prospective methodology rules remain distinguishable.

## 2. Atomic method task

Given:

~~~text
a declared current-state / failure-mode / cause-hypothesis candidate class

present observation/evidence records

typed status / applicability / provenance

explicit evidence-to-candidate compatibility or forward-model bridges

claim-relevant resolution / temporal / regime semantics

and any required support / readout / residual / transition /
measurement / causal handoffs
~~~

Diagnosis determines:

~~~text
which declared candidates remain compatible

which candidates are excluded

which candidates cannot yet be evaluated

which candidate dispositions remain unresolved

what candidate-set identifiability is supported

what additional observation role remains required

and, when requested, what bounded cause claim is supported
~~~

without:

~~~text
inventing observations

treating unavailable evidence as negative evidence

choosing one preimage from a noninjective relation without evidence

promoting candidate compatibility to unrestricted truth

promoting cause compatibility to causal proof

promoting declared-class uniqueness to global uniqueness

silently reconstructing a unique past history

silently performing Measurement / Optimization / Reconstruction /
Prediction / Simulation / Audit in place of Diagnosis
~~~

## 3. Primary claim levels

Exactly one primary claim level is frozen per Diagnosis task.

~~~text
CANDIDATE_COMPATIBILITY_SET

UNIQUE_WITHIN_DECLARED_CANDIDATE_CLASS

CURRENT_STATE_OR_CONDITION_IDENTIFICATION

FAILURE_MODE_IDENTIFICATION

CAUSE_COMPATIBILITY_ONLY

CAUSE_IDENTIFICATION_WITH_SUPPLIED_CAUSAL_BRIDGE
~~~

Subordinate obligations may be present, but they do not replace the primary claim level.

## 4. Validity gates G1-G18

### G1 — task identity / version / claim lock

Freeze:

~~~text
DIAGNOSIS_TASK_ID
TASK_VERSION
PRIMARY_CLAIM_LEVEL
DIAGNOSIS_QUESTION
MAXIMUM_SUPPORTED_CLAIM
~~~

Changing a claim-relevant lock after result inspection requires a new task version.

### G2 — candidate-class identity and completeness lock

Freeze:

~~~text
CANDIDATE_CLASS_ID
CANDIDATE_CLASS_VERSION_OR_DEFINITION
CANDIDATE_IDENTITIES
CANDIDATE_CLASS_COMPLETENESS_STATUS
CANDIDATE_CLASS_COMPLETENESS_PROVENANCE
~~~

Allowed completeness statuses:

~~~text
CANDIDATE_CLASS_DECLARED_BOUNDED
CANDIDATE_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE
CANDIDATE_CLASS_COMPLETENESS_UNDERDETERMINED
CANDIDATE_CLASS_COMPLETENESS_NOT_CLAIMED
~~~

Required guard:

~~~text
ONE_SURVIVING_DECLARED_CANDIDATE
  !=
ONE_POSSIBLE_REAL_STATE
~~~

### G3 — evidence register / provenance / status lock

Freeze every claim-relevant evidence item:

~~~text
EVIDENCE_ID
EVIDENCE_VERSION_IF_RELEVANT
EVIDENCE_TYPE_OR_CARRIER
OBSERVED_OR_SUPPLIED_RECORD
STATUS
APPLICABILITY_SCOPE
PROVENANCE
TIME_OR_WINDOW
LOCATION_IF_RELEVANT
REGIME_OR_SCHEMA_VERSION
DIRECT_OR_PROXY_ROLE
~~~

When Property semantics are used, preserve:

~~~text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_VALUE
~~~

Required guards:

~~~text
UNDEFINED != ZERO
DEFINED_ZERO != ABSENCE
MISSING_REQUIRED_EVIDENCE != NEGATIVE_EVIDENCE
INAPPLICABLE_EVIDENCE != NEGATIVE_EVIDENCE
PROXY_RECORD != DIRECT_OBSERVATION
~~~

### G4 — evidence-set coherence gate

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

A conflicting evidence packet may not be converted into a coherent zero-candidate result.

### G5 — bridge identity / scope / version lock

Freeze:

~~~text
EVIDENCE_TO_CANDIDATE_BRIDGE_ID
BRIDGE_VERSION_OR_DEFINITION
BRIDGE_APPLICABILITY_SCOPE
BRIDGE_PRECEDENCE_OR_RESOLVER_IF_ANY
~~~

Allowed bridge forms include:

~~~text
deterministic forward map
relation-valued compatibility rule
set-valued prediction
typed status relation
residual criterion
transition compatibility relation
domain-specific externally supplied rule
~~~

No missing bridge is inferred.

### G6 — bridge relation and pair-disposition gate

Bridge-level statuses:

~~~text
BRIDGE_RELATION_AVAILABLE
BRIDGE_RELATION_UNAVAILABLE
BRIDGE_RELATION_CONFLICTING
BRIDGE_RELATION_UNDERDETERMINED
BRIDGE_RELATION_OUT_OF_SCOPE
~~~

Pair dispositions:

~~~text
PAIR_COMPATIBLE
PAIR_INCOMPATIBLE
PAIR_BLOCKED
PAIR_CONFLICTING
PAIR_OUT_OF_SCOPE
PAIR_UNDERDETERMINED
~~~

Required guards:

~~~text
PAIR_INCOMPATIBLE != PAIR_CONFLICTING
CONFLICTING != UNDERDETERMINED
UNAVAILABLE != CONFLICTING
~~~

### G7 — required Diagnosis interface availability gate

For every claim-relevant interface not already covered by G3-G6, freeze:

~~~text
REQUIRED_DIAGNOSIS_INTERFACE_ID
REQUIRED_DIAGNOSIS_INTERFACE_ROLE
REQUIRED_DIAGNOSIS_INTERFACE_VERSION_OR_DEFINITION
REQUIRED_DIAGNOSIS_INTERFACE_STATUS
REQUIRED_DIAGNOSIS_INTERFACE_PROVENANCE
~~~

Statuses:

~~~text
REQUIRED_DIAGNOSIS_INTERFACE_AVAILABLE
REQUIRED_DIAGNOSIS_INTERFACE_UNAVAILABLE
REQUIRED_DIAGNOSIS_INTERFACE_CONFLICTING
REQUIRED_DIAGNOSIS_INTERFACE_UNDERDETERMINED
REQUIRED_DIAGNOSIS_INTERFACE_OUT_OF_SCOPE
~~~

Unavailable required interface -> BLOCKED.

### G8 — inference-mode lock

Freeze:

~~~text
INFERENCE_MODE:
  DETERMINISTIC_COMPATIBILITY
  PROBABILISTIC_IF_EXPLICITLY_SUPPLIED
~~~

Default:

~~~text
DETERMINISTIC_COMPATIBILITY
~~~

A probabilistic request requires an explicit frozen probabilistic interface sufficient for that requested claim.

The protocol does not invent priors, likelihoods, posteriors, ranking rules, losses, or utilities.

### G9 — resolution / equivalence / threshold lock

Freeze when claim-relevant:

~~~text
DIAGNOSIS_RESOLUTION_OR_EQUIVALENCE_RULE
RESOLUTION_VERSION
DISTINGUISHABILITY_RULE
THRESHOLD_OR_TOLERANCE
TEMPORAL_SCOPE
ACTIVE_REGIME_OR_SCHEMA
~~~

Required semantics unavailable -> BLOCKED.

Multiple admissible semantics producing different outcomes -> UNDERDETERMINED.

Mutually incompatible applicable semantics -> CONFLICTING.

### G10 — source-status / support / readout-loss gate

When used, freeze and retain:

~~~text
FORMATION_STATUS_HANDOFF
PROPERTY_STATUS_HANDOFF
MEASUREMENT_HANDOFF
SUPPORT_RETENTION_HANDOFF
AGGREGATION_OR_COMPRESSION_LOSS_HANDOFF
INJECTIVITY_OR_COLLISION_RECORD
READOUT_OR_REDUCTION_ID
READOUT_VERSION
RECONSTRUCTION_SCOPE
REQUIRED_SIDECARS
~~~

Required guards:

~~~text
EQUAL_AGGREGATE != EQUAL_CURRENT_STATE
PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY
REDUCED_READOUT != COMPLETE_DIAGNOSTIC_CLASSIFIER
LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
NONINJECTIVE_FORWARD_MAP != LICENSE_TO_SELECT_ONE_PREIMAGE
~~~

### G11 — residual gate

If residual evidence is used, freeze:

~~~text
RESIDUAL_TARGET_ID
RESIDUAL_TARGET_VERSION_OR_DEFINITION
RESIDUAL_CARRIER
RESIDUAL_RULE
RESIDUAL_THRESHOLD_OR_EQUIVALENCE_RULE
~~~

Required guards:

~~~text
RESIDUAL_ZERO != SOURCE_STATE_IDENTITY
RESIDUAL_MATCH != CAUSE_ESTABLISHED
~~~

Scalar subtraction is not assumed universal across arbitrary typed carriers.

### G12 — temporal / transition gate

If dynamic constraints are used, freeze:

~~~text
TEMPORAL_SCOPE
ACTIVE_REGIME
TRANSITION_RELATION_ID
TRANSITION_RELATION_VERSION
DYNAMIC_SUPPORT_STATUS
LINEAGE_OR_SUCCESSION_HANDOFF_IF_USED
~~~

Required guards:

~~~text
TRANSITION_COMPATIBILITY != UNIQUE_SUCCESSOR
TEMPORAL_ORDER != CAUSAL_PROOF
DYNAMIC_SUPPORT_AVAILABILITY != CAUSAL_SUFFICIENCY
CURRENT_STATE_DIAGNOSIS != PAST_HISTORY_RECONSTRUCTION
~~~

Relation-valued transitions may legitimately leave multiple current candidates compatible.

### G13 — candidate disposition gate

For every declared candidate, emit exactly one candidate-level disposition:

~~~text
DIAGNOSIS_CANDIDATE_COMPATIBLE
DIAGNOSIS_CANDIDATE_EXCLUDED
DIAGNOSIS_CANDIDATE_BLOCKED
DIAGNOSIS_CANDIDATE_CONFLICTING
DIAGNOSIS_CANDIDATE_OUT_OF_SCOPE
DIAGNOSIS_CANDIDATE_UNDERDETERMINED
~~~

Candidate exclusion requires an evaluable frozen incompatibility condition.

Unavailable required evidence/interface does not count as exclusion.

### G14 — candidate-set / identifiability gate

Emit one candidate-set outcome:

~~~text
DIAGNOSIS_SET_MULTIPLE_COMPATIBLE
DIAGNOSIS_SET_UNIQUE_WITHIN_DECLARED_CLASS
DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
DIAGNOSIS_SET_PARTIALLY_EVALUATED
DIAGNOSIS_SET_UNDERDETERMINED
~~~

Required guards:

~~~text
MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED
UNIQUE_WITHIN_DECLARED_CLASS != GLOBAL_UNIQUE_DIAGNOSIS
NONE_COMPATIBLE_IN_DECLARED_CLASS != NO_REAL_STATE_EXISTS
~~~

A fully frozen task may legitimately establish a multiple-compatible set.

### G15 — cause-claim gate

Cause statuses:

~~~text
CAUSE_NOT_CLAIMED
CAUSE_COMPATIBILITY_ONLY
CAUSE_BRIDGE_BLOCKED
CAUSE_BRIDGE_CONFLICTING
CAUSE_BRIDGE_UNDERDETERMINED
CAUSE_IDENTIFICATION_ESTABLISHED_ON_DECLARED_MODEL
CAUSE_IDENTIFICATION_NOT_ESTABLISHED
CAUSE_OUT_OF_SCOPE
~~~

Required guards:

~~~text
DIAGNOSTIC_COMPATIBILITY != CAUSAL_PROOF
CORRELATION != CAUSAL_BRIDGE
RESIDUAL_MATCH != CAUSAL_BRIDGE
TEMPORAL_PRECEDENCE != CAUSAL_BRIDGE
CAUSE_IDENTIFICATION_ON_DECLARED_MODEL
  !=
UNRESTRICTED_REAL_WORLD_CAUSAL_CERTAINTY
~~~

### G16 — additional-observation and neighboring-method handoff gate

Diagnosis may emit:

~~~text
UNRESOLVED_CANDIDATE_PAIR_OR_CLASS
REQUIRED_DISTINCTION
MISSING_EVIDENCE_ROLE
POSSIBLE_MEASUREMENT_HANDOFF
~~~

It may consume typed neighboring-method sidecars, but may not silently substitute them for Diagnosis.

Required guards:

~~~text
MEASUREMENT_SUFFICIENCY != DIAGNOSIS
CLASSIFICATION_RESULT != DIAGNOSIS_RESULT
COMPARISON_SIMILARITY != DIAGNOSIS_RESULT
RECONSTRUCTION_CANDIDATE != CURRENT_DIAGNOSIS
PREDICTION_OUTPUT != CURRENT_DIAGNOSIS
SIMULATION_TRAJECTORY != OBSERVED_STATE
AUDIT_PASS != DIAGNOSIS_RESULT
NEED_FOR_ADDITIONAL_OBSERVATION != OPTIMAL_MEASUREMENT_SELECTED
DIAGNOSIS_DISCRIMINATOR_REQUIREMENT != MEASUREMENT_PLAN_EXECUTION
~~~

### G17 — primary Diagnosis status and task-terminal gate

Primary Diagnosis statuses:

~~~text
DIAGNOSIS_ESTABLISHED
DIAGNOSIS_NOT_ESTABLISHED
DIAGNOSIS_BLOCKED
DIAGNOSIS_CONFLICTING
DIAGNOSIS_OUT_OF_SCOPE
DIAGNOSIS_UNDERDETERMINED
~~~

Task terminals:

~~~text
DIAGNOSIS_TASK_ESTABLISHED
DIAGNOSIS_TASK_PARTIAL
DIAGNOSIS_TASK_NOT_ESTABLISHED
DIAGNOSIS_TASK_BLOCKED
DIAGNOSIS_TASK_CONFLICTING
DIAGNOSIS_TASK_OUT_OF_SCOPE
DIAGNOSIS_TASK_UNDERDETERMINED
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

`PARTIAL` requires multiple independently required in-scope obligations, at least one established and at least one evaluably not established, with no higher-priority terminal.

### G18 — conformance / gain / maximum-claim gate

Emit:

~~~text
DIAGNOSIS_PROTOCOL_CONFORMANCE
DIAGNOSIS_METHOD_GAIN_STATUS
MAXIMUM_SUPPORTED_CLAIM
~~~

No result may exceed the frozen:

~~~text
candidate class
candidate completeness status
evidence scope
bridge scope
inference mode
resolution / time / regime
readout / support / loss records
residual / transition scope
cause bridge
and neighboring-method handoffs
~~~

## 5. Binding operation T1-T18

### T1 — freeze task and primary claim

Instantiate G1.

No post-result task mutation is valid under the same task version.

### T2 — freeze candidate class and completeness

Instantiate G2.

Do not manufacture candidate-class completeness.

### T3 — build evidence registry

Instantiate G3.

Preserve native statuses and provenance.

### T4 — evaluate evidence-set coherence

Instantiate G4 before interpreting broad candidate elimination.

Retain evidence conflict separately from candidate failure.

### T5 — freeze bridge registry

Instantiate G5.

No post-hoc bridge substitution.

### T6 — evaluate bridge and pair statuses

Instantiate G6 for every claim-relevant candidate/evidence pair.

### T7 — evaluate required-interface availability

Instantiate G7.

Keep unavailable required interface separate from evaluable incompatibility.

### T8 — freeze inference mode

Instantiate G8.

Reject unsupported posterior/ranking claims rather than inventing probabilistic objects.

### T9 — freeze resolution / temporal / regime semantics

Instantiate G9.

No post-result threshold or regime substitution.

### T10 — build source-status / support / readout-loss ledger

Instantiate G10.

Do not infer hidden-state identity from reduced equality.

### T11 — evaluate residual constraints

Instantiate G11 when residual evidence is used.

### T12 — evaluate transition / dynamic constraints

Instantiate G12 when dynamic constraints are used.

Do not silently reconstruct a unique past history.

### T13 — assign candidate dispositions

Instantiate G13.

Each declared candidate receives exactly one disposition under the frozen rules.

### T14 — construct candidate sets and identifiability record

Instantiate G14.

Preserve multiplicity.

### T15 — evaluate cause claim

Instantiate G15 only at the frozen requested cause level.

### T16 — emit additional-observation / neighbor handoffs

Instantiate G16.

Do not select an optimal measurement unless a separate handed-off task is supplied.

### T17 — assign primary Diagnosis status and task terminal

Instantiate G17.

Apply terminal precedence without erasing subordinate statuses.

### T18 — emit conformance / method gain / maximum claim

Instantiate G18 and required output schema.

## 6. Evidence-set statuses

~~~text
EVIDENCE_SET_CONSISTENT
EVIDENCE_SET_CONFLICTING
EVIDENCE_SET_UNDERDETERMINED
EVIDENCE_SET_BLOCKED
EVIDENCE_SET_OUT_OF_SCOPE
~~~

A zero-candidate result is valid only when the relevant evidence set is sufficiently coherent and all required candidate evaluations are validly evaluable.

## 7. Bridge statuses

~~~text
BRIDGE_RELATION_AVAILABLE
BRIDGE_RELATION_UNAVAILABLE
BRIDGE_RELATION_CONFLICTING
BRIDGE_RELATION_UNDERDETERMINED
BRIDGE_RELATION_OUT_OF_SCOPE
~~~

## 8. Pair dispositions

~~~text
PAIR_COMPATIBLE
PAIR_INCOMPATIBLE
PAIR_BLOCKED
PAIR_CONFLICTING
PAIR_OUT_OF_SCOPE
PAIR_UNDERDETERMINED
~~~

Pair-level conflict remains distinct from candidate incompatibility.

## 9. Required-interface statuses

~~~text
REQUIRED_DIAGNOSIS_INTERFACE_AVAILABLE
REQUIRED_DIAGNOSIS_INTERFACE_UNAVAILABLE
REQUIRED_DIAGNOSIS_INTERFACE_CONFLICTING
REQUIRED_DIAGNOSIS_INTERFACE_UNDERDETERMINED
REQUIRED_DIAGNOSIS_INTERFACE_OUT_OF_SCOPE
~~~

## 10. Candidate dispositions

~~~text
DIAGNOSIS_CANDIDATE_COMPATIBLE
DIAGNOSIS_CANDIDATE_EXCLUDED
DIAGNOSIS_CANDIDATE_BLOCKED
DIAGNOSIS_CANDIDATE_CONFLICTING
DIAGNOSIS_CANDIDATE_OUT_OF_SCOPE
DIAGNOSIS_CANDIDATE_UNDERDETERMINED
~~~

Semantics:

~~~text
COMPATIBLE:
  every required evaluable candidate/evidence obligation is compatible
  under the frozen combination rule

EXCLUDED:
  the frozen exclusion rule is triggered by an evaluable valid
  claim-relevant incompatibility

BLOCKED:
  a required evidence/bridge/interface prerequisite is unavailable

CONFLICTING:
  applicable frozen records impose mutually incompatible dispositions

OUT_OF_SCOPE:
  the candidate or required relation lies outside the frozen task scope

UNDERDETERMINED:
  multiple admissible claim-relevant semantics yield different dispositions
  and no frozen resolver exists
~~~

## 11. Candidate-set / identifiability statuses

~~~text
DIAGNOSIS_SET_MULTIPLE_COMPATIBLE
DIAGNOSIS_SET_UNIQUE_WITHIN_DECLARED_CLASS
DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
DIAGNOSIS_SET_PARTIALLY_EVALUATED
DIAGNOSIS_SET_UNDERDETERMINED
~~~

These statuses do not replace task terminals.

## 12. Cause statuses

~~~text
CAUSE_NOT_CLAIMED
CAUSE_COMPATIBILITY_ONLY
CAUSE_BRIDGE_BLOCKED
CAUSE_BRIDGE_CONFLICTING
CAUSE_BRIDGE_UNDERDETERMINED
CAUSE_IDENTIFICATION_ESTABLISHED_ON_DECLARED_MODEL
CAUSE_IDENTIFICATION_NOT_ESTABLISHED
CAUSE_OUT_OF_SCOPE
~~~

## 13. Inference-mode statuses

~~~text
INFERENCE_MODE_DETERMINISTIC_COMPATIBILITY
INFERENCE_MODE_PROBABILISTIC_EXPLICIT
INFERENCE_MODE_BLOCKED
INFERENCE_MODE_CONFLICTING
INFERENCE_MODE_UNDERDETERMINED
INFERENCE_MODE_OUT_OF_SCOPE
~~~

For probabilistic mode, every required probabilistic object must be explicit and provenance-bearing.

## 14. Primary Diagnosis statuses

~~~text
DIAGNOSIS_ESTABLISHED
DIAGNOSIS_NOT_ESTABLISHED
DIAGNOSIS_BLOCKED
DIAGNOSIS_CONFLICTING
DIAGNOSIS_OUT_OF_SCOPE
DIAGNOSIS_UNDERDETERMINED
~~~

These are methodology-level task-evidence statuses and do not overwrite source-level statuses.

## 15. Task terminals

~~~text
DIAGNOSIS_TASK_ESTABLISHED
DIAGNOSIS_TASK_PARTIAL
DIAGNOSIS_TASK_NOT_ESTABLISHED
DIAGNOSIS_TASK_BLOCKED
DIAGNOSIS_TASK_CONFLICTING
DIAGNOSIS_TASK_OUT_OF_SCOPE
DIAGNOSIS_TASK_UNDERDETERMINED
~~~

Frozen precedence:

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

A negative, blocked, conflicting, underdetermined, or out-of-scope task may still be protocol-conformant.

## 16. Protocol conformance

~~~text
DIAGNOSIS_PROTOCOL_CONFORMANT
DIAGNOSIS_PROTOCOL_NONCONFORMANT
DIAGNOSIS_PROTOCOL_INDETERMINATE
~~~

Protocol conformance asks whether the frozen Diagnosis procedure was followed.

It is separate from whether the substantive Diagnosis result is positive.

## 17. Method-gain statuses

~~~text
DIAGNOSIS_METHOD_GAIN_ESTABLISHED
DIAGNOSIS_METHOD_GAIN_PARTIAL
DIAGNOSIS_METHOD_GAIN_NO_GAIN
DIAGNOSIS_METHOD_GAIN_NOT_ASSESSED
DIAGNOSIS_METHOD_GAIN_UNDERDETERMINED
~~~

Required guard:

~~~text
NO_GAIN != METHOD_FAILURE
~~~

Method gain is assessed only against a prospectively frozen fair comparator when baseline comparison is explicitly part of the task.

## 18. Required output schema

Every executable Diagnosis record must contain, as applicable:

~~~text
TASK_LOCK

CANDIDATE_CLASS_LOCK
CANDIDATE_CLASS_COMPLETENESS_RECORD

EVIDENCE_REGISTER
EVIDENCE_STATUS_PROVENANCE_LEDGER
EVIDENCE_SET_COHERENCE_LEDGER

BRIDGE_REGISTER
BRIDGE_STATUS_LEDGER
PAIR_COMPATIBILITY_MATRIX

REQUIRED_INTERFACE_LEDGER

INFERENCE_MODE_LEDGER
PROBABILISTIC_INTERFACE_LEDGER_IF_USED

RESOLUTION_TEMPORAL_REGIME_LEDGER

SOURCE_STATUS_HANDOFF_LEDGER
SUPPORT_READOUT_INFORMATION_LOSS_LEDGER

RESIDUAL_LEDGER_IF_USED
TRANSITION_DYNAMIC_LEDGER_IF_USED

CANDIDATE_DISPOSITION_LEDGER

COMPATIBLE_CANDIDATE_SET
EXCLUDED_CANDIDATE_SET
BLOCKED_CANDIDATE_SET
CONFLICTING_CANDIDATE_SET
UNDERDETERMINED_CANDIDATE_SET

DIAGNOSIS_SET_OUTCOME
IDENTIFIABILITY_SCOPE

CAUSE_CLAIM_LEDGER

ADDITIONAL_OBSERVATION_HANDOFF
NEIGHBOR_METHOD_SIDECAR_LEDGER

PRIMARY_DIAGNOSIS_STATUS
TASK_TERMINAL_STATUS

PROTOCOL_CONFORMANCE
METHOD_GAIN_STATUS

MAXIMUM_SUPPORTED_CLAIM
~~~

Every claim-relevant optional ledger must be marked:

~~~text
NOT_APPLICABLE
NOT_REQUESTED
BLOCKED
CONFLICTING
UNDERDETERMINED
OUT_OF_SCOPE
or
populated
~~~

rather than silently omitted.

## 19. Core semantic guards

~~~text
OBSERVATION_COMPATIBLE != TRUE_STATE_ESTABLISHED

MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED

UNIQUE_WITHIN_DECLARED_CLASS != GLOBAL_UNIQUE_DIAGNOSIS

NONE_COMPATIBLE_IN_DECLARED_CLASS != NO_REAL_STATE_EXISTS

EVIDENCE_CONFLICT != CANDIDATE_EXCLUSION_BY_DEFAULT

MISSING_REQUIRED_EVIDENCE != NEGATIVE_EVIDENCE

UNAVAILABLE_REQUIRED_INTERFACE != EVALUABLE_INCOMPATIBILITY

BLOCKED != NOT_ESTABLISHED

PAIR_INCOMPATIBLE != PAIR_CONFLICTING

CONFLICTING != UNDERDETERMINED

EQUAL_AGGREGATE != EQUAL_CURRENT_STATE

PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY

REDUCED_READOUT != COMPLETE_DIAGNOSTIC_CLASSIFIER

LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY

NONINJECTIVE_FORWARD_MAP != LICENSE_TO_SELECT_ONE_PREIMAGE

RESIDUAL_ZERO != SOURCE_STATE_IDENTITY

RESIDUAL_MATCH != CAUSE_ESTABLISHED

TRANSITION_COMPATIBILITY != UNIQUE_SUCCESSOR

CURRENT_STATE_DIAGNOSIS != PAST_HISTORY_RECONSTRUCTION

DIAGNOSTIC_COMPATIBILITY != CAUSAL_PROOF

CAUSE_IDENTIFICATION_ON_DECLARED_MODEL
  !=
UNRESTRICTED_REAL_WORLD_CAUSAL_CERTAINTY

PROBABILITY != COMPATIBILITY

CANDIDATE_RANKING != CANDIDATE_ELIMINATION

NO_PROBABILISTIC_INTERFACE != PERMISSION_TO_INVENT_PRIOR

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

## 20. Protocol integrity rules

~~~text
SOURCE_REGISTRY:
  immutable historical basis

TASK_INTERFACE_v0.1-draft:
  immutable historical draft

BOUNDARY_COUNTEREXAMPLES_v0.1-draft:
  immutable historical attack record

TASK_INTERFACE_BOUNDARY_AMENDMENT_001:
  binding prospective refinement basis

PROTOCOL_v0.1:
  frozen execution semantics
~~~

Post-result changes to claim-relevant:

~~~text
candidate class
evidence
bridge
resolver
inference mode
resolution
time/regime
support sidecar
residual rule
transition relation
cause bridge
probabilistic interface
maximum claim
~~~

require a new task version or future protocol revision.

## 21. Current protocol state

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

DEDICATED_DIAGNOSIS_PROTOCOL:
  established v0.1

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18

DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  0

SUCCESSFUL_DIRECT_DIAGNOSIS_PILOTS:
  0

POSITIVE_DIAGNOSIS_CASES:
  0

NEGATIVE_OR_UNRESOLVED_DIAGNOSIS_CASES:
  0

METHOD_BOUNDARY_DIAGNOSIS_CASES:
  0

BASELINE_DIAGNOSIS_CASES:
  0

NO_GAIN_DIAGNOSIS_CASES:
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
  protocol_frozen

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 22. Interpretation lock

~~~text
PROTOCOL_FROZEN != PROTOCOL_INTERNALLY_STANDARDIZED

PROTOCOL_CONFORMANT_RESULT != TRUE_STATE_CERTAINTY

DIAGNOSIS_ESTABLISHED != GLOBAL_TRUTH

DECLARED_CLASS_UNIQUENESS != GLOBAL_UNIQUENESS

CAUSE_IDENTIFICATION_ON_DECLARED_MODEL
  !=
UNRESTRICTED_CAUSAL_CERTAINTY

DETERMINISTIC_DEFAULT != PROBABILITY_REJECTED_IN_PRINCIPLE

NO_GAIN != METHOD_FAILURE
~~~

## 23. Next

Prospectively precommit and execute the first positive constructed Diagnosis challenge.

The challenge should exercise at minimum:

~~~text
coherent evidence set
explicit deterministic bridge
multiple-compatible result under one claim
unique-within-declared-class result under another claim
one noninjective readout
one required support/status handoff
one residual or transition constraint
one bounded cause-compatibility record
protocol conformance
maximum-supported-claim bounding
~~~
