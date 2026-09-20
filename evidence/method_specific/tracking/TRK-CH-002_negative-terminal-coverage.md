# TRK-CH-002 — Negative / Unresolved Terminal Coverage Challenge Result

Status: **EXECUTED — 64/64 PASS**  
Date: **2026-09-21**  
Case ID: `TRK-CH-002`  
Case class: `negative_unresolved_terminal_coverage_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen identities

```text
PROTOCOL_COMMIT:
  a0d979325c11919fecaa4d8eab129477a365af87

PROTOCOL_BLOB:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

BOUNDARY_AMENDMENT_COMMIT:
  086c537b1312838500f6d188f32e7c643bde990b

BOUNDARY_AMENDMENT_BLOB:
  846a195f1e18c1fd1b9824638d98e10fc837f10e

PRECOMMIT_COMMIT:
  bf5ecb9f0ea21e391301bc4de2a0635c6cacb853

PRECOMMIT_BLOB:
  6181f8a53dd89a00164a128a3689f33c2ba7df60
```

No protocol, amendment, subcase, relation schema, query, expected status, terminal rule, or scoring item was changed after precommit.

## 2. N1 — partial trace

Frozen required queries:

```text
Q1 SOURCE_S SOURCE_OF PACKAGE_P
Q2 PACKAGE_P REFERENCES REF_FORBIDDEN
Q3 PACKAGE_P STORED_IN LOCATION_L
Q4 PACKAGE_P REFERENCES "REF_ALPHA"
```

### Q1 — established

Applicable E1 directly supports:

```text
SOURCE_S SOURCE_OF PACKAGE_P
```

Result:

```text
Q1:
  TRACKING_LINK_ESTABLISHED
```

### Q2 — explicitly negated

Applicable E2 explicitly states that, under the frozen schema:

```text
PACKAGE_P does not reference REF_FORBIDDEN
```

Result:

```text
Q2:
  TRACKING_LINK_EXPLICITLY_NEGATED
```

This is not inferred from absence.

```text
EXPLICITLY_NEGATED != MISSING
```

### Q3 — missing

For:

```text
PACKAGE_P STORED_IN LOCATION_L
```

the frozen state is:

```text
support record: absent
explicit negation: absent
required schema/prerequisite/access: available
```

Therefore:

```text
Q3:
  TRACKING_LINK_MISSING
```

It is not blocked because the evaluator is able to evaluate the query and finds neither supporting nor explicitly negating trace evidence.

```text
MISSING != BLOCKED
```

### Q4 — ambiguous node identity

The supplied reference record names display label `REF_ALPHA`.

The node register contains:

```text
R1 display label = REF_ALPHA
R2 display label = REF_ALPHA
R1 != R2
```

No unique target identifier is supplied.

Therefore:

```text
Q4:
  TRACKING_LINK_AMBIGUOUS
```

Neither R1 nor R2 is selected.

```text
SAME_LABEL != SAME_ENTITY
AMBIGUOUS != LICENSE_TO_CHOOSE_POST_HOC
```

### N1 terminal

Q1 and Q2 are resolved under the frozen completion criterion.

Q3 and Q4 remain unresolved.

No out-of-scope, conflicting, underdetermined, or blocked condition dominates.

Therefore:

```text
TRACKING_TRACE_TERMINAL_STATUS:
  TRACKING_TRACE_PARTIAL
```

Preserved:

```text
PARTIAL != COMPLETE
EXPLICITLY_NEGATED != MISSING
MISSING != BLOCKED
AMBIGUOUS != UNDERDETERMINED
```

N1 conformance: `CONFORMANT`.

## 3. N2 — blocked trace with inapplicable relation

### Q1 — blocked

Frozen query:

```text
ARTIFACT_A TRANSFORMATION_HANDOFF_TO ARTIFACT_B
```

Frozen state:

```text
encrypted handoff envelope:
  supplied

required decoder/schema mapping:
  explicitly unavailable

relation evaluation:
  cannot proceed without decoder
```

Therefore:

```text
Q1:
  TRACKING_LINK_BLOCKED
```

The relation is not merely missing: a candidate record exists, but a required prerequisite for interpreting it is unavailable.

```text
BLOCKED != MISSING
BLOCKED != NEGATED
```

### Q2 — inapplicable

Frozen query:

```text
ARTIFACT_A CUSTODY_HELD_BY CONTAINER_C
```

Frozen typing:

```text
CONTAINER_C:
  non-actor storage container

CUSTODY_HELD_BY schema:
  target must be actor/custodian
```

Therefore:

```text
Q2:
  TRACKING_LINK_INAPPLICABLE
```

It is not an explicit negative custody claim.

```text
INAPPLICABLE != NEGATED
INAPPLICABLE != OUT_OF_SCOPE
```

### N2 terminal

Because a required in-scope relation cannot be evaluated due to a missing required decoder:

```text
TRACKING_TRACE_TERMINAL_STATUS:
  TRACKING_TRACE_BLOCKED
```

The separate inapplicable link remains visible at link level.

```text
CONFORMANT_BLOCKED_TRACE != METHOD_FAILURE
```

N2 conformance: `CONFORMANT`.

## 4. N3 — conflicting trace

Frozen query:

```text
ARTIFACT_C STORED_IN ? at T0
```

Applicable records:

```text
E31:
  ARTIFACT_C STORED_IN LOCATION_X at T0

E32:
  ARTIFACT_C STORED_IN LOCATION_Y at T0
```

Frozen relation schema states:

```text
exactly one exclusive storage location at T0
LOCATION_X != LOCATION_Y
```

Both records are applicable.

No precedence rule is supplied.

Therefore:

```text
relation status:
  TRACKING_LINK_CONFLICTING

TRACKING_TRACE_TERMINAL_STATUS:
  TRACKING_TRACE_CONFLICTING
```

Neither record is discarded.

```text
CONFLICTING != AMBIGUOUS
CONFLICTING != UNDERDETERMINED
CONFLICTING_LINKS != LICENSE_TO_DISCARD_ONE
```

The conflict is between applicable evidence assertions under one frozen schema, not between competing schemas.

N3 conformance: `CONFORMANT`.

## 5. N4 — out-of-scope trace request

Frozen task dimensions:

```text
origin/source
version
```

Frozen requested query:

```text
ARTIFACT_D OWNED_BY ACTOR_Z
```

Ownership is not in the frozen trace dimension set.

No scope extension was supplied.

Therefore:

```text
relation status:
  TRACKING_LINK_OUT_OF_SCOPE

TRACKING_TRACE_TERMINAL_STATUS:
  TRACKING_TRACE_OUT_OF_SCOPE
```

No ownership relation is fabricated.

```text
OUT_OF_SCOPE != INAPPLICABLE
OUT_OF_SCOPE != MISSING
OUT_OF_SCOPE != FALSE
NO_SCOPE_EXTENSION != NEGATIVE_RELATION
```

N4 conformance: `CONFORMANT`.

## 6. N5 — underdetermined relation schema

Frozen query:

```text
ARTIFACT_E DEPENDS_ON LIB_Q
```

Frozen candidate record:

```text
DQ-1
```

Two relation-schema versions are simultaneously admissible.

### DEP-v1

```text
DQ-1 means:
  ARTIFACT_E DEPENDS_ON LIB_Q

path result:
  TRACKING_LINK_ESTABLISHED
```

### DEP-v2

```text
DQ-1 means:
  metadata reference only
  the frozen DEPENDS_ON query is explicitly not satisfied

path result:
  TRACKING_LINK_EXPLICITLY_NEGATED
```

Both schemas are supplied and applicable.

No precedence rule exists.

Therefore the final Tracking relation judgment is:

```text
TRACKING_LINK_UNDERDETERMINED
```

and:

```text
TRACKING_TRACE_TERMINAL_STATUS:
  TRACKING_TRACE_UNDERDETERMINED
```

No schema is selected post hoc.

```text
MULTIPLE_ADMISSIBLE_SCHEMAS != MISSING_SCHEMA
UNDERDETERMINED != CONFLICTING
UNDERDETERMINED != BLOCKED
UNDERDETERMINED != LICENSE_TO_CHOOSE_POST_HOC
```

The underdetermination is semantic/schema-level, whereas N3 is evidence-conflict under one fixed schema.

N5 conformance: `CONFORMANT`.

## 7. Link-status coverage after TRK-CH-001 + TRK-CH-002

```text
TRACKING_LINK_ESTABLISHED:
  TRK-CH-001 Q1-Q12
  TRK-CH-002-N1 Q1

TRACKING_LINK_EXPLICITLY_NEGATED:
  TRK-CH-002-N1 Q2

TRACKING_LINK_MISSING:
  TRK-CH-002-N1 Q3

TRACKING_LINK_AMBIGUOUS:
  TRK-CH-002-N1 Q4

TRACKING_LINK_CONFLICTING:
  TRK-CH-002-N3

TRACKING_LINK_BLOCKED:
  TRK-CH-002-N2 Q1

TRACKING_LINK_INAPPLICABLE:
  TRK-CH-002-N2 Q2

TRACKING_LINK_OUT_OF_SCOPE:
  TRK-CH-002-N4

TRACKING_LINK_UNDERDETERMINED:
  TRK-CH-002-N5

ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED:
  yes
```

## 8. Trace-terminal coverage after TRK-CH-001 + TRK-CH-002

```text
TRACKING_TRACE_COMPLETE:
  TRK-CH-001

TRACKING_TRACE_PARTIAL:
  TRK-CH-002-N1

TRACKING_TRACE_BLOCKED:
  TRK-CH-002-N2

TRACKING_TRACE_CONFLICTING:
  TRK-CH-002-N3

TRACKING_TRACE_OUT_OF_SCOPE:
  TRK-CH-002-N4

TRACKING_TRACE_UNDERDETERMINED:
  TRK-CH-002-N5

ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED:
  yes
```

The enum-coverage gap is therefore closed at the constructed internal level.

## 9. Terminal precedence

Frozen protocol precedence:

```text
OUT_OF_SCOPE
-> CONFLICTING
-> UNDERDETERMINED
-> BLOCKED
-> COMPLETE / PARTIAL
```

Execution preserved the intended highest applicable terminal in each subcase.

No run-level terminal erased lower-level link statuses.

## 10. Validity gates

Every subcase satisfied each applicable G1-G14 gate.

Common interpretation:

```text
G1 PASS
  task/scope/dimensions/query/completion records frozen

G2 PASS
  claim-relevant node identity/type/domain records retained

G3 PASS
  relation type/direction/schema-version retained

G4 PASS
  relation state kept separate from supporting/negating evidence

G5 PASS
  established/negated states use supplied applicable evidence only

G6 PASS
  missing/ambiguous/conflicting/blocked/inapplicable/out-of-scope/
  underdetermined distinctions preserved

G7 PASS / NOT_APPLICABLE_WITH_REASON by subcase
  graph topology is preserved where graph structure is present

G8 PASS
  no path reachability promoted to direct link

G9 PASS
  relation families remain typed; custody applicability uses frozen schema

G10 NOT_APPLICABLE_WITH_REASON
  no Aggregation/Compression reduction claim is used

G11 PASS
  no neighboring method is silently executed

G12 PASS
  no reconstructed/inferred link is promoted to established trace

G13 PASS
  each trace terminal follows the frozen completion/precedence rule

G14 PASS
  conformance, gain status, and maximum claim emitted
```

Overall:

```text
TRK-CH-002_CONFORMANCE:
  CONFORMANT

TRACKING_METHOD_GAIN_STATUS:
  NOT_ASSESSED

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 11. Cross-subcase guards

All preserved:

```text
EXPLICITLY_NEGATED != MISSING
MISSING != BLOCKED
AMBIGUOUS != CONFLICTING
AMBIGUOUS != UNDERDETERMINED
CONFLICTING != UNDERDETERMINED
BLOCKED != MISSING
INAPPLICABLE != OUT_OF_SCOPE
OUT_OF_SCOPE != FALSE

CONFORMANT_NEGATIVE_TERMINAL != METHOD_FAILURE
CONFORMANT_NEGATIVE_TERMINAL != METHOD_DELETION_PROOF
CONFORMANT_NEGATIVE_TERMINAL != METHOD_MERGER_PROOF
```

## 12. Frozen scoring

### A. Immutability / common discipline

```text
A1 PASS
A2 PASS
A3 PASS
A4 PASS
A5 PASS
A6 PASS
A7 PASS
A8 PASS

A: 8/8
```

### B. N1 partial / negated / missing / ambiguous

```text
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
B13 PASS
B14 PASS

B: 14/14
```

### C. N2 blocked / inapplicable

```text
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

C: 12/12
```

### D. N3 conflict

```text
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

D: 10/10
```

### E. N4 out-of-scope

```text
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

E: 10/10
```

### F. N5 underdetermination

```text
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

F: 10/10
```

Final:

```text
TOTAL_REQUIRED_CHECKS: 64
PASSED: 64
FAILED: 0
TOTAL: 64/64 PASS
```

## 13. Evidence interpretation

The challenge demonstrates that the frozen protocol can distinguish the nine link statuses and six run-level terminals in the constructed internal fixtures without collapsing them into a generic success/failure state.

```text
SUCCESSFUL_DIRECT_TRACKING_PILOT
  = conformant execution of the frozen challenge

SUCCESSFUL_DIRECT_TRACKING_PILOT
  != POSITIVE_TRACE_TERMINAL
```

No baseline was run.

```text
TRACKING_METHOD_GAIN_STATUS:
  NOT_ASSESSED
```

## 14. Counter update authorized by precommit

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED:
  1 -> 2

SUCCESSFUL_DIRECT_TRACKING_PILOTS:
  1 -> 2

NEGATIVE_OR_FAILURE_TRACKING_CASES:
  0 -> 1

POSITIVE_TRACKING_CASES:
  1

ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED:
  yes
```

Unchanged:

```text
METHOD_BOUNDARY_TRACKING_CASES: 0
BASELINE_TRACKING_CASES: 0
NO_GAIN_TRACKING_CASES: 0
STRONGEST_REASONABLE_BASELINE_TRACKING: not established
REPRODUCIBILITY_CASES: 0

EXTERNAL_TRACKING_APPLICATIONS: 0
INDEPENDENT_TRACKING_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

TRACKING_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_TRACKING_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 15. Maximum supported claim

TRK-CH-002 establishes only direct constructed internal coverage of:

```text
explicitly negated trace relation
missing trace relation
ambiguous target identity
conflicting applicable trace evidence
blocked relation evaluation
inapplicable relation
out-of-scope relation
underdetermined relation semantics

partial
blocked
conflicting
out-of-scope
underdetermined
trace terminals
```

without collapsing these statuses or treating conformant negative/unresolved terminals as method failure.

It does not establish external applicability, truth, authenticity, causality, Lineage identity, legal responsibility, independent validation, comparative gain, or permanent method independence.

## 16. Next

Proceed to a separately precommitted direct method-boundary challenge against neighboring methods under fair shared-artifact access.

The objective is fixture-bounded separation, not permanent method survival.
