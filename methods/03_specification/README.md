# 03. DSD Specification / DSD 명세론

Status: **internally standardized at Protocol v1.0 / method evidence maturity remains developing** — v0.1/v0.2/v0.2.1 records remain historical evidence under their original protocols. `DSD-AUDIT-20260908-METHODOLOGY-004` passed all 14 critical standardization gates and approved v1.0 as the default DSD-internal Specification protocol for new runs. This is an interface-standardization judgment, not independent external validation or superiority over existing specification methods.

Task: state explicitly what entities, statuses, inputs, prerequisites, outputs, transitions, and distinctions a system or study must preserve **without silently replacing the source's original purpose, priority, audience function, viewpoint, intentionally open judgment boundary, or site-specific implementation freedom with DSD-imposed structure**.

Primary DSD sources: Formation + General Property; Static Aggregation and Dynamics when output, reduction, or transition specifications matter.

Typical outputs include typed requirement/status records, explicit bridges, external-standard boundaries, violation/unresolved conditions, guardrail records, and—when relevant—separate source-openness and downstream-determinacy records.

Boundary: DSD Specification organizes structural requirements; it does not replace domain-specific requirements engineering, standards, law, safety rules, clinical standards, scientific definitions, professional judgment, or other competent validation authorities.

## Protocol versions / 프로토콜 버전

- [`PROTOCOL.md`](PROTOCOL.md) — **v0.1 historical**, used for `SPEC-CH-001~005`, `SPEC-APP-001`, and first maturity-audit-era records.
- [`PROTOCOL_v0.2.md`](PROTOCOL_v0.2.md) — **v0.2 historical**, used for `SPEC-CH-006` and `SPEC-APP-002`.
- [`PROTOCOL_v0.2.1.md`](PROTOCOL_v0.2.1.md) — **v0.2.1 historical/evidence basis**, used for `SPEC-CH-007`, `SPEC-APP-003`, and `SPEC-LINK-001`.
- [`PROTOCOL_v1.0.md`](PROTOCOL_v1.0.md) — **standard / default DSD-internal protocol for new Specification runs** after final standardization audit.

v1.0 preserves the stable v0.2.1 semantics while applying only the audited non-breaking cleanup package:

```text
C1 explicit conditionality for context-dependent fields
C2 atom-level VALIDATION_STANDARD inheritance
C3 minimal-core / extended-ledger output separation
C4 NO_GAIN_STATUS as a derived compatibility view
C5 G1-G4 and openness/determinacy preserved without expansion
C6 v0.x protocol/evidence history preserved
```

## Stable v1.0 semantic core / 안정화된 v1.0 핵심

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION

SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS

HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

Conditional fields and ledgers are activated only when material to the declared task. Static Aggregation, Dynamics, and optional specializations are not forced into inactive cases.

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

## Method-family linkage / 방법군 연계

`SPEC-LINK-001` tested the first direct DSD-native receiving-method boundary:

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

This supports:

```text
STANDALONE_NO_GAIN
!= METHOD_FAMILY_INTEGRATION_NO_GAIN
```

A competent external specification can remain the preferred domain-facing representation while DSD Specification still serves as a native typed criterion carrier for another DSD method.

## Minimality / stability audit / 최소성·안정성 감사

[`../../DSD_Audit/audits/methodology/2026-09-08_dsd-specification-v0.2.1-minimality-stability-audit.md`](../../DSD_Audit/audits/methodology/2026-09-08_dsd-specification-v0.2.1-minimality-stability-audit.md)

```text
AUDIT_ID: DSD-AUDIT-20260908-METHODOLOGY-003
PROTOCOL_FREEZE_READINESS: FREEZE_READY_WITH_NONBREAKING_CLEANUP
STRUCTURAL_CONFLICT_COUNT: 0
BREAKING_SEMANTIC_REVISION_REQUIRED: no
STRUCTURAL_REDESIGN_REQUIRED: no
```

## Final v1.0 standardization audit / 최종 표준화 감사

Precommit: [`../../DSD_Audit/audits/methodology/2026-09-08_dsd-specification-v1.0-standardization-audit_precommit.md`](../../DSD_Audit/audits/methodology/2026-09-08_dsd-specification-v1.0-standardization-audit_precommit.md)  
Result: [`../../DSD_Audit/audits/methodology/2026-09-08_dsd-specification-v1.0-standardization-audit.md`](../../DSD_Audit/audits/methodology/2026-09-08_dsd-specification-v1.0-standardization-audit.md)

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

The documented limits concern independent validation, measured practical benefit, and cross-method breadth; they do not require v1.0 semantic redesign.

## Maturity audit / 성숙도 감사

The first maturity audit remains historical:
[`../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md`](../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md)

```text
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

Later evidence supports internal v1.0 standardization but has not been used to silently convert method evidence maturity to `established`.

## Evidence state / 증거 상태

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
METHOD_EVIDENCE_STATUS: developing
```

## Next evidence priority / 다음 증거 우선순위

v1.0 is now the internal default. Further protocol revision should require a concrete defect or new stable obligation rather than routine expansion.

The strongest remaining evidence priorities are independent evaluator retrace, measured practical benefit where feasible, and additional receiving-method linkage only when it answers a real interoperability question. These are maturity/evidence tasks, not prerequisites for using v1.0 as the DSD-internal standard.
