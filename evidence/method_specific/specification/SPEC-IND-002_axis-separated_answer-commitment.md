# SPEC-IND-002 — Axis-Separated Expected-Sequence Commitment

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Packet: `SPEC-IND-002_axis-separated-independent-retrace_packet.md`
Status: PRECOMMITTED_EXPECTED_TARGET_AXIS_HASH_ONLY

## Canonicalization

The hidden expected sequence is eight lines in ascending case-ID order.
Each line has exactly this form:

```text
CASE_ID|TARGET_AXIS|TARGET_AXIS_VALUE
```

Lines are joined with `\n` and there is no trailing newline.

The target-axis names and allowed value vocabularies are exactly those printed in the reviewer packet.

## SHA-256 commitment

```text
962c65d8ad27ca7e0af6aba201ceeb1a9fdbac80e525651942756a911dc455ff
```

## Anti-post-hoc rule

The expected target-axis sequence must not be changed after an independent reviewer submission is received.

No global `PRIMARY_CLASS` or diagnostic precedence may be added after review to alter a case's target-axis score.

When the expected sequence is later reconstructed/revealed, its canonicalized SHA-256 must match this commitment before scoring is reported.

This commitment does not itself reveal the expected values and does not count as independent evidence.
