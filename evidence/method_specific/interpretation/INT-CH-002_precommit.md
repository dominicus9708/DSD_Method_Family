# INT-CH-002 Precommit — Corrected Positive Constructed Interpretation Challenge

Status: **FROZEN BEFORE EXECUTION**  
Date: **2026-09-14**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**

## Evidence identity

```text
CASE_ID: INT-CH-002
CASE_CLASS: corrected_positive_constructed_interpretation_challenge
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_SOURCE_USED: no
BASELINE: none
INTERPRETATION_METHOD_GAIN_STATUS: NOT_ASSESSED
PRIOR_FAILED_CASE_PRESERVED: INT-CH-001
```

## Frozen task

```text
INTERPRETATION_TASK_ID: INT-TASK-002
INTERPRETIVE_QUESTION:
  determine which candidate reading is supported at permission/necessary-condition resolution
TARGET_RESOLUTION: permission + necessary-condition semantics
TEMPORAL_SCOPE: single instruction state at dusk
PERSPECTIVE_OR_ACTOR_SCOPE: courier C and east-gate opening condition only
REQUESTED_OUTPUT_LEVEL: source-grounded candidate-reading verdict + terminal interpretation status
```

## Frozen source set and roles

```text
SOURCE_ID: SRC-001-v1
SOURCE_ROLE: PRIMARY_SOURCE
SOURCE_VERSION_OR_WITNESS: v1 / single constructed witness
SOURCE_SCOPE: L1-L2 only

L1: Open the east gate only after token A is presented.
L2: At dusk, courier C may enter through the east gate.
```

## Frozen context and transformation records

```text
CONTEXT_SET: empty
CONTEXT_PROVENANCE: not_applicable
TRANSLATION_OR_NORMALIZATION_POLICY: not_applicable
LATER_RECEPTION_SET: empty
COMMENTARY_SET: empty
```

## Frozen interpretive bridges

```text
B1:
  `only after X`
  -> X is a necessary prior condition for the opening action
  -> X is not by itself a sufficient condition forcing opening

B2:
  `may enter`
  -> permission is granted
  -> no prediction, certainty, or obligation of actual entry is implied
```

```text
BRIDGE_PROVENANCE: constructed fixture declaration INT-TASK-002
BRIDGE_APPLICABILITY: exact frozen phrases only
```

## Frozen policies

```text
CANDIDATE_READING_GENERATION_POLICY: closed_precommitted_set_R1_R3
AMBIGUITY_POLICY:
  preserve any source-level ambiguity; do not choose an unstated reading
CONFLICT_POLICY:
  preserve conflict; no hidden precedence or harmonization
MISSING_SOURCE_POLICY:
  do not fill; return UNDERDETERMINED or BLOCKED according to protocol role
CLAIM_STRENGTH_LIMIT:
  BRIDGE_DEPENDENT_INTERPRETATION maximum for the supported composite reading
AUTHORIAL_INTENT_CLAIM_ALLOWED: no
OPTIONAL_HANDOFF_STATUS:
  Analysis none
  Comparison none
  Classification none
  Provenance none
  Lineage none
  Reconstruction none
  Aggregation none
  Dynamics none
  Audit none
```

## Frozen candidate readings

```text
R1:
  At dusk courier C is permitted to enter through the east gate;
  opening the gate requires prior presentation of token A.

R2:
  At dusk courier C certainly enters through the east gate even if token A was not presented.

R3:
  Presentation of token A is sufficient by itself to require the east gate to open.
```

## Frozen expected interpretation

```text
R1 -> SUPPORTED
      CLAIM_STRENGTH: BRIDGE_DEPENDENT_INTERPRETATION
R2 -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
R3 -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
SUPPORTED_READING_SET: {R1}
TERMINAL_INTERPRETATION_STATUS: INTERPRETATION_RESOLVED_SINGLE
INTERPRETATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

## Frozen distinctions

```text
PERMISSION != PREDICTION
PERMISSION != OBLIGATION
NECESSARY_CONDITION != SUFFICIENT_CONDITION
SOURCE_RECORD != INTERPRETATION
BRIDGE_DEPENDENT_INTERPRETATION != DIRECT_SOURCE_STATEMENT
UNSUPPORTED_READING != METHOD_FAILURE
EMPTY_CONTEXT_SET != MISSING_CONTEXT_RECORD
NOT_APPLICABLE_TRANSFORMATION != UNRECORDED_TRANSFORMATION
```

## Precommitted scoring

```text
A. precommit/task/source/policy immutability          10
B. validity gates G1-G14                              14
C. three candidate-reading evaluations                12
D. terminal/distinction/scope/conformance discipline   8
TOTAL                                                  44
```

Pass requires **44/44**. No criterion may be weakened after execution.

This case remains entirely constructed and internal.