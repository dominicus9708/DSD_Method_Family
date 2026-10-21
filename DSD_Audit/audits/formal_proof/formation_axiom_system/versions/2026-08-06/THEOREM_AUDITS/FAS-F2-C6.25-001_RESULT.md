# FAS-F2-C6.25-001 — Role obstruction / 역할 관계 장애

**2026-10-20 KST | DSD Audit — Formal Proof Audit v0.1 | One source-bound corollary, not entire-paper or external proof certification**

\`\`\`text
AUDIT_CASE: FAS-F2-C6.25-001
SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, supplied 33-page attachment
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: Section 6.5, Corollary 6.25 (Role obstruction), printed p.24
PREREQUISITES: Definition 6.10 (E8), Theorem 6.23, Closure Clause VI
PRECOMMIT_COMMIT: aa20f23212c1cb2570b389d1e3dedb868c3a6b71
PORTABLE_PYTHON_COMMIT: 7b479190faf449cf66751c537e3d33e6e291f126
SAVED_JSON_COMMIT: 6991638ae5113b948f416064c7b059980f00bfee
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
FPA_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
SOURCE_PDF_ZENODO: unchanged
F2_FULL_MANUSCRIPT_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not established
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-C6.26-001 / NOT_STARTED
\`\`\`

## 1. Exact corollary and general proof

**Source text:** “Corollary 6.25 (Role obstruction). If no candidate comparison preserves the role relation, then no strict base-fixed formation isomorphism exists.”

For two full formation descriptors \`L,M∈FormDesc_(B,F)\` over the SAME fixed base and scalar field, a candidate strict comparison has **bijective** material/configuration/kind/role maps
\`\`\`text
f_M:M_B^L→M_B^M,   f_P:P_B^L→P_B^M,
tau_Lambda:Lambda_L→Lambda_M,   tau_R:R_L→R_M
\`\`\`
and the correctly typed expression, pointed-value and F-linear term-space-isomorphism maps in Definition 6.10. Source (E8) requires, for every \`p,a,lambda,rho\` in the source typed product:
\`\`\`text
Role_L(p,a,lambda,rho)
 iff
Role_M(f_P(p),f_M(a),tau_Lambda(lambda),tau_R(rho)).
\`\`\`

If no typed candidate comparison makes this biconditional true **for all role tuples**, assume a strict base-fixed formation isomorphism exists. Definition 6.10 requires its (E8) clause to be satisfied, contradicting the hypothesis. Equivalently, apply already independently audited Theorem 6.23: each complete candidate fails at least E8, so no strict isomorphism exists. This is a **universal necessary-condition/contradiction proof**; it does not need a fresh formation axiom.

**Quantifiers and boundaries:**
- It is **every candidate** that must fail E8, not one arbitrarily tried candidate.
- Candidate tuples may fail E8 at different \`(p,a,lambda,rho)\`; the corollary does not assert a **single common failing role tuple**.
- If a required bijection, including \`tau_R\`, cannot exist because carrier sizes differ, \`Cand(L,M)=∅\` and the antecedent is vacuously true. This is **not** a witnessed role-relation E8 failure of an actually existing map. For a genuine *nonvacuous* role-relation obstruction, match role-carrier cardinalities and show every candidate fails.
- Do not confuse Definition 6.10's candidate tuples (already requiring F-linear **isomorphism J**) with Definition 6.15's stagewise ambient arbitrary J before Stage 7.
- Role preservation is **not** equality of the numbers of roles, total role edges, admitted channels, trace witnesses or numerical composites. E8 is the fully typed **four-argument relational isomorphism** requirement.
- The theorem does not claim first-branching index \`b(L,M)=6\` merely because E8 fails. That stronger classification would require an audit of nonemptiness of all preceding staged comparison sets \`I_0,...,I_5\`; the present corollary does not assign b.

## 2. Nonvacuous legal source-typed finite witness

Use \`F=F2\` and a fixed external base \`Supp(B)={s0}\`, empty material-record signature. Both full descriptors have **identical** base-anchored primitive data apart from the supplied role predicate:

- Two material items \`{a,b}\`; one expression \`{h}\`; one configuration \`{p}\`; two quantity kinds \`{lam,mu}\`; exactly two role labels \`{r,s}\`.
- \`mat(h)=act(p)={a,b}\`. Anchors of all active/supported materials are \`s0\` in both expression and configuration. \`Adm_expr(h)=Des_expr(h)=true\`; \`Res(h,h)=true\` and \`Realize(h,p)=true\`; \`Adm_cfg(p)=LC(p)=BC(p)=true\`.
- Primitive I, II and III therefore hold, including **identity restriction** and anchor inheritance. The genuine expression witness \`(h,h)\` gives \`Psi(p)=true\` and Closure IV sets \`K_des={p}\` and \`A*=A={a,b}\`.
- Both kinds have pointed value space \`{0}\`; each globally defined partial assignment domain is \`Q_lam=Q_mu={a,b}\`, with **defined** value \`q_lam(a)=q_lam(b)=q_mu(a)=q_mu(b)=0\`. The graph has four distinct assigned material-kind edges. These typed domains lie inside \`A*\`, so Primitive V holds. No nullable value is quietly padded into a graph edge. Negligible-kind subset empty, hence no optional norm/threshold data.
- The sole difference between L and M is this Role predicate on tuples with p fixed:

\`\`\`text
L: Role(p,a,lam,r), Role(p,a,mu,r),
   Role(p,b,lam,s), Role(p,b,mu,s).
   ==> role determined by MATERIAL.

M: Role(p,a,lam,r), Role(p,b,lam,r),
   Role(p,a,mu,s), Role(p,b,mu,s).
   ==> role determined by QUANTITY KIND.
\`\`\`

Closure VI gives **4 admitted channels on each side**, one channel for each displayed Role tuple with v=0. Every admitted channel is supported by a genuine formation trace; the full candidate-channel universe U has **8 elements** on each side and the exact \`Chan⇔Tr(c)≠∅\` test covers 16 source+target candidates. Supply \`W_L=W_M=F2\` and a total component term map \`T(c)=0\` if the channel's material item is a, \`T(c)=1\` if it is b. Closure VII determines all \`2^4=16\` finite channel subsets and their F2 sums, including the empty sum 0; the full admitted-channel families both have composite 0 because each contains two b-material channels and \`1+1=0\` over F2. No rule identifies \`T(c)\` with assigned q=0.

**E8 obstruction despite matched simple counts.** Both sides have exactly two role labels, four Role entries, four admitted channels, two entries per role, four defined assignment graph edges and the same F2 full-family composite 0. However the multiset
\`\`\`text
{ number of distinct role labels incident to material a :
  a ranges over material items }
\`\`\`
equals \`{1,1}\` in L and \`{2,2}\` in M. Any typed bijections \`f_M,f_P,tau_Lambda,tau_R\` preserve this multiset: material and kind permutations only rearrange the fibers, and a role-label bijection preserves the number of distinct labels. Since the multisets differ, **no** comparison satisfies E8. In particular, a hypothesized bijection swapping the material and quantity-kind SORTS would not be type-correct and cannot rescue strict equivalence.

There are exactly \`2!×2!×2!=8\` candidates for material, quantity-kind and role maps; expression/configuration, pointed singleton value maps and \`J=id_F2\` are unique. Each of the eight candidates **satisfies E1–E7** in this example but fails E8, so E9 is not applicable as an induced admitted-channel-bijection comparison. This establishes a nonvacuous legitimate role-only obstruction, **not** merely a role-cardinality mismatch.

## 3. Executed finite checks; positive and vacuous controls

- [Prospective precommit](FAS-F2-C6.25-001_PRECOMMIT.md).
- [Portable Python verifier](../scripts/verify_c625_role_obstruction.py).
- [Recorded JSON results](../results/c625_role_obstruction.json).

The exact GitHub script was authored and previously reported locally checked in this case, with its GitHub source read back at **8,510 characters** and verified to contain the intended executable entry point. The saved JSON was freshly read back in the resume turn and its values independently inspected; an additional short independent Python enumeration run in the resume turn reproduced the 8/8 role failures, 4 positive E8 maps, 2 positive strict term-compatible comparisons and material role-degree profiles. **The complete GitHub script was not downloaded and fresh-run from GitHub in the current container**, since outbound DNS/network access is unavailable. No claim of external independent replication or third-party certification is made.

| Selected check | Recorded result |
|---|---|
| Nonvacuous role comparison candidates (negative pair) | 8 |
| Candidates satisfying all E1–E7 | 8/8 |
| Candidates satisfying E8 in negative pair | **0/8** |
| Role tuples each side | 4 |
| Admitted operational channels each side | 4 |
| Material-specific distinct-role degrees | L \`[1,1]\`, M \`[2,2]\` |
| Candidate channel \`Chan⇔Tr≠∅\` checks, both regimes | 16/16 |
| Full admitted-family F2 aggregate | 0 on both sides |
| Positive comparison (M'=L): candidates | 8 |
| Positive candidates satisfying E8 | 4/8 |
| Positive candidates satisfying all strict conditions including E9 | **2/8** |
| Empty typed candidate control (role-carrier size mismatch) | 0 |

**Positive-control interpretation:** On the true L-vs-L copy, several candidates still fail E8; this cannot refute strictness because at least two others meet all strict requirements. Also, among the four E8-compatible positive candidates, two fail E9 due to the supplied T map; **E8 alone is necessary but not sufficient** to certify full strict isomorphism.

**Empty-Cand control:** Reducing the role carrier to one element while source has two makes the candidate bijection set empty. That case is logically distinct from the main nonvacuous same-size role-pattern witness; do not conflate them.

**Defined-zero guard:** All four global assignment graph edges in each negative example have a **defined** 0 value, and a removed edge in a separate test becomes undefined, not another 0 assignment. Nonadmitted candidates have no T values. Term vectors and channel-family sums are kept separate from these partial-graph values.

**Windows reproduction from the cloned repository root:**

\`\`\`powershell
python .\\DSD_Audit\\audits\\formal_proof\\formation_axiom_system\\scripts\\verify_c625_role_obstruction.py
\`\`\`

Default output: \`DSD_Audit/audits/formal_proof/formation_axiom_system/results/c625_role_obstruction.json\`. Optional first positional argument overrides the output path. Standard-library Python only.

## 4. Formal proof audit gates and verdict

- G01 Frozen source/claim **PASS**: exact Corollary 6.25 from attached hashed 33-page PDF, printed p.24, E8 source text matched; no claim of Zenodo byte identity.
- G02 Logical quantifiers **PASS**: none of the typed candidate comparisons satisfies E8; not simply one failing candidate or a uniform failing input tuple.
- G03 Exact typing **PASS**: f_P/f_M/kind/role bijections, correct four-sorted relation, fixed (B,F), complete Formation models.
- G04 Original primitive/definitional clauses **PASS**: I/II/III/V and Closure IV/VI/VII with genuine trace and defined-zero partial assignment.
- G05 General mathematical inference **PASS**: strict Definition6.10 requires E8; absent E8-compatible candidate precludes strict iso by contradiction / T6.23.
- G06 Existence/conditionality **PASS_WITH_BOUNDARY**: distinguish role-carrier bijection impossibility (empty candidate) from nonvacuous all-candidate E8 failures.
- G07 Adversarial **PASS**: same role/channel/cardinality counts with different incidence, type-swap rejected, role-only obstruction E1–E7 passed in chosen example, strict-positive model includes failed candidates.
- G08 Finite versus general **PASS_WITH_BOUNDARY**: finite chosen structures support but do not prove general logical theorem; complete uploaded script was not freshly executed remotely in this continuation.
- G09 Role/term specificity **PASS**: E8 necessary but not sufficient, E9 guarded by induced channel bijection; no claim b=6 or that equal sums imply equivalence.
- G10 Mathematical background **PASS**: typed relation transport and ordinary finite-set incidence invariants, F2 vector arithmetic.
- G11 Downstream **PASS_WITH_BOUNDARY**: source Corollary 6.26 not yet separately audited, no automatic promotion. Existing optional T4.7 wording clarification unaffected.
- G12 External validation **PASS**: internal project audit; no independent reviewer certification established.

**Final bounded verdict: \`PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE\`.**

These boundaries delimit the source's hypothesis, source typing and selected finite sample; they are **not** an open mathematical proof gap in Corollary 6.25. Whole F2 manuscript FPA remains **OPEN**, original PDF and Zenodo remain unchanged, and DSD Method Family internal-standardization count **22/22** is unchanged.

**Resumable next:** \`FAS-F2-C6.26-001\` — Corollary 6.26 (Channel-cardinality obstruction), **NOT_STARTED**.

[Notion synchronized FAS-F2-C6.25-001 audit](https://app.notion.com/p/3fe81f51e7fa81f7a548fd06e761453f)
