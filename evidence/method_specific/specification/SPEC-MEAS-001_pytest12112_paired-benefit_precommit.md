# SPEC-MEAS-001 — pytest #12112 Paired Practical-Benefit Benchmark Precommit

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Status: PRECOMMITTED_BEFORE_MAINTAINER_RESOLUTION_REVEAL
Case source: `pytest-dev/pytest` issue #12112
Benchmark type: paired source-derived acceptance representations

## 1. Goal

Measure whether DSD Specification v1.0 provides a practical acceptance-structuring advantage over a **strong conventional plain-language acceptance checklist** when both are built from the same real issue report before maintainer comments, PRs, patches, or closing resolution are inspected.

This benchmark does not compare DSD against a deliberately weak baseline.

## 2. Locked source boundary

Before both representations are frozen, the evaluator may inspect only the issue body and coarse metadata of `pytest-dev/pytest#12112`.

Do not inspect until both representations are committed:

```text
issue comments
linked PRs
commits
patches
maintainer diagnosis
closing rationale
regression tests added by the fix
```

Model prior knowledge cannot be excluded, so this is not a full blind test.

## 3. Locked source facts

```text
F1  The report concerns a regression in pytest 8.1.1 for a namespace-package layout containing two installed packages under namespace `ns`.
F2  Each package contains a same-named `ns/test` package with its own local helper module and test module.
F3  In pytest 8.0.2, `python -m pytest --import-mode=importlib` from the top-level example works.
F4  In pytest 8.1.1, `--import-mode=importlib -o consider_namespace_packages=true` collects zero tests and raises two import errors.
F5  The observed imports fail as `No module named 'test.bar'` and `No module named 'test.foo'` rather than resolving the intended package-local relatives.
F6  The issue provides a public reproducer repository and installation/run procedure.
```

No maintainer root cause or implementation fix is treated as known.

## 4. Paired representations

Two frozen artifacts will be produced before reveal:

```text
ROUTE_B  strong conventional plain-language acceptance checklist
ROUTE_D  DSD Specification v1.0 typed acceptance record
```

Both routes receive exactly the same issue-body source facts and downstream task.

Declared downstream task:

> State the behavior-level conditions that a repair should satisfy for the reported namespace-package/importlib collection regression, while avoiding unsupported implementation guesses.

## 5. Frozen comparison axes

Both representations will be scored against the later maintainer resolution using the same axes:

```text
A1_REPRO_LAYOUT_COLLECTION_RESTORED
  the reported two-distribution namespace layout can be collected/run again under the relevant configuration

A2_RELATIVE_IMPORT_PACKAGE_IDENTITY_PRESERVED
  `.foo` and `.bar` resolve within their intended package identity rather than collapsing to an unrelated/top-level `test` identity

A3_IMPORTLIB_MODE_COMPATIBILITY_PRESERVED
  the repair remains compatible with the reported `--import-mode=importlib` use

A4_NAMESPACE_PACKAGE_OPTION_BOUNDARY_PRESERVED
  the role/boundary of `consider_namespace_packages=true` is handled rather than silently ignored or replaced by an unrelated requirement

A5_DIRECT_REGRESSION_TEST_FAMILY
  the actual repair includes or updates regression coverage materially representing this namespace/import identity failure family

A6_IMPLEMENTATION_FREEDOM_PRESERVED
  the frozen representation does not require a specific internal algorithm, module path rewrite, data structure, or exact code patch unsupported by the issue body
```

Allowed axis results:

```text
MATCH
PARTIAL_MATCH
NON_MATCH
UNRESOLVED
NOT_APPLICABLE
```

## 6. Measurement metrics

For each route record:

```text
FULL_MATCH_AXES
PARTIAL_MATCH_AXES
NON_MATCH_AXES
UNRESOLVED_AXES
UNSUPPORTED_REQUIREMENT_COUNT
IMPLEMENTATION_OVERPREDICTION_COUNT
SOURCE_FACT_INVENTION_COUNT
POST_REVEAL_REQUIREMENT_CHANGE
REPRESENTATION_CHARACTER_COUNT
REPRESENTATION_REQUIREMENT_COUNT
```

Character count is UTF-8 text character count of the frozen representation body as stored in its benchmark artifact, excluding repository metadata outside the file.

The character metric is only a representation-burden proxy. It is not human review time.

## 7. Comparative verdict rule

```text
DSD_MEASURED_CASE_GAIN
  DSD has materially better locked-axis coverage or fewer unsupported/overpredicted obligations without a disproportionate representation burden.

MIXED_CASE_RESULT
  DSD improves at least one material correctness/traceability axis but adds measurable burden or loses another material axis.

TIE_WITH_DSD_OVERHEAD
  both routes have equivalent material outcome coverage/error profile, while DSD requires materially more representation.

BASELINE_PREFERRED_FOR_LOCKED_TASK
  the baseline is materially better on coverage/error/burden for this task.

UNRESOLVED
  later artifacts do not support a fair comparison.
```

No threshold is retroactively changed after reveal.

## 8. Guardrails

```text
G1 SOURCE_FIDELITY: active
G2 PURPOSE_AND_PRIORITY_FIDELITY: active at bug-repair acceptance scope
G3 DETAIL_PROPORTIONALITY: active
G4 VIEWPOINT_SEPARATION: active for DSD derivative record
```

## 9. Evidence limit

This is a same-evaluator paired benchmark. It may establish a **measured case-level representation/coverage result**, but it does not establish independent evaluator agreement, general engineering productivity, or universal DSD superiority.
