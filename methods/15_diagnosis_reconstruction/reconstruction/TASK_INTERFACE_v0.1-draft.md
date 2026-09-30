# DSD Reconstruction — Task Interface v0.1 Draft

Status: **PRE-PROTOCOL HISTORICAL DRAFT — NOT AN EXECUTABLE STANDARD**  
Date: **2026-10-01**  
Method: **Reconstruction / DSD 복원론**  
Legacy path ID: `15B`

Source basis:

~~~text
SOURCE_REGISTRY_v0.1.md

commit:
  78acf2532680722cf09a50376d0c69d74803f1a4

blob:
  f00063f285745dd328e5b2d8c82ff3579957d615
~~~

This draft is a prospective method interface built from recovered source constraints.

It is not a theorem of the predecessor papers.

Once direct boundary attack begins, this file must remain immutable historical development evidence. Refinements must be recorded in a separate amendment.

## 1. Atomic task

Working atomic Reconstruction task:

~~~text
Given:
  a declared prior / omitted / damaged / compressed /
  otherwise hidden source or history class,

  available present or retained evidence,

  typed status / support / provenance records,

  explicit forward / aggregation / compression /
  transition / observation bridges where required,

  collision / fiber / kernel / injectivity records when available,

  Tracking and Lineage handoffs when supplied,

  and any claim-relevant temporal / history / regime /
  resolution / relational scope,

determine:
  which declared source structures or histories remain compatible,
  which are excluded,
  which cannot yet be evaluated,
  which distinctions are unresolved,
  which distinctions are provably unrecoverable
  under the frozen interface,
  whether uniqueness holds within the declared class and scope,
  and what additional evidence or sidecars would discriminate
  remaining candidates,

without:
  inventing missing evidence,
  silently changing the reconstruction class,
  promoting one preimage to global historical truth,
  rewriting an inferred link as an observed Tracking relation,
  rewriting a candidate predecessor as established Lineage identity,
  treating formation witness-history as temporal event history,
  or converting interface unavailability into proof of information loss.
~~~

## 2. Method boundary

Reconstruction asks:

~~~text
Which declared prior / omitted / damaged / compressed /
otherwise hidden sources or histories remain compatible
with the frozen evidence and forward-interface semantics?
~~~

It does not by itself answer:

~~~text
Which current hidden state is the diagnosis?
Which trace link was directly observed?
Which predecessor/successor identity is established by Lineage?
Which forward transformation should be executed?
Which measurement should be selected or performed?
Which candidate is optimal?
Which future state will occur?
Did the historical event globally and uniquely occur?
~~~

Working distinctions:

~~~text
DIAGNOSIS:
  current hidden-state / condition / failure-mode inference

RECONSTRUCTION:
  prior / omitted / damaged / compressed source or history inference

TRACKING:
  evidence-bounded trace relations

LINEAGE:
  predecessor / successor identity across change

AGGREGATION:
  declared forward summary operation

COMPRESSION:
  purpose-bounded reduction and information-retention contract

TRANSFORMATION:
  declared source-target mapping / change

MEASUREMENT:
  discrimination adequacy or observed-result interface

PREDICTION:
  future consequence under supplied model

AUDIT:
  conformance / evidence / process evaluation
~~~

## 3. Reconstruction target kind

Every future executable task freezes one primary target kind.

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

Interpretation:

~~~text
PRIOR_STATE:
  one or more earlier state candidates

OMITTED_STRUCTURE:
  structure intentionally or accidentally absent
  from the retained representation

DAMAGED_STRUCTURE:
  source structure partially destroyed or corrupted

COMPRESSED_SOURCE:
  source candidates compatible with a declared
  aggregation/compression/reduction output

MISSING_RELATION_OR_LINK:
  candidate unobserved relation required to complete
  a declared bounded structure or history;
  this remains an inferred Reconstruction object,
  not an established Tracking relation by default

PARTIAL_HISTORY:
  one or more missing historical segments under
  frozen temporal and relation semantics

FULL_DECLARED_HISTORY:
  candidate histories spanning the full frozen
  history scope; not a claim about all possible reality

MIXED_TYPED_SOURCE:
  a declared combination of typed coordinates or
  structures whose coupling must remain explicit
~~~

Changing the target kind after seeing candidate outcomes opens a new task version.

## 4. Primary claim levels

A task freezes one primary claim level.

~~~text
RECONSTRUCTION_COMPATIBILITY_SET

UNIQUE_WITHIN_DECLARED_RECONSTRUCTION_CLASS

DECLARED_SCOPE_SOURCE_RECONSTRUCTION

PARTIAL_RECONSTRUCTION_WITH_LOSS_RECORD

UNRECOVERABLE_INFORMATION_ON_FROZEN_INTERFACE

HISTORY_COMPATIBILITY_SET
~~~

Interpretation:

~~~text
RECONSTRUCTION_COMPATIBILITY_SET:
  determine compatible / excluded / unevaluable
  declared reconstruction candidates without requiring uniqueness

UNIQUE_WITHIN_DECLARED_RECONSTRUCTION_CLASS:
  evaluate whether exactly one declared candidate remains
  after every claim-relevant candidate is evaluable
  under the frozen semantics

DECLARED_SCOPE_SOURCE_RECONSTRUCTION:
  reconstruct the requested source coordinates/relations
  only within a frozen source class and reconstruction scope

PARTIAL_RECONSTRUCTION_WITH_LOSS_RECORD:
  establish supported recovered coordinates/relations
  while explicitly retaining unresolved or lost portions

UNRECOVERABLE_INFORMATION_ON_FROZEN_INTERFACE:
  establish that at least one frozen required distinction
  cannot be recovered from the frozen evidence/interface,
  under an explicit collision/non-identifiability witness
  or other sufficient declared condition

HISTORY_COMPATIBILITY_SET:
  determine the admissible declared histories without
  promoting compatibility to one globally true history
~~~

No claim level implies global exhaustiveness or unrestricted historical truth.

## 5. Required task lock

Every future executable Reconstruction task should freeze at least:

~~~text
RECONSTRUCTION_TASK_ID
TASK_VERSION

PRIMARY_CLAIM_LEVEL
RECONSTRUCTION_QUESTION
RECONSTRUCTION_TARGET_KIND

RECONSTRUCTION_CLASS_ID
RECONSTRUCTION_CLASS_VERSION_OR_DEFINITION
RECONSTRUCTION_CANDIDATE_IDENTITIES
RECONSTRUCTION_CLASS_COMPLETENESS_STATUS

EVIDENCE_SET_ID
EVIDENCE_RECORDS
EVIDENCE_PROVENANCE
EVIDENCE_STATUS_RECORDS
REQUIRED_EVIDENCE_POLICY

FORWARD_OR_OBSERVATION_BRIDGE_ID
BRIDGE_VERSION_OR_DEFINITION
BRIDGE_APPLICABILITY_SCOPE

RECONSTRUCTION_SCOPE_CLASS
UNIQUENESS_SCOPE

TEMPORAL_SCOPE
HISTORY_SCOPE
ACTIVE_REGIME_OR_SCHEMA
RESOLUTION_OR_EQUIVALENCE_RULE

MAXIMUM_SUPPORTED_CLAIM
~~~

Conditionally required when claim-relevant:

~~~text
FORMATION_STATUS_HANDOFF
PROPERTY_STATUS_HANDOFF

AGGREGATION_HANDOFF
COMPRESSION_HANDOFF
TRANSFORMATION_HANDOFF

READOUT_OR_REDUCTION_ID
COLLISION_OR_FIBER_RECORD
KERNEL_RECORD_IF_LINEAR
INJECTIVITY_SCOPE

SUPPORT_RETENTION_SIDECAR
RELATIONAL_OR_CROSS_COORDINATE_CONDITION

TRACKING_HANDOFF
LINEAGE_HANDOFF
TRANSITION_RELATION_HANDOFF

MEASUREMENT_HANDOFF

FORMATION_WITNESS_HISTORY_HANDOFF
DEFINITIONAL_RECOMPLETION_HANDOFF

ADDITIONAL_EVIDENCE_HANDOFF_POLICY
~~~

Changing a claim-relevant lock after observing candidate disposition opens a new task version.

## 6. Reconstruction-class completeness status

Working status family:

~~~text
RECONSTRUCTION_CLASS_DECLARED_BOUNDED

RECONSTRUCTION_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE

RECONSTRUCTION_CLASS_COMPLETENESS_UNDERDETERMINED

RECONSTRUCTION_CLASS_COMPLETENESS_NOT_CLAIMED
~~~

Core draft guards:

~~~text
ONE_SURVIVING_DECLARED_RECONSTRUCTION
  !=
ONE_POSSIBLE_REAL_PAST

NO_SURVIVING_DECLARED_RECONSTRUCTION
  !=
NO_REAL_PAST_STATE_OR_HISTORY
~~~

A completeness claim is itself a supplied claim/handoff with provenance.

Reconstruction does not manufacture class completeness.

## 7. Evidence record

Every claim-relevant evidence item should retain:

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

When Property semantics are imported, preserve:

~~~text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_VALUE
~~~

Draft guards:

~~~text
MISSING_REQUIRED_EVIDENCE != NEGATIVE_EVIDENCE
INAPPLICABLE_EVIDENCE != NEGATIVE_EVIDENCE
UNDEFINED != ZERO
DEFINED_ZERO != ABSENCE
PROXY_RECORD != DIRECT_OBSERVATION
DERIVED_RECORD != ORIGINAL_SOURCE_RECORD
~~~

## 8. Forward / observation bridge

For each reconstruction candidate `h` and evidence item `e`, an explicit supplied bridge must determine how the candidate can be compared with the frozen evidence.

Allowed bridge forms may include:

~~~text
deterministic forward map
relation-valued transition
aggregation map
compression/reduction map
set-valued observation relation
typed status relation
support projection
residual criterion
history-to-evidence relation
domain-specific externally supplied rule
~~~

No missing bridge is inferred.

The bridge must preserve its declared direction.

~~~text
FORWARD_MAP
  !=
INVERSE_FUNCTION_BY_DEFAULT

RELATION_FORWARD_COMPATIBILITY
  !=
UNIQUE_PREIMAGE
~~~

## 9. Candidate-evidence pair disposition

Working pair disposition:

~~~text
RECONSTRUCTION_PAIR_COMPATIBLE

RECONSTRUCTION_PAIR_INCOMPATIBLE

RECONSTRUCTION_PAIR_BLOCKED

RECONSTRUCTION_PAIR_CONFLICTING

RECONSTRUCTION_PAIR_OUT_OF_SCOPE

RECONSTRUCTION_PAIR_UNDERDETERMINED
~~~

Meaning:

~~~text
COMPATIBLE:
  the candidate can produce or coexist with the evidence
  under the frozen bridge and scope

INCOMPATIBLE:
  the frozen bridge/evidence rule validly excludes
  the candidate for this pair

BLOCKED:
  a required bridge, sidecar, provenance record,
  or prerequisite is unavailable

CONFLICTING:
  simultaneously applicable frozen records make
  mutually incompatible pair-level claims

OUT_OF_SCOPE:
  the candidate/evidence relation lies outside
  the declared bridge or task scope

UNDERDETERMINED:
  multiple admissible frozen semantics yield
  different pair outcomes and no resolver is frozen
~~~

## 10. Reconstruction candidate disposition

For each declared source/history candidate `h`:

~~~text
RECONSTRUCTION_CANDIDATE_COMPATIBLE

RECONSTRUCTION_CANDIDATE_EXCLUDED

RECONSTRUCTION_CANDIDATE_BLOCKED

RECONSTRUCTION_CANDIDATE_CONFLICTING

RECONSTRUCTION_CANDIDATE_OUT_OF_SCOPE

RECONSTRUCTION_CANDIDATE_UNDERDETERMINED
~~~

Working interpretation:

~~~text
COMPATIBLE:
  every required evaluable evidence relation is compatible
  under the frozen combination policy

EXCLUDED:
  the frozen exclusion rule is triggered by valid
  claim-relevant incompatibility

BLOCKED:
  a required interface is unavailable, preventing
  a complete candidate disposition

CONFLICTING:
  applicable evidence/bridge records conflict for
  the candidate under the same frozen semantics

OUT_OF_SCOPE:
  the candidate lies outside the declared source/history class
  or required bridge scope

UNDERDETERMINED:
  admissible semantics yield different candidate dispositions
  and no frozen resolver exists
~~~

## 11. Candidate-set outcome

After candidate-level evaluation, record one working set outcome:

~~~text
RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE

RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS

RECONSTRUCTION_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS

RECONSTRUCTION_SET_PARTIALLY_EVALUATED

RECONSTRUCTION_SET_CONFLICTING

RECONSTRUCTION_SET_UNDERDETERMINED
~~~

These are reconstruction results, not truth labels.

Core guards:

~~~text
MULTIPLE_COMPATIBLE
  !=
TASK_UNDERDETERMINED

UNIQUE_WITHIN_DECLARED_CLASS
  !=
GLOBAL_HISTORICAL_TRUTH

NONE_COMPATIBLE_IN_DECLARED_CLASS
  !=
NO_REAL_PAST_EXISTS
~~~

A fully frozen task may legitimately return `MULTIPLE_COMPATIBLE` as an established Reconstruction result.

## 12. Collision, injectivity, and unrecoverability discipline

When a forward/readout/reduction map is used, freeze:

~~~text
READOUT_OR_REDUCTION_ID
READOUT_VERSION

SOURCE_CLASS
RECONSTRUCTION_SCOPE_CLASS

COLLISION_OR_FIBER_STATUS
KERNEL_STATUS_IF_LINEAR
INJECTIVITY_SCOPE

SUPPORT_RETENTION_STATUS
RELATIONAL_OR_CROSS_COORDINATE_CONDITION

REQUIRED_SIDECARS
~~~

Draft guards:

~~~text
EQUAL_OUTPUT != EQUAL_SOURCE

NONINJECTIVE_FORWARD_MAP
  !=
LICENSE_TO_SELECT_ONE_PREIMAGE

LOSSLESS_ON_DECLARED_CLASS
  !=
GLOBAL_INJECTIVITY

COORDINATEWISE_RECOVERY
  !=
RELATIONAL_OR_FULL_SOURCE_RECOVERY
~~~

Working information-recovery status family:

~~~text
RECOVERABLE_ON_DECLARED_SCOPE

NONUNIQUE_ON_DECLARED_SCOPE

UNRECOVERABLE_DISTINCTION_ESTABLISHED_ON_FROZEN_INTERFACE

RECOVERY_ASSESSMENT_BLOCKED

RECOVERY_ASSESSMENT_CONFLICTING

RECOVERY_ASSESSMENT_UNDERDETERMINED
~~~

A claim of `UNRECOVERABLE_DISTINCTION_ESTABLISHED_ON_FROZEN_INTERFACE` requires a sufficient frozen witness, for example:

~~~text
two distinct in-scope admissible sources
+
same complete frozen evidence/readout package
+
no frozen sidecar or relation that distinguishes them
+
the requested distinction lies inside the reconstruction scope
~~~

This remains interface-bounded.

~~~text
UNRECOVERABLE_ON_FROZEN_INTERFACE
  !=
ABSOLUTELY_UNRECOVERABLE_BY_ANY_FUTURE_EVIDENCE
~~~

Required-interface unavailability is not itself a proof of information loss.

~~~text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
DEMONSTRATED_UNRECOVERABILITY
~~~

## 13. Typed status, support, and relational sidecars

Reconstruction must preserve claim-relevant source distinctions rather than flattening them into one numeric output.

At minimum when applicable:

~~~text
DEFINED_ZERO != ABSENCE

UNDEFINED != ZERO

SUPPORT_IDENTITY != REDUCED_VALUE

PROPERTY_KIND_AND_TYPED_INPUT
  remain attached when claim-relevant

PROVENANCE != SOURCE_IDENTITY

COORDINATEWISE_VALUES
  !=
RELATIONAL_COUPLING
~~~

If a sidecar is required for the requested reconstruction scope and is unavailable:

~~~text
required sidecar unavailable
  ->
BLOCKED or PARTIAL
according to the frozen task semantics

not:
  source excluded

and not:
  information loss proven
~~~

## 14. Temporal and history discipline

When reconstructing prior states or histories, freeze:

~~~text
TEMPORAL_SCOPE
HISTORY_SCOPE
TIME_OR_EPOCH_ORDER
ACTIVE_REGIME_OR_SCHEMA

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

Draft guards:

~~~text
STAGE_DEPENDENCY_ORDER
  !=
PHYSICAL_TIME_ORDER

FORMATION_WITNESS_HISTORY
  !=
ACTUAL_TEMPORAL_HISTORY

TRANSITION_COMPATIBILITY
  !=
UNIQUE_PREDECESSOR_HISTORY

TEMPORAL_ADJACENCY
  !=
HISTORICAL_LINK

BRANCHING_HISTORY
  !=
PROTOCOL_FAILURE

MERGING_HISTORY
  !=
PROTOCOL_FAILURE
~~~

A relation-valued transition may retain multiple predecessor candidates.

A unique temporal history may be claimed only under separately frozen uniqueness conditions.

## 15. Tracking and Lineage handoff discipline

Reconstruction may consume:

~~~text
Tracking:
  observed / supported trace relations
  missing / blocked / conflicting trace segments
  relation provenance

Lineage:
  established predecessor/successor relations
  branch/merge records
  identity-bearing component records
  lineage scope
~~~

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
~~~

Reconstruction outputs intended for those methods must be emitted as typed candidate/inferred handoffs.

## 16. Definitional recompletion boundary

Some predecessor systems admit derived coordinates that can be uniquely recomputed from a complete supplied primitive core.

That is not automatically a Reconstruction result.

Working distinction:

~~~text
DEFINITIONAL_RECOMPLETION:
  re-evaluate uniquely defined derived coordinates
  from a fully supplied primitive core

EVIDENCE_BASED_RECONSTRUCTION:
  infer missing prior/hidden structure from incomplete,
  reduced, damaged, or indirect evidence
~~~

Core guard:

~~~text
DEFINITIONAL_RECOMPLETION
  !=
EVIDENCE_BASED_RECONSTRUCTION
~~~

A task whose requested operation is only definitional recompletion may be out of scope for Reconstruction unless the larger reconstruction task uses it as a subordinate deterministic step.

## 17. Additional-evidence handoff

Reconstruction may identify unresolved candidate distinctions and emit:

~~~text
UNRESOLVED_RECONSTRUCTION_PAIR_OR_CLASS

REQUIRED_DISTINCTION

MISSING_EVIDENCE_ROLE

REQUIRED_SIDECAR_OR_RELATION

POSSIBLE_MEASUREMENT_HANDOFF
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
~~~

Selection or execution of the next observation remains a neighboring task unless explicitly handed off.

## 18. Working primary Reconstruction status

Overall claim status family:

~~~text
RECONSTRUCTION_ESTABLISHED

RECONSTRUCTION_NOT_ESTABLISHED

RECONSTRUCTION_BLOCKED

RECONSTRUCTION_CONFLICTING

RECONSTRUCTION_OUT_OF_SCOPE

RECONSTRUCTION_UNDERDETERMINED
~~~

Interpretation:

~~~text
ESTABLISHED:
  requested primary claim level is supported by
  complete evaluation of the required frozen obligations

NOT_ESTABLISHED:
  all required evaluable information is present
  but the requested claim level fails evaluably

BLOCKED:
  required evidence / bridge / sidecar / prerequisite
  is unavailable

CONFLICTING:
  frozen claim-relevant task/rule/evidence records
  are mutually incompatible and no precedence resolves them

OUT_OF_SCOPE:
  requested operation is not a Reconstruction task
  or lies outside the frozen reconstruction class/scope

UNDERDETERMINED:
  multiple admissible claim-relevant semantics remain
  and yield different overall results
~~~

Important:

~~~text
MULTIPLE_COMPATIBLE
  may coexist with
RECONSTRUCTION_ESTABLISHED

when the primary claim level is:
  RECONSTRUCTION_COMPATIBILITY_SET
  or
  HISTORY_COMPATIBILITY_SET
~~~

## 19. Working task terminal

The future protocol is expected to emit exactly one task terminal:

~~~text
RECONSTRUCTION_TASK_ESTABLISHED

RECONSTRUCTION_TASK_PARTIAL

RECONSTRUCTION_TASK_NOT_ESTABLISHED

RECONSTRUCTION_TASK_BLOCKED

RECONSTRUCTION_TASK_CONFLICTING

RECONSTRUCTION_TASK_OUT_OF_SCOPE

RECONSTRUCTION_TASK_UNDERDETERMINED
~~~

Draft meaning of `PARTIAL`:

~~~text
multiple independently required reconstruction obligations exist,
at least one is validly established,
at least one is validly not established or unevaluable,
the supported recovered portion remains meaningful,
and no higher-priority task-level state overrides the mixed outcome
~~~

Draft terminal precedence candidate:

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

This precedence is **not frozen**.

It is an explicit boundary-attack target.

## 20. Binding-operation draft

Working operation:

~~~text
R1
  freeze task identity, primary claim level,
  target kind, reconstruction class, scope, and maximum claim

R2
  freeze reconstruction-class completeness status

R3
  freeze evidence registry, evidence statuses,
  provenance, time/regime, and required-evidence policy

R4
  freeze forward / observation bridges and versions

R5
  freeze claim-relevant resolution / equivalence /
  temporal / history semantics

R6
  register Formation / Property typed-status handoffs

R7
  register Aggregation / Compression / Transformation
  maps, collision, kernel, injectivity, and support sidecars

R8
  register Tracking / Lineage / transition handoffs when used

R9
  evaluate candidate-evidence pair dispositions

R10
  combine pair dispositions under the frozen evidence policy

R11
  assign reconstruction candidate dispositions

R12
  construct compatible / excluded / blocked /
  conflicting / unresolved candidate sets

R13
  evaluate class-bounded uniqueness

R14
  evaluate collision / injectivity /
  reconstruction-scope and unrecoverability status

R15
  evaluate temporal/history obligations,
  including branch/merge preservation

R16
  apply Tracking / Lineage non-substitution gates

R17
  emit additional-evidence / sidecar handoffs

R18
  apply overall Reconstruction status and task terminal;
  emit protocol-conformance placeholder,
  method-gain placeholder,
  and maximum-supported claim
~~~

No future protocol may silently change R1-R8 after observing candidate outcomes.

## 21. Output contract draft

A future executable run should emit:

~~~text
LOCKED_RECONSTRUCTION_TASK_RECORD

RECONSTRUCTION_CLASS_AND_COMPLETENESS_RECORD

EVIDENCE_REGISTER
EVIDENCE_STATUS_AND_PROVENANCE_LEDGER

FORWARD_OR_OBSERVATION_BRIDGE_REGISTER
PAIR_COMPATIBILITY_MATRIX

RECONSTRUCTION_CANDIDATE_DISPOSITION_LEDGER

COMPATIBLE_RECONSTRUCTION_SET
EXCLUDED_RECONSTRUCTION_SET
BLOCKED_CONFLICTING_OR_UNRESOLVED_SET

RECONSTRUCTION_SET_OUTCOME
UNIQUENESS_SCOPE

COLLISION_FIBER_KERNEL_AND_INJECTIVITY_LEDGER
SUPPORT_STATUS_AND_RELATIONAL_SIDECAR_LEDGER

RECOVERY_AND_UNRECOVERABILITY_RECORD

TEMPORAL_HISTORY_LEDGER_IF_USED
TRACKING_HANDOFF_LEDGER_IF_USED
LINEAGE_HANDOFF_LEDGER_IF_USED

DEFINITIONAL_RECOMPLETION_SIDECAR_IF_USED

ADDITIONAL_EVIDENCE_HANDOFF

RECONSTRUCTION_PRIMARY_STATUS
RECONSTRUCTION_TASK_TERMINAL
RECONSTRUCTION_PROTOCOL_CONFORMANCE
RECONSTRUCTION_METHOD_GAIN_STATUS

MAXIMUM_SUPPORTED_CLAIM
~~~

## 22. Five-interface identity

~~~text
INPUTS:
  declared prior/omitted/damaged/compressed source/history candidates
  available evidence
  typed status/support/provenance
  explicit forward/reduction/transition/observation bridges
  collision/kernel/injectivity sidecars
  resolution/time/history/regime scope
  optional Tracking/Lineage/Measurement handoffs

OPERATION:
  evaluate source/history candidates against frozen evidence
  and forward-interface semantics;
  preserve missing/conflicting/ambiguous states;
  construct admissible reconstruction sets;
  evaluate class-bounded uniqueness;
  characterize information loss under the frozen interface;
  preserve branch/merge multiplicity;
  emit neighboring-method handoffs without substitution

OUTPUTS:
  candidate reconstruction ledger
  admissible/excluded/blocked/conflicting/unresolved sets
  class-bounded uniqueness record
  collision/injectivity/recovery record
  unrecoverable-information sidecar
  temporal/history record
  Tracking/Lineage handoffs
  additional-evidence handoff
  bounded maximum-supported claim

FAILURE_OR_NO_GAIN:
  post-hoc class/scope/bridge changes
  unsupported global historical uniqueness
  unjustified one-preimage selection
  witness-history/temporal-history conflation
  reconstructed-link/established-trace promotion
  reconstructed-candidate/established-lineage promotion
  unavailable-interface/information-loss conflation
  coordinatewise/full-source overpromotion
  typed status/support/provenance collapse
  no claim-relevant gain over fair baseline

VALIDATION_STANDARD:
  every candidate disposition follows from frozen evidence/bridges;
  all retained multiplicity remains visible;
  uniqueness is class/scope bounded;
  information-loss claims have explicit witnesses/conditions;
  typed statuses, support, provenance, and relation semantics remain intact;
  no fabricated evidence/history/trace/lineage;
  external and independent validation remain separate
~~~

## 23. Core draft guards

~~~text
EQUAL_OUTPUT != EQUAL_SOURCE

FORMATION_WITNESS_HISTORY
  !=
ACTUAL_TEMPORAL_HISTORY

STAGE_DEPENDENCY_ORDER
  !=
PHYSICAL_TIME_ORDER

LOSSLESS_ON_DECLARED_CLASS
  !=
GLOBAL_INJECTIVITY

COORDINATEWISE_RECOVERY
  !=
RELATIONAL_OR_FULL_SOURCE_RECOVERY

TRANSITION_COMPATIBILITY
  !=
UNIQUE_PREDECESSOR_HISTORY

RECONSTRUCTION_CANDIDATE
  !=
ESTABLISHED_TRACE_LINK

RECONSTRUCTION_CANDIDATE
  !=
ESTABLISHED_LINEAGE

DEFINITIONAL_RECOMPLETION
  !=
EVIDENCE_BASED_RECONSTRUCTION

MISSING_REQUIRED_RECONSTRUCTION_INFORMATION
  !=
NEGATIVE_EVIDENCE

UNAVAILABLE_REQUIRED_INTERFACE
  !=
DEMONSTRATED_UNRECOVERABILITY

SINGLE_REMAINING_DECLARED_RECONSTRUCTION
  !=
GLOBAL_HISTORICAL_TRUTH

NO_ADMISSIBLE_DECLARED_RECONSTRUCTION
  !=
NO_REAL_PAST_STATE_OR_HISTORY

CURRENT_STATE_DIAGNOSIS
  !=
PAST_OR_OMITTED_RECONSTRUCTION

MULTIPLE_COMPATIBLE
  !=
TASK_UNDERDETERMINED

CANDIDATE_RANKING
  !=
CANDIDATE_ELIMINATION

PROBABILITY
  !=
HISTORICAL_TRUTH
~~~

## 24. Current state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

BOUNDARY_AMENDMENT:
  not established

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
  source_and_interface_recovery

PROTOCOL_REVISION_REQUIRED:
  not applicable

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 25. Next

Freeze this draft as historical development evidence and execute a serious pre-protocol boundary attack.

Boundary review must especially pressure:

~~~text
class completeness
zero / multiple / unique candidate semantics
blocked vs conflicting vs underdetermined
equal-output collisions
class-local vs global injectivity
coordinatewise vs relational/full-source recovery
interface unavailability vs demonstrated information loss
formation witness-history vs temporal history
Tracking inferred link vs established trace
Lineage candidate vs established successor identity
relation-valued transition branching/merging
definitional recompletion boundary
current-state Diagnosis vs past/history Reconstruction
additional-evidence / Measurement / Optimization handoff boundaries
terminal precedence
~~~
