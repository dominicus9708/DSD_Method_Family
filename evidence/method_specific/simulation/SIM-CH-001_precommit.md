# SIM-CH-001 — Positive Constructed Simulation Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-05**  
Challenge ID: `SIM-CH-001`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**  
Case class: `positive_constructed_multi-form_trajectory`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Purpose

Directly exercise Simulation Protocol v0.1 on positive constructed trajectory forms without using external validation evidence.

The challenge must test:

~~~text
regular deterministic trajectory
declared branching trajectory family
hybrid regular-transition trajectory
post-transition initial-state admissibility
lineage handoff without lineage substitution
fixed-time static-slice conformance
readout collision without state collapse
bounded numerical approximation without exactness overclaim
stochastic sample-path claim without distributional overclaim
simulation of a supplied Control policy without choosing it
Simulation != Prediction
bounded maximum-supported claim
~~~

Method gain is not tested.

## 2. Frozen protocol

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

No protocol rule may be edited in response to this challenge.

## 3. Subtask A — regular deterministic discrete trajectory

Frozen task:

~~~text
TASK_ID:
  SIM-CH-001-A

PRIMARY_CLAIM_LEVEL:
  DECLARED_TRAJECTORY_ON_FIXED_HORIZON

SIMULATION_MODE:
  DISCRETE_STEP

step domain:
  n = 0,1,2,3

state:
  scalar x

initial state:
  x_0 = 1

regular evolution law:
  x_(n+1) = x_n + 2

regular support signature:
  fixed scalar-defined state

trajectory quantifier:
  DECLARED_DETERMINATE_TRAJECTORY
~~~

Expected trajectory:

~~~text
x_0 = 1
x_1 = 3
x_2 = 5
x_3 = 7
~~~

Expected status:

~~~text
INITIAL_STATE_ADMISSIBLE
STATIC_SLICE_CONFORMANT on every generated slice
REGULAR_TRAJECTORY_ESTABLISHED
SIMULATION_PRIMARY_STATUS:
  SIMULATION_ESTABLISHED
SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_ESTABLISHED
SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

Maximum claim is limited to this frozen model and horizon.

## 4. Subtask B — declared branching trajectory family

Frozen task:

~~~text
TASK_ID:
  SIM-CH-001-B

PRIMARY_CLAIM_LEVEL:
  TRAJECTORY_FAMILY_ON_DECLARED_BRANCHING_MODEL

SIMULATION_MODE:
  EVENT_DRIVEN

step domain:
  n = 0,1,2

initial state:
  s0

transition/evolution relation:
  R(s0) = {a,b}
  R(a) = {a2}
  R(b) = {b2}

trajectory quantifier:
  ALL_DECLARED_BRANCHES_ON_SCOPE
~~~

Expected family:

~~~text
branch 1:
  s0 -> a -> a2

branch 2:
  s0 -> b -> b2
~~~

Expected:

~~~text
BRANCH_COVERAGE_STATUS:
  BRANCH_COVERAGE_COMPLETE_ON_DECLARED_SCOPE

UNIQUENESS_EVIDENCE_STATUS:
  UNIQUENESS_NOT_ESTABLISHED

DECLARED_BRANCHING:
  yes

SEMANTIC_UNDERDETERMINATION:
  no

SIMULATION_PRIMARY_STATUS:
  SIMULATION_ESTABLISHED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_ESTABLISHED
~~~

No branch may be discarded merely to make the result deterministic.

## 5. Subtask C — hybrid regular-transition trajectory

Frozen task:

~~~text
TASK_ID:
  SIM-CH-001-C

PRIMARY_CLAIM_LEVEL:
  HYBRID_REGULAR_TRANSITION_TRAJECTORY

time domain:
  [0,2]

epoch J1:
  [0,1)
  support signature Q_A
  formation background F_A
  state coordinate x
  x(t)=t

pre-transition state at tau=1:
  (A, x=1)

transition relation J_AB:
  (A,1) -> (B,10)

post-transition state class:
  Q_B / F_B
  coordinate y

post-transition initial state:
  (B, y=10)

epoch J2:
  [1,2]
  y(t)=10+(t-1)
~~~

Frozen lineage handoff:

~~~text
identity-bearing component:
  e_A -> e_B

lineage relation:
  supplied and valid on transition scope
~~~

Expected:

~~~text
J1:
  regular evolution

tau=1:
  formation/support-changing typed transition

J2:
  new regular epoch

POST_TRANSITION_INITIAL_STATE:
  admissible

LINEAGE_REQUIRED:
  yes

LINEAGE_SUPPLIED:
  yes

TRANSITION_ESTABLISHED:
  yes

STATIC_SLICE_CONFORMANT:
  yes on both epochs

SIMULATION_PRIMARY_STATUS:
  SIMULATION_ESTABLISHED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_ESTABLISHED
~~~

Guards:

~~~text
FORMATION_CHANGE != VALUE_EVOLUTION_OF_ONE_UNCHANGED_CHANNEL
LINEAGE_HANDOFF != SIMULATION_EXECUTION
REGULAR_EPOCH_CONSERVATION != TRANSITION_CONSERVATION
~~~

No conservation-across-transition claim is requested.

## 6. Subtask D — readout collision without state collapse

Frozen task:

~~~text
TASK_ID:
  SIM-CH-001-D

PRIMARY_CLAIM_LEVEL:
  DECLARED_READOUT_HISTORY

step domain:
  n = 0,1,2

two admissible initial states:
  A_0=(1,2)
  B_0=(2,1)

regular law:
  add (1,1) at every step

A_n:
  (1+n,2+n)

B_n:
  (2+n,1+n)

readout:
  O(u,v)=u+v
~~~

Thus:

~~~text
O(A_n)=O(B_n)=3+2n
for n=0,1,2
~~~

while:

~~~text
A_n != B_n
for n=0,1,2
~~~

Expected:

~~~text
READOUT_HISTORY_A:
  {3,5,7}

READOUT_HISTORY_B:
  {3,5,7}

COLLISION_STATUS:
  collision present

STATE_TRAJECTORY_EQUALITY:
  not established

LINEAGE_IDENTITY_FROM_READOUT:
  not established

SIMULATION_PRIMARY_STATUS:
  SIMULATION_ESTABLISHED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_ESTABLISHED
~~~

## 7. Subtask E — bounded numerical approximation

Frozen task:

~~~text
TASK_ID:
  SIM-CH-001-E

PRIMARY_CLAIM_LEVEL:
  APPROXIMATE_TRAJECTORY_WITH_DECLARED_ERROR

model:
  dx/dt = x

initial state:
  x(0)=1

horizon:
  t=0.1

solver:
  one explicit Euler step
  h=0.1

numerical result:
  x_num(0.1)=1.1

reference exact model value:
  exp(0.1)

declared end-to-end error:
  |exp(0.1)-1.1| < 0.006

acceptance threshold:
  0.01
~~~

Expected:

~~~text
SOLVER_TERMINATION_STATUS:
  SOLVER_TERMINATED_NORMALLY

NUMERICAL_CLAIM_KIND:
  NUMERICAL_APPROXIMATE_TRAJECTORY

GLOBAL_OR_END_TO_END_ERROR_STATUS:
  bound established on frozen horizon

NUMERICAL_ACCEPTANCE_STATUS:
  accepted

EXACT_TRAJECTORY_CLAIM:
  not made

SIMULATION_PRIMARY_STATUS:
  SIMULATION_ESTABLISHED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_ESTABLISHED
~~~

Guards:

~~~text
NUMERICAL_ACCEPTANCE != EXACTNESS
LOCAL_ERROR_CONTROL != GLOBAL_ERROR_BOUND
SOLVER_TERMINATED != TRAJECTORY_ESTABLISHED_BY_ITSELF
~~~

## 8. Subtask F — stochastic sample-path claim only

Frozen task:

~~~text
TASK_ID:
  SIM-CH-001-F

PRIMARY_CLAIM_LEVEL:
  DECLARED_TRAJECTORY_ON_FIXED_HORIZON

SIMULATION_MODE:
  STOCHASTIC_SAMPLE_PATH

initial state:
  X_0=0

supplied stochastic rule:
  X_(n+1)=1 if U_n < 0.5
  X_(n+1)=0 otherwise

externally supplied frozen randomness stream:
  U_0=0.2
  U_1=0.8
  U_2=0.4

trajectory quantifier:
  STOCHASTIC_SAMPLE_PATH

STOCHASTIC_CLAIM_KIND:
  SAMPLE_PATH
~~~

Expected path:

~~~text
X_0=0
X_1=1
X_2=0
X_3=1
~~~

Expected:

~~~text
SAMPLE_PATH:
  established for the frozen supplied randomness stream

DISTRIBUTIONAL_CLAIM:
  not requested

EXACT_PROBABILITY_LAW_FROM_SAMPLE:
  not claimed

SEMANTIC_UNDERDETERMINATION:
  no

SIMULATION_PRIMARY_STATUS:
  SIMULATION_ESTABLISHED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_ESTABLISHED
~~~

## 9. Subtask G — simulate supplied policy without Control or Prediction substitution

Frozen task:

~~~text
TASK_ID:
  SIM-CH-001-G

PRIMARY_CLAIM_LEVEL:
  DECLARED_TRAJECTORY_ON_FIXED_HORIZON

state:
  z

initial state:
  z_0=0

supplied policy:
  pi(z)=+1

model update under supplied action:
  z_(n+1)=z_n + pi(z_n)

horizon:
  n=0,1,2

policy provenance:
  supplied by external Control-side interface
  not selected by Simulation
~~~

Expected trajectory:

~~~text
z_0=0
z_1=1
z_2=2
~~~

Expected boundary record:

~~~text
SIMULATING_SUPPLIED_CONTROL_POLICY:
  yes

CHOOSING_CONTROL_POLICY:
  no

PREDICTION_TRUTH_CLAIM:
  no

OPERATION_EXECUTION_CLAIM:
  no

SIMULATION_PRIMARY_STATUS:
  SIMULATION_ESTABLISHED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_ESTABLISHED

SIMULATION_METHOD_GAIN_STATUS:
  SIMULATION_GAIN_NOT_TESTED
~~~

## 10. Global challenge guards

Across all subtasks preserve:

~~~text
MISSING_EVOLUTION_LAW != ZERO_DYNAMICS
INITIAL_STATE_VALUE_PRESENT != INITIAL_STATE_ADMISSIBLE
REGULAR_VALUE_EVOLUTION != STATUS_OR_DOMAIN_TRANSITION
FORMATION_CHANGE != VALUE_EVOLUTION_OF_ONE_UNCHANGED_CHANNEL
TRANSITION_RELATION != DETERMINISTIC_JUMP_MAP
DECLARED_BRANCHING != SEMANTIC_UNDERDETERMINATION
ONE_TRAJECTORY_WITNESS != UNIQUE_TRAJECTORY
READOUT_HISTORY != COMPONENT_RESOLVED_TRAJECTORY
EQUAL_READOUT_HISTORY != EQUAL_TRAJECTORY
NUMERICAL_TRAJECTORY != EXACT_TRAJECTORY
ONE_STOCHASTIC_SAMPLE_PATH != DISTRIBUTIONAL_CLAIM
SIMULATION_TRAJECTORY != PREDICTION_CLAIM
SIMULATING_SUPPLIED_CONTROL_POLICY != CHOOSING_CONTROL_POLICY
SIMULATION_ESTABLISHED may coexist with SIMULATION_GAIN_NOT_TESTED
~~~

No external validation, empirical future truth, universal law, or method-gain claim may be inferred.

## 11. Frozen scoring — 84 checks

Each subtask receives twelve checks.

### A — regular deterministic trajectory

~~~text
A1 task/model/horizon frozen
A2 initial state admissible
A3 support signature fixed
A4 evolution law frozen
A5 x0=1 retained
A6 x1=3 derived
A7 x2=5 derived
A8 x3=7 derived
A9 all required slices conformant
A10 regular trajectory established
A11 terminal established
A12 maximum claim bounded to model/horizon
~~~

### B — branching trajectory family

~~~text
B1 initial state frozen
B2 relation R frozen
B3 quantifier ALL_DECLARED_BRANCHES_ON_SCOPE frozen
B4 branch s0-a-a2 generated
B5 branch s0-b-b2 generated
B6 no branch discarded
B7 branch coverage complete
B8 uniqueness not established
B9 branching not underdetermination
B10 trajectory family established
B11 terminal established
B12 no deterministic-jump overclaim
~~~

### C — hybrid transition trajectory

~~~text
C1 J1/Q_A/F_A frozen
C2 J1 regular evolution retained
C3 transition trigger tau=1 frozen
C4 J_AB frozen
C5 formation/support change not hidden as value evolution
C6 post-transition state (B,10) admissible
C7 J2/Q_B/F_B frozen
C8 J2 regular evolution retained
C9 lineage required and supplied
C10 no transition-conservation claim invented
C11 static-slice conformance retained
C12 terminal established
~~~

### D — readout collision

~~~text
D1 both initial states retained
D2 component trajectories generated separately
D3 A != B on every frozen step
D4 readout rule frozen
D5 readout history A = {3,5,7}
D6 readout history B = {3,5,7}
D7 collision retained
D8 readout equality not state equality
D9 readout equality not lineage identity
D10 component-resolved states retained
D11 primary established
D12 terminal established
~~~

### E — numerical approximation

~~~text
E1 model/initial state/horizon frozen
E2 Euler rule frozen
E3 numerical result 1.1 retained
E4 exact reference exp(0.1) retained
E5 end-to-end error bound <0.006 retained
E6 acceptance threshold 0.01 retained
E7 solver terminated normally
E8 numerical acceptance established
E9 approximation not relabeled exact
E10 solver termination not sole validity basis
E11 primary established
E12 terminal established
~~~

### F — stochastic sample path

~~~text
F1 stochastic rule frozen
F2 supplied randomness stream frozen
F3 claim kind SAMPLE_PATH frozen
F4 X1=1 derived
F5 X2=0 derived
F6 X3=1 derived
F7 sample path established
F8 no distributional claim
F9 no exact probability law inferred
F10 expected stochastic multiplicity not semantic underdetermination
F11 primary established
F12 terminal established
~~~

### G — neighboring-method boundary

~~~text
G1 supplied policy frozen
G2 policy provenance retained
G3 z0=0 retained
G4 z1=1 derived
G5 z2=2 derived
G6 Simulation does not choose policy
G7 no Prediction truth claim
G8 no Operation execution claim
G9 Simulation trajectory established
G10 task terminal established
G11 method gain = SIMULATION_GAIN_NOT_TESTED
G12 bounded maximum claim retained
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  84

PASS_THRESHOLD:
  84/84

PARTIAL_PASS_ALLOWED:
  no
~~~

## 12. Allowed counter changes on 84/84 PASS

~~~text
DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  0 -> 1

SUCCESSFUL_DIRECT_SIMULATION_PILOTS:
  0 -> 1

POSITIVE_SIMULATION_CASES:
  0 -> 1
~~~

Unchanged:

~~~text
NEGATIVE_OR_UNRESOLVED_SIMULATION_CASES:
  0

METHOD_BOUNDARY_SIMULATION_CASES:
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
~~~

## 13. Next on full PASS

If all 84 checks pass, proceed to:

~~~text
SIM-CH-002
negative / blocked / conflicting / underdetermined /
out-of-scope / PARTIAL terminal coverage
~~~
