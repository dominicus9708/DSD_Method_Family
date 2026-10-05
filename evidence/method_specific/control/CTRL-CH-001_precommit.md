# CTRL-CH-001 — Positive Constructed Control Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**  
Challenge ID: `CTRL-CH-001`  
Method: **Control / DSD 제어론**

~~~text
PROTOCOL_COMMIT:
  cda84e4298be81993a571f8f1277b3c7530c6057
PROTOCOL_BLOB:
  bb22a9b8ebca8d11fd29ae9eb072021e45130881
~~~

No protocol rule, fixture, scoring item, or threshold may change after this precommit.

## A — one-step action

~~~text
state:
  x=0
target:
  x'=2
actions:
  {0,1,2}
effect:
  x'=x+a
all actions admissible
~~~

Expected: action 2, target reached on declared one-step scope, CONTROL_ESTABLISHED.

## B — feedback policy

~~~text
state domain:
  {0,1,2}
target:
  2
actions:
  {0,1}
policy:
  if x<2 choose 1
  if x=2 choose 0
~~~

Expected: state-dependent policy retained as FEEDBACK_POLICY, not one-time action.

## C — open-loop action sequence

~~~text
x0=0
sequence:
  [1,1]
effect:
  x_(n+1)=x_n+a_n
horizon:
  two steps
~~~

Expected: open-loop sequence reaches 2 and is not relabeled feedback policy.

## D — hard-constraint preservation

~~~text
state:
  x=0
target region:
  x' in [1,2]
actions:
  {1,3}
effect:
  x'=x+a
hard constraint:
  x'<=2
~~~

Expected: action 1 admissible/supports target; action 3 excluded. No softening.

## E — hybrid transition with lineage

~~~text
pre mode:
  A
action:
  switch
typed transition:
  (A,s0) -> (B,s1)
post-state admissibility:
  supplied
lineage handoff:
  supplied
~~~

Expected: typed transition and lineage retained; not hidden as regular numeric update.

## F — reduced readout target

~~~text
state alternatives:
  u=(2,5)
  v=(3,4)
readout:
  O(a,b)=a+b
target:
  O=7 only
~~~

Expected: readout target may be established while u!=v remains visible. No full-state target claim.

## G — feedback update / non-retroactivity

~~~text
policy P1:
  issued at decision d0
new observation:
  arrives at d1
policy P2:
  parent P1
  new information cutoff d1
  supersedes P1 for subsequent use
~~~

Expected: P1 retained as historical decision basis; P2 is a new version.

## H — neighboring-method handoff discipline

Use supplied handoffs:

~~~text
Simulation:
  may evaluate supplied policy
Prediction:
  may supply forecast/risk
Optimization:
  may supply one-time optimum
Measurement:
  may supply current observation
Operation:
  may later execute live action
~~~

Expected guards:

~~~text
SIMULATION_OF_POLICY != POLICY_SELECTION
PREDICTION_CLAIM != CONTROL_ACTION
ONE_TIME_OPTIMUM != CONTROL_POLICY
MEASUREMENT_RESULT != CONTROL_DECISION
CONTROL_POLICY != OPERATION_EXECUTION
~~~

Method gain is not tested.

## Frozen scoring

~~~text
A one-step action:
  10
B feedback policy:
  12
C open-loop sequence:
  8
D hard constraint:
  12
E typed transition/lineage:
  12
F readout target:
  8
G policy update:
  10
H neighboring handoffs:
  12

TOTAL_REQUIRED_CHECKS:
  84
PASS_THRESHOLD:
  84/84
PARTIAL_PASS_ALLOWED:
  no
~~~

On full pass:

~~~text
DIRECT_CONTROL_PILOTS_ATTEMPTED:
  0 -> 1
SUCCESSFUL_DIRECT_CONTROL_PILOTS:
  0 -> 1
POSITIVE_CONTROL_CASES:
  0 -> 1
CONTROL_METHOD_GAIN_STATUS:
  CONTROL_GAIN_NOT_TESTED
PROTOCOL_REVISION_REQUIRED:
  no
SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Next on full pass: CTRL-CH-002 status / terminal coverage.
