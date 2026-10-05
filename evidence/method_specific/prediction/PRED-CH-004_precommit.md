# PRED-CH-004 Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**

~~~text
PROTOCOL_COMMIT:
  1a03a96e270f0d975710f5d530a8b1dbf5105bb0
BASELINE_ID:
  B0_GENERIC_VERSIONED_FORECASTER
BASELINE_USES_DSD_AXIOMS:
  no
EQUAL_INFORMATION_ACCESS:
  yes
~~~

B0 receives the same issue-time information, target, horizon, model information, target mapping, uncertainty semantics, update records, and validation rule.

Frozen cases:

~~~text
Q1 point target:
  model 5 -> target 5

Q2 interval target:
  model [9,11] with Y=2m+1 -> [19,23]

Q3 scenarios:
  warm -> 8
  cold -> 2
  no probability inference

Q4 probability:
  explicit interface supplies P(E)=0.7

Q5 versioned update:
  P1=10
  later P2=12
  P1 remains historical

Q6 later scoring:
  forecast interval [4,6]
  later observation 5
  original scoring rule retained

Q7 unavailable / inconsistent / unresolved required interfaces:
  preserve the corresponding protocol statuses

Q8 horizon:
  requested 10
  model valid 8
  bridge valid 6
  effective support through 6
~~~

Gain axes:

~~~text
G1 issue-time integrity
G2 bridge/interval/readout discipline
G3 scenario/probability discipline
G4 update/version discipline
G5 later-validation discipline
G6 status/validity-region discipline
~~~

If all six axes are `BASELINE_MATCH`:

~~~text
PREDICTION_METHOD_GAIN_STATUS:
  PREDICTION_NO_GAIN
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  64
PASS_THRESHOLD:
  64/64
PARTIAL_PASS_ALLOWED:
  no
~~~

On full pass:

~~~text
DIRECT_PREDICTION_PILOTS_ATTEMPTED:
  3 -> 4
SUCCESSFUL_DIRECT_PREDICTION_PILOTS:
  3 -> 4
BASELINE_PREDICTION_CASES:
  0 -> 1
NO_GAIN_PREDICTION_CASES:
  0 -> 1
~~~

~~~text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

Next: PRED-CH-005 stronger non-DSD baseline.
