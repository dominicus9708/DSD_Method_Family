# INT-CH-003 Precommit / DSD Interpretation Negative-Ambiguity-Blocked Terminal Challenge

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-14**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**

## 1. Case identity

```text
CASE_ID: INT-CH-003
CASE_CLASS: negative_ambiguity_blocked_terminal_challenge
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_APPLICATION: no
BASELINE: none
INTERPRETATION_METHOD_GAIN_STATUS: NOT_ASSESSED
```

This case remains entirely internal and constructed. No external textual, legal, historical, scientific, or philological corpus is used.

## 2. Frozen purpose

Test whether Protocol v0.1 preserves legitimate non-single and non-positive interpretation outcomes without forcing one preferred reading or collapsing ambiguity, source silence, missing bridge, missing source, and out-of-scope requests into one generic failure.

The challenge passes only if all frozen task outputs and all cross-task distinctions are preserved without post-hoc source/context/bridge repair.

## 3. Frozen source-role policy

Every task separately locks:

```text
PRIMARY_SOURCE
CONTEXT_RECORD where supplied
INTERPRETIVE_BRIDGE where supplied
CANDIDATE_READING_SET
AMBIGUITY_OR_CONFLICT_POLICY
REQUESTED_OUTPUT_LEVEL
```

No translation, commentary, later reception, reconstruction, provenance, lineage, aggregation, or dynamics handoff is active unless explicitly supplied below.

## 4. Frozen tasks

### N1 — legitimate plurality

Primary source record:

```text
S1: "The marker may be read as alpha or beta under the declared grammar."
```

Frozen grammar/context explicitly licenses both readings and supplies no precedence rule.

Candidate readings:

```text
R1A: marker = alpha
R1B: marker = beta
```

Expected:

```text
R1A: SUPPORTED
R1B: SUPPORTED
READING_RELATION: mutually_exclusive at token-value resolution
TERMINAL: INTERPRETATION_RESOLVED_MULTI
```

Forbidden:

```text
forced single reading
INTERPRETATION_UNDERDETERMINED merely because plurality exists
method failure merely because plurality exists
```

### N2 — underdetermined distinction

Primary source record:

```text
S2: "The gate opened after the signal."
```

Declared question asks whether the signal was a cause or merely temporally prior.
No causal bridge or causal context record is supplied.

Candidate readings:

```text
R2A: signal caused gate opening
R2B: signal merely preceded gate opening
```

Expected:

```text
R2A: UNDERDETERMINED
R2B: UNDERDETERMINED
TERMINAL: INTERPRETATION_UNDERDETERMINED
```

Temporal ordering may be read directly, but causal resolution may not be invented.

### N3 — blocked by missing bridge

Primary source record:

```text
S3: "code = X7"
```

Declared question asks whether X7 means `safe` or `unsafe`.
A codebook bridge is claim-required but not supplied.

Candidate readings:

```text
R3A: X7 = safe
R3B: X7 = unsafe
```

Expected:

```text
R3A: BLOCKED_BY_MISSING_SOURCE_OR_BRIDGE
R3B: BLOCKED_BY_MISSING_SOURCE_OR_BRIDGE
TERMINAL: INTERPRETATION_BLOCKED
```

Forbidden: guessing from label shape or convention.

### N4 — source silence is not negation

Primary source record:

```text
S4: "Unit A entered the room."
```

Declared question asks whether Unit A carried a key.
No key statement and no context/bridge licenses an inference.

Candidate readings:

```text
R4A: Unit A carried a key
R4B: Unit A did not carry a key
```

Expected:

```text
R4A: NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
R4B: NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
TERMINAL: INTERPRETATION_UNDERDETERMINED
```

The source is silent on the requested distinction. Silence may not become the negative claim.

### N5 — out of scope

Primary source record:

```text
S5: "The vessel arrived at noon."
```

Frozen temporal/perspective scope covers arrival-time content only.
Declared request asks for the author's private emotional state.
No source/context/bridge for mental-state attribution is admitted.

Expected:

```text
READING_SUPPORT_STATUS: OUT_OF_SCOPE
TERMINAL: INTERPRETATION_OUT_OF_SCOPE
```

The task is not converted into reconstruction or diagnosis.

## 5. Frozen validity obligations

For every task, the run must preserve applicable G1-G14 gates. In particular:

```text
G1 source identity locked
G3 question/resolution/scope locked
G5 context set/provenance explicit
G6 bridges explicit or explicitly absent
G7 candidate readings explicit
G8 silence/missingness preserved
G9 ambiguity/conflict policy explicit
G10 claim strength not inflated
G11 neighboring-method handoffs not invented
G12 authorial-intent/mental-state claims not inferred without obligations
G14 output certainty does not exceed closure
```

## 6. Frozen cross-task distinctions

```text
MULTIPLE_SUPPORTED_READINGS != INTERPRETATION_UNDERDETERMINED
AMBIGUITY != CONTRADICTION
TEMPORAL_ORDER != CAUSAL_INTERPRETATION
MISSING_BRIDGE != NEGATIVE_MEMBERSHIP_OR_NEGATIVE_READING
SOURCE_SILENCE != NEGATIVE_CLAIM
NOT_SUPPORTED != FALSE
INTERPRETATION_BLOCKED != INTERPRETATION_UNDERDETERMINED
OUT_OF_SCOPE != BLOCKED
OUT_OF_SCOPE != UNDERDETERMINED
CURRENT_REQUEST_FOR_MENTAL_STATE != LICENSE_FOR_DIAGNOSIS_OR_RECONSTRUCTION
```

## 7. Frozen scoring

```text
A. immutability / task locks                         10 checks
B. five task executions                              25 checks
C. cross-task distinctions                           10 checks
D. scope / evidence / protocol discipline             5 checks
TOTAL                                                 50 checks
```

Pass requires all 50 checks.

## 8. Failure interpretation

A failed task does not automatically establish a Protocol-v0.1 defect. Any failure must be classified prospectively as one of:

```text
PROTOCOL_DEFECT
CHALLENGE_DESIGN_DEFECT
EXECUTION_ERROR
UNRESOLVED_CAUSE
```

No failed case may be repaired under the same Case ID after seeing the result.

## 9. Counter policy

If this precommitted challenge passes:

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: +1
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: +1
NEGATIVE_OR_FAILURE_INTERPRETATION_CASES: +1
```

It does not increment external applications, baseline comparisons, NO_GAIN cases, reproducibility cases, or independent validation.

## 10. Next if passed

Proceed to a separately precommitted direct method-boundary challenge against Analysis, Comparison, Provenance, Reconstruction, and Audit. External validation remains deferred.