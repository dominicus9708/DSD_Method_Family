# INT-CH-001 Precommit — Positive Constructed Interpretation Challenge

Status: **FROZEN BEFORE EXECUTION**  
Date: **2026-09-14**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**

## Evidence identity

```text
CASE_ID: INT-CH-001
CASE_CLASS: positive_constructed_interpretation_challenge
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_SOURCE_USED: no
BASELINE: none
INTERPRETATION_METHOD_GAIN_STATUS: NOT_ASSESSED
```

## Frozen task

```text
INTERPRETATION_TASK_ID: INT-TASK-001
INTERPRETIVE_QUESTION:
  determine which frozen candidate reading is supported at permission/condition resolution
TARGET_RESOLUTION: permission + necessary-condition semantics
TEMPORAL_SCOPE: single instruction state at dusk
PERSPECTIVE_OR_ACTOR_SCOPE: courier C and gate-opening condition only
REQUESTED_OUTPUT_LEVEL: source-grounded candidate-reading verdict + terminal interpretation status
```

## Frozen source set

Primary source `SRC-001-v1`:

```text
L1: Open the east gate only after token A is presented.
L2: At dusk, courier C may enter through the east gate.
```

Source role:

```text
SRC-001-v1: PRIMARY_SOURCE
```

No translation, commentary, later reception, provenance dispute, reconstruction, or aggregate handoff is used.

## Frozen interpretive bridges

These are fixture semantics, not external linguistic claims.

```text
B1:
  phrase `only after X`
  -> X is a necessary prior condition for the opening action
  -> X is not by itself a sufficient condition forcing opening

B2:
  phrase `may enter`
  -> permission is granted
  -> no prediction, certainty, or obligation of actual entry is implied
```

Bridge provenance: `constructed fixture declaration INT-TASK-001`.

## Candidate readings

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

TERMINAL_INTERPRETATION_STATUS: INTERPRETATION_RESOLVED_SINGLE
SUPPORTED_READING_SET: {R1}
```

## Frozen distinctions

```text
PERMISSION != PREDICTION
PERMISSION != OBLIGATION
NECESSARY_CONDITION != SUFFICIENT_CONDITION
SOURCE_RECORD != INTERPRETATION
BRIDGE_DEPENDENT_INTERPRETATION != DIRECT_SOURCE_STATEMENT
UNSUPPORTED_READING != METHOD_FAILURE
```

## Validity-gate expectations

All G1-G14 are expected to pass. `G4` is satisfied by explicit `TRANSLATION_OR_NORMALIZATION_POLICY: not_applicable`; `G11` records all optional neighboring handoffs as not used.

## Precommitted scoring

```text
A. precommit / task / source immutability            8
B. validity gates G1-G14                            14
C. three candidate-reading evaluations              12
D. terminal / distinction / scope discipline         6
TOTAL                                                40
```

Pass requires **40/40**. No item may be removed, weakened, or reinterpreted after execution.

A fixture defect discovered after this commit must be preserved under this Case ID rather than silently repaired.

This challenge does not test external validity, baseline gain, independent validation, or method maturity.