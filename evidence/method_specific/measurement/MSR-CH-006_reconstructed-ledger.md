# MSR-CH-006 Reconstruction Ledger — Frozen Before P2 Comparison

Status: **RECONSTRUCTED FROM P0 + P1 / P2 NOT USED IN DERIVATION**  
Date: **2026-09-20**  
Case ID: `MSR-CH-006`

## 1. Reconstruction basis

```text
P0 Measurement Protocol v0.1
commit: 70af7c3ddc618be34d0ff76fcc1ce63c895fc950
blob:   bc24a5e72adaf4a1b1e64203bd14b3e781810331

P1 MSR-CH-005 precommit
commit: 7722081d8b3612fd1c151aac63f7482c6cb882b7
blob:   5465898b17847ed627cb48fe98c678c77a4e7b4d

MSR-CH-006 precommit
commit: 25d32656d5aa50f5f4c3f15b0fa042d27e5f47a1
blob:   a6a31c2a036638fa0c844fb3b4f22af6ccb86dac
```

`MSR-CH-005` result artifact P2 was not used to derive this ledger.

## 2. R1 — version-scoped decision semantics

Frozen raw records:

```text
A=0.6
B=0.4
```

V1:

```text
HIGH iff x >= 0.5
LOW iff x < 0.5

A -> HIGH
B -> LOW

A-B -> PAIRWISE_DISCRIMINATING
candidate -> MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION
plan -> MEASUREMENT_PLAN_SUFFICIENT
```

V2:

```text
HIGH iff x >= 0.7
LOW iff x < 0.7

A -> LOW
B -> LOW

A-B -> PAIRWISE_NONDISCRIMINATING
candidate -> MEASUREMENT_NONDISCRIMINATING
plan -> MEASUREMENT_PLAN_INSUFFICIENT
```

Reconstructed guard:

```text
SAME_RAW_VALUES != SAME_DECISION_SEMANTICS_ACROSS_VERSIONS
LATER_RULE != RETROACTIVE_RULE_FOR_EARLIER_TASK
```

## 3. R2 — dynamic distinguishability support

At t0:

```text
upstream structural difference: exists
distinguishability support at L: NOT_YET_AVAILABLE

local use as present readout evidence:
  prohibited

negative-result inference from non-arrival:
  prohibited

candidate usability:
  blocked by unavailable claim-relevant dynamic-support prerequisite

plan:
  MEASUREMENT_PLAN_BLOCKED
```

At t1:

```text
distinguishability support at L: AVAILABLE

C -> RED
D -> BLUE

C-D -> PAIRWISE_DISCRIMINATING
plan -> MEASUREMENT_PLAN_SUFFICIENT
```

Reconstructed guard:

```text
NOT_YET_DISTINGUISHABLE != NEGATIVE_EVIDENCE
UPSTREAM_DIFFERENCE != PRESENT_LOCAL_READOUT
```

## 4. R3 — mixed candidate quality

```text
m1:
  E-F discriminate
  E-G discriminate
  F-G nondiscriminate
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

m2:
  E-F nondiscriminate
  E-G discriminate
  F-G discriminate
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

m3:
  same discrimination partition as m1
  -> redundant
  -> no new required distinction

m4:
  applicable
  required bridge absent
  -> MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE

m5:
  candidate domain Z
  task object class Y
  -> MEASUREMENT_INAPPLICABLE
```

Predeclared joint plan:

```text
{m1,m2}

E -> (0,0)
F -> (1,0)
G -> (1,1)

E-F discriminate
E-G discriminate
F-G discriminate

plan -> MEASUREMENT_PLAN_SUFFICIENT
```

No DSD claim is made here about global minimality or optimization.

Reconstructed guards:

```text
MORE_CANDIDATES != MORE_INFORMATION
REDUNDANT_CANDIDATE != NEW_DISCRIMINATION
BASELINE_EXTRA_SEARCH_CAPABILITY != DSD_PROTOCOL_FAILURE
```

## 5. R4 — proxy / aggregate collision / reconstruction bounds

Direct candidate:

```text
m_direct:
  H -> P
  I -> Q
  J -> Q

H-I discriminate
H-J discriminate
I-J nondiscriminate

-> MEASUREMENT_PARTIALLY_DISCRIMINATES
```

Proxy aggregate candidate:

```text
H support {+2,-2} -> aggregate 0
I support {0}     -> aggregate 0
J support {+3}    -> aggregate 3

role:
  proxy via aggregate handoff

H-I nondiscriminate
H-J discriminate
I-J discriminate

-> MEASUREMENT_PARTIALLY_DISCRIMINATES
```

Joint:

```text
H -> (P,0)
I -> (Q,0)
J -> (Q,3)

all required pairs discriminate

plan -> MEASUREMENT_PLAN_SUFFICIENT
```

Sidecars:

```text
H/I aggregate collision: retained
aggregate map noninjective: retained
full support reconstruction: unavailable
proxy/direct roles: retained
true alternative: not established
```

Reconstructed guards:

```text
PROXY != DIRECT
EQUAL_AGGREGATE != EQUAL_SUPPORT
DISCRIMINATING_PROXY != FULL_RECONSTRUCTION
PLAN_SUFFICIENT != TRUE_ALTERNATIVE_IDENTIFIED
```

## 6. R5 — competing bridge versions

```text
V1:
  K -> OPEN
  L -> CLOSED
  -> PAIRWISE_DISCRIMINATING

V2:
  K -> OPEN
  L -> OPEN
  -> PAIRWISE_NONDISCRIMINATING

both bridge versions:
  fully supplied
  admissible

precedence:
  none
```

Therefore:

```text
candidate -> MEASUREMENT_UNDERDETERMINED
plan -> MEASUREMENT_PLAN_UNDERDETERMINED
```

Reconstructed guards:

```text
MULTIPLE_ADMISSIBLE_BRIDGES != MISSING_BRIDGE
NO_PRECEDENCE != LICENSE_TO_CHOOSE_POST_HOC
```

## 7. Protocol-level reconstructed outputs

```text
MEASUREMENT_PROTOCOL_CONFORMANCE:
  CONFORMANT

PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

Maximum supported claim:

```text
The frozen Measurement tasks establish only discrimination,
availability, scope, candidate-status, and plan-terminal judgments
under the supplied records and frozen semantics.
```

Not established:

```text
observed experimental result
true alternative
diagnosis
causality
full structural reconstruction
external empirical validity
independent validation
```

## 8. Reconstruction ledger status

```text
R1_RECONSTRUCTED: yes
R2_RECONSTRUCTED: yes
R3_RECONSTRUCTED: yes
R4_RECONSTRUCTED: yes
R5_RECONSTRUCTED: yes

P2_USED_IN_DERIVATION: no
POST_HOC_CORRECTIONS: 0

RECONSTRUCTION_LEDGER_FROZEN:
  yes
```

This artifact is now the retrace output to be compared against immutable P2.
