# Method-Specific Evidence / 개별 방법 직접 증거

This folder records evidence that directly tests one of the **22 independent DSD methods**.

Evidence does not transfer automatically between methods merely because methods share a higher-level field or common DSD source layers.

## Required record fields

```text
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED:
METHOD_VERSION_OR_PROTOCOL:
TASK:
INPUTS:
DSD_LAYERS_USED:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
OPERATION:
OUTPUTS:
FAILURE_OR_NO_GAIN_CRITERIA:
RESULT:
LIMITS:
REPRODUCIBILITY_RECORD:
```

## Current inheritance policy / 현재 상속 정책

- Analysis challenge evidence directly validates DSD Analysis only.
- Audit records directly validate DSD Audit procedures/verdict discipline only.
- Shared-rule lessons may be cross-referenced but do not automatically become another method's direct validation.
- A maturity/status audit is an Audit meta-record and does not itself increase the audited method's direct-pilot count.

## Method-specific evidence lanes / 개별 증거 경로

- [`specification/`](specification/) — **DSD Specification / DSD 명세론**
  - historical v0.1/v0.2 evidence preserved;
  - newer Protocol lineage and external applications remain in the Specification lane;
  - independent evaluator validation is not established.

- [`design/`](design/) — **DSD Design / DSD 설계론**
  - Protocol v0.1 established on `2026-09-08`;
  - current evidence status: `validation_in_progress`;
  - direct constructed pilots: `7`;
  - positive: `DES-CH-001` PASS;
  - negative/failure: `DES-CH-002` PASS;
  - boundary: `DES-CH-003` preserved failed challenge design + corrected `DES-CH-004` PASS;
  - NO_GAIN: `DES-CH-005` PASS;
  - strongest-reasonable-baseline comparison: `DES-CH-006` PASS with `NO_GAIN`;
  - external application: `DES-APP-001` PASS using W3C WCAG 2.2 subset;
  - reproducibility/retrace: `DES-CH-007` PASS at deterministic same-project level;
  - independent evaluator validation: `not established`.

Key Design evidence summary:

```text
DES-CH-001: 11/11 PASS
DES-CH-002: 20/20 PASS
DES-CH-003: 20/21, challenge-design defect preserved
DES-CH-004: 23/23 PASS
DES-CH-005: 25/25 PASS, NO_GAIN
DES-CH-006: 54/54 PASS, competent typed baseline matched DSD, NO_GAIN
DES-APP-001: 36/36 PASS, external W3C WCAG 2.2 subset
DES-CH-007: 44/44 PASS, deterministic retrace of DES-APP-001
```

`DES-APP-001` kept external authority separate from the Design verdict, did not promote best-practice language into a hard requirement, did not invent a post-hoc exception, and did not overclaim full WCAG conformance.

`DES-CH-007` reconstructed W1-W10 verdicts, rejection bases, `{W1,W2,W3}`, `DESIGN_ADMISSIBLE`, `CONFORMANT`, `NOT_ASSESSED`, external source/version, and `WCAG_APPLICATION_BRIDGE_001` from frozen Design Protocol + source precommit and matched the preserved historical result exactly.

The retrace was non-blinded and same-project/common-evaluator; it therefore establishes deterministic record sufficiency/retraceability, **not** independent replication.

Design minimum evidence categories are now populated at least once, but this is not an automatic maturity grant. The next step is a Design maturity audit that explicitly discounts common-evaluator dependence and keeps independent validation open.

## Promotion expectation / 성숙도 승격 기준

A proposed/developing method should accumulate, at minimum:

1. a dedicated method protocol;
2. positive cases;
3. negative/failure cases;
4. boundary cases;
5. `NO_GAIN` cases;
6. reproducibility records;
7. at least one external or independently generated application;
8. a strongest-reasonable-baseline comparison when applicable.

These are minimum evidence categories for promotion consideration, not an automatic promotion rule. Later blind spots may justify prospective refinement without rewriting earlier evidence.

Same-session or same-project retrace does not substitute for a genuinely independent reviewer. External-application count also does not by itself establish independent replication.
