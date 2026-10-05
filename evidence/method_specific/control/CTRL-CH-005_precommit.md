# CTRL-CH-005 — Strongest-Reasonable Non-DSD Control Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**

~~~text
PROTOCOL_COMMIT:
  cda84e4298be81993a571f8f1277b3c7530c6057
PROTOCOL_BLOB:
  bb22a9b8ebca8d11fd29ae9eb072021e45130881

BASELINE_ID:
  B1_STRONG_VERSIONED_HYBRID_FEEDBACK_CONTROLLER

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_controller

BASELINE_USES_DSD_AXIOMS:
  no

EQUAL_INFORMATION_ACCESS:
  yes
~~~

B1 may use conventional controller features:

~~~text
versioned state estimator
explicit target and target region
admissible-action filter
hard safety constraints
state-feedback policy
event-triggered update
hybrid mode transition table
reachability certificate on declared scope
constraint/safety override
historical policy versions
one-step rollout / supplied simulation
ordinary status and error codes
predeclared post-action verification rule
~~~

Frozen cases:

~~~text
R1 version lock:
  decision D1 uses state-estimate version S1
  later S2 arrives
  historical D1 remains bound to S1

R2 reachability:
  state x=0
  target x=2
  action set {0,1}
  horizon 2
  model x_(k+1)=x_k+a_k
  target reachable with [1,1]

R3 hard safety:
  state x=0
  actions {1,3}
  hard x'<=2
  action 3 excluded
  no penalty substitution

R4 hybrid mode:
  mode A --switch--> B
  typed mode/state transition table supplied
  predecessor/successor identity record supplied

R5 feedback/update:
  P1 state-feedback policy
  new observation at d1
  P2 records parent P1 and new cutoff
  P1 retained

R6 reduced readout:
  O(u,v)=u+v
  target O=7
  two full states may share O=7
  target claim remains readout-bounded

R7 neighboring boundaries:
  rollout != policy selection
  forecast != action
  one-time optimum != feedback policy
  control decision != live operation
~~~

Gain axes:

~~~text
G1 decision/state version integrity
G2 reachability/target discipline
G3 hard-constraint/safety discipline
G4 hybrid transition/identity discipline
G5 feedback/update non-retroactivity
G6 readout/information-loss discipline
G7 neighboring-method separation
~~~

If all seven axes are BASELINE_MATCH:

~~~text
CONTROL_METHOD_GAIN_STATUS:
  CONTROL_NO_GAIN

STRONGEST_REASONABLE_BASELINE_CONTROL:
  established_at_constructed_evidence_level
~~~

Frozen scoring:

~~~text
fairness and version integrity:
  12
R2 reachability:
  10
R3 hard safety:
  12
R4 hybrid transition:
  12
R5 feedback/update:
  12
R6 readout:
  10
R7 boundaries:
  8
gain conclusion:
  6

TOTAL_REQUIRED_CHECKS:
  82
PASS_THRESHOLD:
  82/82
PARTIAL_PASS_ALLOWED:
  no
~~~

On full pass:

~~~text
DIRECT_CONTROL_PILOTS_ATTEMPTED:
  4 -> 5
SUCCESSFUL_DIRECT_CONTROL_PILOTS:
  4 -> 5
BASELINE_CONTROL_CASES:
  1 -> 2
NO_GAIN_CONTROL_CASES:
  1 -> 2
STRONGEST_REASONABLE_BASELINE_CONTROL:
  established_at_constructed_evidence_level
~~~

The strongest-reasonable label is bounded to this constructed comparator and is not universal.

Next on full pass: CTRL-CH-006 deterministic same-project retrace.
