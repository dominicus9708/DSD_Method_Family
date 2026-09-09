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
- Independent-evaluator packet preparation is infrastructure only; it becomes evidence only after an eligible external submission is frozen and scored against the precommitted reference.

## Method-specific evidence lanes / 개별 증거 경로

- [`specification/`](specification/) — **DSD Specification / DSD 명세론**
  - historical v0.1/v0.2 evidence preserved;
  - newer Protocol lineage and external applications remain in the Specification lane;
  - independent evaluator validation is not established.

- [`design/`](design/) — **DSD Design / DSD 설계론**
  - Protocol v0.1 established on `2026-09-08`;
  - maturity classification after `DES-AUD-001`: `developing`;
  - current evidence status: `validation_in_progress`;
  - direct constructed pilots: `7`;
  - positive: `DES-CH-001` PASS;
  - negative/failure: `DES-CH-002` PASS;
  - boundary: `DES-CH-003` preserved failed challenge design + corrected `DES-CH-004` PASS;
  - NO_GAIN: `DES-CH-005` PASS;
  - strongest-reasonable-baseline comparison: `DES-CH-006` PASS with `NO_GAIN`;
  - external applications: `DES-APP-001` W3C WCAG 2.2 + `DES-APP-002` NIST SP 800-63B-4 + `DES-APP-003` 2010 ADA ramp-run subset, all PASS;
  - external domains: `3`;
  - reproducibility/retrace: `DES-CH-007` PASS at deterministic same-project level;
  - maturity audit: `DES-AUD-001` completed, 24/24 audit-discipline checks PASS, promotion to established withheld at audit time;
  - independent evaluator packet: `DES-IEP-001` prepared with frozen reviewer packet, submission template, and hidden-reference SHA-256 commitment;
  - independent evaluator submissions: `0`;
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
DES-AUD-001: 24/24 audit checks PASS, maturity = developing at audit time
DES-APP-002: 38/38 PASS, external NIST SP 800-63B-4 AAL2 route-form application
DES-IEP-001: packet prepared, submissions 0, no independent validation yet
DES-APP-003: 38/38 PASS, external 2010 ADA selected ramp-run physical application
```

`DES-APP-003` adds the built-environment / physical-accessibility domain with selected U.S. Access Board ramp requirements:

```text
running slope 1:12 maximum
cross slope 1:48 maximum
clear width 36 inches minimum
rise 30 inches maximum per run
top and bottom landings required
```

It returns `{R1,R2,R9}` within the frozen fixture and preserves absent-ramp `CHANNEL_ABSENCE` versus inapplicable geometry while avoiding full-ADA or engineering-certification overclaims.

`DES-IEP-001` freezes:

```text
reviewer packet commit:
78b1fb45d0b2e40838517828d089942e7b55e7d8

submission template commit:
fe1eedca019b4283a21047d21fcac12dd672e328

reference commitment commit:
8fe4ff64b3fc964746d7e8c11bd03d712c40fedd

SHA-256 commitment:
3f2cf7c7787578063096c98ada872f29fffb6fdef27f7893d039e04604a2b0cf
```

The reference plaintext and nonce are withheld until an eligible evaluator freezes a submission.
Preparation does not increase Design evidence counts.

Current Design status:

```text
DIRECT_CONSTRUCTED_PILOTS: 7
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
EXTERNAL_APPLICATION_PASSES: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

`DES-APP-002`, `DES-APP-003`, and `DES-IEP-001` are post-audit records and do not retroactively modify `DES-AUD-001`.
The next core Design evidence event requires a genuinely separate evaluator to submit against the frozen packet before key reveal.
A later maturity reclassification requires a new audit record.

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

Same-session or same-project retrace does not substitute for a genuinely independent reviewer. External-application count also does not by itself establish independent replication or established cross-domain breadth.
