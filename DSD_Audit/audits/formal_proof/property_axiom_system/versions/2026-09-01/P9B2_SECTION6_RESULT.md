# PA-P9B2-20260901-SECTION6-12-ITEMS-001 — complete Section 6 itemwise audit

**Manuscript:** Kwon Dominicus, `DSD_Property_Axiom_System_EN(4).pdf` (English; printed 2026.09.01; PDF 23 pp; **SHA256** `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`).
**Executed:** 2026-10-23 KST. **Prospective preregistration:** [P9B2_SECTION6_PRECOMMIT.md](P9B2_SECTION6_PRECOMMIT.md), commit `14a2fca9e8dfd11c507a7721e229f0440a767ebb`, frozen before this source-by-source review.
**Pages consulted:** PDF pp12–14 (printed p12–14), fixed Stage-VI and `S_L^{prop}` throughout §6. Original document/source code/Zenodo unchanged.

## Itemwise audit of all twelve original Section 6 numbered headings

| Heading | Exact logical dependency checked | Source-bound verdict |
| --- | --- | --- |
| **Definition 6.1 (Forward property map)** | Source auxiliary sort maps required only on A-available sorts, F1 availability inclusion; F2 declaration inclusion; F3 induced product on **all** `varpi∈Pi_A` as literally written; F4 prerequisite preservation; F5 defined assignment/value preservation. But Def2.5 permits `varpi∈Pi_A` with its profile unavailable, so product `X_A,varpi`, `Ap_A,varpi` and `Xi_A,varpi` need not exist. | **TYPING_SCOPE_GAP_CONFIRMED**: F3–F5 need source-declared **and available** guard; F4/F5 require matching bound `varpi`. |
| **Proposition 6.2 (Category of property models)** | Identity and coordinatewise composition of (F1,F2) and guarded (F3–F5): for `x∈D_A,varpi`, successive maps preserve domain and source value identically; images of `Ap` and each `Sat_d` compose by inclusion. On declared-unavailable models, literal unguarded F3 is undefined, so theorem cannot claim a completely defined category of *all* admitted full cores as written without clarifying Def6.1. | **SUPPORTED_CONDITIONALLY / SOURCE_TYPED_GAP_INHERITED**. |
| **Definition 6.3 (Property embedding)** | All available source auxiliary carrier maps injective and each fully typed source input reflects applicability, each prerequisite satisfaction and assignment domain. The prose `for every source input x∈X_A,varpi` also requires source declared and profile available. | **TYPING_SCOPE_CLARIFICATION_REQUIRED**, coherence otherwise supported. |
| **Proposition 6.4 (Wide embedding subcategory)** | Identity injective; injectivity and membership iff reflection compose; (F5) value equality follows along assignments. Target extra kinds never need be reflected into A. | **SUPPORTED_CONDITIONALLY** on correctly typed 6.1/6.3 definitions. |
| **Definition 6.5 (Inclusion submodel)** | Inclusions of supplied auxiliary carriers and declaration sets; property embedding under inclusion. No implicit converse of declaration inclusion. | **WELL_TYPED_WITH_PRIOR_SCOPE_GUARD**. |
| **Theorem 6.6 (Property-submodel preorder)** | Reflexive inclusion and transitive composite of embeddings; cannot infer antisymmetry or equality from two inclusions without separate hypotheses. | **SUPPORTED_CONDITIONALLY**. |
| **Definition 6.7 (Strict core property isomorphism)** | Explicit S1 each auxiliary carrier bijective, S2 available auxiliary-sort sets equal, S3 declared property-kind sets equal, S4 inverse comparisons. This is stronger than F1/F2 + componentwise bijective maps. | **STRUCTURALLY_SOUND_DEFINITION** given guarded embedding. |
| **Theorem 6.8 (Strict equivalence is equivalence relation)** | Identity: S1–S4; inverse: declared/available sets equal and reflected primitive relations and values; composition: equality of declaration/available-sort sets and biconditional preservation composes. But “Equivalently, ... exactly the bijective property embeddings” cannot mean merely all component carrier maps bijective. P9A's legal 53-core family has 347 carrierwise-bijective embeddings vs 53 strict S1–S4 comparisons; 294 fail strict. | **EQUIVALENCE PROOF SUPPORTED UNDER S1–S4; “BIJECTIVE EMBEDDING” SHORTCUT FALSE ON NATURAL CARRIERWISE READING**. Clarify term and retain theorem's first sentence. |
| **Proposition 6.9 (Strict preserves completion)** | Under S1–S4, declared kinds and type availability match; status depends only on transported `Ap`, `Sat_d`, `D`, values; intersections commute with bijections and full typed records `(varpi,x,z)` map to `(varpi,phi_varpi(x),z)`. | **SUPPORTED_IN_STRICT_SCOPE**, not for arbitrary forward maps. |
| **Definition 6.10 (Representation-preserving lift)** | Requires same representation signature, matching active labels `J_A=J_B`, bijection between selected record tuple domains `Y_A,j` and `Y_B,j`, equality `Enc_B,j(Phi^(n_j)(y))=Enc_A,j(y)`. Does not follow from core isomorphism automatically. | **WELL_TYPED_DEFINITION_WITH_EXPLICIT_EXTRA_BRIDGE**. |
| **Theorem 6.11 (Representation-inclusive strict equivalence)** | Identity from full package equality; inverse of core isomorphism and matched encoding equation; composition of record tuple bijections transports encoding equality. | **SUPPORTED_IN_DECLARED_SCOPE**. |
| **Remark 6.12 (Abstract vs represented comparison)** | Core strict equivalence may hold despite different optional representation data; represented strict equivalence strictly imposes more constraints. | **INTERPRETATION_SUPPORTED**; no automatic matrix/tensor semantics claimed. |

**Coverage:** `SECTION6_REVIEWED=12/12`; cumulative original source-numbered items under structured audit `P9B1 26 + P9B2 12 = 38/56`. This does NOT establish exhaustive automated general proof for all 38.

## Concrete mathematical challenges and qualifications

### Problem A — literal product map undefined in legal full core
Fix any Stage VI background and shared property signature with auxiliary sort u and unary property kind varpi. Let A declare varpi but not supply u. Definition 2.5 explicitly permits this, and no `X_A,varpi` is available. Both primitive soundness axioms are vacuous on unavailable profiles, and C1 completes the core. Nonetheless unguarded Def6.1 F3 asks to form `phi_varpi:X_A,varpi→X_A,varpi` on the **identity** of A. That product does not exist. Treat this as an ill-typed quantifier, NOT as evidence that the two soundness axioms are inconsistent.

### Problem B — componentwise bijection does not ensure strict isomorphism
Two valid one-point auxiliary carrier models A,B with matching carrier map `id_{ {x} }`, but `Pi_A=∅` and `Pi_B={varpi}`, have a source-to-target forward embedding with bijective carrier map and vacuous source property clauses. They fail S3 and cannot be strict. Likewise equality of declared kinds without equal availability does not make all the inverse-map data possible. **The term “bijective property embedding” must either be formally strengthened to include S2/S3 and inverse data, or not be used as the bare characterization.**

### Repair-independent arguments which survive
- Strict isomorphisms under **full** conditions S1–S4: closure under identity/inverse/composition and strict-equivalence relation. Their definition itself did not fail.
- Completion transport is formal because C1 is definitional, provided the primitive data really are transported/reflectable.
- Representation-preserving equivalence is well defined given its **separately supplied** encoding data and selected record domains.
- Inclusion submodel is only a **preorder**, not claimed to be a partial order in the original theorem.

## Execution and limitations

The already existing separate [P9A finite checker](scripts/verify_p9a_finite_morphisms.py) was independently validated in [GitHub Actions #39897341069](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39897341069) with Python 3.10 and 3.12, JSON comparison successful (53 models, 2,809 pairs, 148,877 triple-composition checks). P9B2 is additional **manual source-proof review**; do not claim a newly executed distinct multi-sort verifier.

All twelve numbered headings remain numbered identically. No original author text, old proof audits or experiment code was edited.

```text
CASE: PA-P9B2-20260901-SECTION6-12-ITEMS-001
SECTION6_ORIGINAL_ITEMS_REVIEWED: 12/12
CUMULATIVE_ITEMWISE_REVIEW: 38/56
FORWARD_MAP_ALL_DECLARED_KINDS_PROFILE_UNAVAILABLE: SOURCE_TYPING_GAP_CONFIRMED
BIJECTIVE_EMBEDDING_EQ_STRICT_S1_S4_AS_STATED: INCOMPLETE/FALSE_WITH_COMPONENTWISE_READING
STRICT_EQUIVALENCE_S1_S4_RELATION: SUPPORTED_CONDITIONALLY
SUBMODEL_PREORDER_AND_REPRESENTATION_EQUIVALENCE: SUPPORTED_CONDITIONALLY
NO_NEW_THIRD_FATAL_CONTRADICTION: true
MATHEMATICAL_GENERAL_MACHINE_PROOF: not_claimed
FULL_PROPERTY_FPA: OPEN
NEXT: PA-P9B3-20260901-SECTION7-6-ITEMS-001 / NOT_EXECUTED
```
