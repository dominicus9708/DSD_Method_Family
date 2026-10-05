# DSD Prediction — Protocol v0.1

Status: **EXECUTABLE INTERNAL PROTOCOL — FROZEN FOR DIRECT CHALLENGES**  
Date: **2026-10-06**  
Method: **Prediction / DSD 예측론**

Historical basis:

~~~text
TASK_INTERFACE_COMMIT:
  b5e4004aeb1b90866e17ad0c26ffdba833b0effe
TASK_INTERFACE_BLOB:
  edcafd7e692933a5e02a5384e85cf78553670474

BOUNDARY_STRESS_TEST_COMMIT:
  a1c90a4f6b5500e3dfb23b6dbb7a0b942e3c4121
BOUNDARY_STRESS_TEST_BLOB:
  028eddff450b1bae49176b801cc2b205fab7c173

BOUNDARY_AMENDMENT_001_COMMIT:
  f6df08584c2ec93b654f526b997f6770ff6795ee
BOUNDARY_AMENDMENT_001_BLOB:
  d5ccf44ed1a6db7c466662e4e8253af689428bc6
~~~

## 1. Method identity

Prediction constructs a bounded future-target claim from a frozen issue-time information set, target/horizon, model or Simulation handoff, domain bridge, uncertainty semantics, update/version rules, and domain validation standard.

It does not convert model consistency into future truth by itself.

## 2. Required guards

~~~text
SIMULATION_TRAJECTORY != PREDICTION_CLAIM
MODEL_CONSISTENT_FUTURE_STATE != FUTURE_WORLD_TRUTH
TRAJECTORY_BRANCH != PROBABILITY_MASS_BY_DEFAULT
SCENARIO_SET != PROBABILITY_DISTRIBUTION
UNCERTAINTY != SEMANTIC_UNDERDETERMINATION
MISSING_TARGET_BRIDGE != ZERO_PREDICTION
UNDEFINED_TARGET != PREDICTED_ZERO
ISSUE_TIME_FORECAST != RETROSPECTIVE_FIT
NEW_OBSERVATION_UPDATE != RETROACTIVE_REWRITE
INTERNAL_PROTOCOL_CONFORMANCE != EXTERNAL_PREDICTIVE_VALIDITY
PREDICTION != CONTROL
PREDICTION != OPERATION
PREDICTION != MEASUREMENT
NO_GAIN != METHOD_FAILURE
~~~

## 3. Primary claim kinds

Exactly one per atomic obligation:

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

## 4. Validity gates G1-G18

### G1 — task/version/maximum-claim lock

Freeze:

~~~text
PREDICTION_TASK_ID
TASK_VERSION
PRIMARY_CLAIM_KIND
MAXIMUM_SUPPORTED_CLAIM
CLAIM_MODE
~~~

### G2 — issue-time information lock

Freeze:

~~~text
ISSUE_TIME_OR_ISSUE_ORDER
ISSUE_INFORMATION_SET_ID
ISSUE_INFORMATION_SET_VERSION
ISSUE_INFORMATION_PROVENANCE
INFORMATION_CUTOFF
POST_ISSUE_DATA_REGISTRY
FUTURE_DATA_LEAKAGE_STATUS
~~~

Binding:

~~~text
FUTURE_DATA_LEAKAGE_FOUND
  -> original prospective claim not ESTABLISHED
     under the same Prediction version
~~~

### G3 — target identity/definedness gate

Freeze:

~~~text
TARGET_ID
TARGET_TYPE
TARGET_DOMAIN
TARGET_VARIABLE_OR_EVENT
TARGET_HORIZON
TARGET_APPLICABILITY_RULE
TARGET_DEFINEDNESS_STATUS
TARGET_PROVENANCE
~~~

Bindings:

~~~text
known inapplicability/prerequisite failure -> NOT_ESTABLISHED
required status unavailable -> BLOCKED
conflicting target records -> CONFLICTING
unresolved admissible target semantics -> UNDERDETERMINED
~~~

### G4 — model/Simulation handoff gate

Freeze:

~~~text
MODEL_OR_SIMULATION_HANDOFF_ID
MODEL_ID
MODEL_VERSION
MODEL_SCOPE
CURRENT_STATE_INTERFACE
TRAJECTORY_OR_STATE_SET_INTERFACE
TRANSITION_OR_BRANCH_INTERFACE
HANDOFF_PROVENANCE
~~~

### G5 — domain bridge gate

Freeze:

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

Required in-scope bridge unavailable -> BLOCKED.

### G6 — effective validity-region gate

Freeze:

~~~text
REQUESTED_TARGET_HORIZON
MODEL_VALIDITY_REGION
DOMAIN_BRIDGE_VALIDITY_REGION
UNCERTAINTY_OR_PROBABILITY_VALIDITY_REGION
TARGET_APPLICABILITY_REGION_IF_REQUIRED
EFFECTIVE_PREDICTION_VALIDITY_REGION
~~~

Evaluably outside effective region -> NOT_ESTABLISHED.  
Required validity scope unavailable -> BLOCKED.

### G7 — uncertainty/scenario/probability gate

Freeze:

~~~text
UNCERTAINTY_KIND
UNCERTAINTY_SCOPE
SCENARIO_SET
SCENARIO_CONDITION_REGISTRY
BRANCH_WEIGHTING_INTERFACE
PROBABILITY_INTERFACE_ID
PROBABILITY_MODEL_VERSION
SEMANTIC_RESOLUTION_STATUS
SEMANTIC_ALTERNATIVE_REGISTRY
UNCERTAINTY_PROVENANCE
~~~

Unresolved semantics materially changing the requested output -> UNDERDETERMINED.

### G8 — claim-construction gate

Construct only the frozen claim kind and emit:

~~~text
PREDICTION_VERSION
TARGET_ID
TARGET_HORIZON
PREDICTION_OUTPUT
PREDICTION_SCOPE
PREDICTION_CONDITIONS
UNCERTAINTY_OR_SCENARIO_LEDGER
DOMAIN_BRIDGE_LEDGER
MODEL_HANDOFF_LEDGER
INFORMATION_CUTOFF_LEDGER
MAXIMUM_SUPPORTED_CLAIM
~~~

### G9 — claim-mode / prospective-integrity gate

Allowed claim modes:

~~~text
PROSPECTIVE_ISSUE
RETROSPECTIVE_RECONSTRUCTION
HINDCAST_OR_BACKTEST
POST_OUTCOME_EXPLANATION
~~~

Only PROSPECTIVE_ISSUE supports an original prospective issue-time claim.

### G10 — update/supersession gate

Freeze for every update:

~~~text
UPDATE_EVENT_ID
UPDATE_TRIGGER
PARENT_PREDICTION_VERSION
NEW_PREDICTION_VERSION
NEW_INFORMATION_SET_ID
NEW_INFORMATION_CUTOFF
NEW_MODEL_VERSION_IF_ANY
NEW_DOMAIN_BRIDGE_VERSION_IF_ANY
SUPERSESSION_RELATION
UPDATE_PROVENANCE
~~~

Historical versions remain immutable.

### G11 — readout/information-loss gate

When a reduced predictor/readout is used, freeze its mapping and collision/injectivity sidecars.

~~~text
EQUAL_PREDICTED_READOUT != EQUAL_FUTURE_STATE
REDUCED_READOUT != COMPONENT_RESOLVED_STATE
~~~

### G12 — validation-standard freeze gate

For prospective scoring, freeze before outcome availability:

~~~text
VALIDATION_STANDARD_ID
VALIDATION_STANDARD_VERSION
VALIDATION_METRIC_OR_RULE
VALIDATION_THRESHOLD_IF_ANY
VALIDATION_TARGET_MAPPING
VALIDATION_PRECOMMIT_TIME_OR_ORDER
~~~

A later alternative rule is a new analysis, not a rewrite of the original validation version.

### G13 — target-observation / post-outcome validation gate

Freeze:

~~~text
TARGET_OBSERVATION_ID
TARGET_OBSERVATION_TIME
TARGET_OBSERVATION_PROVENANCE
TARGET_OBSERVATION_STATUS
POST_OUTCOME_VALIDATION_STATUS
VALIDATION_SCORE_OR_RESULT
~~~

Statuses:

~~~text
PREDICTION_VALIDATION_NOT_YET_DUE
PREDICTION_VALIDATION_PASSED_ON_DECLARED_STANDARD
PREDICTION_VALIDATION_FAILED_ON_DECLARED_STANDARD
PREDICTION_VALIDATION_BLOCKED
PREDICTION_VALIDATION_CONFLICTING
PREDICTION_VALIDATION_UNDERDETERMINED
PREDICTION_VALIDATION_OUT_OF_SCOPE
~~~

### G14 — neighboring-method handoff/non-substitution gate

Prediction may consume Simulation, Measurement, Aggregation, Compression, Tracking, Lineage, Computation, Optimization, and Audit handoffs.

But:

~~~text
SIMULATION_TRAJECTORY != PREDICTION_CLAIM
MEASUREMENT_RESULT != PREDICTION_CLAIM
AGGREGATE_READOUT != PREDICTION_TRUTH
COMPUTATION_PLAN != PREDICTION_OUTPUT
OPTIMIZATION_SELECTION != PREDICTION_VALIDITY
PREDICTION != CONTROL
PREDICTION != OPERATION
AUDIT_VERDICT != PREDICTION_OUTPUT
~~~

### G15 — method-gain/comparator-fairness gate

Method gain is separate from Prediction validity.

Statuses:

~~~text
PREDICTION_GAIN_ESTABLISHED
PREDICTION_NO_GAIN
PREDICTION_GAIN_NOT_TESTED
PREDICTION_GAIN_BLOCKED
PREDICTION_GAIN_CONFLICTING
PREDICTION_GAIN_UNDERDETERMINED
PREDICTION_GAIN_OUT_OF_SCOPE
~~~

When tested, freeze equal-information comparator access to issue data, cutoff, target, horizon, model, bridge, uncertainty semantics, and validation standard.

### G16 — primary Prediction status gate

Assign exactly one:

~~~text
PREDICTION_ESTABLISHED
PREDICTION_NOT_ESTABLISHED
PREDICTION_BLOCKED
PREDICTION_CONFLICTING
PREDICTION_OUT_OF_SCOPE
PREDICTION_UNDERDETERMINED
~~~

### G17 — task terminal gate

Assign exactly one:

~~~text
PREDICTION_TASK_ESTABLISHED
PREDICTION_TASK_PARTIAL
PREDICTION_TASK_NOT_ESTABLISHED
PREDICTION_TASK_BLOCKED
PREDICTION_TASK_CONFLICTING
PREDICTION_TASK_OUT_OF_SCOPE
PREDICTION_TASK_UNDERDETERMINED
~~~

Precedence:

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

PARTIAL requires multiple independent required in-scope obligations, at least one ESTABLISHED and at least one evaluably NOT_ESTABLISHED, and no BLOCKED or higher-priority state.

### G18 — conformance / maximum-claim / later-validation separation

Protocol conformance:

~~~text
PREDICTION_PROTOCOL_CONFORMANT
PREDICTION_PROTOCOL_NONCONFORMANT
PREDICTION_PROTOCOL_INDETERMINATE
~~~

Required separation:

~~~text
PREDICTION_TASK_TERMINAL
  !=
POST_OUTCOME_VALIDATION_STATUS

PREDICTION_ESTABLISHED_AT_ISSUE
  !=
PREDICTION_VALIDATION_PASSED_ON_DECLARED_STANDARD
~~~

## 5. Binding operation P1-P18

~~~text
P1  freeze task/version/claim kind
P2  freeze issue information and cutoff
P3  validate target identity/definedness
P4  validate model/Simulation handoff
P5  validate domain bridge
P6  compute effective validity region
P7  validate uncertainty/scenario/probability semantics
P8  check future-data leakage
P9  classify claim mode
P10 construct bounded Prediction claim
P11 record information-loss/readout semantics
P12 freeze update/supersession lineage
P13 freeze validation standard
P14 later ingest target observation without rewriting issue artifact
P15 assign later validation status
P16 preserve neighboring-method boundaries
P17 assign primary Prediction status and task terminal
P18 assign protocol conformance, method-gain status, and maximum claim
~~~

## 6. Current protocol state

~~~text
DEDICATED_PREDICTION_PROTOCOL:
  established v0.1

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  P1-P18

DIRECT_PREDICTION_PILOTS_ATTEMPTED:
  0

PREDICTION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_PREDICTION_EVIDENCE_STATUS:
  protocol_frozen

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 7. Next

Prospectively precommit and execute PRED-CH-001, a positive constructed Prediction challenge.
