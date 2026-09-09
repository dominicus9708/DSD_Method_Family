# QM Core Reconstruction 005E — Continuous CPTP Semigroup / GKSL-Lindblad Generator Gate

Date: 2026-09-09  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: separate a general time-indexed CPTP family, CP-divisible dynamics, a time-homogeneous quantum dynamical semigroup, and a GKSL-Lindblad generator; then identify the exact boundary between reversible Hamiltonian dynamics and dissipative open-system dynamics.

## 1. Question

QM Core 005D established the standard conditional implication

\[
\text{strongly continuous one-parameter unitary group}
\Longrightarrow
U(t)=e^{-itH/\hbar}.
\]

Open-system dynamics is broader.

The next question is:

> If every time slice is a valid CPTP quantum channel, what additional temporal conditions are required before one may infer a time-homogeneous GKSL-Lindblad generator?

The critical distinctions are:

```text
CPTP_AT_EACH_TIME
CP_DIVISIBLE_FAMILY
CPTP_SEMIGROUP
TIME_LOCAL_GKSL_GENERATOR
TIME_HOMOGENEOUS_GKSL_GENERATOR
UNITARY_GROUP_SUBCASE
```

These notions must not be identified automatically.

## 2. Standard finite-dimensional quantum dynamical semigroup

Let

\[
\{\Phi_t\}_{t\ge0}
\]

be linear maps on \(M_d(\mathbb C)\).

Define the finite-dimensional quantum dynamical semigroup gate by

\[
\Phi_0=\operatorname{id},
\]

\[
\Phi_{t+s}=\Phi_t\circ\Phi_s,
\qquad s,t\ge0,
\]

every \(\Phi_t\) is CPTP, and \(t\mapsto\Phi_t\) is continuous.

In finite dimension, the generator is bounded.

The standard Gorini-Kossakowski-Sudarshan-Lindblad theorem gives

\[
\boxed{\Phi_t=e^{t\mathcal L}}
\]

with generator

\[
\boxed{
\mathcal L(\rho)
=
-\frac{i}{\hbar}[H,\rho]
+
\sum_\alpha
\left(
L_\alpha\rho L_\alpha^\dagger
-\frac12\{L_\alpha^\dagger L_\alpha,\rho\}
\right).
}
\]

Equivalent GKS-matrix forms may be used after choosing an operator basis.

The original finite-level result is V. Gorini, A. Kossakowski, and E. C. G. Sudarshan, *Completely positive dynamical semigroups of N-level systems*, J. Math. Phys. 17, 821-825 (1976), DOI 10.1063/1.522979.

The general bounded-generator result is G. Lindblad, *On the generators of quantum dynamical semigroups*, Commun. Math. Phys. 48, 119-130 (1976), DOI 10.1007/BF01608499.

Thus the correct finite-dimensional implication is

\[
\boxed{
\text{continuous time-homogeneous CPTP semigroup}
\Longrightarrow
\text{GKSL generator}.
}
\]

This is a standard quantum theorem under the supplied Hilbert/CPTP specialization.

It is not a theorem of generic DSD Dynamics.

## 3. A channel is not its generator

The map \(\Phi_t\) is a CPTP channel.

Its infinitesimal generator

\[
\mathcal L
=
\lim_{t\downarrow0}\frac{\Phi_t-\operatorname{id}}{t}
\]

is not itself required to be a channel.

For trace-preserving semigroup dynamics,

\[
\operatorname{Tr}\mathcal L(\rho)=0,
\]

whereas a normalized state has trace one.

The generator is therefore a tangent law on the state carrier, not another normalized state or deterministic channel.

This distinction is important in a DSD typed representation.

```text
STATE
CHANNEL
GENERATOR
```

must remain different typed roles.

## 4. Exact positive control: qubit dephasing semigroup

Use the qubit dephasing family

\[
\Phi_t
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
=
\begin{pmatrix}
a&e^{-\kappa t}b\\
e^{-\kappa t}c&d
\end{pmatrix},
\qquad \kappa\ge0.
\]

For every \(t\ge0\), this is a CPTP phase-damping channel.

Because

\[
e^{-\kappa(t+s)}=e^{-\kappa t}e^{-\kappa s},
\]

one has

\[
\boxed{\Phi_{t+s}=\Phi_t\circ\Phi_s.}
\]

The generator is

\[
\boxed{
\mathcal L(\rho)=\frac{\kappa}{2}(Z\rho Z-\rho),
}
\]

which is of GKSL form.

The coherence obeys

\[
\dot\rho_{01}=-\kappa\rho_{01}.
\]

This gives an exact finite-dimensional dissipative quantum dynamical semigroup.

## 5. Counterexample: smooth CPTP family does not imply a semigroup

Define instead

\[
\Gamma_t
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
=
\begin{pmatrix}
a&e^{-t^2}b\\
e^{-t^2}c&d
\end{pmatrix},
\qquad t\ge0.
\]

Each \(\Gamma_t\) is CPTP and the family is smooth.

However,

\[
e^{-(t+s)^2}\neq e^{-t^2}e^{-s^2}
\]

for generic positive \(s,t\).

Therefore

\[
\boxed{
\text{smooth CPTP family}
\not\Rightarrow
\text{time-homogeneous CPTP semigroup}.
}
\]

Consequently one cannot infer one fixed generator \(\mathcal L\) satisfying \(\Gamma_t=e^{t\mathcal L}\) merely from smoothness and pointwise CPTP admissibility.

## 6. Refinement: the counterexample is CP-divisible

For \(t\ge s\ge0\),

\[
\frac{e^{-t^2}}{e^{-s^2}}=e^{-(t^2-s^2)}\in(0,1].
\]

Hence there is a CPTP intermediate dephasing map \(V_{t,s}\) such that

\[
\boxed{\Gamma_t=V_{t,s}\circ\Gamma_s.}
\]

Therefore the family is CP-divisible despite not being a semigroup.

This yields the logical separation

\[
\boxed{
\text{CP-divisible}
\not\Rightarrow
\text{time-homogeneous semigroup}.
}
\]

For this regular invertible example, the time-local generator exists and is

\[
\boxed{
\mathcal L_t(\rho)=t(Z\rho Z-\rho).
}
\]

Equivalently the dephasing rate is \(\kappa(t)=2t\ge0\).

Thus the local equation

\[
\dot\rho(t)=\mathcal L_t(\rho(t))
\]

has GKSL form at every \(t\ge0\), but with a time-dependent rate.

Therefore

\[
\boxed{
\text{time-local GKSL form}
\not\Rightarrow
\text{one fixed GKSL semigroup generator}.
}
\]

This is why the label `Markovian` is not used here as a theorem synonym without qualification.

Open-system literature uses semigroup structure, CP-divisibility, and information-backflow criteria as distinct notions.

## 7. Irreversibility boundary

For the dephasing semigroup with \(\kappa>0\), consider

\[
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}.
\]

Initially,

\[
\|\rho_+-\rho_-\|_1=2.
\]

After time \(t\),

\[
\boxed{
\|\Phi_t(\rho_+)-\Phi_t(\rho_-)\|_1
=2e^{-\kappa t}<2
}
\]

for \(t>0\).

Thus distinguishability is strictly contracted.

By QM Core 005C, a channel with a physical CPTP inverse would preserve trace distance in both directions.

Therefore the dissipative dephasing channel cannot have a physical CPTP inverse.

At finite time \(t\), its linear superoperator is nevertheless algebraically invertible because \(e^{-\kappa t}>0\).

The algebraic inverse multiplies coherence by \(e^{+\kappa t}>1\).

Applying that inverse to \(|+\rangle\langle+|\) gives eigenvalues

\[
\frac{1\pm e^{\kappa t}}2,
\]

one of which is negative for \(t>0\).

Hence

\[
\boxed{
\text{algebraic inverse exists}
\not\Rightarrow
\text{physical CPTP inverse}.
}
\]

This reproduces the 005C distinction inside a continuous open-system family.

## 8. Relation to the 005D Hamiltonian branch

A CPTP semigroup is not automatically irreversible.

If all dissipative terms vanish,

\[
L_\alpha=0,
\]

then

\[
\mathcal L_H(\rho)=-\frac{i}{\hbar}[H,\rho],
\]

and

\[
\Phi_t(\rho)=e^{-itH/\hbar}\rho e^{itH/\hbar}.
\]

This semigroup on \(t\ge0\) extends to a two-sided CPTP group on \(t\in\mathbb R\).

Thus QM Core 005D is recovered as the reversible zero-dissipation subcase.

```text
GKSL quantum dynamical semigroup
├─ Hamiltonian-only branch -> reversible unitary group
└─ dissipative branch       -> may be physically irreversible
```

Therefore

\[
\boxed{
\text{CPTP semigroup}
\not\Rightarrow
\text{irreversible}.
}
\]

Strict contraction or another dissipative witness is needed to establish irreversibility for a particular semigroup.

## 9. Infinite-dimensional boundary

The simple finite-dimensional GKSL formula above relies on a bounded generator.

In infinite dimension, strongly continuous quantum dynamical semigroups can have unbounded generators.

Domains, closability, conservativity, and the exact operator-algebraic setting become substantive.

Therefore this audit does not claim that every infinite-dimensional quantum dynamical semigroup is captured by the finite sum formula without additional hypotheses.

The finite-dimensional result is the locked reconstruction target for QM Core 005E.

## 10. DSD interpretation

The pre-existing DSD Dynamics layer already separates

```text
instantaneous admissible state
time-indexed trajectory
supplied evolution law
cross-time lineage
```

QM Core 005E adds a quantum specialization selector

```text
QDS-QM  Quantum Dynamical Semigroup
```

with the following requirements:

```text
1. fixed declared finite-dimensional Hilbert carrier,
2. Phi_0 = id,
3. every Phi_t is an admitted CPTP channel,
4. Phi_(t+s) = Phi_t o Phi_s for all s,t >= 0,
5. t -> Phi_t is continuous,
6. the semigroup law is part of the supplied temporal specialization,
   not inferred from DSD lineage or continuity.
```

Then

\[
\boxed{
\mathrm{QDS\!-QM}
\Longrightarrow
\Phi_t=e^{t\mathcal L}
}
\]

with \(\mathcal L\) of GKSL form by the standard finite-dimensional theorem.

For a more general time-indexed family, a separate selector may instead admit a two-time propagator or time-local generator.

The DSD role is interface discipline:

\[
\boxed{
\text{DSD temporal admissibility}
\not\Rightarrow
\text{quantum semigroup law}.
}
\]

## 11. Provenance

Conservative classification:

```text
DSD dynamic slice admissibility / supplied-law discipline       A  PRE_EXISTING_DSD
DSD state-law-role separation                                   A  PRE_EXISTING_DSD
normalization preservation from 005B                            B  GENERAL_OPERATIONAL_RESULT
Hilbert state/operator carrier                                  SUPPLIED / C
complete positivity / ACE-QM from 005A                          C + conditional standard result
QDS-QM semigroup/time-homogeneity requirement                    C  TARGET_SPECIALIZATION_SELECTOR
GKSL generator conclusion                                       CONDITIONAL STANDARD-QM THEOREM
CP-divisibility distinction                                     STANDARD OPEN-QM STRUCTURE
"Markovian" terminology                                        NOT LOCKED AS ONE UNIVERSAL SYNONYM
```

Thus 005E does not count as an independent DSD derivation of the GKSL equation.

It does show exactly which temporal structure must be supplied before the standard generator theorem is applicable.

## 12. Reproducibility

Python:

```text
audits/science/2026-09-09_qm_core_005e_cptp_semigroup_gksl_generator_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-09_qm_core_005e_cptp_semigroup_gksl_generator_gate.py --mode all
```

Expected summary:

```text
exponential dephasing satisfies semigroup factor law                         PASS
exponential dephasing preserves trace                                        PASS
Gaussian dephasing slices are CPTP-range coherence factors                   PASS
Gaussian dephasing violates time-homogeneous semigroup law                   PASS
Gaussian intermediate dephasing factor lies in [0,1]                         PASS
Gaussian family is CP-divisible in this witness                              PASS
time-local dephasing generator matches Gaussian derivative                   PASS
generator output has trace zero rather than trace one                        PASS
orthogonal |+>,|-> trace norm starts at 2                                    PASS
dissipative dephasing strictly contracts trace norm                          PASS
algebraic inverse recovers an on-range state                                 PASS
algebraic inverse fails positivity on a valid input                          PASS

OVERALL: PASS_WITH_REFINEMENT
```

## 13. Verdict

**PASS_WITH_REFINEMENT**

The finite-dimensional GKSL-Lindblad generator is recovered conditionally once a continuous time-homogeneous CPTP semigroup is supplied.

Pointwise CPTP admissibility, smoothness, and even CP-divisibility are individually insufficient to force one fixed semigroup generator.

A smooth Gaussian dephasing family gives an explicit CP-divisible but non-semigroup witness, while exponential dephasing gives an exact GKSL semigroup control.

The dissipative semigroup also reproduces the 005C irreversibility boundary: its finite-time superoperator can be algebraically invertible while its inverse fails positivity.

The Hamiltonian result of 005D is retained as the reversible zero-dissipation subcase.

Next target: **QM Core 005F — Kraus / Stinespring dilation / environment-unitary realization gate**, separating mathematical dilation equivalence from a claim that a particular physical environment or microscopic interaction has been uniquely reconstructed.
