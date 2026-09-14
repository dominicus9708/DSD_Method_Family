# INT-CH-002 Result — Corrected Positive Constructed Interpretation Challenge

Status: **EXECUTED — 44/44 PASS**  
Date: **2026-09-14**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**  
Protocol commit: `40110a8a779f0ac6ff93ede6414544b8ec548fdf`  
Protocol blob: `dc3c3a46ba170b3b7565a59a7113c473fb02b463`  
Precommit commit: `28ebd74146372c9d60557a51669775140c616946`  
Precommit blob: `982fc81b706665f5c768936a36de2174d6b7a84a`

## 1. Evidence identity

```text
CASE_ID: INT-CH-002
CASE_CLASS: corrected_positive_constructed_interpretation_challenge
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_SOURCE_USED: no
RESULT: PASS
INTERPRETATION_METHOD_GAIN_STATUS: NOT_ASSESSED
PRIOR_FAILED_CASE_PRESERVED: INT-CH-001
```

No task, source, policy, bridge, expected result, or score was changed after precommit.

## 2. Frozen source and bridge execution

Primary source:

```text
L1: Open the east gate only after token A is presented.
L2: At dusk, courier C may enter through the east gate.
```

Frozen bridge execution:

```text
B1 only-after:
  token A presentation is a necessary prior condition for opening
  token A presentation is not a sufficient condition forcing opening

B2 may-enter:
  permission is established
  prediction/certainty/obligation is not established
```

The run uses no context record, translation, commentary, later reception, reconstruction, aggregate, dynamics, provenance, lineage, comparison, classification, analysis, or audit handoff.

## 3. Candidate-reading results

### R1

```text
READING:
  At dusk courier C is permitted to enter through the east gate;
  opening the gate requires prior presentation of token A.

SOURCE_FEATURES_USED: L1, L2
BRIDGES_USED: B1, B2
CONTEXT_FEATURES_USED: none
READING_SUPPORT_STATUS: SUPPORTED
CLAIM_STRENGTH: BRIDGE_DEPENDENT_INTERPRETATION
```

R1 stays below direct-source-statement status because the composite formal reading depends on the declared bridge semantics.

### R2

```text
READING:
  At dusk courier C certainly enters through the east gate even if token A was not presented.

READING_SUPPORT_STATUS: NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
```

R2 fails both frozen constraints: permission is not certainty, and token A is required before opening.

### R3

```text
READING:
  Presentation of token A is sufficient by itself to require the east gate to open.

READING_SUPPORT_STATUS: NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
```

R3 reverses the frozen necessary-condition relation into sufficiency and is therefore unsupported.

## 4. Validity gates

```text
G1  PASS — source ID/version/witness explicit.
G2  PASS — PRIMARY_SOURCE role explicit; no hidden precedence.
G3  PASS — question/resolution/time/perspective frozen.
G4  PASS — translation/normalization explicitly not_applicable.
G5  PASS — CONTEXT_SET empty and provenance not_applicable explicitly frozen.
G6  PASS — B1/B2 and provenance/applicability explicit.
G7  PASS — closed candidate set R1-R3 explicit.
G8  PASS — no source silence/gap/missingness was completed or coerced.
G9  PASS — ambiguity and conflict policies explicit.
G10 PASS — claim-strength ceiling explicit and respected.
G11 PASS — all optional neighboring handoffs explicitly none.
G12 PASS — authorial-intent claim prohibited.
G13 PASS — no neighboring verdict relabelled.
G14 PASS — result remains at permission/necessary-condition resolution.
```

```text
VALIDITY_GATES: 14/14 PASS
```

## 5. Terminal result

```text
SUPPORTED_READING_SET: {R1}
TERMINAL_INTERPRETATION_STATUS: INTERPRETATION_RESOLVED_SINGLE
INTERPRETATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

Preserved distinctions:

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

## 6. Precommitted scoring

```text
A. precommit/task/source/policy immutability          10/10 PASS
B. validity gates G1-G14                              14/14 PASS
C. three candidate-reading evaluations                12/12 PASS
D. terminal/distinction/scope/conformance discipline   8/8 PASS
TOTAL                                                  44/44 PASS
```

```text
CHALLENGE_VERDICT: PASS
PROTOCOL_DEFECT_EXPOSED: no
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 7. Evidence effect

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: 2
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: 1
SUCCESSFUL_POSITIVE_INTERPRETATION_CASES: 1
PRESERVED_FAILED_CHALLENGE_DESIGNS: 1
BASELINE_INTERPRETATION_CASES: 0
NO_GAIN_INTERPRETATION_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_INTERPRETATION_APPLICATIONS: 0
INDEPENDENT_INTERPRETATION_VALIDATION: not established
INTERPRETATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_INTERPRETATION_EVIDENCE_STATUS: validation_in_progress
```

The PASS is constructed same-project evidence only.

## 8. Limits

This case does not establish external-domain validity, comparative gain, independent validation, independent replication, practical superiority, universal interpretive adequacy, or method-registry survival.

## 9. Next

Precommit and execute the negative/ambiguity/blocked-terminal challenge. It must pressure at least:

```text
INTERPRETATION_RESOLVED_MULTI
INTERPRETATION_UNDERDETERMINED
INTERPRETATION_BLOCKED
INTERPRETATION_OUT_OF_SCOPE
source silence != negation
witness conflict != hidden harmonization
missing source != reconstructed source
```

No external corpus is used.