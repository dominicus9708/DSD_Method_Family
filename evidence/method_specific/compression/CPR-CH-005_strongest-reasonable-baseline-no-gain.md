# CPR-CH-005 — Strongest-Reasonable Non-DSD Compression Baseline Result

Status: **EXECUTED — 82/82 PASS / NO_GAIN**  
Date: **2026-09-29**  
Challenge ID: `CPR-CH-005`  
Method: **Compression / DSD 압축론**  
Protocol: **Compression Protocol v0.1**  
Baseline: **B1_STRONG_COMPRESSION_ENGINE**

## 1. Frozen references

~~~text
COMPRESSION_PROTOCOL_COMMIT:
  b1efa06e4c715e08ce2558a608c7f09aa22172bd

COMPRESSION_PROTOCOL_BLOB:
  4d67d800e107229f91c16cf5b0235928124482b2

PRECOMMIT_COMMIT:
  f55ec8c5818e75184ef941d72467fec9951abc0d

PRECOMMIT_BLOB:
  2c9d7f02ab43a0f37b9765c669b2c26f9d919e1a
~~~

No Compression Protocol rule, B1 capability, subcase, gain axis, scoring item, or pass threshold was changed after precommit.

## 2. Final result

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0

EQUAL_INFORMATION_ACCESS:
  yes

COMPRESSION_HIDDEN_ADVANTAGE_INPUTS:
  0

BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS:
  0

BASELINE_WEAKENED_AFTER_PRECOMMIT:
  no

COMPRESSION_METHOD_GAIN_STATUS:
  COMPRESSION_METHOD_GAIN_NO_GAIN

STRONGEST_REASONABLE_BASELINE_COMPRESSION:
  established_at_constructed_evidence_level

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The materially stronger non-DSD B1 engine matched every claim-relevant Compression result on the frozen strong workload.

The strongest-reasonable label is bounded to this constructed comparator class and workload.

## 3. Equal-information verification

Compression and B1 received the same:

~~~text
task/version identities
source object classes and schemas
typed status/support/provenance records

purpose-registry versions
must-distinguish / safe-to-merge relations
purpose composition semantics

compression-map versions and definitions
output schemas

resolution / metric / sidecar records
source and reduced cost inputs
reduction requirements

linear maps and declared classes
collision/fiber evidence or sufficient data to derive it
losslessness requests

reconstruction scope and prerequisites
multi-stage chain definitions
original source-level purposes

alternative metrics/schemas
conflict records
terminal precedence

neighboring-method sidecars
maximum-supported claims
~~~

Result:

~~~text
FAIRNESS_CHECK:
  PASS
~~~

B1 used greater ordinary automation and algebraic competence than B0.

It received no hidden claim-relevant fact unavailable to Compression.

## 4. R1 — versioned purpose/map registry and non-retroactivity

Frozen TASK-v1 uses:

~~~text
PURPOSE-v1:
  preserve group + status
  detail may merge

MAP-v1:
  C(group,detail,status)=(group,status)
~~~

Source:

~~~text
x1=(A,a1,NONZERO)
x2=(A,a2,NONZERO)
x3=(B,b1,ZERO)
x4=(B,b2,ZERO)
~~~

Both systems produce:

~~~text
x1 -> (A,NONZERO)
x2 -> (A,NONZERO)
x3 -> (B,ZERO)
x4 -> (B,ZERO)
~~~

Collision fibers:

~~~text
{x1,x2}
{x3,x4}
~~~

Both are purpose-safe under PURPOSE-v1.

Accounting:

~~~text
source cost:
  12

reduced cost:
  8

strict reduction:
  established
~~~

Version discipline:

~~~text
PURPOSE-v2 retroactive substitution:
  prohibited

MAP-v2 retroactive substitution:
  prohibited

rule/version provenance:
  retained
~~~

Result:

~~~text
Compression:
  COMPRESSION_TASK_ESTABLISHED

B1:
  corresponding strong-baseline task complete

CLAIM_RELEVANT_MATCH:
  yes
~~~

## 5. R2 — exact linear fiber/kernel and declared-class losslessness

Frozen map:

~~~text
C(x,y,z):
  (x+z, y+z)
~~~

Kernel equation:

~~~text
x+z=0
y+z=0

therefore:
  x=-z
  y=-z

ker(C):
  {(-t,-t,t): t in R}
  =
  span{(-1,-1,1)}
~~~

Both systems therefore preserve:

~~~text
GLOBAL_INJECTIVITY:
  not established
~~~

Declared class:

~~~text
A={(x,y,0): x,y in R}
~~~

Restriction:

~~~text
C|_A(x,y,0):
  (x,y)
~~~

Hence:

~~~text
LOSSLESS_ON_DECLARED_CLASS:
  established
~~~

Outside-A collision witness:

~~~text
u=(0,0,0)
v=(-1,-1,1)

u != v

C(u):
  (0,0)

C(v):
  (0,0)
~~~

Accounting:

~~~text
source fields per record:
  3

reduced fields per record:
  2

strict reduction:
  established
~~~

Both systems retain:

~~~text
LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
~~~

Claim-relevant result:

~~~text
MATCH
~~~

## 6. R3 — required-sidecar dependency closure and total package accounting

Frozen source package:

~~~text
4 records
x 3 fields
=
12 PACKAGE_FIELD_UNIT-v1
~~~

Main reduced output:

~~~text
4 records
x 1 field
=
4 units
~~~

Required sidecar:

~~~text
4 records
x 2 fields
=
8 units
~~~

Dependency closure:

~~~text
required sidecar:
  available

required sidecar:
  included in frozen accounting scope
~~~

Total reduced package:

~~~text
4 + 8 = 12
~~~

Both systems produce:

~~~text
MAIN_OUTPUT_SHRINKAGE:
  yes

TOTAL_PACKAGE_STRICT_REDUCTION:
  no

REDUCTION_STATUS:
  not established

TASK_TERMINAL:
  not established
~~~

Neither system discards the required sidecar to manufacture a compression success.

Preserved:

~~~text
MAIN_OUTPUT_SHRINKAGE != TOTAL_REPRESENTATION_REDUCTION
~~~

Claim-relevant result:

~~~text
MATCH
~~~

## 7. R4 — local-stage success versus end-to-end chain failure

Frozen source:

~~~text
x1=(A,a,0)
x2=(A,b,1)
x3=(B,c,0)
x4=(B,d,1)
~~~

Original purpose P0 requires:

~~~text
group
status
~~~

Stage 1:

~~~text
C1(group,detail,status)
  =
(group,status)

cost:
  12 -> 8

local result:
  established
~~~

Stage 2:

~~~text
C2(group,status)
  =
group

local purpose P2:
  preserve group only

cost:
  8 -> 4

local result:
  established
~~~

Full chain:

~~~text
C2 o C1:
  (group,detail,status)
  ->
  group
~~~

End-to-end collision witnesses relative to original P0:

~~~text
x1 != x2
P0 requires status distinction
(C2 o C1)(x1)=A
(C2 o C1)(x2)=A

x3 != x4
P0 requires status distinction
(C2 o C1)(x3)=B
(C2 o C1)(x4)=B
~~~

Both systems conclude:

~~~text
STAGE_1_LOCAL:
  established

STAGE_2_LOCAL:
  established

END_TO_END_ORIGINAL_PURPOSE:
  not established

COMPOSITION_END_TO_END:
  not established
~~~

Local-stage results remain recorded.

Preserved:

~~~text
LOCAL_STAGE_PASS != END_TO_END_COMPRESSION_PASS
~~~

Claim-relevant result:

~~~text
MATCH
~~~

## 8. R5 — alternative metric / conflict / sidecar / rerun pressure

### Q1 — purpose conflict

Frozen same-version rules:

~~~text
record A:
  (p,q) required-distinct

record B:
  (p,q) safe-to-merge

resolver:
  none
~~~

Compression:

~~~text
PURPOSE_RELATION_CONFLICTING
~~~

B1:

~~~text
purpose-rule conflict
~~~

### Q2 — alternative accounting metrics

~~~text
METRIC-A:
  source=10
  reduced=8
  strict reduction passes

METRIC-B:
  source=10
  reduced=10
  strict reduction fails

both admissible
resolver:
  none
~~~

Compression:

~~~text
metric/reduction semantics:
  underdetermined
~~~

B1:

~~~text
alternative-metric outcome:
  unresolved
~~~

Neither chooses the favorable metric post hoc.

### Q3 — neighboring sidecars

Both receive:

~~~text
Aggregation
Transformation
Measurement
Comparison
Classification
Tracking
Lineage
Reconstruction
Audit
~~~

sidecars.

The forward Compression result remains determined only by the frozen Compression contract.

No sidecar becomes a Compression criterion merely by being present.

### Terminal and replay state

Frozen precedence yields:

~~~text
run terminal:
  conflict
~~~

Both systems retain:

~~~text
Q2 unresolved/underdetermined
Q3 established forward result
~~~

Both emit/retain claim-relevant deterministic evaluation identifiers.

B1 additionally emits its full generic rerun manifest as precommitted.

Claim-relevant result:

~~~text
MATCH
~~~

## 9. Gain-axis execution

### G1 — versioned purpose/map and nonretroactivity

Compression:

~~~text
correct task-bound purpose/map versions
no retroactive substitution
version provenance retained
~~~

B1:

~~~text
same
~~~

Axis result:

~~~text
BASELINE_MATCH
~~~

### G2 — exact fiber/kernel and declared class

Compression:

~~~text
exact kernel derived
declared-class losslessness established
outside-class collision retained
no global promotion
~~~

B1:

~~~text
same
~~~

Axis result:

~~~text
BASELINE_MATCH
~~~

### G3 — package accounting and sidecar dependency

Compression:

~~~text
required-sidecar closure preserved
main shrinkage distinguished from package reduction
12 -> 12 strict reduction rejected
~~~

B1:

~~~text
same
~~~

Axis result:

~~~text
BASELINE_MATCH
~~~

### G4 — end-to-end chain and purpose propagation

Compression:

~~~text
both local stages retained as established
original P0 propagated through full chain
end-to-end failure detected
~~~

B1:

~~~text
same
~~~

Axis result:

~~~text
BASELINE_MATCH
~~~

### G5 — conflict / underdetermination / sidecar boundary

Compression:

~~~text
purpose conflict preserved
alternative metric underdetermination preserved
neighbor sidecars non-authoritative
terminal precedence retained
~~~

B1:

~~~text
same
~~~

Axis result:

~~~text
BASELINE_MATCH
~~~

### G6 — bounded maximum claim

Compression:

~~~text
no universal purpose safety
no global injectivity
no reconstruction promotion
no external-validity promotion
~~~

B1:

~~~text
same
~~~

Axis result:

~~~text
BASELINE_MATCH
~~~

### G7 — deterministic ledger and rerun manifest

Compression:

~~~text
claim-relevant task/rule/map/metric/sidecar/chain identifiers retained
~~~

B1:

~~~text
deterministic evaluation ledger emitted
full rerun manifest emitted
~~~

No claim-relevant difference favorable to DSD is established.

Axis result:

~~~text
BASELINE_MATCH
~~~

Overall:

~~~text
G1: BASELINE_MATCH
G2: BASELINE_MATCH
G3: BASELINE_MATCH
G4: BASELINE_MATCH
G5: BASELINE_MATCH
G6: BASELINE_MATCH
G7: BASELINE_MATCH

COMPRESSION_METHOD_GAIN_STATUS:
  COMPRESSION_METHOD_GAIN_NO_GAIN
~~~

## 10. Execution of the 82 frozen checks

### A. Immutable fairness

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

A: 10/10
~~~

### B. R1 versioned purpose/map registry

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
B11 PASS
B12 PASS

B: 12/12
~~~

### C. R2 exact kernel / declared class

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

### D. R3 package accounting / sidecar dependency

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
D11 PASS
D12 PASS

D: 12/12
~~~

### E. R4 end-to-end chain validation

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
E11 PASS
E12 PASS

E: 12/12
~~~

### F. R5 integrated conflict / unresolved / sidecar pressure

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
F11 PASS
F12 PASS
F13 PASS
F14 PASS

F: 14/14
~~~

### G. Comparative conclusion

~~~text
G1 PASS
G2 PASS
G3 PASS
G4 PASS
G5 PASS
G6 PASS
G7 PASS
G8 PASS

G: 8/8
~~~

Final:

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0
~~~

## 11. Counter update

~~~text
DIRECT_COMPRESSION_PILOTS_ATTEMPTED:
  5

SUCCESSFUL_DIRECT_COMPRESSION_PILOTS:
  5

POSITIVE_COMPRESSION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_COMPRESSION_CASES:
  1

METHOD_BOUNDARY_COMPRESSION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  9

BASELINE_COMPRESSION_CASES:
  2

NO_GAIN_COMPRESSION_CASES:
  2

STRONGEST_REASONABLE_BASELINE_COMPRESSION:
  established_at_constructed_evidence_level

REPRODUCIBILITY_CASES:
  0

EXTERNAL_COMPRESSION_APPLICATIONS:
  0

INDEPENDENT_COMPRESSION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

COMPRESSION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_COMPRESSION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 12. Interpretation lock

The result means:

~~~text
A materially strong non-DSD compression engine matched the
claim-relevant Compression outputs on this frozen constructed
strong workload under equal-information access.
~~~

It does not mean:

~~~text
B1 is universally strongest possible
Compression protocol failure
Compression method deletion
Compression should merge into another method
Compression should be absorbed
permanent redundancy
future DSD-specific gain is impossible
external validity
independent replication
~~~

Required guards:

~~~text
STRONGEST_REASONABLE_BASELINE_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE

NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

## 13. Maximum-supported claim

Supported:

~~~text
Within the frozen CPR-CH-005 constructed comparator class,
B1_STRONG_COMPRESSION_ENGINE matched Compression Protocol v0.1
on versioned purpose/map semantics, exact linear collision/kernel
analysis, declared-class losslessness, required-sidecar package
accounting, multi-stage end-to-end purpose propagation, conflict /
alternative-metric handling, neighboring-sidecar boundaries,
bounded claims, and deterministic replay metadata.

All seven frozen gain axes were BASELINE_MATCH.
~~~

Not established:

~~~text
universal baseline optimality
method redundancy
external applicability
independent validation
independent replication
method superiority
~~~

## 14. Next

Prospectively precommit and execute CPR-CH-006 deterministic same-project retrace.

The retrace must reconstruct the frozen claim-relevant CPR-CH-001~005 evidence from repository artifacts, compare independently reconstructed outputs against recorded outputs, preserve every mismatch, prohibit post-comparison correction, and keep:

~~~text
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
~~~
