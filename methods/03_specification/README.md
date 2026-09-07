# 03. DSD Specification / DSD 명세론

Status: **developing** — Protocol v0.1 historical evidence preserved; Protocol v0.2 is current for new runs; `SPEC-CH-006` and first external v0.2 application `SPEC-APP-002` completed; first maturity audit still retains `developing`.

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
- [`PROTOCOL_v0.2.md`](PROTOCOL_v0.2.md) — **current prospective protocol for new runs**.

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

This sixth challenge directly tests the new guardrail distinction. It does **not** establish broad external usefulness of v0.2 because it is a constructed same-project challenge.

## External applications / 외부 적용

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

The v0.1 application remains valid at its original resolution. Purpose fidelity, detail proportionality, and viewpoint separation were not separately precommitted guardrail axes and must not be retroactively marked as passed.

### SPEC-APP-002 — Belmont Report Part C. Applications

```text
PROTOCOL: v0.2
CASE_ORIGIN: public_normative_ethics_guideline
EXTERNAL_DOMAIN: human-subject research ethics
PRECOMMIT: 2ad9b5820a959195b32e1d9560be6328a4905771
SOURCE_UNIT_COVERAGE: 22/22
LOCAL_PRIORITY_PRESERVATION: 5/5
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED: 4/4
INVENTED_SOURCE_FACTS: 0
NORMATIVE_FORCE_STRENGTHENINGS: 0
DSD_VIEWPOINT_OVERATTRIBUTIONS: 0
FINAL_SPEC_STATUS: usable
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
```

The Belmont application is deliberately treated as a derivative structural checking layer rather than a replacement for the Report's ethical reasoning. DSD added source-unit traceability and downstream coverage/checkability, while the original Belmont prose remains preferred for the primary ethical-reading and contextual-reasoning task.

The application also exposed a new nonfatal v0.2 pressure point:

```text
intentional normative openness
!= accidental specification underspecification
```

The current protocol can preserve that distinction in `UNRESOLVED_CONDITION` and limits, but does not yet give source-intentional open texture its own dedicated status. No retroactive field was added during the run.

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

The original maturity verdict is not overwritten by later evidence. Since that audit, v0.2 gained one external application in a second domain and one mixed positive operational result, but independent evaluator validation and measured practical benefit remain absent. A new status decision requires a new re-audit rather than silent promotion.

## Evidence state / 증거 상태

```text
SPEC-CH-001~005  completed under v0.1
SPEC-CH-006      completed; prospective guardrail model accepted
SPEC-APP-001     completed under v0.1
SPEC-APP-002     completed under v0.2
SPECIFICATION_MATURITY_AUDIT completed; retain developing

CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2
EXTERNAL_APPLICATIONS_TOTAL: 2
EXTERNAL_DOMAINS_TOTAL: 2
V0_2_EXTERNAL_APPLICATIONS: 1
V0_2_EXTERNAL_APPLICATION_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
INDEPENDENT_EVALUATOR_VALIDATION: not_established
METHOD_STATUS: developing
ESTABLISHED_STATUS: not_reaudited_after_SPEC_APP_002
NEXT_STEP: independent_retrace_or_open-texture_boundary_challenge
```

The strongest next evidence is either a genuinely independent retrace of `SPEC-APP-002`, or a prospective challenge that distinguishes source-intentional normative openness from accidental `SPEC_UNDERSPECIFIED` without weakening the latter detector.
