# SPEC-APP-007 — Flask `stream_with_context` teardown-order Resolution-Withheld Test — Precommit

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Case origin: organizational_or_technical_incident
External domain: Python web framework / streamed response request-context lifecycle
External issue: `pallets/flask` #5804
Source exposed before prediction: issue title/body and coarse issue metadata only
Resolution artifacts withheld until after prediction freeze: issue comments, closing PR(s), closing commit(s), patch/diff, changelog entry

## 1. Core input lock

```text
SPECIFICATION_ID: SPEC-APP-007
TARGET_SCOPE: Flask 3.1.2 `stream_with_context` regression described in issue #5804
REQUIREMENT_SOURCE_SET: issue #5804 body only
SOURCE_VERSIONS: reporter comparison Flask 3.1.1 vs 3.1.2; Python 3.13; Werkzeug 3.1.3 as reported
DSD_INTERFACE_PROFILE_DATE: 2026-09-08
SELECTED_DSD_LAYERS: PROPERTY_CORE + DYNAMICS_LAYER
REQUIREMENT_INVENTORY: E1-E6 below
DECLARED_DOWNSTREAM_TASK: freeze behavior-level repair acceptance semantics before maintainer resolution reveal
EXTERNAL_STANDARD_IF_ANY: Flask's own documented/request-lifecycle behavior and actual maintainer resolution; DSD does not replace them
```

## 2. Source-purpose / use-function lock

The issue explicitly reports a regression in the lifecycle of a streamed response wrapped with `stream_with_context`.

```text
SOURCE_PRIMARY_PURPOSE: report and reproduce a regression where teardown occurs before streamed response generation and occurs twice in the locked scenario
SOURCE_PURPOSE_EVIDENCE: EXPLICITLY_STATED
SOURCE_TARGET_USER_OR_ACTOR: Flask maintainers / users of `stream_with_context`
SOURCE_PRIMARY_ACTION_OR_DECISION: determine a repair that restores a coherent streamed-response/request-context lifecycle
SOURCE_PRIORITY_HIERARCHY: no explicit ranked hierarchy beyond restoring correct lifecycle behavior
SOURCE_COMMUNICATION_OR_USE_FUNCTION: bug report with reproducible example and before/after behavior
TRANSFORMATION_PURPOSE: derive a compact DSD acceptance contract without prescribing implementation
VIEWPOINT_CHANGE_DECLARED: yes
DSD_ADDED_STRUCTURE: typed lifecycle requirements and transition-order obligations
DSD_ADDED_DETAIL: only acceptance and regression-test boundaries inferable from the issue body
DERIVATIVE_VIEW_LABEL: DSD repair-acceptance specification
```

## 3. Locked source facts

The issue body reports the following facts for the example:

```text
F1 Flask 3.1.1 output order: response generation starts, then teardown is called once.
F2 Flask 3.1.2 output order: teardown is called before response generation starts, then teardown is called again.
F3 the early teardown removes `g.hello`, causing generator access to `g.hello` to fail.
F4 removing the failing `g` access still leaves the double-teardown observation.
F5 the reporter expects teardown not to occur before the streamed response is actually generated.
```

No implementation fix is inferred from the issue body.

## 4. Precommitted requirement inventory

### E1 — no premature teardown before streamed generation

```text
REQUIREMENT_ID: E1
TARGET_ENTITY_OR_CARRIER: teardown-request lifecycle event relative to streamed generator
REQUIREMENT_TYPE: transition-order obligation
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: a request returns a `stream_with_context` wrapped generator under the locked scenario
REQUIRED_STRUCTURE_OR_VALUE: request teardown must not occur before the wrapped generator begins/continues the streamed response in a way that destroys required request-context state
VIOLATION_CONDITION: teardown occurs before generator use and makes the stream lose required request-scoped state
UNRESOLVED_CONDITION: issue body alone does not specify every legal lifecycle implementation
```

### E2 — request-context state needed by the stream remains usable through generation

```text
REQUIREMENT_ID: E2
TARGET_ENTITY_OR_CARRIER: request/app context state used by streamed generator (`g.hello` in the reproduction)
REQUIREMENT_TYPE: state-availability obligation
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: the generator accesses state that was established before returning the wrapped stream
REQUIRED_STRUCTURE_OR_VALUE: the state remains available at the point the generator uses it
VIOLATION_CONDITION: lifecycle handling makes the state unavailable before generator access in the locked reproduction
UNRESOLVED_CONDITION: exact internal context-copy/push/pop mechanism is not prescribed
```

### E3 — duplicate teardown in the locked single-request scenario is not preserved as normal behavior

```text
REQUIREMENT_ID: E3
TARGET_ENTITY_OR_CARRIER: teardown callback invocation count/order in the reproduction
REQUIREMENT_TYPE: lifecycle cardinality/order obligation
REQUIRED_OR_OPTIONAL: required for the locked scenario
ACTIVATION_CONDITION: the single streamed request from the reproduction completes
REQUIRED_STRUCTURE_OR_VALUE: the regression's premature-plus-later duplicate teardown sequence is eliminated
VIOLATION_CONDITION: the same request still triggers the reported early teardown and later second teardown sequence
UNRESOLVED_CONDITION: this does not claim a universal one-call theorem for every possible nested/request-context construction
```

### E4 — normal streamed response generation succeeds

```text
REQUIREMENT_ID: E4
TARGET_ENTITY_OR_CARRIER: output of the wrapped response generator
REQUIREMENT_TYPE: functional outcome obligation
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: the reproduction request is processed
REQUIRED_STRUCTURE_OR_VALUE: generator can yield the response using the preserved request-scoped state without the reported AttributeError/secondary teardown failure
VIOLATION_CONDITION: the original regression remains observable in the reproduction
UNRESOLVED_CONDITION: exact HTTP body formatting beyond the source example is not material
```

### E5 — implementation freedom

```text
REQUIREMENT_ID: E5
TARGET_ENTITY_OR_CARRIER: Flask internal context/stream implementation
REQUIREMENT_TYPE: implementation-freedom boundary
REQUIRED_OR_OPTIONAL: required restraint
ACTIVATION_CONDITION: repair satisfies E1-E4
REQUIRED_STRUCTURE_OR_VALUE: DSD does not require a specific private function, context-stack algorithm, wrapper shape, or exact patch
VIOLATION_CONDITION: the DSD prediction pretends the issue body uniquely determines an internal fix
UNRESOLVED_CONDITION: maintainer may choose any compatible implementation preserving E1-E4
```

### E6 — regression-test family

```text
REQUIREMENT_ID: E6
TARGET_ENTITY_OR_CARRIER: receiving implementation test
REQUIREMENT_TYPE: verification-family obligation
REQUIRED_OR_OPTIONAL: expected acceptance evidence
ACTIVATION_CONDITION: a repair is proposed
REQUIRED_STRUCTURE_OR_VALUE: a regression test should distinguish the bad lifecycle from the repaired lifecycle by checking ordering/state availability and/or duplicate teardown in a streamed response case
VIOLATION_CONDITION: repair has no direct regression evidence for the reported lifecycle failure family
UNRESOLVED_CONDITION: exact test fixture and assertions remain implementation-specific
```

## 5. DSD transition representation

The issue requires Dynamics only for event order, not a full physical or analytic dynamics model.

```text
R0 request context active
R1 view establishes request-scoped state
R2 wrapped stream returned
R3 generator begins/uses request-scoped state
R4 streamed generation completes
R5 teardown/finalization
```

Precommitted order constraint for the locked reproduction:

```text
R1 -> R2 -> R3 -> R4 -> R5
```

The regression reports an invalid transition ordering in which teardown intrudes before R3 and then occurs again later.

## 6. Guardrail and hard-failure criteria

```text
G1 SOURCE_FIDELITY: active
G2 PURPOSE_AND_PRIORITY_FIDELITY: active at narrow bug-report purpose only
G3 DETAIL_PROPORTIONALITY: active
G4 VIEWPOINT_SEPARATION: active because DSD adds lifecycle typing
```

Hard failures:

```text
SOURCE_FACT_INVENTION
SILENT_REQUIRED_SOURCE_OMISSION
NORMATIVE_FORCE_STRENGTHENING
FABRICATED_DETERMINACY
POST_REVEAL_REQUIREMENT_REWRITE
IMPLEMENTATION_OVERPREDICTION presented as source-required
```

## 7. Locked comparison axes

After the prediction is frozen, compare the actual maintainer resolution against:

```text
A1 premature-teardown elimination relative to generator use
A2 preservation of request-scoped state through streamed generation
A3 elimination of the reported duplicate-teardown sequence in the locked scenario
A4 successful streamed response behavior / regression symptom removal
A5 implementation freedom preserved: actual patch may differ from any imagined mechanism
A6 direct regression-test family covering lifecycle ordering/state/teardown behavior
```

Allowed outcomes per axis:

```text
MATCH
PARTIAL_MATCH
NON_MATCH
UNRESOLVED_FROM_REVEALED_ARTIFACTS
```

No criterion changes after reveal.

## 8. Evidence limits

```text
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: planned yes
FULL_BLINDNESS: no
MODEL_PRIOR_KNOWLEDGE_EXCLUSION: not established
PREDICTING_EVALUATOR_INDEPENDENCE: no
INDEPENDENT_REVIEWER_VALIDATION: not established
MEASURED_ENGINEERING_BENEFIT: not established
```

The case can support a resolution-withheld real-world comparison, not fully blind independent validation.
