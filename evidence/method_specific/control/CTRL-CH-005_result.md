# CTRL-CH-005 — Strongest-Reasonable Non-DSD Control Baseline Result

Status: **82/82 PASS / CONTROL_NO_GAIN**  
Date: **2026-10-06**

~~~text
PROTOCOL_COMMIT:
  cda84e4298be81993a571f8f1277b3c7530c6057
PRECOMMIT_COMMIT:
  86b9641ebfe495b982da7344cab9801a2ed6ff99
PRECOMMIT_BLOB:
  c66208a17f2e91faad13e79a454350c9c2073fd4
BASELINE_ID:
  B1_STRONG_VERSIONED_HYBRID_FEEDBACK_CONTROLLER
EQUAL_INFORMATION_ACCESS:
  yes
~~~

Frozen-case comparison:

~~~text
R1 version lock:
  BASELINE_MATCH

R2 target reachability:
  BASELINE_MATCH

R3 hard safety:
  BASELINE_MATCH

R4 hybrid transition / identity record:
  BASELINE_MATCH

R5 feedback update / historical retention:
  BASELINE_MATCH

R6 reduced-readout target:
  BASELINE_MATCH

R7 neighboring-method separation:
  BASELINE_MATCH
~~~

Gain axes:

~~~text
G1 BASELINE_MATCH
G2 BASELINE_MATCH
G3 BASELINE_MATCH
G4 BASELINE_MATCH
G5 BASELINE_MATCH
G6 BASELINE_MATCH
G7 BASELINE_MATCH
~~~

Therefore:

~~~text
CONTROL_METHOD_GAIN_STATUS:
  CONTROL_NO_GAIN

STRONGEST_REASONABLE_BASELINE_CONTROL:
  established_at_constructed_evidence_level
~~~

Frozen score:

~~~text
TOTAL_REQUIRED_CHECKS:
  82
PASSED:
  82
FAILED:
  0
~~~

Post-state:

~~~text
DIRECT_CONTROL_PILOTS_ATTEMPTED:
  5
SUCCESSFUL_DIRECT_CONTROL_PILOTS:
  5
POSITIVE_CONTROL_CASES:
  1
NEGATIVE_OR_UNRESOLVED_CONTROL_CASES:
  1
METHOD_BOUNDARY_CONTROL_CASES:
  1
BASELINE_CONTROL_CASES:
  2
NO_GAIN_CONTROL_CASES:
  2

STRONGEST_REASONABLE_BASELINE_CONTROL:
  established_at_constructed_evidence_level

REPRODUCIBILITY_CASES:
  0
EXTERNAL_CONTROL_APPLICATIONS:
  0
INDEPENDENT_CONTROL_VALIDATION:
  not established
INDEPENDENT_REPLICATION:
  not established

CONTROL_INTERNAL_STANDARDIZATION_STATUS:
  developing
CURRENT_CONTROL_EVIDENCE_STATUS:
  validation_in_progress
PROTOCOL_REVISION_REQUIRED:
  no
SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The strongest-reasonable label is bounded to constructed evidence. It does not establish universal equivalence with all non-DSD control methods.

Next: CTRL-CH-006 deterministic same-project retrace.
