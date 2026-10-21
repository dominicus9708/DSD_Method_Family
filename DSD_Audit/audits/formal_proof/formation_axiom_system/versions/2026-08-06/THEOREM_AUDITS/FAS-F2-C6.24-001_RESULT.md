# FAS-F2-C6.24-001 — Assignment-domain obstruction: Formal Proof Audit

**Date:** 2026-10-20 KST. **Owner:** DSD Audit / Formal Proof Audit v0.1. **Scope:** Corollary 6.24 only; source-bound mathematical audit, not external peer certification.

```text
AUDIT_CASE: FAS-F2-C6.24-001
SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, 33 pp
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: Corollary 6.24, §6.5 printed p.24; Definition 6.10 E5/E6 printed p.19
PRECOMMIT_COMMIT: 5b84e485525f1c01265dcfaa71421572efb38070
PORTABLE_PYTHON_COMMIT: 3f84aa42c5ddcc3e01dcd2cc50635c01cf8bd5bb
RESULT_JSON_COMMIT: 99491240808177d642df2124eb45e16eb0c2b45b
INDEPENDENT_LOCALLY_EXECUTED_CHECKER_SHA256: c2e2c2da8626f1f4616d607161f04f55b1ed2604d4d721c88baca072f73fc5bf
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
NEW_AXIOM_REQUIRED: no
F2_WHOLE_MANUSCRIPT_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
SOURCE_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-C6.25-001 / NOT_STARTED
```

## 1. Exact source claim, scope and classical proof

**Corollary 6.24 (Assignment-domain obstruction)** in the locked manuscript, printed p.24, reads: “If no candidate material and quantity-kind bijections preserve every assignment domain, then no strict base-fixed formation isomorphism exists.”

Let both descriptors be full Formation models over one fixed base B and scalar field F. For candidate bijections
```text
f : M_B^L → M_B^M,
τ : Λ_L → Λ_M,
```
define the complete assignment-domain test
```text
D(f,τ)  iff  forall λ in Λ_L, forall a in M_B^L:
                   [a ∈ Q_L,λ iff f(a) ∈ Q_M,τ(λ)].
```
Since f is bijective, D(f,τ) is equivalently `f[Q_L,λ]=Q_M,τ(λ)` for **every** source quantity kind λ.

**The exact antecedent** is `¬∃(f,τ) D(f,τ)`, i.e. for every candidate pair at least one item/kind membership mismatch occurs. This is not the assertion that one badly chosen f or τ fails, and does not require one universally bad kind or material item across every bijection.

If a strict base-fixed formation isomorphism Φ existed, Definition 6.10 would provide material and kind **bijections** `Φ_M`, `τ_Λ` satisfying (E5), and (E5) is precisely `D(Φ_M,τ_Λ)`. This contradicts `¬∃(f,τ) D(f,τ)`. Therefore strict isomorphism does not exist. This is a **necessary-condition obstruction**, not a newly imposed Formation axiom or a claim that E5 alone is sufficient for strict equivalence.

**E6/E5 dependency audit.** In the source, `Γ_L,λ = {(a,q_L,λ(a)):a∈Q_L,λ}`. Hence `Q_L,λ` is the first projection of `Γ_L,λ`. Full E6 graph preservation **and reflection**, with a bijective pointed-value map `I_λ`, implies
```text
a∈Q_L,λ
 iff ∃v∈V_L,λ : (a,v)∈Γ_L,λ
 iff ∃v'∈V_M,τλ : (Φ_M(a),v')∈Γ_M,τλ
 iff Φ_M(a)∈Q_M,τλ.
```
The middle reverse direction uses surjectivity of `I_λ`. Thus **E5 is an explicit domain-status coordinate of strict comparison, but not mathematically independent of full E6** under the manuscript's own bijectivity assumptions. This was already explained in Definition 6.10 and Proposition 6.11; it must not be described as a new independent obstacle or axiom.

## 2. Fully legal finite nonvacuous counterexample to strict equivalence

Use F=F₂, fixed external base with `Supp(B)={s0}`, empty material-record relational signature and exactly **two** materials `M_B={a,b}`, **two** kinds `Λ={λ,μ}`, one expression h, one configuration p and one role ρ in each regime. Take `mat(h)=act(p)={a,b}`, all material anchors equal to s0, `Adm_expr(h)=Des_expr(h)=true`, identity `Res(h,h)`, `Realize(h,p)`, and `Adm_cfg(p)=LC(p)=BC(p)=true`. All undeclared primitive predicates false.

Closure IV makes `Ψ(p)=true`, `K_des={p}`, and `A*=A={a,b}`. Let the pointed spaces for λ and μ each be **{0}** with pointed zero 0, `Λ_δ=∅`, and role relation be the **complete** four-element relation `{(p,a,λ,ρ),(p,b,λ,ρ),(p,a,μ,ρ),(p,b,μ,ρ)}`, identically on both sides. Define the global **partial** assignment graphs by the following domains and defined values:

| Domain | L | M |
|---|---|---|
| `Q_λ` | `{a}` | `{a}` |
| `Q_μ` | `{a}` | `{b}` |
| Defined value on every domain item | 0 | 0 |

The primitive formation axioms are all satisfied: I (expression describability implies admission), II (identity restriction sound with unchanged anchors), III (realization active/material inclusion with same anchors), V (both global assignment domains are contained in A* with correctly typed defined 0). The full model is obtained by the definitionally determined closures IV, VI and VII, supplying `W=F₂` and `T(p,a,λ,0,ρ)=0`, `T(p,·,μ,0,ρ)=1` on each admitted channel. Closure VI admits **two channels on each side**, and Closure VII defines every finite composite; both full-channel-set composite outputs equal 1 modulo 2. The equal channel counts and equal numerical composites are NOT sufficient for strict formation equivalence.

There are **exactly four** candidate pairs of material/kind bijections: `2!×2!=4`. On L, the **material-incidence degree multiset** for membership in domains across kinds is `{2,0}`: a lies in both kinds, b in neither. On M it is `{1,1}`: a and b lie in one kind each. A bijection of material elements and a permutation of kinds preserves this multiset. Since `{2,0}≠{1,1}`, no candidate pair can satisfy **all** source (E5) requirements. The four explicit enumeration checks all reject E5 and, consistently, E6.

Importantly, **both models have two assignment graph edges, the same per-kind domain-cardinalities {1,1}, two admitted channels and the same composite sum**. Distinguishing them requires the *incidence structure*, not coarse counts. The role relation is total and the material anchors all s0, so the obstruction is not manufactured by a different external base, role carrier size, or anchor data.

Also, **undefined assignment is not the value 0**: L leaves b undefined for both kinds, whereas M assigns b value 0 for kind μ. Padding undefined items with an invented zero would destroy exactly the E5 distinction.

## 3. Selected executable tests and hostile controls

- [Prospectively fixed precommit](FAS-F2-C6.24-001_PRECOMMIT.md)
- [Portable Python](../scripts/verify_c624_assignment_domain.py)
- [Deterministic JSON](../results/c624_assignment_domain.json)

An independent local standard-library Python checker was **executed** on the explicit primitive input and three source-typed comparison pairs (negative 2-vs-2, strict-positive 2-vs-2, empty-candidate 2-vs-3). It constructs all primitive Axiom I/II/III/V checks and derived Clause IV/VI/VII objects, enumerates all four typed material-kind bijections of the nonvacuous comparison, and records detailed E5/E6 truth values. The longer local executed checker SHA-256 is recorded above; a shorter portable GitHub verifier is provided for repository-root reproducibility, but **its exact uploaded bytes have not independently been executed from a fresh checkout**.

| Finite selected check | Result |
|---|---|
| Nonvacuous candidate material-kind bijection pairs | 4 |
| Failing E5 / E6 (partial domain / graph) | 4/4 each |
| Same per-kind domain cardinalities / total edges | {1,1} / 2 both sides |
| Material-incidence degrees | L {0,2}, M {1,1} |
| Admitted channel counts | 2 vs 2 |
| Equal full-family composite sums (F₂) | 1 vs 1 |
| Positive target with **identical** domains | 2/4 E5-passing maps, 1 full strict isomorphism |
| Positive target has another E5-failing candidate | yes — one failure does not rule out strict equivalence |
| Target with 3 materials vs source 2 | 0 bijection candidates, vacuous antecedent |
| All assigned graph values | 0; undefined entries preserved separately |

**Negative-case E9 evaluation:** because E5/E6 already fail, E1–E8 do not induce the required admitted-channel bijection. The checker therefore records E9 as **not applicable**, rather than fabricating a term-preserving channel map. For the positive source–copy pair, E5 alone passes for two kind permutations, but supplied term T distinguishes λ and μ; only the true identity kind map also satisfies E9 and hence strict isomorphism.

**Finite/general boundary:** The mathematical proof in §1 is universal by direct use of a necessary condition in Definition 6.10. The finite source-typed model is an adversarial illustration and ensures the antecedent is satisfiable with nonempty typed candidates; it does not enumerate all Formation models or independently certify the F2 manuscript.

Reproduction from cloned GitHub root on Windows 11:
```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c624_assignment_domain.py
```
Default result: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/c624_assignment_domain.json`. Optional first CLI argument specifies output path.

## 4. Formal proof audit gates and conclusion

- G01 frozen source and version: **PASS**; attached 33-page PDF SHA checked. No claim of byte identity to Zenodo.
- G02 exact statement: **PASS**; all candidate material and kind bijection pairs fail *complete* assignment-domain preservation, not one arbitrary failed candidate.
- G03 types/quantifiers: **PASS**; fixed (B,F), full descriptors, kind index mapping τ, domain Q as subset of active describable A*.
- G04 primitive vs derived clauses: **PASS**; I/II/III/V and IV/VI/VII explicitly distinguished and legal.
- G05 general logic: **PASS**; strict isomorphism entails E5; negating existence of E5-compatible bijections excludes strictness.
- G06 dependency E5/E6: **PASS_WITH_BOUNDARY**; E5 is not independent of full E6 with bijective pointed maps; graph projection reconstructs domain.
- G07 adversarial: **PASS**; incidence-invariant nonvacuous example, one failing candidate with another successful, vacuous no-bijection case, zero vs undefined.
- G08 computation: **PASS_WITH_BOUNDARY**; selected finite typed checks not universal proof, portable uploaded code not independently fresh-run.
- G09 downstream scope: **PASS**; no automatic statement that first-branch index b is 5, or that role/threshold/term predicates determine the obstruction. C6.25 and C6.26 remain NOT_REVIEWED.
- G10 mathematical background: **PASS**; ordinary typed set theory, finite bijections, partial function graphs.
- G11 original manuscript edits: **PASS**; no source revision needed, historical optional T4.7 wording clarification kept separate.
- G12 external evaluation: **PASS**; project-internal author-assisted audit, no third-party certified proof.

**MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND.**
**DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY.**
**REVISION_NEED: NONE.**

The boundary concerns the exact quantified source hypothesis, full strict candidate requirements, the E5/E6 dependence and selected finite evidence, **not** a missing mathematical proof. F2 whole-paper audit still OPEN, public PDF/Zenodo unchanged and existing DSD Method Family 22/22 internal standardization unaffected.

**Next resumable audit:** `FAS-F2-C6.25-001`, source Corollary 6.25 **Role obstruction**, NOT_STARTED. Corollary 6.26 (channel-cardinality) is independently NOT_REVIEWED.

[Notion synchronized C6.24 audit](https://app.notion.com/p/3fe81f51e7fa8156b493e2e95e8fe987)
