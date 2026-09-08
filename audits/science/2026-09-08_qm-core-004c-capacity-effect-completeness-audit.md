# QM Core Reconstruction 004C — Capacity / Effect Completeness Gate

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: **whether operational capacity and the no-restriction/effect-completeness assumption can be obtained from the integrated DSD four-layer architecture without presupposing Hilbert dimension or a full quantum effect cone**

## 1. Research question

QM Core 004B isolated two comparator assumptions still needed before the DSD quantum-reconstruction package can be compared cleanly with standard finite-dimensional GPT reconstruction theorems:

```text
CAPACITY
NO-RESTRICTION / EFFECT COMPLETENESS
```

The present gate asks:

1. Can capacity be defined in DSD purely through joint perfect distinguishability, without importing Hilbert-space dimension?
2. Is capacity invariant under an explicit typed equivalence preserving states, measurements, and readouts?
3. Does DSD itself force every mathematically admissible effect to be physically available?
4. Is tomographic/readout completeness equivalent to no-restriction?
5. What does the answer do to QM Core 003's conditional Born reconstruction?

The answers are:

```text
capacity: definable operationally without Hilbert dimension        YES
capacity: already primitive in generic DSD                         NO
no-restriction: forced by current DSD Property/readout structure   NO
tomographic completeness -> no-restriction                         NO
QM Core 003 Born reconstruction without effect-domain assumptions  NO
```

## 2. Source-locked DSD facts

The current Formation Axiom System supplies staged formation, sound restriction, partial assignments, operational channels, finite composition relative to supplied post-Stage-VI term data, and strict comparison maps. It does not declare a universal measurement family or a maximal number of jointly distinguishable physical states.

The current Property Axiom System is decisive for the effect-completeness question. Property kinds are explicitly declared as a model-specific subfamily. Applicability and prerequisite satisfaction are primitive presentation data, and property assignments are partial. The converse implications are not imposed: an input may be applicable and prerequisite-satisfied while the value remains undefined. Optional representations are downstream.

Therefore the general Property core permits physically restricted effect/readout families. It does not saturate the mathematical dual carrier.

The static aggregation layer also requires an explicit property bridge and keeps the output type open; it does not construct all positive normalized functionals. Structural Reorganization Dynamics preserves predecessor typing/status and requires supplied dynamic laws rather than completing a static property carrier automatically.

Hence the present issue is not a paper-scope artifact. It is a genuine structural fact of the integrated DSD theory:

\[
\boxed{
\text{declared/readable property family}
\not=
\text{all mathematically admissible effects by default}.
}
\]

## 3. DSD-native operational capacity

Fix a declared state carrier \(S\) and a declared measurement family \(\mathfrak M\).

A measurement

\[
M=\{e_1,\ldots,e_n\}\in\mathfrak M
\]

perfectly distinguishes states \(s_1,\ldots,s_n\in S\) when

\[
\boxed{
e_i(s_j)=\delta_{ij}
}
\]

for all \(i,j\).

Define the **DSD operational distinguishability capacity**

\[
\boxed{
\operatorname{Cap}_{\mathfrak M}(S)
=
\sup\left\{
n:
\exists s_1,\ldots,s_n,\;
\exists M\in\mathfrak M,\;
e_i(s_j)=\delta_{ij}
\right\}.
}
\]

For finite state/measurement families the supremum is a maximum.

This definition does not mention Hilbert dimension.

In standard complex quantum theory it later specializes to Hilbert dimension, but that equality is a theorem/representation fact of the quantum specialization, not the definition of DSD capacity.

### Status

Capacity is therefore:

```text
derived once a state carrier + measurement family are declared
not a primitive Formation coordinate
not automatically a realized-axis rank
not automatically a vector-space dimension
not automatically a Hilbert-space dimension
```

## 4. Joint distinguishability is essential

A finite witness uses three states

\[
S=\{A,B,C\}
\]

and three declared binary measurements:

```text
M_AB distinguishes A and B
M_AC distinguishes A and C
M_BC distinguishes B and C
```

Each third state gives probability \(1/2,1/2\) under the irrelevant binary measurement.

Thus every pair of states is perfectly distinguishable by some measurement, but no declared three-outcome measurement exists that perfectly distinguishes all three simultaneously.

The exact finite audit returns:

```text
every pair perfectly distinguishable : true
all three jointly distinguishable    : false
capacity                              : 2
```

Therefore

\[
\boxed{
\text{pairwise perfect distinguishability}
\not\Rightarrow
\text{joint perfect distinguishability}.
}
\]

Consequently a DSD capacity definition must quantify over one common measurement context for the whole state family.

## 5. Capacity is preserved by typed readout equivalence

Suppose a typed equivalence bridge maps

```text
states       bijectively,
measurements bijectively,
outcomes     bijectively,
probabilities exactly.
```

Then every \(n\)-state perfect-distinguishability witness maps to an \(n\)-state witness in the target model, and the inverse bridge gives the converse.

Hence

\[
\boxed{
\operatorname{Cap}(S)=\operatorname{Cap}(S')
}
\]

under such a readout-preserving equivalence.

The finite witness relabels the three-state model and verifies capacity \(2\) on both sides.

This makes capacity a legitimate invariant of the quantum-specialization equivalence once the measurement/readout coordinates are included.

## 6. Composition gives a lower bound, not automatic multiplicativity

If CRD supplies independent product preparations and a product measurement, then local perfect-distinguishability witnesses combine.

For two declared bits,

\[
\operatorname{Cap}(A)=2,
\qquad
\operatorname{Cap}(B)=2,
\]

and the product measurement distinguishes four product states, so

\[
\operatorname{Cap}(AB)\ge
\operatorname{Cap}(A)\operatorname{Cap}(B)=4.
\]

The finite witness realizes equality \(4\) in this toy case.

The generic structural result is only the lower bound:

\[
\boxed{
\operatorname{Cap}(AB)
\ge
\operatorname{Cap}(A)\operatorname{Cap}(B)
}
\]

when the declared composite rule actually contains those independent product states and product measurements.

Equality is not derived by Formation Clause VII, CRD, or LDC-QM alone.

## 7. No-restriction / effect completeness

For a convex operational state carrier \(\Omega\) in a real ordered vector space, define the mathematically admissible effect set

\[
E_{\max}(\Omega)
=
\{
e:
0\le e(\omega)\le1
\text{ for every }\omega\in\Omega
\}.
\]

Let

\[
E_{\mathrm{phys}}
\subseteq
E_{\max}(\Omega)
\]

be the actually declared/physically implementable effect carrier.

The standard **no-restriction hypothesis** is

\[
\boxed{
E_{\mathrm{phys}}
=
E_{\max}(\Omega).
}
\]

The present DSD core does not imply this equality.

Indeed, Property declaration is explicitly selective and the partial assignment is not completed by a converse axiom. Thus DSD naturally supports

\[
\boxed{
E_{\mathrm{phys}}
\subsetneq
E_{\max}(\Omega).
}
\]

### Finite witness

On a two-point classical state carrier, every pair

\[
(e(0),e(1))\in[0,1]^2
\]

is a mathematically valid effect.

On the exact grid

\[
\{0,\tfrac12,1\}^2
\]

there are nine candidate effects.

Declare physically only

\[
(0,0),\;(1,1),\;(1,0),\;(0,1).
\]

This restricted family still contains a perfect binary measurement, so capacity remains two, while the effect family is a strict subset of the mathematically admissible grid.

Therefore

\[
\boxed{
\text{capacity}
\not\Rightarrow
\text{effect completeness}.
}
\]

## 8. Tomographic completeness is weaker than no-restriction

This distinction is crucial for 004A and 003.

Write a qubit effect as

\[
E=aI+b_xX+b_yY+b_zZ.
\]

Consider only

```text
I,
(I+X)/2, (I-X)/2,
(I+Y)/2, (I-Y)/2,
(I+Z)/2, (I-Z)/2.
```

These seven effects span the full four-dimensional real vector space of Hermitian \(2\times2\) operators.

Hence their readout statistics can be tomographically complete for the state carrier.

But this finite family is not the full quantum effect cone.

For example

\[
E_*=
\frac12 I+\frac15 X+\frac15 Y
\]

has eigenvalues

\[
\frac12\pm\frac{\sqrt2}{5},
\]

both in \([0,1]\), so it is a mathematically valid quantum effect, but it is not one of the seven declared effects.

Thus

\[
\boxed{
\text{tomographic/readout completeness}
\not\Rightarrow
\text{no-restriction}.
}
\]

Equivalently,

\[
\operatorname{span}(E_{\mathrm{phys}})
=
A^*
\]

may hold while

\[
E_{\mathrm{phys}}
\subsetneq
E_{\max}(\Omega).
\]

This separates two ideas that must not be merged in DSD:

```text
READOUT COMPLETENESS:
enough effects to reconstruct the state.

EFFECT-DOMAIN COMPLETENESS:
every mathematically admissible effect is physically allowed.
```

## 9. Refinement of QM Core 003

QM Core 003 established internally that cross-context gluing plus measurement normalization yields finite additivity on the effect domain actually under consideration.

That result remains valid.

However, the step that invokes a generalized Gleason/Busch theorem to conclude

\[
\omega(E)=\operatorname{Tr}(\rho E)
\]

for the full quantum effect carrier requires the theorem's effect-domain assumptions.

If DSD supplies only a restricted effect family, then gluing and normalization yield only a valuation on that restricted family. A unique extension to the full effect cone is not automatic.

Therefore the corrected status is:

\[
\boxed{
\text{003 additive valuation result: PASS}
}
\]

but

\[
\boxed{
\text{003 full Born-trace representation:
CONDITIONAL ON SUFFICIENT EFFECT-DOMAIN ASSUMPTIONS}.
}
\]

This is a refinement, not a retraction.

## 10. Proposed DSD interfaces

### 10.1 Operational Capacity Declaration — OCD

Whenever a DSD physical specialization uses a capacity \(N\), it must declare:

```text
STATE_CARRIER
MEASUREMENT_FAMILY
OUTCOME_EFFECT_CARRIERS
JOINT_PERFECT_DISTINGUISHABILITY_RULE
CAPACITY_FUNCTION
```

Capacity is computed from one jointly distinguishing measurement, not from pairwise distinguishability alone.

### 10.2 Effect-Domain Declaration — EDD

Whenever a specialization makes probabilistic readout claims, it must declare:

```text
MATHEMATICAL_EFFECT_CARRIER   when such a carrier is used
PHYSICAL_EFFECT_SUBCARRIER
NORMALIZATION / MEASUREMENT CLOSURE
WHETHER NO-RESTRICTION IS ASSUMED
WHETHER THE DECLARED EFFECTS SEPARATE STATES
```

### 10.3 Quantum no-restriction selector — NR-QM

For the quantum reconstruction candidate, define

\[
\boxed{
E_{\mathrm{phys}}(Q_N)
=
E_{\max}(Q_N)
}
\]

as **NR-QM** when the standard no-restriction hypothesis is deliberately adopted.

NR-QM is not a universal DSD axiom.

## 11. Comparison with the standard reconstruction theorem

Mueller's GPT lecture notes define capacity operationally as the maximal number of jointly perfectly distinguishable states.

The same notes explicitly state that the reconstruction section assumes:

```text
finite-dimensional state spaces,
the no-restriction hypothesis,
Tomographic Locality,
the Subspace Axiom,
Continuous Reversibility.
```

Under that framework, Theorem 21 identifies the dynamical state spaces with the standard finite-dimensional complex quantum state spaces and unitary-conjugation reversible transformations.

The present 004C step closes two important terminology/interface gaps:

```text
standard capacity
<-> DSD operational distinguishability capacity

standard no-restriction
<-> explicit NR-QM effect-domain saturation
```

But theorem transfer is still premature.

Remaining interface gaps include at least:

```text
convex ordered linear state/effect carrier as an explicit DSD quantum specialization,
exact mixture-linearity assumptions,
precise composite-product embedding assumptions,
proof that LDC-QM matches the required Tomographic Locality definition,
proof that RRDE-QM matches the required Subspace Axiom on both states and transformations.
```

Therefore the external theorem remains a comparator/conditional target, not a DSD theorem.

Primary comparators:

- Markus P. Mueller, *Probabilistic Theories and Reconstructions of Quantum Theory*, arXiv:2011.01286.
- Lluis Masanes and Markus P. Mueller, *A derivation of quantum theory from physical requirements*, arXiv:1004.1483.

## 12. Updated reconstruction package

The present DSD quantum-reconstruction candidate now has:

\[
\boxed{
\text{CRR-QM}
+
\text{CRD}
+
\text{LDC-QM}
+
\text{RRDE-QM}
+
\text{OCD}
+
\text{NR-QM}
}
\]

with distinct logical roles.

```text
CRR-QM  continuous reversible reachability
CRD     explicit composite declaration
LDC-QM  local descriptive completeness
RRDE-QM recursive restriction equivalence
OCD     operational capacity definition/declaration
NR-QM   no-restriction / effect-domain saturation
```

None of these labels is a claim that complex Hilbert quantum theory has already been derived from DSD.

## 13. Next target — QM Core 004D

The next gate should address the largest remaining theorem-interface gap:

```text
CONVEX MIXTURE / ORDERED LINEAR CARRIER
```

Questions:

1. Can DSD's Formation/Property/Static structure derive or naturally specialize to convex closure under operational mixing?
2. Is affine linearity of readout under mixtures forced by the meaning of randomized preparation, or must it be separately postulated?
3. Can state and effect cones be reconstructed from DSD typed mixture operations without assuming Hilbert space?
4. Once convexity, linearity, OCD, NR-QM, LDC-QM, RRDE-QM, and CRR-QM are locked, does the DSD specialization satisfy the exact GPT hypotheses used by the external reconstruction theorem?

This is the most direct next step before any claim that the Hilbert formalism has been conditionally reconstructed.

## 14. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_004c_capacity_effect_completeness_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_004c_capacity_effect_completeness_gate.py --mode all
```

Expected final line:

```text
OVERALL: PASS_WITH_REFINEMENT
```

Finite witnesses implemented:

```text
pairwise-vs-joint distinguishability
capacity invariance under typed relabeling
declared product-capacity witness
capacity without effect completeness
tomographic spanning without no-restriction
```

## 15. Verdict

\[
\boxed{\textbf{PASS\_WITH\_REFINEMENT}}
\]

Refinements established:

1. Capacity can be defined operationally in DSD without Hilbert dimension.
2. Pairwise distinguishability is insufficient; capacity is a joint-measurement property.
3. Capacity is invariant under typed state/measurement/readout equivalence.
4. Product measurements give a capacity lower bound when explicitly supplied, not generic multiplicativity.
5. The current DSD Property/readout architecture does not imply the no-restriction hypothesis.
6. Capacity and tomographic completeness are both strictly weaker than effect-domain completeness.
7. QM Core 003's full Born-trace representation must remain conditional on a sufficiently complete effect domain.
8. OCD and EDD are promotable DSD-wide declaration rules; NR-QM remains a quantum-specialization selector.
9. The next critical gate is convex mixture and ordered-linear structure.
