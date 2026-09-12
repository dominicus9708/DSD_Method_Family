# 07. DSD Classification / DSD 분류론

Status: **Protocol v0.1 frozen / CLS-CH-001~004 PASS / CLS-CH-004 NO_GAIN / strongest-reasonable-baseline challenge next**

Task: classify supplied subjects by explicit class criteria and preserved formation, property, comparison, aggregate, transition, or other declared features rather than by labels alone.

Primary DSD sources are activated conditionally: Formation descriptors, General Property descriptors, explicit comparison/equivalence relations, optional aggregate descriptors with information-loss checks, and optional dynamic/lineage descriptors when the task requires them.

Typical outputs:
- criterion-traceable class assignments and membership status;
- classification criteria, feature provenance, and justification trace;
- equivalence classes or partial-order groupings only when their relation obligations are established;
- boundary, underdetermined, open-world-no-match, unclassified, blocked, and out-of-scope cases;
- distinction between structural class and summary-statistic coincidence.

Boundary: labels do not determine mathematical or semantic properties by name. Every classification claim is relative to a frozen schema/version, criterion source, membership rule, evidence/provenance basis, coverage/closure claim, and any required bridge.

## Development files

- [`PLANNING.md`](PLANNING.md)
- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- [`WORKLOG.md`](WORKLOG.md)

## Direct evidence

- [`CLS-CH-001 precommit`](../../evidence/method_specific/classification/CLS-CH-001_precommit.md)
- [`CLS-CH-001 positive direct classification`](../../evidence/method_specific/classification/CLS-CH-001_positive-direct-classification.md)
- [`CLS-CH-002 precommit`](../../evidence/method_specific/classification/CLS-CH-002_precommit.md)
- [`CLS-CH-002 negative/failure terminal distinction`](../../evidence/method_specific/classification/CLS-CH-002_negative-failure-terminal-distinction.md)
- [`CLS-CH-003 precommit`](../../evidence/method_specific/classification/CLS-CH-003_precommit.md)
- [`CLS-CH-003 direct method-boundary`](../../evidence/method_specific/classification/CLS-CH-003_direct-method-boundary.md)
- [`CLS-CH-004 precommit`](../../evidence/method_specific/classification/CLS-CH-004_precommit.md)
- [`CLS-CH-004 competent-baseline NO_GAIN`](../../evidence/method_specific/classification/CLS-CH-004_competent-baseline-no-gain.md)

## Protocol lineage

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Pre-protocol boundary attack:

```text
BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 12
PRESERVED_WITH_NONBREAKING_REFINEMENT: 6
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
BOUNDARY_AMENDMENT_001: established
```

## Constructed direct evidence summary

```text
CLS-CH-001  36/36 PASS  positive typed-status classification
CLS-CH-002  50/50 PASS  negative/failure-terminal distinction
CLS-CH-003  48/48 PASS  direct method-boundary challenge
CLS-CH-004  50/50 PASS / NO_GAIN  competent baseline
```

`CLS-CH-001` preserved `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED` despite an equal non-authoritative display value and preserved that unequal nonzero values may share a class at a coarser frozen status resolution.

`CLS-CH-002` separately preserved `BOUNDARY_CASE`, `UNDERDETERMINED`, `CRITERION_CONFLICT`, `BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION`, `OUT_OF_SCOPE`, `OPEN_WORLD_NO_CURRENT_MATCH`, and `UNCLASSIFIED_WITHIN_DECLARED_SCHEMA`.

`CLS-CH-003` compared Classification with Analysis, Comparison, Specification, and Diagnosis under the same five-interface non-duplication test. All four frozen pairs resolved to `PARTIAL_OVERLAP_NOT_COLLAPSE`; no exact-collapse candidate was found in those tasks. This is a local boundary result, not permanent irreducibility.

## CLS-CH-004 — competent baseline

Baseline:

```text
B0_TYPED_RULE_CLASSIFIER
```

B0 received exactly the same subject evidence, typed status records, schema IDs/versions, coverage claims, class criteria, composition/decision rules, overlap/exclusion semantics, uncertainty policy, closure evidence, bridge requirements, and terminal-status rules as DSD Classification.

Five frozen tasks produced identical task-level results:

```text
Q1 DSD/B0 -> C-U / CLASSIFIED_SINGLE
Q2 DSD/B0 -> {K-A,K-B} / CLASSIFIED_MULTI
Q3 DSD/B0 -> OPEN_WORLD_NO_CURRENT_MATCH
Q4 DSD/B0 -> BOUNDARY_CASE
Q5 DSD/B0 -> BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
```

Gain axes:

```text
G1 STATUS_DISTINCTION_GAIN: NOT_ESTABLISHED
G2 OVERLAP_AND_CONFLICT_SEPARATION_GAIN: NOT_ESTABLISHED
G3 SCHEMA_COVERAGE_AND_CLOSURE_GAIN: NOT_ESTABLISHED
G4 UNCERTAINTY_AND_BOUNDARY_GAIN: NOT_ESTABLISHED
G5 BRIDGE_AND_BLOCKAGE_GAIN: NOT_ESTABLISHED
G6 TRACEABILITY_GAIN: NOT_ESTABLISHED

CLASSIFICATION_METHOD_GAIN_STATUS: NO_GAIN
```

A competent typed rule classifier supplied with the same semantics matched DSD on these frozen dimensions. This is a valid comparative result and does not constitute method failure, merger evidence, absorption evidence, deletion evidence, or permanent redundancy.

## Core guards

```text
CLASS_LABEL != CLASS_CRITERION
SUMMARY_COINCIDENCE != STRUCTURAL_CLASS_IDENTITY
PAIRWISE_SIMILARITY != EQUIVALENCE_CLASS_MEMBERSHIP
ORDERED_LABELS != PROVEN_PARTIAL_ORDER
CURRENT_CLASS_MATCH != TEMPORAL_LINEAGE_IDENTITY
MISSING_FEATURE != NEGATIVE_FEATURE
UNDEFINED != DEFINED_ZERO
OUT_OF_SCOPE != UNCLASSIFIED
BOUNDARY_CASE != CLASSIFICATION_FAILURE
MULTI_CLASS_MEMBERSHIP != CRITERION_CONFLICT
SCHEMA_STATUS_CLOSED != CLOSED_WORLD_COVERAGE_ESTABLISHED
CRITERION_LIST != MEMBERSHIP_LOGIC
NO_CURRENT_MATCH_IN_OPEN_SCHEMA != UNIVERSAL_NONMEMBERSHIP
NO_GAIN != METHOD_ABSORPTION_PROOF
```

## Current evidence state

```text
DEDICATED_CLASSIFICATION_PROTOCOL: established v0.1
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved
PRE_PROTOCOL_BOUNDARY_ATTACKS: 18 completed
BOUNDARY_AMENDMENT_001: established
DIRECT_CLASSIFICATION_PILOTS: 4
POSITIVE_DIRECT_CHALLENGES: 1
NEGATIVE_FAILURE_CHALLENGES: 1
METHOD_BOUNDARY_CHALLENGES: 1
NO_GAIN_CLASSIFICATION_CASES: 1
BASELINE_CLASSIFICATION_CASES: 1
STRONGEST_REASONABLE_BASELINE_CLASSIFICATION: not established
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CLASSIFICATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Constructed same-project evidence does not establish independent validation, external validity, measured practical benefit, permanent method independence, or registry survival.

## Next development step

Precommit and execute `CLS-CH-005`, a **strongest-reasonable-baseline** challenge with a materially richer baseline and a more demanding task family than `B0_TYPED_RULE_CLASSIFIER`. The strong baseline must again receive all claim-relevant information and may legitimately produce another `NO_GAIN`. The next challenge should pressure interactions among schema/coverage closure, criterion composition, uncertainty, generated or versioned schema semantics, aggregate-information-loss controls, and/or time-sensitive classification without adding unused complexity merely to favor DSD.
