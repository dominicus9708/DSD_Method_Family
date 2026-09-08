# Operational Capacity and Effect-Domain Declaration

Status: reusable DSD Method Family interface  
Origin: QM Core Reconstruction 004C  
Scope: physical/probabilistic specializations using distinguishability, measurements, effects, or capacity

## 1. Purpose

This interface prevents three distinct notions from being silently identified:

```text
operational capacity,
readout/tomographic completeness,
effect-domain completeness (no-restriction).
```

They are logically independent unless an application supplies additional assumptions.

## 2. Operational Capacity Declaration — OCD

Whenever a DSD specialization uses a capacity value, declare:

```text
STATE_CARRIER
MEASUREMENT_FAMILY
OUTCOME_EFFECT_CARRIERS
JOINT_PERFECT_DISTINGUISHABILITY_RULE
CAPACITY_FUNCTION
```

A family `s_1,...,s_n` is jointly perfectly distinguishable only if one declared measurement `M={e_1,...,e_n}` satisfies

\[
e_i(s_j)=\delta_{ij}.
\]

Define

\[
\operatorname{Cap}_{\mathfrak M}(S)
=
\sup\{n:\exists s_1,\ldots,s_n,\exists M\in\mathfrak M,\ e_i(s_j)=\delta_{ij}\}.
\]

Pairwise distinguishability under different measurements does not determine capacity.

Capacity is not automatically identified with:

```text
formation-channel count,
property count,
realized-axis rank,
linear-space dimension,
Hilbert-space dimension.
```

Any such identification requires an explicit specialization theorem or bridge.

## 3. Capacity under equivalence

A claimed capacity-preserving equivalence must preserve/reflect the state carrier, measurement family, outcome-effect assignment, and readout probabilities.

Under a bijective readout-preserving equivalence, capacity is invariant.

## 4. Composition rule

If a declared composite system contains independent product preparations and product measurements, then local distinguishability witnesses give

\[
\operatorname{Cap}(AB)
\ge
\operatorname{Cap}(A)\operatorname{Cap}(B).
\]

Equality is not inferred without an additional result.

## 5. Effect-Domain Declaration — EDD

Whenever probabilistic effects/readouts are used, declare:

```text
MATHEMATICAL_EFFECT_CARRIER   if one is defined
PHYSICAL_EFFECT_SUBCARRIER
MEASUREMENT_NORMALIZATION_RULE
EFFECT-COMPOSITION / COARSE-GRAINING RULES
STATE-SEPARATION / TOMOGRAPHY STATUS
NO-RESTRICTION STATUS
```

If a maximal mathematical effect carrier is defined by

\[
E_{\max}(S)=\{e:0\le e(s)\le1\text{ for all }s\in S\},
\]

then the physically declared carrier may satisfy

\[
E_{\mathrm{phys}}\subseteq E_{\max}(S).
\]

The equality

\[
E_{\mathrm{phys}}=E_{\max}(S)
\]

must be explicitly assumed or derived; it is not inherited from generic DSD Property declarations.

## 6. Readout completeness is not effect completeness

A declared effect family may separate all states or span the relevant linear dual while still being a strict subset of the maximal effect carrier.

Therefore

\[
\boxed{
\text{tomographic/readout completeness}
\not\Rightarrow
\text{effect-domain completeness}.
}
\]

Conversely, no-restriction alone does not establish that a particular finite selected measurement set is tomographically complete.

## 7. Quantum specialization

For the DSD quantum-reconstruction program, the standard no-restriction hypothesis is recorded separately as

```text
NR-QM:
E_phys(Q_N) = E_max(Q_N)
```

when deliberately adopted.

NR-QM is not a universal DSD axiom.

## 8. Audit rule

Before using a theorem whose hypotheses quantify over all effects, check whether the theorem expects:

```text
all mathematically admissible effects,
a separating effect set,
a tomographically complete subset,
or merely the effects in one declared measurement family.
```

Do not transfer conclusions across these domains without an explicit extension or equivalence result.
