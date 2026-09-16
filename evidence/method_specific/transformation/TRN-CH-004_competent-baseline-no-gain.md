# TRN-CH-004 — Competent-Baseline NO_GAIN Transformation Challenge Result

Status: **EXECUTED — 50/50 PASS / NO_GAIN**  
Date: **2026-09-16**  
Case ID: `TRN-CH-004`  
Case class: `competent_baseline_no_gain_challenge`  
Case origin: `constructed_same_project`  
Evidence scope class: `method_specific`  
Protocol: **Transformation Protocol v0.1**  
Protocol blob: `f78393c188c513acb30a10f1b180d598138cea61`  
Precommit commit: `5cb4e429c9dffd6f584a7023ec68a768e90ccdb9`  
Precommit blob: `034d1ba35e29474c4439ede2d2e21e2a83a73aff`  
Baseline: `B0_SCHEMA_MAP_LEDGER_EVALUATOR`

## 1. Execution discipline

The immutable precommit was frozen before execution. DSD Transformation and B0 received the same source/target/map/domain/status/loss/reconstruction records. No baseline capability was weakened and no source, target, map, domain, status, gain criterion, or scoring item was changed after execution began.

No external material was used.

## 2. Q1 — preserving map with status/default discipline

DSD execution:

```text
TARGET_Q1:
  record_id: "A-09"
  mass_kg: 0.25
  retry_count: 0
  schema_tag: "T_Q1"

record_id -> ONE_TO_ONE / PRESERVED_EXACT
mass_g -> ONE_TO_ONE / PRESERVED_UNDER_DECLARED_EQUIVALENCE
retry_count -> ONE_TO_ONE / PRESERVED_EXACT / DEFINED_ZERO preserved
schema_tag -> TARGET_ADDED / TARGET_ADDED_NOT_SOURCE_DERIVED / DEFAULT_VALUE

reconstruction:
  record_id <- "A-09"
  mass_g <- 0.25 * 1000 = 250
  retry_count <- 0

REVERSIBILITY_STATUS: LEFT_INVERTIBLE_ON_DECLARED_DOMAIN
GLOBAL_BIJECTIVITY_CLAIM: not made
TERMINAL: TRANSFORMATION_COMPLETED_PRESERVING
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B0 execution from the same frozen task record:

```text
record_id preserved exactly
mass_g represented as mass_kg under supplied equivalence
retry_count zero retained as a defined source value, not missingness
schema_tag retained as target-only default, not source-derived
all claim-relevant source carriers reconstructible at declared scope
no global bijectivity claim
terminal mapping -> TRANSFORMATION_COMPLETED_PRESERVING
TRACE_SUFFICIENT -> yes
```

No comparative gain is established on Q1.

## 3. Q2 — declared many-to-one loss and omission

DSD execution:

```text
TARGET_Q2:
  total: 13

{x,y} -> MANY_TO_ONE_MERGE / MERGED_IN_TARGET
note -> OMITTED / OMITTED_BY_TRANSFORMATION
ordered-pair reconstruction from total alone -> unavailable
INJECTIVITY_STATUS: rejected at declared x/y scope
REVERSIBILITY_STATUS: NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
TERMINAL: TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B0 execution:

```text
x=4 and y=9 merged into total=13
x/y not individually classified as exactly preserved
source note recorded as deliberately omitted, not source-missing
ordered pair not recoverable from total alone
unsupported reversibility rejected
terminal mapping -> TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
MANY_TO_ONE_MERGE != PRESERVATION
OMITTED_BY_TRANSFORMATION != MISSING_SOURCE_VALUE
FORWARD_SUCCESS != REVERSIBILITY
```

No comparative gain is established on Q2.

## 4. Q3 — missing required unit bridge

DSD execution:

```text
angle_value: 90
angle_unit: MISSING
required source-unit bridge: missing
radian target value: not emitted
default source unit: not introduced
TERMINAL: TRANSFORMATION_BLOCKED
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B0 execution:

```text
required unit metadata absent
no degree/radian assumption introduced
no target radian value emitted
terminal mapping -> TRANSFORMATION_BLOCKED
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
MISSING_REQUIRED_BRIDGE != DEFAULT_UNIT
BLOCKED != NEGATIVE_OR_ZERO_VALUE
```

No comparative gain is established on Q3.

## 5. Q4 — partial batch applicability

DSD execution:

```text
R1.score = 5
  domain_status: inside
  execution: transformed under MAP_SCORE 1.0

R2.score = 14
  domain_status: outside declared domain
  execution: not transformed
  clipping: none
  normalization: none
  omission_status: not OMITTED_BY_TRANSFORMATION

TERMINAL: TRANSFORMATION_PARTIAL
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B0 execution:

```text
R1 accepted by frozen 0..10 domain and transformed
R2 rejected as outside declared domain
R2 not clipped, normalized, or relabeled as omission
terminal mapping -> TRANSFORMATION_PARTIAL
TRACE_SUFFICIENT -> yes
```

No comparative gain is established on Q4.

## 6. Q5 — unresolved map-version identity

DSD execution:

```text
MAP_FAMILY: MAP_ID_RENDER
ALLOWED_VERSIONS: {1.0, 2.0}
SELECTED_MAP_VERSION: unresolved
SOURCE_IDENTIFIER: "007"
UNIQUE_TARGET_IDENTIFIER: unavailable
POST_HOC_VERSION_SELECTION: none
TERMINAL: TRANSFORMATION_UNDERDETERMINED
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B0 execution:

```text
version-dependent target outputs recognized: "007" vs "7"
no supplied precedence/default/latest-version rule
no version selected post hoc
unique target withheld
terminal mapping -> TRANSFORMATION_UNDERDETERMINED
TRACE_SUFFICIENT -> yes
```

No comparative gain is established on Q5.

## 7. Task-level terminal comparison

```text
TASK   DSD TERMINAL                                  B0 TERMINAL
Q1     TRANSFORMATION_COMPLETED_PRESERVING           TRANSFORMATION_COMPLETED_PRESERVING
Q2     TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS   TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
Q3     TRANSFORMATION_BLOCKED                        TRANSFORMATION_BLOCKED
Q4     TRANSFORMATION_PARTIAL                        TRANSFORMATION_PARTIAL
Q5     TRANSFORMATION_UNDERDETERMINED                TRANSFORMATION_UNDERDETERMINED
```

All claim-relevant auxiliary distinctions also matched. B0 retained enough source/target/map/domain/status/loss/reconstruction trace to retrace every frozen verdict.

## 8. Gain evaluation

```text
G1 STATUS_DISTINCTION_GAIN: NOT_ESTABLISHED
G2 CARRIER_RELATION_AND_LOSS_GAIN: NOT_ESTABLISHED
G3 TARGET_ADDITION_PROVENANCE_GAIN: NOT_ESTABLISHED
G4 RECONSTRUCTION_REVERSIBILITY_GAIN: NOT_ESTABLISHED
G5 TERMINAL_STATE_DISCIPLINE_GAIN: NOT_ESTABLISHED
G6 TRACEABILITY_GAIN: NOT_ESTABLISHED
```

Therefore:

```text
TRANSFORMATION_METHOD_GAIN_STATUS: NO_GAIN
```

This is a valid comparative result. A competent non-DSD transformation evaluator supplied with the same semantics can match DSD Transformation on these frozen dimensions.

## 9. DSD conformance ledger

```text
Q1 TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
Q2 TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
Q3 TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
Q4 TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
Q5 TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

Correctness/conformance remains separate from comparative gain:

```text
CORRECT_AND_CONFORMANT != GAIN_ESTABLISHED
CORRECT_AND_CONFORMANT + FAIR_BASELINE_MATCH -> NO_GAIN for this frozen comparison
```

## 10. Precommitted scoring

```text
A. IMMUTABLE_PROTOCOL_PRECOMMIT_FAIRNESS:   8/8 PASS
B. DSD_TASK_EXECUTION:                     15/15 PASS
C. B0_TASK_EXECUTION:                      15/15 PASS
D. COMPARATIVE_GAIN:                        8/8 PASS
E. SCOPE_AND_PROTOCOL_PRESSURE:             4/4 PASS
TOTAL:                                     50/50 PASS
```

```text
CHALLENGE_VERDICT: PASS
TRANSFORMATION_METHOD_GAIN_STATUS: NO_GAIN
PROTOCOL_DEFECT_EXPOSED: no
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

No scoring item was removed, weakened, or reinterpreted after execution.

## 11. Counter update

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: 4
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: 4
SUCCESSFUL_POSITIVE_TRANSFORMATION_CASES: 1
NEGATIVE_OR_FAILURE_TRANSFORMATION_CASES: 1
METHOD_BOUNDARY_TRANSFORMATION_CASES: 1
BASELINE_TRANSFORMATION_CASES: 1
NO_GAIN_TRANSFORMATION_CASES: 1
REPRODUCIBILITY_CASES: 0
EXTERNAL_TRANSFORMATION_APPLICATIONS: 0
INDEPENDENT_TRANSFORMATION_VALIDATION: not established
TRANSFORMATION_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_TRANSFORMATION_EVIDENCE_STATUS: validation_in_progress
```

## 12. Scope and registry discipline

This case does not establish strongest-reasonable-baseline coverage, reproducibility, external applicability, independent validation, measured practical benefit, or internal-standardization completion.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
BASELINE_MATCH != PERMANENT_REDUNDANCY
CASE_PASS != METHOD_SURVIVAL_PROOF
```

## 13. Next

Precommit and execute a materially richer strongest-reasonable-baseline Transformation challenge. It should stress composed transformation chains and intermediate-stage loss, schema-version or temporal migration, stochastic/choice semantics, target enrichment provenance, and claim-scoped reconstruction/reversibility while giving the baseline all claim-relevant information. Another `NO_GAIN` remains admissible. External validation remains deferred.