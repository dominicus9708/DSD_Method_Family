# 03. DSD Specification / DSD 명세론

Status: **developing** — Protocol v0.1 historical evidence preserved; prospective Protocol v0.2 established for new runs after `SPEC-CH-006`; first external application and maturity audit completed; `developing` retained.

Task: state explicitly what entities, statuses, inputs, prerequisites, outputs, transitions, and distinctions a system or study must preserve **without silently replacing the source's original purpose, priority, audience function, or viewpoint with the DSD representation itself**.

Primary DSD sources: Formation + General Property; Static Aggregation and Dynamics when output, reduction, or transition specifications matter.

Typical outputs:
- typed requirement/status tables;
- allowed and disallowed state distinctions;
- explicit bridge declarations;
- domain and undefinedness rules;
- aggregate/reconstruction obligations when reduction is specified;
- transition and lineage obligations;
- external-standard requirements for domain-level claims;
- explicit violation, unresolved, contradiction, and `NO_GAIN` conditions;
- a separate purpose/detail/viewpoint **guardrail ledger** under v0.2.

Boundary: DSD Specification organizes structural requirements; it does not replace domain-specific requirements engineering, standards, law, safety rules, clinical standards, scientific definitions, or other competent validation authorities. A DSD-derived viewpoint may be useful, but it is not attributed to the source author unless the source supports that attribution.

## Protocol versions / 프로토콜 버전

- [`PROTOCOL.md`](PROTOCOL.md) — **DSD Specification Protocol v0.1**, retained as the historical protocol for `SPEC-CH-001~005`, `SPEC-APP-001`, and the first maturity audit.
- [`PROTOCOL_v0.2.md`](PROTOCOL_v0.2.md) — **prospective current protocol for new runs**.

Protocol v0.2 adds, prospectively:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

and separates:

```text
HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

It also adds an optional `PRECEDENCE_OR_PRIORITY` field for sources whose semantics actually depend on ordering or priority. This field is not retroactively inserted into v0.1 records.

## Direct method evidence / 개별 방법 직접 증거

Evidence lane: [`../../evidence/method_specific/specification/`](../../evidence/method_specific/specification/)

```text
SPEC-CH-001  well-formed / malformed discrimination
SPEC-CH-002  contradiction / underspecification
SPEC-CH-003  optional-layer / bridge boundary
SPEC-CH-004  NO_GAIN specification
SPEC-CH-005  reproducibility / independent retrace
```

These five records remain v0.1-era direct pilot evidence.

### SPEC-CH-006 — Guardrail Centerline Challenge

```text
PRECOMMIT: fe009d8da9ab992e6885d07e14ff26355b776a86
EXACT_GUARDRAIL_FAMILY_MATCHES: 8/8
FALSE_HARD_FAILURE_ON_PRESSURE_CASES: 0
FALSE_REJECTION_OF_DECLARED_DERIVATIVE_VIEW: 0
UNKNOWN_PURPOSE_PRESERVED_AS_UNDETERMINED: 1/1
SOURCE_FACT_INVENTION_ESCALATED_TO_HARD_FAILURE: 1/1
RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS
```

This sixth challenge directly tests the new guardrail distinction. It does **not** establish external usefulness of v0.2 because it is still a constructed same-project challenge.

## First external application / 첫 외부 적용

External evidence lane:
[`../../evidence/real_world_cases/specification/`](../../evidence/real_world_cases/specification/)

### SPEC-APP-001 — RFC 9112 §6.3 Message Body Length

```text
PROTOCOL: v0.1
CASE_ORIGIN: public_normative_standard
SOURCE_UNIT_COVERAGE: 13/13
PRECEDENCE_PRESERVATION: 13/13
BCP14_MUST_OBLIGATIONS_PRESERVED: 8/8
INVENTED_SOURCE_FACTS: 0
SOURCE_FIDELITY_RESULT: pass
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
PROTOCOL_PRESSURE: ordered precedence / priority, present_nonfatal
```

The v0.1 application remains valid at its original resolution. However, **purpose fidelity, detail proportionality, and viewpoint separation were not separately precommitted guardrail axes in that run**, so they must not be retroactively marked as passed.

```text
SPEC_APP_001_SOURCE_FIDELITY: pass
SPEC_APP_001_PURPOSE_FIDELITY_GUARDRAIL: untested_as_formal_axis
SPEC_APP_001_DETAIL_PROPORTIONALITY_GUARDRAIL: untested_as_formal_axis
SPEC_APP_001_VIEWPOINT_SEPARATION_GUARDRAIL: untested_as_formal_axis
```

## Maturity audit / 성숙도 감사

Audit record:
[`../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md`](../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md)

```text
AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

A post-audit revision note now records that v0.1 lacked explicit purpose/detail/viewpoint guardrails. This does not invalidate the original audit verdict; it strengthens the reason not to promote prematurely and requires the next external application to use v0.2 prospectively.

## Evidence state / 증거 상태

```text
SPEC-CH-001~005  completed under v0.1
SPEC-CH-006      completed; prospective guardrail model accepted
SPEC-APP-001     completed under v0.1
SPECIFICATION_MATURITY_AUDIT completed; retain developing

CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2
V0_2_EXTERNAL_APPLICATION_EVIDENCE: not_yet_established
INDEPENDENT_EVALUATOR_VALIDATION: not_established
METHOD_STATUS: developing
ESTABLISHED_STATUS: not_justified_on_current_evidence
NEXT_STEP: SPEC-APP-002_less_structured_external_corpus_under_v0.2
```

`SPEC-APP-002` should lock the source's purpose, target user/action, priority hierarchy, DSD transformation purpose, and strongest reasonable baseline before atomization, then score hard failure and guardrail status separately.
