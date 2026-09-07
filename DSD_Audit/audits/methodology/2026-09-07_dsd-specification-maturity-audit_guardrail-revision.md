# DSD Specification Maturity Audit — Guardrail Revision Note / 명세론 성숙도 감사 가드레일 개정 기록

Status: **REVISION NOTE — original verdict preserved**  
Date: 2026-09-07  
Original audit: `DSD-AUDIT-20260907-METHODOLOGY-001`  
Original result file: [`2026-09-07_dsd-specification-maturity-audit.md`](2026-09-07_dsd-specification-maturity-audit.md)

## 1. Reason for revision note

After the first maturity audit was completed, a further method-specific blind spot was identified in discussion and tested separately:

```text
semantic/source fidelity
!= purpose fidelity

more explicit detail
!= automatically better specification

DSD-derived viewpoint
!= source author's original intended viewpoint
```

The original v0.1 protocol had strong source/status/bridge/failure discipline, but did not separately precommit a purpose/detail/viewpoint guardrail ledger.

## 2. What this revision does not do

This note does **not**:

- alter the original precommit;
- rescore `SPEC-CH-001~005`;
- rescore `SPEC-APP-001`;
- change `SPEC-APP-001` source-fidelity PASS;
- convert untested purpose/detail/viewpoint axes into PASS or FAIL;
- change the original maturity verdict.

The original verdict remains:

```text
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
```

## 3. New method-specific evidence

`SPEC-CH-006 — Guardrail Centerline Challenge` was separately precommitted and completed after the original maturity audit.

```text
PRECOMMIT_COMMIT: fe009d8da9ab992e6885d07e14ff26355b776a86
EXACT_GUARDRAIL_FAMILY_MATCHES: 8/8
FALSE_HARD_FAILURE_ON_PRESSURE_CASES: 0
FALSE_REJECTION_OF_DECLARED_DERIVATIVE_VIEW: 0
RESULT: SPECIFICATION_GUARDRAIL_CENTERLINE_PILOT_PASS_WITH_LIMITATIONS
```

Accepted prospective guardrails:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

## 4. Protocol transition

A prospective `Specification Protocol v0.2` was created for new runs.

v0.2 separates hard failure from centerline drift:

```text
HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

It also permits explicitly declared derivative viewpoints and preserves `UNDETERMINED` when source purpose or audience is not supported.

Historical v0.1 remains the governing protocol for its original evidence.

## 5. Effect on maturity interpretation

The new guardrail finding does not undermine the original decision to retain `developing`.

Instead, it adds another reason that `established` status would have been premature: v0.2 has no external application evidence yet.

```text
ORIGINAL_AUDIT_VERDICT_CHANGED: no
CURRENT_METHOD_STATUS: developing
CURRENT_PROTOCOL_FOR_NEW_RUNS: v0.2
V0_2_EXTERNAL_APPLICATION_EVIDENCE: not_established
NEXT_DIRECT_APPLICATION: SPEC-APP-002_less_structured_external_corpus_under_v0.2
```

## 6. Next audit requirement

The next maturity audit must be a new revision/re-audit and should include, prospectively:

- external v0.2 evidence;
- purpose fidelity;
- priority preservation;
- detail proportionality / representation burden;
- viewpoint separation;
- independent retrace/review if available;
- strongest reasonable baseline;
- preservation of negative and `NO_GAIN` results.
