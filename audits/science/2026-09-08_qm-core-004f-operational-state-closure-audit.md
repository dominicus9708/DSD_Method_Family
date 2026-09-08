# QM Core Reconstruction 004F — Operational State Closure / Compactness Gate

Date: 2026-09-08  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge**  
Target: whether the OSC-QM compactness lock isolated by QM Core 004E can be derived from pre-existing DSD structure or from the general operational structure already established in 004D.

## 1. Research question

QM Core 004E isolated

```text
OSC-QM = operational state closure / compactness
```

as one of five exact theorem-interface locks still separating the current DSD quantum specialization from the chosen external finite-dimensional GPT reconstruction theorem.

The present gate asks:

1. Does Formation "completion" imply topological closure of the operational state image?
2. Does the Property complete descriptor imply closure?
3. Does use of a Banach output carrier in Static Aggregation imply that the physically realized state image is closed?
4. Does time-indexed admissible Dynamics imply closure of the whole operational state family?
5. If not, what extra condition is sufficient to recover compactness in the finite evaluation carrier of QM Core 004D?

The answer is:

```text
generic DSD completion -> topological closure             NO
general 004D convex operational quotient -> closure      NO
Banach codomain -> closed physical state image            NO
admissible trajectories -> globally closed state family   NO
explicit sequential limit admission -> closure            YES
finite-dimensional + bounded + closed -> compactness      YES
```

Therefore OSC-QM is **not derived** from current Class-A/Class-B structure.

## 2. Source-locked DSD distinctions

### 2.1 Formation completion is definitional, not topological

The Formation Axiom System separates four primitive stages from three definitional closure clauses. Relative to supplied data, the closure clauses uniquely determine derived configuration, channel, and finite-composition coordinates.

This use of "closure" is logical/definitional closure of a typed descriptor. It does not supply:

```text
a topology on the model class
a metric on physical states
a limit-admission rule
closedness of an image in an analytic carrier
compactness of a specialization state space
```

A complete formation descriptor can therefore be perfectly complete in the DSD sense while the set of physically admitted operational states of a later specialization is topologically open.

### 2.2 Property completion is status completion, not limit completion

The complete core property descriptor retains declared kinds, applicability data, prerequisite satisfaction, partial assignment domains, statuses, and defined records.

It preserves distinctions such as applicable-but-undefined and defined zero. Nothing in this status-sensitive completion states that a convergent sequence of property-bearing physical states must have an admitted limit state.

Thus:

\[
\boxed{
\text{complete typed property descriptor}
\not\Rightarrow
\text{topologically closed physical state carrier}.
}
\]

### 2.3 Banach completeness is codomain completeness

Channel-Indexed Static Aggregation uses Banach spaces to ensure well-defined Bochner-valued analytic outputs and, in the optional countable extension, convergent absolutely summable series.

But a complete codomain need not have every physically realized subset closed.

For example, the inclusion

\[
(0,1)\hookrightarrow\mathbb R
\]

has complete Banach codomain \(\mathbb R\), while the realized image \((0,1)\) is not closed.

Therefore:

\[
\boxed{
\text{Banach output carrier}
\not\Rightarrow
\text{closed operational state image}.
}
\]

### 2.4 Dynamics requires admissible slices, not completion of the state family

Structural Reorganization Dynamics requires each instantaneous slice used by a model to be admissible relative to its predecessor interfaces. It can add regularity, locality, lineage, constitutive laws, and time dependence.

That rule does not say that every limit point of all admissible slices must itself be an admitted physical state.

A trajectory may live entirely inside an open admissible regime and approach an excluded boundary as a parameter approaches an endpoint not included in its domain.

Thus dynamic slice admissibility is distinct from global state-space closedness.

## 3. Countermodel: convex, bounded, operationally separated, but not closed

Take the operational state image

\[
\Omega=(0,1)\subset\mathbb R.
\]

Use the single separating readout

\[
e(x)=x.
\]

Every state has normalized evaluation form

\[
\iota(x)=(1,x).
\]

The state image is bounded.

It is also convex: for every \(x,y\in(0,1)\) and \(\lambda\in[0,1]\),

\[
\lambda x+(1-\lambda)y\in(0,1).
\]

Therefore the ORD/ORE randomization semantics of QM Core 004D can be satisfied inside this open carrier.

However the sequence

\[
x_n=\frac1n,
\qquad n\ge2,
\]

satisfies

\[
x_n\in\Omega,
\qquad
x_n\to0,
\qquad
0\notin\Omega.
\]

Hence

\[
\boxed{
\text{finite-dimensional + bounded + convex + affine readout}
\not\Rightarrow
\text{closedness}.
}
\]

This is a direct countermodel to deriving OSC-QM from the 004D operational carrier alone.

## 4. Why DSD "complete descriptor" does not repair the countermodel

For every \(x\in(0,1)\), one may attach a fully specified DSD-compatible specialization descriptor containing, schematically,

```text
formation status
property status
readout status
value x
```

Every admitted state can therefore be descriptively complete relative to its declared model.

This still does not admit the absent boundary state \(x=0\).

The missing limit point is not an omitted field inside an existing descriptor. It is a missing **physical state object** from the specialization carrier.

Therefore adding more fields to each descriptor cannot substitute for a limit-admission principle.

## 5. Sufficient condition: operational limit admission

Let \(\iota:\Omega\to V\) be the finite-dimensional evaluation embedding supplied by QM Core 004D.

Define the following theorem-interface condition.

### Sequential Operational Limit Admission — SOLA-QM

Whenever

\[
\iota(\omega_n)\to v\in V
\]

for a sequence of admitted operational states \(\omega_n\in\Omega\), require that there exists an admitted operational state \(\omega\in\Omega\) such that

\[
\iota(\omega)=v.
\]

In finite-dimensional metric spaces, sequential closedness is equivalent to closedness. Hence SOLA-QM implies that \(\iota(\Omega)\) is closed.

Because evaluation coordinates are probability coordinates in \([0,1]\), the finite-dimensional image is already bounded.

Therefore, by finite-dimensional Heine-Borel,

\[
\boxed{
\text{finite evaluation carrier}
+
\text{bounded probability coordinates}
+
\text{SOLA-QM}
\Rightarrow
\text{compact operational state image}.
}
\]

This is a valid theorem-interface route to the compactness assumption.

## 6. Provenance classification

SOLA-QM / OSC-QM is not promoted to generic DSD.

Current provenance:

```text
OSC-QM / SOLA-QM    Class D — EXACT_COMPARATOR_LOCK
```

Reason:

- no equivalent rule existed in the original Formation, Property, Static Aggregation, or Dynamics cores;
- 004D's general operational randomization semantics does not force it;
- it is being isolated now because the chosen external reconstruction theorem requires compact normalized state spaces.

A later independent physical or DSD-native argument could reclassify a limit-admission rule, but no such derivation is established here.

## 7. Why automatic closure would be too strong for generic DSD

Generic DSD should be able to describe regimes whose admissibility conditions use strict inequalities or whose boundaries represent a different formation regime.

For such models, automatically adjoining every analytic limit point would silently change the physical carrier and possibly change formation identity, property applicability, or lineage status.

The simple witness

\[
(0,1)\longrightarrow[0,1]
\]

already shows this: topological completion adds two new states.

Therefore:

\[
\boxed{
\text{topological closure is a physical/admissibility assertion, not harmless bookkeeping}.
}
\]

## 8. Audit outcomes

```text
Claim: Formation definitional closure implies OSC-QM
Outcome: REJECTED

Claim: complete Property descriptor implies OSC-QM
Outcome: REJECTED

Claim: Banach-valued Static Aggregation implies closed physical state image
Outcome: REJECTED

Claim: regular dynamic slice admissibility implies closed global state carrier
Outcome: REJECTED

Claim: ORD/ORE + finite separation + bounded probability coordinates imply compactness
Outcome: NOT_SUFFICIENT_FOR_EXTENSION

Claim: add SOLA-QM to the finite evaluation carrier
Outcome: VALID_IN_DOMAIN -> closed and compact normalized state image
```

Overall audit verdict:

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

The audit succeeds by locating the exact non-implication and by isolating a sufficient lock without misreporting it as DSD-derived.

## 9. Effect on QM Core 004E

The 004E entry

```text
OSC-QM  operational state closure / compactness
```

is no longer merely an unspecified gap.

It is now resolved as:

```text
NOT DERIVED FROM CLASS A/B
EXPLICIT CLASS-D ASSUMPTION REQUIRED FOR THE CHOSEN THEOREM INTERFACE
```

The theorem-transfer gate remains blocked unless OSC-QM/SOLA-QM is explicitly adopted together with the other unresolved exact locks.

This does not count as independent evidence that DSD derived quantum theory.

## 10. Next target — QM Core 004G

Proceed to the second 004E lock:

```text
CRG-QM = connected reversible group + pure-state transitivity
```

The next audit should distinguish:

1. continuous reachability of pure states,
2. connectedness of the entire allowed reversible group,
3. topology inherited from an operational carrier,
4. whether DSD lineage/dynamics can independently force connectedness,
5. whether disconnected but pure-state-transitive reversible groups remain DSD-compatible.

The Class-A/B versus Class-C/D provenance rule remains mandatory.

## 11. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_004f_operational_state_closure_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_004f_operational_state_closure_gate.py --mode all
```

Expected final line:

```text
OVERALL: PASS_WITH_BOUNDARY
```

Finite/analytic witnesses implemented:

```text
open state image remains convex under mixing
bounded + convex does not imply closed
Banach codomain does not close physical image
logical descriptor completion != topological closure
explicit limit admission repairs witness sequence
closure augmentation changes physical carrier
```
