# DSD Simulation — Task Interface v0.1 Draft

Status: **PRE-PROTOCOL HISTORICAL DRAFT — NOT AN EXECUTABLE STANDARD**  
Date: **2026-10-05**  
Method: **Simulation / DSD 시뮬레이션론**  
Legacy path ID: `13`  
Higher field: **VIII. Dynamics & Action / 동역학·행동**

Source basis:

~~~text
SOURCE_REGISTRY_v0.1.md
commit:
  8c3879f211d1a024ba903273044e099f7ad7041d
blob:
  a19a771215c0d63144bf613ff3ca6c3a9163151e
~~~

This draft is prospective method construction from recovered source constraints.

It is not a theorem of the predecessor papers.

Once serious direct boundary attack begins, this file becomes immutable historical development evidence. Any refinement after that point must be recorded in a separate amendment rather than by rewriting this draft.

## 1. Atomic task

Working atomic Simulation task:

~~~text
Given:
  a declared simulation task,
  one or more admissible initial state(s) or an initial-state class,
  a frozen source/model/interface version,
  a declared time or ordered-step domain,
  a declared component-resolved state representation,
  a regular support signature for each regular epoch,
  supplied regular evolution law(s),
  supplied transition relation(s) whenever the support signature
  or formation background changes,
  explicit constitutive / cross-layer bridges when required,
  explicit lineage when successor identity is claimed,
  declared solver / symbolic / stochastic execution semantics,
  declared approximation / error semantics when used,
  declared readout maps,
  and stopping / termination rules,

generate or enumerate:
  model-consistent trajectory segment(s),
  regular epochs,
  typed transition events,
  admissible post-transition states,
  lineage records,
  fixed-time static-compatible slices,
  declared readout histories,
  and the maximum Simulation claim justified by the supplied model,

without:
  inventing missing evolution or transition laws,
  replacing missing/undefined states by numerical zero,
  rewriting identity-changing transitions as ordinary value evolution,
  asserting uniqueness from a relation-valued transition,
  inferring full state from lossy readouts,
  turning a numerical approximation into an exact trajectory without
  the required error/convergence interface,
  or promoting model consistency to Prediction truth.
~~~

## 2. Method boundary

Simulation asks:

~~~text
What trajectory or trajectory family does the declared model
generate on the frozen simulation scope?
~~~

It does not by itself answer:

~~~text
Will an external future target actually occur?
Which intervention policy should be chosen?
How should a live process be operated or monitored?
Which sufficient solver plan is cheapest?
What must be evaluated before execution?
What observation was measured?
What aggregate/compressed representation should be produced?
Whether the simulation satisfies an external scientific standard?
~~~

Working distinctions:

~~~text
SIMULATION:
  generate model-consistent state evolution

PREDICTION:
  assert future-target relevance

CONTROL:
  choose state-dependent interventions

OPERATION:
  manage repeated live lifecycle / execution / monitoring

COMPUTATION:
  determine required evaluation / sound omission / reuse

OPTIMIZATION:
  choose among admissible alternatives under objectives

MEASUREMENT:
  acquire / discriminate evidence

AUDIT:
  evaluate conformance / evidence / procedure
~~~

## 3. Primary claim levels

A task freezes one primary claim level:

~~~text
ADMISSIBLE_TRAJECTORY_EXISTENCE_WITNESS

DECLARED_TRAJECTORY_ON_FIXED_HORIZON

TRAJECTORY_FAMILY_ON_DECLARED_BRANCHING_MODEL

HYBRID_REGULAR_TRANSITION_TRAJECTORY

DECLARED_READOUT_HISTORY

APPROXIMATE_TRAJECTORY_WITH_DECLARED_ERROR

REACHABLE_STATE_SET_ON_DECLARED_HORIZON
~~~

Interpretation:

~~~text
ADMISSIBLE_TRAJECTORY_EXISTENCE_WITNESS:
  generate at least one trajectory satisfying the frozen model;
  no uniqueness claim follows

DECLARED_TRAJECTORY_ON_FIXED_HORIZON:
  generate the trajectory when the supplied model/initial state
  and execution semantics support the requested determinacy

TRAJECTORY_FAMILY_ON_DECLARED_BRANCHING_MODEL:
  retain every branch required by the frozen relation-valued model
  on the declared bounded scope

HYBRID_REGULAR_TRANSITION_TRAJECTORY:
  combine regular epochs with typed transition relations
  and required lineage records

DECLARED_READOUT_HISTORY:
  generate a frozen readout history from component-resolved states
  without identifying the readout with the complete state

APPROXIMATE_TRAJECTORY_WITH_DECLARED_ERROR:
  generate an approximate trajectory and explicit error /
  acceptance evidence sufficient for the frozen claim

REACHABLE_STATE_SET_ON_DECLARED_HORIZON:
  generate or characterize the model-reachable state set
  on the declared bounded horizon
~~~

No claim level automatically implies:

~~~text
global uniqueness
external future truth
model correctness
empirical calibration
control optimality
operational success
unbounded-time behavior
~~~

## 4. Required task lock

Every future executable Simulation task should freeze at least:

~~~text
SIMULATION_TASK_ID
TASK_VERSION

PRIMARY_CLAIM_LEVEL
MAXIMUM_SUPPORTED_CLAIM

SOURCE_MODEL_ID
SOURCE_MODEL_VERSION
ACTIVE_DSD_LAYERS

TIME_OR_STEP_DOMAIN
TIME_METRIC_STATUS
SIMULATION_HORIZON

INITIAL_STATE_CLASS_ID
INITIAL_STATE_ID_OR_SET
INITIAL_STATE_VERSION
INITIAL_STATE_ADMISSIBILITY

STATE_CLASS_ID
STATE_REPRESENTATION_MODE
COMPONENT_REGISTRY

REGULAR_SUPPORT_SIGNATURE_ID
REGULAR_SUPPORT_SIGNATURE_VERSION

EVOLUTION_LAW_ID
EVOLUTION_LAW_VERSION_OR_DEFINITION
EVOLUTION_LAW_DOMAIN
EVOLUTION_LAW_PROVENANCE

SIMULATION_MODE

TERMINATION_RULE
STOPPING_CONDITION
~~~

Conditionally required when claim-relevant:

~~~text
PROPERTY_STATUS_HANDOFF
CHANNEL_REGISTRY
STATIC_AGGREGATION_HANDOFF

CONSTITUTIVE_BRIDGE_REGISTRY
DEPENDENCY_OR_COUPLING_INTERFACE

TRANSITION_RELATION_ID
TRANSITION_RELATION_VERSION
TRANSITION_TRIGGER
PRE_TRANSITION_STATE_CLASS
POST_TRANSITION_STATE_CLASS
TRANSITION_BALANCE_RULE

LINEAGE_INTERFACE_ID
LINEAGE_REQUIREMENT
LINEAGE_VALIDITY_SCOPE

SOLVER_OR_EXECUTION_INTERFACE
SOLVER_VERSION

RANDOM_SEED_OR_SAMPLE_RULE
STOCHASTIC_PROCESS_INTERFACE
DISTRIBUTIONAL_CLAIM_INTERFACE

APPROXIMATION_RULE
ERROR_METRIC
ERROR_BOUND
CONVERGENCE_OR_STABILITY_INTERFACE
ACCEPTANCE_THRESHOLD

READOUT_REGISTRY
READOUT_COLLISION_OR_INJECTIVITY_HANDOFF

LOCALITY_OR_PROPAGATION_HANDOFF
~~~

Changing a claim-relevant lock after seeing trajectory outputs opens a new task version.

## 5. Initial-state and state-class discipline

Working initial-state status:

~~~text
INITIAL_STATE_ADMISSIBLE
INITIAL_STATE_INADMISSIBLE
INITIAL_STATE_BLOCKED
INITIAL_STATE_CONFLICTING
INITIAL_STATE_UNDERDETERMINED
INITIAL_STATE_OUT_OF_SCOPE
~~~

A valid initial state must satisfy every predecessor interface actually used by the chosen model.

Draft guards:

~~~text
INITIAL_STATE_VALUE_PRESENT
  !=
INITIAL_STATE_ADMISSIBLE

MISSING_OPTIONAL_INTERFACE
  !=
ZERO_OBJECT

UNDEFINED_PROPERTY_STATE
  !=
DEFINED_ZERO_STATE
~~~

An inadmissible initial state does not become admissible because a numerical solver accepts its vector representation.

## 6. Regular support signature and epoch discipline

Freeze one regular support signature for every regular epoch.

Working epoch record:

~~~text
REGULAR_EPOCH_ID
TIME_OR_STEP_SUBDOMAIN
FORMATION_BACKGROUND_ID
REGULAR_SUPPORT_SIGNATURE_ID
COMPONENT_TYPES
PROPERTY_STATUS_PARTITION_IF_USED
ANALYTIC_CARRIER_TYPES_IF_USED
GEOMETRIC_SPECIALIZATION_IF_USED
~~~

Draft guards:

~~~text
VALUE_CHANGE_WITHIN_Q
  !=
CHANGE_OF_Q

REGULAR_EPOCH
  !=
GLOBAL_TRAJECTORY_WITHOUT_TRANSITIONS

STATUS_OR_DOMAIN_CHANGE_INVALIDATING_Q
  !=
REGULAR_VALUE_EVOLUTION

FORMATION_BACKGROUND_CHANGE
  !=
REGULAR_VALUE_EVOLUTION
~~~

## 7. Evolution-law interface

Every claim-relevant regular evolution law records:

~~~text
EVOLUTION_LAW_ID
EVOLUTION_LAW_VERSION_OR_DEFINITION
EVOLUTION_LAW_DOMAIN
STATE_VARIABLES_ACTED_ON
TIME_OR_STEP_SEMANTICS
DETERMINISTIC_OR_RELATIONAL_STATUS
REGULARITY_ASSUMPTIONS
BOUNDARY_OR_INITIAL_CONDITIONS_IF_REQUIRED
PROVENANCE
~~~

Working law status:

~~~text
EVOLUTION_LAW_AVAILABLE
EVOLUTION_LAW_UNAVAILABLE
EVOLUTION_LAW_CONFLICTING
EVOLUTION_LAW_UNDERDETERMINED
EVOLUTION_LAW_OUT_OF_SCOPE
~~~

Draft guards:

~~~text
MISSING_EVOLUTION_LAW
  !=
ZERO_DYNAMICS

MODEL_LABEL
  !=
EVOLUTION_OPERATOR

PROPERTY_LABEL
  !=
DYNAMIC_COEFFICIENT
~~~

## 8. Constitutive and cross-layer bridge discipline

Whenever Formation, Property, Aggregation, geometric, measured, or other records become dynamic operator inputs, freeze:

~~~text
BRIDGE_ID
BRIDGE_VERSION_OR_DEFINITION
SOURCE_LAYER
SOURCE_RECORD_SCOPE
TARGET_DYNAMIC_OPERATOR
BRIDGE_ASSUMPTIONS
BRIDGE_PROVENANCE
BRIDGE_VALIDITY_SCOPE
~~~

Draft guards:

~~~text
PROPERTY_NAME
  !=
CONSTITUTIVE_COEFFICIENT

AGGREGATE_READOUT
  !=
COMPONENT_DYNAMIC_STATE

STATIC_ASSOCIATION
  !=
DYNAMIC_CAUSAL_OPERATOR
~~~

## 9. Regular trajectory semantics

Working regular-trajectory result:

~~~text
REGULAR_TRAJECTORY_ESTABLISHED
REGULAR_TRAJECTORY_NOT_ESTABLISHED
REGULAR_TRAJECTORY_BLOCKED
REGULAR_TRAJECTORY_CONFLICTING
REGULAR_TRAJECTORY_UNDERDETERMINED
REGULAR_TRAJECTORY_OUT_OF_SCOPE
~~~

A trajectory witness may satisfy an existential claim without satisfying a uniqueness claim.

Draft guards:

~~~text
ONE_ADMISSIBLE_TRAJECTORY
  !=
UNIQUE_TRAJECTORY

DETERMINISTIC_EXECUTION_RESULT
  !=
THEOREM_OF_UNIQUE_MODEL_SOLUTION
  unless uniqueness is supplied/proved for the declared model

SOLVER_RETURNED_A_PATH
  !=
PATH_IS_ADMISSIBLE
~~~

## 10. Transition relation

When a regular support signature or formation background changes, freeze:

~~~text
TRANSITION_RELATION_ID
TRANSITION_RELATION_VERSION
TRANSITION_TRIGGER
PRE_TRANSITION_STATE_CLASS
POST_TRANSITION_STATE_CLASS
TRANSITION_RELATION
TRANSITION_DETERMINISM_STATUS
TRANSITION_BALANCE_RULE_IF_CLAIMED
TRANSITION_PROVENANCE
~~~

Working transition status:

~~~text
TRANSITION_ESTABLISHED
TRANSITION_NOT_ESTABLISHED
TRANSITION_BLOCKED
TRANSITION_CONFLICTING
TRANSITION_UNDERDETERMINED
TRANSITION_OUT_OF_SCOPE
~~~

Draft guards:

~~~text
RELATION_VALUED_TRANSITION
  !=
DETERMINISTIC_JUMP_MAP

MULTIPLE_DECLARED_SUCCESSORS
  !=
UNDERDETERMINED_BY_DEFAULT

BRANCHING_MODEL
  !=
SIMULATION_FAILURE

REGULAR_EPOCH_CONSERVATION
  !=
TRANSITION_CONSERVATION
~~~

A declared branching relation may validly produce a trajectory family.

## 11. Lineage discipline

When successor identity is claim-relevant across a transition, freeze:

~~~text
LINEAGE_INTERFACE_ID
LINEAGE_VERSION
PRE_COMPONENT_SET
POST_COMPONENT_SET
CHANNEL_LINEAGE_RELATION
COMPONENT_LINEAGE_RELATION
IDENTITY_BEARING_COMPONENT_FAMILY
LINEAGE_VALIDITY_SCOPE
~~~

Draft guards:

~~~text
SAME_LABEL_AFTER_TRANSITION
  !=
SAME_FORMATION_OBJECT

READOUT_CONTINUITY
  !=
LINEAGE_CONTINUITY

AGGREGATE_EQUALITY
  !=
SUCCESSOR_IDENTITY

BRANCHING_LINEAGE
  !=
BIJECTIVE_LINEAGE
~~~

## 12. Static-slice compatibility

Every generated trajectory slice used in a claim must remain compatible with the predecessor interfaces actually activated.

Working check:

~~~text
FORMATION_SLICE_VALID
PROPERTY_SLICE_VALID_IF_USED
STATIC_ANALYTIC_SLICE_VALID_IF_USED
SPECIALIZATION_SLICE_VALID_IF_USED
STATIC_READOUT_COMPATIBLE_IF_USED
~~~

Draft guards:

~~~text
VALID_FIXED_TIME_SLICE
  !=
VALID_EVOLUTION_LAW

STATIC_READOUT_MATCH
  !=
DYNAMIC_STATE_IDENTITY
~~~

A dynamic result may not repair an invalid predecessor slice retroactively.

## 13. Numerical / symbolic / stochastic execution semantics

Working simulation modes:

~~~text
CONTINUOUS_ANALYTIC
DISCRETE_STEP
EVENT_DRIVEN
SYMBOLIC
STOCHASTIC_SAMPLE_PATH
STOCHASTIC_ENSEMBLE
HYBRID
EXTERNALLY_SUPPLIED_SOLVER
~~~

When approximate execution is used, freeze:

~~~text
SOLVER_OR_EXECUTION_INTERFACE
SOLVER_VERSION
DISCRETIZATION_OR_APPROXIMATION_RULE
ERROR_METRIC
LOCAL_ERROR_BOUND_IF_USED
GLOBAL_OR_END_TO_END_ERROR_BOUND_IF_USED
CONVERGENCE_OR_STABILITY_INTERFACE
ACCEPTANCE_THRESHOLD
~~~

Draft guards:

~~~text
NUMERICAL_TRAJECTORY
  !=
EXACT_TRAJECTORY

LOCAL_ERROR_CONTROL
  !=
GLOBAL_TRAJECTORY_ERROR_BOUND

SOLVER_CONVERGENCE
  !=
EMPIRICAL_MODEL_VALIDITY

ONE_STOCHASTIC_SAMPLE_PATH
  !=
DISTRIBUTIONAL_CLAIM

FINITE_SAMPLE_ENSEMBLE
  !=
EXACT_PROBABILITY_LAW
~~~

## 14. Readout / aggregation / information-loss discipline

If a reduced readout is used, freeze:

~~~text
READOUT_ID
READOUT_VERSION_OR_DEFINITION
READOUT_DOMAIN
READOUT_CODOMAIN
COLLISION_STATUS
INJECTIVITY_SCOPE
SUPPORT_RETENTION_STATUS
READOUT_VALIDITY_SCOPE
~~~

Draft guards:

~~~text
READOUT_HISTORY
  !=
COMPONENT_RESOLVED_TRAJECTORY

EQUAL_READOUT_HISTORY
  !=
EQUAL_TRAJECTORY

READOUT_FRONT
  !=
COMPONENT_INFORMATION_FRONT

REDUCED_TRAJECTORY_MATCH
  !=
LINEAGE_IDENTITY
~~~

## 15. Propagation / locality specialization

A finite propagation result may be consumed only when the exact specialization assumptions are supplied:

~~~text
LOCALIZATION_CARRIER
PROPAGATION_METRIC
METRIC_TIME_SCALE
DISCREPANCY_CONVENTION
EVOLUTION_LAW
REGULARITY_ASSUMPTIONS
PROPAGATION_BOUND
SUPPORT_FAITHFULNESS_STATUS
~~~

Draft guards:

~~~text
C_INFO
  !=
UNIVERSAL_DSD_CONSTANT

FINITE_PROPAGATION_SPECIALIZATION
  !=
GENERAL_SIMULATION_RULE

PROJECTED_FRONT_SPEED
  !=
COMPONENT_FRONT_SPEED_BY_DEFAULT
~~~

## 16. Conservation / residual / target semantics

If conservation, balance, equilibrium, closure, or target-reaching claims are used, freeze the exact target relation and carrier.

~~~text
CONSERVATION_ID
CONSERVATION_SCOPE
BALANCE_RULE
TARGET_RELATION
RESIDUAL_CARRIER
RESIDUAL_RULE
TARGET_REACHED_RULE
~~~

Draft guards:

~~~text
REGULAR_EPOCH_CONSERVATION
  !=
CROSS_TRANSITION_CONSERVATION

SMALL_SCALAR_RESIDUAL
  !=
STRUCTURAL_TARGET_REACHED

TARGET_REACHED_IN_READOUT
  !=
TARGET_REACHED_IN_FULL_STATE
~~~

## 17. Simulation vs Prediction boundary

~~~text
SIMULATION:
  model-consistent trajectory claim

PREDICTION:
  future-target relevance claim requiring
  empirical/domain validation
~~~

Draft guards:

~~~text
MODEL_CONSISTENT_FUTURE_STATE
  !=
FUTURE_WORLD_TRUTH

SIMULATION_MATCH_TO_ONE_HISTORICAL_CASE
  !=
PREDICTIVE_VALIDATION

SIMULATION_SUCCESS
  !=
PREDICTION_SUCCESS
~~~

## 18. Simulation vs Control / Operation / Computation / Optimization

~~~text
SIMULATING_SUPPLIED_CONTROL_POLICY
  !=
CHOOSING_CONTROL_POLICY

SIMULATING_LIFECYCLE_MODEL
  !=
OPERATING_REAL_LIFECYCLE

EXECUTING_TRAJECTORY
  !=
DETERMINING_REQUIRED_COMPUTATION

SOLVER_PLAN_SELECTED_BY_OPTIMIZATION
  !=
SIMULATION_TRAJECTORY
~~~

Neighboring methods may hand off inputs or consume outputs without substitution.

## 19. Simulation method gain and comparator fairness

Simulation validity and method gain are separate axes.

Working method-gain statuses:

~~~text
SIMULATION_GAIN_ESTABLISHED
SIMULATION_NO_GAIN
SIMULATION_GAIN_NOT_TESTED
SIMULATION_GAIN_BLOCKED
SIMULATION_GAIN_CONFLICTING
SIMULATION_GAIN_UNDERDETERMINED
SIMULATION_GAIN_OUT_OF_SCOPE
~~~

If gain is tested, freeze:

~~~text
GAIN_METRIC_ID
GAIN_SCOPE
GAIN_BASELINE_ID
COMPARATOR_ID
COMPARATOR_VERSION
COMPARATOR_MODEL_EQUIVALENCE
COMPARATOR_INITIAL_STATE_EQUIVALENCE
COMPARATOR_LAW_EQUIVALENCE
COMPARATOR_TRANSITION_EQUIVALENCE
COMPARATOR_SOLVER_INFORMATION_ACCESS
COMPARATOR_ERROR_SEMANTICS
COMPARATOR_HORIZON
COMPARATOR_ENVIRONMENT_IF_EMPIRICAL
COMPARATOR_FAIRNESS_STATUS
~~~

Draft guards:

~~~text
SIMULATION_ESTABLISHED may coexist with SIMULATION_NO_GAIN
NO_GAIN != METHOD_FAILURE
DIFFERENT_MODEL != FAIR_SIMULATION_GAIN_COMPARISON
DIFFERENT_INITIAL_STATE != FAIR_SIMULATION_GAIN_COMPARISON
HIDDEN_TRANSITION_INFORMATION != METHOD_GAIN
~~~

## 20. Working primary statuses

Exactly one primary Simulation status:

~~~text
SIMULATION_ESTABLISHED
SIMULATION_NOT_ESTABLISHED
SIMULATION_BLOCKED
SIMULATION_CONFLICTING
SIMULATION_OUT_OF_SCOPE
SIMULATION_UNDERDETERMINED
~~~

Interpretation:

~~~text
ESTABLISHED:
  requested Simulation claim is supported
  on the frozen model / state / horizon scope

NOT_ESTABLISHED:
  required interfaces are evaluable
  but the requested trajectory claim does not hold

BLOCKED:
  a required in-scope law / initial state / transition /
  bridge / error interface is unavailable

CONFLICTING:
  mutually incompatible applicable claim-relevant
  model/interface records remain unresolved

OUT_OF_SCOPE:
  requested operation lies outside Simulation

UNDERDETERMINED:
  multiple admissible claim-relevant semantics remain
  and generate materially different requested results,
  where the branching itself was not the declared model semantics
~~~

A declared branching transition relation is not UNDERDETERMINED merely because it has multiple outputs.

## 21. Working task terminals

Exactly one task terminal:

~~~text
SIMULATION_TASK_ESTABLISHED
SIMULATION_TASK_PARTIAL
SIMULATION_TASK_NOT_ESTABLISHED
SIMULATION_TASK_BLOCKED
SIMULATION_TASK_CONFLICTING
SIMULATION_TASK_OUT_OF_SCOPE
SIMULATION_TASK_UNDERDETERMINED
~~~

Provisional precedence to attack:

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

PARTIAL is provisionally restricted to multiple independently required in-scope Simulation obligations where at least one is ESTABLISHED and at least one is evaluably NOT_ESTABLISHED, with no BLOCKED or higher-priority state.

This rule must be boundary-attacked before protocol freeze.

## 22. Required output schema

Every future executable record should emit, as applicable:

~~~text
TASK_LOCK
MODEL_LOCK
INITIAL_STATE_LEDGER
STATE_CLASS_AND_COMPONENT_REGISTRY
REGULAR_SUPPORT_SIGNATURE_LEDGER

EVOLUTION_LAW_LEDGER
CONSTITUTIVE_BRIDGE_LEDGER
DEPENDENCY_OR_COUPLING_LEDGER

REGULAR_EPOCH_LEDGER
TRAJECTORY_LEDGER

TRANSITION_EVENT_LEDGER
TRANSITION_BALANCE_LEDGER
LINEAGE_LEDGER

STATIC_SLICE_COMPATIBILITY_LEDGER

SOLVER_OR_EXECUTION_LEDGER
APPROXIMATION_AND_ERROR_LEDGER
STOCHASTIC_EXECUTION_LEDGER

READOUT_HISTORY
READOUT_INFORMATION_LOSS_LEDGER

PROPAGATION_OR_LOCALITY_LEDGER
CONSERVATION_OR_RESIDUAL_LEDGER

NEIGHBORING_METHOD_HANDOFF_LEDGER

SIMULATION_METHOD_GAIN_STATUS
SIMULATION_PRIMARY_STATUS
SIMULATION_TASK_TERMINAL
SIMULATION_PROTOCOL_CONFORMANCE
MAXIMUM_SUPPORTED_CLAIM
~~~

Every claim-relevant optional ledger must be populated or explicitly marked:

~~~text
NOT_APPLICABLE
NOT_REQUESTED
BLOCKED
~~~

rather than silently omitted.

## 23. Five-interface identity

~~~text
INPUTS:
  frozen initial state/state class
  state representation / regular support signatures
  supplied evolution laws
  supplied transition / lineage / bridge semantics
  time/step horizon
  solver / approximation semantics
  optional readout and neighboring-method handoffs

OPERATION:
  verify state and predecessor-slice admissibility
  evolve regular trajectory segments under supplied laws
  detect declared transition triggers
  apply typed transition relations
  preserve or update lineage when required
  propagate approximation / stochastic semantics
  generate readouts without replacing full state
  stop under frozen termination rules

OUTPUTS:
  trajectory or trajectory family
  regular-epoch ledger
  transition / lineage ledger
  fixed-time compatibility record
  readout history
  approximation / stochastic ledger
  primary status / terminal / conformance / gain
  maximum-supported claim

FAILURE_OR_NO_GAIN:
  invalid initial state
  missing/conflicting evolution or transition law
  invalid static slice
  unsupported uniqueness
  unlicensed transition / lineage
  insufficient approximation/error support
  readout-based overclaim
  Prediction/Control/Operation substitution
  fair-baseline NO_GAIN

VALIDATION_STANDARD:
  generated trajectories satisfy every frozen model law,
  state-domain rule, transition relation, lineage obligation,
  fixed-time predecessor interface, execution/error condition,
  and stopping rule required by the declared claim;
  no empirical Prediction validity or external-domain correctness
  is inferred from internal model consistency
~~~

## 24. Draft binding-operation skeleton S1-S18

~~~text
S1  freeze task / model / primary claim / maximum claim
S2  freeze horizon / time-or-step semantics
S3  validate initial state(s) and state class
S4  freeze regular support signature(s)
S5  freeze regular evolution law(s)
S6  freeze constitutive / cross-layer bridges
S7  freeze transition relation(s) / trigger(s)
S8  freeze lineage obligations
S9  freeze solver / symbolic / stochastic execution semantics
S10 freeze approximation / error / convergence interfaces
S11 freeze readout / information-loss interfaces
S12 execute regular evolution segment(s)
S13 evaluate fixed-time static-slice compatibility
S14 detect / classify / execute typed transitions
S15 update lineage / post-transition initial states
S16 evaluate termination / horizon / reachable-result scope
S17 assign primary status / task terminal / method-gain status
S18 emit all ledgers, conformance, and maximum-supported claim
~~~

This skeleton is not yet a protocol.

## 25. Boundary-attack targets

Serious pre-protocol attack must include at least:

~~~text
A1  missing evolution law silently treated as zero dynamics
A2  invalid initial state accepted because solver accepts vector
A3  status/domain transition hidden as regular value evolution
A4  formation/channel identity change hidden as value change
A5  relation-valued transition collapsed to deterministic jump
A6  declared branching mislabeled underdetermined/failure
A7  one trajectory witness promoted to unique trajectory
A8  equal reduced readout histories promoted to equal state histories
A9  invalid fixed-time predecessor slice accepted dynamically
A10 local numerical error promoted to global exact trajectory
A11 one stochastic sample path promoted to distributional claim
A12 regular-epoch conservation promoted across transition
A13 c_info / propagation specialization treated as universal
A14 model-consistent trajectory promoted to Prediction truth
A15 supplied control policy simulation substituted for Control
A16 lifecycle model simulation substituted for Operation
A17 fair-baseline simulation with NO_GAIN
A18 task-terminal precedence / exact PARTIAL pressure
~~~

The attack may add cases if new boundary pressure emerges.

## 26. Current state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 established

TASK_INTERFACE_STATUS:
  PRE-PROTOCOL HISTORICAL DRAFT
  NOT AN EXECUTABLE STANDARD

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

DEDICATED_SIMULATION_PROTOCOL:
  not established

DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  0

BASELINE_SIMULATION_CASES:
  0

NO_GAIN_SIMULATION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_SIMULATION_APPLICATIONS:
  0

INDEPENDENT_SIMULATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

SIMULATION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_SIMULATION_EVIDENCE_STATUS:
  source_and_interface_recovery

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 27. Next

Execute a serious pre-protocol boundary attack against the 18 frozen attack targets.

Once direct boundary attack begins, this Task Interface v0.1 draft must remain immutable historical evidence.
