# Quantum Normalization / Branch Instrument Interface

Date: 2026-09-08  
Status: active methodological interface  
Origin: QM Core Reconstruction 005B

## Purpose

Separate the normalization structure of quantum dynamics from complete positivity so that `CPTP` is not imported as an indivisible label.

The interface is reusable whenever a DSD specialization contains an ordered normalized state carrier, positive branch maps, and a declared deterministic branch aggregate.

## 1. Ordered normalized carrier

Use

\[
(V,V_+,u,\Omega),
\qquad
\Omega=\{x\in V_+:u(x)=1\},
\]

where:

```text
V      real linear state carrier
V_+    positive cone
u      normalization functional
Omega  normalized state set
```

The Hilbert quantum specialization later sets

\[
u(X)=\operatorname{Tr}X.
\]

Do not identify the abstract normalization functional with trace before that specialization is supplied.

## 2. Deterministic normalization rule

A positive linear map

\[
D:V\to V
\]

is deterministic-normalization preserving when

\[
D(\Omega)\subseteq\Omega.
\]

Then for every \(x\in V_+\),

\[
\boxed{u(Dx)=u(x).}
\]

If \(V_+\) spans \(V\), the equality extends linearly to all of \(V\).

This result is general operational mathematics and is not quantum-specific.

## 3. Selective branch rule

Let

\[
B_1,\ldots,B_m:V\to V
\]

be positive linear maps and suppose

\[
D=\sum_i B_i
\]

is deterministic-normalization preserving.

Then for all \(x\in V_+\),

\[
\boxed{0\le u(B_i x)\le u(x)}
\]

and

\[
\boxed{\sum_i u(B_i x)=u(x).}
\]

For normalized \(\omega\), define

\[
p_i(\omega)=u(B_i\omega).
\]

Then \(p_i\ge0\) and \(\sum_i p_i=1\).

## 4. Zero branch discipline

If a branch output is a positive record \(b_i\in V_+\) with

\[
u(b_i)=0,
\]

whether this forces \(b_i=0\) depends on the ordered carrier.

In the finite-dimensional Hilbert positive-semidefinite specialization,

\[
\operatorname{Tr}b_i=0
\Longrightarrow
b_i=0.
\]

Retain the DSD status distinction:

```text
subnormalized branch output = zero      DEFINED_ZERO
branch probability = zero               DEFINED_ZERO
conditional normalized branch state     UNDEFINED
```

Never replace an undefined normalized conditional state by a zero state merely to keep a fixed-size representation.

## 5. Quantum specialization

After supplying the finite-dimensional complex Hilbert carrier:

```text
positive cone       PSD operators
normalization u     trace
branch maps         CP maps
```

005A supplies the ancilla-compatible complete-positivity gate.
The present interface supplies the normalization gate.

Therefore:

```text
deterministic map / branch sum  -> CPTP
selective branch                 -> CPTNI
```

provided the corresponding CP requirement is also satisfied.

For Kraus data,

\[
\mathcal I(X)=\sum_\alpha K_\alpha X K_\alpha^\dagger,
\]

trace nonincrease is equivalent to

\[
\sum_\alpha K_\alpha^\dagger K_\alpha\le I,
\]

and trace preservation is equivalent to equality.

For an instrument,

\[
\sum_{i,\alpha}K_{i\alpha}^\dagger K_{i\alpha}=I.
\]

## 6. DSD firewall

Do not infer any of the following merely from finite DSD aggregation:

```text
finite sum = probability normalization
static weight normalization = quantum trace preservation
branch support = formation-channel support
zero branch probability = undefined branch output
```

Every physical identification must pass an explicit typed bridge.

## 7. Provenance

```text
DSD zero/undefined status separation            A
DSD dynamic slice admissibility                 A
ordered normalization carrier from 004D         B
normalization preservation theorem              B
positive branch-sum theorem                     B
Hilbert trace specialization                    C / supplied
complete positivity                             C + conditional standard theorem
quantum instrument semantics                    C
CPTP/CPTNI structure                            conditional combination
```

This provenance must be retained in later QM Core 005 synthesis work.
