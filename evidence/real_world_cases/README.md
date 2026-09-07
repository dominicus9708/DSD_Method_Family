# Real-World Application Evidence / 외부 실제사례 적용 증거

This folder is reserved for applications to **independent real-world material** rather than synthetic toy cases or internally constructed benchmarks.

Examples include actual events, judicial cases, historical incidents, personal cases, empirical datasets, documented organizational or technical incidents, public normative standards/specifications, ethics/policy guidelines, and public regulatory standards with official guidance.

## Separation rule / 분리 원칙

`CASE_ORIGIN` is separate from `EVIDENCE_SCOPE_CLASS`.

A judicial case may be a method-specific Audit case. A public standard, ethics guideline, or regulatory corpus may directly test Specification while remaining external-source application evidence rather than a synthetic benchmark.

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
  public_regulatory_standard_plus_official_guidance

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
- An ethics/policy guideline should lock purpose, intended actors, normative generality, and acknowledged judgment space.
- A regulation-plus-guidance corpus should distinguish binding regulatory text, incorporated requirements, official explanation, examples, recommendations, and worksite/domain-specific implementation values.
- Conflicting or differently weighted sources are preserved rather than silently merged into one narrative.

## Current external application records / 현재 외부 적용 기록

### DSD Specification

#### SPEC-APP-001 — RFC 9112 §6.3

- [`specification/SPEC-APP-001_RFC9112_message-body-length_precommit.md`](specification/SPEC-APP-001_RFC9112_message-body-length_precommit.md)
- [`specification/SPEC-APP-001_RFC9112_message-body-length.md`](specification/SPEC-APP-001_RFC9112_message-body-length.md)

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

- [`specification/SPEC-APP-002_Belmont-Part-C_precommit.md`](specification/SPEC-APP-002_Belmont-Part-C_precommit.md)
- [`specification/SPEC-APP-002_Belmont-Part-C.md`](specification/SPEC-APP-002_Belmont-Part-C.md)

```text
PROTOCOL: v0.2
CASE_ORIGIN: public_normative_ethics_guideline
EXTERNAL_DOMAIN: human-subject research ethics
SOURCE_UNIT_COVERAGE: 22/22
LOCAL_PRIORITY_PRESERVATION: 5/5
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED: 4/4
HARD_FAILURE_COUNT: 0
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
```

The original Belmont prose remains preferred for primary ethical reasoning; DSD adds a derivative traceability and structural coverage layer.

#### SPEC-APP-003 — OSHA Emergency Action Plan core corpus

- [`specification/SPEC-APP-003_OSHA_EAP_core_guidance_precommit.md`](specification/SPEC-APP-003_OSHA_EAP_core_guidance_precommit.md)
- [`specification/SPEC-APP-003_OSHA_EAP_core_guidance.md`](specification/SPEC-APP-003_OSHA_EAP_core_guidance.md)

```text
PROTOCOL: v0.2.1
CASE_ORIGIN: public_regulatory_standard_plus_official_guidance
EXTERNAL_DOMAIN: workplace emergency planning / occupational safety
SOURCE: 29 CFR 1910.38 + OSHA EAP/alarm eTool and checklist material
SOURCE_UNIT_COVERAGE: 18/18
REGULATORY_MINIMUM_ELEMENTS_PRESERVED: 11/11
SITE_SPECIFIC_OPENNESS_HANDLED_WITHOUT_FABRICATION: 7/7
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
INVENTED_SITE_SPECIFIC_FACTS: 0
NORMATIVE_FORCE_STRENGTHENINGS: 0
REGULATION_GUIDANCE_COLLAPSE: 0
HARD_FAILURE_COUNT: 0
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

This first external v0.2.1 run demonstrates that the method can preserve required categories while leaving source-supported site-specific implementation open, without treating missing workplace facts as a defect in the regulation or fabricating them. It does not establish a practical advantage over OSHA's own strong cross-referenced regulation/eTool/checklist baseline.

## Validation limit / 검증 한계

A real-world or external-source case is application evidence first. It contributes to method validation only when protocol, scoring/failure criteria, external standard, source-purpose boundary, and relevant baseline were locked well enough to make the case a genuine test rather than an illustration.

An external origin and an independent evaluator are different axes. The current Specification external corpus spans three domains and three document/source configurations, but all DSD scoring remains within the same project/model environment. Independent reviewer validation therefore remains unresolved.
