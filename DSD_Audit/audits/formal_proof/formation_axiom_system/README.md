# Formation Axiom System — F2 / FPA audit case

**CASE_STATUS:** IN_PROGRESS_G0_SEC4_3_THEOREMS_3_3_3_6_4_5_4_7_6_5_6_8_6_14_6_16_6_17_PROPOSITION_6_11_AND_COROLLARIES_6_6_6_7_6_12_6_18_COMPLETED  
**DATE:** 2026-10-19  
**SUBJECT_CLASS:** FOUNDATIONAL_THEORY  
**OWNER_METHOD:** DSD Audit  
**PROTOCOL:** [FPA v0.1](../../../protocols/mathematics/FORMAL_PROOF_AUDIT_v0.1.md)  
**MATHEMATICAL_STANDARD:** ordinary mathematics, typed set-theoretic reasoning with declared ZFC-relative scope  
**INDEPENDENT_VALIDATION:** not established  

Files:
- [SOURCE_LOCK.md](SOURCE_LOCK.md) — identified attached PDF edition, 33 pages, SHA-256; Zenodo byte identity explicitly unverified.
- [PROOF_OBLIGATIONS.md](PROOF_OBLIGATIONS.md) — Section 2 G0 base audit, three theorem-level cases and seven Section 4.3 source items reviewed; remaining claims NOT_REVIEWED.
- [EXECUTION_PLAN.md](EXECUTION_PLAN.md) — first action Theorem 3.3; resumable checkpoint and downstream impact.
- [Shared theorem-audit template](../../../templates/FORMAL_PROOF_AUDIT_TEMPLATE.md).

The first theorem-level FPA audit completed: [Theorem 3.3 precommit](THEOREM_AUDITS/FAS-F2-T3.3-001_PRECOMMIT.md) and [Theorem 3.3 result](THEOREM_AUDITS/FAS-F2-T3.3-001_RESULT.md): relative unique closure, mathematical `PROVED_IN_DECLARED_BACKGROUND`, FPA `PASS_WITH_BOUNDARY`, no mandatory revision. This is an internal source-bound review, not independent validation or the full-paper F2 verdict.

Do NOT pre-populate `THEOREM_AUDITS/` with invented pass results. Create a theorem audit file when that theorem's audit actually begins. Preserve old source and audit history; this case does not alter the Formation original or re-open 22/22 internal method-family completion.

NOTION FPA hub: https://app.notion.com/p/3fe81f51e7fa81afb612fa69387cdeee
NOTION Formation case: https://app.notion.com/p/3fe81f51e7fa811a9645d2c684661296

NOTION completed T3.3 audit: https://app.notion.com/p/3fe81f51e7fa815698c1df6ab625ad8c
LATEST: [Theorem 4.5 precommit](THEOREM_AUDITS/FAS-F2-T4.5-001_PRECOMMIT.md), [proof audit result](THEOREM_AUDITS/FAS-F2-T4.5-001_RESULT.md), [finite verifier](scripts/verify_t45_countermodels.py) and [deterministic output](results/t45_axiom_independence.json). MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND; FPA: PASS_WITH_BOUNDARY; no mandatory manuscript change. NOTION: https://app.notion.com/p/3fe81f51e7fa811eb18ff1e5428d7fb2
NEXT: FAS-F2-T6.19-001 — Theorem 6.19 branching symmetry/strict-isomorphism invariance, NOT_STARTED. Other F2 obligations remain open.

LATEST FPA AUDIT: [Theorem 4.7 precommit](THEOREM_AUDITS/FAS-F2-T4.7-001_PRECOMMIT.md) and [Theorem 4.7 result](THEOREM_AUDITS/FAS-F2-T4.7-001_RESULT.md). Six residual clauses each have a counterinterpretation satisfying the other five: `PROVED_IN_DECLARED_BACKGROUND` under **residualized** premises, FPA `PASS_WITH_REFINEMENT`, `REVISION_NEED=CLARIFICATION`. Manuscript "other primitive axioms" needs precise rewording; it cannot include the omitted clause's parent axiom unaltered. [Python](scripts/verify_t47_residual_clauses.py) · [JSON](results/t47_residual_clauses.json). [Notion T4.7 audit](https://app.notion.com/p/3fe81f51e7fa8182ac05f470ddc5c0d9).


LATEST SECTION AUDIT (2026-10-19): [§4.3 precommit](SECTION_AUDITS/FAS-F2-SEC4.3-001_PRECOMMIT.md), [§4.3 seven-item result](SECTION_AUDITS/FAS-F2-SEC4.3-001_RESULT.md), [finite verifier](scripts/verify_sec43.py), [deterministic output](results/sec43_witnesses.json). Verdict `PROVED_IN_DECLARED_BACKGROUND` for these seven source items / `PASS_WITH_BOUNDARY`, with optional Countermodel 4.9 identity-restriction explanation, no mandatory manuscript edit. [Notion audit](https://app.notion.com/p/3fe81f51e7fa81c88b4dfc5f7e936d7d). Theorem 4.7's prior wording clarification remains separately tracked; no silent change to original PDF.


LATEST FOUNDATION AUDIT (2026-10-19): [Section 2 prospective precommit](SECTION_AUDITS/FAS-F2-G0-001_PRECOMMIT.md), [Section 2 mathematical audit](SECTION_AUDITS/FAS-F2-G0-001_RESULT.md), [coordinate-erasure verifier](scripts/verify_g0_stage_reductions.py), [120/36 deterministic JSON](results/g0_stage_reductions.json). Mathematical Proposition 2.5 `PROVED_IN_DECLARED_BACKGROUND`; Definitions 2.1–2.4 are internally coherent with the declared typed conventions (definitions are not independent theorems). FPA `PASS_WITH_BOUNDARY`; class-map/set-function and arbitrary well-typed vs full-model truncation are optional explanatory refinements, **no mandatory theorem/axiom revision**. [Notion G0 audit](https://app.notion.com/p/3fe81f51e7fa81448c14ebbd7c0dc292). All post-standardization reviews are internal, not externally independently verified. Existing Zenodo source remains unmodified.


LATEST COMPLETED THEOREM AUDIT (2026-10-19): [Theorem 3.6 precommit](THEOREM_AUDITS/FAS-F2-T3.6-001_PRECOMMIT.md), [Theorem 3.6 proof audit result](THEOREM_AUDITS/FAS-F2-T3.6-001_RESULT.md), [reproducible Python](scripts/verify_t36_formation_traces.py) and [deterministic JSON](results/t36_trace_witnesses.json). Mathematical verdict PROVED_IN_DECLARED_BACKGROUND; FPA PASS_WITH_BOUNDARY; revision NONE. 8/8 finite fixtures, 21 typed candidate equivalences, 3 singleton-composite checks. Full paper remains OPEN. External replication remains unestablished. NEXT FAS-F2-SEC6.2-C6.6-C6.7-001 / NOT_STARTED.

Notion T3.6 completed audit: https://app.notion.com/p/3fe81f51e7fa81c98284ca75776ab8f9


LATEST COMPLETED MAP-ALGEBRA AUDIT (2026-10-19): [Theorem 6.5 precommit](THEOREM_AUDITS/FAS-F2-T6.5-001_PRECOMMIT.md), [Theorem 6.5 result](THEOREM_AUDITS/FAS-F2-T6.5-001_RESULT.md), [finite Python](scripts/verify_t65_forward_composition.py), [JSON](results/t65_forward_composition.json). VERDICT: PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE. Embedding composition proof includes explicit R1 intersection identity, indexed I-lambda, and witness-reflection two-step. Noninjective forward-map example correctly demonstrates why finite set-aggregate preservation requires separate injectivity. F2 whole-paper audit OPEN; external independent validation not established. NEXT short proof unit: FAS-F2-SEC6.2-C6.6-C6.7-001 / NOT_STARTED.

Notion T6.5 completed audit: https://app.notion.com/p/3fe81f51e7fa8130b7fbe2ebe7f43b53


LATEST SECTION 6.2 COROLLARY AUDIT (2026-10-19): [C6.6 and C6.7 precommit](SECTION_AUDITS/FAS-F2-SEC6.2-C6.6-C6.7-001_PRECOMMIT.md), [result](SECTION_AUDITS/FAS-F2-SEC6.2-C6.6-C6.7-001_RESULT.md), [Python](scripts/verify_c66_c67.py) and [JSON](results/c66_c67_category_preorder.json). Both source corollaries: PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE. Mathematically establish category axioms, wide subcategory and inclusion-submodel preorder. Finite source-legal empty-expression witnesses show 494 identity, 1,152 associativity, 288 embedding compositions, 4 reflexivity, 20 transitivity; finite tests are not general mathematical proof. Five theorem-level FPA audits plus this pair of corollaries. F2 full-paper OPEN; independent external validation not established. **LATEST NEXT: FAS-F2-T6.8-001 / NOT_STARTED**. Earlier historical NEXT statements remain as checkpoints of earlier epochs.

Notion completed C6.6/C6.7 audit: https://app.notion.com/p/3fe81f51e7fa81fdbccef571bee0537b


LATEST FPA THEOREM 6.8 (2026-10-19): [Prospective T6.8 obligations](THEOREM_AUDITS/FAS-F2-T6.8-001_PRECOMMIT.md), [general proof audit](THEOREM_AUDITS/FAS-F2-T6.8-001_RESULT.md), [portable Python](scripts/verify_t68_embedding_reflection.py), [selected finite witnesses](results/t68_embedding_reflection.json). `PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE`. Eight typed source candidate-channel membership checks and four finite-subset compositions passed in local sample; admissible target-only channel and invalid-without-witness-reflection adversarial case retained. Six theorem-level audits complete. Full F2 paper audit OPEN; no independent external review or manuscript change. Current NEXT FAS-F2-P6.11-001 / NOT_STARTED. Historic earlier NEXT fields are not active instructions.

Notion synchronized T6.8 completed audit: https://app.notion.com/p/3fe81f51e7fa812f83c3c7cc3bd5266d


LATEST STRICT-COMPARISON FPA (2026-10-19): [P6.11 prospective precommit](THEOREM_AUDITS/FAS-F2-P6.11-001_PRECOMMIT.md), [P6.11 mathematical audit result](THEOREM_AUDITS/FAS-F2-P6.11-001_RESULT.md), [portable finite verifier](scripts/verify_p611_strict_bijection.py), [finite check JSON](results/p611_strict_bijection.json). Both implications from source E1–E9 and F1–F6/R1–R5, including independent witness reflection and graph-derived E5, are `PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE`. Three admitted source channels, 9 partial-graph candidate pairs, legal defined zero vs undefined and adversarial failures of bijectivity/reflection. A separately constructed local concise Python test passed; no claim of independent rerun of the committed code. **Six** audited theorem-level cases, **one** proposition-level P6.11 case, two separately reviewed C6.6/C6.7, Section 2 G0 and Section 4.3 seven-item group. Full F2 remains OPEN; latest next P6.11→**C6.12 / NOT_STARTED**. Historical NEXT fields are retrospective only.

Notion synchronized P6.11 case: https://app.notion.com/p/3fe81f51e7fa815fb7ddee9623cfd92d


LATEST COMPLETED COROLLARY AUDIT (2026-10-19): [C6.12 precommit](SECTION_AUDITS/FAS-F2-C6.12-001_PRECOMMIT.md), [C6.12 general mathematical proof](SECTION_AUDITS/FAS-F2-C6.12-001_RESULT.md), [portable finite checker](scripts/verify_c612_channel_composites.py), [recorded finite crosscheck](results/c612_channel_composites.json). PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE for strict-isomorphism induced channel bijection, bijection of finite subset families and J-linear finite sum transport. 32 candidate comparisons, 3 admitted channels, 8 inverse-family and 8 composite checks in independent local interface crosscheck (not all primitive full model axioms), 1 nonempty cancellation. Earlier history preserved. **CURRENT NEXT FAS-F2-T6.14-001 / NOT_STARTED**; F2 whole-paper OPEN and no external independent certification.

Notion synchronized C6.12 result: https://app.notion.com/p/3fe81f51e7fa81db92b8d2386b5b6cee


LATEST STRICT EQUIVALENCE THEOREM FPA (2026-10-19): [T6.14 source-locked precommit](THEOREM_AUDITS/FAS-F2-T6.14-001_PRECOMMIT.md), [T6.14 mathematical audit](THEOREM_AUDITS/FAS-F2-T6.14-001_RESULT.md), [portable selected finite checker](scripts/verify_t614_strict_equivalence.py), [finite JSON](results/t614_strict_equivalence.json). Mathematical `PROVED_IN_DECLARED_BACKGROUND`, FPA `PASS_WITH_BOUNDARY`, revision `NONE`. Reflexivity/symmetry/transitivity checked at all E1–E9 levels. **Important:** inverse value maps must be indexed by target quantity kind, and E7 negligible-status/norm/threshold, E9 channel/linear term transport cannot be suppressed. Three model finite experiment: 3 identities, 15 E1–E9 checks, 6 inverse identities, 16 finite channel subsets, 32 composite equalities, selected invalid-premise cases. Selected finite checks supplement general proof; committed code not independently externally rerun. Seven audited theorem-level cases total. F2 paper-wide remains OPEN; **latest NEXT FAS-F2-T6.16-001 / NOT_STARTED**. Older NEXT fields are history only.

Notion synchronized F2 Theorem 6.14 source-bound audit: https://app.notion.com/p/3fe81f51e7fa81219ecaebac9522c311


LATEST FPA THEOREM 6.16 (2026-10-19): [source-locked precommit](THEOREM_AUDITS/FAS-F2-T6.16-001_PRECOMMIT.md), [mathematical result](THEOREM_AUDITS/FAS-F2-T6.16-001_RESULT.md), [executed reproducible Python verifier](scripts/verify_t616_branching.py), [deterministic JSON](results/t616_first_branching.json). `PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE` for I_(k+1)⊆I_k, I7 nonempty iff strict formation isomorphism, and conditional least branching index b∈{0,...,7}. Local in-session source-typed finite exhaustive ambient comparison tests: 8 cases / 56 staged inclusions; indices 0,1,2,3,5,6,7 and strict b undefined; even strict-isomorphic pair may have early failing *individual candidates*. J is arbitrary until Stage 7. Stage 4 nonbranching I3=I4 observed only on fixtures, its general theorem T6.17 NOT_STARTED. No whole-paper F2 validation or external independent certification. **LATEST NEXT FAS-F2-T6.17-001 / NOT_STARTED**, historical NEXT entries remain retrospective.

Notion synchronized Theorem 6.16 source-bound FPA audit: https://app.notion.com/p/3fe81f51e7fa81b88d06d901cd345200


LATEST COMPLETED FPA T6.17 (2026-10-19): [prospective precommit](THEOREM_AUDITS/FAS-F2-T6.17-001_PRECOMMIT.md), [complete mathematical proof audit](THEOREM_AUDITS/FAS-F2-T6.17-001_RESULT.md), [locally executed Python](scripts/verify_t617_closure_nonbranching.py), [JSON](results/t617_closure_nonbranching.json). PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE. Claims (i) Stage4/6/7 unique **relative to supplied Role,W,T**, (ii) **general** I3=I4, (iii) I6 bijective candidate/admitted channel transport, (iv) I7 bijective finite-family and finite-composite preservation all audited separately. Finite selected fixture: 72 carrier/expression/config bijection triples, 1 valid I3+I4, 72 candidate channel membership equivalences, 4 finite composites. This **upgrades previous finite-only I3=I4 observation** to the source-bounded general proof, not C6.18's own completed audit. Nine theorem-level audits complete. F2 whole-paper OPEN, independent external verification not established. CURRENT NEXT FAS-F2-C6.18-001 / NOT_STARTED; earlier historical NEXT labels remain provenance.

Notion synchronized F2 Theorem 6.17 audit: https://app.notion.com/p/3fe81f51e7fa81c0a65dcb1005d56f71


LATEST FPA COROLLARY 6.18 (2026-10-19): [locked precommit](SECTION_AUDITS/FAS-F2-C6.18-001_PRECOMMIT.md), [general source-bounded derivation](SECTION_AUDITS/FAS-F2-C6.18-001_RESULT.md), [portable Python](scripts/verify_c618_closure_exclusion.py), [finite JSON](results/c618_closure_exclusion.json). PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE: if b defined and b=4, minimum yields I3 nonempty but I4 empty, contradicting Theorem 6.17 I3=I4. Adversarial checks: 820 abstract nested profiles, 585 satisfying I3=I4 (zero b4); 71 violating equality demonstrate nestedness alone insufficient. Reused earlier source-typed 8 T6.16 fixtures, all no b4. GitHub script not independent post-commit rerun. Nine theorem-level audits; four separately audited corollaries C6.6/C6.7/C6.12/C6.18, and P6.11. Full F2 paper OPEN, source PDF/Zenodo unchanged, no external independent audit. CURRENT NEXT FAS-F2-T6.19-001 / NOT_STARTED. Older NEXT entries historical only.

Notion synchronized C6.18 full source-bound audit: https://app.notion.com/p/3fe81f51e7fa81349f77dc0038377ba6
