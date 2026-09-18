# MSR-CH-003 Precommit — Direct Method-Boundary Challenge

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-19**  
Case ID: `MSR-CH-003`  
Case class: `direct_method_boundary_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen comparators

```text
MEASUREMENT_PROTOCOL_COMMIT: 70af7c3ddc618be34d0ff76fcc1ce63c895fc950
MEASUREMENT_PROTOCOL_BLOB: bc24a5e72adaf4a1b1e64203bd14b3e781810331

METHOD_FAMILY_REGISTRY_COMMIT_AT_PRECOMMIT:
  6fe215e3f393f00e227a087b72a7803ee12f2399

METHOD_BOUNDARY_MATRIX_COMMIT_AT_PRECOMMIT:
  ced69912a2501761dbf733e99789d1ddadbe0587

TRACKING_SCOPE_COMMIT:
  9527ba8e5be6e9c20f82da06365d2085e7b1ab5e
```

Measurement Protocol v0.1 is immutable for this challenge.

The neighboring-method descriptions are used only as current registry task definitions. This case does not validate, mature, or independently verify any neighboring method.

## 2. Purpose

Test whether Measurement's binding operation remains distinct under fair shared-artifact access from:

```text
B1 Specification
B2 Design
B3 Aggregation
B4 Compression
B5 Comparison
B6 Diagnosis
B7 Prediction
B8 Simulation
B9 Tracking
B10 Audit
```

Allowed boundary outcomes:

```text
DISTINCT_BINDING_OPERATION_WITH_SHARED_ARTIFACTS
PARTIAL_OVERLAP_NOT_COLLAPSE
EXACT_COLLAPSE_CANDIDATE
UNRESOLVED_BOUNDARY
```

No boundary result may be promoted to permanent method-registry survival or permanent merger.

## 3. Fair shared-artifact packet

Every boundary subcase receives the same packet `SP-003`.

### 3.1 Discrimination target

```text
ALTERNATIVES: {H0,H1,H2}

REQUIRED_DISTINCTIONS:
  H0-H1
  H0-H2
  H1-H2

DECISION_RESOLUTION:
  LOW/HIGH

OBSERVED_EXPERIMENTAL_RESULT:
  absent

TRUE_ALTERNATIVE:
  not supplied
```

### 3.2 Structural profile

```text
H0: structural tags {A0,B0}
H1: structural tags {A1,B0}
H2: structural tags {A1,B1}
```

### 3.3 Candidate readouts

```text
m_X:
  H0 -> 0
  H1 -> 1
  H2 -> 1

m_Y:
  H0 -> 0
  H1 -> 0
  H2 -> 1

decision rule for both:
  LOW  iff value < 0.5
  HIGH iff value >= 0.5
```

Expected Measurement-only discrimination result:

```text
m_X:
  H0-H1 discriminate
  H0-H2 discriminate
  H1-H2 nondiscriminate
  -> PARTIAL

m_Y:
  H0-H1 nondiscriminate
  H0-H2 discriminate
  H1-H2 discriminate
  -> PARTIAL

joint {m_X,m_Y} signatures:
  H0 -> (LOW,LOW)
  H1 -> (HIGH,LOW)
  H2 -> (HIGH,HIGH)

MEASUREMENT_PLAN_SUFFICIENT
```

### 3.4 Aggregation artifact

Component values:

```text
H0 -> {+1,-1}
H1 -> {0}
H2 -> {+1}
```

Supplied Aggregation operation:

```text
SUM:
  H0 -> 0
  H1 -> 0
  H2 -> 1
```

Collision sidecar:

```text
H0/H1 aggregate collision at 0
support(H0) != support(H1)
scalar SUM not injective on {H0,H1,H2}
```

### 3.5 Compression artifact

Supplied compression map `C1`:

```text
raw pair (m_X,m_Y)
  -> two-bit code

(LOW,LOW)   -> 00
(HIGH,LOW)  -> 10
(HIGH,HIGH) -> 11

declared retained distinction:
  all three frozen alternatives remain distinguishable

compression objective:
  represent joint signature in a fixed two-bit code
```

### 3.6 Specification artifact

```text
REQ-1 distinguish every pair in REQUIRED_DISTINCTIONS
REQ-2 do not change LOW/HIGH threshold after inspection
REQ-3 do not invent an observed result
REQ-4 preserve explicit missing/inapplicable/undefined distinctions if encountered
```

### 3.7 Design artifact

Supplied candidate design family:

```text
D1 = measurement plan {m_X}
D2 = measurement plan {m_Y}
D3 = measurement plan {m_X,m_Y}
```

Hard design constraint:

```text
must use only supplied candidates
must not add a new sensor/readout
```

The Design task, if invoked, is to construct/filter an admissible target plan family under the supplied design constraints. Measurement separately evaluates discrimination sufficiency under its protocol.

### 3.8 Prediction artifact

Supplied model-output handoff `PRED-v1`:

```text
expected readout outcomes:
  m_X(H0,H1,H2) = (0,1,1)
  m_Y(H0,H1,H2) = (0,0,1)

claim:
  these are model-supplied expected outcomes only
```

Prediction does not select a measurement plan merely by supplying these expected outcomes.

### 3.9 Simulation artifact

Supplied trajectory handoff `SIM-v1`:

```text
t0:
  H0=(A0,B0)
  H1=(A1,B0)
  H2=(A1,B1)

t1:
  H0=(A0,B0)
  H1=(A1,B0)
  H2=(A1,B1)

trajectory type:
  static one-step model-consistent trajectory for this fixture
```

Simulation's task is trajectory generation/consistency under supplied model rules, not measurement-plan sufficiency.

### 3.10 Tracking artifact

Supplied trace ledger:

```text
SRC-0
  -> PRED-v1
  -> candidate outcome table
  -> Measurement packet SP-003

AGG-source
  -> SUM operation record
  -> aggregate sidecar
  -> Measurement packet SP-003

SIM-source
  -> SIM-v1
  -> trajectory handoff
  -> Measurement packet SP-003
```

Tracking may record these links but does not convert trace continuity into Measurement discrimination status.

### 3.11 Audit artifact

Supplied conformance checklist:

```text
question frozen?
alternatives frozen?
required pairs frozen?
decision rule frozen?
outcome maps supplied?
no observed result fabricated?
terminal emitted?
```

Audit may evaluate a completed Measurement execution against this checklist. Audit does not itself perform the Measurement binding operation unless explicitly handed a Measurement result to review.

## 4. Boundary expectations

### B1 — Specification

Shared:
```text
requirements
alternatives
required distinctions
status/threshold guards
```

Specification-specific operation:
```text
state/preserve requirements and constraints
```

Measurement-specific operation:
```text
evaluate candidate readout discrimination and plan sufficiency
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
SPECIFICATION_REQUIREMENTS != MEASUREMENT_DISCRIMINATION_RESULT
```

### B2 — Design

Shared:
```text
candidate plan family
goals/constraints
```

Design-specific operation:
```text
construct/filter admissible target/design family
```

Measurement-specific operation:
```text
evaluate whether supplied readouts discriminate required alternatives
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
ADMISSIBLE_DESIGN_PLAN != MEASUREMENT_PLAN_SUFFICIENT
```

### B3 — Aggregation

Shared:
```text
component values
SUM output
collision sidecar
```

Aggregation-specific operation:
```text
construct declared aggregate readout
```

Measurement-specific operation:
```text
judge whether that readout discriminates the frozen alternatives
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
AGGREGATE_VALUE != DISCRIMINATION_VERDICT
```

### B4 — Compression

Shared:
```text
joint signature
two-bit representation
retained-distinction declaration
```

Compression-specific operation:
```text
reduce/encode representation under declared retention objective
```

Measurement-specific operation:
```text
verify discrimination status of supplied readout/representation at task resolution
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
COMPRESSION_SUCCESS != MEASUREMENT_PLAN_SUFFICIENCY
```

### B5 — Comparison

Shared:
```text
H0/H1/H2 structural profiles
candidate outcome tables
```

Comparison-specific operation:
```text
judge preserved/differing structure across supplied subjects
```

Measurement-specific operation:
```text
map candidate readouts through frozen decision semantics into required-pair and plan sufficiency statuses
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
DIFFERENCE_MATRIX != MEASUREMENT_PLAN_TERMINAL
```

### B6 — Diagnosis

Shared:
```text
alternative hypotheses
candidate readout semantics
```

Diagnosis-specific operation:
```text
infer compatible hidden/current state from actual evidence/observation
```

Measurement-specific operation:
```text
select/evaluate discriminating observations without requiring an observed outcome
```

Because `OBSERVED_EXPERIMENTAL_RESULT=absent`, Diagnosis must not infer H0/H1/H2.

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
MEASUREMENT_PLAN_SUFFICIENCY != DIAGNOSIS
```

### B7 — Prediction

Shared:
```text
alternative models
expected candidate outcomes
```

Prediction-specific operation:
```text
assert model-based future/target outcome relevance
```

Measurement-specific operation:
```text
consume supplied expected outcomes and evaluate discrimination sufficiency
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
PREDICTED_OUTCOME_TABLE != MEASUREMENT_PLAN_TERMINAL
```

### B8 — Simulation

Shared:
```text
alternative states
trajectory/model handoff
```

Simulation-specific operation:
```text
generate model-consistent trajectory/output
```

Measurement-specific operation:
```text
evaluate supplied candidate readouts as discriminators
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
SIMULATED_TRAJECTORY != MEASUREMENT_PLAN_SUFFICIENCY
```

### B9 — Tracking

Shared:
```text
source/version/handoff identities
outcome-table provenance
aggregate/simulation handoffs
```

Tracking-specific operation:
```text
record supported trace links and unresolved trace gaps
```

Measurement-specific operation:
```text
use typed provenance as a constraint while evaluating discrimination
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
TRACE_RECORD != MEASUREMENT_DISCRIMINATION_RESULT
```

### B10 — Audit

Shared:
```text
Measurement task locks
Measurement execution record
conformance checklist
```

Audit-specific operation:
```text
retrace/evaluate completed work against declared rules
```

Measurement-specific operation:
```text
perform the discrimination assessment and emit the plan terminal
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
MEASUREMENT_RESULT != AUDIT_VERDICT
```

## 5. Exact-collapse criterion

A neighboring method is an `EXACT_COLLAPSE_CANDIDATE` only if, under equal access to `SP-003`, its binding operation and output contract materially reproduce Measurement's:

```text
candidate applicability/status evaluation
pairwise discrimination matrix
joint-measurement discrimination
information-loss/injectivity constraints as measurement constraints
plan-level sufficiency terminal
selection-vs-observed-result boundary
Measurement-specific conformance/gain/max-claim output
```

merely by executing that neighboring method's own current declared task.

Sharing some fields, intermediate calculations, or handoffs is insufficient for collapse.

## 6. Frozen scoring — 72 checks

### A. Common fairness / immutability — 12

```text
A1 Measurement protocol identity fixed
A2 registry identity fixed
A3 boundary-matrix identity fixed
A4 Tracking scope identity fixed
A5 all ten neighboring methods named before execution
A6 same SP-003 packet available to all boundary comparisons
A7 no observed result supplied
A8 no true alternative supplied
A9 no neighbor denied a shared artifact available to Measurement
A10 no Measurement-only output preloaded as a neighbor input
A11 no protocol/registry wording changed after precommit
A12 external application remains no
```

### B. Ten method-boundary groups — 50

For each `B1-B10`, five checks:

```text
1 shared artifacts identified
2 neighboring binding operation stated without replacing it by Measurement
3 Measurement binding operation stated
4 output-contract difference preserved
5 exact collapse not asserted unless exact-collapse criterion is met
```

```text
B1-B10 subtotal: 50
```

### C. Global boundary discipline — 10

```text
C1 Specification requirement != Measurement result
C2 Design admissibility != Measurement sufficiency
C3 Aggregate value != discrimination verdict
C4 Compression success != Measurement sufficiency
C5 Comparison difference matrix != Measurement terminal
C6 Measurement sufficiency != Diagnosis
C7 Prediction output != Measurement terminal
C8 Simulation trajectory != Measurement terminal
C9 Tracking trace != Measurement result
C10 Measurement result != Audit verdict
```

```text
TOTAL_REQUIRED_CHECKS: 72
PASS_THRESHOLD: 72/72
PARTIAL_PASS_ALLOWED: no
```

Any unexpected exact collapse or unresolved boundary must be preserved.

## 7. Allowed result summary

If all ten pairs satisfy the precommitted non-collapse criterion:

```text
BOUNDARY_PAIRS_TESTED: 10
EXACT_COLLAPSE_PAIRS: 0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS: 10
BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED
```

This means only that the current frozen fixture does not collapse Measurement into those neighboring method tasks.

It does not establish permanent method independence.

## 8. Allowed counter changes on 72/72 PASS

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 2 -> 3
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 2 -> 3
METHOD_BOUNDARY_MEASUREMENT_CASES: 0 -> 1
```

Unchanged:

```text
POSITIVE_MEASUREMENT_CASES: 1
NEGATIVE_OR_FAILURE_MEASUREMENT_CASES: 1
BASELINE_MEASUREMENT_CASES: 0
NO_GAIN_MEASUREMENT_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established
MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_MEASUREMENT_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no unless contradiction found
SHARED_CORE_REOPEN_REQUIRED: no unless contradiction found
```
