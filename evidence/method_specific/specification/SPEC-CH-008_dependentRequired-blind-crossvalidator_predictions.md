# SPEC-CH-008 — Frozen Pre-Reveal Predictions

Date: 2026-09-08
Protocol: DSD Specification v1.0
Precommit: `92277445b73a72d7d4d9ff29f849d7068eb4244a`
Cross-validator status at this commit: **not yet invoked**

## 1. DSD requirement carrier

The active requirement structure for this challenge is:

```text
TRIGGER_PRESENCE(p)
  -> REQUIRE_PRESENCE(q1,...,qn)
```

with the following preserved boundaries:

```text
absent trigger -> dependency inactive
present trigger -> every listed dependency required
one-way declaration -> no automatic reverse dependency
empty dependency list -> no additional required property
root keyword -> nested property names do not activate root trigger
non-object instance -> not invalidated solely by dependentRequired
```

`DEPENDENCIES` is active. `PRECEDENCE_OR_PRIORITY`, source-openness, downstream-determinacy, alternatives, and prohibited-state ledgers are not needed for these locked cases.

## 2. Frozen predictions

```text
C01 VALID
C02 INVALID
C03 VALID
C04 VALID
C05 VALID
C06 INVALID
C07 VALID
C08 INVALID
C09 VALID
C10 VALID
C11 INVALID
C12 VALID
C13 VALID
C14 VALID
C15 VALID
C16 VALID
```

## 3. Pre-reveal reasoning trace

```text
C01 a present; b present -> active dependency satisfied
C02 a present; b absent -> active dependency violated
C03 a absent -> dependency inactive
C04 a present; dependency list empty -> satisfied
C05 a,c present; b,d both present -> both active dependencies satisfied
C06 a,c present; b present but d absent -> c->d violated
C07 a absent -> no reverse b->a inference
C08 a present; b absent -> active dependency violated
C09 a present and dependency requires a itself -> required name is present
C10 a present; both b and c present -> dependency list satisfied
C11 a present; c absent -> dependency list violated
C12 root a absent; nested x.a does not activate root dependency
C13 array -> keyword does not fail solely on dependentRequired
C14 string -> keyword does not fail solely on dependentRequired
C15 number -> keyword does not fail solely on dependentRequired
C16 null -> keyword does not fail solely on dependentRequired
```

Repeated controls are internally consistent before reveal:

```text
C03 == C07 -> VALID
C02 == C08 -> INVALID
```

## 4. Pre-reveal ledger

```text
UNRESOLVED_PREDICTIONS: 0
FALSE_BIDIRECTIONAL_INFERENCE_BY_DSD: 0 predicted
IRRELEVANT_OPTIONAL_LEDGERS_ACTIVATED: 0
POST_REVEAL_CHANGES_ALLOWED: no
```

The next action is to run an independent software implementation (`jsonschema` Draft202012Validator) on the exact 16 locked cases and compare its outcomes without modifying this file.
