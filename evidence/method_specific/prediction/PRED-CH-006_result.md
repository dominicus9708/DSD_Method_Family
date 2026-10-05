# PRED-CH-006 Result

Status: **70/70 PASS / ZERO CLAIM-RELEVANT MISMATCH**  
Date: **2026-10-06**

~~~text
PRECOMMIT_COMMIT:
  e8660a8a3a28180c31bae4ba45cf5a5686540196
PRECOMMIT_BLOB:
  8760589fa391f657717df807e6e3735d5d2545d1

RETRACE_LEDGER_COMMIT:
  e192005f9c796398767eb73b37a1e5b6e0a3450e
RETRACE_LEDGER_BLOB:
  8edfa1902ca69165815df49be42848d8edd89b22
~~~

The retrace ledger was frozen before formal comparison with the historical results.

Comparison:

~~~text
PRED-CH-001:
  EXACT_MATCH

PRED-CH-002:
  EXACT_MATCH

PRED-CH-003:
  EXACT_MATCH

PRED-CH-004:
  EXACT_MATCH

PRED-CH-005:
  EXACT_MATCH
~~~

Reconstructed claim-relevant records matched:

~~~text
point / interval / scenario / probability claims
update and supersession history
readout information-loss limits
later validation separation

all six primary statuses
all seven task terminals
issue-time leakage handling
effective validity region
validation-not-yet-due separation

11 neighboring-method pairs
exact collapse count 0

B0 baseline NO_GAIN
B1 strongest-reasonable baseline NO_GAIN
Brier score 0.09
~~~

Frozen score:

~~~text
artifact / anti-post-hoc integrity:
  12/12 PASS
CH001 reconstruction:
  12/12 PASS
CH002 reconstruction:
  14/14 PASS
CH003 boundary reconstruction:
  10/10 PASS
CH004 baseline reconstruction:
  10/10 PASS
CH005 baseline reconstruction:
  10/10 PASS
final verdict:
  2/2 PASS

TOTAL_REQUIRED_CHECKS:
  70
PASSED:
  70
FAILED:
  0

CLAIM_RELEVANT_MISMATCHES:
  0
POST_COMPARISON_CORRECTIONS:
  0
~~~

Post-state:

~~~text
DIRECT_PREDICTION_PILOTS_ATTEMPTED:
  5
SUCCESSFUL_DIRECT_PREDICTION_PILOTS:
  5
POSITIVE_PREDICTION_CASES:
  1
NEGATIVE_OR_UNRESOLVED_PREDICTION_CASES:
  1
METHOD_BOUNDARY_PREDICTION_CASES:
  1
BASELINE_PREDICTION_CASES:
  2
NO_GAIN_PREDICTION_CASES:
  2
STRONGEST_REASONABLE_BASELINE_PREDICTION:
  established_at_constructed_evidence_level

REPRODUCIBILITY_CASES:
  1
SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once
CLAIM_RELEVANT_MISMATCHES:
  0
POST_COMPARISON_CORRECTIONS:
  0

EXTERNAL_PREDICTION_APPLICATIONS:
  0
INDEPENDENT_PREDICTION_VALIDATION:
  not established
INDEPENDENT_REPLICATION:
  not established
PREDICTION_INTERNAL_STANDARDIZATION_STATUS:
  developing
CURRENT_PREDICTION_EVIDENCE_STATUS:
  validation_in_progress
PROTOCOL_REVISION_REQUIRED:
  no
SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

~~~text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
~~~

Next: PRED-AUD-001 frozen-axis internal-standardization audit.
