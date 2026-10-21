# FAS-F2-P6.11-001 — Strict base-fixed formation isomorphism iff bijective formation embedding

**2026-10-19 KST · FPA v0.1 · One bounded proposition-level source audit**  
**Scope:** Formation Axiom System F2 §6.3, Definition 6.10 (E1–E9) and Proposition 6.11, printed pp.18–19.  
**Author/source:** Kwon Dominicus, supplied `DSD_Formation_Axiom_System_EN(5).pdf`, 33 pp.  
**Verified attached PDF SHA-256:** `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.

```text
AUDIT_CASE: FAS-F2-P6.11-001
PARENT_METHOD: DSD Audit / Formal Proof Audit v0.1
PRECOMMIT_COMMIT: f782a7930206b344ae58e7eaf69e0e72be2aa9d5
PYTHON_COMMIT: 6bfa5ea887e58f2515d9da433bdea9ee6017b3b2
FINITE_JSON_COMMIT: b583d1ae5a98ad7628c19212c309372ab389f7a2
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
FPA_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
NEW_AXION_NEEDED: no
MANDATORY_MANUSCRIPT_EDIT: no
F2_FULL_PAPER: NOT_COMPLETE
INDEPENDENT_EXTERNAL_VALIDATION: not_established
ORIGINAL_PDF_AND_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-C6.12-001 / NOT_STARTED
```

## 1. Source statement and dependency locks

**Proposition 6.11** states that a strict base-fixed formation isomorphism is exactly a formation embedding whose carrier maps, quantity-kind and role maps, pointed-space maps and term-space map are all bijective.

The structural comparisons are defined between individually set-coded **full Formation descriptors** over the **same** comparison base `(B,F)`. The exact basis consists of:
- Definition 6.2: forward formation map, `(F1)–(F6)`.
- Definition 6.4: formation embedding = forward map, component injections, material-record embedding, image-reflection `(R1)–(R5)`, and the **separate witness-reflection** premise `Psi_M(f_P(p)) ⇒ Psi_L(p)`.
- Definition 6.10: strict base-fixed formation isomorphism, component bijections (pointed `I_lambda`, linear `J`) plus `(E1)–(E9)`.
- Closure IV for configuration describability, Closure VI for admitted channels, Closure VII for finite sums.

No new DSD axiom or interpretation of strict equivalence is presumed.

## 2. General mathematical proof: strict ⇒ bijective embedding

Fix a strict comparison `Phi:L→M`. Its carrier maps `Phi_M,Phi_E,Phi_P`, quantity-kind `tau_Lambda`, role `tau_R`, pointed value maps `I_lambda`, and `J` are bijective by Definition 6.10. Their component injectivity follows; `J` is an `F`-linear isomorphism. Condition E1 gives a material-record isomorphism (therefore embedding), *exact* material/active support and anchor preservation. It implies F1 and R1 after intersecting with the now-surjective material image.

E2 and E4 give F2 and R2. E3 gives F3 and R3. E6 supplies full assignment graph transport, giving F4 and R4's graph condition; E7 provides the negligible quantity-kind iff-status, size preservation and unchanged threshold, with scope **only** on the declared `Lambda_delta` domain. E8 gives F5 and R5. E9 gives F6 once the channel image is known to be admitted.

**Channel image:** E1–E8 transport every Clause VI constituent in both directions: `Des_cfg(p)`, the restricted assignment graph, and the Role predicate. As the component value/carrier/kind/role maps are bijective, the induced candidate-channel map is a bijection of `U_L` with `U_M` and restricts to a bijection of `C_L` with `C_M`. Thus E9 is well-typed and is exactly F6 on source channels.

**Witness reflection is not presumed from R2–R5.** For any target witness `(H_M,h_M)` of `Psi_M(Phi_P(p))`, surjectivity of `Phi_E` provides source candidates `H_L,h_L`; E2/E3 reflect describability, restriction and realization, while E4 reflects the configuration predicates. Hence `Psi_L(p)`. This establishes Definition 6.4's independent witness-reflection condition, not merely the apparent status agreement.

All requirements for a formation embedding are thereby satisfied and each displayed component map is bijective.

## 3. General mathematical proof: bijective embedding ⇒ strict

Now suppose `Phi:L→M` is a formation embedding and **all listed component maps are bijective**. The fixed-background typed `F1` plus bijective material-record embedding and R1 give exact `E1` material supports and anchoring. F2/R2 give E2 and E4; F3/R3 give E3. The pointed maps are bijections preserving the distinguished zero and `J` is an `F`-linear bijection, therefore its inverse is also `F`-linear.

**The delicate E5 derivation.** For each quantity kind `lambda`, the printed source defines the domain of its *partial* assignment `q_{L,lambda}` by
```text
a in Q_(L,lambda)  iff  exists v in V_(L,lambda): (a,v) in Gamma_(L,lambda).
```
R4's full graph biconditional, together with bijectivity of `I_lambda`, gives equivalence of this existential statement to
```text
exists v' in V_(M,tau_Lambda(lambda)):
   (f_M(a),v') in Gamma_(M,tau_Lambda(lambda)).
```
This in turn is `f_M(a) in Q_(M,tau_Lambda(lambda))`. Thus **E5 is a theorem-level consequence of E6 under the source's bijectivity premises**. It is *kept* in the source as an explicit status-preservation coordinate and must not be mistaken for an independent added axiom. In particular assigned `v=0` is present in the graph, whereas an undefined assignment has no graph pair; no default zero padding is permitted.

E6 is R4 itself. F4 plus R4's iff in `Lambda_delta` prove E7, while F5/R5 prove E8. Source-indexed channel membership and the term equation F6 yield E9. Channel map surjectivity again follows from full candidate-component bijections and bidirectional Clause VI, not merely from term-map surjectivity.

Hence all strict conditions E1–E9 are met without any additional primitive premise. The displayed proposition is valid relative to the source's declared background and typed isomorphism/embedding definitions.

## 4. Adversarial cases and selected finite checks (NOT a proof of universality)

The deterministic Python fixture constructs:
- One typed source full model with three material items (two assigned and one unassigned), three admitted/describable expressions with identity and proper restrictions, three configurations (two with genuine formation witnesses and one without), defined value zero, two role kinds, nontrivial restriction/realization, and **three admitted channels**.
- A renamed target model related by bijections `f_M,f_E,f_P,tau_R`, a nontrivial pointed bijection `0→0,1→20,2→10`, and the nonidentity linear isomorphism `J(t)=2t`. All nine E clauses and all embedding clauses R1–R5, witness reflection and F1–F6 are tested as true in this finite instance; its three channels correspond bijectively with transported component terms.
- **Defined zero vs undefined:** source `q(b)=0` and `q(u)` undefined; graph equivalence checked over 3 material items × 3 value candidates = **9 pairs**. A target variant deleting the assigned-zero graph edge causes E5/E6/R4 to fail and removes the corresponding channel term, preserving the *model* domain convention. This is not a counterexample to the proposition because its isomorphism/embedding hypotheses fail.
- **Non-surjective embedding:** a target extension adds an unrelated independent material/expression/configuration/channel. The original model embeds into this extension but is not strictly isomorphic by the given maps because surjectivity fails. This is a valid illustration of necessity of full bijections.
- **Bijective forward map without reflection:** make a source-unadmitted configuration admitted in the target while retaining all forward-positive source data and leaving its witness absent. The component maps can remain bijective and forward conditions can hold, but R2/E4 fail. A componentwise bijection is therefore not automatically an embedding or strict isomorphism.
- **Independent reverse transport:** inverse component bijections exist, with inverse value map zero-preserving and inverse linear term map `J^{-1}(t)=t/2`. This does not elevate the following Corollary 6.12 or Theorem 6.14 to audited status.

A separate, locally executed concise Python cross-check verified the intended representative transport, channel and graph conditions and adversarial boundary distinctions. The portable repository Python verifier and frozen JSON are *stored*; there is no claim that an independent external runner executed the committed version. The exact universally quantified proof is the mathematical derivation in Sections 2–3, not these selected toy examples.

Files:
- [Prospectively fixed obligations](FAS-F2-P6.11-001_PRECOMMIT.md)
- [Portable Python verifier](../scripts/verify_p611_strict_bijection.py)
- [Finite fixture JSON](../results/p611_strict_bijection.json)

To run from the Windows repository root:
```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_p611_strict_bijection.py
```
Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/p611_strict_bijection.json`. An optional positional command-line argument changes the output path. Python standard library only.

## 5. Audit gates / boundary

- G01 source: **PASS** — attached PDF actual SHA256 matches lock; live Zenodo byte identity unverified.
- G02 definitions/noncircularity: **PASS** — E1–E9 and F/R clauses already declared; proof does not assume P6.11.
- G03 typing and surjectivity: **PASS** — all carrier, kind, role, value and term maps covered, indexed `I_lambda` handled under `tau_Lambda`.
- G04 axiom versus closure: **PASS** — no added primitive axiom.
- G05 mathematical inference: **PASS** — both directions shown; explicitly derive E5 from graph and bijections.
- G06 uniqueness/existence: **PASS_WITH_BOUNDARY** — statement is equivalence of map classes, not assertion that every two models are isomorphic.
- G07 attack by countermodels: **PASS** — non-surjective embeddings, forward-but-not-reflecting bijections, graph-definedness mismatch examined.
- G08 finite/general separation: **PASS_WITH_BOUNDARY** — finite examples do not prove arbitrary models; committed script not independently executed.
- G09 composition/strict image: **PASS_WITH_BOUNDARY** — full strict isomorphism is stronger than coarse invariant or mere embedding.
- G10 background: **PASS** — set-coded source structures, fixed base/field, ordinary function/graph algebra.
- G11 downstream impact: **PASS_WITH_BOUNDARY** — Corollary 6.12 and Theorem 6.14 not yet audited.
- G12 validation/evidence statuses: **PASS** — author-led FPA cannot certify independent peer validation.

**Scoped conclusion:** `PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED=NONE`. The boundary denotes the *source's fixed-base full-descriptor and explicit bijectivity/reflective hypotheses*, not a missing theorem premise.

Theorem 4.7's previously noted wording clarification remains recorded. The supplied source PDF and Zenodo unchanged. F2 whole-paper audit OPEN.

**Next one-group checkpoint:** `FAS-F2-C6.12-001`, Corollary 6.12 induced channel and finite-composite preservation; status **NOT_STARTED** pending independent prospective precommit.

[Notion synchronized P6.11 audit](https://app.notion.com/p/3fe81f51e7fa815fb7ddee9623cfd92d)
