# DIAG-CH-006 — Deterministic Same-Project Diagnosis Retrace Result

Status: **EXECUTED — 70/70 PASS**  
Date: **2026-09-30**  
Challenge ID: `DIAG-CH-006`  
Method: **Diagnosis / DSD 진단론**  
Protocol: **Diagnosis Protocol v0.1**  
Case class: `deterministic_same_project_retrace`

## 1. Frozen artifact identities

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

DIAG-CH-006 reconstruction ledger
commit:
  dc8a2bef09d2ccef590bd2dca145e4a707f31ea5
blob:
  5c88893c4a5d643571c19df7033ff4e5498eb21c
~~~

Formal comparison targets:

~~~text
T1 DIAG-CH-001 result
commit:
  6a182dce0976a25b6317e9c9af85b8317781d88b
blob:
  591e9aaeba8176b7a535c979851064294aef0c56

T2 DIAG-CH-002 result
commit:
  edc89cc16df5290c78a7dd033ad67e34c59dc695
blob:
  024ed7f48b06ff20e7eca8e2dbc1136f878cc6d3

T3 DIAG-CH-003 result
commit:
  67b1d448540387426c13fe0d58e8bdc8f1f83cdc
blob:
  1ba8520cbb376867094d413d5bed66258d8c258e

T4 DIAG-CH-004 result
commit:
  8978b543144742dc5d1a7e4bffb2a0a24692eeaf
blob:
  2f3e5f966e8fc6102a633dffee7df9af8c5635a8

T5 DIAG-CH-005 result
commit:
  6dbcd396baf61bf6c05b7ac051a49342c3c03634
blob:
  85c01c39ce6daef445442218b153896f42a8e8a6
~~~

The reconstruction ledger was committed before formal comparison against T1-T5.

~~~text
DERIVATION_BASIS:
  P0 + P1 + P2 + P3 + P4 + P5

T1_T5_ROLE:
  comparison targets only

POST_COMPARISON_CORRECTIONS:
  0
~~~

This is same-project, non-blind artifact-consistency evidence.

## 2. CH-001 comparison

Reconstructed and recorded claim-relevant outputs agree.

~~~text
A compatible set {a1,a2}:
  EXACT_MATCH

A excluded set {a3}:
  EXACT_MATCH

A set outcome MULTIPLE_COMPATIBLE:
  EXACT_MATCH

A primary/terminal ESTABLISHED:
  EXACT_MATCH

B compatible set {b2}:
  EXACT_MATCH

B excluded set {b1,b3}:
  EXACT_MATCH

B UNIQUE_WITHIN_DECLARED_CLASS:
  EXACT_MATCH

B global uniqueness not claimed:
  EXACT_MATCH

C c1 compatible / c2 excluded:
  EXACT_MATCH

C CAUSE_COMPATIBILITY_ONLY:
  EXACT_MATCH

C unrestricted causal proof not claimed:
  EXACT_MATCH

protocol conformance:
  EXACT_MATCH

method gain NOT_ASSESSED:
  EXACT_MATCH
~~~

No claim-relevant mismatch was found.

## 3. CH-002 comparison

All ten frozen terminal/negative cases agree with the committed reconstruction ledger.

~~~text
N1 NOT_ESTABLISHED:
  EXACT_MATCH

N2 BLOCKED:
  EXACT_MATCH

N3 CONFLICTING:
  EXACT_MATCH

N4 UNDERDETERMINED:
  EXACT_MATCH

N5 OUT_OF_SCOPE:
  EXACT_MATCH

N6 PARTIAL:
  EXACT_MATCH

N7 EVIDENCE_SET_CONFLICTING:
  EXACT_MATCH

N7 zero-compatible set not asserted:
  EXACT_MATCH

N8 NONE_COMPATIBLE_IN_DECLARED_CLASS:
  EXACT_MATCH

N8 NO_REAL_STATE_EXISTS not inferred:
  EXACT_MATCH

N9 CAUSE_IDENTIFICATION_NOT_ESTABLISHED:
  EXACT_MATCH

N10 OUT_OF_SCOPE terminal precedence:
  EXACT_MATCH

N10 subordinate conflicting/underdetermined/blocked states retained:
  EXACT_MATCH

all six primary-status coverage:
  EXACT_MATCH

all seven task-terminal coverage:
  EXACT_MATCH
~~~

No claim-relevant mismatch was found.

## 4. CH-003 comparison

The ten neighboring-method boundary results match.

~~~text
Measurement:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Reconstruction:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Classification:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Comparison:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Prediction:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Simulation:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Optimization:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Audit:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Tracking:
  PARTIAL_OVERLAP_NOT_COLLAPSE

Lineage:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

Aggregate comparison:

~~~text
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  10
  EXACT_MATCH

EXACT_COLLAPSE_PAIRS:
  0
  EXACT_MATCH

UNRESOLVED_BOUNDARY_PAIRS:
  0
  EXACT_MATCH

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  10
  EXACT_MATCH

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED
  EXACT_MATCH

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
  EXACT_MATCH
~~~

No permanent irreducibility or superiority claim was introduced.

## 5. CH-004 comparison

The competent non-DSD baseline comparison agrees with the reconstruction ledger.

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_DIAGNOSIS_EVALUATOR
  EXACT_MATCH

EQUAL_INFORMATION_ACCESS:
  yes
  EXACT_MATCH

Q1 multiple-compatible:
  MATCH

Q2 declared-class uniqueness:
  MATCH

Q3 blocked/conflict/underdetermined:
  MATCH

Q4 conflict vs coherent zero-compatible:
  MATCH

Q5 cause/probability scope:
  MATCH

Q6 partial/precedence/sidecar discipline:
  MATCH

G1:
  BASELINE_MATCH

G2:
  BASELINE_MATCH

G3:
  BASELINE_MATCH

G4:
  BASELINE_MATCH

G5:
  BASELINE_MATCH

G6:
  BASELINE_MATCH

DIAGNOSIS_METHOD_GAIN_STATUS:
  DIAGNOSIS_METHOD_GAIN_NO_GAIN
  EXACT_MATCH
~~~

The bounded NO_GAIN interpretation also matches.

## 6. CH-005 comparison

The strongest-reasonable constructed baseline comparison agrees with the reconstruction ledger.

~~~text
BASELINE_ID:
  B1_STRONG_DIAGNOSTIC_INFERENCE_ENGINE
  EXACT_MATCH

EQUAL_INFORMATION_ACCESS:
  yes
  EXACT_MATCH

R1 versioned registry / non-retroactivity:
  MATCH

R2 kernel:
  span{(-1,-1,1)}
  EXACT_MATCH

R2 declared-class preimage:
  {(2,3,0)}
  EXACT_MATCH

R2 global injectivity:
  not established
  EXACT_MATCH

R3 required status sidecar:
  unavailable
  EXACT_MATCH

R3 task:
  BLOCKED
  EXACT_MATCH

R4 P(e):
  1/2
  EXACT_MATCH

R4 posterior:
  (3/4,1/4)
  EXACT_MATCH

R4 ranking:
  p1 > p2
  EXACT_MATCH

R4 ranking-to-truth promotion:
  none
  EXACT_MATCH

R4 probability-to-causal-proof promotion:
  none
  EXACT_MATCH

R5 Q1:
  conflict
  EXACT_MATCH

R5 Q2:
  unresolved / underdetermined
  EXACT_MATCH

R5 sidecar substitution:
  none
  EXACT_MATCH

R5 run terminal:
  conflict
  EXACT_MATCH

R5 lower-level state retention:
  MATCH

R5 deterministic ledger/rerun:
  MATCH
~~~

Gain axes:

~~~text
G1:
  BASELINE_MATCH

G2:
  BASELINE_MATCH

G3:
  BASELINE_MATCH

G4:
  BASELINE_MATCH

G5:
  BASELINE_MATCH

G6:
  BASELINE_MATCH

G7:
  BASELINE_MATCH

DIAGNOSIS_METHOD_GAIN_STATUS:
  DIAGNOSIS_METHOD_GAIN_NO_GAIN

STRONGEST_REASONABLE_BASELINE_DIAGNOSIS:
  established_at_constructed_evidence_level
~~~

No claim-relevant mismatch was found.

## 7. Execution of the 70 frozen checks

### A — artifact and anti-post-hoc integrity

~~~text
A1 PASS
A2 PASS
A3 PASS
A4 PASS
A5 PASS
A6 PASS
A7 PASS
A8 PASS
A9 PASS
A10 PASS
A11 PASS
A12 PASS

A: 12/12
~~~

### B — CH-001 positive-pack reconstruction

~~~text
B1 PASS
B2 PASS
B3 PASS
B4 PASS
B5 PASS
B6 PASS
B7 PASS
B8 PASS
B9 PASS
B10 PASS

B: 10/10
~~~

### C — CH-002 terminal/negative coverage

~~~text
C1 PASS
C2 PASS
C3 PASS
C4 PASS
C5 PASS
C6 PASS
C7 PASS
C8 PASS
C9 PASS
C10 PASS
C11 PASS
C12 PASS
C13 PASS
C14 PASS

C: 14/14
~~~

### D — CH-003 neighboring-method boundary

~~~text
D1 PASS
D2 PASS
D3 PASS
D4 PASS
D5 PASS
D6 PASS
D7 PASS
D8 PASS
D9 PASS
D10 PASS

D: 10/10
~~~

### E — CH-004 competent baseline

~~~text
E1 PASS
E2 PASS
E3 PASS
E4 PASS
E5 PASS
E6 PASS
E7 PASS
E8 PASS
E9 PASS
E10 PASS

E: 10/10
~~~

### F — CH-005 strongest-reasonable baseline

~~~text
F1 PASS
F2 PASS
F3 PASS
F4 PASS
F5 PASS
F6 PASS
F7 PASS
F8 PASS
F9 PASS
F10 PASS

F: 10/10
~~~

### G — final retrace verdict

~~~text
G1 PASS
G2 PASS
G3 PASS
G4 PASS

G: 4/4
~~~

Final:

~~~text
TOTAL_REQUIRED_CHECKS:
  70

PASSED:
  70

FAILED:
  0
~~~

## 8. Retrace verdict and counters

~~~text
RETRACE_VERDICT:
  PASS

REPRODUCIBILITY_CLASS:
  deterministic_same_project_retrace

REPRODUCIBILITY_CASES:
  1

SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once

CLAIM_RELEVANT_MISMATCHES:
  0

POST_COMPARISON_CORRECTIONS:
  0
~~~

Direct and baseline counters remain unchanged:

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
~~~

Protocol-level state:

~~~text
DIAGNOSIS_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_DIAGNOSIS_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 9. Interpretation limit

Supported:

~~~text
The claim-relevant outputs recorded across DIAG-CH-001 through
DIAG-CH-005 can be deterministically retraced within the same
project from the frozen Diagnosis Protocol and prospectively
frozen challenge semantics, with zero claim-relevant mismatch
and zero post-comparison correction.
~~~

Not supported:

~~~text
independent replication
blinded reproduction
independent validation
external applicability
method superiority
universal protocol correctness
~~~

Preserved:

~~~text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
RETRACE_PASS != METHOD_SUPERIORITY
~~~

## 10. Next

Prospectively precommit:

~~~text
DIAG-AUD-001
frozen-axis internal-standardization audit
~~~

The audit may use DIAG-CH-006 as same-project retraceability evidence but must keep that axis conditional rather than relabeling it as independent replication.

External application and independent validation remain a later evidence phase.
