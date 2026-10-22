# PA-P5-P7-20260901-COMPARISON-001 — maps, stage branching, finite summary audit

**Execution date:** 2026-10-22 KST. Manuscript author Kwon Dominicus.
Source locked `DSD_Property_Axiom_System_EN(4).pdf`, 23 pages, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Prospective case lock:** [P5_P7_COMPARISON_PRECOMMIT.md](P5_P7_COMPARISON_PRECOMMIT.md), commit `bf2eabcb4dbfb5030c466f1646ec9264e5b0e21c`.
**Summary verdict: P5 requires TWO source-level typing/claim clarifications; P6 and P7 core arguments supported with the stated background and caveats. No source document was changed.**

## P5-A. Genuine forward-map quantifier / typed-product boundary — §§2.3–2.4 vs Definition 6.1, printed pp7–8,12–13

The paper **explicitly permits** a property kind to be declared even when its profile is unavailable (Definition 2.5: no applicability, prerequisite or assignment coordinate is required in that case). Definition 2.4 defines the input product `X_A,varpi` **only when** every sort in the profile is supplied.

Definition 6.1 requires auxiliary-sort carrier maps **only for sorts available in A** and F1 says such source sorts must be available in B, but then F3 says **“For every varpi∈Pi_A”** a product map
`phi_varpi:X_A,varpi→X_B,varpi` preserves applicability. F4 and F5 implicitly reference the same missing typed products/domains without reiterating source profile availability.

**Concrete allowed-core witness exposing missing guard:**
- One auxiliary sort u; candidate kind varpi with profile (u), value carrier `{0}`, no prerequisites; fixed inherited Stage-VI background otherwise arbitrary.
- A declares varpi: `Pi_A={varpi}`, but does **not** supply `Xaux_A(u)`. This is explicitly permitted by Definition 2.5. Thus `X_A,varpi`, `Ap_A,varpi`, `Xi_A,varpi` are **not defined**, and the two primitive axioms quantify only over declared-and-available kinds, so A has a valid C1-complete full model status “profile unavailable”.
- The *identity* should be a forward map by Proposition 6.2, but its F3 obligation **as literally universally phrased for every declared kind** invokes a nonexistent product map `phi_varpi`. Without an implicit availability guard, F3 is ill typed and the all-model category is not well defined.

**Finding `P5-A = SOURCE_SCOPE_CLARIFICATION_REQUIRED`.** This does NOT prove that the intended category theorem is false if F3–F5 are understood to quantify only over source-declared **and available** property profiles. It means the guard should be explicit in Definition 6.1, Definition 6.3's input-level obligations, and wherever Definition 6.7 inherits those conditions. With this guard, the standard identity/composition and embedding-reflection proofs appear valid.

## P5-B. “strict isomorphisms are exactly bijective embeddings” overstates carrierwise bijectivity — Definition 6.7/Theorem 6.8, printed p14

The source's own strict-isomorphism definition requires:
- (S1) all *defined* auxiliary carrier maps bijective;
- (S2) available auxiliary-sort sets **equal**;
- (S3) declarations `Pi_A=Pi_B`;
- (S4) embedding conditions in **both directions** under inverses.

Theorem 6.8 says “Equivalently, strict property isomorphisms are exactly the bijective property embeddings.” Componentwise bijectivity of carrier maps, by itself, does **not** imply (S2) or (S3) under the one-way F1/F2 conditions.

**Concrete two-core legal counterinterpretation for missing S3:**
- Shared signature has `Saux={u}`, candidate `varpi` with profile (u), value carrier `{0}`, no dependencies. Both A and B supply `Xaux(u)={x}`.
- A declares no kinds (`Pi_A=∅`), B declares varpi (`Pi_B={varpi}`) with `Ap_B,varpi=∅` and the empty partial assignment. Both satisfy PI, PII and C1; all shared inputs are typed.
- Forward embedding A→B has the one carrier component `phi_u=id_{ {x} }` **bijective**; (F1/F2) hold, (F3–F5) and per-source reflection obligations are vacuous. Thus it is an embedding whose **every component map is bijective**, but **S3 fails**. Hence it is not strict and has no two-way inverse as a property morphism.
- Independent availability failure of S2: take A with no auxiliary u supplied and no declared property; B with u supplied and no declared property. The empty component-map family A→B is vacuously componentwise bijective, but available-sort sets differ.

**Finding `P5-B = CLAIM_WORDING_CORRECTION_REQUIRED`** under the natural componentwise reading of “bijective embedding.” The strictly specified S1–S4 notion itself is coherent, and strict isomorphism **does** form an equivalence relation under identity/inverse/composition; this is *not* a counterexample to that equivalence claim.
**Minimal suggested replacement:** “Strict core property isomorphisms are precisely the property embeddings having bijective maps on every available auxiliary carrier, identical available auxiliary-sort sets, identical property declaration sets, and the corresponding two-way preservation/reflection conditions.” Alternatively explicitly define a stronger term *bijective property embedding* including S2–S3. Update corresponding compressed claims in the paper's Abstract and Theorem 11.1(7), which currently inherit the shortened implication.

## P5-C. Other structural results, conditional on the scope repair

- Proposition 6.2 F1–F5 forward-map identities/composition: standard set-inclusion/value transport argument **once defined-product obligations are guarded by availability**.
- Proposition 6.4 embedding identity/composition: true for injectivity and fully source-typed biconditional reflection.
- Theorem 6.6 inclusion-submodel preorder: true via inclusion map identities/transitivity.
- Theorem 6.8 strict-isomorphism equivalence: standard true **with S1–S4 intact**; abbreviated “exactly bijective embeddings” needs the clarification above.
- Proposition 6.9: C1 completed coordinates preserved because they are functions of the reflected primitive data.
- Theorem 6.11: representation-inclusive strict equivalence inherits identity/inverse/composition from a strict core bijection and full encoding compatibility.

The previous finite forward-map-chain CI success only tests an available-profile case and cannot expose P5-A/B.

## P6. Stage comparisons §§7–8, printed pp15–17

Definition 7.1 compares *all* bijection families respecting visible source data, not a hand-picked candidate map. Stage comparison sets are nested. Since every Stage-5 coordinate is functionally defined from Stages ≤4 by C1, `I4=I5` and **Stage 5 cannot be an independent first branch**. These general statements are supported by source-level dependency arguments and presume property comparison is well typed as above.

Source constructions:
- Construction 8.5: declared-varpi vs undeclared-varpi with equal carrier => `bprop=2`.
- Construction 8.6: two unary property applicability sets that cannot be matched by a single carrier bijection => `bprop=3`.
- Construction 8.7: full applicability same, but incompatible second value table after first pins both points => `bprop=4`.
- Corollary 8.8: no independent Stage-5 witness.

Existing source-specific CI runner `39733865420` on Python 3.10 and 3.12 passed 7/7 tests each, checking first-branch comparison counts in the stored deterministic data:
```text
b=2: I1=1, I2=I3=I4=I5=0
b=3: I1=2, I2=2, I3=I4=I5=0
b=4: I1=2, I2=2, I3=2, I4=I5=0
```
These are *finite concrete witness results*. They do not replace the general Stage-5 proof.
**P6 verdict: SUPPORTED_WITH_P5_TYPE_GUARD_DEPENDENCY.**

## P7. Finite summary, optional encoding, and information loss — §§5,9, printed pp12,17–18

Definition 9.1's summary retains property labels and, per property, only domain size/zero/nonzero counts. Construction 8.7 yields two property-finite models with two declared properties; each has domain size two, one zero and one nonzero value. Summaries coincide, yet preserving property 1 forces the input bijection to be identity and then property 2 differs. Theorem 9.2's **existence of equal summary with nonisomorphic full cores** is mathematically supported. Existing CI compression test and optional-representation separation passed in both Python versions.

**Interpretation qualifier, source §9.2:** it states “Aggregate equality is consequently weaker than strict property equivalence unless a reconstruction theorem is supplied.” Since the downstream bridge `Theta_A` and its aggregate outputs are **external supplied data** not constrained in the property core, this should not be read as a universal implication `strict iso⇒equality under arbitrary independently fixed bridges`. A safely delimited form is: “Equality of a selected aggregate alone does not generally imply strict property equivalence; additional source-aware injectivity/equivariance data are required for any stronger statement.” This is an **editorial scope caution** (not an additional formal theorem in this PDF).

**P7 verdict: FINITE_NONCLASSIFICATION_PROVED / AGGREGATE_SCOPE_NOTE_OPEN.**

## Combined verdict and next gate

```text
CASE: PA-P5-P7-20260901-COMPARISON-001
P5_FORWARD_MAP_PROFILE_UNAVAILABLE_GUARD: CLARIFICATION_REQUIRED
P5_BIJECTIVE_EMBEDDING_S2_S3_CONDITIONS: CLAIM_WORDING_CORRECTION_REQUIRED
P5_STRICT_EQUIVALENCE_RELATION_UNDER_S1_S4: SUPPORTED
P6_I4_EQUALS_I5_AND_FINITE_BRANCHES: SUPPORTED_WITH_P5_TYPED_SCOPE
P7_SUMMARY_COLLISION: SUPPORTED
P7_ARBITRARY_DOWNSTREAM_AGGREGATE_ORDERING: SCOPE_NOTE_OPEN
SOURCE_TEX_EDIT: none
PDF_OR_ZENODO_EDIT: none
GENERAL_PROPERTY_FPA: OPEN
EXTERNAL_INDEPENDENT_VALIDATION: not_established
NEXT: PA-P8-20260901-DEPENDENCY-MANUSCRIPT-REVIEW-001 / NOT_STARTED
```

Do not treat two necessary repairs as reasons to discard the original general Property Axiom System or the predecessor axis-specific source. No user PDF, source code, or Zenodo record was altered.
