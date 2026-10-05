# CTRL-CH-006 Retrace Ledger

Status: **FROZEN BEFORE FORMAL COMPARISON**  
Date: **2026-10-06**

~~~text
PRECOMMIT_COMMIT:
  1e96b4d721aaad53b090a906b0631dae6ee05dc9
PRECOMMIT_BLOB:
  d980a921f7db2480e3a2d6a41e5b0736ad6d373a

DERIVATION_SOURCES:
  P0 protocol
  P1-P5 challenge precommits

FORMAL_COMPARISON_TARGETS_USED_DURING_LEDGER_CONSTRUCTION:
  none

POST_COMPARISON_LEDGER_CORRECTION_ALLOWED:
  no
~~~

## Reconstructed CTRL-CH-001

~~~text
one-step action:
  2

feedback policy:
  retained as FEEDBACK_POLICY

open-loop:
  [1,1]
  retained as OPEN_LOOP_ACTION_SEQUENCE

hard constraint:
  action 3 excluded

hybrid transition:
  typed A -> B
  lineage retained

reduced readout:
  target 7
  no full-state equality inference

policy update:
  P1 retained
  P2 parent P1
  no retroactive rewrite
~~~

## Reconstructed CTRL-CH-002

~~~text
all six primary statuses:
  yes

all seven task terminals:
  yes

known inadmissible action:
  NOT_ESTABLISHED

missing required effect bridge:
  BLOCKED

conflicting effect models:
  CONFLICTING

live execution request:
  OUT_OF_SCOPE

unresolved policy semantics:
  UNDERDETERMINED

exact PARTIAL:
  yes

known unsatisfied prerequisite:
  NOT_ESTABLISHED

required observation unavailable:
  BLOCKED

known unreachable target:
  NOT_ESTABLISHED

precedence final:
  OUT_OF_SCOPE
~~~

## Reconstructed CTRL-CH-003

~~~text
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  10
EXACT_COLLAPSE_PAIRS:
  0
UNRESOLVED_BOUNDARY_PAIRS:
  0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  10
SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

## Reconstructed CTRL-CH-004

~~~text
BASELINE_ID:
  B0_GENERIC_VERSIONED_FEEDBACK_CONTROLLER
EQUAL_INFORMATION_ACCESS:
  yes
G1-G6:
  BASELINE_MATCH
CONTROL_METHOD_GAIN_STATUS:
  CONTROL_NO_GAIN
~~~

## Reconstructed CTRL-CH-005

~~~text
BASELINE_ID:
  B1_STRONG_VERSIONED_HYBRID_FEEDBACK_CONTROLLER
EQUAL_INFORMATION_ACCESS:
  yes

version integrity:
  retained
reachability discipline:
  retained
hard-safety discipline:
  retained
hybrid transition:
  retained
feedback update:
  retained
readout limit:
  retained
neighbor boundaries:
  retained

G1-G7:
  BASELINE_MATCH

CONTROL_METHOD_GAIN_STATUS:
  CONTROL_NO_GAIN

STRONGEST_REASONABLE_BASELINE_CONTROL:
  established_at_constructed_evidence_level
~~~

## Protocol-level reconstruction

~~~text
PROTOCOL_REVISION_REQUIRED:
  no
SHARED_CORE_REOPEN_REQUIRED:
  no
CURRENT_CONTROL_EVIDENCE_STATUS:
  validation_in_progress
~~~

## Counter discipline

~~~text
DIRECT_CONTROL_PILOTS_ATTEMPTED:
  retain 5
SUCCESSFUL_DIRECT_CONTROL_PILOTS:
  retain 5
POSITIVE_CONTROL_CASES:
  retain 1
NEGATIVE_OR_UNRESOLVED_CONTROL_CASES:
  retain 1
METHOD_BOUNDARY_CONTROL_CASES:
  retain 1
BASELINE_CONTROL_CASES:
  retain 2
NO_GAIN_CONTROL_CASES:
  retain 2
~~~

Only formal comparison may establish one reproducibility case.
