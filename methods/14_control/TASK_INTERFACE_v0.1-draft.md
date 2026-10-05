# DSD Control — Task Interface v0.1 Draft

Status: **PRE-PROTOCOL HISTORICAL DRAFT**  
Date: **2026-10-06**

~~~text
SOURCE_REGISTRY_COMMIT:
  5a3a124b3e5ff89f36e1ca301f93285eed8fa13f
SOURCE_REGISTRY_BLOB:
  5b4000ccd7a48fd8a537eb15f9efaeaa000813da
~~~

This draft is not yet an executable standard.

## 1. Atomic task

Given a frozen state-information set, target, admissible action set, action-to-state effect interface, constraints, feedback semantics, horizon, stopping rule, and explicit handoffs, determine the supported action or state-dependent policy on the declared scope.

## 2. Required identity

~~~text
CONTROL_TASK_ID
TASK_VERSION
CONTROL_MODE
MAXIMUM_SUPPORTED_CLAIM

DECISION_ORDER
DECISION_INFORMATION_SET_ID
DECISION_INFORMATION_CUTOFF
DECISION_INFORMATION_PROVENANCE
~~~

Candidate modes:

~~~text
ONE_STEP_ACTION
OPEN_LOOP_ACTION_SEQUENCE
FEEDBACK_POLICY
EVENT_TRIGGERED_POLICY
HYBRID_TRANSITION_POLICY
OVERRIDE_POLICY
~~~

## 3. State / target

Freeze:

~~~text
STATE_ID
STATE_VERSION
STATE_CLASS
STATE_OBSERVATION_ID
STATE_DEFINEDNESS_STATUS
STATE_UNCERTAINTY

TARGET_ID
TARGET_TYPE
TARGET_REGION
TARGET_READOUT_IF_USED
TARGET_REACHED_RULE
TARGET_VALIDITY_SCOPE
~~~

Guards:

~~~text
UNAVAILABLE_STATE_INFORMATION != OBSERVED_ZERO
UNDEFINED_STATE != ZERO_STATE
TARGET_DECLARED != TARGET_REACHABLE
TARGET_READOUT_MATCH != FULL_STATE_TARGET_REACHED
~~~

## 4. Action set

Freeze:

~~~text
ACTION_SET_ID
ACTION_SET_VERSION
ACTION_ID_OR_CLASS
ACTION_DOMAIN
ACTION_ADMISSIBILITY_RULE
ACTION_APPLICABILITY_STATUS
ACTION_PREREQUISITES
ACTION_PROVENANCE
~~~

Statuses:

~~~text
ACTION_ADMISSIBLE
ACTION_INADMISSIBLE
ACTION_BLOCKED
ACTION_CONFLICTING
ACTION_UNDERDETERMINED
ACTION_OUT_OF_SCOPE
~~~

Guards:

~~~text
INAPPLICABLE_ACTION != ZERO_ACTION
UNDEFINED_ACTION_PARAMETER != ZERO_PARAMETER
ACTION_EXISTS != ACTION_ADMISSIBLE
~~~

## 5. Action-effect interface

Freeze:

~~~text
ACTION_EFFECT_BRIDGE_ID
ACTION_EFFECT_BRIDGE_VERSION
SOURCE_STATE_ACTION_TYPE
TARGET_STATE_TYPE
ACTION_EFFECT_MODEL_OR_RELATION
ACTION_EFFECT_SCOPE
ACTION_EFFECT_UNCERTAINTY
ACTION_EFFECT_PROVENANCE
ACTION_EFFECT_STATUS
~~~

Guard:

~~~text
MISSING_ACTION_EFFECT_LAW != ZERO_EFFECT
~~~

## 6. Constraint interface

Freeze all required hard and soft constraints and their provenance.

~~~text
CONSTRAINT_REGISTRY
CONSTRAINT_VERSION
HARD_CONSTRAINT_SET
SOFT_CONSTRAINT_SET_IF_SUPPLIED
CONSTRAINT_STATUS
~~~

Guard:

~~~text
HARD_CONSTRAINT != SOFT_PENALTY_BY_DEFAULT
~~~

## 7. Transition / lineage

When an action changes status, domain, support, or formation identity, freeze the corresponding typed transition and any required lineage handoff.

~~~text
REGULAR_VALUE_EVOLUTION != STATUS_OR_DOMAIN_TRANSITION
FORMATION_CHANGE != VALUE_CHANGE_ON_ONE_FIXED_CHANNEL
LINEAGE_HANDOFF != CONTROL_POLICY_SELECTION
~~~

## 8. Policy interface

Freeze:

~~~text
POLICY_ID
POLICY_VERSION
POLICY_DOMAIN
POLICY_MAP_OR_RULE
POLICY_HORIZON
POLICY_TRIGGER_IF_USED
POLICY_STOPPING_RULE
POLICY_PROVENANCE
~~~

Guards:

~~~text
ONE_TIME_ACTION != FEEDBACK_POLICY
OPEN_LOOP_ACTION_SEQUENCE != FEEDBACK_POLICY
ONE_TIME_OPTIMUM != CONTROL_POLICY
SIMULATION_OF_POLICY != POLICY_SELECTION
~~~

## 9. Feedback / update

Freeze:

~~~text
FEEDBACK_INTERFACE_ID
OBSERVATION_UPDATE_RULE
POLICY_UPDATE_RULE
UPDATE_EVENT_ID
PARENT_POLICY_VERSION
NEW_POLICY_VERSION
NEW_INFORMATION_CUTOFF
SUPERSESSION_RELATION
UPDATE_PROVENANCE
~~~

Guard:

~~~text
NEW_OBSERVATION_POLICY_UPDATE != RETROACTIVE_REWRITE
~~~

## 10. Uncertainty / semantic resolution

Freeze:

~~~text
ACTION_EFFECT_UNCERTAINTY_KIND
STATE_UNCERTAINTY_KIND
SEMANTIC_RESOLUTION_STATUS
SEMANTIC_ALTERNATIVE_REGISTRY
~~~

Guard:

~~~text
ACTION_EFFECT_UNCERTAINTY != SEMANTIC_UNDERDETERMINATION
~~~

## 11. Neighboring-method boundaries

~~~text
SIMULATION_OF_POLICY != POLICY_SELECTION
PREDICTION_CLAIM != CONTROL_ACTION
ONE_TIME_OPTIMUM != CONTROL_POLICY
MEASUREMENT_RESULT != CONTROL_DECISION
AGGREGATE_READOUT != FULL_CONTROL_STATE
TRACKING_TRACE != CONTROL_ACTION
LINEAGE_HANDOFF != CONTROL_POLICY
COMPUTATION_PLAN != CONTROL_DECISION
AUDIT_VERDICT != CONTROL_ACTION
CONTROL_POLICY != OPERATION_EXECUTION
~~~

## 12. Provisional primary status

~~~text
CONTROL_ESTABLISHED
CONTROL_NOT_ESTABLISHED
CONTROL_BLOCKED
CONTROL_CONFLICTING
CONTROL_OUT_OF_SCOPE
CONTROL_UNDERDETERMINED
~~~

## 13. Provisional task terminal

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

PARTIAL requires multiple independent required in-scope obligations, at least one ESTABLISHED and at least one evaluably NOT_ESTABLISHED, with no BLOCKED or higher-priority status.

## 14. Conformance / gain

~~~text
CONTROL_PROTOCOL_CONFORMANT
CONTROL_PROTOCOL_NONCONFORMANT
CONTROL_PROTOCOL_INDETERMINATE

CONTROL_GAIN_ESTABLISHED
CONTROL_NO_GAIN
CONTROL_GAIN_NOT_TESTED
CONTROL_GAIN_BLOCKED
CONTROL_GAIN_CONFLICTING
CONTROL_GAIN_UNDERDETERMINED
CONTROL_GAIN_OUT_OF_SCOPE
~~~

~~~text
CONTROL_ESTABLISHED may coexist with CONTROL_NO_GAIN
~~~

## 15. Direct review targets

~~~text
A1 missing effect law treated as zero effect
A2 inapplicable action treated as zero action
A3 prerequisite distinction lost
A4 open-loop sequence mislabeled feedback policy
A5 one-time optimum promoted to policy
A6 Prediction output promoted to action choice
A7 Simulation of supplied policy promoted to policy selection
A8 declared target promoted to reachable target
A9 target readout match promoted to full-state target reached
A10 unavailable state observation treated as zero
A11 effect uncertainty conflated with semantic underdetermination
A12 hard constraint silently softened
A13 required constraint interface silently omitted
A14 typed structural transition hidden as regular value update
A15 lineage requirement ignored across identity-changing transition
A16 policy update retroactively rewrites historical decision basis
A17 fair competent baseline yields NO_GAIN
A18 terminal precedence / PARTIAL pressure
~~~

## 16. Five-interface identity

~~~text
INPUTS:
  state information / target / action set / effect bridge /
  constraints / feedback / horizon

OPERATION:
  select or update an action/policy under supplied interfaces

OUTPUTS:
  action or policy + state/action/effect/constraint/update ledgers +
  status/terminal/conformance/gain + maximum claim

FAILURE_OR_NO_GAIN:
  unavailable/conflicting interfaces, inadmissible action,
  violated required constraints, unresolved semantics,
  unsupported target reach, neighboring-method substitution,
  fair-baseline NO_GAIN

VALIDATION_STANDARD:
  decision follows only frozen state/action/effect/constraint
  interfaces and preserves transition/feedback/target limits
~~~

## 17. Current state

~~~text
TASK_INTERFACE_DRAFT:
  v0.1 established
PRE_PROTOCOL_BOUNDARY_TESTS:
  0
DEDICATED_CONTROL_PROTOCOL:
  not established
CONTROL_INTERNAL_STANDARDIZATION_STATUS:
  developing
CURRENT_CONTROL_EVIDENCE_STATUS:
  source_and_interface_recovery
~~~

## 18. Next

Begin pre-protocol boundary review. The historical Task Interface is not rewritten once review begins.
