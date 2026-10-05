# DSD Simulation — Source / Registry Recovery v0.1

Status: **SOURCE / REGISTRY RECOVERY COMPLETE — PRE-TASK-INTERFACE**  
Date: **2026-10-05**  
Method: **Simulation / DSD 시뮬레이션론**  
Legacy path ID: `13`  
Higher field: **VIII. Dynamics & Action / 동역학·행동**

This document recovers the source constraints and current method-registry boundary for Simulation before any Task Interface is frozen.

It is not a Simulation protocol and does not itself authorize protocol freeze.

## 1. Current registry identity

Current repository / Notion definition:

~~~text
Task:
  generate and compare admissible state trajectories
  under a supplied model while preserving the distinction
  between regular evolution and typed transitions

Typical outputs:
  state-space and support signature
  initial condition
  regular epoch declaration
  supplied evolution / transition laws
  component and channel lineage
  static-slice-compatible readouts
  alternative trajectories
  termination conditions

Boundary:
  DSD supplies a structural simulation interface
  but does not supply a universal physical, biological,
  economic, social, artistic, or other domain law
~~~

Current GitHub path:

~~~text
methods/13_simulation/
~~~

Current Notion page:

~~~text
13. DSD 시뮬레이션론
3d281f51-e7fa-813d-8d68-f7f39098c896
~~~

Registry boundary inside Field VIII:

~~~text
SIMULATION:
  generates model-consistent trajectories

PREDICTION:
  claims relevance to a future target

CONTROL:
  chooses state-dependent interventions

OPERATION:
  manages repeated execution / lifecycle / monitoring / handoff

SIMULATION != PREDICTION
SIMULATION != CONTROL
SIMULATION != OPERATION
~~~

## 2. Source hierarchy used for recovery

### S1 — Formation Axiom System

Source:

~~~text
DSD_Formation_Axiom_System_EN(5).pdf
~~~

Recovered constraints relevant to Simulation:

~~~text
the seven-stage formation system fixes how admitted
operational channels arise before downstream dynamics

undefined assignment
  !=
defined zero

channel absence
  !=
admitted channel with zero component term

assigned value is part of operational-channel identity

finite composition is downstream of admitted channel identity
and supplied term data
~~~

Simulation consequence:

~~~text
a time-varying coordinate that belongs to Stage-VI channel identity
cannot be silently represented as ordinary value evolution of one
unchanged inherited channel

channel birth/death or identity-coordinate change may require
a formation-level transition

zero padding cannot replace absent / undefined channel states

equal composite outputs do not establish equal dynamic source state
~~~

### S2 — Property Axiom System

Source:

~~~text
DSD_Property_Axiom_System_EN(3).pdf
~~~

Recovered status family:

~~~text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_VALUE
~~~

Simulation consequence:

~~~text
property-value evolution inside one fixed defined domain
  !=
property-status or domain transition

defined zero
  !=
undefined / inapplicable / prerequisite-unsatisfied

a property label does not itself determine a physical or
mathematical evolution coefficient

a constitutive dynamic bridge is required whenever typed
property data are used as operator data
~~~

### S3 — Channel-Indexed Static Aggregation

Source:

~~~text
DSD_Channel_Indexed_Static_Aggregation_EN(9).pdf
~~~

Recovered constraints:

~~~text
every fixed-time dynamic slice may use the static analytic
and property-aggregation interfaces only on their declared domains

aggregate equality
  !=
support equality

aggregate equality
  !=
source decomposition equality

reduced readouts may be noninjective

typed property aggregation requires an explicit bridge
~~~

Simulation consequence:

~~~text
STATIC_READOUT_TRAJECTORY
  !=
COMPONENT_RESOLVED_TRAJECTORY

EQUAL_READOUT_HISTORY
  !=
EQUAL_DYNAMIC_STATE_HISTORY

a trajectory may be compared through a reduced readout only
to the extent that the declared simulation claim needs that readout

lossy readouts cannot silently determine lineage,
component identity, or hidden trajectory equality
~~~

### S4 — Structural Reorganization Dynamics

Source:

~~~text
DSD_Structural_Reorganization_Dynamics_EN(20260904-092544).pdf
~~~

This is the primary formal source for Simulation.

Recovered instantaneous-state discipline:

~~~text
S(t):
  complete component-resolved downstream state declared
  by the chosen dynamic model

missing optional interface:
  omitted

missing optional interface:
  != numerical zero object
~~~

Recovered regular-support discipline:

~~~text
Q:
  fixed typing / support signature used to compare slices
  inside a regular epoch

regular epoch (J,Q):
  same inherited Stage-VI formation background
  same regular support signature

inside the epoch:
  values may evolve on the declared fixed domains/types

status/domain or formation change invalidating Q:
  ends the regular epoch
  requires a transition relation
~~~

Recovered trajectory discipline:

~~~text
general DSD trajectory:
  typed state path

smooth field equation:
  one specialization only

continuity / differentiability / Sobolev / PDE assumptions:
  supplied by the chosen model when required
  not forced by DSD foundations
~~~

Recovered static-slice compatibility:

~~~text
for every fixed time t:
  forgetting temporal labels and cross-time relations
  must leave a valid static slice of every predecessor interface used

static aggregate at t:
  agrees with the predecessor static construction
  evaluated directly on the time-t slice
~~~

Recovered lineage discipline:

~~~text
fixed formation background inside a regular epoch:
  canonical identity lineage is available on inherited channels

across formation-level transition:
  successor identity is not automatic

channel lineage / component lineage:
  explicit relation when successor identity is claimed

branching / merging:
  allowed unless a stricter model forbids them

lineage succession:
  != literal state equality
  != aggregate equality
~~~

Recovered event-class separation:

~~~text
analytic / represented value evolution
  !=
property-assignment evolution
  !=
status/domain transition
  !=
formation-level transition

transport
  !=
coupling transfer
  !=
property-status transition
  !=
formation transition
~~~

Recovered transition discipline:

~~~text
J_k : X_k^- => X_k^+

transition relation outputs:
  valid initial states for the post-transition epoch

deterministic jump map:
  special case

relation-valued transition:
  may branch or remain underdetermined
  without asserting uniqueness
~~~

Recovered conservation discipline:

~~~text
regular-epoch conservation:
  additional model condition

conservation across a typed transition:
  requires a supplied balance / jump rule

regular conservation
  !=
automatic transition conservation
~~~

Recovered readout discipline:

~~~text
reduced readout O_t:
  evaluated after the component-resolved state is specified

reduced readout:
  need not classify the complete state

equal D_w(t):
  does not establish equal dynamic state
~~~

Recovered propagation discipline:

~~~text
finite propagation requires explicit localization,
metric-time, discrepancy, evolution, regularity,
and support-faithfulness assumptions

c_info:
  not a universal DSD constant

projected front:
  may be slower or invisible relative to
  component-resolved discrepancy propagation

no converse reconstruction from projected front
without injectivity / reconstruction condition
~~~

### S5 — Method Family registry / shared-core discipline

Project-internal sources:

~~~text
methods/README.md
methods/METHOD_BOUNDARY_MATRIX.md
methods/fields/08_dynamics_action/README.md
methodology/DSD_METHOD_FAMILY_FRAMEWORK.md
methodology/DSD_INTERFACE_PROFILE.md
methodology/SHARED_CORE_EXTRACTION_RULE.md
~~~

Recovered family boundary:

~~~text
SIMULATION:
  generate model-consistent trajectories

PREDICTION:
  assert future-target relevance

CONTROL:
  choose interventions

OPERATION:
  manage repeated live lifecycle / execution / monitoring
~~~

Shared-core rules constrain Simulation construction but do not directly validate Simulation.

### S6 — Computation and Optimization internal-standard handoffs

Project-internal sources:

~~~text
methods/12_computation_optimization/computation/
methods/12_computation_optimization/optimization/
~~~

Recovered boundary:

~~~text
Computation may determine which evolution operations,
dependencies, resolutions, or reusable calculations
must actually be evaluated

Optimization may select among admissible simulation plans
under an explicit objective

Simulation executes / generates the declared model trajectory

COMPUTATION_PLAN != SIMULATION_TRAJECTORY
OPTIMAL_SIMULATION_PLAN != EXECUTED_TRAJECTORY
~~~

### S7 — Audit outcome semantics

Project-internal source:

~~~text
methodology/AUDIT_OUTCOME_SEMANTICS.md
~~~

Simulation consequence:

~~~text
model-consistent trajectory
  may still have NO_GAIN against a competent non-DSD simulator

model-consistent trajectory
  !=
empirically validated prediction

simulation failure due to missing required evolution law
  !=
trajectory contradiction

NO_GAIN
  !=
method failure
~~~

## 3. Source-derived Simulation constraints

These are recovered constraints rather than new Simulation theorems.

~~~text
SR-01
  every simulated state must be admissible on every
  predecessor interface actually used by the model

SR-02
  initial state / state class / support signature /
  temporal scope must be explicit

SR-03
  missing optional interfaces are omitted,
  not zero-filled

SR-04
  regular evolution is restricted to one declared
  regular support signature

SR-05
  a status/domain or formation change invalidating
  the regular signature requires an explicit transition

SR-06
  value evolution must not rewrite coordinates
  belonging to inherited channel identity

SR-07
  property status distinctions required by the claim
  must survive numerical or symbolic representation

SR-08
  a property label becomes dynamic operator data only
  through an explicit constitutive bridge

SR-09
  transport / coupling / status transition /
  formation transition remain distinct event classes

SR-10
  every transition output must be a valid initial state
  of the post-transition epoch

SR-11
  branching transition relations do not imply
  deterministic uniqueness

SR-12
  lineage is required when pre/post-transition
  successor identity is claimed

SR-13
  reduced readout equality does not establish
  full trajectory equality or lineage identity

SR-14
  fixed-time simulation slices must recover valid
  predecessor static slices and compatible readouts

SR-15
  conservation / balance claims require the exact
  regular-epoch or transition rule that supports them

SR-16
  continuity / differentiability / PDE / stochastic /
  discrete-time assumptions are supplied by the model,
  not by generic DSD

SR-17
  numerical discretization / approximation requires
  a declared error / convergence / acceptance interface
  appropriate to the claimed trajectory result

SR-18
  finite propagation / c_info claims require the exact
  localization and regularity specialization assumptions

SR-19
  trajectory generation is distinct from a Prediction
  claim about external future truth

SR-20
  Computation / Optimization / Control / Operation /
  Prediction handoffs do not substitute for Simulation
~~~

## 4. Working atomic task — not yet frozen

Prospective formulation:

~~~text
Given:
  a declared simulation task,
  a frozen initial admissible state or initial-state class,
  a declared time or ordered-step domain,
  a declared state representation and support signature,
  supplied regular evolution law(s),
  supplied transition relation(s) where regular signatures change,
  required constitutive / cross-layer bridges,
  lineage rules when successor identity is claimed,
  declared numerical / symbolic / stochastic execution semantics,
  declared readout / observation maps,
  termination / stopping conditions,
  and declared approximation / error semantics when used,

generate or enumerate:
  model-consistent trajectory segment(s),
  typed transition events,
  post-transition admissible state(s),
  lineage records,
  fixed-time static-compatible slices,
  declared readout histories,
  and the maximum simulation claim justified by the supplied model,

without:
  inventing missing evolution or transition laws,
  silently zero-padding missing states,
  rewriting identity-changing transitions as value evolution,
  assuming deterministic uniqueness from a relation-valued transition,
  inferring full state from a lossy readout,
  or promoting model consistency to Prediction validity.
~~~

This formulation is prospective methodological construction, not a theorem supplied by the predecessor papers.

It remains open to direct boundary attack before protocol freeze.

## 5. Candidate information classes for a future Task Interface

Not yet frozen:

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
INITIAL_STATE_ID
INITIAL_STATE_VERSION
INITIAL_STATE_ADMISSIBILITY

STATE_CLASS_ID
STATE_REPRESENTATION_MODE
COMPONENT_REGISTRY

REGULAR_SUPPORT_SIGNATURE_ID
REGULAR_SUPPORT_SIGNATURE_VERSION

EVOLUTION_LAW_ID
EVOLUTION_LAW_VERSION
EVOLUTION_LAW_DOMAIN
EVOLUTION_LAW_REGULARITY_ASSUMPTIONS
EVOLUTION_LAW_PROVENANCE

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

SIMULATION_MODE
  CONTINUOUS
  DISCRETE_STEP
  EVENT_DRIVEN
  STOCHASTIC_IF_SUPPLIED
  SYMBOLIC
  HYBRID

SOLVER_OR_EXECUTION_INTERFACE
SOLVER_VERSION
RANDOM_SEED_OR_SAMPLE_RULE_IF_RELEVANT

APPROXIMATION_RULE
ERROR_METRIC
ERROR_BOUND
CONVERGENCE_OR_STABILITY_INTERFACE
ACCEPTANCE_THRESHOLD

READOUT_REGISTRY
STATIC_SLICE_COMPATIBILITY_CHECK

TERMINATION_RULE
STOPPING_CONDITION

GENERATED_TRAJECTORY_SET
REGULAR_EPOCH_LEDGER
TRANSITION_EVENT_LEDGER
LINEAGE_LEDGER
READOUT_HISTORY

SIMULATION_PRIMARY_STATUS
SIMULATION_TASK_TERMINAL
SIMULATION_PROTOCOL_CONFORMANCE
SIMULATION_METHOD_GAIN_STATUS
~~~

These are recovery candidates only.

They do not yet constitute a required task record.

## 6. Prospective guards to pressure before freezing

~~~text
VALID_INITIAL_STATE
  !=
VALID_EVOLUTION_LAW

MISSING_EVOLUTION_LAW
  !=
ZERO_DYNAMICS

REGULAR_VALUE_EVOLUTION
  !=
STATUS_OR_DOMAIN_TRANSITION

STATUS_OR_DOMAIN_TRANSITION
  !=
FORMATION_TRANSITION

CHANNEL_IDENTITY_CHANGE
  !=
VALUE_CHANGE_ON_ONE_FIXED_CHANNEL

TRANSITION_RELATION
  !=
DETERMINISTIC_JUMP_MAP

ONE_ADMISSIBLE_TRAJECTORY
  !=
UNIQUE_TRAJECTORY

NUMERICAL_TRAJECTORY
  !=
EXACT_TRAJECTORY

DISCRETIZATION_CONVERGENCE
  !=
EMPIRICAL_VALIDITY

EQUAL_READOUT_HISTORY
  !=
EQUAL_COMPONENT_RESOLVED_TRAJECTORY

STATIC_SLICE_VALIDITY
  !=
DYNAMIC_LAW_VALIDITY

REGULAR_EPOCH_CONSERVATION
  !=
TRANSITION_CONSERVATION

SIMULATION_TRAJECTORY
  !=
PREDICTION

SIMULATION_TRAJECTORY
  !=
CONTROL_POLICY

SIMULATION_EXECUTION
  !=
OPERATION_LIFECYCLE

SIMULATION_PLAN
  !=
COMPUTATION_PLAN

NO_GAIN
  !=
METHOD_FAILURE
~~~

Each guard must be attacked before protocol freeze.

## 7. Open interface questions

~~~text
Q1
  Which primary simulation claim levels are needed:
  one trajectory, trajectory family, transition reachability,
  readout history, or bounded approximation?

Q2
  What exact status distinguishes missing evolution law
  from evaluable law with no admissible trajectory?

Q3
  How should relation-valued transitions preserve
  branching without exploding every task into full reachability?

Q4
  When may one trajectory witness satisfy an existential
  simulation claim without asserting uniqueness?

Q5
  What numerical error / convergence interface is required
  before an approximate trajectory counts as established?

Q6
  How should stochastic simulation distinguish:
  one sample path, sample family, distributional claim,
  and Prediction?

Q7
  How should stopping / termination distinguish
  successful terminal state, bounded horizon,
  solver failure, blocked law, and out-of-scope request?

Q8
  Which lineage conditions are required across
  channel / formation transitions?

Q9
  How should fixed-time static-slice compatibility be
  audited for every state without unnecessary overconstraint?

Q10
  How should NO_GAIN be scored against a competent
  non-DSD hybrid simulator using the same laws and data?
~~~

## 8. Initial neighboring-method pressure map

Direct boundary pressure should include at least:

~~~text
Prediction:
  model-consistent trajectory
  vs future-world claim

Control:
  simulate supplied intervention sequence/policy
  vs choose the intervention policy

Operation:
  simulate a lifecycle model
  vs execute/manage the actual repeated lifecycle

Computation:
  determine required evaluations / solver work
  vs generate the trajectory

Optimization:
  select solver / plan / candidate trajectory under objective
  vs generate model-consistent trajectory

Lineage:
  supply predecessor-successor relation
  vs evolve the dynamic state

Tracking:
  record execution / version / process trace
  vs simulation operation

Measurement:
  supply initial / calibration / validation evidence
  vs generate model outputs

Aggregation / Compression:
  produce or reduce readouts
  vs component-resolved trajectory generation

Audit:
  evaluate simulation conformance
  vs execute the simulation
~~~

Additional neighboring pairs may be added during boundary attack.

## 9. Current recovery state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  not established

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
  source_and_registry_recovery_complete

PROTOCOL_REVISION_REQUIRED:
  not applicable before protocol

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 10. Next

Establish the Simulation planning/worklog lane and draft Simulation Task Interface v0.1 before serious pre-protocol boundary attack.
