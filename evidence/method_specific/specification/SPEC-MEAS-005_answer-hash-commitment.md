# SPEC-MEAS-005 — Gold Answer Hash Commitment

Date: 2026-09-08
Status: COMMITTED BEFORE HUMAN REVIEW

The exact gold closures are withheld from reviewer packets until a human result is frozen.

Canonicalization is fixed by the precommit:

```text
CASE_ID|sorted comma-separated impact IDs|EXTERNAL_STANDARD_REVIEW=yes/no
```

Order:

```text
O-CH1
O-CH2
O-CH3
O-CH4
H-CH1
H-CH2
H-CH3
H-CH4
```

Encoding and join rule:

```text
UTF-8
LF separators
no trailing newline
```

Committed SHA-256:

```text
bf1a27800f58589ee26f25599f105fbf4b2009c88ccff7b06118bc2049151c10
```

This hash must be verified against the plaintext gold sequence only after the evaluator submission is frozen.

```text
HUMAN_SUBMISSION_AT_COMMIT_TIME: absent
POST_REVEAL_GOLD_EDIT_ALLOWED: no
SCORING_RULE_EDIT_AFTER_HUMAN_SUBMISSION: no
```
