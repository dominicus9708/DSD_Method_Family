# PA-P13-20260901-GLOBAL-REVERSE-AUDIT-001 — complete reverse dependency audit (no source edits)

**Reviewed:** 2026-10-23 KST. **Manuscript author:** Kwon Dominicus.
**Exact frozen source:** `DSD_Property_Axiom_System_EN(4).pdf`, printed 2026.09.01, 23 pages, 157854 bytes, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Prospective P13 precommit:** [P13_GLOBAL_REVERSE_AUDIT_PRECOMMIT.md](P13_GLOBAL_REVERSE_AUDIT_PRECOMMIT.md), commit `3a1e40b14c6f71650584bbaa291598c21394c2ba`.

**Evidence actually consulted:** the complete English PDF as uploaded; text of §§2–13 including abstract and appendices, visual layout inspection of printed pp13–14 and pp19–20, the prior individual 56-heading source-scope audit [P9B5](P9B5_SECTION9_11_RESULT.md), independent source algebra [P11](P11_GENERAL_MORPHISM_PROOF_RESULT.md), and [P12](P12_REPRESENTATION_GLOBAL_COUNTERAUDIT_RESULT.md) with real GitHub Actions [#39952098406](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39952098406). **No new Python rerun or machine-checked universal theorem was performed in P13 itself.**

## A. Reverse chain from the THIRTEEN distinct statements in source Theorem 11.1 (printed pp19–20)

| 11.1 item | Direct upstream premises and mathematical rationale | Audit status, for the literal source |
| --- | --- | --- |
| **(1)** Typed profiles, no universal axis | §2.2 Definition 2.1, §2.3–2.4 Definitions 2.3–2.5; finite ordered `sigma_L(varpi)`, disjoint inherited/auxiliary sorts | **SUPPORTED** (definitional). No assertion that axes cannot be additionally specialized. |
| **(2)** PI/PII soundness | §§3.1–3.2; `DomXi⊆Ap` and `DomXi⊆DepSat` for declared **profile-available** kinds | **SUPPORTED** in explicitly quantified domain. |
| **(3)** Independence beyond typing | Typed counterinterpretations 4.1/4.2, Theorem 4.3/Proposition 4.4 | **SUPPORTED_WITH_C1_SCOPE_NOTE**: counterinterpretations are *premodels*, not full cores; “relative to C1” requires applying the **defining formulas** beyond the class of cores that already satisfy both axioms. |
| **(4)** Distinct input statuses | Definition 3.3 and nonconverse Proposition 4.5/Corollary 4.6 | **SUPPORTED_WITH_ZERO_BEARING_SCOPE**: defined-zero/nonzero refinement only for kinds possessing a designated zero, not all value carriers. |
| **(5)** Unique explicit completion/reduction | Clause C1, Definition 3.6, Theorem 3.7 | **SUPPORTED_RELATIVE_TO_FIXED_PRIMITIVE_CORE**; does not assert unique choice of primitive data for fixed Formation Stage VI base. |
| **(6)** Forward category, wide embedding subcategory, preorder | Definitions 6.1,6.3,6.5; Propositions 6.2,6.4; Theorem 6.6 | **CONDITION_MISSING_IN_PRINTED_SOURCE**: the quantifier of F3–F5 and reflection must be restricted to **source declared AND profile available** kinds (guard G), else some existing legal objects lack a typed input product for even an identity map. Conditional general proofs in P11 are sound **with G**. |
| **(7)** Strict isomorphism “exactly bijective embeddings” and equivalence | Definition 6.7 (S1–S4), Theorem 6.8 | **SHORTCUT_CONDITION_MISSING**: componentwise carrier-bijective embeddings need not satisfy S2 equal available-sort sets nor S3 equal declaration sets. **Strict S1–S4 equivalence relation itself is supported** (with G), as P9A/P10 countermodels show the abbreviated characterization false under its natural carrierwise interpretation. |
| **(8)** Representation-preserving strict isomorphism is finer | Definitions 5.3–5.4 and 6.10; Theorem 6.11 | **SUPPORTED_CONDITIONAL_ON_VALID_CORE_STRICT_ISO** plus equal active representation labels, selected record-tuple bijection, encoding commutation. Original source already supplies the latter conditions. Bare core equivalence does NOT lift automatically. |
| **(9)** First-branch comparison symmetry/invariance, no independent P5 | Definition 7.1, Proposition 7.2, Corollary 7.3, Definition 7.4, Theorem 7.5 | **SUPPORTED_ON_STAGEWISE_STRICT_COMPARISON** using full S1–S4 (not abbreviated bijective embedding) and C1; indirect typing dependency on (6)/(7). |
| **(10)** Trivial property extension and finite realization | Theorems 8.1, 8.4, Definition 8.3 | **SUPPORTED_IN_TYPED_COMPATIBLE_FINITE_DATA_SCOPE**; finite primitive supplied data, not necessarily every inherited infinite carrier. Unique standard completion of **given** data, not uniqueness of all primitive presentations. |
| **(11)** Concrete first branches P2/P3/P4 | Constructions 8.5–8.7, Corollary 8.8 | **SUPPORTED_WITH_SHARED_SIGNATURE_PREMISES**; 2-element examples require two distinct named unary kinds, assignment-stage example zero-bearing values. All candidate bijections of the two-point carrier were considered. |
| **(12)** Simple summary equality fails to classify | Definition 9.1, Theorem 9.2, Construction 8.7 | **SUPPORTED_EXISTENTIAL_ONLY**: equality of fixed label-retaining triples need not imply strict property equivalence; not a statement about all possible sufficient summaries. |
| **(13)** Fixed Stage-VI Formation interface | §2.1, Remark 3.5, §10 and Conclusion | **SUPPORTED_AS_CONSTRUCTION_RULE**; property `Xi` does not change inherited formation assignments, role, channel identity or post-VI term/composition coordinates. Later interfaces are separately supplied. |

**Summary classification:** nine source items (1–5,10–13) are directly supported with explicit scope qualifications where needed; two items (6,7) inherit confirmed original Section-6 **condition issues**; two (8,9) are **logically downstream** of the correctly typed strict-core comparison. This is not an unsupported completion claim: the first 56 headings were scoped earlier but general machine-formalized proofs are not furnished.

## B. Reverse propagation of printed Section-6 conditions

**B1 / TRUE TYPING GAP:** source Def2.5, printed p8, permits declared `varpi` with an unavailable source typed profile. It does not require `X_A,varpi`, `Ap`, `Sat`, `Xi` to exist. But source Def6.1 F3, printed p13, explicitly states **“For every varpi∈Pi_A”** while using `phi_varpi:X_A,varpi→X_B,varpi`; F4 also omits the bound `varpi`, F5 refers to its assigned domain without the guard. Def6.3 says “for every source input x∈X_A,varpi” with analogous unbound guard. On a legal declared-unavailable full core even identity is ill typed as literally quantified. The corrected hypothesis `G: varpi declared in A AND profile available in A` resolves the reference while preserving unavailable ≠ supplied-empty; F1 ensures target profile availability. P11 proved category/embedding/inverse properties under G. **Printed source remains CONDITION_MISSING**; do not silently rewrite it as already correct.

**B2 / TRUE CHARACTERIZATION ISSUE:** source Definition 6.7, printed p14, separately requires S1 componentwise bijection, S2 available-sort sets equality, S3 declaration sets equality and S4 inverse reflection. Source Theorem6.8 says strict isomorphisms are “exactly the bijective property embeddings” without incorporating S2/S3 into a defined special term. A bijective carrier-component embedding A→B with `Pi_A=∅`, `Pi_B={varpi}` is a counterexample to that shorthand. Finite P9A/P10 and general P11 agree. **Strict equivalence under full S1–S4 is not disproved**, but the abbreviated “exactly” implication needs extra hypotheses. The incorrect shorthand also appears in **Abstract and Theorem 11.1(7)**.

**Dependencies affected:** Proposition 6.2 and 6.4, Theorem 6.6, Theorem 6.8 shorthand; Theorem 11.1(6,7) directly; Theorem 11.1(8,9) via reliance on a valid strict-core category/comparison. Prop6.9 and Theorem6.11 themselves admit conditional general derivations. No need to rewrite the two primitive axioms or C1 because of these localized map/characterization defects.

## C. Original non-numbered source statements with separate obligations

| Source | Audit classification | Why it matters |
| --- | --- | --- |
| Abstract: two axioms/independence/C1 | **SUPPORTED_WITH_PREMODEL_SCOPE** | Prevents treating axiom-falsifying countermodels as admitted full models. |
| Theorem 4.3 “relative to ... C1” (p11) | **INTERPRETATION_CLARIFICATION_OPEN** | C1 printed p9 begins “Given a primitive property core”. The independence countermodels are well-typed **premodels**, not primitive cores. Interpret C1's defining formulas conservatively on premodels for the independence argument; absent an explicit extension sentence this should not be labeled an additional validated full-model counterexample. |
| Definition 3.3 refined statuses (p9) | **SCOPE-BOUND** | Zero/nonzero is defined only on zero-bearing kinds; profile-unavailable is a kind-level status before `x∈X_A,varpi` exists. |
| Definition 2.5 “no coordinate required” (p8) | **PRESENTATION_NOTE** | A canonical core should identify whether surplus undeclared/unavailable primitive coordinates are forbidden/ignored; avoid treating optional unused metadata as independently compared primitives. No direct counterexample to PI/PII follows. |
| §9.2 downstream aggregate sentence (p18) | **NONRECONSTRUCTION_SCOPE_NOTE** | Arbitrary independent bridges `Theta_A` need not be equivariant or injective. External aggregate equality neither recovers strict property core nor follows from it without extra assumptions. Existing P12 14/14 examples are distinct finite evidence. |
| §10.1 earlier axis system is a specialization (p18–19) | **INTERFACE/EXTENSION CLAIM; GENERAL REALIZATION PROOF NOT IN THIS PAPER** | Aux sorts, prerequisite kinds and **additional specialization axioms** may encode the earlier geometry. The source does not provide an explicit full functor/interpretation theorem transferring *all* older axis-theory axioms; do not claim that was proved here. This is a scope/roadmap qualification, not a new core inconsistency. |
| §10.2 static aggregation/§10.3 dynamics | **SCOPE / FUTURE BRIDGE ONLY** | External analytic bridge and dynamics laws are not entailed by primitive Property axioms; stage-VI record stays fixed within the specified layer. |
| §12 and §13 discussion/conclusion | **DEPENDS_ON_PRIOR_RESULTS** | Their general comparison claims inherit same two Section-6 conditions; no distinct new axiom proof is supplied. |
| Appendix C finite construction instructions | **TYPED_GUARD_FOR_AVAILABLE_DECLARED** | Applicability/satisfaction/assignment coordinates only exist on declared profile-available kinds; finite satisfaction tests should retain this premise. |
| Data/code status and repository subtitle | **EDITORIAL / RELEASE METADATA** | Repository exists independently of the original paper sentence saying software is intended; subtitle differs between PDF and repository README. Not mathematical defects. |

### Special warning about logical levels

An independence counterinterpretation has to violate at least one primitive axiom; such an object is a typed *premodel*. Using a countermodel “of a full core satisfying both axioms” is impossible. The source's proof of mutual nonderivability is valid over the typed premodel background, **if C1 is treated as optional definitional equations extendable to such premodels**, not as a premise that already quantifies only over admitted cores. Mark `C1_COUNTERMODEL_FORMULAS_SCOPE_EXPLICITNESS_OPEN`, not `AXIOM_INDEPENDENCE_FAIL`.

## D. Evidence vs verdict / non-edit closure

**Completed evidence:**
- [P9B source-index cycle](P9B5_SECTION9_11_RESULT.md): 56/56 numbered headings received *manual definition/statement/proof-scope inspection*, not 56 machine-formal proofs.
- [P9A finite suite](P9A_FINITE_MORPHISM_EXHAUSTIVE_RESULT.md): 53 legal core configurations, actually GitHub-CI reproduced.
- [P10 finite suite](P10_CROSS_SORT_MORPHISM_RESULT.md): 108 mixed-sort legal core configurations, actual dual-Python GitHub-CI reproduced.
- [P11 general conditional proof](P11_GENERAL_MORPHISM_PROOF_RESULT.md) plus 10 distinct edge tests actually GitHub-CI reproduced.
- [P12 representation + aggregation](P12_REPRESENTATION_GLOBAL_COUNTERAUDIT_RESULT.md) plus 14 finite cases and both-Python actual archive/replay [Actions #39952098406](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39952098406).
- **P13 newly executed review:** original uploaded 23-page PDF exact-byte SHA256 verified and Theorem 11.1 dependencies reverse traced, unnumbered claims and proof scope crosschecked. **No additional code or external peer-review verification performed as part of P13.**

**Remaining separate obligations:**
1. `CONDITION_MISSING` in printed Def6.1 F3–F5 and Def6.3 source typed quantifiers.
2. `CONDITION_MISSING` in printed Theorem6.8 shorthand and Abstract/Th11.1(7).
3. `SCOPE_CLARIFICATION_OPEN` for the C1-defining formulas on §4 typed premodels (not a fatal core axiom contradiction).
4. `SCOPE_NOTE_OPEN` for §9.2 independent external aggregate bridges.
5. `EXTENSION_INTERPRETATION_NOT_PROVED` for all details of the prior realized-axis specialization.
6. Editable EN/KR LaTeX/PDF source parity, manuscript-level revision and regression audit; **not part of non-edit P13**.
7. External independent mathematical review, proof assistant formalization or genuinely separate manuscript-level adversarial proof validation has **not** been established.

**No new third core-axiom contradiction was found in this P13 audit; this does not prove absence of all possible further problems.**

```text
CASE: PA-P13-20260901-GLOBAL-REVERSE-AUDIT-001
SOURCE_EN_PDF_SHA256: 03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c
THEOREM_11_1_13_CLAIMS_REVERSE_TRACED: 13/13
NUMBERED_SOURCE_ITEM_SCOPE_AUDIT_FROM_P9B: 56/56
MATHEMATICAL_SOURCE_GAPS_IN_SECTION_6: 2 / STILL_OPEN
DEPENDENT_STATEMENTS_REQUIRING_THESE: ABSTRACT; 6.2,6.4,6.6,6.8,11.1(6,7); CONDITIONAL 6.9,6.11,7.1-7.5,11.1(8,9)
C1_TYPED_PREMODEL_INDEPENDENCE_SCOPE: PRESENTATIONAL_CLARIFICATION_OPEN
DOWNSTREAM_ARBITRARY_AGGREGATE_SCOPE: PRESENTATIONAL_CLARIFICATION_OPEN
AXIS_SPECIALIZATION_FULL_INTERPRETATION_PROVED_HERE: no
NEW_FATAL_PRIMITIVE_CONTRADICTION_FOUND: no
ADDITIONAL_P13_MACHINE_TESTS: none
MANUSCRIPT_OR_ZENODO_ORIGINAL_PYTHON_EDITED: no
WHOLE_PROPERTY_FPA: OPEN
NEXT: PA-P14-20260901-RELEASE_READINESS_AND_INDEPENDENT_OBLIGATION-001
```
