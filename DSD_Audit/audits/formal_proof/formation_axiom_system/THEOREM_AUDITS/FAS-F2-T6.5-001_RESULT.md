# FAS-F2-T6.5-001 — Identity and composition laws: source-bound FPA result

**2026-10-19 KST · Formal Proof Audit v0.1 · Internal source-bound mathematical review, not independent external certification.**

```text
AUDIT_ID: FAS-F2-T6.5-001
SOURCE: Kwon Dominicus, DSD Formation Axiom System (F2)
SOURCE_FILE: DSD_Formation_Axiom_System_EN(5).pdf (33 pages)
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: Definition 6.1; Definition 6.2 (F1-F6); Proposition 6.3; Definition 6.4 (R1-R5 and witness reflection); Theorem 6.5; printed pp.15-17
PRECOMMIT_COMMIT: d02d18a88b3dff7de7cce3c388408d1d4da5fea8
FINITE_PYTHON_COMMIT: de8af7e256a79b325f425be3fe16087bbe91df68
FINITE_JSON_COMMIT: 2dbaf97fec24063e00a60bbf389e6922abeed75d
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
CRITICAL_GAP_FOUND: no
WHOLE_F2_PAPER: NOT_COMPLETE
INDEPENDENT_EXTERNAL_VALIDATION: not_established
PUBLIC_PDF_ZENODO: unchanged
INTERNAL_METHOD_FAMILY: 22/22 unchanged
NEXT: FAS-F2-SEC6.2-C6.6-C6.7-001 / NOT_STARTED
```

## 1. Claim and precommitted scope

For fixed formation comparison pair (B,F), every full formation model has an identity forward map. If Phi:L->M and Theta:M->N are forward maps satisfying Definition 6.2, their componentwise composite satisfies F1-F6, indexed value-map compositions I^(Theta∘Phi)_lambda = I^Theta_(tau^Phi_Lambda(lambda)) ∘ I^Phi_lambda and term-map J^(Theta∘Phi) = J^Theta ∘ J^Phi, and the induced candidate-channel map composes. Identity maps are embeddings under Definition 6.4; embeddings are closed under composition.

The theorem does not assert arbitrary forward maps preserve finite set-composites when the induced channel map is noninjective. That stronger conclusion requires the injectivity condition already stipulated by Proposition 6.3.

## 2. General mathematical proof audit (independent of finite fixtures)

**Identity.** All identity maps preserve typed carrier data, material record operations and external anchors, predicates, relations, assignments, zero values, metric-threshold auxiliary information (where declared), roles, and the term map. They are injective and reflect each item on its own image. R1 reduces to A=A∩A, while R2-R5 and witness reflection are logical identities. Thus the identity map is a formation embedding and, a fortiori, a forward map.

**Forward composition F1.** The composite of homomorphisms preserves the material-record relations/functions in the stipulated type and fixes external codomains. Two successive subset inclusions yield inclusion into the third model's material and active-material supports, and equality of anchors at each map gives equality after composition. This holds even without injectivity.

**F2/F3/F5.** Each predicate/relation/role implication passes through M. Applying it first under Phi and then Theta proves the corresponding composite implication.

**F4 and typing.** Each I_lambda is typed from V_(L,lambda) to V_(M,tau^Phi_Lambda(lambda)). Its composite with I^Theta_(tau^Phi_Lambda(lambda)) is typed into N, preserves distinguished zero, and transports the graph edge under two steps. For lambda in Lambda^delta_L, membership preservation in both forward maps yields membership in Lambda^delta_N. The size-preservation equations and threshold equality compose transitively; no new metric/threshold assumption is needed. Indexed composition, rather than applying an I with the original source index at the second stage, is essential.

**F6 and channel map.** Proposition 6.3 derives Phi-hat(c) in C_M whenever c in C_L. Therefore the following T_M argument is defined:
```text
J^(Theta∘Phi)(T_L(c))
  = J^Theta(J^Phi(T_L(c)))
  = J^Theta(T_M(Phi-hat(c)))
  = T_N(Theta-hat(Phi-hat(c)))
  = T_N((Theta∘Phi)-hat(c)).
```
The induced tuple transformation commutes with componentwise mapping of p,a,lambda,v,rho by associativity and the indexed I-map formula. J is F-linear because it is a composite of F-linear maps.

**Embeddings and R1.** Let f=f_M, g=g_M be injective material maps. Put A=f[M_L] subset M_M. For any source expression x:
```text
(g∘f)[mat_L(x)]
  = g[mat_M(f_E(x)) ∩ A]                    (R1 for Phi)
  = g[mat_M(f_E(x))] ∩ g[A]                  (injectivity of g)
  = (mat_N(g_E(f_E(x))) ∩ g[M_M]) ∩ g[A]      (R1 for Theta)
  = mat_N((g_E∘f_E)(x)) ∩ (g∘f)[M_L].
```
The last step uses A subset M_M. The active-material identity is identical with act_L(p) in place of mat_L(x). This proves R1 rather than merely saying it is preserved.

**R2-R5 and witness reflection.** Each source-indexed equivalence composes: P_L(x) iff P_M(f(x)) iff P_N(g(f(x))). The same applies to restriction, realization, role tuples, assignment graphs and Lambda-delta membership (with correctly reindexed type maps). Component injections compose, as does the material-record embedding property; J is again an F-linear injection. If Psi_N((Theta_P∘Phi_P)(p)), witness reflection for Theta gives Psi_M(Phi_P(p)); reflection for Phi gives Psi_L(p). Thus the separate witness-reflection condition is stable under composition.

These arguments follow from source Definitions 6.2 and 6.4, the already derived Proposition 6.3, and ordinary set/function algebra. No new primitive axiom or added theorem premise was used.

## 3. Reproducible finite adversarial checks

[Portable Python fixture](../scripts/verify_t65_forward_composition.py), [deterministic JSON](../results/t65_forward_composition.json). Run from the repository root on Windows:
```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t65_forward_composition.py
```
Output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/t65_forward_composition.json`.

Executed local finite tests on typed toy structures with constant anchors, identity value maps (including the distinguished zero), one quantity kind and one role kind, empty material-internal signature, admissible restriction/realization and assignments:
- Three nested models L⊆M⊆N, including added target material and witnesses: identity embedding, each embedding, composite embedding, R1 image intersection, image-channel composition PASSED.
- Two distinct source admitted channels mapping to one target admitted channel under a legitimate noninjective forward map: forward composition PASSED; source selected finite component sum 22, target *set image* finite composite 11. No contradictory F6 term relation; Proposition 6.3 does not assert aggregate equality in this case.
- Additional target-only expression realizing an image configuration: source is not describable but target becomes describable. F1-F6 and source-indexed R1-R5 may still hold, while the independently required witness reflection fails. This is **not** a countermodel to Theorem 6.5; it shows why omitting Definition 6.4's separate witness-reflection clause would be unsound.

The finite test specializes all I_lambda and J to identity maps and does **not** executable-test arbitrary changed quantity-type indices, nontrivial linear injections, optional Lambda-delta metrics, or nonempty material-record signatures. Those general properties are addressed by the written mathematical proof above. Finite fixture success must not be generalized without that proof.

## 4. Verdict, limitation, revision

- MATHEMATICAL_VERDICT: **PROVED_IN_DECLARED_BACKGROUND** for Theorem 6.5's exact claims within the frozen F2 typed setting.
- FPA VERDICT: **PASS_WITH_BOUNDARY**: preserves explicit applicability and distinguishes theorem-level composition from conditional aggregate preservation, and internal verification from independent certification.
- REVISION_NEED: **NONE**. No need to modify the primitive axioms, introduce an additional hypothesis, rewrite the proof or change the manuscript/Zenodo under the scoped findings.
- Keep the existing Theorem 4.7 language clarification open as a separate case.
- Whole-paper F2 remains OPEN. No inference from T6.5 to an independent blanket PASS for Corollaries 6.6/6.7, Theorem 6.8 or later map algebra.

**Next checkpoint (NOT_STARTED):** Corollaries 6.6 and 6.7 as a separately locked short Section 6.2 proof group; then Theorem 6.8 and further dependency-prioritized obligations. This is a deliberate bounded stop under the project's timeout-prevention rule.
