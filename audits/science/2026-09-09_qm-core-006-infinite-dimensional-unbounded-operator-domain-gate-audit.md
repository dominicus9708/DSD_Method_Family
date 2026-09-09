# QM Core Reconstruction 006 — Infinite-Dimensional Hilbert / Unbounded-Operator / Domain Gate

Date: 2026-09-09  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: extend the reconstruction beyond finite-dimensional bounded-operator quantum mechanics while preventing operator symbols, domains, self-adjoint realizations, spectral probabilities, and differentiability domains from being silently identified.

## 1. Question

QM Core 003–005G reconstructed a substantial finite-dimensional standard-QM chain conditionally on a complex Hilbert carrier.

The present question is:

> Which parts survive in infinite-dimensional Hilbert space, which statements require explicit domain/topology hypotheses, and how should DSD type applicability so that an unbounded observable or generator is not treated as an everywhere-defined matrix?

The critical distinctions are:

```text
HILBERT_STATE
OPERATOR_SYMBOL
OPERATOR_DOMAIN
SYMMETRIC_OPERATOR
SELF_ADJOINT_OPERATOR
ESSENTIALLY_SELF_ADJOINT_OPERATOR
SPECTRAL_PVM
SPECTRAL_PROBABILITY
FINITE_MOMENT
OPERATOR_ACTION
STRONGLY_CONTINUOUS_UNITARY_GROUP
STRONGLY_DIFFERENTIABLE_ORBIT
UNBOUNDED_SEMIGROUP_GENERATOR
```

These are related structures, but they are not interchangeable.

## 2. Operator = action plus domain

For an unbounded operator the pair

\[
(A,D(A))
\]

is the mathematical object.

Two operators with the same formal differential expression but different domains can have different adjoints, spectra, and physical interpretations.

For a densely defined operator \(A\), symmetry means

\[
\langle \phi,A\psi\rangle
=
\langle A\phi,\psi\rangle,
\qquad \phi,\psi\in D(A).
\]

Self-adjointness is stronger:

\[
\boxed{A=A^*}
\]

including equality of domains.

Thus

\[
\boxed{
\text{symmetric}
\not\Rightarrow
\text{self-adjoint}
}.
\]

This distinction is invisible in finite-dimensional Hermitian-matrix notation because every matrix is everywhere defined and bounded.

## 3. Position operator witness

On

\[
\mathcal H=L^2(\mathbb R),
\]

the position operator is

\[
(Q\psi)(x)=x\psi(x),
\]

with maximal self-adjoint domain

\[
\boxed{
D(Q)=\{\psi\in L^2(\mathbb R):x\psi(x)\in L^2(\mathbb R)\}.
}
\]

Consider normalized translated Gaussians

\[
\psi_n(x)=\pi^{-1/4}e^{-(x-n)^2/2}.
\]

Then

\[
\|\psi_n\|=1,
\]

but

\[
\boxed{
\|Q\psi_n\|^2=n^2+\frac12.
}
\]

Therefore no constant \(C\) satisfies

\[
\|Q\psi\|\le C\|\psi\|
\]

for every \(\psi\in D(Q)\).

Hence \(Q\) is genuinely unbounded.

A normalized quantum state is therefore not automatically in the action domain of every observable.

## 4. Momentum operator witness

On \(L^2(\mathbb R)\), the standard momentum operator is

\[
P=-i\hbar\frac{d}{dx}
\]

with its standard self-adjoint Sobolev domain, equivalently the Fourier-transform pullback of the multiplication-operator domain.

For

\[
\phi_k(x)=e^{ikx}\psi_0(x),
\]

where \(\psi_0\) is the centered Gaussian above,

\[
\boxed{
\|P\phi_k\|^2
=
\hbar^2\left(k^2+\frac12\right).
}
\]

Thus \(P\) is also unbounded.

Again:

\[
\boxed{
\text{normalized state}
\not\Rightarrow
\text{state lies in }D(P).
}
\]

## 5. Spectral probability does not require operator action on the state

Let \(A\) be self-adjoint with spectral projection-valued measure \(E_A\).

The spectral theorem gives the operator through

\[
A=\int_{\mathbb R}\lambda\,dE_A(\lambda)
\]

with the appropriate operator domain.

For every normalized \(\psi\in\mathcal H\), regardless of whether \(\psi\in D(A)\),

\[
\boxed{
\mu_\psi(\Delta)
=
\langle\psi,E_A(\Delta)\psi\rangle
}
\]

is a probability measure on Borel sets \(\Delta\subseteq\mathbb R\).

Hence three statuses must be separated:

```text
spectral probability distribution exists
finite first absolute moment exists
A psi exists as a Hilbert-space vector
```

More precisely,

\[
\psi\in D(A)
\iff
\int \lambda^2\,d\mu_\psi(\lambda)<\infty,
\]

whereas the finite first absolute moment is controlled by the weaker form-domain condition

\[
\psi\in D(|A|^{1/2})
\iff
\int |\lambda|\,d\mu_\psi(\lambda)<\infty.
\]

Therefore

\[
\boxed{
\text{measurement probability describability}
\not\Rightarrow
\text{operator-action describability}
}.
\]

This is an important infinite-dimensional refinement of the finite-dimensional readout interface.

## 6. Strong continuity does not imply differentiability on every state

Define the translation group

\[
(U(a)\psi)(x)=\psi(x-a).
\]

It is a strongly continuous one-parameter unitary group on all of \(L^2(\mathbb R)\).

Stone's theorem gives a unique self-adjoint generator \(P/\hbar\), equivalently

\[
U(a)=e^{-iaP/\hbar}.
\]

However, the strong derivative

\[
\lim_{a\to0}\frac{U(a)\psi-\psi}{a}
\]

exists only for \(\psi\in D(P)\).

Use the normalized state

\[
\chi(x)=\mathbf 1_{[0,1]}(x).
\]

For \(0<|a|<1\),

\[
\boxed{
\|U(a)\chi-\chi\|_2
=
\sqrt{2|a|}
\to0.
}
\]

Thus the orbit is strongly continuous.

But

\[
\boxed{
\left\|\frac{U(a)\chi-\chi}{a}\right\|_2
=
\sqrt{\frac{2}{|a|}}
\to\infty.
}
\]

Hence

\[
\boxed{
\text{strongly continuous unitary evolution}
\not\Rightarrow
\text{strongly differentiable evolution for every state}.
}
\]

This refines QM Core 005D:

```text
strongly continuous unitary group
    -> unique self-adjoint generator                [Stone]

state-vector differential equation
    -> only on the generator domain                 [domain gate]
```

The statement

\[
i\hbar\frac{d}{dt}\psi(t)=H\psi(t)
\]

must therefore carry the prerequisite

\[
\psi(t)\in D(H).
\]

## 7. Symmetric is not self-adjoint — finite-interval momentum

Consider

\[
P_0=-i\frac{d}{dx}
\]

on \(L^2(0,1)\) with

\[
D(P_0)=H_0^1(0,1).
\]

This operator is symmetric, but its adjoint has the larger maximal first-derivative domain.

The deficiency equations

\[
P_0^*\psi_+=+i\psi_+,
\qquad
P_0^*\psi_-=-i\psi_-
\]

have square-integrable solutions

\[
\psi_+(x)=e^{-x},
\qquad
\psi_-(x)=e^x.
\]

Both belong to \(L^2(0,1)\), so the deficiency indices are

\[
\boxed{(1,1)}.
\]

The symmetric operator is therefore not self-adjoint and has a \(U(1)\) family of self-adjoint extensions. A standard parametrization is

\[
\boxed{
D(P_\theta)
=
\{\psi\in H^1(0,1):\psi(1)=e^{i\theta}\psi(0)\}.
}
\]

Thus the formal symbol \(-i\,d/dx\) does not uniquely specify one observable.

The boundary/domain data are part of the operator identity.

## 8. DSD domain-applicability gate

Define the target selector

```text
IDU-QM  Infinite-Dimensional Unbounded-Operator Gate

input:
    complex Hilbert carrier H
    state psi or density operator rho
    operator symbol A

must supply when A is unbounded:
    dense domain D(A)
    adjoint/domain relation
    self-adjointness or stated extension status
    spectral PVM E_A when A is treated as an observable
    topology for any limiting/evolution statement

state-specific prerequisites:
    SPECTRAL_PROBABILITY      psi in H
    FINITE_FIRST_MOMENT       psi in D(|A|^(1/2))
    OPERATOR_ACTION           psi in D(A)
    GENERATOR_DERIVATIVE      psi in D(generator)
```

Then the DSD Property applicability layer can represent a state as fully defined while an operator action on that state is inapplicable.

That is not a contradiction or missing state.

It is a domain prerequisite.

## 9. DSD placement

The conservative placement is:

```text
Formation
    stable identity of system / observable role / boundary convention when supplied

Property
    state record
    operator-domain membership
    self-adjoint-extension label
    spectral probability
    moment/applicability status

Static Aggregation
    bounded readout vectors or selected spectral probabilities

Dynamics
    strongly continuous unitary/semigroup law
    generator-domain condition
    differentiability only where applicable

Quantum specialization
    infinite-dimensional Hilbert carrier
    self-adjoint operator theory
    spectral theorem
    Stone theorem
```

The key DSD rule is

\[
\boxed{
\text{state defined}
\neq
\text{every operator action applicable}.
}
\]

## 10. Audit of earlier QM Core gates

### QM Core 003 — Born/effect valuation

For trace-class states and bounded effects, the probability rule

\[
\operatorname{Tr}(\rho E)
\]

remains well defined.

For an unbounded observable, the safer general interface is its spectral PVM:

\[
\Pr(A\in\Delta)=\operatorname{Tr}[\rho E_A(\Delta)].
\]

The finite-dimensional representation proof used in 003 is not re-declared as an infinite-dimensional derivation here.

### QM Core 005D — continuous unitary / Hamiltonian gate

This gate survives and becomes more precise.

Stone's theorem permits an unbounded self-adjoint generator, but the differential Schrödinger equation is a domain-restricted statement.

### QM Core 005E — GKSL semigroup gate

The finite-dimensional bounded-generator formula does **not** export unchanged.

Strongly continuous quantum dynamical semigroups can have unbounded generators. Domain, conservativity, and operator-algebra hypotheses become essential, and naive use of the bounded GKSL form can fail.

Therefore:

\[
\boxed{
\text{005E finite-dimensional GKSL formula}
\not\Rightarrow
\text{general unbounded infinite-dimensional generator formula}.
}
\]

### QM Core 005F — Kraus/Stinespring gate

Stinespring dilation survives in general operator-algebra form, but a finite Kraus list and finite environment dimension are no longer guaranteed.

Any infinite-dimensional use must declare the representation class and convergence topology rather than importing the finite-dimensional bookkeeping literally.

### QM Core 005G — Naimark gate

Naimark dilation also survives beyond finite dimensions, but the dilation carrier may itself be infinite-dimensional.

The 005G identifiability boundary remains unchanged:

\[
\text{POVM}
\not\Rightarrow
\text{unique instrument or laboratory implementation}.
\]

## 11. Finite truncation warning — exact CCR cannot be certified by matrices

For finite matrices \(A,B\),

\[
\operatorname{Tr}[A,B]=0.
\]

But

\[
\operatorname{Tr}(i\hbar I_d)=i\hbar d\ne0.
\]

Hence no finite-dimensional matrices can satisfy

\[
[A,B]=i\hbar I_d
\]

exactly.

Therefore a finite matrix truncation may approximate oscillator matrix elements, but it cannot prove the exact canonical commutation relation.

This is a methodological warning for the next gate, not yet a full CCR reconstruction.

## 12. Provenance classification

```text
DSD typed applicability / undefined-vs-defined discipline          A PRE_EXISTING_DSD
DSD readout-vs-transition separation                               A PRE_EXISTING_DSD
infinite-dimensional Hilbert carrier                               C TARGET SPECIALIZATION
operator domain requirement                                        STANDARD FUNCTIONAL ANALYSIS
symmetric vs self-adjoint distinction                              STANDARD FUNCTIONAL ANALYSIS
spectral PVM / self-adjoint observable interface                   STANDARD QM/MATH
Stone generator theorem                                            STANDARD QM/MATH
interval-momentum deficiency witness                               STANDARD QM/MATH + analytic witness
finite-CCR trace obstruction                                       GENERAL FINITE-DIM ALGEBRA
unbounded Lindblad warning                                         STANDARD OPEN-QM BOUNDARY
Hilbert-carrier origin                                              STILL NOT DERIVED
```

## 13. Audit verdict

**PASS_WITH_REFINEMENT**.

The finite-dimensional reconstruction does not collapse when infinite-dimensional Hilbert space is admitted, but several statements must be upgraded from matrix equalities to domain-aware operator statements.

The principal result is:

\[
\boxed{
\text{operator symbol}
\neq
\text{operator realization}
=
(\text{action},\text{domain}).
}
\]

For DSD, this produces a particularly clean applicability distinction:

\[
\boxed{
\text{normalized state}
\not\Rightarrow
\text{all observable/generator operations applicable}.
}
\]

At the same time, spectral probabilities can remain fully describable even when \(A\psi\) is not defined.

No new quantum prediction is obtained at this gate.

## 14. Reproducibility

GitHub paths:

```text
audits/science/2026-09-09_qm_core_006_infinite_dimensional_unbounded_operator_domain_gate.py
audits/science/2026-09-09_qm-core-006-infinite-dimensional-unbounded-operator-domain-gate-audit.md
methodology/QUANTUM_INFINITE_DIMENSIONAL_OPERATOR_DOMAIN_INTERFACE.md
```

Run from repository root:

```bash
python audits/science/2026-09-09_qm_core_006_infinite_dimensional_unbounded_operator_domain_gate.py --mode all
```

Expected:

```text
OVERALL: PASS_WITH_REFINEMENT
```

The script deliberately uses exact analytic formulas and finite algebraic obstructions. It does not claim that a finite discretization proves an infinite-dimensional theorem.

## 15. Standard external references used for theorem checking

- Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, 2nd ed., AMS GSM 157 (2014), online edition authorized by AMS. Relevant chapters: self-adjointness and spectrum; spectral theorem; quantum dynamics and Stone's theorem; position and momentum operators. https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/
- Guy Bonneau, Jacques Faraut, Galliano Valent, “Self-adjoint extensions of operators and the teaching of quantum mechanics,” *American Journal of Physics* 69 (2001) 322–331. DOI: 10.1119/1.1328351. arXiv: quant-ph/0103153.
- Inken Siemon, Alexander S. Holevo, Reinhard F. Werner, “Unbounded generators of dynamical semigroups,” *Open Systems & Information Dynamics* 24 (2017). arXiv:1707.02266.

These references supply standard functional-analysis and quantum-mechanical theorems. They are not counted as DSD-derived structure.

## 16. Next target

**QM Core 007 — Canonical Position–Momentum / CCR / Weyl Representation Gate**.

The next audit should separate:

```text
formal commutator [Q,P]=i hbar I
common invariant domain
Schwartz-core realization
Weyl exponentiated relations
strong continuity
irreducibility
Stone-von Neumann uniqueness
finite truncation approximation
```

The central question will be whether DSD can preserve the exact domain/representation prerequisites without mistaking a formal commutator or a finite matrix truncation for the canonical representation theorem.
