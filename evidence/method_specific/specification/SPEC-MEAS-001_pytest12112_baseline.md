# SPEC-MEAS-001 — ROUTE_B Strong Plain-Language Acceptance Checklist

Date: 2026-09-08
Source: `pytest-dev/pytest#12112` issue body only
Status: FROZEN_BEFORE_MAINTAINER_RESOLUTION_REVEAL

## Acceptance checklist

B1. Under the reported project layout with two installed packages in namespace `ns`, pytest should again collect and run the intended tests rather than fail collection with `ModuleNotFoundError`.

B2. With `--import-mode=importlib`, the relative imports in `python/foo/ns/test/test_foo.py` and `python/bar/ns/test/test_bar.py` should resolve to their intended package-local helper modules, not collapse to an unrelated or ambiguous top-level `test.foo` / `test.bar` identity.

B3. The repair must preserve compatibility with the issue's reported `--import-mode=importlib` execution path; replacing the task with a different import mode is not sufficient closure of the reported regression.

B4. The reported `consider_namespace_packages=true` configuration must be handled consistently with the repaired namespace-package collection behavior. The repair should not merely ignore the option while satisfying an unrelated layout.

B5. A repair should include regression coverage representing the reported failure family: multiple distributions sharing a namespace, overlapping `ns/test` package naming, package-local relative imports, and successful collection/execution under the relevant import configuration.

B6. The checklist does not prescribe the internal pytest algorithm, import-path construction, cache/data structure, module-name derivation, or exact patch. Any implementation is acceptable if it satisfies B1-B5 without introducing an unsupported new requirement.

## Limits

This baseline is intentionally strong. It is a source-derived conventional acceptance checklist, not a strawman. It does not use DSD field names, DSD layers, source-openness ledgers, or method-family handoff semantics.
