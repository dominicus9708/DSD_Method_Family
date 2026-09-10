# SYN-CH-001 Positive Chain Composition Result / DSD 합성론 첫 Positive Challenge 결과

Status: **EXECUTED — PASS**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Precommit commit: `4eeba2aaa7e684460a5c824a62301b6e8ed89b77`  
Precommit blob: `3de8320f6f1f967a485c21df538c940c289b7dc6`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-001
CASE_CLASS: positive
CASE_ORIGIN: constructed_same_session
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
```

The frozen precommit was read at its immutable commit before execution.
No candidate, rule, coverage, expected result, or scoring criterion was changed.

## 2. Frozen task executed

```text
SYNTHESIS_TASK_ID: SYN-TASK-001
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
CANDIDATE_UNIVERSE: {K1,K2,K3,K4,K5,K6}
COMPOSITION_COVERAGE: exhaustive relative only to SYN-TASK-001 candidate universe
RULE: R_CHAIN_3
GROUPING: fixed_left_associated_only
PROCESS_SCOPE: static_order_only
TARGET_DSD_LAYER_SCOPE: Formation + General Property
```

The execution does not claim exhaustive coverage of every possible arrangement of the component inventory outside the six frozen candidates.

## 3. Candidate execution

### K1 — `(SRC ⊙ AD0) ⊙ SNK`

```text
H1 COMPONENT_ADMISSION: PASS
H2 ADJACENT_INTERFACE_MATCH:
  SRC.output alpha -> AD0.input alpha: PASS
  AD0.output beta -> SNK.input beta: PASS
H3 READINESS_DEFINED:
  SRC DEFINED_NONZERO: PASS
  AD0 DEFINED_ZERO: PASS
  SNK DEFINED_NONZERO: PASS
H4 SUPPORT_RETENTION: PASS
H5 RELATION_RETENTION: PASS
H6 NO_TARGET_RESOLUTION_INFORMATION_LOSS: PASS

PROPERTY_LIFT_RESULT:
  no whole-object readiness Property created

FORMATION_EFFECT:
  same_background

ASSEMBLY_PROCESS_SCOPE_RESULT:
  static_order_only

SYNTHESIS_CANDIDATE_RESULT: admissible
FAILURE_SET: NONE
```

`DEFINED_ZERO` is preserved as a defined value and is not collapsed into `APPLICABLE_BUT_UNDEFINED`.

### K2 — `(SRC ⊙ AD1) ⊙ SNK`

```text
H1: PASS
H2:
  alpha -> alpha: PASS
  beta -> beta: PASS
H3:
  SRC DEFINED_NONZERO: PASS
  AD1 DEFINED_NONZERO: PASS
  SNK DEFINED_NONZERO: PASS
H4: PASS
H5: PASS
H6: PASS

PROPERTY_LIFT_RESULT:
  no whole-object readiness Property created

FORMATION_EFFECT:
  same_background

ASSEMBLY_PROCESS_SCOPE_RESULT:
  static_order_only

SYNTHESIS_CANDIDATE_RESULT: admissible
FAILURE_SET: NONE
```

### K3 — `(SRC ⊙ ADU) ⊙ SNK`

```text
H1: PASS
H2:
  alpha -> alpha: PASS
  beta -> beta: PASS
H3:
  SRC DEFINED_NONZERO: PASS
  ADU APPLICABLE_BUT_UNDEFINED: FAIL
  SNK DEFINED_NONZERO: PASS

SYNTHESIS_CANDIDATE_RESULT: rejected
FAILURE_SET: {H3}
```

No whole Property is inferred from the component records.
H4-H6 are not fabricated as failures because the candidate does not reach successful whole construction after H3 fails.

### K4 — `(AD0 ⊙ SRC) ⊙ SNK`

```text
H1: PASS
H2:
  AD0.output beta -> SRC.input NONE: FAIL
  SRC.output alpha -> SNK.input beta: FAIL
H3: PASS for all participating component readiness records

SYNTHESIS_CANDIDATE_RESULT: rejected
FAILURE_SET: {H2}
```

The supplied noncommutative/order-sensitive rule is respected; the valid order `SRC -> AD0 -> SNK` is not used to rescue the reversed candidate.

### K5 — `(SRC ⊙ SNK) ⊙ AD0`

```text
H1: PASS
H2:
  SRC.output alpha -> SNK.input beta: FAIL
  SNK.output NONE -> AD0.input alpha: FAIL
H3: PASS

SYNTHESIS_CANDIDATE_RESULT: rejected
FAILURE_SET: {H2}
```

### K6 — `(AD1 ⊙ SNK) ⊙ SRC`

```text
H1: PASS
H2:
  AD1.output beta -> SNK.input beta: PASS
  SNK.output NONE -> SRC.input NONE: FAIL
H3: PASS

SYNTHESIS_CANDIDATE_RESULT: rejected
FAILURE_SET: {H2}
```

`NONE -> NONE` is not treated as an interface match because the frozen rule requires both ports to exist before their types may match.

## 4. Admissible family and material distinctness

```text
SYNTHESIS_ADMISSIBLE_FAMILY:
  {K1,K2}
```

Under the frozen target resolution and equivalence rule:

```text
K1 ordered sequence = SRC, AD0, SNK
K2 ordered sequence = SRC, AD1, SNK

K1 != K2 at TARGET_RESOLUTION
```

The distinction comes from the middle component identity inside the declared resolution, not merely from candidate IDs.

No candidate outside `{K1,...,K6}` is claimed evaluated.

## 5. Protocol-v0.1 boundary observations

The run directly exercised the following protocol guards:

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY
!= AUTOMATIC_COMPOSABILITY
```

All components are individually admitted, yet K4-K6 fail interface composability.

```text
DEFINED_ZERO
!= APPLICABLE_BUT_UNDEFINED
```

K1 remains admissible with `AD0 = DEFINED_ZERO`; K3 is rejected with `ADU = APPLICABLE_BUT_UNDEFINED`.

```text
COMPONENT_PROPERTY
!= WHOLE_PROPERTY
```

No synthesized whole readiness Property is inferred.

```text
STATIC_COMPOSITION_ORDER
!= TEMPORAL_ASSEMBLY_SEQUENCE
```

The result is static only and does not establish time-resolved assembly feasibility.

## 6. Three-ledger result

```text
TERMINAL_SYNTHESIS_STATUS:
  SYNTHESIS_ADMISSIBLE

SYNTHESIS_PROTOCOL_CONFORMANCE:
  CONFORMANT

SYNTHESIS_METHOD_GAIN_STATUS:
  NOT_ASSESSED
```

No baseline was frozen, so neither `GAIN_ESTABLISHED` nor `NO_GAIN` is available from this case.

## 7. Precommitted scoring

```text
A. task/rule lock integrity          8 / 8 PASS
B. candidate verdicts               6 / 6 PASS
C. rejected-candidate failure sets  4 / 4 PASS
D. success/status/retention guards  4 / 4 PASS
E. closure/material distinctness    3 / 3 PASS
F. three ledgers                    3 / 3 PASS

PRECOMMITTED_REQUIRED_CHECKS: 28
PASSED: 28
FAILED: 0
CHALLENGE_VERDICT: PASS
```

## 8. Direct-evidence increment

```text
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
POSITIVE_SYNTHESIS_CASE_INCREMENT: +1
```

Post-run Synthesis evidence state attributable to this case:

```text
DIRECT_SYNTHESIS_PILOTS: 1
POSITIVE_SYNTHESIS_CASES: 1
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

## 9. Limits

This case establishes only that Protocol v0.1 correctly executes this frozen finite symbolic positive/negative mixed composition fixture.

It does **not** establish:

```text
external applicability
method superiority over a competent baseline
NO_GAIN behavior
negative/failure terminal-status breadth
method-boundary robustness under the executable protocol
reproducibility beyond this project
independent evaluator agreement
Synthesis method maturity
universal composition semantics
```

The next evidence task should be a separately precommitted negative/failure challenge that distinguishes at least `SYNTHESIS_INFEASIBLE`, `SYNTHESIS_UNDERDETERMINED`, and `SYNTHESIS_BLOCKED` without changing Protocol v0.1 after seeing the case outcomes.
