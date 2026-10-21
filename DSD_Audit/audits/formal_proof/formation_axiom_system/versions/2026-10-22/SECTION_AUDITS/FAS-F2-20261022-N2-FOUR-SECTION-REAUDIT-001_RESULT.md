# FAS-F2-20261022-N2-FOUR-SECTION-REAUDIT-001 — New-source four-section mathematical re-audit

**2026-10-22 KST · Original source author: Kwon Dominicus.**
**Important:** this record applies **only** to the 34-page user-uploaded English PDF \`DSD_Formation_Axiom_System_EN(7).pdf\`, printed date **2026.10.22**, SHA256 \`af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe\`.
It is an independently labelled review of the corrected source, not a recasting of any 2026-08-06 \`PASS\` verdict.
The original 2026-08-06 33-page paper, SHA256 \`8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a\`, and its FPA records remain separately archived.

## 1. Version lock and execution provenance

- [New-version prospective N2 precommit](FAS-F2-20261022-N2-FOUR-SECTION-REAUDIT-001_PRECOMMIT.md): commit \`a21f95a49f355209a42b7a04c20417f10ddc4309\`, committed **before** new local finite checks.
- Source inspected directly: §4.2 Theorem 4.7 at new printed p11; §5 Proposition 5.13 p14; §7.3 D2 model at pp26–27; §8 Discussion at p29, with Definition 6.21/Proposition 6.22 pp23–24, Theorem 6.16 p21, Corollary 6.12 pp19–20, and §9 Conclusion p30.
- [Actual standard-library Python](../scripts/verify_n2_four_sections.py) was **executed** under \`python -W error -m py_compile\` and \`python -W error\`, resulting in \`ALL_SELECTED_ASSERTIONS_PASS\`.
  - Final Python 12,788 bytes; SHA256 \`06218533b3bf38072edf7a09fbaa5315a3f938f2006aaf8c97f0f3914bd48380\`; Git blob \`562cad9ae7399c8c81b64c793f0afea43c7a726d\`; final code commit \`dbeadbaa148e1638e21c56f2f341bc10320c0983\`. Actual local source Git blob **equals** GitHub fetched blob, after strengthening the boundary-record inheritance assertion and rerunning both checks.
  - [Exact generated new-version JSON](../results/n2_four_sections.json) 3,746 bytes; SHA256 \`4ee1a38e0e1eab76df8cfa14ed15513592db8cd53a8d47317b2c744a3d8a35db\`; Git blob \`844113c067a9c487607663dd7d39b738264a2b8d\`; commit \`1607f64f2016cbd4b0bc8925b88fae6c28a9dfe8\`. The SHA and Git blob are identical to the *actual produced local JSON*. Fixed output stayed unchanged after strengthening the executable D2 inheritance check.
- These are **selected finite structural tests**, not automated proofs of universal quantified theorems. The independent source-level arguments below establish their intended logical scopes.

## 2. Corrected §4.2 Theorem 4.7 (printed p11)

**Source states:** six residual constraints (i)–(vi) of Primitive I, II, III, V, after Proposition 4.6's typing-induced dependencies are factored out, are each independent **of the other five residual constraints** in the equivalent residualized presentation over the fixed typed background.

### General source logic
The six named clauses are:
1. \`Desexpr(x) ⇒ Admexpr(x)\`;
2. anchored restriction soundness \`Res(H,h) ⇒ anch_h = anch_H|mat(h)\`;
3. restriction-target admission \`Res(H,h) ⇒ Admexpr(h)\`;
4. identity restriction on every admitted expression;
5. anchored realization soundness \`Realize(h,p) ⇒ anch_p = anch_h|act(p)\`;
6. the global assignment-domain inclusion \`Q_L,lambda ⊆ A*_L\`.

Under the paper's fixed set-theoretic domain and induced-material-record conventions, Proposition 4.6 already derives subset inclusions from the equality of anchor-map domains, along with induced type/incidence inheritance and global single-valuedness from function declaration. They do not constitute additional independent residual clauses.

For each j, the source's active-kernel expansion makes residual j false while retaining every other residual (the parent undecomposed axiom containing j **cannot** be required simultaneously). This is exactly the corrected original theorem's strength.

### New-version finite independent check
The newly executed N2 Python uses one material core \`a\` with a describable and admitted g, the sound restriction/realization \`g→g→p\`, a global assignment \`q(a)=1\`, and an admitted component-channel witness. Each of six additional typed counterinterpretations has residual truth pattern **five true and the named one false** and preserves the nonempty active kernel and one admitted channel.
Results: **6/6**. These six counterinterpretations are *not* themselves models satisfying the full conjunction of all primitive axioms; treating them as such would beg the independence question.

**N2 subverdict T4.7: SUPPORTED_IN_DECLARED_RESIDUAL_BACKGROUND / no renewed source-language revision need in revised statement.**

## 3. Corrected §5 Proposition 5.13 (printed p14)

The new source now explicitly defines the external \`bar T_L : mathfrak U_L → W_L\` by retaining \`T_L(c)\` for \`c∈C_L\`, assigning \`0_W\` outside \`C_L\`, and asserts the *conditional* loss of membership discrimination **if** one absent candidate u and one admitted c0 with \`T_L(c0)=0_W\` coexist. This is valid because both outputs then equal \`0_W\` despite different membership. The new final sentence disclaims this consequence in every model.

**Independent derived criterion (NOT original Proposition 5.13):** from *output value alone*, channel admission fails to be decodable exactly when
\`\`\`text
(mathfrak U_L \ C_L != empty)
AND
(exists c in C_L: T_L(c) = 0_W).
\`\`\`
Proof: if both exist, two different admission states share the same value zero, ruling out any decoder from value to membership. If there is no absent candidate, a constant-admitted decoder suffices. Otherwise, when every admitted term is nonzero, decode “admitted” by testing whether the output is nonzero. This argument does not depend on the assigned quantity \`q(a)\` being zero: \`T(c)\` is independent term data in the Formation core.

New finite fixture: two candidate channels differing by role (one admitted, one absent); zero-valued admitted term causes collision; nonzero term 5 allows membership recovery; all admitted candidates permit constant decoder. Enumerated **16** typed two-candidate membership/term assignments using terms in \`{-1,0,1}\`; all satisfy the exact criterion. These are exhaustive only for that chosen toy universe.

**N2 subverdict P5.13: CONDITIONALLY PROVED AS WRITTEN; no renewed manuscript change needed.** Proposition 5.12's undefined \`T_L\` outside \`C_L\` is preserved; \`bar T_L\` is explicitly *external*, not a primitive zero channel.

## 4. Revised §7.3 D2 finite source model (printed pp26–27)

**Newly explicit source carrier and inheritance:**

- Grid \`X_D2={0,1,2}×{0,1,2}\`, row–column convention; common full typed material: **9 site vertices + 12 undirected nearest-neighbor edge items + 36 directional slots = 57 material items**.
- Selected \`S*={(0,0),(1,0)}\` has one internal nearest-neighbor connecting edge r*, and six exposed directional slots (eight cardinal incidences minus two internal incidences), hence **two retained vertices + one retained edge + six retained slots = 9 selected items**.
- The **supplied** annotation record marks the six S*-exposed slots blocked and other thirty potential directional slots transmissive. This is *not* claimed as a physical law derivable from grid geometry. h* inherits exactly the selected material and annotations from H*; p* inherits the same selected material, anchor restrictions, incidence and blocked-slot marks from h*. Both regimes use the same full material/annotation records.
- Both regimes admit H*,h*, describe h*, and have restriction edges \`Res(H*,h*)\`, \`Res(H*,H*)\`, \`Res(h*,h*)\` plus \`Realize(h*,p*)\`. Their primitive config admission and local coherence are equal/true.
- Only the **primitive** boundary compatibility truth of p* differs: \`BC_+(p*)=true\` for blocked boundary policy, \`BC_-(p*)=false\` for transmissive-only policy. Thus \`K^des_+={p*}\`, \`K^des_-=empty\`.
- On the positive side global \`q_+(r*)=1\` with Q+={r*}, one role and one channel term 1. On the negative side Q− empty, roles empty and C− empty, preserving Axiom V. These Stage 5–7 differences occur **after** the already-obstructed Stage 3.

### Why exactly b=3
The *identity* on all common typed carriers and values preserves Stage 0, 1 and 2 data, so \`I_2(L+,L−)≠empty\`. There is exactly one candidate configuration p* in each regime, so every candidate configuration bijection sends p*→p*. Since \`BC_+(p*)\` and \`BC_-(p*)\` differ, **no** Stage-3 comparison tuple can preserve/refelect the BC predicate: \`I_3(L+,L−)=empty\`. By original Definition 6.15, \`b(L+,L−)=3\`.

New executed fixture directly enumerated all 57 and the subset of 9 material identifiers, explicitly carried down restricted blocked annotations and anchors, and validated C+=1, C−=0, I2-nonempty/I3-empty. This is still a selected model check, not exhaustive search over all D2 physical boundary policies or structural regimes.

**N2 subverdict D2: CONSISTENT FULL-MODEL WITNESS UNDER EXPLICIT SUPPLIED BC / b=3 VERIFIED.** Original missing boundary-annotation and axis information is now in the PDF, not merely in a proposed external patch. No new correction need found in this locus.

## 5. Revised §8 Discussion and dependencies (printed p29)

Source Definition 6.21 (p23) compares **some nonempty finite admitted-channel families** \`F_L,F_M\` under a separately prescribed F-linear isomorphism J. Proposition 6.22 (p24) gives a legal *existential* counterexample to \`composite coincidence ⇒ strict isomorphism\`, taking C_L of size 1, C_M of size 2, with nonempty composite sums both zero.

- This one-way nonimplication is supported by the full formation-model role-multiplicity construction described in the original source.
- The reverse implication for an **arbitrarily independently prescribed J** is false: one full model with one admitted channel term 1 is strictly isomorphic to itself under the identity strict isomorphism, but at fixed \`J=-id_R\` its only nonempty component sum maps to -1 rather than 1. No fixed-J coincidence can be exhibited.
- Even under J=id, a strictly equivalent pair with \`C=empty\` has no **nonempty** family in Definition 6.21 and so fails the existential coincidence test.
- Positive qualified direction is valid **under the J belonging to the strict isomorphism itself** and only if the admitted channel set is nonempty: E9 and induced channel bijectivity give componentwise equality for corresponding finite families; Corollary 6.12 states this. The old p29 text overclaimed an unconditional “strictly weaker” implication; the new p29 correctly states there is no unconditional implication ordering **for independently fixed J**.

The phrase “selected composite-output agreement retains less information” remains a scope description of the **observables recorded**, not a new universal logical equivalence theorem. The indexed 3×3 example in §7.4 and Proposition 6.22 remain compatible with this distinction. The new §9 Conclusion says fixed-J composite agreement can coexist with strict non-equivalence, **without reinstating** the previously overstrong converse.

**N2 subverdict §8: SOURCE QUALIFICATION SUPPORTED; earlier fixed-J logic-strength issue corrected in new printed PDF.** Four target scalar boundary conditions were checked, with the analytic hypotheses made explicit.

## 6. Scope, residual risks and version-release action

- All **four** corrections from old-edition G6 are incorporated and source-bound re-audited in the **new** 34-page PDF. This does not imply source-wide proof FPA closure.
- The **remaining original mathematical items, unedited sections and new-edition dependency graph** require a separate N3 whole-paper regression audit. Original 2026-08-06 numbered-item coverage 69/69 is historical and cannot substitute automatically.
- The English PDF prints **2026.10.22**, but both G7 LaTeX revised copies were previously compiled with the **2026.08.06** date. Before preparing a new Zenodo version, align source \`\\date\` or equivalent and recompile, then lock the exact release candidate bytes. English PDF new source does not certify that the Korean PDF/source has gone through analogous *new-edition* semantic re-audit.
- No changes to the archived 2026-08-06 original, new user-uploaded 2026-10-22 PDF, original editable LaTeX, or any Zenodo record were executed by N2.

## 7. Verdict, Windows replay and next N3

\`\`\`text
CASE: FAS-F2-20261022-N2-FOUR-SECTION-REAUDIT-001
MATHEMATICAL_VERDICT: FOUR_REVISED_LOCI_SUPPORTED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY (FOUR CORRECTED LOCI ONLY)
FOUR_G6_EDITS_PRESENT_AND_ADVERSARIALLY_REVIEWED: yes
NEW_N2_REGRESSION_FOUND_IN_FOUR_LOCI: none
NEW_SOURCE_SECTIONS_REVIEWED: Theorem 4.7 / Proposition 5.13 / Section 7.3 D2 / Section 8
FINITE_EVIDENCE: 6 residual witnesses; 16 zero-extension toy assignments; 1 D2 model; 4 fixed-J situations
EXECUTED_SCRIPT_GITHUB_BYTE_MATCH: yes
EXECUTED_JSON_GITHUB_BYTE_MATCH: yes
NEW_F2_FULL_PAPER_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
ZENODO_2026_10_22_RELEASE_PUBLISHED: not_verified
LEGACY_2026_08_06_AUDIT: unchanged historical archive
NEXT: FAS-F2-20261022-N3-MANUSCRIPT-DEPENDENCY-REGRESSION-001 / NOT_STARTED
\`\`\`

Run from the previously established \`DSD_Method_Family\` **checked-out repository root** on Windows 11:

\`\`\`powershell
python .\\DSD_Audit\\audits\\formal_proof\\formation_axiom_system\\versions\\2026-10-22\\scripts\\verify_n2_four_sections.py
\`\`\`

Default generated JSON path:
\`\`\`text
DSD_Audit/audits/formal_proof/formation_axiom_system/versions/2026-10-22/results/n2_four_sections.json
\`\`\`

The verifier uses the Python standard library only and supports an optional alternative destination path as its first positional argument.
