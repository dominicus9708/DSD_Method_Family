# FAS-F2-T6.20-001 — Static formation closure: bounded formal proof audit

**Date:** 2026-10-20 KST. **Owner:** Existing DSD Audit / Formal Proof Audit (FPA) v0.1. **Scope:** source-locked mathematical synthesis theorem only, not a complete paper audit or external certification.

```text
AUDIT_ID: FAS-F2-T6.20-001
SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, attached 33-page copy
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: Section 6.4, Theorem 6.20, printed p.23
PRECOMMIT_COMMIT: d3f033ec6b5ed23fb1dcaec2953a322382496828
EXECUTED_PYTHON_COMMIT: 357a7e36bc6a3c50f7dd161c2d47f6df925d3f1d
EXECUTED_PYTHON_SHA256: e2bc5fc457edb787687de671ccdd6d00cd6e2a72f15e412aa53f9a3be80738b4
FINITE_JSON_COMMIT: d19a71b77ba98599e45d99c657c0e13c42b020c4
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
SOURCE_DEPENDENCY_CORRECTION: none
MANDATORY_SOURCE_EDIT: none
F2_WHOLE_PAPER: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
SOURCE_PDF_AND_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-P6.22-001 / NOT_STARTED
```

## 1. Exact manuscript claim and dependency map

Source Theorem 6.20, *Static formation closure*, states **five** results over a fixed `(B,F)`; it is an explicit conjunction/summary of earlier source claims, not a new primitive axiom. The original proof gives this exact dependency assignment:

| Part | Source statement (scope preserved) | Required manuscript support |
|---|---|---|
| (i) | Every **primitive formation core**, **together with supplied post-Stage-VI term data**, has a **unique full closure expansion** | Theorem **3.3** |
| (ii) | Stage reductions form a coherent chain; typed candidate channel admitted iff formation-trace set **nonempty** | Proposition **2.5**, Theorem **3.6** |
| (iii) | Definitional closure layers determined by their **declared primitive or supplied inputs**; no extra *independent* comparison obstruction | Theorem **6.17** |
| (iv) | Forward maps and embeddings have identities and composition closure; strict isomorphism = **bijective embedding** and is an equivalence relation | Theorem **6.5**, Corollary **6.6**, Proposition **6.11**, Theorem **6.14** |
| (v) | For every **strictly non-isomorphic** pair, b is defined, symmetric, b≠4 and invariant under strict isomorphism of either model | Theorem **6.16**, Corollary **6.18**, Theorem **6.19** |

Each cited source result has already received a bounded earlier source-level FPA treatment, or in Proposition 2.5's case was included in Section 2 G0. No later, not-yet-audited Section 6.5 or Section 7 theorem is silently imported. The dependency graph is acyclic: no proof of T6.20 is needed to establish its individual prerequisites.

## 2. Independent audit of inference from dependencies

**(i) Unique relative closure.** A primitive core contains all typed structural/primitive data satisfying I, II, III and V. Clause IV uniquely sets `Psi,Des_cfg,K_des,A*,A` from the core and its supplied predicates/relations; candidate channel types and assignment graphs are determined; Clause VI uniquely yields `Chan` and admitted `C` from the **already supplied Role**. Given **arbitrary separately supplied** `F`-vector space `W` and **total** `T:C→W`, Clause VII uniquely fixes `Dcomp=P_fin(C)` and `Comp(F)=∑_{c∈F}T(c)`. Existence follows by those definitions; uniqueness is pointwise extensionality of their output sets/functions. T3.3 identifies the primitive reduct of full models as exactly primitive formation cores. **Critical boundary:** the primitive core alone does **not** choose a canonical W or T; distinct T inputs may produce distinct full models without refuting (i).

**(ii) Reductions and trace iff.** Definition 2.4 gives ordered stage records and erasure maps. For `0≤i≤j≤k≤7`, `π_{j,i}∘π_{k,j}=π_{k,i}`; `π_{k,k}=id`. They are **truncations of a full model**, not stand-alone claims that each truncated record is itself full. Definition 3.5 gives `Tr(c)` by a *restriction-realization witness* and assignment+role conditions. By Closure IV `Des_cfg(p)⇔Psi(p)`; by Closure VI, `c∈C` iff `Des_cfg(p)`, the configuration-local **regime-global partial-assignment graph** and Role all hold. Thus `c∈C ⇔ Tr(c)≠∅` (T3.6). Multiple witnesses in Tr do **not** produce multiple operational channels: channel identity is the five-tuple `(p,a,λ,v,ρ)`. Undefined assignment is not value zero. A nonadmitted candidate has no T value.

**(iii) Definitional vs independent-data branching.** T6.17 shows Stage IV is uniquely determined by Stage III, with **I3=I4** for full model comparisons. Stage VI is determined only **after Stage V and Role** are supplied; Stage VII only **after Stage VI and W,T** are supplied. Therefore the *definitional closure rules* IV, VI and VII do not choose new independent parameters or create new branching beyond the primitive/supplied data. This **does not** say `I5=I6` or `I6=I7`, nor exclude `b=6` (Role difference) or `b=7` (term-space/data difference). Those cases are actually allowed by T6.16/T6.19. Read the source's “no additional independent comparison obstruction” in exactly this **relative** sense; it is not a stronger unconditional uniqueness claim.

**(iv) Map categories and strict equivalence.** By T6.5, typed forward formation maps have identities and componentwise composition, with correct **quantity-kind-indexed** pointed map `I^{Θ∘Φ}_λ = I^Θ_{τ^Φ_Λ(λ)}∘I^Φ_λ` and linear term map `J^{Θ∘Φ}=J^Θ∘J^Φ`. Formation embeddings additionally require injectivity, material-record embedding, exact image reflection and a **separate witness-reflection condition**; these persist under composition. Corollary 6.6 yields the possibly large category and wide embedding subcategory by associativity. Proposition 6.11 proves strict base-fixed isomorphisms **exactly** bijective embeddings, *not* arbitrary bijective forward maps without R1–R5/witness reflection. T6.14 shows the strict equivalence relation is reflexive/symmetric/transitive, including inverse of F-linear term-space isomorphism and kind-indexed inverse pointed maps. Thus the source's composite claim (iv) follows without broadening the morphism definitions.

**(v) First branching.** For **every pair not strictly base-fixed formation-isomorphic**, T6.16 says `I7=∅` and the least empty `b∈{0,...,7}` exists. C6.18 deduces **b≠4** from equality `I3=I4` (T6.17), not from mere nestedness. T6.19 provides exact symmetry of all stage nonemptiness profiles and invariance under **strict base-fixed** representative replacement, implying b has simultaneous definedness and equal values after reversal or strict model reidentification. It makes no claim about replacing a model by one with only matching numerical composites, by a forward map, or by a non-surjective embedding. **If strictly isomorphic, `b` is undefined**, not an assigned numeral. `b=0` is an ambient/anchored-background failure label, not an eighth formation stage.

Since (i)–(v) follow from their respective previously proved source claims in the declared set-theoretic/F-vector-space background, **T6.20 is proved as the source actually states it**. No extra axiom, silent regularity constraint, empirical assumption or comparison structure is required.

## 3. Locally executed source-typed finite supplemental checker

- [Prospectively fixed attack plan](FAS-F2-T6.20-001_PRECOMMIT.md).
- [Windows-runnable Python](../scripts/verify_t620_static_closure.py).
- [Selected deterministic result JSON](../results/t620_static_closure.json).

An actually executed **7,007-byte** Python script (local SHA-256 `e2bc5fc457edb787687de671ccdd6d00cd6e2a72f15e412aa53f9a3be80738b4`) checks a small typed Formation core, including nontrivial **proper restriction H→h**, primitive identity restrictions, exact anchor inheritance and realization, configuration witnesses/nonwitnesses, typed size/threshold and one regime-global **partial** assignment with **defined 0** and other undefined values. It constructs closure IV, VI, VII rather than simply setting an expected pass flag, and evaluates trace sets for **all typed candidate operational channels**.

| Selected finite test | Result |
|---|---|
| Primitive axioms I/II/III/V checked on selected core | All satisfied |
| Derived closure layers IV/VI/VII constructed | Completed |
| Typed operational candidate channels and trace/admission iff tests | **72/72** |
| Admitted channels | **2** |
| Restriction-realization trace witnesses for each admitted channel | **2 each** |
| Unique expansion for identical full primitive and supplied W,T inputs | Identical |
| Stage-coordinate erasure/π composition triples `0≤i≤j≤k≤7` | **120/120** |
| Empty-family composite and nonempty cancellation | Checked |
| Defined zero versus undefined assignment | Distinguished |
| Nonadmitted candidate T values | Absent |
| Change Role alone after same through-Stage5 input | Different Stage6 channel result |
| Change T alone after same through-Stage6 input | Different Stage7 composite result |
| Prescribed `J(t)=2t` transport for all four finite channel families | **4/4** |

The Role and T variations are **hostile boundary controls** confirming relative, not unconditional, uniqueness. Two separate valid trace witnesses yield only **one** five-tuple operational channel for that role/value; trace multiplicity is not channel multiplicity. Numerically equal empty and cancellation composites do not imply channel-family equality, let alone strict isomorphism.

The finite checker does **not** retest all universal map/categorical/branching lemmas. Earlier typed finite results ([T6.16](../results/t616_first_branching.json), [T6.17](../results/t617_closure_nonbranching.json), [T6.19](../results/t619_symmetry.json)) remain separate evidence with their original provenance. Their source-mathematical theorems, rather than raw JSON flags, are the proof prerequisites used in Section 2. A finite example is not a universal proof or independent external certification.

**Code reproducibility:** The script was executed in the local tool runtime and the matching 7,007-character portable Python script and deterministic JSON were uploaded to GitHub. The committed artifact has **not separately been run from a fresh GitHub checkout or by a third party**, so no independent replication is claimed.

Windows repository root command:

```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t620_static_closure.py
```

Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/t620_static_closure.json`. An optional first argument sets the output filename. Python standard library only.

## 4. Formal audit gates

- G01 Source/version: **PASS**; source-attached 33-page PDF checksum independently matched. Zenodo exact bytes not independently compared.
- G02 Exact dependency map/noncircularity: **PASS**; T3.3, P2.5, T3.6, T6.17, T6.5, C6.6, P6.11, T6.14, T6.16, C6.18 and T6.19 are all prior results, none depends on T6.20.
- G03 Typing/quantification: **PASS**; fixed (B,F), primitive cores and full descriptors, set-sized individual structures, conditional b.
- G04 Original axioms and supplied vs derived: **PASS**; I/II/III/V primitive, IV/VI/VII closure; W,T and Role independently supplied in declared positions.
- G05 Mathematics: **PASS**; each of five clauses follows from named earlier source statements without broadening.
- G06 Existence/uniqueness: **PASS_WITH_BOUNDARY**; uniqueness only **relative** to supplied W,T, not selection/canonicity.
- G07 Adversarial: **PASS**; changing supplied Role/T, trace multiplicity, zero-vs-undefined, b6/b7 controls.
- G08 Finite/general separation: **PASS_WITH_BOUNDARY**; small fixture and prior finite tests do not prove universal correctness.
- G09 Map/branch semantics: **PASS**; forward vs embedding vs strict distinguished; I5/I6/I7 independence preserved and strict b conditional.
- G10 Mathematical background: **PASS**; typed set/class metatheory, finite family sums, ordinary function composition.
- G11 Downstream: **PASS_WITH_BOUNDARY**; Definition 6.21 and Proposition 6.22, later 6.23–6.26/Section7 remain unaudited, not promoted.
- G12 External validation: **PASS**; project-internal source-bound audit not independent external mathematical review.

**MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND / DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY / REVISION_NEED: NONE.**

This is an **integration/synthesis theorem**: successful verification does not turn past FPA checks into an external proof of the entire F2 manuscript. The earlier Theorem 4.7 minor scope-wording clarification remains recorded independently. Source PDF/Zenodo unchanged; the existing DSD Method Family 22/22 internal-standardization count is not modified.

**Next unstarted bounded case:** `FAS-F2-P6.22-001`, Definition 6.21 and Proposition 6.22, *Composite-level coincidence does not imply strict formation equivalence*, **NOT_STARTED**. Do not invent a “Theorem 6.21” (the original manuscript's 6.21 is a Definition).
