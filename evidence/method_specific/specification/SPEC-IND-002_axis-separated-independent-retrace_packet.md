# SPEC-IND-002 — Axis-Separated Independent Evaluator Retrace Packet

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Status: AWAITING_INDEPENDENT_EVALUATOR
Evidence class if completed: method-specific independent-evaluator retrace
Successor to: `SPEC-IND-001`

## 1. Purpose

This packet tests whether a genuinely separate reviewer can reproduce selected DSD Specification v1.0 judgments from the public protocol without being forced to collapse several simultaneously valid diagnostics into one global `PRIMARY_CLASS`.

Each case declares exactly one **scored target axis**. Other diagnostics may be reported as secondary information, but they do not change the score on that case.

The expected target-axis sequence is cryptographically committed in a separate public commitment record. The expected values are not included here.

This packet does not itself count as independent validation. It becomes independent-evaluator evidence only after a genuinely separate reviewer completes it without access to the committed expected values and freezes the result before answer comparison.

## 2. Reviewer instructions

Read `methods/03_specification/PROTOCOL_v1.0.md` in full.

For each case, report:

```text
CASE_ID:
TARGET_AXIS:
TARGET_AXIS_VALUE:
SECONDARY_FINAL_SPEC_STATUS_IF_ACTIVE:
SECONDARY_HARD_FAILURES_IF_ACTIVE:
SECONDARY_SOURCE_OPENNESS_STATUS_IF_ACTIVE:
SECONDARY_DOWNSTREAM_DETERMINACY_STATUS_IF_ACTIVE:
SECONDARY_GUARDRAIL_VERDICT_IF_ACTIVE:
SHORT_REASON:
```

Rules:

```text
1. Score only the TARGET_AXIS printed in the case.
2. Choose exactly one TARGET_AXIS_VALUE from the case's allowed target values.
3. Secondary diagnostics may contain additional valid protocol judgments.
4. Secondary diagnostics do not change TARGET_AXIS_VALUE.
5. Do not invent a global primary-diagnostic precedence rule.
6. Do not browse DSD evidence folders for prior answers.
7. Do not consult the answer commitment beyond verifying that it exists before review.
```

## 3. Scored target-axis vocabularies

### SOURCE_OPENNESS_STATUS

```text
SOURCE_DETERMINATE
SOURCE_INTENTIONAL_OPENNESS
OPENNESS_INTENT_UNDETERMINED
NOT_APPLICABLE
```

### DOWNSTREAM_DETERMINACY_STATUS

```text
SUFFICIENT_AT_DECLARED_RESOLUTION
UNDERDETERMINED_FOR_DECLARED_TASK
NOT_APPLICABLE
```

### FINAL_SPEC_STATUS

```text
usable
usable_with_unresolved_items
contradictory
underspecified
no_gain
```

### HARD_FAILURES

For the scored hard-failure cases in this packet, choose the **directly instantiated target hard-failure class** from the representative v1.0 hard-failure vocabulary:

```text
SOURCE_FACT_INVENTION
SILENT_REQUIRED_SOURCE_OMISSION
NORMATIVE_FORCE_STRENGTHENING
SPEC_CONTRADICTION
REQUIRED_BRIDGE_OMISSION
SPEC_WRONG_STANDARD
CLAIM_RELEVANT_STATUS_COLLAPSE
FABRICATED_DETERMINACY
```

Other secondary problems may be noted separately, but do not replace the directly instantiated scored class.

### GUARDRAIL_VERDICT

```text
INSIDE_GUARDRAILS
GUARDRAIL_PRESSURE
GUARDRAIL_EXCEEDED_RECOVERABLE
PURPOSE_OR_VIEWPOINT_DISTORTED
UNDETERMINED
```

## 4. Locked cases

### IND2-01 — bounded discretion in the source

Scored target axis:

```text
TARGET_AXIS: SOURCE_OPENNESS_STATUS
```

Source statement:

> A qualified reviewer may choose procedure A or procedure B after considering local site conditions. Either procedure is permitted.

The supplied source itself intentionally leaves the A/B selection to the qualified reviewer under local conditions. No hidden rule ranking A over B is supplied.

Declared downstream task:

> Represent whether the source itself fixes one unique procedure or intentionally permits bounded reviewer choice.

Allowed target values are the `SOURCE_OPENNESS_STATUS` vocabulary in Section 3.

---

### IND2-02 — stronger downstream task than the supplied rule can determine

Scored target axis:

```text
TARGET_AXIS: DOWNSTREAM_DETERMINACY_STATUS
```

Source statement:

> A qualified reviewer may choose procedure A or procedure B after considering local site conditions. Either procedure is permitted.

Declared downstream task:

> Without receiving local site-condition input and without human review, automatically choose the uniquely correct procedure A or B for every possible case.

No additional decision rule is supplied.

Allowed target values are the `DOWNSTREAM_DETERMINACY_STATUS` vocabulary in Section 3.

---

### IND2-03 — jointly active incompatible requirements

Scored target axis:

```text
TARGET_AXIS: FINAL_SPEC_STATUS
```

Source requirements, both active under the same condition `C`:

```text
R1: If C holds, the device shall be OFF.
R2: If C holds, the device shall be ON.
```

No priority, exception, timing separation, or conflict-resolution rule is supplied.

Declared downstream task:

> Produce one active-state specification for condition C while preserving the supplied requirements as written.

Allowed target values are the `FINAL_SPEC_STATUS` vocabulary in Section 3.

---

### IND2-04 — already complete external representation for the locked standalone task

Scored target axis:

```text
TARGET_AXIS: FINAL_SPEC_STATUS
```

Source description:

> The external baseline is authoritative and machine-readable. For this declared standalone validation task it already provides stable requirement IDs, typed inputs, activation conditions, dependencies, allowed alternatives, violation conditions, unresolved conditions, provenance, and the applicable external validation standard. A competent validator consumes that representation directly.

Declared downstream task:

> Re-express the same information for the same standalone validation task. No downstream DSD-method handoff is requested, and no missing distinction, ambiguity reduction, traceability gap, or additional checkability need has been identified.

Allowed target values are the `FINAL_SPEC_STATUS` vocabulary in Section 3.

---

### IND2-05 — replacing an external validation authority with DSD internal consistency

Scored target axis:

```text
TARGET_AXIS: HARD_FAILURES
```

Source statement:

> Conformance shall be determined under External Standard E by the competent authority specified in E.

Declared downstream task:

> Preserve the conformance requirement and the external validation authority.

Proposed DSD record:

```text
VALIDATION_STANDARD: DSD internal structural consistency
EXTERNAL_STANDARD_E_REQUIRED_FOR_CONFORMANCE: no
```

The proposal does not claim that Standard E is missing or unavailable. It deliberately substitutes a different validation basis for the source-required one.

Choose the directly instantiated scored hard-failure class from the `HARD_FAILURES` vocabulary in Section 3.

---

### IND2-06 — claim-relevant cross-carrier transfer with no bridge

Scored target axis:

```text
TARGET_AXIS: HARD_FAILURES
```

Source A defines field `load` as **instantaneous electrical current in amperes**.

Source B defines field `load` as **mechanical mass in kilograms**.

Declared downstream task:

> Transfer the value of `load` from carrier A into carrier B and use the transferred value as if the two fields were structurally identical.

Proposed DSD record:

```text
BRIDGE_DECLARED: no
TRANSFER_JUSTIFICATION: same field name "load"
```

The downstream claim depends on the cross-carrier mapping.

Choose the directly instantiated scored hard-failure class from the `HARD_FAILURES` vocabulary in Section 3.

---

### IND2-07 — explicitly declared derivative typed view

Scored target axis:

```text
TARGET_AXIS: GUARDRAIL_VERDICT
```

Source statement:

> Provide a concise prose summary of the operating requirements for human readers.

Declared transformation task:

> Preserve the prose source and additionally create a typed DSD derivative representation for a later DSD Audit. Clearly label all DSD-added structure as derivative and do not attribute it to the source author.

Resulting record:

```text
SOURCE_PROSE_PRESERVED: yes
VIEWPOINT_CHANGE_DECLARED: yes
DERIVATIVE_VIEW_LABEL: DSD typed audit carrier
SOURCE_REQUIREMENT_STRENGTHENED: no
SOURCE_PRIORITY_CHANGED: no
ADDED_DETAIL_LIMITED_TO_RECEIVING_TASK: yes
```

Allowed target values are the `GUARDRAIL_VERDICT` vocabulary in Section 3.

---

### IND2-08 — declared source priority is erased and the derivative is presented as original

Scored target axis:

```text
TARGET_AXIS: GUARDRAIL_VERDICT
```

Source statement:

> Requirement A has priority over Requirement B. If both cannot be satisfied, satisfy A first and record the unresolved B condition.

Declared downstream task:

> Create a typed DSD derivative representation while preserving source priority and clearly separating added structure from source content.

Proposed DSD record:

```text
A_PRIORITY_OVER_B: no
A_AND_B_EQUAL_PRIORITY: yes
VIEWPOINT_CHANGE_DECLARED: no
DERIVATIVE_VIEW_LABEL: none
PRESENTED_AS_SOURCE_AUTHORED_STRUCTURE: yes
```

Allowed target values are the `GUARDRAIL_VERDICT` vocabulary in Section 3.

## 5. Independence requirements

For a submission to count as independent-evaluator evidence:

```text
REVIEWER_NOT_PART_OF_ORIGINAL_DSD_SPECIFICATION_DEVELOPMENT: yes
REVIEWER_DID_NOT_SEE_EXPECTED_TARGET_AXIS_VALUES: yes
REVIEWER_DID_NOT_RECEIVE_CASE_SPECIFIC_HINTS_BEYOND_THIS_PACKET: yes
REVIEWER_PROTOCOL_AVAILABLE: yes
REVIEWER_RESULT_FROZEN_BEFORE_ANSWER_COMPARISON: yes
```

A different prompt to the same continuous evaluator/session is not sufficient.
The current project evaluator must not complete this packet and label the result independent.
A software validator alone is not sufficient for the semantic judgments in this packet.

## 6. Scoring rule after independent submission

After the independent result is frozen:

1. For each case, canonicalize only the scored target as:

```text
CASE_ID|TARGET_AXIS|TARGET_AXIS_VALUE
```

2. Order lines by ascending case ID `IND2-01` through `IND2-08`.
3. Join the eight lines with `\n` and no trailing newline.
4. Verify the SHA-256 against the precommitted expected-sequence hash.
5. Only after the hash check, reveal the expected target-axis sequence and calculate exact target-axis matches.

Primary score:

```text
EXACT_TARGET_AXIS_MATCHES: x/8
```

Secondary diagnostics may be compared descriptively, but they cannot alter the primary score.

No scalar global `PRIMARY_CLASS` is used.

## 7. Interpretation rule

A disagreement on a secondary diagnostic is not automatically a target-axis disagreement.

A target-axis match does not prove that every secondary diagnostic was exhaustively identified.

This packet tests **axis-specific semantic retraceability** under v1.0, not evaluator agreement on a total ordering of all possible diagnostics.

## 8. Limits

This packet is constructed evidence, not an external-domain application.
It does not test superiority over conventional specification methods, measured engineering benefit, or all-method interoperability.
It does not revise `SPEC-IND-001` or DSD Specification Protocol v1.0.
