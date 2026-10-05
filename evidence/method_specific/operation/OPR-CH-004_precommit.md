# OPR-CH-004 — Competent Non-DSD Operation Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**

~~~text
PROTOCOL_COMMIT:
  f732733fd871cbfed930abe44c6970e8ec34fed6
PROTOCOL_BLOB:
  5c6df2773f57ecad85d7ddbc4f06e607b79cc02e

BASELINE_ID:
  B0_GENERIC_VERSIONED_RUNBOOK_ORCHESTRATOR

BASELINE_CLASS:
  competent_non_DSD_constructed_operations_workflow

BASELINE_USES_DSD_AXIOMS:
  no

EQUAL_INFORMATION_ACCESS:
  required
~~~

B0 may use ordinary operations/workflow machinery:

~~~text
versioned runbook
readiness checklist
actor/resource availability checks
monitoring status
handoff trigger and acceptance fields
retry/recovery/escalation/stop rules
repeated-cycle counter
historical execution versions
status/error codes
audit/re-measurement triggers
~~~

Frozen fixtures:

~~~text
Q1 readiness:
  STEP-A
  readiness yes
  actor/resource available
  monitor defined
  expected execute STEP-A

Q2 handoff:
  source complete
  target ready
  trigger and acceptance both explicit
  expected accepted handoff

Q3 repeated cycle:
  two batches
  inspect -> process -> verify
  reset after pass
  stop at zero remaining

Q4 exception route:
  recoverable resource fault
  backup available
  expected RECOVERY
  no escalation/stop

Q5 version update:
  O1 historical
  new monitoring information
  O2 parent O1
  O1 retained

Q6 dashboard scope:
  readiness readout sufficient only for start/no-start decision
  full state not inferred

Q7 negative/status bundle:
  required resource interface unavailable -> BLOCKED
  conflicting monitoring -> CONFLICTING
  unresolved exception semantics -> UNDERDETERMINED
  authority-creation request -> OUT_OF_SCOPE
~~~

Gain axes:

~~~text
G1 lifecycle/procedure/version discipline
G2 readiness/resource/monitoring discipline
G3 handoff trigger/acceptance discipline
G4 exception/repeated-cycle discipline
G5 update/readout-limit discipline
G6 neighboring-method/authority boundary discipline
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
OPERATION_METHOD_GAIN_STATUS:
  OPERATION_NO_GAIN
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

On full pass:

~~~text
DIRECT_OPERATION_PILOTS_ATTEMPTED:
  3 -> 4
SUCCESSFUL_DIRECT_OPERATION_PILOTS:
  3 -> 4
BASELINE_OPERATION_CASES:
  0 -> 1
NO_GAIN_OPERATION_CASES:
  0 -> 1
OPERATION_METHOD_GAIN_STATUS:
  OPERATION_NO_GAIN
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

Next on full pass: OPR-CH-005 strongest-reasonable non-DSD baseline.
