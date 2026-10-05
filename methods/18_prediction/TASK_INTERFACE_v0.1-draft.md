# DSD Prediction — Task Interface v0.1 Draft

Status: **PRE-PROTOCOL HISTORICAL DRAFT — FREEZE ON BOUNDARY-ATTACK START**  
Date: **2026-10-06**  
Method: **Prediction / DSD 예측론**  
Canonical path ID: `18`

Source recovery basis:

~~~text
SOURCE_REGISTRY_COMMIT:
  7c7bc16cf93e756a12688dc5261aecfce5e83533

SOURCE_REGISTRY_BLOB:
  8a93199fdb4abb8c4a4ffbfa0a7ea0f1c3ac34cf
~~~

This file is a prospective Task Interface draft.

It becomes immutable historical evidence when serious pre-protocol boundary attack begins.

It is not yet an executable Prediction standard.

## 1. Atomic task

Given:

~~~text
a frozen issue-time information set
an explicitly declared future target
a target horizon
a model / Simulation handoff
a model-output-to-target domain bridge
target applicability / definedness semantics
uncertainty / scenario / probability semantics when used
an update-version rule
and a declared domain validation standard
~~~

construct and bound:

~~~text
the strongest future-target claim supported at issue time

while preserving:
  information cutoff
  model / bridge / target versions
  uncertainty versus underdetermination
  branch versus probability distinctions
  reduced-readout information loss
  prospective versus retrospective separation
  update / supersession lineage
  later outcome-validation separation
  neighboring-method boundaries
~~~

Prediction does not establish future truth merely because a model trajectory exists.

## 2. Required task identity

Every Prediction task should identify:

~~~text
PREDICTION_TASK_ID
TASK_VERSION

PRIMARY_CLAIM_KIND
MAXIMUM_SUPPORTED_CLAIM

ISSUE_TIME_OR_ISSUE_ORDER
INFORMATION_CUTOFF

ISSUE_INFORMATION_SET_ID
ISSUE_INFORMATION_SET_VERSION
ISSUE_INFORMATION_PROVENANCE
~~~

A claim-relevant change to the issue-time information set requires a new Prediction version or a declared update/supersession relation.

Required guard:

~~~text
NEW_INFORMATION_AFTER_ISSUE
  !=
PERMITTED_ORIGINAL_ISSUE_INPUT
~~~

## 3. Target interface

Freeze:

~~~text
TARGET_ID
TARGET_TYPE
TARGET_DOMAIN
TARGET_VARIABLE_OR_EVENT
TARGET_HORIZON
TARGET_VERIFICATION_TIME_OR_RULE
TARGET_APPLICABILITY_RULE
TARGET_DEFINEDNESS_STATUS
TARGET_PROVENANCE
~~~

Candidate target-definedness states:

~~~text
TARGET_DECLARED_AND_DEFINED
TARGET_DECLARED_BUT_UNAVAILABLE_AT_ISSUE
TARGET_INAPPLICABLE
TARGET_PREREQUISITE_UNSATISFIED
TARGET_APPLICABLE_BUT_UNDEFINED
TARGET_DEFINED_ZERO
TARGET_DEFINED_NONZERO_OR_VALUE
TARGET_CONFLICTING
TARGET_UNDERDETERMINED
TARGET_OUT_OF_SCOPE
~~~

Required guards:

~~~text
UNDEFINED_TARGET != PREDICTED_ZERO
UNAVAILABLE_TARGET_INPUT != NEGATIVE_EVENT
INAPPLICABLE_TARGET != ZERO_VALUE_TARGET
~~~

## 4. Model / Simulation handoff

Freeze:

~~~text
MODEL_OR_SIMULATION_HANDOFF_ID
MODEL_ID
MODEL_VERSION
MODEL_SCOPE
MODEL_VALIDITY_REGION
CURRENT_STATE_INTERFACE
TRAJECTORY_OR_STATE_SET_INTERFACE
TRANSITION_OR_BRANCH_INTERFACE
NUMERICAL_OR_STOCHASTIC_ERROR_INTERFACE
HANDOFF_PROVENANCE
~~~

Prediction may consume:

~~~text
deterministic trajectory
trajectory family
reachable set
interval/enclosure
stochastic sample/ensemble
declared model readout
~~~

Required guards:

~~~text
SIMULATION_TRAJECTORY != PREDICTION_CLAIM
MODEL_CONSISTENT_FUTURE_STATE != FUTURE_WORLD_TRUTH
MODEL_VALIDITY_REGION != TARGET_VALIDITY_REGION_BY_DEFAULT
~~~

## 5. Domain bridge

When model output and target are not definitionally identical, freeze:

~~~text
DOMAIN_BRIDGE_ID
DOMAIN_BRIDGE_VERSION
SOURCE_MODEL_OUTPUT_TYPE
TARGET_TYPE
DOMAIN_BRIDGE_MAP_OR_RELATION
DOMAIN_BRIDGE_SCOPE
DOMAIN_BRIDGE_ASSUMPTIONS
DOMAIN_BRIDGE_UNCERTAINTY
DOMAIN_BRIDGE_PROVENANCE
DOMAIN_BRIDGE_STATUS
~~~

Candidate bridge statuses:

~~~text
DOMAIN_BRIDGE_AVAILABLE
DOMAIN_BRIDGE_UNAVAILABLE
DOMAIN_BRIDGE_CONFLICTING
DOMAIN_BRIDGE_UNDERDETERMINED
DOMAIN_BRIDGE_OUT_OF_SCOPE
~~~

Required guards:

~~~text
MISSING_TARGET_BRIDGE != ZERO_PREDICTION
SIMILAR_VARIABLE_NAME != VALID_DOMAIN_BRIDGE
MODEL_READOUT != TARGET_BY_DEFAULT
~~~

## 6. Primary claim kinds

Freeze exactly one primary claim kind per atomic Prediction obligation:

~~~text
POINT_TARGET_CLAIM
SET_VALUED_TARGET_CLAIM
INTERVAL_TARGET_CLAIM
SCENARIO_CONDITIONAL_TARGET_CLAIM
EVENT_OCCURRENCE_CLAIM
PROBABILISTIC_TARGET_CLAIM
RANKING_OR_ORDERING_CLAIM
TARGET_REACHABILITY_CLAIM
~~~

Each claim kind must declare its semantics.

Examples:

~~~text
POINT_TARGET_CLAIM:
  one target value under declared conditions

INTERVAL_TARGET_CLAIM:
  target lies inside declared interval under declared semantics

SCENARIO_CONDITIONAL_TARGET_CLAIM:
  if scenario condition C_i holds, target claim Y_i applies

PROBABILISTIC_TARGET_CLAIM:
  requires an explicit probability interface
  and cannot be inferred from branch count alone
~~~

## 7. Uncertainty / scenario / probability interface

Freeze, as applicable:

~~~text
UNCERTAINTY_REPRESENTATION
UNCERTAINTY_SCOPE
SCENARIO_SET
SCENARIO_CONDITION_REGISTRY
BRANCH_WEIGHTING_INTERFACE
PROBABILITY_INTERFACE_ID
PROBABILITY_MODEL_VERSION
CALIBRATION_INTERFACE_IF_USED
UNCERTAINTY_PROVENANCE
~~~

Candidate uncertainty categories:

~~~text
DETERMINISTIC_BOUNDED
INTERVAL_OR_SET_UNCERTAINTY
SCENARIO_CONDITIONAL
STOCHASTIC_MODEL_SUPPLIED
EMPIRICAL_PROBABILITY_INTERFACE_SUPPLIED
SEMANTIC_UNDERDETERMINATION
~~~

Required guards:

~~~text
TRAJECTORY_BRANCH != PROBABILITY_MASS_BY_DEFAULT
SCENARIO_SET != PROBABILITY_DISTRIBUTION
UNCERTAINTY != SEMANTIC_UNDERDETERMINATION
FINITE_ENSEMBLE != EXACT_PROBABILITY_LAW
~~~

## 8. Prediction output

Emit:

~~~text
PREDICTION_VERSION
ISSUE_TIME_OR_ISSUE_ORDER
INFORMATION_CUTOFF

TARGET_ID
TARGET_HORIZON
PRIMARY_CLAIM_KIND

PREDICTION_OUTPUT
PREDICTION_SCOPE
PREDICTION_CONDITIONS

UNCERTAINTY_OR_SCENARIO_LEDGER
DOMAIN_BRIDGE_LEDGER

MODEL_OR_SIMULATION_HANDOFF_LEDGER
INFORMATION_CUTOFF_LEDGER

MAXIMUM_SUPPORTED_CLAIM
~~~

No omitted condition may be silently promoted to a universal claim.

## 9. Future-data leakage control

Freeze:

~~~text
ISSUE_INFORMATION_SET
INFORMATION_CUTOFF
POST_ISSUE_DATA_REGISTRY
LEAKAGE_CHECK_RULE
FUTURE_DATA_LEAKAGE_STATUS
~~~

Candidate leakage statuses:

~~~text
NO_FUTURE_DATA_LEAKAGE_FOUND
FUTURE_DATA_LEAKAGE_FOUND
LEAKAGE_CHECK_BLOCKED
LEAKAGE_CHECK_CONFLICTING
LEAKAGE_CHECK_UNDERDETERMINED
LEAKAGE_CHECK_OUT_OF_SCOPE
~~~

Required guards:

~~~text
POST_OUTCOME_INFORMATION
  !=
ORIGINAL_ISSUE_TIME_INPUT

RETROSPECTIVE_FIT
  !=
PROSPECTIVE_PREDICTION_BY_DEFAULT
~~~

A future-data leak invalidates the prospective status of the affected claim.

## 10. Update / supersession interface

When new observations or model revisions arrive after issue time, freeze:

~~~text
UPDATE_EVENT_ID
UPDATE_TRIGGER
NEW_INFORMATION_SET_ID
NEW_INFORMATION_CUTOFF
NEW_MODEL_VERSION_IF_ANY
NEW_DOMAIN_BRIDGE_VERSION_IF_ANY
PREDICTION_VERSION_PARENT
SUPERSESSION_RELATION
UPDATE_PROVENANCE
~~~

Required guards:

~~~text
NEW_OBSERVATION_UPDATE != RETROACTIVE_REWRITE
NEW_MODEL_VERSION != RETROACTIVE_REINTERPRETATION
SUPERSEDED_FORECAST != ERASED_HISTORICAL_FORECAST
~~~

Historical Prediction versions remain immutable issue-time records.

## 11. Post-outcome target verification

Prediction issuance and later outcome validation are separate axes.

Freeze:

~~~text
VALIDATION_STANDARD_ID
VALIDATION_STANDARD_VERSION
VALIDATION_METRIC_OR_RULE
VALIDATION_THRESHOLD_IF_ANY
TARGET_OBSERVATION_ID
TARGET_OBSERVATION_TIME
TARGET_OBSERVATION_PROVENANCE
TARGET_OBSERVATION_STATUS
POST_OUTCOME_VALIDATION_STATUS
VALIDATION_SCORE_OR_RESULT
~~~

Candidate target-observation statuses:

~~~text
TARGET_OBSERVATION_NOT_YET_DUE
TARGET_OBSERVATION_AVAILABLE
TARGET_OBSERVATION_UNAVAILABLE
TARGET_OBSERVATION_CONFLICTING
TARGET_OBSERVATION_UNDERDETERMINED
TARGET_OBSERVATION_OUT_OF_SCOPE
~~~

Candidate validation statuses:

~~~text
PREDICTION_VALIDATION_NOT_YET_DUE
PREDICTION_VALIDATION_PASSED_ON_DECLARED_STANDARD
PREDICTION_VALIDATION_FAILED_ON_DECLARED_STANDARD
PREDICTION_VALIDATION_BLOCKED
PREDICTION_VALIDATION_CONFLICTING
PREDICTION_VALIDATION_UNDERDETERMINED
PREDICTION_VALIDATION_OUT_OF_SCOPE
~~~

Required guards:

~~~text
PREDICTION_ESTABLISHED_AT_ISSUE
  !=
PREDICTION_CORRECT_AFTER_OUTCOME

TARGET_NOT_YET_DUE
  !=
VALIDATION_FAILURE

TARGET_OBSERVATION_UNAVAILABLE
  !=
PREDICTION_MISS

VALIDATION_SCORE
  !=
UNIVERSAL_MODEL_TRUTH
~~~

## 12. Neighboring-method handoffs

Prediction may consume:

~~~text
Simulation trajectories
Measurement observations
Aggregation readouts
Compression representations
Tracking provenance
Lineage identity handoffs
Computation evaluation plans
Optimization model/forecast selection
Audit results
~~~

Prediction does not become those methods by handoff.

Required guards:

~~~text
SIMULATION_TRAJECTORY != PREDICTION_CLAIM
MEASUREMENT_RESULT != PREDICTION_CLAIM
AGGREGATE_READOUT != PREDICTION_TRUTH
COMPRESSED_REPRESENTATION != TARGET_VALIDITY
TRACKING_TRACE != FORECAST_RESULT
LINEAGE_HANDOFF != PREDICTION_RESULT
COMPUTATION_PLAN != PREDICTION_OUTPUT
OPTIMIZATION_SELECTION != PREDICTION_VALIDITY
AUDIT_VERDICT != PREDICTION_OUTPUT

PREDICTION != CONTROL
PREDICTION != OPERATION
~~~

## 13. Prediction primary status

Provisional primary-status family:

~~~text
PREDICTION_ESTABLISHED
PREDICTION_NOT_ESTABLISHED
PREDICTION_BLOCKED
PREDICTION_CONFLICTING
PREDICTION_OUT_OF_SCOPE
PREDICTION_UNDERDETERMINED
~~~

Interpretation:

~~~text
PREDICTION_ESTABLISHED:
  the requested future-target claim is well-formed and supported
  for issuance on the frozen issue-time/model/bridge/horizon scope

PREDICTION_NOT_ESTABLISHED:
  required interfaces are evaluable, but the requested claim
  is not supported on the declared scope

PREDICTION_BLOCKED:
  one or more required in-scope issue/model/bridge/target/
  uncertainty interfaces are unavailable

PREDICTION_CONFLICTING:
  mutually incompatible applicable claim-relevant records remain

PREDICTION_OUT_OF_SCOPE:
  requested operation is not Prediction

PREDICTION_UNDERDETERMINED:
  multiple admissible unresolved claim semantics or model/bridge
  choices yield materially different requested prediction outputs
~~~

Critical guard:

~~~text
PREDICTION_ESTABLISHED
  !=
PREDICTION_VALIDATION_PASSED_ON_DECLARED_STANDARD
~~~

## 14. Task terminal

Provisional task terminals:

~~~text
PREDICTION_TASK_ESTABLISHED
PREDICTION_TASK_PARTIAL
PREDICTION_TASK_NOT_ESTABLISHED
PREDICTION_TASK_BLOCKED
PREDICTION_TASK_CONFLICTING
PREDICTION_TASK_OUT_OF_SCOPE
PREDICTION_TASK_UNDERDETERMINED
~~~

Provisional precedence:

~~~text
PREDICTION_TASK_OUT_OF_SCOPE
>
PREDICTION_TASK_CONFLICTING
>
PREDICTION_TASK_UNDERDETERMINED
>
PREDICTION_TASK_BLOCKED
>
PREDICTION_TASK_ESTABLISHED /
PREDICTION_TASK_PARTIAL /
PREDICTION_TASK_NOT_ESTABLISHED
~~~

Provisional PARTIAL semantics:

~~~text
multiple independently required in-scope Prediction obligations
at least one ESTABLISHED
at least one evaluably NOT_ESTABLISHED
no required obligation BLOCKED
no higher-priority state
~~~

This precedence must be pressure-tested before protocol freeze.

## 15. Protocol-conformance and method-gain candidates

Future executable protocol should distinguish:

~~~text
PREDICTION_PROTOCOL_CONFORMANT
PREDICTION_PROTOCOL_NONCONFORMANT
PREDICTION_PROTOCOL_INDETERMINATE
~~~

Method-gain candidates:

~~~text
PREDICTION_GAIN_ESTABLISHED
PREDICTION_NO_GAIN
PREDICTION_GAIN_NOT_TESTED
PREDICTION_GAIN_BLOCKED
PREDICTION_GAIN_CONFLICTING
PREDICTION_GAIN_UNDERDETERMINED
PREDICTION_GAIN_OUT_OF_SCOPE
~~~

Required guard:

~~~text
PREDICTION_ESTABLISHED may coexist with PREDICTION_NO_GAIN
~~~

## 16. Comparator fairness candidates

When method gain is tested, freeze:

~~~text
COMPARATOR_ID
COMPARATOR_VERSION

COMPARATOR_ISSUE_INFORMATION_EQUIVALENCE
COMPARATOR_INFORMATION_CUTOFF_EQUIVALENCE
COMPARATOR_TARGET_EQUIVALENCE
COMPARATOR_HORIZON_EQUIVALENCE
COMPARATOR_MODEL_INFORMATION_ACCESS
COMPARATOR_DOMAIN_BRIDGE_INFORMATION_ACCESS
COMPARATOR_UNCERTAINTY_INFORMATION_ACCESS
COMPARATOR_VALIDATION_STANDARD_EQUIVALENCE

COMPARATOR_FAIRNESS_STATUS
COMPARATOR_FAIRNESS_PROVENANCE
~~~

A baseline denied target, bridge, or issue-time information available to DSD Prediction is not a fair comparator.

## 17. Direct attack targets before protocol freeze

The serious pre-protocol boundary attack must include at least:

~~~text
A1  post-outcome/future data leaks into issue-time prediction
A2  missing target bridge silently treated as zero prediction
A3  undefined/inapplicable target silently treated as zero
A4  trajectory branch count silently converted to probability mass
A5  scenario set silently converted to probability distribution
A6  uncertainty conflated with semantic underdetermination
A7  Simulation trajectory promoted to future-world truth
A8  newer model version retroactively rewrites old forecast
A9  new observation update retroactively rewrites old forecast
A10 retrospective fit mislabeled as prospective prediction
A11 equal reduced readouts promoted to equal future structural state
A12 target horizon exceeds model/bridge validity region
A13 validation metric/threshold changed after target outcome is known
A14 target observation unavailable treated as hit or miss
A15 Prediction substituted for Control intervention choice
A16 Prediction substituted for Operation live execution
A17 fair competent baseline yields NO_GAIN
A18 terminal precedence / PARTIAL / NOT_YET_DUE validation pressure
~~~

## 18. Five-interface working identity

~~~text
INPUTS:
  issue-time information set
  target/horizon
  model or Simulation handoff
  domain bridge
  uncertainty/scenario/probability semantics
  update/version semantics
  validation standard

OPERATION:
  construct a future-target claim from only the frozen issue-time
  information and supplied bridge/model semantics;
  preserve uncertainty, target definedness, and information cutoff;
  later evaluate the historical claim under the declared
  post-outcome validation standard without rewriting it

OUTPUTS:
  versioned future-target claim
  target/horizon/scope
  uncertainty/scenario/probability ledger
  information-cutoff/leakage ledger
  domain-bridge ledger
  update/supersession ledger
  later validation result
  primary status / task terminal / conformance / method-gain status
  maximum-supported claim

FAILURE_OR_NO_GAIN:
  future-data leakage
  invalid/missing target bridge
  undefined target misuse
  horizon outside validity region
  unsupported probability semantics
  unresolved model/bridge semantics
  retrospective substitution
  neighboring-method substitution
  fair-baseline NO_GAIN

VALIDATION_STANDARD:
  issue-time claim must be derivable only from frozen information
  under the declared model/bridge/horizon semantics;
  later predictive success must be evaluated against the
  separately declared domain validation standard without
  retroactive forecast rewriting
~~~

## 19. Current draft state

~~~text
TASK_INTERFACE_DRAFT:
  v0.1 established

TASK_INTERFACE_STATUS:
  PRE-PROTOCOL HISTORICAL DRAFT

DEDICATED_PREDICTION_PROTOCOL:
  not established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

PREDICTION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_PREDICTION_EVIDENCE_STATUS:
  source_and_interface_recovery
~~~

## 20. Next

Freeze this Task Interface as historical evidence by beginning the serious pre-protocol boundary attack.

The attack must not rewrite this file.
