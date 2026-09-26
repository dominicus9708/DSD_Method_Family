# AGG-CH-005 — Strongest-Reasonable Non-DSD Aggregation Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-26**  
Challenge ID: `AGG-CH-005`  
Method: **Aggregation / DSD 집계론**  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen comparator identities

```text
AGGREGATION_PROTOCOL_VERSION:
  v0.1

AGGREGATION_PROTOCOL_COMMIT:
  85b4263ad47cd10acd2230add542f381bd5d6a05

AGGREGATION_PROTOCOL_BLOB:
  5ac926aa40594126b42dac99762ff33fe87450f1

PREVIOUS_COMPETENT_BASELINE:
  AGG-CH-004
  B0_GENERIC_TYPED_AGGREGATION_EVALUATOR
  64/64 PASS / NO_GAIN
```

No Aggregation Protocol revision is allowed in response to this baseline result.

## 2. Strong baseline identity

```text
BASELINE_ID:
  B1_STRONG_AGGREGATION_ENGINE

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_aggregation_engine

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
```

B1 is materially stronger than B0.

B1 may use ordinary:

```text
versioned aggregation-rule registries
typed finite/countable operator families
automatic domain/admission validation
exact rational/vector arithmetic
symbolic or exact collision detection where decidable
kernel/rank analysis on supplied linear maps and algebraic classes
support-aware provenance graphs
multiple coordinate-family registries
explicit postprocessing pipelines
alternative-schema management
dependency-aware inverse-claim prerequisite closure
terminal-precedence engines
deterministic evaluation ledgers
bounded-claim generation
full rerun manifests
```

B1 may not be weakened after precommit.

## 3. Strong baseline operation

B1 performs:

```text
B1-1 freeze task, rule-registry version, source/interface versions,
     selected supports, operator family, output coordinates, and maximum claim

B1-2 bind every aggregation and postprocessing rule to an explicit
     version and applicability domain; prohibit retroactive rule substitution

B1-3 validate typed source status and selected-support membership before
     applying any operator; absent/undefined data are never silently zero-filled

B1-4 evaluate finite operators exactly when the supplied arithmetic is exact

B1-5 validate countable-extension admission against the supplied convergence
     rule before evaluating a countable operator

B1-6 preserve multiple output-coordinate families and their provenance separately

B1-7 retain support/status provenance graphs independently from reduced outputs

B1-8 execute explicit postprocessing pipelines without replacing the primary
     aggregation result

B1-9 when requested and decidable from supplied algebraic data, compute
     collision witnesses, kernel/rank information, and declared-class injectivity

B1-10 freeze reconstruction scope separately from forward aggregation scope

B1-11 compute dependency closure for inverse/cross-coordinate claims;
      unavailable required prerequisites produce blockage rather than a false negative

B1-12 preserve alternative admissible schemas/classes and conflicts without
      post-hoc selection when no resolver is frozen

B1-13 apply frozen terminal precedence while retaining lower-level states

B1-14 keep Comparison / Classification / Tracking / Lineage / Reconstruction /
      Audit sidecars non-authoritative unless an explicit rule promotes them

B1-15 emit bounded claims that prohibit unsupported source identity,
      support identity, global injectivity, lineage identity, audit success,
      or external-validity promotion

B1-16 emit deterministic result ledgers and a rerun manifest containing all
      claim-relevant version/scope/operator/support/provenance identifiers
```

## 4. Equal-information and fairness rule

Aggregation and B1 receive exactly the same claim-relevant records.

```text
EQUAL_INFORMATION_REQUIRED:
  yes

HIDDEN_FAVORABLE_INPUT_ALLOWED:
  no

BASELINE_WEAKENING_ALLOWED:
  no

POST_HOC_RULE_CHANGE_ALLOWED:
  no
```

B1 is not required to derive the DSD ontology.

It receives the same already-frozen source-status and operator semantics that the Aggregation task exposes.

## 5. Strong subcase R1 — versioned rule registry and postprocessing pipeline

Frozen versions:

```text
AGG-RULE-v1:
  valid for task version 1
  finite direct sum on support F

AGG-RULE-v2:
  valid only for task version 2
  weighted finite operator

POST-v1:
  downstream equal-weight average
```

Task version:

```text
TASK_VERSION:
  1

F:
  {c1,c2,c0}

T(c1)=(2,1)
T(c2)=(-1,3)
T(c0)=(0,0)
```

Expected both:

```text
primary rule:
  AGG-RULE-v1

primary result:
  (1,4)

AGG-RULE-v2 retroactive substitution:
  prohibited

POST-v1:
  separately produces (1/3,4/3)

primary result replaced by postprocessing:
  no

rule/version provenance:
  retained
```

## 6. Strong subcase R2 — exact kernel and declared-class injectivity

Frozen linear operator:

```text
S:
  R^3 -> R^2

S(x,y,z):
  (x+z, y+z)
```

Exact matrix:

```text
[1 0 1]
[0 1 1]
```

Expected exact kernel:

```text
ker(S):
  span{(-1,-1,1)}
```

Therefore:

```text
GLOBAL_INJECTIVITY:
  false / not established
```

Frozen admissible class:

```text
A:
  {(x,y,0) : x,y in R}
```

Restricted operator:

```text
S|_A(x,y,0):
  (x,y)
```

Expected:

```text
INJECTIVITY_ON_DECLARED_CLASS:
  established

GLOBAL_INJECTIVITY:
  not established

collision witness outside A:
  (0,0,0)
  and
  (-1,-1,1)
  both map to (0,0)
```

Both systems receive the exact operator and class definition.

## 7. Strong subcase R3 — admitted countable extension with exact sum

Frozen countable terms for n >= 1:

```text
T_n:
  (2^-n, 2^-(n+1))
```

Absolute-norm majorant:

```text
||T_n||_1:
  3 * 2^-(n+1)

sum ||T_n||_1:
  3/2
```

Thus the supplied absolute-summability admission rule passes.

Expected exact componentwise aggregate:

```text
sum_{n>=1} 2^-n:
  1

sum_{n>=1} 2^-(n+1):
  1/2

COUNTABLE_AGGREGATE:
  (1,1/2)
```

Frozen support/provenance rule:

```text
countable support identity:
  retained as countable support sidecar

finite-core substitution:
  prohibited
```

Expected both:

```text
countable domain:
  admitted

aggregate:
  (1,1/2)

finite-core relabel:
  no

absolute-summability evidence:
  retained
```

## 8. Strong subcase R4 — multi-coordinate inverse dependency closure

Frozen forward coordinates:

```text
Y1:
  channel aggregate
  available

Y2:
  property aggregate
  available
```

Frozen inverse claim:

```text
RECONSTRUCTION_SCOPE:
  combined_coordinate
```

Required dependencies:

```text
D1:
  channel support sidecar
  available

D2:
  property support sidecar
  available

D3:
  cross-coordinate coupling rule
  requires schema XC-v3

XC-v3:
  unavailable
```

Expected both:

```text
forward Y1/Y2:
  remain established

dependency closure:
  D3 blocked

combined-coordinate inverse claim:
  BLOCKED

no evaluable negative reconstruction claim inferred
no coordinatewise-injectivity promotion
```

## 9. Strong subcase R5 — integrated alternative schema / conflict / sidecar / rerun pressure

Frozen obligations:

```text
Q1:
  one aggregation-rule registry entry says MAP-v7 = direct sum
  another equally applicable MAP-v7 entry says MAP-v7 = normalized mean
  same version identity
  no precedence

Q2:
  two admissible injectivity classes
  one injective
  one non-injective
  no resolver

Q3:
  forward aggregate established
  Tracking provenance sidecar present
  Lineage identity sidecar present
  high Comparison similarity present
  same Classification class present
  Reconstruction candidate present
  Audit conformance sidecar present
```

Frozen precedence:

```text
OUTSIDE_SCOPE
>
CONFLICT
>
UNRESOLVED
>
BLOCKED
>
COMPLETE/PARTIAL/NOT_ESTABLISHED
```

Expected both:

```text
Q1:
  conflict

Q2:
  unresolved / underdetermined

Q3:
  forward aggregate established only from the supplied aggregation rule;
  neighboring sidecars do not become aggregation or source-identity criteria

run terminal:
  conflict

lower-level Q2 and Q3:
  retained

deterministic ledger:
  emitted

rerun manifest:
  emitted
```

## 10. Frozen gain axes

```text
G1 VERSIONED_RULE_AND_NONRETROACTIVITY_GAIN

G2 EXACT_OPERATOR_KERNEL_AND_DECLARED_CLASS_GAIN

G3 COUNTABLE_ADMISSION_AND_EXACT_EXTENSION_GAIN

G4 MULTICOORDINATE_DEPENDENCY_CLOSURE_GAIN

G5 CONFLICT_UNDERDETERMINATION_AND_SIDECAR_BOUNDARY_GAIN

G6 BOUNDED_MAXIMUM_CLAIM_GAIN

G7 DETERMINISTIC_LEDGER_AND_RERUN_MANIFEST_GAIN
```

Allowed per-axis result:

```text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
```

Overall rule:

```text
if Aggregation is protocol-nonconformant or wrong:
  FAIL

if one or more frozen axes establish a real DSD advantage
against the still-fair B1:
  AGGREGATION_METHOD_GAIN_ESTABLISHED

if all seven axes are BASELINE_MATCH:
  AGGREGATION_METHOD_GAIN_NO_GAIN

if a baseline advantage appears:
  preserve BASELINE_ADVANTAGE
  and do not relabel it as DSD gain

otherwise:
  AGGREGATION_METHOD_GAIN_UNDERDETERMINED
```

## 11. Frozen scoring — 72 checks

### A. Immutable fairness — 10

```text
A1 Aggregation protocol identity frozen
A2 B1 identity and capabilities frozen
A3 R1-R5 frozen before execution
A4 equal-information rule frozen
A5 Aggregation hidden favorable inputs = 0
A6 B1 claim-relevant withheld inputs = 0
A7 B1 not weakened after precommit
A8 output/gain mapping frozen
A9 scoring frozen
A10 external application/evaluator not counted
```

### B. R1 versioned rule registry — 12

```text
B1 Aggregation selects AGG-RULE-v1 for task v1
B2 B1 selects same v1 rule
B3 Aggregation primary result = (1,4)
B4 B1 primary result = (1,4)
B5 Aggregation blocks retroactive v2 substitution
B6 B1 blocks retroactive v2 substitution
B7 Aggregation POST-v1 = (1/3,4/3)
B8 B1 POST-v1 = (1/3,4/3)
B9 Aggregation retains primary/postprocess separation
B10 B1 retains same separation
B11 Aggregation rule/version provenance retained
B12 B1 rule/version provenance retained
```

### C. R2 exact kernel / declared class — 14

```text
C1 Aggregation exact kernel relation recognized
C2 B1 exact kernel relation recognized
C3 Aggregation ker(S)=span{(-1,-1,1)}
C4 B1 same kernel
C5 Aggregation global injectivity not established
C6 B1 global injectivity not established
C7 Aggregation declared class A frozen
C8 B1 declared class A frozen
C9 Aggregation S|_A injective
C10 B1 S|_A injective
C11 Aggregation outside-A collision witness retained
C12 B1 same collision witness retained
C13 neither promotes class-local injectivity globally
C14 claim-relevant outputs match
```

### D. R3 countable admitted extension — 12

```text
D1 Aggregation recognizes absolute-summability evidence
D2 B1 recognizes same evidence
D3 Aggregation countable domain admitted
D4 B1 countable domain admitted
D5 Aggregation first-coordinate sum = 1
D6 B1 first-coordinate sum = 1
D7 Aggregation second-coordinate sum = 1/2
D8 B1 second-coordinate sum = 1/2
D9 Aggregation result = (1,1/2)
D10 B1 result = (1,1/2)
D11 neither relabels countable result as finite core
D12 both retain countable-support/convergence provenance
```

### E. R4 inverse dependency closure — 12

```text
E1 Aggregation Y1 remains established
E2 B1 Y1 remains established
E3 Aggregation Y2 remains established
E4 B1 Y2 remains established
E5 Aggregation D1 available
E6 B1 D1 available
E7 Aggregation D2 available
E8 B1 D2 available
E9 Aggregation XC-v3 unavailable -> inverse BLOCKED
E10 B1 same dependency closure -> inverse BLOCKED
E11 neither infers evaluable negative reconstruction
E12 neither promotes coordinatewise evidence to combined reconstruction
```

### F. R5 integrated conflict / unresolved / sidecar pressure — 14

```text
F1 Aggregation Q1 conflict
F2 B1 Q1 conflict
F3 Aggregation Q2 underdetermined
F4 B1 Q2 unresolved
F5 Aggregation Q3 forward aggregate remains established
F6 B1 Q3 forward aggregate remains established
F7 Aggregation neighboring sidecars not promoted
F8 B1 neighboring sidecars not promoted
F9 Aggregation terminal conflict by frozen precedence
F10 B1 terminal conflict by frozen precedence
F11 lower-level Q2/Q3 retained by Aggregation
F12 lower-level Q2/Q3 retained by B1
F13 Aggregation deterministic ledger + rerun identifiers retained
F14 B1 deterministic ledger + rerun manifest emitted
```

### G. Comparative conclusion — 8

```text
G1 all five strong subcases scored from frozen evidence only
G2 seven gain axes scored from frozen outputs only
G3 terminology differences not counted as gain
G4 baseline extra unused capabilities not counted as an advantage
G5 DSD advantage recorded only if claim-relevant
G6 baseline advantage preserved if claim-relevant
G7 NO_GAIN preserved if all seven axes BASELINE_MATCH
G8 no deletion/merger/absorption/permanent-redundancy conclusion inferred
```

```text
TOTAL_REQUIRED_CHECKS:
  82
```

Correction before commit:

```text
A 10
B 12
C 14
D 12
E 12
F 14
G 8
=
82
```

The frozen challenge therefore uses **82 checks**, not 72.

```text
PASS_THRESHOLD:
  82/82

PARTIAL_PASS_ALLOWED:
  no
```

Any mismatch remains visible.

## 12. Allowed counter changes on 82/82 PASS

```text
DIRECT_AGGREGATION_PILOTS_ATTEMPTED:
  4 -> 5

SUCCESSFUL_DIRECT_AGGREGATION_PILOTS:
  4 -> 5

BASELINE_AGGREGATION_CASES:
  1 -> 2
```

If all seven gain axes are `BASELINE_MATCH`:

```text
NO_GAIN_AGGREGATION_CASES:
  1 -> 2

STRONGEST_REASONABLE_BASELINE_AGGREGATION:
  established_at_constructed_evidence_level
```

Unchanged:

```text
POSITIVE_AGGREGATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_AGGREGATION_CASES:
  1

METHOD_BOUNDARY_AGGREGATION_CASES:
  1

REPRODUCIBILITY_CASES:
  0

EXTERNAL_AGGREGATION_APPLICATIONS:
  0

INDEPENDENT_AGGREGATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established
```

## 13. Interpretation lock

```text
STRONGEST_REASONABLE_BASELINE_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE

NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```

A strongest-reasonable NO_GAIN result would mean only that a materially strong non-DSD aggregation engine matched the claim-relevant outputs on this frozen constructed workload under equal-information access.
