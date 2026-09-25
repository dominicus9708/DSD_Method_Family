# AGG-CH-004 — Competent Non-DSD Aggregation Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-26**  
Challenge ID: `AGG-CH-004`  
Method: **Aggregation / DSD 집계론**  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

```text
AGGREGATION_PROTOCOL_VERSION:
  v0.1

AGGREGATION_PROTOCOL_COMMIT:
  85b4263ad47cd10acd2230add542f381bd5d6a05

AGGREGATION_PROTOCOL_BLOB:
  5ac926aa40594126b42dac99762ff33fe87450f1
```

No Aggregation Protocol revision is allowed in response to this baseline result.

## 2. Baseline identity

```text
BASELINE_ID:
  B0_GENERIC_TYPED_AGGREGATION_EVALUATOR

BASELINE_CLASS:
  competent_non_DSD_constructed_aggregation_evaluator

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
```

B0 is intentionally competent rather than weak.

It may use ordinary:

```text
stable object IDs
typed status flags
finite sets and lists
vector/scalar addition
declared output spaces
explicit source/support ledgers
ordinary convergence tests
explicit postprocessing maps
finite collision tests
declared-class injectivity tests
scope/version locks
required-interface checks
conflict/ambiguity tables
deterministic terminal precedence
bounded-claim reporting
```

It does not invoke Formation, Property, Static Aggregation, Dynamics, or the DSD shared core as theory.

Vocabulary or organizational differences alone do not count as DSD gain.

## 3. B0 generic operation

B0 performs:

```text
B0-1 freeze task ID/version, declared operation, domain, support,
     output type, optional sidecar requirements, and maximum claim

B0-2 retain supplied source IDs, typed status flags, provenance,
     and human-readable labels separately

B0-3 admit only records explicitly marked usable by the supplied
     task interface; do not coerce unavailable/undefined records to zero

B0-4 apply the supplied finite combination operator exactly on
     the supplied selected support

B0-5 when two output coordinates are declared separately,
     retain coordinate identity and provenance separately

B0-6 retain support/status sidecars when the task says they are
     required for interpretation or inverse claims

B0-7 when a countable extension is requested, apply the supplied
     convergence admission rule before evaluating the extension

B0-8 keep any declared postprocessing map separate from the
     primary combination operator

B0-9 when collision testing is requested on a finite declared class,
     compare distinct admissible assignments for equal outputs

B0-10 when injectivity is requested, evaluate only on the supplied
      admissible class and support; never promote class-local success
      to global injectivity

B0-11 when source/support reconstruction is requested, retain its
      declared scope and required interfaces separately from the
      forward readout

B0-12 preserve required-interface absence as BLOCKED rather than
      evaluable negative evidence

B0-13 preserve conflict, outside-scope, unresolved semantics,
      evaluable failure, and multi-obligation partial results separately

B0-14 apply the supplied terminal precedence deterministically

B0-15 retain neighboring-method records only as sidecars unless a
      supplied rule makes them part of the current aggregation task

B0-16 emit only the bounded result justified by the supplied
      operator/domain/status/support/injectivity records
```

## 4. Frozen output mapping

Primary-result mapping:

```text
B0_READOUT_ESTABLISHED
  <-> AGGREGATION_ESTABLISHED

B0_READOUT_NOT_ESTABLISHED
  <-> AGGREGATION_NOT_ESTABLISHED

B0_READOUT_BLOCKED
  <-> AGGREGATION_BLOCKED

B0_READOUT_CONFLICT
  <-> AGGREGATION_CONFLICTING

B0_READOUT_OUTSIDE_SCOPE
  <-> AGGREGATION_OUT_OF_SCOPE

B0_READOUT_UNRESOLVED
  <-> AGGREGATION_UNDERDETERMINED
```

Task-terminal mapping:

```text
B0_TASK_COMPLETE
  <-> AGGREGATION_TASK_ESTABLISHED

B0_TASK_PARTIAL
  <-> AGGREGATION_TASK_PARTIAL

B0_TASK_NOT_ESTABLISHED
  <-> AGGREGATION_TASK_NOT_ESTABLISHED

B0_TASK_BLOCKED
  <-> AGGREGATION_TASK_BLOCKED

B0_TASK_CONFLICT
  <-> AGGREGATION_TASK_CONFLICTING

B0_TASK_OUTSIDE_SCOPE
  <-> AGGREGATION_TASK_OUT_OF_SCOPE

B0_TASK_UNRESOLVED
  <-> AGGREGATION_TASK_UNDERDETERMINED
```

Collision/injectivity mapping:

```text
B0_COLLISION_NOT_TESTED
  <-> COLLISION_NOT_TESTED

B0_COLLISION_WITNESS
  <-> COLLISION_WITNESS_ESTABLISHED

B0_NO_COLLISION_ON_DECLARED_CLASS
  <-> NO_COLLISION_ON_TESTED_CLASS

B0_INJECTIVE_ON_DECLARED_CLASS
  <-> INJECTIVITY_ESTABLISHED_ON_DECLARED_CLASS

B0_NOT_INJECTIVE_ON_DECLARED_CLASS
  <-> INJECTIVITY_NOT_ESTABLISHED

B0_INJECTIVITY_BLOCKED
  <-> INJECTIVITY_BLOCKED

B0_INJECTIVITY_UNRESOLVED
  <-> INJECTIVITY_UNDERDETERMINED
```

## 5. Equal-information rule

For every fixture, Aggregation and B0 receive the same claim-relevant:

```text
task ID/version
primary claim level
maximum-supported claim

source/interface IDs
selected supports
source object identities
typed status flags
provenance

aggregation domain class
aggregation operator
output space/type

coordinate declarations
support-retention policy
negative-status sidecar policy

countable-extension request
convergence admission rule and relevant term data

postprocessing request and map

collision-test request
injectivity support/operator/admissible class
reconstruction-scope declaration
cross-coordinate reconstruction condition

required-interface availability
conflict records
scope records
alternative admissible semantics/classes
terminal precedence
```

Neither side receives hidden favorable information.

The baseline is not asked to derive the DSD source ontology; it is asked to execute the same frozen task once the claim-relevant interface is supplied.

## 6. Frozen fixtures

### Q1 — positive combined finite aggregation

Use the claim-relevant AGG-CH-001 fixture.

Frozen formation-side values:

```text
c1 -> (2,1)
c2 -> (-1,3)
c0 -> (0,0) with explicit defined-zero status
cX -> absent
F = {c1,c2,c0}
```

Frozen property-side values:

```text
i1 -> (4,0)
i2 -> (-1,2), complete typed input (x1,x2)
i0 -> (0,0) with explicit defined-zero status
u1 -> applicable but undefined
G = {i1,i2,i0}
```

Expected Aggregation:

```text
Comp(F) = (1,4)
Agg(G) = (3,2)
combined = ((1,4),(3,2))
separate equal-weight channel postprocessing = (1/3,4/3)
terminal = AGGREGATION_TASK_ESTABLISHED
```

Expected B0:

```text
channel readout = (1,4)
property readout = (3,2)
combined pair = ((1,4),(3,2))
separate declared postprocessing = (1/3,4/3)
terminal = B0_TASK_COMPLETE
```

Both must preserve:

```text
defined zero != absent
defined zero != undefined
multi-input record retains complete typed input
coordinate 1 != coordinate 2
primary combination != postprocessing
```

### Q2 — finite-domain and countable-admission failures

Q2A uses AGG-CH-002 N1:

```text
selected finite support includes one explicitly absent channel
complete register available
```

Expected:

```text
Aggregation:
  domain NOT_ADMITTED
  task NOT_ESTABLISHED

B0:
  input/domain rejected as evaluably not admitted
  task B0_TASK_NOT_ESTABLISHED
```

Q2B uses AGG-CH-002 N2:

```text
T_n = (-1)^(n+1)/n
ordinary conditional convergence
absolute-sum divergence
supplied countable admission rule requires absolute summability
```

Expected:

```text
Aggregation:
  NOT_ESTABLISHED

B0:
  B0_TASK_NOT_ESTABLISHED
```

Neither may accept the countable task merely from conditional convergence.

### Q3 — blocked / conflict / unresolved semantics

Q3A uses AGG-CH-002 N3:

```text
combined-coordinate inverse claim
required support sidecar unavailable
required cross-coordinate condition unavailable
```

Expected:

```text
Aggregation:
  BLOCKED

B0:
  B0_TASK_BLOCKED
```

Q3B uses AGG-CH-002 N4:

```text
same frozen postprocessing ID/version
two applicable incompatible definitions
no precedence
```

Expected:

```text
Aggregation:
  CONFLICTING

B0:
  B0_TASK_CONFLICT
```

Q3C uses AGG-CH-002 N6:

```text
two admissible injectivity classes
one injective
one non-injective
no resolver
```

Expected:

```text
Aggregation:
  UNDERDETERMINED

B0:
  B0_TASK_UNRESOLVED
```

### Q4 — collision and declared-class injectivity

Q4A uses AGG-CH-002 N8:

```text
support F = {a,b}
operator S(u_a,u_b)=u_a+u_b
assignments (1,-1) and (2,-2)
both map to 0
```

Expected:

```text
Aggregation:
  COLLISION_WITNESS_ESTABLISHED
  INJECTIVITY_NOT_ESTABLISHED
  task NOT_ESTABLISHED

B0:
  B0_COLLISION_WITNESS
  B0_NOT_INJECTIVE_ON_DECLARED_CLASS
  B0_TASK_NOT_ESTABLISHED
```

Q4B uses AGG-CH-002 N9:

```text
A_F = {(0,0),(1,0),(2,0)}
outputs = {0,1,2}
```

Expected:

```text
Aggregation:
  NO_COLLISION_ON_TESTED_CLASS
  INJECTIVITY_ESTABLISHED_ON_DECLARED_CLASS
  task ESTABLISHED
  no global promotion

B0:
  B0_NO_COLLISION_ON_DECLARED_CLASS
  B0_INJECTIVE_ON_DECLARED_CLASS
  B0_TASK_COMPLETE
  no global promotion
```

### Q5 — partial / outside-scope / precedence

Q5A uses AGG-CH-002 N7:

```text
one independent formation obligation established
one independent property obligation evaluably not established
no higher terminal
```

Expected:

```text
Aggregation:
  AGGREGATION_TASK_PARTIAL

B0:
  B0_TASK_PARTIAL
```

Q5B uses AGG-CH-002 N5:

```text
uncountable aggregation requested
current supplied interface supports only finite/countable
```

Expected:

```text
Aggregation:
  AGGREGATION_TASK_OUT_OF_SCOPE

B0:
  B0_TASK_OUTSIDE_SCOPE
```

Q5C uses AGG-CH-002 N10:

```text
Q1 conflict
Q2 unresolved admissible semantics
Q3 blocked required interface

precedence:
  OUT_OF_SCOPE > CONFLICT > UNRESOLVED > BLOCKED >
  COMPLETE/PARTIAL/NOT_ESTABLISHED
```

Expected:

```text
Aggregation:
  AGGREGATION_TASK_CONFLICTING
  lower states retained

B0:
  B0_TASK_CONFLICT
  lower states retained
```

### Q6 — bounded-claim and neighboring-sidecar discipline

Both evaluators receive:

```text
same forward aggregate
same support sidecar
same collision result
same declared-class injectivity result
same Tracking / Lineage / Comparison / Classification / Audit sidecars
```

Neither may infer without an explicit rule:

```text
source identity
support identity
global injectivity
Lineage identity
classification membership
comparison equivalence
audit pass
external validity
```

Expected:

```text
claim-relevant bounded outputs:
  match
```

## 7. Frozen gain axes

```text
G1 typed-status and support-preservation advantage

G2 finite/countable domain and convergence-discipline advantage

G3 coordinate-separation and postprocessing-boundary advantage

G4 collision / declared-class injectivity /
   reconstruction-scope advantage

G5 negative / blocked / conflict / scope /
   underdetermination / partial terminal-semantic advantage

G6 bounded-claim / neighboring-sidecar /
   overclaim-prevention advantage
```

Allowed axis result:

```text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
```

Overall gain rule:

```text
if all claim-relevant outputs and all six gain axes match:
  AGGREGATION_METHOD_GAIN_STATUS =
    AGGREGATION_METHOD_GAIN_NO_GAIN

if one or more frozen claim-relevant axes establish a DSD advantage:
  AGGREGATION_METHOD_GAIN_STATUS =
    AGGREGATION_METHOD_GAIN_ESTABLISHED

if one or more axes establish a baseline advantage:
  preserve BASELINE_ADVANTAGE on those axes
  and do not relabel it as DSD gain

otherwise:
  AGGREGATION_METHOD_GAIN_STATUS =
    AGGREGATION_METHOD_GAIN_UNDERDETERMINED
```

Terminology, file organization, or use of DSD names is not a gain axis.

## 8. Frozen scoring — 64 checks

### A. Fairness and immutability — 10

```text
A1 Aggregation Protocol commit/blob fixed
A2 B0 operation fixed before execution
A3 output mappings fixed
A4 Q1-Q6 fixed before execution
A5 equal-information rule respected
A6 B0 receives every Aggregation-visible claim-relevant input
A7 Aggregation receives no hidden favorable input
A8 no post-hoc gain axis added
A9 no baseline rule changed after result inspection
A10 external application remains no
```

### B. Q1 positive combined aggregation — 14

```text
B1 Aggregation channel aggregate = (1,4)
B2 B0 channel readout = (1,4)
B3 Aggregation property aggregate = (3,2)
B4 B0 property readout = (3,2)
B5 Aggregation combined pair = ((1,4),(3,2))
B6 B0 combined pair = ((1,4),(3,2))
B7 both preserve c0 defined-zero vs cX absent
B8 both preserve i0 defined-zero vs u1 undefined
B9 both retain i2 complete multi-input record
B10 neither infers single-channel ownership for i2
B11 both keep coordinate identities distinct
B12 both compute separate postprocessing = (1/3,4/3)
B13 neither substitutes postprocessing for primary aggregate
B14 corresponding task terminals match claim-relevantly
```

### C. Q2 finite/countable admission — 10

```text
C1 Aggregation absent selected channel -> NOT_ADMITTED
C2 B0 rejects same finite-domain input
C3 neither zero-extends absent channel
C4 corresponding Q2A terminals match
C5 Aggregation recognizes conditional convergence
C6 B0 recognizes conditional convergence
C7 Aggregation absolute-sum gate fails
C8 B0 supplied absolute-sum gate fails
C9 neither silently admits the countable extension
C10 corresponding Q2B terminals match
```

### D. Q3 blockage / conflict / unresolved — 10

```text
D1 Aggregation required-interface absence = BLOCKED
D2 B0 required-interface absence = BLOCKED
D3 Aggregation same-ID incompatible map records = CONFLICTING
D4 B0 same records = CONFLICT
D5 neither selects one conflicting map post hoc
D6 Aggregation competing admissible classes = UNDERDETERMINED
D7 B0 same alternatives = UNRESOLVED
D8 neither selects one class post hoc
D9 corresponding task terminals match
D10 unavailable required input remains distinct from evaluable failure
```

### E. Q4 collision / injectivity — 10

```text
E1 Aggregation collision witness found
E2 B0 same collision witness found
E3 Aggregation injectivity NOT_ESTABLISHED on collision class
E4 B0 same class non-injective
E5 corresponding negative terminals match
E6 Aggregation no collision on declared injective class
E7 B0 no collision on same class
E8 Aggregation declared-class injectivity established
E9 B0 declared-class injectivity established
E10 neither promotes declared-class success to global injectivity
```

### F. Q5 terminal and precedence semantics — 6

```text
F1 Aggregation multi-obligation terminal PARTIAL
F2 B0 same task PARTIAL
F3 Aggregation uncountable request OUT_OF_SCOPE
F4 B0 same request OUTSIDE_SCOPE
F5 both apply conflict > unresolved > blocked precedence in Q5C
F6 both retain lower-level states under the winning terminal
```

### G. Q6 and gain conclusion — 4

```text
G1 both preserve bounded-claim / neighboring-sidecar non-substitution
G2 six gain axes scored from frozen outputs only
G3 NO_GAIN preserved if all six axes are BASELINE_MATCH
G4 NO_GAIN does not imply merger/deletion/absorption/permanent redundancy
```

```text
TOTAL_REQUIRED_CHECKS:
  64

PASS_THRESHOLD:
  64/64

PARTIAL_PASS_ALLOWED:
  no
```

Any mismatch must remain visible.

## 9. Allowed counter changes on 64/64 PASS

```text
DIRECT_AGGREGATION_PILOTS_ATTEMPTED:
  3 -> 4

SUCCESSFUL_DIRECT_AGGREGATION_PILOTS:
  3 -> 4

BASELINE_AGGREGATION_CASES:
  0 -> 1
```

If all six gain axes are `BASELINE_MATCH`:

```text
NO_GAIN_AGGREGATION_CASES:
  0 -> 1
```

Unchanged:

```text
POSITIVE_AGGREGATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_AGGREGATION_CASES:
  1

METHOD_BOUNDARY_AGGREGATION_CASES:
  1

STRONGEST_REASONABLE_BASELINE_AGGREGATION:
  not established

REPRODUCIBILITY_CASES:
  0

EXTERNAL_AGGREGATION_APPLICATIONS:
  0

INDEPENDENT_AGGREGATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established
```

## 10. Interpretation lock

A fair `NO_GAIN` result means only:

```text
no claim-relevant DSD performance advantage over this
competent constructed baseline was established for these
frozen tasks under equal-information access
```

It does not mean:

```text
Aggregation protocol failure
Aggregation method deletion
Aggregation must merge into Compression
Aggregation must merge into Reconstruction
permanent redundancy
absence of theoretical/organizational value
future gain is impossible
```

Required guards:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```
