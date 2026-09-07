# 03. DSD Specification / DSD 명세론

Status: **developing** — Protocol v0.1/v0.2 evidence preserved; Protocol v0.2.1 is current for new runs; `SPEC-CH-007` and first external v0.2.1 application `SPEC-APP-003` completed; first maturity audit still retains `developing` and has not yet been superseded by a re-audit.

Task: state explicitly what entities, statuses, inputs, prerequisites, outputs, transitions, and distinctions a system or study must preserve **without silently replacing the source's original purpose, priority, audience function, viewpoint, intentionally open judgment boundary, or site-specific implementation freedom with DSD-imposed structure**.

Primary DSD sources: Formation + General Property; Static Aggregation and Dynamics when output, reduction, or transition specifications matter.

Typical outputs include typed requirement/status tables, explicit bridges, external-standard boundaries, violation/unresolved conditions, guardrail records, and—when relevant—separate source-openness and downstream-determinacy records.

Boundary: DSD Specification organizes structural requirements; it does not replace domain-specific requirements engineering, standards, law, safety rules, clinical standards, scientific definitions, professional judgment, or other competent validation authorities.

## Protocol versions / 프로토콜 버전

- [`PROTOCOL.md`](PROTOCOL.md) — **v0.1**, historical protocol for `SPEC-CH-001~005`, `SPEC-APP-001`, and the first maturity audit.
- [`PROTOCOL_v0.2.md`](PROTOCOL_v0.2.md) — **v0.2**, protocol governing `SPEC-CH-006` transition evidence and `SPEC-APP-002`.
- [`PROTOCOL_v0.2.1.md`](PROTOCOL_v0.2.1.md) — **current protocol for new runs**, established after `SPEC-CH-007` and used for `SPEC-APP-003`.

v0.2 introduced:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION

HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

v0.2.1 adds:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

so intentional source openness does not become an excuse for a downstream task that genuinely demands missing determinacy.

## Direct method evidence / 개별 방법 직접 증거

Evidence lane: [`../../evidence/method_specific/specification/`](../../evidence/method_specific/specification/)

```text
SPEC-CH-001~005  v0.1 direct pilots
SPEC-CH-006      guardrail centerline challenge
SPEC-CH-007      source-openness / downstream-determinacy boundary challenge
```

### SPEC-CH-006

```text
PRECOMMIT: fe009d8da9ab992e6885d07e14ff26355b776a86
EXACT_GUARDRAIL_FAMILY_MATCHES: 8/8
FALSE_HARD_FAILURE_ON_PRESSURE_CASES: 0
RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-007

```text
PRECOMMIT: 1b3665696007b29535b3f46815cad39f4f02c03f
EXACT_SOURCE_OPENNESS_AXIS_MATCHES: 8/8
EXACT_DOWNSTREAM_DETERMINACY_AXIS_MATCHES: 8/8
EXACT_JOINT_AXIS_MATCHES: 8/8
FALSE_UNDERSPECIFICATION_ON_TASK_SUFFICIENT_INTENTIONAL_OPENNESS: 0
FALSE_OPENNESS_EXCUSE_FOR_MISSING_REQUIRED_DATA: 0
FALSE_DETERMINACY_FROM_INVENTED_VALUE: 0
RESULT: SPECIFICATION_OPENNESS_DETERMINACY_AXIS_SEPARATION_PILOT_PASS_WITH_LIMITATIONS
```

## External applications / 외부 적용

External evidence lane: [`../../evidence/real_world_cases/specification/`](../../evidence/real_world_cases/specification/)

### SPEC-APP-001 — RFC 9112 §6.3

Protocol: **v0.1**.

```text
SOURCE_UNIT_COVERAGE: 13/13
PRECEDENCE_PRESERVATION: 13/13
SOURCE_FIDELITY_RESULT: pass
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

### SPEC-APP-002 — Belmont Report Part C

Protocol: **v0.2**.

```text
EXTERNAL_DOMAIN: human-subject research ethics
SOURCE_UNIT_COVERAGE: 22/22
LOCAL_PRIORITY_PRESERVATION: 5/5
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED: 4/4
HARD_FAILURE_COUNT: 0
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
```

The Belmont original remains preferred for primary ethical reasoning; DSD adds a derivative trace/coverage checking layer.

### SPEC-APP-003 — OSHA Emergency Action Plan core corpus

Protocol: **v0.2.1**.

```text
EXTERNAL_DOMAIN: workplace emergency planning / occupational safety
PRECOMMIT: ccda4cfe9e9b25b3a97029c6a19c2e8e07076eb0
SOURCE_UNIT_COVERAGE: 18/18
REGULATORY_MINIMUM_ELEMENTS_PRESERVED: 11/11
SITE_SPECIFIC_OPENNESS_HANDLED_WITHOUT_FABRICATION: 7/7
INVENTED_SITE_SPECIFIC_FACTS: 0
NORMATIVE_FORCE_STRENGTHENINGS: 0
REGULATION_GUIDANCE_COLLAPSE: 0
HARD_FAILURE_COUNT: 0
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
RESULT: SPECIFICATION_EXTERNAL_V0_2_1_NO_GAIN_WITH_GUARDRAIL_PRESSURE
```

The OSHA corpus already combines a concise regulation, cross-referenced official guidance, and checklist-style review support. DSD v0.2.1 preserved the distinction between legal obligations, helpful guidance, and worksite-specific implementation openness, but did not demonstrate a material task-matched gain over that competent baseline. The DSD derivative is therefore retained as a method/evidence trace layer rather than a preferred operational replacement.

## Maturity audit / 성숙도 감사

First audit record: [`../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md`](../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md)

```text
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

That audit predates `SPEC-APP-002`, `SPEC-CH-007`, and `SPEC-APP-003`. Its verdict remains historical and is not silently overwritten. A new status decision requires a new re-audit.

## Evidence state / 증거 상태

```text
V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
V0_2_1_OPENNESS_TRANSITION_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 7

EXTERNAL_APPLICATIONS_TOTAL: 3
EXTERNAL_DOMAINS_TOTAL: 3
V0_2_EXTERNAL_APPLICATIONS: 1
V0_2_1_EXTERNAL_APPLICATIONS: 1

LATEST_EXTERNAL_RESULT: SPEC_NO_GAIN_WITH_GUARDRAIL_PRESSURE
CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2.1
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established
METHOD_STATUS: developing
ESTABLISHED_STATUS_AFTER_LATEST_EVIDENCE: not_reaudited
```

The strongest next evidence is now a genuinely independent retrace of an existing locked application. If that cannot be obtained, the next project-controlled step should be a new maturity re-audit that explicitly discounts dependence among same-project evaluations rather than treating three external corpora as three independent evaluators.
