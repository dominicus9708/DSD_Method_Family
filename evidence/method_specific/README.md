# Method-Specific Evidence / 개별 방법 직접 증거

This folder records evidence that directly tests one of the **22 independent DSD methods**. Evidence does not transfer automatically between methods merely because methods share a higher-level field or common DSD source layers.

## Current inheritance policy / 현재 상속 정책

- Shared-rule lessons may be cross-referenced but do not automatically become another method's direct validation.
- Maturity/status audits do not themselves increase the audited method's direct-pilot count.
- Independent-evaluator packet preparation is infrastructure until an eligible external submission exists.
- Failed challenge designs remain historical evidence of test pressure but do not fill successful validation categories.
- A success or failure in one case does not by itself imply that a method must survive, merge, be absorbed, or be deleted. Method independence is assessed separately.
- Established method/protocol evidence maturity does not permanently freeze the method registry.

## Method-specific evidence lanes / 개별 증거 경로

### `design/` — DSD Design / DSD 설계론

```text
PROTOCOL: v0.1 established
METHOD_MATURITY_CLASSIFICATION: established after DES-AUD-002
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
DIRECT_CONSTRUCTED_PILOTS: 7
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
```

### `synthesis/` — DSD Synthesis / DSD 합성론

Planning opened `2026-09-10`; executable `PROTOCOL_v0.1.md` was established at commit `8787b24`.

Current Synthesis state after `SYN-AUD-001` and `SYN-IEP-001` preparation:

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
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
REFERENCE_KEY_COMMITMENT: frozen
CLEAN_DISTRIBUTION_RECORD: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

Key Synthesis evidence includes `SYN-CH-001` through `SYN-CH-007`, three external applications, `SYN-AUD-001`, and the prepared `SYN-IEP-001` packet. The next Synthesis evidence event requires a genuinely separate evaluator submission frozen before reference reveal.

### `comparison/` — DSD Comparison / DSD 비교론

Planning opened `2026-09-10` after the Synthesis internal-development track reached the point where further high-value evidence requires an external evaluator.

```text
DEDICATED_COMPARISON_PROTOCOL: not established
PRE_PROTOCOL_BOUNDARY_ATTACKS: 0
DIRECT_COMPARISON_PILOTS: 0
POSITIVE_COMPARISON_CASES: 0
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 0
BOUNDARY_COMPARISON_CASES: 0
NO_GAIN_COMPARISON_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_COMPARISON_APPLICATIONS: 0
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_pending
```

Planning artifacts:

```text
methods/06_comparison/TASK_INTERFACE_v0.1-draft.md
methods/06_comparison/PLANNING.md
methods/06_comparison/WORKLOG.md
evidence/method_specific/comparison/README.md
```

Initial Comparison guards:

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
COMMON_LABEL != COMMON_COORDINATE_OR_SEMANTIC_ROLE
EMBEDDING != STRICT_EQUIVALENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
SIMILAR_OUTPUT != SHARED_LINEAGE_OR_IDENTITY
```

These planning records are not direct evidence. The next internal step is pre-protocol boundary attack and only the refinements actually forced by those attacks should enter the first executable Comparison protocol.

## Promotion expectation / 성숙도 승격 기준

A proposed/developing method should accumulate, at minimum, a dedicated method protocol; positive, negative/failure, boundary and `NO_GAIN` cases; reproducibility records; external or independently generated applications; and a strongest-reasonable-baseline comparison when applicable. These are evidence categories, not automatic promotion rules. Same-project retrace does not substitute for independent review, and external-application count does not establish practical superiority or method survival.
