# Exact External Reconstruction-Theorem Interface and Anti-Post-Hoc Rule

Status: **methodology / comparator interface**  
Applies to: DSD core-theory reconstruction programs that compare a DSD specialization with an external reconstruction theorem.

## 1. Rule

A DSD specialization may invoke an external reconstruction theorem only after every theorem hypothesis has been mapped to an explicit DSD-side datum, derived result, or declared specialization assumption.

Vocabulary similarity is never sufficient.

## 2. Four provenance classes

Every interface condition must be labeled:

```text
A  PRE_EXISTING_DSD
B  GENERAL_OPERATIONAL_DERIVATION
C  TARGET_SPECIALIZATION_SELECTOR
D  EXACT_COMPARATOR_LOCK
```

Interpretation:

- **A** existed in DSD before the target theory was used.
- **B** was derived from general operational semantics and is not target-specific.
- **C** was introduced while specializing toward the target theory.
- **D** was introduced specifically to make an external theorem's hypothesis exact.

Only A and independently validated B conditions may count as evidence that DSD recovered a target structure independently.

C and D may establish compatibility or conditional theorem applicability, but must not be counted as independent derivation evidence.

## 3. Exact theorem-interface checklist

For every external theorem record:

```text
THEOREM_ID
SOURCE
DOMAIN
OBJECT_CARRIER
TOPOLOGY / REGULARITY
STATE assumptions
EFFECT assumptions
COMPOSITE assumptions
TRANSFORMATION assumptions
EQUIVALENCE notion
CAPACITY / DIMENSION assumptions
UNIVERSAL QUANTIFIERS
CONCLUSION
```

For every hypothesis write:

```text
EXTERNAL_HYPOTHESIS
DSD_COUNTERPART
PROVENANCE_CLASS
STATUS
BRIDGE / PROOF
COUNTERMODEL IF NOT DERIVED
```

Allowed statuses:

```text
DERIVED
CONDITIONAL_DERIVATION
EXPLICIT_ASSUMPTION
NOT_EQUIVALENT
GAP
REJECTED
```

## 4. Theorem-transfer gate

An external theorem may be invoked conditionally only if every hypothesis is `DERIVED`, `CONDITIONAL_DERIVATION`, or `EXPLICIT_ASSUMPTION`, and every required equivalence map is typed and proved adequate.

If any hypothesis remains `GAP` or `NOT_EQUIVALENT`, theorem transfer is blocked.

## 5. Claim discipline

If a theorem is instantiated using any Class-C or Class-D condition, report:

> an external theorem applies to a declared DSD specialization.

Do not report:

> generic DSD derived the external theory.

A theorem conclusion inherited through Class-C/D assumptions is validation of specialization compatibility, not independent evidence for the DSD core.

## 6. Current QM 004E lock

For Mueller's finite-dimensional GPT reconstruction comparator, the currently isolated exact locks are:

```text
OSC-QM      operational state closure / compactness
ETC-QM      exact tomographic composite tensor lock
ULRRDE-QM   universal linear recursive restriction equivalence
CRG-QM      connected reversible group + pure-state transitivity
CFE-QM      capacity-family existence
```

These are Class D unless a later independent DSD argument derives them.

`NR-QM` remains Class C.

`ORD/ORE`, `MPT`, and `OCD` are Class B at present.

`CRD` is a DSD-wide declaration discipline, while `LDC-QM`, `RRDE-QM`, and `CRR-QM` remain target-specialization selectors unless independently re-derived.

## 7. Purpose

This rule protects the core-theory challenge from two different errors:

```text
predefinition contamination
post-hoc target fitting
```

The first is controlled by independent premise locking before comparison.

The second is controlled by provenance labeling after new target-specific conditions are introduced.
