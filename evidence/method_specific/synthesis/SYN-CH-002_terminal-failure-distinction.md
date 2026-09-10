# SYN-CH-002 Terminal-Failure Distinction Result / DSD 합성론 Negative-Failure Challenge 결과

Status: **EXECUTED — PASS**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Precommit commit: `09fc616835880e28aabcb4e9b47182d620a0da30`  
Precommit blob: `69c362e16c31fd887dadd6474e310c372a678fd4`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-002
CASE_CLASS: negative_failure
CASE_ORIGIN: constructed_same_session
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
SUBCASES: I, U, B
```

The immutable precommit was read after its commit and before this result was created. No frozen candidate, coverage class, composition-rule availability state, expected terminal status, or scoring criterion was modified.

## 2. Subcase I — exhaustive all rejected

Frozen task:

```text
SYNTHESIS_TASK_ID: SYN-TASK-002-I
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
COMPOSITION_CANDIDATE_BASIS: {I1,I2}
COMPOSITION_COVERAGE: exhaustive relative to SYN-TASK-002-I
RULE: R_PAIR_MATCH
```

Execution:

```text
I1 = L ⊙ R
  H1 COMPONENT_ADMISSION: PASS
  H2 INTERFACE_MATCH: FAIL
    L.output alpha
    R.input beta
    alpha != beta
  SYNTHESIS_CANDIDATE_RESULT: rejected
  FAILURE_SET: {H2}

I2 = R ⊙ L
  H1 COMPONENT_ADMISSION: PASS
  H2 INTERFACE_MATCH: FAIL
    R.output NONE
    L.input NONE
    absent ports are not an interface match
  SYNTHESIS_CANDIDATE_RESULT: rejected
  FAILURE_SET: {H2}
```

Closure:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_I: {}
COMPOSITION_COVERAGE_I: exhaustive
TERMINAL_SYNTHESIS_STATUS_I: SYNTHESIS_INFEASIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE_I: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_I: NOT_ASSESSED
```

The infeasibility claim is scoped only to the frozen exhaustive candidate universe under `R_PAIR_MATCH`. It is not generalized to other components, rules, or unbounded composition spaces.

## 3. Subcase U — non-exhaustive uniqueness closure

Frozen task:

```text
SYNTHESIS_TASK_ID: SYN-TASK-002-U
CLAIMED_OUTPUT_LEVEL: UNIQUE_SYNTHESIZED_TARGET
COMPONENT_INVENTORY: {A,B,C}
EVALUATED_CANDIDATE_BASIS: {U1,U2}
COMPOSITION_COVERAGE: non_exhaustive
RULE: R_PAIR_MATCH
```

Execution within the frozen evaluated basis:

```text
U1 = A ⊙ B
  H1 COMPONENT_ADMISSION: PASS
  H2 INTERFACE_MATCH: PASS
    gamma -> gamma
  SYNTHESIS_CANDIDATE_RESULT: admissible
  FAILURE_SET: NONE

U2 = B ⊙ A
  H1 COMPONENT_ADMISSION: PASS
  H2 INTERFACE_MATCH: FAIL
    B.output NONE
    A.input NONE
    absent ports are not an interface match
  SYNTHESIS_CANDIDATE_RESULT: rejected
  FAILURE_SET: {H2}
```

Covered family:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_U_WITHIN_COVERAGE: {U1}
```

The candidate `A ⊙ C` was not evaluated because it was deliberately outside the frozen candidate basis. Its presence in the supplied inventory demonstrates that the evaluated coverage is genuinely non-exhaustive and that a materially distinct additional admissible target may remain.

Therefore:

```text
UNIQUE_SYNTHESIZED_TARGET: not established
TERMINAL_SYNTHESIS_STATUS_U: SYNTHESIS_UNDERDETERMINED
SYNTHESIS_PROTOCOL_CONFORMANCE_U: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_U: NOT_ASSESSED
```

A locally admissible `U1` does not make the requested **unique-target** claim admissible when the frozen composition coverage is insufficient for uniqueness closure.

## 4. Subcase B — required composition rule unavailable

Frozen task:

```text
SYNTHESIS_TASK_ID: SYN-TASK-002-B
CLAIMED_OUTPUT_LEVEL: SYNTHESIZED_TARGET
COMPONENT_SET_OR_FAMILY: {P,Q}
COMPOSITION_RULE: UNAVAILABLE
COMPOSITION_RULE_SOURCE: UNAVAILABLE
COMPOSITION_COVERAGE: unknown
```

Execution stops before rule-dependent candidate construction or interface evaluation.

```text
COMPONENT_RECORDS: available
COMPOSITION_RULE: unavailable
SUBSTANTIVE_CANDIDATE_EVALUATION: not performed
SYNTHESIS_ADMISSIBLE_FAMILY_B: not constructed
RULE_DEPENDENT_INTERFACE_VERDICT: not evaluated
RULE_DEPENDENT_RETENTION_VERDICT: not evaluated
```

No substitute rule was imported from Formation Clause VII, notation, coexistence, Design, Transformation, Aggregation, or any other neighboring method.

Result:

```text
BLOCKING_BASIS: required composition rule unavailable
TERMINAL_SYNTHESIS_STATUS_B: SYNTHESIS_BLOCKED
SYNTHESIS_PROTOCOL_CONFORMANCE_B: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_B: NOT_ASSESSED
```

This is not an ordinary rejected candidate. The requested Synthesis operation cannot be substantively executed because a claim-required input is absent.

## 5. Cross-subcase terminal-status distinction

Protocol v0.1 preserved the three non-success forms exactly as precommitted:

```text
Subcase I
  exhaustive all rejected
  -> SYNTHESIS_INFEASIBLE

Subcase U
  at least one locally admissible candidate
  + non-exhaustive coverage
  + requested uniqueness closure unsupported
  -> SYNTHESIS_UNDERDETERMINED

Subcase B
  composition rule unavailable before substantive evaluation
  -> SYNTHESIS_BLOCKED
```

The run therefore preserves:

```text
REJECTED_UNDER_EXHAUSTIVE_COVERAGE
!= INSUFFICIENT_COVERAGE_FOR_CLOSURE
!= MISSING_REQUIRED_INPUT
```

and also:

```text
local admissibility
!= requested output-level closure
```

## 6. Three-ledger separation

Each subcase is protocol-conformant even though none yields the same terminal status:

```text
I: SYNTHESIS_INFEASIBLE      / CONFORMANT / NOT_ASSESSED
U: SYNTHESIS_UNDERDETERMINED / CONFORMANT / NOT_ASSESSED
B: SYNTHESIS_BLOCKED         / CONFORMANT / NOT_ASSESSED
```

No baseline was frozen, so `GAIN_ESTABLISHED` and `NO_GAIN` are unavailable from this challenge.

## 7. Precommitted scoring

```text
A. common precommit integrity           6 / 6 PASS
B. Subcase I                            9 / 9 PASS
C. Subcase U                           10 / 10 PASS
D. Subcase B                            6 / 6 PASS
E. cross-subcase status discipline      5 / 5 PASS

PRECOMMITTED_REQUIRED_CHECKS: 36
PASSED: 36
FAILED: 0
CHALLENGE_VERDICT: PASS
```

No check was deleted or weakened after execution.

## 8. Direct-evidence increment

```text
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASE_INCREMENT: +1
```

Post-run evidence state attributable to the first two Protocol-v0.1 challenges:

```text
DIRECT_SYNTHESIS_PILOTS: 2
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

The three subcases remain one direct pilot because they share one frozen `CASE_ID`.

## 9. Protocol-defect check

No Protocol-v0.1 defect was exposed by this challenge.

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

This does not prove Protocol v0.1 complete; it only means this challenge did not force a revision.

## 10. Limits

This case directly supports terminal-status discrimination under a frozen finite symbolic fixture.

It does **not** establish:

```text
external applicability
method superiority over a competent baseline
NO_GAIN behavior
executable Design/Transformation/Aggregation/Optimization boundary robustness
reproducibility beyond this project
independent evaluator agreement
Synthesis method maturity
universal infeasibility criteria outside declared coverage
```

The next evidence task should be a separately precommitted direct boundary challenge under Protocol v0.1, preferably forcing Synthesis to reject or hand off hidden Design, Transformation, Aggregation, or Optimization operations without absorbing their verdicts.
