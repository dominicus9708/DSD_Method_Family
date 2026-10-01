# RECON-CH-004 — Competent Non-DSD Reconstruction Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-01**  
Challenge ID: `RECON-CH-004`  
Method: **Reconstruction / DSD 복원론**  
Protocol: **Reconstruction Protocol v0.1**  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

~~~text
RECONSTRUCTION_PROTOCOL_COMMIT:
  2d4cdcab4b646a9d75f96dcc2ef301722eb612ad

RECONSTRUCTION_PROTOCOL_BLOB:
  1f009e81b9992fbdec75abbd9551e9d06f0a170e
~~~

No Reconstruction Protocol revision is allowed in response to this baseline result.

## 2. Baseline identity

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_INVERSE_RECONSTRUCTION_EVALUATOR

BASELINE_CLASS:
  competent_non_DSD_constructed_inverse_reconstruction_evaluator

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
stable task and candidate IDs
extensional or intensional source classes
symbolic set / exact preimage / theorem-based evaluation
class-completeness flags

typed evidence records
provenance / time / regime metadata
evidence consistency checks

versioned forward / observation / reduction maps
relation-valued transition/history constraints
required-interface availability flags

support / status / provenance sidecars
collision / fiber / kernel / injectivity records
declared-class inverse uniqueness checks

interface-closure declarations
recoverability / nonidentifiability tests
history-relation consistency/composition checks

blocked / conflicting / unresolved / outside-scope states
deterministic terminal precedence
bounded-claim reporting
neighbor-method handoff records
~~~

It does not invoke Formation, Property, Static Aggregation, Structural Reorganization Dynamics, or DSD shared-core concepts as theory.

Terminology, file organization, or DSD naming alone cannot count as gain.

## 3. B0 generic operation

~~~text
B0-1 freeze task/version/primary claim/target kind/maximum claim

B0-2 freeze source/history candidate class, representation mode,
     evaluation mode, and completeness status

B0-3 retain evidence identity/status/provenance/time/regime/direct-or-proxy role

B0-4 evaluate evidence-set consistency/conflict under supplied schema

B0-5 freeze forward/observation/reduction/history bridge
     identity/version/scope/direction

B0-6 distinguish bridge unavailable/conflicting/unresolved/outside-scope states

B0-7 retain required support/status/provenance/relational sidecars;
     block dependent claims when required interfaces are unavailable

B0-8 evaluate candidate/evidence compatibility elementwise or symbolically

B0-9 compute compatible/excluded/blocked/conflicting/unresolved candidate sets

B0-10 evaluate collision/fiber/kernel/injectivity only on the supplied scope

B0-11 evaluate uniqueness only inside the supplied class/scope

B0-12 preserve multiple compatible candidates without arbitrary selection

B0-13 preserve zero-compatible declared-class outcome without
      promoting it to universal source nonexistence

B0-14 evaluate interface-bounded nonidentifiability only when
      the supplied interface is explicitly complete for the requested claim

B0-15 evaluate history relation consistency/composition while
      preserving branch/merge multiplicity

B0-16 keep inferred predecessor/trace candidates distinct from
      supplied established trace or identity relations

B0-17 preserve definitional recomputation separately from inverse inference

B0-18 apply supplied terminal precedence while retaining subordinate states;
      emit bounded maximum claim and method-gain placeholder
~~~

## 4. Frozen output mapping

Primary-status mapping:

~~~text
B0_RECONSTRUCTION_ESTABLISHED
  <-> RECONSTRUCTION_ESTABLISHED

B0_RECONSTRUCTION_NOT_ESTABLISHED
  <-> RECONSTRUCTION_NOT_ESTABLISHED

B0_RECONSTRUCTION_BLOCKED
  <-> RECONSTRUCTION_BLOCKED

B0_RECONSTRUCTION_CONFLICT
  <-> RECONSTRUCTION_CONFLICTING

B0_RECONSTRUCTION_OUTSIDE_SCOPE
  <-> RECONSTRUCTION_OUT_OF_SCOPE

B0_RECONSTRUCTION_UNRESOLVED
  <-> RECONSTRUCTION_UNDERDETERMINED
~~~

Task-terminal mapping:

~~~text
B0_TASK_COMPLETE
  <-> RECONSTRUCTION_TASK_ESTABLISHED

B0_TASK_PARTIAL
  <-> RECONSTRUCTION_TASK_PARTIAL

B0_TASK_NOT_ESTABLISHED
  <-> RECONSTRUCTION_TASK_NOT_ESTABLISHED

B0_TASK_BLOCKED
  <-> RECONSTRUCTION_TASK_BLOCKED

B0_TASK_CONFLICT
  <-> RECONSTRUCTION_TASK_CONFLICTING

B0_TASK_OUTSIDE_SCOPE
  <-> RECONSTRUCTION_TASK_OUT_OF_SCOPE

B0_TASK_UNRESOLVED
  <-> RECONSTRUCTION_TASK_UNDERDETERMINED
~~~

Candidate-set mapping:

~~~text
B0_MULTIPLE_COMPATIBLE
  <-> RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE

B0_UNIQUE_WITHIN_DECLARED_CLASS
  <-> RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS

B0_NONE_COMPATIBLE_IN_DECLARED_CLASS
  <-> RECONSTRUCTION_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS

B0_PARTIALLY_EVALUATED
  <-> RECONSTRUCTION_SET_PARTIALLY_EVALUATED

B0_SET_CONFLICT
  <-> RECONSTRUCTION_SET_CONFLICTING

B0_SET_UNRESOLVED
  <-> RECONSTRUCTION_SET_UNDERDETERMINED
~~~

Recovery mapping:

~~~text
B0_RECOVERABLE_ON_DECLARED_SCOPE
  <-> RECOVERABLE_ON_DECLARED_SCOPE

B0_NONUNIQUE_ON_DECLARED_SCOPE
  <-> NONUNIQUE_ON_DECLARED_SCOPE

B0_UNRECOVERABLE_ON_COMPLETE_FROZEN_INTERFACE
  <-> UNRECOVERABLE_DISTINCTION_ESTABLISHED_ON_FROZEN_INTERFACE
~~~

## 5. Equal-information rule

Reconstruction and B0 receive the same claim-relevant:

~~~text
task ID/version
primary claim level
target kind
maximum-supported claim

reconstruction class
class representation/evaluation mode
class completeness status

evidence records
typed evidence statuses
provenance / time / regime
evidence-set coherence inputs

forward / observation / reduction / history bridge
bridge ID/version/scope/direction
pair compatibility rules

required-interface availability
support/status/provenance/relational sidecars

collision/fiber/kernel/injectivity records
reconstruction scope / uniqueness scope

interface-closure declaration
frozen interface component register
recoverability/unrecoverability claim scope

history relation / composition rule
Tracking / Lineage handoff records when supplied

definitional-recompletion role
terminal precedence
neighboring-method sidecars
~~~

Neither side receives hidden favorable information.

B0 is not asked to derive DSD ontology from first principles.

It executes the same already-frozen claim-relevant inverse-reconstruction task information.

## 6. Frozen fixtures

### Q1 — multiple-compatible compressed-source reconstruction

Reuse RECON-CH-001 Subtask A.

~~~text
class:
  a1=(1,2)
  a2=(2,1)
  a3=(0,0)

forward:
  F(x1,x2)=x1+x2

evidence:
  y=3
~~~

Expected Reconstruction:

~~~text
compatible:
  {a1,a2}

excluded:
  {a3}

RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE
RECONSTRUCTION_TASK_ESTABLISHED
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
equal output != equal source
multiple compatible != task unresolved
noninjective map != permission to select one preimage
~~~

### Q2 — declared-class prior-state uniqueness

Reuse RECON-CH-001 Subtask B.

~~~text
b1:
  prior=P1
  marker=RED

b2:
  prior=P2
  marker=BLUE

b3:
  prior=P3
  marker=BLUE

current:
  C

transition:
  P1 !-> C
  P2  -> C
  P3 !-> C

marker evidence:
  BLUE

class completeness:
  not claimed
~~~

Expected both:

~~~text
only b2 compatible
unique within declared class
global historical uniqueness not claimed
lineage identity not promoted
~~~

### Q3 — blocked / conflict / underdetermined semantics

Q3A reuses RECON-CH-002 N2.

~~~text
required support/source-identity sidecar unavailable
replacement interface absent
~~~

Expected:

~~~text
Reconstruction:
  RECONSTRUCTION_TASK_BLOCKED

B0:
  B0_TASK_BLOCKED
~~~

Q3B reuses RECON-CH-002 N3.

~~~text
same bridge/version/scope
rule A compatible
rule B incompatible
resolver none
~~~

Expected:

~~~text
Reconstruction:
  RECONSTRUCTION_TASK_CONFLICTING

B0:
  B0_TASK_CONFLICT
~~~

Q3C reuses RECON-CH-002 N4.

~~~text
two admissible bridge interpretations
different outcomes
no resolver
~~~

Expected:

~~~text
Reconstruction:
  RECONSTRUCTION_TASK_UNDERDETERMINED

B0:
  B0_TASK_UNRESOLVED
~~~

### Q4 — evidence conflict versus coherent zero-compatible class

Q4A reuses RECON-CH-002 N7.

~~~text
same readout carrier/time/regime/schema
e1:
  Y=0
e2:
  Y=1
both valid
resolver none
~~~

Expected:

~~~text
Reconstruction:
  EVIDENCE_SET_CONFLICTING
  RECONSTRUCTION_TASK_CONFLICTING
  zero-compatible set not asserted

B0:
  evidence packet conflict
  B0_TASK_CONFLICT
  zero-compatible set not asserted
~~~

Q4B reuses RECON-CH-002 N8.

~~~text
class:
  {n1,n2}

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
Reconstruction:
  RECONSTRUCTION_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
  RECONSTRUCTION_TASK_ESTABLISHED

B0:
  B0_NONE_COMPATIBLE_IN_DECLARED_CLASS
  B0_TASK_COMPLETE

neither:
  NO_REAL_PAST_STATE_OR_HISTORY
~~~

### Q5 — interface-bounded unrecoverability and recoverability

Q5A reuses RECON-CH-001 Subtask C.

~~~text
u1=(1,0)
u2=(0,1)

F(x1,x2)=x1+x2

F(u1)=1
F(u2)=1

evidence:
  readout=1

interface closure:
  complete for distinguishing u1 versus u2

frozen sidecars:
  none
~~~

Expected:

~~~text
both retain {u1,u2}
both establish interface-bounded unrecoverability
neither claims absolute future unrecoverability
~~~

Q5B reuses RECON-CH-002 N9.

~~~text
k1:
  main readout=1
  support=S1

k2:
  main readout=1
  support=S2

evidence:
  readout=1
  support=S1

interface closure:
  complete for claim
~~~

Expected:

~~~text
both retain only k1
both establish recoverability on declared scope
requested unrecoverability claim not established
~~~

### Q6 — partial / precedence / history-handoff / neighboring-sidecar discipline

Q6A reuses RECON-CH-002 N6.

~~~text
Q1:
  established compatibility-set obligation

Q2:
  evaluably failed uniqueness obligation

both independent
both in scope
no higher-priority terminal
~~~

Expected:

~~~text
Reconstruction:
  RECONSTRUCTION_TASK_PARTIAL

B0:
  B0_TASK_PARTIAL
~~~

Q6B reuses RECON-CH-002 N10.

~~~text
Q1 OUT_OF_SCOPE
Q2 CONFLICTING
Q3 UNDERDETERMINED
Q4 BLOCKED
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

and retain lower subordinate states.

Q6C supplies identical neighboring/source handoffs:

~~~text
Diagnosis
Aggregation
Compression
Tracking
Lineage
Measurement
Transformation
Prediction
Simulation
Optimization
Audit
Formation witness-history
~~~

Neither evaluator may infer without an explicit supplied rule:

~~~text
past Reconstruction from current Diagnosis
source identity from aggregate equality
recovery success from Compression success
established trace from reconstructed link
established Lineage from candidate predecessor
Reconstruction success from Measurement sufficiency
inverse identity from forward Transformation correctness
past history from Prediction output
actual history from simulated trajectory
historical exclusion from Optimization ranking
historical truth from Audit pass
actual temporal history from Formation witness-history
~~~

## 7. Frozen gain axes

~~~text
G1 class-representation / completeness / candidate-set advantage

G2 typed-evidence / bridge-coherence / required-interface advantage

G3 collision-fiber / injectivity / bounded-uniqueness advantage

G4 interface-closure / recoverability / unrecoverability advantage

G5 history-relation / Tracking-Lineage / source-handoff discipline advantage

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
  RECONSTRUCTION_METHOD_GAIN_STATUS =
    RECONSTRUCTION_NO_GAIN

if one or more frozen claim-relevant axes establish a DSD advantage:
  RECONSTRUCTION_METHOD_GAIN_STATUS =
    RECONSTRUCTION_GAIN_SHOWN

if one or more axes establish a baseline advantage:
  preserve BASELINE_ADVANTAGE on those axes
  and do not relabel it as DSD gain

otherwise:
  RECONSTRUCTION_METHOD_GAIN_STATUS =
    RECONSTRUCTION_GAIN_UNDERDETERMINED
~~~

Vocabulary, notation, file organization, or DSD naming is not a gain axis.

## 8. Frozen scoring — 64 checks

### A. Fairness and immutability — 10

~~~text
A1 Reconstruction Protocol commit/blob fixed
A2 B0 operation fixed before execution
A3 output mappings fixed
A4 Q1-Q6 fixed before execution
A5 equal-information rule respected
A6 B0 receives every Reconstruction-visible claim-relevant input
A7 Reconstruction receives no hidden favorable input
A8 no post-hoc gain axis added
A9 no baseline rule changed after result inspection
A10 external application remains no
~~~

### B. Q1 multiple-compatible compressed source — 12

~~~text
B1 both retain a1,a2,a3
B2 both use the same F(x1,x2)=x1+x2
B3 both retain evidence y=3
B4 both compute a1 -> 3
B5 both compute a2 -> 3
B6 both compute a3 -> 0
B7 both keep a1 compatible
B8 both keep a2 compatible
B9 both exclude a3
B10 both return exactly {a1,a2}
B11 both return multiple-compatible without selecting one preimage
B12 corresponding task terminals match
~~~

### C. Q2 declared-class prior-state uniqueness — 10

~~~text
C1 both retain P1/P2/P3 candidate identities
C2 both retain RED/BLUE/BLUE marker values
C3 both retain the same transition relation
C4 both retain observed marker BLUE
C5 both exclude b1
C6 both retain b2
C7 both exclude b3
C8 both return unique-within-declared-class
C9 neither promotes to global historical truth or established Lineage
C10 corresponding task terminals match
~~~

### D. Q3 blocked / conflict / underdetermined — 10

~~~text
D1 both treat unavailable required sidecar as BLOCKED
D2 neither converts unavailable sidecar to destructive-loss proof
D3 both detect same-version bridge conflict
D4 both return conflict terminal
D5 neither relabels conflict as ordinary incompatibility
D6 both retain two admissible bridge semantics in Q3C
D7 both detect different outcomes
D8 both preserve no-resolver state
D9 both return unresolved/underdetermined terminal
D10 blocked, conflict, and underdetermined remain distinct
~~~

### E. Q4-Q5 zero-compatible / interface closure / recovery — 10

~~~text
E1 both distinguish evidence conflict from coherent zero-compatible class
E2 both return bounded zero-compatible declared-class result for Q4B
E3 neither asserts no real past/source exists
E4 both retain u1 and u2 in Q5A
E5 both require complete-for-claim interface before unrecoverability
E6 both establish interface-bounded unrecoverability in Q5A
E7 neither promotes Q5A to absolute future unrecoverability
E8 both use the frozen support sidecar in Q5B
E9 both retain only k1 in Q5B
E10 both establish declared-scope recoverability and reject Q5B unrecoverability
~~~

### F. Q6 partial / precedence / handoff discipline — 8

~~~text
F1 both return PARTIAL for valid mixed independent obligations
F2 neither uses PARTIAL to rescue one atomic failure
F3 both apply frozen terminal precedence
F4 both retain lower subordinate states
F5 both preserve Tracking non-substitution
F6 both preserve Lineage non-substitution
F7 both preserve current-Diagnosis / past-Reconstruction separation
F8 both preserve source/neighboring-sidecar non-substitution
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

Any mismatch must remain visible.

## 9. Allowed counter changes on 64/64 PASS

~~~text
DIRECT_RECONSTRUCTION_PILOTS_ATTEMPTED:
  3 -> 4

SUCCESSFUL_DIRECT_RECONSTRUCTION_PILOTS:
  3 -> 4

BASELINE_RECONSTRUCTION_CASES:
  0 -> 1
~~~

If all six gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_RECONSTRUCTION_CASES:
  0 -> 1
~~~

Unchanged:

~~~text
POSITIVE_RECONSTRUCTION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_RECONSTRUCTION_CASES:
  1

METHOD_BOUNDARY_RECONSTRUCTION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11

STRONGEST_REASONABLE_BASELINE_RECONSTRUCTION:
  not established

REPRODUCIBILITY_CASES:
  0

EXTERNAL_RECONSTRUCTION_APPLICATIONS:
  0

INDEPENDENT_RECONSTRUCTION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established
~~~

## 10. Interpretation lock

A fair `NO_GAIN` result means only:

~~~text
no claim-relevant DSD Reconstruction performance advantage over this
competent constructed baseline was established for these frozen
Reconstruction tasks under equal-information access
~~~

It does not mean:

~~~text
Reconstruction Protocol failure
Reconstruction method deletion
Reconstruction should merge into Diagnosis
Reconstruction should merge into Aggregation or Compression
permanent redundancy
absence of theoretical or organizational value
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

After execution, if all frozen outputs match and the result is NO_GAIN, proceed to a strongest-reasonable non-DSD Reconstruction baseline challenge.
