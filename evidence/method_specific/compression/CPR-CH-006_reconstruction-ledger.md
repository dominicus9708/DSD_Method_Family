# CPR-CH-006 — Deterministic Same-Project Compression Reconstruction Ledger

Status: **FROZEN BEFORE FORMAL COMPARISON AGAINST P2**  
Date: **2026-09-29**  
Challenge ID: `CPR-CH-006`  
Method: **Compression / DSD 압축론**

## 1. Derivation basis

This ledger was reconstructed from:

~~~text
P0 Compression Protocol v0.1
commit:
  b1efa06e4c715e08ce2558a608c7f09aa22172bd
blob:
  4d67d800e107229f91c16cf5b0235928124482b2

P1 CPR-CH-005 strongest-reasonable baseline precommit
commit:
  f55ec8c5818e75184ef941d72467fec9951abc0d
blob:
  2c9d7f02ab43a0f37b9765c669b2c26f9d919e1a

CPR-CH-006 precommit
commit:
  cb7b6b1f945d34a184aff94dae5c6af6124f62c0
blob:
  556df56b7f50f3694c1558d538482924d36b689c
~~~

The CPR-CH-005 result artifact P2 was not used to derive the following ledger.

## 2. R1 reconstructed ledger — versioned purpose/map registry

Frozen task:

~~~text
TASK_VERSION:
  v1

PURPOSE-v1:
  preserve group + status
  detail may merge

PURPOSE-v2:
  preserve group + status + detail
  TASK-v2 only

MAP-v1:
  C(group,detail,status)=(group,status)
  TASK-v1

MAP-v2:
  identity map
  TASK-v2 only
~~~

Frozen source:

~~~text
x1=(A,a1,NONZERO)
x2=(A,a2,NONZERO)
x3=(B,b1,ZERO)
x4=(B,b2,ZERO)
~~~

Reconstructed map output:

~~~text
x1 -> (A,NONZERO)
x2 -> (A,NONZERO)
x3 -> (B,ZERO)
x4 -> (B,ZERO)
~~~

Reconstructed fibers:

~~~text
F1:
  {x1,x2}

F2:
  {x3,x4}
~~~

Under PURPOSE-v1:

~~~text
F1:
  COLLISION_PURPOSE_SAFE

F2:
  COLLISION_PURPOSE_SAFE
~~~

Accounting:

~~~text
SOURCE_COST:
  12 FIELD_UNIT_COUNT-v1

REDUCED_PACKAGE_COST:
  8 FIELD_UNIT_COUNT-v1

REDUCTION_STATUS:
  REDUCTION_ESTABLISHED
~~~

Version discipline:

~~~text
PURPOSE_V2_RETROACTIVE_SUBSTITUTION:
  no

MAP_V2_RETROACTIVE_SUBSTITUTION:
  no

RULE_VERSION_PROVENANCE:
  retained
~~~

Task status:

~~~text
PRIMARY_TASK_STATUS:
  COMPRESSION_ESTABLISHED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_ESTABLISHED
~~~

Maximum R1 claim:

~~~text
For TASK-v1, PURPOSE-v1 and MAP-v1 establish purpose-safe
lossy compression on the frozen source with strict reduction
from 12 to 8 field units; TASK-v2 semantics are not applied
retroactively.
~~~

## 3. R2 reconstructed ledger — exact kernel and declared-class losslessness

Frozen map:

~~~text
C(x,y,z):
  (x+z,y+z)
~~~

Kernel equations:

~~~text
x+z=0
y+z=0
~~~

Hence:

~~~text
x=-z
y=-z

ker(C):
  {(-t,-t,t): t in R}
  =
  span{(-1,-1,1)}
~~~

Reconstructed global status:

~~~text
NONTRIVIAL_KERNEL:
  yes

GLOBAL_INJECTIVITY:
  not established
~~~

Frozen declared class:

~~~text
A:
  {(x,y,0): x,y in R}
~~~

Restriction:

~~~text
C|_A(x,y,0):
  (x,y)
~~~

Therefore:

~~~text
LOSSLESS_ON_DECLARED_CLASS:
  established
~~~

Outside-A collision witness:

~~~text
u:
  (0,0,0)

v:
  (-1,-1,1)

u != v

C(u):
  (0,0)

C(v):
  (0,0)
~~~

Accounting:

~~~text
SOURCE_FIELDS_PER_RECORD:
  3

REDUCED_FIELDS_PER_RECORD:
  2

REDUCTION_STATUS:
  REDUCTION_ESTABLISHED
~~~

Preserved:

~~~text
DECLARED_CLASS_TO_GLOBAL_PROMOTION:
  no

LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
~~~

Maximum R2 claim:

~~~text
The frozen linear map is lossless on declared class A and
strictly reduces 3 fields to 2 there, while the nontrivial
global kernel and explicit outside-A collision prohibit a
global injectivity claim.
~~~

## 4. R3 reconstructed ledger — required-sidecar dependency and package accounting

Frozen package:

~~~text
SOURCE_RECORDS:
  4

SOURCE_FIELDS_PER_RECORD:
  3

SOURCE_COST:
  12 PACKAGE_FIELD_UNIT-v1
~~~

Main compressed output:

~~~text
MAIN_OUTPUT_RECORDS:
  4

MAIN_OUTPUT_FIELDS_PER_RECORD:
  1

MAIN_OUTPUT_COST:
  4
~~~

Required sidecar:

~~~text
REQUIRED_SIDECAR_STATUS:
  available

REQUIRED_SIDECAR_RECORDS:
  4

REQUIRED_SIDECAR_FIELDS_PER_RECORD:
  2

REQUIRED_SIDECAR_COST:
  8
~~~

Frozen accounting scope:

~~~text
REPRESENTATION_ACCOUNTING_SCOPE:
  output_plus_required_sidecars
~~~

Thus:

~~~text
REDUCED_PACKAGE_COST:
  4 + 8
  =
  12
~~~

Reconstructed statuses:

~~~text
MAIN_OUTPUT_SHRINKAGE:
  yes

STRICT_TOTAL_PACKAGE_REDUCTION:
  not established

REDUCTION_STATUS:
  REDUCTION_NOT_ESTABLISHED

PRIMARY_TASK_STATUS:
  COMPRESSION_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_NOT_ESTABLISHED

REQUIRED_SIDECAR_OMITTED:
  no
~~~

Preserved:

~~~text
MAIN_OUTPUT_SHRINKAGE != TOTAL_REPRESENTATION_REDUCTION
~~~

Maximum R3 claim:

~~~text
The main output shrinks from 12 source field units to 4 main-output
field units, but the frozen required sidecar adds 8 units, leaving
the total package cost at 12; strict Compression is therefore not
established under the frozen accounting scope.
~~~

## 5. R4 reconstructed ledger — end-to-end chain validation

Frozen source:

~~~text
x1=(A,a,0)
x2=(A,b,1)
x3=(B,c,0)
x4=(B,d,1)
~~~

Original purpose P0:

~~~text
preserve group
preserve status
detail may merge
~~~

Stage 1:

~~~text
C1(group,detail,status):
  (group,status)

cost:
  12 -> 8
~~~

Reconstructed stage-1 status:

~~~text
STAGE_1_LOCAL_RESULT:
  COMPRESSION_ESTABLISHED
~~~

Stage 2:

~~~text
C2(group,status):
  group

local stage-2 purpose:
  preserve group only

cost:
  8 -> 4
~~~

Reconstructed stage-2 status:

~~~text
STAGE_2_LOCAL_RESULT:
  COMPRESSION_ESTABLISHED
~~~

Full chain:

~~~text
C2 o C1:
  (group,detail,status)
  ->
  group
~~~

Original P0 remains authoritative for the end-to-end claim.

Collision reconstruction:

~~~text
x1 and x2:
  P0 required-distinct by status
  full-chain outputs both A
  destructive under original P0

x3 and x4:
  P0 required-distinct by status
  full-chain outputs both B
  destructive under original P0
~~~

End-to-end status:

~~~text
END_TO_END_ORIGINAL_PURPOSE:
  not established

COMPOSITION_STATUS:
  COMPOSITION_END_TO_END_NOT_ESTABLISHED

LOCAL_STAGE_RESULTS_RETAINED:
  yes
~~~

Preserved:

~~~text
LOCAL_STAGE_PASS != END_TO_END_COMPRESSION_PASS
~~~

Maximum R4 claim:

~~~text
Both local stages satisfy their local contracts, but the composed
chain destroys the original P0 status distinction, so end-to-end
Compression under P0 is not established.
~~~

## 6. R5 reconstructed ledger — conflict / alternative metric / sidecars / rerun

### Q1 — purpose conflict

Frozen same-version records:

~~~text
PURPOSE-RULE-v7 record A:
  (p,q) required-distinct

PURPOSE-RULE-v7 record B:
  (p,q) safe-to-merge

resolver:
  none
~~~

Reconstructed:

~~~text
Q1_PURPOSE_RELATION_STATUS:
  PURPOSE_RELATION_CONFLICTING

Q1_PRIMARY_STATUS:
  COMPRESSION_CONFLICTING

POST_HOC_RULE_SELECTION:
  no
~~~

### Q2 — alternative accounting metrics

Frozen:

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

Reconstructed:

~~~text
Q2_REDUCTION_STATUS:
  REDUCTION_UNDERDETERMINED

Q2_PRIMARY_STATUS:
  COMPRESSION_UNDERDETERMINED

POST_HOC_METRIC_SELECTION:
  no
~~~

### Q3 — neighboring sidecars

Frozen sidecars:

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

Reconstructed:

~~~text
Q3_FORWARD_COMPRESSION_STATUS:
  COMPRESSION_ESTABLISHED

Q3_ESTABLISHMENT_BASIS:
  frozen Compression contract

NEIGHBORING_SIDECARS_PROMOTED_TO_COMPRESSION_CRITERIA:
  no
~~~

Frozen terminal precedence:

~~~text
OUT_OF_SCOPE
>
CONFLICTING
>
UNDERDETERMINED
>
BLOCKED
>
ESTABLISHED / PARTIAL / NOT_ESTABLISHED
~~~

Reconstructed run terminal:

~~~text
TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_CONFLICTING

LOWER_LEVEL_Q2_STATUS_RETAINED:
  yes

LOWER_LEVEL_Q3_STATUS_RETAINED:
  yes
~~~

Deterministic metadata:

~~~text
CLAIM_RELEVANT_LEDGER:
  emitted

RERUN_IDENTIFIERS:
  task/version/purpose/map/metric/sidecar/collision/chain IDs retained
~~~

Maximum R5 claim:

~~~text
The run terminal is conflicting because the highest-priority present
claim-relevant state is the same-version purpose-rule conflict;
alternative-metric underdetermination and the established forward
Compression result remain visible as lower-level states.
~~~

## 7. Protocol-level reconstructed state

~~~text
COMPRESSION_PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT

PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 8. Reconstructed baseline/gain metadata

This retrace reconstructs the Compression-side task outputs only.

It does not re-execute B1 and therefore does not independently regenerate the comparative NO_GAIN judgment.

~~~text
BASELINE_REEXECUTED:
  no

BASELINE_COUNTER_INCREMENT:
  no

NO_GAIN_COUNTER_INCREMENT:
  no
~~~

## 9. Retrace ledger freeze

~~~text
DERIVATION_BASIS:
  P0 + P1

P2_USED_AS_DERIVATION_SOURCE:
  no

LEDGER_STATUS:
  FROZEN_BEFORE_FORMAL_P2_COMPARISON

POST_COMPARISON_CORRECTION_ALLOWED:
  no
~~~
