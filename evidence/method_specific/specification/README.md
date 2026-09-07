# DSD Specification Method-Specific Evidence / DSD 명세론 개별 방법 직접 증거

Status: **six direct constructed pilots + two external applications + first maturity audit completed / v0.2 current for new runs / developing retained**  
Date: 2026-09-07  
Method: **DSD Specification / DSD 명세론**

Protocol versions:
- v0.1 historical: [`../../../methods/03_specification/PROTOCOL.md`](../../../methods/03_specification/PROTOCOL.md)
- v0.2 current for new runs: [`../../../methods/03_specification/PROTOCOL_v0.2.md`](../../../methods/03_specification/PROTOCOL_v0.2.md)

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

### SPEC-CH-006 — Guardrail Centerline Challenge / 가드레일 중심선 도전

Precommit: [`SPEC-CH-006_guardrail-centerline_precommit.md`](SPEC-CH-006_guardrail-centerline_precommit.md)  
Result: [`SPEC-CH-006_guardrail-centerline.md`](SPEC-CH-006_guardrail-centerline.md)

```text
PRECOMMIT_COMMIT: fe009d8da9ab992e6885d07e14ff26355b776a86
EXACT_GUARDRAIL_FAMILY_MATCHES: 8/8
FALSE_HARD_FAILURE_ON_PRESSURE_CASES: 0
FALSE_REJECTION_OF_DECLARED_DERIVATIVE_VIEW: 0
UNDECLARED_PURPOSE_SHIFT_DETECTED: 1/1
AUTHORIAL_INTENT_OVERATTRIBUTION_DETECTED: 1/1
UNKNOWN_PURPOSE_PRESERVED_AS_UNDETERMINED: 1/1
SOURCE_FACT_INVENTION_ESCALATED_TO_HARD_FAILURE: 1/1
RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS
```

Accepted prospective guardrail profile:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

Key boundary:

```text
HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

## Protocol v0.2 / 프로토콜 v0.2

`SPEC-CH-006` authorized prospective v0.2 use for new runs. Protocol v0.2 adds source-purpose / target-user / priority lock, declared transformation viewpoint, a separate guardrail ledger, optional `PRECEDENCE_OR_PRIORITY`, and separate hard-failure/guardrail verdicts. It does not rescore v0.1 evidence.

## External applications / 외부·독립 생성 corpus 적용

### SPEC-APP-001 — RFC 9112 §6.3 Message Body Length

Protocol: **v0.1**

```text
CASE_ORIGIN: public_normative_standard
PRECOMMIT_COMMIT: 9b91cecda9516fd7cd65c9eb181e80ab4fa45deb
SOURCE_UNIT_COVERAGE: 13/13
PRECEDENCE_PRESERVATION: 13/13
BCP14_MUST_OBLIGATIONS_PRESERVED: 8/8
INVENTED_SOURCE_FACTS: 0
SOURCE_FIDELITY_RESULT: pass
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

Purpose/detail/viewpoint guardrails were not separately precommitted in this v0.1 run and therefore remain formally untested for that record.

### SPEC-APP-002 — Belmont Report Part C. Applications

Protocol: **v0.2**  
Precommit: [`../../real_world_cases/specification/SPEC-APP-002_Belmont-Part-C_precommit.md`](../../real_world_cases/specification/SPEC-APP-002_Belmont-Part-C_precommit.md)  
Result: [`../../real_world_cases/specification/SPEC-APP-002_Belmont-Part-C.md`](../../real_world_cases/specification/SPEC-APP-002_Belmont-Part-C.md)

```text
CASE_ORIGIN: public_normative_ethics_guideline
EXTERNAL_DOMAIN: human-subject research ethics
PRECOMMIT_COMMIT: 2ad9b5820a959195b32e1d9560be6328a4905771
SOURCE_UNIT_COVERAGE: 22/22
LOCAL_PRIORITY_PRESERVATION: 5/5
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED: 4/4
INVENTED_SOURCE_FACTS: 0
NORMATIVE_FORCE_STRENGTHENINGS: 0
DSD_VIEWPOINT_OVERATTRIBUTIONS: 0
HARD_FAILURE_COUNT: 0
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
RESULT: SPECIFICATION_EXTERNAL_GUARDRAIL_APPLICATION_PASS_WITH_MIXED_GAIN
```

The DSD derivative adds source-unit traceability, actor/condition separation, and downstream coverage/checkability. The Belmont original remains preferred for primary ethical reading and contextual reasoning. The DSD derivative is therefore an additional checking layer, not a replacement.

A nonfatal v0.2 pressure point was discovered:

```text
intentional normative openness
!= accidental specification underspecification
```

The source deliberately leaves some ethical boundaries open to judgment. v0.2 preserves them without false deterministic resolution, but does not yet provide a dedicated status distinct from ordinary underspecification.

### Baseline-status note

`SPEC-APP-002` precommitted the OHRP Assurance Training summary as a secondary concise baseline. Before scoring, the HHS page itself was found to mark that tutorial as outdated and archived. It was therefore retained only as a historical comparator, not silently treated as a current regulatory-compliance baseline. No replacement baseline was inserted after reveal.

## Maturity meta-audit / 성숙도 메타감사

The first maturity audit remains a DSD Audit meta-record, not a seventh direct Specification pilot.

```text
AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

That audit predates `SPEC-APP-002`; its verdict is preserved. A new status decision requires a separate re-audit.

## Current evidence state / 현재 증거 상태

```text
V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 6
EXTERNAL_APPLICATIONS_TOTAL: 2
EXTERNAL_DOMAINS_TOTAL: 2
V0_2_EXTERNAL_APPLICATIONS: 1
V0_2_EXTERNAL_APPLICATION_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
INDEPENDENT_EVALUATOR_VALIDATION: not_established
CURRENT_METHOD_STATUS: developing
CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2
ESTABLISHED_STATUS_AFTER_SPEC_APP_002: not_reaudited
NEXT_EVIDENCE: independent_retrace_or_open-texture_boundary_challenge
```

Do not promote Specification automatically from the second external case. The strongest next evidence is either an independent blinded retrace of `SPEC-APP-002`, or a dedicated prospective challenge separating intentional normative openness from accidental `SPEC_UNDERSPECIFIED`.
