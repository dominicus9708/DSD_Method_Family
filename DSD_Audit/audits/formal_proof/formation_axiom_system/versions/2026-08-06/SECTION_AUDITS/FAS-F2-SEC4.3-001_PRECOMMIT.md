# FAS-F2-SEC4.3-001 — prospective precommit
Date: 2026-10-19. STATUS: NOT_VERDICTED. Parent: DSD Audit / FPA v0.1 / Formation F2.
SOURCE: supplied 33-page English Formation Axiom System, SHA-256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
FROZEN LOCUS: Section 4.3, printed pp.11–12 (text begins on printed p.11), exact items Corollary 4.8, Countermodel 4.9, Lemma 4.10, Corollary 4.11, Proposition 4.12, Lemma 4.13, Corollary 4.14. Source §2.1–2.2, Primitive Axioms I–III and Clause IV are dependencies.
PRIOR: FAS-F2-T4.7-001 completed with scoped PASS_WITH_REFINEMENT. That result and original manuscript wording are frozen; 4.7 clarification remains a separate suggested edit.

## Prospectively locked proof obligations and attacks
01. Corollary 4.8: prove `¬Admexpr(x) ⇒ ¬Desexpr(x)` as classical contrapositive of Axiom I; note dependence on classical logic, if relevant.
02. Countermodel 4.9: explicitly construct a primitive *full* model with admitted yet undescribable x. Catch hidden identity restriction `Admexpr(x)⇒Res(x,x)` of Axiom II; `Res=∅` is INVALID if x admitted. Check typed empty material, anchors, configurations, assignments, channel absence, supplied zero term space.
03. Lemma 4.10: from Res(H,h) and Res(h,g) deduce nested material, and anch_g = anch_H|mat(g) using source restriction `f|A=f|(A∩dom f)`. Check equal maps via domain and values. Do not infer Res(H,g).
04. Corollary 4.11: show chain induction for n=0 and n>=1; no hidden nonempty condition.
05. Proposition 4.12: independently construct a model satisfying Axioms I, II, III, V with Res(H,h), Res(h,g), ¬Res(H,g), and identities on *all admitted expressions*. Prefer an active-channel nonvacuous base alongside distinct inert expressions; verify all anchor and induced material relations. Explicitly distinguish inherited material data from membership in the primitive Res relation.
06. Lemma 4.13: combine Axiom II and III inclusions and anchor restrictions; include induced relation/annotations and exposed boundary terms only within source assumptions.
07. Corollary 4.14: verify two disjunctive obstruction cases, by contraposition of the relevant necessary conjuncts of Ψ; do not assume converse or infer `¬Desexpr(h)` for all h when only witness failure is known.
08. Full-model legality of 4.9 and 4.12: typed carriers, optional emptiness, vector space W and T, full closure IV/VI/VII; check any unstated convention needed.
09. Inspect for necessary missing manuscript premises or overstrong language; avoid inventing or repairing errors without evidence.
10. Separate math verdicts of seven source items from FPA process verdict and manuscript revision; register finite test evidence separately from general proof steps, external independent verification not claimed.
11. Independently verify finite counterinterpretations with reproducible Python standard-library validator; no source PDF edit or Zenodo update; preserve exact script path and command.
12. Stop after Section 4.3 and record next bounded step, with separate GitHub/Notion result ledger and sync state. No paper-wide F2 certificate.

## Bounded outcomes
Items audited: exact seven labeled statements of §4.3; possible math statuses PROVED_IN_DECLARED_BACKGROUND / PROOF_GAP / DISPROVED_BY_VALID_COUNTERMODEL / INDETERMINATE.
Possible process statuses PASS / PASS_WITH_BOUNDARY / PASS_WITH_REFINEMENT / FAIL / INDETERMINATE.
If a source construction is **underspecified but can be completed** under existing axioms, record CLARIFICATION_ONLY, not an axiomatic failure. A countermodel without full-model status must not be used to refute `Adm⇒Des` if it fails unrelated axioms.
