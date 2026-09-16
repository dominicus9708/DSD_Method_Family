# TRN-CH-004 — Competent-Baseline NO_GAIN Transformation Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-16**  
Case ID: `TRN-CH-004`  
Case class: `competent_baseline_no_gain_challenge`  
Case origin: `constructed_same_project`  
Evidence scope class: `method_specific`  
Protocol: **Transformation Protocol v0.1**  
Protocol blob: `f78393c188c513acb30a10f1b180d598138cea61`  
Baseline: `B0_SCHEMA_MAP_LEDGER_EVALUATOR`

## 1. Purpose

Compare DSD Transformation with a competent non-DSD transformation evaluator that receives exactly the same claim-relevant source, target, map, domain, carrier-status, preservation/loss, target-addition, reconstruction, and terminal-state information.

A fair `NO_GAIN` result is explicitly admissible.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_REDUNDANCY
```

This is the first competent-baseline case for Transformation. It is not the strongest-reasonable-baseline test; that remains a later separately frozen case.

No external source, standard, benchmark, corpus, or evaluator is used.

## 2. Frozen common task family

Five constructed subcases are frozen:

```text
Q1 preserving map with declared equivalence, DEFINED_ZERO, and target-only default
Q2 declared many-to-one loss plus explicit omission
Q3 missing required unit bridge requiring blockage
Q4 mixed batch applicability requiring partial terminal
Q5 unresolved claim-relevant map version requiring underdetermination
```

Both DSD Transformation and B0 receive identical task records and may legitimately produce identical results.

## 3. Q1 — preserving map with status/default discipline

Frozen source:

```text
SOURCE_OBJECT_ID: SRC-Q1
SOURCE_SCHEMA: S_Q1 1.0
TARGET_SCHEMA: T_Q1 1.0
MAP: MAP_Q1 1.0

record_id = "A-09" / DEFINED_NONZERO
mass_g = 250 / DEFINED_NONZERO
retry_count = 0 / DEFINED_ZERO
```

Frozen map:

```text
record_id -> record_id / ONE_TO_ONE / exact
mass_g -> mass_kg = mass_g / 1000 / ONE_TO_ONE / declared equivalence
retry_count -> retry_count / ONE_TO_ONE / exact
schema_tag -> target-only default "T_Q1" / TARGET_ADDED / DEFAULT_VALUE
```

Expected DSD and B0:

```text
record_id -> PRESERVED_EXACT
mass_g -> PRESERVED_UNDER_DECLARED_EQUIVALENCE
retry_count -> PRESERVED_EXACT / DEFINED_ZERO preserved
schema_tag -> TARGET_ADDED_NOT_SOURCE_DERIVED / DEFAULT_VALUE
TERMINAL -> TRANSFORMATION_COMPLETED_PRESERVING
```

Reconstruction of all claim-relevant source carriers must be available at declared scope. No global bijectivity claim is permitted.

## 4. Q2 — declared many-to-one loss and omission

Frozen source:

```text
SOURCE_OBJECT_ID: SRC-Q2
SOURCE_SCHEMA: S_Q2 1.0
TARGET_SCHEMA: T_Q2 1.0
MAP: MAP_Q2 1.0

x = 4
y = 9
note = "keep-source-only"
```

Frozen map:

```text
{x,y} -> total = x + y = 13 / MANY_TO_ONE_MERGE
note -> OMITTED
```

Expected DSD and B0:

```text
{x,y} -> MERGED_IN_TARGET
note -> OMITTED_BY_TRANSFORMATION
ordered pair (x,y) not uniquely reconstructible from total alone
REVERSIBILITY -> NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
TERMINAL -> TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
```

Forbidden:

```text
MANY_TO_ONE_MERGE -> PRESERVED_EXACT
OMITTED_BY_TRANSFORMATION -> MISSING_SOURCE_VALUE
FORWARD_SUCCESS -> REVERSIBLE
```

## 5. Q3 — missing required unit bridge

Frozen source/task:

```text
SOURCE_OBJECT_ID: SRC-Q3
SOURCE_SCHEMA: S_ANGLE 1.0
TARGET_SCHEMA: T_RAD 1.0
MAP: MAP_ANGLE_RAD 1.0

angle_value = 90
angle_unit = MISSING
```

Map requires an explicit source-unit bridge before conversion to radians. No default unit is allowed.

Expected DSD and B0:

```text
no target radian value emitted
required unit bridge -> missing
TERMINAL -> TRANSFORMATION_BLOCKED
CONFORMANCE/CORRECTNESS -> valid handling of supplied-task deficiency
```

Forbidden: silently assuming degrees.

## 6. Q4 — partial batch applicability

Frozen map domain:

```text
MAP_SCORE 1.0 accepts integer scores 0..10 inclusive
```

Frozen batch:

```text
R1.score = 5      -> inside domain
R2.score = 14     -> outside domain
```

Expected DSD and B0:

```text
R1 transformed
R2 not transformed and recorded OUTSIDE_DECLARED_DOMAIN
R2 is not OMITTED_BY_TRANSFORMATION
TERMINAL -> TRANSFORMATION_PARTIAL
```

No clipping `14 -> 10`, normalization, or domain extension is permitted.

## 7. Q5 — unresolved map-version identity

Frozen task:

```text
SOURCE_OBJECT_ID: SRC-Q5
SOURCE_SCHEMA: S_ID 1.0
TARGET_SCHEMA: T_ID 1.0
MAP_FAMILY: MAP_ID_RENDER
ALLOWED_VERSIONS: {1.0, 2.0}
SELECTED_MAP_VERSION: unresolved
identifier = "007"
```

Claim-relevant version difference:

```text
MAP_ID_RENDER 1.0 -> target text "007"
MAP_ID_RENDER 2.0 -> target text "7"
```

No precedence/default/latest-version rule is supplied.

Expected DSD and B0:

```text
no unique target identifier emitted
no version selected post hoc
TERMINAL -> TRANSFORMATION_UNDERDETERMINED
```

## 8. Competent baseline freeze

Baseline identity:

```text
B0_SCHEMA_MAP_LEDGER_EVALUATOR
```

B0 receives exactly the same:

```text
source object/record identities
source and target schemas/versions
transformation-map identities/versions
map domain/codomain/applicability records
claim-relevant source carriers and source statuses
declared equivalence/tolerance rules
carrier relation rules
target default/addition provenance
loss/merge/omission rules
reconstruction/inverse claims and scope
terminal-status decision rules required by Q1-Q5
```

B0 is explicitly competent to:

```text
1 keep source and target identities distinct;
2 preserve MISSING, DEFINED_ZERO, and defined-nonzero distinctions when supplied;
3 distinguish exact preservation from declared-equivalence preservation;
4 record merge, omission, and target-only additions separately;
5 detect many-to-one loss and reject unsupported injectivity/reversibility claims;
6 block execution when a required bridge is missing rather than inventing a default;
7 check map applicability before execution and retain out-of-domain records as such;
8 withhold a unique target when a claim-relevant map version is unresolved;
9 retain enough map/carrier/loss/reconstruction trace to retrace every verdict.
```

B0 does not need DSD terminology internally. For scoring, its outputs are mapped one-to-one to the frozen Transformation statuses above.

B0 may not be weakened after this precommit.

## 9. Frozen gain criteria

```text
G1 STATUS_DISTINCTION_GAIN
  established only if DSD preserves a claim-relevant missing/zero/defined distinction that B0 loses.

G2 CARRIER_RELATION_AND_LOSS_GAIN
  established only if DSD preserves merge/omission/preservation semantics more correctly than B0.

G3 TARGET_ADDITION_PROVENANCE_GAIN
  established only if DSD preserves target-only/default provenance more correctly than B0.

G4 RECONSTRUCTION_REVERSIBILITY_GAIN
  established only if DSD bounds injectivity/reconstruction/reversibility claims more correctly than B0.

G5 TERMINAL_STATE_DISCIPLINE_GAIN
  established only if DSD distinguishes preserving/lossy/blocked/partial/underdetermined outcomes more correctly than B0.

G6 TRACEABILITY_GAIN
  established only if DSD preserves a claim-relevant source-map-target derivation trace that B0 cannot reconstruct from the same frozen inputs.
```

Decision rule:

```text
If DSD is incorrect or NONCONFORMANT -> challenge FAIL.
If one or more G1-G6 are established against a correct B0 -> GAIN_ESTABLISHED.
If DSD and B0 are both correct and B0 matches all six dimensions -> NO_GAIN.
Otherwise -> challenge FAIL or unresolved according to the frozen scoring record.
```

No implementation speed, elegance, notation, pedagogical clarity, external practical benefit, independent-evaluator outcome, or strongest-baseline claim is scored.

## 10. Frozen expected task-level outputs

```text
Q1 DSD/B0 -> COMPLETED_PRESERVING
Q2 DSD/B0 -> COMPLETED_WITH_DECLARED_LOSS
Q3 DSD/B0 -> BLOCKED
Q4 DSD/B0 -> PARTIAL
Q5 DSD/B0 -> UNDERDETERMINED
```

All five DSD executions are expected to be `TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT` if executed correctly.

## 11. Frozen scoring — 50 checks

```text
A. immutable protocol / precommit / fairness          8
B. DSD task execution                                15
C. B0 task execution                                 15
D. comparative gain                                   8
E. scope and protocol pressure                        4
TOTAL                                                 50
```

Detailed check lock:

```text
A1 protocol blob fixed
A2 five subcases fixed
A3 baseline identity/capabilities fixed
A4 same claim-relevant inputs frozen
A5 gain criteria G1-G6 fixed
A6 scoring fixed
A7 baseline may not be weakened post-hoc
A8 no source/target/map/domain/status/loss/reconstruction revision after execution begins

B1-B5 exact terminal outputs Q1-Q5
B6 Q1 DEFINED_ZERO preserved
B7 Q1 target default remains non-source-derived
B8 Q1 declared equivalence and scoped reconstruction preserved
B9 Q2 merge not mislabeled exact preservation
B10 Q2 omission not mislabeled source missingness
B11 Q2 noninvertibility retained
B12 Q3 no unit guess/default
B13 Q4 outside-domain record not normalized or mislabeled omission
B14 Q5 no post-hoc map-version selection
B15 all five DSD executions CONFORMANT

C1-C5 exact terminal outputs Q1-Q5
C6 Q1 DEFINED_ZERO preserved
C7 Q1 target-default provenance preserved
C8 Q1 declared equivalence and reconstruction trace sufficient
C9 Q2 merge/loss recorded
C10 Q2 omission/source-missing distinction preserved
C11 Q2 unsupported reversibility rejected
C12 Q3 no unit guess/default
C13 Q4 domain/applicability discipline preserved
C14 Q5 unresolved version retained
C15 B0 trace sufficient to reconstruct all five verdicts

D1-D6 G1-G6 each NOT_ESTABLISHED if B0 matches
D7 final method gain = NO_GAIN when D1-D6 hold
D8 NO_GAIN not interpreted as method failure/merger/absorption/deletion evidence

E1 protocol revision not required if no contradiction appears
E2 no strongest-reasonable-baseline claim
E3 no external/reproducibility/internal-standardization claim
E4 no permanent survival/independence/redundancy conclusion
```

Decision:

```text
50/50 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

If a challenge-design defect is discovered, this Case ID is preserved as failed and any correction must use a new Case ID.

## 12. Evidence-count lock

Before execution:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: 3
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: 3
SUCCESSFUL_POSITIVE_TRANSFORMATION_CASES: 1
NEGATIVE_OR_FAILURE_TRANSFORMATION_CASES: 1
METHOD_BOUNDARY_TRANSFORMATION_CASES: 1
BASELINE_TRANSFORMATION_CASES: 0
NO_GAIN_TRANSFORMATION_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_TRANSFORMATION_APPLICATIONS: 0
```

A 50/50 PASS with final `NO_GAIN` may add exactly:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: +1
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: +1
BASELINE_TRANSFORMATION_CASES: +1
NO_GAIN_TRANSFORMATION_CASES: +1
```

It does not establish strongest-reasonable-baseline coverage, reproducibility, external applicability, independent validation, internal standardization, permanent method survival, or non-merger.

## 13. Next if passed

Precommit and execute a materially richer strongest-reasonable-baseline Transformation challenge stressing transformation chains, intermediate loss, temporal/schema-version migration, stochastic or choice semantics, and claim-scoped reversibility while giving the baseline all claim-relevant information. Another `NO_GAIN` remains admissible. External validation remains deferred.