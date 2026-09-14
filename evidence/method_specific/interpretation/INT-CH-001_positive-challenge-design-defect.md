# INT-CH-001 Result — Positive Challenge Design Defect Preserved

Status: **EXECUTED — 38/40 FAIL / CHALLENGE_DESIGN_DEFECT**  
Date: **2026-09-14**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**  
Protocol commit: `40110a8a779f0ac6ff93ede6414544b8ec548fdf`  
Protocol blob: `dc3c3a46ba170b3b7565a59a7113c473fb02b463`  
Precommit commit: `f932971c1144f1a2fd49db5927a8765e498e6e51`  
Precommit blob: `7a18e74b35aebbfe0768407aa274560384ce46d5`

## 1. Evidence identity

```text
CASE_ID: INT-CH-001
CASE_CLASS: positive_constructed_interpretation_challenge
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_SOURCE_USED: no
RESULT: FAIL
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_DEFECT_EXPOSED: no
INTERPRETATION_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The precommit was not repaired after execution began.

## 2. Candidate-reading execution

The source and bridge semantics themselves produce the frozen candidate results:

```text
R1 -> SUPPORTED
      CLAIM_STRENGTH: BRIDGE_DEPENDENT_INTERPRETATION

R2 -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET

R3 -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET

SUPPORTED_READING_SET: {R1}
TERMINAL_INTERPRETATION_STATUS: INTERPRETATION_RESOLVED_SINGLE
```

The source-level distinctions also hold:

```text
PERMISSION != PREDICTION
PERMISSION != OBLIGATION
NECESSARY_CONDITION != SUFFICIENT_CONDITION
SOURCE_RECORD != INTERPRETATION
BRIDGE_DEPENDENT_INTERPRETATION != DIRECT_SOURCE_STATEMENT
UNSUPPORTED_READING != METHOD_FAILURE
```

## 3. Validity-gate audit

```text
G1  PASS — source ID/version locked as SRC-001-v1.
G2  PASS — PRIMARY_SOURCE role explicit.
G3  PASS — question, resolution, temporal scope, perspective scope frozen.
G4  PASS — precommit explicitly required translation/normalization as not_applicable.
G5  FAIL — CONTEXT_SET and CONTEXT_PROVENANCE were not explicitly frozen as empty/not_applicable.
G6  PASS — B1/B2 and fixture provenance explicit.
G7  PASS — R1/R2/R3 candidate set explicit.
G8  PASS — no damaged/missing source content was introduced or completed.
G9  FAIL — AMBIGUITY_POLICY and CONFLICT_POLICY were not explicitly frozen.
G10 PASS — candidate R1 claim strength was precommitted and no stronger source-fact status was issued.
G11 PASS — no reconstruction/aggregation or other neighboring handoff was actually used.
G12 PASS — no authorial-intent/original-context claim requested.
G13 PASS — no neighboring-method verdict relabelled.
G14 PASS — output stayed at the frozen permission/necessary-condition resolution.
```

```text
VALIDITY_GATES: 12/14 PASS
```

The two failed gates are precommit completeness defects. They do not contradict Protocol v0.1; they demonstrate that the protocol rejects an incompletely locked fixture even when the substantive reading happens to be straightforward.

## 4. Precommitted scoring

```text
A. precommit / task / source immutability             8/8 PASS
B. validity gates G1-G14                            12/14 FAIL
C. three candidate-reading evaluations              12/12 PASS
D. terminal / distinction / scope discipline          6/6 PASS
TOTAL                                                38/40 FAIL
```

Precommitted threshold was 40/40, therefore:

```text
CHALLENGE_VERDICT: FAIL
```

No scoring item was removed or weakened.

## 5. Failure interpretation

```text
SUBSTANTIVE_READING_MATCH: yes
PROTOCOL_CONFORMANCE_FOR_RUN: NONCONFORMANT due incomplete precommit locks
CHALLENGE_DESIGN_DEFECT: yes
PROTOCOL_DEFECT_EXPOSED: no
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The defect is not repaired in place. A new Case ID must freeze explicit empty/not-applicable context records plus ambiguity/conflict policies before rerunning a positive fixture.

## 6. Evidence effect

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: 1
SUCCESSFUL_POSITIVE_INTERPRETATION_CASES: 0
PRESERVED_FAILED_CHALLENGE_DESIGNS: 1
EXTERNAL_INTERPRETATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INTERPRETATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_INTERPRETATION_EVIDENCE_STATUS: validation_in_progress
```

This failure is internal constructed evidence about evaluation discipline. It does not count as external validation or positive method success.

## 7. Next

Create a prospective corrected positive challenge under a new Case ID. The corrected precommit must explicitly freeze:

```text
CONTEXT_SET
CONTEXT_PROVENANCE
AMBIGUITY_POLICY
CONFLICT_POLICY
MISSING_SOURCE_POLICY
CLAIM_STRENGTH_LIMIT
OPTIONAL_HANDOFF_STATUS
```

The source/bridge fixture may be reused only under the new immutable precommit, with the failed INT-CH-001 record preserved.