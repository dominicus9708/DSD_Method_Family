# QM Core Reconstruction 007 — Canonical Position–Momentum / CCR / Weyl Representation Gate

Date: 2026-09-09  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: reconstruct the canonical position–momentum representation gate after QM Core 006, while separating formal commutators, operator domains, exponentiated Weyl relations, continuity, irreducibility, Stone–von Neumann uniqueness, and finite truncation.

## 1. Question

QM Core 006 established that an unbounded operator must be treated as an action together with a domain, not as an everywhere-defined matrix.

The present question is:

> Under what explicit conditions does the standard canonical pair \(Q,P\) arise, what does the Stone–von Neumann theorem actually make unique, and which weaker statements are insufficient?

The critical distinctions are:

```text
FORMAL_OPERATOR_EXPRESSION
COMMON_DENSE_DOMAIN
COMMON_INVARIANT_CORE
CCR_ON_CORE
SELF_ADJOINT_REALIZATION
EXPONENTIATED_WEYL_RELATIONS
STRONG_CONTINUITY / REGULARITY
IRREDUCIBILITY
FIXED_CENTRAL_CHARACTER / HBAR
STONE_VON_NEUMANN_EQUIVALENCE
FINITE_TRUNCATION_APPROXIMATION
PHYSICAL_POSITION_MOMENTUM_INTERPRETATION
```

These must not be collapsed.

## 2. Standard Schrödinger canonical pair

Use

\[
\mathcal H=L^2(\mathbb R).
\]

The standard position and momentum realizations are

\[
(Q\psi)(x)=x\psi(x),
\]

and

\[
(P\psi)(x)=-i\hbar\,\psi'(x),
\]

with their self-adjoint domains.

The Schwartz space

\[
\mathcal S(\mathbb R)
\]

is a common dense invariant core for the usual canonical calculations.

For every \(\psi\in\mathcal S(\mathbb R)\),

\[
QP\psi-PQ\psi=i\hbar\psi.
\]

Thus the exact core statement is

\[
\boxed{
[Q,P]\psi=i\hbar\psi,
\qquad
\psi\in\mathcal S(\mathbb R).
}
\]

The domain clause is part of the statement.

## 3. CCR-on-core is not the same statement as the Weyl relations

A formal or domain-restricted commutator identity does not, by itself, supply all hypotheses needed for representation uniqueness.

The exponentiated bounded-unitary form is cleaner for this purpose.

Define

\[
T(a)=e^{-iaP/\hbar},
\qquad
M(b)=e^{ibQ/\hbar}.
\]

In the Schrödinger representation,

\[
(T(a)\psi)(x)=\psi(x-a),
\]

and

\[
(M(b)\psi)(x)=e^{ibx/\hbar}\psi(x).
\]

They satisfy

\[
\boxed{
T(a)M(b)
=
e^{-iab/\hbar}M(b)T(a).
}
\]

This is the one-degree-of-freedom Weyl form of the canonical commutation relation in the sign convention used by this audit.

The audit therefore keeps separate:

```text
CCR_ON_COMMON_CORE
WEYL_RELATION_FOR_BOUNDED_UNITARIES
```

and never silently replaces one by the other.

## 4. Strong continuity gate

The standard translation and modulation groups are strongly continuous.

For the normalized Gaussian

\[
\psi_0(x)=\pi^{-1/4}e^{-x^2/2},
\]

the translation overlap is

\[
\langle\psi_0,T(a)\psi_0\rangle=e^{-a^2/4},
\]

so

\[
\|T(a)\psi_0-\psi_0\|^2
=2\left(1-e^{-a^2/4}\right)
\to0.
\]

Similarly,

\[
\langle\psi_0,M(b)\psi_0\rangle
=e^{-b^2/(4\hbar^2)},
\]

and

\[
\|M(b)\psi_0-\psi_0\|^2
=2\left(1-e^{-b^2/(4\hbar^2)}\right)
\to0.
\]

This matters because regularity/strong continuity is a real theorem prerequisite, not decorative wording.

## 5. CWR-QM selector

Define the target specialization:

```text
CWR-QM  Canonical Weyl Representation

input:
    finite number of canonical degrees of freedom
    complex Hilbert carrier H
    fixed nonzero hbar / central character

supply:
    strongly continuous unitary families T(a), M(b)

constraints:
    T(a1+a2) = T(a1)T(a2)
    M(b1+b2) = M(b1)M(b2)
    T(a)M(b) = exp(-iab/hbar) M(b)T(a)
    representation is irreducible
```

For one canonical pair, the standard Stone–von Neumann theorem then yields unitary equivalence to the Schrödinger representation, up to the chosen convention for the canonical variables and central character.

Thus:

\[
\boxed{
\mathrm{CWR\!-\!QM}
\Longrightarrow
\text{Schrödinger representation up to unitary equivalence}
}
\]

by a standard representation theorem.

This is not a generic DSD theorem.

## 6. What Stone–von Neumann uniqueness actually means

The theorem does not say that one coordinate basis, one laboratory apparatus, or one literal physical embedding is uniquely selected.

It says that, for a finite number of canonical degrees of freedom and under the regularity plus irreducibility hypotheses with fixed nonzero central character, the irreducible Weyl representation is unique up to unitary equivalence.

Therefore:

\[
\boxed{
\text{representation uniqueness up to unitary}
\neq
\text{unique coordinate description}
}
\]

and

\[
\boxed{
\text{representation uniqueness up to unitary}
\neq
\text{unique physical apparatus}.
}
\]

The theorem also does not derive the numerical value of \(\hbar\) from DSD.

## 7. Irreducibility is an independent gate

The audit constructs the direct sum of two identical Schrödinger Weyl representations.

The direct sum still satisfies exactly the same Weyl phase relation componentwise.

However, projection onto either copy is a nontrivial projection that commutes with every translation and modulation operator.

Hence the representation is reducible.

Therefore:

\[
\boxed{
\text{Weyl relation}
\not\Rightarrow
\text{irreducibility}.
}
\]

This blocks an invalid shortcut from the algebraic relation directly to the irreducible Stone–von Neumann conclusion.

For reducible regular representations, one obtains multiplicity/decomposition structure rather than one single irreducible copy.

## 8. Regularity is also a real boundary

Strong continuity cannot simply be omitted.

Nonregular representations of the Weyl algebra can evade the Stone–von Neumann uniqueness conclusion because one or both one-parameter unitary families fail the continuity needed to obtain the standard self-adjoint generators through Stone's theorem.

Therefore:

\[
\boxed{
\text{abstract Weyl-type algebraic relation alone}
\not\Rightarrow
\text{standard Schrödinger representation}.
}
\]

The audit does not identify nonregular representations with a new DSD prediction; they are a standard mathematical boundary of the theorem.

## 9. Finite-dimensional obstruction

For finite matrices \(A,B\),

\[
\operatorname{Tr}[A,B]=0.
\]

But for \(d>0\),

\[
\operatorname{Tr}(i\hbar I_d)=i\hbar d\ne0.
\]

Therefore

\[
\boxed{
[A,B]=i\hbar I_d
}
\]

cannot hold exactly in finite dimension.

This confirms the boundary already opened in QM Core 006.

## 10. Truncated oscillator witness

Let the finite cutoff dimension be \(d\), with truncated ladder operators

\[
a|n\rangle=\sqrt n\,|n-1\rangle,
\]

and truncated \(a^\dagger\).

Define dimensionless

\[
Q_d=\frac{a+a^\dagger}{\sqrt2},
\qquad
P_d=\frac{a-a^\dagger}{i\sqrt2}.
\]

The audit verifies the exact finite identity

\[
\boxed{
[Q_d,P_d]
=i\left(I_d-d|d-1\rangle\langle d-1|\right).
}
\]

Consequently, for every basis state below the cutoff edge,

\[
[Q_d,P_d]|n\rangle=i|n\rangle,
\qquad n<d-1,
\]

while the full finite operator still fails the exact CCR because the entire trace-balancing defect appears at the top state.

This gives a precise interpretation of finite truncation:

\[
\boxed{
\text{good low-sector CCR approximation}
\not\Rightarrow
\text{exact finite-dimensional CCR}.
}
\]

The cutoff defect is not evidence that the continuum CCR has failed.

## 11. DSD placement

The conservative placement is:

```text
Formation:
    system identity
    canonical-observable role labels
    representation-sector identity when explicitly supplied

Property:
    state
    domain membership
    Schwartz-core membership
    spectral records
    representation labels

Static Aggregation:
    bounded readouts / spectral probabilities

Continuous transformation interface:
    translation group T(a)
    modulation group M(b)

Quantum specialization:
    Hilbert carrier
    self-adjoint Q,P
    CCR-on-core
    Weyl relations
    strong continuity
    irreducibility
    Stone-von Neumann theorem
```

The group parameters \(a,b\) are not automatically physical time.

Therefore the Weyl one-parameter groups must not be identified with DSD temporal dynamics merely because they are continuous groups.

## 12. Describability consequence

The most useful DSD distinction at this gate is:

\[
\boxed{
\text{formal relation describable}
\neq
\text{representation uniquely determined}
}
\]

until the following additional structure is supplied:

```text
operator/domain realization
Weyl exponentiation
strong continuity
irreducibility
fixed central character
finite number of canonical degrees of freedom
```

Once those conditions are present, the standard representation theorem sharply reduces representation ambiguity to unitary equivalence.

Thus 007 provides a genuine closure result for the canonical pair inside the supplied Hilbert specialization, not an independent derivation of the Hilbert carrier itself.

## 13. Infinite-degree-of-freedom boundary

Stone–von Neumann uniqueness is a finite-canonical-degree-of-freedom theorem.

It must not be exported unchanged to quantum field theory or other systems with infinitely many canonical degrees of freedom, where unitarily inequivalent representations occur.

Therefore:

\[
\boxed{
\text{finite-DOF canonical uniqueness}
\not\Rightarrow
\text{QFT representation uniqueness}.
}
\]

This boundary is important for later DSD/QFT work.

## 14. What DSD does and does not establish

### Established conditionally

Given the standard Hilbert specialization, the usual self-adjoint canonical pair, the Weyl relations, strong continuity, irreducibility, fixed nonzero \(\hbar\), and finitely many canonical degrees of freedom:

\[
\boxed{
\text{canonical Weyl representation}
\Longrightarrow
\text{Schrödinger representation up to unitary equivalence}
}
\]

by the Stone–von Neumann theorem.

The finite witness independently verifies the exact finite-dimensional obstruction and the structure of the truncation defect.

### Not established

Generic DSD does not imply:

\[
\text{Hilbert carrier},
\]

\[
\text{CCR},
\]

\[
\text{Weyl relations},
\]

\[
\text{irreducibility},
\]

\[
\text{strong continuity},
\]

or

\[
\text{the value of }\hbar.
\]

A domain-restricted formal commutator alone is not sufficient for Stone–von Neumann uniqueness.

No new quantum prediction is obtained at this gate.

## 15. Provenance classification

```text
DSD typed applicability / definedness                         PRE_EXISTING_DSD
operator-domain discipline                                   CARRIED FROM QM CORE 006 / STANDARD MATH
common-core distinction                                      STANDARD FUNCTIONAL ANALYSIS
Schrödinger Q,P realization                                  TARGET SPECIALIZATION
CCR on Schwartz core                                         STANDARD QM/MATH
Weyl exponentiation                                          STANDARD QM/MATH
strong continuity / regularity                               STANDARD REPRESENTATION THEORY
irreducibility                                               TARGET-SPECIALIZATION SELECTOR
Stone-von Neumann theorem                                    CONDITIONAL STANDARD MATH
finite trace obstruction                                     GENERAL FINITE-DIM ALGEBRA
truncated-oscillator boundary defect                          GENERAL FINITE-DIM WITNESS
physical-implementation uniqueness rejection                 REPRESENTATION/IDENTIFIABILITY BOUNDARY
```

## 16. Audit verdict

**PASS_WITH_REFINEMENT**.

QM Core 007 closes the ordinary finite-degree-of-freedom canonical position–momentum representation gate conditionally on the Hilbert/Weyl specialization.

The valid reconstruction chain is:

```text
Hilbert carrier + self-adjoint canonical pair
    -> common invariant core
    -> CCR on that core

strongly continuous Weyl representation
    + fixed nonzero hbar
    + irreducibility
    + finite canonical degree count
    -> Stone-von Neumann
    -> Schrödinger representation up to unitary equivalence
```

The invalid shortcuts are:

```text
formal [Q,P]=i hbar I somewhere
    != automatic Weyl representation

Weyl relation
    != automatic irreducibility

finite truncation
    != exact finite-dimensional CCR

finite-DOF Stone-von Neumann
    != QFT uniqueness
```

The remaining primary reconstruction boundary is still the one identified in QM Core 004: why the admissible quantum carrier should be complex Hilbertian in the first place.

## 17. Reproducibility

GitHub paths:

```text
audits/science/2026-09-09_qm_core_007_canonical_position_momentum_ccr_weyl_representation_gate.py
audits/science/2026-09-09_qm-core-007-canonical-position-momentum-ccr-weyl-representation-gate-audit.md
methodology/QUANTUM_CANONICAL_CCR_WEYL_REPRESENTATION_INTERFACE.md
```

Run from repository root:

```bash
python audits/science/2026-09-09_qm_core_007_canonical_position_momentum_ccr_weyl_representation_gate.py --mode all
```

Observed result:

```text
OVERALL: PASS_WITH_REFINEMENT
```

## 18. Standard external references used for theorem checking

- David Tong, *Quantum Mechanics*, Section 3, canonical commutation relations and the finite-matrix trace obstruction.
- Jan Dereziński, *Introduction to representations of the canonical commutation and anticommutation relations*, arXiv:math-ph/0511030, especially the regular CCR and Stone–von Neumann discussion.
- Standard Stone and von Neumann representation theorem for strongly continuous/regular irreducible Weyl representations with fixed nonzero central character and finitely many canonical degrees of freedom.

These references supply standard quantum-mechanical and representation-theoretic results. They are not counted as DSD-derived structure.

## 19. Next target

**QM Core 008 — Complex-Hilbert Carrier Closure / Independent-Origin Boundary Gate**.

The next audit should return to the unresolved boundary from QM Core 004 and classify, with explicit provenance, which ingredients can be obtained from generic DSD plus operational assumptions and which remain quantum-specific selectors:

```text
real ordered state carrier
convexity / affine probability structure
complex scalar field
inner-product structure
projective pure-state geometry
tensor-product composition
local tomography / composition selectors
continuous reversible symmetry
full effect structure
Hilbert-space representation
```

The goal is not to force an independent Hilbert derivation, but to determine exactly where the independent DSD reconstruction stops and where standard quantum specialization begins.
