# PA-P15-20260901-C1-COUNTERMODEL-SEMANTICS-001 — independent metatheoretic audit

**Executed:** 2026-10-24 KST. **Author:** Kwon Dominicus.
**Exact manuscript:** `DSD_Property_Axiom_System_EN(4).pdf`, 23 PDF pages, printed 2026.09.01, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Precommit:** [P15 prospective audit plan](P15_C1_COUNTERMODEL_SEMANTICS_PRECOMMIT.md), preserved *before* executing the independent Python.
**Source passages verified:** Definition 2.5 and Definition 2.6 (printed pp7–8), Primitive Axioms I/II and Definition 3.3 and C1 (pp8–9), Theorem 3.7 (p10), Countermodels 4.1/4.2 and Theorem 4.3 and Proposition 4.4 (pp10–11), Theorem 11.1(3) (p19). Original PDF, TeX, public archive and previous Python sources remain unchanged.

## 1. General theorem on primitive soundness and exclusive status sets (independent proof)

Fix any *typed, declared, profile-available* input product `X=X_A,varpi`, primitive `Ap⊆X`, `Dep=DepSat_A,varpi⊆X`, and partial assignment domain `D=Dom Xi_A,varpi⊆X`. No PI/PII is presumed.

Define the four raw predicates by exact source Definition 3.3 set clauses:
- `S_inapp=X\Ap`;
- `S_unsat=Ap\Dep`;
- `S_undef=(Ap∩Dep)\D`;
- `S_defined=D`.

The union is always **X**, with no need for either primitive axiom: membership in `X\Ap`, `Ap\Dep`, or `Ap∩Dep` exhausts X; the final subset splits according to D. However the four sets need **not** be disjoint on a typed premodel.

**Theorem (proved elementwise for arbitrary sets):**

```text
[S_inapp, S_unsat, S_undef, S_defined form a pairwise disjoint partition of X]
     if and only if
        [D ⊆ Ap] AND [D ⊆ Dep].
```

**Forward proof:** If `S_defined∩S_inapp=∅`, then `D∩(X\Ap)=∅`, so `D⊆Ap` (PI). If also `S_defined∩S_unsat=∅`, then `D∩(Ap\Dep)=∅`; together with `D⊆Ap` this implies `D⊆Dep` (PII). These are exact primitive axioms for this kind.

**Reverse proof:** If `D⊆Ap∩Dep` holds, defined inputs can lie in none of the other three regions; the remaining first three are automatically pairwise disjoint because they have respectively `¬Ap`, `Ap∧¬Dep`, `Ap∧Dep∧¬D`. They cover X along with D.

The theorem extends componentwise to every declared profile-available kind (no need for finite X). The defined-zero / defined-nonzero refinement is a further disjoint split of `S_defined` when the value carrier has a designated zero; it does not fix any premodel-level overlap between defined and inapplicable/unsatisfied. The undeclared and profile-unavailable statuses are **kind-level** and not false instances of an absent typed input product.

**Important consequence:** If one promotes *globally exclusive* C1 statuses to an extra all-premodel axiom, that axiom **already implies PI and PII**. Their independence does **not** hold relative to *that stronger* exclusive-status axiom class. This observation is about the interpretation of an extended C1, not a contradiction inside already admitted full property cores.

## 2. Both source countermodels and exact raw-predicate overlaps

**Countermodel 4.1:** X={x}, `Ap=∅`, `Dep={x}`, `D={x}`. Then PI fails, PII holds. The same input lies simultaneously in `S_inapp` and `S_defined`. If a priority-ordered software label returns just `inapplicable`, it does not preserve the semantic equivalence `defined iff x∈D` that Definition 3.3(6) would provide on admitted full cores.

**Countermodel 4.2:** X={x}, `Ap={x}`, `Dep=∅`, `D={x}`. Then PI holds, PII fails. The input lies simultaneously in `S_unsat` and `S_defined`. The chosen one-label priority output again masks a raw predicate.

**Both countermodels are correctly typed property *premodels*** by Definition 2.5, but not admitted *primitive property cores* by Definition 2.6. They **prove independence of PI and PII over the typing conditions alone**. They do **not** by themselves prove independence in a class where every premodel is already required to have an exclusive status partition.

## 3. Four possible meanings of “relative to C1” — do not conflate

**A. Literal C1 as a completion operation ONLY on primitive cores (printed C1):**
C1 starts `Given a primitive property core`, i.e., an object already satisfying both PI and PII. Countermodels 4.1/4.2 lie **outside this operation's domain**. Hence the source's one-paragraph Theorem 4.3 proof alone does not establish the theorem “relative to C1” if that phrase means relative to the class of already completed cores. It is a **scope gap**, not a claim that PI and PII are logically dependent over typing.

**B. C1 as an implication with a full-core antecedent:**
If `C1(P)` is intended merely as `if PI(P)∧PII(P), the completion formulas determine a full core`, then counterpremodels failing an axiom satisfy that *conditional premise vacuously*. Independence can coexist with this conditional C1, but “relative to C1” adds **no independent restriction** to these countermodels. Explicit presentation is required to avoid misunderstanding.

**C. Conservative definitional extension `C1^{raw}` of *all typed premodels*:**
Introduce new symbols `D,DepSat,Rprop,S_inapp,S_unsat,S_undef,S_defined` by **explicit formulas** and interpret statuses as **possibly overlapping Boolean predicates or sets**, *not* an exhaustive mutually exclusive **single-valued** status function. Given any typed premodel, there is exactly one expansion interpreting these new symbols by their defining formulas. Conversely forgetting these symbols recovers precisely the same typed premodel. Hence the expansion is conservative over the typed background: it cannot by itself entail PI or PII, and both source countermodels expand uniquely. Under this **explicit additional metatheoretic convention**, mutual nonderivability remains **valid relative to C1^{raw}**. This is a mathematically valid *clarification option*, but not a statement that the paper literally defines C1 on axiom-violating premodels.

**D. Strong all-premodel `C1^{exclusive}` with an exclusive single-valued status partition matching every Definition 3.3 predicate:**
As §1 proves, `C1^{exclusive}` implies PI and PII. In this class there can be no countermodel to either axiom: any “independence relative to C1^{exclusive}” claim is **false**. A *priority-function* reinterpretation assigning just one label for the first applicable condition can be total for all typed premodels, but cannot also retain the biconditional defined-status semantics of Definition 3.3(6) on those invalid premodels. It is another explicitly changed notion, not automatic source equivalence.

**Source verdict:** Printed Theorem 4.3's *typed-background* independence is **SUPPORTED**. Its phrase **“relative to ... Definitional Closure Clause C1” is NOT YET VALIDATED AS PRINTED**, because A, B, C, D have substantively different consequences and the printed C1 explicitly starts from an admitted primitive property core. This is a **third, separate metatheoretic proof-scope issue**, distinct from the two previously confirmed source Section-6 typing/characterization issues. Do not claim a new inconsistency of the sound admitted property cores.

## 4. Independent finite exhaustive computation and actual dual-Python CI

New separate [source-locked P15 checker](scripts/verify_p15_c1_premodel_semantics.py), with actual [archived JSON](results/p15_c1_premodel_semantics.json). It constructs **every subset** `Ap,DepSat,D⊆X` for X of sizes 0,1,2,3. For one prerequisite d, choosing `Sat_{varpi,d}=DepSat` realizes every tested DepSat, so the tested set triples are typed primitive presentations (with any fixed defined assignment value on D). All source countermodel truth assignments are included.

| |X| | Number of typed premodels | Both PI & PII | Exclusive status partitions | Overlapping-status premodels |
| --- | ---: | ---: | ---: | ---: |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 8 | 5 | 5 | 3 |
| 2 | 64 | 25 | 25 | 39 |
| 3 | 512 | 125 | 125 | 387 |
| **Total** | **585** | **156** | **156** | **429** |

The four-count relation is exactly `8^n` total, `5^n` admitted/partitioned, `8^n−5^n` invalid/overlapping for each n. It *illustrates* the separately provided arbitrary-set proof, not a replacement for it.

**Initial actual GitHub Actions [#40030313786](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40030313786):** `completed/success`, Python 3.10 and 3.12 both computed 585,156,429 and generated **exactly the same JSON** extracted from the actual CI job logs and then committed.

**Archive-replay actual GitHub Actions [#40030362094](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40030362094):** `completed/success`, Python 3.10 and 3.12 both executed the frozen script and printed `P15 ARCHIVED JSON MATCH`. Source SHA256 `f256daf3acbe5a178406b2b995b085e7ecdc1a625c437d01affe189d0a968c85`; fresh JSON SHA256 `256cce709d060902a019a6c9fc16b8d48dd37c4c2004f851aab1051bfce0b956`. Neither result is an automatically machine-checked arbitrary-cardinality proof.

## 5. Consequences for printed other sections and code

- **Theorem 3.7 and C1 unique completion:** still **SUPPORTED** on actual primitive cores satisfying PI and PII. These statuses partition correctly; C1's unique function construction and reduction inverse do not rely on any invalid premodel.
- **Proposition 4.4 (non-typing tautologies):** still **SUPPORTED** independently from countermodels typed via Definition 2.5.
- **Proposition 4.5 and Corollary 4.6:** valid full-core counterexamples, unaffected by the above ambiguity.
- **Theorem 11.1(3):** inherits Theorem 4.3's C1-relative qualification; maintain `PROOF_SCOPE_OPEN`, but not downgrade typing-based PI/PII independence.
- **Existing `Property_Axiom_System` Python `status()`:** is a priority-ordered label function when run on counterpremodels, as found in P14R negative controls; its returned label is **not** a faithful enumeration of all raw predicates in those invalid premodels. Its output on valid PI/PII-sound cores remains appropriate.
- **Two independent §6 issues** (unguarded declared/unavailable source profiles in F3–F5, bare componentwise-bijective embedding shorthand without S2/S3) remain `OPEN`; no blending with the distinct C1-relative metatheory issue.

## 6. Non-edit conclusion, explicit possible future wording (not inserted into author source)

A *possible* future clarification of the mathematical argument would distinguish:
1. `Mutual nonderivability over the class of well-typed property premodels` (proved as printed by the two countermodels); from
2. `Conservatively defining raw completion coordinate sets on all typed premodels` (the conditional general argument proven in P15); from
3. `Applying C1's exclusive full status completion only to well-typed cores satisfying both PI and PII` (original intended full models).

Only a later authorized manuscript section edit should decide how to express this; no reclassification as “new axiom failed” or deletion of the countermodels is justified.

```text
CASE: PA-P15-20260901-C1-COUNTERMODEL-SEMANTICS-001
EXACT_SOURCE_EN_20260901_SHA256: 03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c
GENERAL_EXCLUSIVE_PARTITION_IFF_PI_AND_PII: PROVED_BY_ELEMENTWISE_SET_ARGUMENT
TYPED_PREMODEL_MUTUAL_INDEPENDENCE: PROVED
C1_RAW_CONSERVATIVE_EXTENSION_PRESERVES_INDEPENDENCE: PROVED_UNDER_EXPLICIT_ADDED_INTERPRETATION
C1_EXCLUSIVE_ALL_PREMODELS_PRESERVES_INDEPENDENCE: FALSE
PRINTED_THEOREM_4_3_RELATIVE_TO_C1: PROOF_SCOPE_NOT_ESTABLISHED_AS_WRITTEN
ORIGINAL_FULL_CORE_C1_THEOREM_3_7: NOT_REFUTED
FINITE_PREMODELS_CHECKED: 585
FINITE_STATUS_PARTITIONS: 156
FINITE_STATUS_OVERLAPS: 429
PYTHON_3_10_3_12_RUN: PASS / ARCHIVED_JSON_EQUAL
ORIGINAL_EXPERIMENT_PYTHON_PDF_TEX_ZENODO_MODIFIED: NO
SECTION_6_PRINTED_GAPS: 2 OPEN
WHOLE_PROPERTY_FPA: OPEN
NEXT: SOURCE_AND_CODE_TYPE_VALIDATION_OBLIGATION_MATRIX (NONEDIT) / NOT_STARTED
```
