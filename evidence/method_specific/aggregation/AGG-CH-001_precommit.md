# AGG-CH-001 — Positive Constructed Aggregation Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-26**  
Challenge ID: `AGG-CH-001`  
Method: **Aggregation / DSD 집계론**  
Protocol: **Aggregation Protocol v0.1**  
Case class: `positive_constructed_aggregation_challenge`  
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

The protocol is immutable for this challenge.

It must not be edited in response to the result.

## 2. Challenge purpose

Test whether frozen Aggregation Protocol v0.1 can execute one positive constructed combined static aggregation task that simultaneously contains:

```text
formation-side finite channel aggregation
typed-property finite aggregation
defined-zero source data
an applicable-but-undefined property sidecar
a multi-input typed property datum
combined-coordinate separation
support-retaining sidecars
separate normalized-average postprocessing
bounded maximum claim
```

The case deliberately does not request source reconstruction or injectivity.

Therefore an established aggregate must not be promoted into a reconstruction result.

This is constructed internal validation.

It is not external validation, independent replication, or method-gain evidence.

## 3. Frozen task lock

```text
AGGREGATION_TASK_ID:
  AGG-CH-001

AGGREGATION_TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  COMBINED_STATIC_DESCRIPTOR

SOURCE_INTERFACE_ID:
  AGG-CH-001-SOURCE-v1

FORMATION_BACKGROUND_ID:
  B-AGG-001

PROPERTY_MODEL_ID:
  A-AGG-001

INPUT_SUPPORT_OR_SELECTION:
  F = {c1,c2,c0}
  G = {i1,i2,i0}

AGGREGATION_DOMAIN_CLASS:
  finite

AGGREGATION_MAP_ID:
  AGG-SUM-v1

OUTPUT_SPACE_AND_TYPE:
  W = R^2
  U = R^2
  combined output in W x U

SUPPORT_RETENTION_POLICY:
  required

NEGATIVE_STATUS_SIDECAR_POLICY:
  required

INJECTIVITY_OR_RECONSTRUCTION_CLAIM:
  none

COUNTABLE_EXTENSION_REQUESTED:
  no

POSTPROCESSING_REQUESTED:
  yes
  POSTPROCESSING_ID = EQUAL_WEIGHT_CHANNEL_AVERAGE-v1

MAXIMUM_SUPPORTED_CLAIM:
  the frozen finite formation and property aggregates,
  their ordered-pair combined descriptor,
  and the separately declared equal-weight channel average
  are correctly computed on the frozen supports while
  source-status/support distinctions remain preserved
```

No claim-relevant lock may change after execution begins.

## 4. Frozen formation-channel fixture

Admitted channel set:

```text
C_L:
  {c1,c2,c0}
```

A non-admitted comparison symbol is also frozen:

```text
cX:
  not in C_L
```

Component-term ledger:

```text
T(c1):
  (2,1)
  status = CHANNEL_PRESENT_TERM_DEFINED_NONZERO
  provenance = CH-TERM-01

T(c2):
  (-1,3)
  status = CHANNEL_PRESENT_TERM_DEFINED_NONZERO
  provenance = CH-TERM-02

T(c0):
  (0,0)
  status = CHANNEL_PRESENT_TERM_DEFINED_ZERO
  provenance = CH-TERM-00

T(cX):
  undefined
  status = CHANNEL_ABSENT
  provenance = CHANNEL_REGISTER_ABSENCE
```

Selected finite support:

```text
F:
  {c1,c2,c0}
```

Frozen formation aggregation operator:

```text
Comp(F):
  sum of T(c) for c in F
```

Expected direct result:

```text
Comp(F):
  (1,4)
```

No normalization is part of the core operator.

## 5. Frozen property fixture

Defined typed-property carrier includes:

```text
i1:
  property kind = p_unary
  typed input = (x1)
  bridge image Theta(i1) = (4,0)
  status = PROPERTY_DEFINED_NONZERO
  provenance = PROP-01

i2:
  property kind = p_binary
  typed input = (x1,x2)
  bridge image Theta(i2) = (-1,2)
  status = PROPERTY_DEFINED_NONZERO
  provenance = PROP-02

i0:
  property kind = p_zero
  typed input = (x0)
  bridge image Theta(i0) = (0,0)
  status = PROPERTY_DEFINED_ZERO
  provenance = PROP-00
```

Negative-status sidecar:

```text
u1:
  property kind = p_pending
  typed input = (x3)
  status = PROPERTY_APPLICABLE_UNDEFINED
  provenance = PROP-UNDEF-01
```

`u1` is not a member of the defined typed-property carrier and must not be zero-padded into the aggregate.

Selected finite property support:

```text
G:
  {i1,i2,i0}
```

Frozen property aggregation operator:

```text
Agg(G):
  sum of Theta(iota) for iota in G
```

Expected result:

```text
Agg(G):
  (3,2)
```

## 6. Frozen multi-input property rule

For `i2`:

```text
typed input:
  (x1,x2)

explicit single-channel selector/allocation rule:
  none
```

Expected:

```text
complete ordered typed input:
  retained

canonical single-channel owner:
  not inferred
```

## 7. Frozen combined descriptor

Expected combined output:

```text
Static(F,G):
  ((1,4),(3,2))
```

Required coordinate interpretation:

```text
first coordinate:
  formation-compatible finite channel aggregate

second coordinate:
  finite typed-property aggregate

FORMATION_COORDINATE
  !=
PROPERTY_COORDINATE
```

Numerical comparison between coordinates is not an identity rule.

## 8. Frozen support/status sidecars

Required channel support sidecar:

```text
H_channel(F):
  {
    (c1,(2,1)),
    (c2,(-1,3)),
    (c0,(0,0))
  }
```

Required property support sidecar:

```text
H_property(G):
  {
    (i1,(4,0)),
    (i2,(-1,2)),
    (i0,(0,0))
  }
```

Required negative-status sidecar:

```text
u1:
  PROPERTY_APPLICABLE_UNDEFINED
```

Expected preservation:

```text
c0 defined zero != cX absent
i0 defined zero != u1 applicable but undefined
```

## 9. Frozen postprocessing

Equal-weight channel average is separately declared:

```text
Avg(F):
  (1/3) T(c1)
  + (1/3) T(c2)
  + (1/3) T(c0)

expected:
  (1/3,4/3)
```

Required guard:

```text
Avg(F)
  !=
Comp(F)
```

The average is a downstream readout and does not replace the direct finite Formation-compatible aggregate.

## 10. Frozen optional-ledger expectations

```text
COUNTABLE_EXTENSION_LEDGER:
  NOT_REQUESTED

COLLISION_LEDGER:
  COLLISION_NOT_TESTED

INJECTIVITY_LEDGER:
  INJECTIVITY_NOT_TESTED

RECONSTRUCTION_SCOPE_LEDGER:
  RECONSTRUCTION_NOT_CLAIMED

CROSS_COORDINATE_CONDITION_LEDGER:
  NOT_APPLICABLE

STABILITY_LEDGER:
  NOT_REQUESTED

SPECIALIZED_READOUT_LEDGER:
  NOT_REQUESTED
```

No global no-collision, injectivity, or reconstruction claim may be inferred from this positive task.

## 11. Frozen expected task result

```text
FORMATION_AGGREGATION_STATUS:
  AGGREGATION_ESTABLISHED

PROPERTY_AGGREGATION_STATUS:
  AGGREGATION_ESTABLISHED

COMBINED_STATIC_DESCRIPTOR_STATUS:
  AGGREGATION_ESTABLISHED

AGGREGATION_TASK_TERMINAL_STATUS:
  AGGREGATION_TASK_ESTABLISHED

AGGREGATION_PROTOCOL_CONFORMANCE:
  AGGREGATION_PROTOCOL_CONFORMANT

AGGREGATION_METHOD_GAIN_STATUS:
  AGGREGATION_METHOD_GAIN_NOT_ASSESSED

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 12. Frozen scoring — 64 checks

### A. Task/source immutability — 8

```text
A1 protocol commit/blob frozen
A2 task ID/version frozen
A3 primary claim level frozen
A4 formation/property source IDs frozen
A5 supports F and G frozen
A6 aggregation operator/output spaces frozen
A7 support/status sidecar policies frozen
A8 no post-hoc task repair
```

### B. Formation-side execution — 12

```text
B1 c1 admitted
B2 c2 admitted
B3 c0 admitted
B4 cX absent
B5 c0 defined-zero status preserved
B6 cX not zero-extended
B7 T(c1) retained exactly
B8 T(c2) retained exactly
B9 T(c0) retained exactly
B10 direct finite sum computed as (1,4)
B11 direct sum is unnormalized
B12 formation aggregate established
```

### C. Property-side execution — 12

```text
C1 i1 defined and selected
C2 i2 defined and selected
C3 i0 defined zero and selected
C4 u1 applicable-but-undefined retained in negative-status sidecar
C5 u1 excluded from defined aggregate carrier
C6 u1 not zero-padded
C7 i2 complete ordered typed input retained
C8 no canonical single-channel owner inferred for i2
C9 Theta(i1) retained exactly
C10 Theta(i2) retained exactly
C11 Theta(i0) retained exactly
C12 property aggregate computed as (3,2) and established
```

### D. Combined descriptor — 8

```text
D1 combined descriptor computed as ((1,4),(3,2))
D2 formation coordinate identified correctly
D3 property coordinate identified correctly
D4 coordinates not conflated
D5 formation/property provenance retained
D6 finite domain retained
D7 no countable-core substitution
D8 combined claim established
```

### E. Support/status retention — 10

```text
E1 H_channel(F) emitted
E2 H_property(G) emitted
E3 negative-status sidecar emitted
E4 c0 present/zero preserved
E5 cX absent preserved
E6 i0 defined-zero preserved
E7 u1 undefined preserved
E8 aggregate equality/source identity not inferred
E9 support equality/source reconstruction not inferred
E10 required support/status interfaces available
```

### F. Postprocessing and optional-boundary discipline — 8

```text
F1 equal-weight Avg(F) computed as (1/3,4/3)
F2 Avg(F) recorded as postprocessing
F3 Avg(F) not substituted for Comp(F)
F4 countable extension NOT_REQUESTED
F5 collision COLLISION_NOT_TESTED
F6 injectivity INJECTIVITY_NOT_TESTED
F7 reconstruction RECONSTRUCTION_NOT_CLAIMED
F8 static stability and specialized readout remain NOT_REQUESTED
```

### G. Final protocol result — 6

```text
G1 terminal AGGREGATION_TASK_ESTABLISHED
G2 protocol AGGREGATION_PROTOCOL_CONFORMANT
G3 method gain AGGREGATION_METHOD_GAIN_NOT_ASSESSED
G4 maximum-supported claim remains bounded
G5 protocol revision not required
G6 shared core reopening not required
```

```text
TOTAL_REQUIRED_CHECKS:
  64

PASS_THRESHOLD:
  64/64

PARTIAL_PASS_ALLOWED:
  no
```

## 13. Counter rule on full PASS

If and only if all 64 checks pass:

```text
DIRECT_AGGREGATION_PILOTS_ATTEMPTED:
  0 -> 1

SUCCESSFUL_DIRECT_AGGREGATION_PILOTS:
  0 -> 1

POSITIVE_AGGREGATION_CASES:
  0 -> 1
```

No baseline, NO_GAIN, reproducibility, external, or independent-validation counter changes.
