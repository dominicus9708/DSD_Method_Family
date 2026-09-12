# 07. DSD Classification / DSD 분류론

Status: **Protocol v0.1 frozen / CLS-CH-001~003 PASS / competent-baseline challenge next**

Task: classify supplied subjects by explicit class criteria and preserved formation, property, comparison, aggregate, transition, or other declared features rather than by labels alone.

Primary DSD sources are activated conditionally: Formation descriptors, General Property descriptors, explicit comparison/equivalence relations, optional aggregate descriptors with information-loss checks, and optional dynamic/lineage descriptors when the task requires them.

Typical outputs:
- criterion-traceable class assignments and membership status;
- classification criteria, feature provenance, and justification trace;
- equivalence classes or partial-order groupings only when their relation obligations are established;
- boundary, underdetermined, open-world-no-match, unclassified, blocked, and out-of-scope cases;
- distinction between structural class and summary-statistic coincidence.

Boundary: typology labels do not determine mathematics or semantics by name; every classification rule requires explicit criteria and a frozen membership decision rule. Pairwise similarity is not automatically equivalence-class membership, ordered labels are not automatically a partial order, aggregate equality is not automatically structural identity, a schema marked closed is not automatically proven exhaustive, and current class equality is not lineage identity.

Development files:
- [`PLANNING.md`](PLANNING.md)
- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- [`WORKLOG.md`](WORKLOG.md)

Direct evidence:
- [`CLS-CH-001 precommit`](../../evidence/method_specific/classification/CLS-CH-001_precommit.md)
- [`CLS-CH-001 positive direct classification`](../../evidence/method_specific/classification/CLS-CH-001_positive-direct-classification.md)
- [`CLS-CH-002 precommit`](../../evidence/method_specific/classification/CLS-CH-002_precommit.md)
- [`CLS-CH-002 negative/failure terminal distinction`](../../evidence/method_specific/classification/CLS-CH-002_negative-failure-terminal-distinction.md)
- [`CLS-CH-003 precommit`](../../evidence/method_specific/classification/CLS-CH-003_precommit.md)
- [`CLS-CH-003 direct method-boundary`](../../evidence/method_specific/classification/CLS-CH-003_direct-method-boundary.md)

Protocol lineage:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Boundary-stage result:

```text
BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 12
PRESERVED_WITH_NONBREAKING_REFINEMENT: 6
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
BOUNDARY_AMENDMENT_001: established
```

First direct challenge:

```text
CASE_ID: CLS-CH-001
CASE_CLASS: positive_direct_classification_challenge
PRECOMMIT_COMMIT: 2c5944b2830201c8d9bdbbc3d945bb6bfb6f772d
RESULT_COMMIT: 8107d13f8b191199c202a324b8362e662ff6ab54
SCORE: 36/36 PASS
RESULT: PASS
PROTOCOL_CONFORMANCE: CONFORMANT for all four subject results
METHOD_GAIN: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED_BY_THIS_CASE: no
```

The case directly tested that `DEFINED_ZERO` and `APPLICABLE_BUT_UNDEFINED` remain distinct even when a non-authoritative display field is equal, while two different defined-nonzero values may share one class when the frozen target resolution classifies status rather than sign or magnitude.

Second direct challenge:

```text
CASE_ID: CLS-CH-002
CASE_CLASS: negative_failure_terminal_distinction
PRECOMMIT_COMMIT: eef7ea276186c382953c3b207ffa6c7dc237f603
PRECOMMIT_BLOB: a15719f5b7aebaf3b8df5c05f94f9b4f319ff464
RESULT_COMMIT: ba9ef338c95912ebec14d89f944ad54a640b7686
SCORE: 50/50 PASS
RESULT: PASS
METHOD_GAIN: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED_BY_THIS_CASE: no
```

It preserved seven distinct outcomes under frozen task semantics:

```text
BOUNDARY_CASE
UNDERDETERMINED
CRITERION_CONFLICT
BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
OUT_OF_SCOPE
OPEN_WORLD_NO_CURRENT_MATCH
UNCLASSIFIED_WITHIN_DECLARED_SCHEMA
```

All seven executions were protocol-conformant because each result represented the strongest justified status under its frozen scope, evidence, closure, and decision rules. In particular, open-world no-match was not upgraded to universal nonmembership, out-of-scope was not relabeled unclassified, and a missing bridge was not guessed from a raw label.

Third direct challenge:

```text
CASE_ID: CLS-CH-003
CASE_CLASS: direct_method_boundary_challenge
PRECOMMIT_COMMIT: 494711e72f9a9d025e59a66269e3af5c855a9e42
PRECOMMIT_BLOB: 25d8be7f899d0cf6ff5e496f59d9c593e713dc41
RESULT_COMMIT: 44b6095132dd9233ab85986af87d15c5f799b55d
SCORE: 48/48 PASS
RESULT: PASS
METHOD_GAIN: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED_BY_THIS_CASE: no
```

The challenge used the same five-interface non-duplication rule for Analysis, Comparison, Specification, and Diagnosis:

```text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
```

It explicitly permitted `DISTINCT_AT_TASK_INTERFACE`, `PARTIAL_OVERLAP_NOT_COLLAPSE`, or `EXACT_COLLAPSE_CANDIDATE` and did not define PASS as survival. All four tested pairs resolved to `PARTIAL_OVERLAP_NOT_COLLAPSE`: they shared subjects, observations, status records, or handoff carriers, while operation, output, failure semantics, and validation targets remained materially different. No exact-collapse candidate was found in these frozen tasks, but this is not a permanent irreducibility finding.

Current evidence state:

```text
DEDICATED_CLASSIFICATION_PROTOCOL: established v0.1
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved
DIRECT_CLASSIFICATION_PILOTS: 3
POSITIVE_DIRECT_CHALLENGES: 1
NEGATIVE_FAILURE_CHALLENGES: 1
METHOD_BOUNDARY_CHALLENGES: 1
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CLASSIFICATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: validation_in_progress
```

Three constructed same-project direct cases do not establish superiority, independent validation, external validity, permanent method independence, or a method-registry governance result. The next valid step is a pre-frozen competent-baseline challenge in which the baseline receives exactly the same task, schema/version, criteria, decision logic, subject evidence, and claim-relevant bridges. `NO_GAIN` must remain an allowed valid result and must not be treated as a merger, absorption, or deletion decision.