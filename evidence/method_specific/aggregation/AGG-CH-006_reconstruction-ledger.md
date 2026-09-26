# AGG-CH-006 — Deterministic Same-Project Aggregation Reconstruction Ledger

Status: **FROZEN BEFORE FORMAL COMPARISON AGAINST P2**  
Date: **2026-09-27**  
Challenge ID: `AGG-CH-006`  
Method: **Aggregation / DSD 집계론**

## 1. Derivation basis

This ledger was reconstructed from:

```text
P0 Aggregation Protocol v0.1
commit:
  85b4263ad47cd10acd2230add542f381bd5d6a05
blob:
  5ac926aa40594126b42dac99762ff33fe87450f1

P1 AGG-CH-005 strongest-reasonable baseline precommit
commit:
  da2bb2cb33d51f902e0a9a956846a13c0403a46a
blob:
  d384d7f1c7a4fae71ad46ae12e7cbf504a8dc0d4

AGG-CH-006 precommit
commit:
  2c01089445a7c03a9a8d05f2308c066169253616
blob:
  20e9d4f3beb5096e79c8d01fc7ecaa433df18723
```

The AGG-CH-005 result artifact P2 was not used to derive the following ledger.

## 2. R1 reconstructed ledger — versioned rule registry and postprocessing

Frozen task:

```text
TASK_VERSION:
  1

AGG-RULE-v1:
  finite direct sum
  applicable to task version 1

AGG-RULE-v2:
  weighted finite operator
  applicable only to task version 2

POST-v1:
  downstream equal-weight average

T(c1)=(2,1)
T(c2)=(-1,3)
T(c0)=(0,0)
```

Reconstructed Aggregation output:

```text
PRIMARY_RULE:
  AGG-RULE-v1

PRIMARY_AGGREGATE:
  (1,4)

AGG_RULE_V2_RETROACTIVE_SUBSTITUTION:
  no

POSTPROCESSING_RULE:
  POST-v1

POSTPROCESSING_RESULT:
  (1/3,4/3)

PRIMARY_RESULT_REPLACED_BY_POSTPROCESSING:
  no

RULE_VERSION_PROVENANCE:
  retained

DIRECT_FINITE_SUM_SEMANTICS:
  retained
```

Maximum R1 claim:

```text
For task version 1, the frozen direct finite-sum rule yields
(1,4), while the separately declared equal-weight postprocessing
yields (1/3,4/3); the two operations remain distinct.
```

## 3. R2 reconstructed ledger — kernel and declared-class injectivity

Frozen operator:

```text
S(x,y,z):
  (x+z,y+z)
```

Kernel equations:

```text
x+z=0
y+z=0
```

Hence:

```text
x=-z
y=-z

ker(S):
  {(-t,-t,t): t in R}
  =
  span{(-1,-1,1)}
```

Reconstructed global status:

```text
NONTRIVIAL_KERNEL:
  yes

GLOBAL_INJECTIVITY:
  not established
```

Frozen declared class:

```text
A:
  {(x,y,0): x,y in R}
```

Restricted operator:

```text
S|_A(x,y,0):
  (x,y)
```

Reconstructed declared-class status:

```text
INJECTIVITY_ON_DECLARED_CLASS:
  established
```

Outside-A collision witness:

```text
u:
  (0,0,0)

v:
  (-1,-1,1)

u != v

S(u):
  (0,0)

S(v):
  (0,0)
```

Preserved:

```text
DECLARED_CLASS_INJECTIVITY_TO_GLOBAL_PROMOTION:
  no

COLLISION_INJECTIVITY_SCOPE_PROVENANCE:
  retained
```

Maximum R2 claim:

```text
S is injective on the frozen class A, while the nontrivial
global kernel and explicit outside-A collision prohibit a
global injectivity claim.
```

## 4. R3 reconstructed ledger — admitted countable extension

Frozen terms:

```text
T_n:
  (2^-n,2^-(n+1))
  for n >= 1
```

Absolute-norm majorant:

```text
||T_n||_1:
  2^-n + 2^-(n+1)
  =
  3 * 2^-(n+1)
```

Majorant sum:

```text
sum_{n>=1} 3 * 2^-(n+1)
  =
  3/2
```

Thus:

```text
ABSOLUTE_SUMMABILITY:
  established

COUNTABLE_DOMAIN:
  admitted
```

Component sums:

```text
sum_{n>=1} 2^-n:
  1

sum_{n>=1} 2^-(n+1):
  1/2
```

Reconstructed output:

```text
COUNTABLE_AGGREGATE:
  (1,1/2)

FINITE_CORE_RELABEL:
  no

COUNTABLE_SUPPORT_IDENTITY:
  retained

CONVERGENCE_PROVENANCE:
  retained
```

Maximum R3 claim:

```text
The frozen countable family satisfies the supplied absolute-
summability admission rule and has aggregate (1,1/2);
this remains an admitted countable extension, not the finite core.
```

## 5. R4 reconstructed ledger — multi-coordinate inverse dependency closure

Frozen forward coordinates:

```text
Y1:
  channel aggregate
  established

Y2:
  property aggregate
  established
```

Frozen dependencies:

```text
D1 channel support sidecar:
  available

D2 property support sidecar:
  available

D3 cross-coordinate coupling rule:
  requires XC-v3

XC-v3:
  unavailable
```

Reconstructed:

```text
Y1_STATUS:
  AGGREGATION_ESTABLISHED

Y2_STATUS:
  AGGREGATION_ESTABLISHED

D1_AVAILABILITY:
  available

D2_AVAILABILITY:
  available

D3_AVAILABILITY:
  unavailable

RECONSTRUCTION_SCOPE:
  RECONSTRUCTION_COMBINED_COORDINATE

COMBINED_COORDINATE_INVERSE_CLAIM:
  AGGREGATION_BLOCKED

EVALUABLE_NEGATIVE_RECONSTRUCTION_INFERRED:
  no

COORDINATEWISE_EVIDENCE_PROMOTED_TO_COMBINED_RECONSTRUCTION:
  no
```

Maximum R4 claim:

```text
The forward coordinates remain established, but the combined
inverse claim is blocked by the unavailable frozen cross-coordinate
coupling prerequisite XC-v3.
```

## 6. R5 reconstructed ledger — conflict / underdetermination / sidecars / rerun

### Q1

Frozen registry conflict:

```text
MAP-v7:
  direct sum

MAP-v7:
  normalized mean

same version identity:
  yes

precedence resolver:
  none
```

Reconstructed:

```text
Q1_PRIMARY_STATUS:
  AGGREGATION_CONFLICTING

POST_HOC_MAP_SELECTION:
  no
```

### Q2

Frozen alternative classes:

```text
class schema A:
  injective

class schema B:
  non-injective

resolver:
  none
```

Reconstructed:

```text
Q2_INJECTIVITY_STATUS:
  INJECTIVITY_UNDERDETERMINED

Q2_PRIMARY_STATUS:
  AGGREGATION_UNDERDETERMINED
```

### Q3

Frozen state:

```text
forward aggregation rule:
  supplied and applicable

sidecars:
  Tracking provenance
  Lineage identity
  Comparison similarity
  Classification class
  Reconstruction candidate
  Audit conformance
```

Reconstructed:

```text
Q3_FORWARD_AGGREGATE_STATUS:
  AGGREGATION_ESTABLISHED

Q3_ESTABLISHMENT_BASIS:
  supplied aggregation rule

NEIGHBORING_SIDECARS_PROMOTED_TO_AGGREGATION_CRITERIA:
  no

NEIGHBORING_SIDECARS_PROMOTED_TO_SOURCE_IDENTITY:
  no
```

Frozen terminal precedence:

```text
OUT_OF_SCOPE
>
CONFLICTING
>
UNDERDETERMINED
>
BLOCKED
>
ESTABLISHED / PARTIAL / NOT_ESTABLISHED
```

Reconstructed run terminal:

```text
AGGREGATION_TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_CONFLICTING

LOWER_LEVEL_Q2_STATUS_RETAINED:
  yes

LOWER_LEVEL_Q3_STATUS_RETAINED:
  yes
```

Deterministic metadata:

```text
CLAIM_RELEVANT_LEDGER:
  emitted

RERUN_IDENTIFIERS:
  task/version/operator/support/source/provenance IDs retained
```

Maximum R5 claim:

```text
The run is conflicting because the highest-priority present
condition is the same-version aggregation-rule conflict;
the unresolved injectivity class and established forward
aggregation remain visible as lower-level states.
```

## 7. Protocol-level reconstructed state

```text
AGGREGATION_PROTOCOL_CONFORMANCE:
  AGGREGATION_PROTOCOL_CONFORMANT

PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 8. Reconstructed baseline/gain metadata

This retrace reconstructs the Aggregation-side task outputs only.

It does not re-execute B1 and therefore does not independently regenerate the comparative NO_GAIN judgment.

```text
BASELINE_REEXECUTED:
  no

BASELINE_COUNTER_INCREMENT:
  no

NO_GAIN_COUNTER_INCREMENT:
  no
```

## 9. Retrace ledger freeze

```text
DERIVATION_BASIS:
  P0 + P1

P2_USED_AS_DERIVATION_SOURCE:
  no

LEDGER_STATUS:
  FROZEN_BEFORE_FORMAL_P2_COMPARISON

POST_COMPARISON_CORRECTION_ALLOWED:
  no
```
