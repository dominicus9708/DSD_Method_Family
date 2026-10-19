# FPA v0.1 — Formal Proof Audit / 형식 증명 감사
Status: **prepared / not yet executed** · Date: 2026-10-19 · Parent method: **DSD Audit (one of 22)** · Phase: **post-standardization application**, not a new method or SC rule.

## 1. Purpose and independence / 목적·독립성
Audit the exact proof obligations of a frozen mathematical manuscript using **ordinary mathematics, its declared background logic (for Formation: set-theoretic reasoning relative to ZFC), exact definitions, explicit countermodels, and valid inference**. DSD Audit helps organize and retrace proof claims; **no DSD axiom, FPA PASS, software test, author's own review, or analogy substitutes for mathematical proof**. Because Formation itself is a DSD foundation, proof verdicts MUST be assessed without assuming the theorem to be proved or importing results from a DSD method that depends on it. Source/version independence, logical noncircularity, and independent external-evaluator status are THREE DIFFERENT axes. Author-led FPA is NOT independent external validation.

## 2. Inputs / 입력
- Immutable, identified original manuscript: title, source, capture provenance, cryptographic hash, scope and date. Source lock records are version-specific; an attachment hash does not certify identity to a Zenodo or GitHub revision.
- Exact theorem, definitions, axiom clauses, standing assumptions, previous lemmas, proof text, codomain/typing/signature, and proof obligation.
- External/domain mathematical validity standard and background logic; where needed, explicitly state use of ZFC or another formal base.
- Existing finite witness/code metadata; execution evidence belongs in a separate run ledger and is NEVER automatic general proof.

## 3. Mandatory procedure / 절차
**FPA-01 Source lock:** capture exact edition and checksums; preserve prior audits as historical records. Record missing links to other editions as OPEN, not equivalent.
**FPA-02 Obligation extraction:** register every numbered theorem/corollary/proposition/lemma and any unnumbered proof-claim of consequence; identify existence, uniqueness, necessity, sufficiency, equivalence, independence, transport, invariance, and generality separately.
**FPA-03 Stepwise derivation:** for each inference record premises, cited rules, exact quantifiers, set sizes, sorts, definedness, map domains/codomains, and any imported theorem. A restatement of a conclusion is not a proof.
**FPA-04 Adversarial cases:** negate or remove one relevant premise at a time; seek smallest legal countermodel (including degenerate/empty/nonempty cases where admissible). Distinguish falsifying the theorem under the locked assumptions from showing an assumption is necessary.
**FPA-05 Finite/computational boundary:** match each runnable witness to the claimed statement, input and output; classify finite exhaustive evidence vs selected instance vs arbitrary-model proof. Do not infer universal validity from finite tests.
**FPA-06 Dependency and cross-paper impact:** trace every accepted, limited, rejected or OPEN claim to dependent results; do not automatically invalidate unrelated statements.
**FPA-07 Verdict and release gate:** separate domain mathematical verdict, DSD audit process verdict, manuscript revision need, and external independent validation; record unresolved/failed checks without deletion. Never post-hoc tune the frozen audit criteria.
For heavy mathematical cases execute **one logically bounded theorem group per session**, stop with a resumable checkpoint before timeouts, and log next theorem.

## 4. Verification gates / 필수 검사
G01 source immutability and known version; G02 definition before use and noncircular dependency; G03 quantifier/typing/domain/range; G04 axiom vs definitional closure; G05 independent premise and proof-step validity; G06 existence/uniqueness separated; G07 countermodels for independence/negative assertions; G08 general theorem vs finite run; G09 map composition, reflection, isomorphism and invariant scopes; G10 imported theorem/background assumptions; G11 cross-paper bridge and downstream impact; G12 epistemic limits, NO_GAIN/failure/post-hoc preservation.
Gate statuses: PASS / FAIL / NEEDS_EVIDENCE / NOT_APPLICABLE; no percentage without an explicit denominator and completed execution ledger.

## 5. Non-overclaim verdicts / 판정
MATHEMATICAL_VERDICT = PROVED_IN_DECLARED_BACKGROUND | DISPROVED_BY_VALID_COUNTERMODEL | PROOF_GAP | NOT_REVIEWED | INDETERMINATE.
DSD_AUDIT_VERDICT = PASS | PASS_WITH_BOUNDARY | PASS_WITH_REFINEMENT | FAIL | INDETERMINATE | NOT_EXECUTED.
REVISION_NEED = NONE | CLARIFICATION | ASSUMPTION | PROOF | THEOREM | DEPENDENCY_REAUDIT | UNDETERMINED.
EVIDENCE_ROLE = method_specific_application_of_Audit; CASE_ORIGIN = existing_author_manuscript; INDEPENDENT_EXTERNAL_REPLICATION = not_established unless separately proven.
A mathematically false theorem may be *correctly detected* by the audit; that does not mean the underlying theorem passed. A properly conducted audit with no discovered issue does NOT establish mathematical completeness.

## 6. Supporting DSD methods / 보조 방법 구별
Specification freezes statement/obligations; Analysis splits a single proof; Tracking/Lineage capture dependencies; Computation audits concrete finite witnesses; Comparison tests cross-source statements; **Audit** independently owns the process verdict. Auxiliary use must be evidenced, never inferred from labels.

## 7. Publication / 공개
Store evolving execution records in the method-family GitHub and Notion, cross-reference the Formation companion repository. Retain existing Zenodo manuscript unchanged during audit. If a material error affects the public claim, separately decide public correction/version release; do not silently defer correction or update Zenodo after every minor audit. Release an independent report/paper only for a warranted scholarly contribution; self-audit is not third-party certification.

## 8. First case / 최초 대상
See `../../audits/formal_proof/formation_axiom_system/SOURCE_LOCK.md`, `PROOF_OBLIGATIONS.md` and `EXECUTION_PLAN.md`. Start with Theorem 3.3, not a prewritten PASS. Preserve SC-01–SC-10 and the completed 22/22 registry without modification.
