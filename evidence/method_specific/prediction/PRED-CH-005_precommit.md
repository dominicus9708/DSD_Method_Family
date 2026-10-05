# PRED-CH-005 Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**

~~~text
PROTOCOL_COMMIT:
  1a03a96e270f0d975710f5d530a8b1dbf5105bb0
BASELINE_ID:
  B1_STRONG_VERSIONED_FORECAST_ENGINE
BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_forecaster
BASELINE_USES_DSD_AXIOMS:
  no
EQUAL_INFORMATION_ACCESS:
  yes
~~~

B1 may use ordinary forecast-engine features:

~~~text
strict issue-time cutoff
versioned model/target mapping
scenario trees
explicit probability models
interval and set forecasts
forecast-update lineage
hindcast/prospective labels
predeclared scoring rules
historical forecast retention
missing-target handling
calibration sidecars
deterministic rerun manifests
~~~

Frozen cases:

~~~text
R1 version lock:
  P1 issued with model M-v1
  later M-v2 arrives
  P1 remains bound to M-v1

R2 target mapping:
  model interval [2,4]
  bridge Y=3m-1
  target interval [5,11]
  bridge validity includes horizon

R3 scenario/probability:
  branches A,B,C
  explicit probabilities 0.5,0.3,0.2
  probability comes from supplied interface, not branch count

R4 update lineage:
  P1 at t0
  new evidence at t1
  P2 records parent P1 and new cutoff
  P1 remains immutable

R5 prospective/hindcast separation:
  prospective claim uses only pre-target data
  later retrospective analysis is separately labeled

R6 validation:
  event probability forecast p=0.7
  frozen Brier rule before outcome
  constructed outcome y=1
  score=(0.7-1)^2=0.09
  historical metric not changed afterward

R7 validity/status:
  requested horizon extends past one required validity region
  bounded claim stops at effective region
  missing/conflicting/unresolved interfaces preserve their statuses
~~~

Gain axes:

~~~text
G1 issue/model/version non-retroactivity
G2 target mapping and validity-region discipline
G3 scenario/probability semantics
G4 update lineage and historical retention
G5 prospective/hindcast separation
G6 later scoring-rule integrity
G7 status and maximum-claim discipline
~~~

If all seven axes are BASELINE_MATCH:

~~~text
PREDICTION_METHOD_GAIN_STATUS:
  PREDICTION_NO_GAIN
STRONGEST_REASONABLE_BASELINE_PREDICTION:
  established_at_constructed_evidence_level
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  82
PASS_THRESHOLD:
  82/82
PARTIAL_PASS_ALLOWED:
  no
~~~

On full pass:

~~~text
DIRECT_PREDICTION_PILOTS_ATTEMPTED:
  4 -> 5
SUCCESSFUL_DIRECT_PREDICTION_PILOTS:
  4 -> 5
BASELINE_PREDICTION_CASES:
  1 -> 2
NO_GAIN_PREDICTION_CASES:
  1 -> 2
~~~

The strongest-reasonable label is bounded to constructed evidence and is not universal.

Next on full pass: PRED-CH-006 deterministic same-project retrace.
