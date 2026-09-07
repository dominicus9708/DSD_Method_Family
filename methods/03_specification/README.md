# 03. DSD Specification / DSD 명세론

Status: **developing / internally freeze-ready for v1.0 candidate with non-breaking cleanup** — Protocol v0.1/v0.2 evidence is preserved; Protocol v0.2.1 remains current for new runs until a v1.0 candidate is constructed and finally audited. `SPEC-LINK-001` and the v0.2.1 minimality/stability audit are now complete. Method maturity remains `developing`; protocol freeze readiness is not external validation.

Task: state explicitly what entities, statuses, inputs, prerequisites, outputs, transitions, and distinctions a system or study must preserve **without silently replacing the source's original purpose, priority, audience function, viewpoint, intentionally open judgment boundary, or site-specific implementation freedom with DSD-imposed structure**.

Primary DSD sources: Formation + General Property; Static Aggregation and Dynamics when output, reduction, or transition specifications matter.

Typical outputs include typed requirement/status tables, explicit bridges, external-standard boundaries, violation/unresolved conditions, guardrail records, and—when relevant—separate source-openness and downstream-determinacy records.

Boundary: DSD Specification organizes structural requirements; it does not replace domain-specific requirements engineering, standards, law, safety rules, clinical standards, scientific definitions, professional judgment, or other competent validation authorities.

## Protocol versions / 프로토콜 버전

- [`PROTOCOL.md`](PROTOCOL.md) — **v0.1**, historical protocol for `SPEC-CH-001~005`, `SPEC-APP-001`, and the first maturity audit.
- [`PROTOCOL_v0.2.md`](PROTOCOL_v0.2.md) — **v0.2**, protocol governing `SPEC-CH-006` transition evidence and `SPEC-APP-002`.
- [`PROTOCOL_v0.2.1.md`](PROTOCOL_v0.2.1.md) — **current protocol for new runs**, established after `SPEC-CH-007`, used for `SPEC-APP-003` and `SPEC-LINK-001`, and now judged freeze-ready as the semantic basis of a future v1.0 candidate.

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

## Method-family linkage / 방법군 연계

`SPEC-LINK-001` tests the first direct DSD-native receiving-method boundary:

```text
external OSHA source
-> DSD Specification v0.2.1
-> DSD Audit
```

Result:

```text
AUDIT_FINDING_MATCHES: 6/6
REQUIREMENT_IDENTITY_PRESERVATION: pass
NORMATIVE_FORCE_PRESERVATION: pass
OPENNESS_PRESERVATION: pass
HIDDEN_RETRANSLATION_REQUIRED: no
EXTERNAL_STANDARD_BOUNDARY_PRESERVED: yes
RESULT: SPECIFICATION_TO_AUDIT_NATIVE_HANDOFF_PILOT_PASS_WITH_LIMITATIONS
```

This supports the distinction:

```text
STANDALONE_NO_GAIN
!= METHOD_FAMILY_INTEGRATION_NO_GAIN
```

A competent external specification can remain the preferred domain-facing representation while DSD Specification still serves as a native typed criterion carrier for another DSD method.

## Minimality / stability audit and v1.0 preparation

Audit record:
[`../../DSD_Audit/audits/methodology/2026-09-08_dsd-specification-v0.2.1-minimality-stability-audit.md`](../../DSD_Audit/audits/methodology/2026-09-08_dsd-specification-v0.2.1-minimality-stability-audit.md)

```text
AUDIT_ID: DSD-AUDIT-20260908-METHODOLOGY-003
PROTOCOL_FREEZE_READINESS: FREEZE_READY_WITH_NONBREAKING_CLEANUP
STRUCTURAL_CONFLICT_COUNT: 0
BREAKING_SEMANTIC_REVISION_REQUIRED: no
STRUCTURAL_REDESIGN_REQUIRED: no
METHOD_STATUS_CHANGED: no
```

The locked v1.0 cleanup package is limited to:

```text
C1 mark context-dependent fields explicitly conditional
C2 allow atom-level VALIDATION_STANDARD inheritance from a locked higher-level standard
C3 split minimal core output from extended diagnostic ledgers
C4 treat NO_GAIN_STATUS as derived when FINAL_SPEC_STATUS already equals no_gain
C5 preserve G1-G4 and openness/determinacy without adding a new conceptual layer
C6 preserve all v0.x protocols and evidence as historical versions
```

Protocol freeze readiness is an **internal standardization judgment**, not proof of independent evaluator agreement, practical superiority, or method maturity.

## Maturity audit / 성숙도 감사

First audit record: [`../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md`](../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md)

```text
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

That first maturity audit predates `SPEC-APP-002`, `SPEC-CH-007`, `SPEC-APP-003`, `SPEC-LINK-001`, and the minimality/stability audit. Its historical verdict is preserved; no automatic `established` promotion is inferred from v1.0 freeze readiness.

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
METHOD_FAMILY_LINKAGE_PILOTS: 1

CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2.1
PROTOCOL_FREEZE_READINESS: FREEZE_READY_WITH_NONBREAKING_CLEANUP
LATEST_EXTERNAL_RESULT: SPEC_NO_GAIN_WITH_GUARDRAIL_PRESSURE
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established
METHOD_STATUS: developing
```

## Next stage / 다음 단계

Construct **DSD Specification Protocol v1.0 candidate** from v0.2.1 using only cleanup package `C1-C6`, then run a final standardization audit. If that audit passes, v1.0 may become the default **DSD-internal** Specification protocol while evidence maturity remains separately recorded.
