# DSD Interpretation Task Interface v0.1 — historical draft

Status: **historical draft preserved**  
Date: **2026-09-14**

## 1. Task form

```text
supplied source set
+ source identity/version/role records
+ declared interpretive question and resolution
+ declared contextual records
+ explicit interpretive bridge(s)
-> source-grounded reading profile
```

The method does not infer a source's meaning merely from labels, a later summary, a translation choice, or an interpreter's preferred conclusion.

## 2. Required input record

```text
INTERPRETATION_TASK_ID
INTERPRETIVE_QUESTION
TARGET_RESOLUTION
SOURCE_SET
SOURCE_ID_VERSION_OR_WITNESS
SOURCE_ROLE
SOURCE_SCOPE
TEMPORAL_SCOPE
PERSPECTIVE_OR_ACTOR_SCOPE
CONTEXT_SET
CONTEXT_PROVENANCE
TRANSLATION_OR_NORMALIZATION_POLICY
INTERPRETIVE_BRIDGE_SET
BRIDGE_PROVENANCE
CANDIDATE_READING_SET_OR_GENERATION_POLICY
AMBIGUITY_POLICY
CONFLICT_POLICY
MISSING_SOURCE_POLICY
CLAIM_STRENGTH_LIMIT
REQUESTED_OUTPUT_LEVEL
```

Fields not material to the task may be explicitly `not_applicable`; they are not silently invented.

## 3. Source-role vocabulary

```text
PRIMARY_SOURCE
TRANSLATION
COMMENTARY
LATER_RECEPTION
CONTEXT_RECORD
PROVENANCE_METADATA
RECONSTRUCTION_HANDOFF
SUMMARY_OR_AGGREGATE_HANDOFF
```

A role is descriptive, not a truth ranking by itself. Any precedence or authority relation must be declared separately.

## 4. Reading-level output

Each candidate reading records:

```text
READING_ID
READING_STATEMENT
SOURCE_FEATURES_USED
CONTEXT_FEATURES_USED
BRIDGE_IDS_USED
INFERENCE_STEPS
READING_SUPPORT_STATUS
ALTERNATIVE_READINGS
FIRST_SUPPORTED_BRANCH_POINT
SOURCE_GAPS_OR_AMBIGUITIES
CLAIM_STRENGTH
LIMITS
```

`READING_SUPPORT_STATUS` uses:

```text
SUPPORTED
PARTIALLY_SUPPORTED
NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
UNDERDETERMINED
BLOCKED_BY_MISSING_SOURCE_OR_BRIDGE
OUT_OF_SCOPE
```

## 5. Terminal interpretation status

```text
INTERPRETATION_RESOLVED_SINGLE
INTERPRETATION_RESOLVED_MULTI
INTERPRETATION_UNDERDETERMINED
INTERPRETATION_BLOCKED
INTERPRETATION_OUT_OF_SCOPE
```

A multi-reading result can be valid and resolved when multiple readings remain supported at the declared resolution.

## 6. Core distinctions

```text
SOURCE_RECORD != INTERPRETATION
TRANSLATION != SOURCE_RECORD
COMMENTARY != SOURCE_RECORD
LATER_RECEPTION != ORIGINAL_CONTEXT
PARAPHRASE != SOURCE_CLAIM
SOURCE_SILENCE != NEGATIVE_CLAIM
AMBIGUITY != CONTRADICTION
MULTIPLE_SUPPORTED_READINGS != METHOD_FAILURE
CONTEXTUAL_SUPPORT != DIRECT_TEXTUAL_STATEMENT
INTERPRETIVE_BRIDGE != SOURCE_FACT
SOURCE_GAP != LICENSE_TO_FILL
CURRENT_READING != AUTHORIAL_INTENT
SAME_WORDING != SAME_MEANING_ACROSS_CONTEXT
SUMMARY_COINCIDENCE != SOURCE_EQUIVALENCE
PROVENANCE_IDENTITY != INTERPRETIVE_EQUIVALENCE
```

## 7. Minimal operation

1. Lock task, source identities/versions/witnesses, roles, scope, resolution, time, and perspective.
2. Separate source records from translations, commentary, later reception, context, provenance, reconstructions, and summaries.
3. Apply only declared translation/normalization operations and record their mapping/loss.
4. Extract claim-relevant source features without replacing absence, ambiguity, or undefined material by invented values.
5. Lock context records and their provenance separately from the source.
6. Lock interpretive bridges and bridge provenance.
7. Generate or read candidate interpretations only under the frozen generation policy.
8. Evaluate each reading against source and context separately.
9. Preserve ambiguity, conflict, alternatives, and first supported branch points.
10. Bound claim strength to the strongest support actually available.
11. Record handoffs to/from neighboring methods without absorbing their verdicts.
12. Emit terminal interpretation status, reading ledger, limits, and reproducibility record.

## 8. Method boundaries

Interpretation does not by itself:

```text
reconstruct missing source text
prove provenance or custody
prove historical lineage identity
classify a source into a taxonomy unless Classification is invoked
compare two sources/readings unless Comparison is invoked
perform single-target structural decomposition as an Analysis verdict
issue an Audit conformance verdict
replace textual criticism, philology, history, law, scientific interpretation, or domain expertise
```

## 9. Method-gain ledger

```text
INTERPRETATION_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

A competent baseline receives the same source roles, versions, context, bridge records, ambiguity/conflict policy, and output target.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
```

## 10. Evidence discipline

Protocol construction and boundary refinement are infrastructure, not direct method evidence.

External origin, evaluator independence, source authority, method conformance, and method gain remain separate axes.