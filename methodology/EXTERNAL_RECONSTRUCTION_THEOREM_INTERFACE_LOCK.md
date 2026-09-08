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

## 8. QM Core 004F resolution — OSC-QM

QM Core 004F tested whether operational-state closedness can be derived from existing Class-A/Class-B structure.

Result:

```text
Formation definitional closure                       != topological closure
complete Property descriptor                         != topological closure
Banach-valued static carrier                         != closed physical image
regular dynamic slice admissibility                  != closed global state family
ORD/ORE + finite separation + bounded coordinates    != compactness
```

Countermodel:

\[
\Omega=(0,1)\subset\mathbb R
\]

is bounded, convex, and compatible with affine randomized-preparation readouts, but is not closed.

The sufficient exact lock is sequential operational limit admission in the finite evaluation carrier:

\[
\iota(\omega_n)\to v
\Longrightarrow
\exists\omega\in\Omega:\ \iota(\omega)=v.
\]

In finite dimension, this yields closedness; bounded probability coordinates then yield compactness.

Current provenance remains:

```text
OSC-QM / SOLA-QM    D  EXACT_COMPARATOR_LOCK
```

Status:

```text
NOT DERIVED FROM CLASS A/B
EXPLICIT ASSUMPTION REQUIRED FOR THE CHOSEN THEOREM INTERFACE
```

This resolution narrows the theorem-interface gap without increasing the independent DSD-derived evidence count.

## 9. QM Core 004G resolution — CRG-QM

QM Core 004G tested whether connectedness of the full reversible-transformation group follows from DSD Dynamics/lineage or from continuous pure-state reachability.

Result:

```text
strict Formation equivalence                         != connected reversible topology
continuous regular DSD trajectories                  != connected full reversible group
lineage preservation                                 != connected full reversible group
continuous pure-state reachability                    != connected full reversible group
```

Countermodel:

\[
G=O(2)
\]

acting on the unit circle. `SO(2)` supplies continuous reversible paths between any two pure states, while `O(2)` also contains determinant-`-1` reflections. The continuous determinant map separates the `+1` and `-1` components, so the full reversible group is disconnected.

Thus the earlier `CRR-QM` selector is strictly weaker than the comparator's Continuous Reversibility condition.

A sufficient exact lock is:

```text
RGPR-QM  Reversible-Group Path Realizability
```

requiring an explicit topology on the reversible group and a continuous path from the identity to every allowed reversible transformation. Together with pure-state transitivity this yields the required CRG-QM condition.

Current provenance remains:

```text
CRG-QM / RGPR-QM    D  EXACT_COMPARATOR_LOCK
```

Status:

```text
NOT DERIVED FROM CLASS A/B
CRR-QM IS STRICTLY WEAKER
EXPLICIT CLASS-D ASSUMPTION REQUIRED FOR THE CHOSEN THEOREM INTERFACE
```

After 004F–004G, two of the five 004E locks are classified rather than left open. The unresolved locks are:

```text
ETC-QM
ULRRDE-QM
CFE-QM
```

The theorem-transfer gate remains blocked until these are likewise resolved or explicitly adopted.
