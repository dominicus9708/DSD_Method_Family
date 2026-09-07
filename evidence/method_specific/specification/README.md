# DSD Specification Method-Specific Evidence / DSD 명세론 개별 방법 직접 증거

Status: **seven direct constructed pilots + three external applications + one method-family linkage pilot + internal Protocol v1.0 standardization completed / method evidence maturity remains developing**  
Date: 2026-09-08  
Method: **DSD Specification / DSD 명세론**

Protocol versions:
- v0.1 historical: [`../../../methods/03_specification/PROTOCOL.md`](../../../methods/03_specification/PROTOCOL.md)
- v0.2 historical: [`../../../methods/03_specification/PROTOCOL_v0.2.md`](../../../methods/03_specification/PROTOCOL_v0.2.md)
- v0.2.1 historical/evidence basis: [`../../../methods/03_specification/PROTOCOL_v0.2.1.md`](../../../methods/03_specification/PROTOCOL_v0.2.1.md)
- v1.0 standard/default for new DSD-internal runs: [`../../../methods/03_specification/PROTOCOL_v1.0.md`](../../../methods/03_specification/PROTOCOL_v1.0.md)

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

The key result remains:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

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

The Belmont case exposed the openness/underspecification pressure subsequently isolated by `SPEC-CH-007`. It remains a v0.2 record and is not rescored under later protocols.

### SPEC-APP-003 — OSHA Emergency Action Plan core corpus

Protocol: **v0.2.1**  
Precommit: [`../../real_world_cases/specification/SPEC-APP-003_OSHA_EAP_core_guidance_precommit.md`](../../real_world_cases/specification/SPEC-APP-003_OSHA_EAP_core_guidance_precommit.md)  
Result: [`../../real_world_cases/specification/SPEC-APP-003_OSHA_EAP_core_guidance.md`](../../real_world_cases/specification/SPEC-APP-003_OSHA_EAP_core_guidance.md)

```text
CASE_ORIGIN: public_regulatory_standard_plus_official_guidance
EXTERNAL_DOMAIN: workplace emergency planning / occupational safety
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

The unfavorable comparison is preserved: DSD Specification did not beat the strong OSHA regulation/eTool/checklist baseline for that locked standalone task.

## Method-family linkage evidence / 방법군 연계 증거

`SPEC-LINK-001` is a linkage pilot, not an eighth direct Specification challenge and not direct Audit validation.

Result: [`SPEC-LINK-001_specification-to-audit-handoff.md`](SPEC-LINK-001_specification-to-audit-handoff.md)

```text
RECEIVING_METHOD: DSD Audit
AUDIT_FINDING_MATCHES: 6/6
REQUIREMENT_IDENTITY_PRESERVATION: pass
NORMATIVE_FORCE_PRESERVATION: pass
OPENNESS_PRESERVATION: pass
HIDDEN_RETRANSLATION_REQUIRED: no
EXTERNAL_STANDARD_BOUNDARY_PRESERVED: yes
RESULT: SPECIFICATION_TO_AUDIT_NATIVE_HANDOFF_PILOT_PASS_WITH_LIMITATIONS
```

This supports method-family handoff utility separately from standalone domain-task gain.

## Protocol stability and standardization audits / 프로토콜 안정성·표준화 감사

These are DSD Audit methodology records and are not counted as additional direct Specification pilots.

### v0.2.1 minimality/stability audit

```text
AUDIT_ID: DSD-AUDIT-20260908-METHODOLOGY-003
PROTOCOL_FREEZE_READINESS: FREEZE_READY_WITH_NONBREAKING_CLEANUP
STRUCTURAL_CONFLICT_COUNT: 0
BREAKING_SEMANTIC_REVISION_REQUIRED: no
STRUCTURAL_REDESIGN_REQUIRED: no
```

### v1.0 final standardization audit

```text
AUDIT_ID: DSD-AUDIT-20260908-METHODOLOGY-004
CRITICAL_GATES_PASSED: 14/14
CRITICAL_FAILURES: 0
BREAKING_SEMANTIC_LOSS: 0
REGRESSION_FAMILIES_WITH_REQUIRED_CARRIER_LOSS: 0/11
NEW_UNPRECOMMITTED_SEMANTIC_OBLIGATION: 0
STANDARDIZATION_VERDICT: STANDARDIZE_WITH_DOCUMENTED_LIMITS
DEFAULT_DSD_INTERNAL_PROTOCOL: DSD Specification Protocol v1.0
METHOD_EVIDENCE_STATUS: developing
METHOD_MATURITY_PROMOTION: no
```

Protocol standardization and evidence maturity remain separate axes.

## Maturity meta-audit / 성숙도 메타감사

The first maturity audit remains historical rather than being silently replaced:

```text
AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

Later work establishes internal v1.0 interface stability but does not itself establish independent evaluator agreement or measured practical benefit.

## Current evidence state / 현재 증거 상태

```text
V0_1_DIRECT_PILOTS: 5
V0_2_GUARDRAIL_TRANSITION_PILOT: 1
V0_2_1_OPENNESS_TRANSITION_PILOT: 1
TOTAL_DIRECT_CONSTRUCTED_PILOTS: 7

EXTERNAL_APPLICATIONS_TOTAL: 3
EXTERNAL_DOMAINS_TOTAL: 3
METHOD_FAMILY_LINKAGE_PILOTS: 1

CURRENT_PROTOCOL_FOR_NEW_RUNS: v1.0
INTERNAL_PROTOCOL_STATUS: standardized
LATEST_EXTERNAL_RESULT: SPEC_NO_GAIN_WITH_GUARDRAIL_PRESSURE
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established
ALL_METHOD_HANDOFF_INTEROPERABILITY: not_established
CURRENT_METHOD_EVIDENCE_STATUS: developing
```

Further evidence should prioritize genuinely independent retrace, measured practical benefit where feasible, or a second receiving-method linkage only when it resolves a concrete interoperability question. Additional same-project corpora should not be treated as independent evaluator replication.
