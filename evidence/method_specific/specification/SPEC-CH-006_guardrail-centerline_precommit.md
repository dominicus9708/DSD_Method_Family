# SPEC-CH-006 Precommit — Guardrail Centerline Challenge / 가드레일 중심선 도전

Date: 2026-09-07
Evidence scope: `method_specific`
Method directly tested: **DSD Specification / DSD 명세론**
Protocol basis: **Specification Protocol v0.1 + prospective guardrail candidate profile**

## 1. Purpose

This challenge tests whether purpose, priority, detail burden, and viewpoint changes can be treated as **guardrails** rather than automatic discard conditions.

The challenge is designed to distinguish:

```text
HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_BUT_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

A viewpoint change or added detail is not automatically an error. The failure occurs when the change is undeclared, source intent is invented, purpose/priority is functionally displaced, or representation burden exceeds the declared task without being bounded.

## 2. Candidate guardrails locked before scoring

### G1 — Source fidelity / 원문 충실도

Do not invent, silently delete, or strengthen source facts, requirements, normative force, or authorial intent.

### G2 — Purpose and priority fidelity / 목적·우선순위 충실도

Preserve the source's primary purpose, target user/action, and priority hierarchy when they are source-supported. If the DSD representation changes purpose, the change must be declared as a derivative viewpoint rather than attributed back to the source.

### G3 — Detail proportionality / 디테일 비례성

Additional atomization or structural detail is permitted when it serves the declared task. Added detail becomes a guardrail concern when it obscures the source's primary action path, materially increases representation burden without operational gain, or makes secondary structure appear coequal with primary structure.

### G4 — Viewpoint separation / 관점 분리

Keep source-stated structure separate from DSD-added structure, interpretation, grouping, or purpose. A DSD-derived viewpoint may be useful, but it must not be presented as the source author's original intended ontology, hierarchy, or purpose without evidence.

## 3. Guardrail status vocabulary

```text
INSIDE_GUARDRAILS
GUARDRAIL_PRESSURE
GUARDRAIL_EXCEEDED_RECOVERABLE
PURPOSE_OR_VIEWPOINT_DISTORTED
UNDETERMINED
```

These statuses are separate from hard specification failures.

## 4. Hard-failure boundary

The following remain hard specification failures or unresolved specification defects under the existing protocol when applicable:

```text
SOURCE_FACT_INVENTION
SILENT_REQUIRED_SOURCE_OMISSION
SPEC_CONTRADICTION
REQUIRED_BRIDGE_OMISSION
SPEC_WRONG_STANDARD
CLAIM_RELEVANT_STATUS_COLLAPSE
```

Guardrail pressure does not become a hard failure merely because the representation is verbose, differently organized, or explicitly derivative.

## 5. Locked cases and expected verdicts

### C1 — Declared derivative appendix

Source purpose: short operator checklist for immediate action.
DSD representation: preserves the checklist as the primary view and adds a separately labeled analytic appendix with typed states and dependencies.
Viewpoint change: explicitly declared as DSD analytic derivative.

Expected:

```text
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
HARD_FAILURE: no
```

### C2 — Redundant but bounded detail

Source purpose and action path remain visible and unchanged.
DSD representation repeats several type/status annotations that add little operational value.

Expected:

```text
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
PRESSURE: detail_inflation
HARD_FAILURE: no
```

### C3 — Priority encoded but presentation flattened

All source priority relations are preserved in explicit metadata, but the visible DSD table presents primary and secondary items with equal prominence.

Expected:

```text
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
PRESSURE: priority_flattening_risk
HARD_FAILURE: no
```

### C4 — Critical path buried by atomization

All source facts remain present, but the original rapid-action path is replaced by a long atom list and the critical first action is no longer readily identifiable.
The representation can be repaired by restoring a primary view without changing the atoms.

Expected:

```text
GUARDRAIL_VERDICT: GUARDRAIL_EXCEEDED_RECOVERABLE
BREACH: purpose_function_obscured_by_detail
HARD_FAILURE: no
```

### C5 — Undeclared purpose substitution

Source purpose: rapid emergency action guidance.
DSD output is presented as if the source's purpose were comprehensive structural classification, with no declaration that the purpose was changed for analysis.
All source facts are otherwise retained.

Expected:

```text
GUARDRAIL_VERDICT: PURPOSE_OR_VIEWPOINT_DISTORTED
BREACH: undeclared_purpose_shift
HARD_FAILURE: no
```

### C6 — DSD ontology attributed to source author

The source lists operational conditions but does not claim a DSD-style status ontology.
The output states that the source author intended the DSD ontology.

Expected:

```text
GUARDRAIL_VERDICT: PURPOSE_OR_VIEWPOINT_DISTORTED
BREACH: authorial_intent_overattribution
HARD_FAILURE: no unless extra source facts are also invented
```

### C7 — Unknown source purpose preserved as unknown

The source gives requirements but does not establish a primary audience or communicative purpose.
The DSD record leaves `SOURCE_PRIMARY_PURPOSE` and `SOURCE_TARGET_USER` as `UNDETERMINED` and does not invent them.

Expected:

```text
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
HARD_FAILURE: no
```

### C8 — Invented purpose used to justify a new obligation

The source does not establish a primary purpose or the added obligation.
The DSD output invents a purpose and uses it to justify a new mandatory requirement.

Expected:

```text
GUARDRAIL_VERDICT: PURPOSE_OR_VIEWPOINT_DISTORTED
HARD_FAILURE: yes
HARD_FAILURE_CLASS: SOURCE_FACT_INVENTION
```

## 6. Scoring criteria

The challenge passes only if all of the following hold:

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

## 7. Promotion rule if challenge passes

A pass authorizes creation of a prospective **DSD Specification Protocol v0.2** that:

1. preserves v0.1 historical records unchanged;
2. adds a source-purpose/viewpoint lock;
3. adds a separate guardrail ledger rather than converting all guardrail pressure into hard failure;
4. permits declared derivative viewpoints;
5. records detail and priority burden;
6. may add an optional precedence/priority field prospectively because `SPEC-APP-001` already exposed that nonfatal pressure point;
7. does not retroactively rescore `SPEC-CH-001~005` or `SPEC-APP-001`.
