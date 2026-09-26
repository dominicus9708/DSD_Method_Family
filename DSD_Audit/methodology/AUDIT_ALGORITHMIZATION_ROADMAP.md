# DSD Audit Algorithmization Roadmap / DSD 감사 알고리즘화 로드맵

Status: **planning document**
Baseline date: **2026-09-05**

This document is the implementation roadmap for turning the manual DSD Audit records into a reproducible software-assisted audit pipeline.
It does not reduce domain validity to one universal algorithm.

## 1. Three-layer separation / 3층 분리

```text
A. mechanically checkable record integrity
B. semi-automatic DSD structural audit
C. external-domain judgment
```

A common program may enforce A strongly and assist B. C remains governed by field-specific standards unless a dedicated checker is explicitly supplied.

## 2. Stable input schema / 안정 입력 스키마

```text
record_identity
interface_lock
scope_lock
source_preservation
evidence_status
object_status
selection_exclusion
bridge_declarations
transition_ledger
lineage_records
alternatives
aggregation_reconstruction
witness_counterexample
contradiction_audit
verdict
reproducibility
revision_migration
```

Optional conditional groups for materially multi-step cases:

```text
claim_requirement_relation
dependency_frontier
representation_relation
escalation_information_loss
branch_state_reopen
gain_set
```

These optional groups are not required for every audit.

## 3. Phase 0 — manual structure stabilization / 수동 구조 안정화

1. Apply the separated DSD Audit template to mathematics, science, software/algorithm, and at least one non-technical domain.
2. Track fields that are repeatedly unused, ambiguous, or missing.
3. Keep research-line-specific fields out of the common schema unless the same need recurs independently.
4. Preserve failed mappings and cases where DSD adds no useful distinction.
5. Version every interface migration.

Exit condition: the common record schema remains stable across heterogeneous audits.

## 4. Phase 1 — static schema validator / 정적 스키마 검사기

Potential deterministic checks:

- missing record identifiers
- missing DSD interface/source locks when a DSD layer is used
- evidence status and DSD object status conflation
- absent/undefined/inapplicable states serialized as defined zero without declared coarsening
- missing selector or bridge declarations
- unsupported reconstruction from reduced data
- formation-level identity change recorded without lineage or justification
- revision that erases a previous verdict

Output should be validation messages and traceable warnings, not truth verdicts.

## 5. Phase 2 — DSD structural rule engine / DSD 구조 규칙 엔진

Potential rules:

```text
undefined -> zero                       [warn unless justified]
absent channel -> zero-valued channel   [warn]
inapplicable -> defined false/zero       [warn]
profile unavailable -> inapplicable      [warn]
same aggregate -> same support           [warn without injectivity]
same summary -> strict equivalence        [warn without proof]
identity change -> same literal channel   [warn without lineage]
```

Additional candidate warning rules for materially multi-step cases:

```text
stronger sufficient -> necessary                  [warn without implication basis]
weaker requirement -> sufficient                  [warn without bridge/argument]
incomparable axes -> scalar total order            [warn without ordering rule]
OR alternative -> mandatory AND prerequisite       [warn]
attack method -> theorem/domain gate                [warn]
established-equivalent obligations -> double count [warn]
shared parent -> representation equivalence         [warn without preservation proof]
one-way bound -> equivalence                        [warn]
material claim-strength escalation -> unrecorded   [warn]
claim-relevant information loss -> unrecorded      [warn]
frozen branch -> false/impossible                   [warn]
supporting/exploratory work -> direct closure      [warn]
```

Bridge rules should flag multi-input property allocation without selectors, property-to-dynamic coefficient use without constitutive bridges, and optional specialization treated as universal core.

## 6. Phase 3 — domain adapters / 분야별 어댑터

- Mathematics: theorem lock, proof-step graph, finite-computation boundary, counterexample metadata.
- Science: observation/model separation, uncertainty, dataset provenance, constitutive assumptions, reproducibility.
- Software: executable environment, tests, branch/state trace, deterministic or seeded execution.
- Law/institutions: source-time information state, authority, burden/standard, evidence/norm separation.

Domain verdict and DSD structural audit verdict remain separate.

## 7. Phase 4 — reproducible pipeline / 재현 실행 파이프라인

```text
SOURCE LOCK
-> INTERFACE LOCK
-> SCOPE / CLAIM-REQUIREMENT RELATION        [conditional]
-> TYPE/STATUS VALIDATION
-> SELECTION/EXCLUSION CHECK
-> DEPENDENCY / FRONTIER CHECK               [conditional]
-> BRIDGE CHECK
-> REPRESENTATION-RELATION CHECK             [conditional]
-> TRANSITION/LINEAGE CHECK
-> ESCALATION / INFORMATION-LOSS CHECK       [conditional]
-> ALTERNATIVE/WITNESS CHECK
-> AGGREGATION/RECONSTRUCTION CHECK
-> CONTRADICTION CHECK
-> MAXIMUM-SUPPORTED-CLAIM CHECK
-> DOMAIN VERDICT + DSD AUDIT VERDICT
```

Every generated warning or verdict component should preserve an audit trace back to the input field and rule that produced it.

## 8. Default non-automation boundary / 기본 자동화 금지 영역

The common engine must not decide by itself:

- whether an unproved mathematical proposition is true
- whether an empirical constitutive model is physically correct
- whether a legal norm is authoritative or correctly interpreted
- whether a policy value judgment is normatively preferable
- whether one historical interpretation is uniquely correct when sources do not establish uniqueness

## 9. Test fixtures / 시험 fixture

```text
valid minimal audit
missing interface lock
undefined-zero conflation
absent-channel zero extension
undeclared-property misuse
missing multi-input selector
missing dynamic constitutive bridge
aggregate collision
unsupported reconstruction
formation-level identity change without lineage
finite computation overclaimed as proof
post-hoc exclusion
```

Include fixtures whose correct status is `UNDETERMINED` or `NOT_APPLICABLE`.

## 10. Implementation gate / 구현 시작 조건

Begin a full rule engine only after:

1. the shared DSD interface profile is sufficiently stable;
2. repeated fields have consistent meanings;
3. several independent domains can use the same core fields;
4. mechanical checks can be separated from domain judgment;
5. legacy migration rules are documented and exercised.
