# Specialization-Restraint Separation / Duplication Audit / 특수화 절제 분리·중복 감사

Status: **resolved_as_derived_profile / no_new_SC_id**  
Date: 2026-09-06  
Evidence scope: `shared_method_family_meta_audit`  
Case origin: `source_interface_and_existing_challenge_audit`

## 1. Question / 감사 질문

Does the recurring rule

> removing an optional specialization should preserve predecessor/core claims, withdraw only specialization-dependent claims, and avoid fake defaults

contain an independent shared-core obligation not already represented by SC-01, SC-03, and SC-04?

The decision criterion is intentionally strict:

```text
NEW_SHARED_CORE_ID only if
  candidate has a stable invariant meaning
  AND at least one necessary failure criterion
  AND at least one transfer obligation
  that cannot be expressed without changing the meaning of existing promoted rules.
```

## 2. Source-supported optional modules / 소스상 선택 모듈

The current source set provides several genuinely optional structures rather than one isolated realized-axis example:

1. **Realized-axis specialization** — the Property core does not require axes, lines, rank, normals, or related geometry; Dynamics also treats realized-axis data as optional specialization coordinates.
2. **Property optional representation extension** — matrices, tensors, operators, graphs, and other encodings may be added downstream without becoming the abstract property core.
3. **Static countable extension** — absolutely summable countable aggregation is an optional extension and does not redefine the finite Formation-compatible core.
4. **One-channel local-scaling / `D_w` specialization** — metric-measure and local-scaling data are specialization data, not requirements on every DSD channel.

The earlier Analysis challenge `ANL-CH-006` already tested realized-axis removal and obtained an exact partition: independently supported Property/Dynamics claims survived, geometry-dependent claims were withdrawn, and no rank-zero or other fake default was introduced.

## 3. Candidate obligation decomposition / 후보 규율 분해

Specialization restraint can be decomposed into five operational obligations.

```text
SR1 OPTIONALITY:
  an optional specialization is not a hidden prerequisite for a claim that does not use it.

SR2 CORE SURVIVAL:
  removing a claim-irrelevant specialization must not change the predecessor/core result.

SR3 DEPENDENT-CLAIM WITHDRAWAL:
  if a claim actually needs the specialization, removing it removes support for that claim.

SR4 NO FAKE DEFAULT:
  missing specialization data are not replaced by rank=0, false, zero vector, empty geometry,
  or another defined value unless that default is separately declared by the model.

SR5 NO UNDECLARED FEEDBACK:
  specialization data do not alter independent core outputs merely by co-occurrence;
  if an application claims feedback/coupling, the relevant bridge/law must be explicit.
```

## 4. Coverage against promoted shared core / 기존 공통 코어와의 대응

| Candidate obligation | Existing shared rule | Coverage |
|---|---|---|
| `SR1` optionality | SC-04 Minimum-Layer / Optional-Interface Restraint | exact — SC-04 prohibits turning claim-irrelevant optional interfaces/specializations into hidden prerequisites |
| `SR2` core survival | SC-04 | exact — SC-04 requires core-result invariance under irrelevant optional extensions |
| `SR3` dependent-claim withdrawal | SC-04 | exact — a specialization becomes a required dependency when the claim targets it; deletion then makes that claim unsupported |
| `SR4` no fake default | SC-01 Status / Typed-Domain Discipline + SC-04 omission semantics | exact jointly — unavailable/not supplied is not silently collapsed into a defined zero/false/default |
| `SR5` no undeclared feedback | SC-04 + SC-03 Explicit Bridge Discipline | exact jointly — irrelevant specialization must not contaminate core results; a genuine cross-interface effect requires an explicit bridge/law |

Result:

```text
CANDIDATE_OBLIGATIONS: 5
OBLIGATIONS_COVERED_BY_EXISTING_SHARED_CORE: 5/5
UNIQUE_INVARIANT_REMAINDER: none
UNIQUE_FAILURE_CRITERION_REMAINDER: none
UNIQUE_TRANSFER_CONDITION_REMAINDER: none
```

## 5. Cross-specialization removal checks / 특수화별 제거 검사

### A. Realized-axis geometry

Remove `G` while keeping the general Property/Dynamics predecessor data fixed.

Expected under existing rules:

```text
core property/dynamic claims survive                -> SC-04
rank/orthogonality/normal claims become unavailable -> SC-04
no rank=0 or false default                          -> SC-01 + SC-04
no core change from geometry removal alone          -> SC-04
explicit coupling, if claimed                       -> SC-03
```

No new obligation remains.

### B. Optional Property representation

Remove a supplied matrix/tensor/graph representation while keeping the abstract complete property descriptor fixed.

Expected:

```text
abstract property status/typed data survive         -> SC-04
representation-dependent equivalence/readout claims withdraw -> SC-04
missing representation is not a zero matrix         -> SC-01 + SC-04
```

No new obligation remains.

### C. Optional countable Static extension

Remove the absolutely summable countable extension while keeping the finite core.

Expected:

```text
finite Formation-compatible aggregation survives    -> SC-04
claims about the removed countable extension withdraw -> SC-04
absence of extension is not a zero infinite sum object -> SC-01 + SC-04
```

No new obligation remains.

### D. `D_w` local-scaling specialization

Remove metric-measure/local-scaling specialization data while keeping the general channel-indexed analytic interface.

Expected:

```text
general analytic component realization survives     -> SC-04
D_w/local-scaling-specific claims withdraw           -> SC-04
missing local-scaling field is not alpha=0           -> SC-01 + SC-04
```

No new obligation remains.

## 6. Independence test / 독립성 시험

Three independence questions were applied.

```text
Q1. Remove the candidate name "specialization restraint".
    Can all valid/invalid cases still be classified by promoted rules?
    RESULT: yes

Q2. Is there a counterexample that violates specialization restraint
    while satisfying SC-01, SC-03, and SC-04 as currently defined?
    RESULT: none found within the locked source interfaces and candidate vocabulary

Q3. Would creating SC-10 add a new input, operation, output,
    failure criterion, or validation obligation?
    RESULT: no; it would restate a composite use-profile of existing rules
```

Therefore the candidate fails the non-duplication threshold for a new shared-core ID.

## 7. Verdict / 판정

```text
SPECIALIZATION_RESTRAINT_INDEPENDENCE: not_independent
DUPLICATION_WITH_EXISTING_SHARED_CORE: yes
PRIMARY_COVERAGE: SC-04
STATUS_DEFAULT_COVERAGE: SC-01
CROSS_INTERFACE_FEEDBACK_COVERAGE: SC-03
NEW_SC10_CREATED: no
RESULT: resolved_as_derived_profile
```

Canonical operational profile:

```text
SPECIALIZATION_RESTRAINT_PROFILE
  = SC-04 dependency/optionality discipline
  + SC-01 no-silent-status/default collapse
  + SC-03 explicit bridge when specialization affects another interface
```

This profile may be cited by name for convenience, but it is **not a tenth independent shared-core rule**.

## 8. Relation to ANL-CH-006 / 기존 특수화 제거 도전과의 관계

`ANL-CH-006` remains valid Analysis-specific evidence. Its useful result is not deleted or relabeled. Instead, its reusable lessons are now classified as support for the existing shared-core combination:

```text
CORE SURVIVAL                -> SC-04
SPECIALIZATION CLAIM WITHDRAWAL -> SC-04
NO DEFAULT SUBSTITUTION      -> SC-01 + SC-04
NO FEEDBACK / NO LEAKAGE     -> SC-04, with SC-03 when an actual bridge is claimed
```

Historical challenge records remain append-only.

## 9. Limits / 한계

- This is a duplication/separation audit, not a new direct validation of all 22 DSD methods.
- The audit uses the current Property, Static Aggregation, Dynamics interfaces and existing Analysis challenge evidence.
- The conclusion is scoped to the present shared-core definitions. If a future specialization introduces an obligation not expressible by SC-01/SC-03/SC-04, the independence question may be reopened under a new version.
- `none found` in the independence counterexample search is not a proof over every conceivable future DSD specialization; it is a closure decision for the current method-family registry.

## 10. Next step / 다음 단계

Proceed to the **shared-core closure audit**. That audit should check SC-01 through SC-09 for mutual duplication, coverage gaps across the eight higher-level fields, conditional-activation clarity, and continued separation between shared-rule evidence and direct method validation.
