# PA-P17-20260901-INDEPENDENT-TYPED-REFERENCE-VALIDATOR-001 — prospective independent validation gate

**STATUS: NOT_EXECUTED AT REGISTRATION**, 2026-10-24 KST.
Author/source: Kwon Dominicus, `DSD_Property_Axiom_System_EN(4).pdf`, 23 pp, printed 2026.09.01, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
Previous non-edit P16 [source-to-implementation audit](P16_TYPED_PREMODEL_VALIDATION_RESULT.md) executed **22 expected-positive/negative checks** successfully in Python 3.10 and 3.12 on original unchanged source, with archived JSON equality; the original implementation is a finite witness generator and is not a comprehensive typed-premodel validator.

## Required source-independent P17 obligations

1. Define a **reference typed signature** independently of `PropertySpec`: shared inherited-sort universe + fixed Stage-VI inherited carriers, auxiliary-sort universe, `hat Pi_L` candidate kind set, finite nonempty ordered property input profiles (m>=1), per-kind explicit set-coded value carrier `Z_L,varpi`, optional designated zero belonging to `Z`, finite prerequisite universe and per-kind prerequisite set.
2. Define a typed premodel validator with a supplied **partial** auxiliary-carrier interpretation and `Pi_A⊆hat Pi_L`. Differentiate **UNAVAILABLE** sorts from supplied but **EMPTY** carrier sets; never manufacture a product if its profile is unavailable.
3. For every declared, profile-available property, require typed primitive `Ap⊆X_A,varpi`, each `Sat_{varpi,d}⊆X_A,varpi`, and `Xi:X_A,varpi⇀Z_L,varpi`. Validate domain/codomain, partial function single-valuedness (when graph representation rather than Python dict is used), coordinate arity and exact type membership.
4. Identify and preserve distinct **kind-level statuses** for undeclared/profile-unavailable kinds; do not require undefined typed coordinates there. Separately **pre-register policy variants** for *surplus undeclared/unavailable metadata*: ignore as extraneous vs reject as malformed input. Do not decide this ambiguous paper convention by accident; report both rather than asserting source invalidity.
5. Show that soundness PI/PII are **additional checks only after typed-premodel validation**; distinguish invalid typed presentation, typed premodel failing PI/PII, and admitted full core. Reproduce and maintain original Countermodels 4.1 and 4.2 as legitimate typed *premodels*, not full models.
6. Build negative regression inputs for P16 observations: out-of-product application/satisfaction, wrong-length tuples, missing mandatory coordinates, wrong value carrier, unknown sort/kind/prerequisite, empty property profile, duplicate repeated-carrier data representation, duplicative declaration and metadata policy, inherited carrier participation, and C1 called before admission.
7. Differentially test **all original seven witness constructors** against the new reference validator without modifying `Property_Axiom_System/src/`, `tests/` or `results/`. If a mismatch arises, retain the original object and report whether the mathematical source requirement or the reference validator modeling is at fault; never "fix" original data to force passing.
8. New independent audit implementation should live under the **already established** `DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/scripts/` and `results/` paths, with exact GitHub CI run in Python 3.10 and 3.12 and archived JSON parity before any PASS.
9. No author manuscript/TeX/Zenodo edits or original experiment Python replacements. Keep known two printed Section-6 mathematical condition gaps and printed Theorem 4.3 C1-relative scope gate explicitly OPEN.

```text
CASE: PA-P17-20260901-INDEPENDENT-TYPED-REFERENCE-VALIDATOR-001
STATUS: NOT_STARTED / PREREGISTERED
SOURCE_EXACT_SHA256: 03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c
P16_22_EXPECTED_OBSERVATIONS: REPRODUCED
P16_GENERAL_ZFC_PROOF_FROM_PYTHON: NOT_CLAIMED
ORIGINAL_MANUSCRIPT_OR_EXPERIMENT_MODIFIED: NO
FULL_PROPERTY_FPA: OPEN
```
