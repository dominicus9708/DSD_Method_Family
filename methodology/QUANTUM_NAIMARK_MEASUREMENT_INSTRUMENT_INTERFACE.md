# Quantum Naimark Measurement / Instrument Interface

Status: **ACTIVE — QM Core 005G PASS_WITH_REFINEMENT**

## Purpose

This interface prevents four different statements from being collapsed:

```text
POVM statistics
projective measurement on a dilation
quantum instrument / post-measurement dynamics
physical laboratory implementation
```

The interface is downstream of the finite-dimensional Hilbert specialization.  
It is not a generic DSD axiom.

## 1. POVM interface

For a finite outcome set \(\Omega\),

\[
E_i\ge0,
\qquad
\sum_{i\in\Omega}E_i=I.
\]

The outcome readout is

\[
p_i(\rho)=\operatorname{Tr}(\rho E_i).
\]

This records probabilities only.

## 2. NMD-QM selector

```text
NMD-QM  Naimark Measurement Dilation

input:
    finite-dimensional complex Hilbert space H
    POVM {E_i}

supply:
    enlarged Hilbert space K
    isometry V : H -> K
    orthogonal projectors {P_i}

constraints:
    V†V = I
    P_i = P_i† = P_i^2
    P_i P_j = 0 for i != j
    sum_i P_i = I_K
    E_i = V† P_i V
```

Standard consequence:

\[
\operatorname{Tr}(\rho E_i)
=
\operatorname{Tr}(V\rho V^\dagger P_i).
\]

Interpretation:

```text
same outcome statistics on H
=
projective outcome statistics on a larger representation
```

Do not infer a unique ancilla or apparatus.

## 3. Instrument interface

An instrument is a family

\[
\{\mathcal I_i\}_{i\in\Omega}
\]

of CP trace-nonincreasing branch maps such that

\[
\sum_i\mathcal I_i
\]

is CPTP.

Associated POVM:

\[
E_i=\mathcal I_i^*(I).
\]

Branch probability:

\[
p_i=\operatorname{Tr}\mathcal I_i(\rho).
\]

Conditional state, only when \(p_i>0\):

\[
\rho_i=\frac{\mathcal I_i(\rho)}{p_i}.
\]

Zero branch:

```text
I_i(rho) = 0       DEFINED_ZERO
p_i = 0            DEFINED_ZERO
rho_i              UNDEFINED
```

## 4. Non-identifiability rule

Never use:

```text
same POVM
therefore same instrument
```

or

```text
one Naimark dilation exists
therefore this is the actual unique physical apparatus
```

Allowed statement:

```text
the supplied POVM admits at least one standard projective dilation representation
```

A fixed POVM can admit different branch operators \(M_{i\alpha}\) and hence different post-measurement state updates while preserving

\[
\sum_\alpha M_{i\alpha}^\dagger M_{i\alpha}=E_i.
\]

## 5. DSD role separation

```text
Formation:
    protocol/system/outcome identity

Property:
    state/effect/probability records

Static Aggregation:
    outcome probability vector

Dynamics:
    instrument branch map
    nonselective state update

Quantum specialization:
    Hilbert/POVM/CP/projective-dilation structure
```

Core rule:

\[
\boxed{
\text{readout equivalence}
\not\Rightarrow
\text{transition equivalence}
}
\]

## 6. Finite witness used by 005G

\[
E_0=\operatorname{diag}(0.8,0.2),
\qquad
E_1=\operatorname{diag}(0.2,0.8).
\]

Baseline:

\[
M_i=\sqrt{E_i}.
\]

Alternative:

\[
N_0=M_0,
\qquad
N_1=XM_1.
\]

Then

\[
N_i^\dagger N_i=M_i^\dagger M_i=E_i,
\]

so the outcome statistics agree for every state, while conditional states and the nonselective channel can differ.

## 7. Provenance

```text
typed status / branch distinction             PRE_EXISTING_DSD
readout-vs-transition separation              PRE_EXISTING_DSD
Hilbert / POVM                                TARGET SPECIALIZATION
Naimark theorem                               STANDARD QM/MATH
instrument CP-map structure                   STANDARD QM
apparatus non-uniqueness conclusion           REPRESENTATION BOUNDARY
```

## 8. Next interface

Proceed to:

**QM Core 006 — Infinite-Dimensional Hilbert / Unbounded-Operator / Domain Gate**

before the canonical observables / CCR gate.
