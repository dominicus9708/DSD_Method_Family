# DSD Audit Records / DSD 감사 기록

This directory is the authoritative location for **new DSD Audit case records** created after the audit module was separated from DSD Analysis on 2026-09-05.

이 디렉터리는 2026-09-05 이후 DSD 분석론과 분리된 **새 DSD 감사 실행 기록의 기준 위치**입니다.

## Recommended layout / 권장 구조

```text
audits/
├─ methodology/
├─ mathematics/
├─ science/
├─ law/
├─ software/
├─ ai/
├─ history_media/
├─ administration_organization/
└─ README.md
```

Create a domain directory when the first real audit exists. `methodology/` is used for audits whose object is a DSD method, protocol, evidence architecture, or maturity/status decision rather than an external subject-matter case.

## Current methodology audits / 현재 방법론 감사

### DSD Specification maturity audit — 2026-09-07

- Precommit: [`methodology/2026-09-07_dsd-specification-maturity-audit_precommit.md`](methodology/2026-09-07_dsd-specification-maturity-audit_precommit.md)
- Result: [`methodology/2026-09-07_dsd-specification-maturity-audit.md`](methodology/2026-09-07_dsd-specification-maturity-audit.md)

```text
AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
PRINCIPAL_BLOCKER: insufficient external/cross-domain evidence breadth
```

The audit does not treat the first external `SPEC_NO_GAIN` / baseline-preferred result as a failure. It preserves that result and separately finds that one external corpus in one domain is insufficient evidence breadth for `established` status.

### Specification -> Audit native handoff audit — 2026-09-07

- Result: [`methodology/2026-09-07_specification-to-audit-handoff.md`](methodology/2026-09-07_specification-to-audit-handoff.md)

```text
AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-002
AUDIT_FINDING_MATCHES: 6/6
REQUIREMENT_IDENTITY_PRESERVATION: pass
NORMATIVE_FORCE_PRESERVATION: pass
OPENNESS_PRESERVATION: pass
HIDDEN_RETRANSLATION_REQUIRED: no
```

This record tests one method-family boundary only. It does not count as a new direct Audit validation case or as proof of universal inter-method interoperability.

### DSD Specification v0.2.1 minimality / stability audit — 2026-09-08

- Precommit: [`methodology/2026-09-08_dsd-specification-v0.2.1-minimality-stability-audit_precommit.md`](methodology/2026-09-08_dsd-specification-v0.2.1-minimality-stability-audit_precommit.md)
- Result: [`methodology/2026-09-08_dsd-specification-v0.2.1-minimality-stability-audit.md`](methodology/2026-09-08_dsd-specification-v0.2.1-minimality-stability-audit.md)

```text
AUDIT_ID: DSD-AUDIT-20260908-METHODOLOGY-003
PROTOCOL_FREEZE_READINESS: FREEZE_READY_WITH_NONBREAKING_CLEANUP
STRUCTURAL_CONFLICT_COUNT: 0
BREAKING_SEMANTIC_REVISION_REQUIRED: no
STRUCTURAL_REDESIGN_REQUIRED: no
CURRENT_METHOD_STATUS: developing
```

The audit separates **protocol freeze readiness** from **method evidence maturity**. v0.2.1 is judged stable enough to serve as the semantic basis of a v1.0 candidate, but independent evaluator validation and measured practical benefit remain unestablished.

## Starting a new audit / 새 감사 시작

1. Copy `../templates/AUDIT_CASE_TEMPLATE.md`.
2. Place the copy under the appropriate domain directory.
3. Lock audit question, scope, time, descriptive resolution, and external standard.
4. Lock the shared DSD interface profile and exact source revisions when DSD formal layers matter.
5. Preserve original sources before reinterpretation.
6. Keep audit evidence status separate from DSD object status.
7. Record selections and exclusions.
8. Record material bridges, aggregation/reconstruction assumptions, transition classes, and lineage requirements.
9. End with external-domain verdict, DSD structural audit verdict, limits, and reproducibility information.

## File naming / 파일명

Recommended:

```text
YYYY-MM-DD_short-audit-title.md
```

Formal ID:

```text
DSD-AUDIT-YYYYMMDD-DOMAIN-NNN
```

## Audit status / 감사 상태

```text
STATUS: PLANNED
STATUS: IN_PROGRESS
STATUS: BLOCKED_BY_MISSING_EVIDENCE
STATUS: COMPLETED
STATUS: REVISED
```

`BLOCKED_BY_MISSING_EVIDENCE` is not a negative verdict.

## Legacy records / 기존 감사 기록

Audit records created before the separated `DSD_Audit/` structure may remain in the repository's previous `audits/` paths.
They are historical records and should not be silently relocated or rewritten simply to appear current.

When a legacy case is actively re-audited under the separated DSD Audit structure:

1. preserve the original file and verdict;
2. create a new audit record or explicit migration record here;
3. state old and current interface profiles separately;
4. identify which conclusions survive, require reinterpretation, or become unsupported;
5. cross-link the legacy path and new path.

## Revision policy / 개정 원칙

Do not erase a previous reasonable verdict when new evidence or a new DSD interface appears.
Append a revision or migration record showing the new source, changed scope/interface, changed verdict, and reason.
