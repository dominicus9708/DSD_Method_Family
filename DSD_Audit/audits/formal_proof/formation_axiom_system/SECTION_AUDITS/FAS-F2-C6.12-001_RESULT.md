# FAS-F2-C6.12-001 — Induced channel and finite-composite preservation (FPA result)

**2026-10-19 KST · Formal Proof Audit v0.1 · Source-bound internal mathematical review, not independent external verification**

```text
AUDIT_ID: FAS-F2-C6.12-001
OWNER_METHOD: DSD Audit (existing method)
SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, printed page 20 of 33
ATTACHED_SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: Corollary 6.12, Definition 6.10 (E1-E9), Closure Clauses VI-VII
PRECOMMIT_COMMIT: 61e06af98797f0217e7093c9bf431bbe4b1ec99b
PORTABLE_PYTHON_COMMIT: 0e3fffc9b8d2ca3f8aeb7f8bdf225696424cee48
FINITE_JSON_COMMIT: 03f0b2e3ffc2f86915f3074af61dd5e04a9c7b83
COROLLARY_MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
NEW_AXIOM_OR_HYPOTHESIS_REQUIRED: no
F2_FULL_PAPER: NOT_COMPLETE
INDEPENDENT_EXTERNAL_VALIDATION: not_established
ORIGINAL_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-T6.14-001 / NOT_STARTED
```

## 1. Source statement and exact scope

The frozen PDF's original **Corollary 6.12 (Induced channel and composite preservation)** says: every *strict base-fixed formation isomorphism* induces bijections `hatPhi_C:C_L -> C_M` and `F -> hatPhi_C[F]` on admitted channels and finite channel families; and, for all `F in Dcomp_L`, `J(Comp_L(F))=Comp_M(hatPhi_C[F])`.

- `C_L` is the admitted-channel set defined by Closure Clause VI.
- `Dcomp_L=P_fin(C_L)` is the set of **finite subsets** (not lists/multisets) defined by Clause VII. `C_L` itself need not be finite.
- `T_L:C_L -> W_L` is the supplied component-term map. `J:W_L -> W_M` is an `F`-linear isomorphism in Definition 6.10; E9 requires `J(T_L(c))=T_M(hatPhi_C(c))`.
- This conclusion holds for **strict isomorphisms**, not every forward map, not every non-surjective embedding, and not merely two models with equal composite values.

## 2. General mathematical proof (separate from finite computational checks)

**Channel bijection.** Definition 6.10 provides bijections `Phi_P, Phi_M, tau_Lambda, tau_R`, and for each source kind `lambda`, `I_lambda:V_L,lambda -> V_M,tau_Lambda(lambda)` bijective and zero-preserving. Consequently the componentwise induced candidate map

```text
hatPhi(p,a,lambda,v,rho)
 = (Phi_P(p),Phi_M(a),tau_Lambda(lambda),I_lambda(v),tau_R(rho))
```

is a well-typed bijection `U_L -> U_M`. To invert a target channel candidate, first invert `tau_Lambda` to determine the correct source kind, then invert its indexed `I_lambda`; invert the remaining typed component maps.

Closure VI defines admission as the conjunction of source configuration describability, local assignment-graph membership, and role membership. Conditions E1-E8, especially E2-E4 (describability and witnesses), E5-E6 (assignment graph including definedness), and E8 (Role), preserve and reflect *each* conjunct. Therefore for every `c in U_L`,

```text
c in C_L  iff  hatPhi(c) in C_M.
```

Hence the candidate bijection restricts to a bijection `hatPhi_C:C_L -> C_M`. It is not merely an injection of the source channels, and no target-only admitted channel can remain outside the image under a strict comparison.

**Finite-family bijection.** For `F in P_fin(C_L)`, define `P_fin(hatPhi_C)(F)=hatPhi_C[F]`. Images of finite sets are finite; injectivity of `hatPhi_C` ensures the image-set operator is injective; surjectivity ensures every finite target family is the image of its finite inverse image. The inverse is explicitly `G -> hatPhi_C^{-1}[G]`. Both empty and nonempty finite families are included.

**Composite preservation.** For an arbitrary finite `F subset C_L`, Clause VII, `F`-linearity of `J`, E9 and the channel injection yield

```text
J(Comp_L(F))
 = J(sum_{c in F} T_L(c))
 = sum_{c in F} J(T_L(c))
 = sum_{c in F} T_M(hatPhi_C(c))
 = sum_{d in hatPhi_C[F]} T_M(d)
 = Comp_M(hatPhi_C[F]).
```

The penultimate equality needs injectivity to avoid accidentally treating collisions in a multiset as an ordinary set. The empty family satisfies `J(0_WL)=0_WM`; nonzero positive and negative component terms can cancel, without weakening channel identity. A channel with an assigned numerical value of zero is still present if Clause VI admits it, whereas a candidate without a defined assignment is absent. No new value-to-term algebraic rule is needed.

This is a general deduction in the declared typed set-theoretic and vector-space background, matching the source's printed proof. It does not rest on software enumeration.

## 3. Adversarial finite crosschecks and limitations

- [Prospectively fixed attack criteria](FAS-F2-C6.12-001_PRECOMMIT.md)
- [Portable Python source](../scripts/verify_c612_channel_composites.py)
- [Internal finite crosscheck JSON](../results/c612_channel_composites.json)

The finite fixture models just the **typed Clause VI/E1-E9 interface**, with candidate configurations, material items, two quantity kinds with correctly indexed value bijections (both mapping 0 to 0), and two roles. It is *not* an independent full-model certification of Primitive Axioms I-III/V or all Stage IV witness data. A separate local Python crosscheck on the same interface passed; the committed GitHub version has not been independently rerun.

Results from the local interface crosscheck:

| Check | Outcome |
|---|---|
| Typed source candidates, reflected into target candidates | **32/32** |
| Admitted channels on each side | **3**, matched bijectively |
| Finite channel families on each side | **8** (=2^3) |
| Inverse finite-family images | **8/8** |
| Finite composite identities under `J(x)=2x` over `R` | **8/8** |
| Nonempty zero-sum family | **1** verified |
| Channel with assigned value 0 | Present as an admitted channel |
| Deliberate loss of role reflection | Target admitted channels increase to **4**, so the strict-isomorphism premise fails |

The hostile boundary is **not** a countermodel to Corollary 6.12: when role reflection fails, E8 is violated, so the map is no longer strict. Under the source's strict conditions, an extra admitted target channel cannot appear.

The finite test cannot prove the universal quantified corollary. The complete mathematical proof is above; the emitted JSON represents a source-clause interface exercise only. Neither the artifact nor the author-led FPA constitutes external independent replication.

Run from the root of the cloned `dominicus9708/DSD_Method_Family` repository on Windows:

```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c612_channel_composites.py
```

Output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/c612_channel_composites.json`. An explicit first CLI positional argument overrides that output path.

## 4. Audit gates, verdict, continuation

- G01 source: PASS, 33-page PDF SHA-256 verified locally; Zenodo byte identity not checked.
- G02 source dependencies: PASS, E1-E9, Clause VI/VII and P6.11 referenced explicitly; no circular use of C6.12.
- G03 typed/bijection: PASS, indexed value maps and full candidate U inverse handled.
- G04 primitive versus definitional: PASS, no new axiom inserted.
- G05 channel and family proof: PASS, admission biconditionals and powerset inverse explicit.
- G06 existence/uniqueness: PASS_WITH_BOUNDARY, conditional existence of a *given strict isomorphism*; no assertion that arbitrary descriptors are isomorphic.
- G07 adversarial cases: PASS, role-reflection removal is outside strict premise; noninjective forward-map collision barred by component bijection.
- G08 finite/general boundary: PASS_WITH_BOUNDARY, local finite clause-interface only, not full model verification.
- G09 maps/invariants: PASS, structural strict equivalence is stronger than mere equality of composite outputs.
- G10 background: PASS, fixed (B,F), ordinary finite-set and linear algebra.
- G11 downstream impact: PASS_WITH_BOUNDARY, **Theorem 6.14 NOT_STARTED** and no whole-paper certificate.
- G12 independent audit: PASS, internal author's project verdict not external validation.

**Final scoped verdict:** `PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED=NONE`. The boundary is the exact strict-isomorphism/fixed-base/finitely supported family premise and finite-test limitation; it is **not** a missing proof obligation.

Earlier **Theorem 4.7** statement-scope clarification remains a distinct recorded issue. Frozen F2 PDF and Zenodo unchanged. **Stop this two-stage (mathematical derivation + finite supplement) corollary unit under timeout-prevention rule.** Next: `FAS-F2-T6.14-001`, Theorem 6.14 strict formation equivalence as an equivalence relation, NOT_STARTED. F2 full-manuscript FPA remains OPEN.

[Notion synchronized C6.12 source-bound audit](https://app.notion.com/p/3fe81f51e7fa81db92b8d2386b5b6cee)
