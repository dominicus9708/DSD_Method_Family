# PA-P21-20260901-FULL-COMPLETION-ADVERSARIAL-SERIALIZATION-001 — audit result

**Date:** 2026-10-25 KST. **Author:** Kwon Dominicus.
**Frozen source:** original Property Axiom System English PDF (2026.09.01), SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Prospective plan:** [P21 preregistration](P21_FULL_COMPLETION_ADVERSARIAL_SERIALIZATION_PRECOMMIT.md).
**Tested implementation:** unchanged P20 full primitive-preserving reference C1 code, original Git blob `9fac2c171834f126b9af12d8fedde3e0fbc59b23`. Original mathematical author PDF, previous Python and Zenodo untouched.

## Audited outcomes

**Independent P21 Python** [source](scripts/verify_p21_adversarial_full_completion.py) executed **30 expected positive and negative observations** on two Python versions. These include actual code limitations rather than thirty guarantees of correct arbitrary-input handling.

- Repeated identical (input,value) pairs in a partial-function graph are reduced to a Python dict by P20's canonical snapshot. The **mathematical extensional function** is preserved, but `RedProp(CompProp(P))` is NOT identical as a Python presentation if P originally serialized the same graph entry twice. This is a presentation-identity issue, **not** a counterexample to Theorem3.7 for mathematical functions.
- Conflicting repeated input with two different values is rejected as not a function.
- P20's `frozen=True` dataclasses hold **mutable nested dictionaries**. Mutating the primitive inside a produced Completion invalidates the derived fields; `full_is_valid` detects this and `red_prop` rejects it. Altering the caller-owned primitive AFTER completion does not alter the snapshot's container dictionaries.
- However, typed carrier elements may be mutable hashable custom objects; P20's snapshot retains references to them. Such a reference can be mutated externally without the full model ceasing to validate. This **object-immutability/aliasing scope gap** is genuine at the Python representation level.
- Every independently tampered derived coordinate (domain, prerequisite-satisfied, status, unavailable-kind set, record set) is rejected; the reduction check refuses it.
- Source-extra metadata remains distinct under `ignore` versus `reject` policies.
- A malformed, unhashable auxiliary-carrier element still triggers uncaught `TypeError` via P17 admission validator. No P17/P20 code was edited.
- NaN is non-reflexive in ordinary Python float equality; it must not be used uncritically as if it were an ordinary mathematical set element without defined equivalence semantics.
- Stage-VI inherited Formation base in P20 is a **plain anchor string**, not a verified full Formation Stage-VI descriptor.

**Mathematical boundary:** None of these examples disproves source Theorem3.7 for admitted mathematical property cores, whose primitive functions and typed values are treated extensionally. The printed §6 source conditions 2 and Theorem4.3's “relative to C1” proof scope continue OPEN.

## Execution and archive evidence

- [First actual CI #40114853583](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40114853583): **30/30 expected observations** pass in Python 3.10 and 3.12; emitted full live detailed JSON into workflow logs.
- A deliberately too-strict archive comparison after storing a compact P21 summary was **unsuccessful**: [workflow #40114938401](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40114938401). It compared complete live detailed JSON against intentionally shorter archived summary JSON. This was an audit-control mistake, not a failed source mathematical test. Preserve this run in the audit trail.
- [Final archive-scoped CI #40114963231](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40114963231): Python 3.10 and 3.12 both **completed/success**. Each independently reran **30** check flags, confirmed all are true, and compared the **summary-only stored fields** against the live generated detailed results. Both printed `P21 ARCHIVED SUMMARY AND ALL 30 CHECK FLAGS MATCH`.
- [Archived *summary*, not full output JSON](results/p21_full_completion_adversarial.json). Full detailed JSON remains available as a CI log; DO NOT assert bit-for-bit full JSON archival.

## Closure

```text
CASE: PA-P21-20260901-FULL-COMPLETION-ADVERSARIAL-SERIALIZATION-001
SOURCE_PDF_SHA256: 03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c
FINITE_EXPECTED_OBSERVATIONS: 30/30 PASS
PYTHON_3_10_3_12_FINAL_ARCHIVED_SUMMARY: PASS / RUN 40114963231
P20_FULL_COMPLETION_MUTABLE_ALIASES: CONFIRMED
P20_SERIALIZATION_PRESENTATION_EQUALS_MATHEMATICAL_FUNCTION: NOT_ALWAYS
P20_MALFORMED_PYTHON_TYPED_INPUT_ROBUSTNESS: OPEN
SOURCE_THEOREM3_7_REFUTED: NO
SOURCE_SECTION6_TWO_GAPS: OPEN
SOURCE_THEOREM4_3_C1_QUALIFIER: OPEN
WHOLE_PROPERTY_FPA: OPEN
ORIGINAL_P20_AND_AUTHOR_PDF_CODE_ZENODO_MODIFIED: NO
NEXT: PA-P22-20260901-PRIMITIVE-IDENTITY-AND-STAGEVI-INTERFACE-001 / NOT_EXECUTED
```

**Windows 11:** from the existing `DSD_Method_Family` checkout root:
```powershell
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p21_adversarial_full_completion.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p21_full_completion_adversarial.json
```
**Caution:** this direct command writes **detailed** JSON to the specified file and will overwrite the committed summary-only JSON. For archival comparison, regenerate in a separate temporary output path and compare the common summary keys instead.
