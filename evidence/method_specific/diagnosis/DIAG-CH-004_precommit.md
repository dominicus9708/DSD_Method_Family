# DIAG-CH-004 — Competent Non-DSD Diagnosis Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-30**  
Challenge ID: `DIAG-CH-004`  
Method: **Diagnosis / DSD 진단론**  
Protocol: **Diagnosis Protocol v0.1**  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

~~~text
DIAGNOSIS_PROTOCOL_COMMIT:
  2d6eb83301860f044cba9a67a87c3a937335823b

DIAGNOSIS_PROTOCOL_BLOB:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129
~~~

No Diagnosis Protocol revision is allowed in response to this baseline result.

## 2. Baseline identity

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_DIAGNOSIS_EVALUATOR

BASELINE_CLASS:
  competent_non_DSD_constructed_diagnosis_evaluator

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
~~~

B0 is intentionally competent rather than weak.

It may use ordinary:

~~~text
stable candidate IDs
versioned task records
typed evidence statuses
provenance/time/regime metadata
candidate-class completeness flags
explicit deterministic forward/compatibility rules
relation-valued compatibility tables
evidence-set consistency checks
required-interface availability flags
support/status sidecars
finite collision/injectivity records
declared residual functions
declared transition relations
explicit cause-model tables
explicit probabilistic interfaces when supplied
candidate filtering
declared-class identifiability checks
blocked/conflict/ambiguity/out-of-scope states
deterministic terminal precedence
bounded-claim reporting
neighbor-method sidecars
~~~

It does not invoke Formation, Property, Static Aggregation, Dynamics, or DSD shared-core concepts as theory.

Terminology, file organization, or DSD naming alone cannot count as gain.

## 3. B0 generic operation

~~~text
B0-1 freeze task/version/claim level/candidate class/completeness
     and maximum-supported claim

B0-2 retain evidence identity, status, provenance, time, regime,
     and direct/proxy role without coercing missing/undefined to zero

B0-3 evaluate evidence-set consistency/conflict under supplied
     schema and precedence rules

B0-4 freeze bridge identity/version/scope and pair rules

B0-5 distinguish bridge unavailable, conflicting, ambiguous,
     and outside-scope states

B0-6 retain required support/status/readout/injectivity sidecars
     and block when a required interface is unavailable

B0-7 freeze deterministic or explicitly supplied probabilistic
     inference mode; never invent priors/likelihoods/posteriors

B0-8 apply supplied resolution/threshold/time/regime rules

B0-9 evaluate supplied residual and transition constraints on
     their declared carriers/scopes

B0-10 assign one disposition per declared candidate:
      compatible / excluded / blocked / conflicting /
      outside scope / unresolved

B0-11 construct compatible/excluded/blocked/conflicting/unresolved sets

B0-12 evaluate uniqueness only within the supplied candidate class
      unless completeness is explicitly supplied

B0-13 preserve zero-compatible declared-class result without
      promoting it to ontological impossibility

B0-14 evaluate cause compatibility or model-bounded cause identification
      only when the requested cause interface is supplied

B0-15 retain additional-observation requirements as handoffs
      rather than selecting an optimum unless a separate objective exists

B0-16 preserve current-state inference separately from past-history recovery

B0-17 apply supplied terminal precedence deterministically while
      retaining subordinate states

B0-18 emit conformance, method-gain placeholder, and bounded maximum claim
~~~

## 4. Frozen output mapping

Primary-status mapping:

~~~text
B0_DIAGNOSIS_ESTABLISHED
  <-> DIAGNOSIS_ESTABLISHED

B0_DIAGNOSIS_NOT_ESTABLISHED
  <-> DIAGNOSIS_NOT_ESTABLISHED

B0_DIAGNOSIS_BLOCKED
  <-> DIAGNOSIS_BLOCKED

B0_DIAGNOSIS_CONFLICT
  <-> DIAGNOSIS_CONFLICTING

B0_DIAGNOSIS_OUTSIDE_SCOPE
  <-> DIAGNOSIS_OUT_OF_SCOPE

B0_DIAGNOSIS_UNRESOLVED
  <-> DIAGNOSIS_UNDERDETERMINED
~~~

Task-terminal mapping:

~~~text
B0_TASK_COMPLETE
  <-> DIAGNOSIS_TASK_ESTABLISHED

B0_TASK_PARTIAL
  <-> DIAGNOSIS_TASK_PARTIAL

B0_TASK_NOT_ESTABLISHED
  <-> DIAGNOSIS_TASK_NOT_ESTABLISHED

B0_TASK_BLOCKED
  <-> DIAGNOSIS_TASK_BLOCKED

B0_TASK_CONFLICT
  <-> DIAGNOSIS_TASK_CONFLICTING

B0_TASK_OUTSIDE_SCOPE
  <-> DIAGNOSIS_TASK_OUT_OF_SCOPE

B0_TASK_UNRESOLVED
  <-> DIAGNOSIS_TASK_UNDERDETERMINED
~~~

Candidate-set mapping:

~~~text
B0_MULTIPLE_COMPATIBLE
  <-> DIAGNOSIS_SET_MULTIPLE_COMPATIBLE

B0_UNIQUE_WITHIN_DECLARED_CLASS
  <-> DIAGNOSIS_SET_UNIQUE_WITHIN_DECLARED_CLASS

B0_NONE_COMPATIBLE_IN_DECLARED_CLASS
  <-> DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS

B0_PARTIALLY_EVALUATED
  <-> DIAGNOSIS_SET_PARTIALLY_EVALUATED

B0_SET_UNRESOLVED
  <-> DIAGNOSIS_SET_UNDERDETERMINED
~~~

## 5. Equal-information rule

Diagnosis and B0 receive the same claim-relevant:

~~~text
task ID/version
primary claim level
maximum-supported claim

candidate class / candidate IDs
candidate-class completeness status

evidence records
typed evidence statuses
provenance / time / regime
evidence-set coherence inputs

bridge IDs/versions/scopes
pair compatibility rules

required-interface availability
Property/Formation status sidecars
support-retention sidecars
readout/collision/injectivity records

resolution / threshold records
residual target/carrier/rule
transition relations / dynamic support

cause-hypothesis class
cause bridge if supplied

probabilistic interface if supplied

terminal precedence
neighboring-method sidecars
~~~

Neither side receives hidden favorable information.

B0 is not asked to derive DSD ontology from first principles.

It executes the same already-frozen claim-relevant task information.

## 6. Frozen fixtures

### Q1 — multiple-compatible current-state diagnosis

Reuse DIAG-CH-001 Subtask A.

~~~text
candidates:
  a1 ALPHA / readout 0 / DEFINED_ZERO / S1
  a2 BETA  / readout 0 / DEFINED_ZERO / S1
  a3 GAMMA / readout 0 / APPLICABLE_BUT_UNDEFINED / S2

transition:
  p0 -> {a1,a2}

evidence:
  readout 0
  status DEFINED_ZERO
  support S1
  transition from p0
~~~

Expected Diagnosis:

~~~text
compatible:
  {a1,a2}

excluded:
  {a3}

DIAGNOSIS_SET_MULTIPLE_COMPATIBLE
DIAGNOSIS_TASK_ESTABLISHED
~~~

Expected B0:

~~~text
compatible:
  {a1,a2}

excluded:
  {a3}

B0_MULTIPLE_COMPATIBLE
B0_TASK_COMPLETE
~~~

Both must preserve:

~~~text
equal readout != equal hidden state
undefined status != defined zero
multiple compatible != task ambiguity
~~~

### Q2 — declared-class uniqueness by residual

Reuse DIAG-CH-001 Subtask B.

~~~text
b1 q=9
b2 q=10
b3 q=11

target:
  q*=10

residual:
  abs(q-10)

criterion:
  compatible iff residual=0

candidate-class completeness:
  not claimed
~~~

Expected both:

~~~text
only b2 compatible
unique within declared class
no global uniqueness claim
~~~

### Q3 — blocked / conflict / underdetermined semantics

Q3A reuses DIAG-CH-002 N2.

~~~text
required support sidecar unavailable
~~~

Expected:

~~~text
Diagnosis:
  DIAGNOSIS_TASK_BLOCKED

B0:
  B0_TASK_BLOCKED
~~~

Q3B reuses DIAG-CH-002 N3.

~~~text
same bridge/version/scope:
  rule A compatible
  rule B incompatible
  no resolver
~~~

Expected:

~~~text
Diagnosis:
  DIAGNOSIS_TASK_CONFLICTING

B0:
  B0_TASK_CONFLICT
~~~

Q3C reuses DIAG-CH-002 N4.

~~~text
two admissible bridge interpretations
different outcomes
no resolver
not mutually contradictory under one interpretation
~~~

Expected:

~~~text
Diagnosis:
  DIAGNOSIS_TASK_UNDERDETERMINED

B0:
  B0_TASK_UNRESOLVED
~~~

### Q4 — evidence conflict versus coherent zero-compatible class

Q4A reuses DIAG-CH-002 N7.

~~~text
same sensor/time/schema:
  S(t0)=0
  S(t0)=1

both marked valid
no resolver
~~~

Expected:

~~~text
Diagnosis:
  EVIDENCE_SET_CONFLICTING
  DIAGNOSIS_TASK_CONFLICTING
  zero-compatible result not asserted

B0:
  evidence packet conflict
  B0_TASK_CONFLICT
  zero-compatible result not asserted
~~~

Q4B reuses DIAG-CH-002 N8.

~~~text
evidence:
  y=2

n1 predicts:
  0

n2 predicts:
  1

evidence coherent
bridge available
~~~

Expected:

~~~text
Diagnosis:
  DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
  DIAGNOSIS_TASK_ESTABLISHED

B0:
  B0_NONE_COMPATIBLE_IN_DECLARED_CLASS
  B0_TASK_COMPLETE

neither:
  NO_REAL_STATE_EXISTS
~~~

### Q5 — cause and inference-mode scope

Q5A reuses DIAG-CH-001 Subtask C.

~~~text
cause candidates:
  c1
  c2

marker evidence:
  M=PRESENT
  K=PRESENT

compatibility bridge:
  c1 compatible
  c2 incompatible

causal proof bridge:
  not supplied

claim:
  CAUSE_COMPATIBILITY_ONLY
~~~

Expected both:

~~~text
c1 compatible
c2 excluded
cause compatibility only
no causal-proof promotion
~~~

Q5B uses the DIAG-CH-002 probabilistic boundary.

~~~text
request:
  rank compatible candidates by posterior probability

priors:
  absent

likelihood:
  absent

posterior semantics:
  absent
~~~

Expected:

~~~text
Diagnosis:
  ranking claim OUT_OF_SCOPE

B0:
  ranking claim OUTSIDE_SCOPE

neither invents priors
~~~

### Q6 — partial / precedence / neighboring-sidecar discipline

Q6A reuses DIAG-CH-002 N6.

~~~text
Q1:
  established compatibility-set obligation

Q2:
  evaluably failed uniqueness obligation

both:
  independent
  in scope
  no higher terminal
~~~

Expected:

~~~text
Diagnosis:
  DIAGNOSIS_TASK_PARTIAL

B0:
  B0_TASK_PARTIAL
~~~

Q6B reuses DIAG-CH-002 N10.

~~~text
Q1 out_of_scope
Q2 conflicting
Q3 underdetermined
Q4 blocked
~~~

Both apply:

~~~text
OUT_OF_SCOPE
>
CONFLICT
>
UNRESOLVED
>
BLOCKED
>
COMPLETE/PARTIAL/NOT_ESTABLISHED
~~~

Expected final:

~~~text
Diagnosis:
  DIAGNOSIS_TASK_OUT_OF_SCOPE

B0:
  B0_TASK_OUTSIDE_SCOPE

lower states retained:
  yes
~~~

Q6C supplies identical neighboring sidecars:

~~~text
Measurement
Reconstruction
Classification
Comparison
Prediction
Simulation
Optimization
Audit
Tracking
Lineage
~~~

Neither evaluator may infer without an explicit rule:

~~~text
Diagnosis from Measurement sufficiency
current Diagnosis from Reconstruction candidate
Diagnosis from Classification label
Diagnosis from Comparison similarity
observed state from Simulation trajectory
current Diagnosis from Prediction output
compatibility from Optimization optimum
Diagnosis result from Audit pass
hidden-state identity from Tracking provenance
current Diagnosis from Lineage identity
~~~

## 7. Frozen gain axes

~~~text
G1 typed-status / evidence-coherence advantage

G2 bridge / pair-status / required-interface advantage

G3 candidate-set / declared-class identifiability advantage

G4 readout-loss / residual / transition-discipline advantage

G5 cause-scope / probabilistic-interface advantage

G6 terminal / bounded-claim / neighboring-sidecar advantage
~~~

Allowed axis result:

~~~text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
~~~

Overall gain rule:

~~~text
if all claim-relevant outputs and all six gain axes match:
  DIAGNOSIS_METHOD_GAIN_STATUS =
    DIAGNOSIS_METHOD_GAIN_NO_GAIN

if one or more frozen claim-relevant axes establish a DSD advantage:
  DIAGNOSIS_METHOD_GAIN_STATUS =
    DIAGNOSIS_METHOD_GAIN_ESTABLISHED

if one or more axes establish a baseline advantage:
  preserve BASELINE_ADVANTAGE on those axes
  and do not relabel it as DSD gain

otherwise:
  DIAGNOSIS_METHOD_GAIN_STATUS =
    DIAGNOSIS_METHOD_GAIN_UNDERDETERMINED
~~~

Vocabulary or DSD-specific naming is not a gain axis.

## 8. Frozen scoring — 64 checks

### A. Fairness and immutability — 10

~~~text
A1 Diagnosis Protocol commit/blob fixed
A2 B0 operation fixed before execution
A3 output mappings fixed
A4 Q1-Q6 fixed before execution
A5 equal-information rule respected
A6 B0 receives every Diagnosis-visible claim-relevant input
A7 Diagnosis receives no hidden favorable input
A8 no post-hoc gain axis added
A9 no baseline rule changed after result inspection
A10 external application remains no
~~~

### B. Q1 multiple-compatible diagnosis — 12

~~~text
B1 both retain all three candidate IDs
B2 both retain equal main readout 0
B3 both retain typed status distinction
B4 both retain support distinction
B5 both retain transition relation
B6 both keep a1 compatible
B7 both keep a2 compatible
B8 both exclude a3
B9 both return exactly {a1,a2}
B10 both return multiple-compatible set outcome
B11 neither converts multiplicity to task underdetermination
B12 corresponding task terminals match
~~~

### C. Q2 residual / declared-class uniqueness — 10

~~~text
C1 both use same scalar residual
C2 both compute residuals 1,0,1
C3 both exclude b1
C4 both retain b2
C5 both exclude b3
C6 both return unique-within-declared-class
C7 both retain completeness-not-claimed
C8 neither promotes to global uniqueness
C9 neither treats residual zero as universal identity
C10 corresponding task terminals match
~~~

### D. Q3 blocked / conflict / underdetermined — 10

~~~text
D1 both treat unavailable support interface as BLOCKED
D2 neither converts unavailable to negative evidence
D3 both detect same-version bridge conflict
D4 both return conflict terminal
D5 neither relabels conflict as ordinary incompatibility
D6 both retain two admissible semantics in Q3C
D7 both detect differing outcomes
D8 both preserve no-resolver state
D9 both return unresolved/underdetermined terminal
D10 blocked, conflict, and underdetermined remain distinct
~~~

### E. Q4 evidence conflict / zero-compatible class — 10

~~~text
E1 both detect Q4A evidence conflict
E2 neither asserts zero-compatible set in Q4A
E3 both return conflict terminal in Q4A
E4 both treat Q4B evidence as coherent
E5 both exclude n1
E6 both exclude n2
E7 both return zero-compatible declared-class outcome
E8 both return established/complete terminal for Q4B
E9 neither asserts no real state exists
E10 evidence conflict remains distinct from coherent zero-candidate result
~~~

### F. Q5-Q6 cause / probability / partial / precedence / sidecars — 8

~~~text
F1 both preserve cause compatibility without causal proof
F2 both reject unsupported posterior ranking as outside scope
F3 neither invents priors/likelihoods
F4 both return PARTIAL for valid mixed in-scope obligations
F5 neither uses PARTIAL to rescue one atomic failure
F6 both apply frozen terminal precedence
F7 both retain lower subordinate states
F8 both preserve neighboring-sidecar non-substitution
~~~

### G. Gain conclusion — 4

~~~text
G1 six gain axes scored only from frozen outputs
G2 equal-information fairness remains visible
G3 NO_GAIN preserved if all six axes are BASELINE_MATCH
G4 NO_GAIN does not imply failure/deletion/merger/absorption/redundancy
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  64

PASS_THRESHOLD:
  64/64

PARTIAL_PASS_ALLOWED:
  no
~~~

## 9. Allowed counter changes on 64/64 PASS

~~~text
DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  3 -> 4

SUCCESSFUL_DIRECT_DIAGNOSIS_PILOTS:
  3 -> 4

BASELINE_DIAGNOSIS_CASES:
  0 -> 1
~~~

If all six gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_DIAGNOSIS_CASES:
  0 -> 1
~~~

Unchanged:

~~~text
POSITIVE_DIAGNOSIS_CASES:
  1

NEGATIVE_OR_UNRESOLVED_DIAGNOSIS_CASES:
  1

METHOD_BOUNDARY_DIAGNOSIS_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  10

STRONGEST_REASONABLE_BASELINE_DIAGNOSIS:
  not established

REPRODUCIBILITY_CASES:
  0

EXTERNAL_DIAGNOSIS_APPLICATIONS:
  0

INDEPENDENT_DIAGNOSIS_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established
~~~

## 10. Interpretation lock

A fair `NO_GAIN` result means only:

~~~text
no claim-relevant DSD Diagnosis performance advantage over this
competent constructed baseline was established for these
frozen Diagnosis tasks under equal-information access
~~~

It does not mean:

~~~text
Diagnosis Protocol failure
Diagnosis method deletion
Diagnosis must merge into Measurement
Diagnosis must merge into Reconstruction
Diagnosis must merge into Classification
permanent redundancy
absence of theoretical/organizational value
future DSD gain is impossible
~~~

Required guards:

~~~text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

## 11. Next

After execution, if all frozen outputs match and the result is NO_GAIN, proceed to a strongest-reasonable non-DSD Diagnosis baseline challenge.
