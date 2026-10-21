# FAS-F2-APPC-CONSTRUCT-001 — prospective source-locked audit obligations

2026-10-20 KST · Formal Proof Audit v0.1 · Source section: original **Appendix C**, printed pp.31–32 of the 33-page Formation Axiom System, Kwon Dominicus. This is an unnumbered original appendix audit, not a new theorem or a full-paper F2 certificate.

## Immutable source
- File: `DSD_Formation_Axiom_System_EN(5).pdf`.
- SHA256: `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
- Primary source: original Appendix C, "Finite-Construction and Witness Reconstruction Protocol" (printed pp.31–32).
- Dependencies: §7.2 Theorem 7.3 (standard finite-data realization); §7.4 specified synthetic 3×3 indexed witness; primitive formation axioms/Closure IV, VI, VII; related previous FPA cases T7.3, SEC7.4-3X3, Appendix B; do not inherit their audit verdict automatically.
- Original manuscript PDF and Zenodo remain unchanged.

## Frozen independent obligations, decided before new computation
1. **C01 — Coverage and limits:** transcribe Appendix C's two source procedures verbatim in substance, and preserve its explicit bound: 2^9=512 site subsets for the *specified* assignment/value rules, not all conceivable 3×3 formation rules.
2. **C02 — Standard data preconditions:** finite relational material structure M with alpha:M→Supp(B), finite Lambda and R, partial q_lambda:D_lambda→V_lambda and role seed R0 subset of P(M)×M×Lambda×R, only with a∈A∩D_lambda for each role tuple; inspect empty M and empty R0 boundaries.
3. **C03 — Exact constructive typing:** e_A and p_A for all A⊆M; material and active subsets A; anchors alpha|A; induced relational records; Res(e_A,e_B) and Realize(e_A,p_B) iff B⊆A; identity restrictions and all three configuration predicates; all p_A are describable, A*=M; global q with D_lambda.
4. **C04 — Term map:** admitted channels biject the *role-seed tuples* R0 via (A,a,lambda,rho)↦(p_A,a,lambda,q_lambda(a),rho); finite free F-vector W=F^(C) including C=empty zero-dimensional case; basis term T(c)=e_c and finite Clause-VII set summation; no extra dynamic/probabilistic inference.
5. **C05 — 3×3 fixture scope:** all i=0..511 and three distinct typed private carrier items a_i^H,V,D, plus nine site items; role triples all declared; one global q per regime and channel per locally assigned carrier only.
6. **C06 — Independent finite arithmetic:** prespecified LH four slices [0,125),[125,187),[187,506),[506,512), sizes 125/62/319/6; LG all three. Check LH=768, LG=1536 channels; 387 structural mismatches, 62 vertical-without-horizontal LH; fixed J=id_R full-family sums; 127 mismatched coincidences, 252 all-index coincidences, exact zero/one/two distribution. A successful check must recompute, not hardcode assertions as outputs.
7. **C07 — Historical/operational identity:** ignore multiplicity of restriction witnesses as extra channel identity; do not conflate defined zero with absent channel; do not count partial subsets instead of full admitted-channel family.
8. **C08 — Logical limit:** finite executable fixtures do not prove arbitrarily quantified Theorem 7.3. Check its general argument separately from finite smoke tests; no external independent validation or automatic F2 manuscript-wide closure.
9. **C09 — Prior exception inheritance:** retain historical independent §7.3 D2 boundary-mark clarification, §8 Discussion fixed-J logical-strength correction and T4.7 wording clarification. Appendix C cannot silently clear them.
10. **C10 — Reproducibility:** save the actual executed standard-library Python and deterministic JSON with GitHub exact-byte blob comparisons, then record mathematical verdict, FPA process verdict, revision need, limits, and Notion crosslinks. Precommit precedes new tests.

## Adjudication gates
MATHEMATICAL_VERDICT: pending
DSD_AUDIT_VERDICT: NOT_EXECUTED
REVISION_NEED: UNDETERMINED
INDEPENDENT_EXTERNAL_VALIDATION: not_established
FULL_F2_MANUSCRIPT_FPA: OPEN
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged

Next action: perform source-bound formal reasoning, then independent selected constructive Python fixtures, evaluate actual results, and separately document all failures, omissions and limitations. No advance pass or expected verdict is assumed.