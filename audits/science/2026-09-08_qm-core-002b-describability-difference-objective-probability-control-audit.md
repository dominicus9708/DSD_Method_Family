# QM Core Reconstruction 002B — Describability Difference / Property Handling / Objective Probability Control

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: **whether a DSD describability-difference construction can be used to raise a target quantum outcome probability, and what additional property information must be retained for that claim to be objective**

## 1. Research question

QM Core 002 established a branch-resolved DSD representation of a finite-dimensional quantum instrument.

The present 002B asks a stronger question before proceeding to Born-rule reconstruction:

> If an object-bounded quantum state and a group-bounded measurement/interaction context are given an explicit DSD describability-difference property, can an interaction that reduces that difference objectively raise the target quantum outcome probability?

The question is split into two non-identical cases:

```text
access-only / observer-relative difference
physical state-effect difference
```

The first may change what an observer can condition on.
The second may enter an actual physical transition and thereby change the objective ensemble probability.

This audit does not treat paper-local scope defenses as a prohibition on joining the four DSD layers.

The hard gates are:

```text
well-typed cross-layer placement
mathematical exactness
standard-QM agreement
no hidden replacement of a fixed Born probability by an unsupported extra scalar
```

## 2. DSD source placement

The current four-paper DSD architecture supplies the needed roles.

### Formation

The Formation Axiom System provides stable operational identity and staged comparison structure.
Routine variation of a downstream state/effect property need not be hidden inside the Stage-VI assigned-value coordinate.

### Property

The Property Axiom System allows auxiliary carriers, mixed typed input profiles, contextual prerequisites, and partial assignments.

Therefore an application-level specialization may declare properties such as:

```text
QSTATE
QEFFECT
QPURITY
QEFFECT_NORM
QDESCRIBABILITY_DIFFERENCE
QINTERACTION_SCORE
```

without identifying these with Formation channel identity.

### Static aggregation

The static layer permits vector-valued and other Banach-valued downstream property aggregates.
Hence the difference scalar need not be kept alone; purity and effect-norm data may remain in the same typed reduced descriptor.

This is essential because the audit finds that scalar distance alone loses information relevant to probability change.

### Dynamics

Structural Reorganization Dynamics permits time-dependent property values and supplied constitutive transitions.
It explicitly does not make every aggregate monotone.

Therefore a positive probability-control result must come from an actual supplied physical transition, not merely from declaring that a DSD difference “should decrease.”

## 3. Object-bounded / group-bounded specialization

For this audit, use the following application-level roles.

```text
object-bounded carrier:
    quantum state rho

group-bounded interaction/readout context:
    target measurement effect E
    interaction law Gamma
    observer/access record
```

The words `object-bounded` and `group-bounded` are used here as specialization roles.
The quantitative result below comes from the typed quantum state/effect properties and their interaction.

## 4. Candidate quantum describability-difference property

Let \(\rho\) be a finite-dimensional density operator and \(E\) a fixed Hermitian quantum effect.

Define the representation-level difference

\[
\boxed{
D_Q^2(\rho,E)
=
\|\rho-E\|_{\mathrm{HS}}^2
=
\operatorname{Tr}[(\rho-E)^2].
}
\]

Also retain the typed properties

\[
\pi(\rho)=\operatorname{Tr}(\rho^2)
\]

and

\[
\nu(E)=\operatorname{Tr}(E^2).
\]

Then the elementary operator identity gives

\[
D_Q^2
=
\pi+\nu-2\operatorname{Tr}(\rho E).
\]

Under the standard Born pairing

\[
p_E(\rho)=\operatorname{Tr}(\rho E),
\]

one obtains

\[
\boxed{
2p_E
=
\pi+\nu-D_Q^2.
}
\]

This is the key 002B identity.

It does not derive the Born rule.
It shows how a DSD-style difference property and additional typed properties decompose the already-locked quantum probability.

## 5. Interaction number

Between `before` and `after`, define the raw difference-reduction interaction number

\[
\boxed{
I_D
=
D_{Q,\mathrm{before}}^2
-
D_{Q,\mathrm{after}}^2.
}
\]

Also define

\[
\Delta\pi
=
\pi_{\mathrm{after}}-\pi_{\mathrm{before}},
\]

\[
\Delta\nu
=
\nu_{\mathrm{after}}-\nu_{\mathrm{before}}.
\]

Subtracting the identity in Section 4 gives the exact relation

\[
\boxed{
2\Delta p
=
I_D+\Delta\pi+\Delta\nu.
}
\]

Therefore define the corrected objective interaction score

\[
\boxed{
J_Q
=
I_D+\Delta\pi+\Delta\nu.
}
\]

Then

\[
\boxed{
\Delta p=\frac{J_Q}{2}.
}
\]

For a fixed target effect \(E\),

\[
\Delta\nu=0
\]

and hence

\[
\boxed{
\Delta p=\frac{I_D+\Delta\pi}{2}.
}
\]

For a fixed-purity evolution as well,

\[
\Delta\pi=0
\]

so

\[
\boxed{
\Delta p=\frac{I_D}{2}.
}
\]

Thus in fixed-purity target approach, reducing the selected quantum describability difference is exactly equivalent to increasing the target Born probability.

## 6. Positive witness — fixed-purity interaction

Take the qubit target

\[
E=P_0=|0\rangle\langle0|.
\]

Start from

\[
|+\rangle,
\qquad
p_0=\frac12.
\]

Use a pure-state interaction taking the state to

\[
|\psi\rangle
=
\cos\frac{\pi}{6}|0\rangle
+
\sin\frac{\pi}{6}|1\rangle.
\]

Then

\[
p_0'=\frac34.
\]

The state remains pure, so

\[
\Delta\pi=0.
\]

The Hilbert-Schmidt difference changes from

\[
D_Q^2: 1\to\frac12.
\]

Hence

\[
I_D=\frac12
\]

and

\[
\Delta p
=
\frac{I_D}{2}
=
\frac14.
\]

This is an objective probability increase produced by a physical state transition.

## 7. Positive witness — open-system interaction

Start again from \(|+\rangle\) and apply amplitude damping toward \(|0\rangle\) with

\[
\gamma=\frac12.
\]

The target probability changes

\[
p_0:\frac12\to\frac34.
\]

The selected difference changes

\[
D_Q^2:1\to0.375,
\]

so

\[
I_D=0.625.
\]

Purity changes

\[
\pi:1\to0.875,
\]

so

\[
\Delta\pi=-0.125.
\]

Therefore

\[
J_Q
=
0.625-0.125
=
0.5
\]

and

\[
\Delta p
=
\frac{0.5}{2}
=
0.25.
\]

Thus a purity-changing physical interaction can still objectively raise the target probability, but the raw distance reduction must be interpreted together with the purity property.

## 8. Counterexample — total difference reduction alone is insufficient

Take a qubit with Bloch vector

\[
r=(0.8,0,0.5)
\]

and target \(P_0\).

Initially,

\[
p_0=0.75,
\]

\[
\pi=0.945,
\]

\[
D_Q^2=0.445.
\]

Apply isotropic depolarizing contraction

\[
r\mapsto0.8r.
\]

Then

\[
p_0'=0.70,
\]

\[
\pi'=0.7848,
\]

\[
D_Q'^2=0.3848.
\]

Therefore the total selected distance has decreased:

\[
I_D
=
0.445-0.3848
=
0.0602
>0.
\]

But the target probability also decreased:

\[
\Delta p=-0.05.
\]

The purity loss is

\[
\Delta\pi=-0.1602.
\]

Hence

\[
J_Q
=
0.0602-0.1602
=
-0.1,
\]

which correctly gives

\[
\Delta p
=
\frac{-0.1}{2}
=
-0.05.
\]

Therefore

\[
\boxed{
I_D>0
\not\Rightarrow
\Delta p>0
}
\]

under general purity-changing dynamics.

This is the central refinement result.

A scalar “describability distance” can be too compressed.
The relevant property attributes must be retained.

## 9. DSD interpretation of the refinement

The result matches the DSD static-aggregation warning that a reduced scalar need not reconstruct the richer typed state.

For probability control, the minimal tested descriptor is not merely

\[
D_Q^2.
\]

It is at least the typed triple

\[
\boxed{
\mathcal D_Q
=
(D_Q^2,\pi,\nu).
}
\]

For a fixed effect,

\[
\mathcal D_Q=(D_Q^2,\pi).
\]

The interaction must then be scored by the signed combination

\[
J_Q
=
I_D+\Delta\pi+\Delta\nu.
\]

This directly answers the question “does handling the properties differently matter?”

Yes.

If the purity/effect-norm coordinates are discarded, the same sign of distance reduction may correspond to opposite probability changes.

## 10. Observer/access difference versus objective difference

Suppose an internal observer has a more complete branch record than an external observer, and interaction reduces only the access gap.

If \(\rho\), \(E\), and the quantum instrument remain unchanged, then

\[
p_E=\operatorname{Tr}(\rho E)
\]

remains unchanged.

The external observer may update a conditional probability after receiving information, but that is not an objective change in the physical ensemble probability.

Therefore:

\[
\boxed{
\text{access-gap reduction}
\not\Rightarrow
\text{objective Born-probability increase}.
}
\]

By contrast, if the describability-difference property is attached to the physical state/effect pair and enters an actual supplied transition

\[
\rho'
=
\Gamma_{D}(\rho),
\]

then the resulting change in \(\rho\) can objectively alter

\[
p_E'=\operatorname{Tr}(\rho' E).
\]

## 11. Fixed-primitive no-extra-probability gate

If

\[
\rho,\quad E,\quad \mathcal I
\]

are held fixed, standard quantum mechanics already fixes

\[
p=\operatorname{Tr}(\rho E).
\]

A DSD difference computed downstream from those same fixed objects cannot add an independent objective probability increase unless it is fed back into a physical transition or the probability law itself is modified.

Therefore:

\[
\boxed{
\text{DSD descriptor only}
+
\text{fixed quantum primitives}
\Rightarrow
\Delta p=0.
}
\]

An expression such as

\[
p_{\mathrm{new}}
=
p_{\mathrm{Born}}
+
g(D_Q)
\]

would be a new physical probability law, not a consequence of the present DSD/QM reconstruction.

No such additional law is established here.

## 12. What 002B establishes

### Mathematical / structural theorem

For finite-dimensional Hermitian state/effect representations,

\[
\boxed{
2\Delta p
=
I_D+\Delta\pi+\Delta\nu.
}
\]

For fixed \(E\),

\[
\boxed{
2\Delta p
=
I_D+\Delta\pi.
}
\]

For fixed \(E\) and fixed purity,

\[
\boxed{
2\Delta p=I_D.
}
\]

### Finite exact witnesses

- pure-state target approach raises probability;
- amplitude damping raises probability despite some purity loss;
- depolarization provides a counterexample to raw-distance monotonicity;
- access-only change leaves objective probability unchanged.

### DSD reconstruction result

A difference scalar alone is insufficient in general.

Typed property retention matters:

\[
\boxed{
\text{difference}
+
\text{purity}
+
\text{effect norm}
}
\]

is the exact tested combination.

### Not established

- a probability contribution additional to the Born rule;
- a universal DSD distance independent of the quantum representation;
- a universal probability-raising law for arbitrary interaction;
- a derivation of Hilbert-Schmidt geometry from Formation/Property alone.

These become pressure points for QM Core 003.

## 13. Verdict

### Raw describability-difference reduction as universal probability control

\[
\boxed{\textbf{REJECTED}}
\]

because of the depolarizing counterexample.

### Typed describability-difference + relevant property attributes

\[
\boxed{\textbf{PASS}}
\]

for the exact identity in the declared finite-dimensional quantum specialization.

### DSD-guided objective probability increase through physical interaction

\[
\boxed{\textbf{PASS\_WITH\_REFINEMENT}}
\]

The increase is objective when the interaction actually changes the quantum state/effect/instrument and the corrected score is positive.

### Independent extra-Born DSD probability term

\[
\boxed{\textbf{NOT\_DERIVED}}
\]

No additional probability law is claimed.

## 14. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_002b_describability_probability_control.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_002b_describability_probability_control.py --mode all
```

Expected overall status:

```text
OVERALL: PASS_WITH_REFINEMENT
```

## 15. Consequence for QM Core 003

QM Core 003 should not begin from a single scalar “describability probability.”

It should pressure-test whether the richer structure

```text
typed state
typed effect
difference geometry
purity / norm properties
mixture compatibility
branch structure
admissible dynamics
```

can constrain the Born pairing itself.

The 002B result suggests a precise direction:

\[
\boxed{
\text{probability may be reconstructed as a relation among typed difference and norm properties,}
}
\]

but the present exact identity still uses the standard Hilbert/operator representation and Born pairing as the locked quantum specialization.

That remaining circularity is the next target rather than something to hide.
