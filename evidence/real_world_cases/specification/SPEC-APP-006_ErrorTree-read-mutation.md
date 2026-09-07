# SPEC-APP-006 — `ErrorTree` Read-Mutation Real-World Resolution-Withheld Test

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Case origin: organizational_or_technical_incident
External domain: Python library API behavior / error-structure semantics
Precommit: `70a9ffd9b02d839057f1efb62b7c8a605e6cc813`
Frozen prediction: `cbabc9d6533da1643588a1b934d5a41da2be6022`
External issue: `python-jsonschema/jsonschema` #1328
Actual closing commit: `7fa1acc948b34ab6283b3621ecbdc4360a717ba7`

## 1. Result in one line

The DSD Specification v1.0 acceptance contract was frozen from the issue body before reading the maintainer discussion, candidate PRs, or closing commit. After reveal, the actual maintainer fix matched all five precommitted behavioral/test-family axes: error-free child access no longer adds a phantom key, `__contains__`/`__iter__` remain accurate, genuine error state remains visible, missing-child access remains supported through an unstored empty subtree, and a direct regression test was added. No prediction was rewritten after reveal.

```text
A1_BEHAVIORAL_REQUIREMENT_MATCH: MATCH
A2_MEMBERSHIP_ITERATION_SEMANTICS_MATCH: MATCH
A3_READ_NONMUTATION_OR_EQUIVALENT_OBSERVATIONAL_INVARIANT_MATCH: MATCH
A4_PREEXISTING_ERROR_PRESERVATION_MATCH: MATCH
A5_REGRESSION_TEST_FAMILY_MATCH: MATCH

PRIMARY_AXES_MATCHED: 5/5
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
SOURCE_FACT_INVENTION_COUNT: 0
POST_REVEAL_PREDICTION_CHANGE: 0
HARD_FAILURES: 0
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_REAL_WORLD_RESOLUTION_WITHHELD_ACCEPTANCE_MATCH_WITH_LIMITATIONS
```

## 2. Reveal sequence

Before the frozen prediction commit, only the issue body and coarse issue metadata were inspected.

After commit `cbabc9d6533da1643588a1b934d5a41da2be6022`, the following were revealed:

1. issue comments;
2. candidate PRs referencing #1328;
3. the actual closing commit `7fa1acc948b34ab6283b3621ecbdc4360a717ba7`.

The maintainer's earlier comment identified a likely `defaultdict` misuse and noted that ErrorTree mutation compatibility complicated the fix. This was not visible when the DSD acceptance record was frozen.

## 3. Actual maintainer resolution

The closing commit states:

```text
Don't mutate ErrorTrees when purely checking indices.
Also improve the behavior when indexing into subtrees using an index not present in the tree.
Closes: #1328
```

The implementation:

```text
1. removes `defaultdict` child storage;
2. explicitly creates real error-path subtrees during construction;
3. for an existing error child, returns the stored subtree;
4. for an error-free valid child, returns a fresh ErrorTree carrying the corresponding instance without storing it;
5. preserves underlying lookup errors for genuinely invalid nested indices.
```

The added regression tests verify that reading an error-free child:

```text
subtree.total_errors == 0
1 not in tree
list(tree) == [0]
tree.total_errors == 1
```

and additionally verify correct lookup-error propagation through error-free subtrees.

## 4. Precommitted requirement comparison

### E1 — iteration reflects real error-bearing keys

Frozen prediction:

```text
reading an error-free key must not cause it to appear in iteration
```

Actual closing test:

```text
list(tree) == [0]
```

after `subtree = tree[1]`.

```text
E1_RESULT: MATCH
```

### E2 — containment reflects real error-bearing membership

Frozen prediction:

```text
1 in tree remains False after reading tree[1]
```

Actual closing test:

```text
self.assertNotIn(1, tree)
```

```text
E2_RESULT: MATCH
```

### E3 — read preserves the observable error-key state

Frozen prediction intentionally allowed multiple implementation families and required only the observable invariant.

Actual implementation uses an unstored empty subtree for the error-free access path.

```text
E3_RESULT: MATCH
ACTUAL_IMPLEMENTATION_FAMILY: allowed alternative A
```

### E4 — genuine error state remains represented

Frozen prediction:

```text
genuine index 0 remains observable after reading index 1
```

Actual test preserves both:

```text
list(tree) == [0]
tree.total_errors == 1
```

```text
E4_RESULT: MATCH
```

### E5 — implementation freedom remains open

The frozen DSD record did not require `dict`, `defaultdict`, `setdefault`, a particular private field shape, or any exact code patch.

The actual fix chose a plain dictionary plus explicit subtree construction and instance-carrying empty subtrees.

```text
E5_RESULT: MATCH
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
```

## 5. Regression-test family comparison

Frozen prediction:

```text
T1 construct ErrorTree with a real child error
T2 verify error-free key absent
T3 read error-free key
T4 iteration unchanged
T5 containment unchanged
T6 genuine error remains present (secondary)
```

Actual closing commit added a direct test with the same core sequence and also checked `total_errors` stability.

```text
A5_REGRESSION_TEST_FAMILY_MATCH: MATCH
CORE_SEQUENCE_MATCH: 5/5
SECONDARY_GENUINE_ERROR_PRESERVATION: supported
```

## 6. Lower-confidence compatibility prediction

Frozen prediction:

```text
PREDICT_ACCESS_ITSELF_REMAINS_SUPPORTED: yes
PREDICT_MISSING_CHILD_ACCESS_NEED_NOT_RAISE: yes
CONFIDENCE: medium
```

Actual closing behavior returns a new empty subtree for a valid error-free index rather than raising.

```text
COMPATIBILITY_PREDICTION: MATCH
```

The closing commit also improves nested lookup-error propagation for indices genuinely absent from the underlying instance. That extra behavior was not predicted and is recorded as an additional maintainer resolution, not retroactively added to the DSD prediction.

## 7. Unpredicted but non-conflicting resolution scope

Actual commit additionally introduced:

```text
ErrorTree(instance=...)
instance propagation into empty subtrees
KeyError/IndexError propagation tests for genuinely invalid nested lookups
CHANGELOG entry for v4.26.1
```

These are compatible with the frozen acceptance contract but were not implied strongly enough by the issue body to be predicted as required.

```text
UNPREDICTED_ADDITIONAL_RESOLUTION_ITEMS: 4 families
RETROACTIVE_REQUIREMENT_ADDITION: 0
```

This is a positive restraint result: DSD did not need to guess every implementation or adjacent repair in order to match the core acceptance semantics.

## 8. Guardrail evaluation

```text
G1 SOURCE_FIDELITY: INSIDE_GUARDRAILS
G2 PURPOSE_AND_PRIORITY_FIDELITY: inactive for narrow bug contract
G3 DETAIL_PROPORTIONALITY: INSIDE_GUARDRAILS
G4 VIEWPOINT_SEPARATION: inactive
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
```

The DSD record was compact enough for the issue: four behavioral requirements plus one explicit implementation-freedom record. The actual fix required more implementation detail, but that detail was appropriately left to the receiving implementation task.

## 9. External-source and evaluator boundary

This case is stronger than a labeled regression because the actual maintainer resolution artifacts were not read until after the DSD prediction was committed.

However:

```text
EXTERNAL_SOURCE_AUTHORSHIP: independent_of_DSD
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
PREDICTING_EVALUATOR_INDEPENDENCE: no
INDEPENDENT_REVIEWER_VALIDATION: not_established
FULL_BLINDNESS: no
MODEL_PRIOR_KNOWLEDGE_EXCLUSION: not_established
```

Therefore the correct description is **resolution-withheld real-world comparison**, not fully blind independent validation.

## 10. Baseline / NO_GAIN interpretation

The original issue report already identifies the visible bug clearly. DSD's gain is not discovering that `tree[1]` changes membership; the reporter had already demonstrated it.

The useful DSD contribution in this locked task is the separation between:

```text
behavioral acceptance contract
implementation freedom
source-supported requirement
later implementation-specific repair
```

and the ability to freeze those boundaries before seeing the actual repair.

Accordingly:

```text
BUG_DISCOVERY_GAIN: no
BEHAVIORAL_ACCEPTANCE_STRUCTURING_GAIN: demonstrated_on_case
RESOLUTION_MATCH: demonstrated_on_case
MEASURED_ENGINEERING_TIME_OR_DEFECT_GAIN: not measured
```

`FINAL_SPEC_STATUS` is therefore `usable`, not a superiority claim over ordinary issue-driven development.

## 11. Final record

```text
SPECIFICATION_RESULT_ID: SPEC-APP-006
SPECIFICATION_PROTOCOL_VERSION: v1.0
TARGET_SCOPE: python-jsonschema ErrorTree issue #1328
DECLARED_DOWNSTREAM_TASK: freeze repair acceptance semantics before resolution reveal
LOCKED_REQUIREMENT_INVENTORY: E1-E5
SELECTED_DSD_LAYERS: PROPERTY_CORE only
FINAL_SPEC_STATUS: usable
HARD_FAILURES: none
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS

PRIMARY_AXES_MATCHED: 5/5
POST_REVEAL_PREDICTION_CHANGE: 0
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established

RESULT:
SPECIFICATION_V1_0_REAL_WORLD_RESOLUTION_WITHHELD_ACCEPTANCE_MATCH_WITH_LIMITATIONS
```
