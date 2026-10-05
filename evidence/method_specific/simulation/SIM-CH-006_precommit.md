# SIM-CH-006 — Deterministic Same-Project Simulation Retrace Precommit

Status: **PRECOMMITTED BEFORE RETRACE LEDGER FREEZE**  
Date: **2026-10-06**  
Challenge ID: `SIM-CH-006`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**  
Case class: `deterministic_same_project_retrace`  
Case origin: `same_project_retrace_of_SIM_CH_001_through_005`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Purpose

Determine whether claim-relevant Simulation outputs recorded in `SIM-CH-001` through `SIM-CH-005` can be regenerated from immutable project artifacts under frozen Simulation Protocol v0.1 and prospectively frozen retrace semantics.

~~~text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
RETRACE_PASS != METHOD_SUPERIORITY
~~~

## 2. Frozen derivation artifacts

The retrace ledger may use only the frozen protocol and challenge precommits below as derivation sources.

~~~text
P0 Simulation Protocol v0.1
   commit: ea271d04eb09d252299d9420d0fb1191564f5bc6
   blob:   c3d6f80d99dabb5b84c7a60fd2df3f58bf9dba35

P1 SIM-CH-001 precommit
   commit: 7605e452268295c9cc1b48a1c4ac6dfb0c167f5f
   blob:   bf150326b076869da88dabfb50df8f883db45be9

P2 SIM-CH-002 precommit
   commit: 8db0d4fd374c5576acf4fc80809775d6ea1630f3
   blob:   f76d39d1e9bd183f948237c4c12e8f7325edee49

P3 SIM-CH-003 precommit
   commit: 28438af12f0e80b441381b45b2cb836e587c4aa3
   blob:   3f750323283a3525a4925d122f3ffee26211d654

P4 SIM-CH-004 precommit
   commit: 7d85d57625f109ba2e1836c000d24b7b5a5fee16
   blob:   066104319e65f5a5f420a494cf5857df9a6f7c47

P5 SIM-CH-005 precommit
   commit: da364f3999558c71fb705a8bd87b734c0132a8d6
   blob:   5a980110d8e2cab5b9fbef654bc4acfe0dbce16b
~~~

No `SIM-CH-001~005` result artifact may be used to construct the retrace ledger.

## 3. Frozen comparison targets

Only after the retrace ledger is committed may the following result artifacts be used as formal comparison targets.

~~~text
T1 SIM-CH-001 result
   commit: 86ff6673229356500317d58eee404b45f1b66ca6
   blob:   b566582c9dfc5e31cb8607138c624aa14ff8bccd

T2 SIM-CH-002 result
   commit: 250232d9a513d6b679746e039c2cda0ad4f57bb7
   blob:   0333f487032c7bd9971e07684cc1fee7e3a576f8

T3 SIM-CH-003 result
   commit: abc626363574c8f9bd535a377cb705351e735129
   blob:   a8e8e9f547ccde46196761df146394ce35481e2f

T4 SIM-CH-004 result
   commit: b0f923f25258cfa877ec68268a5b04275a3ecab8
   blob:   818125814c82a2893510dd6e972ba1633d98ee88

T5 SIM-CH-005 result
   commit: c055c0c1beeb6ff8a5cb91b60a61f06e1869ed1f
   blob:   01c4a5b38da961a7763b0f83b1775618f11b6bdf
~~~

## 4. Anti-post-hoc sequence

~~~text
1. freeze this SIM-CH-006 precommit
2. reconstruct a dedicated ledger from P0+P1+P2+P3+P4+P5 only
3. commit the retrace ledger
4. only then formally compare against T1+T2+T3+T4+T5
5. record every claim-relevant mismatch
6. do not modify the retrace ledger after comparison
~~~

Allowed comparison labels:

~~~text
EXACT_MATCH
SEMANTIC_EQUIVALENT_MATCH
NONCLAIM_RELEVANT_WORDING_DIFFERENCE
CLAIM_RELEVANT_MISMATCH
~~~

## 5. Frozen retrace target — SIM-CH-001

Reconstruct:

~~~text
A deterministic:
  x={1,3,5,7}
  established

B branching:
  s0->a->a2
  s0->b->b2
  branch coverage complete
  uniqueness not established
  branching != underdetermined

C hybrid:
  J1 regular evolution
  typed formation/support-changing transition
  post-state admissible
  J2 regular evolution
  supplied lineage consumed
  no transition-conservation invention

D readout:
  component trajectories distinct
  readout histories both {3,5,7}
  no state/lineage identity inference

E numerical:
  x_num(0.1)=1.1
  end-to-end error <0.006
  acceptance threshold 0.01
  accepted approximate claim
  no exactness claim

F stochastic:
  sample path {0,1,0,1}
  no distributional claim

G supplied policy:
  z={0,1,2}
  policy simulation in scope
  Control choice not performed
  no Prediction/Operation substitution
  method gain not tested
~~~

## 6. Frozen retrace target — SIM-CH-002

Reconstruct:

~~~text
N1:
  NOT_ESTABLISHED

N2:
  BLOCKED
  no zero-dynamics default

N3:
  CONFLICTING

N4:
  OUT_OF_SCOPE
  Prediction handoff

N5:
  UNDERDETERMINED
  not declared branching

N6:
  PARTIAL

N7:
  NOT_ESTABLISHED
  evaluable numerical inadequacy

N8:
  final OUT_OF_SCOPE
  CONFLICTING / UNDERDETERMINED / BLOCKED lower states retained
~~~

Across SIM-CH-001/002:

~~~text
ALL_SIX_SIMULATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_SIMULATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

## 7. Frozen retrace target — SIM-CH-003

Neighboring pairs:

~~~text
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
~~~

Every pair:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

Aggregate:

~~~text
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
~~~

No permanent irreducibility/superiority/deletion/merger claim.

## 8. Frozen retrace target — SIM-CH-004

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_HYBRID_SIMULATOR

EQUAL_INFORMATION_ACCESS:
  yes
~~~

Six gain axes:

~~~text
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

## 9. Frozen retrace target — SIM-CH-005

~~~text
BASELINE_ID:
  B1_STRONG_HYBRID_SIMULATION_ENGINE

EQUAL_INFORMATION_ACCESS:
  yes
~~~

Reconstruct:

~~~text
R1:
  v1 trajectory {1,2,4}
  newer model does not rewrite v1
  v2 may generate {1,3,9}

R2:
  both hybrid branches retained
  branch coverage complete
  uniqueness not established
  supplied lineage consumed, not generated

R3:
  enclosure [0.367,0.369]
  width 0.002
  exp(-1) inside
  accepted approximate bounded claim
  no exactness/global-time claim

R4:
  three finite-ensemble paths retained
  final-state empirical mean 4/3
  no exact probability/distributional-convergence claim

R5:
  readout collision without state identity
  typed undefined->defined-zero transition retained
  Control/Prediction/Operation handoffs preserved

R6:
  final OUT_OF_SCOPE with lower states retained
~~~

Seven gain axes:

~~~text
G1-G7:
  BASELINE_MATCH

SIMULATION_METHOD_GAIN_STATUS:
  SIMULATION_NO_GAIN

STRONGEST_REASONABLE_BASELINE_SIMULATION:
  established_at_constructed_evidence_level
~~~

## 10. Protocol-level retrace target

Across SIM-CH-001 through SIM-CH-005 reconstruct:

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

## 11. Frozen scoring — 70 checks

### A. Artifact / anti-post-hoc integrity — 12

~~~text
A1 P0 protocol commit/blob frozen
A2 P1 CH001 precommit frozen
A3 P2 CH002 precommit frozen
A4 P3 CH003 precommit frozen
A5 P4 CH004 precommit frozen
A6 P5 CH005 precommit frozen
A7 T1-T5 frozen as comparison targets only
A8 derivation basis excludes T1-T5
A9 retrace ledger committed before comparison
A10 post-comparison ledger correction prohibited
A11 same-project/non-blind limitation stated
A12 direct/baseline/NO_GAIN counters not incremented by retrace
~~~

### B. SIM-CH-001 positive reconstruction — 12

~~~text
B1 deterministic trajectory reconstructed
B2 deterministic terminal reconstructed
B3 both branching trajectories reconstructed
B4 branch coverage/uniqueness distinction reconstructed
B5 hybrid epoch/transition structure reconstructed
B6 lineage handoff/no transition-conservation overclaim reconstructed
B7 readout collision/state distinction reconstructed
B8 numerical bounded-approximation semantics reconstructed
B9 stochastic sample path reconstructed
B10 no distributional overclaim reconstructed
B11 supplied-policy trajectory reconstructed
B12 Prediction/Control/Operation boundaries reconstructed
~~~

### C. SIM-CH-002 terminal coverage — 14

~~~text
C1 N1 NOT_ESTABLISHED reconstructed
C2 N2 BLOCKED reconstructed
C3 no zero-dynamics default reconstructed
C4 N3 CONFLICTING reconstructed
C5 N4 OUT_OF_SCOPE reconstructed
C6 Prediction handoff reconstructed
C7 N5 UNDERDETERMINED reconstructed
C8 N5 not declared branching
C9 N6 PARTIAL reconstructed
C10 N7 NOT_ESTABLISHED reconstructed
C11 N8 OUT_OF_SCOPE reconstructed
C12 N8 lower states retained
C13 all six primary statuses coverage reconstructed
C14 all seven task terminals coverage reconstructed
~~~

### D. SIM-CH-003 boundary — 10

~~~text
D1 12 neighboring pairs reconstructed
D2 Computation/Optimization/Measurement distinctions retained
D3 Aggregation/Compression/Transformation distinctions retained
D4 Tracking/Lineage distinctions retained
D5 Prediction/Control/Operation/Audit distinctions retained
D6 all pairs PARTIAL_OVERLAP_NOT_COLLAPSE
D7 exact collapse count=0
D8 unresolved count=0 / partial-overlap count=12
D9 source-handoff separation retained
D10 no permanent irreducibility/superiority/deletion/merger claim
~~~

### E. SIM-CH-004 competent baseline — 10

~~~text
E1 B0 identity reconstructed
E2 equal-information condition reconstructed
E3 deterministic/branching matches reconstructed
E4 hybrid transition match reconstructed
E5 readout match reconstructed
E6 numerical/stochastic match reconstructed
E7 negative/status match reconstructed
E8 all six gain axes BASELINE_MATCH
E9 SIMULATION_NO_GAIN reconstructed
E10 bounded NO_GAIN interpretation retained
~~~

### F. SIM-CH-005 strongest-reasonable baseline — 10

~~~text
F1 B1 identity/equal-information reconstructed
F2 model-version non-retroactivity reconstructed
F3 hybrid branch/lineage result reconstructed
F4 numerical enclosure result reconstructed
F5 finite stochastic ensemble result reconstructed
F6 readout/status-transition boundary reconstructed
F7 Control/Prediction/Operation handoffs reconstructed
F8 terminal lower-state retention reconstructed
F9 all seven gain axes BASELINE_MATCH
F10 strongest-reasonable constructed status / NO_GAIN interpretation retained
~~~

### G. Final retrace verdict — 2

~~~text
G1 claim-relevant mismatch / post-comparison correction counts recorded exactly
G2 reproducibility classification / revision / shared-core decisions follow comparison
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  70

PASS_THRESHOLD:
  70/70

PARTIAL_PASS_ALLOWED:
  no
~~~

## 12. Allowed counter changes on 70/70 PASS

~~~text
REPRODUCIBILITY_CASES:
  0 -> 1

SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once

CLAIM_RELEVANT_MISMATCHES:
  must equal 0

POST_COMPARISON_CORRECTIONS:
  must equal 0
~~~

Do not change direct-pilot, baseline, NO_GAIN, method-boundary, external, or independent-validation counters.

## 13. Interpretation lock

~~~text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
RETRACE_PASS != METHOD_SUPERIORITY
RETRACE_PASS != PROOF_OF_UNIVERSAL_PROTOCOL_CORRECTNESS
~~~

## 14. Next on full PASS

If all 70 checks pass with zero claim-relevant mismatch and zero post-comparison correction:

~~~text
SIM-AUD-001
frozen-axis internal-standardization audit
prospective precommit required
~~~
