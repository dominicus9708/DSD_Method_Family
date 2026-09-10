# Method-Specific Evidence / 개별 방법 직접 증거

This folder records evidence that directly tests one of the **22 independent DSD methods**. Evidence does not transfer automatically between methods merely because methods share a higher-level field or common DSD source layers.

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
- Failed challenge designs remain historical evidence of test pressure but do not fill successful validation categories.
- A success or failure in one case does not by itself imply that a method must survive, merge, be absorbed, or be deleted. Method independence is assessed separately.

## Method-specific evidence lanes / 개별 증거 경로

### `specification/` — DSD Specification / DSD 명세론

Historical v0.1/v0.2 evidence is preserved. Use the newest Specification-specific records for detailed maturity truth.

### `design/` — DSD Design / DSD 설계론

```text
PROTOCOL: v0.1 established
METHOD_MATURITY_CLASSIFICATION: established after DES-AUD-002
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
DIRECT_CONSTRUCTED_PILOTS: 7
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
INDEPENDENT_EVALUATOR_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
```

Key Design records include positive, negative/failure, corrected boundary, NO_GAIN, strongest-reasonable-baseline, three external applications, deterministic same-project retrace, two maturity audits, and the prepared `DES-IEP-001` independent-evaluator packet.

### `synthesis/` — DSD Synthesis / DSD 합성론

Planning opened `2026-09-10` and executable `PROTOCOL_v0.1.md` was established at commit `8787b24`.

Current Synthesis state:

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_SYNTHESIS_APPLICATIONS: 1
EXTERNAL_SYNTHESIS_DOMAINS: 1
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 1
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

Key Synthesis evidence:

```text
SYN-CH-001
  28/28 PASS
  positive

SYN-CH-002
  36/36 PASS
  INFEASIBLE != UNDERDETERMINED != BLOCKED

SYN-CH-003
  46/46 PASS
  Design / Transformation / Aggregation / Optimization handoffs preserved

SYN-CH-004
  33/35 FAIL
  CHALLENGE_DESIGN_DEFECT preserved
  Protocol failure not inferred

SYN-CH-005
  37/37 PASS
  competent B0 baseline
  SYNTHESIS_ADMISSIBLE / CONFORMANT / NO_GAIN

SYN-CH-006
  PRECOMMIT: 4a6c1fe
  RESULT: 8ad51b5
  52/52 PASS
  competent B1 strongest-reasonable baseline
  raw family DSD = B1 = {A1,A2,A3,A4}
  canonical family DSD = B1 = {C0,C1}
  supplied grouping equivalence + whole-Property lift + relation retention + formation effect
  SYNTHESIS_ADMISSIBLE / CONFORMANT / NO_GAIN
  STRONGEST_REASONABLE_BASELINE_COMPARISON:
    established_at_constructed_evidence_level

SYN-APP-001
  EXTERNAL_STANDARD: RFC 3986 / STD 66
  EXTERNAL_DOMAIN: Internet identifier syntax / URI generic syntax
  PRECOMMIT: 29ea45a
  RESULT: 6985246
  40/40 PASS
  admissible family {R1,R2,R3,R4,R10,R11,R12}
  R5/R6 -> H2
  R7 -> H1
  R8 -> H4 declared-component roundtrip failure
  R9 -> H3 lexical failure
  SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED

SYN-CH-007
  RETRACE_TARGET: SYN-APP-001
  PRECOMMIT: 9bbcadf
  RESULT: 7256456
  48/48 PASS
  reconstructed all R1-R12 verdicts/failure staging
  reconstructed family {R1,R2,R3,R4,R10,R11,R12}
  REPRODUCIBILITY_LEVEL: deterministic_same_project
  INDEPENDENT_REPLICATION: not established
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
PRESENT_EMPTY != ABSENT when the external interface distinguishes them
GENERIC_EXTERNAL_SYNTAX != STRONGER_DOMAIN_SPECIFIC_VALIDITY
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
```

The next Synthesis task is a second materially different external application in a non-URI domain before maturity review.

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

These are minimum evidence categories for promotion consideration, not an automatic promotion rule. Same-session or same-project retrace does not substitute for independent review, and external-application count does not establish practical superiority or method survival.
