# PA-P24 manuscript amendment proposal — smallest section-by-section edits (NOT APPLIED)

**Draft status:** proposed text only; original Property PDF, TeX and Zenodo were NOT edited. **Author: Kwon Dominicus.**
**Frozen original:** Property Axiom System, 2026-09-01, 23 pp, SHA256 \`03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c\`.
**Underlying audited revision:** [P24 full result](P24_PROPERTY_SOURCE_CHANGE_AUDIT_RESULT.md).
The English paragraphs below are targeted **replacement or insertion proposals**, not quotations from the original paper. A matching Korean review line accompanies each. Mathematical meaning must be reviewed again when editing the source.

---

## A. §6.1 Definition 6.1, printed pp.12–13 — REQUIRED

**Keep F1 and F2 exactly as written. Insert a common guard between F2 and F3:**

**EN proposed insertion:**
> In conditions (F3)–(F5), let \(\varpi\) range over the property kinds in \(\Pi_A\) whose input profiles are available in \(A\). By (F1), such profiles are also available in \(B\); thus the coordinatewise product map \(\phi_\varpi:X_{A,\varpi}\to X_{B,\varpi}\) is well defined. No product-map condition is imposed for a source kind with unavailable input profile.

**KR corresponding review:**
> (F3)–(F5)의 속성 종류 \(\varpi\)는 \(A\)에서 선언되어 있고 입력 프로필이 이용 가능한 경우에 한한다. (F1)에 따라 그러한 프로필은 \(B\)에서도 이용 가능하므로 입력 곱 사상 \(\phi_\varpi\)가 정의된다. 원천 모형에서 프로필이 이용 불가능한 속성 종류에는 입력 곱 사상 조건을 부과하지 않는다.

**Revise the quantifier at F3 to avoid two independent scopes:**
> (F3) For every \(\varpi\in\Pi_A\) with an available input profile in \(A\), the induced product map \(\phi_\varpi:X_{A,\varpi}\to X_{B,\varpi}\) satisfies \(\phi_\varpi(\mathrm{Ap}_{A,\varpi})\subseteq\mathrm{Ap}_{B,\varpi}\).

**F4 in the same common scope:**
> (F4) For every such \(\varpi\) and every \(d\in\delta_L(\varpi)\), \(\phi_\varpi(\mathrm{Sat}_{A,\varpi,d})\subseteq\mathrm{Sat}_{B,\varpi,d}\).

**F5 in the same common scope:**
> (F5) For every such \(\varpi\), if \(x\in D_{A,\varpi}\), then \(\phi_\varpi(x)\in D_{B,\varpi}\) and \(\Xi_{B,\varpi}(\phi_\varpi(x))=\Xi_{A,\varpi}(x)\).

**KR F3–F5 validation:**
> 선언되었고 이용 가능한 원천 프로필에 대해서만 적합성 영역·선결조건 집합·할당 정의역과 값을 순방향 보존한다. 미공급 프로필과 공급된 빈 운반체를 동일시하지 않는다.

**Reason:** Original Def2.4 makes \(X_{A,\varpi}\) undefined if any required auxiliary sort is not supplied; original Def2.5 explicitly allows declaring such a kind without requiring its primitive coordinates. Original unguarded F3 therefore fails to define its product map even for identity \(A\to A\).

## B. §6.1 Proposition 6.2, printed p.13 — RECOMMENDED dependent proof insertion

**EN proposed insertion at proof opening:**
> For an unavailable source profile, (F3)–(F5) impose no condition. Under (F1), every available profile in the first source remains available in all successive targets. Hence all component product maps used in the identity and composition arguments exist, and the usual pointwise inclusion and assignment-preservation proofs apply to them.

**KR:**
> 원천 프로필이 이용 불가능하면 (F3)–(F5)는 조건을 부과하지 않는다. (F1)에 의해 이용 가능한 원천 프로필은 연속된 대상에서도 이용 가능하므로, 항등·합성 증명에서 쓰이는 곱 사상은 모두 정의된다.

**Verdict:** original category conclusion survives once the guard is made explicit.

## C. §6.2 Definition 6.3, printed p.13 — REQUIRED dependent change

**EN proposed replacement for the first scope:**
> A forward property map \(\Phi:A\to B\) is a property embedding when each auxiliary carrier map is injective and, for every \(\varpi\in\Pi_A\) whose profile is available in \(A\), every input \(x\in X_{A,\varpi}\) satisfies the following biconditionals:

Retain the original applicability, prerequisite, assignment-domain, and value equations verbatim.

**KR:**
> 모든 보조 운반체 사상이 단사이고, \(A\)에서 선언되었으며 프로필이 이용 가능한 각 속성 종류의 모든 입력에 대해 적합성·선결조건·할당 정의역의 양방향 동치가 성립할 때 매장이라 한다.

**Reason:** otherwise the original phrase “for every source input \(x\in X_{A,\varpi}\)” has the same undefined-profile scope defect as Def6.1.

## D. §6.3 Theorem 6.8, printed p.14 — REQUIRED

**EN proposed full theorem statement replacement:**
> **Theorem 6.8 (Strict property equivalence is an equivalence relation).** Strict Stage-VI-fixed, signature-fixed property isomorphism is reflexive, symmetric, and transitive. Equivalently, the strict isomorphisms are precisely those property embeddings \(\Phi:A\to B\) for which (S1) all source auxiliary carrier maps are bijective, (S2) the sets of available auxiliary sorts in \(A,B\) coincide, and (S3) \(\Pi_A=\Pi_B\). Under these conditions the reverse embedding requirement (S4) follows.

**KR theorem:**
> **정리 6.8 (엄격한 속성 동형관계는 동치관계이다).** 엄격한 Stage-VI 고정·시그니처 고정 속성 동형관계는 반사성·대칭성·추이성을 만족한다. 이는 매장 조건에 더해 (S1) 보조 운반체 사상의 전단사성, (S2) 이용 가능한 보조 정렬 집합의 일치, (S3) 선언된 속성 종류 집합의 일치를 충족하는 경우와 정확히 동치이다. 해당 조건에서는 역방향 매장 조건 (S4)가 도출된다.

**EN proposed proof replacement:**
> Every identity embedding satisfies (S1)–(S3), and its inverse is itself. Let \(\Phi:A\to B\) be an embedding satisfying (S1)–(S3). By (S2), each available auxiliary source sort is available in the target and conversely. By (S1), its carrier map is bijective; identity maps act on inherited carriers. Therefore, for every common declared kind with available profile, the induced product map is bijective. Because the original embedding conditions reflect applicability, prerequisite satisfaction, and assignment-domain membership, these biconditionals remain valid under inverse product maps. Preservation of assigned values reverses by substitution on those domains. Thus the inverse family is an embedding, establishing (S4). For unavailable profiles, no product-map conditions are imposed on either side. Identity, inverse, and componentwise composition preserve bijectivity, equal availability sets, and equal declaration sets; consequently strict isomorphisms form an equivalence relation.

**KR proof verification:**
> (S1)과 (S2)는 공통의 이용 가능한 입력 정렬마다 곱 사상에 전단사성을 준다. (S3)는 양쪽에서 검사할 선언된 종류가 동일함을 보장한다. 원래 매장의 적합성·선결조건·정의역 양방향 동치는 역함수에서도 유지되고 값 보존은 대입으로 역방향에서 성립한다. 따라서 (S4)가 도출되며 항등·역·합성에 대해 해당 조건이 닫힌다.

**Two countermodels required before publication:**
1. \(\Pi_A=\Pi_B=\varnothing\), \(A\) supplies no auxiliary \(u\), \(B\) supplies \(u=\{b\}\). Empty family of source maps is vacuously a bijective embedding, but (S2) fails.
2. Both supply singleton \(u\) and its bijection. \(\Pi_A=\varnothing\), \(\Pi_B=\{\varpi\}\) with a valid empty assignment and typed property coordinates. Embedding vacuous on source kinds, but (S3) fails.

## E. §4.2 Theorem 4.3, printed p.11 — REQUIRED logical-scope clarification

**EN proposed replacement:**
> **Theorem 4.3 (Mutual non-derivability over typed premodels).** Relative to the shared typed-premodel background, Primitive Axioms I and II are mutually non-derivable. The countermodels proving this claim are not primitive property cores. Closure Clause C1 is a definitional completion applied only after both axioms are satisfied and is not an additional axiom imposed on those countermodels.

**KR:**
> **정리 4.3 (자료형을 갖춘 전모형에서의 상호 비도출성).** 공통 타입 전모형 배경에서 원시공리 I과 II는 서로 도출되지 않는다. 이를 보이는 반모형은 원시 속성 코어가 아니며, 폐포 C1은 두 공리를 모두 충족한 코어에 적용되는 정의적 완성이지 해당 반모형에 부과되는 추가 공리가 아니다.

**Original proof:** Countermodels 4.1 and 4.2 can be retained; modify only one explanatory sentence so that each is recognized as a typed premodel, not a full C1-admissible model.

## F. Abstract, printed p.1 — REQUIRED downstream wording

**EN replace only:**
> “strict Stage-VI-fixed, signature-fixed property isomorphisms are exactly the bijective embeddings”

**with:**
> “strict Stage-VI-fixed, signature-fixed property isomorphisms are exactly the bijective embeddings with matching auxiliary-sort availability and property-kind declarations”

**KR:**
> 엄격한 Stage-VI 고정·시그니처 고정 속성 동형은 보조 정렬 이용 가능 집합과 속성 선언 집합이 일치하는 전단사 매장이다.

## G. §11 Theorem 11.1, item (7), printed p.19 — REQUIRED downstream wording

**EN replace item (7) with:**
> (7) Strict Stage-VI-fixed, signature-fixed property isomorphism is exactly a property embedding satisfying (S1)–(S3) of Definition 6.7, with (S4) following under those conditions, and strict property equivalence is an equivalence relation.

**KR:**
> (7) 엄격한 Stage-VI 고정·시그니처 고정 속성 동형은 정의 6.7의 (S1)–(S3)을 충족하는 매장과 정확히 일치하며 이 조건들에서 (S4)가 도출된다. 엄격한 속성 동형관계는 동치관계이다.

## H. Optional editorial check and regression references

- Def2.5 scope: confirm requirements (2)–(4) all refer to kinds declared **and** with available profiles; the original final paragraph already says no primitive coordinates are required otherwise. Clarify numbering if editorial ambiguity remains.
- §7 stage-comparison sets and Corollary 7.3 already demand complete strict conditions; review phrasing after S1–S4 correction but no independent theorem reversal was found.
- §11 item (3) already says relative to shared typed background; it is compatible with Theorem4.3 amendment.
- Do not touch Stage-VI operational-channel identity, P23 typed inherited interface, or Formation v4.5 source for this Property-only logical correction.
- Do not merge the P24 source patch with unrelated wording changes or silently assert that the original manuscript has already been revised.

\`\`\`text
P24_PATCH_STATUS: PROPOSED_SECTION_TEXT_NOT_APPLIED
MUST_EDIT: DEF6.1_F3_F4_F5 + DEF6.3 + THEOREM6.8 + THEOREM4.3 + ABSTRACT + TH11.1(7)
RECOMMENDED: PROP6.2_PROOF + DEF2.5_SCOPE_EDITS
ORIGINAL_PROPERTY_PDF_TEX_ZENODO: UNCHANGED
\`\`\`
