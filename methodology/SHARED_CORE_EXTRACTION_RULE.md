# DSD Shared-Core Extraction Rule / DSD 공통 구조 추출 규칙

Status: **closed for current registry with conditions**
Date: 2026-09-06

This document governs the DSD Method Family stage that extracts structures genuinely reusable across methods **without merging the methods themselves**.

## 1. Core principle / 핵심 원칙

A common element belongs to the shared core only when its meaning and obligation remain stable across multiple receiving methods.

```text
shared operator or rule
!=
identical method
```

Method identity remains determined by task-specific inputs, operations, outputs, failure/no-gain criteria, and validation standards.

## 2. Extraction record / 추출 기록

Every proposed shared element should be recorded with:

```text
SHARED_CORE_ID:
NAME:
SOURCE_METHODS:
SOURCE_RECORDS:
DSD_LAYERS_USED:
INVARIANT_MEANING:
RECEIVING_METHODS:
TRANSFER_CONDITIONS:
NON_TRANSFER_CASES:
METHOD_SPECIFIC_INPUT_REMAINS:
METHOD_SPECIFIC_OPERATION_REMAINS:
METHOD_SPECIFIC_OUTPUT_REMAINS:
METHOD_SPECIFIC_FAILURE_CRITERIA_REMAINS:
METHOD_SPECIFIC_VALIDATION_REMAINS:
EVIDENCE_STATUS:
```

## 3. Current shared-core registry / 현재 공통 코어 레지스트리

The current promoted shared core is:

- **SC-01 status and typed-domain discipline** — promoted with conditions; see `../evidence/shared/SC-01_status-typed-domain-discipline.md`;
- **SC-02 source / interface / version lock** — promoted with conditions; see `../evidence/shared/SC-02_source-interface-version-lock.md`;
- **SC-03 explicit bridge discipline** — promoted with conditions; see `../evidence/shared/SC-03_explicit-bridge-discipline.md`;
- **SC-04 minimum-layer / optional-interface restraint** — promoted with conditions; see `../evidence/shared/SC-04_minimum-layer-optional-interface-restraint.md`;
- **SC-05 aggregate / information-loss / reconstruction restraint** — promoted with conditions; see `../evidence/shared/SC-05_aggregate-information-loss-reconstruction-restraint.md`;
- **SC-06 transition / lineage discipline** — promoted with conditions; see `../evidence/shared/SC-06_transition-lineage-discipline.md`;
- **SC-07 evidence scope / case-origin separation** — promoted with conditions; see `../evidence/shared/SC-07_evidence-scope-case-origin-separation.md`;
- **SC-08 baseline / failure-NO_GAIN / anti-post-hoc discipline** — promoted with conditions; see `../evidence/shared/SC-08_baseline-failure-no-gain-anti-post-hoc-discipline.md`;
- **SC-09 evidence-status / DSD-object-status separation** — promoted with conditions; see `../evidence/shared/SC-09_evidence-status-object-status-separation.md`;
- **SC-10 external-standard / domain-validation separation** — promoted with conditions; see `../evidence/shared/SC-10_external-standard-domain-validation-separation.md`.

The former specialization-restraint candidate was resolved by a separation/duplication audit as a **derived operational profile**, not a new independent shared-core rule. See `../evidence/shared/SPECIALIZATION_RESTRAINT_DUPLICATION_AUDIT.md`.

```text
SPECIALIZATION_RESTRAINT_PROFILE
  = SC-04 dependency/optionality discipline
  + SC-01 no-silent-status/default collapse
  + SC-03 explicit bridge when specialization affects another interface
```

The current closure result is recorded in `../evidence/shared/SHARED_CORE_CLOSURE_AUDIT.md`.

## 4. Promotion test / 공통 코어 승격 시험

A candidate becomes shared core only after all applicable questions are answered:

1. Does the rule have the same semantic meaning in at least two independent methods?
2. Does reusing it avoid changing either method's task definition?
3. Can a counterexample show when the rule is inapplicable rather than forcing it universally?
4. Is the rule supported by current DSD source layers or an explicit domain-independent operating requirement?
5. Are direct method validation claims kept separate from shared-rule support?

If these conditions are not met, the rule remains method-specific, a derived profile, a maturity requirement, or a conditional protocol module.

## 5. Evidence rule / 증거 규칙

Existing Analysis and Audit records can support a shared rule, but they do not directly validate another method.

```text
SOURCE_RECORD -> shared-rule support
shared-rule support -> candidate transfer
candidate transfer != method validation
```

Receiving methods must re-test the shared rule in their own task interfaces.

## 6. Relation to method boundaries / 방법 경계와의 관계

See [`../methods/METHOD_BOUNDARY_MATRIX.md`](../methods/METHOD_BOUNDARY_MATRIX.md).

If shared-core extraction makes two methods appear indistinguishable across all five method-boundary axes, the pair must be re-opened for a duplication audit. Otherwise shared infrastructure remains shared infrastructure, not a reason to merge methods.

Likewise, if two shared rules become indistinguishable across all five shared-rule closure axes — activation trigger, protected distinction/dependency, prohibited failure, required record/justification, and non-transfer condition — the pair must be re-opened for a shared-rule merge audit.

## 7. Development order / 개발 순서

The shared-core extraction sequence for the current registry is complete:

1. **SC-01 status and typed-domain discipline — completed: promoted_with_conditions**;
2. **SC-02 source / interface / version lock — completed: promoted_with_conditions**;
3. **SC-03 explicit bridge discipline — completed: promoted_with_conditions**;
4. **SC-04 minimum-layer / optional-interface restraint — completed: promoted_with_conditions**;
5. **SC-05 aggregate / information-loss / reconstruction restraint — completed: promoted_with_conditions**;
6. **SC-06 transition / lineage discipline — completed: promoted_with_conditions**;
7. **SC-07 evidence scope / case-origin separation — completed: promoted_with_conditions**;
8. **SC-08 baseline / failure-NO_GAIN / anti-post-hoc discipline — completed: promoted_with_conditions**;
9. **SC-09 evidence-status / DSD-object-status separation — completed: promoted_with_conditions**;
10. **specialization-restraint separation/duplication audit — completed: resolved_as_derived_profile**;
11. **shared-core closure gap: external-standard / domain-validation separation — resolved as SC-10**;
12. **shared-core closure audit — completed: closed_for_current_registry_with_conditions**.

Meta-audits do not receive an SC number unless they leave an independent reusable obligation.

## 8. Promotion registry / 승격 기록

### SC-01 — Status and Typed-Domain Discipline

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
STATUS_COLLAPSE_CHECKS: 8/8 detected
TYPED_DOMAIN_PROJECTION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Do not silently collapse claim-relevant status or complete typed-domain distinctions merely because they can be mapped to the same numerical or reduced representation.

Transfer conditions:

- the selected interface actually distinguishes the relevant status or typed coordinates;
- the claimed result depends, or may depend, on those distinctions;
- an intentional quotient/coarsening uses an explicit map and records its loss boundary.

Non-transfer case:

- a method does not use the relevant status-bearing interface; or
- an explicit quotient is part of the declared task, the claim is restricted to the quotient, and no recovery of discarded distinctions is asserted.

Evidence record: [`../evidence/shared/SC-01_status-typed-domain-discipline.md`](../evidence/shared/SC-01_status-typed-domain-discipline.md).

### SC-02 — Source / Interface / Version Lock

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
SOURCE_SUBSTITUTION_CHECKS: 8/8 detected
SEMANTIC_VERSION_DRIFT_CHECKS: 8/8 detected
INTERFACE_OMISSION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Lock every source, interface branch, and revision whose semantics can affect the claimed result. If exact revisions are replaced by a range or equivalence class, equivalence over the actually used interface must be established explicitly.

Transfer conditions:

- source-defined semantics, optional interfaces, or revisions can affect the method result;
- reproducibility, auditability, comparison, or historical traceability is claimed;
- downstream work inherits upstream definitions whose revision can change the interpretation.

Non-transfer/minimal-lock cases:

- unused downstream layers are explicitly recorded as `not used` and do not need to become dependencies;
- an exact revision may be replaced by a documented equivalence class only after equivalence on the used interface is shown.

Evidence record: [`../evidence/shared/SC-02_source-interface-version-lock.md`](../evidence/shared/SC-02_source-interface-version-lock.md).

### SC-03 — Explicit Bridge Discipline

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
BRIDGE_OMISSION_CHECKS: 8/8 detected
NAME_OR_COORDINATE_INFERENCE_CHECKS: 8/8 detected
BRIDGE_SUBSTITUTION_SENSITIVITY_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Do not infer a claim-relevant cross-layer, cross-representation, cross-carrier, or cross-domain correspondence from labels, raw values, or coordinate occurrence alone. Supply the map/relation and its assumptions explicitly unless the locked interface already does so or invariance across the admissible bridge class has been established.

Transfer conditions:

- the claim connects distinct DSD layers, representations, typed carriers, external domains, or method outputs;
- alternative admissible mappings could change ownership, support, coefficient, classification, ranking, diagnosis, or intervention;
- external-domain meaning is being supported from DSD structure.

Non-transfer/minimal-bridge cases:

- the operation remains inside the same typed carrier and uses a declared identity map;
- the locked interface already supplies the required structure-preserving map and the claim remains inside its stated preservation range;
- a separate invariance theorem proves the same result for every admissible bridge in the declared class.

Evidence record: [`../evidence/shared/SC-03_explicit-bridge-discipline.md`](../evidence/shared/SC-03_explicit-bridge-discipline.md).

### SC-04 — Minimum-Layer / Optional-Interface Restraint

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
REQUIRED_LAYER_DELETION_CHECKS: 8/8 detected
OPTIONAL_LAYER_OVERCONSTRAINT_CHECKS: 8/8 detected
IRRELEVANT_EXTENSION_CONTAMINATION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
MINIMALITY_SCOPE: inclusion-minimal_relative_to_locked_layer_inventory
```

Invariant meaning:

> Keep every DSD layer required to justify a claim, but do not make a claim-irrelevant optional interface or specialization a hidden prerequisite and do not let an irrelevant extension alter the core result merely because it is present.

Transfer conditions:

- the claim depends on one or more DSD source/interface layers;
- optional interfaces or specializations could be mistaken for mandatory prerequisites;
- several layers are used and their claim-specific roles need to remain explicit.

Non-transfer/minimal-layer cases:

- a single-interface task with no optional downstream interface does not need a long layer-selection protocol;
- a multi-claim task may use the union of the layers required by each declared claim;
- an extra layer may support a declared secondary output or sensitivity analysis while remaining explicitly non-required for the core claim;
- when the optional specialization itself is the target, it becomes a required dependency rather than an irrelevant extension.

Evidence record: [`../evidence/shared/SC-04_minimum-layer-optional-interface-restraint.md`](../evidence/shared/SC-04_minimum-layer-optional-interface-restraint.md).

### SC-05 — Aggregate / Information-Loss / Reconstruction Restraint

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
AGGREGATE_EQUALITY_INFLATION_CHECKS: 8/8 detected
RECONSTRUCTION_WITHOUT_INJECTIVITY_CHECKS: 8/8 detected
LOSS_BOUNDARY_ERASURE_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Equality of a reduced aggregate supports only distinctions proved to be preserved by the reduction. Reconstruction of support, decomposition, typed input, provenance, component state, or history requires injectivity/inverse data or sufficient support-retaining side information on the declared admissible class.

Transfer conditions:

- a method uses an aggregate, summary, compressed descriptor, reduced readout, or another potentially many-to-one representation;
- downstream claims attempt to recover structure that may have been discarded;
- a reduced result is reused as a cache key, identity criterion, provenance token, or reconstruction input.

Non-transfer/reconstruction cases:

- the rule is inactive when no reduced/aggregate representation is used;
- claims confined to the aggregate itself need not retain unrelated support data;
- unique or partial reconstruction is allowed within the range covered by an explicit injectivity/inverse result and any required side information.

Evidence record: [`../evidence/shared/SC-05_aggregate-information-loss-reconstruction-restraint.md`](../evidence/shared/SC-05_aggregate-information-loss-reconstruction-restraint.md).

### SC-06 — Transition / Lineage Discipline

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
TRANSITION_AS_REGULAR_EVOLUTION_CHECKS: 8/8 detected
LINEAGE_OMISSION_OR_INVENTION_CHECKS: 8/8 detected
LINEAGE_COHERENCE_OR_TYPE_VIOLATION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Keep ordinary downstream evolution inside a regular epoch only while inherited Stage-VI identity and declared support typing remain valid. When literal identity is broken, record a transition and supply typed lineage for any successor/history claim; do not infer succession from labels, values, aggregate equality, or apparent continuity alone.

Transfer conditions:

- time/order-indexed work makes identity, persistence, succession, history, or successor claims;
- a change may invalidate Stage-VI identity, admitted support, or the regular support signature;
- pre/post objects need to remain connected without being treated as literally equal.

Non-transfer/minimal-lineage cases:

- purely static single-slice work does not activate SC-06;
- fixed-background regular evolution may use canonical identity lineage without a transition record;
- branching/merging is allowed when the relation is typed and coherent unless the task explicitly requires uniqueness.

Evidence record: [`../evidence/shared/SC-06_transition-lineage-discipline.md`](../evidence/shared/SC-06_transition-lineage-discipline.md).

### SC-07 — Evidence Scope / Case-Origin Separation

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
SCOPE_INFLATION_OR_TARGET_ERASURE_CHECKS: 8/8 detected
ORIGIN_CLASS_CONFLATION_CHECKS: 8/8 detected
ORIGIN_TO_VALIDATION_SUBSTITUTION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Record what an evidence item directly validates separately from what kind of case produced it. Real-world origin does not by itself broaden direct validation scope, and synthetic/constructed origin does not by itself prevent a record from supporting a shared operating rule.

Transfer conditions:

- an evidence record supports a method, shared rule, maturity claim, or real-world application;
- one record has both case-origin metadata and method-specific/shared applicability;
- reusable shared lessons are extracted from method-specific evidence without changing which method was directly tested.

Non-transfer/minimal-record cases:

- private scratch work not entered into the evidence corpus does not need the full schema;
- case origin may change source-verification, privacy, authority, or external-standard obligations without changing applicability scope;
- evidence scope may legitimately broaden only when the actual protocol and validation basis are broadened to test additional methods;
- no new judicial, historical, personal, empirical, or organizational case is claimed by the synthetic SC-07 pilot.

Evidence record: [`../evidence/shared/SC-07_evidence-scope-case-origin-separation.md`](../evidence/shared/SC-07_evidence-scope-case-origin-separation.md).

### SC-08 — Baseline / Failure-NO_GAIN / Anti-Post-Hoc Discipline

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
STRAWMAN_BASELINE_SUBSTITUTION_CHECKS: 8/8 detected
NEGATIVE_RESULT_RESCUE_OR_ERASURE_CHECKS: 8/8 detected
POST_REVEAL_CRITERION_OR_EXCEPTION_EDIT_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> When a method makes a comparative, superiority, gain, performance, or locked success claim, use the strongest reasonable task-matched baseline available within the declared comparison scope, preserve unfavorable/null/tied/indeterminate outcomes, and do not retroactively change locked criteria after reveal to rescue the same run. Revisions must be versioned and applied prospectively or through a separately recorded rerun.

Transfer conditions:

- a superiority, gain, novelty, performance, error-reduction, efficiency, or predictive-quality claim is made;
- PASS/FAIL/NO_GAIN/TIE/INDETERMINATE-style evaluative outcomes are recorded;
- criteria, thresholds, exclusions, predictions, or scoring rules can be fixed before reveal for confirmatory evidence;
- baseline choice could materially change the claimed advantage.

Non-transfer/conditional cases:

- a genuinely descriptive/non-comparative task does not require a competitive baseline merely to be valid;
- if no competent baseline exists, record that limitation rather than inventing a weak comparator;
- exploratory criteria may evolve after seeing data, but the exposed run is not retroactively confirmatory under the revised criteria;
- factual bugs or invalid inputs may justify a corrected protocol/version, while the original record remains preserved;
- genuine DSD superiority is allowed when a strong task-matched baseline and locked criteria support it.

Source support:

- `ANL-CH-003` — baseline sufficiency and `NO_GAIN` preservation;
- `ANL-CH-007` — strongest reasonable baseline and anti-strawman discipline;
- `ANL-CH-008` — rule-lock transfer and no silent post-reveal exception;
- `ANL-CH-009` — commit-before-reveal and prediction-miss preservation.

Evidence record: [`../evidence/shared/SC-08_baseline-failure-no-gain-anti-post-hoc-discipline.md`](../evidence/shared/SC-08_baseline-failure-no-gain-anti-post-hoc-discipline.md).

### SC-09 — Evidence-Status / DSD-Object-Status Separation

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
EVIDENCE_TO_OBJECT_COERCION_CHECKS: 8/8 detected
OBJECT_TO_EVIDENCE_COERCION_CHECKS: 8/8 detected
COUPLED_UPDATE_CONTAMINATION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Keep the DSD object/model status separate from the evidence/audit status of a claim about that object or its external application. Evidence may assess a proposition about object status, but evidence-status values and object-status values are not interchangeable categories.

Transfer conditions:

- a record contains a DSD Formation, Property, or Dynamics object/status distinction and an evidential/audit judgment about a claim involving that object;
- terms such as `undefined`, `inapplicable`, `absent`, or `zero` could be confused with `unknown`, `insufficient`, `unverified`, or `out of scope`;
- evidence changes may trigger reassessment or a new model revision, but the old object status must not be silently rewritten.

Non-transfer/minimal-record cases:

- purely formal object work with no evidential claim need not invent an evidence status;
- pure evidence/provenance work without a DSD object model need not invent a DSD object status;
- receiving domains may use richer evidence vocabularies; the shared obligation is axis separation, not one universal evidence ontology;
- an explicit new model revision may be triggered by new evidence, but the revision/update must be recorded rather than represented as automatic cross-axis coercion.

Source support:

- Property Axiom System — explicit object-side status ladder;
- Formation / Static / Dynamics — compatible preservation of undefined/zero/absence/status distinctions;
- DSD General Audit and Audit Automation Roadmap — evidence-status and object-status ledgers are explicitly separate.

Evidence record: [`../evidence/shared/SC-09_evidence-status-object-status-separation.md`](../evidence/shared/SC-09_evidence-status-object-status-separation.md).

### SC-10 — External-Standard / Domain-Validation Separation

```text
DATE: 2026-09-06
SOURCE_SUPPORT: pass
CROSS_FIELD_REPRESENTATIVE_METHODS: 8
STANDARD_OMISSION_CHECKS: 8/8 detected
DSD_TO_DOMAIN_SUBSTITUTION_CHECKS: 8/8 detected
WRONG_STANDARD_SUBSTITUTION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> A DSD-internal structural result and even an explicit domain bridge do not by themselves replace the receiving domain's own proof, empirical, professional, interpretive, legal, ethical, safety, or other task-relevant validation standard. Domain-level claims must retain the applicable external standard unless an independent equivalence result legitimately identifies the standards over the declared claim class.

Transfer conditions:

- a DSD method output is used to support a claim about an external domain;
- the receiving domain has a distinct proof, authority, empirical, professional, interpretive, ethical, safety, or acceptance standard relevant to the claim;
- DSD-internal success could be mistaken for the domain verdict itself.

Non-transfer/minimal-standard cases:

- the claim is explicitly DSD-internal and makes no external-domain truth/authority assertion;
- the task record already supplies and separately applies the receiving domain standard;
- a legitimate theorem, calibration, institutional rule, or equivalent basis proves that the DSD-side criterion is equivalent to the domain standard on the declared class;
- DSD is used to organize evidence/assumptions while the actual domain verdict remains assigned to the domain standard.

Source support:

- `DSD_METHOD_FAMILY_FRAMEWORK.md` domain-bridge rule;
- `METHOD_BOUNDARY_MATRIX.md` retention of `VALIDATION_STANDARD` as a method-boundary axis;
- Simulation/Prediction distinction requiring domain validation for prediction beyond model consistency.

Evidence record: [`../evidence/shared/SC-10_external-standard-domain-validation-separation.md`](../evidence/shared/SC-10_external-standard-domain-validation-separation.md).

## 9. Specialization-restraint separation / duplication audit / 특수화 절제 분리·중복 감사

The former specialization-restraint candidate was decomposed into five obligations: optionality, core survival, dependent-claim withdrawal, no fake default, and no undeclared feedback.

```text
CANDIDATE_OBLIGATIONS: 5
OBLIGATIONS_COVERED_BY_EXISTING_SHARED_CORE: 5/5
PRIMARY_COVERAGE: SC-04
STATUS_DEFAULT_COVERAGE: SC-01 + SC-04
CROSS_INTERFACE_FEEDBACK_COVERAGE: SC-03
UNIQUE_INVARIANT_REMAINDER: none
UNIQUE_FAILURE_CRITERION_REMAINDER: none
UNIQUE_TRANSFER_CONDITION_REMAINDER: none
NEW_SPECIALIZATION_SC_CREATED: no
RESULT: resolved_as_derived_profile
```

Four optional structures were checked against the same coverage logic: realized-axis geometry, Property optional representation, Static countable extension, and the one-channel local-scaling / `D_w` specialization. In each case, predecessor/core survival and dependent-claim withdrawal are already SC-04 obligations; fake-default prohibition is jointly covered by SC-01 and SC-04; any claimed cross-interface feedback requires SC-03.

The existing `ANL-CH-006` challenge remains valid Analysis-specific evidence and is not rewritten. Its reusable lessons are cross-referenced into the existing shared core rather than promoted as a duplicate rule.

Meta-audit record: [`../evidence/shared/SPECIALIZATION_RESTRAINT_DUPLICATION_AUDIT.md`](../evidence/shared/SPECIALIZATION_RESTRAINT_DUPLICATION_AUDIT.md).

## 10. Relations among the promoted rules / 승격 규율 관계

```text
SC-01 = preserve claim-relevant distinctions inside the selected DSD status/type space
SC-02 = lock the semantics that determine which rules/interfaces are active
SC-03 = explicitly supply claim-relevant mappings between active structures
SC-04 = keep only claim-relevant layers as dependencies and avoid optional-interface overconstraint
SC-05 = do not infer beyond the information-preservation/reconstruction capacity of reduced aggregates
SC-06 = separate identity-preserving evolution from identity-breaking transition and use lineage for succession
SC-07 = keep evidence applicability separate from case origin/reality status
SC-08 = protect evaluation integrity from weak-baseline selection, unfavorable-result erasure, and retroactive criterion changes
SC-09 = keep evidence/audit status separate from DSD object/model status
SC-10 = keep receiving-domain validation standards separate from DSD-internal structural success
```

## 11. Closure status / 종료 상태

The closure audit reviewed all 45 unordered pairs among SC-01 through SC-10 and found no exact duplicate shared rules.

```text
SHARED_CORE_RULES_PROMOTED: 10
PAIRWISE_RULE_PAIRS_REVIEWED: 45
EXACT_SHARED_RULE_DUPLICATES: 0
HIGHER_FIELDS_WITH_REPRESENTATIVE_TRANSFER_COVERAGE: 8/8
RULES_WITH_ACTIVATION_AND_NON_TRANSFER_CONDITIONS: 10/10
DIRECT_METHOD_VALIDATION_SEPARATION: pass
FRAMEWORK_SEMANTIC_GAPS_UNRESOLVED: 0
RESULT: closed_for_current_registry_with_conditions
```

`REPRODUCIBILITY_RECORD` remains a method/evidence maturity requirement rather than a new shared semantic-core ID because its concrete rerun/retrace validation differs materially by method.

Method identity/boundary remains meta-architecture rather than a shared operator. Symmetry/equivariance, holdout/transfer, resolution sensitivity, and robustness remain conditional challenge/protocol modules rather than universal shared-core obligations.

Closure record: [`../evidence/shared/SHARED_CORE_CLOSURE_AUDIT.md`](../evidence/shared/SHARED_CORE_CLOSURE_AUDIT.md).

### Reopening conditions

Reopen shared-core extraction only when at least one of the following occurs:

1. a DSD source revision changes the semantics of a promoted rule;
2. a new independent DSD method exposes a stable obligation not expressible by SC-01 through SC-10;
3. a future specialization violates the current derived-profile decomposition;
4. two methods or two shared rules become indistinguishable under their respective boundary tests;
5. a maturity requirement such as reproducibility is later formalized into a stable domain-independent DSD operating invariant.

Until then, development should proceed to **method-specific protocols, evidence, and real-world application cases**, not continued proliferation of shared-core labels.
