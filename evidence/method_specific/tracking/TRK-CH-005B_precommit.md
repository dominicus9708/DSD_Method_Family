# TRK-CH-005B Precommit — Corrected Strongest-Reasonable Non-DSD Tracking Baseline

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-21**  
Case ID: `TRK-CH-005B`  
Case class: `strongest_reasonable_baseline_constructed_corrective`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Corrective lineage

Historical artifacts remain immutable:

```text
TRK-CH-005_PRECOMMIT_COMMIT:
  b410f63882fd311c24033e4527899023474ce7bc

TRK-CH-005_PRECOMMIT_BLOB:
  fc408e2ee33a422964ed1c966d4a2e7edfce421b

TRK-CH-005_RESULT_COMMIT:
  89b7f183c1bb567c1c133221f91feddf9d7e85c9

TRK-CH-005_RESULT_BLOB:
  b98f1ae00e9817d4379793abefe9b2d107d10d19

TRK-CH-005_RESULT:
  68/72
  FAIL_PRECOMMIT_FIXTURE_EXPECTATION
```

This corrective challenge does not rewrite TRK-CH-005.

It corrects only the prospectively identified R1-t1 expectation error.

## 2. Frozen DSD comparator and baseline

```text
TRACKING_PROTOCOL_COMMIT:
  a0d979325c11919fecaa4d8eab129477a365af87

TRACKING_PROTOCOL_BLOB:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

BASELINE_ID:
  B1_STRONG_TYPED_TRACE_ENGINE

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
```

B1 capabilities remain exactly those frozen in TRK-CH-005.

B1 may not be weakened.

## 3. Frozen correction

The original R1-t1 supplied:

```text
REL-v2:
  "USES" means REFERENCES
  and does not establish DEPENDS_ON

required query:
  A DEPENDS_ON L

explicit non-dependency evidence:
  absent

prerequisites:
  available
```

Correct prospectively frozen expectations:

```text
Tracking:
  TRACKING_LINK_MISSING
  TRACKING_TRACE_PARTIAL

B1:
  B1_ABSENT_REQUIRED_LINK
  B1_TRACE_PARTIAL
```

Required guard:

```text
NOT_ESTABLISHED != EXPLICITLY_NEGATED
MISSING_LINK != NEGATIVE_LINK
```

R1-t0 is unchanged:

```text
REL-v1:
  "USES" means DEPENDS_ON

Tracking:
  TRACKING_LINK_ESTABLISHED
  TRACKING_TRACE_COMPLETE

B1:
  B1_PRESENT
  B1_TRACE_COMPLETE
```

## 4. Unchanged strong subcases

The following TRK-CH-005 subcases are reused without semantic change:

```text
R2 branch / merge / cycle / reachability discipline

R3 Reconstruction candidate versus established history
   plus explicit Lineage handoff

R4 temporal location/custody evolution
   without causality/ownership/formation/Lineage promotion

R5 integrated conflict / underdetermination / blockage
   plus Aggregation/Compression loss sidecars
```

All nodes, relations, evidence, sidecars, schema rules, terminal precedence, and maximum-claim limits for R2-R5 remain as frozen in TRK-CH-005.

No post-hoc favorable data is added.

## 5. Equal-information rule

Tracking and B1 receive exactly the same claim-relevant records.

```text
EQUAL_INFORMATION_REQUIRED: yes
HIDDEN_FAVORABLE_INPUT_ALLOWED: no
BASELINE_WEAKENING_ALLOWED: no
```

## 6. Frozen gain axes

The same seven gain axes are reused:

```text
G1 VERSION_AND_SCHEMA_GAIN
G2 GRAPH_TOPOLOGY_GAIN
G3 RECONSTRUCTION_LINEAGE_BOUNDARY_GAIN
G4 TEMPORAL_RELATION_GAIN
G5 LOSS_AND_UNRESOLVED_GAIN
G6 BOUNDED_MAXIMUM_CLAIM_GAIN
G7 TRACEABILITY_GAIN
```

Allowed per-axis result:

```text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
```

Overall rule:

```text
if Tracking is nonconformant or wrong:
  FAIL

if one or more precommitted gain axes show a real DSD advantage
against the still-fair B1 comparator:
  GAIN_ESTABLISHED

if all seven axes are BASELINE_MATCH:
  NO_GAIN

otherwise:
  FAIL or UNRESOLVED
```

## 7. Frozen scoring — 72 checks

### A. Immutable fairness — 10

```text
A1 Tracking protocol identity frozen
A2 B1 identity/capabilities frozen
A3 corrective lineage frozen
A4 only R1-t1 expectation corrected
A5 R2-R5 unchanged
A6 equal information supplied
A7 gain axes frozen
A8 scoring frozen
A9 no external evaluator/application counted
A10 failed TRK-CH-005 artifact preserved
```

### B. R1 version semantics — 10

```text
B1 Tracking R1-t0 established
B2 B1 R1-t0 present
B3 Tracking R1-t1 missing
B4 B1 R1-t1 absent-required-link
B5 Tracking preserves version lock
B6 B1 preserves version lock
B7 Tracking no retroactive schema use
B8 B1 no retroactive schema use
B9 Tracking terminals: t0 COMPLETE / t1 PARTIAL
B10 B1 terminals: t0 COMPLETE / t1 PARTIAL
```

### C. R2 graph topology — 14

```text
C1 Tracking branch retained
C2 B1 branch retained
C3 Tracking merge-shaped inclusion retained
C4 B1 merge-shaped inclusion retained
C5 Tracking reference cycle retained
C6 B1 reference cycle retained
C7 Tracking path reachability retained
C8 B1 path reachability retained
C9 Tracking unsupported direct X REFERENCES Z not created
C10 B1 unsupported direct edge not created
C11 Tracking branch/merge not promoted to Lineage
C12 B1 same no-identity overclaim
C13 Tracking terminal complete
C14 B1 terminal complete
```

### D. R3 Reconstruction / Lineage boundary — 12

```text
D1 Tracking edit link established
D2 B1 edit link present
D3 Tracking direct legacy query missing
D4 B1 equivalent absent-required-link
D5 Tracking RC-1/RC-2 retained as candidates
D6 B1 candidates retained as candidates
D7 Tracking no reconstructed link promoted
D8 B1 no candidate promoted
D9 Tracking explicit LIN-1 handoff retained
D10 B1 explicit identity handoff retained
D11 neither derives Lineage identity from edit continuity
D12 both terminals partial
```

### E. R4 temporal location/custody — 12

```text
E1 Tracking t0 location retained
E2 B1 t0 location retained
E3 Tracking t1 location retained
E4 B1 t1 location retained
E5 Tracking custody changes retained
E6 B1 custody changes retained
E7 neither infers ownership
E8 neither infers responsibility
E9 neither infers causality
E10 neither infers formation change
E11 neither infers Lineage change
E12 both terminals complete
```

### F. R5 integrated unresolved/loss case — 10

```text
F1 Tracking location conflicting
F2 B1 equivalent conflict
F3 Tracking dependency underdetermined
F4 B1 equivalent unresolved schema
F5 Tracking handoff blocked
F6 B1 equivalent blocked
F7 both preserve conflict > underdetermined > blocked terminal precedence
F8 both emit conflict run terminal
F9 both preserve aggregate/compression loss sidecars
F10 neither reconstructs lost support or selects preferred unresolved branch
```

### G. Comparative conclusion — 4

```text
G1 all seven gain axes scored from claim-relevant results
G2 final gain status follows frozen rule
G3 strongest-reasonable status limited to constructed-evidence level
G4 NO_GAIN, if obtained, not interpreted as merger/deletion/absorption evidence
```

```text
TOTAL_REQUIRED_CHECKS: 72
PASS_THRESHOLD: 72/72
PARTIAL_PASS_ALLOWED: no
```

## 8. Counter lock

Canonical counters before this corrective execution remain those from successful TRK-CH-004:

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED: 4
SUCCESSFUL_DIRECT_TRACKING_PILOTS: 4
BASELINE_TRACKING_CASES: 1
NO_GAIN_TRACKING_CASES: 1

STRONGEST_REASONABLE_BASELINE_TRACKING:
  not established

REPRODUCIBILITY_CASES: 0
EXTERNAL_TRACKING_APPLICATIONS: 0
```

TRK-CH-005 did not advance canonical counters because its own precommit authorized changes only on 72/72 PASS.

A `72/72 PASS` here with final `NO_GAIN` authorizes:

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED:
  4 -> 5

SUCCESSFUL_DIRECT_TRACKING_PILOTS:
  4 -> 5

BASELINE_TRACKING_CASES:
  1 -> 2

NO_GAIN_TRACKING_CASES:
  1 -> 2

STRONGEST_REASONABLE_BASELINE_TRACKING:
  established_at_constructed_evidence_level
```

No reproducibility, external validation, or independent replication counter changes.

## 9. Next if passed

Proceed to deterministic same-project retrace using immutable Tracking Protocol v0.1, this corrective precommit, and the resulting strongest-reasonable baseline artifact.

A same-project retrace is not independent replication.
