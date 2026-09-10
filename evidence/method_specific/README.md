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
  - use the newest Specification-specific records rather than this cross-method summary for detailed maturity truth.

- [`design/`](design/) — **DSD Design / DSD 설계론**
  - Protocol v0.1 established on `2026-09-08`;
  - revision maturity classification after `DES-AUD-002`: **established**;
  - current evidence status: `validation_in_progress` because independent/practical validation remains open;
  - direct constructed pilots: `7`;
  - positive: `DES-CH-001` PASS;
  - negative/failure: `DES-CH-002` PASS;
  - boundary: `DES-CH-003` preserved failed challenge design + corrected `DES-CH-004` PASS;
  - NO_GAIN: `DES-CH-005` PASS;
  - strongest-reasonable-baseline comparison: `DES-CH-006` PASS with `NO_GAIN`;
  - external applications: `DES-APP-001` W3C WCAG 2.2 + `DES-APP-002` NIST SP 800-63B-4 + `DES-APP-003` 2010 ADA selected ramp-run subset, all PASS;
  - external domains: `3`;
  - reproducibility/retrace: `DES-CH-007` PASS at deterministic same-project level;
  - historical maturity audit: `DES-AUD-001` developing at its audit time;
  - revision maturity audit: `DES-AUD-002` 26/26 audit checks PASS, M9 external breadth PASS, `PROMOTE_ESTABLISHED`;
  - independent evaluator packet: `DES-IEP-001` prepared and cleanroom-distributable;
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
DES-APP-002: 38/38 PASS, external NIST AAL2 route-form application
DES-IEP-001: packet prepared, submissions 0, no independent validation yet
DES-APP-003: 38/38 PASS, external ADA ramp-run physical application
DES-AUD-002: 26/26 audit checks PASS, method/protocol maturity = established
```

### Design maturity separation

`DES-AUD-002` establishes only **method/protocol evidence maturity under the current DSD method-family framework**.

```text
METHOD_MATURITY_CLASSIFICATION: established
M9_EXTERNAL_BREADTH: PASS
M5_REPRODUCIBILITY: CONDITIONAL_PASS
M10_INDEPENDENT_PRACTICAL: UNRESOLVED_BUT_BOUNDED
INDEPENDENT_EVALUATOR_VALIDATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
```

Therefore:

```text
established method/protocol maturity
!= independent evaluator validation
!= independent replication
!= measured practical superiority
```

Current Design status:

```text
DIRECT_CONSTRUCTED_PILOTS: 7
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
EXTERNAL_APPLICATION_PASSES: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
METHOD_MATURITY_CLASSIFICATION: established
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

The next core Design evidence event requires a genuinely separate evaluator to submit against the frozen `DES-IEP-001` packet before key reveal.
A later audit should preserve either agreement or disagreement rather than treating independent review as a required positive result.

- [`synthesis/`](synthesis/) — **DSD Synthesis / DSD 합성론**
  - planning opened on `2026-09-10`;
  - current maturity classification: `proposed`;
  - current evidence status: `validation_pending`;
  - dedicated executable protocol: **`PROTOCOL_v0.1.md` established**, creation commit `8787b24`;
  - direct Synthesis pilots: `0`;
  - pre-protocol boundary attacks: `16`;
  - boundary result: `11` preserved without refinement + `5` preserved with non-breaking refinement, `0` collapse, `0` fundamental interface failure;
  - protocol lineage: `TASK_INTERFACE_v0.1-draft.md + TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md -> PROTOCOL_v0.1.md`;
  - external Synthesis applications: `0`;
  - independent Synthesis validation: not established;
  - next direct task: separately precommit and execute positive `SYN-CH-001`.

Current Synthesis protocol guards:

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY
!= AUTOMATIC_COMPOSABILITY

EXHAUSTIVE_COMPONENT_LIST
!= EXHAUSTIVE_COMPOSITION_SPACE

FORMATION_CLAUSE_VII_COMPOSITION
!= DOMAIN_SYNTHESIS_LEGITIMACY

AGGREGATE_READOUT
!= SYNTHESIZED_WHOLE

COMPONENT_PROPERTY
!= WHOLE_PROPERTY

candidate ID / syntax tree
!= material synthesized-target distinctness

PARTIAL_SYNTHESIS
!= completed synthesized target

STATIC_COMPOSITION_ORDER
!= TEMPORAL_ASSEMBLY_SEQUENCE
```

Protocol v0.1 freezes composition-law/grouping, target equivalence/canonicalization, partial residuals, process scope, candidate coverage, target resolution, property lift, retention/loss, and formation effect before closure claims.

Current Synthesis state:

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 0
POSITIVE_SYNTHESIS_CASES: 0
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 0
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 0
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_pending
```

Protocol establishment and pre-protocol attacks are **not** counted as direct Synthesis pilot evidence.

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

Same-session or same-project retrace does not substitute for a genuinely independent reviewer. External-application count also does not by itself establish independent replication or practical superiority.
