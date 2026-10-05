# CTRL-CH-006 — Deterministic Same-Project Control Retrace Result

Status: **70/70 PASS / ZERO CLAIM-RELEVANT MISMATCH**  
Date: **2026-10-06**

~~~text
PRECOMMIT_COMMIT:
  1e96b4d721aaad53b090a906b0631dae6ee05dc9
PRECOMMIT_BLOB:
  d980a921f7db2480e3a2d6a41e5b0736ad6d373a

RETRACE_LEDGER_COMMIT:
  0214c47a326366144546aa3c56c2494e504dc0f2
RETRACE_LEDGER_BLOB:
  3377a848fcee9e939596b3a3eb45f23336c6e45d
~~~

The retrace ledger was frozen before formal comparison.

Comparison:

~~~text
CTRL-CH-001:
  EXACT_MATCH

CTRL-CH-002:
  EXACT_MATCH

CTRL-CH-003:
  EXACT_MATCH

CTRL-CH-004:
  EXACT_MATCH

CTRL-CH-005:
  EXACT_MATCH
~~~

Reconstructed claim-relevant records matched:

~~~text
one-step action 2
feedback/open-loop distinction
hard-constraint exclusion
typed hybrid transition and lineage
readout-bounded target claim
policy update non-retroactivity

all six primary statuses
all seven task terminals
prerequisite/observation/reachability distinctions
terminal precedence

10 neighboring-method pairs
exact collapse 0
unresolved 0

B0 baseline NO_GAIN
B1 strongest-reasonable baseline NO_GAIN
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
  1
SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once
CLAIM_RELEVANT_MISMATCHES:
  0
POST_COMPARISON_CORRECTIONS:
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

~~~text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
~~~

Next: CTRL-AUD-001 frozen-axis internal-standardization audit.
