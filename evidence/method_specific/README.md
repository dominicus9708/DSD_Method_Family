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
  - maturity classification after `DES-AUD-001`: `developing`;
  - current evidence status: `validation_in_progress`;
  - direct constructed pilots: `7`;
  - positive: `DES-CH-001` PASS;
  - negative/failure: `DES-CH-002` PASS;
  - boundary: `DES-CH-003` preserved failed challenge design + corrected `DES-CH-004` PASS;
  - NO_GAIN: `DES-CH-005` PASS;
  - strongest-reasonable-baseline comparison: `DES-CH-006` PASS with `NO_GAIN`;
  - external applications: `DES-APP-001` W3C WCAG 2.2 + `DES-APP-002` NIST SP 800-63B-4, both PASS;
  - external domains: `2`;
  - reproducibility/retrace: `DES-CH-007` PASS at deterministic same-project level;
  - maturity audit: `DES-AUD-001` completed, 24/24 audit-discipline checks PASS, promotion to established withheld at audit time;
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
```

`DES-APP-002` uses a source-supplied positive authenticator-route grammar and preserves:

```text
TWO_DISTINCT_FACTOR_STRUCTURE
!= NIST_AAL2_PERMITTED_FORM
```

It also keeps verifier-level phishing-resistant-option requirements separate from per-route filtering and does not fabricate replay-resistance, cryptographic implementation, protected-channel, FIPS, or full deployed-system conformance from form-level data.

Current Design status:

```text
DIRECT_CONSTRUCTED_PILOTS: 7
EXTERNAL_APPLICATIONS: 2
EXTERNAL_DOMAINS: 2
EXTERNAL_APPLICATION_PASSES: 2
INDEPENDENT_EVALUATOR_VALIDATION: not established
METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

`DES-APP-002` is post-audit evidence and does not retroactively modify `DES-AUD-001`. The next preferred evidence step is a genuinely independent evaluator packet with expected results committed separately before reviewer submission. A later maturity reclassification requires a new audit record.

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
