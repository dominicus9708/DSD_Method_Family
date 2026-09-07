# SPEC-APP-002 — Belmont Report Part C External Application Precommit

Date: 2026-09-07
Method directly tested: **DSD Specification / DSD 명세론**
Protocol: **Specification Protocol v0.2**
Case origin: `public_normative_ethics_guideline`
External domain: human-subject research ethics

## 1. Locked source

Primary source:
- **The Belmont Report — Ethical Principles and Guidelines for the Protection of Human Subjects of Research**
- National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research
- Original report date: 1979-04-18
- Authoritative current host: HHS Office for Human Research Protections (OHRP)
- Locked corpus: **Part C. Applications**, comprising:
  - C.1 Informed Consent
  - C.2 Assessment of Risks and Benefits
  - C.3 Selection of Subjects

Purpose/context evidence is locked from the report summary and introductory ethical-principles section, not inferred from DSD.

Secondary competent baseline:
- HHS OHRP Assurance Training summary of Belmont principles and resulting conduct requirements.

No later regulation, Common Rule provision, IRB decision, or modern clinical guideline may be silently merged into the locked Belmont corpus.

## 2. Source-purpose / viewpoint lock

```text
SOURCE_PRIMARY_PURPOSE:
  provide basic ethical principles and guidelines that assist resolution of ethical problems in research involving human subjects

SOURCE_PURPOSE_EVIDENCE:
  explicit in Belmont summary/introduction

SOURCE_TARGET_USER_OR_ACTOR:
  scientists / investigators, IRB or review-board members, Federal employees;
  broader explanatory audience includes subjects, reviewers, and interested citizens

SOURCE_PRIMARY_ACTION_OR_DECISION:
  ethical analysis and judgment concerning conduct/review of human-subject research

SOURCE_PRIORITY_HIERARCHY:
  no single total ordering among Respect for Persons / Beneficence / Justice is declared;
  Part C links them respectively to informed consent, risk-benefit assessment, and subject selection;
  local conditional priority relations may appear inside particular applications

SOURCE_COMMUNICATION_OR_USE_FUNCTION:
  analytical ethical framework and guidance, not a mechanically complete administrative rulebook
```

The source explicitly acknowledges that its principles do not always resolve difficult cases beyond dispute. DSD must not convert that acknowledged normative openness into a false deterministic decision procedure.

## 3. DSD transformation lock

```text
TRANSFORMATION_PURPOSE:
  produce a retraceable structural requirement map of Part C while preserving the Belmont Report's ethical-framework function and unresolved judgment boundaries

VIEWPOINT_CHANGE_DECLARED: yes
DERIVATIVE_VIEW_LABEL: DSD structural specification view of Belmont Part C

DSD_ADDED_STRUCTURE_ALLOWED:
  typed requirement atoms
  actor/scope separation
  activation conditions
  explicit local dependencies
  explicit unresolved conditions
  optional local precedence markers when source-supported

DSD_ADDED_STRUCTURE_PROHIBITED_FROM_SOURCE_ATTRIBUTION:
  DSD ontology or status vocabulary may not be attributed to Belmont authors
  no new legal/regulatory force may be assigned
  no global priority among the three principles may be invented
  no unresolved ethical judgment may be rewritten as a deterministic algorithm without source support
```

## 4. DSD layer lock

```text
FORMATION_LAYER: not used as substantive external-domain ontology
PROPERTY_CORE: used only as an internal typed/status bookkeeping aid where necessary
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: none
```

This application is primarily a Specification-method test, not a claim that Belmont itself instantiates DSD formal objects.

## 5. Strongest reasonable baselines

```text
BASELINE_A:
  Belmont Part C original prose itself
  role: semantic/purpose/nuance baseline

BASELINE_B:
  current HHS OHRP Assurance Training summary
  role: competent official concise requirement-summary baseline
```

A DSD gain claim must beat the relevant competent baseline for the claimed task. Cosmetic atomization, relabeling, or extra length does not count as gain.

## 6. Precommitted source-unit inventory

The locked corpus will be evaluated over these source-supported units before DSD atomization:

```text
U01 three Part-C application domains
U02 informed-consent opportunity/autonomy purpose
U03 informed-consent three-element structure
U04 information disclosure scope and sufficiency problem
U05 incomplete-disclosure constraints
U06 comprehension presentation/context obligation
U07 comprehension adaptation and verification obligation
U08 diminished-capacity subject protection / third-party role
U09 voluntariness / coercion / undue-influence boundary
U10 risk-benefit assessment actor-specific functions
U11 risk and benefit conceptual distinctions
U12 multi-domain harms/benefits and affected parties
U13 subject-centered weighting with protected rights
U14 systematic nonarbitrary risk-benefit assessment
U15 explicit risk-estimation and alternative-procedure checks
U16 nonnegotiable / heightened risk-review considerations
U17 justice link to fair subject selection
U18 individual vs social justice distinction
U19 class-order / vulnerable-population conditionality
U20 distributive injustice beyond individual fairness
U21 already-burdened populations and therapeutic-relevance exception
U22 anti-convenience / anti-manipulability protection for vulnerable groups
```

The final atom count may differ from 22, but all 22 locked source units must remain traceable.

## 7. Precommitted hard-failure criteria

```text
H1 SOURCE_FACT_INVENTION
H2 SILENT_REQUIRED_SOURCE_OMISSION
H3 NORMATIVE_FORCE_STRENGTHENING
H4 FALSE_GLOBAL_PRIORITY_INVENTION
H5 UNRESOLVED_ETHICAL_JUDGMENT_CONVERTED_TO_DETERMINISTIC_RULE
H6 REQUIRED_ACTOR_OR_SCOPE_COLLAPSE
H7 EXTERNAL_STANDARD_SUBSTITUTION
H8 DSD_DERIVATIVE_STRUCTURE_ATTRIBUTED_TO_SOURCE_AUTHOR
```

Any H1-H8 occurrence is a hard failure for the affected claim/atom.

## 8. Precommitted guardrail criteria

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

Guardrail verdict vocabulary:

```text
INSIDE_GUARDRAILS
GUARDRAIL_PRESSURE
GUARDRAIL_EXCEEDED_RECOVERABLE
PURPOSE_OR_VIEWPOINT_DISTORTED
UNDETERMINED
```

Guardrail pressure is not automatically a hard failure.

## 9. Precommitted gain criteria

Possible DSD operational gains are limited to:

```text
DISTINCTION_GAIN
TRACEABILITY_GAIN
AMBIGUITY_REDUCTION_GAIN
DOWNSTREAM_CHECKABILITY_GAIN
```

A gain is counted only if it is achieved without purpose/viewpoint distortion and against the relevant competent baseline.

The following do not count as gain:
- more fields;
- longer output;
- DSD terminology by itself;
- extracting distinctions already explicit in Baseline B;
- turning ethical judgment into false certainty.

## 10. Required scoring outputs

```text
SOURCE_UNIT_COVERAGE:
SOURCE_PURPOSE_PRESERVATION:
ACTOR_SCOPE_PRESERVATION:
LOCAL_PRIORITY_PRESERVATION:
GLOBAL_PRIORITY_INVENTION_COUNT:
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED:
INVENTED_SOURCE_FACTS:
SILENTLY_DROPPED_SOURCE_OBLIGATIONS:
NORMATIVE_FORCE_STRENGTHENINGS:
DSD_VIEWPOINT_OVERATTRIBUTIONS:

DISTINCTION_GAIN:
TRACEABILITY_GAIN:
AMBIGUITY_REDUCTION_GAIN:
DOWNSTREAM_CHECKABILITY_GAIN:

DETAIL_INFLATION:
REPRESENTATION_BURDEN:
GUARDRAIL_VERDICT:
FINAL_SPEC_STATUS:
COMPETITIVE_RESULT:
```

## 11. Allowed final result families

```text
DSD_GAIN_DEMONSTRATED_WITHIN_GUARDRAILS
MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
SPEC_NO_GAIN
BASELINE_PREFERRED
GUARDRAIL_EXCEEDED_RECOVERABLE
PURPOSE_OR_VIEWPOINT_DISTORTED
SPEC_UNDERSPECIFIED
HARD_FAILURE
```

Unfavorable, mixed, and `NO_GAIN` results must be preserved.

## 12. Anti-post-hoc rule

After this precommit is committed:
- no source unit may be dropped because it hurts DSD performance;
- no gain criterion may be relaxed;
- no guardrail may be removed;
- no Belmont ambiguity may be resolved by importing later regulation unless explicitly marked as external context and excluded from the locked score;
- no new DSD field may be added and then scored retrospectively for this run.
