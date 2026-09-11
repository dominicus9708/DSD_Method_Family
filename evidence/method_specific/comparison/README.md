# DSD Comparison Direct Evidence / DSD 비교론 직접 증거

Status: **Protocol v0.1 established / positive + negative-failure + boundary + two NO_GAIN baseline challenges PASS / strongest-reasonable baseline established at constructed-evidence level / validation in progress**

This lane records evidence that directly tests **DSD Comparison / DSD 비교론**.

## Current development state

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

Protocol establishment and the 16 pre-protocol attacks do not increase the direct-pilot count.

## Protocol and planning artifacts

```text
methods/06_comparison/PROTOCOL_v0.1.md
  creation commit a1700d960e0b41dfe32bf85b6334448d9104100d
methods/06_comparison/TASK_INTERFACE_v0.1-draft.md
methods/06_comparison/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
methods/06_comparison/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
methods/06_comparison/PLANNING.md
methods/06_comparison/WORKLOG.md
```

## Direct Protocol-v0.1 evidence

### CMP-CH-001 — positive relation-separation challenge

```text
PRECOMMIT: 16c4b15
RESULT: c601bd2
SCORE: 40/40 PASS
```

### CMP-CH-002 — negative/failure terminal distinction

```text
PRECOMMIT: c852a68
RESULT: ca2e91f
SCORE: 48/48 PASS
```

### CMP-CH-003 — direct method-boundary challenge

```text
PRECOMMIT: 68d330b
RESULT: b4256d2
SCORE: 48/48 PASS
```

### CMP-CH-004 — competent-baseline NO_GAIN

```text
PRECOMMIT: 0d96d6b
RESULT: 4cacd55
BASELINE: B0_TYPED_COMPARISON_LEDGER
SCORE: 50/50 PASS
GAIN: NO_GAIN
```

B0 received the same claim-relevant records and matched DSD on strict equivalence, encoded correspondence, non-exhaustive closure, aggregate collision, and missing-bridge blockage.

### CMP-CH-005 — strongest-reasonable-baseline comparison

```text
PRECOMMIT: ad54230
RESULT: 61675b3
BASELINE: B1_STRONG_TYPED_COMPARISON_ENGINE
SCORE: 60/60 PASS

R1 DSD = B1
  PARTIAL_CORRESPONDENCE / FIRST_BRANCH S2 / RESOLVED
R2 DSD = B1
  DIRECT_CORRESPONDENCE / strict equivalence no / RESOLVED
R3 DSD = B1
  PARTIAL_CORRESPONDENCE / global equivalence unclosed / RESOLVED
R4 DSD = B1
  ENCODED_CORRESPONDENCE / bridge provenance preserved / RESOLVED
R5 DSD = B1
  sampled-trajectory STRICT_EQUIVALENT / DISTINCT_LINEAGES / RESOLVED

G1-G7: NOT_ESTABLISHED
COMPARISON_METHOD_GAIN_STATUS: NO_GAIN
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
PROTOCOL_REVISION_REQUIRED: no
```

This richer challenge simultaneously exercised first-branch closure, later re-convergence, direction/inverse requirements, partial-vs-global element coverage, bridge/representation provenance, and dynamic-trajectory-versus-lineage separation. The strong baseline was not weakened and matched all frozen dimensions.

## Protocol-v0.1 core guards

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
PARTIAL_ELEMENT_COVERAGE != STRICT_EQUIVALENCE
COMPARISON_EQUIVALENCE != INTERNAL_DECOMPOSITION
COMPARISON_RELATION != TAXONOMY_ASSIGNMENT
TRACE_DIFFERENCE != AUDIT_CONFORMANCE_VERDICT
STRUCTURAL_EQUIVALENCE != LINEAGE_IDENTITY
```

## Output / terminal / ledger structure

```text
OUTPUT_LEVELS:
  COMPARISON_PROFILE
  CORRESPONDENCE_CLASSIFICATION
  STRICT_EQUIVALENCE_DECISION
  FIRST_BRANCH_POINT
  PARTIAL_COMPARISON

TERMINAL:
  COMPARISON_RESOLVED
  COMPARISON_UNDERDETERMINED
  COMPARISON_BLOCKED

THREE LEDGERS:
  TERMINAL_COMPARISON_STATUS
  COMPARISON_PROTOCOL_CONFORMANCE
  COMPARISON_METHOD_GAIN_STATUS
```

## Evidence IDs

```text
CMP-CH-###   constructed Comparison challenges
CMP-APP-###  external or independently generated Comparison applications
CMP-AUD-###  Comparison-specific audit/maturity records
CMP-IEP-###  independent-evaluator infrastructure
```

## Inheritance and method-survival rule

Neighboring-method evidence may inform challenge design but does not automatically validate Comparison.

```text
BOUNDARY_PASS != PERMANENT_METHOD_INDEPENDENCE
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
PROTOCOL_ESTABLISHED != METHOD_VALIDATED
```

## Immediate next task

Precommit and execute `CMP-APP-001`, the first external Comparison application. Use a stable public source that supplies the compared records and a defensible external comparison criterion. Keep source-level truth, DSD Comparison conformance, and method gain separate.
