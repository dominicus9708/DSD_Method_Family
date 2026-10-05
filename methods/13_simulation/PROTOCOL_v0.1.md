# DSD Simulation Protocol v0.1

Status: **EXECUTABLE INTERNAL PROTOCOL — FROZEN FOR DIRECT CHALLENGES**  
Date: **2026-10-05**  
Method: **Simulation / DSD 시뮬레이션론**  
Legacy path ID: `13`  
Higher field: **VIII. Dynamics & Action / 동역학·행동**

Historical basis:

~~~text
SOURCE_REGISTRY_COMMIT:
  8c3879f211d1a024ba903273044e099f7ad7041d
SOURCE_REGISTRY_BLOB:
  a19a771215c0d63144bf613ff3ca6c3a9163151e

TASK_INTERFACE_COMMIT:
  31d2ff76c377f70a2a53f733d63b9e723661620d
TASK_INTERFACE_BLOB:
  62006cb8142a1f461c1c48ab48cb00354bf6f462

BOUNDARY_ATTACK_COMMIT:
  22ae5d92444d8eb0d27b0437cc9f944eff024e9c
BOUNDARY_ATTACK_BLOB:
  2966801192e0a0630ad88387cd314e433ed06ebf

BOUNDARY_AMENDMENT_001_COMMIT:
  2c7b22af07c0980472cbbad4c06f113337201374
BOUNDARY_AMENDMENT_001_BLOB:
  a0b1c47c7334f5420047d7eeeb868a2b6da4a8de
~~~

This protocol binds the historical Task Interface v0.1 draft and Boundary Amendment 001.

The historical Task Interface and boundary-attack record remain immutable development evidence.

## 1. Method task

Given:

~~~text
a frozen Simulation task and model version

a declared time / ordered-step horizon

an admissible initial state, initial-state set, or initial-state class

a component-resolved state representation

a regular support signature for each regular epoch

supplied regular evolution laws

supplied typed transition relations whenever the regular support
signature or formation background changes

explicit constitutive / cross-layer bridges when required

lineage handoffs when successor identity is claimed

declared analytic / symbolic / numerical / stochastic execution semantics

declared approximation / error / convergence semantics when used

declared readout maps and information-loss sidecars

declared stopping / termination semantics
~~~

generate or characterize:

~~~text
the model-consistent trajectory, trajectory family,
reachable-state set, hybrid regular-transition path,
declared readout history, or bounded approximate trajectory
requested by the primary claim

while preserving:
  regular epoch boundaries
  typed status/domain transitions
  formation-level transitions
  branch multiplicity
  lineage obligations
  fixed-time predecessor-slice validity
  numerical/stochastic claim limits
  readout information loss
  neighboring-method boundaries
~~~

Simulation does not invent missing dynamic laws or promote model consistency to external future truth.

## 2. Method boundary

~~~text
SIMULATION:
  generates model-consistent trajectories

PREDICTION:
  asserts relevance to a future external target

CONTROL:
  chooses state-dependent interventions

OPERATION:
  manages repeated live lifecycle / monitoring / handoff

COMPUTATION:
  determines required evaluations and sound reuse/omission

OPTIMIZATION:
  chooses among admissible alternatives under objectives

MEASUREMENT:
  acquires / discriminates evidence

LINEAGE:
  establishes predecessor-successor identity across change

AUDIT:
  evaluates conformance / evidence / procedure
~~~

Required guards:

~~~text
SIMULATION_TRAJECTORY != PREDICTION_CLAIM
SIMULATING_SUPPLIED_CONTROL_POLICY != CHOOSING_CONTROL_POLICY
SIMULATING_LIFECYCLE_MODEL != OPERATING_REAL_LIFECYCLE
COMPUTATION_PLAN != SIMULATION_EXECUTION
OPTIMAL_SIMULATION_PLAN != SIMULATION_TRAJECTORY
MEASUREMENT_RESULT != EVOLUTION_LAW
LINEAGE_HANDOFF != SIMULATION_EXECUTION
AUDIT_PASS != SIMULATION_TRAJECTORY
~~~

## 3. Primary claim levels

Exactly one primary claim level is frozen per task:

~~~text
ADMISSIBLE_TRAJECTORY_EXISTENCE_WITNESS
DECLARED_TRAJECTORY_ON_FIXED_HORIZON
TRAJECTORY_FAMILY_ON_DECLARED_BRANCHING_MODEL
HYBRID_REGULAR_TRANSITION_TRAJECTORY
DECLARED_READOUT_HISTORY
APPROXIMATE_TRAJECTORY_WITH_DECLARED_ERROR
REACHABLE_STATE_SET_ON_DECLARED_HORIZON
~~~

No primary claim automatically implies:

~~~text
global uniqueness
unbounded-time existence
external future truth
empirical calibration
model correctness
control optimality
operational success
exactness of a numerical result
distributional truth from one stochastic path
~~~

## 4. Validity gates G1-G18

### G1 — task / model / primary claim / maximum-claim lock

Freeze:

~~~text
SIMULATION_TASK_ID
TASK_VERSION
PRIMARY_CLAIM_LEVEL
MAXIMUM_SUPPORTED_CLAIM

SOURCE_MODEL_ID
SOURCE_MODEL_VERSION
SOURCE_MODEL_SCOPE
SOURCE_MODEL_PROVENANCE
ACTIVE_DSD_LAYERS
~~~

Changing a claim-relevant lock after seeing trajectory outputs requires a new task version.

### G2 — time / horizon / trajectory-quantifier lock

Freeze:

~~~text
TIME_OR_STEP_DOMAIN
TIME_METRIC_STATUS
SIMULATION_HORIZON

TRAJECTORY_QUANTIFIER
BRANCH_COMPLETENESS_RULE
REACHABILITY_SCOPE
~~~

Allowed trajectory quantifiers:

~~~text
EXISTENTIAL_WITNESS
DECLARED_DETERMINATE_TRAJECTORY
ALL_DECLARED_BRANCHES_ON_SCOPE
REACHABLE_SET_ON_SCOPE
SUPPLIED_SELECTED_BRANCH
STOCHASTIC_SAMPLE_PATH
~~~

Required guards:

~~~text
ONE_TRAJECTORY_WITNESS != UNIQUE_TRAJECTORY
ONE_SELECTED_BRANCH != ALL_BRANCHES
BOUNDED_HORIZON_RESULT != UNBOUNDED_TIME_RESULT
DECLARED_BRANCHING != SEMANTIC_UNDERDETERMINATION
~~~

### G3 — initial-state / state-class admissibility gate

Freeze:

~~~text
INITIAL_STATE_CLASS_ID
INITIAL_STATE_ID_OR_SET
INITIAL_STATE_VERSION
STATE_CLASS_ID
STATE_REPRESENTATION_MODE
COMPONENT_REGISTRY
INITIAL_STATE_ADMISSIBILITY
INITIAL_STATE_PROVENANCE
~~~

Status family:

~~~text
INITIAL_STATE_ADMISSIBLE
INITIAL_STATE_INADMISSIBLE
INITIAL_STATE_BLOCKED
INITIAL_STATE_CONFLICTING
INITIAL_STATE_UNDERDETERMINED
INITIAL_STATE_OUT_OF_SCOPE
~~~

Binding consequences:

~~~text
known inadmissible
  -> SIMULATION_NOT_ESTABLISHED

required admissibility interface unavailable
  -> SIMULATION_BLOCKED

conflicting applicable initial-state records
  -> SIMULATION_CONFLICTING

multiple admissible unresolved initial-state semantics
with different requested results
  -> SIMULATION_UNDERDETERMINED
~~~

Required guards:

~~~text
INITIAL_STATE_VALUE_PRESENT != INITIAL_STATE_ADMISSIBLE
SOLVER_ACCEPTS_VECTOR != STATE_ADMISSIBLE
UNDEFINED_STATE != DEFINED_ZERO_STATE
MISSING_OPTIONAL_INTERFACE != ZERO_OBJECT
~~~

### G4 — regular support signature / epoch gate

For every regular epoch freeze:

~~~text
REGULAR_EPOCH_ID
TIME_OR_STEP_SUBDOMAIN
FORMATION_BACKGROUND_ID
REGULAR_SUPPORT_SIGNATURE_ID
REGULAR_SUPPORT_SIGNATURE_VERSION
COMPONENT_TYPES
PROPERTY_STATUS_PARTITION_IF_USED
ANALYTIC_CARRIER_TYPES_IF_USED
GEOMETRIC_SPECIALIZATION_IF_USED
~~~

Required guards:

~~~text
VALUE_CHANGE_WITHIN_Q != CHANGE_OF_Q
REGULAR_EPOCH != GLOBAL_TRAJECTORY_WITHOUT_TRANSITIONS
STATUS_OR_DOMAIN_CHANGE_INVALIDATING_Q != REGULAR_VALUE_EVOLUTION
FORMATION_BACKGROUND_CHANGE != REGULAR_VALUE_EVOLUTION
~~~

### G5 — regular evolution-law gate

Freeze each claim-relevant law:

~~~text
EVOLUTION_LAW_ID
EVOLUTION_LAW_VERSION_OR_DEFINITION
EVOLUTION_LAW_DOMAIN
STATE_VARIABLES_ACTED_ON
TIME_OR_STEP_SEMANTICS
DETERMINISTIC_OR_RELATIONAL_STATUS
REGULARITY_ASSUMPTIONS
BOUNDARY_OR_INITIAL_CONDITIONS_IF_REQUIRED
EVOLUTION_LAW_PROVENANCE
~~~

Law statuses:

~~~text
EVOLUTION_LAW_AVAILABLE
EVOLUTION_LAW_UNAVAILABLE
EVOLUTION_LAW_CONFLICTING
EVOLUTION_LAW_UNDERDETERMINED
EVOLUTION_LAW_OUT_OF_SCOPE
~~~

Required guards:

~~~text
MISSING_EVOLUTION_LAW != ZERO_DYNAMICS
MODEL_LABEL != EVOLUTION_OPERATOR
PROPERTY_LABEL != DYNAMIC_COEFFICIENT
AVAILABLE_LAW != VALID_INITIAL_STATE
~~~

### G6 — constitutive / cross-layer bridge gate

When predecessor records become dynamic operator inputs, freeze:

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

Required guards:

~~~text
PROPERTY_NAME != CONSTITUTIVE_COEFFICIENT
STATIC_PROPERTY_BRIDGE != DYNAMIC_EVOLUTION_OPERATOR
AGGREGATE_READOUT != COMPONENT_DYNAMIC_STATE
STATIC_ASSOCIATION != DYNAMIC_CAUSAL_OPERATOR
~~~

### G7 — typed transition relation gate

When the regular support signature or formation background changes, freeze:

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

Transition statuses:

~~~text
TRANSITION_ESTABLISHED
TRANSITION_NOT_ESTABLISHED
TRANSITION_BLOCKED
TRANSITION_CONFLICTING
TRANSITION_UNDERDETERMINED
TRANSITION_OUT_OF_SCOPE
~~~

Required guards:

~~~text
RELATION_VALUED_TRANSITION != DETERMINISTIC_JUMP_MAP
MULTIPLE_DECLARED_SUCCESSORS != UNDERDETERMINED_BY_DEFAULT
BRANCHING_MODEL != SIMULATION_FAILURE
REGULAR_EPOCH_CONSERVATION != TRANSITION_CONSERVATION
~~~

Every transition output used in a trajectory must be admissible as a post-transition initial state.

### G8 — lineage / successor-identity gate

When successor identity is claim-relevant, freeze:

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

Required guards:

~~~text
SAME_LABEL_AFTER_TRANSITION != SAME_FORMATION_OBJECT
READOUT_CONTINUITY != LINEAGE_CONTINUITY
AGGREGATE_EQUALITY != SUCCESSOR_IDENTITY
BRANCHING_LINEAGE != BIJECTIVE_LINEAGE
LINEAGE_HANDOFF != SIMULATION_EXECUTION
~~~

### G9 — fixed-time static-slice conformance gate

Freeze:

~~~text
PREDECESSOR_INTERFACE_SET_CHECKED
STATIC_SLICE_CONFORMANCE_STATUS
STATIC_SLICE_FAILURE_SCOPE
STATIC_SLICE_CONFORMANCE_PROVENANCE
~~~

Status family:

~~~text
STATIC_SLICE_CONFORMANT
STATIC_SLICE_NONCONFORMANT
STATIC_SLICE_BLOCKED
STATIC_SLICE_CONFLICTING
STATIC_SLICE_UNDERDETERMINED
STATIC_SLICE_OUT_OF_SCOPE
~~~

Binding consequences:

~~~text
known nonconformant required slice
  -> requested trajectory claim NOT_ESTABLISHED

required slice check unavailable
  -> BLOCKED

conflicting applicable slice records
  -> CONFLICTING

multiple admissible slice semantics with different results
  -> UNDERDETERMINED
~~~

Required guards:

~~~text
SOLVER_PRODUCED_STATE != STATIC_SLICE_CONFORMANT
STATIC_READOUT_MATCH != DYNAMIC_STATE_IDENTITY
DYNAMIC_EXECUTION_CANNOT_REPAIR_INVALID_STATIC_SLICE
~~~

### G10 — execution / numerical adequacy gate

Freeze execution mode:

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

When numerical/approximate execution is used, freeze:

~~~text
SOLVER_OR_EXECUTION_INTERFACE
SOLVER_VERSION
SOLVER_TERMINATION_STATUS

NUMERICAL_CLAIM_KIND
DISCRETIZATION_OR_APPROXIMATION_RULE
ERROR_METRIC
LOCAL_ERROR_BOUND_IF_USED
GLOBAL_OR_END_TO_END_ERROR_BOUND_IF_REQUIRED
ERROR_PROPAGATION_RULE
CONVERGENCE_OR_STABILITY_STATUS
NUMERICAL_ACCEPTANCE_THRESHOLD
NUMERICAL_ACCEPTANCE_STATUS
~~~

Solver termination statuses:

~~~text
SOLVER_TERMINATED_NORMALLY
SOLVER_STOPPED_BY_DECLARED_RULE
SOLVER_FAILED
SOLVER_BLOCKED
SOLVER_CONFLICTING
SOLVER_UNDERDETERMINED
SOLVER_OUT_OF_SCOPE
~~~

Required guards:

~~~text
SOLVER_TERMINATED != TRAJECTORY_ESTABLISHED
LOCAL_ERROR_CONTROL != GLOBAL_ERROR_BOUND
SOLVER_FAILURE != MODEL_NO_TRAJECTORY
NUMERICAL_ACCEPTANCE != EXACTNESS
CONVERGENCE_OF_SCHEME != EMPIRICAL_MODEL_VALIDITY
~~~

### G11 — stochastic claim / adequacy gate

When stochastic execution is claim-relevant, freeze:

~~~text
STOCHASTIC_CLAIM_KIND
RANDOMNESS_INTERFACE_ID
STOCHASTIC_PROCESS_VERSION_OR_DEFINITION
SEED_OR_SAMPLE_RULE
SAMPLE_COUNT_OR_COVERAGE
DISTRIBUTIONAL_TARGET_IF_ANY
STOCHASTIC_ADEQUACY_RULE
STOCHASTIC_ADEQUACY_STATUS
~~~

Allowed claim kinds:

~~~text
SAMPLE_PATH
FINITE_ENSEMBLE
EMPIRICAL_DISTRIBUTION_SUMMARY
DISTRIBUTIONAL_PROPERTY_IF_SUPPLIED
~~~

Required guards:

~~~text
EXPECTED_RANDOM_MULTIPLICITY != SEMANTIC_UNDERDETERMINATION
ONE_SAMPLE_PATH != DISTRIBUTIONAL_CLAIM
FINITE_ENSEMBLE != EXACT_PROBABILITY_LAW
FIXED_SEED_REPRODUCIBILITY != DISTRIBUTIONAL_VALIDITY
~~~

### G12 — trajectory / branch / uniqueness / reachability gate

Construct the result appropriate to the frozen quantifier:

~~~text
TRAJECTORY_LEDGER
TRAJECTORY_FAMILY
BRANCH_COVERAGE_STATUS
BRANCH_COMPLETENESS_RULE
UNIQUENESS_EVIDENCE_STATUS
REACHABLE_STATE_SET_IF_REQUESTED
REACHABILITY_SCOPE
~~~

Branch statuses:

~~~text
BRANCH_COVERAGE_COMPLETE_ON_DECLARED_SCOPE
BRANCH_COVERAGE_PARTIAL
BRANCH_COVERAGE_BLOCKED
BRANCH_COVERAGE_CONFLICTING
BRANCH_COVERAGE_UNDERDETERMINED
BRANCH_COVERAGE_OUT_OF_SCOPE
~~~

Uniqueness statuses:

~~~text
UNIQUENESS_ESTABLISHED_ON_DECLARED_SCOPE
UNIQUENESS_NOT_ESTABLISHED
UNIQUENESS_BLOCKED
UNIQUENESS_CONFLICTING
UNIQUENESS_UNDERDETERMINED
UNIQUENESS_OUT_OF_SCOPE
~~~

Required guards:

~~~text
SOLVER_DETERMINISM != MODEL_SOLUTION_UNIQUENESS
EXISTENCE_WITNESS != COMPLETE_BRANCH_FAMILY
REACHABLE_SET_ON_SCOPE != GLOBAL_REACHABILITY
~~~

### G13 — readout / information-loss gate

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

Required guards:

~~~text
READOUT_HISTORY != COMPONENT_RESOLVED_TRAJECTORY
EQUAL_READOUT_HISTORY != EQUAL_TRAJECTORY
READOUT_FRONT != COMPONENT_INFORMATION_FRONT
REDUCED_TRAJECTORY_MATCH != LINEAGE_IDENTITY
~~~

A readout-based state-equivalence claim requires an explicit sufficient preservation/injectivity condition.

### G14 — conservation / propagation / specialization gate

If conservation, balance, propagation, locality, equilibrium, or target-reaching claims are used, freeze only the exact specialization needed.

Possible records:

~~~text
CONSERVATION_ID
CONSERVATION_SCOPE
BALANCE_RULE

LOCALIZATION_CARRIER
PROPAGATION_METRIC
METRIC_TIME_SCALE
DISCREPANCY_CONVENTION
PROPAGATION_BOUND
SUPPORT_FAITHFULNESS_STATUS

TARGET_RELATION
RESIDUAL_CARRIER
RESIDUAL_RULE
TARGET_REACHED_RULE
~~~

Required guards:

~~~text
REGULAR_EPOCH_CONSERVATION != CROSS_TRANSITION_CONSERVATION
C_INFO != UNIVERSAL_DSD_CONSTANT
FINITE_PROPAGATION_SPECIALIZATION != GENERAL_SIMULATION_RULE
PROJECTED_FRONT_SPEED != COMPONENT_FRONT_SPEED_BY_DEFAULT
SMALL_SCALAR_RESIDUAL != STRUCTURAL_TARGET_REACHED
~~~

### G15 — neighboring-method handoff / non-substitution gate

Simulation may consume explicit handoffs from:

~~~text
Computation
Optimization
Measurement
Aggregation
Compression
Transformation
Tracking
Lineage
Prediction
Control
Operation
Audit
~~~

But:

~~~text
COMPUTATION_PLAN != SIMULATION_EXECUTION
OPTIMIZATION_SELECTION != SIMULATION_TRAJECTORY
MEASUREMENT_RESULT != EVOLUTION_LAW
AGGREGATE_READOUT != COMPONENT_TRAJECTORY
COMPRESSION_OUTPUT != SIMULATION_STATE_BY_DEFAULT
TRANSFORMATION_RESULT != TIME_EVOLUTION
TRACKING_TRACE != TRAJECTORY_DYNAMICS
LINEAGE_HANDOFF != SIMULATION_EXECUTION
SIMULATION_TRAJECTORY != PREDICTION_TRUTH
SIMULATING_POLICY != CHOOSING_POLICY
SIMULATING_LIFECYCLE != OPERATING_LIFECYCLE
AUDIT_VERDICT != SIMULATION_TRAJECTORY
~~~

### G16 — method-gain / comparator-fairness gate

Simulation validity and method gain are independent axes.

Method-gain status family:

~~~text
SIMULATION_GAIN_ESTABLISHED
SIMULATION_NO_GAIN
SIMULATION_GAIN_NOT_TESTED
SIMULATION_GAIN_BLOCKED
SIMULATION_GAIN_CONFLICTING
SIMULATION_GAIN_UNDERDETERMINED
SIMULATION_GAIN_OUT_OF_SCOPE
~~~

When gain is tested, freeze:

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
COMPARATOR_BRANCH_QUANTIFIER_EQUIVALENCE
COMPARATOR_SOLVER_INFORMATION_ACCESS
COMPARATOR_ERROR_SEMANTICS
COMPARATOR_STOCHASTIC_SEMANTICS
COMPARATOR_HORIZON
COMPARATOR_ENVIRONMENT_IF_EMPIRICAL
COMPARATOR_FAIRNESS_STATUS
COMPARATOR_FAIRNESS_PROVENANCE
~~~

Required guards:

~~~text
SIMULATION_ESTABLISHED may coexist with SIMULATION_NO_GAIN
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
DIFFERENT_MODEL != FAIR_GAIN_COMPARISON
DIFFERENT_INITIAL_STATE != FAIR_GAIN_COMPARISON
DIFFERENT_BRANCH_QUANTIFIER != FAIR_GAIN_COMPARISON
HIDDEN_TRANSITION_INFORMATION != METHOD_GAIN
~~~

### G17 — primary Simulation status gate

Assign one primary status:

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
  on the frozen model/state/horizon/quantifier scope

NOT_ESTABLISHED:
  required claim interfaces are evaluable
  but the requested trajectory claim does not hold

BLOCKED:
  one or more required in-scope initial-state/law/transition/
  lineage/slice/error/stochastic interfaces are unavailable

CONFLICTING:
  mutually incompatible applicable claim-relevant
  model/interface records remain unresolved

OUT_OF_SCOPE:
  requested operation lies outside Simulation

UNDERDETERMINED:
  multiple admissible claim-relevant semantics remain
  and produce materially different requested results,
  excluding multiplicity explicitly declared by the model
~~~

### G18 — task terminal / protocol conformance / maximum-claim gate

Assign exactly one task terminal:

~~~text
SIMULATION_TASK_ESTABLISHED
SIMULATION_TASK_PARTIAL
SIMULATION_TASK_NOT_ESTABLISHED
SIMULATION_TASK_BLOCKED
SIMULATION_TASK_CONFLICTING
SIMULATION_TASK_OUT_OF_SCOPE
SIMULATION_TASK_UNDERDETERMINED
~~~

Frozen precedence:

~~~text
SIMULATION_TASK_OUT_OF_SCOPE
>
SIMULATION_TASK_CONFLICTING
>
SIMULATION_TASK_UNDERDETERMINED
>
SIMULATION_TASK_BLOCKED
>
SIMULATION_TASK_ESTABLISHED /
SIMULATION_TASK_PARTIAL /
SIMULATION_TASK_NOT_ESTABLISHED
~~~

PARTIAL is permitted only when:

~~~text
1. multiple independently required in-scope Simulation obligations exist
2. at least one required obligation is ESTABLISHED
3. at least one other required obligation is evaluably NOT_ESTABLISHED
4. no required obligation is BLOCKED
5. no higher-priority OUT_OF_SCOPE / CONFLICTING /
   UNDERDETERMINED condition applies
~~~

Required guards:

~~~text
PARTIAL != BLOCKED_WITH_SOME_SUCCESS
PARTIAL != ATOMIC_FAILURE_RELABELED
DECLARED_BRANCHING != PARTIAL
STOCHASTIC_MULTIPLICITY != PARTIAL
SIMULATION_NO_GAIN != SIMULATION_TASK_PARTIAL_BY_DEFAULT
~~~

Then emit protocol conformance, method-gain status, and maximum-supported claim.

## 5. Binding operation S1-S18

### S1 — freeze task / model / primary claim / maximum claim
Instantiate G1.

### S2 — freeze time / horizon / trajectory quantifier
Instantiate G2.

### S3 — validate initial state(s) and state class
Instantiate G3.

### S4 — freeze regular support signature(s) / epoch structure
Instantiate G4.

### S5 — freeze regular evolution law(s)
Instantiate G5.

### S6 — freeze constitutive / cross-layer bridges
Instantiate G6.

### S7 — freeze typed transition relations and triggers
Instantiate G7.

### S8 — freeze lineage obligations
Instantiate G8.

### S9 — evaluate fixed-time predecessor-slice conformance
Instantiate G9.

### S10 — freeze/execute analytic, symbolic, numerical, or hybrid semantics
Instantiate G10.

### S11 — freeze/evaluate stochastic claim semantics when used
Instantiate G11.

### S12 — generate regular trajectory segments and branch/reachability results
Instantiate G12.

### S13 — generate declared readouts and preserve information-loss limits
Instantiate G13.

### S14 — apply conservation / propagation / target specializations only when supplied
Instantiate G14.

### S15 — apply neighboring-method handoffs without substitution
Instantiate G15.

### S16 — evaluate method gain / comparator fairness if requested
Instantiate G16.

If gain is not requested:

~~~text
SIMULATION_GAIN_NOT_TESTED
~~~

is allowed.

### S17 — assign primary Simulation status
Instantiate G17.

### S18 — assign task terminal / protocol conformance / maximum claim
Instantiate G18.

Preserve all subordinate states beneath the task terminal.

## 6. Protocol conformance

~~~text
SIMULATION_PROTOCOL_CONFORMANT
SIMULATION_PROTOCOL_NONCONFORMANT
SIMULATION_PROTOCOL_INDETERMINATE
~~~

A blocked, conflicting, underdetermined, branching, stochastic, approximate, negative, partial, or out-of-scope result may still be protocol-conformant.

Protocol conformance concerns whether the frozen Simulation protocol was followed, not whether a unique or empirically accurate trajectory was obtained.

## 7. Required output schema

Every executable record must emit, as applicable:

~~~text
TASK_LOCK
MODEL_LOCK
TIME_HORIZON_AND_QUANTIFIER_LOCK

INITIAL_STATE_LEDGER
STATE_CLASS_AND_COMPONENT_REGISTRY
REGULAR_SUPPORT_SIGNATURE_LEDGER

EVOLUTION_LAW_LEDGER
CONSTITUTIVE_BRIDGE_LEDGER
DEPENDENCY_OR_COUPLING_LEDGER

REGULAR_EPOCH_LEDGER
TRAJECTORY_LEDGER
BRANCH_COVERAGE_LEDGER
UNIQUENESS_EVIDENCE_LEDGER
REACHABILITY_LEDGER_IF_REQUESTED

TRANSITION_EVENT_LEDGER
TRANSITION_BALANCE_LEDGER
LINEAGE_LEDGER

STATIC_SLICE_CONFORMANCE_LEDGER

SOLVER_TERMINATION_LEDGER
NUMERICAL_ADEQUACY_LEDGER

STOCHASTIC_CLAIM_LOCK
STOCHASTIC_ADEQUACY_LEDGER

READOUT_HISTORY
READOUT_INFORMATION_LOSS_LEDGER

PROPAGATION_OR_LOCALITY_LEDGER
CONSERVATION_OR_RESIDUAL_LEDGER

NEIGHBORING_METHOD_HANDOFF_LEDGER

COMPARATOR_EQUIVALENCE_AND_FAIRNESS_LEDGER_IF_GAIN_TESTED
SIMULATION_METHOD_GAIN_STATUS

SIMULATION_PRIMARY_STATUS
SIMULATION_TASK_TERMINAL
SIMULATION_PROTOCOL_CONFORMANCE

MAXIMUM_SUPPORTED_CLAIM
~~~

Every claim-relevant optional ledger must be explicitly:

~~~text
populated
NOT_APPLICABLE
NOT_REQUESTED
BLOCKED
~~~

rather than silently omitted.

## 8. Five-interface identity

~~~text
INPUTS:
  frozen dynamic model
  admissible initial-state/state-class interface
  time/horizon/trajectory quantifier
  regular support signatures
  supplied evolution / transition / lineage / bridge semantics
  execution/error/stochastic semantics
  optional readout and neighboring-method handoffs

OPERATION:
  validate initial and fixed-time predecessor states
  evolve regular segments under supplied laws
  preserve declared branch multiplicity and claim quantifier
  execute typed transitions
  consume lineage where successor identity is claimed
  propagate numerical/stochastic semantics
  generate readouts without replacing the full state
  apply only supplied conservation/propagation specializations

OUTPUTS:
  trajectory / trajectory family / reachable set
  regular-epoch / transition / lineage ledgers
  slice-conformance and execution/error ledgers
  readout history
  primary status / task terminal / conformance
  separate method-gain status
  maximum-supported claim

FAILURE_OR_NO_GAIN:
  known inadmissible initial state
  missing/conflicting/underdetermined model interface
  invalid predecessor slice
  unsupported uniqueness/branch completeness
  numerical/stochastic overclaim
  unlicensed transition/lineage
  readout-based identity overclaim
  neighboring-method substitution
  fair-baseline NO_GAIN

VALIDATION_STANDARD:
  every generated result follows the frozen model,
  state domain, regular-epoch structure, transition relation,
  trajectory quantifier, lineage obligation, predecessor-slice
  interface, execution/error/stochastic semantics, readout limits,
  and stopping scope required by the declared claim;
  no external Prediction truth, Control choice, Operation success,
  or universal domain law is inferred
~~~

## 9. Core semantic guards

~~~text
MISSING_EVOLUTION_LAW != ZERO_DYNAMICS

INITIAL_STATE_VALUE_PRESENT != INITIAL_STATE_ADMISSIBLE

REGULAR_VALUE_EVOLUTION != STATUS_OR_DOMAIN_TRANSITION

STATUS_OR_DOMAIN_TRANSITION != FORMATION_TRANSITION

CHANNEL_IDENTITY_CHANGE != VALUE_CHANGE_ON_ONE_FIXED_CHANNEL

TRANSITION_RELATION != DETERMINISTIC_JUMP_MAP

DECLARED_BRANCHING != SEMANTIC_UNDERDETERMINATION

ONE_TRAJECTORY_WITNESS != UNIQUE_TRAJECTORY

SOLVER_DETERMINISM != MODEL_SOLUTION_UNIQUENESS

SOLVER_TERMINATED != TRAJECTORY_ESTABLISHED

SOLVER_FAILURE != MODEL_NO_TRAJECTORY

NUMERICAL_TRAJECTORY != EXACT_TRAJECTORY

LOCAL_ERROR_CONTROL != GLOBAL_ERROR_BOUND

ONE_STOCHASTIC_SAMPLE_PATH != DISTRIBUTIONAL_CLAIM

READOUT_HISTORY != COMPONENT_RESOLVED_TRAJECTORY

EQUAL_READOUT_HISTORY != EQUAL_TRAJECTORY

REGULAR_EPOCH_CONSERVATION != CROSS_TRANSITION_CONSERVATION

C_INFO != UNIVERSAL_DSD_CONSTANT

SIMULATION_TRAJECTORY != PREDICTION_CLAIM

SIMULATING_SUPPLIED_CONTROL_POLICY != CHOOSING_CONTROL_POLICY

SIMULATING_LIFECYCLE_MODEL != OPERATING_REAL_LIFECYCLE

SIMULATION_ESTABLISHED may coexist with SIMULATION_NO_GAIN
~~~

## 10. Current protocol state

~~~text
DEDICATED_SIMULATION_PROTOCOL:
  established v0.1

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  S1-S18

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

BOUNDARY_AMENDMENT_001:
  established

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
  protocol_frozen

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 11. Next

Prospectively precommit and execute **SIM-CH-001**, the positive constructed Simulation challenge.

The first challenge should directly exercise at least:

~~~text
regular deterministic trajectory
declared branching trajectory family
hybrid regular-transition trajectory
fixed-time static-slice conformance
readout collision without state collapse
bounded numerical approximation
stochastic sample-path claim without distributional overclaim
Simulation-Prediction-Control boundary preservation
method gain not tested
bounded maximum-supported claim
~~~
