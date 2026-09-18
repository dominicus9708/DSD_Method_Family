# MSR-CH-001 — Positive Constructed Measurement Challenge Result

Status: **EXECUTED — 48/48 PASS**  
Date: **2026-09-19**  
Case ID: `MSR-CH-001`  
Case class: `positive_constructed_measurement_challenge`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen identities

```text
PROTOCOL_COMMIT: 70af7c3ddc618be34d0ff76fcc1ce63c895fc950
PROTOCOL_BLOB: bc24a5e72adaf4a1b1e64203bd14b3e781810331

BOUNDARY_AMENDMENT_COMMIT: 7f09baa7e2bb2701b4f01471abbbd443d226a78a
BOUNDARY_AMENDMENT_BLOB: 1ac7933fc19d95e9070432de99deb5a0fd1d382c

PRECOMMIT_COMMIT: bfe3898ce181f8b2d8bcf0cffe153e947d75b486
PRECOMMIT_BLOB: cedf69207c5b183ce6474573f2a96f80f50df51e
```

No protocol, amendment, task, candidate, decision rule, or scoring criterion was changed after precommit.

## 2. Frozen task execution

```text
ALTERNATIVES:
  H_A, H_B, H_C

REQUIRED_DISTINCTIONS:
  H_A vs H_B
  H_A vs H_C
  H_B vs H_C

DECISION RESOLUTION:
  LOW / HIGH under frozen candidate-specific decision rules

OBSERVED EXPERIMENTAL RESULT:
  not supplied

TRUE ALTERNATIVE:
  not established
```

The run therefore evaluates measurement-plan discrimination only.

## 3. Candidate m_X

Frozen raw outcomes:

```text
H_A -> 0.0 / DEFINED_ZERO
H_B -> 0.8 / DEFINED_NONZERO_OR_VALUE
H_C -> 0.8 / DEFINED_NONZERO_OR_VALUE
```

Frozen rule:

```text
LOW  iff x < 0.5
HIGH iff x >= 0.5
```

Decision classes:

```text
H_A -> LOW
H_B -> HIGH
H_C -> HIGH
```

Pairwise matrix:

```text
H_A vs H_B -> PAIRWISE_DISCRIMINATING
H_A vs H_C -> PAIRWISE_DISCRIMINATING
H_B vs H_C -> PAIRWISE_NONDISCRIMINATING
```

Candidate result:

```text
m_X -> MEASUREMENT_PARTIALLY_DISCRIMINATES
```

The `0.0` outcome for H_A remains a defined zero. It is not missing, undefined, unavailable, or negative evidence.

## 4. Candidate m_Y

Frozen raw outcomes:

```text
H_A -> 0.2
H_B -> 0.2
H_C -> 0.9
```

Frozen rule:

```text
LOW  iff y < 0.5
HIGH iff y >= 0.5
```

Decision classes:

```text
H_A -> LOW
H_B -> LOW
H_C -> HIGH
```

Pairwise matrix:

```text
H_A vs H_B -> PAIRWISE_NONDISCRIMINATING
H_A vs H_C -> PAIRWISE_DISCRIMINATING
H_B vs H_C -> PAIRWISE_DISCRIMINATING
```

Candidate result:

```text
m_Y -> MEASUREMENT_PARTIALLY_DISCRIMINATES
```

## 5. Candidate m_AGG

Frozen Aggregation handoff:

```text
H_A:
  support {a_plus,a_minus}
  values {+1,-1}
  aggregate 0

H_B:
  support {b_zero}
  values {0}
  aggregate 0

H_C:
  support {c_plus}
  values {+1}
  aggregate 1
```

Frozen decision rule:

```text
LOW  iff a < 0.5
HIGH iff a >= 0.5
```

Decision classes:

```text
H_A -> LOW
H_B -> LOW
H_C -> HIGH
```

Pairwise matrix:

```text
H_A vs H_B -> PAIRWISE_NONDISCRIMINATING
H_A vs H_C -> PAIRWISE_DISCRIMINATING
H_B vs H_C -> PAIRWISE_DISCRIMINATING
```

Candidate result:

```text
m_AGG -> MEASUREMENT_PARTIALLY_DISCRIMINATES
```

The information-loss sidecar remains:

```text
H_A support != H_B support
aggregate(H_A) = aggregate(H_B) = 0

READOUT_COLLISION_STATUS:
  explicit H_A/H_B collision

INJECTIVITY_SCOPE:
  not injective on {H_A,H_B,H_C}

FULL SUPPORT RECONSTRUCTION FROM SCALAR AGGREGATE:
  unavailable
```

This produces the intended distinction:

```text
EQUAL_AGGREGATE != EQUAL_SUPPORT
NONINJECTIVE_READOUT != RECONSTRUCTIVE_MEASUREMENT
GLOBAL_NONINJECTIVITY != FAILURE_TO_DISCRIMINATE_A_DECLARED_PAIR
DISCRIMINATING_READOUT != FULL_STRUCTURE_RECONSTRUCTION
```

Although m_AGG is globally noninjective on the frozen alternative set, it still distinguishes H_C from H_A and H_B.

## 6. Joint measurement {m_X,m_Y}

Frozen joint rule:

```text
Y_JOINT(H_i) = (D_X(Y_X(H_i)), D_Y(Y_Y(H_i)))
```

No independence assumption is used.

Joint signatures:

```text
H_A -> (LOW,  LOW)
H_B -> (HIGH, LOW)
H_C -> (HIGH, HIGH)
```

Required-pair result:

```text
H_A vs H_B -> JOINT_DISCRIMINATING
H_A vs H_C -> JOINT_DISCRIMINATING
H_B vs H_C -> JOINT_DISCRIMINATING
```

Therefore:

```text
MEASUREMENT_PLAN_TERMINAL_STATUS:
  MEASUREMENT_PLAN_SUFFICIENT
```

No individual candidate is promoted to full sufficiency.

```text
SINGLE_MEASUREMENT_INSUFFICIENCY != JOINT_MEASUREMENT_INSUFFICIENCY
JOINT_SUFFICIENCY != SINGLE_MEASUREMENT_SUFFICIENCY
MEMBER_COUNT != INFORMATION_GAIN
```

The sufficiency comes from the frozen ordered signatures, not from having two measurements by itself.

## 7. Selection versus observation

The protocol output is strictly:

```text
MEASUREMENT_SELECTION_RESULT:
  the declared plan {m_X,m_Y} is sufficient to discriminate
  all frozen required pairs under the constructed decision semantics

OBSERVED_EXPERIMENTAL_RESULT:
  not supplied

TRUE_ALTERNATIVE:
  not established

EMPIRICAL_VALIDITY:
  not assessed

DIAGNOSIS:
  not inferred

CAUSAL_CLAIM:
  not inferred
```

Thus:

```text
MEASUREMENT_SELECTION != EXPERIMENTAL_EXECUTION
AVAILABLE_MEASUREMENT != OBSERVED_RESULT
PLAN_SUFFICIENCY != TRUTH_OF_ANY_ALTERNATIVE
DISCRIMINATION_SUFFICIENCY != DIAGNOSIS
DISCRIMINATION_SUFFICIENCY != CAUSAL_PROOF
```

## 8. Validity gates

```text
G1  PASS
  task ID/version, question, alternatives, required distinctions, resolution, scope frozen

G2  PASS
  m_X, m_Y, m_AGG identity/type/domain/unit fixed

G3  PASS
  typed status preserved; H_A under m_X remains DEFINED_ZERO

G4  NOT_APPLICABLE_WITH_REASON
  no Formation first-branching or separate structural-difference handoff is used;
  required distinctions are declared directly by the frozen task

G5  PASS
  all outcome maps are supplied; no prediction/calibration invented

G6  PASS
  D_X_v1, D_Y_v1, D_AGG_v1 frozen prospectively

G7  PASS
  all required in-scope pairs evaluated for each candidate

G8  PASS
  joint product-signature semantics explicit; no hidden independence assumption

G9  PASS
  m_AGG collision, noninjectivity, support loss, reconstruction limit preserved

G10 PASS
  direct roles and aggregation handoff provenance preserved

G11 NOT_APPLICABLE_WITH_REASON
  static constructed fixture; no temporal/dynamic-support claim

G12 PASS
  Aggregation remains a typed handoff; Measurement does not relabel it as its own aggregation operation

G13 PASS
  selected plan not relabeled as observed experimental result

G14 PASS
  terminal, conformance, gain status, and maximum claim emitted
```

Overall:

```text
MEASUREMENT_PROTOCOL_CONFORMANCE: CONFORMANT
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 9. Frozen scoring

### A. Task and immutability

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

### B. Candidate typing and status

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

B: 10/10
```

### C. Pairwise and joint discrimination

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

### D. Aggregate collision and reconstruction

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

### E. Decision discipline, conformance, scope

```text
E1 PASS
E2 PASS
E3 PASS
E4 PASS
E5 PASS
E6 PASS
E7 PASS
E8 PASS

E: 8/8
```

Final:

```text
TOTAL_REQUIRED_CHECKS: 48
PASSED: 48
FAILED: 0
TOTAL: 48/48 PASS
```

## 10. Method-gain status

No baseline was run.

```text
MEASUREMENT_METHOD_GAIN_STATUS: NOT_ASSESSED
```

This case is direct internal protocol evidence, not comparative advantage evidence.

## 11. Status changes authorized by the precommit

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 0 -> 1
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 0 -> 1
POSITIVE_MEASUREMENT_CASES: 0 -> 1

CURRENT_MEASUREMENT_EVIDENCE_STATUS:
  protocol_frozen_pre_validation -> validation_in_progress
```

Unchanged:

```text
NEGATIVE_OR_FAILURE_MEASUREMENT_CASES: 0
METHOD_BOUNDARY_MEASUREMENT_CASES: 0
BASELINE_MEASUREMENT_CASES: 0
NO_GAIN_MEASUREMENT_CASES: 0
STRONGEST_REASONABLE_BASELINE_MEASUREMENT: not established
REPRODUCIBILITY_CASES: 0
EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established
MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 12. Maximum supported claim

This challenge establishes only that Protocol v0.1 can execute the frozen constructed fixture while correctly preserving:

```text
defined zero
pairwise partial discrimination
joint-plan sufficiency
aggregate collision and noninjectivity
specific-pair discrimination despite global noninjectivity
reconstruction limits
prospective decision rules
typed aggregation handoff provenance
measurement-selection versus observed-result separation
```

It does not establish empirical truth, instrument validity, metrological traceability, external applicability, diagnosis, causality, independent validation, method superiority, or permanent method independence.

## 13. Next

Run a separately precommitted negative / blocked / insufficient / out-of-scope Measurement challenge. Preserve any protocol-compliant negative terminal as valid evidence rather than treating it as method failure.
