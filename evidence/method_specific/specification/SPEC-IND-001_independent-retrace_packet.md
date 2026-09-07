# SPEC-IND-001 — Independent Evaluator Retrace Packet

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Status: AWAITING_INDEPENDENT_EVALUATOR
Evidence class if completed: method-specific independent-evaluator retrace

## 1. Purpose

This packet is designed for a reviewer who has not participated in the DSD Specification development conversation.

The reviewer should apply `methods/03_specification/PROTOCOL_v1.0.md` to the eight locked cases below and return one `PRIMARY_CLASS` for each case, plus the requested supporting fields.

The canonical expected classification sequence was cryptographically committed in a separate public commitment record before any independent reviewer result exists. The answer sequence itself is not included in this packet.

This packet does not itself count as independent validation. It becomes independent-evaluator evidence only after a genuinely separate reviewer completes it without access to an answer key.

## 2. Reviewer instructions

For each case, report:

```text
CASE_ID:
PRIMARY_CLASS:
FINAL_SPEC_STATUS_IF_APPLICABLE:
SOURCE_OPENNESS_STATUS_IF_ACTIVE:
DOWNSTREAM_DETERMINACY_STATUS_IF_ACTIVE:
HARD_FAILURE_IF_ANY:
GUARDRAIL_VERDICT_IF_ACTIVE:
SHORT_REASON:
```

Choose exactly one `PRIMARY_CLASS` from:

```text
SOURCE_INTENTIONAL_OPENNESS_SUFFICIENT
SPEC_UNDERSPECIFIED
SPEC_CONTRADICTION
SPEC_NO_GAIN
SPEC_OVERCONSTRAINED
SPEC_WRONG_STANDARD
SOURCE_FACT_INVENTION
DECLARED_DERIVATIVE_VIEW_ACCEPTABLE
```

Do not browse the DSD evidence folders for prior answers. The protocol itself may be read in full.

No score should be assigned if the reviewer has already seen the committed canonical answer sequence.

## 3. Locked cases

### IND-01 — bounded open choice sufficient for the task

Source statement:

> A qualified reviewer may choose procedure A or procedure B after considering local site conditions. Either procedure is permitted.

Declared downstream task:

> Check whether the submitted procedure is one of the source-permitted procedures and whether the choice was made by the designated reviewer. Do not decide whether A or B is intrinsically better.

No additional source constraint ranks A over B.

### IND-02 — same source, stronger automation task

Source statement:

> A qualified reviewer may choose procedure A or procedure B after considering local site conditions. Either procedure is permitted.

Declared downstream task:

> Without receiving any local site-condition input and without human review, automatically decide whether A or B is the uniquely correct procedure for every case.

No additional decision rule is supplied.

### IND-03 — jointly active incompatible requirements

Source statements, both active under the same condition `C`:

```text
R1: If C holds, the device shall be OFF.
R2: If C holds, the device shall be ON.
```

No priority, exception, timing separation, or conflict-resolution rule is supplied.

Declared downstream task:

> Produce one active-state specification for condition C.

### IND-04 — already complete external specification

Source description:

> The external baseline is an authoritative machine-readable specification. For the declared standalone validation task it already provides stable requirement IDs, typed inputs, activation conditions, dependencies, allowed alternatives, violation conditions, unresolved conditions, provenance, and the applicable external validation standard. A competent validator already consumes that representation directly.

Declared downstream task:

> Re-express the same information for the same standalone validation task, without any receiving DSD method handoff requirement.

No missing distinction, ambiguity reduction, traceability gap, or additional checkability need is identified.

### IND-05 — irrelevant mandatory dynamic layer

Source statement:

```text
At inspection time, measured temperature T must satisfy T <= 80 °C.
```

Declared downstream task:

> Check the current inspection value only.

A proposed DSD specification makes `DYNAMICS_LAYER` mandatory and requires a complete historical lineage of all earlier temperature values even though neither the source nor the downstream task uses temporal history.

### IND-06 — external standard replaced by internal consistency

Source statement:

> Conformance shall be determined under External Standard E by the competent authority specified in E.

Declared downstream task:

> Record the conformance requirement while preserving the external validation authority.

A proposed DSD specification states:

> If the DSD record is internally structurally consistent, the target is conformant under External Standard E; no external validation is required.

### IND-07 — invented threshold closes an unresolved source

Source statement:

> The reviewer shall reject values judged excessively high under the documented review criteria. The numeric threshold is not present in the supplied source packet.

Declared downstream task:

> Represent the supplied packet only; do not consult missing external criteria.

A proposed DSD specification inserts:

```text
REJECTION_THRESHOLD = 7
REQUIRED_OR_OPTIONAL = required
```

No source evidence supports the value 7.

### IND-08 — explicitly declared derivative viewpoint

Source statement:

> Provide a concise prose summary of the operating requirements for human readers.

Declared downstream transformation task:

> In addition to preserving the prose source, create a typed DSD derivative view so that a later DSD Audit can consume the requirements. Label the typed representation as a DSD-added derivative structure and do not attribute it to the source author.

The resulting DSD record preserves the source prose, declares `VIEWPOINT_CHANGE_DECLARED: yes`, labels its additional typed structure as derivative, and does not strengthen any source requirement.

## 4. Independence requirements

For evidence to count as independent-evaluator validation:

```text
REVIEWER_NOT_PART_OF_ORIGINAL_DSD_SPECIFICATION_DEVELOPMENT: yes
REVIEWER_DID_NOT_SEE_CANONICAL_ANSWER_SEQUENCE: yes
REVIEWER_DID_NOT_RECEIVE_CASE-SPECIFIC_HINTS_BEYOND_THIS_PACKET: yes
REVIEWER_PROTOCOL_AVAILABLE: yes
REVIEWER_RESULT_FROZEN_BEFORE_ANSWER_COMPARISON: yes
```

A different prompt to the same continuous evaluator/session is not sufficient.
A software validator alone is not sufficient for the semantic classifications in this packet.

## 5. Scoring rule after independent submission

After the independent result is frozen:

1. Canonicalize each response as `CASE_ID|PRIMARY_CLASS` in case-ID order.
2. Join the eight lines with `\n` and no trailing newline.
3. Compare the SHA-256 of the reconstructed canonical expected sequence with the precommitted hash record.
4. Only then reveal/record the expected sequence and calculate exact matches.

Primary score:

```text
EXACT_PRIMARY_CLASS_MATCHES: x/8
```

Secondary diagnostics may compare openness/determinacy, hard-failure, final-status, and guardrail fields, but they must not alter the precommitted primary score.

## 6. Limits

This packet is constructed evidence, not an external-domain application.
It tests semantic retraceability of DSD Specification v1.0, not superiority over other specification methods.
The current project evaluator must not self-complete this packet and label the result independent.
