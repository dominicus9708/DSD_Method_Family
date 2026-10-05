# SIM-CH-004 — Competent Non-DSD Simulation Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**  
Challenge ID: `SIM-CH-004`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

~~~text
SIMULATION_PROTOCOL_COMMIT:
  ea271d04eb09d252299d9420d0fb1191564f5bc6

SIMULATION_PROTOCOL_BLOB:
  c3d6f80d99dabb5b84c7a60fd2df3f58bf9dba35

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  S1-S18
~~~

No Simulation Protocol rule may be changed in response to this baseline.

## 2. Baseline identity

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_HYBRID_SIMULATOR

BASELINE_CLASS:
  competent_non_DSD_constructed_simulator

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
~~~

B0 may use ordinary simulation machinery:

~~~text
typed state records
explicit initial-state admissibility checks
discrete/continuous update laws
relation-valued branching transitions
hybrid event/transition handling
state-domain validation at each required slice
explicit readout maps
numerical approximation/error acceptance
stochastic sample-path execution
status classes for missing/conflicting/ambiguous interfaces
bounded claim reporting
~~~

B0 may not invoke Formation, Property, Static Aggregation, Structural Reorganization Dynamics, or DSD shared-core rules as theory.

Terminology or file organization is never counted as Simulation gain.

## 3. Equal-information rule

Simulation and B0 receive the same claim-relevant:

~~~text
task / version / primary claim / maximum claim
model identity/version/scope
time or ordered-step horizon
state class / component representation
initial state / initial-state admissibility information
regular support / epoch declarations when used
evolution laws
transition relations
lineage handoff records when supplied
branch quantifier / branch-completeness requirement
readout maps / collision information
solver / discretization / error semantics
stochastic process / supplied randomness stream
neighboring-method handoff records
terminal precedence
~~~

Neither side receives hidden favorable information.

## 4. Frozen fixtures

### Q1 — regular deterministic trajectory

Reuse the core of `SIM-CH-001-A`.

~~~text
x_0=1
x_(n+1)=x_n+2
n=0..3

expected:
  {1,3,5,7}
~~~

Both evaluators must return the same frozen trajectory and bounded horizon claim.

### Q2 — declared branching trajectory family

Reuse `SIM-CH-001-B`.

~~~text
R(s0)={a,b}
R(a)={a2}
R(b)={b2}

trajectory quantifier:
  ALL_DECLARED_BRANCHES_ON_SCOPE
~~~

Expected:

~~~text
{s0->a->a2, s0->b->b2}
branch coverage complete
uniqueness not established
declared branching != underdetermined
~~~

### Q3 — hybrid typed transition

Reuse `SIM-CH-001-C`.

~~~text
J1:
  Q_A/F_A
  x(t)=t
  0<=t<1

transition:
  (A,1)->(B,10)

J2:
  Q_B/F_B
  y(t)=10+(t-1)
  1<=t<=2

lineage handoff:
  supplied
~~~

Expected:

~~~text
regular epoch J1 retained
typed support/formation-changing transition retained
post-transition initial state admissible
regular epoch J2 retained
lineage handoff retained
no cross-transition conservation invented
~~~

### Q4 — readout collision without state collapse

Reuse `SIM-CH-001-D`.

~~~text
A_n=(1+n,2+n)
B_n=(2+n,1+n)
O(u,v)=u+v
n=0,1,2
~~~

Expected:

~~~text
O(A)=O(B)={3,5,7}
A_n != B_n on every step
readout equality != state equality
readout equality != lineage identity
~~~

### Q5 — numerical approximation and stochastic sample path

Q5A reuses `SIM-CH-001-E`.

~~~text
dx/dt=x
x(0)=1
one explicit Euler step h=0.1
x_num(0.1)=1.1
certified end-to-end error <0.006
acceptance threshold 0.01
~~~

Expected:

~~~text
numerical approximation accepted
exactness not claimed
~~~

Q5B reuses `SIM-CH-001-F`.

~~~text
X_0=0
U={0.2,0.8,0.4}
X_(n+1)=1 if U_n<0.5 else 0
~~~

Expected:

~~~text
sample path {0,1,0,1}
no distributional claim
no exact probability law inferred
~~~

### Q6 — negative/status boundary bundle

Reuse selected `SIM-CH-002` semantics.

Q6A:

~~~text
required evolution law unavailable

expected:
  BLOCKED
  no zero-dynamics default
~~~

Q6B:

~~~text
two incompatible applicable evolution laws
no resolver

expected:
  CONFLICTING
~~~

Q6C:

~~~text
two admissible unresolved model semantics
different trajectory results
no declared branching relation
no resolver

expected:
  UNDERDETERMINED
~~~

Q6D:

~~~text
requested claim:
  external future-world truth

expected:
  OUT_OF_SCOPE for Simulation
  Prediction handoff
~~~

## 5. Frozen gain axes

~~~text
G1 trajectory-generation correctness on frozen regular model

G2 branch / hybrid-transition / lineage-handoff discipline

G3 readout-information-loss / state-identity discipline

G4 numerical / stochastic claim discipline

G5 blocked / conflicting / underdetermined / out-of-scope discipline

G6 claim-relevant Simulation outcome equivalence
   under equal-information access
~~~

Allowed axis result:

~~~text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
~~~

Overall gain rule:

~~~text
if all six axes and claim-relevant outputs match:
  SIMULATION_METHOD_GAIN_STATUS =
    SIMULATION_NO_GAIN

if one or more frozen axes establish a DSD advantage:
  SIMULATION_GAIN_ESTABLISHED

if one or more axes establish a baseline advantage:
  preserve BASELINE_ADVANTAGE

otherwise:
  SIMULATION_GAIN_UNDERDETERMINED
~~~

Vocabulary and DSD naming are not gain axes.

## 6. Frozen scoring — 64 checks

### A. Fairness and immutability — 10

~~~text
A1 Simulation Protocol commit/blob fixed
A2 B0 operation frozen before execution
A3 output mappings frozen
A4 Q1-Q6 frozen before execution
A5 equal-information rule respected
A6 B0 receives every claim-relevant Simulation-visible input
A7 Simulation receives no hidden favorable input
A8 no post-hoc gain axis added
A9 no baseline rule changed after result inspection
A10 external application remains no
~~~

### B. Q1 regular deterministic trajectory — 8

~~~text
B1 same initial state
B2 same update law
B3 same horizon
B4 x1=3 on both
B5 x2=5 on both
B6 x3=7 on both
B7 established terminal on both
B8 bounded claim matches
~~~

### C. Q2 branching family — 10

~~~text
C1 same relation R
C2 same branch quantifier
C3 branch s0-a-a2 on both
C4 branch s0-b-b2 on both
C5 no branch discarded
C6 branch coverage complete on both
C7 uniqueness not established on both
C8 branching not relabeled underdetermined
C9 established terminal on both
C10 bounded claim matches
~~~

### D. Q3 hybrid transition — 10

~~~text
D1 same J1 semantics
D2 same typed transition
D3 same J2 semantics
D4 formation/support change retained
D5 post-transition initial state admissible
D6 lineage handoff retained
D7 lineage not generated by Simulation
D8 no transition conservation invented
D9 static-slice validity retained
D10 terminal matches
~~~

### E. Q4-Q5 readout / numerical / stochastic — 12

~~~text
E1 same A/B component trajectories
E2 same readout map
E3 readout histories both {3,5,7}
E4 state trajectories remain distinct
E5 no lineage identity inferred from readout
E6 same Euler result 1.1
E7 same declared error bound and threshold
E8 numerical acceptance matches
E9 exactness not claimed
E10 same supplied randomness stream
E11 same sample path {0,1,0,1}
E12 no distributional overclaim
~~~

### F. Q6 negative/status bundle — 10

~~~text
F1 missing law remains BLOCKED on both
F2 neither supplies zero dynamics
F3 conflicting laws remain CONFLICTING on both
F4 neither picks one conflicting law
F5 unresolved semantics remain UNDERDETERMINED on both
F6 unresolved semantics not relabeled declared branching
F7 future-world truth remains OUT_OF_SCOPE on both
F8 Prediction handoff retained
F9 four status classes remain distinct
F10 corresponding task terminals match
~~~

### G. Gain conclusion — 4

~~~text
G1 six gain axes scored only from frozen outputs
G2 equal-information fairness remains visible
G3 NO_GAIN preserved if all six axes are BASELINE_MATCH
G4 NO_GAIN does not imply failure/deletion/merger/absorption/redundancy
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  64

PASS_THRESHOLD:
  64/64

PARTIAL_PASS_ALLOWED:
  no
~~~

## 7. Allowed counter changes on 64/64 PASS

~~~text
DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  3 -> 4

SUCCESSFUL_DIRECT_SIMULATION_PILOTS:
  3 -> 4

BASELINE_SIMULATION_CASES:
  0 -> 1
~~~

If all six gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_SIMULATION_CASES:
  0 -> 1
~~~

Unchanged:

~~~text
POSITIVE_SIMULATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_SIMULATION_CASES:
  1

METHOD_BOUNDARY_SIMULATION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  12

REPRODUCIBILITY_CASES:
  0

EXTERNAL_SIMULATION_APPLICATIONS:
  0

INDEPENDENT_SIMULATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established
~~~

## 8. Interpretation lock

A fair `SIMULATION_NO_GAIN` result means only:

~~~text
no claim-relevant DSD Simulation advantage over this competent
constructed non-DSD simulator was established for the frozen
tasks under equal-information access
~~~

It does not mean:

~~~text
Simulation Protocol failure
method deletion
merger into Computation
merger into Dynamics source layer
merger into Prediction/Control/Operation
permanent redundancy
future DSD gain is impossible
~~~

Required guards:

~~~text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

## 9. Next

After execution, if all frozen outputs match and the result is NO_GAIN, proceed to a strongest-reasonable non-DSD Simulation baseline challenge.
