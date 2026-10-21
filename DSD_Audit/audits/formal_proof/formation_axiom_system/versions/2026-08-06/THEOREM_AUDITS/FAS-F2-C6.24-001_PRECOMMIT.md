# FAS-F2-C6.24-001 — prospective audit precommit

Date: 2026-10-20 KST. Established DSD Audit / Formal Proof Audit v0.1, bounded to original Corollary 6.24.

Primary source: Kwon Dominicus, `DSD_Formation_Axiom_System_EN(5).pdf`, 33 pp, SHA-256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`. Source locus: §6.5 printed p.24: **Corollary 6.24 (Assignment-domain obstruction)**; source Definition 6.10 E5/E6 printed p.19 and Primitive Axiom V printed pp.7–8. Prior T6.23 proved source conditional obstruction; C6.24 NOT_STARTED before prospective lock.

**EXACT locked source statement**: “If no candidate material and quantity-kind bijections preserve every assignment domain, then no strict base-fixed formation isomorphism exists.”

## Frozen source obligations

1. Formalize `f:M_B^L→M_B^M`, `τ:Λ_L→Λ_M` bijections, `Q_{L,λ}⊆M_B^L`, `Q_{M,τλ}⊆M_B^M`:
   `D(f,τ) ⇔ ∀λ∀a[a∈Q_{L,λ} ⇔ f(a)∈Q_{M,τ(λ)}]`, equivalently `f[Q_{L,λ}]=Q_{M,τλ}`.
   The antecedent is `¬∃(f,τ)D(f,τ)` over **all typed candidate bijection pairs**, not “some f fails,” not necessarily a single uniformly bad (a,λ).
2. By Definition 6.10, strict isomorphism supplies such bijections and requires **E5=D(f,τ)**. Its absence is sufficient contradiction. Cross-check E6 full graph preservation with bijective pointed maps implies E5 because domain is graph projection; but do not assert E5 is independent under full E6.
3. Examine vacuous empty candidate pairs (differing carrier/kind cardinality), nonvacuous all-fail pairs with same carrier/kind cardinalities, and positive pairs where one f,τ preserves all domains even if other candidates fail.
4. Construct two legitimate full Formation models over same fixed B and scalar field, with primitive I/II/III/V and derived IV/VI/VII. Use at least two material items a,b and two quantity kinds λ,μ; one describable config with act={a,b}; zero pointed values; in L domains Qλ=Qμ={a}; in M Qλ={a},Qμ={b}. Their total number of assigned graph edges and per-kind domain cardinalities coincide but the **per-material domain-incidence degrees** (2,0) vs (1,1) differ, an invariant under any (f,τ).
5. Include role labels/relation identical and nonempty, full C/T and Comp through Closure VI/VII; ensure global q and defined-zero vs undefined are distinguished, no illegal local assignments or q-domain outside A*. Set anchors equal on a,b so even f-swaps do not automatically fail E1: isolate E5 as obstruction.
6. Exhaustively enumerate all `2!×2!=4` material and kind bijection pairs, document each offending (a,λ) or domain image, check no E5 and no E6. For one positive target identical to L, show **at least one** candidate passes, without inferring strictness from E5 alone.
7. Test a designated actual strict-isomorphic positive fixture with identical remaining structure and chosen term-space F-linear identity, to refute the invalid implication “one failing candidate pair ⇒ strict non-equivalence”.
8. Test empty-Cand vacuity separately without claiming an E5 witness or independent domain obstruction diagnosis.
9. Distinguish comparison of domain incidence vs comparison of counts, aggregate channel sums, or extra role data. Do not broaden to E7, E8, E9 or claim the first branching b is exactly 5 unless earlier stages are explicitly audited.
10. Run portable standard-library Python in the existing FPA scripts folder, commit JSON in canonical results, test executable code locally before upload if possible, and describe any GitHub fresh-checkout execution limit precisely.
11. Outcome categories: MATHEMATICAL_VERDICT / FPA_VERDICT / REVISION_NEED, source and external validation independently; F2 paper-wide OPEN, unchanged PDF/Zenodo, historical T4.7 optional clarification maintained. Do not certify C6.25/C6.26 without separate precommits.

Prospective verdicts: MATHEMATICAL_VERDICT ∈ {PROVED_IN_DECLARED_BACKGROUND, DISPROVED_BY_VALID_COUNTERMODEL, PROOF_GAP, INDETERMINATE}; FPA_VERDICT ∈ {PASS, PASS_WITH_BOUNDARY, PASS_WITH_REFINEMENT, FAIL, INDETERMINATE}; REVISION_NEED ∈ {NONE, CLARIFICATION, ASSUMPTION, PROOF, THEOREM, DEPENDENCY_REAUDIT, UNDETERMINED}.

NEXT if this audit closes: `FAS-F2-C6.25-001` — Role obstruction, NOT_STARTED.
