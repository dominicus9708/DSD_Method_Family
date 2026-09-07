# SPEC-IND-001 — Canonical Answer Commitment

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Packet: `SPEC-IND-001_independent-retrace_packet.md`
Status: PRECOMMITTED_EXPECTED-SEQUENCE_HASH_ONLY

## Canonicalization

The hidden expected sequence is eight lines in ascending case-ID order.
Each line has exactly this form:

```text
CASE_ID|PRIMARY_CLASS
```

Lines are joined with `\n` and there is no trailing newline.

Allowed `PRIMARY_CLASS` vocabulary is exactly the vocabulary printed in the reviewer packet.

## SHA-256 commitment

```text
8655a3adc0e953c7de4e69d6732d3142a82717b7eebae938229ecb2f425d0bfe
```

## Anti-post-hoc rule

The expected sequence must not be changed after an independent reviewer submission is received.
When the answer sequence is later reconstructed/revealed, its canonicalized SHA-256 must match this commitment before scoring is reported.

This commitment does not itself reveal or count the independent result.
