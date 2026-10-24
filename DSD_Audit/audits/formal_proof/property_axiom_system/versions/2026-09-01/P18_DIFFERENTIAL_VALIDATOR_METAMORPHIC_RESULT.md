# PA-P18-20260901-DIFFERENTIAL-VALIDATOR-METAMORPHIC-AUDIT-001 — executed independent follow-on audit

**Date:** 2026-10-24 KST. **Original author:** Kwon Dominicus.
**Source locked:** `DSD_Property_Axiom_System_EN(4).pdf` printed 2026.09.01, 23 pp, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**P18 prospectively frozen obligations:** [P18 precommit](P18_DIFFERENTIAL_VALIDATOR_METAMORPHIC_PRECOMMIT.md) (commit `9fb3040676128101bf23828c3fc8f2a44c4273eb`). This P18 was run after [P17's independently verified 30-self/13-original tests](P17_INDEPENDENT_TYPED_REFERENCE_VALIDATOR_RESULT.md).

## Mathematical problem and independent tests

Instead of retesting the same positive P17 examples, P18 applied **adversarial metamorphic changes** to the P17 reference-typed model and verified the expected invariants or transitions:
1. A mixed typed signature with inherited input sort `h`, supplied aux sorts `u,v`, property kinds `p:(u,v),q:(v,u),r:(u,u),hkind:(h,u)`, and two independent prerequisites `d1,d2`.
2. **Bijection relabeling** independently on u and v: all input tuples, applicability sets, prerequisite-satisfaction sets and partial assignment graphs are transported while property kinds and coordinate order are fixed. The original and transported primitive cores remain admitted, complete input statuses are pointwise transported, and domain and prerequisite-satisfied counts agree.
3. **Input-order probes** reject `(v1,a)` when supplied in property profile `(u,v)`, and reject insufficient tuple arity. Repeated-sort `(u,u)` retains both independent positions. Inherited `h` is fixed, not relabeled.
4. **Type-soundness mutations** (missing one mandatory Ap/Sat/Xi coordinate, wrong value carrier, conflicting same-input assignments) change classification to `INVALID_PRESENTATION` rather than confusing a typing violation with a typed axiom counterpremodel.
5. **Axiom-only violations:** correctly typed `D⊆Ap` with a value outside the intersection `Sat_{d1}∩Sat_{d2}` is `TYPED_PREMODEL` with PI true/PII false. A `D⊄Ap` but `D⊆DepSat` case is `TYPED_PREMODEL` with PI false/PII true. Both are rejected as inputs to the reference `completion` function.
6. **Empty prerequisite family:** no contextual prerequisite conditions means `DepSat=X` (the full typed product). This is not mistakenly interpreted as the empty set.
7. **Supplied-empty versus unsupplied:** where v is explicitly supplied `∅`, the property product `(u,v)` is a defined empty product, and an empty primitive coordinate is well typed. Where v is unsupplied, there is **no typed product** and the kind gets a profile-unavailable C1 status. No conversion of unavailability into a supplied empty carrier occurs.
8. **Surplus metadata:** explicitly compare `ignore` versus `reject` modes. This is a chosen input-admission policy, not an automatically established theorem about surplus metadata in the paper.
9. **C1 nonmutation:** completion constructs derived coordinates without rewriting the supplied primitive data.

### Actual computation

- [Independent P18 Python](scripts/verify_p18_reference_metamorphic.py) imports the **unaltered P17 reference code** and performs **47 distinct Boolean controls**. The source main test case uses finite set-coded input carriers; its universal status is NOT formalized.
- Initial [actual GitHub Actions run #40085702953](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40085702953): Python 3.10 and 3.12 both **PASS 47**, but a P18 JSON key inadvertently contained two zero-width characters. This was a **serialization label issue only**; audited P17 reference code and original algorithms were unchanged.
- P18-owned JSON field spelling normalized in a follow-up P18-only commit. [Actual run #40085753470](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40085753470) confirmed **47 PASS** under Python 3.10 and 3.12, and both machine-generated output JSONs were independently parsed from real job logs and matched.
- Committed actual [P18 result JSON](results/p18_reference_metamorphic.json) to the versioned results folder.
- [Archived JSON replay run #40085788170](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40085788170) **completed/success** under Python **3.10 and 3.12**. Each printed `P18 METAMORPHIC PASS 47` and `P18 ARCHIVED JSON MATCH`.

## What P18 does and does not establish

**Established within tested finite scope:** new independent reference validator preserves typed set validity and status classification under consistent carrier bijection renaming; rejects malformed input; separates correctly typed PI-only vs PII-only violations; respects inherited and repeated sorts, domain requirements, zero prerequisites and C1 completion rules. 47 controls passed in two Python versions with archived JSON parity.

**Not established:**
- an all-signature/all-set complete ZFC formalization;
- a verified full implementation of the entire Stage-VI inherited Formation model;
- a proof of arbitrary-domain manuscript category theorems;
- any repair of manuscript §6's two missing morphism conditions;
- a resolution of printed Theorem4.3's “relative to C1” interpretation, without later manuscript clarification;
- external independent referee review or author-source EN/KR LaTeX parity.

P18 **did not** modify the P17 reference code, the original `Property_Axiom_System` source, its original historical fixtures, the author's PDF/TeX, or Zenodo.

## Windows 11 replay (repository-root relative)

In the existing `DSD_Method_Family` checkout:
```powershell
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p18_reference_metamorphic.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p18_reference_metamorphic.json
```
It uses the P17 reference validator in the **same `scripts/` directory**, with no external numerical input file. This locally overwrites the P18 result JSON; run in a clean checkout or compare its parsed JSON to the archived record.

```text
CASE: PA-P18-20260901-DIFFERENTIAL-VALIDATOR-METAMORPHIC-AUDIT-001
SOURCE_EXACT_PDF_SHA256: 03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c
P18_REFERENCE_METAMORPHIC_CHECKS: 47/47 PASS
PYTHON_3_10_ARCHIVED_REPLAY: PASS
PYTHON_3_12_ARCHIVED_REPLAY: PASS
P17_REFERENCE_CODE_MODIFIED: NO
ORIGINAL_EXPERIMENT_OR_MANUSCRIPT_MODIFIED: NO
MANUSCRIPT_§6_TWO_PRINTED_CONDITION_GAPS: OPEN
Th4_3_RELATIVE_TO_C1_PROOF_SCOPE: OPEN
GENERAL_PROPERTY_FPA: OPEN
NEXT: PA-P19-20260901-REFERENCE_VALIDATOR_LIMITS-AND-RELEASE-GATE-001 / NOT_STARTED
```
