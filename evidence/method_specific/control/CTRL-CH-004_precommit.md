# CTRL-CH-004 — Competent Non-DSD Control Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**

~~~text
PROTOCOL_COMMIT:
  cda84e4298be81993a571f8f1277b3c7530c6057
PROTOCOL_BLOB:
  bb22a9b8ebca8d11fd29ae9eb072021e45130881

BASELINE_ID:
  B0_GENERIC_VERSIONED_FEEDBACK_CONTROLLER

BASELINE_CLASS:
  competent_non_DSD_constructed_controller

BASELINE_USES_DSD_AXIOMS:
  no

EQUAL_INFORMATION_ACCESS:
  required
~~~

B0 may use ordinary control-engineering bookkeeping:

~~~text
versioned state estimate
declared target
admissible action set
action-effect model
hard constraints
feedback policy
event triggers
policy updates
historical decision retention
status codes for unavailable/conflicting inputs
~~~

Frozen fixtures:

~~~text
Q1 one-step action:
  x=0
  target x'=2
  action set {0,1,2}
  x'=x+a
  expected action 2

Q2 feedback policy:
  x in {0,1,2}
  if x<2 choose 1
  if x=2 choose 0

Q3 open-loop sequence:
  x0=0
  sequence [1,1]
  two-step target 2

Q4 hard constraint:
  actions {1,3}
  x'=x+a
  target [1,2]
  hard x'<=2
  action 1 retained / action 3 excluded

Q5 typed transition bookkeeping:
  mode A --switch--> mode B
  successor identity record supplied

Q6 policy update:
  P1 historical
  new observation at d1
  P2 parent P1
  no retroactive rewrite

Q7 negative/status bundle:
  missing effect bridge -> BLOCKED
  conflicting effect models -> CONFLICTING
  unresolved policy semantics -> UNDERDETERMINED
  live execution request -> OUT_OF_SCOPE
~~~

Gain axes:

~~~text
G1 state/target/action version discipline
G2 action-effect and constraint discipline
G3 feedback/open-loop distinction
G4 transition/update history discipline
G5 status/terminal discipline
G6 neighboring-method separation
~~~

Allowed per-axis result:

~~~text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
~~~

If all six axes are BASELINE_MATCH:

~~~text
CONTROL_METHOD_GAIN_STATUS:
  CONTROL_NO_GAIN
~~~

Frozen scoring:

~~~text
fairness/immutability:
  10
Q1-Q2:
  12
Q3-Q4:
  12
Q5-Q6:
  12
Q7:
  10
gain conclusion:
  8

TOTAL_REQUIRED_CHECKS:
  64
PASS_THRESHOLD:
  64/64
PARTIAL_PASS_ALLOWED:
  no
~~~

On full pass with all axes BASELINE_MATCH:

~~~text
DIRECT_CONTROL_PILOTS_ATTEMPTED:
  3 -> 4
SUCCESSFUL_DIRECT_CONTROL_PILOTS:
  3 -> 4
BASELINE_CONTROL_CASES:
  0 -> 1
NO_GAIN_CONTROL_CASES:
  0 -> 1
CONTROL_METHOD_GAIN_STATUS:
  CONTROL_NO_GAIN
PROTOCOL_REVISION_REQUIRED:
  no
SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

~~~text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

Next on full pass: CTRL-CH-005 strongest-reasonable non-DSD baseline.
