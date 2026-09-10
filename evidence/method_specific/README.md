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

- `specification/` — **DSD Specification / DSD 명세론**
  - historical v0.1/v0.2 evidence preserved;
  - use the newest Specification-specific records for detailed maturity truth.

- `design/` — **DSD Design / DSD 설계론**
  - Protocol v0.1 established on `2026-09-08`;
  - revision maturity classification after `DES-AUD-002`: **established**;
  - current evidence status: `validation_in_progress` because independent/practical validation remains open;
  - direct constructed pilots: `7`;
  - positive `DES-CH-001` PASS;
  - negative/failure `DES-CH-002` PASS;
  - boundary `DES-CH-003` preserved failed challenge design + corrected `DES-CH-004` PASS;
  - `DES-CH-005` NO_GAIN PASS;
  - `DES-CH-006` strongest-reasonable-baseline comparison PASS with NO_GAIN;
  - external applications: WCAG 2.2, NIST SP 800-63B-4, and 2010 ADA subset, all PASS;
  - external domains: `3`;
  - `DES-CH-007` deterministic same-project retrace PASS;
  - `DES-AUD-001` historical developing verdict preserved;
  - `DES-AUD-002` 26/26 audit checks PASS and `PROMOTE_ESTABLISHED`;
  - `DES-IEP-001` independent evaluator packet prepared, submissions `0`.

Current Design separation:

```text
METHOD_MATURITY_CLASSIFICATION: established
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
INDEPENDENT_EVALUATOR_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
```

- `synthesis/` — **DSD Synthesis / DSD 합성론**
  - planning opened on `2026-09-10`;
  - current maturity classification: `proposed`;
  - current evidence status: `validation_in_progress`;
  - dedicated executable protocol: `PROTOCOL_v0.1.md`, creation commit `8787b24`;
  - direct Synthesis pilots: `3`;
  - positive cases: `1`;
  - negative/failure cases: `1`;
  - boundary cases under executable Protocol: `1`;
  - pre-protocol boundary attacks: `16` = 11 no-refinement + 5 non-breaking-refinement, 0 collapse, 0 fundamental interface failure;
  - NO_GAIN cases: `0`;
  - baseline comparison cases: `0`;
  - reproducibility cases: `0`;
  - external Synthesis applications: `0`;
  - independent Synthesis validation: `not established`.

Key Synthesis evidence:

```text
SYN-CH-001
  precommit 4eeba2a
  result 71e5d5c
  28/28 PASS
  {K1,K2} admissible
  SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED

SYN-CH-002
  precommit 09fc616
  result 7dac87c
  36/36 PASS
  I -> SYNTHESIS_INFEASIBLE
  U -> SYNTHESIS_UNDERDETERMINED
  B -> SYNTHESIS_BLOCKED
  all CONFORMANT / NOT_ASSESSED

SYN-CH-003
  precommit 2eea8ae
  result cb55dba
  46/46 PASS
  common Synthesis family {S0,S1}
  D -> DESIGN_REQUIRED handoff
  T -> TRANSFORMATION_REQUIRED handoff
  A -> AGGREGATION_REQUIRED handoff
  O -> OPTIMIZATION_REQUIRED handoff
  Synthesis family unchanged in all four subcases
  all SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
  PROTOCOL_REVISION_REQUIRED: no
```

Current Synthesis guards include:

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY != AUTOMATIC_COMPOSABILITY
EXHAUSTIVE_COMPONENT_LIST != EXHAUSTIVE_COMPOSITION_SPACE
FORMATION_CLAUSE_VII_COMPOSITION != DOMAIN_SYNTHESIS_LEGITIMACY
AGGREGATE_READOUT != SYNTHESIZED_WHOLE
COMPONENT_PROPERTY != WHOLE_PROPERTY
candidate ID / syntax tree != material synthesized-target distinctness
PARTIAL_SYNTHESIS != completed synthesized target
STATIC_COMPOSITION_ORDER != TEMPORAL_ASSEMBLY_SEQUENCE
REJECTED_UNDER_EXHAUSTIVE_COVERAGE != INSUFFICIENT_COVERAGE_FOR_CLOSURE != MISSING_REQUIRED_INPUT
local admissibility != requested output-level closure
```

Executable method-boundary evidence additionally preserves:

```text
SYNTHESIS_SUCCESS != MIXED_WORKFLOW_COMPLETION
SYNTHESIS_ADMISSIBLE_FAMILY != OPTIMIZED_SELECTION
SYNTHESIZED_WHOLE != AGGREGATE_READOUT
SYNTHESIZED_STRUCTURE != TRANSFORMED_REPRESENTATION
SUPPLIED_PARTS != DESIGN_LICENSE_TO_INVENT_MISSING_PARTS
```

Current Synthesis state:

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 3
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

The next Synthesis task is the first separately precommitted `NO_GAIN` case against a competent baseline. The baseline must receive the same composition-relevant information and must not be weakened to manufacture DSD advantage.

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

These are minimum evidence categories for promotion consideration, not an automatic promotion rule. Same-session or same-project retrace does not substitute for independent review, and external-application count does not establish practical superiority.
