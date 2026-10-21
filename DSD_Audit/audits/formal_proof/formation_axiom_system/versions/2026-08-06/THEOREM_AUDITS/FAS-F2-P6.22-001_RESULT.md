# FAS-F2-P6.22-001 — Composite coincidence without strict equivalence

Date: 2026-10-20 KST. Formal Proof Audit (FPA) v0.1. Source-bound internal mathematical audit, not third-party certification.

## Identifiers and frozen verdict

- Case: FAS-F2-P6.22-001.
- Source: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, 33 pages, SHA-256 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a.
- Exact source: Section 6.5, Definition 6.21 and Proposition 6.22, printed p.23.
- Prospective precommit: 6f375adb5979f10cca3e77f401f78ddf1362f4d4.
- Portable locally executed Python commit: 0fd98592f1dbc3c2dc33773c76e4bbc6013f3188.
- Finite JSON commit: c26ca62a689f4d410d477c8abb129ce3fb3da44f.
- MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND.
- DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY.
- REVISION_NEED: NONE.
- FULL_PAPER_F2_AUDIT: OPEN.
- INDEPENDENT_EXTERNAL_VALIDATION: not established.
- SOURCE_PDF_ZENODO: unchanged.
- NEXT: FAS-F2-T6.23-001 / NOT_STARTED.

## 1. Exact source claim and required quantifiers

Definition 6.21 (Composite-level coincidence relative to a fixed map) first prescribes an F-linear ISOMORPHISM J: W_L -> W_M, independently of the channel families. Two NONEMPTY finite admitted-channel families F_L in Dcomp_L and F_M in Dcomp_M are J-composite-level coincident exactly if J(Comp_L(F_L)) = Comp_M(F_M). The triple (Sigma_L, Sigma_M; J) exhibits this coincidence UNDER STRICT NON-EQUIVALENCE when the descriptors are not strictly base-fixed formation-isomorphic AND those two nonempty families exist.

Proposition 6.22 asserts existence of TWO FULL source Formation models on a COMMON fixed base and a PRECHOSEN J satisfying the definition while strict equivalence fails. It does not claim that all equal aggregate outputs imply nonequivalence, nor that equal composites entail matching channel families.

## 2. Constructive full-model witness (independent of software)

Fix the same field F = R and base B with support carrier Supp(B) = {s}. Choose the empty material-record relational signature in both regimes. The shared typed primitive formation data are:

- Material M_B = {a}, expression E_B = {h}, configuration P_B = {p}.
- mat(h) = act(p) = {a}, with both anchors carrying a to the SAME external support element s.
- Adm_expr(h), Des_expr(h), Res(h,h), Realize(h,p), Adm_cfg(p), LC(p), BC(p) all true. All otherwise unlisted primitive relations false.
- One quantity kind Lambda = {lambda}; pointed value set V_lambda = {0}, distinguished zero 0; global domain Q_lambda = {a}, partial assignment q_lambda(a) = 0, graph Gamma_lambda = {(a,0)}.
- Negligible quantity-kind subset Lambda_delta = empty; no optional size/threshold function is required.

Primitive Axiom I holds because h describable implies h admitted. Axiom II holds because the sole restriction Res(h,h) preserves material and anchor and the admitted h has its identity restriction. Axiom III holds because act(p) is contained in mat(h) and the inherited anchors coincide. Axiom V holds because Psi(p) is witnessed by (h,h), hence A* = {a}, and Q_lambda = {a} is a subset of A* with q_lambda(a)=0 in V_lambda. All types are set-sized and well formed, and the SAME (B,R) applies to both models.

Clause IV uniquely gives Psi(p) true, Des_cfg(p) true, K_des={p}, and A=A*={a}. The ONLY difference in primitive inputs is the role label carrier and corresponding role relation:

- In L: R_L={rho0}, Role_L={(p,a,lambda,rho0)}.
- In M: R_M={rho_plus,rho_minus}, Role_M={(p,a,lambda,rho_plus),(p,a,lambda,rho_minus)}.

Clause VI therefore determines EXACTLY the admitted channel sets

    C_L={c0},             c0=(p,a,lambda,0,rho0).
    C_M={d_plus,d_minus}, d_plus=(p,a,lambda,0,rho_plus),
                          d_minus=(p,a,lambda,0,rho_minus).

Each candidate has one genuine formation-trace witness (h,h,p,a,lambda,0,rho); the trace characterization is satisfied, and admitted-channel identity is the FIVE-TUPLE, not the numerical term or witness history.

AFTER Stage VI, supply W_L=W_M=R as R-vector spaces and total component term maps

    T_L(c0)=0,   T_M(d_plus)=1,   T_M(d_minus)=-1.

The supplied T is NOT forced to equal the assignment value v=0, as stated in Closure Clause VII. Thus the nonzero M terms are legal despite the zero assigned value. Clause VII uniquely produces Dcomp_L=P_fin(C_L), Dcomp_M=P_fin(C_M), and finite Comp sums. Definition 2.2 and Theorem 3.3 then identify BOTH structures as complete full Formation models satisfying primitive I/II/III/V and closure IV/VI/VII.

Choose the fixed comparison map J = identity_R BEFORE selecting families. This map is an R-linear isomorphism for ALL real scalars (ordinary algebra, not a numerical finite test). Now select the two NONEMPTY admitted families

    F_L={c0},  F_M={d_plus,d_minus}.

Both are in their respective finite-subset composition domains, and

    J(Comp_L(F_L)) = id_R(0) = 0 = 1 + (-1) = Comp_M(F_M).

However |R_L|=1 while |R_M|=2, so Definition 6.10's REQUIRED role-label bijection tau_R is impossible. Independently |C_L|=1 while |C_M|=2, so strict formation-isomorphism's induced channel bijection (Corollary 6.12) is also impossible. Therefore strict nonequivalence and fixed-J composite-level coincidence both hold. This explicit pair PROVES source Proposition 6.22 as an existential statement and refutes the discarded implication from composite coincidence to strict equivalence. It is NOT a countermodel to the DSD primitive axioms.

## 3. Adversarial controls and locally executed supplementary checker

- PRECOMMIT: FAS-F2-P6.22-001_PRECOMMIT.md in this folder.
- Python: ../scripts/verify_p622_composite_coincidence.py.
- JSON: ../results/p622_composite_coincidence.json.

The 7,084-character locally executed source-typed Python constructs the two primitive cores, checks Axioms I, II, III, V, and derives all of Clauses IV, VI, VII from those primitive inputs rather than assigning expected admitted results by hand. It verifies the trace iff for ALL 3/3 candidate channels (one in L and two in M); confirms exact channel cardinalities 1 vs 2, distinct roles 1 vs 2 and full-definition output domains for T; and checks both nonempty family memberships, exact sum zero on both sides, and fixed identity J.

Additional hostile checks ensure:
- Neither target singleton family has composite zero: their outputs are +1 or -1. The pair of target channels is required for cancellation.
- The EMPTY family is NOT used to satisfy Definition 6.21 (it is checked only as an auxiliary Clause VII consequence).
- Both regimes have a DEFINED assignment q_lambda(a)=0; no undefined-to-zero substitution.
- J is prescribed as identity before selecting families. A nonlinear or zero noninvertible comparison map would not satisfy Definition 6.21.
- The source's lack of prescribed algebraic dependence of T(c) on assigned v allows T_M(d_plus)=1 and T_M(d_minus)=-1.

Local execution returned all_checks_passed=true, prescribed_J='identity on R (fixed before families)', source/target admitted channels 1/2, nonempty family sizes 1/2, source/target composite 0/0, and all trace membership tests 3/3.

COMPUTATION LIMIT: Python verifies only the displayed exact integer and finite typed relations, not the uncountably infinite real space or universal F-linearity. The full mathematical witness is valid because identity_R is provably an R-linear bijection and both concrete full Formation structures have been explicitly constructed. The committed script has not been independently rerun after fresh checkout or externally peer validated; matching local and uploaded script lengths do not constitute independent replication.

From the root of the cloned dominicus9708/DSD_Method_Family repository on Windows:

    python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_p622_composite_coincidence.py

Default output: DSD_Audit/audits/formal_proof/formation_axiom_system/results/p622_composite_coincidence.json. Optional first CLI positional argument selects another output path. Python standard library only.

## 4. G01–G12 FPA audit decisions

- G01 SOURCE_LOCK PASS: attached PDF checksum verified; no claim Zenodo exact byte identity.
- G02 exact quantifiers PASS: prescribed J independent of NONEMPTY families, strict nonequivalence explicitly separate.
- G03 primitive axioms PASS: I/II/III/V satisfied with explicit same-base anchors.
- G04 closure typing PASS: IV and VI determine C, T supplied AFTER C, VII defines families/sums.
- G05 explicit existential proof PASS: real-linear identity and cancellation with provable channel cardinality obstruction.
- G06 assigned zero vs terms PASS_WITH_BOUNDARY: T not algebraically constrained by q; no guessed q-to-T law.
- G07 adversarial PASS: target singleton nonzero, empty family excluded, map J invertible.
- G08 finite/general PASS_WITH_BOUNDARY: a finite executable calculation does not certify all R-vector-space points.
- G09 strict structural invariant PASS: both role and admitted channel cardinality obstruct strict bijection.
- G10 declared background PASS: ordinary set theory and R-vector algebra.
- G11 propagation PASS_WITH_BOUNDARY: Theorem 6.23/Corollaries 6.24–6.26 and Section 7 remain NOT_STARTED.
- G12 independent status PASS: author-project internal mathematical audit is not independent certified review.

FINAL: MATHEMATICAL_VERDICT=PROVED_IN_DECLARED_BACKGROUND; DSD_AUDIT_VERDICT=PASS_WITH_BOUNDARY; REVISION_NEED=NONE. The BOUNDARY reflects exact fixed-J/nonempty/full-model hypotheses and computation scope, NOT an open mathematical gap in this proposition.

The prior optional wording-scope clarification for Theorem 4.7 remains separately recorded. F2 whole-paper audit OPEN, original PDF and Zenodo unchanged, DSD Method Family internal 22/22 unchanged.

NEXT: FAS-F2-T6.23-001 — original manuscript Theorem 6.23, Layerwise obstruction to strict formation equivalence, NOT_STARTED. Do not invent a Theorem 6.21: 6.21 is a Definition.

[Notion synchronized FAS-F2-P6.22-001 audit](https://app.notion.com/p/3fe81f51e7fa81468bd0df0551cd8170)
