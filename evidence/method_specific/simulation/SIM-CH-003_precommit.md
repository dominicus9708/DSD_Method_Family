# SIM-CH-003 — Direct Neighboring-Method Simulation Boundary Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-05**  
Challenge ID: `SIM-CH-003`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**  
Case class: `direct_neighboring_method_boundary`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  ea271d04eb09d252299d9420d0fb1191564f5bc6

PROTOCOL_BLOB:
  c3d6f80d99dabb5b84c7a60fd2df3f58bf9dba35

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  S1-S18
~~~

No protocol rule may be changed in response to this challenge.

## 2. Purpose

Test whether Simulation collapses into neighboring Method Family methods when every compared pair receives fair access to the same relevant constructed artifact bundle.

Frozen neighboring methods:

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

This is fixture-bounded method-boundary evidence.

It is not:

~~~text
a permanent irreducibility proof
a method-survival vote
a merger/deletion decision
a superiority claim
an external-validation result
~~~

## 3. Shared artifact bundle

Every pair receives fair access to the relevant parts of one frozen bundle:

~~~text
source/model/interface versions
initial-state/state-class records
regular support signatures
evolution laws
constitutive bridges
transition relations
lineage handoffs
time/horizon records
trajectory quantifier
solver/execution records
numerical error/convergence records
stochastic process/sample records
component-resolved trajectory records
readout maps / information-loss sidecars
measurement observations / uncertainty
aggregation readouts
compression retained-distinction ledgers
transformation maps
tracking provenance/version/process traces
prediction target records
control policy/action records
operation lifecycle/monitoring records
audit criteria/evidence records
computation plans
optimization candidate/objective records
maximum-supported claim
~~~

No compared method receives hidden claim-relevant information unavailable to its partner.

Fair access does not require identical task contracts.

## 4. Five-interface non-collapse rule

For each pair compare:

~~~text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
~~~

Allowed pair result:

~~~text
EXACT_COLLAPSE
PARTIAL_OVERLAP_NOT_COLLAPSE
UNRESOLVED_BOUNDARY
~~~

`EXACT_COLLAPSE` requires no material claim-relevant distinction across all five interfaces in the frozen fixture.

Shared models, state variables, trajectories, maps, observations, or ledgers are insufficient for collapse.

## 5. B1 — Simulation vs Computation

Shared overlap:

~~~text
state variables
update functions
dependency graph
time/horizon
solver/update work
~~~

Frozen distinction:

~~~text
Computation:
  determines what must be evaluated, omitted, reused,
  or symbolically discharged for a declared target

Simulation:
  generates the model-consistent trajectory or trajectory family
  under supplied temporal/update semantics
~~~

Outputs:

~~~text
Computation:
  bounded evaluation plan + soundness ledgers

Simulation:
  trajectory / trajectory family / reachable set /
  dynamic readout history + transition/execution ledgers
~~~

Failure distinction:

~~~text
Computation:
  may succeed without producing any state trajectory

Simulation:
  must satisfy the frozen evolution/transition semantics
  of the requested trajectory claim
~~~

Guard:

~~~text
COMPUTATION_PLAN != SIMULATION_EXECUTION
REQUIRED_UPDATE_SET != GENERATED_TRAJECTORY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 6. B2 — Simulation vs Optimization

Shared overlap:

~~~text
candidate policies/plans
trajectory evidence
resource/cost descriptors
constraints
time/regime semantics
~~~

Frozen distinction:

~~~text
Optimization:
  selects among admissible alternatives
  under objective/constraint semantics

Simulation:
  evolves a supplied model/candidate under its dynamic semantics
~~~

Outputs:

~~~text
Optimization:
  selected alternative / optimum / Pareto or tied set

Simulation:
  model-consistent trajectory result
~~~

Failure distinction:

~~~text
Simulation:
  may correctly generate trajectories for several candidates
  without choosing among them

Optimization:
  requires selection semantics to rank/choose
~~~

Guard:

~~~text
SIMULATION_TRAJECTORY != OPTIMUM
MODEL_EVOLUTION != SELECTION_RULE
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 7. B3 — Simulation vs Measurement

Shared overlap:

~~~text
initial conditions
observations
state variables
uncertainty/error
readout variables
~~~

Frozen distinction:

~~~text
Measurement:
  acquires/defines evidence or determines observational
  distinguishability under a measurement interface

Simulation:
  generates model states from supplied initial/model semantics
~~~

Outputs:

~~~text
Measurement:
  observation/measurement/distinguishability record

Simulation:
  generated trajectory + model-consistency ledgers
~~~

Failure distinction:

~~~text
Measurement:
  insufficient resolution may prevent discrimination

Simulation:
  may consume measured inputs while never performing
  the observation itself
~~~

Guard:

~~~text
MEASUREMENT_RESULT != SIMULATED_STATE
OBSERVED_VALUE != MODEL_GENERATED_VALUE_BY_DEFAULT
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 8. B4 — Simulation vs Aggregation

Shared overlap:

~~~text
component states
readout maps
weights
support information
readout histories
~~~

Frozen distinction:

~~~text
Aggregation:
  constructs a declared composite/readout

Simulation:
  evolves component-resolved states and may emit
  a readout only downstream of those states
~~~

Outputs:

~~~text
Aggregation:
  aggregate/readout + collision/support ledger

Simulation:
  state trajectory + optional readout history
~~~

Failure distinction:

~~~text
Aggregation:
  may validly map distinct sources to the same readout

Simulation:
  may not infer equal state histories from equal readouts
~~~

Guard:

~~~text
AGGREGATE_READOUT != COMPONENT_TRAJECTORY
EQUAL_READOUT_HISTORY != EQUAL_STATE_HISTORY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 9. B5 — Simulation vs Compression

Shared overlap:

~~~text
state representation
reduced trajectory representation
retained distinctions
loss/collision sidecars
~~~

Frozen distinction:

~~~text
Compression:
  reduces representation while preserving declared
  downstream distinctions

Simulation:
  generates model-consistent temporal state evolution
~~~

Outputs:

~~~text
Compression:
  reduced representation + retention/loss ledger

Simulation:
  trajectory / trajectory family + dynamic ledgers
~~~

Failure distinction:

~~~text
Compression:
  may succeed even with intentional information loss
  if declared downstream distinctions are preserved

Simulation:
  fails a full-state claim if a reduced form cannot preserve
  required dynamic distinctions
~~~

Guard:

~~~text
COMPRESSED_TRAJECTORY_REPRESENTATION != SIMULATION_STATE_BY_DEFAULT
REPRESENTATION_PRESERVATION != DYNAMIC_LAW_VALIDITY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 10. B6 — Simulation vs Transformation

Shared overlap:

~~~text
source/target representations
maps
state records
versioned interfaces
preservation/loss records
~~~

Frozen distinction:

~~~text
Transformation:
  maps a source object into a target representation/regime

Simulation:
  advances state through a time/step evolution law
~~~

Outputs:

~~~text
Transformation:
  transformed object + preservation/loss ledger

Simulation:
  time-indexed trajectory + transition/epoch ledger
~~~

Failure distinction:

~~~text
Transformation:
  can be correct with no temporal semantics

Simulation:
  requires the frozen temporal/update semantics
~~~

Guard:

~~~text
TRANSFORMATION_RESULT != TIME_EVOLUTION
REPRESENTATION_MAP != DYNAMIC_LAW_BY_DEFAULT
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 11. B7 — Simulation vs Tracking

Shared overlap:

~~~text
timestamps/step labels
versions
execution records
process stages
provenance
handoffs
~~~

Frozen distinction:

~~~text
Tracking:
  establishes supported trace links for origin/version/process/
  location/handoff/status/reference/evidence

Simulation:
  generates state evolution under supplied dynamic semantics
~~~

Outputs:

~~~text
Tracking:
  trace graph/path/link-status/evidence ledger

Simulation:
  trajectory / transition / solver/readout ledgers
~~~

Failure distinction:

~~~text
Tracking:
  missing provenance remains a trace gap

Simulation:
  missing required provenance may block a model/transition handoff
  but Simulation does not infer the missing trace link
~~~

Guard:

~~~text
TRACKING_TRACE != TRAJECTORY_DYNAMICS
SIMULATION_LOG != TRACKING_PROOF_BY_DEFAULT
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 12. B8 — Simulation vs Lineage

Shared overlap:

~~~text
pre/post states
components
transitions
successor labels
identity-bearing records
~~~

Frozen distinction:

~~~text
Lineage:
  establishes predecessor-successor identity/continuity across change

Simulation:
  consumes lineage when successor identity is claimed
  and generates the dynamic path
~~~

Outputs:

~~~text
Lineage:
  predecessor/successor/coherence ledger

Simulation:
  hybrid trajectory + transition and consumed-lineage ledger
~~~

Failure distinction:

~~~text
Lineage:
  may remain unresolved about successor identity

Simulation:
  may then block/underdetermine identity-bearing trajectory claims
  without establishing lineage itself
~~~

Guard:

~~~text
LINEAGE_HANDOFF != SIMULATION_EXECUTION
TRAJECTORY_CONTINUITY != LINEAGE_IDENTITY_PROOF
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 13. B9 — Simulation vs Prediction

Shared overlap:

~~~text
future-time model states
uncertainty
target variables
trajectory outputs
historical evidence
~~~

Frozen distinction:

~~~text
Simulation:
  generates model-consistent future-labeled states

Prediction:
  asserts relevance to a future external target and therefore
  requires prediction-specific empirical/domain validation
~~~

Outputs:

~~~text
Simulation:
  trajectory / model readout history

Prediction:
  future-target claim / forecast validity status
~~~

Failure distinction:

~~~text
Simulation:
  may be internally correct for the supplied model

Prediction:
  may still be empirically unsupported or false
~~~

Guard:

~~~text
MODEL_CONSISTENT_FUTURE_STATE != FUTURE_WORLD_TRUTH
SIMULATION_SUCCESS != PREDICTION_SUCCESS
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 14. B10 — Simulation vs Control

Shared overlap:

~~~text
states
actions
policies
transition model
controlled trajectory
~~~

Frozen distinction:

~~~text
Control:
  chooses a state-dependent intervention/action policy

Simulation:
  may execute a supplied policy to generate its model trajectory
  but does not choose or validate the policy as Control
~~~

Outputs:

~~~text
Control:
  intervention policy / action mapping / control-validity records

Simulation:
  trajectory under supplied intervention semantics
~~~

Failure distinction:

~~~text
Simulation:
  may faithfully simulate a poor supplied policy

Control:
  fails if the intervention-selection requirement is not met
~~~

Guard:

~~~text
SIMULATING_SUPPLIED_CONTROL_POLICY != CHOOSING_CONTROL_POLICY
CONTROL_POLICY != SIMULATION_TRAJECTORY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 15. B11 — Simulation vs Operation

Shared overlap:

~~~text
schedules
runtime states
monitoring variables
resource records
handoffs/resets
lifecycle model
~~~

Frozen distinction:

~~~text
Operation:
  manages repeated live lifecycle / execution / monitoring / handoff

Simulation:
  generates a model trajectory of such a lifecycle
  without operating the real process
~~~

Outputs:

~~~text
Operation:
  actual execution/lifecycle/monitoring/handoff records

Simulation:
  model lifecycle trajectory/readout records
~~~

Failure distinction:

~~~text
Simulation:
  can succeed on a model even when real operation later fails

Operation:
  depends on actual lifecycle execution and state handling
~~~

Guard:

~~~text
SIMULATING_LIFECYCLE_MODEL != OPERATING_REAL_LIFECYCLE
MODEL_RUN != LIVE_OPERATION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 16. B12 — Simulation vs Audit

Shared overlap:

~~~text
frozen protocol
model/trajectory records
error/transition ledgers
provenance
maximum-supported claim
~~~

Frozen distinction:

~~~text
Simulation:
  generates the trajectory result

Audit:
  retraces and evaluates work/evidence/procedure
  against frozen criteria
~~~

Outputs:

~~~text
Simulation:
  substantive trajectory/status/conformance result

Audit:
  criterion-level findings and audit verdict
~~~

Failure distinction:

~~~text
Simulation:
  BLOCKED/CONFLICTING/UNDERDETERMINED/NOT_ESTABLISHED
  may still be protocol-conformant

Audit:
  may pass precisely because those bounded states were
  correctly preserved and reported
~~~

Guard:

~~~text
SIMULATION_PROTOCOL_CONFORMANCE != GENERAL_AUDIT_PASS
AUDIT_VERDICT != SIMULATION_TRAJECTORY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 17. Source-layer / handoff separation

Simulation legitimately consumes constraints from:

~~~text
Formation
Property
Static Aggregation
Structural Reorganization Dynamics
~~~

and handoffs from neighboring methods.

Required guards:

~~~text
SOURCE_LAYER_HANDOFF != METHOD_IDENTITY
DYNAMICS_LAYER != SIMULATION_METHOD_VALIDATION
STATIC_BRIDGE != DYNAMIC_EVOLUTION_OPERATOR
LINEAGE_HANDOFF != SIMULATION_EXECUTION
MEASUREMENT_HANDOFF != SIMULATION_RESULT
CONTROL_HANDOFF != CONTROL_SELECTION_BY_SIMULATION
~~~

Expected:

~~~text
SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

## 18. Frozen scoring — 108 checks

Each pair receives nine checks.

For every pair B1-B12:

~~~text
-1 shared artifact access fair
-2 INPUTS overlap/difference recorded without identity claim
-3 OPERATION distinction preserved
-4 OUTPUTS distinction preserved
-5 FAILURE/NO_GAIN distinction preserved
-6 VALIDATION_STANDARD distinction preserved
-7 semantic guard preserved
-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
-9 no permanent irreducibility/superiority claim
~~~

Expected:

~~~text
B1  Simulation vs Computation: 9/9
B2  Simulation vs Optimization: 9/9
B3  Simulation vs Measurement: 9/9
B4  Simulation vs Aggregation: 9/9
B5  Simulation vs Compression: 9/9
B6  Simulation vs Transformation: 9/9
B7  Simulation vs Tracking: 9/9
B8  Simulation vs Lineage: 9/9
B9  Simulation vs Prediction: 9/9
B10 Simulation vs Control: 9/9
B11 Simulation vs Operation: 9/9
B12 Simulation vs Audit: 9/9

TOTAL_REQUIRED_CHECKS:
  108

PASS_THRESHOLD:
  108/108

PARTIAL_PASS_ALLOWED:
  no
~~~

## 19. Expected aggregate boundary result

If all 108 checks pass:

~~~text
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  12

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  12

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Counter update on full pass:

~~~text
DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  2 -> 3

SUCCESSFUL_DIRECT_SIMULATION_PILOTS:
  2 -> 3

METHOD_BOUNDARY_SIMULATION_CASES:
  0 -> 1
~~~

Do not change baseline, NO_GAIN, reproducibility, external, or independent-validation counters.

## 20. Interpretation lock

~~~text
FIXTURE_BOUNDED_SEPARATION != PERMANENT_METHOD_IRREDUCIBILITY
PARTIAL_OVERLAP_NOT_COLLAPSE != METHOD_SUPERIORITY
NO_EXACT_COLLAPSE_IN_THIS_FIXTURE != PERMANENT_REGISTRY_SURVIVAL
SHARED_INPUT != SHARED_METHOD_IDENTITY
SHARED_OUTPUT_ARTIFACT != SHARED_OPERATION
NO_GAIN_OR_FAILURE != METHOD_DELETION_PROOF
~~~

## 21. Next

If the frozen bundle passes, proceed to `SIM-CH-004`, a fair competent non-DSD Simulation baseline challenge.

The baseline must receive equal claim-relevant information and must permit `SIMULATION_NO_GAIN` as a valid outcome.
