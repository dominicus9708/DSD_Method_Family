# SPEC-APP-007 — Flask `stream_with_context` Teardown-Order Resolution-Withheld Test

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Case origin: organizational_or_technical_incident
External domain: Python web framework / streamed-response request-context lifecycle
Precommit: `f6bca91ec8b5e6db5d88be603f57f865567a2f12`
Frozen prediction: `09ea2055c9fedce578f7e993003287ee5f327d60`
External issue: `pallets/flask` #5804
Maintainer-designated resolution PR: `pallets/flask` #5812
Resolution PR head: `c2705ffd9ce1dc8476cb29eaf5ff5d4c719852d9`
Merge commit: `adf363679da2d9a5ddc564bb2da563c7ca083916`

## 1. Result in one line

The DSD Specification v1.0 lifecycle acceptance contract was frozen from the issue body before issue comments and the maintainer-designated resolving PR were read. After reveal, the actual context redesign matched the five behavioral/implementation-freedom axes and only partially matched the precommitted direct-regression-test axis: the PR preserved and adapted stream context-retention tests, but did not add a dedicated reproduction asserting teardown callback ordering/count for issue #5804.

```text
A1_PREMATURE_TEARDOWN_ELIMINATION: MATCH
A2_REQUEST_SCOPED_STATE_THROUGH_STREAM: MATCH
A3_REPORTED_DUPLICATE_TEARDOWN_SEQUENCE_ELIMINATED: MATCH
A4_STREAMED_RESPONSE_REGRESSION_REMOVED: MATCH
A5_IMPLEMENTATION_FREEDOM_PRESERVED: MATCH
A6_DIRECT_REGRESSION_TEST_FAMILY: PARTIAL_MATCH

FULL_MATCH_AXES: 5/6
PARTIAL_MATCH_AXES: 1/6
NON_MATCH_AXES: 0/6
UNRESOLVED_AXES: 0/6
POST_REVEAL_PREDICTION_CHANGE: 0
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
SOURCE_FACT_INVENTION_COUNT: 0
HARD_FAILURES: 0
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_REAL_WORLD_LIFECYCLE_RESOLUTION_WITHHELD_MATCH_WITH_ONE_TEST_COVERAGE_PARTIAL
```

## 2. Reveal sequence

Before frozen prediction commit `09ea2055c9fedce578f7e993003287ee5f327d60`, only the issue body and coarse metadata had been inspected.

After the freeze, the following were revealed:

1. issue comments;
2. maintainer statement that #5812 would fix the issue as a side effect;
3. reporter confirmation that #5812 addressed the observed timing problem;
4. PR #5812 body/diff;
5. relevant `stream_with_context` implementation at PR head;
6. `AppContext.push/pop` behavior at PR head;
7. changed test files in PR #5812.

No acceptance axis was added, removed, or weakened after reveal.

## 3. Revealed maintainer interpretation

A maintainer explicitly stated that issue #5804 would be fixed as a side effect of PR #5812 in Flask 3.2, while cautioning that callers should not generally assume teardown callback invocation count or exact surrounding state.

The reporter clarified that the original concern was primarily **when** teardown occurs — specifically, before entering the generator passed to `stream_with_context` — and reported that #5812 did the trick for that issue.

This distinction matters for the precommitted E3 axis. E3 was scoped to elimination of the specific premature-plus-later duplicate sequence in the locked reproduction; it did **not** claim a universal one-teardown-call rule for every Flask context configuration.

## 4. Actual resolution mechanism

PR #5812 merges `RequestContext` into `AppContext` and changes context handling so a context can be pushed multiple times while cleanup occurs only after corresponding pops reduce the push count to zero.

At PR head, `stream_with_context`:

```text
1. captures the active merged context;
2. enters `with ctx:` before yielding the sentinel used to freeze the generator state;
3. leaves that context pushed while control returns to the request/WSGI path;
4. resumes the original generator while the same context remains active;
5. exits the context only after the wrapped generator completes or closes.
```

`AppContext.push/pop` records `_push_count`; `pop` returns without teardown while `_push_count > 0`, and only when the count reaches zero does it call request/app teardown and remove the context.

This directly supplies the lifecycle mechanism needed to prevent the outer request return from performing the final teardown while the streamed generator still depends on the context.

## 5. Precommitted axis comparison

### A1 — premature teardown elimination

Frozen requirement:

```text
teardown must not destroy required request-context state before wrapped generator use
```

Actual resolution holds an additional push across streamed generation; an intermediate pop does not trigger cleanup while `_push_count > 0`.

```text
A1_RESULT: MATCH
```

### A2 — request-scoped state through generation

Frozen requirement:

```text
state established before returning the stream remains available when the generator uses it
```

The PR documentation and implementation explicitly preserve `request`, `session`, and `g` for `stream_with_context`, and the merged context remains active through generator execution.

```text
A2_RESULT: MATCH
```

### A3 — reported premature-plus-later duplicate sequence

Frozen requirement was intentionally narrow: remove the regression sequence in the single locked reproduction, without asserting a universal teardown-count invariant.

The merged context's push-count behavior makes the initial outer pop non-final while the stream still holds the context; cleanup occurs when the final held context exits.

The maintainer's warning that teardown functions may run multiple times in other situations is preserved as an external semantic limit, not treated as a contradiction.

```text
A3_RESULT: MATCH
UNIVERSAL_ONE_TEARDOWN_CLAIM: not made
```

### A4 — streamed-response regression removed

The reporter stated that #5812 addressed the reported timing problem, and the resulting implementation keeps the required context active during stream generation.

```text
A4_RESULT: MATCH
```

### A5 — implementation freedom

The frozen DSD record did not predict merging `RequestContext` with `AppContext`, `_push_count`, a single ContextVar, or any exact helper rewrite.

The actual solution is therefore a permitted implementation family rather than a guessed patch.

```text
A5_RESULT: MATCH
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
```

### A6 — direct regression-test family

Frozen expectation:

```text
a repair should include direct regression evidence for ordering/state availability and/or duplicate teardown in a streamed response case
```

PR #5812 changed tests that verify preserved context behavior and updated a test whose response close releases the context held by `stream_with_context`. Existing `TestStreaming` coverage also verifies that request/session data remain usable in wrapped streams.

However, PR #5812 did not add a dedicated test reproducing issue #5804 with a teardown callback and explicit assertions for:

```text
teardown timing relative to generator start
or
reported duplicate teardown count/order
```

Therefore the precommitted test-family expectation is only partially met.

```text
A6_RESULT: PARTIAL_MATCH
DEDICATED_ISSUE_5804_TEARDOWN_ORDER_TEST_ADDED: no
GENERAL_STREAM_CONTEXT_RETENTION_TEST_COVERAGE: yes
```

## 6. Important negative result

This case did **not** produce 6/6 full matches.

The missing dedicated regression test is preserved as a partial result rather than being reclassified after reveal.

```text
FULL_MATCH_AXES: 5/6
PARTIAL_MATCH_AXES: 1/6
POST_REVEAL_EXCEPTION_ADDED: no
```

This is useful evidence for the method because DSD Specification did not need to convert every external resolution into a perfect pass.

## 7. DSD Dynamics activation check

Unlike the previous ErrorTree case, this case materially required transition order.

```text
SELECTED_DSD_LAYERS:
  PROPERTY_CORE
  DYNAMICS_LAYER
```

The minimal event-order carrier was:

```text
R1 request state established
-> R2 wrapped stream returned
-> R3 generator begins/uses context state
-> R4 stream completes
-> R5 final teardown
```

The DYNAMICS layer was useful only for event ordering and lifecycle/transition constraints. Static Aggregation and Formation were not activated.

```text
IRRELEVANT_OPTIONAL_LAYERS_ACTIVATED: 0
DYNAMICS_LAYER_JUSTIFIED_BY_TASK: yes
```

This is the first completed v1.0 external Specification application in the current evidence sequence where the Dynamics layer was materially selected for transition ordering.

## 8. Guardrail evaluation

```text
G1 SOURCE_FIDELITY: INSIDE_GUARDRAILS
G2 PURPOSE_AND_PRIORITY_FIDELITY: INSIDE_GUARDRAILS at narrow bug-report purpose
G3 DETAIL_PROPORTIONALITY: INSIDE_GUARDRAILS
G4 VIEWPOINT_SEPARATION: INSIDE_GUARDRAILS
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
```

The DSD representation added a lifecycle order without attributing that typed representation to the issue author or Flask maintainers.

## 9. Baseline and gain interpretation

The issue report already discovered and reproduced the bug. DSD therefore receives no bug-discovery credit.

```text
BUG_DISCOVERY_GAIN: no
LIFECYCLE_ACCEPTANCE_STRUCTURING_GAIN: demonstrated_on_case
IMPLEMENTATION_FREEDOM_SEPARATION_GAIN: demonstrated_on_case
TRANSITION_ORDER_CARRIER_GAIN: demonstrated_on_case
MEASURED_ENGINEERING_TIME_OR_DEFECT_GAIN: not measured
```

The strongest baseline remains ordinary issue/maintainer development plus Flask's own tests and lifecycle documentation.

DSD's demonstrated case-level contribution is the ability to freeze a behavior-level transition contract before seeing the actual architectural repair, while leaving implementation freedom intact.

## 10. External/evaluator boundary

```text
EXTERNAL_SOURCE_AUTHORSHIP: independent_of_DSD
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
PREDICTING_EVALUATOR_INDEPENDENCE: no
INDEPENDENT_REVIEWER_VALIDATION: not_established
FULL_BLINDNESS: no
MODEL_PRIOR_KNOWLEDGE_EXCLUSION: not_established
```

This is a second **resolution-withheld real-world comparison**, not fully blind independent validation.

## 11. Final record

```text
SPECIFICATION_RESULT_ID: SPEC-APP-007
SPECIFICATION_PROTOCOL_VERSION: v1.0
TARGET_SCOPE: Flask issue #5804 streamed-response teardown-order regression
DECLARED_DOWNSTREAM_TASK: freeze behavior-level repair acceptance semantics before maintainer resolution reveal
LOCKED_REQUIREMENT_INVENTORY: E1-E6
SELECTED_DSD_LAYERS: PROPERTY_CORE + DYNAMICS_LAYER
FINAL_SPEC_STATUS: usable
HARD_FAILURES: none
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS

FULL_MATCH_AXES: 5/6
PARTIAL_MATCH_AXES: 1/6
NON_MATCH_AXES: 0/6
POST_REVEAL_PREDICTION_CHANGE: 0
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established

RESULT:
SPECIFICATION_V1_0_REAL_WORLD_LIFECYCLE_RESOLUTION_WITHHELD_MATCH_WITH_ONE_TEST_COVERAGE_PARTIAL
```
