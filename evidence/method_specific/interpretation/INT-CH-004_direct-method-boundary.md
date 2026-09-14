# INT-CH-004 Result / DSD Interpretation Direct Method-Boundary Challenge

Status: **EXECUTED AGAINST FROZEN PRECOMMIT**  
Date: **2026-09-15**

## 1. Identity

```text
CASE_ID: INT-CH-004
CASE_CLASS: direct_method_boundary_challenge
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
PROTOCOL: Interpretation Protocol v0.1
PROTOCOL_BLOB: dc3c3a46ba170b3b7565a59a7113c473fb02b463
PRECOMMIT_COMMIT: fb2657f37a1e9f784337f4502000a66d10f69334
PRECOMMIT_BLOB: b8f982bacd70b3acd330e97c88f58f60b0374698
EXTERNAL_APPLICATION: no
BASELINE: none
INTERPRETATION_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No fixture, boundary vocabulary, five-interface dimensions, or scoring rule was changed after the precommit.

## 2. Pair results

### B1 — Interpretation vs Analysis

```text
SHARED_CARRIER: source record A1
INTERPRETATION_OPERATION: source/context/bridge -> source-grounded reading support
ANALYSIS_OPERATION: single-target structural decomposition/re-expression
INTERPRETATION_OUTPUT: reading support + interpretation terminal + justification provenance
ANALYSIS_OUTPUT: decomposed entities/relations/structure
FAILURE_TARGETS: unsupported/underdetermined/blocked reading vs inadequate/invalid decomposition
VALIDATION_TARGETS: source-grounded support discipline vs decomposition fidelity
BOUNDARY_FINDING: PARTIAL_OVERLAP_NOT_COLLAPSE
```

A structural decomposition can be a handoff to Interpretation, but it does not itself decide whether the source supports the requested reading.

### B2 — Interpretation vs Comparison

```text
SHARED_CARRIERS: source W + readings R1/R2
INTERPRETATION_OPERATION: evaluate support of each reading from source/context/bridge
COMPARISON_OPERATION: evaluate correspondence/divergence between R1 and R2 under supplied criterion
INTERPRETATION_OUTPUT: reading-support profile
COMPARISON_OUTPUT: comparison relation/profile
FAILURE_TARGETS: insufficient interpretive closure vs insufficient comparison map/criterion/coverage
VALIDATION_TARGETS: source-support fidelity vs correspondence/preservation fidelity
BOUNDARY_FINDING: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Two readings can be very similar or very different without that comparison deciding whether either reading is supported by the source.

### B3 — Interpretation vs Provenance

```text
SHARED_CARRIER: witness W7 and source metadata
INTERPRETATION_OPERATION: source/context/bridge -> reading
PROVENANCE_OPERATION: artifact/record -> origin/custody/source chain
INTERPRETATION_OUTPUT: reading-support profile
PROVENANCE_OUTPUT: provenance chain/status
FAILURE_TARGETS: unsupported/blocked reading vs unsupported/uncertain source-chain claim
VALIDATION_TARGETS: interpretive support discipline vs origin/custody traceability
BOUNDARY_FINDING: PARTIAL_OVERLAP_NOT_COLLAPSE
```

Provenance can constrain which witness is being interpreted, but provenance identity does not supply the witness's meaning.

### B4 — Interpretation vs Reconstruction

```text
SHARED_CARRIER: damaged source R0
INTERPRETATION_OPERATION: evaluate readings while preserving observed/reconstructed distinction
RECONSTRUCTION_OPERATION: incomplete observation -> candidate missing structure/content
INTERPRETATION_OUTPUT: reading support with reconstruction-handoff provenance
RECONSTRUCTION_OUTPUT: candidate reconstruction set/status
FAILURE_TARGETS: overclaimed reading support vs unsupported/nonunique/blocked reconstruction
VALIDATION_TARGETS: source/context/bridge support vs reconstruction admissibility/consistency
BOUNDARY_FINDING: PARTIAL_OVERLAP_NOT_COLLAPSE
```

The reconstruction candidate may be consumed as an explicit handoff, but it remains reconstructed content rather than observed source content.

### B5 — Interpretation vs Audit

```text
SHARED_CARRIER: completed Interpretation execution record I5
INTERPRETATION_OPERATION: generate source-grounded reading result
AUDIT_OPERATION: retrace I5 against frozen scope/protocol/standard
INTERPRETATION_OUTPUT: support/terminal/conformance records
AUDIT_OUTPUT: audit conformance/defect/evidence finding
FAILURE_TARGETS: interpretation support/closure failure vs audit nonconformance/defect finding
VALIDATION_TARGETS: interpretive evidence discipline vs retrace/conformance fidelity
BOUNDARY_FINDING: PARTIAL_OVERLAP_NOT_COLLAPSE
```

An Audit can evaluate an Interpretation run, but the audit verdict is not a new reading of the source.

## 3. Five-interface summary

All five frozen pairs share at least one carrier or possible handoff, but each preserves a material difference in operation, output, failure semantics, and validation target.

```text
B1 Analysis        -> PARTIAL_OVERLAP_NOT_COLLAPSE
B2 Comparison      -> PARTIAL_OVERLAP_NOT_COLLAPSE
B3 Provenance      -> PARTIAL_OVERLAP_NOT_COLLAPSE
B4 Reconstruction  -> PARTIAL_OVERLAP_NOT_COLLAPSE
B5 Audit           -> PARTIAL_OVERLAP_NOT_COLLAPSE

EXACT_COLLAPSE_CANDIDATES_FOUND: 0/5
DISTINCT_AT_TASK_INTERFACE_FINDINGS: 0/5
PARTIAL_OVERLAP_NOT_COLLAPSE_FINDINGS: 5/5
```

The absence of an exact-collapse candidate in this fixture is local evidence only and does not prove permanent irreducibility or registry survival.

## 4. Governance checks

All frozen governance distinctions were preserved:

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

## 5. Scoring

```text
A. IMMUTABILITY_PAIR_DEFINITION_CHECKS:   8/8 PASS
B1. ANALYSIS_BOUNDARY:                     8/8 PASS
B2. COMPARISON_BOUNDARY:                   8/8 PASS
B3. PROVENANCE_BOUNDARY:                   8/8 PASS
B4. RECONSTRUCTION_BOUNDARY:               8/8 PASS
B5. AUDIT_BOUNDARY:                        8/8 PASS
C. CROSS_BOUNDARY_GOVERNANCE:             10/10 PASS
TOTAL:                                    58/58 PASS
```

```text
CHALLENGE_VERDICT: PASS
PROTOCOL_DEFECT_EXPOSED: no
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 6. Counter update

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: 4
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: 3
SUCCESSFUL_POSITIVE_INTERPRETATION_CASES: 1
NEGATIVE_OR_FAILURE_INTERPRETATION_CASES: 1
METHOD_BOUNDARY_INTERPRETATION_CASES: 1
PRESERVED_FAILED_CHALLENGE_DESIGNS: 1
BASELINE_INTERPRETATION_CASES: 0
NO_GAIN_INTERPRETATION_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_INTERPRETATION_APPLICATIONS: 0
INDEPENDENT_INTERPRETATION_VALIDATION: not established
INTERPRETATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_INTERPRETATION_EVIDENCE_STATUS: validation_in_progress
```

## 7. Scope of the result

This case supports local task-interface separation under the frozen constructed fixtures. It does not establish external validity, superiority, permanent method independence, permanent non-merger, or independent validation.

## 8. Next

Precommit a fair competent baseline challenge for Interpretation. The baseline must receive the same source/context/bridge/reading-policy information as DSD Interpretation, and `NO_GAIN` must remain an admissible result. External validation remains deferred.