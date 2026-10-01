# RECON-CH-006 — Deterministic Same-Project Reconstruction Ledger

Status: **FROZEN BEFORE FORMAL COMPARISON AGAINST T1-T5**  
Date: **2026-10-02**  
Challenge ID: `RECON-CH-006`  
Method: **Reconstruction / DSD 복원론**

## 1. Derivation basis

This ledger is reconstructed from the frozen Reconstruction Protocol and RECON-CH-001~005 precommit semantics only.

~~~text
P0 Reconstruction Protocol v0.1
commit:
  2d4cdcab4b646a9d75f96dcc2ef301722eb612ad
blob:
  1f009e81b9992fbdec75abbd9551e9d06f0a170e

P1 RECON-CH-001 precommit
commit:
  f56cce9a1228384b5607b89ce9092606053696bf
blob:
  88058d72c76ff953e75dc18f179c64f040f8e51d

P2 RECON-CH-002 precommit
commit:
  9235e37685fbdd75d5f64200412416cf464212d0
blob:
  8312fe0f0722bba44b21e2e8a50c04336de7f888

P3 RECON-CH-003 precommit
commit:
  d2eae78393e5eb37c3f9c5719ef1e74df7bc81b5
blob:
  6e3adb97f1357a3ad69237141f6a8e716d2586e9

P4 RECON-CH-004 precommit
commit:
  f06ceaad98ecd9e993483f48e46fd91911ddf6e5
blob:
  126c168d43bf8fa0daa44bf2d16c9cb6618104ce

P5 RECON-CH-005 precommit
commit:
  c8fa76c3c7764a77c9c3f01a49edae7b93dcf005
blob:
  a134bab5a6d1da5f556cb2783166defefd5e6b82

RECON-CH-006 precommit
commit:
  2fe975ffef49293d7afabec940f22d5ac756f27c
blob:
  586c4eecb90232800ecd235e29bc925d123ea722
~~~

Formal result comparison targets T1-T5 are not derivation inputs for this ledger.

Because this is same-project work, this ledger does not claim blindness.

## 2. Reconstructed CH-001 ledger

### CH-001-A — compressed-source compatibility set

~~~text
CANDIDATES:
  a1=(1,2)
  a2=(2,1)
  a3=(0,0)

FORWARD_MAP:
  F(x1,x2)=x1+x2

FORWARD_VALUES:
  F(a1)=3
  F(a2)=3
  F(a3)=0

EVIDENCE:
  y=3

COMPATIBLE:
  {a1,a2}

EXCLUDED:
  {a3}

RECONSTRUCTION_SET_OUTCOME:
  RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE

RECONSTRUCTION_PRIMARY_STATUS:
  RECONSTRUCTION_ESTABLISHED

TASK_TERMINAL_STATUS:
  RECONSTRUCTION_TASK_ESTABLISHED
~~~

Preserved:

~~~text
EQUAL_OUTPUT != EQUAL_SOURCE
MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED
NONINJECTIVE_FORWARD_MAP != LICENSE_TO_SELECT_ONE_PREIMAGE
~~~

### CH-001-B — prior-state uniqueness within declared class

~~~text
CANDIDATES:
  b1 prior=P1 marker=RED
  b2 prior=P2 marker=BLUE
  b3 prior=P3 marker=BLUE

CURRENT_STATE:
  C

TRANSITION:
  P1 !-> C
  P2  -> C
  P3 !-> C

OBSERVED_MARKER:
  BLUE

COMPATIBLE:
  {b2}

EXCLUDED:
  {b1,b3}

RECONSTRUCTION_SET_OUTCOME:
  RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS

RECONSTRUCTION_PRIMARY_STATUS:
  RECONSTRUCTION_ESTABLISHED

TASK_TERMINAL_STATUS:
  RECONSTRUCTION_TASK_ESTABLISHED

GLOBAL_HISTORICAL_UNIQUENESS:
  not established

ESTABLISHED_LINEAGE_IDENTITY:
  not established
~~~

Preserved:

~~~text
UNIQUE_WITHIN_DECLARED_CLASS != GLOBAL_HISTORICAL_TRUTH
TRANSITION_COMPATIBILITY != ESTABLISHED_LINEAGE
CURRENT_STATE_DIAGNOSIS != PAST_STATE_RECONSTRUCTION
~~~

### CH-001-C — frozen-interface unrecoverability

~~~text
CANDIDATES:
  u1=(1,0)
  u2=(0,1)

FORWARD_MAP:
  F(x1,x2)=x1+x2

FORWARD_VALUES:
  F(u1)=1
  F(u2)=1

EVIDENCE:
  readout=1

INTERFACE_CLOSURE:
  INTERFACE_COMPLETE_FOR_DECLARED_CLAIM

FROZEN_COMPONENTS:
  F-C-v1
  E-C-v1

COMPATIBLE:
  {u1,u2}

RECONSTRUCTION_SET_OUTCOME:
  RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE

RECOVERY_STATUS:
  UNRECOVERABLE_DISTINCTION_ESTABLISHED_ON_FROZEN_INTERFACE

RECONSTRUCTION_PRIMARY_STATUS:
  RECONSTRUCTION_ESTABLISHED

TASK_TERMINAL_STATUS:
  RECONSTRUCTION_TASK_ESTABLISHED

ABSOLUTE_FUTURE_UNRECOVERABILITY:
  not claimed
~~~

Across A/B/C:

~~~text
PROTOCOL_CONFORMANCE:
  RECONSTRUCTION_PROTOCOL_CONFORMANT

METHOD_GAIN_STATUS:
  RECONSTRUCTION_GAIN_NOT_YET_TESTED
~~~

## 3. Reconstructed CH-002 ledger

~~~text
N1:
  compatible = {h1,h2}
  set = RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE
  primary = RECONSTRUCTION_NOT_ESTABLISHED
  terminal = RECONSTRUCTION_TASK_NOT_ESTABLISHED

N2:
  required support-retention sidecar = unavailable
  replacement = none
  primary = RECONSTRUCTION_BLOCKED
  terminal = RECONSTRUCTION_TASK_BLOCKED
  unavailable interface != evaluable destructive loss

N3:
  bridge = BRIDGE_RELATION_CONFLICTING
  pair = RECONSTRUCTION_PAIR_CONFLICTING
  candidate = RECONSTRUCTION_CANDIDATE_CONFLICTING
  primary = RECONSTRUCTION_CONFLICTING
  terminal = RECONSTRUCTION_TASK_CONFLICTING

N4:
  bridge = BRIDGE_RELATION_UNDERDETERMINED
  pair = RECONSTRUCTION_PAIR_UNDERDETERMINED
  candidate = RECONSTRUCTION_CANDIDATE_UNDERDETERMINED
  primary = RECONSTRUCTION_UNDERDETERMINED
  terminal = RECONSTRUCTION_TASK_UNDERDETERMINED

N5:
  bridge = BRIDGE_RELATION_OUT_OF_SCOPE
  primary = RECONSTRUCTION_OUT_OF_SCOPE
  terminal = RECONSTRUCTION_TASK_OUT_OF_SCOPE

N6:
  Q1 = RECONSTRUCTION_ESTABLISHED
  Q2 = RECONSTRUCTION_NOT_ESTABLISHED
  terminal = RECONSTRUCTION_TASK_PARTIAL
  no higher-priority terminal

N7:
  evidence set = EVIDENCE_SET_CONFLICTING
  primary = RECONSTRUCTION_CONFLICTING
  terminal = RECONSTRUCTION_TASK_CONFLICTING
  NONE_COMPATIBLE_IN_DECLARED_CLASS = not asserted

N8:
  n1 excluded
  n2 excluded
  set = RECONSTRUCTION_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
  primary = RECONSTRUCTION_ESTABLISHED
  terminal = RECONSTRUCTION_TASK_ESTABLISHED
  NO_REAL_PAST_STATE_OR_HISTORY = not inferred

N9:
  k1 compatible
  k2 excluded
  set = RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS
  recovery = RECOVERABLE_ON_DECLARED_SCOPE
  primary unrecoverability claim = RECONSTRUCTION_NOT_ESTABLISHED
  terminal = RECONSTRUCTION_TASK_NOT_ESTABLISHED

N10:
  Q1 = RECONSTRUCTION_OUT_OF_SCOPE
  Q2 = RECONSTRUCTION_CONFLICTING
  Q3 = RECONSTRUCTION_UNDERDETERMINED
  Q4 = RECONSTRUCTION_BLOCKED
  terminal = RECONSTRUCTION_TASK_OUT_OF_SCOPE
  Q2/Q3/Q4 subordinate states retained
~~~

Coverage reconstructed:

~~~text
ALL_SIX_RECONSTRUCTION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_RECONSTRUCTION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

All ten subcases remain protocol-conformant.

## 4. Reconstructed CH-003 boundary ledger

The eleven pair results are reconstructed as:

~~~text
Reconstruction vs Diagnosis:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction vs Aggregation:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction vs Compression:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction vs Tracking:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction vs Lineage:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction vs Measurement:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction vs Transformation:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction vs Prediction:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction vs Simulation:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction vs Optimization:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction vs Audit:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

Aggregate:

~~~text
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  11

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

Interpretation remains fixture-bounded.

~~~text
FIXTURE_BOUNDED_SEPARATION != PERMANENT_METHOD_IRREDUCIBILITY
PARTIAL_OVERLAP_NOT_COLLAPSE != METHOD_SUPERIORITY
NO_EXACT_COLLAPSE_IN_THIS_FIXTURE != PERMANENT_REGISTRY_SURVIVAL
~~~

## 5. Reconstructed CH-004 competent-baseline ledger

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_INVERSE_RECONSTRUCTION_EVALUATOR

EQUAL_INFORMATION_ACCESS:
  yes

Q1:
  multiple-compatible compressed-source Reconstruction/B0 outputs correspond

Q2:
  declared-class prior-state uniqueness outputs correspond

Q3:
  blocked / conflicting / underdetermined outputs correspond

Q4:
  evidence conflict remains distinct from coherent zero-compatible declared class

Q5:
  frozen-interface unrecoverability remains distinct from declared-scope recoverability

Q6:
  PARTIAL / terminal precedence / Tracking-Lineage-source handoff non-substitution preserved
~~~

Gain axes:

~~~text
G1 class-representation / completeness / candidate-set:
  BASELINE_MATCH

G2 typed-evidence / bridge-coherence / required-interface:
  BASELINE_MATCH

G3 collision-fiber / injectivity / bounded-uniqueness:
  BASELINE_MATCH

G4 interface-closure / recoverability / unrecoverability:
  BASELINE_MATCH

G5 history-relation / Tracking-Lineage / source-handoff:
  BASELINE_MATCH

G6 terminal / bounded-claim / neighboring-sidecar:
  BASELINE_MATCH

RECONSTRUCTION_METHOD_GAIN_STATUS:
  RECONSTRUCTION_NO_GAIN
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
  B1_STRONG_INVERSE_RECONSTRUCTION_ENGINE

EQUAL_INFORMATION_ACCESS:
  yes
~~~

### R1 — versioned registries

~~~text
TASK-v1 binds:
  CLASS-v1
  EVIDENCE-v1
  BRIDGE-v1

compatible:
  {h1,h2}

excluded:
  {h3}

set outcome:
  MULTIPLE_COMPATIBLE

retroactive v2 substitution:
  prohibited

registry/version provenance:
  retained
~~~

### R2 — exact affine preimage

~~~text
F(x,y,z):
  (x+z,y+z)

ker(F):
  span{(-1,-1,1)}

observed:
  (2,3)

global affine preimage:
  {(2-t,3-t,t): t in R}

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

### R3 — required-interface dependency

~~~text
main readout:
  non-discriminating

support:
  non-discriminating

required typed source-status sidecar:
  unavailable

task:
  BLOCKED

unavailable status coerced to zero:
  no

unavailability promoted to destructive loss:
  no
~~~

### R4 — probabilistic inverse inference

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

unique/global history from ranking:
  not established

Lineage identity from probability:
  not established
~~~

### R5 — temporal relation algebra / handoff pressure

~~~text
H_01:
  (a0,a1)
  (b0,a1)

H_12:
  (a1,c2)
  (a1,d2)

H_12 o H_01:
  (a0,c2)
  (a0,d2)
  (b0,c2)
  (b0,d2)

direct H_02:
  (a0,c2)
  (a0,d2)
  (b0,c2)
  (b0,d2)
  (e0,c2)

composed predecessors of c2:
  {a0,b0}

direct predecessors of c2:
  {a0,b0,e0}

reconstructed prior candidate set:
  {a0,b0,e0}

branch:
  retained

merge:
  retained

unique predecessor:
  not established

direct relation replaced by composition:
  no

Tracking / Lineage / Formation / neighboring sidecars substituted:
  no

deterministic history ledger:
  required

rerun manifest:
  required
~~~

Gain axes reconstructed:

~~~text
G1 VERSIONED_REGISTRY_AND_NONRETROACTIVITY_GAIN:
  BASELINE_MATCH

G2 EXACT_AFFINE_PREIMAGE_KERNEL_AND_DECLARED_CLASS_GAIN:
  BASELINE_MATCH

G3 REQUIRED_INTERFACE_DEPENDENCY_CLOSURE_GAIN:
  BASELINE_MATCH

G4 EXPLICIT_PROBABILISTIC_INVERSE_INFERENCE_AND_SCOPE_GAIN:
  BASELINE_MATCH

G5 TEMPORAL_RELATION_ALGEBRA_BRANCH_MERGE_AND_HANDOFF_GAIN:
  BASELINE_MATCH

G6 BOUNDED_MAXIMUM_CLAIM_AND_TERMINAL_GAIN:
  BASELINE_MATCH

G7 DETERMINISTIC_LEDGER_AND_RERUN_MANIFEST_GAIN:
  BASELINE_MATCH

RECONSTRUCTION_METHOD_GAIN_STATUS:
  RECONSTRUCTION_NO_GAIN

STRONGEST_REASONABLE_BASELINE_RECONSTRUCTION:
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
RECONSTRUCTION_PROTOCOL_CONFORMANCE:
  conformant across frozen executable cases

CURRENT_RECONSTRUCTION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 8. Counter state before formal comparison

This ledger does not increment direct-pilot, baseline, or NO_GAIN counters.

~~~text
DIRECT_RECONSTRUCTION_PILOTS_ATTEMPTED:
  5

SUCCESSFUL_DIRECT_RECONSTRUCTION_PILOTS:
  5

POSITIVE_RECONSTRUCTION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_RECONSTRUCTION_CASES:
  1

METHOD_BOUNDARY_RECONSTRUCTION_CASES:
  1

BASELINE_RECONSTRUCTION_CASES:
  2

NO_GAIN_RECONSTRUCTION_CASES:
  2

STRONGEST_REASONABLE_BASELINE_RECONSTRUCTION:
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
