# Recursive Restriction and Complete-Measurement Transitivity Interface

Status: reusable DSD Method Family comparator interface  
Origin: QM Core Reconstruction 004I  
Scope: finite-dimensional operational specializations that use recursive restriction to lower-capacity system types

## 1. Purpose

This interface prevents three distinct claims from being silently collapsed:

```text
restriction to a retained face,
one designated lower-type recursion,
universal recursion over every complete measurement.
```

It also separates selected retained dynamics from the full reversible transformation structure of the retained face.

## 2. Reference recursive restriction declaration

When a specialization claims that excluding an outcome from one declared complete measurement produces a lower-capacity system, record:

```text
SYSTEM_TYPE_N
CAPACITY_N
REFERENCE_COMPLETE_MEASUREMENT
EXCLUDED_OUTCOME
ZERO_FACE
LOWER_SYSTEM_TYPE
STATE_EQUIVALENCE_MAP
LINEARITY_STATUS
NORMALIZED_STATE_SURJECTIVITY
EFFECT_TRANSPORT_STATUS
FULL_FACE_REVERSIBLE_GROUP
LOWER_REVERSIBLE_GROUP
GROUP_CONJUGACY_STATUS
```

A subset inclusion or valid restriction alone is not a lower-type equivalence theorem.

## 3. LFRR — Linear Full Reference Recursion

For a reference complete measurement

\[
M_N^0=\{e_1^0,\ldots,e_N^0\},
\]

define

\[
F_i^0=\{\omega\in\Omega_N:e_i^0(\omega)=0\}.
\]

`LFRR` holds when, for every reference outcome `i`, there is an invertible linear map

\[
L_i^0:\operatorname{span}(F_i^0)\to V_{N-1}
\]

that maps the normalized face onto the declared lower-capacity normalized state space and conjugates the full induced face-preserving reversible transformation group to the lower-system reversible group.

Intertwining only a chosen retained subgroup is weaker than LFRR.

## 4. CMT — Complete-Measurement Transitivity

Fix the same reference measurement `M_N^0`.

`CMT` holds when for every declared complete measurement

\[
M=\{e_1,\ldots,e_N\}
\]

there exists a reversible transformation `T` and a permutation `pi` such that

\[
e_i=e_{\pi(i)}^0\circ T^{-1}
\]

for every outcome.

Pure-state transitivity is not a substitute for CMT.

## 5. Universal transfer theorem

If LFRR and CMT hold, then every zero face of every complete measurement is linearly and dynamically equivalent to the lower-capacity system.

Indeed,

\[
F_i=T(F_{\pi(i)}^0),
\]

and

\[
L_i=L_{\pi(i)}^0\circ T^{-1}
\]

transfers the state-space equivalence.

For the full face-preserving reversible groups,

\[
G_{F_i}=T G_{F_{\pi(i)}^0}T^{-1},
\]

so the reference group conjugacy transfers as well.

Therefore:

\[
\boxed{
\mathrm{LFRR}+\mathrm{CMT}
\Longrightarrow
\mathrm{universal\ recursive\ restriction\ equivalence}.
}
\]

## 6. Firewalls

```text
retained subset != lower physical system type
formation/property submodel != operational state-space equivalence
one recursive measurement != universal recursive measurement family
pure-state transitivity != complete-measurement transitivity
selected retained dynamics != full face-stabilizer dynamics
state-space bijection != linear dynamical equivalence
```

## 7. Countermodel requirement

When universal recursion is claimed without CMT or an equivalent theorem, audit whether two complete measurements can have zero faces of different structure or capacity.

QM Core 004I supplies a reusable finite-dimensional countermodel:

```text
state space        D^2 x D^2
capacity           2
reversible group   SO(2) x SO(2)
effect domain      maximal affine effects

one zero face      singleton
another zero face  D^2
```

The group is connected and pure-state transitive, yet the two complete frames lie in distinct reversible-group orbits.

## 8. Provenance rule

For the present quantum reconstruction program:

```text
RRDE-QM       C  target-specialization selector
LFRR-QM       D  exact comparator refinement
CMT-QM        D  exact comparator lock
ULRRDE-QM        conditional theorem-interface consequence of LFRR-QM + CMT-QM
```

Do not count a conclusion inherited from Class-C/D inputs as independent evidence that generic DSD derives quantum theory.

## 9. DSD relation

Generic DSD supplies useful separation machinery:

```text
restriction vs realization
embedding vs strict equivalence
submodel vs isomorphism
selected dynamics vs transition/lineage
```

It does not impose LFRR or CMT universally.

This interface is therefore a method-family comparator/audit tool, not a new DSD axiom.
