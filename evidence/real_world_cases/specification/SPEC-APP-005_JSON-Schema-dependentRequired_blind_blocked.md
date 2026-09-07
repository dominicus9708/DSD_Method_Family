# SPEC-APP-005 — JSON Schema `dependentRequired` Blind External Test — Blocked Without Scoring

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Precommit: `154af0ae57e1cc6bc78bdefdcfb83faf1ba71a9c`
Pinned external corpus: JSON-Schema-Test-Suite commit `f6fd52a0a95472e079cbfc6ef7f089702b80e045`, `tests/draft2020-12/dependentRequired.json`

## Status

```text
STATUS: BLOCKED_BY_LABEL_ISOLATION_TOOLING
PREDICTIONS_COMMITTED: no
OFFICIAL_LABELS_SCORED: no
COUNT_AS_EXTERNAL_APPLICATION_COMPLETION: no
COUNT_AS_BLIND_EVIDENCE: no
```

The external test-suite file embeds schema, instance data, descriptive text, and expected `valid` labels in the same JSON resource. In the current connector/runtime path, the file could not be delivered to the evaluator as a redacted schema+data packet without first exposing the embedded expected labels.

The precommit required labels/descriptions to remain withheld until after predictions. Rather than weaken the criterion after encountering this tooling constraint, the run is left unscored.

## Anti-post-hoc preservation

```text
PRECOMMIT_CHANGED_AFTER_BLOCK: no
CASES_REMOVED_TO_AVOID_BLOCK: no
BLINDNESS_CLAIM_MADE: no
EXTERNAL_RESULT_INFERRED_FROM_VISIBLE_LABELS: no
```

A future run may resume only if the locked source can be transformed by an external/redaction step that does not expose expected labels to the predicting evaluator before predictions are frozen.

The separately completed `SPEC-CH-008` constructed label-withheld cross-validator challenge is not a substitute for this external application and is classified separately.
