# DSD Specification Method-Specific Evidence / DSD 명세론 개별 방법 직접 증거

Status: **six direct constructed pilots + first external application + first maturity audit completed / v0.2 current for new runs / developing retained**  
Date: 2026-09-07  
Method: **DSD Specification / DSD 명세론**

Protocol versions:
- v0.1 historical: [`../../../methods/03_specification/PROTOCOL.md`](../../../methods/03_specification/PROTOCOL.md)
- v0.2 current for new runs: [`../../../methods/03_specification/PROTOCOL_v0.2.md`](../../../methods/03_specification/PROTOCOL_v0.2.md)

Shared-core pilots SC-01 through SC-10 may be reused as operating disciplines, but they do not count as direct Specification validation.

## Direct evidence registry / 직접 증거 레지스트리

### SPEC-CH-001 through SPEC-CH-005 — v0.1 evidence

The five initial direct pilots remain under the v0.1 protocol family and preserve their original verdicts:

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

The accepted prospective guardrail profile is:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

and the key boundary is:

```text
HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

This means extra detail or a changed analytic viewpoint is not automatically discarded. The representation crosses the guardrail when the change is undeclared, the source purpose or priority is functionally displaced, DSD-added structure is attributed to the source, or source facts/intent are invented.

## Protocol v0.2 / 프로토콜 v0.2

`SPEC-CH-006` authorizes prospective v0.2 use for new runs.

Protocol v0.2 adds:

- source-purpose / target-user / priority lock;
- explicit DSD transformation-purpose and viewpoint-change declaration;
- separate guardrail ledger;
- optional `PRECEDENCE_OR_PRIORITY` for genuinely ordered sources;
- separate hard-failure and guardrail verdicts.

It does not rescore v0.1 evidence.

## External application / 외부·독립 생성 corpus 적용

### SPEC-APP-001 — RFC 9112 §6.3 Message Body Length

Protocol: **v0.1**

```text
CASE_ORIGIN: public_normative_standard
PRECOMMIT_COMMIT: 9b91cecda9516fd7cd65c9eb181e80ab4fa45deb
SOURCE_UNIT_COVERAGE: 13/13
TRIGGER_OR_ACTOR_SCOPE_PRESERVATION: 13/13
PRECEDENCE_PRESERVATION: 13/13
BCP14_MUST_OBLIGATIONS_PRESERVED: 8/8
INVENTED_SOURCE_FACTS: 0
SOURCE_FIDELITY_RESULT: pass
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
```

The first external corpus did not produce a forced DSD advantage. The baseline was already a compact ordered normative specification.

The following v0.2 guardrail axes were **not separately precommitted in SPEC-APP-001** and therefore remain untested as formal axes for that record:

```text
PURPOSE_FIDELITY_GUARDRAIL: untested_as_formal_axis
DETAIL_PROPORTIONALITY_GUARDRAIL: untested_as_formal_axis
VIEWPOINT_SEPARATION_GUARDRAIL: untested_as_formal_axis
```

## Maturity meta-audit / 성숙도 메타감사

The first maturity audit remains a DSD Audit meta-record, not a seventh direct Specification pilot.

```text
AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

A post-audit revision note records the newly recognized purpose/detail/viewpoint guardrail gap in v0.1. The original verdict is not erased or rescored.

## Current evidence state / 현재 증거 상태

```text
V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 6
EXTERNAL_APPLICATIONS: 1
V0_2_EXTERNAL_APPLICATIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not_established
ESTABLISHED_EVIDENCE_BREADTH: insufficient
CURRENT_METHOD_STATUS: developing
CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2
NEXT_DIRECT_APPLICATION: SPEC-APP-002_less_structured_external_corpus_under_v0.2
```

`SPEC-APP-002` should be precommitted under v0.2 with source purpose, target user/action, priority, DSD transformation purpose, guardrail criteria, and strongest reasonable baseline locked before atomization.
