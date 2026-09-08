# QM Core Reconstruction 002 — Quantum Instrument / Measurement Update in Integrated DSD

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: **finite-dimensional quantum measurement — outcome probability / conditional update / unconditioned channel / disturbance / repeatability**

## 1. Research question

This audit uses the stronger integrated-DSD premise:

```text
Formation Axiom System
-> Property Axiom System
-> Channel-Indexed Static Aggregation
-> Structural Reorganization Dynamics
```

Paper-local scope boundaries are not treated as global prohibitions on DSD reconstruction.

The target is not merely to represent a POVM. The question is:

> Can one finite-dimensional quantum instrument be reconstructed as one DSD four-layer measurement structure in which the same branch record yields the outcome probability, the conditional post-measurement state, the unconditioned output channel, disturbance, and repeatability tests without collapsing defined-zero and undefined statuses?

The hard gates are:

```text
type consistency
cross-layer logical consistency
mathematical well-definedness
exact agreement with standard finite-dimensional QM
```

## 2. Standard finite-dimensional quantum lock

Let \(\mathcal H\) be finite-dimensional.

A quantum instrument is a finite family of completely positive trace-nonincreasing maps

\[
\{\mathcal I_i\}_{i\in\Omega}
\]

whose sum

\[
\mathcal E
=
\sum_i \mathcal I_i
\]

is trace preserving.

For input state \(\rho\), define the subnormalized branch operator

\[
\boxed{\tau_i=\mathcal I_i(\rho).}
\]

The outcome probability is

\[
\boxed{p_i=\operatorname{Tr}\tau_i.}
\]

When \(p_i>0\), the normalized conditional state is

\[
\boxed{\rho_i'=\frac{\tau_i}{p_i}.}
\]

The unconditioned post-measurement state is

\[
\boxed{\rho'=\sum_i\tau_i=\mathcal E(\rho).}
\]

The associated POVM effect is

\[
\boxed{E_i=\mathcal I_i^*(I),}
\]

so

\[
p_i=\operatorname{Tr}(\rho E_i).
\]

Standard references used for this lock:

- John Watrous, quantum-information lecture notes and *The Theory of Quantum Information*: quantum channels, measurements, subchannels, and instruments.
- Standard measurement-operator formalism: outcome probability \(\operatorname{Tr}(M_i\rho M_i^\dagger)\) and normalized conditional state.

## 3. Integrated DSD placement

Define the measurement specialization schematically by

\[
\boxed{
\mathfrak M_{\mathrm{DSD}}
=
\left(
F_{\mathrm{meas}}^{\le6},
P_{\mathrm{inst}},
\Theta_{\mathrm{branch}},
S_{\mathrm{branch}},
\Gamma_{\mathrm{inst}}
\right).
}
\]

### 3.1 Formation layer

Formation keeps the stable identity of:

```text
system / preparation protocol
measurement protocol
outcome label
quantity kind
operational role
```

Routine changes of \(p_i\), \(\tau_i\), or \(\rho_i'\) are not placed into the inherited Stage-VI assigned-value coordinate unless a formation-level transition is intentionally declared.

### 3.2 Property layer

Declare typed quantum property kinds such as

```text
QBRANCH:
    (state, instrument, outcome) -> subnormalized positive operator

QPROB:
    branch -> [0,1]

QCOND:
    branch -> normalized density operator   [partial assignment]
```

with

\[
\Xi_{\mathrm{QBRANCH}}(\rho,\mathcal I,i)=\tau_i=\mathcal I_i(\rho),
\]

\[
\Xi_{\mathrm{QPROB}}(\tau_i)=\operatorname{Tr}\tau_i,
\]

and

\[
\Xi_{\mathrm{QCOND}}(\tau_i)=\frac{\tau_i}{\operatorname{Tr}\tau_i}
\]

only on the domain

\[
\operatorname{Tr}\tau_i>0.
\]

This placement uses the Property Axiom System's actual status discipline rather than padding an undefined conditional state by a zero matrix.

## 4. Defined zero versus undefined conditional state

For an outcome branch with

\[
\tau_i=0,
\]

the branch operator is a **defined zero** property value.

Its probability

\[
p_i=\operatorname{Tr}\tau_i=0
\]

is also a **defined zero**.

But the normalized conditional state

\[
\rho_i'=\tau_i/p_i
\]

is not the zero density operator; it is **undefined** because the normalization map has no value at \(p_i=0\).

Therefore the DSD status chain distinguishes:

\[
\boxed{
\tau_i=0\ \text{defined}
\quad\land\quad
p_i=0\ \text{defined}
\quad\land\quad
\rho_i'\ \text{undefined}.
}
\]

This is a nontrivial integrated placement result: one quantum measurement branch naturally exercises the Property distinction between defined-zero and applicable-but-undefined downstream data.

## 5. Branch-resolved static aggregate

Let the selected branch records be

\[
r_i=(\mathrm{QBRANCH},(\rho,\mathcal I,i),\tau_i).
\]

Use the direct-sum output space

\[
U_{\mathrm{branch}}=\bigoplus_{i\in\Omega}\mathcal L(\mathcal H)
\]

and bridge

\[
\Theta_{\mathrm{branch}}(r_i)=e_i\otimes\tau_i.
\]

Then the DSD property-side static aggregate is

\[
\boxed{B_{\mathcal I}(\rho)=\bigoplus_i\tau_i.}
\]

Two standard quantum outputs are downstream postprocessings of the same aggregate.

### Probability readout

\[
\boxed{
\Pi_{\mathrm{prob}}\left(\bigoplus_i\tau_i\right)
=(\operatorname{Tr}\tau_i)_i=(p_i)_i.
}
\]

### Unconditioned state

\[
\boxed{
\Pi_{\mathrm{sum}}\left(\bigoplus_i\tau_i\right)
=\sum_i\tau_i=\rho'.
}
\]

Thus a branch-resolved DSD aggregate contains strictly more measurement-update information than the probability vector alone.

## 6. POVM as a lossy readout of an instrument

The map

\[
\{\mathcal I_i\}_i\longmapsto\{E_i=\mathcal I_i^*(I)\}_i
\]

need not be injective.

Therefore

\[
\boxed{\text{same POVM}\not\Rightarrow\text{same quantum instrument}.}
\]

The finite witness compares two qubit instruments with the same Z-basis POVM.

### Instrument A — Lüders Z instrument

\[
\mathcal I_0^L(\rho)=P_0\rho P_0,
\qquad
\mathcal I_1^L(\rho)=P_1\rho P_1.
\]

### Instrument B — same-POVM reprepare-\(|+\rangle\) instrument

\[
K_0=|+\rangle\langle0|,
\qquad
K_1=|+\rangle\langle1|,
\]

\[
\mathcal I_i^R(\rho)=K_i\rho K_i^\dagger.
\]

Both have

\[
E_0=P_0,
\qquad
E_1=P_1.
\]

For input

\[
\rho_+=|+\rangle\langle+|,
\]

both yield

\[
\boxed{p_0=p_1=\frac12.}
\]

But their unconditioned outputs differ:

\[
\sum_i\mathcal I_i^L(\rho_+)=\frac I2,
\]

while

\[
\sum_i\mathcal I_i^R(\rho_+)=|+\rangle\langle+|.
\]

Hence selected X readout gives

\[
\langle X\rangle_L=0,
\qquad
\langle X\rangle_R=1.
\]

So the same Born probability vector does not determine disturbance or post-measurement dynamics.

## 7. Repeatability is an instrument property, not a POVM property alone

For the Lüders Z instrument, conditioned on outcome \(i\),

\[
\rho_i'=P_i,
\]

and immediately repeating the same projective measurement gives outcome \(i\) with probability \(1\).

For the reprepare-\(|+\rangle\) instrument, conditioned on either outcome,

\[
\rho_i'=|+\rangle\langle+|,
\]

so repeating the Z measurement gives either Z outcome with probability \(1/2\).

Therefore

\[
\boxed{\text{same POVM}\not\Rightarrow\text{same repeatability}.}
\]

Repeatability belongs to the transition/instrument structure, not to the probability readout layer alone.

## 8. DSD reconstruction of measurement update

The measurement process is reconstructed as

\[
\boxed{
\rho\overset{\mathcal I_i}{\longmapsto}\tau_i
\overset{\operatorname{Tr}}{\longmapsto}p_i
}
\]

with the partial normalization

\[
\boxed{
\tau_i\overset{p_i>0}{\longmapsto}\rho_i'=\tau_i/p_i.
}
\]

At the full branch-family level:

\[
\boxed{
\rho
\longmapsto
\bigoplus_i\tau_i
\longmapsto
\begin{cases}
(p_i)_i,\\
\sum_i\tau_i,\\
\rho_i'\ \text{on selected nonzero branch}.
\end{cases}
}
\]

This is stronger than a noun-by-noun relabeling because one branch-resolved DSD object controls three distinct standard-QM outputs:

```text
outcome probability
conditional state
unconditioned state
```

and also exposes exactly where information is lost if only the POVM probability vector is retained.

## 9. Cross-paper interpretation

The four DSD layers now do nonredundant work.

```text
Formation
    stabilizes measurement protocol / outcome identity

Property
    carries branch operator, probability, conditional-state statuses

Static Aggregation
    assembles outcome-resolved branch data and supports probability/sum postprocessing

Dynamics
    supplies the instrument / unconditioned channel and branch-conditioned succession
```

The quantum instrument is therefore a stronger DSD measurement object than the POVM alone.

The reconstruction also sharpens the DSD principle:

\[
\boxed{
\text{readout equality}
\neq
\text{transition equality}
\neq
\text{post-state equality}.
}
\]

## 10. What has and has not been derived

### Established in the present reconstruction

- exact instrument probability formula;
- exact conditional normalization when \(p_i>0\);
- exact unconditioned channel output;
- branch aggregate recovery of both probabilities and unconditioned state;
- same-POVM / different-instrument counterexample;
- repeatability separation;
- DSD defined-zero versus undefined conditional-state placement.

### Still not derived internally from DSD

- complete positivity itself;
- the Born trace pairing as a theorem of Formation/Property alone;
- the Hilbert-space operator structure;
- why physical measurements must be represented by quantum instruments rather than another admissible mathematical family.

These are no longer excluded by manuscript scope. They remain explicit reconstruction targets.

## 11. Verdict

### Mathematical / standard-QM verdict

\[
\boxed{\text{PASS}}
\]

for the finite-dimensional instrument identities and witnesses.

### Integrated DSD reconstruction verdict

\[
\boxed{\textbf{PASS\_WITH\_REFINEMENT}}
\]

The refinement is substantive:

1. the measurement object should be branch-resolved at the Property/Static interface;
2. the probability vector is a reduced readout of that richer object;
3. conditional normalization is a partial property map and must preserve the zero/undefined distinction;
4. repeatability and disturbance belong to transition structure and cannot be inferred from POVM probabilities alone.

## 12. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_002_quantum_instrument_measurement_update.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_002_quantum_instrument_measurement_update.py --mode all
```

Standard library only.

## 13. Next core challenge

The next aggressive target is not another defensive compatibility check.

It is:

```text
QM Core 003
Hilbert geometry / effect-state pairing / Born-rule reconstruction pressure test
```

The question is whether the integrated DSD requirements already identified —

```text
typed state/readout duality
complete readout reconstruction
convex mixture compatibility
positive normalized readouts
composition with admissible dynamics
branch aggregation
zero/undefined status discipline
```

— constrain the admissible pairing strongly enough to recover or sharply narrow the standard Born form, and exactly where an external quantum axiom remains necessary.
