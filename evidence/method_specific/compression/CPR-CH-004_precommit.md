# CPR-CH-004 — Competent Non-DSD Compression Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-28**  
Challenge ID: `CPR-CH-004`  
Method: **Compression / DSD 압축론**  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

~~~text
COMPRESSION_PROTOCOL_VERSION:
  v0.1

COMPRESSION_PROTOCOL_COMMIT:
  b1efa06e4c715e08ce2558a608c7f09aa22172bd

COMPRESSION_PROTOCOL_BLOB:
  4d67d800e107229f91c16cf5b0235928124482b2
~~~

No Compression Protocol revision is allowed in response to this baseline result.

## 2. Baseline identity

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_COMPRESSION_EVALUATOR

BASELINE_CLASS:
  competent_non_DSD_constructed_compression_evaluator

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
stable object IDs
typed status flags
versioned task records
declared source and output schemas
declared deterministic maps
purpose / feature-retention rules
safe-merge / must-distinguish pair tables
finite collision/fiber checks
explicit representation-cost metrics
sidecar accounting
resolution/threshold records
finite injectivity tests on declared classes
inverse/reconstruction prerequisite tables
composition-chain records
required-interface availability checks
conflict/ambiguity tables
deterministic terminal precedence
bounded-claim reporting
neighboring-record sidecars
~~~

It does not invoke Formation, Property, Static Aggregation, Dynamics, or the DSD shared core as theory.

Vocabulary, file layout, or DSD naming alone cannot count as gain.

## 3. B0 generic operation

B0 performs:

~~~text
B0-1 freeze task ID/version, source schema, purpose, deterministic map,
     output schema, accounting metric, reduction requirement,
     optional sidecar requirements, and maximum claim

B0-2 retain supplied object IDs, typed statuses, support/provenance fields,
     and labels separately

B0-3 freeze must-distinguish and safe-to-merge relations;
     reject same-pair incompatible rules unless a supplied resolver exists

B0-4 when multiple purposes or thresholds are supplied, apply the supplied
     composition/precedence rule and preserve unresolved alternatives

B0-5 reject stochastic encoders unless a stochastic interface was supplied;
     otherwise execute only the frozen deterministic map/chain

B0-6 apply the frozen map to the supplied source class without post-hoc
     replacement

B0-7 compare equal-output source pairs/fibers against the supplied
     must-distinguish and safe-merge rules

B0-8 retain collision consequences separately for purpose, typed-status,
     support, provenance, and requested inverse/reconstruction claims

B0-9 preserve required typed status/support/provenance information directly
     or in supplied sidecars; do not coerce unavailable/undefined to zero

B0-10 evaluate source cost and reduced-package cost under the same supplied
      accounting metric and sidecar scope

B0-11 distinguish purpose preservation from actual reduction;
      preserving all distinctions with no required reduction does not pass
      a strict compression task

B0-12 when losslessness is requested on a declared finite class,
      test injectivity only on that class and do not promote to global

B0-13 keep inverse/reconstruction scope and required prerequisites separate
      from forward compression success

B0-14 keep unavailable required interfaces as BLOCKED rather than evaluable
      destructive-loss evidence

B0-15 keep conflict, outside-scope, unresolved, evaluable failure, and
      multi-obligation partial outcomes distinct

B0-16 for composed chains, apply the supplied end-to-end preservation rule;
      do not infer end-to-end success from local stage success

B0-17 apply supplied terminal precedence deterministically and retain
      lower-level statuses

B0-18 retain neighboring-method records as sidecars unless a supplied rule
      explicitly makes them part of the compression task; emit only the
      bounded claim justified by supplied data
~~~

## 4. Frozen output mapping

Primary-result mapping:

~~~text
B0_COMPRESSION_ESTABLISHED
  <-> COMPRESSION_ESTABLISHED

B0_COMPRESSION_NOT_ESTABLISHED
  <-> COMPRESSION_NOT_ESTABLISHED

B0_COMPRESSION_BLOCKED
  <-> COMPRESSION_BLOCKED

B0_COMPRESSION_CONFLICT
  <-> COMPRESSION_CONFLICTING

B0_COMPRESSION_OUTSIDE_SCOPE
  <-> COMPRESSION_OUT_OF_SCOPE

B0_COMPRESSION_UNRESOLVED
  <-> COMPRESSION_UNDERDETERMINED
~~~

Task-terminal mapping:

~~~text
B0_TASK_COMPLETE
  <-> COMPRESSION_TASK_ESTABLISHED

B0_TASK_PARTIAL
  <-> COMPRESSION_TASK_PARTIAL

B0_TASK_NOT_ESTABLISHED
  <-> COMPRESSION_TASK_NOT_ESTABLISHED

B0_TASK_BLOCKED
  <-> COMPRESSION_TASK_BLOCKED

B0_TASK_CONFLICT
  <-> COMPRESSION_TASK_CONFLICTING

B0_TASK_OUTSIDE_SCOPE
  <-> COMPRESSION_TASK_OUT_OF_SCOPE

B0_TASK_UNRESOLVED
  <-> COMPRESSION_TASK_UNDERDETERMINED
~~~

Reduction mapping:

~~~text
B0_REDUCTION_ESTABLISHED
  <-> REDUCTION_ESTABLISHED

B0_REDUCTION_NOT_ESTABLISHED
  <-> REDUCTION_NOT_ESTABLISHED
~~~

Collision mapping:

~~~text
B0_COLLISION_WITNESS
  <-> COLLISION_WITNESS_ESTABLISHED

B0_NO_COLLISION_ON_DECLARED_CLASS
  <-> NO_COLLISION_ON_TESTED_CLASS

B0_PURPOSE_SAFE_COLLISION
  <-> COLLISION_PURPOSE_SAFE

B0_PURPOSE_DESTRUCTIVE_COLLISION
  <-> COLLISION_PURPOSE_DESTRUCTIVE
~~~

Losslessness / reconstruction mapping:

~~~text
B0_LOSSLESS_ON_DECLARED_CLASS
  <-> LOSSLESS_ON_DECLARED_CLASS

B0_LOSSLESSNESS_NOT_ESTABLISHED
  <-> LOSSLESSNESS_NOT_ESTABLISHED

B0_RECONSTRUCTION_NOT_CLAIMED
  <-> RECONSTRUCTION_NOT_CLAIMED

B0_RECONSTRUCTION_NOT_ESTABLISHED
  <-> RECONSTRUCTION_NOT_ESTABLISHED

B0_RECONSTRUCTION_BLOCKED
  <-> RECONSTRUCTION_BLOCKED
~~~

## 5. Equal-information rule

For every fixture, Compression and B0 receive the same claim-relevant:

~~~text
task ID/version
primary claim level
maximum-supported claim

source/interface IDs
source object class
source representation
typed statuses
support/provenance data

downstream purpose
purpose scope/composition/precedence
must-distinguish relation
safe-to-merge relation

compression map/version
output schema

resolution records and resolver state

representation-accounting scope
cost metric
source cost inputs
reduced-package cost inputs
reduction requirement

collision/fiber data or data sufficient to derive it
status/support/provenance-retention requirements

declared-class losslessness request/data
reconstruction scope/prerequisites
relational/cross-coordinate requirements

composition-chain records
required-interface availability
conflict/scope/alternative-semantics records
terminal precedence

neighboring-method sidecars
~~~

Neither side receives hidden favorable information.

B0 is not asked to derive the DSD source ontology from first principles.

It is asked to execute the same already-frozen claim-relevant task information.

## 6. Frozen fixtures

### Q1 — positive lossy purpose-safe compression

Reuse CPR-CH-001.

~~~text
x1=(A,a1,NONZERO)
x2=(A,a2,NONZERO)
x3=(B,b1,ZERO)
x4=(B,b2,ZERO)

map:
  C(group,detail,status)=(group,status)

must distinguish:
  all cross-group/status pairs

safe to merge:
  (x1,x2)
  (x3,x4)

source cost:
  12 FIELD_UNIT_COUNT-v1

reduced package cost:
  8 FIELD_UNIT_COUNT-v1
~~~

Expected Compression:

~~~text
PURPOSE_RELATION_CONSISTENT
COLLISION_WITNESS_ESTABLISHED
two purpose-safe collisions
status preserved
REDUCTION_ESTABLISHED
LOSSLESSNESS_NOT_ESTABLISHED
RECONSTRUCTION_NOT_CLAIMED
COMPRESSION_TASK_ESTABLISHED
~~~

Expected B0:

~~~text
purpose rules consistent
same two collision witnesses
both collisions safe for supplied purpose
typed status preserved
B0_REDUCTION_ESTABLISHED
B0_LOSSLESSNESS_NOT_ESTABLISHED
B0_RECONSTRUCTION_NOT_CLAIMED
B0_TASK_COMPLETE
~~~

### Q2 — destructive collision and failed reduction

Q2A reuses CPR-CH-002 N1.

~~~text
x1=(A,1)
x2=(B,1)
C(group,value)=value

pair required-distinct
C(x1)=C(x2)=1
~~~

Expected:

~~~text
Compression:
  COLLISION_PURPOSE_DESTRUCTIVE
  REDUCTION_ESTABLISHED
  COMPRESSION_TASK_NOT_ESTABLISHED

B0:
  B0_PURPOSE_DESTRUCTIVE_COLLISION
  B0_REDUCTION_ESTABLISHED
  B0_TASK_NOT_ESTABLISHED
~~~

Q2B reuses CPR-CH-002 N2.

~~~text
identity map
all required distinctions preserved
source cost=4
reduced cost=4
strict reduction required
~~~

Expected:

~~~text
Compression:
  REDUCTION_NOT_ESTABLISHED
  COMPRESSION_TASK_NOT_ESTABLISHED

B0:
  B0_REDUCTION_NOT_ESTABLISHED
  B0_TASK_NOT_ESTABLISHED
~~~

### Q3 — blocked / conflict / unresolved semantics

Q3A reuses CPR-CH-002 N3.

~~~text
defined-zero vs absent distinction required
required source-status sidecar unavailable
~~~

Expected:

~~~text
Compression:
  COMPRESSION_TASK_BLOCKED

B0:
  B0_TASK_BLOCKED
~~~

Q3B reuses CPR-CH-002 N4.

~~~text
same pair:
  required-distinct
  safe-to-merge

same purpose/version
no precedence resolver
~~~

Expected:

~~~text
Compression:
  PURPOSE_RELATION_CONFLICTING
  COMPRESSION_TASK_CONFLICTING

B0:
  purpose-rule conflict
  B0_TASK_CONFLICT
~~~

Q3C reuses CPR-CH-002 N6.

~~~text
epsilon_1:
  pass

epsilon_2:
  fail

both admissible
resolver absent
~~~

Expected:

~~~text
Compression:
  RESOLUTION_UNDERDETERMINED
  COMPRESSION_TASK_UNDERDETERMINED

B0:
  unresolved threshold semantics
  B0_TASK_UNRESOLVED
~~~

### Q4 — reconstruction boundary and declared-class losslessness

Q4A reuses CPR-CH-002 N8.

~~~text
x1=(A,a1)
x2=(A,a2)
C(group,detail)=group

immediate purpose:
  detail may merge

required inverse claim:
  exact detail recovery
~~~

Expected:

~~~text
Compression:
  COLLISION_PURPOSE_SAFE
  COLLISION_RECONSTRUCTION_DESTRUCTIVE
  RECONSTRUCTION_NOT_ESTABLISHED
  COMPRESSION_TASK_NOT_ESTABLISHED

B0:
  purpose-safe collision
  inverse claim destructive
  B0_RECONSTRUCTION_NOT_ESTABLISHED
  B0_TASK_NOT_ESTABLISHED
~~~

Q4B reuses CPR-CH-002 N9.

~~~text
declared class:
  A={u0,u1,u2}

outputs on A:
  0,1,2

source cost:
  9

reduced package cost:
  3

outside A:
  v0 != v1
  both map to 9
~~~

Expected:

~~~text
Compression:
  NO_COLLISION_ON_TESTED_CLASS
  LOSSLESS_ON_DECLARED_CLASS
  REDUCTION_ESTABLISHED
  COMPRESSION_TASK_ESTABLISHED
  no global promotion

B0:
  B0_NO_COLLISION_ON_DECLARED_CLASS
  B0_LOSSLESS_ON_DECLARED_CLASS
  B0_REDUCTION_ESTABLISHED
  B0_TASK_COMPLETE
  no global promotion
~~~

### Q5 — partial / outside-scope / precedence

Q5A reuses CPR-CH-002 N7.

~~~text
Q1:
  purpose preserved
  strict reduction 6 -> 4
  established

Q2:
  purpose preserved
  strict reduction 4 -> 4
  not established

independent obligations
no higher terminal
~~~

Expected:

~~~text
Compression:
  COMPRESSION_TASK_PARTIAL

B0:
  B0_TASK_PARTIAL
~~~

Q5B reuses CPR-CH-002 N5.

~~~text
stochastic encoder requested
seed absent
probability kernel absent
stochastic interface absent
~~~

Expected:

~~~text
Compression:
  COMPRESSION_TASK_OUT_OF_SCOPE

B0:
  B0_TASK_OUTSIDE_SCOPE
~~~

Q5C reuses CPR-CH-002 N10.

~~~text
Q1 out_of_scope
Q2 conflicting
Q3 unresolved
Q4 blocked

precedence:
  OUT_OF_SCOPE > CONFLICT > UNRESOLVED > BLOCKED >
  COMPLETE/PARTIAL/NOT_ESTABLISHED
~~~

Expected:

~~~text
Compression:
  COMPRESSION_TASK_OUT_OF_SCOPE
  lower states retained

B0:
  B0_TASK_OUTSIDE_SCOPE
  lower states retained
~~~

### Q6 — bounded claim and neighboring-sidecar discipline

Both evaluators receive the same:

~~~text
compressed output
purpose relation
collision consequences
reduction result
declared-class losslessness record
reconstruction record
Tracking / Lineage / Comparison / Classification / Audit /
Aggregation / Transformation / Measurement sidecars
~~~

Neither may infer without an explicit supplied rule:

~~~text
source identity from compressed equality
global injectivity
reconstruction success from compression success
Lineage identity
classification membership
comparison equivalence
audit pass
measurement validity
aggregation validity
transformation validity
external validity
~~~

Expected:

~~~text
claim-relevant bounded outputs:
  match
~~~

## 7. Frozen gain axes

~~~text
G1 typed-status / purpose-relation preservation advantage

G2 representation-accounting / actual-reduction advantage

G3 collision-fiber / safe-versus-destructive consequence advantage

G4 declared-class losslessness / reconstruction-scope advantage

G5 negative / blocked / conflict / scope /
   underdetermination / partial terminal-semantic advantage

G6 bounded-claim / neighboring-sidecar /
   overclaim-prevention advantage
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
  COMPRESSION_METHOD_GAIN_STATUS =
    COMPRESSION_METHOD_GAIN_NO_GAIN

if one or more frozen claim-relevant axes establish a DSD advantage:
  COMPRESSION_METHOD_GAIN_STATUS =
    COMPRESSION_METHOD_GAIN_ESTABLISHED

if one or more axes establish a baseline advantage:
  preserve BASELINE_ADVANTAGE on those axes
  and do not relabel it as DSD gain

otherwise:
  COMPRESSION_METHOD_GAIN_STATUS =
    COMPRESSION_METHOD_GAIN_UNDERDETERMINED
~~~

Terminology, file organization, or use of DSD names is not a gain axis.

## 8. Frozen scoring — 64 checks

### A. Fairness and immutability — 10

~~~text
A1 Compression Protocol commit/blob fixed
A2 B0 operation fixed before execution
A3 output mappings fixed
A4 Q1-Q6 fixed before execution
A5 equal-information rule respected
A6 B0 receives every Compression-visible claim-relevant input
A7 Compression receives no hidden favorable input
A8 no post-hoc gain axis added
A9 no baseline rule changed after result inspection
A10 external application remains no
~~~

### B. Q1 positive lossy compression — 12

~~~text
B1 Compression outputs frozen reduced records
B2 B0 outputs corresponding reduced records
B3 both preserve group/status required distinctions
B4 both establish the same two collision witnesses
B5 both mark both collisions purpose-safe
B6 both preserve NONZERO/ZERO status
B7 both compute source cost=12
B8 both compute reduced package cost=8
B9 both establish strict reduction
B10 both keep losslessness not established
B11 both keep reconstruction not claimed
B12 corresponding task terminals match
~~~

### C. Q2 destructive collision / no reduction — 10

~~~text
C1 both establish Q2A collision witness
C2 both mark Q2A collision purpose-destructive
C3 both establish Q2A reduction
C4 both return Q2A NOT_ESTABLISHED terminal
C5 neither converts destructive loss into BLOCKED
C6 both preserve every Q2B required distinction
C7 both compute Q2B source cost=4
C8 both compute Q2B reduced cost=4
C9 both mark Q2B reduction not established
C10 both return Q2B NOT_ESTABLISHED terminal
~~~

### D. Q3 blocked / conflict / unresolved — 10

~~~text
D1 both treat unavailable required status sidecar as BLOCKED
D2 neither fabricates evaluable destructive loss in Q3A
D3 both identify same-pair incompatible purpose rules in Q3B
D4 both return conflict terminal in Q3B
D5 neither selects one purpose rule post hoc
D6 both retain epsilon_1 and epsilon_2 as admissible in Q3C
D7 both detect differing outcomes
D8 both preserve no-resolver state
D9 both return unresolved/underdetermined terminal
D10 blocked, conflict, and unresolved remain distinct
~~~

### E. Q4 inverse/losslessness boundary — 10

~~~text
E1 both detect Q4A collision
E2 both mark immediate purpose safe
E3 both mark exact inverse/reconstruction not established
E4 both return Q4A NOT_ESTABLISHED terminal
E5 neither infers reconstruction from purpose safety
E6 both find no collision on declared class A in Q4B
E7 both establish class-local losslessness
E8 both establish strict reduction 9 -> 3
E9 both return Q4B established/complete terminal
E10 neither promotes class-local result to global injectivity
~~~

### F. Q5 terminal and precedence semantics — 8

~~~text
F1 both return PARTIAL for mixed independent obligations
F2 neither uses PARTIAL to rescue one atomic failed proposition
F3 both treat unconfigured stochastic encoder as OUT_OF_SCOPE
F4 neither relabels OUT_OF_SCOPE as evaluable false
F5 both apply OUT_OF_SCOPE > CONFLICT > UNRESOLVED > BLOCKED precedence
F6 both retain conflict under winning outside-scope terminal
F7 both retain unresolved under winning outside-scope terminal
F8 both retain blocked under winning outside-scope terminal
~~~

### G. Q6 and gain conclusion — 4

~~~text
G1 both preserve bounded-claim / neighboring-sidecar non-substitution
G2 six gain axes scored only from frozen outputs
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
DIRECT_COMPRESSION_PILOTS_ATTEMPTED:
  3 -> 4

SUCCESSFUL_DIRECT_COMPRESSION_PILOTS:
  3 -> 4

BASELINE_COMPRESSION_CASES:
  0 -> 1
~~~

If all six gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_COMPRESSION_CASES:
  0 -> 1
~~~

Unchanged:

~~~text
POSITIVE_COMPRESSION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_COMPRESSION_CASES:
  1

METHOD_BOUNDARY_COMPRESSION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  9

STRONGEST_REASONABLE_BASELINE_COMPRESSION:
  not established

REPRODUCIBILITY_CASES:
  0

EXTERNAL_COMPRESSION_APPLICATIONS:
  0

INDEPENDENT_COMPRESSION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established
~~~

## 10. Interpretation lock

A fair `NO_GAIN` result means only:

~~~text
no claim-relevant DSD performance advantage over this
competent constructed baseline was established for these
frozen Compression tasks under equal-information access
~~~

It does not mean:

~~~text
Compression protocol failure
Compression method deletion
Compression must merge into Aggregation
Compression must merge into Transformation
Compression must merge into Reconstruction
permanent redundancy
absence of theoretical/organizational value
future gain is impossible
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

After execution, if all frozen outputs match and the result is NO_GAIN, proceed to a strongest-reasonable non-DSD Compression baseline challenge.
