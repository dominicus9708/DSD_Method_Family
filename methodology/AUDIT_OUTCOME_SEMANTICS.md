# DSD Audit Outcome Semantics / DSD 감사 판정 의미 규칙

Status: working operational rule
Date: 2026-09-08

## 1. Purpose

DSD Audit must not use `FAIL` as a catch-all label for every non-implication, non-identity, information-loss case, or scope boundary.

The controlling distinction is:

```text
object/process valid in its declared domain
!= sufficient for an extension task
!= identical to another object/process
!= reconstructible after a reduction
!= globally invalid
```

This rule refines reporting only. It does not alter DSD foundational object statuses or external-domain standards.

## 2. Primary scoped outcome labels

### PASS

The tested claim or operation satisfies the declared criteria in the declared domain.

### VALID_IN_DOMAIN

The object, map, rule, or description works correctly for its declared domain or query family, while no claim is made that it is sufficient outside that domain.

Example:

```text
rho_A is sufficient for all A-local quantum queries
```

under the supplied tensor-product specialization.

### NOT_SUFFICIENT_FOR_EXTENSION

A valid in-domain object or readout does not contain enough information or structure to support a stronger target outside its declared scope.

Example:

```text
(rho_A, rho_B) does not generally reconstruct rho_AB.
```

This is not a failure of the reduced states as local states.

### NON_IDENTICAL

Two valid objects, statuses, or operations must not be identified merely because they are associated, share labels, or may coincide in selected cases.

Example:

```text
local-to-global unreconstructibility != entanglement.
```

### RECONSTRUCTION_LOSS

A reduction/readout/compression map is non-injective on the relevant admissible carrier, so distinct inputs can occupy the same output fiber.

This label records information loss relative to the declared reconstruction target. It does not imply that the reduced output is unusable for every task.

### REJECTED

The tested implication, equivalence, or claim is false under the locked assumptions or is contradicted by an explicit counterexample.

Use `REJECTED` for a claim, not as a status label for a valid object appearing in the counterexample.

### FAIL

Reserve `FAIL` for cases in which the tested object/procedure itself fails its declared in-domain criteria, a required audit condition is violated, or the evidence/procedure is insufficient to support the claimed result after the criteria were locked.

`FAIL` must not be substituted for `NOT_SUFFICIENT_FOR_EXTENSION`, `NON_IDENTICAL`, or `RECONSTRUCTION_LOSS`.

### NO_GAIN

The method or additional DSD structuring produces no justified improvement over the locked baseline for the declared task. This remains distinct from invalidity.

### INDETERMINATE

Available evidence or the locked interface is insufficient to decide the tested claim without adding assumptions that are not yet justified.

## 3. Summary verdicts

A detailed audit may still end with one of the existing summary verdicts:

```text
PASS
PASS_WITH_BOUNDARY
PASS_WITH_REFINEMENT
FAIL
INDETERMINATE
NO_GAIN
```

A summary verdict does not erase the scoped outcomes of individual propositions.

For example:

```text
SUMMARY: PASS_WITH_REFINEMENT

CLAIM A: VALID_IN_DOMAIN
CLAIM B: NOT_SUFFICIENT_FOR_EXTENSION
CLAIM C: NON_IDENTICAL
MAP D: RECONSTRUCTION_LOSS
CLAIM E: REJECTED
```

is internally consistent.

## 4. Reporting rule

For every negative-looking result, ask in order:

```text
1. Did the object/process fail inside its declared domain?
   -> FAIL

2. Is the object/process valid locally but insufficient for a stronger target?
   -> VALID_IN_DOMAIN + NOT_SUFFICIENT_FOR_EXTENSION

3. Are two valid notions merely not the same notion?
   -> NON_IDENTICAL

4. Did a reduction erase distinctions needed for reconstruction?
   -> RECONSTRUCTION_LOSS

5. Is a tested implication/equivalence specifically false?
   -> REJECTED

6. Is there simply no demonstrated added value?
   -> NO_GAIN

7. Is the evidence insufficient to decide?
   -> INDETERMINATE
```

## 5. Relation to shared-core disciplines

This reporting rule operationalizes existing method-family restraints, especially:

```text
SC-05  Aggregate / Information-Loss / Reconstruction Restraint
SC-08  Baseline / Failure-NO_GAIN / Anti-Post-Hoc Discipline
SC-09  Evidence-Status / DSD-Object-Status Separation
SC-10  External-Standard / Domain-Validation Separation
```

It does not create a new shared-core ID at this stage.

## 6. Preservation rule

Historical audit records keep their original labels.

New audits should use the scoped labels above. Old `FAIL` entries should only be reinterpreted or migrated when a later audit explicitly revisits them; no silent historical rewrite is permitted.
