# DES-IEP-001 — Independent Evaluator Submission Template

Status: **BLIND SUBMISSION TEMPLATE**  
Packet: `DES-IEP-001_reviewer-packet.md`

## A. Evaluator declaration

```text
EVALUATOR_ID_OR_PSEUDONYM:
EVALUATOR_TYPE: human / separate_model_session / external_team / other
DATE_STARTED:
DATE_COMPLETED:
PRIOR_DSD_EXPOSURE:

E1_NO_REFERENCE_KEY_OR_NONCE_ACCESS: yes/no
E2_NO_ANSWER_REVEALING_DESIGN_EVIDENCE_INSPECTION_AFTER_ACCEPTANCE: yes/no
E3_ONLY_ALLOWED_MATERIALS_USED: yes/no
E4_NO_ANSWER_LEADING_FEEDBACK_AFTER_START: yes/no
E5_SUBMISSION_FROZEN_BEFORE_KEY_REVEAL: yes/no
E6_ACCIDENTAL_CONTAMINATION_OR_OTHER_DISCLOSURE: none / describe

PROCEDURAL_CLARIFICATIONS_RECEIVED:
  none / list exact question and reply
```

Do not inspect or request the hidden reference key before freezing this submission.

---

## B. Task W — WCAG candidate results

Fill one line per candidate.

```text
E1 | ADMISSIBILITY_RESULT= | FAILURE_SET=
E2 | ADMISSIBILITY_RESULT= | FAILURE_SET=
E3 | ADMISSIBILITY_RESULT= | FAILURE_SET=
E4 | ADMISSIBILITY_RESULT= | FAILURE_SET=
E5 | ADMISSIBILITY_RESULT= | FAILURE_SET=
E6 | ADMISSIBILITY_RESULT= | FAILURE_SET=
```

Task-level result:

```text
ADMISSIBLE_FAMILY_W:
TERMINAL_DESIGN_STATUS_W:
DESIGN_PROTOCOL_CONFORMANCE_W:
DESIGN_METHOD_GAIN_STATUS_W:
```

Scope answers:

```text
W-S1 FULL_WCAG_2_2_CONFORMANCE_JUSTIFIED: yes/no
W-S1_RATIONALE:

W-S2 LABEL_AT_START_IS_HARD_REQUIREMENT: yes/no
W-S2_RATIONALE:
```

---

## C. Task N — NIST AAL2 candidate results

```text
D1 | ADMISSIBILITY_RESULT= | FAILURE_SET=
D2 | ADMISSIBILITY_RESULT= | FAILURE_SET=
D3 | ADMISSIBILITY_RESULT= | FAILURE_SET=
D4 | ADMISSIBILITY_RESULT= | FAILURE_SET=
D5 | ADMISSIBILITY_RESULT= | FAILURE_SET=
D6 | ADMISSIBILITY_RESULT= | FAILURE_SET=
```

Task-level result:

```text
ADMISSIBLE_FAMILY_N:
TERMINAL_DESIGN_STATUS_N:
DESIGN_PROTOCOL_CONFORMANCE_N:
DESIGN_METHOD_GAIN_STATUS_N:
```

Scope answers:

```text
N-S1 FULL_DEPLOYED_AAL2_CONFORMANCE_JUSTIFIED: yes/no
N-S1_RATIONALE:

N-S2 EVERY_ROUTE_MUST_ITSELF_BE_PHISHING_RESISTANT: yes/no
N-S2_RATIONALE:
```

---

## D. Source/task identity confirmation

```text
SOURCE_TASK_W:
  W3C WCAG 2.2 / frozen SC 1.4.3, 2.5.3, 2.5.8 subset
  MATCHES_PACKET: yes/no

SOURCE_TASK_N:
  NIST SP 800-63B-4 / frozen AAL2 route-form subset
  MATCHES_PACKET: yes/no
```

---

## E. Evaluator critique

Optional but strongly encouraged.

```text
AMBIGUITIES_FOUND:
PROTOCOL_DEFECTS_SUSPECTED:
SOURCE_BRIDGE_DISAGREEMENTS:
CANDIDATE_OR_COVERAGE_CONCERNS:
OTHER_LIMITATIONS:
```

A disagreement is evidence and must not be edited away to match the later-revealed reference key.

---

## F. Freeze record

Before reference-key reveal, complete:

```text
SUBMISSION_FREEZE_METHOD:
SUBMISSION_FREEZE_IDENTIFIER:
SUBMISSION_FREEZE_TIME:
POST_FREEZE_EDITS_BEFORE_REVEAL: none / describe
```

After freezing, provide the immutable identifier to the project owner.
