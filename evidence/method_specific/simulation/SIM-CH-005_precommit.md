# SIM-CH-005 — Strongest-Reasonable Non-DSD Simulation Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**  
Challenge ID: `SIM-CH-005`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**  
Case class: `strongest_reasonable_baseline_constructed`  
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
  B1_STRONG_HYBRID_SIMULATION_ENGINE

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_simulator

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes

BASELINE_WEAKENING_AFTER_PRECOMMIT:
  prohibited
~~~

B1 is materially stronger than B0.

It may use ordinary non-DSD mechanisms including:

~~~text
versioned model/interface registries
typed state-domain validation
deterministic and relation-valued transitions
hybrid event processing
branch-complete finite exploration
reachable-set enumeration on finite scope
explicit lineage/identity sidecars when supplied
symbolic execution
exact finite-step execution
interval enclosures
adaptive numerical integration
local/global error propagation
stability/convergence sidecars
stochastic sample paths
finite stochastic ensembles
empirical summary generation
readout/noninjectivity sidecars
terminal-precedence engine
bounded maximum-claim reporting
deterministic rerun manifests
~~~

B1 may choose any sound ordinary simulation algorithm suitable for the frozen task.

Algorithm choice itself is not a gain axis.

## 3. Equal-information rule

Simulation and B1 receive exactly the same claim-relevant:

~~~text
task / version / primary claim / maximum claim
model identity/version/scope
time/step domain and horizon
state class / state representation / component registry
initial-state interface
regular support signatures / epoch declarations
evolution laws
constitutive dynamic bridges
transition relations / transition balance rules when supplied
lineage handoffs
trajectory quantifier / branch coverage requirement
readout maps / collision/injectivity sidecars
solver/discretization/error/convergence semantics
stochastic process/randomness/sample semantics
neighboring-method handoff records
terminal precedence
~~~

No hidden favorable inputs are supplied to either side.

## 4. R1 — versioned model non-retroactivity

Frozen task v1:

~~~text
TASK_VERSION:
  v1

MODEL_VERSION:
  M-v1

state:
  x

x_0=1

law M-v1:
  x_(n+1)=2*x_n

horizon:
  n=0..2
~~~

Expected v1:

~~~text
trajectory:
  {1,2,4}
~~~

A later model version is then supplied:

~~~text
MODEL_VERSION:
  M-v2

law M-v2:
  x_(n+1)=3*x_n
~~~

Expected:

~~~text
TASK-v1 remains bound to M-v1
v1 trajectory remains {1,2,4}
new v2 task may generate {1,3,9}
M-v2 does not retroactively rewrite v1
~~~

Guards:

~~~text
NEWER_MODEL_VERSION != RETROACTIVE_REINTERPRETATION
TASK_VERSION_LOCK != LATEST_MODEL_WINS
~~~

## 5. R2 — branch-complete hybrid transition with supplied lineage

Frozen model:

~~~text
initial:
  s0

regular step:
  s0 -> p

event transition at p:
  J(p)={q1,q2}

post-transition branches:
  q1 -> r1
  q2 -> r2

trajectory quantifier:
  ALL_DECLARED_BRANCHES_ON_SCOPE
~~~

Supplied lineage sidecar:

~~~text
pre identity-bearing component:
  e_p

post branch components:
  e_q1
  e_q2

lineage relation:
  e_p -> {e_q1,e_q2}
~~~

Expected:

~~~text
branches:
  s0->p->q1->r1
  s0->p->q2->r2

branch coverage:
  complete on declared scope

uniqueness:
  not established

lineage:
  consumed, not generated

declared branching:
  not semantic underdetermination
~~~

## 6. R3 — bounded numerical enclosure

Frozen model:

~~~text
dx/dt=-x
x(0)=1
horizon:
  t in [0,1]
~~~

Frozen numerical interface:

~~~text
method:
  supplied interval-capable numerical integrator

certified end-to-end enclosure at t=1:
  x(1) in [0.367,0.369]

reference model value:
  exp(-1)

requested acceptance:
  enclosure width <=0.003
  and reference value lies inside enclosure
~~~

Expected:

~~~text
enclosure width:
  0.002

reference exp(-1):
  inside [0.367,0.369]

NUMERICAL_ACCEPTANCE:
  established on frozen horizon

EXACTNESS:
  not claimed
~~~

No stronger global-time claim is allowed.

## 7. R4 — stochastic finite ensemble without probability-law overclaim

Frozen stochastic model:

~~~text
X_0=0

update:
  X_(n+1)=X_n + B_n

B_n in {0,1}

supplied frozen randomness streams:
  stream A: {0,1,0}
  stream B: {1,1,0}
  stream C: {0,0,1}

horizon:
  n=0..3
~~~

Generated sample paths:

~~~text
A:
  {0,0,1,1}

B:
  {0,1,2,2}

C:
  {0,0,0,1}
~~~

Frozen stochastic claim:

~~~text
STOCHASTIC_CLAIM_KIND:
  FINITE_ENSEMBLE

SAMPLE_COUNT:
  3

requested empirical final-state mean:
  (1+2+1)/3 = 4/3
~~~

Expected:

~~~text
three sample paths retained
empirical final-state mean = 4/3
finite ensemble summary established

exact probability law:
  not claimed

distributional convergence:
  not claimed
~~~

## 8. R5 — readout collision, transition status, and neighboring-method handoffs

### R5A — readout collision

~~~text
state A=(2,5)
state B=(3,4)

readout:
  O(u,v)=u+v
~~~

Expected:

~~~text
O(A)=O(B)=7
A != B
no state-identity inference
~~~

### R5B — evaluable status/domain transition

Frozen model:

~~~text
pre-transition property status:
  APPLICABLE_BUT_UNDEFINED

transition:
  supplied status/domain transition

post-transition property status:
  DEFINED_ZERO
~~~

Expected:

~~~text
status transition retained as typed transition
not represented as numeric 0 evolving from undefined
~~~

### R5C — Control / Prediction / Operation handoffs

Frozen requests:

~~~text
Q1:
  simulate supplied policy pi
  -> Simulation in scope

Q2:
  choose policy pi
  -> Control handoff

Q3:
  assert future-world target truth
  -> Prediction handoff

Q4:
  execute and monitor live repeated lifecycle
  -> Operation handoff
~~~

Expected:

~~~text
Simulation executes Q1 only
Q2/Q3/Q4 remain neighboring-method requests
~~~

## 9. R6 — terminal-pressure / status preservation

Independent required obligations:

~~~text
Q1:
  future-world truth request
  -> OUT_OF_SCOPE

Q2:
  incompatible applicable laws
  -> CONFLICTING

Q3:
  multiple admissible unresolved model semantics
  -> UNDERDETERMINED

Q4:
  required transition interface unavailable
  -> BLOCKED
~~~

Expected final task terminal:

~~~text
SIMULATION_TASK_OUT_OF_SCOPE
~~~

with all lower states retained.

## 10. Frozen gain axes

~~~text
G1 versioned task/model non-retroactivity discipline

G2 branch-complete hybrid/lineage discipline

G3 numerical enclosure/error/maximum-claim discipline

G4 stochastic ensemble/sample-coverage discipline

G5 readout/status-transition/neighboring-method boundary discipline

G6 terminal-precedence and lower-state retention discipline

G7 deterministic ledger / equal-information / bounded-claim discipline
~~~

Allowed axis result:

~~~text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
~~~

Overall rule:

~~~text
if all seven axes and claim-relevant outputs match:
  SIMULATION_METHOD_GAIN_STATUS =
    SIMULATION_NO_GAIN

if a frozen axis establishes a DSD advantage:
  SIMULATION_GAIN_ESTABLISHED

if a frozen axis establishes a B1 advantage:
  preserve BASELINE_ADVANTAGE

otherwise:
  SIMULATION_GAIN_UNDERDETERMINED
~~~

## 11. Strongest-reasonable interpretation rule

On full pass with equal-information access:

~~~text
STRONGEST_REASONABLE_BASELINE_SIMULATION:
  established_at_constructed_evidence_level
~~~

This must not be interpreted as:

~~~text
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE
~~~

Required guards:

~~~text
STRONGEST_REASONABLE_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE

NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

## 12. Frozen scoring — 82 checks

### A. Fairness / strength / immutability — 12

~~~text
A1 Simulation Protocol commit/blob fixed
A2 B1 identity frozen
A3 B1 materially stronger than B0
A4 B1 capability frozen before execution
A5 R1-R6 frozen before execution
A6 equal-information access
A7 B1 receives every claim-relevant Simulation-visible input
A8 Simulation receives no hidden favorable input
A9 no baseline weakening after precommit
A10 no post-hoc gain axis
A11 external application remains no
A12 strongest-reasonable label bounded to constructed evidence
~~~

### B. R1 version / non-retroactivity — 10

~~~text
B1 v1 task frozen
B2 M-v1 frozen
B3 v1 trajectory {1,2,4}
B4 M-v2 arrives later
B5 M-v2 law retained
B6 v1 not retroactively rewritten
B7 v2 may generate {1,3,9}
B8 version provenance retained
B9 latest-model-wins rejected
B10 outputs match
~~~

### C. R2 hybrid branching / lineage — 12

~~~text
C1 initial state frozen
C2 regular pre-event step retained
C3 relation-valued event transition retained
C4 branch q1 generated
C5 branch q2 generated
C6 both post branches extended
C7 branch coverage complete
C8 uniqueness not established
C9 declared branching not underdetermination
C10 supplied lineage relation retained
C11 lineage not generated by Simulation
C12 outputs match
~~~

### D. R3 numerical enclosure — 10

~~~text
D1 model/initial/horizon frozen
D2 enclosure [0.367,0.369] retained
D3 enclosure width 0.002
D4 acceptance width threshold satisfied
D5 exp(-1) lies inside enclosure
D6 numerical acceptance established
D7 exactness not claimed
D8 no unbounded-time claim
D9 maximum claim bounded
D10 outputs match
~~~

### E. R4 stochastic ensemble — 12

~~~text
E1 stochastic rule frozen
E2 three frozen randomness streams retained
E3 path A reconstructed
E4 path B reconstructed
E5 path C reconstructed
E6 sample count=3 retained
E7 empirical final-state mean=4/3
E8 finite ensemble summary established
E9 exact probability law not claimed
E10 distributional convergence not claimed
E11 finite ensemble not semantic underdetermination
E12 outputs match
~~~

### F. R5-R6 boundaries / terminal discipline — 14

~~~text
F1 readout collision retained
F2 no state identity inferred
F3 undefined->defined-zero status transition retained as typed transition
F4 undefined not replaced by numeric zero
F5 supplied policy simulation remains in Simulation
F6 policy selection handed to Control
F7 future-world truth handed to Prediction
F8 live lifecycle handed to Operation
F9 OUT_OF_SCOPE subordinate retained
F10 CONFLICTING subordinate retained
F11 UNDERDETERMINED subordinate retained
F12 BLOCKED subordinate retained
F13 final terminal OUT_OF_SCOPE
F14 outputs match
~~~

### G. Gain conclusion — 12

~~~text
G1 seven gain axes scored only from frozen outputs
G2 G1 axis BASELINE_MATCH
G3 G2 axis BASELINE_MATCH
G4 G3 axis BASELINE_MATCH
G5 G4 axis BASELINE_MATCH
G6 G5 axis BASELINE_MATCH
G7 G6 axis BASELINE_MATCH
G8 G7 axis BASELINE_MATCH
G9 equal-information fairness retained
G10 overall SIMULATION_NO_GAIN follows
G11 strongest-reasonable constructed-evidence status follows
G12 no universalization or method-deletion inference
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASS_THRESHOLD:
  82/82

PARTIAL_PASS_ALLOWED:
  no
~~~

## 13. Allowed counter changes on 82/82 PASS

~~~text
DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  4 -> 5

SUCCESSFUL_DIRECT_SIMULATION_PILOTS:
  4 -> 5

BASELINE_SIMULATION_CASES:
  1 -> 2
~~~

If all seven gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_SIMULATION_CASES:
  1 -> 2

STRONGEST_REASONABLE_BASELINE_SIMULATION:
  established_at_constructed_evidence_level
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

## 14. Next

On full pass, prospectively precommit and execute `SIM-CH-006`, a deterministic same-project retrace of SIM-CH-001~005.

The retrace must freeze its reconstruction ledger before formal comparison with the historical result artifacts.
