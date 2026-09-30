# DIAG-CH-006 — Deterministic Same-Project Diagnosis Reconstruction Ledger

Status: **FROZEN BEFORE FORMAL COMPARISON AGAINST T1-T5**  
Date: **2026-09-30**  
Challenge ID: `DIAG-CH-006`  
Method: **Diagnosis / DSD 진단론**

## 1. Derivation basis

This ledger is reconstructed from the frozen Diagnosis Protocol and DIAG-CH-001~005 precommit semantics.

~~~text
P0 Diagnosis Protocol v0.1
commit:
  2d6eb83301860f044cba9a67a87c3a937335823b
blob:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129

P1 DIAG-CH-001 precommit
commit:
  2d832246197b9ed474962c10732fa2196ed065a5
blob:
  53874c7c53115373b358b467eeb79682bade5034

P2 DIAG-CH-002 precommit
commit:
  119407929fe5e9d43fd9fc04ac21ec9a49147950
blob:
  655c5feab5626453027d89faca66842cd5506fc5

P3 DIAG-CH-003 precommit
commit:
  8b21d04280c5c54e5897033acd8a42fbaffdd26c
blob:
  299f1d74a60f0da07746abde6fa677f8c6c5d3f9

P4 DIAG-CH-004 precommit
commit:
  cf85b4299cfdedb85fffdc3ef4c588681c71f268
blob:
  af35f3074b96a1764c71f7c4bf9ed8e5e1a638bb

P5 DIAG-CH-005 precommit
commit:
  ce3c6d7e0bdab70453916875ef18b59720069114
blob:
  7becc81d1ac3b9822fa6331fd8cfc6953e106c27

DIAG-CH-006 precommit
commit:
  9e9ba8d6b7e832d1456778559f5431a2c650f556
blob:
  3d2337667e058442cf744a6af4a93bb2a6a17484
~~~

Formal result comparison targets T1-T5 are not derivation inputs for this ledger.

Because this is same-project work, this ledger does not claim blindness.

## 2. Reconstructed CH-001 ledger

### CH-001-A

~~~text
CANDIDATES:
  a1, a2, a3

MAIN_READOUT:
  all 0

STATUS:
  a1 DEFINED_ZERO
  a2 DEFINED_ZERO
  a3 APPLICABLE_BUT_UNDEFINED

SUPPORT:
  a1 S1
  a2 S1
  a3 S2

TRANSITION:
  p0 -> {a1,a2}

COMPATIBLE:
  {a1,a2}

EXCLUDED:
  {a3}

DIAGNOSIS_SET_OUTCOME:
  DIAGNOSIS_SET_MULTIPLE_COMPATIBLE

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_ESTABLISHED
~~~

Preserved:

~~~text
EQUAL_READOUT != EQUAL_HIDDEN_STATE
MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED
APPLICABLE_BUT_UNDEFINED != DEFINED_ZERO
~~~

### CH-001-B

~~~text
CANDIDATES:
  b1 q=9
  b2 q=10
  b3 q=11

RESIDUAL:
  abs(q-10)

RESIDUALS:
  b1 1
  b2 0
  b3 1

COMPATIBLE:
  {b2}

EXCLUDED:
  {b1,b3}

DIAGNOSIS_SET_OUTCOME:
  DIAGNOSIS_SET_UNIQUE_WITHIN_DECLARED_CLASS

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_ESTABLISHED

GLOBAL_UNIQUENESS:
  not established
~~~

Preserved:

~~~text
UNIQUE_WITHIN_DECLARED_CLASS != GLOBAL_UNIQUE_DIAGNOSIS
RESIDUAL_ZERO != SOURCE_STATE_IDENTITY
~~~

### CH-001-C

~~~text
CAUSE_CANDIDATES:
  c1, c2

EVIDENCE:
  M=PRESENT
  K=PRESENT

COMPATIBLE:
  {c1}

EXCLUDED:
  {c2}

CAUSE_CLAIM_STATUS:
  CAUSE_COMPATIBILITY_ONLY

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_ESTABLISHED

UNRESTRICTED_CAUSAL_PROOF:
  not established
~~~

Across A/B/C:

~~~text
PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT

METHOD_GAIN_STATUS:
  DIAGNOSIS_METHOD_GAIN_NOT_ASSESSED
~~~

## 3. Reconstructed CH-002 ledger

~~~text
N1:
  set = MULTIPLE_COMPATIBLE
  primary = DIAGNOSIS_NOT_ESTABLISHED
  terminal = DIAGNOSIS_TASK_NOT_ESTABLISHED

N2:
  required support interface = unavailable
  primary = DIAGNOSIS_BLOCKED
  terminal = DIAGNOSIS_TASK_BLOCKED

N3:
  bridge = BRIDGE_RELATION_CONFLICTING
  pair = PAIR_CONFLICTING
  primary = DIAGNOSIS_CONFLICTING
  terminal = DIAGNOSIS_TASK_CONFLICTING

N4:
  bridge = BRIDGE_RELATION_UNDERDETERMINED
  pair = PAIR_UNDERDETERMINED
  primary = DIAGNOSIS_UNDERDETERMINED
  terminal = DIAGNOSIS_TASK_UNDERDETERMINED

N5:
  bridge = BRIDGE_RELATION_OUT_OF_SCOPE
  primary = DIAGNOSIS_OUT_OF_SCOPE
  terminal = DIAGNOSIS_TASK_OUT_OF_SCOPE

N6:
  Q1 = DIAGNOSIS_ESTABLISHED
  Q2 = DIAGNOSIS_NOT_ESTABLISHED
  terminal = DIAGNOSIS_TASK_PARTIAL

N7:
  evidence set = EVIDENCE_SET_CONFLICTING
  primary = DIAGNOSIS_CONFLICTING
  terminal = DIAGNOSIS_TASK_CONFLICTING
  NONE_COMPATIBLE_IN_DECLARED_CLASS = not asserted

N8:
  n1 excluded
  n2 excluded
  set = DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
  primary = DIAGNOSIS_ESTABLISHED
  terminal = DIAGNOSIS_TASK_ESTABLISHED
  NO_REAL_STATE_EXISTS = not inferred

N9:
  cause = CAUSE_IDENTIFICATION_NOT_ESTABLISHED
  primary = DIAGNOSIS_NOT_ESTABLISHED
  terminal = DIAGNOSIS_TASK_NOT_ESTABLISHED

N10:
  Q1 = DIAGNOSIS_OUT_OF_SCOPE
  Q2 = DIAGNOSIS_CONFLICTING
  Q3 = DIAGNOSIS_UNDERDETERMINED
  Q4 = DIAGNOSIS_BLOCKED
  terminal = DIAGNOSIS_TASK_OUT_OF_SCOPE
  Q2/Q3/Q4 subordinate states retained
~~~

Coverage reconstructed:

~~~text
ALL_SIX_DIAGNOSIS_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_DIAGNOSIS_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

All ten subcases remain protocol-conformant.

## 4. Reconstructed CH-003 boundary ledger

The ten pair results are reconstructed as:

~~~text
Diagnosis vs Measurement:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Diagnosis vs Reconstruction:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Diagnosis vs Classification:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Diagnosis vs Comparison:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Diagnosis vs Prediction:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Diagnosis vs Simulation:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Diagnosis vs Optimization:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Diagnosis vs Audit:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Diagnosis vs Tracking:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Diagnosis vs Lineage:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

Aggregate:

~~~text
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  10

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  10

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

Interpretation remains fixture-bounded.

~~~text
FIXTURE_BOUNDED_SEPARATION != PERMANENT_METHOD_IRREDUCIBILITY
PARTIAL_OVERLAP_NOT_COLLAPSE != METHOD_SUPERIORITY
~~~

## 5. Reconstructed CH-004 competent-baseline ledger

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_DIAGNOSIS_EVALUATOR

EQUAL_INFORMATION_ACCESS:
  yes

Q1:
  multiple-compatible Diagnosis/B0 outputs correspond

Q2:
  unique-within-declared-class outputs correspond

Q3:
  blocked / conflicting / underdetermined outputs correspond

Q4:
  evidence conflict remains distinct from coherent zero-compatible class

Q5:
  cause compatibility remains bounded
  unsupported posterior ranking remains outside scope

Q6:
  PARTIAL / terminal precedence / sidecar non-substitution preserved
~~~

Gain axes:

~~~text
G1 typed-status / evidence-coherence:
  BASELINE_MATCH

G2 bridge / pair-status / required-interface:
  BASELINE_MATCH

G3 candidate-set / declared-class identifiability:
  BASELINE_MATCH

G4 readout-loss / residual / transition discipline:
  BASELINE_MATCH

G5 cause-scope / probabilistic-interface:
  BASELINE_MATCH

G6 terminal / bounded-claim / neighboring-sidecar:
  BASELINE_MATCH

DIAGNOSIS_METHOD_GAIN_STATUS:
  DIAGNOSIS_METHOD_GAIN_NO_GAIN
~~~

Preserved:

~~~text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

## 6. Reconstructed CH-005 strongest-baseline ledger

~~~text
BASELINE_ID:
  B1_STRONG_DIAGNOSTIC_INFERENCE_ENGINE

EQUAL_INFORMATION_ACCESS:
  yes
~~~

### R1

~~~text
TASK-v1 binds:
  CANDIDATES-v1
  EVIDENCE-v1
  BRIDGE-v1

compatible:
  {h1,h2}

excluded:
  {h3}

retroactive v2 substitution:
  prohibited

registry/version provenance:
  retained
~~~

### R2

~~~text
F(x,y,z):
  (x+z,y+z)

ker(F):
  span{(-1,-1,1)}

observed:
  (2,3)

declared class:
  A={(x,y,0)}

declared-class preimage:
  {(2,3,0)}

unique within declared class:
  established

global injectivity:
  not established

outside-A alternative:
  (1,2,1) retained
~~~

### R3

~~~text
main readout:
  non-discriminating

support:
  non-discriminating

required Property-status sidecar:
  unavailable

task:
  BLOCKED

unavailable status coerced to zero:
  no
~~~

### R4

~~~text
prior:
  (1/2,1/2)

likelihood:
  (3/4,1/4)

P(e):
  1/2

posterior:
  (3/4,1/4)

ranking:
  p1 > p2

candidate truth from ranking:
  not established

causal proof from probability:
  not established
~~~

### R5

~~~text
Q1:
  conflict

Q2:
  unresolved / underdetermined

Q3:
  Diagnosis result retained only from supplied Diagnosis relation

neighbor sidecars substitute for Diagnosis:
  no

run terminal:
  conflict

lower-level Q2/Q3:
  retained

deterministic ledger:
  required

rerun manifest:
  required
~~~

Gain axes reconstructed:

~~~text
G1 VERSIONED_REGISTRY_AND_NONRETROACTIVITY_GAIN:
  BASELINE_MATCH

G2 EXACT_PREIMAGE_KERNEL_AND_DECLARED_CLASS_GAIN:
  BASELINE_MATCH

G3 REQUIRED_INTERFACE_DEPENDENCY_CLOSURE_GAIN:
  BASELINE_MATCH

G4 EXPLICIT_PROBABILISTIC_INFERENCE_AND_SCOPE_GAIN:
  BASELINE_MATCH

G5 CONFLICT_UNDERDETERMINATION_AND_SIDECAR_BOUNDARY_GAIN:
  BASELINE_MATCH

G6 BOUNDED_MAXIMUM_CLAIM_GAIN:
  BASELINE_MATCH

G7 DETERMINISTIC_LEDGER_AND_RERUN_MANIFEST_GAIN:
  BASELINE_MATCH

DIAGNOSIS_METHOD_GAIN_STATUS:
  DIAGNOSIS_METHOD_GAIN_NO_GAIN

STRONGEST_REASONABLE_BASELINE_DIAGNOSIS:
  established_at_constructed_evidence_level
~~~

Preserved:

~~~text
STRONGEST_REASONABLE_BASELINE_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE
~~~

## 7. Reconstructed protocol-level state

~~~text
DIAGNOSIS_PROTOCOL_CONFORMANCE:
  conformant across frozen executable cases

CURRENT_DIAGNOSIS_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 8. Counter state before formal comparison

This ledger does not increment direct-pilot, baseline, or NO_GAIN counters.

~~~text
DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  5

SUCCESSFUL_DIRECT_DIAGNOSIS_PILOTS:
  5

POSITIVE_DIAGNOSIS_CASES:
  1

NEGATIVE_OR_UNRESOLVED_DIAGNOSIS_CASES:
  1

METHOD_BOUNDARY_DIAGNOSIS_CASES:
  1

BASELINE_DIAGNOSIS_CASES:
  2

NO_GAIN_DIAGNOSIS_CASES:
  2

STRONGEST_REASONABLE_BASELINE_DIAGNOSIS:
  established_at_constructed_evidence_level

REPRODUCIBILITY_CASES:
  0
~~~

## 9. Ledger freeze

~~~text
DERIVATION_BASIS:
  P0 + P1 + P2 + P3 + P4 + P5

FORMAL_RESULT_COMPARISON_TARGETS_USED_AS_DERIVATION_SOURCE:
  no

LEDGER_STATUS:
  FROZEN_BEFORE_FORMAL_T1_T5_COMPARISON

POST_COMPARISON_CORRECTION_ALLOWED:
  no
~~~
