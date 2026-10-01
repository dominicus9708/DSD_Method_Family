# DSD Reconstruction Protocol v0.1

Status: **FROZEN EXECUTABLE INTERNAL PROTOCOL**  
Date: **2026-10-01**  
Method: **Reconstruction / DSD 복원론**  
Legacy path ID: `15B`

## 1. Frozen lineage of this protocol

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

AMENDMENT_COMMIT:
  fbbf3840e606d1e005f7efcda3b38dfd33e2a2ce

AMENDMENT_BLOB:
  206926e77584398860ded1ccf2d7aac30cdf154a
~~~

This protocol operationalizes the recovered Reconstruction source registry, the historical Task Interface v0.1, the pre-protocol boundary attack, and Boundary Amendment 001.

It does not rewrite any predecessor paper, source registry, historical Task Interface, boundary-attack record, or Amendment.

Source-derived constraints and prospective method rules remain distinguishable.

## 2. Atomic method task

Given:

~~~text
a declared prior / omitted / damaged / compressed /
otherwise hidden source or history class

available present or retained evidence

typed status / support / provenance records

explicit forward / observation / aggregation / compression /
transition / history bridges when required

collision / fiber / kernel / injectivity records when available

Tracking and Lineage handoffs when supplied

claim-relevant temporal / history / regime /
resolution / relational scope

and any required reconstruction sidecars
~~~

Reconstruction determines:

~~~text
which declared source structures or histories remain compatible

which are excluded

which cannot yet be evaluated

which candidate distinctions remain unresolved

whether uniqueness holds within the frozen declared class and scope

which requested distinctions are provably unrecoverable
on the frozen interface

what recovered portion is supported when a partial claim is requested

and what additional evidence or sidecar role would discriminate
remaining candidates
~~~

without:

~~~text
inventing missing evidence or sidecars

changing the reconstruction class after seeing results

treating equal output as equal source

selecting one preimage from a noninjective relation without evidence

promoting declared-class uniqueness to global historical truth

promoting formation witness-history to temporal event history

promoting reconstructed links to established Tracking relations

promoting candidate predecessor/successor relations to established Lineage

treating interface unavailability as demonstrated information loss

counting pure definitional recompletion as independent Reconstruction evidence

inventing probabilistic priors or likelihoods

silently performing Measurement / Optimization / Diagnosis /
Tracking / Lineage / Prediction / Audit in place of Reconstruction
~~~

## 3. Primary claim levels

Exactly one primary claim level is frozen per Reconstruction task.

~~~text
RECONSTRUCTION_COMPATIBILITY_SET

UNIQUE_WITHIN_DECLARED_RECONSTRUCTION_CLASS

DECLARED_SCOPE_SOURCE_RECONSTRUCTION

PARTIAL_RECONSTRUCTION_WITH_LOSS_RECORD

UNRECOVERABLE_INFORMATION_ON_FROZEN_INTERFACE

HISTORY_COMPATIBILITY_SET
~~~

Subordinate obligations may be present, but they do not replace the primary claim level.

No claim level implies global exhaustiveness or unrestricted historical truth.

## 4. Reconstruction target kinds

Exactly one primary target kind is frozen per task.

~~~text
PRIOR_STATE

OMITTED_STRUCTURE

DAMAGED_STRUCTURE

COMPRESSED_SOURCE

MISSING_RELATION_OR_LINK

PARTIAL_HISTORY

FULL_DECLARED_HISTORY

MIXED_TYPED_SOURCE
~~~

Changing the primary target kind after claim-relevant result inspection requires a new task version.

## 5. Validity gates G1-G18

### G1 — task identity / version / primary-claim / target lock

Freeze:

~~~text
RECONSTRUCTION_TASK_ID
TASK_VERSION
PRIMARY_CLAIM_LEVEL
RECONSTRUCTION_QUESTION
RECONSTRUCTION_TARGET_KIND
MAXIMUM_SUPPORTED_CLAIM
~~~

No post-hoc claim or target rewrite is allowed.

### G2 — reconstruction-class representation and completeness lock

Freeze:

~~~text
RECONSTRUCTION_CLASS_ID
RECONSTRUCTION_CLASS_VERSION_OR_DEFINITION
RECONSTRUCTION_CLASS_REPRESENTATION_MODE
RECONSTRUCTION_CLASS_REPRESENTATION
CANDIDATE_EVALUATION_MODE
RECONSTRUCTION_CLASS_COMPLETENESS_STATUS
RECONSTRUCTION_CLASS_COMPLETENESS_PROVENANCE
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

Allowed completeness statuses:

~~~text
RECONSTRUCTION_CLASS_DECLARED_BOUNDED
RECONSTRUCTION_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE
RECONSTRUCTION_CLASS_COMPLETENESS_UNDERDETERMINED
RECONSTRUCTION_CLASS_COMPLETENESS_NOT_CLAIMED
~~~

Required guards:

~~~text
NON_ENUMERATED_CLASS != UNDECLARED_CLASS

INTENSIONAL_CLASS_DEFINITION
  !=
POST_HOC_CANDIDATE_EXPANSION

ONE_SURVIVING_DECLARED_RECONSTRUCTION
  !=
ONE_POSSIBLE_REAL_PAST
~~~

### G3 — evidence register / provenance / typed-status lock

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
REGIME_OR_SCHEMA_VERSION
DIRECT_OR_PROXY_ROLE
SOURCE_OR_DERIVATION_ROLE
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
MISSING_REQUIRED_EVIDENCE != NEGATIVE_EVIDENCE
INAPPLICABLE_EVIDENCE != NEGATIVE_EVIDENCE
UNDEFINED != ZERO
DEFINED_ZERO != ABSENCE
PROXY_RECORD != DIRECT_OBSERVATION
DERIVED_RECORD != ORIGINAL_SOURCE_RECORD
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

A conflicting evidence packet may not be silently converted into a zero-candidate historical conclusion.

### G5 — forward / observation bridge identity and status gate

Freeze every claim-relevant bridge:

~~~text
FORWARD_OR_OBSERVATION_BRIDGE_ID
BRIDGE_VERSION_OR_DEFINITION
BRIDGE_APPLICABILITY_SCOPE
BRIDGE_DIRECTION
BRIDGE_RELATION_STATUS
BRIDGE_PRECEDENCE_OR_RESOLVER_IF_ANY
~~~

Allowed bridge forms include:

~~~text
deterministic forward map
relation-valued transition
aggregation map
compression / reduction map
set-valued observation relation
typed status relation
support projection
residual criterion
history-to-evidence relation
domain-specific externally supplied rule
~~~

Bridge status family:

~~~text
BRIDGE_RELATION_AVAILABLE
BRIDGE_RELATION_UNAVAILABLE
BRIDGE_RELATION_CONFLICTING
BRIDGE_RELATION_UNDERDETERMINED
BRIDGE_RELATION_OUT_OF_SCOPE
~~~

Required guards:

~~~text
FORWARD_MAP
  !=
INVERSE_FUNCTION_BY_DEFAULT

RELATION_FORWARD_COMPATIBILITY
  !=
UNIQUE_PREIMAGE
~~~

### G6 — candidate evaluation and pair-disposition gate

Apply the frozen candidate evaluation mode.

When elementwise pair evaluation is meaningful, use:

~~~text
RECONSTRUCTION_PAIR_COMPATIBLE
RECONSTRUCTION_PAIR_INCOMPATIBLE
RECONSTRUCTION_PAIR_BLOCKED
RECONSTRUCTION_PAIR_CONFLICTING
RECONSTRUCTION_PAIR_OUT_OF_SCOPE
RECONSTRUCTION_PAIR_UNDERDETERMINED
~~~

For symbolic/fiber/theorem-based evaluation, emit an equivalent class-level compatibility/exclusion record that preserves the same logical distinctions.

Required guards:

~~~text
PAIR_INCOMPATIBLE != PAIR_CONFLICTING
PAIR_BLOCKED != PAIR_INCOMPATIBLE
CLASS_LEVEL_SYMBOLIC_RESULT != GLOBAL_COMPLETENESS_BY_DEFAULT
~~~

### G7 — required Reconstruction interface availability gate

Freeze each required claim-relevant interface not already fully captured by G3-G6:

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

Required unavailable interface -> dependent claim BLOCKED.

Required available information that evaluably demonstrates destructive loss -> evaluable NOT_ESTABLISHED or a supported frozen-interface unrecoverability claim, not BLOCKED.

### G8 — inference-mode gate

Freeze:

~~~text
INFERENCE_MODE
~~~

Allowed v0.1 modes:

~~~text
DETERMINISTIC_COMPATIBILITY
PROBABILISTIC_IF_EXPLICITLY_SUPPLIED
~~~

Default:

~~~text
DETERMINISTIC_COMPATIBILITY
~~~

For a probabilistic claim, freeze all required probabilistic objects for that claim, such as:

~~~text
PROBABILISTIC_MODEL_ID
PROBABILISTIC_MODEL_VERSION
PRIOR_OR_BASE_MEASURE
LIKELIHOOD_OR_HISTORY_OBSERVATION_MODEL
NORMALIZATION_DOMAIN
POSTERIOR_SEMANTICS
RANKING_RULE
DECISION_LOSS_OR_UTILITY_IF_REQUESTED
PROBABILISTIC_SCOPE
~~~

Required guards:

~~~text
PROBABILITY != HISTORICAL_TRUTH
CANDIDATE_RANKING != CANDIDATE_ELIMINATION
NO_PROBABILISTIC_INTERFACE != PERMISSION_TO_INVENT_PRIOR
MOST_PROBABLE_HISTORY != ONLY_COMPATIBLE_HISTORY
~~~

### G9 — resolution / equivalence / regime / scope lock

Freeze every claim-relevant:

~~~text
RECONSTRUCTION_SCOPE_CLASS
UNIQUENESS_SCOPE
TEMPORAL_SCOPE
HISTORY_SCOPE
ACTIVE_REGIME_OR_SCHEMA
RESOLUTION_OR_EQUIVALENCE_RULE
DISTINGUISHABILITY_RULE_IF_USED
~~~

Changing these after claim-relevant result inspection opens a new task version.

### G10 — Formation / Property / support / relational sidecar gate

When used, preserve claim-relevant source distinctions:

~~~text
FORMATION_STATUS_HANDOFF
PROPERTY_STATUS_HANDOFF
SUPPORT_RETENTION_SIDECAR
PROPERTY_KIND_AND_TYPED_INPUT
RELATIONAL_OR_CROSS_COORDINATE_CONDITION
PROVENANCE_RECORD
~~~

Required guards:

~~~text
DEFINED_ZERO != ABSENCE
UNDEFINED != ZERO
SUPPORT_IDENTITY != REDUCED_VALUE
PROPERTY_TYPED_INPUT != PROPERTY_VALUE_ALONE
PROVENANCE != SOURCE_IDENTITY
COORDINATEWISE_VALUES != RELATIONAL_COUPLING
~~~

Formation-specific guards:

~~~text
FORMATION_WITNESS_HISTORY
  !=
ACTUAL_TEMPORAL_HISTORY

STAGE_DEPENDENCY_ORDER
  !=
PHYSICAL_TIME_ORDER
~~~

### G11 — collision / fiber / kernel / injectivity and reconstruction-scope gate

When a forward/readout/reduction map is claim-relevant, freeze:

~~~text
READOUT_OR_REDUCTION_ID
READOUT_OR_REDUCTION_VERSION
SOURCE_CLASS
RECONSTRUCTION_SCOPE_CLASS
COLLISION_OR_FIBER_STATUS
KERNEL_STATUS_IF_LINEAR
INJECTIVITY_SCOPE
SUPPORT_RETENTION_STATUS
RELATIONAL_OR_CROSS_COORDINATE_CONDITION
REQUIRED_SIDECARS
~~~

Required guards:

~~~text
EQUAL_OUTPUT != EQUAL_SOURCE

NONINJECTIVE_FORWARD_MAP
  !=
LICENSE_TO_SELECT_ONE_PREIMAGE

LOSSLESS_ON_DECLARED_CLASS
  !=
GLOBAL_INJECTIVITY

INJECTIVITY_ON_DECLARED_CLASS
  !=
GLOBAL_RECONSTRUCTION

COORDINATEWISE_RECOVERY
  !=
RELATIONAL_OR_FULL_SOURCE_RECOVERY
~~~

### G12 — frozen-interface closure and unrecoverability gate

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

A claim of:

~~~text
UNRECOVERABLE_DISTINCTION_ESTABLISHED_ON_FROZEN_INTERFACE
~~~

requires at minimum:

~~~text
two distinct in-scope admissible source/history candidates

+
the same complete frozen claim-relevant evidence/readout package

+
INTERFACE_COMPLETE_FOR_DECLARED_CLAIM

+
no frozen interface component distinguishes them

+
the requested distinction lies inside the frozen reconstruction scope
~~~

Required guards:

~~~text
NO_REGISTERED_DISTINGUISHER
  !=
PROVED_UNRECOVERABILITY

UNRECOVERABLE_ON_FROZEN_INTERFACE
  !=
ABSOLUTELY_UNRECOVERABLE_BY_ANY_FUTURE_EVIDENCE

INTERFACE_COMPLETE_FOR_DECLARED_CLAIM
  !=
GLOBAL_INFORMATION_COMPLETENESS
~~~

### G13 — temporal / history relation coherence and composition gate

When reconstructing prior states or histories, freeze:

~~~text
HISTORY_RELATION_FAMILY_ID
HISTORY_RELATION_FAMILY_VERSION
HISTORY_RELATION_COHERENCE_STATUS
HISTORY_COMPOSITION_RULE_OR_NONE
HISTORY_PRECEDENCE_RULE_OR_NONE
DIRECT_VS_COMPOSED_RELATION_POLICY

TRANSITION_RELATION_ID
TRANSITION_RELATION_VERSION

DIRECT_LONG_INTERVAL_RECORDS
INTERMEDIATE_RELATION_RECORDS

BRANCHING_ALLOWED
MERGING_ALLOWED

UNIQUE_PREDECESSOR_REQUIREMENT
UNIQUE_PATH_REQUIREMENT
OTHER_HISTORY_CONSTRAINTS
~~~

History status family:

~~~text
HISTORY_RELATION_CONSISTENT
HISTORY_RELATION_CONFLICTING
HISTORY_RELATION_UNDERDETERMINED
HISTORY_RELATION_BLOCKED
HISTORY_RELATION_OUT_OF_SCOPE
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
UNIQUE_PREDECESSOR_HISTORY

BRANCHING_OR_MERGING
  !=
PROTOCOL_FAILURE
~~~

### G14 — Tracking / Lineage non-substitution gate

Reconstruction may consume typed Tracking and Lineage handoffs.

It may emit inferred candidates back to those methods.

But:

~~~text
RECONSTRUCTED_LINK
  !=
ESTABLISHED_TRACE_LINK

RECONSTRUCTION_CANDIDATE
  !=
ESTABLISHED_LINEAGE

MISSING_TRACE_LINK
  !=
LICENSE_TO_INVENT_ONE

TRACE_CONTINUITY
  !=
LINEAGE_IDENTITY

CURRENT_STATE_DIAGNOSIS
  !=
PAST_OR_OMITTED_RECONSTRUCTION
~~~

Any output intended for Tracking or Lineage must retain its Reconstruction/inferred status.

### G15 — definitional recompletion gate

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

Rules:

~~~text
PRIMARY_REQUEST_ONLY
+
complete primitive core supplied
+
requested result uniquely follows from frozen definition
->
RECONSTRUCTION_TASK_OUT_OF_SCOPE
for the Reconstruction claim

SUBORDINATE_DETERMINISTIC_STEP:
  allowed inside a genuine Reconstruction task
  but not counted as independent Reconstruction evidence
~~~

Required guard:

~~~text
DEFINITIONAL_RECOMPLETION
  !=
EVIDENCE_BASED_RECONSTRUCTION
~~~

### G16 — candidate disposition / set outcome / uniqueness gate

Candidate disposition family:

~~~text
RECONSTRUCTION_CANDIDATE_COMPATIBLE
RECONSTRUCTION_CANDIDATE_EXCLUDED
RECONSTRUCTION_CANDIDATE_BLOCKED
RECONSTRUCTION_CANDIDATE_CONFLICTING
RECONSTRUCTION_CANDIDATE_OUT_OF_SCOPE
RECONSTRUCTION_CANDIDATE_UNDERDETERMINED
~~~

Candidate-set outcome family:

~~~text
RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE
RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS
RECONSTRUCTION_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
RECONSTRUCTION_SET_PARTIALLY_EVALUATED
RECONSTRUCTION_SET_CONFLICTING
RECONSTRUCTION_SET_UNDERDETERMINED
~~~

Required guards:

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

A symbolic or intensional candidate set may satisfy these outcomes if the frozen evaluator establishes them without hidden enumeration assumptions.

### G17 — additional-evidence and neighboring-method handoff gate

Reconstruction may emit:

~~~text
UNRESOLVED_RECONSTRUCTION_PAIR_OR_CLASS
REQUIRED_DISTINCTION
MISSING_EVIDENCE_ROLE
REQUIRED_SIDECAR_OR_RELATION
POSSIBLE_MEASUREMENT_HANDOFF
TRACKING_CANDIDATE_HANDOFF
LINEAGE_CANDIDATE_HANDOFF
~~~

But:

~~~text
NEED_FOR_ADDITIONAL_EVIDENCE
  !=
OPTIMAL_MEASUREMENT_SELECTED

RECONSTRUCTION_DISCRIMINATOR_REQUIREMENT
  !=
MEASUREMENT_PLAN_EXECUTION

RECONSTRUCTION_DISCRIMINATOR_REQUIREMENT
  !=
OPTIMIZATION_RESULT

NEIGHBORING_METHOD_RESULT
  !=
RECONSTRUCTION_RESULT
~~~

### G18 — primary status / task terminal / conformance / gain / maximum-claim gate

Assign one primary Reconstruction status:

~~~text
RECONSTRUCTION_ESTABLISHED
RECONSTRUCTION_NOT_ESTABLISHED
RECONSTRUCTION_BLOCKED
RECONSTRUCTION_CONFLICTING
RECONSTRUCTION_OUT_OF_SCOPE
RECONSTRUCTION_UNDERDETERMINED
~~~

Assign exactly one task terminal:

~~~text
RECONSTRUCTION_TASK_ESTABLISHED
RECONSTRUCTION_TASK_PARTIAL
RECONSTRUCTION_TASK_NOT_ESTABLISHED
RECONSTRUCTION_TASK_BLOCKED
RECONSTRUCTION_TASK_CONFLICTING
RECONSTRUCTION_TASK_OUT_OF_SCOPE
RECONSTRUCTION_TASK_UNDERDETERMINED
~~~

Binding precedence:

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

PARTIAL requires:

~~~text
multiple independently required in-scope Reconstruction obligations

+
at least one ESTABLISHED obligation

+
at least one other evaluably NOT_ESTABLISHED obligation

+
no required obligation BLOCKED

+
no OUT_OF_SCOPE / CONFLICTING / UNDERDETERMINED terminal
~~~

Then emit:

~~~text
RECONSTRUCTION_PROTOCOL_CONFORMANCE
RECONSTRUCTION_METHOD_GAIN_STATUS
MAXIMUM_SUPPORTED_CLAIM
~~~

## 6. Binding operation T1-T18

### T1 — freeze task, target, and primary claim

Bind G1.

No claim-relevant result may be inspected before the task identity, target kind, primary claim, and maximum claim are frozen.

### T2 — freeze reconstruction class and evaluation mode

Bind G2.

Record extensional or intensional class representation, candidate evaluation mode, and completeness status.

### T3 — build evidence registry

Bind G3.

Preserve evidence identity, provenance, applicability, status, time/regime, and direct/proxy/source/derived role.

### T4 — evaluate evidence-set coherence

Bind G4.

Resolve or record conflict, underdetermination, blocked coherence, or out-of-scope evidence before interpreting candidate exclusion.

### T5 — freeze bridge registry

Bind G5.

Record bridge identity, version, direction, applicability scope, status, and any precedence/resolver.

### T6 — execute candidate/class compatibility evaluation

Bind G6.

Use the frozen evaluation mode to produce pair-level or class-level compatibility/exclusion records.

### T7 — evaluate required-interface availability

Bind G7.

Missing required interfaces are BLOCKED, not negative evidence and not demonstrated loss.

### T8 — freeze inference mode

Bind G8.

Default to deterministic compatibility.

Use probability only through a complete explicit probabilistic interface for the requested claim.

### T9 — freeze resolution / equivalence / regime / scope

Bind G9.

No post-hoc scope or distinguishability change.

### T10 — build typed source / support / relational ledger

Bind G10.

Preserve Formation, Property, support, provenance, and relational sidecars required by the claim.

### T11 — evaluate collision / fiber / kernel / injectivity and reconstruction scope

Bind G11.

Retain multiplicity where the frozen map is noninjective on the relevant class.

Evaluate uniqueness only at the frozen scope.

### T12 — evaluate interface closure and unrecoverability

Bind G12.

Do not infer unrecoverability from missing registrations.

Emit frozen-interface unrecoverability only when the complete-for-claim closure condition and witness requirements are satisfied.

### T13 — evaluate temporal / history relation obligations

Bind G13.

Preserve direct/composed conflicts, branch/merge multiplicity, and absence of unique-predecessor/path conditions.

### T14 — apply Tracking / Lineage / Diagnosis non-substitution gates

Bind G14.

Keep inferred Reconstruction objects distinct from established trace, lineage, or current-state Diagnosis results.

### T15 — apply definitional recompletion gate

Bind G15.

Pure recompletion from a complete primitive core is out of scope as a primary Reconstruction claim.

Subordinate recompletion remains typed as such.

### T16 — assign candidate dispositions, set outcome, and uniqueness record

Bind G16.

Construct compatible/excluded/blocked/conflicting/underdetermined records and the class-bounded set outcome.

### T17 — emit additional-evidence and neighboring-method handoffs

Bind G17.

State what distinction remains, but do not silently select or execute the next Measurement/Optimization/Tracking/Lineage action.

### T18 — assign primary status, terminal, conformance, gain, and maximum claim

Bind G18.

Preserve all lower-level ledgers under the task terminal.

## 7. Reconstruction-class representation statuses

Representation modes:

~~~text
EXPLICIT_ENUMERATION
PARAMETRIC_CLASS
PREDICATE_DEFINED_CLASS
RELATION_DEFINED_CLASS
EXTERNALLY_SUPPLIED_CLASS_INTERFACE
~~~

Evaluation modes:

~~~text
ELEMENTWISE
SYMBOLIC_SET
EXACT_FIBER_OR_PREIMAGE
THEOREM_OR_RELATION_BASED
EXTERNALLY_SUPPLIED_EVALUATOR
~~~

Completeness statuses:

~~~text
RECONSTRUCTION_CLASS_DECLARED_BOUNDED
RECONSTRUCTION_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE
RECONSTRUCTION_CLASS_COMPLETENESS_UNDERDETERMINED
RECONSTRUCTION_CLASS_COMPLETENESS_NOT_CLAIMED
~~~

## 8. Evidence-set statuses

~~~text
EVIDENCE_SET_CONSISTENT
EVIDENCE_SET_CONFLICTING
EVIDENCE_SET_UNDERDETERMINED
EVIDENCE_SET_BLOCKED
EVIDENCE_SET_OUT_OF_SCOPE
~~~

## 9. Bridge and pair statuses

Bridge statuses:

~~~text
BRIDGE_RELATION_AVAILABLE
BRIDGE_RELATION_UNAVAILABLE
BRIDGE_RELATION_CONFLICTING
BRIDGE_RELATION_UNDERDETERMINED
BRIDGE_RELATION_OUT_OF_SCOPE
~~~

Pair dispositions:

~~~text
RECONSTRUCTION_PAIR_COMPATIBLE
RECONSTRUCTION_PAIR_INCOMPATIBLE
RECONSTRUCTION_PAIR_BLOCKED
RECONSTRUCTION_PAIR_CONFLICTING
RECONSTRUCTION_PAIR_OUT_OF_SCOPE
RECONSTRUCTION_PAIR_UNDERDETERMINED
~~~

## 10. Required-interface statuses

~~~text
REQUIRED_RECONSTRUCTION_INTERFACE_AVAILABLE
REQUIRED_RECONSTRUCTION_INTERFACE_UNAVAILABLE
REQUIRED_RECONSTRUCTION_INTERFACE_CONFLICTING
REQUIRED_RECONSTRUCTION_INTERFACE_UNDERDETERMINED
REQUIRED_RECONSTRUCTION_INTERFACE_OUT_OF_SCOPE
~~~

## 11. Candidate dispositions

~~~text
RECONSTRUCTION_CANDIDATE_COMPATIBLE
RECONSTRUCTION_CANDIDATE_EXCLUDED
RECONSTRUCTION_CANDIDATE_BLOCKED
RECONSTRUCTION_CANDIDATE_CONFLICTING
RECONSTRUCTION_CANDIDATE_OUT_OF_SCOPE
RECONSTRUCTION_CANDIDATE_UNDERDETERMINED
~~~

## 12. Candidate-set outcomes

~~~text
RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE
RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS
RECONSTRUCTION_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
RECONSTRUCTION_SET_PARTIALLY_EVALUATED
RECONSTRUCTION_SET_CONFLICTING
RECONSTRUCTION_SET_UNDERDETERMINED
~~~

These are reconstruction-set results, not truth labels.

## 13. Recovery / unrecoverability statuses

~~~text
RECOVERABLE_ON_DECLARED_SCOPE
NONUNIQUE_ON_DECLARED_SCOPE
UNRECOVERABLE_DISTINCTION_ESTABLISHED_ON_FROZEN_INTERFACE
RECOVERY_ASSESSMENT_BLOCKED
RECOVERY_ASSESSMENT_CONFLICTING
RECOVERY_ASSESSMENT_UNDERDETERMINED
~~~

Interface-closure statuses:

~~~text
INTERFACE_COMPLETE_FOR_DECLARED_CLAIM
INTERFACE_EXPLICITLY_PARTIAL
INTERFACE_COMPLETENESS_UNDERDETERMINED
INTERFACE_CLOSURE_BLOCKED
INTERFACE_CLOSURE_OUT_OF_SCOPE
~~~

## 14. History-relation statuses

~~~text
HISTORY_RELATION_CONSISTENT
HISTORY_RELATION_CONFLICTING
HISTORY_RELATION_UNDERDETERMINED
HISTORY_RELATION_BLOCKED
HISTORY_RELATION_OUT_OF_SCOPE
~~~

Branching and merging remain ordinary relation structures unless the frozen task explicitly requires uniqueness.

## 15. Inference-mode and recompletion statuses

Inference modes:

~~~text
DETERMINISTIC_COMPATIBILITY
PROBABILISTIC_IF_EXPLICITLY_SUPPLIED
~~~

Definitional-recompletion roles:

~~~text
DEFINITIONAL_RECOMPLETION_NOT_USED
DEFINITIONAL_RECOMPLETION_SUBORDINATE_DETERMINISTIC_STEP
DEFINITIONAL_RECOMPLETION_PRIMARY_REQUEST_ONLY
~~~

## 16. Primary Reconstruction statuses

~~~text
RECONSTRUCTION_ESTABLISHED
RECONSTRUCTION_NOT_ESTABLISHED
RECONSTRUCTION_BLOCKED
RECONSTRUCTION_CONFLICTING
RECONSTRUCTION_OUT_OF_SCOPE
RECONSTRUCTION_UNDERDETERMINED
~~~

Important:

~~~text
RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE
  may coexist with
RECONSTRUCTION_ESTABLISHED

when the primary claim is a compatibility-set claim.
~~~

## 17. Task terminals

~~~text
RECONSTRUCTION_TASK_ESTABLISHED
RECONSTRUCTION_TASK_PARTIAL
RECONSTRUCTION_TASK_NOT_ESTABLISHED
RECONSTRUCTION_TASK_BLOCKED
RECONSTRUCTION_TASK_CONFLICTING
RECONSTRUCTION_TASK_OUT_OF_SCOPE
RECONSTRUCTION_TASK_UNDERDETERMINED
~~~

Binding precedence:

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

The terminal does not erase subordinate records.

## 18. Protocol conformance

Allowed conformance statuses:

~~~text
RECONSTRUCTION_PROTOCOL_CONFORMANT
RECONSTRUCTION_PROTOCOL_NONCONFORMANT
RECONSTRUCTION_PROTOCOL_CONFORMANCE_UNDERDETERMINED
~~~

At minimum, conformance requires:

~~~text
task locks frozen before evaluation

class representation/evaluation mode frozen

evidence and bridge registries provenance-preserving

required interfaces not silently imputed

candidate multiplicity retained where required

unrecoverability claim closure conditions respected

history-relation conflicts not hidden

Tracking / Lineage / Diagnosis non-substitution respected

definitional recompletion correctly typed

terminal precedence correctly applied

maximum-supported claim not exceeded
~~~

A nonconformant run does not become a successful Reconstruction case merely because its final candidate happens to match an expected answer.

## 19. Method-gain statuses

Allowed internal method-gain statuses:

~~~text
RECONSTRUCTION_GAIN_SHOWN
RECONSTRUCTION_GAIN_NOT_YET_TESTED
RECONSTRUCTION_NO_GAIN
RECONSTRUCTION_GAIN_UNDERDETERMINED
~~~

Rules:

~~~text
protocol conformance
  !=
method gain

correct bounded reconstruction result
  !=
novel advantage

fair baseline match
  may yield
RECONSTRUCTION_NO_GAIN

NO_GAIN
  !=
method failure

NO_GAIN
  !=
method deletion / merger / absorption
~~~

## 20. Required output schema

Every executable Reconstruction run must emit, as applicable:

~~~text
LOCKED_RECONSTRUCTION_TASK_RECORD

RECONSTRUCTION_CLASS_RECORD
RECONSTRUCTION_CLASS_REPRESENTATION_MODE
CANDIDATE_EVALUATION_MODE
RECONSTRUCTION_CLASS_COMPLETENESS_STATUS

EVIDENCE_REGISTER
EVIDENCE_SET_COHERENCE_STATUS

FORWARD_OR_OBSERVATION_BRIDGE_REGISTER
BRIDGE_STATUS_LEDGER

PAIR_OR_CLASS_COMPATIBILITY_LEDGER

REQUIRED_INTERFACE_LEDGER

FORMATION_PROPERTY_SUPPORT_RELATIONAL_LEDGER

COLLISION_FIBER_KERNEL_INJECTIVITY_LEDGER
RECONSTRUCTION_SCOPE_RECORD

INTERFACE_CLOSURE_RECORD
RECOVERY_AND_UNRECOVERABILITY_RECORD

TEMPORAL_HISTORY_RELATION_LEDGER_IF_USED

TRACKING_HANDOFF_LEDGER_IF_USED
LINEAGE_HANDOFF_LEDGER_IF_USED

DEFINITIONAL_RECOMPLETION_SIDECAR_IF_USED

RECONSTRUCTION_CANDIDATE_DISPOSITION_LEDGER
COMPATIBLE_RECONSTRUCTION_SET
EXCLUDED_RECONSTRUCTION_SET
BLOCKED_CONFLICTING_OR_UNRESOLVED_SET

RECONSTRUCTION_SET_OUTCOME
UNIQUENESS_SCOPE

ADDITIONAL_EVIDENCE_HANDOFF

RECONSTRUCTION_PRIMARY_STATUS
RECONSTRUCTION_TASK_TERMINAL

RECONSTRUCTION_PROTOCOL_CONFORMANCE
RECONSTRUCTION_METHOD_GAIN_STATUS

MAXIMUM_SUPPORTED_CLAIM
~~~

No omitted ledger may be silently treated as PASS when it was claim-relevant.

## 21. Core semantic guards

~~~text
EQUAL_OUTPUT != EQUAL_SOURCE

FORMATION_WITNESS_HISTORY != ACTUAL_TEMPORAL_HISTORY

STAGE_DEPENDENCY_ORDER != PHYSICAL_TIME_ORDER

LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY

INJECTIVITY_ON_DECLARED_CLASS != GLOBAL_RECONSTRUCTION

COORDINATEWISE_RECOVERY != RELATIONAL_OR_FULL_SOURCE_RECOVERY

TRANSITION_COMPATIBILITY != UNIQUE_PREDECESSOR_HISTORY

RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK

RECONSTRUCTION_CANDIDATE != ESTABLISHED_LINEAGE

CURRENT_STATE_DIAGNOSIS != PAST_OR_OMITTED_RECONSTRUCTION

DEFINITIONAL_RECOMPLETION != EVIDENCE_BASED_RECONSTRUCTION

MISSING_REQUIRED_RECONSTRUCTION_INFORMATION != NEGATIVE_EVIDENCE

UNAVAILABLE_REQUIRED_INTERFACE != DEMONSTRATED_UNRECOVERABILITY

NO_REGISTERED_DISTINGUISHER != PROVED_UNRECOVERABILITY

SINGLE_REMAINING_DECLARED_RECONSTRUCTION != GLOBAL_HISTORICAL_TRUTH

NO_ADMISSIBLE_DECLARED_RECONSTRUCTION != NO_REAL_PAST_STATE_OR_HISTORY

MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED

PROBABILITY != HISTORICAL_TRUTH

CANDIDATE_RANKING != CANDIDATE_ELIMINATION

PARTIAL != BLOCKED_RESCUE_LABEL
~~~

## 22. Protocol integrity rules

1. Do not modify the source registry, historical Task Interface, boundary attack, or Amendment to make a later run pass.
2. Any claim-relevant task change after result inspection opens a new task version.
3. Preserve PASS, FAIL, BLOCKED, CONFLICTING, UNDERDETERMINED, OUT_OF_SCOPE, NO_GAIN, and SUPERSEDED results.
4. Do not infer absent sidecars, priors, likelihoods, history links, or lineage identity.
5. Keep Reconstruction result status separate from protocol conformance and method-gain status.
6. Keep internal protocol evidence separate from external/independent validation.
7. A same-project deterministic retrace is not independent replication.
8. Protocol evolution after direct evidence requires explicit amendment/revision provenance.

## 23. Current protocol state

~~~text
DEDICATED_RECONSTRUCTION_PROTOCOL:
  established v0.1

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18

SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 historical draft preserved

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

BOUNDARY_AMENDMENT_001:
  established

REFINEMENT_GROUPS_ADOPTED:
  8/8

DIRECT_RECONSTRUCTION_PILOTS_ATTEMPTED:
  0

SUCCESSFUL_DIRECT_RECONSTRUCTION_PILOTS:
  0

POSITIVE_RECONSTRUCTION_CASES:
  0

NEGATIVE_OR_UNRESOLVED_RECONSTRUCTION_CASES:
  0

METHOD_BOUNDARY_RECONSTRUCTION_CASES:
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
  protocol_frozen_pre_challenge

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Protocol freeze itself is not a successful Reconstruction pilot.

## 24. Interpretation lock

This Protocol v0.1 establishes an executable internal method interface.

It does not establish:

~~~text
that any real historical reconstruction has been validated externally

that any declared candidate class is globally exhaustive by default

that a unique declared-class reconstruction is global historical truth

that frozen-interface unrecoverability is absolute impossibility
under all possible future evidence

that probability establishes historical truth

that Reconstruction outperforms competent non-DSD inverse methods

that same-project deterministic retrace is independent replication
~~~

## 25. Next

Prospectively precommit and execute the first direct positive constructed Reconstruction challenge.

Working next challenge ID:

~~~text
RECON-CH-001
~~~

The challenge should exercise at minimum:

~~~text
one explicit reconstruction class

one frozen forward/observation bridge

one coherent evidence packet

at least one compatible candidate

at least one excluded candidate when feasible

class-bounded set outcome

maximum-supported claim

protocol conformance

without using external validation evidence
~~~
