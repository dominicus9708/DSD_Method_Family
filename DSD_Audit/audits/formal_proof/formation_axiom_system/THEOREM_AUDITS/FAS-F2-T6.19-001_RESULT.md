# FAS-F2-T6.19-001 — Symmetry and strict-isomorphism invariance of first branching

**Date:** 2026-10-19 KST.
**Owner:** existing DSD Audit / Formal Proof Audit v0.1.
**Scope:** One exact source theorem, not full Formation F2 manuscript certification or external peer validation.

```text
AUDIT_CASE: FAS-F2-T6.19-001
SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, 33 pp
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: Theorem 6.19, printed page 22; Definitions 6.10 and 6.15
PRECOMMIT_COMMIT: 27551ddfd2ae9d683f02d6f5eefc058be30a4e1d
PYTHON_COMMIT: 88aa62e5af39972188778aea15e8174dfd2adf17
FINITE_JSON_COMMIT: 0cc8765f4845d3ab90aaca94fa71706a61180418
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
NEW_AXION_OR_MANDATORY_SOURCE_EDIT: no
NEXT: FAS-F2-T6.20-001 / NOT_STARTED
WHOLE_F2_PAPER: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
SOURCE_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
```

## 1. Exact source theorem and declared background

**Theorem 6.19 (Symmetry and strict-isomorphism invariance of first branching)**, §6.4, printed p.22, asserts:

1. For each `0≤k≤7`, `I_k(L,M)≠∅ iff I_k(M,L)≠∅`.
2. The first branching indices `b(L,M)` and `b(M,L)` have the same definedness and, when defined, `b(L,M)=b(M,L)`.
3. When strict base-fixed isomorphisms `L'≅^fix_B L` and `M≅^fix_B M'` exist, for each k `I_k(L,M)≠∅ iff I_k(L',M')≠∅`; hence defined first branching indices agree.
4. Thus b depends only on the unordered pair of **strict formation-isomorphism classes** in the precise sense of source equivalence and symmetry.

As in Definitions 6.10 and 6.15, the compared models are **full Formation descriptors over the same fixed pair (B,F)**. Each `I_k(L,M)` is a collection of **typed full comparison tuples** `Theta=(Phi_M,Phi_E,Phi_P,tau_Lambda,tau_R,{I_lambda},J)`. The carriers/kinds/roles and each pointed `I_lambda` are source-typed bijections preserving zero; `J:W_L→W_M` is an **arbitrary function until k=7**, where it must be an F-linear isomorphism satisfying E9. Stage subsets are drawn from the same ambient space in each orientation, but oppositely oriented tuple spaces are **not literally equal sets**; their *nonemptiness profiles* are compared.

The previously audited Definition 6.10 E1–E9 and T6.14 strict equivalence relation are available as dependencies; the theorem itself is not assumed during the derivation below.

## 2. General proof of symmetry — split at the exact J boundary

Fix k≤6 and suppose `Theta∈I_k(L,M)`. Invert the original component **bijections** `Phi_M,Phi_E,Phi_P,tau_Lambda,tau_R`. For each target kind `lambda'=tau_Lambda(lambda)`, set the inverse pointed map indexed by its **target-side kind**:

```text
I^reverse_(tau_Lambda(lambda)) = (I_lambda)^(-1).
```

It remains zero-preserving, with the correct target-to-source pointed-space typing. Choose **any** map `W_M→W_L` as the reverse term-space component; in particular the **zero map** `0_(W_M→W_L)` exists because `W_L` is an F-vector space. **Do not try to invert J**, which may be noninjective, nonsurjective, nonlinear or constant before Stage 7.

The staged conditions through 6 are exact preservation-and-reflection conditions:

- Stage 0 E1: invert anchored material-record isomorphism and exact support/active structure while external Supp(B) stays fixed.
- Stage 1 E2: expression admission/describability biconditionals are symmetric.
- Stage 2 + Stage 3 E3 and primitive E4: restriction/realization and the three primitive config predicates are biconditionals. Stage 4's derived configuration describability and `K_des` are also reflected, by T6.17(ii).
- Stage 5 E5/E6: partial-assignment **domain** and graph biconditionals remain biconditionals under inverted `I_lambda`; a defined zero-value assignment cannot be mistaken for an undefined graph edge. E7 negligible-status is an iff. Its norm equality and threshold equality reverse by substitution of the inverted pointed map, **only for qualified kinds**.
- Stage 6 E8: role relation equivalence reverses under inverse carrier, kind and role bijections.

The resulting full reverse tuple is in `I_k(M,L)`, independently of whether the *original J* is invertible or linear. The construction with L,M exchanged gives the other implication.

For k=7, the original `Theta` is a strict base-fixed formation isomorphism, so J is an F-linear isomorphism. Set `J^reverse=J^{-1}` instead of an arbitrary zero map. The admitted-channel bijection induced by E1–E8 has inverse `hatTheta_C^{-1}`, and E9

```text
J(T_L(c)) = T_M(hatTheta_C(c))
```

becomes, for every `d∈C_M`,

```text
J^{-1}(T_M(d)) = T_L(hatTheta_C^{-1}(d)).
```

All Stage 7 conditions hold in the reverse orientation. Therefore **for every k∈{0,...,7}**, nonemptiness of `I_k(L,M)` is equivalent to nonemptiness of `I_k(M,L)`.

By Definition 6.15 and T6.16, `b(L,M)` is defined **iff** `I_7(L,M)=∅`. Equality of the eight emptiness indicators gives simultaneous definedness and equality of their **least** empty index. Strictly isomorphic pairs instead have undefined b on both sides — not numeric b=7 or infinity.

## 3. General proof of strict-representative invariance

Assume strict formation isomorphisms between L' and L and between M and M'. By T6.14, orient these as strict maps `A:L'→L` and `B:M→M'`. Let `Theta∈I_k(L,M)`. Compose carrier, expression, configuration, kind, role and indexed pointed-space maps to obtain the **full** comparison tuple

```text
Theta' = B ∘ Theta ∘ A : L' → M'.
J_Theta' = J_B ∘ J_Theta ∘ J_A.
I^Theta'_lambda =
    I^B_(tauLambda^Theta(tauLambda^A(lambda)))
      ∘ I^Theta_(tauLambda^A(lambda))
      ∘ I^A_lambda .
```

All component bijections and zero-preservation conditions remain satisfied, with the kind indexing as shown. **At k≤6**, `J_Theta` was merely a map: composition with the (linear isomorphic) `J_A,J_B` produces a correctly typed **arbitrary** map. Requiring it to be linear before Stage 7 would incorrectly shift the source's first-branching boundary.

The strictness of A and B transports every E1–E8 predicate/relation graph iff, anchored material-record datum and qualified E7 norm/threshold through both intermediate models. Consequently every stage requirement P0,…,Pk satisfied by Theta is satisfied by `Theta'`. At k=7 all three term-space maps are F-linear isomorphisms, and channel term compatibility E9 composes through the two intermediate channel bijections. Thus `Theta'∈I_k(L',M')`.

Conversely, compose an arbitrary `Theta'∈I_k(L',M')` with `A^{-1}:L→L'` and `B^{-1}:M'→M` to obtain an element of `I_k(L,M)`. This supplies **both implications** and proves equal nonemptiness of each stage. Their least-empty indices — conditional on definedness — agree. The theorem does not assert canonical isomorphisms between representatives, or equality of their raw differently typed sets `I_k`.

Combining this invariance with stagewise symmetry shows b is well-defined on unordered **strict** formation-isomorphism class pairs when the compared classes are distinct in the source's sense.

## 4. Selected finite test and hostile boundaries — separate from general proof

[Prospective source-locked precommit](FAS-F2-T6.19-001_PRECOMMIT.md) · [Python verifier](../scripts/verify_t619_symmetry.py) · [Finite JSON](../results/t619_symmetry.json).

An independent local standard-library Python fixture was actually executed. The byte-for-byte matching 9,400-character Python source was also committed to the repository; a *fresh remote checkout run* has not been separately verified. It uses **small source-typed toy Formation comparisons**, not an exhaustive set of arbitrary full Formation models: one material item, two candidate expressions, one configuration, one quantity kind with `{0,1}` pointed values and qualified size, one role, F2 vector-space terms (xor addition) of dimension 1 or 2, and consistent partial graph/role/term identity in the selected cases.

It reconstructs **nine** source-target pairs: first branch 0 (anchors), 1 (expression), 2 (restriction), 3 (realization), 5 (assignment including defined zero), 6 (role), 7 (different term-space dimensions), plus two strict-isomorphic cases (empty channels and one admitted **nonzero-term** channel) whose b is undefined. Its typed representative replacements use distinct carrier/kind/role labels and preserve anchored base s0. Stage profiles are computed by enumerating source-typed bijections and **all finite arbitrary J maps** before Stage 7, then separately evaluating linearity and E9 at Stage 7.

| Finite result | Count/observation |
|---|---:|
| Source-typed selected model pairs | **9** |
| Stagewise bidirectional nonemptiness equivalences | **72/72** |
| Stagewise strict representative-relabeling invariances | **72/72** |
| Explicit reversed full comparison-tuple witnesses | **358** |
| Cases featuring a noninvertible J surviving through Stage 6 | **3** |
| Earliest branches sampled | **0,1,2,3,5,6,7, undefined** |
| Stage-7 first failure with W dimension 1 vs 2 | Both directions fail at Stage 7 |
| Strict-isomorphic nonzero channel-term case | Survives Stage 7 in both directions |

For **every individual** surviving local comparison tuple at stage k, the fixture verifies a reverse witness at the same k. Before Stage 7 it assigns a **zero reverse J**, including deliberately **nonbijective** source J; at Stage 7 it constructs the actual inverse J. Each representative renaming is also checked as strict in both appropriate orientations before stage profiles are compared. These checks are stronger than just verifying b on nine samples, but remain selected finite tests.

**Guardrails:** Theorem 6.19 does NOT assert that an arbitrary forward map's J has an inverse, that an embedding which is not strict may be used to replace a representative, or that equal numerical composites imply strict structural isomorphism. The fixture uses a single pointed quantity kind, so it is not a standalone exhaustive numerical test of multi-kind reindexing; the typed general proof above explicitly covers the `tau_Lambda` dependency.

Windows 11 command from the `dominicus9708/DSD_Method_Family` cloned repository root:

```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t619_symmetry.py
```

Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/t619_symmetry.json`, optional first positional argument overrides output path. Standard-library Python only.

## 5. FPA audit gates, verdict and checkpoint

- G01 source identity: **PASS** — 33-page supplied PDF hash `8856fc...` matches; Zenodo byte equality not asserted.
- G02 exact theorem scope: **PASS** — all stages 0–7, both definedness/symmetry and strict representative replacement, fixed B,F.
- G03 types/inverse J: **PASS** — inverse carrier/kind/role/pointed bijections; **zero J for pre-Stage7**, true inverse F-linear J only at Stage7.
- G04 primitive/closure: **PASS** — original E1–E9 and definitional Stage4; no extra primitive axiom.
- G05 mathematical inference: **PASS** — reverse and conjugation constructions given for each k with converse.
- G06 definedness/existence: **PASS_WITH_BOUNDARY** — b defined only where I7 empty, stagewise nonemptiness not literal set equality.
- G07 adversarial: **PASS** — noninvertible pre7 J and typed inverse indexing, strictness of class representatives separately examined.
- G08 finite/general: **PASS_WITH_BOUNDARY** — 9 finite selected models cannot certify all Formation structures.
- G09 invariant meaning: **PASS** — result is invariant under **strict** base-fixed isomorphism and symmetric in two arguments; not under arbitrary embeddings.
- G10 declared background: **PASS** — ordinary function/vector-space operations and comparison-tuple collection.
- G11 downstream: **PASS_WITH_BOUNDARY** — no promotion of Theorem 6.20 static closure to audited status.
- G12 external status: **PASS** — internal source audit not independent external mathematical certification.

**MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND**
**DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY**
**REVISION_NEED: NONE**

The boundaries are fixed-base full Formation descriptors, *strict* representative equivalence, the pre/post Stage-7 difference for J, conditional b definedness, and finite testing limitations. They are **not** hidden added assumptions or a source proof gap.

Historical Theorem 4.7 optional claim-scope wording clarification stays open, unchanged. Neither attached source PDF nor Zenodo was edited. Method Family 22/22 internally standardized status unchanged; F2 full-manuscript FPA still OPEN.

**Next prospective case:** `FAS-F2-T6.20-001` — Theorem 6.20 **Static formation closure**, NOT_STARTED.

[Notion synchronized T6.19 FPA result](https://app.notion.com/p/3fe81f51e7fa810fa32afcf4a8825294)
