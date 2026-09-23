# LIN-CH-001 — Positive Constructed Lineage Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-23**  
Challenge ID: `LIN-CH-001`  
Method: **Lineage / DSD 계보론**  
Protocol: **Lineage Protocol v0.1**

Frozen protocol identity:

```text
PROTOCOL_COMMIT:
  f69f364985d604d2c883b14b2efa18535a6bbf6e

PROTOCOL_BLOB:
  0ef686f3987b590e67e07b9ee5e4861c31e6e1ef

VALIDITY_GATES: G1-G16
BINDING_OPERATION: T1-T16
```

## 1. Challenge purpose

Test whether frozen Lineage Protocol v0.1 can establish an interval-level identity claim across:

```text
one fixed-background regular segment
followed by
one explicit formation-transition lineage segment
```

while preserving:

```text
canonical fixed-background channel lineage
explicit cross-transition lineage
component-level lineage
coherent family obligations
branching
identity-bearing state coverage
direct long-interval lineage
interval identity preservation
non-substitution by reduced readouts or Tracking continuity
```

This is constructed internal validation.

It is not external validation, independent replication, or method-gain evidence.

## 2. Frozen task

```text
LINEAGE_TASK_ID:
  LIN-CH-001

TASK_VERSION:
  1

LINEAGE_CLAIM_LEVEL:
  INTERVAL_IDENTITY_PRESERVATION

TIME_SET:
  t0 < t1 < t2

SOURCE_TIME_OR_EPOCH:
  t0

TARGET_TIME_OR_EPOCH:
  t2

TIME_DIRECTION:
  forward

DECLARED_LINEAGE_SCOPE:
  {t0,t1,t2}
  channel lineage
  component lineage
  state succession
  interval identity preservation

REQUIRED_ORDERED_TIME_PAIRS:
  (t0,t1)
  (t1,t2)
  (t0,t2)

TASK_SCOPE_VERSION:
  LIN-CH-001-SCOPE-v1
```

No task field may be changed after execution begins.

## 3. Frozen formation / epoch fixture

### t0 and t1

```text
FORMATION_BACKGROUND:
  B0

REGULAR_EPOCH:
  E0 = {t0,t1}

ADMITTED_CHANNEL_FAMILY:
  C0 = {cA,cB}
```

The source-defined fixed-background canonical channel-lineage gate is expected to apply between t0 and t1.

### t2

```text
FORMATION_BACKGROUND:
  B1

FORMATION_LEVEL_TRANSITION:
  B0 -> B1

ADMITTED_CHANNEL_FAMILY:
  C2 = {cA2,cB2,cC2}
```

The fixed-background canonical gate is expected **not** to cross t1 -> t2.

Cross-transition lineage is supplied explicitly.

## 4. Frozen channel-lineage family

Self-time relations:

```text
Lambda_00:
  (cA,cA)
  (cB,cB)

Lambda_11:
  (cA,cA)
  (cB,cB)

Lambda_22:
  (cA2,cA2)
  (cB2,cB2)
  (cC2,cC2)
```

Cross-time relations:

```text
Lambda_01:
  (cA,cA)
  (cB,cB)

Lambda_12:
  (cA,cA2)
  (cB,cB2)
  (cB,cC2)

Lambda_02:
  (cA,cA2)
  (cB,cB2)
  (cB,cC2)
```

Frozen provenance:

```text
Lambda_01:
  source-defined canonical fixed-background identity relation

Lambda_12:
  explicit transition-lineage fixture record

Lambda_02:
  explicit direct long-interval lineage fixture record
```

Expected:

```text
channel family coherence:
  COHERENT

branching:
  cB -> {cB2,cC2}
  allowed
```

## 5. Frozen component fixture

Component sets:

```text
Xcmp(t0):
  {a0,b0}

Xcmp(t1):
  {a1,b1}

Xcmp(t2):
  {a2,b2,c2}
```

Types and inherited channel tags:

```text
a0,a1,a2:
  COMPONENT_TYPE = identity_core_A
  inherited tags = cA,cA,cA2

b0,b1,b2,c2:
  COMPONENT_TYPE = identity_core_B
  inherited tags = cB,cB,cB2,cC2
```

No auxiliary lineage is required in this fixture.

Self-time component relations are exact identities on each Xcmp(t).

Cross-time component lineage:

```text
L_01:
  (a0,a1)
  (b0,b1)

L_12:
  (a1,a2)
  (b1,b2)
  (b1,c2)

L_02:
  (a0,a2)
  (b0,b2)
  (b0,c2)
```

Expected:

```text
component family coherence:
  COHERENT

component types:
  preserved

inherited channel compatibility:
  preserved

branching:
  b1 -> {b2,c2}
  allowed
```

## 6. Frozen identity-bearing family

```text
IDENTITY_BEARING_FAMILY_ID:
  I-LIN-001

IDENTITY_BEARING_FAMILY_VERSION:
  1

IDENTITY_BEARING_FAMILY_PROVENANCE:
  constructed_fixture_precommit

IDENTITY_BEARING_FAMILY_SELECTION_RULE_OR_JUSTIFICATION:
  all declared identity_core_A and identity_core_B components
  in the frozen fixture are identity-bearing

I(t0):
  {a0,b0}

I(t1):
  {a1,b1}

I(t2):
  {a2,b2,c2}
```

This family is frozen before execution.

## 7. Frozen secondary / neighboring records

Tracking sidecar:

```text
TRACKING_HANDOFF:
  the fixture trace records t0 -> t1 -> t2
  and the explicit transition event
```

Reduced readout sidecar:

```text
REDUCED_READOUT(t0): 10
REDUCED_READOUT(t1): 10
REDUCED_READOUT(t2): 13
```

These records may be retained but may not create or negate lineage.

No Reconstruction candidate is supplied.

No optional unique-successor, bijection, or cardinality-conservation requirement is declared.

## 8. Frozen expected method result

Expected relation-level results:

```text
all required supplied/canonical channel lineage queries:
  LINEAGE_SUCCESSOR_ESTABLISHED

all required component lineage queries:
  LINEAGE_SUCCESSOR_ESTABLISHED

LINEAGE_FAMILY_COHERENCE_STATUS:
  LINEAGE_FAMILY_COHERENT

STATE_SUCCESSION(t0,t1):
  established

STATE_SUCCESSION(t1,t2):
  established

STATE_SUCCESSION(t0,t2):
  established

INTERVAL_IDENTITY_PRESERVATION:
  established

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_ESTABLISHED

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT

LINEAGE_METHOD_GAIN_STATUS:
  LINEAGE_METHOD_GAIN_NOT_ASSESSED
```

Maximum claim:

```text
The constructed state at t2 is a lineage-connected successor
of the constructed state at every earlier required time in the
frozen interval, relative to the frozen identity-bearing family.

The fixture therefore preserves Lineage identity over {t0,t1,t2}
under Protocol v0.1.
```

The result must not be expanded to truth, causality, external identity, uniqueness, bijection, or cardinality conservation.

## 9. Precommitted checks — 64

### A. Task and scope lock — 8

```text
A1 task ID frozen
A2 task version frozen
A3 claim level = INTERVAL_IDENTITY_PRESERVATION
A4 time set frozen
A5 time direction frozen
A6 lineage scope frozen
A7 required ordered pairs frozen
A8 scope version frozen
```

### B. Channel lineage — 10

```text
B1 t0/t1 fixed-background preconditions established
B2 Lambda_01 uses canonical fixed-background identity relation
B3 canonical gate is not extended across t1/t2
B4 Lambda_12 is explicit transition lineage
B5 Lambda_02 is explicit direct long-interval lineage
B6 cA -> cA2 established
B7 cB -> cB2 established
B8 cB -> cC2 established
B9 branching is preserved
B10 no literal tuple-equality claim across transition
```

### C. Component lineage — 10

```text
C1 component IDs remain distinct
C2 component types preserved for A family
C3 component types preserved for B family
C4 inherited channel compatibility preserved for A
C5 inherited channel compatibility preserved for B
C6 a0 -> a1 -> a2 supported
C7 b0 -> b1 supported
C8 b1 -> b2 supported
C9 b1 -> c2 supported
C10 no bijection requirement invented
```

### D. Family coherence — 8

```text
D1 channel self-time identity passes at t0
D2 channel self-time identity passes at t1
D3 channel self-time identity passes at t2
D4 channel composition inclusion passes
D5 component self-time identity passes
D6 component composition inclusion passes
D7 direct Lambda_02 kept distinct from composition result source
D8 direct L_02 kept distinct from composition result source
```

### E. State-succession coverage — 8

```text
E1 identity-bearing family ID/version/provenance frozen
E2 t0 -> t1 predecessor-to-successor coverage passes
E3 t0 -> t1 successor-to-predecessor coverage passes
E4 t1 -> t2 predecessor-to-successor coverage passes
E5 t1 -> t2 successor-to-predecessor coverage passes
E6 t0 -> t2 predecessor-to-successor coverage passes
E7 t0 -> t2 successor-to-predecessor coverage passes
E8 branching does not invalidate state succession
```

### F. Interval identity — 6

```text
F1 state succession established for (t0,t1)
F2 state succession established for (t1,t2)
F3 state succession established for (t0,t2)
F4 every required ordered pair passes
F5 interval identity preservation established
F6 interval claim does not rely on one pair only
```

### G. Boundary guards — 8

```text
G1 Tracking trace not used as successor decision
G2 reduced readout equality t0/t1 not used as lineage criterion
G3 reduced readout change t1/t2 not used as lineage-collapse criterion
G4 formation transition not treated as automatic succession
G5 branching not treated as protocol failure
G6 unique successor not silently imposed
G7 bijection not silently imposed
G8 cardinality conservation not silently imposed
```

### H. Conformance and bounded claim — 6

```text
H1 all applicable G1-G16 protocol gates pass
H2 task terminal = LINEAGE_TASK_ESTABLISHED
H3 protocol conformance = LINEAGE_PROTOCOL_CONFORMANT
H4 method gain = NOT_ASSESSED
H5 maximum-supported claim remains lineage-bounded
H6 no protocol revision or shared-core reopening is inferred from a pass
```

```text
PRECOMMITTED_REQUIRED_CHECKS: 64
```

## 10. Counter rule

If and only if all 64 checks pass:

```text
DIRECT_LINEAGE_PILOTS_ATTEMPTED: 1
SUCCESSFUL_DIRECT_LINEAGE_PILOTS: 1
POSITIVE_LINEAGE_CASES: 1

BASELINE_LINEAGE_CASES: 0
NO_GAIN_LINEAGE_CASES: 0
REPRODUCIBILITY_CASES: 0

EXTERNAL_LINEAGE_APPLICATIONS: 0
INDEPENDENT_LINEAGE_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

CURRENT_LINEAGE_EVIDENCE_STATUS:
  validation_in_progress
```

A failure remains a preserved challenge result and does not authorize post-hoc fixture rewriting.
