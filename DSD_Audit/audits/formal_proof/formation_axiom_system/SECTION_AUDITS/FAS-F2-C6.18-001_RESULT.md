# FAS-F2-C6.18-001 — Closure-stage exclusion / 폐포 단계 최초 분기 제외

2026-10-19 KST. Existing DSD Audit / FPA v0.1. Internal source-bound mathematical review, NOT independent external certification.

## Locked audit and verdict

- Source: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, supplied 33-page attachment.
- Checked SHA-256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a.
- Source: Section 6.4, Corollary 6.18 (Closure-stage exclusion), printed p.22, Definition 6.15 and Theorems 6.16–6.17.
- Audit ID: FAS-F2-C6.18-001.
- Precommitted prospective criteria: commit 0ebf06c9eb674ee991f22f624a7efe357c6b94d8.
- Portable Python script: commit 68d5d74807c76b44128432c2da48669d4114c1dd.
- Supplemental finite JSON: commit 0c8a538c95fea74e9742de8d211f1afa918035eb.
- MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND.
- DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY.
- REVISION_NEED: NONE.
- Whole F2 manuscript: OPEN. Independent external validation: not established. Original PDF/Zenodo: unchanged.
- NEXT: FAS-F2-T6.19-001 / NOT_STARTED.

## Exact original statement

The source's Corollary 6.18: Whenever the first branching index is defined, b(L,M) is not equal to 4. A Stage-4 failure would already be a Stage-3 failure; configuration describability cannot be the first independent comparison obstruction when all Stage-3 material is preserved and reflected.

Source Definition 6.15 constructs the comparison sets I0,...,I7 using the SAME ambient population of typed full comparison tuples for full formation descriptors over fixed (B,F). Source Theorem 6.16 states nestedness and that b(L,M) is defined as the MINIMUM index k in 0,...,7 for which Ik is empty, ONLY when I7 is empty. Source Theorem 6.17(ii), already independently mathematically audited, gives the stronger equality I3(L,M)=I4(L,M). This proof uses the prior theorem as a premise, not the desired corollary.

## General mathematical proof

Assume b(L,M) is defined. Suppose toward contradiction that b=4. By the definition of MINIMUM, I4(L,M) is empty, while ALL earlier I0,I1,I2,I3 are nonempty. In particular I3 is nonempty.

But Theorem 6.17(ii) says I3=I4 for every pair of full fixed-base formation descriptors under the source comparison construction. Hence I3 nonempty implies I4 nonempty. Contradiction. Therefore b is not 4.

Equivalent formulation: if I4 is empty, so is I3. A first empty stage cannot be 4. This is elementary finite-index set reasoning after the nontrivial input I3=I4 has been established. It is NOT a new formation axiom. A strict-isomorphic pair has I7 nonempty and b UNDEFINED; do not identify that case with any numeric branch index.

Stage 0 is the source's special anchored-background/ambient-typing bookkeeping index, not an eighth formation stage. The corollary does not exclude branches 0,1,2,3,5,6,7 and does not itself certify invariance or symmetry of b (Theorem 6.19 remains unreviewed).

## Finite and adversarial checks

The finite check has two explicitly separate evidence categories.

First, all abstract nested profiles of ambient candidate sets of sizes n=0,1,2,3 are enumerated. Assign to each candidate one of nine outcomes (first discarded at k in 0,...,7, or retained through k=7). There are 1+9+81+729 = 820 nested profiles. Of these, 1+8+64+512 = 585 satisfy EXACT equality I3=I4; none has first branch b=4.

If ONLY nestedness is required without I3=I4, b=4 is possible in 71 of these nested profiles. For example the one-candidate profile of stage cardinalities (1,1,1,1,0,0,0,0) is nested and b=4, but violates I3=I4. Thus nestedness ALONE cannot prove C6.18. These hypothetical profiles are NOT legal countermodels satisfying the source's full formation closure assumptions.

Second, the earlier Theorem 6.16 finite full-model comparison record was actually fetched from its existing canonical GitHub result JSON and checked for all eight fixture pairs. Every pair satisfies equal Stage3/Stage4 cardinalities (the original stage-set script also asserts set equality); its b is 0,1,2,3,5,6,7 or undefined for the strict-isomorphic pair. Those are REUSED previous source-typed fixtures, not eight newly audited real-world instances. The 820 abstract profiles and reused eight typed fixtures do not constitute a census of all full formation models.

Local abstract profile enumeration was executed using Python, with counts independently reproduced through JavaScript when constructing the JSON and inspecting the prior GitHub fixture. The committed portable Python script was NOT separately executed from a fresh checkout after upload because direct raw GitHub download was inaccessible in the runtime. This distinction is part of the audit record.

Dependencies and reproducibility links:
- Prospective precommit: FAS-F2-C6.18-001_PRECOMMIT.md in this SECTION_AUDITS folder.
- Portable Python: ../scripts/verify_c618_closure_exclusion.py
- Finite JSON: ../results/c618_closure_exclusion.json
- Reused T6.16 typed fixture: ../results/t616_first_branching.json

From cloned DSD_Method_Family repository root on Windows run:

    python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c618_closure_exclusion.py

The script requires the already-existing results/t616_first_branching.json at its canonical path. It emits results/c618_closure_exclusion.json by default, or the caller's optional first positional output path.

## Gate audit

- G01 source/version PASS: 33-page attached PDF SHA checked. Zenodo byte identity not claimed.
- G02 source dependency PASS: use definition 6.15 and previously audited T6.16/T6.17, no circular invocation of C6.18.
- G03 type/quantifiers PASS: fixed (B,F), full source descriptors, one ambient full-comparison-tuple collection; b only when I7 empty.
- G04 original closure discipline PASS: derived Stage4 is not a free independent parameter.
- G05 proof PASS: minimality contradicts exact equality I3=I4. Nestedness alone is explicitly insufficient.
- G06 definedness PASS_WITH_BOUNDARY: strict-isomorphic pairs have undefined b, not a numeral.
- G07 adversarial PASS: a nested-only b=4 abstract profile deliberately violates T6.17 and is not a Formation theorem countermodel.
- G08 finite/general PASS_WITH_BOUNDARY: 820 abstract profiles and eight reused typed fixtures supplement the general proof but cannot prove all models.
- G09 scope PASS: collective emptiness of all comparison tuples, not early failure of one map.
- G10 mathematical background PASS: ordinary finite-set minimum and equality.
- G11 dependencies PASS_WITH_BOUNDARY: T6.19 first-branch symmetry/invariance NOT_REVIEWED.
- G12 validation PASS: author-led FPA not independent review.

Final verdict is PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE. Boundary denotes precise full-model and conditional-definedness assumptions plus selected finite test limitations, not a missing proof step.

Historical T4.7 wording-scope clarification recommendation remains unchanged. Method Family internal standardization remains 22/22. No PDF or Zenodo edits. Whole-F2 FPA remains OPEN.

Next scoped audit: FAS-F2-T6.19-001, symmetry and strict-isomorphism invariance of first branching, NOT_STARTED. Start with a NEW prospective precommit and inspect reversed kind-indexed value maps and why J is arbitrary before Stage 7, but invertible at Stage 7.
