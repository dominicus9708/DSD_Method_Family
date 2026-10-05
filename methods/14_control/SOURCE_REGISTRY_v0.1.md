# DSD Control — Source / Registry Recovery v0.1

Status: **SOURCE / REGISTRY RECOVERY COMPLETE — PRE-TASK-INTERFACE**  
Date: **2026-10-06**  
Method: **Control / DSD 제어론**  
Canonical path ID: `14`  
Higher field: **VIII. Dynamics & Action / 동역학·행동**

This document recovers source constraints before Control Task Interface construction.

## 1. Working method identity

~~~text
Control chooses or updates an intervention/action policy
for a declared dynamic state under explicit target,
admissibility, transition, observation, safety, and authority interfaces.

Control does not invent the physical actuator,
domain-specific treatment/action law,
legal authority, safety rule, or optimization objective.
~~~

## 2. Source hierarchy

### C1 — Formation

Recovered constraints:

~~~text
undefined assignment != defined zero
channel absence != zero-valued admitted channel
formation/channel identity is typed
maps act only on declared domains
~~~

Control consequence:

~~~text
unavailable actuator/action assignment != zero action
formation-changing intervention != value update on one fixed channel
~~~

### C2 — Property

Recovered status discipline:

~~~text
applicability
prerequisites
definedness
defined zero
defined nonzero/value
~~~

Control consequence:

~~~text
inapplicable intervention != zero-strength intervention
unsatisfied prerequisite != action failure after execution
undefined effect parameter != zero effect
~~~

### C3 — Static Aggregation

Recovered constraints:

~~~text
aggregate equality != support equality
readout equality != source identity
readout/bridge semantics are downstream supplied structure
~~~

Control consequence:

~~~text
equal observed control readout != equal component state
aggregate target error != full structural target by default
~~~

### C4 — Structural Reorganization Dynamics

Recovered interfaces:

~~~text
instantaneous typed state
regular support signature / epoch
regular evolution law
typed status/domain transition
formation/channel transition
lineage across identity change
constitutive dynamic bridge
optional propagation/locality specialization
~~~

Control consequence:

~~~text
a control action that changes support/status/formation
must use the corresponding typed transition interface

regular-epoch action effect != cross-transition effect by default
~~~

### C5 — Simulation internal-standard handoff

~~~text
Simulation may execute a supplied policy
and return model-consistent controlled trajectories
~~~

Control consequence:

~~~text
SIMULATING_SUPPLIED_CONTROL_POLICY
  !=
CHOOSING_CONTROL_POLICY

simulation success
  !=
control validity
~~~

### C6 — Prediction internal-standard handoff

~~~text
Prediction may supply a future target/risk claim
under frozen issue-time semantics
~~~

Control consequence:

~~~text
PREDICTION_CLAIM != CONTROL_ACTION
forecasted risk != authorized intervention
~~~

### C7 — Optimization internal-standard handoff

~~~text
Optimization may select among alternatives
under explicit objectives and constraints
~~~

Control consequence:

~~~text
ONE_TIME_OPTIMUM != CONTROL_POLICY
OPTIMAL_ACTION_AT_ONE_STATE != CLOSED_LOOP_POLICY
objective/constraint choice is not invented by Control
~~~

### C8 — Measurement / Tracking / Lineage / Audit handoffs

Control may consume:

~~~text
Measurement:
  current-state observation / uncertainty

Tracking:
  action/version/provenance trace

Lineage:
  identity continuity across controlled transitions

Audit:
  conformance/safety/evidence evaluation
~~~

These handoffs do not become Control.

### C9 — shared core

Apply SC-01~SC-10, especially:

~~~text
typed status preservation
source/interface/version locks
explicit cross-structure maps
information-loss limits
regular evolution vs transition vs lineage separation
evaluation/precommit integrity
external-domain validation separation
~~~

## 3. Source-derived Control constraints

~~~text
CR-01
  control task/state/target/action interface versions must be explicit

CR-02
  current state and observation provenance must be frozen per decision step

CR-03
  admissible action set must be supplied or derivable from an explicit external/domain rule

CR-04
  action applicability and prerequisites are distinct from action magnitude

CR-05
  missing action-effect law/bridge != zero effect

CR-06
  an action-to-state transition/effect bridge must be explicit

CR-07
  regular value evolution != status/domain transition != formation transition

CR-08
  successor identity across controlled structural change may require Lineage

CR-09
  supplied target set does not imply target reachability

CR-10
  target readout equality does not imply full-state equality

CR-11
  open-loop action sequence != feedback policy

CR-12
  one-time optimized action != state-dependent Control policy

CR-13
  Prediction risk/forecast != Control decision

CR-14
  Simulation of a supplied policy != Control policy selection

CR-15
  Control policy != live Operation execution

CR-16
  measurement unavailable/undefined != observed zero

CR-17
  action/effect uncertainty != semantic underdetermination

CR-18
  hard safety/authority constraints may not be silently softened

CR-19
  policy update after new observation creates a new decision/policy version
  rather than rewriting the historical action basis

CR-20
  Control validity and method gain versus a competent non-DSD controller
  are separate evidence axes
~~~

## 4. Prospective atomic task

~~~text
Given:
  a frozen current-state information set,
  a declared target or target region,
  an admissible action set,
  action applicability/prerequisites,
  an action-to-state dynamic/effect interface,
  required safety/authority constraints,
  observation/feedback semantics,
  horizon and stopping rules,
  and neighboring-method handoffs,

determine:
  which action or state-dependent policy is supported
  on the declared scope,
  while preserving typed transitions,
  uncertainty/underdetermination,
  safety and authority boundaries,
  versioned feedback updates,
  and neighboring-method separation.
~~~

This is prospective method construction, not a theorem already supplied by predecessor papers.

## 5. Candidate Task Interface fields

~~~text
CONTROL_TASK_ID
TASK_VERSION
CONTROL_MODE

STATE_ID
STATE_VERSION
STATE_OBSERVATION_ID
STATE_OBSERVATION_PROVENANCE
STATE_DEFINEDNESS_STATUS

TARGET_ID
TARGET_TYPE
TARGET_REGION
TARGET_PRIORITY_IF_SUPPLIED

ACTION_SET_ID
ACTION_SET_VERSION
ACTION_ADMISSIBILITY_RULE
ACTION_APPLICABILITY_STATUS
ACTION_PREREQUISITES

ACTION_EFFECT_BRIDGE_ID
ACTION_EFFECT_BRIDGE_VERSION
ACTION_EFFECT_MODEL
ACTION_EFFECT_UNCERTAINTY

SAFETY_CONSTRAINT_REGISTRY
AUTHORITY_CONSTRAINT_REGISTRY
HARD_CONSTRAINT_STATUS

POLICY_ID
POLICY_VERSION
POLICY_DOMAIN
POLICY_MAP_OR_RULE

FEEDBACK_INTERFACE
OBSERVATION_UPDATE_RULE
POLICY_UPDATE_RULE
SUPERSESSION_RELATION

CONTROL_HORIZON
STOPPING_RULE
TARGET_REACHED_RULE

SIMULATION_HANDOFF
PREDICTION_HANDOFF
OPTIMIZATION_HANDOFF
MEASUREMENT_HANDOFF
LINEAGE_HANDOFF

CONTROL_PRIMARY_STATUS
CONTROL_TASK_TERMINAL
CONTROL_PROTOCOL_CONFORMANCE
CONTROL_METHOD_GAIN_STATUS
MAXIMUM_SUPPORTED_CLAIM
~~~

## 6. Candidate Control modes

~~~text
ONE_STEP_INTERVENTION
OPEN_LOOP_ACTION_SEQUENCE
FEEDBACK_POLICY
EVENT_TRIGGERED_POLICY
HYBRID_TRANSITION_POLICY
SAFETY_OVERRIDE_POLICY
~~~

These modes must not be silently identified.

## 7. Core guards to pressure

~~~text
MISSING_ACTION_EFFECT_LAW != ZERO_EFFECT
INAPPLICABLE_ACTION != ZERO_ACTION
UNDEFINED_ACTION_PARAMETER != ZERO_PARAMETER

ONE_TIME_ACTION != FEEDBACK_POLICY
OPEN_LOOP_SEQUENCE != CLOSED_LOOP_POLICY
ONE_TIME_OPTIMUM != CONTROL_POLICY

SIMULATION_OF_POLICY != POLICY_SELECTION
PREDICTION_CLAIM != CONTROL_ACTION
CONTROL_POLICY != OPERATION_EXECUTION

TARGET_DECLARED != TARGET_REACHABLE
TARGET_READOUT_MATCH != FULL_STATE_TARGET_REACHED

MEASUREMENT_UNAVAILABLE != OBSERVED_ZERO

ACTION_EFFECT_UNCERTAINTY != SEMANTIC_UNDERDETERMINATION

HARD_SAFETY_CONSTRAINT != SOFT_PENALTY_BY_DEFAULT

NEW_OBSERVATION_POLICY_UPDATE != RETROACTIVE_REWRITE

CONTROL_ESTABLISHED may coexist with CONTROL_NO_GAIN
~~~

## 8. Initial neighboring-method pressure map

At minimum:

~~~text
Simulation
Prediction
Optimization
Measurement
Aggregation
Tracking
Lineage
Computation
Operation
Audit
~~~

Potential additional pair pressure:

~~~text
Design
Transformation
Specification
~~~

## 9. Recovery state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

SOURCE_DERIVED_CONSTRAINTS:
  CR-01~CR-20

TASK_INTERFACE_DRAFT:
  not established

PRE_PROTOCOL_BOUNDARY_TESTS:
  0

DEDICATED_CONTROL_PROTOCOL:
  not established

DIRECT_CONTROL_PILOTS_ATTEMPTED:
  0

BASELINE_CONTROL_CASES:
  0

NO_GAIN_CONTROL_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_CONTROL_APPLICATIONS:
  0

INDEPENDENT_CONTROL_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

CONTROL_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_CONTROL_EVIDENCE_STATUS:
  source_and_registry_recovery_complete

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 10. Next

Establish the Control planning/worklog lane and draft Control Task Interface v0.1 before serious pre-protocol boundary review.
