# Real-World Application Evidence / 외부 실제사례 적용 증거

This folder is reserved for applications to **independent real-world material** rather than synthetic toy cases or internally constructed benchmarks.

Examples include actual events, judicial cases, historical incidents, personal cases, empirical datasets, documented organizational or technical incidents, public normative standards/specifications, ethics/policy guidelines, public regulatory standards with official guidance, and public regulatory safety investigations.

## Separation rule / 분리 원칙

`CASE_ORIGIN` is separate from `EVIDENCE_SCOPE_CLASS`.

A judicial case may be a method-specific Audit case. A public standard, ethics guideline, regulatory corpus, or official investigation may directly test Specification while remaining external-source application evidence rather than a synthetic benchmark.

## Required case fields

```text
CASE_ORIGIN:
SOURCE_STATUS:
PRIMARY_OR_AUTHORITATIVE_SOURCE:
SECONDARY_SOURCES:
FACT_INTERPRETATION_BOUNDARY:
METHODS_APPLIED:
METHODS_DIRECTLY_TESTED:
EVIDENCE_SCOPE_CLASS:
SHARED_RULES_SUPPORTED:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
BASELINE_OR_ALTERNATIVE:
PRIVACY_OR_SENSITIVITY_HANDLING:
RESULT:
LIMITS:
REPRODUCIBILITY_RECORD:
```

Origin labels are not validation verdicts. An independently authored source can provide an external corpus while still leaving method superiority, independent evaluator agreement, practical benefit, and domain correctness unresolved.

## Source discipline / 출처 규율

- Case facts are locked separately from DSD interpretation.
- Prefer official, primary, or otherwise authoritative records where available.
- Judicial, historical, personal, normative, ethical, regulatory, and safety-investigation corpora keep their domain-specific source hierarchy and uncertainty boundaries.
- Public standards lock authoritative version/status and exact section scope before DSD scoring.
- Conflicting or differently weighted sources are preserved rather than silently merged.
- A blocked or contaminated precommit remains visible and is not counted as a completed application.
- A resolution-withheld incident or investigation test must freeze its acceptance prediction before comments, patches, closing resumes, recall reports, or other later resolution artifacts are revealed.

## Current external application records / 현재 외부 적용 기록

### DSD Specification

#### SPEC-APP-001 — RFC 9112 §6.3

```text
PROTOCOL: v0.1
CASE_ORIGIN: public_normative_standard
EXTERNAL_DOMAIN: HTTP message framing
SOURCE_UNIT_COVERAGE: 13/13
PRECEDENCE_PRESERVATION: 13/13
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

#### SPEC-APP-002 — Belmont Report Part C. Applications

```text
PROTOCOL: v0.2
CASE_ORIGIN: public_normative_ethics_guideline
EXTERNAL_DOMAIN: human-subject research ethics
SOURCE_UNIT_COVERAGE: 22/22
LOCAL_PRIORITY_PRESERVATION: 5/5
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED: 4/4
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
```

The original Belmont prose remains preferred for primary ethical reasoning; DSD adds a derivative traceability and structural coverage layer.

#### SPEC-APP-003 — OSHA Emergency Action Plan core corpus

```text
PROTOCOL: v0.2.1
CASE_ORIGIN: public_regulatory_standard_plus_official_guidance
EXTERNAL_DOMAIN: workplace emergency planning / occupational safety
SOURCE_UNIT_COVERAGE: 18/18
REGULATORY_MINIMUM_ELEMENTS_PRESERVED: 11/11
SITE_SPECIFIC_OPENNESS_HANDLED_WITHOUT_FABRICATION: 7/7
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

#### SPEC-APP-004 — WCAG 2.2 Contrast (Minimum) + official ACT labeled examples

```text
PROTOCOL: v1.0
CASE_ORIGIN: public_normative_standard_plus_official_labeled_examples
EXTERNAL_DOMAIN: web accessibility / text contrast
SELECTED_OFFICIAL_EXAMPLES: 8
EXAMPLE_OUTCOME_FAMILY_MATCHES: 8/8
NORMAL_LARGE_THRESHOLD_SEPARATION: pass
INCIDENTAL_INACTIVE_BOUNDARY_PRESERVATION: pass
INACTIVE_CONDITIONAL_LEDGER_BOILERPLATE: 0
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
RESULT: SPECIFICATION_V1_0_EXTERNAL_LABELED_REGRESSION_NO_GAIN_WITH_LIMITATIONS
```

This is a post-standardization labeled regression/interface test, not blind predictive evidence.

#### SPEC-APP-005 — JSON Schema Draft 2020-12 `dependentRequired` blind attempt — blocked

- Precommit: [`specification/SPEC-APP-005_JSON-Schema-dependentRequired_blind_precommit.md`](specification/SPEC-APP-005_JSON-Schema-dependentRequired_blind_precommit.md)
- Block record: [`specification/SPEC-APP-005_JSON-Schema-dependentRequired_blind_blocked.md`](specification/SPEC-APP-005_JSON-Schema-dependentRequired_blind_blocked.md)

```text
PINNED_CORPUS: JSON-Schema-Test-Suite commit f6fd52a0a95472e079cbfc6ef7f089702b80e045
STATUS: BLOCKED_BY_LABEL_ISOLATION_TOOLING
PREDICTIONS_COMMITTED: no
OFFICIAL_LABELS_SCORED: no
COUNT_AS_EXTERNAL_APPLICATION_COMPLETION: no
COUNT_AS_BLIND_EVIDENCE: no
```

The official file embeds expected `valid` labels with schema/data. The current source-delivery path could not supply a redacted packet without first exposing those labels to the predicting evaluator. The test was therefore stopped rather than weakening the precommitted blind rule.

The separately completed `SPEC-CH-008` uses constructed cases and a post-freeze `jsonschema` implementation comparison; it is method-specific constructed evidence and does not complete this external application.

#### SPEC-APP-006 — python-jsonschema `ErrorTree` read-mutation issue #1328

- Precommit: [`specification/SPEC-APP-006_ErrorTree-read-mutation_precommit.md`](specification/SPEC-APP-006_ErrorTree-read-mutation_precommit.md)
- Frozen prediction: [`specification/SPEC-APP-006_ErrorTree-read-mutation_prediction.md`](specification/SPEC-APP-006_ErrorTree-read-mutation_prediction.md)
- Result: [`specification/SPEC-APP-006_ErrorTree-read-mutation.md`](specification/SPEC-APP-006_ErrorTree-read-mutation.md)

```text
PROTOCOL: v1.0
CASE_ORIGIN: organizational_or_technical_incident
EXTERNAL_DOMAIN: Python library API behavior / error-structure semantics
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
ACTUAL_CLOSING_COMMIT: 7fa1acc948b34ab6283b3621ecbdc4360a717ba7
PRIMARY_AXES_MATCHED: 5/5
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
SOURCE_FACT_INVENTION_COUNT: 0
POST_REVEAL_PREDICTION_CHANGE: 0
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_REAL_WORLD_RESOLUTION_WITHHELD_ACCEPTANCE_MATCH_WITH_LIMITATIONS
```

The issue body was used to freeze a behavioral acceptance contract before issue comments, candidate PRs, and the closing commit were inspected. The actual maintainer resolution matched the predicted non-mutating iteration/containment behavior and regression-test family, while also adding adjacent lookup-error improvements that were not retroactively inserted into the prediction. This is stronger than a labeled regression but is **not** independent-evaluator or full-blind validation.

#### SPEC-APP-007 — Flask `stream_with_context` teardown-order issue #5804

- Precommit: [`specification/SPEC-APP-007_Flask-stream-with-context_teardown_precommit.md`](specification/SPEC-APP-007_Flask-stream-with-context_teardown_precommit.md)
- Frozen prediction: [`specification/SPEC-APP-007_Flask-stream-with-context_teardown_predictions.md`](specification/SPEC-APP-007_Flask-stream-with-context_teardown_predictions.md)
- Result: [`specification/SPEC-APP-007_Flask-stream-with-context_teardown.md`](specification/SPEC-APP-007_Flask-stream-with-context_teardown.md)

```text
PROTOCOL: v1.0
CASE_ORIGIN: organizational_or_technical_incident
EXTERNAL_DOMAIN: Python web framework / streamed-response request-context lifecycle
SELECTED_DSD_LAYERS: PROPERTY_CORE + DYNAMICS_LAYER
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
MAINTAINER_RESOLUTION_PR: pallets/flask#5812
FULL_MATCH_AXES: 5/6
PARTIAL_MATCH_AXES: 1/6
NON_MATCH_AXES: 0/6
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
POST_REVEAL_PREDICTION_CHANGE: 0
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_REAL_WORLD_LIFECYCLE_RESOLUTION_WITHHELD_MATCH_WITH_ONE_TEST_COVERAGE_PARTIAL
```

The issue body was used to freeze a lifecycle acceptance contract before maintainer comments and the resolving PR were inspected. The actual merged-context / push-count repair matched five behavioral and implementation-freedom axes. The sixth, direct regression-test-family axis, remains `PARTIAL_MATCH`: PR #5812 retained/adapted stream-context retention coverage but did not add a dedicated issue-#5804 teardown timing/count regression reproduction. The partial result is preserved rather than inflated to a full match.

This is also the first completed v1.0 external Specification application in the current sequence where `DYNAMICS_LAYER` was materially selected for event-order/lifecycle constraints.

#### SPEC-APP-008 — NHTSA PE24003 / Alfa Romeo low-pressure fuel-pump investigation

- Precommit: [`specification/SPEC-APP-008_NHTSA-PE24003-fuel-pump_precommit.md`](specification/SPEC-APP-008_NHTSA-PE24003-fuel-pump_precommit.md)
- Frozen prediction: [`specification/SPEC-APP-008_NHTSA-PE24003-fuel-pump_prediction.md`](specification/SPEC-APP-008_NHTSA-PE24003-fuel-pump_prediction.md)
- Result: [`specification/SPEC-APP-008_NHTSA-PE24003-fuel-pump.md`](specification/SPEC-APP-008_NHTSA-PE24003-fuel-pump.md)

```text
PROTOCOL: v1.0
CASE_ORIGIN: public_regulatory_safety_investigation
EXTERNAL_DOMAIN: automotive safety / defect investigation
SELECTED_DSD_LAYERS: PROPERTY_CORE + DYNAMICS_LAYER
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
OFFICIAL_CLOSING_ACTION: recall 25V586
FULL_MATCH_AXES: 5/6
PARTIAL_MATCH_AXES: 1/6
NON_MATCH_AXES: 0/6
SOURCE_FACT_INVENTION_COUNT: 0
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
POST_REVEAL_PREDICTION_CHANGE: 0
FINAL_SPEC_STATUS: usable_with_unresolved_items
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_AUTOMOTIVE_SAFETY_RESOLUTION_WITHHELD_MATCH_WITH_REMEDY_DETAIL_PARTIAL
```

The NHTSA Opening Resume was used to freeze six acceptance axes before the Closing Resume and Part 573 recall report were inspected. The later official resolution expanded the scope from the initial Giulia population to a 53,849-vehicle Giulia/Stelvio recall population, identified a suspect fuel-delivery-module failure chain, and closed the PE with recall 25V586. The remedy-to-hazard axis remains `PARTIAL_MATCH` because the concrete remedy was still under development in the official closure-stage materials and ODI explicitly retained later remedy evaluation.

This is the first completed resolution-withheld case in the current sequence from a **non-software safety-regulatory domain**. It supports the distinction between resolved defect/recall disposition and still-open remedy implementation/effectiveness.

## Validation limit / 검증 한계

A real-world or external-source case is application evidence first. It contributes to method validation only when protocol, scoring/failure criteria, external standard, source-purpose boundary, and relevant baseline were locked well enough to make the case a genuine test rather than an illustration.

An external origin and an independent evaluator are different axes. The current Specification corpus has **seven completed external applications across seven completed domains**, plus one blocked/unscored external blind precommit. `SPEC-APP-006`, `SPEC-APP-007`, and `SPEC-APP-008` provide three resolution-artifact-withheld real-world comparisons; `SPEC-APP-008` is the first of those in a non-software safety-regulatory domain. All DSD reasoning remains within the same project/model environment. Independent reviewer validation and measured practical benefit therefore remain unresolved.
