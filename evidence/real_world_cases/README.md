# Real-World Application Evidence / 외부 실제사례 적용 증거

This folder is reserved for applications to **independent real-world material** rather than synthetic toy cases or internally constructed benchmarks.

Examples include actual events, judicial cases, historical incidents, personal cases, empirical datasets, documented organizational or technical incidents, public normative standards/specifications, and independently authored ethics/policy guidelines.

## Separation rule / 분리 원칙

`CASE_ORIGIN` is separate from `EVIDENCE_SCOPE_CLASS`.

A judicial case may be a method-specific Audit case. A historical incident may combine Interpretation, Comparison, Provenance, and Lineage. A public normative standard or ethics guideline may directly test Specification while remaining external-source application evidence rather than a synthetic benchmark.

## Required case fields

```text
CASE_ORIGIN:
  real_event
  judicial_case
  historical_case
  personal_case
  empirical_dataset
  organizational_or_technical_incident
  public_normative_standard
  public_normative_ethics_guideline

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
- A real event should prefer official, primary, or otherwise authoritative records where available.
- A judicial case should distinguish the judgment/decision text, procedural posture, legal issue, later treatment, and commentary.
- A historical case should distinguish primary sources, later compilations, scholarship, and uncertain reconstruction.
- A personal case should minimize identifying or sensitive information and document consent/permission where relevant.
- A public normative standard should lock authoritative version/status, relevant updates/errata, normative-force notation, and exact section scope before DSD scoring.
- An ethics/policy guideline should additionally lock its **purpose, intended audience/actors, level of normative generality, and acknowledged judgment space** so a derivative structural representation does not silently convert principles into a false deterministic rulebook.
- Conflicting sources are preserved rather than silently merged into one narrative.

## Current external application records / 현재 외부 적용 기록

### DSD Specification

#### SPEC-APP-001 — RFC 9112 §6.3

- [`specification/SPEC-APP-001_RFC9112_message-body-length_precommit.md`](specification/SPEC-APP-001_RFC9112_message-body-length_precommit.md)
- [`specification/SPEC-APP-001_RFC9112_message-body-length.md`](specification/SPEC-APP-001_RFC9112_message-body-length.md)

```text
PROTOCOL: v0.1
CASE_ORIGIN: public_normative_standard
SOURCE: RFC 9112 §6.3 core message-body-length precedence algorithm
METHOD_DIRECTLY_TESTED: DSD Specification
SOURCE_UNIT_COVERAGE: 13/13
PRECEDENCE_PRESERVATION: 13/13
BCP14_MUST_OBLIGATIONS_PRESERVED: 8/8
INVENTED_SOURCE_FACTS: 0
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
PROTOCOL_PRESSURE: ordered precedence / priority, present_nonfatal
INDEPENDENT_EVALUATOR_VALIDATION: not_established
```

#### SPEC-APP-002 — Belmont Report Part C. Applications

- [`specification/SPEC-APP-002_Belmont-Part-C_precommit.md`](specification/SPEC-APP-002_Belmont-Part-C_precommit.md)
- [`specification/SPEC-APP-002_Belmont-Part-C.md`](specification/SPEC-APP-002_Belmont-Part-C.md)

```text
PROTOCOL: v0.2
CASE_ORIGIN: public_normative_ethics_guideline
EXTERNAL_DOMAIN: human-subject research ethics
SOURCE: Belmont Report Part C. Applications
SOURCE_UNIT_COVERAGE: 22/22
LOCAL_PRIORITY_PRESERVATION: 5/5
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED: 4/4
HARD_FAILURE_COUNT: 0
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
```

The Belmont case is the first external v0.2 run. It preserves the source's analytical-ethical function and keeps the DSD structural map derivative. The original prose remains preferred for primary ethical reasoning, while DSD adds traceability and coverage/checkability for a review task.

The case also exposes a nonfatal distinction requiring future method-specific testing:

```text
source-intentional normative openness
!= accidental specification underspecification
```

## Validation limit / 검증 한계

A real-world or external-source case is application evidence first. It contributes to method validation only when the method protocol, scoring/failure criteria, external standard, source-purpose boundary, and relevant baseline were locked well enough to make the case a genuine test rather than an illustration.

An external origin and an independent evaluator are different axes. The current Specification external corpus spans two domains, but genuinely independent reviewer/model validation remains unresolved.
