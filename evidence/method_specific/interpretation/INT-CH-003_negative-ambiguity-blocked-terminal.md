# INT-CH-003 Result / DSD Interpretation Negative-Ambiguity-Blocked Terminal Challenge

Status: **EXECUTED — 50/50 PASS**  
Date: **2026-09-14**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**  
Precommit commit: `f7185dcfdc03781841c563fa85a689f040e923fc`  
Precommit blob: `10b8c2a4bf3b777538c990ea035f1fe5333397bb`

## 1. Evidence identity

```text
CASE_ID: INT-CH-003
CASE_CLASS: negative_ambiguity_blocked_terminal_challenge
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_APPLICATION: no
BASELINE: none
RESULT: PASS
INTERPRETATION_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The committed precommit was re-read before execution. No source record, candidate reading, scope, bridge state, ambiguity policy, expected terminal, distinction, or scoring item was changed after execution began.

## 2. N1 — legitimate plurality

Frozen source explicitly licensed both `alpha` and `beta` readings and supplied no precedence rule.

Execution:

```text
R1A marker = alpha -> SUPPORTED
R1B marker = beta  -> SUPPORTED
READING_RELATION: mutually_exclusive at token-value resolution
TERMINAL_INTERPRETATION_STATUS: INTERPRETATION_RESOLVED_MULTI
INTERPRETATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

The run did not force one reading and did not relabel legitimate plurality as failure or underdetermination.

Preserved:

```text
MULTIPLE_SUPPORTED_READINGS != INTERPRETATION_UNDERDETERMINED
AMBIGUITY != METHOD_FAILURE
```

## 3. N2 — temporal order does not settle causality

Frozen source:

```text
"The gate opened after the signal."
```

The source directly establishes temporal ordering at the frozen resolution but supplies no causal bridge.

Execution:

```text
R2A signal caused gate opening        -> UNDERDETERMINED
R2B signal merely preceded opening    -> UNDERDETERMINED
DIRECT_TEMPORAL_ORDER_SUPPORTED: yes
CAUSAL_OR_NONCAUSAL_RESOLUTION_SUPPORTED: no
TERMINAL_INTERPRETATION_STATUS: INTERPRETATION_UNDERDETERMINED
INTERPRETATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

The word `merely` was not treated as a source-supported non-causality claim; it remained one side of the unresolved requested distinction.

Preserved:

```text
TEMPORAL_ORDER != CAUSAL_INTERPRETATION
LACK_OF_CAUSAL_BRIDGE != PROOF_OF_NONCAUSALITY
```

## 4. N3 — missing required bridge

Frozen source:

```text
code = X7
```

No codebook bridge was supplied.

Execution:

```text
R3A X7 = safe   -> BLOCKED_BY_MISSING_SOURCE_OR_BRIDGE
R3B X7 = unsafe -> BLOCKED_BY_MISSING_SOURCE_OR_BRIDGE
TERMINAL_INTERPRETATION_STATUS: INTERPRETATION_BLOCKED
LABEL_SHAPE_GUESS_USED: no
INTERPRETATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

Preserved:

```text
MISSING_BRIDGE != NEGATIVE_READING
RAW_CODE != SEMANTIC_MEANING
```

## 5. N4 — source silence is not negation

Frozen source:

```text
"Unit A entered the room."
```

No key-related statement, context, or bridge was supplied.

Execution:

```text
R4A Unit A carried a key         -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
R4B Unit A did not carry a key   -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
SOURCE_SILENCE_PRESERVED: yes
NEGATION_INFERRED_FROM_SILENCE: no
TERMINAL_INTERPRETATION_STATUS: INTERPRETATION_UNDERDETERMINED
INTERPRETATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

`NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET` was not interpreted as false. Both positive and negative readings lack support within the frozen source set.

Preserved:

```text
SOURCE_SILENCE != NEGATIVE_CLAIM
NOT_SUPPORTED != FALSE
```

## 6. N5 — out of scope

Frozen source:

```text
"The vessel arrived at noon."
```

Frozen scope covers arrival-time content only. The requested authorial private emotional state has no admitted source/context/bridge basis.

Execution:

```text
READING_SUPPORT_STATUS: OUT_OF_SCOPE
TERMINAL_INTERPRETATION_STATUS: INTERPRETATION_OUT_OF_SCOPE
DIAGNOSIS_HANDOFF_INVENTED: no
RECONSTRUCTION_HANDOFF_INVENTED: no
INTERPRETATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

Preserved:

```text
OUT_OF_SCOPE != BLOCKED
OUT_OF_SCOPE != UNDERDETERMINED
OUT_OF_SCOPE_REQUEST != LICENSE_TO_DIAGNOSE_OR_RECONSTRUCT
```

## 7. Cross-task terminal matrix

```text
N1 -> two SUPPORTED readings
   -> INTERPRETATION_RESOLVED_MULTI

N2 -> causal distinction UNDERDETERMINED
   -> INTERPRETATION_UNDERDETERMINED

N3 -> required semantic bridge missing
   -> INTERPRETATION_BLOCKED

N4 -> positive and negative key claims both NOT_SUPPORTED
   -> INTERPRETATION_UNDERDETERMINED

N5 -> mental-state request outside frozen scope
   -> INTERPRETATION_OUT_OF_SCOPE
```

The same non-single surface appearance therefore does not imply one common terminal state.

## 8. Frozen distinction execution

All ten precommitted distinctions were preserved:

```text
1  MULTIPLE_SUPPORTED_READINGS != INTERPRETATION_UNDERDETERMINED            PASS
2  AMBIGUITY != CONTRADICTION                                                PASS
3  TEMPORAL_ORDER != CAUSAL_INTERPRETATION                                   PASS
4  MISSING_BRIDGE != NEGATIVE_MEMBERSHIP_OR_NEGATIVE_READING                 PASS
5  SOURCE_SILENCE != NEGATIVE_CLAIM                                          PASS
6  NOT_SUPPORTED != FALSE                                                     PASS
7  INTERPRETATION_BLOCKED != INTERPRETATION_UNDERDETERMINED                  PASS
8  OUT_OF_SCOPE != BLOCKED                                                    PASS
9  OUT_OF_SCOPE != UNDERDETERMINED                                            PASS
10 CURRENT_REQUEST_FOR_MENTAL_STATE != LICENSE_FOR_DIAGNOSIS_OR_RECONSTRUCTION PASS
```

## 9. Protocol-gate pressure

The task family directly exercised the following obligations without exposing a Protocol-v0.1 contradiction:

```text
G1  source identity lock                         PASS
G3  question/resolution/scope lock               PASS
G5  context set/provenance explicit              PASS
G6  bridge supplied-or-absent state explicit     PASS
G7  candidate readings explicit                  PASS
G8  silence/missingness preserved                PASS
G9  ambiguity/alternative policy explicit        PASS
G10 claim strength not inflated                  PASS
G11 neighboring handoffs not invented            PASS
G12 mental-state/intent obligations respected    PASS
G14 output certainty bounded by closure          PASS
```

No inactive optional DSD layer was activated merely to increase task complexity.

## 10. Precommitted scoring

```text
A. immutability / task locks                         10 / 10 PASS
B. five task executions                              25 / 25 PASS
C. cross-task distinctions                           10 / 10 PASS
D. scope / evidence / protocol discipline             5 /  5 PASS

PRECOMMITTED_REQUIRED_CHECKS:                        50
PASSED:                                               50
FAILED:                                                0
CHALLENGE_VERDICT:                                  PASS
```

No scoring item was removed, weakened, or reinterpreted after execution.

## 11. Evidence increment

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: 3
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: 2
SUCCESSFUL_POSITIVE_INTERPRETATION_CASES: 1
NEGATIVE_OR_FAILURE_INTERPRETATION_CASES: 1
PRESERVED_FAILED_CHALLENGE_DESIGNS: 1
METHOD_BOUNDARY_INTERPRETATION_CASES: 0
BASELINE_INTERPRETATION_CASES: 0
NO_GAIN_INTERPRETATION_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_INTERPRETATION_APPLICATIONS: 0
INDEPENDENT_INTERPRETATION_VALIDATION: not established
INTERPRETATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_INTERPRETATION_EVIDENCE_STATUS: validation_in_progress
```

`INT-CH-001` remains the preserved 38/40 challenge-design defect. It is not rewritten or removed by this pass.

## 12. Protocol pressure

```text
PROTOCOL_DEFECT_EXPOSED: no
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 13. Limits

This case establishes internal constructed evidence that Protocol v0.1 can preserve legitimate plurality, underdetermination, blockage, source silence, and out-of-scope results separately.

It does not establish:

```text
external-domain interpretive correctness
philological validity
historical consensus
legal interpretive validity
scientific interpretive validity
baseline gain
independent validation
independent replication
method maturity
permanent registry survival
```

## 14. Next

Precommit and execute a direct method-boundary challenge against Analysis, Comparison, Provenance, Reconstruction, and Audit. External validation remains deferred until the internal standardization sequence is complete.