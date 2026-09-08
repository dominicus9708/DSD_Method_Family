# Quantum Trace-Normalization / Instrument Interface

Date: 2026-09-08

## Purpose

This interface separates complete positivity from normalization preservation in DSD quantum specializations.

## Ordered-carrier normalization

Let \((V,V_+,u,\Omega)\) be a finite-dimensional ordered normalized carrier with

\[
\Omega=\{x\in V_+:u(x)=1\}.
\]

If a positive linear deterministic map \(D\) satisfies \(D(\Omega)\subseteq\Omega\), then

\[
\boxed{u(Dx)=u(x)}
\]

for every \(x\in V_+\).

If positive branch maps \(B_i\) satisfy \(D=\sum_i B_i\) and \(D\) is deterministic, then

\[
\boxed{0\le u(B_i x)\le u(x)},
\qquad
\boxed{\sum_i u(B_i x)=u(x)}.
\]

Thus deterministic evolution is normalization-preserving while selective branches are normalization-nonincreasing.

## Quantum specialization

For the finite-dimensional Hilbert-state carrier,

\[
u(X)=\operatorname{Tr}X.
\]

Hence:

```text
deterministic positive linear map  -> trace preserving
positive selective branch          -> trace non-increasing
branch family with deterministic sum -> branch probabilities sum to one
```

Combining this normalization interface with the separate complete-positivity / ancilla interface gives:

```text
deterministic quantum channel -> CPTP
selective quantum branch      -> CPTNI
```

## Zero / undefined status

For a positive branch output \(\tau_i\),

\[
p_i=u(\tau_i).
\]

If \(p_i=0\), positivity implies \(\tau_i=0\), but the normalized conditional state \(\tau_i/p_i\) is undefined.

Record:

```text
branch output tau_i = 0       DEFINED_ZERO
branch probability p_i = 0    DEFINED_ZERO
conditional normalized state  UNDEFINED
```

Do not pad the undefined conditional state by a zero matrix.

## Provenance

```text
DSD zero/undefined status discipline      A
DSD dynamic slice admissibility           A
ordered normalization carrier             B
normalization preservation theorem        B
branch nonincrease theorem                 B
Hilbert trace representation               C / SUPPLIED
complete positivity                        C + standard result
instrument semantics                       C
CPTP/CPTNI conclusion                      CONDITIONAL COMBINATION
```

The normalization theorem may be reused outside quantum mechanics; complete positivity and Hilbert trace remain specialization-specific.
