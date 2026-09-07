# SPEC-CH-006 — Guardrail Centerline Challenge / 가드레일 중심선 도전

Date: 2026-09-07
Evidence scope: `method_specific`
Method directly tested: **DSD Specification / DSD 명세론**
Protocol basis: **Specification Protocol v0.1 + prospective guardrail candidate profile**
Precommit: [`SPEC-CH-006_guardrail-centerline_precommit.md`](SPEC-CH-006_guardrail-centerline_precommit.md)
Precommit commit: `fe009d8da9ab992e6885d07e14ff26355b776a86`

## 1. Question

Can DSD Specification keep purpose, priority, detail burden, and viewpoint changes as **centerline guardrails** without turning every deviation into an automatic discard condition?

The required distinction is:

```text
HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

## 2. Locked guardrails

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

A derivative DSD viewpoint is allowed when declared. Added detail is allowed when proportionate to the declared task. Source purpose may remain `UNDETERMINED` when the source does not establish it.

## 3. Case results

| Case | Locked expected family | Observed family | Hard failure? | Result |
|---|---|---|---|---|
| C1 declared derivative appendix | `INSIDE_GUARDRAILS` | `INSIDE_GUARDRAILS` | no | match |
| C2 redundant but bounded detail | `GUARDRAIL_PRESSURE` | `GUARDRAIL_PRESSURE` | no | match |
| C3 priority encoded but presentation flattened | `GUARDRAIL_PRESSURE` | `GUARDRAIL_PRESSURE` | no | match |
| C4 critical path buried by atomization | `GUARDRAIL_EXCEEDED_RECOVERABLE` | `GUARDRAIL_EXCEEDED_RECOVERABLE` | no | match |
| C5 undeclared purpose substitution | `PURPOSE_OR_VIEWPOINT_DISTORTED` | `PURPOSE_OR_VIEWPOINT_DISTORTED` | no | match |
| C6 DSD ontology attributed to source author | `PURPOSE_OR_VIEWPOINT_DISTORTED` | `PURPOSE_OR_VIEWPOINT_DISTORTED` | no | match |
| C7 unknown source purpose preserved as unknown | `INSIDE_GUARDRAILS` | `INSIDE_GUARDRAILS` | no | match |
| C8 invented purpose used for new obligation | `PURPOSE_OR_VIEWPOINT_DISTORTED` | `PURPOSE_OR_VIEWPOINT_DISTORTED` | yes: `SOURCE_FACT_INVENTION` | match |

## 4. Why the cases separate

### C1 — Declared derivative viewpoint is permitted

The source's rapid-action checklist remains the primary view. The DSD appendix is separately labeled as a derivative analytic view. No source purpose is overwritten and no DSD-added ontology is attributed to the source.

```text
G2: inside
G3: inside
G4: inside
```

This prevents the guardrail framework from becoming a ban on analysis or viewpoint change.

### C2 — Detail inflation can be pressure without failure

The extra annotations are unnecessary for the original task, but the primary action path is still available and no source meaning is changed.

```text
DETAIL_INFLATION: present
SOURCE_PURPOSE_PRESERVED: yes
TARGET_USER_FUNCTION_PRESERVED: yes
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
```

The correct response is to flag burden, not discard the representation.

### C3 — Priority flattening risk is distinct from priority loss

The precedence relation remains explicitly encoded, so semantic priority is not lost. However, the visible presentation makes primary and secondary items look coequal.

```text
PRIORITY_SEMANTICS_PRESERVED: yes
PRIORITY_PRESENTATION_PRESERVED: partial
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
```

This is a centerline warning rather than a hard specification error.

### C4 — Recoverable purpose-function obstruction

All atoms are source-faithful, but the rapid-action function is obscured by the atomized representation. Restoring a primary quick-action view would repair the problem without changing the underlying atoms.

```text
SEMANTIC_CONTENT_PRESERVED: yes
SOURCE_PURPOSE_FUNCTION_PRESERVED: no_at_current_presentation
RECOVERABLE_WITHOUT_SOURCE_REINTERPRETATION: yes
GUARDRAIL_VERDICT: GUARDRAIL_EXCEEDED_RECOVERABLE
```

### C5 — Undeclared purpose shift is distortion

Changing a rapid-action guide into a comprehensive classification document is allowed only as a declared derivative task. Presenting that new task as the source's own purpose crosses G2 and G4.

### C6 — Authorial-intent overattribution is distortion

A DSD status decomposition can be a legitimate analytic structure. What is not legitimate is asserting that the source author intended that ontology when the source does not establish it.

```text
DSD_ADDED_STRUCTURE: yes
VIEWPOINT_CHANGE_DECLARED: no
AUTHORIAL_INTENT_SUPPORTED_BY_SOURCE: no
GUARDRAIL_VERDICT: PURPOSE_OR_VIEWPOINT_DISTORTED
```

### C7 — Unknown purpose is allowed to remain unknown

The candidate guardrail profile does not force a purpose or audience into every source. `UNDETERMINED` is a valid state when the source does not support a stronger claim.

### C8 — Invented purpose can escalate to hard failure

The invented purpose is not merely an interpretive viewpoint because it is used to create a new mandatory obligation and is presented as source-grounded. This crosses the guardrail and independently triggers the existing source-invention prohibition.

```text
GUARDRAIL_VERDICT: PURPOSE_OR_VIEWPOINT_DISTORTED
HARD_FAILURE: yes
HARD_FAILURE_CLASS: SOURCE_FACT_INVENTION
```

## 5. Scoring

```text
EXACT_GUARDRAIL_FAMILY_MATCHES: 8/8
FALSE_HARD_FAILURE_ON_PRESSURE_CASES: 0
FALSE_REJECTION_OF_DECLARED_DERIVATIVE_VIEW: 0
UNDECLARED_PURPOSE_SHIFT_DETECTED: 1/1
AUTHORIAL_INTENT_OVERATTRIBUTION_DETECTED: 1/1
UNKNOWN_PURPOSE_PRESERVED_AS_UNDETERMINED: 1/1
SOURCE_FACT_INVENTION_ESCALATED_TO_HARD_FAILURE: 1/1
POST_REVEAL_CRITERION_CHANGE: no
POST_REVEAL_EXCEPTION_ADDED: no
```

## 6. Result

```text
RESULT:
SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS

GUARDRAIL_MODEL:
accepted_for_prospective_protocol_revision

HARD_FAILURE_AND_GUARDRAIL_SEPARATION:
pass_on_locked_constructed_cases
```

## 7. Methodological consequence

The guardrail model is accepted for prospective Specification protocol development.

It establishes the following operating principle:

```text
added_detail_or_viewpoint_change
!= automatic_failure

undeclared_or_unbounded_change_that_displaces_source_purpose_or_attributes_DSD_structure_to_source
= guardrail_breach
```

Guardrail status remains a separate ledger from hard specification status.

## 8. Limits

- constructed finite cases only;
- same project session and same assistant/model family;
- no independent evaluator;
- no measured comprehension, review-time, or error-rate effect;
- no external corpus has yet been scored under the new guardrail ledger;
- the challenge validates the internal distinction, not broad practical usefulness.

## 9. Next step

Create a prospective **DSD Specification Protocol v0.2** that incorporates the accepted guardrail ledger without rewriting v0.1 history, then apply v0.2 to `SPEC-APP-002` on a less-structured external corpus.
