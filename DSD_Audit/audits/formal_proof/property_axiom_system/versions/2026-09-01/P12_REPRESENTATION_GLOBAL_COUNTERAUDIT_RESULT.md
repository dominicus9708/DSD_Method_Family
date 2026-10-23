# PA-P12 — representation and aggregation reverse audit (2026-10-23)

**Original:** Kwon Dominicus, `DSD_Property_Axiom_System_EN(4).pdf`, 2026.09.01, 23 pages, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`. Prospective obligations: [P12 precommit](P12_REPRESENTATION_AND_GLOBAL_COUNTERAUDIT_PRECOMMIT.md). This is a non-edit, source-bound mathematical review.

## 1. Representation-preserving strict equivalence

The original Definition 5.4 supplies active labels `J_A`, selected record-tuple sets `Y_A,j`, and encodings `Enc_A,j:Y_A,j→E_L,j` for a shared signature with fixed positive arity `n_j`. Definition 6.10 additionally requires equal active labels, bijective transport of selected tuple domains, and encoding equality under the induced core strict-isomorphism map.

For a strict core isomorphism `Phi`, the induced map on defined property records is bijective by C1; its coordinatewise extension to tuples respects identity, inverse, and composition for every positive arity. Under Definition 6.10's *separately required* active-label, domain, and encoding conditions, identity/inverse/composition make representation-inclusive strict equivalence an equivalence relation (Theorem 6.11), provided the underlying core S1–S4 category is well typed under the P11 guard G.

**Core strict equivalence alone does not imply that the additional representation conditions are met.** A label active with empty selected domain differs from an inactive label, although the encoding equation on an empty domain is vacuous. Repeated defined records in a tuple and mixed property labels are permitted by the fixed tuple arity and selected-domain definition.

## 2. External aggregation: limits of implication

The source §9.2 permits application-supplied finite selected records and bridge `Theta_A:G_A→U`. Neither this external bridge nor a chosen aggregation operator is forced to commute with a core isomorphism by the Property axioms.

Three statements must be kept separate:
- Strict core equivalence does **not** imply equality of independently selected aggregate outputs without a bridge compatibility/equivariance requirement.
- Equality of aggregate outputs does **not** imply strict property equivalence without injectivity or a reconstruction theorem.
- An equivariant bridge and an aggregation operation invariant under the corresponding finite-support permutation **can** preserve aggregate equality under strict core isomorphism; the converse is not implied.

Theorem 9.2's source-specific *existential* summary-collision counterexample remains valid. The §9.2 sentence about aggregate equality being “weaker” is defensible as an information-loss statement, but it should not be expanded into an unconditional implication ordering for arbitrary different external bridges. Mark as a scope note, not a new primitive axiom problem.

## 3. Executed finite negative controls

New code: [P12 independent Python](scripts/verify_p12_representation_aggregate.py). [Results JSON](results/p12_representation_aggregate.json).

Actual [initial GitHub Actions #39951975171](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39951975171): Python 3.10 and 3.12 produced identical **14/14 passed** JSON cases. The actual outputs were parsed from each job log and archived unchanged.

Actual [archive-replay GitHub Actions #39952098406](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39952098406): Python 3.12 job `120408777553` and Python 3.10 job `120408777986` completed success; both printed `P12 archived JSON matches fresh computation`. Script SHA256 `fa5ef8c2b5e293775fff0b580360a9afd6f30098ab6e699742cad809139aaff4`; fresh output SHA256 `201d26f90f55ca8829392504effdca5959b6d908cceb246b8d8db236981314c9`.

The checks cover representation identity/inverse/composition across transported strict cores, repeated records and mixed labels, altered encoding, mismatched selected domain, changed active label, empty and inactive packages, mismatched arbitrary external bridge outputs on the same core, equal bridge outputs on non-isomorphic finite two-kind cores, and a positive example under a deliberately equivariant bridge. This is **14 finite test cases, not a universal mechanical proof**.

## 4. Independent boundary arguments

**Locally small categories:** under a fixed set-sized property signature, component maps between two set-coded models form a set-indexed product of ordinary function sets. Morphisms satisfying F1–F5 form a subset and hence a set (locally small), although the class of all models with unrestricted auxiliary carrier sizes may be proper. This agrees with the manuscript's “possibly large category,” subject to P11's guarded Definition 6.1.

**Inverse strict embedding:** under P11 guard G, full Definition 6.3 reflection, bijective source carrier maps, identical availability-sort sets S2 and declaration sets S3 imply the inverse also preserves/refects primitive coordinates and defined values. Empty-but-available products are genuinely empty typed products; declared-but-unavailable profiles yield no primitive coordinates in either direction. Consequently S4 can be derived in this conditional setting, but retaining S4 explicitly is consistent and does not validate an unconditional “componentwise bijective embedding equals strict” shorthand.

## 5. Manuscript dependency verdict

| Item | Verdict |
| --- | --- |
| Definition 5.4, Definition 6.10 | WELL-TYPED within declared representation signatures |
| Theorem 6.11 representation-inclusive equivalence | SUPPORTED under explicit lift and correctly typed core isomorphism |
| §9.2 aggregate hierarchy prose | SCOPE NOTE; arbitrary external bridges need compatibility |
| Theorem 11.1(6) and literal Definition 6.1 | CONDITION_MISSING for declared/unavailable source profiles |
| Theorem 11.1(7) and Theorem 6.8 shorthand | CONDITION_MISSING for S2/S3 under componentwise bijection |
| Theorem 11.1(8–9) | SUPPORTED conditionally on correct strict core S1–S4 comparison |
| Primitive Axioms I/II and Closure C1 | No new counterexample detected in this P12 review |

No third independent fundamental contradiction was found here. **This is not proof that none exists.** No PDF, LaTeX, Zenodo or original experimental Python was modified.

```text
P12_REPRESENTATION_EQUIVALENCE: SUPPORTED_CONDITIONAL_ON_CORE_G
P12_FINITE_CASES: 14/14 PASS
P12_GITHUB_PYTHON_3_10_3_12: SUCCESS / ARCHIVED_JSON_MATCH
P12_AGGREGATE_IMPLIES_CORE_ISO: FALSE_WITHOUT_RECONSTRUCTION
P12_CORE_ISO_IMPLIES_ARBITRARY_AGGREGATE_EQUAL: FALSE_WITHOUT_EQUIVARIANCE
P12_SECTION6_EXISTING_TWO_GAPS: OPEN
P12_UNIVERSAL_MACHINE_FORMALIZATION: NOT_PERFORMED
FULL_PROPERTY_FPA: OPEN
SOURCE_EDITED: no
NEXT: PA-P13-20260901-GLOBAL-REVERSE-AUDIT-001
```
