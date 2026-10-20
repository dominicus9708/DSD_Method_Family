# FAS-F2-SEC7.4-3X3-001 — 3×3 indexed formation-finite synthetic witness

2026-10-20 KST · DSD Audit, Formal Proof Audit v0.1 · ORIGINAL UNNUMBERED SOURCE §7.4 (not a newly invented theorem).

## Source lock and final bounded verdict

- Author: Kwon Dominicus.
- Frozen manuscript: DSD_Formation_Axiom_System_EN(5).pdf, 33 pages, SHA256 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a.
- Exact locus: Section 7.4, printed pages 26–28, heading “Fully specified synthetic formation-finite 3 × 3 indexed witness”.
- Prospective PRECOMMIT commit: 86ee4ef9e96e1fa78e9263cb4d326beecc222eb9.
- Python uploaded commit: df2582951789d8577a62944f682a76af7e33ca06.
- JSON uploaded commit: 159cb211e32ebe407144ccf64577f12c9c5358b3.
- MATHEMATICAL_VERDICT: **PROVED_IN_DECLARED_BACKGROUND**.
- DSD_AUDIT_VERDICT: **PASS_WITH_BOUNDARY**.
- REVISION_NEED: **NONE**.
- F2_FULL_MANUSCRIPT_FPA: OPEN; INDEPENDENT_EXTERNAL_VALIDATION: not established.
- SOURCE_PDF_ZENODO: unchanged. METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged.
- NEXT: **FAS-F2-SEC8-DISC-001 / NOT_STARTED**.

## 1. Exact typed source construction and all seven formation stages

Let X={0,1,2}² be nine typed sites. The source defines the exact binary index i(S)=Σ over (r,c)∈S of 2^(3r+c). Distinct S yield precisely the integers 0,...,511, so 512 configurations and 512 expressions exist in each regime L_H and L_G.

Their COMMON material set is the disjoint union of nine site items with three index-private material carrier items a_i^H,a_i^V,a_i^D per index i, hence **9+512×3=1545 material items**. Each expression h_i and configuration p_i retains the S_i site material and all three a_i^R private carriers; even i=0 has three private carrier items. The source anchors site items to their sites and private H/V/D items to horizontal/vertical/whole-base supports. A concrete source-compatible support coding uses nine site supports and three typed H/V/D support representatives, shared by both regimes. The source gives support *types*, not a complete literal ZFC coding of each support representative; this optional representation does not affect any count or comparison obstruction.

Both regimes admit and describe all h_i, and declare precisely identity restrictions Res(h_i,h_i) and same-index Realize(h_i,p_i), with all three primitive configuration predicates Adm_cfg/LC/BC true. Accordingly Primitive I/II/III are satisfied by identity inheritance of retained material, anchors and any same internal induced material-record relation. Definitional Closure IV makes every p_i describable, K_des=P_B (size 512), and A* equal to the entire 1545-element shared material universe (every site occurs in some S_i; each private carrier occurs in its p_i).

Both regimes use one quantity kind λ_E with pointed value space **real R**, negligible-kind subset empty, and three roles ρ_H,ρ_V,ρ_D. Importantly, BOTH have all **1536 primitive Role tuples** Role(p_i,a_i^R,λ_E,ρ_R), EVEN if L_H does not assign a value at the corresponding carrier item. Role does NOT by itself force channel admission.

### One regime-global partial assignment, not 512 unrelated maps

L_G assigns every private carrier globally, with q_G(a_i^H)=1, q_G(a_i^V)=1, q_G(a_i^D)=-2, for every i. Thus Q_G contains exactly **1536** items.

L_H's notation Q_H(p_i) in the source describes pairwise DISJOINT, index-private portions of one global domain Q_H; its exact partition is:

| i range | assigned carrier roles | index count | assigned items |
|---|---|---:|---:|
| 0–124 | H, V, D | 125 | 375 |
| 125–186 | V | 62 | 62 |
| 187–505 | H | 319 | 319 |
| 506–511 | H, V | 6 | 12 |
| TOTAL | | 512 | **768** |

For i<125, H uses values 1,1,-2, as G does. For assigned carriers in 125≤i<252, H uses **DEFINED 0**; for assigned carriers in 252≤i<512, H uses 1. Unassigned carriers remain undefined, not zero. Since Q_H,Q_G are subsets of A*=M, Primitive V is satisfied; the global functions have no conflicting assignments.

Closure VI admits precisely the channels (p_i,a_i^R,λ_E,q(a_i^R),ρ_R) at the carrier items where global q is DEFINED. Each channel has a real formation trace using the h_i identity restriction/realization. Therefore **|C_H|=768 and |C_G|=1536**, and H has 127 admitted channels with defined zero rather than absent channels.

The source supplies **real vector spaces W_H=W_G=R** and components T(channel)=the assigned real v; Clause VII defines composition of every FINITE subset of the admitted global C. Because C is finite, all global admitted-channel subsets are finite, although their counts 2^768 and 2^1536 are too large to enumerate. The specific F_L,i is the family of ALL admitted channels based on p_i, one finite family for each i, not the whole global family collection. Both full Formation models satisfy original Definition 2.2 and are formation-finite under Definition 2.3, which does not demand that the real value/term spaces be finite.

## 2. Index-aligned scalar sums: 127 versus 252 is NOT a contradiction

For EVERY i, the G index-full-family composite is 1+1−2=0.

| i range | H terms | H composite | indices |
|---|---|---:|---:|
| 0–124 | 1+1−2 | 0 | 125 |
| 125–186 | 0 on V | 0 | 62 |
| 187–251 | 0 on H | 0 | 65 |
| 252–505 | 1 on H | 1 | 254 |
| 506–511 | 1+1 on H,V | 2 | 6 |

Channels and assigned values STRUCTURALLY match at exactly 125 indices i<125. At remaining 387 indices i≥125 the channel structures differ, including 62 vertical-without-horizontal cases i=125..186 in L_H. Of these **387 structural mismatches**, precisely **127** (125..251) have equal index-full-family scalar sums, using the **fixed prescribed J=id_R**. Across all 512 indices, the number with equal scalar composites is 125+127=**252**. The source explicitly calls its 127 the coincidences **among mismatched cases**, and this is correct. The H composite histogram is 252 zeros, 254 ones and 6 twos.

These coincide only AFTER scalar aggregation and do **not** imply typed channel set equality, domain equality or strict formation equivalence. They also do not prove physical facts or a random statistical frequency: the index partition is chosen as source model data.

## 3. First branching at Stage 5: all candidate tuples excluded

The source stage comparison classes are the nested I_0,...,I_7 of Definition 6.15. All material, anchors, quantity-kind/pointed-space/role carriers, expression and configuration carriers and early expression/restriction/realization primitive predicates are identical in L_H and L_G, as are derived K_des and A*. Therefore the identity comparison tuple survives **I_0,I_1,I_2,I_3,I_4**, showing I_4≠∅.

At Stage 5, condition **(E5)** requires EVERY surviving typed comparison to transport one regime-global assignment domain bijectively: f_M(Q_H)=Q_G. But **|Q_H|=768≠1536=|Q_G|**. A finite-domain cardinality mismatch forbids such a bijection under ANY possible material permutation, not merely under the identity. Hence I_5=∅ and, by Definition 6.15 and Theorem 6.16, the FIRST branching index is **b(L_H,L_G)=5**. I_6 and I_7 remain empty by nestedness. Corollary 6.26 independently rules out strict isomorphism because |C_H|≠|C_G|, but that is a downstream channel obstruction, not an earlier Stage 5 cause.

Adversarial boundaries: restoring equality of domain cardinalities alone would only remove this particular numerical obstruction; E5–E7 also compare the actual assigned graph and zero/size data. In H, the 127 zero-valued admitted channels are distinct from missing-role channels. The candidate channel universe over R can be infinite even though the admitted C is finite; the original formation-finite definition allows that.

## 4. Executed finite checker, exact artifact equality and Windows reproduction

- [Prospective source-lock](FAS-F2-SEC7.4-3X3-001_PRECOMMIT.md)
- [Verified Python](../scripts/verify_sec74_indexed_3x3.py)
- [Verified JSON](../results/sec74_indexed_3x3_witness.json)

The executable source enumerates ALL 512 nine-bit index patterns, computes the disjoint tagged material universe 1545, creates actual 512 h_i/p_i with real-number-valued source components evaluated using exact integer arithmetic on {-2,0,1}, tests global Q/C sizes, identity witnesses, every per-index channel membership and scalar aggregate, and the 125/387/62/127/252 partitions. It does NOT attempt to enumerate 2^768 or 2^1536 global families, or infinitely many hypothetical real candidate values.

The locally executed Python **exactly matches the committed GitHub blob**; the locally executed JSON also exactly matches its separate saved GitHub blob. Read-back evidence:

- Python: **6274 bytes**, SHA256 076c6abc64ce872c73280f48ecaf410864aab8b006389806de3f9a7eb8839731, Git blob **e293f224fa9c864ab2ae5c4b10b2c5cb703571ce**.
- JSON: **1621 bytes**, SHA256 94a3f5eae3a9da6c5d82b4d88ada3bf9877dfdf1ba98a1ac2816674df8298c3c, Git blob **72fcf1af32d3c03f03ccbcefd6787fd173da88b8**.

Windows 11, execute in cloned repository root:

    python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_sec74_indexed_3x3.py

Default output goes to DSD_Audit/audits/formal_proof/formation_axiom_system/results/sec74_indexed_3x3_witness.json. Optional first CLI argument overrides output path. Standard-library Python only.

## 5. FPA v0.1 gates

- G01 PASS: original 33-page source, SHA, printed §7.4 pp.26–28 and UNNUMBERED-case status.
- G02 PASS: X↔9-bit index bijection; sites 9 and unique 512×3 private items; 1545 common material items.
- G03 PASS: Primitive I/II/III and definitional Closure IV: identity Res/Realize, every p_i described, A*=all material.
- G04 PASS: Primitive V: one global typed partial q per regime, Q sizes 768/1536, defined zero ≠ undefined, no duplicate domain items.
- G05 PASS: identical primitive Role 1536, correct admitted-channel iff, C sizes 768/1536, formation trace witness for each.
- G06 PASS: source real W,T and Clause VII finite-family sums; 512 specific per-index full-family sums explicitly computed.
- G07 PASS: exact counts 125 same structures, 387 different, 62 V-only, 127 mismatched coincident, 252 total coincident, H composite 252/254/6 histogram.
- G08 PASS: identity typed comparison at I4 and no possible comparison at I5 by universal global-domain cardinality obstruction; b=5.
- G09 PASS_WITH_BOUNDARY: a concrete support-record implementation and optional shared empty material relational signature are source-compatible representative codings, not extra original axioms; no essential source correction required.
- G10 PASS_WITH_BOUNDARY: global finite powersets and real value spaces are not exhaustively enumerated; all actually indexed source data are.
- G11 PASS: separate §8 Discussion/§9 Conclusion not yet audited; historical §7.3 D2 and T4.7 optional clarity recommendations remain separate.
- G12 PASS: local and GitHub executed Python/JSON byte equality verified; no independent outside peer validation.

**FINAL: PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE.**

This proves source-specific finite indexed model and its first branching and aggregation examples under the declared background; it is not an independent certification of the entire Formation F2 manuscript. Original PDF and Zenodo unchanged, method-family internal standardization 22/22 unchanged, F2 full paper OPEN.

**NEXT: FAS-F2-SEC8-DISC-001 / NOT_STARTED**, bounded audit of source Section 8 Discussion conclusions against prior theorem audits.
