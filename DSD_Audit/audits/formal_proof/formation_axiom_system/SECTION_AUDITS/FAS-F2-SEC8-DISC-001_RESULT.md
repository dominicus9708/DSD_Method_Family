# FAS-F2-SEC8-DISC-001 — Section 8 Discussion claim-to-proof cross-audit

2026-10-20 KST · Existing DSD Audit FPA v0.1 · Original unnumbered Discussion section, **not a theorem-level proof**.

```text
CASE: FAS-F2-SEC8-DISC-001
AUTHOR: Kwon Dominicus
PRIMARY_SOURCE: DSD_Formation_Axiom_System_EN(5).pdf, 33 pages
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCATION: §8 Discussion, printed pp.28–29
PRECOMMIT_COMMIT: cba0f0829e84d8e2e03e6fdf1f30a37b9997dab0
EXECUTED_PYTHON_COMMIT: 671c7c1397cdb96b64fc5099bfc1afa5a63e160f
PYTHON_SHA256: 44869e0da75fc42cb18d67a659b4f2ad526f6d7b260f4a4106762dbd3d1a03ce
PYTHON_GIT_BLOB: 8543abfbd20d2804f70ba81b89de1ac15bea21d1
EXECUTED_JSON_COMMIT: f02759b245a104ddc63fc25dbf772e9868247d8d
JSON_SHA256: 1e35018c94a78de453f94f5d490488a2752d0386041704e6f7afffc801f51670
JSON_GIT_BLOB: fcd549afc355a92250e00552db468e6305885cdd
MATHEMATICAL_VERDICT: PARTIALLY_SUPPORTED_WITH_VALID_COUNTEREXAMPLE_TO_UNQUALIFIED_COMPARISON
DSD_AUDIT_VERDICT: PASS_WITH_REFINEMENT
REVISION_NEED: CLARIFICATION
COUNTEREXAMPLE_AFFECTS: §8 strictly-weaker logical reading ONLY
PROPOSITION_6_22: UNCHANGED; VALID ONE-WAY NONIMPLICATION
F2_FULL_PAPER_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not established
ORIGINAL_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-SEC9-CONC-001 / NOT_STARTED
```

## 1. Original Discussion and claim-trace ledger

The source §8, printed pp.28–29, summarizes results in prior sections. This is an **audit of interpretive and summary assertions**, not a new theorem and not a re-verification of every proof from scratch. The verified claim ledger preserves source ordering:

| Claim ID | §8 exact-topic claim (faithful paraphrase) | Source prerequisite | Result / caveat |
|---|---|---|---|
| D01 | Undefined assignment, defined zero, defined nonzero negligible value, channel absence, and admitted zero-term channel are distinct formal statuses. | §2.2 primitive interface; Primitive V; Closure VI; supply W,T in §3.2 | **SUPPORTED**. Distinct status does NOT imply every regime instantiates each case; negligible nonzero is a typed/status distinction when applicable. |
| D02 | Primitive versus derived closure preserves seven-stage order; ZFC and set size give metatheory without using the whole class as a model carrier. | Definitions 2.2/2.4, Proposition 2.5; §2.1; Theorem 3.3 | **SUPPORTED**, not a theorem proving ZFC consistency and not an assertion that all stage truncations are full models. |
| D03 | Four primitive axioms are non-vacuously independent. | Source §4.1 Countermodels 4.1–4.4, Theorem 4.5 | **SUPPORTED IN DECLARED TYPING**; independence of the four packages, not absence of any dependencies inside their clauses. |
| D04 | Six residual primitive constraints are clausewise independent after eliminating typed/functional/induced-record consequences. | Proposition 4.6; Theorem 4.7 | **SUPPORTED WITH EXACT SCOPE**; historic optional T4.7 claim-scope wording clarification remains independently recorded. |
| D05 | Relative to supplied post-Stage-VI W,T, unique full closure and exact primitive-reduct characterization, with no added primitive-core admissibility restriction. | Theorem 3.3, Remark 3.4 | **SUPPORTED**. Relative unique closure, not unique choice of W or T. |
| D06 | One-point existence and general standard realization of typed finite anchored data. | Theorem 7.1, Corollary 7.2, Theorem 7.3 and Corollary 7.4 | **SUPPORTED** under stated input typing; finite formation carriers/domains do not force finite external Vλ or W. |
| D07 | Truncations/reductions preserve stage order; admitted c iff nonempty formation-trace set; witness history is not part of five-tuple channel identity. | Proposition 2.5, Definition 3.5, Theorem 3.6 | **SUPPORTED** with no converse reinterpretation of history as channel identity. |
| D08 | Forward maps, witness-reflecting embeddings, bijective strict embeddings; identities/composition; possibly large category and wide embedding subcategory; inclusion-submodel preorder. | Definition 6.2, 6.4, Theorem 6.5, Corollaries 6.6/6.7, Theorem 6.8, Proposition 6.11, Theorem 6.14 | **SUPPORTED**; witness *reflection* applies to embeddings, not arbitrary forward maps; possibly large category is metatheoretic. |
| D09 | Strict formation isomorphism compares the entire candidate-level and primitive presentation, including unsuccessful candidates, and is presentation-sensitive. | Definition 6.10 (E1–E9), Theorem 6.14 | **SUPPORTED BY DEFINITION**; no implication that numerical composite equality recovers primitive presentation. |
| D10 | Composite-level coincidence under prescribed output-space comparison is “strictly weaker” than strict formation equivalence. | Definition 6.21, Proposition 6.22 | **REQUIRES CLAIM-SCOPE CORRECTION.** P6.22 proves coincidence does **NOT** imply strict equivalence, but the reverse strict⇒coincidence can FAIL for an arbitrary prescribed J and even for J=id if C=∅. Thus logical relation is **NOT** simply a weak/strong implication ordering as worded. |
| D11 | Nested comparisons yield an earliest branching index invariant under strict isomorphism. | Definition 6.15, Theorems 6.16/6.19/6.20, Corollary 6.18 | **SUPPORTED WHERE DEFINED**, with Stage0 an ambient comparison status, not an eighth formation stage, and Stage4 excluded as first independent obstruction. |
| D12 | D2 finite witness has early config-input branch, synthetic 3×3 indexed witness later assignment-domain/channel mismatch after configs held fixed. | Original §7.3 D2 case and §7.4 3×3 indexed case; Definition 6.15 | **SUPPORTED WITH PRECISION**: D2 first b=3 from supplied primitive BC; 3×3 first b=5 from global Q mismatch (channel C mismatch is *downstream*, not a separate first cause at Stage6). Original §7.3 inherited blocked annotation clarity recommendation remains separate. |

**Ledger tally:** 11 Discussion-level statements supported under their declared prerequisites, **one with an unqualified logical-strength wording issue (D10)**. Source §8 is not itself an independently proved theorem; this ledger does not upgrade it to one.

## 2. Exact counterexample to the unqualified “strictly weaker” logical entailment (D10)

Definition 6.21 first fixes an **F-linear isomorphism J independently of the families** and demands **NONEMPTY finite admitted-channel families** F_L,F_M with J(Comp_L(F_L))=Comp_M(F_M). Proposition 6.22 proves there exist full models exhibiting composite coincidence despite strict non-equivalence; hence

```text
fixed-J composite coincidence DOES NOT IMPLY strict formation equivalence.
```

This direction is source-proven. However it does **not** establish the logically different

```text
strict formation equivalence IMPLIES fixed-J composite coincidence
```

for an arbitrarily prescribed J.

### Counterexample A: even with admitted nonempty channels

Fix F=R and base B with singleton support s. Take a full model with material {a}, expression {h}, configuration {p}, mat(h)=act(p)={a}, shared anchors a↦s, admitted/described h, identity Res(h,h), Realize(h,p), all three configuration gates true, quantity kind λ with pointed Vλ=R, **globally defined qλ(a)=1**, one role tuple Role(p,a,λ,ρ). Primitive I/II/III/V hold; Closure IV yields K_des={p}, A*={a}; Closure VI yields the unique admitted five-tuple c=(p,a,λ,1,ρ) with nonempty trace. Supply **W=R and T(c)=1**, Clause VII Dcomp={∅,{c}}, with Comp({c})=1.

Compare this **identical full model to itself**: its strict formation isomorphism is identity on every typed sort and J₀=id_R on W. Thus the descriptors are **strictly equivalent**.

But preselect the **other valid real-linear isomorphism** J(x)=−x independently of the families. The **only possible nonempty admitted-channel family** on either side is {c}. Therefore

```text
J(Comp_L({c})) = -1  ≠ 1 = Comp_M({c}).
```

There is **no fixed-J composite-level coincidence** for this strictly isomorphic pair and this valid prescribed J. J=-id_R is R-linear and invertible; the counterexample does not exploit an illegal nonlinear comparator.

### Counterexample B: empty admitted-channel carriers (even with the identity J)

Use the same well-typed identity-expression-realization primitive core and anchor, but global assignment Qλ=∅, qλ empty, Role empty, C=∅, and W=R,T empty. Axiom V is valid because ∅⊆A*={a}; all closure definitions still produce a full formation model; its only admissible finite family is ∅ with composite zero. Compare the model to **itself** with the identity strict isomorphism and **prescribed J=id_R**. Definition 6.21 **explicitly excludes ∅** from the witness families, so **there are no possible nonempty F_L or F_M at all**. Thus strict equivalence holds but fixed-id-J composite coincidence does not.

This second counterexample also means that an existential “choose some compatible J” formulation would still require the qualification that both admitted-channel families be nonempty.

### Implication diagnosis and correction

Proposition 6.22 and the related §7.4 counterexample establish **only nonimplication from equal composites to strict structural isomorphism**. Neither Proposition 6.22 nor Definition 6.21 establishes a simple **strictly weaker logical binary relation** on all full descriptors with an arbitrarily specified J. The structural comparison examines **more information**, but information-content ordering is different from a formal implication relation. No primitive axiom, Theorem 3.3 or Proposition 6.22 is refuted by these two full-model examples.

**English wording recommended for the final two Discussion sentences at this point (replace only the misleading logical-strength clause):**

> By contrast, composite-level coincidence compares selected nonempty channel families only through a prescribed output-space isomorphism, without requiring strict formation equivalence. As Proposition 6.22 demonstrates, such coincidence does not imply strict formation equivalence; the two notions do not form an unconditional logical implication ordering when the comparison map is fixed independently and empty admitted-channel sets are permitted.

**Korean 1:1 check:**

> 반면 합성량 수준의 일치는 미리 지정된 출력 공간 동형사상을 통해 선택된 비공집합 채널 가족만 비교하며, 엄격한 형성 동형성을 요구하지 않는다. 명제 6.22가 보이듯 이러한 일치로부터 엄격한 형성 동형성이 도출되지는 않는다. 그러나 비교 사상을 독립적으로 고정하고 허용 채널 집합의 공집합도 허용하는 경우, 두 개념 사이에 무조건적인 논리 함의 순서가 성립하는 것은 아니다.

This is a **necessary wording/scope refinement if “strictly weaker” is intended as formal logical entailment**, not an axiom-system contradiction or a need to alter underlying proven results. Alternatively source may retain “less informative about primitive formation structure” **as an explanatory, not logical, comparison** with this qualification.

## 3. First-branch illustration precision (D12)

§8 references the two original unnumbered examples:
- D2 §7.3: **b(L+,L−)=3**, from the different **PRIMITIVE boundary compatibility BC** on its singleton p*, with common earlier typed inputs. This is a supplied regime-policy difference, not a physical theorem derived from D2 grid geometry. Historical annotation inheritance and axis-naming source clarifications remain recorded in **FAS-F2-SEC7.3-D2-001**.
- Synthetic indexed 3×3 §7.4: **b(L_H,L_G)=5**, witnessed by |Q_H|=768 versus |Q_G|=1536 and condition E5 of Definition 6.15. The downstream channel count mismatch is also real (768 vs 1536), but is **NOT** an earlier independent “Stage6 first branch”. Its 127 composite coincidences are among 387 structurally mismatched index families; 252 are equal if counting all 512. Source §8 does not itself give those numerics; they are imported from the cited construction, not invented new §8 claims.

§8 is otherwise consistent with the separate FPA cases of T3.3/T3.6/T4.5/T4.7/T6.5/T6.8/T6.14/T6.16–T6.20 and §7.1–§7.4, with the known **relative** and **typed** qualifications retained.

## 4. Executed reproducible negative-controls

- [Prospective precommit](FAS-F2-SEC8-DISC-001_PRECOMMIT.md)
- [Exact locally executed Python](../scripts/verify_sec8_discussion_scope.py)
- [Executed deterministic JSON](../results/sec8_discussion_scope.json)

Standard-library Python was executed locally via `python -W error`, plus successful `python -m py_compile`. It builds two source-typed finite full Formation models (one admitted channel and zero admitted channels), validates admitted expression/restriction/realization, actual Ψ witness, q global partial-domain subset, Role and Closure VI/VII, then compares each model to **itself** using identity strict formation structure. With one admitted channel and T(c)=1, fixed J=-id_R gives no coincidence; fixed J=id_R does. With zero admitted channels, fixed J=id_R gives no nonempty witness families. Representative exact scalar calculations check that J=-id_R is a linear bijection; its arbitrary-real linearity is elementary mathematics, not deduced from sampling.

**Local file and GitHub byte identity validated by read-back of matching Git blob SHA:**
```text
PYTHON_BYTES: 6527
PYTHON_SHA256: 44869e0da75fc42cb18d67a659b4f2ad526f6d7b260f4a4106762dbd3d1a03ce
PYTHON_GIT_BLOB: 8543abfbd20d2804f70ba81b89de1ac15bea21d1
JSON_BYTES: 1212
JSON_SHA256: 1e35018c94a78de453f94f5d490488a2752d0386041704e6f7afffc801f51670
JSON_GIT_BLOB: fcd549afc355a92250e00552db468e6305885cdd
```

Windows 11 at cloned repository root:
```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_sec8_discussion_scope.py
```
Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/sec8_discussion_scope.json`; optional first argument overrides output. Selected finite witnesses disprove an implication **because one counterexample suffices**, not because the program constitutes a universal proof certificate.

## 5. FPA v0.1 gates and bounded result

- G01 **PASS** original user-attached edition/hash, exact Section8 Discussion pp.28–29.
- G02 **PASS** twelve claim units mapped to exact source lemmas/axioms; none silently treated as new theorem.
- G03 **PASS_WITH_BOUNDARY** five formal statuses and four primitive versus residual six independence retained at correct scope.
- G04 **PASS_WITH_BOUNDARY** unique closure relative to W,T and metatheoretic class/set separation preserved.
- G05 **PASS** T7.1/T7.3 constructive existence and finite realizability not overstated.
- G06 **PASS** truncation, formation traces and category/embedding/strict preservation linked to correct conditions.
- G07 **PASS** candidate-level/presentation-sensitive strict isomorphism follows Definition6.10.
- G08 **REFINEMENT_REQUIRED** the statement “therefore strictly weaker” is invalid **as an unqualified formal logical implication** under Definition6.21, shown by fully valid positive and empty-channel counterexamples.
- G09 **PASS** Proposition6.22 itself remains valid; coincident composites do not imply strict equivalent descriptions.
- G10 **PASS_WITH_BOUNDARY** D2 first branch3 (primitive BC), indexed example first branch5 (global Q); channel count secondary, not newly independent Stage6 branch.
- G11 **PASS** actual executed script and JSON byte-identical to GitHub via Git blob SHA; fixed-J use adheres to definition.
- G12 **PASS_WITH_BOUNDARY** no external independent validation; source PDF and Zenodo not changed; F2 full manuscript still OPEN.

**FINAL BOUNDED DISCUSSION AUDIT:**
```text
MATHEMATICAL_VERDICT: PARTIALLY_SUPPORTED_WITH_VALID_COUNTEREXAMPLE_TO_UNQUALIFIED_COMPARISON
DSD_AUDIT_VERDICT: PASS_WITH_REFINEMENT
REVISION_NEED: CLARIFICATION
SOURCE_PROPOSITION_6_22: VALID; no theorem proof retraction
SOURCE_DISCUSSION_D10: correct nonimplication direction, fix unqualified strict-weakness formulation
NEXT: FAS-F2-SEC9-CONC-001 / NOT_STARTED
```

The previous optional Theorem4.7 wording and §7.3 inherited boundary-record/coordinate naming clarifications remain separate. **Numbered FPA counts unchanged:** 14 theorems, 2 propositions, 9 corollaries; unnumbered §7.3/7.4/8 cases now three separately audited. No PDF/Zenodo change, outside independent review or whole-paper F2 certification is claimed.
