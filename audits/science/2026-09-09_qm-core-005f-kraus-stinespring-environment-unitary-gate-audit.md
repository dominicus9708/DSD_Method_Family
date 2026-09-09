# QM Core Reconstruction 005F — Kraus / Stinespring / Environment-Unitary Realization Gate

Date: 2026-09-09  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: reconstruct the finite-dimensional representation theorem connecting CPTP maps, Kraus operators, Stinespring isometries, and unitary-plus-ancilla realizations, while separating mathematical representation existence from claims about a unique or physically literal environment.

## 1. Question

QM Core 005A–005B established the conditional route to CPTP maps, 005C separated physical channel reversibility from algebraic invertibility, 005D reconstructed Hamiltonian generation for coherent unitary groups, and 005E reconstructed the time-homogeneous GKSL generator gate for continuous CPTP semigroups.

The present question is different:

> Given one finite-dimensional CPTP map, what representation structure follows mathematically, which parts are non-unique, and what may DSD legitimately infer from the existence of those representations?

The critical distinctions are:

```text
DSD_FORMATION_CHANNEL
QUANTUM_CHANNEL_MAP
KRAUS_REPRESENTATION
STINESPRING_ISOMETRY
UNITARY_PLUS_ANCILLA_REALIZATION
PHYSICAL_ENVIRONMENT_CLAIM
```

The first two uses of the word `channel` must not be silently identified.

## 2. Standard finite-dimensional channel characterization

Let

\[
\Phi:\mathcal L(\mathcal H_A)\to\mathcal L(\mathcal H_B)
\]

be linear, with finite-dimensional complex Hilbert spaces.

For a quantum channel, the following standard descriptions are equivalent.

### 2.1 CPTP description

\[
\Phi\text{ is completely positive and trace preserving.}
\]

### 2.2 Kraus description

There exist operators

\[
K_a:\mathcal H_A\to\mathcal H_B
\]

such that

\[
\boxed{\Phi(X)=\sum_a K_a X K_a^\dagger}
\]

and

\[
\boxed{\sum_a K_a^\dagger K_a=I_A.}
\]

### 2.3 Stinespring description

There exists a finite-dimensional auxiliary Hilbert space \(\mathcal H_E\) and an isometry

\[
V:\mathcal H_A\to\mathcal H_B\otimes\mathcal H_E,
\qquad V^\dagger V=I_A,
\]

such that

\[
\boxed{\Phi(X)=\operatorname{Tr}_E(VXV^\dagger).}
\]

For finite-dimensional channels the environment dimension may be chosen equal to the Choi rank, and the minimal Kraus number is the same rank.

Thus, once the finite-dimensional Hilbert carrier and CPTP status are already supplied,

\[
\boxed{\mathrm{CPTP}\Longleftrightarrow\mathrm{Kraus}\Longleftrightarrow\mathrm{Stinespring\ isometry}}
\]

is a standard representation theorem rather than an additional DSD physical axiom.

## 3. Kraus non-uniqueness

A Kraus family is not uniquely identified by the channel.

If \(\{K_a\}_{a=1}^r\) is a Kraus family and \(u\) is a unitary matrix acting on the Kraus label space, define

\[
L_b=\sum_a u_{ba}K_a.
\]

Then

\[
\sum_b L_b X L_b^\dagger=\sum_a K_a X K_a^\dagger.
\]

The finite witness uses the amplitude-damping pair \(K_0,K_1\) and the Hadamard mixing

\[
L_0=\frac{K_0+K_1}{\sqrt2},
\qquad
L_1=\frac{K_0-K_1}{\sqrt2}.
\]

The two operator lists are different but define exactly the same linear channel on a basis of \(\mathcal L(\mathbb C^2)\).

Therefore

\[
\boxed{\text{Kraus-list identity}\neq\text{quantum-channel identity}.}
\]

A specific Kraus operator also must not automatically be interpreted as a physically realized branch or measurement outcome. Such an interpretation requires an instrument or another explicit operational bridge.

## 4. Finite amplitude-damping witness

Choose

\[
0<\gamma<1
\]

and

\[
K_0=
\begin{pmatrix}
1&0\\
0&\sqrt{1-\gamma}
\end{pmatrix},
\qquad
K_1=
\begin{pmatrix}
0&\sqrt\gamma\\
0&0
\end{pmatrix}.
\]

Then

\[
K_0^\dagger K_0+K_1^\dagger K_1=I.
\]

The channel is

\[
\Phi_\gamma(\rho)=K_0\rho K_0^\dagger+K_1\rho K_1^\dagger.
\]

For \(0<\gamma<1\), the two vectorized Kraus operators are linearly independent, so the Choi matrix has rank 2. The two-dimensional environment used below is therefore minimal for this witness.

## 5. Stinespring isometry witness

Define

\[
V|0\rangle=|0\rangle|0_E\rangle,
\]

\[
V|1\rangle=\sqrt{1-\gamma}|1\rangle|0_E\rangle+\sqrt\gamma|0\rangle|1_E\rangle.
\]

Then

\[
V^\dagger V=I
\]

and direct calculation gives

\[
\boxed{\operatorname{Tr}_E(V\rho V^\dagger)=\Phi_\gamma(\rho).}
\]

This establishes one explicit Kraus-to-Stinespring reconstruction.

## 6. Environment-coordinate non-uniqueness

For any environment unitary \(W_E\), let

\[
V'=(I_B\otimes W_E)V.
\]

Then

\[
\operatorname{Tr}_E(V'\rho V'^\dagger)=\operatorname{Tr}_E(V\rho V^\dagger).
\]

The audit uses a Hadamard rotation on the two-dimensional environment and verifies both

```text
V' != V
```

and

```text
reduced channel from V' = reduced channel from V.
```

Hence the reduced map does not reconstruct a unique environment basis or unique dilation coordinates.

For minimal Stinespring representations, the remaining freedom is the standard environment isometric/unitary equivalence. Non-minimal representations have still more redundant coordinates.

## 7. Isometry versus unitary realization

A Stinespring dilation is naturally an isometry

\[
V:\mathcal H_A\to\mathcal H_B\otimes\mathcal H_E,
\]

not automatically a unitary operator on \(\mathcal H_A\) itself.

In the equal system-dimension finite witness one may identify the input with the subspace

\[
\mathcal H_S\otimes |0_E\rangle\subset\mathcal H_S\otimes\mathcal H_E
\]

and extend the isometry to a unitary \(U\) on the full joint space so that

\[
V|\psi\rangle=U(|\psi\rangle\otimes|0_E\rangle).
\]

For amplitude damping, one such unitary satisfies

\[
U|0,0\rangle=|0,0\rangle,
\]

\[
U|1,0\rangle=\sqrt{1-\gamma}|1,0\rangle+\sqrt\gamma|0,1\rangle.
\]

The remaining orthogonal columns complete the unitary.

Then

\[
\boxed{\Phi_\gamma(\rho)=\operatorname{Tr}_E\left[U(\rho\otimes|0_E\rangle\langle0_E|)U^\dagger\right].}
\]

For unequal input/output dimensions, additional padding or ancilla spaces may be required before a single square unitary realization is written. Therefore

\[
\boxed{\text{Stinespring isometry}\not\equiv\text{unitary on the system alone}.}
\]

## 8. Global reversibility versus reduced irreversibility

The joint dilation \(U\) is unitary and therefore reversible.

The reduced amplitude-damping channel need not be physically reversible.

For the states

\[
\rho_0=|0\rangle\langle0|,
\qquad
\rho_1=|1\rangle\langle1|,
\]

one has

\[
\|\rho_0-\rho_1\|_1=2,
\]

while

\[
\|\Phi_\gamma(\rho_0)-\Phi_\gamma(\rho_1)\|_1=2(1-\gamma)<2.
\]

If a CPTP inverse existed, contractivity applied in both directions would force equality, contradicting the strict contraction.

Therefore

\[
\boxed{\text{reversible global dilation}\not\Rightarrow\text{reversible reduced channel}.}
\]

This is fully consistent with QM Core 005C.

## 9. DSD placement

The current DSD source hierarchy already distinguishes the relevant logical layers.

### 9.1 Formation boundary

Formation Stage VI supplies DSD operational-channel identity, and the Formation paper makes representation-sensitive strict descriptive equivalence stronger than coincidence after an output comparison.

A target-theory quantum map \(\Phi\) is therefore not automatically one Formation channel merely because both literatures use the word `channel`.

### 9.2 Property and representation boundary

The Property Axiom System treats optional representation packages as downstream extensions after the typed property core is completed.

Thus density operators, Kraus lists, dilation coordinates, or environment labels may be introduced only through explicit quantum specialization/representation bridges rather than silently promoted into primitive DSD property coordinates.

### 9.3 Static aggregation boundary

The static aggregation paper explicitly treats representation bridges as additional analytic data and warns that distinct realizations may produce the same aggregate.

005F supplies an exact quantum analogue at the dynamic representation level:

```text
same quantum channel map
<- many Kraus families
<- many Stinespring coordinate realizations
```

### 9.4 Dynamics boundary

Structural Reorganization Dynamics fixes the predecessor types and allows constitutive operators and representations to be supplied downstream. It also does not identify reduced readouts with complete component-resolved state.

Accordingly, the Stinespring environment can be typed as an auxiliary representation carrier without asserting that DSD itself has discovered a literal microscopic bath.

## 10. Mathematical environment versus physical environment

The most important refinement is ontological.

The theorem establishes:

\[
\boxed{\text{there exists an auxiliary Hilbert-space dilation representing }\Phi.}
\]

It does not by itself establish:

```text
this particular environment is physically present;
this basis labels actual microscopic degrees of freedom;
this Kraus family is the physically realized branch decomposition;
this unitary is the unique microscopic interaction Hamiltonian;
the environment dimension equals a DSD geometric dimension or realized-axis rank.
```

In particular, Choi rank is a finite-dimensional quantum representation invariant. It is not a DSD universal dimension quantity.

## 11. Reconstruction package

005F therefore adds no new universal DSD axiom. It adds a target-specific downstream representation package:

```text
KSD-QM  Kraus–Stinespring Dilation Representation Package

Input:
  fixed finite-dimensional complex Hilbert carrier
  admitted CPTP quantum channel map Phi

Derived standard representations:
  Choi-positive channel representation
  Kraus operator families
  Stinespring isometries
  optional unitary-plus-initialized-ancilla extension

Equivalence discipline:
  compare the induced Phi before comparing representation coordinates
  Kraus/dilation non-uniqueness is retained
  physical-environment interpretation requires an explicit additional bridge
```

The implication is

\[
\boxed{\mathrm{finite\text{-}dimensional\ CPTP\ map}\Longrightarrow\mathrm{KSD\text{-}QM\ representation\ package}}
\]

by standard quantum information theory.

## 12. Provenance audit

```text
fixed Stage-VI formation / typed downstream separation     A PRE_EXISTING_DSD
optional representation package                            A PRE_EXISTING_DSD
explicit downstream analytic/constitutive bridges          A PRE_EXISTING_DSD
finite-dimensional complex Hilbert carrier                  C TARGET SPECIALIZATION
CPTP channel status                                         005A+005B / CONDITIONAL QM
Kraus representation theorem                               STANDARD FINITE-DIM QM
Stinespring isometric dilation                             STANDARD FINITE-DIM QM
minimal Kraus/environment dimension = Choi rank            STANDARD FINITE-DIM QM
unitary completion after ancilla initialization/padding    STANDARD FINITE-DIM LINEAR ALGEBRA
literal physical-environment identification                NOT DERIVED
unique microscopic interaction                             NOT DERIVED
```

## 13. Rejected shortcuts

\[
\boxed{\text{CPTP map}\not\Rightarrow\text{unique Kraus family}}
\]

\[
\boxed{\text{CPTP map}\not\Rightarrow\text{unique Stinespring coordinates}}
\]

\[
\boxed{\text{Stinespring environment exists mathematically}\not\Rightarrow\text{a specified literal bath has been identified}}
\]

\[
\boxed{\text{global unitary realization}\not\Rightarrow\text{reduced channel is reversible}}
\]

\[
\boxed{\text{Kraus operator}\not\Rightarrow\text{measurement outcome / physical trajectory}}
\]

unless an explicit instrument interpretation is supplied.

## 14. Finite reproducibility witness

File:

```text
audits/science/2026-09-09_qm_core_005f_kraus_stinespring_environment_unitary_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-09_qm_core_005f_kraus_stinespring_environment_unitary_gate.py --mode all
```

Expected final line:

```text
OVERALL: PASS_WITH_REFINEMENT
```

The script checks:

```text
Kraus completeness
Kraus-unitary-mixing non-uniqueness
Choi-rank = 2 amplitude-damping witness
Stinespring isometry
partial-trace recovery
non-unique environment coordinates
unitary extension with initialized ancilla
global reversibility / reduced irreversibility separation
```

## 15. Verdict

**PASS_WITH_REFINEMENT.**

Once a finite-dimensional complex Hilbert carrier and CPTP map are supplied, Kraus and Stinespring representations are recovered exactly by standard theorem. DSD contributes a useful typing and equivalence discipline: the quantum transition map, its representations, its reduced readout, and any literal environment interpretation remain separate objects.

The main refinement is that dilation existence is representational, not by itself ontological.

The reconstructed chain is now

```text
005A  ancilla-compatible admissibility -> CP
005B  deterministic normalization      -> TP
005C  physical reversible channel       -> unitary conjugation
005D  coherent unitary group            -> Hamiltonian generator
005E  continuous CPTP semigroup         -> GKSL generator
005F  finite-dimensional CPTP map       -> Kraus / Stinespring dilation package
```

Next target: **QM Core 005G — Naimark / measurement-dilation / instrument realization gate**. The next audit should distinguish POVM equivalence from a unique laboratory measurement implementation and connect the earlier Born/effect reconstruction to ancilla-assisted projective measurement.

## References

1. John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018, Section 2.2, especially Corollary 2.27 (characterizations of quantum channels). Manuscript: https://cs.uwaterloo.ca/~watrous/TQI/
2. W. F. Stinespring, “Positive Functions on C*-Algebras,” *Proceedings of the American Mathematical Society* 6 (1955), 211–216.
3. Kwon Dominicus, *Formation Axiom System: Dimensional-Structural Describability*, 2026.
4. Kwon Dominicus, *Property Axiom System in Dimensional-Structural Describability*, 2026.
5. Kwon Dominicus, *Channel-Indexed Static Aggregation in Dimensional-Structural Describability*, 2026.
6. Kwon Dominicus, *Structural Reorganization Dynamics in Dimensional-Structural Describability*, 2026.
