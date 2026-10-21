# FAS-F2-G3-SEC5-001 — Section 5 Assignment, Channel, and Composition Results

**2026-10-21 KST · author Kwon Dominicus · original printed pp12–14 · FPA v0.1**

## A. Source/provenance and audit status

- Original immutable PDF: `DSD_Formation_Axiom_System_EN(5).pdf` (33 pages); SHA256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`. Original §5 visually inspected on printed pp12–14; no edits to PDF/Zenodo.
- [Prospective obligations and item inventory](FAS-F2-G3-SEC5-001_PRECOMMIT.md): commit `3be4cc27d4f543efa4cb6f3cda2adbbc808a65bb`; locked before new execution.
- Independently verified finite fixtures in [Python](../scripts/verify_sec5_assignment_channels.py), SHA256 `5653127f5adf2eda00f204f3bb48432ee562c6fe903c8f7a96d39c546232f811`, Git blob `88f77b1cb68d2e5635b356ceb62e2467caf6722c` (upload final byte-corrected commit `1f62070e27c818474792862861ee1b33466c3dc7`).
- Actual deterministic [JSON](../results/sec5_assignment_channels.json), SHA256 `50e940f517bd6afce6505e30dd92b6d55f964eea383381b70bab4dec363b5563`, Git blob `2649595ab64ede2ee5d43e1856d4ca56a0ee6b35` (commit `92ec2eba32aa87ebffc17cb84daff658daa8ee22`).
- Audit labels (14 in original §5): Definition 5.1; **10 propositions** 5.2, 5.4, 5.5, 5.6, 5.8, 5.9, 5.11, 5.12, 5.13, 5.14; **2 corollaries** 5.3, 5.7; **1 countermodel** 5.10. No numbered theorem added. The count is of original *claims examined in this group*, not 14 newly proved theorems or 14 new independent audits.

## B. Individually audited source items

| Original label | Domain proof/countermodel evidence | Verdict and limit |
| --- | --- | --- |
| Definition 5.1 | For p∈K_des, U(p)=act(p)\\Q(p), Z(p)={a∈Q(p):q(a)=0}, N_δ(p)={a∈Q(p):q(a)≠0 and ||q(a)||≤δ}. The last is meaningful **only** for λ∈Λ_δ. | WELL_TYPED. These three sets are pairwise disjoint, but **not claimed exhaustive**. |
| Proposition 5.2 | U is outside Q; Z and N inside Q; Z defined zero and N defined nonzero. | PROVED_IN_DECLARED_BACKGROUND, no converse/exhaustiveness invented. |
| Corollary 5.3 | From q:Q→V genuinely partial, a∈act(p)\\Q(p) implies a∉Q, so q(a) undefined; no zero conclusion. | PROVED_IN_DECLARED_BACKGROUND. |
| Proposition 5.4 | Given u∉Q, z∈Q, q(z)=0, zero padding makes qbar(u)=qbar(z)=0; definedness statuses distinct. | PROVED **CONDITIONALLY on the specified u and z**; no universal collision if no such pair exists. |
| Proposition 5.5 | Full model with nonempty act(p), describable p, q-domain empty; Axiom V allows Q=∅⊆A*. | PROVED BY LEGAL COUNTERMODEL of putative implication. |
| Proposition 5.6 | VI channel test gives p∈K_des, local Q, graph and role, while IV gives H,h and III gives anchoring; Q(p)⊆act(p)⊆A*. | PROVED_IN_DECLARED_BACKGROUND. |
| Corollary 5.7 | Contraposition of any required conjunction in VI, including local **graph pair** (a,v), not mere existence of some assigned value. | PROVED_IN_DECLARED_BACKGROUND. |
| Proposition 5.8 | Take p describable, a in Q(p) but no matching role, then no operational channel with that triple. | PROVED BY LEGAL COUNTERMODEL. |
| Proposition 5.9 | q(a)=distinguished zero remains *defined*; if p describable, matching local graph and role, VI admits c at v=0. T(c) need not be 0. | PROVED_IN_DECLARED_BACKGROUND. |
| Countermodel 5.10 | Full model with K_des={p} and Q=∅; C=∅; Dcomp={∅}, Comp(∅)=0_W. This is a defined empty **composite** not a defined term on a missing channel. | FULL LEGAL MODEL RECONSTRUCTED. |
| Proposition 5.11 | Different rho coordinates give unequal operational 5-tuples even when all other four entries match. Histories do not make extra channels. | PROVED_IN_DECLARED_BACKGROUND. |
| Proposition 5.12 | T is supplied with exact domain C. Candidate c∈U\\C is **outside dom(T)**; T(c)=0 is not a well-typed evaluation. | PROVED_IN_DECLARED_BACKGROUND. |
| Proposition 5.13 | **Genuine collision case**: one admitted c0 has T(c0)=0 and one absent u∈U\\C; zero extension maps both to 0. **Adversarial case**: one admitted c1 with T(c1)=1 and at least one absent candidate; extension maps admitted to 1 and absent to 0, so membership is exactly recovered as `c∈C iff Tbar(c)≠0`. | COLLISION CLAIM PROVED **CONDITIONALLY**; **unqualified universal** “it therefore loses channel membership” is **false if interpreted as every valid model**, by a legal countermodel. Require explicit quantifier/meaning of faithfulness. |
| Proposition 5.14 | Exact source model: material {a}, p describable, q(a)=0, three different rho, three admitted channels c1,c2,c3, supplied W=R and T=(1,-1,0). F1={c1,c2} != F2={c3}; sums both 0. | EXISTENTIAL CLAIM PROVED BY SOURCE-MATCHING FULL MODEL. |

### B1. Four assignment states (original 5.1 not claimed exhaustive)

With Lambda_delta={lambda}, δ=1 and size |v|, take active p on four material items, globally assigned q(zero)=0, q(small)=1/4, q(large)=2 and no q(missing). These four belong, respectively, to Z, N_delta, an **assigned nonnegligible complement**, and U. Thus U,Z,N_delta pairwise disjoint, while `U∪Z∪N_delta != act(p)` (size three versus four). This is no defect: the original proposition asserts disjointness only.

### B2. Independent quantifier/meaning issue in 5.13

The literal original sentence is: “An external extension that maps every absent channel to 0_W identifies absence with any admitted channel whose component term is 0_W. It therefore loses channel membership.” The first sentence's collision is valid **when both an absent candidate and an admitted zero-term channel exist**. It is not logically forced for every model with an absent candidate: a permissible model may have `T(c)≠0_W` for all c∈C. For such a model, the zero-padded map on U satisfies `c∈C ⇔ Tbar(c)≠0_W`, so **the value alone recovers membership**. Another boundary is U=C, when no absent candidate exists. The original presentation gives no formal definition of “channel-faithful,” so the safest narrow conclusion is that an **unqualified universal nonfaithfulness inference is not justified**, while a conditional counterexample to guaranteed faithfulness is correct.

**Recommended draft clarification only (not applied to manuscript):** “If at least one absent candidate channel and at least one admitted channel with zero component term coexist, a zero-extension identifies their output values; therefore such an extension cannot in general recover admission status from output value alone. This does not imply failure of recovery in every possible model.”

Do not collapse this into a claim that Axiom I/II/III/V, Closure IV/VI/VII or the entire Section 5 are inconsistent. The intended anti-conflation principle is correct; one quantifier/condition needs tightening. If original claim is read as explicitly conditional on `T(c_0)=0` and `u∉C`, **no mathematical falsehood arises**, only definitional clarity of “faithful” is lacking.

### B3. Composite collisions distinct from domain status

In the source-matching 5.14 model, all three channels have **assigned value zero** despite their **component terms (1,-1,0)**. There are exactly 8 possible finite channel subsets (2^3). The program separately enumerates all 8 and finds **8 unordered distinct pairs** having equal composite sums in this particular model. This strengthens **only the finite illustration**, not an assertion that every formation model has noninjective Comp.

## C. Execution reproducibility

Tested with local standard-library Python, `python -W error -m py_compile` then `python -W error`. Actual program output:

```json
{"collisions": 8, "composite_family_count": 8, "prop5_13_countermodel": true, "status_channels": 4}
```

Both the executed script and deterministic JSON were compared as exact SHA256/Git blob against uploaded GitHub files; they matched. Model constructors test primitive identity restriction, anchoring, valid realization witness, V-domain subset, VI channel identity and VII finite-family behavior for the selected fixtures. This is **not** a universal theorem prover. All universal steps stated above rest on domain logic and closure formulas; existential failures/satisfiability rest on fully specified finite models.

From the checked-out repository root in Windows 11:

```powershell
python .\\DSD_Audit\\audits\\formal_proof\\formation_axiom_system\\scripts\\verify_sec5_assignment_channels.py
```

Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/sec5_assignment_channels.json`. An optional first argument is output JSON path.

## D. Verdict; scope; historical separation

```text
CASE: FAS-F2-G3-SEC5-001
ITEM_COUNT: definition 1 / proposition 10 / corollary 2 / countermodel 1
MATHEMATICAL_VERDICT: MIXED — 5.13 unqualified universal nonfaithfulness DISPROVED_BY_VALID_COUNTERMODEL; conditional 5.13 true; other items PROVED_IN_DECLARED_BACKGROUND or LEGAL_MODEL_RECONSTRUCTED
DSD_AUDIT_VERDICT: PASS_WITH_REFINEMENT
REVISION_NEED: CLARIFICATION (Proposition 5.13 quantifier/existence and "channel-faithful" scope)
SOURCE_PDF_OR_ZENODO_CHANGED: no
FULL_F2_PAPER_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
PREVIOUS_STANDALONE_NAMED_CASE_COUNTS: 14 theorem / 2 proposition / 9 corollary
ADDITIONAL_GROUPED_SOURCE_LABELS_THIS_CASE: 10 propositions / 2 corollaries / 1 countermodel / 1 definition
PREVIOUS_UNNUMBERED_SECTION_APPENDIX_AUDITS: 9 (unchanged; this group tracks numbered Section 5 claims)
NEXT: FAS-F2-G4-CLAIM-INVENTORY-001 / NOT_STARTED
```

**Counting caution:** Previously reported 14/2/9 represented separately identified audit cases, and did not count, e.g., Proposition 4.12 or Corollaries 4.8/4.11/4.14 reviewed within the grouped Section 4.3 audit, nor some Section 2 and Section 4 source items. Therefore simply adding 10 and 2 to 2 and 9 **does not produce a trustworthy all-paper count of distinct audited numbered labels**. The next G4 step must reconcile every source-labelled definition, theorem, proposition, lemma, corollary and countermodel against evidence and distinguish `standalone` vs `bundled` vs `not reviewed` rather than announcing all claims cleared.

Historical independent advisories retained without silent resolution: Theorem 4.7 six-clause independence phrasing; §7.3 D2 exposure/boundary detail; §8 fixed-J comparison overstrength. This case adds a localized Proposition 5.13 wording-scope advisory. No new primitive-axiom contradiction discovered and no external-independent validation.


**Reciprocal Notion case:** https://app.notion.com/p/40081f51e7fa8148b69ec47a9898b7f6
