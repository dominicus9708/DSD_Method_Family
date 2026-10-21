# FAS-F2-P6.3-FORWARD-001 — Independent source-bound audit of Proposition 6.3

**Date:** 2026-10-21 KST. **Source author:** Kwon Dominicus. **Method:** existing DSD Audit / Formal Proof Audit v0.1, not third-party certification.

## 1. Source and provenance

- Original immutable attachment: \`DSD_Formation_Axiom_System_EN(5).pdf\`, 33 pages, sha256 \`8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a\`.
- Original Definition 6.2 at printed p.15 and Proposition 6.3 plus source proof at printed p.16. The original and previously audited T6.5 use identical definitions (F1–F6). Source language explicitly says "**If** the induced channel map is injective" for the finite-set composite equality; no necessity or converse is claimed.
- [Prospective precommit](FAS-F2-P6.3-FORWARD-001_PRECOMMIT.md): commit \`120a592360c871e000a3ddc7345e18830238acf5\`, fixed before the finite testing.
- [Published reproducibility Python](../scripts/verify_p63_forward_preservation.py): commit \`16e60dfcc7ffbc947678c53568eb98ef88d1255f\`, verified GitHub blob \`86cd52c82afed8f192fc6ff3138e03150e6b6fc4\`; 8722-byte self-contained standard-library variant with six named Formation fixture pairs and 16 finite channel-set cases.
- [GitHub structured evidence summary JSON](../results/p63_forward_preservation_summary.json): commit \`4bef093f893a5c7ba7a82342a44b5bfe87faa0a5\`, verified GitHub blob \`43b7c18d9de4ffb9b0ffa06c42320073acfcbf5e\`.
- **Execution provenance boundary:** The locally executed **fuller** source-bound verifier (12,309 bytes, locally tested with \`python -W error -m py_compile\` and \`python -W error\`) reported six fully typed fixture model pairs and sixteen finite-family checks. Its local SHA256 is \`015276ecd094450b1ee3f072cb1e9ab96d4d7abae47f4bb736cff87aebf9b404\`, its local full JSON SHA256 \`5a478bfaa669fe8018431455297fcd2974c45ec9b6e92b1917261cf4d10d50bf\`. The **GitHub-published 8,722-byte script is a compact equivalent-scope implementation, not byte-identical to the locally executed fuller verifier**; execution of the exact published build has NOT yet been independently re-established in this container. Therefore do not call the GitHub summary or script a byte-for-byte executed output pair. Mathematical verdict below rests on direct proof, and finite-case evidence on the explicitly executed local verifier.

## 2. Locked original source statement and correct type scope

For a forward Formation map \`Phi:L→M\` between full models over fixed (B,F), with typed maps \`(f_M,f_E,f_P,tau_Lambda,tau_R,{I_lambda},J)\` satisfying Definition 6.2 (F1–F6):

(1) \`Psi_L(p) => Psi_M(f_P(p))\` for source candidate configuration p;

(2) \`f_M[A*_L] ⊆ A*_M\`;

(3) \`c ∈ C_L => PhiHat(c) ∈ C_M\`, where \`PhiHat(p,a,lambda,v,rho)=(f_P(p),f_M(a),tau_Lambda(lambda),I_lambda(v),tau_R(rho))\`;

(4) if \`PhiHat|C_L\` is injective, then every finite source channel **set** \`F⊆C_L\` satisfies \`J(Comp_L(F)) = Comp_M(PhiHat[F])\`.

No global source-to-target equality \`K_L→K_M\`, reverse image inclusion, injective f_M, or automatic full-family composite preservation in the noninjective case is asserted.

## 3. Independent general proof without downstream Theorem 6.5 / 6.8

### P02 — configuration witnesses

Unfold original Closure IV: \`Psi_L(p)\` requires the three configuration predicates and source expressions \`H,h\` with \`Res_L(H,h)∧Desexpr_L(h)∧Realize_L(h,p)\`. By F2 all four primitive predicate truths are preserved on the corresponding images. F3 preserves both restriction and realization edges; F1 guarantees material/anchor support compatibility on those target images. Therefore \`(f_E(H),f_E(h))\` witnesses \`Psi_M(f_P(p))\`. This proof uses **forward implications only**, no reflectivity.

### P03 — active material image

By Closure IV, every \`p∈K_L^des\` has \`f_P(p)∈K_M^des\` as just proved. F1 states \`f_M[act_L(p)]⊆act_M(f_P(p))\`. Therefore

\`\`\`text
f_M[A*_L]
 = f_M[union_{p ∈ K_L^des} act_L(p)]
 = union_{p ∈ K_L^des} f_M[act_L(p)]
 ⊆ union_{p ∈ K_L^des} act_M(f_P(p))
 ⊆ union_{p' ∈ K_M^des} act_M(p') = A*_M.
\`\`\`

The set-image/union equality is valid even for noninjective maps and empty K_L. The target may have extra describable configurations and active material.

### P04–P05 — admitted channel image and legal term evaluation

For \`c=(p,a,lambda,v,rho)∈C_L\` Closure VI means \`p∈K_L^des\`, \`(a,v)∈Gamma_L,lambda(p)\`, and \`Role_L(p,a,lambda,rho)\`. The graph is **local** to p: it additionally entails \`a∈act_L(p)\` while the underlying partial q_\`lambda\` is regime-global. P02 maps p to \`K_M^des\`; F1 sends its active a into \`act_M(f_P(p))\`; F4 sends \`(a,v)\` to \`(f_M(a),I_lambda(v))∈Gamma_M,tau(lambda)\` **globally**, and the F1 inclusion upgrades this to the target **local** graph for f_P(p). F5 maps the role. All three target VI conditions hold: \`PhiHat(c)∈C_M\`.

Only **after** this membership proof is F6's \`T_M(PhiHat(c))\` a well-typed component-term application. F6 asserts \`J(T_L(c))=T_M(PhiHat(c))\` for all admitted source c. In particular, neither absent candidate channels nor undefined terms are padded with zeros.

### P06 — finite set composites and exactly needed injectivity

For finite \`F⊆C_L\`, linearity and F6 yield

\`\`\`text
J(Comp_L(F))
 = J(sum_{c∈F} T_L(c))
 = sum_{c∈F} J(T_L(c))
 = sum_{c∈F} T_M(PhiHat(c)).
\`\`\`

When \`PhiHat\` is injective on **this F**, the terms on the right biject with the elements of the target *set* \`PhiHat[F]\`, with no repeated image; hence this sum equals \`Comp_M(PhiHat[F])\`. The source's **global** injectivity on \`C_L\` suffices simultaneously for every F. No unconditional infinite-sum issue occurs; these are finite sums.

## 4. Legal adversarial models and exact strengthening boundaries

**Noninjective, nonzero countermodel to dropping the proviso.** Fix a one-support-point base and empty internal material relations, scalar F=R, term W_L=W_M=R, a pointed assignment value 0 and one kind/role. In source L let material \`{a,b}\`, expression h and describable configuration p each use \`{a,b}\`, admitted identity restriction \`Res(h,h)\`, realization \`Realize(h,p)\`, all three configuration gates true, q_L(a)=q_L(b)=0, and roles \`Role(p,a,lambda,r)\`, \`Role(p,b,lambda,r)\`. There are two distinct admitted channels c_a,c_b, with \`T_L(c_a)=T_L(c_b)=1\`. In target M collapse a,b to x by \`f_M(a)=f_M(b)=x\`, with corresponding h',p', q_M(x)=0, role \`Role(p',x,lambda,r)\`, and one admitted channel d with \`T_M(d)=1\`. Choose identity maps on expression, configuration, quantity kind, role and pointed values, and \`J=id_R\`. All F1–F6 hold, including per-channel \`J(T_L(c_a))=J(T_L(c_b))=T_M(d)=1\`, but for \`F={c_a,c_b}\`:

\`\`\`text
J(Comp_L(F)) = 2;
Comp_M(PhiHat[F]) = Comp_M({d}) = 1.
\`\`\`

This is **NOT** a counterexample to original Proposition 6.3 (its injectivity hypothesis fails). It refutes only the stronger proposed theorem without that hypothesis.

**Global injectivity sufficient but not necessary.** Repeat the same full model collapse with all source and target component terms zero. The induced channel map remains noninjective, yet every finite family's sum and its image-set sum both equal zero. More generally, source F6 gives for any finite F

\`\`\`text
J(Comp_L(F)) - Comp_M(PhiHat[F])
 = Σ_{d∈PhiHat[F]} (multiplicity_F(d)-1) T_M(d).
\`\`\`

Thus for **all finite source sets F**, equality holds iff every image d with at least two distinct source preimages has \`T_M(d)=0\`. Necessity follows using just F containing two distinct channels mapping to d; sufficiency follows term-by-term. This is an additional *derived audit observation*, not a source-rewrite or an original theorem of §6.2. For one selected F, injectivity restricted to F is also only sufficient, not always necessary.

**Forward preservation is not reflection.** A valid source model with admitted but undescribable h, no realization, and candidate p with gates true may have \`Psi_L(p)=false\`, \`A*_L=empty\`; its valid forward target may additionally make h describable with a realization, so \`Psi_M(f_P(p))=true\` and \`A*_M≠empty\`. The forward axioms permit this, and do not imply target-to-source reflection. A separate target extra assigned material/role is also permitted while preserving all source roles and assignments.

**Empty channel domain.** With describable configurations and q-domain empty, both models can have C=empty. Their only finite composite is \`Comp(empty)=0_W\`; the source theorem remains meaningful and F6 is vacuous. This is not an absent channel carrying an actual zero term.

## 5. Bounded code evidence and replay

A locally executed more detailed full-model checker validated source primitive soundness, required admitted identity restrictions, realization and anchor inheritance, partial global q, closure IV–VII, all Definition 6.2 forward clauses and finite set-composite calculations for **6 legal source–target model pairs, 16 source finite-family choices**. Sample results:

| Scenario | Source channels | Target channels | Finite source families | Outcome |
|---|---:|---:|---:|---|
| two nonzero source channels collapse | 2 | 1 | 4 | F1–F6 true; image-set composite 2 vs 1 for full F |
| two injective channels, J(x)=2x | 2 | 2 | 4 | 4/4 finite-family equalities |
| noninjective collapsed zero channel | 2 | 1 | 4 | 4/4 equal despite noninjectivity |
| no reflected describability | 0 | 0 | 1 | only forward implication holds |
| describable, no assigned channels | 0 | 0 | 1 | Comp(empty)=0 |
| target has additional admitted channel | 1 | 2 | 2 | 2/2 source-family equalities |

The archived **GitHub** reproducer covers the same six source-scope boundary scenarios, but was authored as a compact variant; because the current container did not run that exact published blob byte-for-byte, a GitHub-script execution attestation is **not** asserted. The separate **GitHub** JSON is explicitly a test result *summary* drawn from the locally executed case group, not necessarily the exact stdout/full JSON from that compact variant. The full locally executed JSON is at \`/mnt/data/DSD_Audit/audits/formal_proof/formation_axiom_system/results/p63_forward_preservation.json\` (local artifact only). A subsequent independent run of the published GitHub script can remove this tooling provenance boundary.

Windows 11, from the existing checked-out \`DSD_Method_Family\` repository root:

\`\`\`powershell
python .\\DSD_Audit\\audits\\formal_proof\\formation_axiom_system\\scripts\\verify_p63_forward_preservation.py
\`\`\`

Expected generated JSON by this published script: \`DSD_Audit/audits/formal_proof/formation_axiom_system/results/p63_forward_preservation.json\`. Optional first positional CLI argument overrides the location. Standard library only.

## 6. FPA judgement and project checkpoint

\`\`\`text
AUDIT_CASE: FAS-F2-P6.3-FORWARD-001
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE (original Proposition 6.3)
COUNTEREXAMPLE_TO_ORIGINAL_CLAIM: no
COUNTEREXAMPLE_TO_UNQUALIFIED_FINITE_COMPOSITE_TRANSPORT: yes
SOURCE_WIDE_DIRECT_MATH_LABELS_AUDITED: 52/52 (14 theorem, 16 proposition, 14 corollary, 2 lemma, 6 countermodel)
DEFINITIONS_TYPED_REVIEWED: 12/12
REMARK_SOURCE_ITEM_REVIEWS_PENDING: 5
F2_FULL_MANUSCRIPT_AUDIT: OPEN
EXTERNAL_INDEPENDENT_VALIDATION: not_established
PUBLIC_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-G5-REMARK-SCOPE-001 / NOT_STARTED
\`\`\`

Previously recorded, independent source-language advisories remain unresolved by this theorem: T4.7 residual-six qualification, §7.3 D2 boundary inheritance, §8 fixed-J comparison phrase, and P5.13 zero-extension universal-scope wording.

**Important distinction:** every *numbered mathematical claim* now has recorded source-bound audit coverage, but this does not constitute theorem-prover certification, proof-dependency closure, correction of the four scope advisories, prose Remark reviews, independent external vetting, or a full-F2 manuscript-wide PASS. The next source task should check the five Remarks one by one, not invent new theorem numbers.