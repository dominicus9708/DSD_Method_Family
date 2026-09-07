# 03. DSD Specification / DSD 명세론

Status: **developing** — Protocol v0.1/v0.2 evidence preserved; prospective Protocol v0.2.1 is current for new runs after `SPEC-CH-007`; two external applications completed; first maturity audit still retains `developing`.

Task: state explicitly what entities, statuses, inputs, prerequisites, outputs, transitions, and distinctions a system or study must preserve **without silently replacing the source's original purpose, priority, audience function, viewpoint, or intentionally open judgment boundary with a DSD-imposed deterministic structure**.

Primary DSD sources: Formation + General Property; Static Aggregation and Dynamics when output, reduction, or transition specifications matter.

Typical outputs include typed requirement/status tables, explicit bridges, external-standard boundaries, violation/unresolved conditions, guardrail records, and—when relevant—separate source-openness and downstream-determinacy records.

Boundary: DSD Specification organizes structural requirements; it does not replace domain-specific requirements engineering, standards, law, safety rules, clinical standards, scientific definitions, professional judgment, or other competent validation authorities.

## Protocol versions / 프로토콜 버전

- [`PROTOCOL.md`](PROTOCOL.md) — **v0.1**, historical protocol for `SPEC-CH-001~005`, `SPEC-APP-001`, and the first maturity audit.
- [`PROTOCOL_v0.2.md`](PROTOCOL_v0.2.md) — **v0.2**, historical/prospective protocol governing `SPEC-CH-006` transition evidence and `SPEC-APP-002`.
- [`PROTOCOL_v0.2.1.md`](PROTOCOL_v0.2.1.md) — **current protocol for new runs** after `SPEC-CH-007`.

v0.2 introduced the method-specific guardrails:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

with:

```text
HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

v0.2.1 adds a separate two-axis distinction:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

A valid joint state is:

```text
SOURCE_INTENTIONAL_OPENNESS
+ UNDERDETERMINED_FOR_DECLARED_TASK
```

so intentional source openness does not become an excuse for a downstream task that genuinely demands missing determinacy.

## Direct method evidence / 개별 방법 직접 증거

Evidence lane: [`../../evidence/method_specific/specification/`](../../evidence/method_specific/specification/)

### SPEC-CH-001~005 — v0.1

The five initial direct pilots remain unchanged.

### SPEC-CH-006 — Guardrail Centerline Challenge

```text
PRECOMMIT: fe009d8da9ab992e6885d07e14ff26355b776a86
EXACT_GUARDRAIL_FAMILY_MATCHES: 8/8
FALSE_HARD_FAILURE_ON_PRESSURE_CASES: 0
FALSE_REJECTION_OF_DECLARED_DERIVATIVE_VIEW: 0
RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-007 — Source-Intentional Openness / Underspecification Boundary

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

The crucial result is that `SOURCE_INTENTIONAL_OPENNESS` and `SPEC_UNDERSPECIFIED` are not logical opposites. The former describes source-supported openness; the latter remains relative to the declared downstream task.

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

Purpose/detail/viewpoint guardrails were not formal precommitted axes in this run and are not retroactively scored.

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

The Belmont original remains preferred for primary ethical reading/contextual reasoning; the DSD derivative adds source-unit traceability and coverage/review checkability. This application exposed the openness/underspecification pressure later tested by `SPEC-CH-007`.

## Maturity audit / 성숙도 감사

First audit record: [`../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md`](../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md)

```text
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

That audit predates `SPEC-APP-002` and `SPEC-CH-007`. Its verdict is preserved. A new status decision requires a separate re-audit rather than silent promotion.

## Evidence state / 증거 상태

```text
V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
V0_2_1_OPENNESS_TRANSITION_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 7

EXTERNAL_APPLICATIONS_TOTAL: 2
EXTERNAL_DOMAINS_TOTAL: 2
V0_2_EXTERNAL_APPLICATIONS: 1
V0_2_1_EXTERNAL_APPLICATIONS: 0

CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2.1
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established
METHOD_STATUS: developing
ESTABLISHED_STATUS_AFTER_LATEST_EVIDENCE: not_reaudited
```

The strongest next evidence is a genuinely independent retrace of an existing locked application. If that cannot yet be obtained, the next project-controlled step should be a new external application under v0.2.1 rather than pretending a same-session rerun is independent.
