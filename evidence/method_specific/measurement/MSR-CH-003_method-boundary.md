# MSR-CH-003 — Direct Method-Boundary Challenge Result

Status: **EXECUTED — 72/72 PASS**  
Date: **2026-09-19**  
Case ID: `MSR-CH-003`  
Case class: `direct_method_boundary_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen identities

```text
MEASUREMENT_PROTOCOL_COMMIT:
  70af7c3ddc618be34d0ff76fcc1ce63c895fc950
MEASUREMENT_PROTOCOL_BLOB:
  bc24a5e72adaf4a1b1e64203bd14b3e781810331

METHOD_FAMILY_REGISTRY_COMMIT_AT_PRECOMMIT:
  6fe215e3f393f00e227a087b72a7803ee12f2399

METHOD_BOUNDARY_MATRIX_COMMIT_AT_PRECOMMIT:
  ced69912a2501761dbf733e99789d1ddadbe0587

TRACKING_SCOPE_COMMIT:
  9527ba8e5be6e9c20f82da06365d2085e7b1ab5e

PRECOMMIT_COMMIT:
  30fe7177a23034cc99bf9fb31ed36938571429ae
PRECOMMIT_BLOB:
  c561318e51817f300bb11bbe46b2a2469270ebd2
```

No protocol, registry comparator, boundary criterion, shared-artifact packet, or scoring rule was changed after precommit.

## 2. Measurement execution on SP-003

Frozen outcomes:

```text
m_X:
  H0 -> LOW
  H1 -> HIGH
  H2 -> HIGH
  H0-H1 discriminate
  H0-H2 discriminate
  H1-H2 nondiscriminate
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

m_Y:
  H0 -> LOW
  H1 -> LOW
  H2 -> HIGH
  H0-H1 nondiscriminate
  H0-H2 discriminate
  H1-H2 discriminate
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

joint {m_X,m_Y}:
  H0 -> (LOW,LOW)
  H1 -> (HIGH,LOW)
  H2 -> (HIGH,HIGH)
  -> all required pairs discriminate
  -> MEASUREMENT_PLAN_SUFFICIENT
```

The supplied SUM aggregate remains noninjective for H0/H1:

```text
SUM(H0)=0
SUM(H1)=0
support(H0) != support(H1)
```

Measurement consumes that collision as a discrimination/reconstruction constraint rather than redefining the Aggregation operation.

No observed experimental result or true alternative is created.

## 3. B1 — Specification boundary

Shared artifacts used:

```text
REQ-1..REQ-4
alternatives
required distinctions
decision-rule guards
status guards
```

Specification binding operation on the shared packet remains:

```text
state and preserve requirements/constraints
```

Measurement binding operation remains:

```text
evaluate candidate readout applicability/status,
pairwise discrimination,
joint discrimination,
and plan sufficiency
```

Result:

```text
SPECIFICATION_REQUIREMENTS != MEASUREMENT_DISCRIMINATION_RESULT
BOUNDARY_RESULT: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Specification may supply the requirement "distinguish every pair", but that requirement is not itself evidence that m_X, m_Y, or their joint plan satisfies it.

Checks B1.1-B1.5: **5/5 PASS**.

## 4. B2 — Design boundary

Shared artifacts used:

```text
candidate family {D1,D2,D3}
hard constraint: supplied candidates only
requirement to distinguish required pairs
```

Design binding operation:

```text
construct/filter an admissible target or plan family under goals/constraints
```

Measurement binding operation:

```text
evaluate supplied readouts under outcome/decision semantics
and emit discrimination/sufficiency status
```

A Design run can preserve or filter candidate plan structures. If it wishes to know that D3 actually discriminates all required pairs, it must consume an appropriate Measurement result or perform an equivalent Measurement suboperation explicitly. The Design label alone does not supply the pairwise/joint discrimination ledger.

Result:

```text
ADMISSIBLE_DESIGN_PLAN != MEASUREMENT_PLAN_SUFFICIENT
BOUNDARY_RESULT: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B2.1-B2.5: **5/5 PASS**.

## 5. B3 — Aggregation boundary

Shared artifacts:

```text
component values
SUM mapping
aggregate outputs
collision sidecar
```

Aggregation binding operation:

```text
construct the declared aggregate readout
```

Measurement binding operation:

```text
judge whether the supplied aggregate readout
discriminates required alternatives at the frozen resolution
```

The same aggregate `0` for H0/H1 is a valid Aggregation result and simultaneously a nondiscriminating Measurement outcome for that pair.

Result:

```text
AGGREGATE_VALUE != DISCRIMINATION_VERDICT
BOUNDARY_RESULT: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B3.1-B3.5: **5/5 PASS**.

## 6. B4 — Compression boundary

Shared artifacts:

```text
joint LOW/HIGH signatures
compression map C1
two-bit codes 00,10,11
declared retained distinction
```

Compression binding operation:

```text
reduce/encode representation under a declared retention objective
```

Measurement binding operation:

```text
judge whether a supplied readout/representation
discriminates the frozen required alternatives
```

The two-bit code may preserve all three signatures, but compression success is assessed relative to its representation objective. Measurement sufficiency is separately assessed relative to the discrimination task.

Result:

```text
COMPRESSION_SUCCESS != MEASUREMENT_PLAN_SUFFICIENCY
BOUNDARY_RESULT: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B4.1-B4.5: **5/5 PASS**.

## 7. B5 — Comparison boundary

Shared artifacts:

```text
H0/H1/H2 structural tags
m_X/m_Y outcome tables
```

Comparison binding operation:

```text
judge preserved/differing structure across supplied subjects
```

Measurement binding operation:

```text
apply frozen candidate semantics and decision rules,
evaluate required pairwise/joint discrimination,
then emit plan sufficiency
```

Comparison can report that H0 differs from H1 in tag A and H1 differs from H2 in tag B, or compare outcome values. That difference report does not by itself establish whether a particular candidate measurement or joint plan is applicable, discriminating, blocked, or sufficient under Measurement's output contract.

Result:

```text
DIFFERENCE_MATRIX != MEASUREMENT_PLAN_TERMINAL
BOUNDARY_RESULT: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B5.1-B5.5: **5/5 PASS**.

## 8. B6 — Diagnosis boundary

Shared artifacts:

```text
alternative hypotheses H0/H1/H2
candidate readout semantics
```

Diagnosis binding operation:

```text
infer compatible current hidden state/cause
from actual supplied evidence or observation
```

Measurement binding operation:

```text
evaluate which observations/readouts would discriminate
the alternatives without requiring an observed result
```

The shared packet explicitly contains:

```text
OBSERVED_EXPERIMENTAL_RESULT: absent
TRUE_ALTERNATIVE: not supplied
```

Therefore Diagnosis cannot legitimately infer H0, H1, or H2 from this fixture, while Measurement can still establish that `{m_X,m_Y}` is a sufficient discrimination plan.

Result:

```text
MEASUREMENT_PLAN_SUFFICIENCY != DIAGNOSIS
BOUNDARY_RESULT: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B6.1-B6.5: **5/5 PASS**.

## 9. B7 — Prediction boundary

Shared artifacts:

```text
alternative states/models
PRED-v1 expected m_X/m_Y outcomes
```

Prediction binding operation:

```text
supply/assert model-based target or future outcome relevance
under its own declared scope
```

Measurement binding operation:

```text
consume supplied expected outcomes as a typed handoff
and evaluate their discrimination sufficiency
```

`PRED-v1` supplies the expected values but does not itself emit Measurement candidate statuses, joint-measurement sufficiency, or Measurement's selection/observation boundary.

Result:

```text
PREDICTED_OUTCOME_TABLE != MEASUREMENT_PLAN_TERMINAL
BOUNDARY_RESULT: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B7.1-B7.5: **5/5 PASS**.

## 10. B8 — Simulation boundary

Shared artifacts:

```text
H0/H1/H2 states
SIM-v1 trajectory
model handoff
```

Simulation binding operation:

```text
generate a model-consistent trajectory/output
under supplied model rules
```

Measurement binding operation:

```text
evaluate supplied readouts as discriminators
at the frozen resolution and scope
```

The static one-step `SIM-v1` trajectory can be model-consistent without answering whether m_X, m_Y, or their joint plan distinguishes all required alternative pairs.

Result:

```text
SIMULATED_TRAJECTORY != MEASUREMENT_PLAN_SUFFICIENCY
BOUNDARY_RESULT: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B8.1-B8.5: **5/5 PASS**.

## 11. B9 — Tracking boundary

Shared artifacts:

```text
source identities
version/handoff identities
PRED-v1 provenance
SUM provenance
SIM-v1 provenance
Measurement packet provenance
```

Tracking binding operation:

```text
record supported trace links, states, handoffs,
versions, and unresolved trace gaps
```

Measurement binding operation:

```text
use typed provenance as a constraint while
evaluating candidate discrimination and plan sufficiency
```

Tracking correctly records:

```text
SRC-0 -> PRED-v1 -> outcome table -> SP-003
AGG-source -> SUM -> sidecar -> SP-003
SIM-source -> SIM-v1 -> trajectory handoff -> SP-003
```

but those trace links do not themselves establish that the joint readout plan distinguishes all required pairs.

Result:

```text
TRACE_RECORD != MEASUREMENT_DISCRIMINATION_RESULT
BOUNDARY_RESULT: PARTIAL_OVERLAP_NOT_COLLAPSE
```

The broadened Tracking scope is therefore compatible with Measurement as an upstream/sidecar trace method rather than an exact replacement in this fixture.

Checks B9.1-B9.5: **5/5 PASS**.

## 12. B10 — Audit boundary

Initial fair packet access:

```text
SP-003 available
conformance checklist available
Measurement output not preloaded
```

This preserves precommit check A10.

Before a Measurement execution exists, Audit can inspect task/checklist structure but cannot audit a completed Measurement result that does not yet exist.

After Measurement executes, the resulting execution record is handed to Audit as a **subsequent-stage artifact**. Audit can then retrace whether the Measurement run froze its task, used supplied maps, preserved the threshold, avoided fabricated observations, and emitted a terminal.

Audit binding operation:

```text
retrace/evaluate completed work against declared rules
```

Measurement binding operation:

```text
perform the discrimination assessment
and emit the plan terminal/conformance record
```

Thus the sequential handoff itself exposes the boundary:

```text
MEASUREMENT_RESULT
  -> may become AUDIT_INPUT

MEASUREMENT_RESULT != AUDIT_VERDICT
```

Result:

```text
BOUNDARY_RESULT: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B10.1-B10.5: **5/5 PASS**.

## 13. Exact-collapse review

The precommitted exact-collapse criterion required a neighboring method, merely by executing its own current declared task, to materially reproduce Measurement's combined:

```text
candidate applicability/status evaluation
pairwise discrimination matrix
joint-measurement discrimination
information-loss/injectivity constraints as measurement constraints
plan-level sufficiency terminal
selection-vs-observed-result boundary
Measurement-specific conformance/gain/max-claim output
```

Observed result:

```text
BOUNDARY_PAIRS_TESTED: 10
EXACT_COLLAPSE_PAIRS: 0
UNRESOLVED_BOUNDARY_PAIRS: 0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS: 10

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED
```

No pair satisfies the exact-collapse criterion in SP-003.

## 14. Global boundary guards

All preserved:

```text
SPECIFICATION_REQUIREMENT != MEASUREMENT_RESULT
DESIGN_ADMISSIBILITY != MEASUREMENT_SUFFICIENCY
AGGREGATE_VALUE != DISCRIMINATION_VERDICT
COMPRESSION_SUCCESS != MEASUREMENT_SUFFICIENCY
COMPARISON_DIFFERENCE_MATRIX != MEASUREMENT_TERMINAL
MEASUREMENT_SUFFICIENCY != DIAGNOSIS
PREDICTION_OUTPUT != MEASUREMENT_TERMINAL
SIMULATION_TRAJECTORY != MEASUREMENT_TERMINAL
TRACKING_TRACE != MEASUREMENT_RESULT
MEASUREMENT_RESULT != AUDIT_VERDICT
```

Additional preserved handoff rules:

```text
SHARED_ARTIFACT != SAME_METHOD
HANDOFF_COMPATIBILITY != METHOD_COLLAPSE
SEQUENTIAL_DEPENDENCY != METHOD_IDENTITY
FIXTURE_BOUNDED_SEPARATION != PERMANENT_METHOD_SURVIVAL
```

## 15. Frozen scoring

### A. Common fairness / immutability

```text
A1 PASS
A2 PASS
A3 PASS
A4 PASS
A5 PASS
A6 PASS
A7 PASS
A8 PASS
A9 PASS
A10 PASS
A11 PASS
A12 PASS
A: 12/12
```

For A10, Audit received the completed Measurement execution only after the Measurement stage. It was not preloaded into the initial shared packet.

### B. Boundary groups

```text
B1 Specification: 5/5 PASS
B2 Design:        5/5 PASS
B3 Aggregation:   5/5 PASS
B4 Compression:   5/5 PASS
B5 Comparison:    5/5 PASS
B6 Diagnosis:     5/5 PASS
B7 Prediction:    5/5 PASS
B8 Simulation:    5/5 PASS
B9 Tracking:      5/5 PASS
B10 Audit:        5/5 PASS

B subtotal: 50/50
```

### C. Global boundary discipline

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

C: 10/10
```

Final:

```text
TOTAL_REQUIRED_CHECKS: 72
PASSED: 72
FAILED: 0
TOTAL: 72/72 PASS
```

## 16. Conformance and method-gain status

```text
MSR-CH-003_CONFORMANCE: CONFORMANT
MEASUREMENT_METHOD_GAIN_STATUS: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

No competent non-DSD baseline was run, so no gain claim is permitted.

## 17. Counter update authorized by precommit

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 2 -> 3
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 2 -> 3
METHOD_BOUNDARY_MEASUREMENT_CASES: 0 -> 1

POSITIVE_MEASUREMENT_CASES: 1
NEGATIVE_OR_FAILURE_MEASUREMENT_CASES: 1
BASELINE_MEASUREMENT_CASES: 0
NO_GAIN_MEASUREMENT_CASES: 0
REPRODUCIBILITY_CASES: 0

EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established
MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_MEASUREMENT_EVIDENCE_STATUS: validation_in_progress

PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 18. Maximum supported claim

MSR-CH-003 supports only:

```text
Under the frozen SP-003 constructed packet and current registry task definitions,
Measurement's binding operation and output contract did not exactly collapse into
Specification, Design, Aggregation, Compression, Comparison, Diagnosis,
Prediction, Simulation, Tracking, or Audit.
```

It does not establish:

```text
permanent method independence
future-proof registry survival
external validity
independent validation
practical superiority
neighboring-method invalidity
neighboring-method maturity
```

## 19. Next

Proceed to a separately precommitted competent non-DSD baseline comparison using equal information access. Preserve `NO_GAIN` if a competent baseline reproduces the same claim-relevant Measurement outputs.
