# 07. DSD Classification / DSD 분류론

Status: **Protocol v0.1 frozen / CLS-CH-001 positive direct challenge PASS / negative challenge next**

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

Current evidence state:

```text
DEDICATED_CLASSIFICATION_PROTOCOL: established v0.1
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved
DIRECT_CLASSIFICATION_PILOTS: 1
POSITIVE_DIRECT_CHALLENGES: 1
NEGATIVE_FAILURE_CHALLENGES: 0
METHOD_BOUNDARY_CHALLENGES: 0
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CLASSIFICATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: validation_in_progress
```

One constructed positive case does not establish superiority, independent validation, external validity, or permanent method independence. The next valid step is a pre-frozen negative/failure-terminal challenge testing that non-positive states remain distinguishable rather than collapsing into one generic failure state. PASS, FAIL, `NO_GAIN`, boundary, or underdetermined results remain separate from any method survival, merger, absorption, or deletion decision.