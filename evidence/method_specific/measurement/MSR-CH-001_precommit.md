# MSR-CH-001 Precommit — Positive Constructed Measurement Challenge

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-19**  
Case ID: `MSR-CH-001`  
Case class: `positive_constructed_measurement_challenge`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol

```text
PROTOCOL_PATH: methods/11_measurement/PROTOCOL_v0.1.md
PROTOCOL_COMMIT: 70af7c3ddc618be34d0ff76fcc1ce63c895fc950
PROTOCOL_BLOB: bc24a5e72adaf4a1b1e64203bd14b3e781810331

BOUNDARY_AMENDMENT_COMMIT: 7f09baa7e2bb2701b4f01471abbbd443d226a78a
BOUNDARY_AMENDMENT_BLOB: 1ac7933fc19d95e9070432de99deb5a0fd1d382c
```

The protocol and amendment are immutable comparators for this challenge. They must not be edited in response to the result.

## 2. Challenge purpose

Test whether Protocol v0.1 can, in one constructed fixture:

```text
1 preserve a defined-zero outcome without treating it as missing;
2 distinguish pairwise from complete-plan discrimination;
3 establish a joint measurement plan even when every single candidate is only partial;
4 preserve an aggregate-readout collision and noninjectivity;
5 distinguish specific-pair discrimination from full reconstruction;
6 use prospectively frozen decision semantics;
7 preserve typed handoff provenance for the aggregate readout;
8 keep measurement selection distinct from an observed result or truth claim.
```

No baseline, external-domain correctness, independent validation, or method superiority is tested here.

## 3. Frozen task identity

```text
MEASUREMENT_TASK_ID: MSR-CH-001
TASK_VERSION: 1
DISCRIMINATION_QUESTION:
  Can the declared measurement plan distinguish H_A, H_B, and H_C
  for every required pair under the frozen decision semantics?

ALTERNATIVE_SET_AND_IDENTITIES:
  {H_A, H_B, H_C}

REQUIRED_DISTINCTION_SET:
  { {H_A,H_B}, {H_A,H_C}, {H_B,H_C} }

DECLARED_DECISION_RESOLUTION:
  binary decision classes LOW / HIGH under the candidate-specific frozen rules below

TASK_SCOPE:
  constructed static discrimination task only

OBSERVED_EXPERIMENTAL_RESULT_SUPPLIED:
  no

EMPIRICAL_TRUTH_OF_ANY_ALTERNATIVE_SUPPLIED:
  no
```

The task does not ask which alternative is true.

## 4. Frozen candidate register

### 4.1 Candidate m_X

```text
MEASUREMENT_ID: m_X
READOUT_TYPE: real scalar
DECLARED_DOMAIN: {H_A,H_B,H_C}
UNIT_OR_REPRESENTATION: arbitrary constructed scalar unit UX
DIRECT_OR_PROXY_ROLE: DIRECT_SOURCE_OR_RECORD
APPLICABILITY: applicable to all three alternatives

RAW OUTCOME RECORD:
  Y_X(H_A) = 0.0
  Y_X(H_B) = 0.8
  Y_X(H_C) = 0.8

TYPED VALUE STATUS:
  H_A -> DEFINED_ZERO
  H_B -> DEFINED_NONZERO_OR_VALUE
  H_C -> DEFINED_NONZERO_OR_VALUE
```

Decision rule `D_X_v1`:

```text
LOW  iff x < 0.5
HIGH iff x >= 0.5
```

This threshold is frozen before execution.

### 4.2 Candidate m_Y

```text
MEASUREMENT_ID: m_Y
READOUT_TYPE: real scalar
DECLARED_DOMAIN: {H_A,H_B,H_C}
UNIT_OR_REPRESENTATION: arbitrary constructed scalar unit UY
DIRECT_OR_PROXY_ROLE: DIRECT_SOURCE_OR_RECORD
APPLICABILITY: applicable to all three alternatives

RAW OUTCOME RECORD:
  Y_Y(H_A) = 0.2
  Y_Y(H_B) = 0.2
  Y_Y(H_C) = 0.9

TYPED VALUE STATUS:
  all three -> DEFINED_NONZERO_OR_VALUE
```

Decision rule `D_Y_v1`:

```text
LOW  iff y < 0.5
HIGH iff y >= 0.5
```

This threshold is frozen before execution.

### 4.3 Candidate m_AGG

```text
MEASUREMENT_ID: m_AGG
READOUT_TYPE: real scalar aggregate
DECLARED_DOMAIN: {H_A,H_B,H_C}
UNIT_OR_REPRESENTATION: arbitrary constructed scalar unit UA
DIRECT_OR_PROXY_ROLE: AGGREGATION_OR_COMPRESSION_HANDOFF
HANDOFF_ID: AGG-HO-001
APPLICABILITY: applicable to all three alternatives
```

Frozen support-retaining handoff:

```text
H_A:
  support = {a_plus, a_minus}
  component values = {+1, -1}
  aggregate = 0

H_B:
  support = {b_zero}
  component values = {0}
  aggregate = 0

H_C:
  support = {c_plus}
  component values = {+1}
  aggregate = 1
```

Frozen aggregate sidecar:

```text
READOUT_COLLISION_STATUS:
  collision between H_A and H_B at aggregate value 0

INJECTIVITY_SCOPE:
  not injective on {H_A,H_B,H_C}

SUPPORT_RETENTION_STATUS:
  scalar aggregate alone does not retain support;
  support sidecar is retained only for this challenge's loss audit

RECONSTRUCTION_SCOPE:
  full support reconstruction from scalar aggregate: unavailable

INFORMATION_LOSS_NOTE:
  H_A and H_B have different supports but equal aggregate
```

Decision rule `D_AGG_v1`:

```text
LOW  iff a < 0.5
HIGH iff a >= 0.5
```

This rule is frozen before execution.

## 5. Frozen joint-measurement policy

The only joint plan assessed for sufficiency is:

```text
M_JOINT = {m_X, m_Y}
```

Joint semantics are the ordered product of the already frozen decision classes:

```text
Y_JOINT(H_i) = (D_X(Y_X(H_i)), D_Y(Y_Y(H_i)))
```

No probabilistic independence assumption is used or needed.

Expected signatures derived from the frozen inputs are:

```text
H_A -> (LOW,  LOW)
H_B -> (HIGH, LOW)
H_C -> (HIGH, HIGH)
```

The challenge passes the joint-discrimination portion only if all required pairs have different joint signatures.

## 6. Frozen expected candidate-level logic

These are deterministic consequences to be checked, not post-hoc target edits.

### m_X

```text
H_A vs H_B -> PAIRWISE_DISCRIMINATING
H_A vs H_C -> PAIRWISE_DISCRIMINATING
H_B vs H_C -> PAIRWISE_NONDISCRIMINATING

candidate status:
MEASUREMENT_PARTIALLY_DISCRIMINATES
```

### m_Y

```text
H_A vs H_B -> PAIRWISE_NONDISCRIMINATING
H_A vs H_C -> PAIRWISE_DISCRIMINATING
H_B vs H_C -> PAIRWISE_DISCRIMINATING

candidate status:
MEASUREMENT_PARTIALLY_DISCRIMINATES
```

### m_AGG

```text
H_A vs H_B -> PAIRWISE_NONDISCRIMINATING
H_A vs H_C -> PAIRWISE_DISCRIMINATING
H_B vs H_C -> PAIRWISE_DISCRIMINATING

candidate status:
MEASUREMENT_PARTIALLY_DISCRIMINATES
```

The `m_AGG` result must coexist with:

```text
NONINJECTIVE_READOUT != RECONSTRUCTIVE_MEASUREMENT
GLOBAL_NONINJECTIVITY != FAILURE_TO_DISCRIMINATE_A_DECLARED_PAIR
DISCRIMINATING_READOUT != FULL_STRUCTURE_RECONSTRUCTION
```

## 7. Frozen expected plan logic

```text
M_JOINT distinguishes:
  H_A vs H_B
  H_A vs H_C
  H_B vs H_C

MEASUREMENT_PLAN_TERMINAL_STATUS:
  MEASUREMENT_PLAN_SUFFICIENT
```

No single candidate is permitted to be relabeled as fully sufficient.

## 8. Frozen selection/result boundary

The challenge must emit:

```text
MEASUREMENT_SELECTION_RESULT:
  {m_X,m_Y} is sufficient under the frozen constructed semantics

OBSERVED_EXPERIMENTAL_RESULT:
  not supplied

TRUE_ALTERNATIVE:
  not established

EMPIRICAL_VALIDITY:
  not assessed
```

Forbidden upgrade:

```text
MEASUREMENT_SELECTION != EXPERIMENTAL_EXECUTION
AVAILABLE_MEASUREMENT != OBSERVED_RESULT
PLAN_SUFFICIENCY != TRUTH_OF_ANY_ALTERNATIVE
```

## 9. Temporal / dynamic scope

This fixture is static.

```text
G11_TEMPORAL_REGIME_DYNAMIC_SUPPORT:
  NOT_APPLICABLE_WITH_REASON(static constructed fixture)
```

No claim about propagation, causal timing, or dynamic arrival is scored in this challenge.

## 10. Validity-gate acceptance

The run passes protocol-conformance only if:

```text
G1  PASS
G2  PASS
G3  PASS
G4  NOT_APPLICABLE_WITH_REASON
G5  PASS
G6  PASS
G7  PASS
G8  PASS
G9  PASS
G10 PASS
G11 NOT_APPLICABLE_WITH_REASON
G12 PASS
G13 PASS
G14 PASS
```

For G4, no Formation first-branching or separate structural-difference handoff is used; the required distinction set is declared directly by the task.

## 11. Frozen scoring — 48 checks

### A. Task and immutability — 8

```text
A1 protocol commit/blob fixed
A2 amendment commit/blob fixed
A3 task ID/version fixed
A4 alternatives fixed
A5 all three required pairs fixed
A6 resolution/decision rules fixed before execution
A7 observed result explicitly absent
A8 external application explicitly no
```

### B. Candidate typing and status — 10

```text
B1 m_X identity/type/domain/unit fixed
B2 m_Y identity/type/domain/unit fixed
B3 m_AGG identity/type/domain/unit fixed
B4 m_X H_A preserved as DEFINED_ZERO
B5 m_X H_A not treated as missing/undefined
B6 all supplied candidate outcomes retain defined/nonzero status as frozen
B7 all candidates applicable on declared domain
B8 no observed result fabricated
B9 aggregate handoff typed
B10 proxy/directness roles retained
```

### C. Pairwise and joint discrimination — 12

```text
C1-C3 m_X three pairwise results exact
C4 m_X candidate status exact
C5-C7 m_Y three pairwise results exact
C8 m_Y candidate status exact
C9-C11 joint signatures distinguish all three required pairs
C12 plan terminal = MEASUREMENT_PLAN_SUFFICIENT
```

### D. Aggregate collision and reconstruction — 10

```text
D1 H_A aggregate = 0
D2 H_B aggregate = 0
D3 H_C aggregate = 1
D4 H_A/H_B support difference retained in sidecar
D5 H_A/H_B aggregate collision explicit
D6 aggregate noninjectivity explicit
D7 full support reconstruction unavailable
D8 m_AGG H_A/H_B nondiscriminating
D9 m_AGG H_A/H_C and H_B/H_C discriminating
D10 no full-structure reconstruction claim
```

### E. Decision discipline, conformance, scope — 8

```text
E1 all thresholds are pre-frozen
E2 no post-hoc threshold change
E3 no hidden independence assumption in joint semantics
E4 selection != observed result preserved
E5 truth/diagnosis/causality not inferred
E6 all applicable G1-G14 gates conform as precommitted
E7 method-gain status = NOT_ASSESSED
E8 maximum claim limited to constructed frozen discrimination status
```

```text
TOTAL_REQUIRED_CHECKS: 48
PASS_THRESHOLD: 48/48
PARTIAL_PASS_ALLOWED: no
```

Any mismatch is preserved as a challenge result; the precommit is not edited to rescue the case.

## 12. Allowed status changes on PASS

Only on 48/48 PASS:

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 0 -> 1
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 0 -> 1
POSITIVE_MEASUREMENT_CASES: 0 -> 1
CURRENT_MEASUREMENT_EVIDENCE_STATUS:
  protocol_frozen_pre_validation -> validation_in_progress
```

All other evidence counters remain unchanged.

```text
MEASUREMENT_METHOD_GAIN_STATUS: NOT_ASSESSED
EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established
REPRODUCIBILITY_CASES: 0
MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
```
