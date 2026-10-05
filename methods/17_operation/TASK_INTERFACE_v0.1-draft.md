# DSD Operation — Task Interface v0.1 Draft

Status: **PRE-PROTOCOL HISTORICAL DRAFT**  
Date: **2026-10-06**

~~~text
SOURCE_REGISTRY_COMMIT:
  73e007bbce27fbcd241b413908aeac22eff32e90
SOURCE_REGISTRY_BLOB:
  ed4fa251935919513f8b14fe8c868ef781c4a4d8
~~~

This draft is not an executable standard.

## 1. Atomic task

Given a frozen lifecycle state, procedure/version, readiness/prerequisite criteria, actor/resource registry, monitoring interfaces, method handoffs, handoff criteria, retry/recovery/escalation/stop rules, authority/safety constraints, and update semantics, determine the supported operational step or transition on the declared scope.

## 2. Required identity

~~~text
OPERATION_TASK_ID
TASK_VERSION
OPERATION_MODE
MAXIMUM_SUPPORTED_CLAIM

LIFECYCLE_ID
LIFECYCLE_VERSION
OPERATIONAL_STATE_ID
OPERATIONAL_STATE_VERSION
DECISION_INFORMATION_CUTOFF
~~~

Candidate modes:

~~~text
ONE_SHOT_PROCEDURE
REPEATED_CYCLE
LIFECYCLE_ORCHESTRATION
EVENT_TRIGGERED_HANDOFF
RECOVERY_OR_ESCALATION
CONTROLLED_SHUTDOWN
~~~

## 3. Procedure / readiness

Freeze:

~~~text
PROCEDURE_ID
PROCEDURE_VERSION
PROCEDURE_SCOPE
PROCEDURE_STEP_ID

READINESS_CRITERIA
READINESS_STATUS
PREREQUISITE_REGISTRY
PREREQUISITE_STATUS
~~~

Guards:

~~~text
PROCEDURE_SPECIFICATION != PROCEDURE_EXECUTION
NOT_READY != READY_WITH_ZERO_WORK
PREREQUISITE_UNSATISFIED != EXECUTION_FAILURE
~~~

## 4. Actors / resources

Freeze:

~~~text
ACTOR_ROLE_REGISTRY
ACTOR_AVAILABILITY_STATUS
RESOURCE_REGISTRY
RESOURCE_AVAILABILITY_STATUS
RESOURCE_PROVENANCE
~~~

Guards:

~~~text
MISSING_ACTOR != IDLE_ACTOR
MISSING_RESOURCE != ZERO_LOAD
~~~

## 5. Monitoring

Freeze:

~~~text
MONITORING_INTERFACE_ID
MONITORING_INTERFACE_VERSION
MONITORING_STATUS
OBSERVATION_ID
OBSERVATION_DEFINEDNESS
OBSERVATION_PROVENANCE
~~~

Guard:

~~~text
UNAVAILABLE_MONITOR != OBSERVED_ZERO
~~~

## 6. Handoff

Freeze:

~~~text
HANDOFF_ID
HANDOFF_SOURCE
HANDOFF_TARGET
HANDOFF_TRIGGER
HANDOFF_ACCEPTANCE_RULE
HANDOFF_STATUS
HANDOFF_PROVENANCE
~~~

Guards:

~~~text
HANDOFF_TRIGGERED != HANDOFF_ACCEPTED
SOURCE_STEP_COMPLETE != TARGET_READY_BY_DEFAULT
~~~

## 7. Retry / recovery / escalation / stop

Freeze separate rules:

~~~text
RETRY_RULE
RECOVERY_RULE
ESCALATION_RULE
STOP_RULE
RULE_PRECEDENCE_IF_NEEDED
~~~

Guards:

~~~text
RETRY != RECOVERY
RECOVERY != ESCALATION
ESCALATION != STOP
~~~

## 8. Authority / safety / governance

Freeze required external interfaces:

~~~text
AUTHORITY_INTERFACE
SAFETY_CONSTRAINT_REGISTRY
GOVERNANCE_INTERFACE_IF_USED
REQUIRED_AUTHORITY_COMPONENTS
REQUIRED_SAFETY_COMPONENTS
COMPLETENESS_STATUS
~~~

Operation does not invent missing authority or safety rules.

## 9. Transition / lineage

When status, domain, support, or formation identity changes, freeze typed transition and any required lineage handoff.

~~~text
REGULAR_EXECUTION != STATUS_OR_DOMAIN_TRANSITION
FORMATION_CHANGE != ORDINARY_OPERATIONAL_VALUE_UPDATE
LINEAGE_HANDOFF != OPERATION_HANDOFF_RULE
~~~

## 10. Method handoffs

~~~text
CONTROL_HANDOFF
PREDICTION_HANDOFF
SIMULATION_HANDOFF
MEASUREMENT_HANDOFF
TRACKING_HANDOFF
LINEAGE_HANDOFF
OPTIMIZATION_HANDOFF
COMPUTATION_HANDOFF
SPECIFICATION_HANDOFF
DESIGN_HANDOFF
AUDIT_HANDOFF
~~~

Guards:

~~~text
CONTROL_POLICY != OPERATION_EXECUTION
PREDICTION_CLAIM != OPERATION_DECISION
SIMULATION_TRAJECTORY != LIVE_EXECUTION_RECORD
MEASUREMENT_RESULT != OPERATION_ACTION
TRACKING_TRACE != OPERATION_DECISION
OPTIMIZATION_SELECTION != OPERATION_EXECUTION
COMPUTATION_PLAN != OPERATION_COMPLETION
SPECIFICATION_RULE != EXECUTION_RECORD
DESIGN_PLAN != OPERATION_STATE
AUDIT_VERDICT != OPERATION_ACTION
~~~

## 11. Reduced readout / dashboard

Freeze:

~~~text
DASHBOARD_OR_READOUT_ID
READOUT_MAP
READOUT_SCOPE
READOUT_SUFFICIENCY_RULE
READOUT_COLLISION_STATUS
~~~

Guard:

~~~text
DASHBOARD_EQUALITY != FULL_OPERATIONAL_STATE_EQUALITY
~~~

## 12. Update / version history

Freeze:

~~~text
UPDATE_EVENT_ID
PARENT_OPERATION_VERSION
NEW_OPERATION_VERSION
NEW_INFORMATION_CUTOFF
SUPERSESSION_RELATION
UPDATE_PROVENANCE
~~~

Guard:

~~~text
NEW_OPERATION_UPDATE != RETROACTIVE_REWRITE
~~~

## 13. Provisional primary status

~~~text
OPERATION_ESTABLISHED
OPERATION_NOT_ESTABLISHED
OPERATION_BLOCKED
OPERATION_CONFLICTING
OPERATION_OUT_OF_SCOPE
OPERATION_UNDERDETERMINED
~~~

## 14. Provisional task terminal

~~~text
OPERATION_TASK_ESTABLISHED
OPERATION_TASK_PARTIAL
OPERATION_TASK_NOT_ESTABLISHED
OPERATION_TASK_BLOCKED
OPERATION_TASK_CONFLICTING
OPERATION_TASK_OUT_OF_SCOPE
OPERATION_TASK_UNDERDETERMINED
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

## 15. Conformance / gain

~~~text
OPERATION_PROTOCOL_CONFORMANT
OPERATION_PROTOCOL_NONCONFORMANT
OPERATION_PROTOCOL_INDETERMINATE

OPERATION_GAIN_ESTABLISHED
OPERATION_NO_GAIN
OPERATION_GAIN_NOT_TESTED
OPERATION_GAIN_BLOCKED
OPERATION_GAIN_CONFLICTING
OPERATION_GAIN_UNDERDETERMINED
OPERATION_GAIN_OUT_OF_SCOPE
~~~

~~~text
OPERATION_ESTABLISHED may coexist with OPERATION_NO_GAIN
~~~

## 16. Direct review targets

~~~text
A1 missing resource treated as zero load
A2 not-ready treated as ready-with-zero-work
A3 unavailable monitor treated as observed zero
A4 procedure specification promoted to execution
A5 Simulation trajectory promoted to live execution record
A6 Control policy promoted to Operation execution
A7 Prediction claim promoted to Operation decision
A8 Measurement result promoted to Operation action
A9 handoff trigger promoted to accepted handoff
A10 source completion promoted to target readiness
A11 retry/recovery/escalation/stop collapsed
A12 one-shot procedure promoted to repeated cycle
A13 dashboard equality promoted to full-state equality
A14 typed structural transition hidden as regular execution
A15 required lineage ignored across identity change
A16 operation update retroactively rewrites historical basis
A17 fair competent baseline yields NO_GAIN
A18 terminal precedence / PARTIAL pressure
~~~

## 17. Five-interface identity

~~~text
INPUTS:
  lifecycle state / procedure / readiness / actors/resources /
  monitoring / handoffs / exception rules / authority-safety /
  neighboring-method inputs

OPERATION:
  coordinate the supported live/repeated operational transition,
  handoff, retry, recovery, escalation, or stop

OUTPUTS:
  operational decision/transition + execution/handoff ledger +
  monitoring/re-audit triggers + statuses/terminal/conformance/gain

FAILURE_OR_NO_GAIN:
  missing/conflicting required interfaces, not-ready state,
  unavailable resources, unresolved handoff/exception semantics,
  unsupported authority/safety, neighboring-method substitution,
  fair-baseline NO_GAIN

VALIDATION_STANDARD:
  decision follows only frozen lifecycle/procedure/readiness/resource/
  monitoring/handoff/authority interfaces and preserves
  transition/lineage/readout/version limits
~~~

## 18. Current state

~~~text
TASK_INTERFACE_DRAFT:
  v0.1 established
PRE_PROTOCOL_BOUNDARY_TESTS:
  0
DEDICATED_OPERATION_PROTOCOL:
  not established
OPERATION_INTERNAL_STANDARDIZATION_STATUS:
  developing
CURRENT_OPERATION_EVIDENCE_STATUS:
  source_and_interface_recovery
~~~

## 19. Next

Begin serious pre-protocol boundary review. The historical Task Interface is not rewritten once review begins.
