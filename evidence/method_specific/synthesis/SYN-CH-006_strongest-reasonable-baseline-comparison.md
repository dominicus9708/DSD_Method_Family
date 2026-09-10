# SYN-CH-006 Strongest-Reasonable-Baseline Result / DSD 합성론 Broader Baseline 결과

Status: **EXECUTED — PASS / NO_GAIN**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Precommit commit: `4a6c1fe7c702a0fd04bb01a029a9672bc5c7b6d1`  
Precommit blob: `5f210fe84ea8ade1bf34449f1a09236bff03c45e`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-006
CASE_CLASS: strongest_reasonable_baseline_comparison
CASE_ORIGIN: constructed_same_session
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
BASELINE: B1_TYPED_COMPOSITION_GRAPH_CHECKER
```

The immutable precommit was fetched after commit and before execution. No candidate, hard condition, staging rule, composition-law profile, equivalence rule, baseline capability, gain criterion, or scoring item was changed.

## 2. DSD Synthesis execution

The frozen hard-condition sequence is:

```text
H1 COMPONENT_ADMISSION
H2 INTERFACE_COMPATIBILITY
H3 WHOLE_READINESS_DEFINED through L_READY
H4 RELATION_RETENTION
H5 INHERITED_FORMATION_BACKGROUND through F_FORM
```

`H1-H2` are structural prerequisites. If either fails, `H3-H5` are `NOT_REACHED` and do not enter the failure set.

### A1

```text
A1 = ((SRC ⊙ M0) ⊙ SNK), RETAIN_ALL
H1 PASS
H2 PASS
L_READY(M0): DEFINED_ZERO -> whole.readiness DEFINED_ZERO
H3 PASS
relations retained: {r(SRC,M0), r(M0,SNK)}
H4 PASS
F_FORM: same_background
H5 PASS
RESULT: admissible
FAILURE_SET: NONE
CANONICAL_CLASS: C0
```

### A2

```text
A2 = (SRC ⊙ (M0 ⊙ SNK)), RETAIN_ALL
H1 PASS
H2 PASS
L_READY(M0): DEFINED_ZERO -> whole.readiness DEFINED_ZERO
H3 PASS
relations retained: {r(SRC,M0), r(M0,SNK)}
H4 PASS
F_FORM: same_background
H5 PASS
RESULT: admissible
FAILURE_SET: NONE
CANONICAL_CLASS: C0
```

Under the supplied associativity and frozen canonicalization rule, the grouping syntax difference does not create a second material synthesized target.

### A3

```text
A3 = ((SRC ⊙ M1) ⊙ SNK), RETAIN_ALL
H1 PASS
H2 PASS
L_READY(M1): DEFINED_NONZERO -> whole.readiness DEFINED_NONZERO
H3 PASS
relations retained: {r(SRC,M1), r(M1,SNK)}
H4 PASS
F_FORM: same_background
H5 PASS
RESULT: admissible
FAILURE_SET: NONE
CANONICAL_CLASS: C1
```

### A4

```text
A4 = (SRC ⊙ (M1 ⊙ SNK)), RETAIN_ALL
H1 PASS
H2 PASS
L_READY(M1): DEFINED_NONZERO -> whole.readiness DEFINED_NONZERO
H3 PASS
relations retained: {r(SRC,M1), r(M1,SNK)}
H4 PASS
F_FORM: same_background
H5 PASS
RESULT: admissible
FAILURE_SET: NONE
CANONICAL_CLASS: C1
```

Again the supplied associativity/canonicalization rule identifies A3 and A4 at the declared target resolution.

### A5

```text
A5 = ((SRC ⊙ MU) ⊙ SNK), RETAIN_ALL
H1 PASS
H2 PASS
L_READY(MU): APPLICABLE_BUT_UNDEFINED -> whole.readiness APPLICABLE_BUT_UNDEFINED
H3 FAIL
H4 PASS
H5 PASS
RESULT: rejected
FAILURE_SET: {H3}
```

The component Property does not become a defined whole Property merely because the interfaces compose.

### A6

```text
A6 = ((SRC ⊙ MX) ⊙ SNK), RETAIN_ALL
H1 PASS
H2 FAIL because SRC.output alpha != MX.input delta
H3 NOT_REACHED
H4 NOT_REACHED
H5 NOT_REACHED
RESULT: rejected
FAILURE_SET: {H2}
```

No whole-level property, relation-retention, or formation-effect claim was fabricated after structural composition failed.

### A7

```text
A7 = ((SRC ⊙ ML) ⊙ SNK), DROP_FIRST_RELATION
H1 PASS
H2 PASS
L_READY(ML): DEFINED_NONZERO -> whole.readiness DEFINED_NONZERO
H3 PASS
retained relations: {r(ML,SNK)}
missing relation: r(SRC,ML)
H4 FAIL
F_FORM: same_background
H5 PASS
RESULT: rejected
FAILURE_SET: {H4}
```

Structural interface compatibility is therefore kept separate from required relation retention.

### A8

```text
A8 = ((SRC ⊙ MN) ⊙ SNK), RETAIN_ALL
H1 PASS
H2 PASS
L_READY(MN): DEFINED_NONZERO -> whole.readiness DEFINED_NONZERO
H3 PASS
relations retained
H4 PASS
F_FORM: new_formation_required
H5 FAIL under the task's inherited-background requirement
RESULT: rejected
FAILURE_SET: {H5}
```

The result records the formation obligation rather than silently treating the new whole as unchanged inherited formation.

## 3. DSD closure and equivalence

Raw candidate closure:

```text
RAW_ADMISSIBLE_CANDIDATES_DSD: {A1,A2,A3,A4}
```

Canonicalization:

```text
C0 = {A1,A2}
  ordered identity: SRC,M0,SNK
  whole.readiness: DEFINED_ZERO
  full relations retained
  formation: same_background

C1 = {A3,A4}
  ordered identity: SRC,M1,SNK
  whole.readiness: DEFINED_NONZERO
  full relations retained
  formation: same_background
```

Therefore:

```text
CANONICAL_SYNTHESIS_ADMISSIBLE_FAMILY_DSD: {C0,C1}
C0 != C1 at TARGET_RESOLUTION
TERMINAL_SYNTHESIS_STATUS_DSD: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE_DSD: CONFORMANT
```

No Optimization ranking, transformed representation, aggregate readout, temporal process feasibility, or external-domain validity was inferred.

## 4. Strong competent baseline execution

`B1_TYPED_COMPOSITION_GRAPH_CHECKER` received exactly the same frozen records and was explicitly permitted to preserve every claim-relevant distinction.

Execution:

```text
A1 -> admissible / NONE / C0
A2 -> admissible / NONE / C0
A3 -> admissible / NONE / C1
A4 -> admissible / NONE / C1
A5 -> rejected / {H3}
A6 -> rejected / {H2}; H3-H5 NOT_REACHED
A7 -> rejected / {H4}
A8 -> rejected / {H5}

RAW_ADMISSIBLE_CANDIDATES_B1: {A1,A2,A3,A4}
CANONICAL_ADMISSIBLE_FAMILY_B1: {C0,C1}
```

B1 preserved:

```text
DEFINED_ZERO
DEFINED_NONZERO
APPLICABLE_BUT_UNDEFINED
explicit L_READY whole-property lift
staged NOT_REACHED dependency discipline
exact retained relation sets
same_background vs new_formation_required
left/right grouping equivalence only under supplied associativity
C0 vs C1 material distinctness
raw candidate trace and canonical-class trace
```

It performed no hidden Design, Transformation, Aggregation, Optimization, or dynamic-process inference.

## 5. DSD versus B1 comparison

```text
DIMENSION                         DSD                       B1
A1-A8 verdict/failure sets       exact frozen result       exact frozen result
raw admissible family            {A1,A2,A3,A4}            {A1,A2,A3,A4}
canonical family                 {C0,C1}                  {C0,C1}
A1/A2 grouping equivalence       C0                       C0
A3/A4 grouping equivalence       C1                       C1
C0/C1 material distinction       preserved                preserved
Property status/lift             preserved                preserved
A6 NOT_REACHED staging           preserved                preserved
relation-loss distinction        preserved                preserved
formation-effect distinction     preserved                preserved
candidate/result retraceability  preserved                preserved
```

No precommitted claim-relevant superiority dimension remains unmatched by B1.

## 6. Gain evaluation

```text
G1 STATUS_AND_PROPERTY_LIFT_GAIN: NOT_ESTABLISHED
  B1 preserved the same component/whole Property status and L_READY result.

G2 FAILURE_TRACEABILITY_GAIN: NOT_ESTABLISHED
  B1 preserved the same reached failure sets and A6 NOT_REACHED staging.

G3 GROUPING_EQUIVALENCE_GAIN: NOT_ESTABLISHED
  B1 canonicalized the same left/right syntax pairs under exactly the supplied associativity rule.

G4 RELATION_RETENTION_GAIN: NOT_ESTABLISHED
  B1 preserved the same retained/lost adjacency-relation distinction.

G5 FORMATION_EFFECT_GAIN: NOT_ESTABLISHED
  B1 preserved same_background versus new_formation_required.

G6 COMPOSITION_CLOSURE_GAIN: NOT_ESTABLISHED
  B1 returned the same raw and canonical admissible families.

G7 RETRACEABILITY_GAIN: NOT_ESTABLISHED
  B1 retained enough frozen candidate/rule/status records to reconstruct every verdict and canonical class.
```

Final gain ledger:

```text
SYNTHESIS_METHOD_GAIN_STATUS: NO_GAIN
```

This is not a method failure. It means a strong non-DSD checker explicitly equipped with the same typed composition semantics matched DSD on every scored dimension in this constructed task.

## 7. Three-ledger result

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NO_GAIN
```

Correctness/conformance and comparative gain remain separate.

## 8. Precommitted scoring

```text
A. precommit / source integrity          8 / 8 PASS
B. DSD candidate checks                16 / 16 PASS
C. B1 competent-baseline checks        16 / 16 PASS
D. gain/comparison checks               9 / 9 PASS
E. scope/category checks                3 / 3 PASS

PRECOMMITTED_REQUIRED_CHECKS:          52
PASSED:                                 52
FAILED:                                  0
CHALLENGE_VERDICT:                    PASS
```

No check was deleted, weakened, or reclassified after execution.

## 9. Evidence increment

```text
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
SUCCESSFUL_BASELINE_COMPARISON_PASS_INCREMENT: +1
SUCCESSFUL_NO_GAIN_CASE_INCREMENT: +1
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

Post-run evidence state:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_CASES: 1
SUCCESSFUL_BOUNDARY_CASES: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

## 10. Protocol pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The richer test did not expose a Protocol-v0.1 contradiction or method-boundary collapse.

## 11. Limits

This result establishes the broader strongest-reasonable-baseline comparison category **only at constructed-evidence level**.

It does not establish:

```text
DSD Synthesis superiority
practical efficiency gain
external-domain applicability
cross-domain generality
reproducibility beyond this project
independent evaluator agreement
method maturity
```

The next evidence step should be the first external Synthesis application in which composition legitimacy, component/interface semantics, or an assembly grammar is supplied by a stable external public source rather than invented by the project fixture.
