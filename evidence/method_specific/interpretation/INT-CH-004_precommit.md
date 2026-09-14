# INT-CH-004 Precommit / DSD Interpretation Direct Method-Boundary Challenge

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-15**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**  
Protocol blob at freeze: `dc3c3a46ba170b3b7565a59a7113c473fb02b463`

## 1. Case identity

```text
CASE_ID: INT-CH-004
CASE_CLASS: direct_method_boundary_challenge
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_APPLICATION: no
BASELINE: none
INTERPRETATION_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The case is entirely constructed and internal. It does not use Sunzi, legal cases, historical documents, scientific corpora, or other external-domain material.

## 2. Frozen purpose

Test whether Interpretation remains operationally distinguishable from five neighboring methods even when they share source records, readings, metadata, reconstructions, or execution traces.

The five frozen neighbors are:

```text
B1 Analysis
B2 Comparison
B3 Provenance
B4 Reconstruction
B5 Audit
```

The test does not precommit method survival. Exact collapse, partial overlap, or task-interface distinction are all admissible findings.

## 3. Frozen boundary-finding vocabulary

```text
DISTINCT_AT_TASK_INTERFACE
PARTIAL_OVERLAP_NOT_COLLAPSE
EXACT_COLLAPSE_CANDIDATE
```

An `EXACT_COLLAPSE_CANDIDATE` may be issued only if no material difference remains across the five interface dimensions below at the frozen task resolution.

## 4. Frozen five-interface test

Every pair is examined on exactly these dimensions:

```text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
```

Shared data carriers, shared DSD layers, or possible handoffs do not by themselves establish collapse.

## 5. Frozen fixtures

### B1 — Interpretation vs Analysis

Shared source record:

```text
A1: "The gate opens when token G is present."
```

Frozen Interpretation task:

```text
question: does the source support the reading that G is a sufficient condition for opening?
operation: source/context/bridge -> source-grounded reading support
output: reading-support status + terminal interpretation status + provenance trace
```

Frozen Analysis task:

```text
question: what conditional structure and declared entities are present in A1?
operation: single-target structural decomposition/re-expression
output: decomposition of gate / opening / token G / conditional relation
```

The Analysis output may be handed to Interpretation, but structural decomposition is not itself a source-support verdict.

### B2 — Interpretation vs Comparison

Shared records:

```text
C1: source wording W
R1: reading alpha
R2: reading beta
```

Frozen Interpretation task:

```text
question: which supplied readings are supported by W under the frozen context/bridge?
operation: evaluate source-grounded support
output: support status for R1/R2 + interpretation terminal
```

Frozen Comparison task:

```text
question: how do R1 and R2 correspond or diverge under a supplied comparison criterion?
operation: cross-reading correspondence/divergence evaluation
output: comparison relation/profile
```

Similarity or divergence between readings does not determine whether the source supports either reading.

### B3 — Interpretation vs Provenance

Shared artifact:

```text
P1: document witness W7 with metadata origin=archive-A, copy-chain=K1->K2->W7
```

Frozen Interpretation task:

```text
question: what reading of a supplied sentence in W7 is supported under the frozen context/bridge?
operation: source/context/bridge -> reading
output: reading-support profile
```

Frozen Provenance task:

```text
question: what origin/custody/source chain is supported for W7?
operation: artifact/record -> origin/custody/source-chain trace
output: provenance chain/status
```

Provenance identity may constrain source admissibility but does not itself establish interpretive equivalence or meaning.

### B4 — Interpretation vs Reconstruction

Shared damaged source:

```text
R0: "The signal was [MISSING] before closure."
```

Frozen Reconstruction task:

```text
question: what candidate missing token(s) are admissible from supplied reconstruction constraints?
operation: incomplete observation -> candidate missing structure/content
output: reconstruction candidate set with status/provenance
```

Frozen Interpretation task:

```text
question: what can the observed source plus any explicit reconstruction handoff support?
operation: preserve observed/reconstructed distinction and evaluate readings
output: reading support with reconstruction handoff provenance
```

A reconstruction candidate is not relabelled as observed source content.

### B5 — Interpretation vs Audit

Shared completed Interpretation execution record:

```text
I5: source/context/bridge locks + candidate readings + Interpretation result
```

Frozen Interpretation task:

```text
operation: produce source-grounded reading result
output: interpretation support/terminal/conformance records
```

Frozen Audit task:

```text
operation: retrace I5 against frozen protocol/scope/standard
output: audit finding on conformance/defect/evidence discipline
```

An Interpretation result is not automatically an Audit pass, and an Audit finding is not a new interpretation reading.

## 6. Frozen boundary derivation rule

For each B1-B5 pair:

```text
if all five interface dimensions are materially identical
  -> EXACT_COLLAPSE_CANDIDATE
else if one or more carriers/steps materially overlap but at least one task-interface dimension remains materially different
  -> PARTIAL_OVERLAP_NOT_COLLAPSE
else
  -> DISTINCT_AT_TASK_INTERFACE
```

The finding is local to the frozen fixture and cannot establish permanent irreducibility.

## 7. Frozen governance rules

```text
SHARED_SOURCE_RECORD != SAME_METHOD
SHARED_DSD_LAYER != SAME_OPERATION
HANDOFF_COMPATIBILITY != METHOD_COLLAPSE
STRUCTURAL_DECOMPOSITION != INTERPRETIVE_SUPPORT
READING_COMPARISON != SOURCE_SUPPORT
PROVENANCE_IDENTITY != INTERPRETIVE_EQUIVALENCE
RECONSTRUCTED_CONTENT != OBSERVED_SOURCE_CONTENT
AUDIT_CONFORMANCE_VERDICT != INTERPRETIVE_READING
BOUNDARY_PASS != METHOD_SURVIVAL_PROOF
EXACT_COLLAPSE_CANDIDATE != AUTOMATIC_MERGER_OR_DELETION
```

## 8. Frozen scoring

```text
A. immutability / pair-definition checks             8
B1. Analysis boundary                                8
B2. Comparison boundary                              8
B3. Provenance boundary                              8
B4. Reconstruction boundary                          8
B5. Audit boundary                                   8
C. cross-boundary governance                        10
TOTAL                                                58
```

Pass requires all 58 checks. A PASS means the predeclared boundary analysis was executed consistently; it does not require any particular boundary-finding vocabulary result.

For each pair, the eight checks are:

```text
1 inputs recorded correctly
2 Interpretation operation recorded correctly
3 neighboring-method operation recorded correctly
4 outputs kept distinct where the fixture requires
5 failure/no-gain criteria compared without substitution
6 validation standards compared without substitution
7 shared carriers/handoffs not treated as automatic collapse
8 boundary finding derived by the frozen rule
```

## 9. Failure interpretation

Any failed check must be classified as:

```text
PROTOCOL_DEFECT
CHALLENGE_DESIGN_DEFECT
EXECUTION_ERROR
UNRESOLVED_CAUSE
```

No post-hoc repair under the same Case ID is allowed.

## 10. Counter policy

If the execution passes:

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: +1
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: +1
METHOD_BOUNDARY_INTERPRETATION_CASES: +1
```

No baseline, NO_GAIN, reproducibility, external-application, or independent-validation counter changes.

## 11. Next if passed

Proceed to a fair competent/strongest-reasonable baseline sequence with `NO_GAIN` admissible. External validation remains deferred until internal standardization is complete.