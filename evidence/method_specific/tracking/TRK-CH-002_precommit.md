# TRK-CH-002 Precommit — Negative / Unresolved Terminal Coverage Challenge

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-21**  
Case ID: `TRK-CH-002`  
Case class: `negative_unresolved_terminal_coverage_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen comparators

```text
PROTOCOL_PATH:
  methods/09_provenance_lineage/provenance/PROTOCOL_v0.1.md

PROTOCOL_COMMIT:
  a0d979325c11919fecaa4d8eab129477a365af87

PROTOCOL_BLOB:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

BOUNDARY_AMENDMENT_COMMIT:
  086c537b1312838500f6d188f32e7c643bde990b

BOUNDARY_AMENDMENT_BLOB:
  846a195f1e18c1fd1b9824638d98e10fc837f10e
```

The frozen protocol and amendment may not be edited in response to this challenge.

## 2. Purpose

Exercise every remaining Tracking link status not directly exercised by TRK-CH-001:

```text
TRACKING_LINK_EXPLICITLY_NEGATED
TRACKING_LINK_MISSING
TRACKING_LINK_AMBIGUOUS
TRACKING_LINK_CONFLICTING
TRACKING_LINK_BLOCKED
TRACKING_LINK_INAPPLICABLE
TRACKING_LINK_OUT_OF_SCOPE
TRACKING_LINK_UNDERDETERMINED
```

TRK-CH-001 already directly exercised:

```text
TRACKING_LINK_ESTABLISHED
```

The challenge also directly exercises every non-COMPLETE trace terminal:

```text
N1 -> TRACKING_TRACE_PARTIAL
N2 -> TRACKING_TRACE_BLOCKED
N3 -> TRACKING_TRACE_CONFLICTING
N4 -> TRACKING_TRACE_OUT_OF_SCOPE
N5 -> TRACKING_TRACE_UNDERDETERMINED
```

Together with TRK-CH-001:

```text
TRACKING_TRACE_COMPLETE
```

all six trace terminals will have direct constructed execution if and only if every frozen subcase executes as specified.

A conformant negative or unresolved terminal counts as successful protocol execution.

```text
CONFORMANT_NEGATIVE_TERMINAL != METHOD_FAILURE
```

## 3. Common locks

Every subcase uses:

```text
RELATION_SCHEMA_FAMILY:
  TRK-NEG-v1 unless otherwise stated

EXTERNAL_APPLICATION:
  no

AUTHENTICITY_CLAIM:
  not requested

TRUTH_CLAIM:
  not requested

CAUSAL_CLAIM:
  not requested

LINEAGE_IDENTITY_CLAIM:
  not requested

AUDIT_VERDICT:
  not requested
```

No hidden link may be reconstructed.

No ambiguous/conflicting/underdetermined branch may be selected post hoc.

## 4. N1 — partial trace with explicit negation, missing link, and ambiguous identity

Task:

```text
TASK_ID:
  TRK-CH-002-N1

TARGET:
  PACKAGE_P

DECLARED_TRACE_SCOPE:
  bounded workflow P1

TRACE_DIMENSIONS:
  source
  reference
  location

REQUIRED_QUERY_SET:
  Q1, Q2, Q3, Q4

COMPLETION_RULE:
  all Q1-Q4 must be ESTABLISHED or EXPLICITLY_NEGATED
  for COMPLETE.
```

Frozen nodes:

```text
S = SOURCE_S
P = PACKAGE_P
R1 = REF_ALPHA_ID_1
R2 = REF_ALPHA_ID_2
L = LOCATION_L
```

Q1:

```text
SOURCE_S SOURCE_OF PACKAGE_P

evidence E1:
  applicable
  supports relation

expected:
  TRACKING_LINK_ESTABLISHED
```

Q2:

```text
PACKAGE_P REFERENCES REF_FORBIDDEN

evidence E2:
  applicable
  explicitly states PACKAGE_P does not reference REF_FORBIDDEN
  under schema TRK-NEG-v1

expected:
  TRACKING_LINK_EXPLICITLY_NEGATED
```

Q3:

```text
PACKAGE_P STORED_IN LOCATION_L

supporting record:
  absent

explicit negation:
  absent

prerequisite/schema/access:
  available

expected:
  TRACKING_LINK_MISSING
```

Q4:

```text
PACKAGE_P REFERENCES "REF_ALPHA"

supplied reference record:
  target display label = REF_ALPHA

node register:
  R1 display label = REF_ALPHA
  R2 display label = REF_ALPHA

no unique target identifier:
  supplied

expected:
  TRACKING_LINK_AMBIGUOUS
```

No rule permits choosing R1 or R2.

Expected terminal:

```text
TRACKING_TRACE_PARTIAL
```

Reason:

```text
Q1 and Q2 are resolved.
Q3 and Q4 remain unresolved.
No OUT_OF_SCOPE / CONFLICTING / UNDERDETERMINED / BLOCKED condition dominates.
```

Required guards:

```text
EXPLICITLY_NEGATED != MISSING
MISSING != BLOCKED
AMBIGUOUS != UNDERDETERMINED
AMBIGUOUS != LICENSE_TO_CHOOSE_POST_HOC
PARTIAL != COMPLETE
```

## 5. N2 — blocked trace with separate inapplicable relation

Task:

```text
TASK_ID:
  TRK-CH-002-N2

TARGET:
  ARTIFACT_A

TRACE_DIMENSIONS:
  transformation
  custody

REQUIRED_QUERY_SET:
  Q1, Q2
```

Q1:

```text
ARTIFACT_A TRANSFORMATION_HANDOFF_TO ARTIFACT_B

source record:
  encrypted handoff envelope exists

required decoder/schema map:
  explicitly unavailable

relation evidence cannot be evaluated without decoder.

expected:
  TRACKING_LINK_BLOCKED
```

Q2:

```text
ARTIFACT_A CUSTODY_HELD_BY CONTAINER_C

node type of CONTAINER_C:
  non-actor storage container

relation schema:
  CUSTODY_HELD_BY requires actor/custodian target

expected:
  TRACKING_LINK_INAPPLICABLE
```

No other required query resolves the trace.

Expected terminal:

```text
TRACKING_TRACE_BLOCKED
```

Required guards:

```text
BLOCKED != MISSING
BLOCKED != NEGATED
INAPPLICABLE != NEGATED
INAPPLICABLE != OUT_OF_SCOPE
BLOCKED_TRACE != METHOD_FAILURE
```

## 6. N3 — conflicting trace

Task:

```text
TASK_ID:
  TRK-CH-002-N3

TARGET:
  ARTIFACT_C

TRACE_DIMENSION:
  location

REQUIRED_QUERY:
  ARTIFACT_C STORED_IN ? at frozen snapshot T0

RELATION_SCHEMA:
  LOCATION-v1
```

Applicable evidence records:

```text
E31:
  ARTIFACT_C STORED_IN LOCATION_X at T0

E32:
  ARTIFACT_C STORED_IN LOCATION_Y at T0

schema constraint:
  exactly one exclusive storage location at T0

LOCATION_X != LOCATION_Y

precedence:
  none
```

Expected relation status:

```text
TRACKING_LINK_CONFLICTING
```

Expected terminal:

```text
TRACKING_TRACE_CONFLICTING
```

Required guards:

```text
CONFLICTING != AMBIGUOUS
CONFLICTING != UNDERDETERMINED
CONFLICTING_LINKS != LICENSE_TO_DISCARD_ONE
CONFLICTING_TRACE != METHOD_FAILURE
```

## 7. N4 — out-of-scope trace request

Task:

```text
TASK_ID:
  TRK-CH-002-N4

TARGET:
  ARTIFACT_D

DECLARED_TRACE_DIMENSIONS:
  {origin/source, version}

requested required query:
  ARTIFACT_D OWNED_BY ACTOR_Z

ownership dimension:
  not included in frozen task dimensions

scope extension:
  not declared
```

Expected relation status:

```text
TRACKING_LINK_OUT_OF_SCOPE
```

Expected terminal:

```text
TRACKING_TRACE_OUT_OF_SCOPE
```

Required guards:

```text
OUT_OF_SCOPE != INAPPLICABLE
OUT_OF_SCOPE != MISSING
OUT_OF_SCOPE != FALSE
NO_SCOPE_EXTENSION != NEGATIVE_RELATION
```

No ownership relation is fabricated.

## 8. N5 — underdetermined relation schema

Task:

```text
TASK_ID:
  TRK-CH-002-N5

TARGET:
  ARTIFACT_E

TRACE_DIMENSION:
  dependency

REQUIRED_QUERY:
  ARTIFACT_E DEPENDS_ON LIB_Q

candidate evidence:
  one frozen dependency record DQ-1

two relation-schema versions:
  both fully supplied
  both declared admissible
  no precedence
```

Schema `DEP-v1`:

```text
DQ-1 means:
  ARTIFACT_E DEPENDS_ON LIB_Q

=> TRACKING_LINK_ESTABLISHED
```

Schema `DEP-v2`:

```text
DQ-1 means:
  ARTIFACT_E merely references LIB_Q metadata
  no DEPENDS_ON relation

=> TRACKING_LINK_EXPLICITLY_NEGATED
   for the frozen dependency query
```

Both schemas are applicable and claim-relevant.

Nothing is missing.

Expected relation status:

```text
TRACKING_LINK_UNDERDETERMINED
```

Expected terminal:

```text
TRACKING_TRACE_UNDERDETERMINED
```

Required guards:

```text
MULTIPLE_ADMISSIBLE_SCHEMAS != MISSING_SCHEMA
UNDERDETERMINED != CONFLICTING
UNDERDETERMINED != BLOCKED
UNDERDETERMINED != LICENSE_TO_CHOOSE_POST_HOC
```

The underdetermination is over relation semantics, not over node identity.

## 9. Terminal precedence check

The frozen protocol terminal precedence is:

```text
OUT_OF_SCOPE
-> CONFLICTING
-> UNDERDETERMINED
-> BLOCKED
-> COMPLETE / PARTIAL
```

Each subcase is constructed so that its expected terminal is the highest applicable terminal for that subcase.

No lower-level link status is erased by the run-level terminal.

## 10. Coverage target after TRK-CH-001 + TRK-CH-002

If this challenge passes exactly:

```text
TRACKING_LINK_ESTABLISHED
  -> TRK-CH-001

TRACKING_LINK_EXPLICITLY_NEGATED
  -> TRK-CH-002-N1 Q2

TRACKING_LINK_MISSING
  -> TRK-CH-002-N1 Q3

TRACKING_LINK_AMBIGUOUS
  -> TRK-CH-002-N1 Q4

TRACKING_LINK_CONFLICTING
  -> TRK-CH-002-N3

TRACKING_LINK_BLOCKED
  -> TRK-CH-002-N2 Q1

TRACKING_LINK_INAPPLICABLE
  -> TRK-CH-002-N2 Q2

TRACKING_LINK_OUT_OF_SCOPE
  -> TRK-CH-002-N4

TRACKING_LINK_UNDERDETERMINED
  -> TRK-CH-002-N5

ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED:
  yes
```

and:

```text
TRACKING_TRACE_COMPLETE
  -> TRK-CH-001

TRACKING_TRACE_PARTIAL
  -> TRK-CH-002-N1

TRACKING_TRACE_BLOCKED
  -> TRK-CH-002-N2

TRACKING_TRACE_CONFLICTING
  -> TRK-CH-002-N3

TRACKING_TRACE_OUT_OF_SCOPE
  -> TRK-CH-002-N4

TRACKING_TRACE_UNDERDETERMINED
  -> TRK-CH-002-N5

ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED:
  yes
```

## 11. Validity-gate policy

Each subcase must satisfy every applicable G1-G14 gate.

Allowed non-PASS value:

```text
NOT_APPLICABLE_WITH_REASON
```

A negative/unresolved link or terminal is not itself a validity-gate failure.

No subcase uses Aggregation/Compression reduction; G10 may be marked `NOT_APPLICABLE_WITH_REASON`.

No reconstructed link is supplied; G12 must still preserve the no-promotion rule.

## 12. Cross-subcase guards

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

## 13. Frozen scoring — 64 checks

### A. Immutability / common discipline — 8

```text
A1 protocol commit/blob fixed
A2 amendment commit/blob fixed
A3 five subcases frozen before execution
A4 no external application
A5 no protocol edit after precommit
A6 no hidden Reconstruction step
A7 no post-hoc precedence/schema choice
A8 method gain remains NOT_ASSESSED
```

### B. N1 partial / negated / missing / ambiguous — 14

```text
B1 task/scope/dimensions/query set fixed
B2 Q1 established
B3 Q2 has explicit applicable negation evidence
B4 Q2 = EXPLICITLY_NEGATED
B5 Q2 not relabeled MISSING
B6 Q3 support absent
B7 Q3 explicit negation absent
B8 Q3 prerequisites available
B9 Q3 = MISSING
B10 Q3 not relabeled BLOCKED
B11 Q4 duplicate display-label identities retained
B12 Q4 = AMBIGUOUS
B13 no R1/R2 target chosen post hoc
B14 terminal = TRACE_PARTIAL
```

### C. N2 blocked / inapplicable — 12

```text
C1 task/query set fixed
C2 Q1 encrypted handoff exists
C3 Q1 required decoder unavailable
C4 Q1 = BLOCKED
C5 Q1 not relabeled MISSING
C6 Q2 target node type fixed as non-actor container
C7 custody schema requires actor/custodian
C8 Q2 = INAPPLICABLE
C9 Q2 not relabeled NEGATED
C10 terminal = TRACE_BLOCKED
C11 blocked terminal not called method failure
C12 conformance preserved
```

### D. N3 conflict — 10

```text
D1 frozen T0 snapshot retained
D2 E31 applicable
D3 E32 applicable
D4 exclusive-location schema retained
D5 LOCATION_X != LOCATION_Y
D6 no precedence supplied
D7 relation = CONFLICTING
D8 no evidence branch discarded
D9 terminal = TRACE_CONFLICTING
D10 conformance preserved
```

### E. N4 out-of-scope — 10

```text
E1 task dimensions fixed to source/version
E2 ownership query fixed
E3 ownership dimension absent from task dimensions
E4 no scope extension supplied
E5 relation = OUT_OF_SCOPE
E6 not relabeled INAPPLICABLE
E7 not relabeled MISSING
E8 no ownership relation fabricated
E9 terminal = TRACE_OUT_OF_SCOPE
E10 conformance preserved
```

### F. N5 underdetermination — 10

```text
F1 dependency query fixed
F2 DQ-1 supplied
F3 DEP-v1 supplied/applicable
F4 DEP-v2 supplied/applicable
F5 v1 yields ESTABLISHED
F6 v2 yields EXPLICITLY_NEGATED
F7 no precedence supplied
F8 relation = UNDERDETERMINED
F9 terminal = TRACE_UNDERDETERMINED
F10 no post-hoc schema choice / conformance preserved
```

```text
TOTAL_REQUIRED_CHECKS: 64
PASS_THRESHOLD: 64/64
PARTIAL_PASS_ALLOWED: no
```

Any mismatch must remain visible.

## 14. Allowed counter changes on 64/64 PASS

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED:
  1 -> 2

SUCCESSFUL_DIRECT_TRACKING_PILOTS:
  1 -> 2

NEGATIVE_OR_FAILURE_TRACKING_CASES:
  0 -> 1
```

Here `SUCCESSFUL_DIRECT_TRACKING_PILOT` means conformant execution against the frozen challenge.

It does not mean a positive trace terminal.

If all frozen statuses/terminals are produced exactly, record:

```text
ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED: yes
```

Unchanged:

```text
POSITIVE_TRACKING_CASES: 1
METHOD_BOUNDARY_TRACKING_CASES: 0
BASELINE_TRACKING_CASES: 0
NO_GAIN_TRACKING_CASES: 0
STRONGEST_REASONABLE_BASELINE_TRACKING: not established
REPRODUCIBILITY_CASES: 0

EXTERNAL_TRACKING_APPLICATIONS: 0
INDEPENDENT_TRACKING_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

TRACKING_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_TRACKING_EVIDENCE_STATUS: validation_in_progress

PROTOCOL_REVISION_REQUIRED: no unless contradiction found
SHARED_CORE_REOPEN_REQUIRED: no unless contradiction found
```
