# DSD Specification Method-Specific Evidence / DSD 명세론 개별 방법 직접 증거

Status: **seven direct constructed pilots + three external applications + first maturity audit completed / v0.2.1 current for new runs / developing retained**  
Date: 2026-09-07  
Method: **DSD Specification / DSD 명세론**

Protocol versions:
- v0.1 historical: [`../../../methods/03_specification/PROTOCOL.md`](../../../methods/03_specification/PROTOCOL.md)
- v0.2 historical/current-evidence protocol: [`../../../methods/03_specification/PROTOCOL_v0.2.md`](../../../methods/03_specification/PROTOCOL_v0.2.md)
- v0.2.1 current for new runs: [`../../../methods/03_specification/PROTOCOL_v0.2.1.md`](../../../methods/03_specification/PROTOCOL_v0.2.1.md)

Shared-core pilots SC-01 through SC-10 may be reused as operating disciplines, but they do not count as direct Specification validation.

## Direct evidence registry / 직접 증거 레지스트리

### SPEC-CH-001 through SPEC-CH-005 — v0.1 evidence

```text
SPEC-CH-001  SPECIFICATION_DISCRIMINATION_PILOT_PASS_WITH_LIMITATIONS
SPEC-CH-002  SPECIFICATION_CONTRADICTION_UNDERSPECIFICATION_PILOT_PASS_WITH_LIMITATIONS
SPEC-CH-003  SPECIFICATION_OPTIONAL_LAYER_BRIDGE_BOUNDARY_PILOT_PASS_WITH_LIMITATIONS
SPEC-CH-004  SPECIFICATION_NO_GAIN_PILOT_PASS_WITH_LIMITATIONS
SPEC-CH-005  SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_PASS_WITH_LIMITATIONS
```

`SPEC-CH-005` supports procedural retraceability and order stability on a locked constructed packet, not independent reviewer validation.

### SPEC-CH-006 — Guardrail Centerline Challenge

```text
PRECOMMIT_COMMIT: fe009d8da9ab992e6885d07e14ff26355b776a86
EXACT_GUARDRAIL_FAMILY_MATCHES: 8/8
FALSE_HARD_FAILURE_ON_PRESSURE_CASES: 0
FALSE_REJECTION_OF_DECLARED_DERIVATIVE_VIEW: 0
RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS
```

Accepted guardrail profile:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

### SPEC-CH-007 — Source-Intentional Openness / Accidental Underspecification Boundary

Precommit: [`SPEC-CH-007_open-texture-underspecification_precommit.md`](SPEC-CH-007_open-texture-underspecification_precommit.md)  
Result: [`SPEC-CH-007_open-texture-underspecification.md`](SPEC-CH-007_open-texture-underspecification.md)

```text
PRECOMMIT_COMMIT: 1b3665696007b29535b3f46815cad39f4f02c03f
EXACT_SOURCE_OPENNESS_AXIS_MATCHES: 8/8
EXACT_DOWNSTREAM_DETERMINACY_AXIS_MATCHES: 8/8
EXACT_JOINT_AXIS_MATCHES: 8/8
TASK_SUFFICIENT_INTENTIONAL_OPENNESS_ACCEPTED: 2/2
INTENTIONAL_OPENNESS_WITH_AUTOMATION_GAP_PRESERVED: 1/1
ACCIDENTAL_OR_UNRESOLVED_MISSING_DATA_DETECTED: 3/3
UNSUPPORTED_INTENT_NOT_INVENTED: 3/3
INVENTED_RESOLUTION_ESCALATED_TO_HARD_FAILURE: 1/1
FALSE_UNDERSPECIFICATION_ON_TASK_SUFFICIENT_INTENTIONAL_OPENNESS: 0
FALSE_OPENNESS_EXCUSE_FOR_MISSING_REQUIRED_DATA: 0
FALSE_DETERMINACY_FROM_INVENTED_VALUE: 0
RESULT: SPECIFICATION_OPENNESS_DETERMINACY_AXIS_SEPARATION_PILOT_PASS_WITH_LIMITATIONS
```

The key result is:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

A source may intentionally preserve professional/contextual judgment while still being underdetermined for a stronger automated downstream task. `SPEC_UNDERSPECIFIED` remains task-relative and is not weakened.

## External applications / 외부·독립 생성 corpus 적용

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
RESULT: SPECIFICATION_EXTERNAL_GUARDRAIL_APPLICATION_PASS_WITH_MIXED_GAIN
```

The Belmont case exposed the openness/underspecification pressure subsequently isolated by `SPEC-CH-007`. It remains a v0.2 record and is not rescored under v0.2.1.

### SPEC-APP-003 — OSHA Emergency Action Plan core corpus

Protocol: **v0.2.1**  
Precommit: [`../../real_world_cases/specification/SPEC-APP-003_OSHA_EAP_core_guidance_precommit.md`](../../real_world_cases/specification/SPEC-APP-003_OSHA_EAP_core_guidance_precommit.md)  
Result: [`../../real_world_cases/specification/SPEC-APP-003_OSHA_EAP_core_guidance.md`](../../real_world_cases/specification/SPEC-APP-003_OSHA_EAP_core_guidance.md)

```text
CASE_ORIGIN: public_regulatory_standard_plus_official_guidance
EXTERNAL_DOMAIN: workplace emergency planning / occupational safety
PRECOMMIT_COMMIT: ccda4cfe9e9b25b3a97029c6a19c2e8e07076eb0
SOURCE_UNIT_COVERAGE: 18/18
REGULATORY_MINIMUM_ELEMENTS_PRESERVED: 11/11
SOURCE_INTENTIONAL_OPENNESS_HANDLED_WITHOUT_FABRICATION: 7/7
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
INVENTED_SITE_SPECIFIC_FACTS: 0
NORMATIVE_FORCE_STRENGTHENINGS: 0
REGULATION_GUIDANCE_COLLAPSE: 0
HARD_FAILURE_COUNT: 0
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
RESULT: SPECIFICATION_EXTERNAL_V0_2_1_NO_GAIN_WITH_GUARDRAIL_PRESSURE
```

This is the first external v0.2.1 application. The corpus determines required EAP categories while intentionally leaving exact worksite implementation to the employer within applicable constraints. v0.2.1 preserved that openness as sufficient for the locked structural-review task and did not fabricate local routes, devices, people, or procedures.

The strongest OSHA baseline already combines regulation, section-linked eTool guidance, and checklist-style review support. Therefore the additional DSD typing and openness/determinacy ledger did not demonstrate a material operational gain for this locked task. The unfavorable comparative result is preserved.

## Maturity meta-audit / 성숙도 메타감사

The first maturity audit remains a DSD Audit meta-record rather than an eighth direct Specification pilot.

```text
AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

That audit predates `SPEC-APP-002`, `SPEC-CH-007`, and `SPEC-APP-003`. Its verdict is preserved until a new re-audit is explicitly performed.

## Current evidence state / 현재 증거 상태

```text
V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
V0_2_1_OPENNESS_TRANSITION_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 7

EXTERNAL_APPLICATIONS_TOTAL: 3
EXTERNAL_DOMAINS_TOTAL: 3
V0_2_EXTERNAL_APPLICATIONS: 1
V0_2_1_EXTERNAL_APPLICATIONS: 1

CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2.1
LATEST_EXTERNAL_RESULT: SPEC_NO_GAIN_WITH_GUARDRAIL_PRESSURE
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established
CURRENT_METHOD_STATUS: developing
ESTABLISHED_STATUS_AFTER_LATEST_EVIDENCE: not_reaudited
```

At this point another same-project external application has lower evidential value than a genuinely independent retrace. If independent review remains unavailable, the next internal step should be a new maturity re-audit that explicitly discounts the common evaluator/model dependence across all three external corpora.
