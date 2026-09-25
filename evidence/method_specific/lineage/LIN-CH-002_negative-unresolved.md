# LIN-CH-002 — Negative and Unresolved-Terminal Lineage Challenge Result

Status: **EXECUTED — 80/80 PASS**  
Date: **2026-09-25**  
Challenge ID: `LIN-CH-002`  
Method: **Lineage / DSD 계보론**  
Protocol: **Lineage Protocol v0.1**

Frozen references:

```text
PROTOCOL_COMMIT:
  f69f364985d604d2c883b14b2efa18535a6bbf6e

PROTOCOL_BLOB:
  0ef686f3987b590e67e07b9ee5e4861c31e6e1ef

PRECOMMIT_COMMIT:
  169021711ea5069f1e63246efdd2ddfafbb3067a

PRECOMMIT_BLOB:
  d5537721f9dc55291f61569ad57eaa7e6b844a5b
```

## 1. Final result

```text
PRECOMMITTED_REQUIRED_CHECKS: 80
PASSED: 80
FAILED: 0

ALL_NINE_LINEAGE_SUCCESSOR_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_LINEAGE_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

LIN-CH-001 directly exercised the established relation/task case.

LIN-CH-002 directly exercised all eight remaining successor statuses and all six remaining task terminals.

All ten LIN-CH-002 subcases remained protocol-conformant.

## 2. N1 — explicit negation

Frozen record:

```text
claim:
  cA -> cB

applicable relation source:
  explicitly negates the directed successor relation
```

Result:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_EXPLICITLY_NEGATED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_NOT_ESTABLISHED

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT
```

Preserved distinction:

```text
EXPLICITLY_NEGATED
  !=
NOT_ESTABLISHED_AT_RELATION_LEVEL
```

The coarser task terminal remains NOT_ESTABLISHED because the requested proposition is evaluable and fails.

## 3. N2 — evaluable absence / not established

The complete relevant relation interface is available.

The requested pair is absent.

No explicit negation exists.

Result:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_NOT_ESTABLISHED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_NOT_ESTABLISHED

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT
```

Preserved:

```text
EVALUABLE_ABSENCE != BLOCKED
EVALUABLE_ABSENCE != EXPLICITLY_NEGATED
```

## 4. N3 — ambiguous target identity

The display label `cX` refers to two distinct frozen target identities:

```text
cX-1
cX-2
```

No identity resolver is supplied.

Both candidate resolutions fail to establish the requested lineage relation.

Result:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_AMBIGUOUS

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_NOT_ESTABLISHED

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT
```

Preserved:

```text
AMBIGUOUS != UNDERDETERMINED
SAME_LABEL != SAME_ENTITY
```

Because all admissible identity resolutions yield the same task-level non-establishment, this is ambiguity, not outcome underdetermination.

## 5. N4 — conflicting lineage records

Frozen records:

```text
R1:
  supports cA -> cB

R2:
  explicitly negates cA -> cB

precedence resolver:
  none
```

Result:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_CONFLICTING

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_CONFLICTING

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT
```

Both lower-level records remain preserved.

```text
CONFLICTING != UNDERDETERMINED
```

## 6. N5 — blocked by unavailable required auxiliary lineage

Frozen component claim requires auxiliary lineage for input sort `b`.

The primary object/type records are available.

The required auxiliary-lineage interface is unavailable.

Result:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_BLOCKED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_BLOCKED

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT
```

Preserved:

```text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
EVALUABLE_ABSENCE

BLOCKED
  !=
NOT_ESTABLISHED
```

## 7. N6 — inapplicable relation type

The Lineage task is in scope.

The requested relation type does not apply to the declared source/target object types.

All type records are available and unambiguous.

Result:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_INAPPLICABLE

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_NOT_ESTABLISHED

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT
```

Preserved:

```text
INAPPLICABLE != OUT_OF_SCOPE
INAPPLICABLE != EXPLICITLY_NEGATED
```

## 8. N7 — out of frozen scope

The frozen task covers only:

```text
component lineage for {p0,p1}
```

The requested pair:

```text
q0 -> q1
```

is outside both the frozen object set and obligation set.

Result:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_OUT_OF_SCOPE

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_OUT_OF_SCOPE

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT
```

No false or negated lineage claim is created.

## 9. N8 — underdetermined lineage semantics

Object identity is unambiguous.

Two admissible frozen relation-schema interpretations yield different outcomes:

```text
S1:
  successor relation established

S2:
  successor relation not established

resolver:
  none
```

Result:

```text
LINEAGE_SUCCESSOR_STATUS:
  LINEAGE_SUCCESSOR_UNDERDETERMINED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_UNDERDETERMINED

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT
```

Preserved:

```text
UNDERDETERMINED != AMBIGUOUS
UNDERDETERMINED != CONFLICTING
```

## 10. N9 — partial multi-obligation task

Two independent obligations are frozen.

```text
Q1:
  cA -> cA1
  established

Q2:
  cB -> cB1
  evaluable absence
  not established
```

Result:

```text
Q1:
  LINEAGE_SUCCESSOR_ESTABLISHED

Q2:
  LINEAGE_SUCCESSOR_NOT_ESTABLISHED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_PARTIAL

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT
```

No higher-priority terminal condition is present.

The PARTIAL terminal is not used to rescue a single failed state-succession proposition.

## 11. N10 — evaluably incoherent family

Frozen family:

```text
L_01:
  (a0,a1)

L_12:
  (a1,a2)

L_02:
  empty
```

Composition:

```text
L_12 o L_01
  =
{(a0,a2)}
```

Therefore:

```text
{(a0,a2)}
  not subset
L_02
```

Result:

```text
LINEAGE_FAMILY_COHERENCE_STATUS:
  LINEAGE_FAMILY_INCOHERENT

COHERENT_FAMILY_PROPOSITION:
  NOT_ESTABLISHED

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_NOT_ESTABLISHED

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT
```

All required records are present, so this is not BLOCKED.

Pairwise record presence is preserved separately from family-coherence failure.

## 12. Terminal precedence verification

The frozen precedence remained unchanged:

```text
OUT_OF_SCOPE
-> CONFLICTING
-> UNDERDETERMINED
-> BLOCKED
-> ESTABLISHED / PARTIAL / NOT_ESTABLISHED
```

Direct terminal coverage across LIN-CH-001 and LIN-CH-002:

```text
LINEAGE_TASK_ESTABLISHED:
  LIN-CH-001

LINEAGE_TASK_PARTIAL:
  LIN-CH-002 N9

LINEAGE_TASK_NOT_ESTABLISHED:
  LIN-CH-002 N1, N2, N3, N6, N10

LINEAGE_TASK_BLOCKED:
  LIN-CH-002 N5

LINEAGE_TASK_CONFLICTING:
  LIN-CH-002 N4

LINEAGE_TASK_OUT_OF_SCOPE:
  LIN-CH-002 N7

LINEAGE_TASK_UNDERDETERMINED:
  LIN-CH-002 N8
```

Thus:

```text
ALL_SEVEN_LINEAGE_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
```

## 13. Successor-status coverage verification

Direct coverage across LIN-CH-001 and LIN-CH-002:

```text
LINEAGE_SUCCESSOR_ESTABLISHED:
  LIN-CH-001
  LIN-CH-002 N9 Q1

LINEAGE_SUCCESSOR_EXPLICITLY_NEGATED:
  LIN-CH-002 N1

LINEAGE_SUCCESSOR_NOT_ESTABLISHED:
  LIN-CH-002 N2
  LIN-CH-002 N9 Q2

LINEAGE_SUCCESSOR_AMBIGUOUS:
  LIN-CH-002 N3

LINEAGE_SUCCESSOR_CONFLICTING:
  LIN-CH-002 N4

LINEAGE_SUCCESSOR_BLOCKED:
  LIN-CH-002 N5

LINEAGE_SUCCESSOR_INAPPLICABLE:
  LIN-CH-002 N6

LINEAGE_SUCCESSOR_OUT_OF_SCOPE:
  LIN-CH-002 N7

LINEAGE_SUCCESSOR_UNDERDETERMINED:
  LIN-CH-002 N8
```

Thus:

```text
ALL_NINE_LINEAGE_SUCCESSOR_STATUSES_DIRECTLY_EXERCISED:
  yes
```

## 14. Execution of the 80 precommitted checks

```text
A1 PASS
A2 PASS
A3 PASS
A4 PASS
A5 PASS
A6 PASS
A7 PASS
A8 PASS

B1 PASS
B2 PASS
B3 PASS
B4 PASS
B5 PASS
B6 PASS
B7 PASS

C1 PASS
C2 PASS
C3 PASS
C4 PASS
C5 PASS
C6 PASS
C7 PASS

D1 PASS
D2 PASS
D3 PASS
D4 PASS
D5 PASS
D6 PASS
D7 PASS

E1 PASS
E2 PASS
E3 PASS
E4 PASS
E5 PASS
E6 PASS
E7 PASS

F1 PASS
F2 PASS
F3 PASS
F4 PASS
F5 PASS
F6 PASS
F7 PASS

G1 PASS
G2 PASS
G3 PASS
G4 PASS
G5 PASS
G6 PASS
G7 PASS

H1 PASS
H2 PASS
H3 PASS
H4 PASS
H5 PASS
H6 PASS
H7 PASS

I1 PASS
I2 PASS
I3 PASS
I4 PASS
I5 PASS
I6 PASS
I7 PASS

J1 PASS
J2 PASS
J3 PASS
J4 PASS
J5 PASS
J6 PASS
J7 PASS
J8 PASS

K1 PASS
K2 PASS
K3 PASS
K4 PASS
K5 PASS
K6 PASS
K7 PASS
K8 PASS

PRECOMMITTED_REQUIRED_CHECKS: 80
PASSED: 80
FAILED: 0
```

## 15. Conformance result

All ten subcases are:

```text
LINEAGE_PROTOCOL_CONFORMANT
```

The challenge demonstrates that negative and unresolved outcomes are valid protocol outputs rather than protocol failures.

No scope, identity, relation schema, terminal rule, or expected status was changed after execution began.

## 16. Counter update

Because all 80 checks passed:

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

LINEAGE_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_LINEAGE_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 17. Maximum-supported claim

Supported:

```text
Within the constructed LIN-CH-002 fixture set,
Protocol v0.1 preserves the frozen distinctions among
negative, ambiguous, conflicting, blocked, inapplicable,
out-of-scope, underdetermined, partial, and incoherent-family
Lineage outcomes without turning those outcomes into protocol failure.
```

Not established:

```text
external applicability
independent validation
independent replication
method superiority
permanent method irreducibility
```

## 18. Next

Prospectively precommit and execute the direct neighboring-method boundary challenge.

The next challenge should compare Lineage against at least:

```text
Tracking
Reconstruction
Transformation
Comparison
Classification
Aggregation / Compression
Dynamics source handoff
Audit
```

under fair shared-artifact access, while preserving that fixture-bounded non-collapse is not a permanent method-survival proof.
