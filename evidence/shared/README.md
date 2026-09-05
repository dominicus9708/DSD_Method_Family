# Shared Method-Family Evidence / 방법군 공통 규율 증거

This folder records evidence for **shared operating disciplines** that may be reused across multiple DSD methods.

It does **not** directly validate the correctness, performance, or usefulness of every method.

## Promoted shared-core records / 승격된 공통 구조 기록

- [`SC-01_status-typed-domain-discipline.md`](SC-01_status-typed-domain-discipline.md) — **Status and Typed-Domain Discipline / 상태·타입 도메인 규율** — `promoted_with_conditions` (2026-09-06)
  - 8 higher-level fields, one representative method per field;
  - status-collapse perturbation: 8/8 loss detected;
  - typed-input projection perturbation: 8/8 loss detected;
  - explicit quotient/status-map negative control: pass;
  - does not directly validate all 22 methods.

- [`SC-02_source-interface-version-lock.md`](SC-02_source-interface-version-lock.md) — **Source / Interface / Version Lock / 소스·인터페이스·버전 잠금** — `promoted_with_conditions` (2026-09-06)
  - 8 higher-level fields, one representative method per field;
  - source-substitution perturbation: 8/8 detected;
  - semantic-version-drift perturbation: 8/8 detected;
  - optional-interface-omission perturbation: 8/8 detected;
  - minimal/equivalence-class lock negative control: pass;
  - counterfactual `V*` is not asserted to be an actual historical DSD revision;
  - does not directly validate all 22 methods.

## Shared rule families / 공통 규율군

- **status / typed-domain discipline**: absence, undefinedness, inapplicability, prerequisite failure, defined zero, and complete typed input remain distinct when the selected interface and claim require those distinctions; intentional coarsening requires an explicit map and loss boundary;
- **source / interface / version lock**: lock every source, interface branch, and revision whose semantics can affect the claimed result; unused layers may be recorded as `not used`, and a documented equivalence class may replace an exact revision only after interface-level equivalence is established;
- bridge discipline: cross-layer and cross-domain mappings require explicit justification;
- minimum-layer discipline: use only the DSD layers required by the task;
- aggregate/reconstruction discipline: equal aggregate does not imply equal support, decomposition, cause, or history without a reconstruction basis;
- specialization restraint: removing optional specialization withdraws specialization-dependent claims without inventing defaults;
- failure / NO_GAIN preservation: negative, null, non-correspondence, and indeterminate results remain valid records;
- strongest-baseline discipline: comparison must not rely only on a weak strawman baseline;
- precommit / anti-post-hoc discipline: locked criteria or predictions are not silently rewritten after reveal.

## Required record fields

```text
EVIDENCE_SCOPE_CLASS: shared_method_family
SHARED_RULES_SUPPORTED:
SOURCE_RECORDS:
METHODS_DIRECTLY_TESTED:
METHODS_NOT_DIRECTLY_VALIDATED:
TRANSFER_LIMIT:
REPRODUCIBILITY_RECORD:
```

A shared rule should later be re-tested inside each method whose task interface materially changes how that rule operates.

## Promotion rule / 승격 규칙

A shared candidate is promoted only when its semantic obligation remains stable across independent method tasks, a collapse/removal test shows why the distinction matters, and explicit non-transfer conditions prevent overgeneralization.

Promotion of a shared rule is evidence for the **rule**, not automatic validation of every method that may later receive it.
