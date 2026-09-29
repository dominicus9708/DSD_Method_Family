# DSD Diagnosis — Task Interface v0.1 Draft

Status: **PRE-PROTOCOL HISTORICAL DRAFT — NOT AN EXECUTABLE STANDARD**  
Date: **2026-09-29**  
Method: **Diagnosis / DSD 진단론**  
Legacy path ID: `15A`

Source basis:

~~~text
SOURCE_REGISTRY_v0.1.md
commit:
  63ccc25d5bc8ddadadabfe698852d846e5671f15
blob:
  1152759be5b56462156c83ecd3c508c73f1755f7
~~~

This draft is a prospective method interface built from recovered source constraints.

It is not a theorem of the predecessor papers.

Once direct boundary attack begins, this file must remain immutable historical development evidence. Refinements must be recorded in a separate amendment.

## 1. Atomic task

Working atomic Diagnosis task:

~~~text
Given:
  a declared current-state / failure-mode / cause-hypothesis candidate class,
  present observation/evidence records,
  typed status/applicability/provenance,
  explicit evidence-to-candidate compatibility or forward-model bridges,
  and any claim-relevant resolution / temporal / support /
  residual / transition constraints,

determine:
  which declared candidates remain compatible,
  which are excluded,
  which cannot yet be evaluated,
  which distinctions remain unresolved,
  and which additional observations would discriminate
  the remaining candidates,

without:
  inventing observations,
  silently changing candidate class or bridge semantics,
  selecting one preimage from a noninjective relation without evidence,
  promoting compatibility to causal proof,
  or reconstructing a unique past history unless a separate
  Reconstruction task is supplied.
~~~

## 2. Method boundary

Diagnosis asks:

~~~text
Which declared current hidden states / failure modes /
cause hypotheses / structural conditions remain compatible
with the frozen present evidence?
~~~

It does not by itself answer:

~~~text
Which measurement should be built or executed?
What result was experimentally observed?
What unique past history occurred?
What future state will occur?
What control action should be selected?
Which candidate is optimal?
Is a cause proven?
~~~

Working distinctions:

~~~text
MEASUREMENT:
  discrimination adequacy of observations/readouts

DIAGNOSIS:
  evidence compatibility of current-state/cause candidates

RECONSTRUCTION:
  prior / omitted structure or history compatibility

PREDICTION:
  future consequence under supplied state/model

SIMULATION:
  execution of supplied dynamic model

OPTIMIZATION:
  selection according to declared objective

AUDIT:
  conformance/evidence/process evaluation
~~~

## 3. Primary claim levels

A task freezes one primary claim level.

~~~text
CANDIDATE_COMPATIBILITY_SET

UNIQUE_WITHIN_DECLARED_CANDIDATE_CLASS

CURRENT_STATE_OR_CONDITION_IDENTIFICATION

FAILURE_MODE_IDENTIFICATION

CAUSE_COMPATIBILITY_ONLY

CAUSE_IDENTIFICATION_WITH_SUPPLIED_CAUSAL_BRIDGE
~~~

Interpretation:

~~~text
CANDIDATE_COMPATIBILITY_SET:
  determine compatible / excluded / unevaluable candidates
  without requiring uniqueness

UNIQUE_WITHIN_DECLARED_CANDIDATE_CLASS:
  evaluate whether exactly one declared candidate remains compatible
  after every claim-relevant candidate is evaluable under frozen semantics

CURRENT_STATE_OR_CONDITION_IDENTIFICATION:
  candidate identity is a current state/condition rather than only a cause label

FAILURE_MODE_IDENTIFICATION:
  candidate identity is a declared present failure-mode class

CAUSE_COMPATIBILITY_ONLY:
  determine compatibility of cause hypotheses;
  no causal certainty is claimed

CAUSE_IDENTIFICATION_WITH_SUPPLIED_CAUSAL_BRIDGE:
  requires an explicit causal bridge and its validity scope;
  compatibility alone is insufficient
~~~

No claim level implies global exhaustiveness unless candidate-class completeness is separately supplied and valid for the declared scope.

## 4. Required task lock

Every future executable Diagnosis task should freeze at least:

~~~text
DIAGNOSIS_TASK_ID
TASK_VERSION

PRIMARY_CLAIM_LEVEL
DIAGNOSIS_QUESTION

CANDIDATE_CLASS_ID
CANDIDATE_CLASS_VERSION_OR_DEFINITION
CANDIDATE_IDENTITIES
CANDIDATE_CLASS_COMPLETENESS_STATUS

EVIDENCE_SET_ID
EVIDENCE_RECORDS
EVIDENCE_PROVENANCE
EVIDENCE_STATUS_RECORDS
REQUIRED_EVIDENCE_POLICY

EVIDENCE_TO_CANDIDATE_BRIDGE_ID
BRIDGE_VERSION_OR_DEFINITION
BRIDGE_APPLICABILITY_SCOPE

DIAGNOSIS_RESOLUTION_OR_EQUIVALENCE_RULE
TEMPORAL_SCOPE
ACTIVE_REGIME_OR_SCHEMA

MAXIMUM_SUPPORTED_CLAIM
~~~

Conditionally required when claim-relevant:

~~~text
FORMATION_STATUS_HANDOFF
PROPERTY_STATUS_HANDOFF

MEASUREMENT_HANDOFF
MEASUREMENT_DECISION_RULE_VERSION

SUPPORT_RETENTION_HANDOFF
AGGREGATION_OR_COMPRESSION_LOSS_HANDOFF
INJECTIVITY_OR_COLLISION_RECORD

RESIDUAL_TARGET_ID
RESIDUAL_CARRIER
RESIDUAL_RULE

TRANSITION_CONSTRAINT_ID
TRANSITION_RELATION_VERSION
DYNAMIC_SUPPORT_HANDOFF

CAUSE_CLAIM_SCOPE
CAUSAL_BRIDGE_ID
CAUSAL_BRIDGE_VERSION
CAUSAL_BRIDGE_VALIDITY_SCOPE

ADDITIONAL_OBSERVATION_HANDOFF_POLICY
~~~

Changing a claim-relevant lock after seeing the candidate disposition opens a new task version.

## 5. Candidate-class completeness status

Working status family:

~~~text
CANDIDATE_CLASS_DECLARED_BOUNDED
CANDIDATE_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE
CANDIDATE_CLASS_COMPLETENESS_UNDERDETERMINED
CANDIDATE_CLASS_COMPLETENESS_NOT_CLAIMED
~~~

Core draft guard:

~~~text
ONE_SURVIVING_DECLARED_CANDIDATE
  !=
ONE_POSSIBLE_REAL_STATE
~~~

A `CANDIDATE_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE` record is itself a supplied claim/handoff and must retain provenance.

Diagnosis does not manufacture candidate-class completeness.

## 6. Evidence record

Every claim-relevant observation/evidence item should retain:

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
~~~

## 7. Evidence-to-candidate bridge

For candidate `h` and evidence item `e`, an explicit supplied bridge determines whether the candidate predicts, permits, excludes, or cannot yet evaluate the evidence under the frozen semantics.

The draft does not require the bridge to be numeric.

Allowed bridge forms may include:

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

Draft pair disposition:

~~~text
PAIR_COMPATIBLE

PAIR_INCOMPATIBLE

PAIR_BLOCKED

PAIR_OUT_OF_SCOPE

PAIR_UNDERDETERMINED
~~~

A future boundary review must determine whether a separate `PAIR_CONFLICTING` state is necessary or whether conflict belongs only at the task/rule layer.

## 8. Candidate disposition

For each declared candidate `h`, working status family:

~~~text
DIAGNOSIS_CANDIDATE_COMPATIBLE

DIAGNOSIS_CANDIDATE_EXCLUDED

DIAGNOSIS_CANDIDATE_BLOCKED

DIAGNOSIS_CANDIDATE_OUT_OF_SCOPE

DIAGNOSIS_CANDIDATE_UNDERDETERMINED
~~~

Working interpretation:

~~~text
COMPATIBLE:
  every required evaluable evidence relation is compatible
  under the frozen combination policy

EXCLUDED:
  the frozen exclusion rule is triggered by at least one
  valid claim-relevant incompatible evidence relation

BLOCKED:
  a required evidence/bridge/prerequisite is unavailable,
  so candidate disposition cannot be completed

OUT_OF_SCOPE:
  candidate or required relation lies outside the declared task scope

UNDERDETERMINED:
  multiple admissible bridge/rule/scope interpretations
  yield different candidate dispositions and no resolver is frozen
~~~

The boundary attack must pressure whether evidence conflict and candidate conflict require separate statuses.

## 9. Candidate-set outcome / identifiability record

After candidate-level evaluation, record one working set outcome:

~~~text
DIAGNOSIS_SET_MULTIPLE_COMPATIBLE

DIAGNOSIS_SET_UNIQUE_WITHIN_DECLARED_CLASS

DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS

DIAGNOSIS_SET_PARTIALLY_EVALUATED

DIAGNOSIS_SET_UNDERDETERMINED
~~~

These are not truth labels.

Core guards:

~~~text
MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED

NONE_COMPATIBLE_IN_DECLARED_CLASS
  !=
NO_REAL_STATE_EXISTS

UNIQUE_WITHIN_DECLARED_CLASS
  !=
GLOBAL_UNIQUE_DIAGNOSIS
~~~

A fully frozen task may legitimately produce `MULTIPLE_COMPATIBLE` as an established Diagnosis result.

## 10. Residual discipline

If residual evidence is used, freeze:

~~~text
RESIDUAL_TARGET_ID
RESIDUAL_TARGET_VERSION_OR_DEFINITION
RESIDUAL_CARRIER
RESIDUAL_RULE
RESIDUAL_THRESHOLD_OR_EQUIVALENCE_RULE
~~~

The residual operation must match its carrier.

~~~text
SCALAR_SUBTRACTION
  is not a universal residual operation

RESIDUAL_ZERO
  !=
SOURCE_STATE_IDENTITY

RESIDUAL_MATCH
  !=
CAUSE_ESTABLISHED
~~~

## 11. Dynamic / transition discipline

If current-state candidates are constrained dynamically, freeze:

~~~text
TEMPORAL_SCOPE
ACTIVE_REGIME
TRANSITION_RELATION_ID
TRANSITION_RELATION_VERSION
DYNAMIC_SUPPORT_STATUS
LINEAGE_OR_SUCCESSION_HANDOFF_IF_USED
~~~

A relation-valued transition may preserve several admissible current states.

~~~text
TRANSITION_COMPATIBILITY != UNIQUE_SUCCESSOR
TEMPORAL_ORDER != CAUSAL_PROOF
DYNAMIC_SUPPORT_AVAILABILITY != CAUSAL_SUFFICIENCY
~~~

Diagnosis may use transition constraints on the current candidate set.

It must not silently reconstruct a unique predecessor history.

## 12. Readout / information-loss discipline

When evidence uses an aggregate, compression, projection, or reduced readout, record:

~~~text
READOUT_OR_REDUCTION_ID
READOUT_VERSION
COLLISION_STATUS
INJECTIVITY_SCOPE
SUPPORT_RETENTION_STATUS
RECONSTRUCTION_SCOPE
REQUIRED_SIDECARS
~~~

Draft guards:

~~~text
EQUAL_AGGREGATE != EQUAL_CURRENT_STATE
PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY
REDUCED_READOUT != COMPLETE_DIAGNOSTIC_CLASSIFIER
LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
NONINJECTIVE_FORWARD_MAP != LICENSE_TO_SELECT_ONE_PREIMAGE
~~~

## 13. Cause-claim discipline

Cause-hypothesis compatibility may be evaluated as Diagnosis.

Causal identification requires an explicit supplied causal bridge and its scope.

Working cause status family:

~~~text
CAUSE_NOT_CLAIMED
CAUSE_COMPATIBILITY_ONLY
CAUSE_BRIDGE_BLOCKED
CAUSE_BRIDGE_UNDERDETERMINED
CAUSE_IDENTIFICATION_ESTABLISHED_ON_DECLARED_MODEL
CAUSE_IDENTIFICATION_NOT_ESTABLISHED
~~~

Core draft guard:

~~~text
DIAGNOSTIC_COMPATIBILITY != CAUSAL_PROOF
CORRELATION != CAUSAL_BRIDGE
RESIDUAL_MATCH != CAUSAL_BRIDGE
TEMPORAL_PRECEDENCE != CAUSAL_BRIDGE
~~~

The phrase `CAUSE_IDENTIFICATION_ESTABLISHED_ON_DECLARED_MODEL` is intentionally model-scoped and must not be read as unrestricted real-world causal proof.

## 14. Additional-observation handoff

Diagnosis may identify remaining candidate distinctions that present evidence does not resolve.

It may emit:

~~~text
UNRESOLVED_CANDIDATE_PAIR_OR_CLASS
REQUIRED_DISTINCTION
MISSING_EVIDENCE_ROLE
POSSIBLE_MEASUREMENT_HANDOFF
~~~

But:

~~~text
NEED_FOR_ADDITIONAL_OBSERVATION
  !=
OPTIMAL_MEASUREMENT_SELECTED

DIAGNOSIS_DISCRIMINATOR_REQUIREMENT
  !=
MEASUREMENT_PLAN_EXECUTION
~~~

Selection or optimization of the next measurement remains a neighboring task unless explicitly handed off.

## 15. Working primary Diagnosis status

Overall claim status family:

~~~text
DIAGNOSIS_ESTABLISHED
DIAGNOSIS_NOT_ESTABLISHED
DIAGNOSIS_BLOCKED
DIAGNOSIS_CONFLICTING
DIAGNOSIS_OUT_OF_SCOPE
DIAGNOSIS_UNDERDETERMINED
~~~

Interpretation:

~~~text
ESTABLISHED:
  requested claim level is supported by a complete evaluation
  of the required declared candidate/evidence obligations

NOT_ESTABLISHED:
  all required claim-evaluation information is present,
  but the requested claim level fails evaluably

BLOCKED:
  required evidence/bridge/prerequisite is unavailable

CONFLICTING:
  frozen claim-relevant task/rule records are mutually incompatible
  and no declared precedence resolves them

OUT_OF_SCOPE:
  the requested operation is not a Diagnosis task
  or lies outside the declared candidate/bridge scope

UNDERDETERMINED:
  multiple admissible claim-relevant semantics remain
  and yield different overall results
~~~

Important:

~~~text
MULTIPLE_COMPATIBLE
  may coexist with
DIAGNOSIS_ESTABLISHED

when the primary claim level is:
  CANDIDATE_COMPATIBILITY_SET
~~~

## 16. Working task terminal

The future protocol is expected to emit exactly one task terminal:

~~~text
DIAGNOSIS_TASK_ESTABLISHED

DIAGNOSIS_TASK_PARTIAL

DIAGNOSIS_TASK_NOT_ESTABLISHED

DIAGNOSIS_TASK_BLOCKED

DIAGNOSIS_TASK_CONFLICTING

DIAGNOSIS_TASK_OUT_OF_SCOPE

DIAGNOSIS_TASK_UNDERDETERMINED
~~~

Draft meaning of `PARTIAL`:

~~~text
multiple independently required diagnosis obligations exist,
at least one is validly established,
at least one is validly not established or unevaluable,
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

## 17. Binding-operation draft

Working operation:

~~~text
D1
  freeze task identity, claim level, candidate class, scope, and maximum claim

D2
  freeze evidence registry, evidence status, provenance, time/regime,
  and required-evidence policy

D3
  freeze evidence-to-candidate bridges and versions

D4
  freeze claim-relevant resolution / equivalence / threshold semantics

D5
  register Formation / Property / Measurement /
  support-retention / reduction-loss handoffs when used

D6
  register residual and transition constraints when used

D7
  evaluate candidate-evidence pair dispositions

D8
  combine pair dispositions under the frozen required-evidence policy

D9
  assign candidate dispositions

D10
  construct compatible / excluded / blocked / unresolved candidate sets

D11
  evaluate candidate-set identifiability within the declared class

D12
  apply cause-claim gate when a causal claim is requested

D13
  record remaining discriminator / additional-observation handoff

D14
  apply overall Diagnosis status and task terminal

D15
  emit protocol-conformance placeholder and maximum-supported claim
~~~

No future protocol may silently change D1-D6 after observing candidate outcomes.

## 18. Output contract draft

A future executable run should emit:

~~~text
LOCKED_DIAGNOSIS_TASK_RECORD

CANDIDATE_CLASS_AND_COMPLETENESS_RECORD

EVIDENCE_REGISTER
EVIDENCE_STATUS_AND_PROVENANCE_LEDGER

BRIDGE_REGISTER
PAIR_COMPATIBILITY_MATRIX

CANDIDATE_DISPOSITION_LEDGER

COMPATIBLE_CANDIDATE_SET
EXCLUDED_CANDIDATE_SET
BLOCKED_OR_UNRESOLVED_CANDIDATE_SET

DIAGNOSIS_SET_OUTCOME
IDENTIFIABILITY_SCOPE

READOUT_COLLISION_AND_INFORMATION_LOSS_LEDGER
RESIDUAL_LEDGER_IF_USED
TEMPORAL_TRANSITION_LEDGER_IF_USED

CAUSE_CLAIM_RECORD

ADDITIONAL_OBSERVATION_HANDOFF

DIAGNOSIS_PRIMARY_STATUS
DIAGNOSIS_TASK_TERMINAL
DIAGNOSIS_PROTOCOL_CONFORMANCE
DIAGNOSIS_METHOD_GAIN_STATUS

MAXIMUM_SUPPORTED_CLAIM
~~~

## 19. Five-interface identity

~~~text
INPUTS:
  declared candidates
  present evidence
  typed status/provenance
  explicit compatibility/forward bridges
  resolution/time/regime
  optional residual/transition/readout/cause handoffs

OPERATION:
  evaluate candidate-evidence compatibility under frozen semantics;
  preserve missing/conflicting/ambiguous states;
  construct admissible candidate sets;
  evaluate declared-class identifiability;
  gate uniqueness and causal claims

OUTPUTS:
  candidate compatibility ledger
  admissible/excluded/blocked/unresolved sets
  identifiability record
  remaining discriminator handoff
  cause-claim record
  bounded maximum claim

FAILURE_OR_NO_GAIN:
  required evidence/bridge unavailable
  frozen rule conflict
  unresolved competing semantics
  unsupported uniqueness/causal promotion
  hidden neighboring-method substitution
  no claim-relevant gain over fair baseline

VALIDATION_STANDARD:
  every candidate disposition follows from frozen evidence/bridges;
  typed statuses and provenance retained;
  multiplicity preserved when warranted;
  information-loss limits retained;
  no fabricated observation/history/causal proof;
  claims remain candidate-class and scope bounded
~~~

## 20. Core draft guards

~~~text
OBSERVATION_COMPATIBLE != TRUE_STATE_ESTABLISHED

SINGLE_REMAINING_DECLARED_CANDIDATE
  !=
GLOBAL_UNIQUE_DIAGNOSIS

NO_ADMISSIBLE_DECLARED_CANDIDATE
  !=
NO_REAL_STATE_EXISTS

DIAGNOSTIC_COMPATIBILITY != CAUSAL_PROOF

RESIDUAL_MATCH != CAUSE_ESTABLISHED

MEASUREMENT_SUFFICIENCY != DIAGNOSIS

EQUAL_READOUT != EQUAL_HIDDEN_STATE

NONINJECTIVE_FORWARD_MAP
  !=
LICENSE_TO_SELECT_ONE_PREIMAGE

MISSING_REQUIRED_EVIDENCE
  !=
NEGATIVE_EVIDENCE

CURRENT_STATE_DIAGNOSIS
  !=
PAST_HISTORY_RECONSTRUCTION

CANDIDATE_RANKING
  !=
CANDIDATE_ELIMINATION

PROBABILITY
  !=
COMPATIBILITY

MULTIPLE_COMPATIBLE
  !=
TASK_UNDERDETERMINED
~~~

## 21. Current state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

BOUNDARY_AMENDMENT:
  not established

DEDICATED_DIAGNOSIS_PROTOCOL:
  not established

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
  source_and_interface_recovery

PROTOCOL_REVISION_REQUIRED:
  not applicable

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 22. Next

Freeze this draft as historical development evidence and execute a serious pre-protocol boundary attack.

Boundary review must especially pressure:

~~~text
candidate-class completeness
zero/multiple/unique candidate semantics
blocked vs underdetermined vs conflicting
evidence conflict vs model mismatch
cause compatibility vs causal proof
noninjective readout/forward map
current-state Diagnosis vs history Reconstruction
Measurement / Optimization handoff boundaries
probabilistic/ranking requests
terminal precedence
~~~
