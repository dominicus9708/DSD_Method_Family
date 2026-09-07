# SPEC-MEAS-001 — ROUTE_D DSD Specification v1.0 Acceptance Record

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Source: `pytest-dev/pytest#12112` issue body only
Status: FROZEN_BEFORE_MAINTAINER_RESOLUTION_REVEAL

## Core lock

```text
SPECIFICATION_ID: SPEC-MEAS-001-ROUTE-D
TARGET_SCOPE: pytest #12112 namespace-package/importlib collection regression
REQUIREMENT_SOURCE_SET: issue body only
SELECTED_DSD_LAYERS: PROPERTY_CORE
DECLARED_DOWNSTREAM_TASK: behavior-level repair acceptance for the reported regression
```

`FORMATION_LAYER`, `STATIC_AGGREGATION_LAYER`, and `DYNAMICS_LAYER` are not activated because the locked task does not require formation semantics, aggregation, or temporal transition/lineage.

## Requirement atoms

### D1 — collection restoration

```text
REQUIREMENT_ID: D1
SOURCE_REFERENCE: reported 8.0.2 success vs 8.1.1 zero-collected/two-error regression
TARGET_ENTITY_OR_CARRIER: pytest collection/run behavior for the supplied namespace layout
REQUIREMENT_TYPE: behavioral acceptance
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: reported two-distribution namespace layout under the relevant configuration
REQUIRED_STRUCTURE_OR_VALUE: intended tests collect/run instead of failing collection with ModuleNotFoundError
VIOLATION_CONDITION: the reproduced layout still fails collection in the reported failure family
UNRESOLVED_CONDITION: later resolution artifacts do not establish behavior for the reported layout
```

### D2 — package-relative import identity

```text
REQUIREMENT_ID: D2
SOURCE_REFERENCE: `.foo` / `.bar` relative imports and observed `No module named 'test.foo'` / `'test.bar'`
TARGET_ENTITY_OR_CARRIER: imported test/helper module identity
REQUIREMENT_TYPE: identity/scoping acceptance
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: collection/import of the reported `ns/test` packages
REQUIRED_STRUCTURE_OR_VALUE: each relative import resolves within its intended package-local identity rather than collapsing to unrelated/ambiguous top-level `test.*`
VIOLATION_CONDITION: the same identity collapse or equivalent cross-package misresolution remains
UNRESOLVED_CONDITION: actual repair does not expose enough behavior to determine identity preservation
```

### D3 — importlib-mode boundary

```text
REQUIREMENT_ID: D3
SOURCE_REFERENCE: working 8.0.2 and failing 8.1.1 commands use `--import-mode=importlib`
TARGET_ENTITY_OR_CARRIER: repaired execution configuration
REQUIREMENT_TYPE: configuration-bound acceptance
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: reported issue reproduction
REQUIRED_STRUCTURE_OR_VALUE: repair remains valid for the reported importlib-mode path
VIOLATION_CONDITION: closure requires replacing the task with another import mode
UNRESOLVED_CONDITION: later artifacts do not establish importlib-mode behavior
```

### D4 — namespace-package option boundary

```text
REQUIREMENT_ID: D4
SOURCE_REFERENCE: failing 8.1.1 command explicitly supplies `consider_namespace_packages=true`
TARGET_ENTITY_OR_CARRIER: namespace-package collection configuration
REQUIREMENT_TYPE: conditional configuration acceptance
REQUIRED_OR_OPTIONAL: required for the locked reproducer
ACTIVATION_CONDITION: the reported 8.1.1 reproduction with `consider_namespace_packages=true`
REQUIRED_STRUCTURE_OR_VALUE: repaired behavior handles the option consistently with correct namespace-package collection/import identity
VIOLATION_CONDITION: the option is silently bypassed while only an unrelated configuration is repaired
UNRESOLVED_CONDITION: later artifacts leave the option's repaired behavior unclear
DEPENDENCIES: D1, D2, D3
```

### D5 — regression coverage

```text
REQUIREMENT_ID: D5
SOURCE_REFERENCE: supplied public reproducer with two packages under the same namespace and overlapping `ns/test` package names
TARGET_ENTITY_OR_CARRIER: repair verification
REQUIREMENT_TYPE: regression-evidence acceptance
REQUIRED_OR_OPTIONAL: required for the benchmark acceptance comparison
ACTIVATION_CONDITION: a code repair is used to close the issue
REQUIRED_STRUCTURE_OR_VALUE: test coverage materially represents the reported namespace/import identity failure family under relevant configuration
VIOLATION_CONDITION: repair closes the issue with no materially corresponding regression coverage in revealed artifacts
UNRESOLVED_CONDITION: test artifacts are unavailable
```

### D6 — implementation freedom

```text
REQUIREMENT_ID: D6
SOURCE_REFERENCE: issue body reports behavior and reproducer but no maintainer root cause or mandatory patch architecture
TARGET_ENTITY_OR_CARRIER: this DSD acceptance record
REQUIREMENT_TYPE: anti-overprediction constraint
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always active
REQUIRED_STRUCTURE_OR_VALUE: leave internal algorithm, path construction, cache/data structure, module-name derivation, and exact patch open
VIOLATION_CONDITION: frozen record claims unsupported prior knowledge of the actual implementation fix
UNRESOLVED_CONDITION: none
```

## Guardrails

```text
G1 SOURCE_FIDELITY: active
G2 PURPOSE_AND_PRIORITY_FIDELITY: active at narrow bug-repair acceptance scope
G3 DETAIL_PROPORTIONALITY: active
G4 VIEWPOINT_SEPARATION: active
VIEWPOINT_CHANGE_DECLARED: yes
DERIVATIVE_VIEW_LABEL: DSD v1.0 acceptance representation
```

No source-openness/downstream-determinacy ledger is activated because the issue gives a sufficiently determinate behavior-level reproducer for this task.

## Frozen claim limits

```text
PREDICTED_ROOT_CAUSE: no
PREDICTED_INTERNAL_ALGORITHM: no
PREDICTED_EXACT_PATCH: no
PREDICTED_MAINTAINER_DIAGNOSIS: no
```

```text
FINAL_SPEC_STATUS: usable
HARD_FAILURES: none
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
```
