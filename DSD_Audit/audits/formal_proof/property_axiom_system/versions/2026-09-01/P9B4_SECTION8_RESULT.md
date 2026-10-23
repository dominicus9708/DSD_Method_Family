# PA-P9B4-20260901-SECTION8-8-ITEMS-001 — existence and finite construction audit

**Executed 2026-10-23 KST**. Source author **Kwon Dominicus**; `DSD_Property_Axiom_System_EN(4).pdf`, printed 2026.09.01, 23 pp, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`, inspected pp16–17.
**Precommit:** [P9B4_SECTION8_PRECOMMIT.md](P9B4_SECTION8_PRECOMMIT.md), commit `658caba3db980882b4a78d32f72c795b25087e5d`. This is a manual mathematical/finite-witness source audit, not an automated ZFC proof.

## Eight original item reviews

| Original heading | Exact source conditions and verification | Verdict |
| --- | --- | --- |
| **Theorem 8.1, Trivial extension** | On any fixed Stage-VI record and any shared typed property signature, choose no auxiliary sorts supplied and `Π_A=∅`, so there are no active `Ap`, `Sat` or `Xi`. PI/PII hold vacuously; C1 unique completion relative to this primitive core. Inherited carriers remain given, not erased. | **EXISTENCE_PROOF_SUPPORTED**. |
| **Construction 8.2, One-input nontrivial model** | Conditional existence of auxiliary sort u and unary kind `varpi` with nonempty value carrier and chosen `z∈Z_varpi`. `X_A(u)={x}`, `Π_A={varpi}`, `Ap={x}`, each `Sat_d={x}`, `Xi(x)=z`. `DomXi={x}⊆Ap∩DepSat`; if `δ(varpi)=∅`, empty-intersection rule gives `DepSat=X_A,varpi={x}`. | **FINITE_WITNESS_VALID_UNDER_STATED_SIGNATURE_EXISTENCE**. |
| **Definition 8.3, Finite primitive property data** | `property-finite` tests supplied auxiliary carriers, declared set, applicability, prerequisite-satisfied and assignment domains. Does not require external value carrier `Z` to be finite. Inherited Stage-VI carriers might also be infinite, so do **not** infer all typed product carriers or all possible status-input universes are finite. | **WELL_TYPED_DEFINITION_WITH_FINITE_GRAIN_BOUNDARY**. |
| **Theorem 8.4, Standard finite realization** | Finite compatible primitive data, actual typed partial `Xi` values, and both soundness axioms via `DomXi⊆Ap∩DepSat` for every *declared profile-available kind* give a primitive core. C1 yields exactly one **completed model over these fixed inputs**. Does not claim uniqueness of primitive data on a shared Stage-VI base. | **PROOF_SUPPORTED_IN_COMPATIBLE_FINITE_DATA_SCOPE**. |
| **Construction 8.5, Stage-2 declaration branch** | Same one-point carrier, source declared `Π_A={varpi}`, target undeclared, so an auxiliary carrier bijection exists at P1, but declaration equality impossible at P2. `b_prop=2`. | **FINITE_WITNESS_VALID**. |
| **Construction 8.6, Stage-3 applicability branch** | Both same `{a,b}`, two unary property labels with no prerequisites and empty `Xi`. For kind `varpi_1`, `Ap_A={a}=Ap_B` forces a↦a and b↦b. For kind `varpi_2`, `Ap_A={a}`, `Ap_B={b}` forces a↦b, incompatible. Full two-permutation check: identity matches kind 1, fails kind 2; swap fails kind 1, matches kind 2. Thus `I2≠∅,I3=∅, b_prop=3`. | **FINITE_ALL_BIJECTIONS_CHECKED / VALID**. |
| **Construction 8.7, Stage-4 assignment branch** | `{a,b}`, two zero-bearing kinds, value `{0,1}`, no prerequisites, full applicability; both primitive axioms hold. `varpi_1` values (0,1) in both A and B force identity as a Stage-4 candidate; `varpi_2` is (0,1) in A vs (1,0) in B, which fails under identity; swap already fails `varpi_1`. Thus `I3≠∅,I4=∅,b_prop=4`. These same two cores furnish the §9.2 summary collision. | **FINITE_ALL_BIJECTIONS_CHECKED / VALID**. |
| **Corollary 8.8, No independent Stage-5 witness** | `I4=I5` for all full models by Prop7.2 and unique C1. Hence no full pair with `I4≠∅,I5=∅`. | **PROOF_SUPPORTED_FROM_C1**. |

## Explicit additional mathematics and guards

- For §8.6 and §8.7 the two possible bijections on a two-point carrier were **both** evaluated at the necessary first-failure step; a single failed coordinate map was not mistaken for emptiness of the entire comparison set.
- `Property-finite` measures **primitive supplied information**, not finiteness of an inherited universal Stage-VI sort. A finite construction can have finite assigned/application support while other inherited carrier sorts remain infinite.
- Stage-4 witness §8.7 requires two *different* declared property kinds with retained labels (no unintended interchange of `varpi_1,varpi_2` under strict signature-fixed comparison). Source §7 requires preservation of property labels.
- Source §§8.1–8.4 do not force arbitrary property values, masses, line/axis geometry, totality or runtime evolution; these are not inferable from the existence constructions.
- Actual prior property experiment GitHub Actions [#39733865420](https://github.com/dominicus9708/Property_Axiom_System/actions/runs/39733865420), Python 3.10/3.12 7 unit tests each, also executed finite branch witnesses. P9B4 here is the separate direct manuscript argument check; neither implies fully mechanized universal proof.

```text
CASE: PA-P9B4-20260901-SECTION8-8-ITEMS-001
SECTION8_NUMBERED_ITEMS_REVIEWED: 8/8
CUMULATIVE_NUMBERED_ITEMS_SOURCE_REVIEWED: 52/56
TRIVIAL_AND_ONE_INPUT_EXISTENCE: SUPPORTED_IN_SCOPE
FINITE_GENERAL_REALIZATION: SUPPORTED_ON_COMPATIBLE_FINITE_PRIMITIVES
TWO_POINT_FIRST_BRANCHES_2_3_4: FINITE_WITNESSES_VALID
STAGE5_INDEPENDENT_BRANCH: IMPOSSIBLE_BY_C1
NEW_FATAL_CONTRADICTION_IN_SECTION8: none
ORIGINAL_PDF_TEX_MODIFIED: no
FPA_FULL: OPEN
NEXT: PA-P9B5-20260901-SECTION9-11-4-ITEMS-001 / NOT_STARTED
```
