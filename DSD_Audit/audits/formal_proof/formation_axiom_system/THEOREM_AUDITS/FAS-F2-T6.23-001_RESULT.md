# FAS-F2-T6.23-001 — Layerwise obstruction to strict formation equivalence

**Date:** 2026-10-20 KST. **Method:** Established DSD Audit / Formal Proof Audit v0.1. **Authority:** Internal source-bound mathematical audit, not independent external certification.

```text
AUDIT_CASE: FAS-F2-T6.23-001
SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, 33 pages
SOURCE_PDF_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCATION: Theorem 6.23 statement, printed p.23; proof, printed p.24
SOURCE_DEFINITION: Definition 6.10, E1–E9 (printed pp.18–19)
PRECOMMIT_COMMIT: 2bc3fbb674a3e043ed3e4ad74195045162e080c1
GITHUB_PYTHON_FINAL_COMMIT: 62eca23ecf21073571d2aed17d2de3998d140c15
GITHUB_JSON_COMMIT: df907c4d2b4f28b70c496bb0c4cfec8d444bbcec
INDEPENDENT_LOCAL_CHECKER_SHA256: be5262159da834797eb98a3bac1463a87c262d8caf144a27d4cc9b164bc27921
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
F2_WHOLE_PAPER_AUDIT: OPEN
EXTERNAL_INDEPENDENT_VALIDATION: not established
SOURCE_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-C6.24-001 / NOT_STARTED
```

## 1. Source-frozen exact proposition

The exact manuscript Theorem 6.23 states:

Let `Cand(L,M)` denote all *typed tuples of candidate bijections AND isomorphisms* required by Definition 6.10. If

```text
for every Phi in Cand(L,M),
    there exists i in {1,2,...,9} with not E_i(Phi),
```

then `Sigma_L` and `Sigma_M` are **not** strictly base-fixed formation-isomorphic.

**Crucial typing:** In Definition 6.10, candidate comparison tuples already have bijective material/expression/configuration maps, kind/role maps and zero-preserving kind-indexed pointed-value maps, **plus an F-LINEAR ISOMORPHISM J of term spaces**. This is **different** from Definition 6.15's stage-comparison ambient population, where `J` is allowed to be any function until the final Stage 7. In particular, `Cand(L,M)` may be empty because of a role/carrier mismatch or because no suitable term-space linear isomorphism exists, without testing any E_i.

Definition 6.10 defines strict isomorphism exactly by the existence of one member of this candidate class satisfying **all** E1–E9. The E-conditions include E1 exact anchored material structure, E2 expression predicates, E3 restriction/realization, E4 configuration predicates and derived describability, E5 assignment domains, E6 assignment graph, E7 qualified negligible size/threshold, E8 role relation and E9 term compatibility under the induced channel bijection.

## 2. General mathematical proof, including all quantifiers

Let `P(Phi)` be the finite conjunction `E1(Phi) ∧ ... ∧ E9(Phi)`. By Definition 6.10,

```text
StrictIso_B_fix(L,M)  <=>  exists Phi in Cand(L,M) with P(Phi).
```

The theorem premise is

```text
forall Phi in Cand(L,M):
     exists i in {1,...,9}: not E_i(Phi).
```

By finite De Morgan law, `exists i not E_i(Phi)` is the negation of `P(Phi)`; by classical quantifier negation, `forall Phi not P(Phi)` is the negation of `exists Phi P(Phi)`. Consequently the theorem's premise is precisely **the logical negation of strict formation-isomorphism existence**. The stated implication is proved. The inference assumes only the ordinary declared set-theoretic/classical logical background and the source Definition 6.10, not an extra DSD axiom.

### Exact logical limits

- **Correct:** `forall Phi exists i not E_i(Phi)`.
- **Not implied:** `exists i forall Phi not E_i(Phi)`. Different candidates can fail *different* coordinates. The source does not require one uniform failed clause.
- **Incorrect:** One poorly chosen or failed candidate does NOT disprove strict isomorphism, because another candidate may satisfy all nine coordinates.
- **Empty candidate set:** The universal premise is vacuously true if `Cand(L,M)` is empty. This gives nonexistence of strict isomorphism by Definition 6.10, but does not identify any *existing* candidate's failed condition.
- **E9 evaluation:** Source E9 concerns `J(T_L(c))=T_M(hatPhi_C(c))` under a channel bijection **induced by E1–E8**. If an earlier E_i fails, the candidate already fails the all-nine conjunction; there is no need to fabricate a bijection of admitted channels or declare E9 meaningful independently in that invalid comparison. The finite checker records E9 as **not applicable** until E1–E8 hold.
- **No numeric first branch inferred:** This is the nine-coordinate condition index i, **not** the stage index `b(L,M)∈{0,...,7}` of Definition 6.15. Even with strict nonequivalence, Theorem 6.23 alone does not locate the earliest stage of collective emptiness. In particular it cannot simply equate a violated E_i with b.
- **Set/class point:** A typed candidate comparison is set-coded for each fixed pair of full descriptors. The proof's quantifier manipulations remain valid if described metatheoretically as a class of candidates; no new global ZFC "set of all full models" is required.

## 3. Selected finite source-typed full-model adversarial audit

The independent local Python checker (re-run after adding Clause VII finite-family closure; SHA256 recorded above) actually executed and returned:

```text
T6.23 PASS 7 full-model pairs 12 typed candidate comparisons
5 nonvacuous failure pairs.
```

A portable simplified self-contained repository Python was additionally committed; **its final GitHub bytes were not separately run from a fresh checkout**, so do not infer independent execution of that exact artifact. The locally executed checker and repository checker use the same seven elementary model scenarios and agree on expected candidate failures. Public artifacts: [portable verifier](../scripts/verify_t623_layerwise_obstruction.py) and [finite result JSON](../results/t623_layerwise_obstruction.json).

Each finite compared structure is a **source-typed full formation model over a fixed base with support {s0,s1} and field F2**. It has one material item, one admitted/describable expression with identity restriction and realization, one describable configuration, a singleton pointed value set {0} and defined global assignment q(a)=0 when declared, role labels, and a one-dimensional term vector space W=F2. The source-tuple roles are the only nontrivial carrier bijections (two permutations). Kind-indexed pointed maps on the singleton value set and the F2-linear term isomorphism on the one-dimensional term space are uniquely the identity; this allows **finite complete candidate enumeration within the selected signatures**, but not across all possible Formation model signatures. The checker validates primitive I/II/III/V, Closure IV/VI and the full finite-family/term Closure VII; material anchors remain fixed to the same external B in E1.

| Selected pair | Cand count | Full-model mathematical status and candidate gate |
|---|---:|---|
| Positive strict-isomorphic control | 2 | One comparison satisfies all E1–E9, while another fails E8. Therefore the universal-failure premise is false. |
| Different external-fixed anchors, same B | 2 | All fail E1; model typing and primitive axioms remain legal. |
| Defined assignment vs undefined assignment | 2 | All fail E5 and E6; 0 is a genuinely defined source value, not an automatically extended default. |
| Different qualified negligible-kind membership | 2 | All fail E7; size and threshold are supplied only for the source-declared negligible kinds. |
| Source one active role, target two, with equal role carrier size | 2 | All fail E8, illustrating **non-vacuous** failure. |
| Same role relation but incompatible supplied term T | 2 | The role-identity comparison passes E1–E8 and fails **E9**; the role-swap comparison fails E8. No one candidate survives all conditions. |
| Different role carrier cardinalities | 0 | `Cand=∅`: theorem's universal premise holds **vacuously**, no actual comparison tuple to diagnose. |

Selected source fixtures thus yield 7 model pairs, 12 typed candidate rows, 5 non-vacuous all-candidates-fail pairs, one empty-candidate pair and one positive pair.

**Quantifier inversion hostile check:** A separate **abstract** two-candidate truth table with one candidate failing only E1 and the other failing only E2 satisfies `∀Phi∃i¬E_i` but not `∃i∀Phi¬E_i`. This table is a *logical* counterexample to the erroneous quantifier swap, **not a purported full Formation model**. The source-compatible term-difference fixture independently illustrates why candidate failures can be distributed across distinct E-coordinates without relying on the abstract table.

### Reproducibility and scope

GitHub portable Python:
```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t623_layerwise_obstruction.py
```
Run from the cloned `dominicus9708/DSD_Method_Family` repository root on Windows 11. Standard library only. Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/t623_layerwise_obstruction.json`; optional first CLI argument overrides it.

**Limits:** The mathematical proof in §2 is universal because it is a direct quantified negation of Definition 6.10. The seven selected finite models verify the method boundaries and typed examples, **not** all full-model isomorphism existence decisions. The committed GitHub script is a related portable implementation of the independently executed local test, not a claim of third-party replication or post-upload execution. External independent verification has not been established.

## 4. FPA v0.1 audit gates

- G01 Source/hash: **PASS**; SHA-256 of provided 33-page PDF verified, printed pp.23–24. Not claiming Zenodo byte equality.
- G02 Exact statement and quantifiers: **PASS**; all candidate tuples (possibly empty), each fails at least one coordinate, not uniform coordinate and not merely one bad tuple.
- G03 Typed candidates: **PASS**; F-linear term-space J is an isomorphism **already** in Cand; Def 6.15 stage-J distinction maintained.
- G04 Source E1–E9: **PASS**; exact nine-coordinate conjunction as Definition 6.10, no new primitive axiom.
- G05 Logical inference: **PASS**; classical finite De Morgan and existence negation derive the conclusion with no circular premise.
- G06 Existence and definedness: **PASS_WITH_BOUNDARY**; vacuous empty-Cand case is accepted without invented failure witness; E9 guarded by E1–E8.
- G07 Adversarial: **PASS**; positive strict control, empty-Cand control, distributed failures across E8/E9, pure logical noncommuting-quantifier table.
- G08 Finite/general: **PASS_WITH_BOUNDARY**; selected finite source-typed models, not universal software verification.
- G09 Comparison-stage distinction: **PASS**; source theorem does not return minimal first-branch stage b or individual failed-E-coordinate uniform across candidates.
- G10 Mathematical background: **PASS**; ordinary set-theoretic classical logic and finite conjunction.
- G11 Downstream: **PASS_WITH_BOUNDARY**; source Corollaries 6.24/6.25/6.26 remain **NOT_REVIEWED** as individual FPA cases, despite being immediate candidates for further audits.
- G12 External evaluation: **PASS**; internal source-based review not independent external mathematical certification.

**MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND**
**DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY**
**REVISION_NEED: NONE**

The boundary is the exact Definition 6.10 typed-candidate and source full-model/fixed-base scope and the limits of finite testing. It is **not a missing inference**. Theorem 4.7's earlier **nonurgent optional scope-wording clarification** remains separately open. No source PDF/Zenodo changes, and the DSD Method Family internal 22/22 standardization count is unaffected. **Full Formation F2 manuscript FPA remains OPEN.**

**Resumable next:** `FAS-F2-C6.24-001` — Corollary 6.24 (Assignment-domain obstruction), **NOT_STARTED**. Corollaries 6.25 and 6.26 remain NOT_STARTED as separate future cases.
