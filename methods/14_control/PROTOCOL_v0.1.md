# DSD Control — Protocol v0.1

Status: **EXECUTABLE INTERNAL PROTOCOL — FROZEN FOR DIRECT CHALLENGES**  
Date: **2026-10-06**  
Method: **Control / DSD 제어론**

Historical basis:

~~~text
SOURCE_REGISTRY_COMMIT:
  5a3a124b3e5ff89f36e1ca301f93285eed8fa13f
SOURCE_REGISTRY_BLOB:
  5b4000ccd7a48fd8a537eb15f9efaeaa000813da

TASK_INTERFACE_COMMIT:
  5a8d11191f0a76b0223a68155e34d8700927a651
TASK_INTERFACE_BLOB:
  037a03e6249b835d479e4498869a28cd7293838a

BOUNDARY_REVIEW_COMMIT:
  a74f3d6c663b6c26ed1c46909c9fa629a9adf394
BOUNDARY_REVIEW_BLOB:
  c9efeaeb76f612e1b757bff04d74205633a62532

BOUNDARY_AMENDMENT_001_COMMIT:
  09488d68b3777841ab9ea261278b6d83e7f0a48c
BOUNDARY_AMENDMENT_001_BLOB:
  6245048c4fb91df0292adb78b2d9277124a23603
~~~

## 1. Method identity

Control selects or updates an intervention/action policy from a frozen state-information set, target, action set, action-effect interface, constraints, feedback semantics, horizon, and explicit neighboring-method handoffs.

It does not invent physical actuators, domain authority, safety rules, target desirability, or universal objectives.

## 2. Core guards

~~~text
MISSING_ACTION_EFFECT_LAW != ZERO_EFFECT
INAPPLICABLE_ACTION != ZERO_ACTION
ONE_TIME_ACTION != FEEDBACK_POLICY
OPEN_LOOP_ACTION_SEQUENCE != FEEDBACK_POLICY
ONE_TIME_OPTIMUM != CONTROL_POLICY
SIMULATION_OF_POLICY != POLICY_SELECTION
PREDICTION_CLAIM != CONTROL_ACTION
CONTROL_POLICY != OPERATION_EXECUTION
TARGET_DECLARED != TARGET_REACHABLE
TARGET_READOUT_MATCH != FULL_STATE_TARGET_REACHED
MEASUREMENT_UNAVAILABLE != OBSERVED_ZERO
ACTION_EFFECT_UNCERTAINTY != SEMANTIC_UNDERDETERMINATION
HARD_CONSTRAINT != SOFT_PENALTY_BY_DEFAULT
NEW_OBSERVATION_POLICY_UPDATE != RETROACTIVE_REWRITE
CONTROL_ESTABLISHED may coexist with CONTROL_NO_GAIN
~~~

## 3. Control modes

Exactly one primary mode per atomic obligation:

~~~text
ONE_STEP_ACTION
OPEN_LOOP_ACTION_SEQUENCE
FEEDBACK_POLICY
EVENT_TRIGGERED_POLICY
HYBRID_TRANSITION_POLICY
OVERRIDE_POLICY
~~~

## 4. Validity gates G1-G18

### G1 — task/version/mode/maximum-claim lock

Freeze task ID, version, control mode, primary claim, and maximum-supported claim.

### G2 — decision-information/state gate

Freeze:

~~~text
DECISION_ORDER
DECISION_INFORMATION_SET_ID
DECISION_INFORMATION_CUTOFF
STATE_ID
STATE_VERSION
STATE_CLASS
STATE_OBSERVATION_ID
STATE_OBSERVATION_STATUS
STATE_UNCERTAINTY
~~~

Required observation unavailable -> BLOCKED.  
Known invalid required observation -> NOT_ESTABLISHED.  
Conflicting records -> CONFLICTING.  
Unresolved admissible semantics -> UNDERDETERMINED.

### G3 — target gate

Freeze:

~~~text
TARGET_ID
TARGET_TYPE
TARGET_REGION
TARGET_READOUT_IF_USED
TARGET_REACHED_RULE
TARGET_VALIDITY_SCOPE
~~~

Target declaration alone does not establish reachability.

### G4 — target-reachability evidence gate

Freeze:

~~~text
TARGET_REACHABILITY_INTERFACE
TARGET_REACHABILITY_STATUS
TARGET_REACH_SCOPE
TARGET_REACH_PROVENANCE
~~~

Required guards:

~~~text
TARGET_DECLARED != TARGET_REACHABLE
ONE_SIMULATED_SUCCESS != UNIVERSAL_TARGET_REACHABILITY
~~~

### G5 — action-set/status gate

Freeze action-set identity/version, action domain, admissibility rule, applicability status, and provenance.

Bindings:

~~~text
known inadmissible/inapplicable action -> CONTROL_NOT_ESTABLISHED
required action-status interface unavailable -> CONTROL_BLOCKED
conflicting applicable action records -> CONTROL_CONFLICTING
unresolved admissible action semantics -> CONTROL_UNDERDETERMINED
~~~

### G6 — action-prerequisite gate

Freeze prerequisite identity, requiredness, satisfaction/evaluation status, and provenance.

Known unsatisfied required prerequisite -> NOT_ESTABLISHED.  
Unavailable check -> BLOCKED.  
Conflict -> CONFLICTING.  
Unresolved semantics -> UNDERDETERMINED.

### G7 — action-effect bridge gate

Freeze:

~~~text
ACTION_EFFECT_BRIDGE_ID
ACTION_EFFECT_BRIDGE_VERSION
ACTION_EFFECT_MODEL_OR_RELATION
ACTION_EFFECT_SCOPE
ACTION_EFFECT_UNCERTAINTY
ACTION_EFFECT_STATUS
ACTION_EFFECT_PROVENANCE
~~~

Missing required bridge -> BLOCKED.

### G8 — constraint and authority gate

Freeze required:

~~~text
CONSTRAINT_REGISTRY
CONSTRAINT_VERSION
HARD_CONSTRAINT_SET
SOFT_CONSTRAINT_SET_IF_SUPPLIED
REQUIRED_CONSTRAINT_COMPONENTS
CONSTRAINT_COMPLETENESS_STATUS
AUTHORITY_CONSTRAINT_REGISTRY_IF_USED
~~~

Missing required component -> BLOCKED.

### G9 — explicit constraint-transformation gate

Any hard-to-soft or other constraint transformation must freeze source, target, scope, rule, authorization, and provenance.

Unregistered transformation cannot change admissibility.

### G10 — transition/lineage gate

When the intervention changes status, domain, support, or formation identity, freeze typed transition and required lineage handoff.

~~~text
REGULAR_VALUE_EVOLUTION != STATUS_OR_DOMAIN_TRANSITION
FORMATION_CHANGE != VALUE_CHANGE_ON_ONE_FIXED_CHANNEL
LINEAGE_HANDOFF != CONTROL_POLICY_SELECTION
~~~

### G11 — policy semantics gate

Freeze policy ID/version/domain/map or rule, horizon, trigger, stopping rule, and provenance.

~~~text
ONE_TIME_ACTION != FEEDBACK_POLICY
OPEN_LOOP_ACTION_SEQUENCE != FEEDBACK_POLICY
ONE_TIME_OPTIMUM != CONTROL_POLICY
~~~

### G12 — feedback/update gate

Freeze feedback interface, observation-update rule, policy-update rule, parent/new policy version, information cutoff, supersession relation, and provenance.

Historical decision versions remain immutable.

### G13 — uncertainty/semantic-resolution gate

Freeze uncertainty kind/scope and semantic alternatives.

Declared action-effect uncertainty may remain inside a supported claim.  
Unresolved semantics producing materially different decisions -> UNDERDETERMINED.

### G14 — target-readout/information-loss gate

If a reduced readout is used, freeze map, collision/injectivity scope, and target sufficiency rule.

~~~text
TARGET_READOUT_MATCH != FULL_STATE_TARGET_REACHED
EQUAL_CONTROL_READOUT != EQUAL_COMPONENT_STATE
~~~

### G15 — neighboring-method handoff/non-substitution gate

Control may consume Simulation, Prediction, Optimization, Measurement, Aggregation, Tracking, Lineage, Computation, Operation, and Audit handoffs.

But:

~~~text
SIMULATION_OF_POLICY != POLICY_SELECTION
PREDICTION_CLAIM != CONTROL_ACTION
ONE_TIME_OPTIMUM != CONTROL_POLICY
MEASUREMENT_RESULT != CONTROL_DECISION
AGGREGATE_READOUT != FULL_CONTROL_STATE
TRACKING_TRACE != CONTROL_ACTION
LINEAGE_HANDOFF != CONTROL_POLICY
COMPUTATION_PLAN != CONTROL_DECISION
CONTROL_POLICY != OPERATION_EXECUTION
AUDIT_VERDICT != CONTROL_ACTION
~~~

### G16 — method-gain/comparator-fairness gate

Statuses:

~~~text
CONTROL_GAIN_ESTABLISHED
CONTROL_NO_GAIN
CONTROL_GAIN_NOT_TESTED
CONTROL_GAIN_BLOCKED
CONTROL_GAIN_CONFLICTING
CONTROL_GAIN_UNDERDETERMINED
CONTROL_GAIN_OUT_OF_SCOPE
~~~

When tested, comparator access to state, target, action set, effect model, constraints, feedback, and horizon must be equivalent.

### G17 — primary Control status gate

Assign exactly one:

~~~text
CONTROL_ESTABLISHED
CONTROL_NOT_ESTABLISHED
CONTROL_BLOCKED
CONTROL_CONFLICTING
CONTROL_OUT_OF_SCOPE
CONTROL_UNDERDETERMINED
~~~

### G18 — task terminal/conformance/maximum-claim gate

Task terminals:

~~~text
CONTROL_TASK_ESTABLISHED
CONTROL_TASK_PARTIAL
CONTROL_TASK_NOT_ESTABLISHED
CONTROL_TASK_BLOCKED
CONTROL_TASK_CONFLICTING
CONTROL_TASK_OUT_OF_SCOPE
CONTROL_TASK_UNDERDETERMINED
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

PARTIAL requires multiple independent required in-scope obligations, at least one ESTABLISHED and at least one evaluably NOT_ESTABLISHED, with no BLOCKED or higher-priority state.

Protocol conformance:

~~~text
CONTROL_PROTOCOL_CONFORMANT
CONTROL_PROTOCOL_NONCONFORMANT
CONTROL_PROTOCOL_INDETERMINATE
~~~

## 5. Binding operation C1-C18

~~~text
C1  freeze task/version/mode/max claim
C2  freeze decision information/state observation
C3  freeze target and target criterion
C4  validate target-reachability interface
C5  validate action set/admissibility
C6  validate prerequisites
C7  validate action-effect bridge
C8  validate required constraints/authority
C9  validate explicit constraint transformations
C10 validate typed transition/lineage obligations
C11 freeze policy semantics
C12 freeze feedback/update lineage
C13 separate uncertainty from semantic underdetermination
C14 validate reduced readout sufficiency if used
C15 preserve neighboring-method handoffs
C16 assess comparator fairness/method gain if requested
C17 assign primary Control status
C18 assign task terminal, conformance, and maximum claim
~~~

## 6. Current state

~~~text
DEDICATED_CONTROL_PROTOCOL:
  established v0.1
VALIDITY_GATES:
  G1-G18
BINDING_OPERATION:
  C1-C18
DIRECT_CONTROL_PILOTS_ATTEMPTED:
  0
CONTROL_INTERNAL_STANDARDIZATION_STATUS:
  developing
CURRENT_CONTROL_EVIDENCE_STATUS:
  protocol_frozen
PROTOCOL_REVISION_REQUIRED:
  no
SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 7. Next

Prospectively precommit and execute `CTRL-CH-001`, the positive constructed Control challenge.
