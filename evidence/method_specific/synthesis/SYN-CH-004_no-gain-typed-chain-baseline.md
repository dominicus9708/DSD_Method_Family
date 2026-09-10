# SYN-CH-004 NO_GAIN Typed-Chain Baseline Result / DSD 합성론 NO_GAIN Baseline Challenge 결과

Status: **EXECUTED — PASS / NO_GAIN**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Precommit commit: `1c77a0e293551b0d9e9b0a0ba7c6bddc4d78ed8e`  
Precommit blob: `49ea58db1a659228056df966445cf21bf6405e6a`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-004
CASE_CLASS: no_gain_baseline
CASE_ORIGIN: constructed_same_session
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
BASELINE: B0_TYPED_CHAIN_CHECKER
```

The immutable precommit was read after commit and before execution. No candidate, coverage, baseline capability, target resolution, gain criterion, or scoring item was changed.

## 2. DSD Synthesis execution

Frozen hard conditions:

```text
H1 all participating components are Formation-admitted
H2 first adjacent interface exactly matches
H3 second adjacent interface exactly matches
H4 middle readiness is defined
```

Execution:

```text
Q1 = (SRC ⊙ M0) ⊙ SNK
  H1 PASS
  H2 alpha -> alpha PASS
  H3 beta -> beta PASS
  H4 DEFINED_ZERO counts as defined PASS
  RESULT: admissible
  FAILURE_SET: NONE

Q2 = (SRC ⊙ M1) ⊙ SNK
  H1 PASS
  H2 alpha -> alpha PASS
  H3 beta -> beta PASS
  H4 DEFINED_NONZERO counts as defined PASS
  RESULT: admissible
  FAILURE_SET: NONE

Q3 = (SRC ⊙ MU) ⊙ SNK
  H1 PASS
  H2 PASS
  H3 PASS
  H4 APPLICABLE_BUT_UNDEFINED is not defined FAIL
  RESULT: rejected
  FAILURE_SET: {H4}

Q4 = (SRC ⊙ MX) ⊙ SNK
  H1 PASS
  H2 alpha != delta FAIL
  H3 beta -> beta PASS
  H4 DEFINED_NONZERO PASS
  RESULT: rejected
  FAILURE_SET: {H2}

Q5 = (M1 ⊙ SRC) ⊙ SNK
  H1 PASS
  H2 M1.output beta and SRC.input NONE FAIL
  H3 SRC.output alpha != SNK.input beta FAIL
  H4 readiness(SRC) is not the middle-component readiness field required by the frozen role pattern; no additional H4 failure is added because the frozen candidate expectation and role-specific rule test H4 on the declared middle role only after the fixed candidate-role record is applied
  RESULT: rejected
  FAILURE_SET: {H2,H3}
```

Closure:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_DSD: {Q1,Q2}
COMPOSITION_COVERAGE: exhaustive relative only to SYN-TASK-004
TERMINAL_SYNTHESIS_STATUS_DSD: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE_DSD: CONFORMANT
```

`Q1` and `Q2` remain materially distinct because middle-component identity and readiness class are inside `TARGET_RESOLUTION`.

No whole-object readiness Property, temporal assembly feasibility, Optimization selection, Transformation output, or Aggregate readout was inferred.

## 3. Competent baseline execution

`B0_TYPED_CHAIN_CHECKER` received the same component identities, admission flags, typed port records, readiness status classes, `R_CHAIN_READY`, candidate basis, coverage, grouping/order lock, and target resolution.

B0 execution:

```text
Q1 -> admissible / NONE
Q2 -> admissible / NONE
Q3 -> rejected / {H4}
Q4 -> rejected / {H2}
Q5 -> rejected / {H2,H3}

BASELINE_ADMISSIBLE_FAMILY: {Q1,Q2}
BASELINE_CLOSURE:
  admissible synthesis family exists within frozen exhaustive candidate basis
```

B0 preserved:

```text
DEFINED_ZERO
DEFINED_NONZERO
APPLICABLE_BUT_UNDEFINED
```

and independently retained the complete failure set for each rejected candidate.
It also preserved Q1/Q2 as materially distinct at the frozen target resolution.

No hidden Design, Transformation, Aggregation, or Optimization was performed.

## 4. Comparison

Candidate-level comparison:

```text
             DSD                         B0
Q1           admissible / NONE           admissible / NONE
Q2           admissible / NONE           admissible / NONE
Q3           rejected / {H4}             rejected / {H4}
Q4           rejected / {H2}             rejected / {H2}
Q5           rejected / {H2,H3}          rejected / {H2,H3}
FAMILY       {Q1,Q2}                     {Q1,Q2}
DISTINCTNESS Q1 != Q2                    Q1 != Q2
```

The two procedures therefore agree on every precommitted claim-relevant dimension.

## 5. Gain evaluation

```text
G1 STATUS_DISTINCTION_GAIN: NOT_ESTABLISHED
  B0 preserved the same readiness distinctions.

G2 FAILURE_TRACEABILITY_GAIN: NOT_ESTABLISHED
  B0 preserved the same complete failure sets.

G3 COMPOSITION_CLOSURE_GAIN: NOT_ESTABLISHED
  B0 returned the same admissible family and frozen-scope closure.

G4 TARGET_DISTINCTNESS_GAIN: NOT_ESTABLISHED
  B0 preserved Q1/Q2 material distinctness at TARGET_RESOLUTION.

G5 RETRACEABILITY_GAIN: NOT_ESTABLISHED
  both procedures are retraceable from the frozen candidate/rule/status records.
```

Final gain ledger:

```text
SYNTHESIS_METHOD_GAIN_STATUS: NO_GAIN
```

`NO_GAIN` is not a failure of Synthesis correctness or conformance. It means that this competent baseline already preserved all dimensions scored in this finite task.

## 6. Three-ledger result

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NO_GAIN
```

These ledgers remain logically separate.

## 7. Precommitted scoring

```text
A. precommit integrity                 6 / 6 PASS
B. DSD candidate/closure              10 / 10 PASS
C. competent baseline                  9 / 9 PASS
D. gain checks                         7 / 7 PASS
E. scope discipline                    3 / 3 PASS

PRECOMMITTED_REQUIRED_CHECKS:         35
PASSED:                                35
FAILED:                                 0
CHALLENGE_VERDICT:                   PASS
```

No failed check was deleted or weakened after execution.

## 8. Direct-evidence increment

```text
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
NO_GAIN_SYNTHESIS_CASE_INCREMENT: +1
BASELINE_COMPARISON_CASE_INCREMENT: +1
```

Post-run Synthesis evidence state:

```text
DIRECT_SYNTHESIS_PILOTS: 4
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
NO_GAIN_SYNTHESIS_CASES: 1
BASELINE_COMPARISON_CASES: 1
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

## 9. Protocol pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The case did not expose a Protocol-v0.1 defect.

## 10. Limits

This is the first dedicated Synthesis `NO_GAIN` pilot and a first baseline-comparison case.
It does **not** establish a strongest-reasonable-baseline comparison category by itself.

It also does not establish:

```text
external applicability
cross-domain generality
reproducibility beyond this project
independent evaluator agreement
method superiority
practical efficiency advantage
Synthesis method maturity
```

The next step should use a materially broader competent baseline and a richer composition task — including at least composition equivalence/grouping or property/retention distinctions — to test a strongest-reasonable-baseline comparison without forcing DSD gain.
