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

- [`SC-03_explicit-bridge-discipline.md`](SC-03_explicit-bridge-discipline.md) — **Explicit Bridge Discipline / 명시적 브리지 규율** — `promoted_with_conditions` (2026-09-06)
  - 8 higher-level fields, one representative method per field;
  - bridge-omission perturbation: 8/8 detected;
  - name/coordinate-inference perturbation: 8/8 detected;
  - bridge-substitution sensitivity: 8/8 detected;
  - identity/locked-map/invariance negative control: pass;
  - does not directly validate all 22 methods.

- [`SC-04_minimum-layer-optional-interface-restraint.md`](SC-04_minimum-layer-optional-interface-restraint.md) — **Minimum-Layer / Optional-Interface Restraint / 최소 층위·선택 인터페이스 절제** — `promoted_with_conditions` (2026-09-06)
  - 8 higher-level fields, one representative method per field;
  - required-layer deletion: 8/8 detected;
  - optional-layer overconstraint: 8/8 detected;
  - irrelevant-extension contamination: 8/8 detected;
  - multi-claim/secondary-output harmless-extension negative control: pass;
  - minimality is only inclusion-minimal relative to the locked layer inventory;
  - does not directly validate all 22 methods.

- [`SC-05_aggregate-information-loss-reconstruction-restraint.md`](SC-05_aggregate-information-loss-reconstruction-restraint.md) — **Aggregate / Information-Loss / Reconstruction Restraint / 집계·정보손실·복원 절제** — `promoted_with_conditions` (2026-09-06)
  - 8 higher-level fields, one representative method per field;
  - aggregate-equality inflation: 8/8 detected;
  - reconstruction without injectivity: 8/8 detected;
  - loss-boundary erasure: 8/8 detected;
  - injectivity/reduced-claim/support-sidecar negative control: pass;
  - does not directly validate all 22 methods.

- [`SC-06_transition-lineage-discipline.md`](SC-06_transition-lineage-discipline.md) — **Transition / Lineage Discipline / 전이·계보 규율** — `promoted_with_conditions` (2026-09-06)
  - 8 higher-level fields, one representative method per field;
  - transition-as-regular-evolution: 8/8 detected;
  - lineage omission/invention: 8/8 detected;
  - lineage coherence/type violation: 8/8 detected;
  - fixed-background canonical lineage and coherent branching/merging negative control: pass;
  - does not directly validate all 22 methods.

- [`SC-07_evidence-scope-case-origin-separation.md`](SC-07_evidence-scope-case-origin-separation.md) — **Evidence Scope / Case-Origin Separation / 증거 적용범위·사례 출처 분리** — `promoted_with_conditions` (2026-09-06)
  - 8 higher-level fields, one representative method per field;
  - scope inflation/direct-target erasure: 8/8 detected;
  - origin-class conflation: 8/8 detected;
  - origin-to-validation substitution: 8/8 detected;
  - method-specific real-world and shared constructed-case negative controls: pass;
  - no new real-world case is asserted by this synthetic metadata pilot;
  - does not directly validate all 22 methods.

- [`SC-08_baseline-failure-no-gain-anti-post-hoc-discipline.md`](SC-08_baseline-failure-no-gain-anti-post-hoc-discipline.md) — **Baseline / Failure-NO_GAIN / Anti-Post-Hoc Discipline / 기준선·실패·무이득·사후변경 방지 규율** — `promoted_with_conditions` (2026-09-06)
  - 8 higher-level fields, one representative method per field;
  - strawman-baseline substitution: 8/8 detected;
  - negative-result rescue/erasure: 8/8 detected;
  - post-reveal criterion/exception editing: 8/8 detected;
  - descriptive/exploratory/versioned-revision negative controls: pass;
  - baseline clause is conditional on comparative/gain/performance claims;
  - does not directly validate all 22 methods.

- [`SC-09_evidence-status-object-status-separation.md`](SC-09_evidence-status-object-status-separation.md) — **Evidence-Status / DSD-Object-Status Separation / 증거상태·DSD 객체상태 분리** — `promoted_with_conditions` (2026-09-06)
  - 8 higher-level fields, one representative method per field;
  - evidence-to-object coercion: 8/8 detected;
  - object-to-evidence coercion: 8/8 detected;
  - coupled-update contamination: 8/8 detected;
  - two-axis status-pair negative controls: pass;
  - evidence vocabulary may be domain-richer; the shared rule requires axis separation rather than one universal evidence ontology;
  - does not directly validate all 22 methods.

## Shared rule families / 공통 규율군

- **status / typed-domain discipline**: absence, undefinedness, inapplicability, prerequisite failure, defined zero, and complete typed input remain distinct when the selected interface and claim require those distinctions; intentional coarsening requires an explicit map and loss boundary;
- **source / interface / version lock**: lock every source, interface branch, and revision whose semantics can affect the claimed result; unused layers may be recorded as `not used`, and a documented equivalence class may replace an exact revision only after interface-level equivalence is established;
- **explicit bridge discipline**: cross-layer, cross-representation, cross-carrier, and cross-domain mappings require explicit source/target carriers, mapping rules, assumptions, and preservation/loss obligations unless the locked interface already supplies the relevant map or bridge-invariance has been proved;
- **minimum-layer / optional-interface restraint**: keep every layer needed by a claim, but do not make claim-irrelevant optional interfaces mandatory or let irrelevant extensions alter the core result merely by being present;
- **aggregate / information-loss / reconstruction restraint**: equal reduced aggregates do not imply equal support, decomposition, provenance, component state, or history unless the reduction is proved injective on the relevant admissible class or sufficient reconstruction side information is retained;
- **transition / lineage discipline**: keep identity-preserving regular evolution separate from identity-breaking transitions, and require typed, coherent lineage for successor/history claims whenever literal identity is not retained;
- **evidence scope / case-origin separation**: record what a record directly validates separately from whether its case is synthetic, constructed, real, judicial, historical, personal, empirical, or organizational/technical; case origin does not by itself broaden validation scope;
- **baseline / failure-NO_GAIN / anti-post-hoc discipline**: where comparison or confirmatory evaluation is claimed, use the strongest reasonable task-matched baseline available, preserve unfavorable/null/tied/indeterminate outcomes, and never silently rewrite locked criteria after reveal to rescue the same run;
- **evidence-status / DSD-object-status separation**: keep model/object status separate from evidence/audit status; evidence may assess a proposition about object status, but `unknown/insufficient/out-of-scope` is not an object status and `undefined/inapplicable/zero/absent` is not an evidence grade;
- specialization restraint: removing optional specialization withdraws specialization-dependent claims without inventing defaults; separate duplication audit still required to decide whether this deserves its own shared-core ID or is already covered by SC-01 and SC-04.

## Required record fields

```text
EVIDENCE_SCOPE_CLASS: shared_method_family / method_specific
METHOD_DIRECTLY_TESTED:
SHARED_RULES_SUPPORTED:
METHODS_NOT_DIRECTLY_VALIDATED:
TRANSFER_LIMIT:
CASE_ORIGIN:
REPRODUCIBILITY_RECORD:
```

When SC-09 is active, preserve separate `DSD_OBJECT_STATUS` and `EVIDENCE_STATUS` fields plus the claim/evidence relation between them.

For comparison/confirmatory records that activate SC-08, also preserve the relevant baseline, failure/no-gain criteria, precommit status, and post-reveal revision fields.

A shared rule should later be re-tested inside each method whose task interface materially changes how that rule operates.

## Promotion rule / 승격 규칙

A shared candidate is promoted only when its semantic obligation remains stable across independent method tasks, a collapse/removal test shows why the distinction matters, and explicit non-transfer conditions prevent overgeneralization.

Promotion of a shared rule is evidence for the **rule**, not automatic validation of every method that may later receive it.
