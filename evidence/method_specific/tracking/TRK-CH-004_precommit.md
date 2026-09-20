# TRK-CH-004 Precommit — Competent Non-DSD Tracking Baseline Comparison

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-21**  
Case ID: `TRK-CH-004`  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

```text
TRACKING_PROTOCOL_COMMIT:
  a0d979325c11919fecaa4d8eab129477a365af87

TRACKING_PROTOCOL_BLOB:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

TRACKING_PROTOCOL_VERSION:
  v0.1
```

No DSD protocol revision is allowed in response to the baseline result.

## 2. Baseline identity

```text
BASELINE_ID:
  B0_GENERIC_TYPED_TRACE_LEDGER

BASELINE_CLASS:
  competent_non_DSD_constructed_trace_evaluator

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
```

B0 is intentionally competent rather than weak.

It may use ordinary directed-graph records, stable node identifiers, typed edge labels, explicit evidence references, finite query lists, explicit status flags, and deterministic completion rules.

It does not invoke Formation, Property, Static Aggregation, Dynamics, or the DSD shared core as theory.

## 3. B0 generic operation

B0 performs:

```text
B0-1 lock target, bounded scope, requested relation dimensions, query set,
     and completion rule

B0-2 retain supplied node IDs, versions, types, domains, and labels separately

B0-3 register supplied directed relation records by relation type

B0-4 keep relation records separate from evidence/provenance records

B0-5 mark a supplied relation as PRESENT when applicable evidence supports it

B0-6 mark an explicit non-relation record as EXPLICIT_NEGATIVE

B0-7 mark a required in-scope query with neither support nor explicit negation
     as ABSENT_REQUIRED_LINK when prerequisites are otherwise available

B0-8 retain duplicate-label target ambiguity without choosing a node

B0-9 retain incompatible applicable records as CONFLICT

B0-10 retain an unavailable required decoder/schema/access prerequisite as BLOCKED

B0-11 retain relation-type/domain mismatch as NOT_APPLICABLE

B0-12 retain a requested relation outside frozen scope as OUTSIDE_SCOPE

B0-13 retain multiple admissible relation semantics with no precedence
      as UNRESOLVED_SCHEMA

B0-14 build the directed graph without forcing a linear chain

B0-15 distinguish direct edges from path reachability

B0-16 retain supplied handoff/loss/reconstruction-warning sidecars
      without converting them into stronger claims

B0-17 summarize the finite query set as COMPLETE / PARTIAL / BLOCKED /
      CONFLICT / OUTSIDE_SCOPE / UNRESOLVED

B0-18 emit a bounded result statement and do not infer truth, authenticity,
      causality, ownership, responsibility, successor identity,
      reconstruction truth, or audit success
```

B0 is generic trace bookkeeping.

Vocabulary differences alone do not count as DSD gain.

## 4. Frozen comparison mapping

Link-level comparison mapping:

```text
B0_PRESENT
  <-> TRACKING_LINK_ESTABLISHED

B0_EXPLICIT_NEGATIVE
  <-> TRACKING_LINK_EXPLICITLY_NEGATED

B0_ABSENT_REQUIRED_LINK
  <-> TRACKING_LINK_MISSING

B0_AMBIGUOUS
  <-> TRACKING_LINK_AMBIGUOUS

B0_CONFLICT
  <-> TRACKING_LINK_CONFLICTING

B0_BLOCKED
  <-> TRACKING_LINK_BLOCKED

B0_NOT_APPLICABLE
  <-> TRACKING_LINK_INAPPLICABLE

B0_OUTSIDE_SCOPE
  <-> TRACKING_LINK_OUT_OF_SCOPE

B0_UNRESOLVED_SCHEMA
  <-> TRACKING_LINK_UNDERDETERMINED
```

Trace-level mapping:

```text
B0_TRACE_COMPLETE
  <-> TRACKING_TRACE_COMPLETE

B0_TRACE_PARTIAL
  <-> TRACKING_TRACE_PARTIAL

B0_TRACE_BLOCKED
  <-> TRACKING_TRACE_BLOCKED

B0_TRACE_CONFLICT
  <-> TRACKING_TRACE_CONFLICTING

B0_TRACE_OUTSIDE_SCOPE
  <-> TRACKING_TRACE_OUT_OF_SCOPE

B0_TRACE_UNRESOLVED
  <-> TRACKING_TRACE_UNDERDETERMINED
```

## 5. Equal-information rule

For every fixture, Tracking and B0 receive the same claim-relevant:

```text
task target
scope
trace dimensions
query set
completion rule
node IDs / versions / types / domains
relation types and directions
relation-schema records
evidence records and provenance
explicit support / explicit negation / absence flags
prerequisite/decoder/access availability
graph topology
location/container/custody records
method-handoff records
collision/loss/reconstruction-warning sidecars
precedence or explicit absence of precedence
```

Neither side receives hidden favorable information.

## 6. Frozen fixtures

### Q1 — positive multidimensional trace

Use the claim-relevant semantics of TRK-CH-001.

Required direct relations include:

```text
SRC_MASTER SOURCE_OF DOC_DRAFT_V1
DOC_DRAFT_V1 EDITED_TO DOC_DRAFT_V2
DOC_DRAFT_V2 TRANSFORMATION_HANDOFF_TO PDF_EXPORT
PDF_EXPORT COPIED_TO COPY_A
PDF_EXPORT COPIED_TO COPY_B
COPY_A INCLUDED_IN PKG_FINAL
REF_TABLE INCLUDED_IN PKG_FINAL
PKG_FINAL DEPENDS_ON COPY_A
PKG_FINAL DEPENDS_ON REF_TABLE
PDF_EXPORT STORED_IN REPO_MAIN
COPY_B STORED_IN ARCHIVE_BOX
PDF_EXPORT CUSTODY_HELD_BY OPERATOR_A
```

Supplementary records preserve process-order and reference-path edges.

Expected Tracking:

```text
all required links ESTABLISHED
branching retained
many-source inclusion retained
dependency distinct from inclusion
two-edge reference reachability retained
unsupported direct reference edge not created
custody not upgraded to ownership/responsibility
Transformation handoff not upgraded to transformation correctness
terminal = TRACKING_TRACE_COMPLETE
```

Expected B0:

```text
all required links B0_PRESENT
same graph topology retained
same direct-edge/path distinction retained
same bounded no-overclaim discipline
terminal = B0_TRACE_COMPLETE
```

### Q2 — explicit negative + missing + ambiguity

Use TRK-CH-002 N1 semantics:

```text
Q1 supported source relation
Q2 explicit applicable non-reference record
Q3 no support / no explicit negation / prerequisites available
Q4 duplicate display label REF_ALPHA maps to two node IDs
```

Expected:

```text
Tracking:
  ESTABLISHED
  EXPLICITLY_NEGATED
  MISSING
  AMBIGUOUS
  -> TRACE_PARTIAL

B0:
  PRESENT
  EXPLICIT_NEGATIVE
  ABSENT_REQUIRED_LINK
  AMBIGUOUS
  -> B0_TRACE_PARTIAL
```

### Q3 — blocked + inapplicable

Use TRK-CH-002 N2 semantics:

```text
transformation envelope supplied
required decoder unavailable

custody query targets a non-actor storage container
while custody schema requires actor/custodian
```

Expected:

```text
Tracking:
  BLOCKED + INAPPLICABLE
  -> TRACE_BLOCKED

B0:
  BLOCKED + NOT_APPLICABLE
  -> B0_TRACE_BLOCKED
```

### Q4 — conflicting applicable evidence

Use TRK-CH-002 N3 semantics:

```text
ARTIFACT_C STORED_IN LOCATION_X at T0
ARTIFACT_C STORED_IN LOCATION_Y at T0
exactly-one-location schema
no precedence
```

Expected:

```text
Tracking:
  LINK_CONFLICTING
  -> TRACE_CONFLICTING

B0:
  B0_CONFLICT
  -> B0_TRACE_CONFLICT
```

Neither side may discard one applicable record.

### Q5 — outside-scope and underdetermined semantics

Two independent subfixtures:

#### Q5A — outside scope

```text
frozen trace dimensions:
  source/version

requested query:
  ownership relation

scope extension:
  absent
```

Expected:

```text
Tracking:
  LINK_OUT_OF_SCOPE
  -> TRACE_OUT_OF_SCOPE

B0:
  B0_OUTSIDE_SCOPE
  -> B0_TRACE_OUTSIDE_SCOPE
```

#### Q5B — underdetermined schema

```text
one frozen dependency record DQ-1

DEP-v1:
  DQ-1 means DEPENDS_ON

DEP-v2:
  DQ-1 means metadata-reference-only,
  so dependency query is explicitly negative

both admissible
no precedence
```

Expected:

```text
Tracking:
  LINK_UNDERDETERMINED
  -> TRACE_UNDERDETERMINED

B0:
  B0_UNRESOLVED_SCHEMA
  -> B0_TRACE_UNRESOLVED
```

## 7. Frozen gain axes

```text
G1 typed trace-link classification advantage
G2 graph topology / direct-edge discipline advantage
G3 evidence-versus-relation provenance advantage
G4 gap / ambiguity / conflict / blockage semantic advantage
G5 scope / schema / terminal discipline advantage
G6 overclaim-boundary advantage
```

Allowed axis result:

```text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
```

Overall gain rule:

```text
if all claim-relevant outputs match:
  TRACKING_METHOD_GAIN_STATUS = NO_GAIN

if one or more precommitted claim-relevant axes show a DSD advantage:
  TRACKING_METHOD_GAIN_STATUS = GAIN_ESTABLISHED

otherwise:
  TRACKING_METHOD_GAIN_STATUS = NOT_ASSESSED
```

No wording or label difference counts as gain.

## 8. Frozen scoring — 64 checks

### A. Fairness and immutability — 10

```text
A1 Tracking protocol commit/blob fixed
A2 B0 operation fixed before execution
A3 output mapping fixed
A4 Q1-Q5B fixed before execution
A5 equal-information rule respected
A6 B0 not denied any Tracking-visible claim-relevant information
A7 Tracking receives no hidden favorable information
A8 no post-hoc gain axis added
A9 no baseline rule changed after result inspection
A10 external application remains no
```

### B. Q1 positive multidimensional trace — 16

```text
B1 Tracking required links established
B2 B0 equivalent required links present
B3 Tracking branch retained
B4 B0 branch retained
B5 Tracking many-source inclusion retained
B6 B0 many-source inclusion retained
B7 Tracking dependency/inclusion relation types distinct
B8 B0 same distinction retained
B9 Tracking reference path retained without unsupported direct edge
B10 B0 same direct-edge discipline retained
B11 Tracking custody not upgraded to ownership/responsibility
B12 B0 same no-overclaim discipline
B13 Tracking Transformation handoff not upgraded to correctness
B14 B0 same no-overclaim discipline
B15 Tracking terminal COMPLETE
B16 B0 terminal COMPLETE
```

### C. Q2 negative/missing/ambiguous — 12

```text
C1 Tracking explicit negative retained
C2 B0 explicit negative retained
C3 Tracking explicit negative not relabeled missing
C4 B0 explicit negative not relabeled absence
C5 Tracking missing retained
C6 B0 absent-required-link retained
C7 Tracking missing not relabeled blocked
C8 B0 absence not relabeled blocked
C9 Tracking duplicate-label ambiguity retained
C10 B0 duplicate-label ambiguity retained
C11 Tracking terminal PARTIAL
C12 B0 terminal PARTIAL
```

### D. Q3 blocked/inapplicable — 10

```text
D1 Tracking decoder absence explicit
D2 B0 decoder absence explicit
D3 Tracking relation BLOCKED
D4 B0 relation BLOCKED
D5 Tracking custody query INAPPLICABLE
D6 B0 custody query NOT_APPLICABLE
D7 neither side converts blocked to missing
D8 neither side converts inapplicable to explicit negative
D9 Tracking terminal BLOCKED
D10 B0 terminal BLOCKED
```

### E. Q4 conflict — 8

```text
E1 both applicable location records preserved by Tracking
E2 both preserved by B0
E3 exactly-one-location schema retained by Tracking
E4 same retained by B0
E5 Tracking relation CONFLICTING
E6 B0 relation CONFLICT
E7 neither side discards a record
E8 both emit conflict trace terminal
```

### F. Q5 scope + underdetermination — 6

```text
F1 Tracking Q5A out-of-scope
F2 B0 Q5A outside-scope
F3 both emit corresponding outside-scope terminal
F4 Tracking Q5B underdetermined
F5 B0 Q5B unresolved-schema
F6 both emit corresponding underdetermined/unresolved terminal
```

### G. Gain conclusion — 2

```text
G1 six frozen gain axes scored from claim-relevant outputs only
G2 NO_GAIN preserved if all six axes are BASELINE_MATCH,
   without merger/deletion conclusion
```

```text
TOTAL_REQUIRED_CHECKS: 64
PASS_THRESHOLD: 64/64
PARTIAL_PASS_ALLOWED: no
```

Any mismatch remains visible.

## 9. Allowed counter changes on 64/64 PASS

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED:
  3 -> 4

SUCCESSFUL_DIRECT_TRACKING_PILOTS:
  3 -> 4

BASELINE_TRACKING_CASES:
  0 -> 1
```

If all six gain axes are `BASELINE_MATCH`:

```text
NO_GAIN_TRACKING_CASES:
  0 -> 1

TRACKING_METHOD_GAIN_STATUS:
  NO_GAIN
```

Unchanged:

```text
POSITIVE_TRACKING_CASES: 1
NEGATIVE_OR_FAILURE_TRACKING_CASES: 1
METHOD_BOUNDARY_TRACKING_CASES: 1

ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED: yes

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

`NO_GAIN` is not evidence for deleting, merging, or absorbing Tracking.
