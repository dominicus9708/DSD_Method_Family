# SYN-CH-005 Corrected NO_GAIN Typed-Chain Baseline Result / DSD 합성론 NO_GAIN Baseline Challenge 결과

Status: **EXECUTED — PASS / NO_GAIN**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Precommit commit: `3c6f3239e817343223f44a308c3554deb11fad6e`  
Precommit blob: `9c7e41e782def200a9bdda671c75962bb435ea4b`  
Preserved failed predecessor audit: `fe55899cb08946d15e8d901d68f6097837b82b7d`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-005
CASE_CLASS: no_gain_baseline
CASE_ORIGIN: constructed_same_session
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
BASELINE: B0_TYPED_CHAIN_CHECKER
```

This is a prospective corrected case. `SYN-CH-004` remains preserved as a challenge-design failure and is not rewritten into a pass.

## 2. DSD Synthesis execution

Frozen hard conditions:

```text
H1 every participating component is Formation-admitted
H2 X.output exists and exactly matches Y.input
H3 Y.output exists and exactly matches Z.input
H4 readiness(Y) is DEFINED_ZERO or DEFINED_NONZERO
```

Candidate execution:

```text
R1 = (SRC ⊙ M0) ⊙ SNK
  H1 PASS
  H2 alpha -> alpha PASS
  H3 beta -> beta PASS
  H4 readiness(M0)=DEFINED_ZERO PASS
  RESULT: admissible
  FAILURE_SET: NONE

R2 = (SRC ⊙ M1) ⊙ SNK
  H1 PASS
  H2 alpha -> alpha PASS
  H3 beta -> beta PASS
  H4 readiness(M1)=DEFINED_NONZERO PASS
  RESULT: admissible
  FAILURE_SET: NONE

R3 = (SRC ⊙ MU) ⊙ SNK
  H1 PASS
  H2 PASS
  H3 PASS
  H4 readiness(MU)=APPLICABLE_BUT_UNDEFINED FAIL
  RESULT: rejected
  FAILURE_SET: {H4}

R4 = (SRC ⊙ MX) ⊙ SNK
  H1 PASS
  H2 alpha != delta FAIL
  H3 beta -> beta PASS
  H4 readiness(MX)=DEFINED_NONZERO PASS
  RESULT: rejected
  FAILURE_SET: {H2}

R5 = (M1 ⊙ SRC) ⊙ SNK
  H1 PASS
  H2 M1.output beta and SRC.input NONE FAIL
  H3 SRC.output alpha != SNK.input beta FAIL
  H4 readiness(SRC)=DEFINED_ZERO PASS
  RESULT: rejected
  FAILURE_SET: {H2,H3}
```

Closure:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_DSD: {R1,R2}
COMPOSITION_COVERAGE: exhaustive relative only to SYN-TASK-005
TERMINAL_SYNTHESIS_STATUS_DSD: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE_DSD: CONFORMANT
```

`R1` and `R2` remain materially distinct at `TARGET_RESOLUTION` because both exact middle-component identity and readiness status/value class are preserved.

## 3. Competent baseline execution

`B0_TYPED_CHAIN_CHECKER` received exactly the same frozen component, interface, readiness, rule, grouping, candidate-basis, coverage, and target-resolution records.

Baseline execution:

```text
R1 -> admissible / NONE
R2 -> admissible / NONE
R3 -> rejected / {H4}
R4 -> rejected / {H2}
R5 -> rejected / {H2,H3}
BASELINE_ADMISSIBLE_FAMILY: {R1,R2}
```

B0 preserved the exact readiness classes, full failure sets, and R1/R2 material distinctness. It performed no hidden Design, Transformation, Aggregation, or Optimization.

## 4. Comparison

```text
             DSD                         B0
R1           admissible / NONE           admissible / NONE
R2           admissible / NONE           admissible / NONE
R3           rejected / {H4}             rejected / {H4}
R4           rejected / {H2}             rejected / {H2}
R5           rejected / {H2,H3}          rejected / {H2,H3}
FAMILY       {R1,R2}                     {R1,R2}
DISTINCTNESS R1 != R2                    R1 != R2
```

All frozen claim-relevant comparison dimensions match.

## 5. Gain evaluation

```text
G1 STATUS_DISTINCTION_GAIN: NOT_ESTABLISHED
G2 FAILURE_TRACEABILITY_GAIN: NOT_ESTABLISHED
G3 COMPOSITION_CLOSURE_GAIN: NOT_ESTABLISHED
G4 TARGET_DISTINCTNESS_GAIN: NOT_ESTABLISHED
G5 RETRACEABILITY_GAIN: NOT_ESTABLISHED
```

Therefore:

```text
SYNTHESIS_METHOD_GAIN_STATUS: NO_GAIN
```

`NO_GAIN` means the competent baseline already preserved every dimension measured in this task. It does not negate DSD Synthesis correctness or protocol conformance.

## 6. Three-ledger result

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NO_GAIN
```

## 7. Precommitted scoring

```text
A. lineage/precommit integrity          8 / 8 PASS
B. DSD checks                          10 / 10 PASS
C. competent baseline                   9 / 9 PASS
D. gain checks                          7 / 7 PASS
E. scope discipline                     3 / 3 PASS

PRECOMMITTED_REQUIRED_CHECKS:          37
PASSED:                                 37
FAILED:                                  0
CHALLENGE_VERDICT:                    PASS
```

No failed predecessor check was erased. `SYN-CH-004` remains separately preserved as 33/35 challenge-design failure.

## 8. Evidence increment

```text
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASE_INCREMENT: +1
SUCCESSFUL_BASELINE_COMPARISON_PASS_INCREMENT: +1
```

Current Synthesis direct-case state including the preserved failed predecessor:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 5
SUCCESSFUL_POSITIVE_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_CASES: 1
SUCCESSFUL_BOUNDARY_CASES: 1
SUCCESSFUL_NO_GAIN_CASES: 1
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGN: 1
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

## 9. Protocol pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The predecessor failure arose from its fixture, not from Protocol v0.1. The corrected prospective case executes without requiring a protocol change.

## 10. Limits and next step

This case establishes one successful dedicated `NO_GAIN` and one successful competent-baseline comparison at constructed-fixture level.
It does not yet establish the broader strongest-reasonable-baseline category.

It does not establish external applicability, cross-domain generality, independent validation, independent replication, practical superiority, or method maturity.

The next challenge should use a richer competent baseline and task that activates multiple Synthesis-specific dimensions at once, including composition equivalence/grouping and at least one property-lift, relation-retention, partial-residual, or formation-effect distinction, while remaining willing to return `NO_GAIN` again.
