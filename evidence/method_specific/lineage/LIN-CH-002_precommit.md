# LIN-CH-002 — Negative and Unresolved-Terminal Lineage Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-25**  
Challenge ID: `LIN-CH-002`  
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

Directly exercise the remaining successor-status and task-terminal distinctions without modifying Protocol v0.1.

The challenge is a bundle of ten independent constructed subcases.

It is internal constructed validation only.

It is not external validation, independent replication, or method-gain evidence.

## 2. Frozen status targets

The challenge must directly exercise:

```text
LINEAGE_SUCCESSOR_EXPLICITLY_NEGATED
LINEAGE_SUCCESSOR_NOT_ESTABLISHED
LINEAGE_SUCCESSOR_AMBIGUOUS
LINEAGE_SUCCESSOR_CONFLICTING
LINEAGE_SUCCESSOR_BLOCKED
LINEAGE_SUCCESSOR_INAPPLICABLE
LINEAGE_SUCCESSOR_OUT_OF_SCOPE
LINEAGE_SUCCESSOR_UNDERDETERMINED
```

and the remaining task terminals:

```text
LINEAGE_TASK_PARTIAL
LINEAGE_TASK_NOT_ESTABLISHED
LINEAGE_TASK_BLOCKED
LINEAGE_TASK_CONFLICTING
LINEAGE_TASK_OUT_OF_SCOPE
LINEAGE_TASK_UNDERDETERMINED
```

`LINEAGE_TASK_ESTABLISHED` was directly exercised by LIN-CH-001 and is not the target of this challenge except as one constituent obligation inside the PARTIAL subcase.

## 3. Frozen subcases

### N1 — explicit negation

Claim:

```text
CHANNEL_LINEAGE:
  cA -> cB
```

The frozen applicable relation source explicitly records that the directed successor relation does not hold.

Expected:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_EXPLICITLY_NEGATED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_NOT_ESTABLISHED
```

Guard:

```text
EXPLICITLY_NEGATED != NOT_ESTABLISHED_AT_RELATION_LEVEL
```

The task terminal may still be `NOT_ESTABLISHED` because the requested proposition is evaluable and fails.

---

### N2 — evaluable absence / not established

The complete in-scope relation is available and evaluable.

The requested pair is absent.

No applicable record explicitly negates it.

Expected:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_NOT_ESTABLISHED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_NOT_ESTABLISHED
```

Guard:

```text
EVALUABLE_ABSENCE != BLOCKED
EVALUABLE_ABSENCE != EXPLICITLY_NEGATED
```

---

### N3 — ambiguous target identity

The request identifies target only by display label `cX`.

The frozen target register contains two distinct objects:

```text
cX-1
cX-2
```

Both share the same display label, and the task supplies no identity resolver.

Neither candidate has an admissible established lineage relation from the predecessor.

Expected:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_AMBIGUOUS

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_NOT_ESTABLISHED
```

Guard:

```text
AMBIGUOUS != UNDERDETERMINED
SAME_LABEL != SAME_ENTITY
```

Because both admissible target resolutions lead to the same task-level failure, this fixture is identity ambiguity rather than outcome underdetermination.

---

### N4 — conflicting lineage records

For the same frozen pair and semantics:

```text
record R1:
  supports cA -> cB

record R2:
  explicitly negates cA -> cB

precedence resolver:
  none
```

Expected:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_CONFLICTING

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_CONFLICTING
```

Guard:

```text
CONFLICTING != UNDERDETERMINED
```

---

### N5 — blocked by unavailable required auxiliary lineage

Component claim:

```text
p0 -> p1
```

The component type and inherited channel relation are supplied.

The frozen multi-input component claim explicitly requires auxiliary lineage for input sort `b`.

That required auxiliary lineage interface is unavailable.

Expected:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_BLOCKED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_BLOCKED
```

Guard:

```text
UNAVAILABLE_REQUIRED_INTERFACE != EVALUABLE_ABSENCE
BLOCKED != NOT_ESTABLISHED
```

---

### N6 — inapplicable relation type

The task is in Lineage scope, but the requested candidate relation attempts a component-successor relation between declared types for which that relation does not apply under the frozen type interface.

The required type records are available and unambiguous.

Expected:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_INAPPLICABLE

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_NOT_ESTABLISHED
```

Guard:

```text
INAPPLICABLE != OUT_OF_SCOPE
INAPPLICABLE != EXPLICITLY_NEGATED
```

---

### N7 — relation outside frozen lineage scope

The frozen task scope includes only:

```text
component lineage for {p0,p1}
```

A separate requested lineage query concerns:

```text
q0 -> q1
```

which is explicitly outside the frozen object set and obligation set.

Expected:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_OUT_OF_SCOPE

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_OUT_OF_SCOPE
```

Guard:

```text
OUT_OF_SCOPE != FALSE
OUT_OF_SCOPE != INAPPLICABLE
```

---

### N8 — underdetermined lineage semantics

Two admissible, frozen relation-schema interpretations are supplied for the same candidate pair.

```text
schema S1:
  pair counts as admissible successor

schema S2:
  pair does not count as admissible successor

precedence resolver:
  none
```

Object identity is unambiguous.

Expected:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_UNDERDETERMINED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_UNDERDETERMINED
```

Guard:

```text
UNDERDETERMINED != AMBIGUOUS
UNDERDETERMINED != CONFLICTING
```

---

### N9 — partial multi-obligation task

The frozen task contains two independent required channel-lineage obligations.

```text
Q1:
  cA -> cA1
  explicit admissible relation supplied

Q2:
  cB -> cB1
  complete relation available
  requested pair absent
  no explicit negation
```

Expected:

```text
Q1:
  LINEAGE_SUCCESSOR_ESTABLISHED

Q2:
  LINEAGE_SUCCESSOR_NOT_ESTABLISHED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_PARTIAL
```

Guard:

```text
PARTIAL requires multiple required obligations

PARTIAL does not rescue
a single failed state-succession proposition
```

---

### N10 — evaluably incoherent lineage family

The frozen family contains:

```text
L_01:
  (a0,a1)

L_12:
  (a1,a2)

L_02:
  empty
```

Therefore:

```text
L_12 o L_01
  =
{(a0,a2)}

not subset
L_02
```

All required relations are available and evaluable.

Expected:

```text
LINEAGE_FAMILY_COHERENCE_STATUS:
  LINEAGE_FAMILY_INCOHERENT

required coherent-family proposition:
  NOT_ESTABLISHED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_NOT_ESTABLISHED
```

Guard:

```text
INCOHERENT != BLOCKED
PAIRWISE_RECORD_PRESENCE != COHERENT_FAMILY
```

## 4. Terminal precedence fixture lock

The ten subcases are independent.

No subcase may borrow another subcase's higher-priority terminal.

Within each subcase, the frozen precedence remains:

```text
OUT_OF_SCOPE
-> CONFLICTING
-> UNDERDETERMINED
-> BLOCKED
-> ESTABLISHED / PARTIAL / NOT_ESTABLISHED
```

Relation-level status must remain recorded even when the task terminal has a coarser label.

## 5. Protocol-conformance lock

All ten subcases are expected to be:

```text
LINEAGE_PROTOCOL_CONFORMANT
```

A negative, blocked, conflicting, out-of-scope, underdetermined, partial, or not-established result is not itself protocol failure.

No post-hoc schema, scope, identity, or terminal change is allowed.

## 6. Precommitted checks — 80

### A. Freeze discipline — 8

```text
A1 protocol commit/blob unchanged
A2 challenge ID frozen
A3 ten subcases frozen
A4 expected relation status for each subcase frozen
A5 expected task terminal for each subcase frozen
A6 terminal precedence frozen
A7 no cross-subcase borrowing
A8 no post-hoc fixture rewrite
```

### B. N1 explicit negation — 7

```text
B1 applicable explicit negation record present
B2 pair identity unambiguous
B3 relation status = EXPLICITLY_NEGATED
B4 relation status != NOT_ESTABLISHED
B5 task terminal = NOT_ESTABLISHED
B6 protocol conformance = CONFORMANT
B7 maximum claim remains bounded
```

### C. N2 evaluable absence — 7

```text
C1 complete relevant relation interface available
C2 requested pair absent
C3 no explicit negation record
C4 relation status = NOT_ESTABLISHED
C5 relation status != BLOCKED
C6 task terminal = NOT_ESTABLISHED
C7 protocol conformance = CONFORMANT
```

### D. N3 ambiguity — 7

```text
D1 two target identities share display label
D2 no identity resolver supplied
D3 both candidate resolutions yield no established lineage
D4 relation status = AMBIGUOUS
D5 relation status != UNDERDETERMINED
D6 task terminal = NOT_ESTABLISHED
D7 protocol conformance = CONFORMANT
```

### E. N4 conflict — 7

```text
E1 support and negation records use same frozen semantics
E2 no precedence resolver supplied
E3 relation status = CONFLICTING
E4 relation status != UNDERDETERMINED
E5 task terminal = CONFLICTING
E6 lower-level records preserved
E7 protocol conformance = CONFORMANT
```

### F. N5 blocked auxiliary lineage — 7

```text
F1 auxiliary lineage explicitly required
F2 required auxiliary interface unavailable
F3 primary object identity/type records available
F4 relation status = BLOCKED
F5 relation status != NOT_ESTABLISHED
F6 task terminal = BLOCKED
F7 protocol conformance = CONFORMANT
```

### G. N6 inapplicable — 7

```text
G1 task itself remains in Lineage scope
G2 object identities unambiguous
G3 requested relation type does not apply
G4 relation status = INAPPLICABLE
G5 relation status != OUT_OF_SCOPE
G6 task terminal = NOT_ESTABLISHED
G7 protocol conformance = CONFORMANT
```

### H. N7 out of scope — 7

```text
H1 frozen object/obligation scope explicit
H2 requested pair outside frozen scope
H3 relation status = OUT_OF_SCOPE
H4 relation status != INAPPLICABLE
H5 task terminal = OUT_OF_SCOPE
H6 no false/negated claim created
H7 protocol conformance = CONFORMANT
```

### I. N8 underdetermined — 7

```text
I1 object identity unambiguous
I2 two admissible relation schemas supplied
I3 schemas yield different claim outcomes
I4 no frozen resolver
I5 relation status = UNDERDETERMINED
I6 task terminal = UNDERDETERMINED
I7 protocol conformance = CONFORMANT
```

### J. N9 partial — 8

```text
J1 two independent required obligations frozen
J2 Q1 relation status = ESTABLISHED
J3 Q2 relation status = NOT_ESTABLISHED
J4 Q2 is evaluable and not blocked
J5 no conflict/underdetermination/out-of-scope condition dominates
J6 task terminal = PARTIAL
J7 PARTIAL is not used for a single failed state-succession proposition
J8 protocol conformance = CONFORMANT
```

### K. N10 incoherent family — 8

```text
K1 all required family relations available
K2 self-time identity records available
K3 L_01 contains (a0,a1)
K4 L_12 contains (a1,a2)
K5 L_02 omits (a0,a2)
K6 composition inclusion fails evaluably
K7 family status = INCOHERENT and task terminal = NOT_ESTABLISHED
K8 protocol conformance = CONFORMANT
```

```text
PRECOMMITTED_REQUIRED_CHECKS: 80
```

## 7. Coverage success criterion

A full challenge pass requires:

```text
all 80 checks PASS

all eight remaining relation statuses directly exercised

all six remaining task terminals directly exercised

protocol conformance preserved in all ten subcases

no protocol revision required

no shared-core reopening required
```

If all pass, update counters to:

```text
DIRECT_LINEAGE_PILOTS_ATTEMPTED: 2
SUCCESSFUL_DIRECT_LINEAGE_PILOTS: 2

POSITIVE_LINEAGE_CASES: 1
NEGATIVE_OR_UNRESOLVED_LINEAGE_CASES: 1

ALL_NINE_LINEAGE_SUCCESSOR_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_LINEAGE_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

BASELINE_LINEAGE_CASES: 0
NO_GAIN_LINEAGE_CASES: 0
REPRODUCIBILITY_CASES: 0

EXTERNAL_LINEAGE_APPLICATIONS: 0
INDEPENDENT_LINEAGE_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

CURRENT_LINEAGE_EVIDENCE_STATUS:
  validation_in_progress
```

A failure is preserved and does not authorize post-hoc rewriting of the fixture or Protocol v0.1.
