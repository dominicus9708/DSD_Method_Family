# 07. DSD Classification / DSD 분류론

Status: **pre-protocol boundary stage completed / Protocol v0.1 next**

Task: classify supplied subjects by explicit class criteria and preserved formation, property, comparison, aggregate, transition, or other declared features rather than by labels alone.

Primary DSD sources are activated conditionally: Formation descriptors, General Property descriptors, explicit comparison/equivalence relations, optional aggregate descriptors with information-loss checks, and optional dynamic/lineage descriptors when the task requires them.

Typical outputs:
- criterion-traceable class assignments and membership status;
- classification criteria, feature provenance, and justification trace;
- equivalence classes or partial-order groupings only when their relation obligations are established;
- boundary, underdetermined, unclassified, blocked, and out-of-scope cases;
- distinction between structural class and summary-statistic coincidence.

Boundary: typology labels do not determine mathematics or semantics by name; every classification rule requires explicit criteria and a frozen membership decision rule. Pairwise similarity is not automatically equivalence-class membership, ordered labels are not automatically a partial order, aggregate equality is not automatically structural identity, a schema marked closed is not automatically proven exhaustive, and current class equality is not lineage identity.

Development files:
- [`PLANNING.md`](PLANNING.md)
- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- [`WORKLOG.md`](WORKLOG.md)

Boundary-stage result:

```text
BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 12
PRESERVED_WITH_NONBREAKING_REFINEMENT: 6
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
BOUNDARY_AMENDMENT_001: established
```

Current evidence state:

```text
DEDICATED_CLASSIFICATION_PROTOCOL: not established
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved
DIRECT_CLASSIFICATION_PILOTS: 0
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: pre_validation
```

Next: build executable `PROTOCOL_v0.1.md` from the historical Task Interface v0.1 draft plus Boundary Amendment 001. Protocol construction remains infrastructure and does not by itself validate the method or decide its survival, merger, absorption, or deletion.
