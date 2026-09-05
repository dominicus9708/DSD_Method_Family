# Real-World Application Evidence / 외부 실제사례 적용 증거

This folder is reserved for applications to **independent real-world material** rather than synthetic toy cases or internally constructed benchmarks.

Examples include actual events, judicial cases, historical incidents, personal cases, empirical datasets, and documented organizational or technical incidents.

## Separation rule / 분리 원칙

`CASE_ORIGIN` is separate from `EVIDENCE_SCOPE_CLASS`.

A judicial case may be a method-specific Audit case. A historical incident may combine Interpretation, Comparison, Provenance, and Lineage. A personal case may be useful as an application example but remain too weak to validate a method.

## Required case fields

```text
CASE_ORIGIN:
  real_event
  judicial_case
  historical_case
  personal_case
  empirical_dataset
  organizational_or_technical_incident

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

## Source discipline / 출처 규율

- Case facts are locked separately from DSD interpretation.
- A real event should prefer official, primary, or otherwise authoritative records where available.
- A judicial case should distinguish the judgment/decision text, procedural posture, legal issue, later treatment, and commentary.
- A historical case should distinguish primary sources, later compilations, scholarship, and uncertain reconstruction.
- A personal case should minimize identifying or sensitive information and document consent/permission where relevant.
- Conflicting sources are preserved rather than silently merged into one narrative.

## Validation limit / 검증 한계

A real-world case is application evidence first. It contributes to method validation only when the method protocol, scoring/failure criteria, external standard, and relevant baseline were locked well enough to make the case a genuine test rather than an illustration.
