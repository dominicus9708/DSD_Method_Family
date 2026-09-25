# AGG-CH-002 — Negative / Unresolved-Terminal Aggregation Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-26**  
Challenge ID: `AGG-CH-002`  
Method: **Aggregation / DSD 집계론**  
Protocol: **Aggregation Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

```text
PROTOCOL_COMMIT:
  85b4263ad47cd10acd2230add542f381bd5d6a05

PROTOCOL_BLOB:
  5ac926aa40594126b42dac99762ff33fe87450f1

VALIDITY_GATES:
  G1-G16

BINDING_OPERATION:
  T1-T16
```

The frozen protocol may not be modified in response to this challenge.

## 2. Purpose

Directly exercise the negative and unresolved Aggregation task terminals plus collision/injectivity/reconstruction-scope distinctions that AGG-CH-001 intentionally did not claim.

This bundle contains ten independent constructed subcases.

A conformant negative or unresolved result counts as successful protocol execution.

```text
CONFORMANT_NEGATIVE_TERMINAL != METHOD_FAILURE
```

The challenge is internal constructed validation only.

It is not external validation, independent replication, or method-gain evidence.

## 3. Frozen terminal targets

The bundle must directly exercise:

```text
AGGREGATION_TASK_NOT_ESTABLISHED
AGGREGATION_TASK_BLOCKED
AGGREGATION_TASK_CONFLICTING
AGGREGATION_TASK_OUT_OF_SCOPE
AGGREGATION_TASK_UNDERDETERMINED
AGGREGATION_TASK_PARTIAL
```

AGG-CH-001 already directly exercised:

```text
AGGREGATION_TASK_ESTABLISHED
```

If all expected subcases execute, all seven task terminals will have direct constructed execution across AGG-CH-001 and AGG-CH-002.

## 4. N1 — evaluable finite-domain failure from absent channel

Frozen task:

```text
TASK_ID:
  AGG-CH-002-N1

PRIMARY_CLAIM_LEVEL:
  FORMATION_CHANNEL_AGGREGATE

C_L:
  {c1}

F:
  {c1,cX}

T(c1):
  3

cX:
  not in C_L

channel register:
  complete and available
```

The selected support is evaluable and contains a non-admitted channel.

Expected:

```text
cX:
  CHANNEL_ABSENT

T(cX):
  undefined

AGGREGATION_DOMAIN_STATUS:
  AGGREGATION_DOMAIN_NOT_ADMITTED

PRIMARY_TASK_STATUS:
  AGGREGATION_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_NOT_ESTABLISHED
```

Guards:

```text
ABSENT_CHANNEL != DEFINED_ZERO
EVALUABLE_NOT_ADMITTED != BLOCKED
```

## 5. N2 — countable extension fails absolute-summability gate

Frozen task:

```text
TASK_ID:
  AGG-CH-002-N2

PRIMARY_CLAIM_LEVEL:
  COUNTABLE_ANALYTIC_EXTENSION

term space:
  R

countable terms:
  T_n = (-1)^(n+1) / n

requested aggregation:
  sum over n >= 1
```

The scalar series converges conditionally, but:

```text
sum |T_n|
  diverges
```

The frozen protocol/source-defined extension requires the stronger absolute/unconditional condition.

Expected:

```text
ABSOLUTE_SUMMABILITY:
  failed

AGGREGATION_DOMAIN_STATUS:
  AGGREGATION_DOMAIN_NOT_ADMITTED

PRIMARY_TASK_STATUS:
  AGGREGATION_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_NOT_ESTABLISHED
```

Guard:

```text
CONDITIONAL_CONVERGENCE
  !=
SOURCE_DEFINED_COUNTABLE_EXTENSION_ADMISSION
```

## 6. N3 — blocked combined reconstruction claim

Frozen task:

```text
TASK_ID:
  AGG-CH-002-N3

PRIMARY_CLAIM_LEVEL:
  AGGREGATE_INJECTIVITY

RECONSTRUCTION_SCOPE:
  combined_coordinate

channel aggregate:
  available

property aggregate:
  available

required channel support sidecar:
  unavailable

required property support sidecar:
  available

CROSS_COORDINATE_RECONSTRUCTION_CONDITION:
  required_but_unavailable
```

Expected:

```text
INJECTIVITY_STATUS:
  INJECTIVITY_BLOCKED

PRIMARY_TASK_STATUS:
  AGGREGATION_BLOCKED

TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_BLOCKED
```

Guards:

```text
REQUIRED_INTERFACE_UNAVAILABLE != EVALUABLE_FAILURE
BLOCKED != NOT_ESTABLISHED
COORDINATEWISE_DATA != CROSS_COORDINATE_RECONSTRUCTION
```

## 7. N4 — conflicting aggregation/postprocessing map records

Frozen task:

```text
TASK_ID:
  AGG-CH-002-N4

PRIMARY_CLAIM_LEVEL:
  POSTPROCESSED_READOUT

input aggregate:
  y = (2,4)

POSTPROCESSING_ID:
  P-CONFLICT-v1
```

Two applicable records under the same frozen ID/version:

```text
R1:
  P-CONFLICT-v1(y) = y_1 + y_2

R2:
  P-CONFLICT-v1(y) = (y_1 + y_2)/2

precedence resolver:
  none
```

Expected:

```text
candidate outputs:
  6
  3

PRIMARY_TASK_STATUS:
  AGGREGATION_CONFLICTING

TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_CONFLICTING
```

Guard:

```text
CONFLICTING_RECORDS != LICENSE_TO_SELECT_ONE_POST_HOC
```

## 8. N5 — uncountable aggregation request outside current protocol scope

Frozen task:

```text
TASK_ID:
  AGG-CH-002-N5

PRIMARY_CLAIM_LEVEL:
  COUNTABLE_ANALYTIC_EXTENSION

requested index family:
  uncountable

later uncountable aggregation interface:
  not supplied
```

Expected:

```text
AGGREGATION_DOMAIN_STATUS:
  AGGREGATION_DOMAIN_OUT_OF_SCOPE

PRIMARY_TASK_STATUS:
  AGGREGATION_OUT_OF_SCOPE

TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_OUT_OF_SCOPE
```

Guard:

```text
OUT_OF_SCOPE != FALSE
OUT_OF_SCOPE != NOT_ESTABLISHED
```

## 9. N6 — underdetermined injectivity class

Frozen task:

```text
TASK_ID:
  AGG-CH-002-N6

PRIMARY_CLAIM_LEVEL:
  AGGREGATE_INJECTIVITY

fixed support:
  F = {a,b}

aggregation operator:
  S_F(u_a,u_b) = u_a + u_b

two admissible class specifications:
  A_F^(1)
  A_F^(2)

resolver:
  none
```

Frozen classes:

```text
A_F^(1):
  {(0,0),(1,0)}
  S_F is injective on this class

A_F^(2):
  {(1,-1),(2,-2)}
  S_F is not injective on this class
```

Expected:

```text
INJECTIVITY_STATUS:
  INJECTIVITY_UNDERDETERMINED

PRIMARY_TASK_STATUS:
  AGGREGATION_UNDERDETERMINED

TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_UNDERDETERMINED
```

Guard:

```text
MULTIPLE_ADMISSIBLE_CLASSES_WITH_DIFFERENT_OUTCOMES
  !=
CONFLICTING_EVIDENCE_RECORDS
```

## 10. N7 — partial combined task

Frozen task contains two independent required obligations.

```text
TASK_ID:
  AGG-CH-002-N7

PRIMARY_CLAIM_LEVEL:
  COMBINED_STATIC_DESCRIPTOR
```

Q1 — formation coordinate:

```text
F = {c1,c2}
T(c1)=2
T(c2)=5

Comp(F)=7

expected:
  AGGREGATION_ESTABLISHED
```

Q2 — property coordinate:

```text
G = {i1,u1}

i1:
  defined
  Theta(i1)=4

u1:
  applicable but undefined

all status records:
  available and evaluable
```

Because `u1` is not defined typed property data and cannot be zero-padded:

```text
property aggregate obligation:
  AGGREGATION_NOT_ESTABLISHED
```

Expected task terminal:

```text
AGGREGATION_TASK_PARTIAL
```

Guards:

```text
PARTIAL requires multiple independent required obligations
UNDEFINED_PROPERTY != ZERO
PARTIAL != ESTABLISHED
```

## 11. N8 — collision witness defeats fixed-support injectivity

Frozen task:

```text
TASK_ID:
  AGG-CH-002-N8

PRIMARY_CLAIM_LEVEL:
  AGGREGATE_INJECTIVITY

fixed support:
  F = {a,b}

S_F(u_a,u_b):
  u_a + u_b

A_F:
  {
    (1,-1),
    (2,-2)
  }
```

Compute:

```text
S_F(1,-1) = 0
S_F(2,-2) = 0
```

The assignments differ.

Expected:

```text
COLLISION_STATUS:
  COLLISION_WITNESS_ESTABLISHED

INJECTIVITY_STATUS:
  INJECTIVITY_NOT_ESTABLISHED

PRIMARY_TASK_STATUS:
  AGGREGATION_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_NOT_ESTABLISHED
```

Guard:

```text
SAME_AGGREGATE != SAME_ASSIGNMENT
COLLISION_WITNESS != RECONSTRUCTION
```

## 12. N9 — declared-class injectivity without global promotion

Frozen task:

```text
TASK_ID:
  AGG-CH-002-N9

PRIMARY_CLAIM_LEVEL:
  AGGREGATE_INJECTIVITY

fixed support:
  F = {a,b}

S_F(u_a,u_b):
  u_a + u_b

DECLARED_ADMISSIBLE_CLASS:
  A_F = {(0,0),(1,0),(2,0)}
```

Outputs:

```text
0
1
2
```

Expected:

```text
COLLISION_STATUS:
  NO_COLLISION_ON_TESTED_CLASS

INJECTIVITY_STATUS:
  INJECTIVITY_ESTABLISHED_ON_DECLARED_CLASS

PRIMARY_TASK_STATUS:
  AGGREGATION_ESTABLISHED

TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_ESTABLISHED

GLOBAL_INJECTIVITY:
  not claimed
```

Guards:

```text
INJECTIVITY_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
NO_COLLISION_ON_TESTED_CLASS != GLOBAL_INJECTIVITY
```

This positive subcase is included only to pressure the scope boundary inside the negative/unresolved bundle.

## 13. N10 — frozen terminal precedence with lower-level state retention

Frozen task has three independent required obligations:

```text
TASK_ID:
  AGG-CH-002-N10
```

Q1:

```text
same frozen postprocessing map ID/version
two mutually incompatible applicable definitions
no precedence

status:
  AGGREGATION_CONFLICTING
```

Q2:

```text
two admissible injectivity classes
different outcomes
no resolver

status:
  AGGREGATION_UNDERDETERMINED
```

Q3:

```text
required support sidecar unavailable

status:
  AGGREGATION_BLOCKED
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

Expected:

```text
TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_CONFLICTING

LOWER_LEVEL_Q2_RETAINED:
  yes

LOWER_LEVEL_Q3_RETAINED:
  yes
```

No lower-level state may be erased merely because Q1 determines the task terminal.

## 14. Protocol-conformance expectation

Every subcase is expected to remain:

```text
AGGREGATION_PROTOCOL_CONFORMANT
```

including negative, blocked, conflicting, out-of-scope, underdetermined, and partial results.

No subcase assesses method gain.

```text
AGGREGATION_METHOD_GAIN_STATUS:
  AGGREGATION_METHOD_GAIN_NOT_ASSESSED
```

## 15. Frozen scoring — 80 checks

Each subcase has eight frozen checks.

### N1 — 8 checks

```text
N1-1 c1 admitted
N1-2 cX absent
N1-3 T(cX) undefined
N1-4 cX not zero-extended
N1-5 domain NOT_ADMITTED
N1-6 primary NOT_ESTABLISHED
N1-7 terminal NOT_ESTABLISHED
N1-8 protocol CONFORMANT
```

### N2 — 8 checks

```text
N2-1 countable request frozen
N2-2 terms fixed
N2-3 conditional convergence recognized
N2-4 absolute summability fails
N2-5 domain NOT_ADMITTED
N2-6 primary NOT_ESTABLISHED
N2-7 terminal NOT_ESTABLISHED
N2-8 protocol CONFORMANT
```

### N3 — 8 checks

```text
N3-1 combined-coordinate scope frozen
N3-2 aggregate coordinates available
N3-3 required channel sidecar unavailable
N3-4 required cross-coordinate condition unavailable
N3-5 injectivity BLOCKED
N3-6 primary BLOCKED
N3-7 terminal BLOCKED
N3-8 protocol CONFORMANT
```

### N4 — 8 checks

```text
N4-1 one task/map ID frozen
N4-2 R1 applicable
N4-3 R2 applicable
N4-4 outputs differ
N4-5 no precedence resolver
N4-6 primary CONFLICTING
N4-7 terminal CONFLICTING
N4-8 protocol CONFORMANT
```

### N5 — 8 checks

```text
N5-1 uncountable domain frozen
N5-2 current protocol has no uncountable interface
N5-3 no silent countable reduction
N5-4 domain OUT_OF_SCOPE
N5-5 primary OUT_OF_SCOPE
N5-6 terminal OUT_OF_SCOPE
N5-7 no false/negative reinterpretation
N5-8 protocol CONFORMANT
```

### N6 — 8 checks

```text
N6-1 support/operator frozen
N6-2 A_F^(1) admissible
N6-3 A_F^(2) admissible
N6-4 injectivity outcomes differ
N6-5 no resolver
N6-6 injectivity UNDERDETERMINED
N6-7 task UNDERDETERMINED
N6-8 protocol CONFORMANT
```

### N7 — 8 checks

```text
N7-1 two independent obligations frozen
N7-2 formation aggregate established
N7-3 u1 applicable but undefined
N7-4 u1 not zero-padded
N7-5 property obligation NOT_ESTABLISHED
N7-6 no higher terminal condition
N7-7 terminal PARTIAL
N7-8 protocol CONFORMANT
```

### N8 — 8 checks

```text
N8-1 fixed support/operator frozen
N8-2 admissible class frozen
N8-3 two distinct assignments retained
N8-4 equal aggregate outputs computed
N8-5 collision witness established
N8-6 injectivity NOT_ESTABLISHED
N8-7 task NOT_ESTABLISHED
N8-8 protocol CONFORMANT
```

### N9 — 8 checks

```text
N9-1 declared class frozen
N9-2 outputs computed as 0,1,2
N9-3 no collision on declared class
N9-4 injectivity established on declared class
N9-5 primary ESTABLISHED
N9-6 terminal ESTABLISHED
N9-7 no global injectivity promotion
N9-8 protocol CONFORMANT
```

### N10 — 8 checks

```text
N10-1 conflicting Q1 retained
N10-2 underdetermined Q2 retained
N10-3 blocked Q3 retained
N10-4 frozen precedence applied
N10-5 terminal CONFLICTING
N10-6 Q2 remains visible
N10-7 Q3 remains visible
N10-8 protocol CONFORMANT
```

```text
TOTAL_REQUIRED_CHECKS:
  80

PASS_THRESHOLD:
  80/80

PARTIAL_PASS_ALLOWED:
  no
```

## 16. Counter rule on full PASS

If all 80 checks pass:

```text
DIRECT_AGGREGATION_PILOTS_ATTEMPTED:
  1 -> 2

SUCCESSFUL_DIRECT_AGGREGATION_PILOTS:
  1 -> 2

NEGATIVE_OR_UNRESOLVED_AGGREGATION_CASES:
  0 -> 1

ALL_SEVEN_AGGREGATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
```

Do not change baseline, NO_GAIN, reproducibility, external, or independent-validation counters.
