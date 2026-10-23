# PA-P9B1-20260901-FIRST26-ITEMS-001 — detailed §2–§5 claim-by-claim audit

Kwon Dominicus. Reviewed 2026-10-23 KST. Locked original PDF `DSD_Property_Axiom_System_EN(4).pdf` (printed 2026.09.01, 23 pp), SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
Prospective preregistration: `P9B_FIRST26_PRECOMMIT.md`, commit `48db31c4f98689be24d77cab476c27ff0bd0e27f`.

**Source method:** each of the **first 26 numbered source items** is distinguished as either a *typed definition*, *conditional mathematical claim*, *counterinterpretation*, *theorem proof*, *corollary*, or *non-theorem remark*. Prior section-level P1–P4 report is used as corroboration but not counted as 26 independent machine proofs. This is a manual source-consistency and proof-dependency pass, not mechanized ZFC formalization.

## Exact 26-item source index and current audit

| Item | Role / condition actually checked | Verdict |
| --- | --- | --- |
| Definition 2.1 | Shared inherited/auxiliary sorts, finite nonempty ordered typed profiles, per-kind value carrier and optional zero, fixed prerequisites | TYPED_DEFINITION_SOUND |
| Remark 2.2 | Property label alone does not imply symmetry/geometry/dynamics | INTERPRETATION_SCOPE_SUPPORTED |
| Definition 2.3 | Partial supply of auxiliary carriers; absent sorts left genuinely unavailable, inherited sorts fixed | TYPED_DEFINITION_SOUND |
| Definition 2.4 | Product `X_A,varpi` exists only for available ordered input profile, not as default empty product for missing sorts | TYPED_DEFINITION_SOUND |
| Definition 2.5 | Premodel coordinates `Ap/Sat/Xi` required only for declared kinds with available profiles; typing does not enforce PI/PII | TYPED_DEFINITION_SOUND_WITH_SCOPE_NOTE |
| Definition 2.6 | Primitive core = typed premodel satisfying PI/PII; full model = C1-complete primitive core | DEFINITION_SOUND |
| Definition 2.7 | Cumulative stages P0..P5; P5 contains only derived coordinates; these are dependency stages, not time | TYPED_DEFINITION_SOUND |
| Definition 3.1 | `DepSat=∩Sat_d`; with zero prerequisites the intersection is the **full typed product** `X_A,varpi` | TYPED_DEFINITION_SOUND |
| Definition 3.2 | Assignment domain is `Dom(Xi)` only where source profile exists | TYPED_DEFINITION_SOUND |
| Definition 3.3 | Undeclared and unavailable kind-level; inapplicable / prereq-unsatisfied / applicable-undefined / defined input-level, assigned zero only when zero-bearing | TYPED_PARTITION_SOUND |
| Definition 3.4 | Record retains `(varpi,x,z)`; no implicit channel-index collapse or missing input tuple coordinate | TYPED_DEFINITION_SOUND |
| Remark 3.5 | Property `Xi` does not mutate predecessor Formation assignment, role, channel or trace | INTERFACE_SCOPE_SUPPORTED |
| Definition 3.6 | Reduction forgets precisely C1-derived coordinates, not primitive data or Stage-VI interface | DEFINITION_SOUND |
| Theorem 3.7 | Two-sided CompProp/RedProp inverse equality follows from functional definitions **relative to a fixed primitive core** | PROOF_SUPPORTED_IN_SCOPE |
| Remark 3.8 | No recursive fixed point or well-foundedness is demanded because `Sat_d` is primitive data | INTERPRETATION_SCOPE_SUPPORTED |
| Countermodel 4.1 | A one-point typed premodel falsifies PI only: `Ap=∅`, `Sat={x}`, `Xi(x)=1` | FINITE_COUNTERINTERPRETATION_VALID |
| Countermodel 4.2 | A one-point typed premodel falsifies PII only: `Ap={x}`, `Sat=∅`, `Xi(x)=1` | FINITE_COUNTERINTERPRETATION_VALID |
| Theorem 4.3 | Mutual nonderivability from two counterinterpretations against same background; distinct from full models satisfying both axioms | PROOF_SUPPORTED_WITH_C1_SCOPE_NOTE |
| Proposition 4.4 | Typed subset relations + partial function alone do not force either PI/PII: 4.1 and 4.2 are counterexamples | PROOF_SUPPORTED |
| Proposition 4.5 | Both converse implications fail with `Ap=DepSat={x}` and `Dom(Xi)=∅` | PROOF_SUPPORTED |
| Corollary 4.6 | Same full core from 4.5 has applicable, prerequisites satisfied, yet undefined input | PROOF_SUPPORTED |
| Definition 5.1 | Full core descriptor retains primitive and derived status-sensitive coordinates, not just numeric outputs | DEFINITION_SOUND |
| Remark 5.2 | Defined values insufficient to reconstruct declarations/availability/Ap/Sat distinctions | INTERPRETATION_SCOPE_SUPPORTED |
| Definition 5.3 | Optional representation signature `(J_L,n_j,E_{L,j})`, no compulsory activation | TYPED_DEFINITION_SOUND |
| Definition 5.4 | Package declares `J_A⊆J_L`, chooses `Y_{A,j}⊆(R_A^{prop})^{n_j}`, maps to externally supplied representation carrier | TYPED_DEFINITION_SOUND |
| Proposition 5.5 | Forgetting optional package leaves core unaffected; choose `J_A=∅` for core without active representation | PROOF_SUPPORTED |

**Count: 26/26 numbered items evaluated at this source-argument/typing level, 0 new direct fatal contradiction in this batch.** This is NOT 26/26 mechanically verified general theorems and does not override P5's actual category/strict-isomorphism typing problems in §6.

## Separate unnumbered requirements in §§3–4
- **PI:** `Dom(Xi)⊆Ap` for declared/profile-available kinds. Non-converse allowed.
- **PII:** `Dom(Xi)⊆DepSat` for declared/profile-available kinds. Non-converse allowed.
- **C1:** derived `Dom(Xi)`, intersections, statuses and defined records determined relative to admitted primitive cores.

These unnumbered items must not be miscounted as 56 numbered headings.

## Edge of this review: conservative C1 reading of the independence countermodels

Theorem 4.3 describes independence **“relative to ... Definitional Closure Clause C1”**, whereas the paper states Clause C1 “Given a primitive property core.” Countermodels 4.1 and 4.2 are **not primitive cores** because they intentionally falsify one axiom. The derived formulas `Dom(Xi)`, `DepSat`, status and records can nevertheless be applied to these well-typed *premodels* as a conservative definitional expansion, without requiring either soundness axiom. Therefore the non-derivability argument remains substantively valid **as an independence of primitive constraints relative to the typed premodel background, with the C1 *formulas* extendable outside the admitted full-model class**.

**Nonfatal explicit-scope note for any later source revision:** state that for logical independence the defining formulas of C1 are interpreted on the well-typed counterinterpretations despite those intentionally not being full models. Do not incorrectly claim either countermodel is a valid full property model.

Definition 2.5 says unused coordinates are “not required” for undeclared or profile-unavailable kinds. The intended primitive descriptor uses only relevant coordinates. If a reader interprets optional surplus unused coordinates as part of `Apre`, whether the strict descriptor preserves them is not specified. This is a *low-priority presentation completeness question*, not a disproved theorem; do not impose extra axioms merely to resolve it.

## Consequences for progress

- No source edits made, no existing experimental Python code changed.
- **P9A** separate declared-unavailable finite checker supplies strong additional evidence for §6 scope gaps; see [P9A full result](P9A_FINITE_MORPHISM_EXHAUSTIVE_RESULT.md) and GitHub Actions `39897341069`.
- Remaining **30 numbered source headings** belong to §§6–9 and §11: 6.1–6.12 (12), 7.1–7.6 (6), 8.1–8.8 (8), 9.1–9.3 (3), 11.1 (1). Next audit should review first the **12 numbered §6 map/equivalence items** with special quantifier, surjectivity, unavailable-profile and extra-declaration cases. Only then carry the fixes' implications into §§7–11.
- Any original text modification remains separate and pending actual EN/KR LaTeX source verification.

```text
CASE: PA-P9B1-20260901-FIRST26-ITEMS-001
SOURCE_ITEMS_SEEN: 26/26 in §§2–§5
DIRECT_FATAL_CONTRADICTION_DISCOVERED_IN_BATCH: no
PROOF_LEVEL: manual scoped proof / typed-definition audit (not mechanized general ZFC)
C1_COUNTERMODEL_SCOPE_NOTE: OPEN_PRESENTATIONAL
FULL_56_ITEM_REVIEW: 26/56 at this audit granularity
NEXT: PA-P9B2-20260901-SECTION6-CLAIM-ROW-REVIEW-001
WHOLE_PROPERTY_FPA: OPEN
```
