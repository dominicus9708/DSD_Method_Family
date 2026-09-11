# Method-Specific Evidence / 개별 방법 직접 증거

This folder records evidence that directly tests one of the **22 independent DSD methods**. Evidence does not transfer automatically between methods merely because methods share a higher-level field or common DSD source layers.

## Current inheritance policy / 현재 상속 정책

- Shared-rule lessons may be cross-referenced but do not automatically become another method's direct validation.
- Maturity/status audits do not themselves increase the audited method's direct-pilot count.
- Independent-evaluator packet preparation is infrastructure until an eligible external submission exists.
- Failed challenge designs remain historical evidence of test pressure but do not fill successful validation categories.
- A success or failure in one case does not by itself imply that a method must survive, merge, be absorbed, or be deleted. Method independence is assessed separately.
- `NO_GAIN` or baseline matching does not by itself prove redundancy or absorption.
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

### `comparison/` — DSD Comparison / DSD 비교론

Planning opened `2026-09-10`; executable `PROTOCOL_v0.1.md` was established at commit `a1700d960e0b41dfe32bf85b6334448d9104100d` after 16 pre-protocol boundary attacks.

Current Comparison state after `CMP-CH-005`:

```text
DEDICATED_COMPARISON_PROTOCOL: v0.1 established
PROTOCOL_CREATION_COMMIT: a1700d960e0b41dfe32bf85b6334448d9104100d
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
BOUNDARY_PRESERVED_NO_REFINEMENT: 11
BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_COMPARISON_PILOTS: 5
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 2
BASELINE_COMPARISON_CASES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 0
EXTERNAL_COMPARISON_APPLICATIONS: 0
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

Direct evidence:

```text
CMP-CH-001
  PRECOMMIT: 16c4b15
  RESULT: c601bd2
  SCORE: 40/40 PASS

CMP-CH-002
  PRECOMMIT: c852a68
  RESULT: ca2e91f
  SCORE: 48/48 PASS

CMP-CH-003
  PRECOMMIT: 68d330b
  RESULT: b4256d2
  SCORE: 48/48 PASS

CMP-CH-004
  PRECOMMIT: 0d96d6b
  RESULT: 4cacd55
  SCORE: 50/50 PASS
  BASELINE: B0_TYPED_COMPARISON_LEDGER
  G1-G6: NOT_ESTABLISHED
  COMPARISON_METHOD_GAIN_STATUS: NO_GAIN

CMP-CH-005
  PRECOMMIT: ad54230
  RESULT: 61675b3
  SCORE: 60/60 PASS
  BASELINE: B1_STRONG_TYPED_COMPARISON_ENGINE
  R1 first-branch S2 preserved
  R2 directional direct correspondence != strict equivalence
  R3 partial element coverage preserved
  R4 encoded bridge provenance preserved
  R5 trajectory equivalence != lineage identity
  G1-G7: NOT_ESTABLISHED
  COMPARISON_METHOD_GAIN_STATUS: NO_GAIN
  STRONGEST_REASONABLE_BASELINE_COMPARISON:
    established_at_constructed_evidence_level
```

Current Comparison guards include:

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
COMMON_LABEL != COMMON_COORDINATE_OR_SEMANTIC_ROLE
EMBEDDING != STRICT_EQUIVALENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
UNSUPPLIED_NORMALIZATION_OR_CONVERSION != COMPARISON_MAP
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
NONEXHAUSTIVE_MAP_FAILURE != RESOLVED_NONCORRESPONDENCE
COMPARISON_EQUIVALENCE != INTERNAL_DECOMPOSITION
COMPARISON_RELATION != TAXONOMY_ASSIGNMENT
TRACE_DIFFERENCE != AUDIT_CONFORMANCE_VERDICT
STRUCTURAL_EQUIVALENCE != LINEAGE_IDENTITY
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
```

The next Comparison event is the first external application `CMP-APP-001` using a stable public source with externally supplied compared records and comparison criterion.

## Promotion expectation / 성숙도 승격 기준

A proposed/developing method should accumulate, at minimum, a dedicated method protocol; positive, negative/failure, boundary and `NO_GAIN` cases; reproducibility records; external or independently generated applications; and a strongest-reasonable-baseline comparison when applicable. These are evidence categories, not automatic promotion rules. Same-project retrace does not substitute for independent review, and external-application count does not establish practical superiority or method survival.
