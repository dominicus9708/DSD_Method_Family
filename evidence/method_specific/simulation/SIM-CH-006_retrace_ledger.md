# SIM-CH-006 — Deterministic Same-Project Simulation Retrace Ledger

Status: **RECONSTRUCTED AND FROZEN BEFORE FORMAL COMPARISON**  
Date: **2026-10-06**  
Challenge ID: `SIM-CH-006`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**

## 1. Retrace control

~~~text
CH006_PRECOMMIT_COMMIT:
  cccf36124f3eab6cffeb00b5d770bc8a403cf327

CH006_PRECOMMIT_BLOB:
  c22a0a45ac27eb92de37ef71fe79ae6fae639c9e

DERIVATION_SOURCES:
  P0 Simulation Protocol v0.1
  P1 SIM-CH-001 precommit
  P2 SIM-CH-002 precommit
  P3 SIM-CH-003 precommit
  P4 SIM-CH-004 precommit
  P5 SIM-CH-005 precommit

FORMAL_COMPARISON_TARGETS_USED_DURING_LEDGER_CONSTRUCTION:
  none

POST_COMPARISON_LEDGER_CORRECTION_ALLOWED:
  no

SAME_PROJECT_RETRACE:
  yes

BLIND_OR_INDEPENDENT_REPLICATION:
  no
~~~

## 2. Reconstructed SIM-CH-001

~~~text
A:
  deterministic trajectory {1,3,5,7}
  established

B:
  s0->a->a2
  s0->b->b2
  branch coverage complete
  uniqueness not established
  branching != underdetermined

C:
  J1 regular epoch
  typed support/formation transition
  admissible post-transition initial state
  J2 regular epoch
  supplied lineage consumed
  no cross-transition conservation claim

D:
  distinct component trajectories
  equal readout histories {3,5,7}
  no state equality
  no lineage identity

E:
  Euler result 1.1
  end-to-end error <0.006
  threshold 0.01
  accepted approximate claim
  no exactness claim

F:
  stochastic sample path {0,1,0,1}
  no distributional claim

G:
  supplied-policy trajectory {0,1,2}
  Simulation executes supplied policy
  Control choice not performed
  no Prediction/Operation substitution
  SIMULATION_GAIN_NOT_TESTED
~~~

## 3. Reconstructed SIM-CH-002

~~~text
N1:
  SIMULATION_TASK_NOT_ESTABLISHED

N2:
  SIMULATION_TASK_BLOCKED
  no zero-dynamics default

N3:
  SIMULATION_TASK_CONFLICTING

N4:
  SIMULATION_TASK_OUT_OF_SCOPE
  Prediction handoff retained

N5:
  SIMULATION_TASK_UNDERDETERMINED
  not a declared branching model

N6:
  SIMULATION_TASK_PARTIAL

N7:
  SIMULATION_TASK_NOT_ESTABLISHED
  evaluable numerical inadequacy

N8:
  final SIMULATION_TASK_OUT_OF_SCOPE
  lower CONFLICTING retained
  lower UNDERDETERMINED retained
  lower BLOCKED retained

ALL_SIX_SIMULATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_SIMULATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

## 4. Reconstructed SIM-CH-003

~~~text
NEIGHBORING_METHODS:
  Computation
  Optimization
  Measurement
  Aggregation
  Compression
  Transformation
  Tracking
  Lineage
  Prediction
  Control
  Operation
  Audit

PAIR_RESULT_FOR_ALL:
  PARTIAL_OVERLAP_NOT_COLLAPSE

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  12

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  12

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level

PERMANENT_IRREDUCIBILITY_OR_SUPERIORITY_CLAIM:
  none
~~~

## 5. Reconstructed SIM-CH-004

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_HYBRID_SIMULATOR

EQUAL_INFORMATION_ACCESS:
  yes

G1 trajectory-generation correctness:
  BASELINE_MATCH

G2 branch/hybrid-transition/lineage discipline:
  BASELINE_MATCH

G3 readout-information-loss/state-identity discipline:
  BASELINE_MATCH

G4 numerical/stochastic discipline:
  BASELINE_MATCH

G5 negative/status discipline:
  BASELINE_MATCH

G6 claim-relevant outcome equivalence:
  BASELINE_MATCH

SIMULATION_METHOD_GAIN_STATUS:
  SIMULATION_NO_GAIN
~~~

NO_GAIN is not interpreted as failure, deletion, merger, absorption, or permanent redundancy.

## 6. Reconstructed SIM-CH-005

~~~text
BASELINE_ID:
  B1_STRONG_HYBRID_SIMULATION_ENGINE

EQUAL_INFORMATION_ACCESS:
  yes
~~~

### R1

~~~text
v1 trajectory:
  {1,2,4}

newer v2:
  may generate {1,3,9}

retroactive rewrite of v1:
  no
~~~

### R2

~~~text
branches:
  s0->p->q1->r1
  s0->p->q2->r2

branch coverage:
  complete

uniqueness:
  not established

supplied lineage:
  consumed
  not generated
~~~

### R3

~~~text
enclosure:
  [0.367,0.369]

width:
  0.002

exp(-1):
  inside enclosure

numerical acceptance:
  established

exactness:
  not claimed
~~~

### R4

~~~text
ensemble A:
  {0,0,1,1}

ensemble B:
  {0,1,2,2}

ensemble C:
  {0,0,0,1}

empirical final-state mean:
  4/3

exact probability law:
  not claimed

distributional convergence:
  not claimed
~~~

### R5/R6

~~~text
readout collision:
  no state identity inference

undefined -> defined zero:
  typed status/domain transition retained

supplied policy simulation:
  in Simulation

policy selection:
  Control handoff

future truth:
  Prediction handoff

live lifecycle:
  Operation handoff

terminal pressure:
  final OUT_OF_SCOPE
  lower CONFLICTING / UNDERDETERMINED / BLOCKED retained
~~~

Gain ledger:

~~~text
G1-G7:
  BASELINE_MATCH

SIMULATION_METHOD_GAIN_STATUS:
  SIMULATION_NO_GAIN

STRONGEST_REASONABLE_BASELINE_SIMULATION:
  established_at_constructed_evidence_level
~~~

## 7. Protocol-level reconstruction

~~~text
SIMULATION_PROTOCOL_CONFORMANCE:
  conformant on all executable frozen cases

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no

CURRENT_SIMULATION_EVIDENCE_STATUS:
  validation_in_progress
~~~

## 8. Counter discipline

~~~text
DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  retain 5

SUCCESSFUL_DIRECT_SIMULATION_PILOTS:
  retain 5

POSITIVE_SIMULATION_CASES:
  retain 1

NEGATIVE_OR_UNRESOLVED_SIMULATION_CASES:
  retain 1

METHOD_BOUNDARY_SIMULATION_CASES:
  retain 1

BASELINE_SIMULATION_CASES:
  retain 2

NO_GAIN_SIMULATION_CASES:
  retain 2

STRONGEST_REASONABLE_BASELINE_SIMULATION:
  retain established_at_constructed_evidence_level
~~~

Only formal comparison may decide:

~~~text
REPRODUCIBILITY_CASES:
  0 -> 1

SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once
~~~

## 9. Frozen pre-comparison statement

~~~text
FORMAL_COMPARISON_PERFORMED:
  no

CLAIM_RELEVANT_MISMATCH_COUNT:
  not yet scored

POST_COMPARISON_CORRECTIONS:
  prohibited

LEDGER_FREEZE_STATE:
  ready_for_commit_before_comparison
~~~

After this ledger is committed, formal comparison must use T1-T5 exactly as frozen in the SIM-CH-006 precommit and preserve every mismatch.
