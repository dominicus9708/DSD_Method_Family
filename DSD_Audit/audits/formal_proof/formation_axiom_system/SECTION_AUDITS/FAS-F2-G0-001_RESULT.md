# FAS-F2-G0-001 — Section 2 typed setting, source signature and formation reductions
**2026-10-19 · FPA v0.1 · Source-bound, internal mathematical review; NOT a full Formation F2 certificate.**

```text
AUDIT_ID: FAS-F2-G0-001
SOURCE: Kwon Dominicus, Formation Axiom System: Dimensional-Structural Describability
SOURCE_FILE: user-supplied DSD_Formation_Axiom_System_EN(5).pdf (33 pages)
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: Section 2, printed pp.3–6; Appendix A, printed p.30
PRECOMMIT_COMMIT: fbf51249db4c36f2d9c2135cec40b843ea2696d7
SCOPE: Definitions 2.1–2.4, Proposition 2.5, §2.1–2.3 conventions
PROPOSITION_2_5_MATH_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DEFINITIONAL_AND_TYPING_VERDICT: INTERNALLY_COHERENT_WITH_DECLARED_CONVENTIONS
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: CLARIFICATION_OPTIONAL
GATES_REVIEWED: G01-G14 / 14 (all substantively addressed; G10-G11 WITH_BOUNDARY)
FINITE_PROJECTION_SMOKE_TEST: 120 triple-index checks + 36 prefix-reduction checks
INDEPENDENT_EXTERNAL_VALIDATION: not_established
WHOLE_PAPER_F2_VERDICT: not_issued
MANUSCRIPT_ZENODO_CHANGED: no
NEXT_CASE: FAS-F2-T3.6-001 / NOT_STARTED (Formation-trace characterization)
```

## 1. Source fidelity: mathematical nature and size status

Section 2.1 expressly defines a **static typed set-theoretic axiom system** relative to ZFC, NOT a fully given minimal first-order derivation calculus. Primitive Axioms I, II, III, V are imposed; Stages IV, VI, VII are definitional closures. All carriers, component value spaces, term spaces, maps, relations and **individual** descriptors are sets. The carrier B, `Supp(B)`, and common scalar field F are sets. Broad families, including `FormDesc_(B,F)` and `F_k(B,F)`, are explicitly *metatheoretic classes* unless a set-indexed family has been fixed. They cannot be silently used as individual model-carrier elements or ZFC sets.

**Class-map formalization boundary**: The notation `π_(j,i):F_j(B,F)→F_i(B,F)` is justified as a metatheoretically definable coordinate-erasure operation on the (potentially proper) classes of typed records. In bare first-order ZFC, it need not denote a **set-valued graph of a function with proper-class domain**. The source's §2.1 class convention already permits such notation in its intended informal set-theoretic/metatheoretic reading. An optional explanatory phrase would prevent a foundationally stricter reading; this is not a theorem refutation.

The source promises no additional choice principle in elementary finite constructions: this is consistent with its adoption of ZFC and does not assert ZFC-independent results.

## 2. Primitive carriers and typed maps (§2.2)

- `M_B^L` has an `S_mat` structure; **material-internal** signature symbols are relational. Annotations into **fixed external codomains** can be restricted in their material arguments. Hence every retained subset carries an induced substructure in the stipulated relational-material sense. This is a convention on the primitive data signature, not a general theorem for arbitrary material-returning function symbols.
- For every expression x, `mat_L(x)⊆M_B^L` and `anch_x:mat_L(x)→Supp(B)`. For configuration p, `act_L(p)⊆M_B^L`, `anch_p:act_L(p)→Supp(B)`. In particular **anchor maps are defined on their full material/active sets**, even when those sets are empty. Empty anchors are the unique empty function where typing permits it.
- Section 2.1 uses `f|A := f restricted to A∩dom(f)`, so `anch_h=anch_H|mat(h)` implies `mat(h)⊆mat(H)` **by equality of domains**; no unspoken prior inclusion is necessary. Analogous reasoning applies to `anch_p=anch_h|act(p)`.
- `Adm_expr, Des_expr` are separate primitive predicates on E; `Adm_cfg, LC, BC` are separate primitive predicates on P. The relation `Res` and `Realize` are **primitive relations**, not secretly sound by their very spelling; their soundness is asserted by Axiom II and III respectively. `Role` likewise is primitive.
- Each quantity kind λ has a *pointed value set* (V_λ,0_λ), **not necessarily an F-vector space**; the term space W is a distinct, post-Stage-VI F-vector space. `q_λ:Q_λ→V_λ` is a single-valued partial assignment from its type declaration, while `Q_λ⊆A*` is the separate axiom condition V. For λ in Λδ, `size_λ:V_λ→[0,∞)` vanishes exactly on the distinguished zero and δ_λ>0; no size map for λ outside Λδ is tacitly required.
- `Supp(B)` can be empty if all anchors have empty domains; the source does not claim universal non-emptiness of each carrier in Section 2. Its later existence constructions must be audited separately.

All map/function applications above are only meaningful on explicitly declared domains; Appendix A reinforces this for q_λ(a) and T(c).

## 3. Definitions 2.1–2.3 and primitive/derived noncircularity

**Definition 2.1.** Primitive data include carrier data; expression and configuration predicates; restriction and realization relations; quantity kinds, q maps and role; plus declared status data. The term data W,T are *supplied only after* accepted channels C have been defined.
Derived:
```text
ConfAdm(p) := Adm_cfg(p) ∧ LC(p) ∧ BC(p)
Ψ(p) := ∃H,h[Res(H,h) ∧ Des_expr(h) ∧ Realize(h,p)
              ∧ Adm_cfg(p) ∧ LC(p) ∧ BC(p)]
A* := union_{p in P and Ψ(p)} act(p)
```
All quantified H,h range over typed expression carriers; the comprehension defining Kdes and union A* are sets because P and M are sets. When no configuration satisfies Ψ, Kdes=∅ and A*=∅. **No q, T, Role or Chan appears in Ψ**, so the subsequent V constraint `Q_λ⊆A*` does not feed its result back into Ψ: no definitional circularity.

**Definition 2.2.** A primitive *core* is well typed and satisfies I, II, III and V. A full model has the same primitive core plus supplied W,T and IV/VI/VII derived coordinates. It is incorrect to infer that arbitrary well-typed raw inputs automatically satisfy primitive axioms or define a full model. Definitional closure alone does not certify primitive-axiom truth.

**Definition 2.3.** Formation-finite requires only material, expression, configuration, quantity-kind and role carriers, accepted channels and each Q_λ to be finite. Support B, pointed value spaces and term space W need not be finite, consistent with the source's explicit caveat. Formation-finite ≠ finite every background sort; no inconsistency.

## 4. Definition 2.4 stage records: ordering and Stage 0

The source builds eight **records indexed 0,...,7**, but exactly seven formation stages indexed I–VII. Stage 0 is inherited bookkeeping and NOT an eighth generative stage. The sort `R_L` for roles is fixed in `F_<=0`, while the primitive relation `Role_L` is first *recorded* in `F_<=6`; these are distinct objects. Similarly, the carrier `Λ` and pointed value sets appear at Stage 0 while individual assignment domains and functions are first recorded at Stage 5. This is not an inconsistent stage double definition; primitive data can be declared as a whole in Definition 2.1 and recorded at their particular stages by Definition 2.4.

For every **full model L**, the records `F_L<=0,...,F_L<=7` are cumulative, each containing all coordinates from earlier stages. For any k, `F_k(B,F)` is the metatheoretic class of well-typed Stage-k records *of the displayed form*, not asserted to contain only reductions of full models. Consequently a purely well-typed Stage-4 record may have a wrong arbitrary Ψ field and **not** be a reduction of any full model. This neither makes the coordinate projection ill typed nor refutes Proposition 2.5; it means that source-specific closure and primitive axioms must be enforced whenever a theorem reasons about actual full-model truncations or their images. This distinction merits optional explanatory emphasis.

## 5. Proposition 2.5 proof, independently reconstructed

Let a Stage-k record be a finite ordered sequence of consecutive blocks `(D_0,...,D_k)`, each block D_s being the coordinates first recorded at stage s (with background block D_0). For `0≤i≤j≤k≤7` the reduction `π_(k,j)` drops blocks `D_(j+1),...,D_k`, and `π_(j,i)` drops blocks `D_(i+1),...,D_j`. Hence:
```text
π_(k,k)(D_0,...,D_k) = (D_0,...,D_k),
π_(j,i)(π_(k,j)(D_0,...,D_k))
   = π_(j,i)(D_0,...,D_j)
   = (D_0,...,D_i)
   = π_(k,i)(D_0,...,D_k).
```
Thus `π_(k,k)=id` and `π_(j,i) ◦ π_(k,j) = π_(k,i)` as stage-coordinate operations on their declared classes. For a fixed full model L, `F_L<=j=(D_0^L,...,D_j^L)`; projection gives `π_(j,i)(F_L<=j)=F_L<=i`. This reasoning works for any well-typed cumulative record; it does not require all intermediate records to satisfy the primitive axioms independently. The proof does not use Choice, topological assumptions or numerical convergence.

**Edge/index coverage:** identity case i=j=k; nontrivial i<j<k; i=0 and k=7; successive one-stage deletion; the order of role-sort and Role-relation blocks; and empty carriers where typed. No counterexample to the stated reduction law arises, since it follows from the operation definition.

## 6. Reproducible auxiliary coordinate checks

- [Python verifier](../scripts/verify_g0_stage_reductions.py), commit `0cf53f8a87a3b272014ff2a83d59ff4e3f650c0a`.
- [Deterministic JSON](../results/g0_stage_reductions.json), commit `5b3f6e1eb6093f868d26ef41db57ab53b19f559e`.
- The local in-session coordinate model tested all **120** nondecreasing index triples `0≤i≤j≤k≤7` and **36** ordered index pairs `0≤i≤j≤7`, with no assertion failures. It also explicitly places the role carrier in Stage 0 and role *relation* in Stage 6.
- This is a **structural smoke test** of a representative coordinate-record implementation. The general theorem's proof is the symbolic argument in §5, NOT a consequence of 120 passing finite tests. The committed Python code represents the same check; **its execution by external parties/CI has not been confirmed**.
- Run from the GitHub method-family repository root on Windows 11 / PowerShell:
```powershell
py -3.11 DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_g0_stage_reductions.py --output DSD_Audit\audits\formal_proof\formation_axiom_system\results\g0_stage_reductions.json
```

## 7. Frozen gate results G01–G14
| Gate | Outcome | Scope note |
|---|---|---|
| G01 set/class status | PASS_WITH_BOUNDARY | Class maps are metatheoretic, not ZFC set-functions on proper-class domains |
| G02 static ZFC-relative framework | PASS | Not a fixed independent first-order calculus |
| G03 total anchors and restriction f\|A | PASS | Works also when retained material is empty |
| G04 relational-induced substructure | PASS | Relies on restricted signature, not arbitrary functions into M |
| G05 primitive vs derived and Ψ | PASS | No q/Role/T feedback into Ψ |
| G06 q / pointed V / F-vector W | PASS | q single-valued by typing; V separately from W |
| G07 empty/formation-finite | PASS | Finite data not all background value sorts |
| G08 core/full model noncircularity | PASS | IV/VI/VII do not imply I–III/V |
| G09 Stage 0 vs I–VII | PASS | Role sort ≠ Role relation |
| G10 projector law | PASS | Direct general coordinate-erasure proof; 120 checks auxiliary |
| G11 typed records vs full truncations | PASS_WITH_BOUNDARY | A typed arbitrary Stage-4 record need not satisfy derived definitions |
| G12 no beyond-source overclaim | PASS | No absolute W,T uniqueness, physics or infinite-family claim |
| G13 evidence hierarchy | PASS | General proof and finite test separated |
| G14 bounded stop and transparent reporting | PASS | Next audit separate |

## 8. Final bounded judgment / suggested wording

**Proposition 2.5: PROVED_IN_DECLARED_BACKGROUND** as a formal consequence of stage-record coordinate erasure. **Definitions 2.1–2.4: internally well typed and coherent under stated source conventions**, not independently “proved theorems.” The independent FPA process verdict is **PASS_WITH_BOUNDARY** due to explicit metaclass-vs-set and well-typed-vs-full-record distinctions. These distinctions are already implicit or explicit in the source; no new mathematical axiom, structural rewrite, or mandatory source amendment is justified by this review.

Optional next source edit (when a genuinely warranted section revision is already being made):
1. After Definition 2.4's `F_k(B,F)` declaration, note that `π` is a **metatheoretically defined class-map operation** if these families are not set-sized.
2. Explain that an arbitrary well-typed Stage-k record need not be extendable to a full formation model unless relevant primitive and closure conditions hold.

Do **not** modify the historical manuscript or Zenodo merely for these expository points. **No comprehensive F2 PASS**, no external independent verification, and no automatic certification of later map/isomorphism and branching theorems.

**STOP:** Next `FAS-F2-T3.6-001` — Formation-trace characterization (Theorem 3.6) and Definition 3.5, NOT STARTED. Restart with exact-source prospective precommit.
