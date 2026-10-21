# FAS-F2-G6-REVISION-SCOPE-001 — Section-specific manuscript amendment proposal (EN)

Author: **Kwon Dominicus**.
Status: **PROPOSAL / NOT APPLIED**.
Original source: `DSD_Formation_Axiom_System_EN(5).pdf`, 33 pages, SHA256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
This file is an audit editorial proposal, **not** a replacement or an attributed quote of the source manuscript.
Each unit stands alone and must be approved/edited by original source section.

---

## 1. Theorem 4.7 — Residual clausewise independence (printed p.11)

**Original issue:** “relative to the typed background and the other primitive axioms” can appear to include the undecomposed parent primitive axiom, which itself contains the omitted residual condition.

**Proposed replacement for Theorem 4.7 preamble:**

> After the dependencies in Proposition 4.6 have been factored out, replace Primitive Axioms I, II, III, and V by the equivalent list of the six residual constraints (i)–(vi) over the fixed typed background.
> Each residual constraint is independent of the other five residual constraints within this residualized presentation.

**Proposed replacement for its proof's final clause:**

> In each of the six counterinterpretations, the named residual constraint fails while the other five residual constraints remain satisfied.
> Hence the residualized axiom list is clausewise independent.
> The undecomposed primitive axiom containing the omitted clause is not asserted to remain true in that counterinterpretation.

**Unchanged claim:** six independent residual constraints, source counterexamples, explicit material typing side conditions and independence of the *whole four* primitive axioms (separate Theorem 4.5).

---

## 2. Proposition 5.13 — Zero extension and channel membership (printed p.14)

**Original issue:** a zero-extended output does not always lose enough information to prevent reconstruction of channel membership.
The collision is real **when** an absent candidate and an admitted zero-term channel coexist.

**Proposed full replacement statement:**

> Proposition 5.13 (Conditional membership loss under zero extension).
> Let \\(\overline{T}_L\\) extend \\(T_L:C_L\\to W_L\\) to the candidate-channel universe \\(U_L\\) by assigning \\(0_{W_L}\\) to every candidate outside \\(C_L\\).
> If there are \\(u\\in U_L\\setminus C_L\\) and \\(c_0\\in C_L\\) with \\(T_L(c_0)=0_{W_L}\\), then \\(\overline{T}_L(u)=\overline{T}_L(c_0)\\) although only \\(c_0\\) is admitted.
> Therefore the value of this zero extension alone cannot determine channel membership in every model.
> No claim of inevitable loss in each model is made.

**Source-preserving mathematical nuance:** if every admitted component term is nonzero, membership is recovered by \\(c\\in C_L\\iff\overline{T}_L(c)\\ne0\\).
This is a condition on the **component term**, not on the originally assigned quantity value.
The original distinction “absent channel ≠ admitted channel with a zero term” is unaffected.

---

## 3. Section 7.3 — Formation-finite D2 witness record completion (printed pp.25–26)

**Original issue:** 3×3 boundary-material carrier is described, but the full inherited blocked-annotation map is not stated.
The label “horizontal” for the edge joining (0,0) and (1,0) is coordinate-convention sensitive.
The source's branching claim at Stage 3 uses the **primitive regime-specific BC predicate** rather than a physical boundary law calculated from geometry.

**Proposed insertion after defining \\(S_*=\{(0,0),(1,0)\}\\):**

> Use the row-column convention for ordered grid coordinates and let \\(r_*\\) denote the nearest-neighbor edge joining the two vertices of \\(S_*\\).
> The common typed material carrier contains nine vertex items, twelve undirected nearest-neighbor edge items, and thirty-six directional boundary-slot items, totaling fifty-seven material items.
> The restricted expression \\(h_*\\) and the configuration \\(p_*\\) retain exactly the two selected vertex items, their joining edge item, and the six directional boundary slots exposed by \\(S_*\\), totaling nine active material items.
> Supply one common boundary annotation on the material records: mark those six exposed slots blocked and the remaining thirty slots transmissive; inherit the corresponding restrictions into \\(h_*\\) and \\(p_*\\).
> Both regimes have the same material records and inherited boundary annotations.
> Their primitive boundary-compatibility predicates differ because \\(L_+\\) admits the selected blocked boundary configuration while \\(L_-\\) does not.
> Consequently \\(BC_{L_+}(p_*)\\) holds and \\(BC_{L_-}(p_*)\\) fails.

**Proposed terminology change:** “their internal horizontal relation” → “their joining nearest-neighbor edge relation”.
This avoids choosing a geometrically misleading axis orientation.

**Unchanged claim:** the retained witnesses, original \\(K_{L_+}^{des}=\{p_*\}\\), \\(K_{L_-}^{des}=\varnothing\\), the absence of admitted channels on \\(L_-\\), and first branching index \\(b(L_+,L_-)=3\\).
The explicit annotation map above is a **proposed consistent completion**; it is not literally enumerated in the originally published PDF.

---

## 4. Section 8 Discussion — Fixed-J coincidence versus strict equivalence (printed p.29)

**Original issue:** “composite-level coincidence ... is therefore strictly weaker than strict formation equivalence” can be read as a universally valid logical implication comparison for an arbitrarily prescribed \\(J\\).
This reading is false.

**Proposed replacement for the two sentences beginning “By contrast, composite-level coincidence…”:**

> By contrast, composite-level coincidence under Definition 6.21 tests selected nonempty admitted-channel families under an independently prescribed linear isomorphism \\(J\\), rather than the entire candidate-level formation structure.
> Proposition 6.22 establishes that such coincidence does not imply strict formation equivalence.
> Conversely, a strict formation isomorphism transports corresponding finite composites under its **own** term map, provided that admitted channels are nonempty, but it need not produce coincidence for an arbitrary independently fixed \\(J\\).
> Because empty admitted-channel sets also fail Definition 6.21's nonempty-family requirement, the two relations do not have an unconditional implication ordering for fixed \\(J\\).
> In this structural-information sense only, agreement of selected composite outputs records less than full strict formation equivalence.

**Source-typed counterexample to the removed overstatement:** Let \\(L=M\\) be a one-channel model with term 1 and \\(W_L=W_M=\\mathbb R\\).
The descriptors are strictly formation-equivalent via identity, but under independently prescribed \\(J=-\mathrm{id}_{\\mathbb R}\\) their only nonempty full-family composites are -1 and +1, so fixed-J coincidence fails.
Also a strictly equivalent empty-channel pair has no nonempty family under Definition 6.21.
Both are compatible with Proposition 6.22's unchanged one-way nonimplication.

---

## 5. Source governance / explicit non-actions

No original PDF/Zenodo or public manuscript content is changed by this proposal.
No primitive axiom, closure rule, named theorem identifier, or original channel identity has been changed.
Any future paper revision must be section by section, with the author's approval and a separate version/diff audit.
The Section 8 replacement is a **logical-strength correction**; the Theorem 4.7 and Proposition 5.13 replacements clarify quantifier/premise scope; the D2 addition provides reproducible material-record specification and coordinate terminology.
