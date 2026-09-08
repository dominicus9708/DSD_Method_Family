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
  - external application: `DES-APP-001` PASS using W3C WCAG 2.2 subset;
  - reproducibility/retrace: `DES-CH-007` PASS at deterministic same-project level;
  - maturity audit: `DES-AUD-001` completed, 24/24 audit-discipline checks PASS, promotion to established withheld;
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
DES-AUD-001: 24/24 audit checks PASS, maturity = developing
```

`DES-AUD-001` scored the maturity axes as:

```text
M1  dedicated executable protocol                  PASS
M2  positive/negative terminal discrimination      PASS
M3  neighboring-method boundary discrimination     PASS
M4  NO_GAIN preservation                           PASS
M5  reproducibility/retraceability                 CONDITIONAL_PASS
M6  external application origin                    PASS
M7  strongest-reasonable-baseline comparison       PASS
M8  external source fidelity and bridge discipline PASS
M9  established-level evidence breadth             INSUFFICIENT
M10 independent/practical-performance evidence     UNRESOLVED_BUT_BOUNDED
M11 protocol pressure / unresolved core defect     PRESENT_NONFATAL
M12 maximum-supported-claim discipline             PASS
M13 candidate/construction-basis discipline        PASS
M14 historical failure / anti-post-hoc preservation PASS
```

Final Design maturity decision:

```text
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
METHOD_MATURITY_CLASSIFICATION: developing
PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
PRIMARY_BLOCKER: insufficient external evidence breadth
SECONDARY_BLOCKER: independent/practical evidence not established
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The maturity audit explicitly does not count as a new Design direct pilot.
The preferred next evidence is a second external Design application in a materially different domain, ideally with an externally supplied artifact or candidate/construction basis rather than a project-authored fixture.

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
