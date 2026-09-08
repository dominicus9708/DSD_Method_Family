# QM Core Reconstruction 005A — Positive vs Complete Positivity Gate

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: determine why isolated-system positivity is insufficient for quantum dynamics once a local map is required to remain admissible on declared composites.

## 1. Question

QM Core 004 closed the static/pre-Hilbert reconstruction audit. QM Core 005 begins the dynamical question:

\[
\boxed{\text{Why must an admissible quantum state map be completely positive rather than merely positive?}}
\]

The present step does not assume that generic DSD requires complete positivity. It tests the exact relation between pre-existing DSD dynamic admissibility and the standard quantum composite criterion.

## 2. Standard quantum definitions

For a linear map

\[
\Phi:M_d(\mathbb C)\to M_{d'}(\mathbb C),
\]

positivity means

\[
X\ge0\Longrightarrow \Phi(X)\ge0.
\]

Complete positivity means that for every ancillary dimension \(n\),

\[
\boxed{
\Phi\otimes \operatorname{id}_n
}
\]

is positive on \(M_d\otimes M_n\).

Equivalently in finite dimension, the Choi operator

\[
J(\Phi)
=(\Phi\otimes\operatorname{id})(|\Omega\rangle\langle\Omega|)
\]

is positive semidefinite. This is the standard Choi criterion. A standard reference is John Watrous, *The Theory of Quantum Information*, Chapter 2, Theorem 2.22.

## 3. Positive but not completely positive counterexample

Use matrix transposition

\[
T(X)=X^{\mathsf T}.
\]

### 3.1 Positivity

If \(X\ge0\), write

\[
X=C^\dagger C.
\]

Then

\[
X^{\mathsf T}=C^{\mathsf T}\overline C=(\overline C)^\dagger\overline C\ge0.
\]

Thus \(T\) is positive.

It is also trace-preserving:

\[
\operatorname{Tr}(X^{\mathsf T})=\operatorname{Tr}(X).
\]

### 3.2 Failure on an entangled composite

Take

\[
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
\rho_\Phi=|\Phi^+\rangle\langle\Phi^+|.
\]

Apply transposition only to the first subsystem:

\[
(T\otimes\operatorname{id})(\rho_\Phi)
=
\frac12
\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix}.
\]

For

\[
v=(0,1,-1,0)^{\mathsf T},
\]

one gets

\[
(T\otimes\operatorname{id})(\rho_\Phi)v=-\frac12v.
\]

Hence

\[
\boxed{
T\text{ is positive and trace-preserving but not completely positive.}
}
\]

Therefore

\[
\boxed{
\text{positivity}\not\Rightarrow\text{complete positivity}.
}
\]

This is a counterexample to an implication between dynamical admissibility conditions, not a counterexample to quantum mechanics or DSD.

## 4. DSD-side interpretation

The Structural Reorganization Dynamics layer already requires a declared trajectory to remain inside the admissible instantaneous-state class at every time slice, while the actual evolution law is supplied by the chosen dynamic specialization.

That pre-existing rule gives a useful whole-state admissibility gate:

```text
if a composite AB is declared,
a purported local evolution on A is not validated merely by checking isolated A states;
the resulting declared AB state must remain admissible as well.
```

However generic DSD does not itself provide:

```text
complex Hilbert positive cones
quantum tensor products
an arbitrary ancillary family
Phi tensor id as the mandatory local extension rule
```

so generic DSD does not imply quantum complete positivity.

## 5. Quantum specialization interface

Define

```text
ACE-QM  Ancilla-Compatible Extension
```

for a quantum specialization as follows.

For every admitted ancillary system \(B\), every admitted joint positive state \(\rho_{AB}\), and every declared local map \(\Phi_A\), the extension rule is

\[
\Phi_A\otimes\operatorname{id}_B
\]

and its output must remain an admitted positive joint state.

Within the supplied finite-dimensional Hilbert/tensor specialization, ACE-QM is exactly the complete-positivity requirement when the ancillary family is sufficiently complete. In particular, the standard Choi theorem shows that an ancilla with dimension equal to the input dimension suffices to test complete positivity.

Thus the conditional chain is

\[
\boxed{
\text{DSD whole-state dynamic admissibility}
+
\text{quantum composite/extension rule}
+
\text{ancilla closure}
\Longrightarrow
\text{CP admissibility}.
}
\]

The first ingredient is pre-existing DSD discipline. The Hilbert/tensor/ancilla ingredients are quantum-specialization data.

## 6. Provenance

Conservative classification:

```text
instantaneous-state admissibility along a declared trajectory     A  PRE_EXISTING_DSD
supplied dynamic law / constitutive bridge                         A  PRE_EXISTING_DSD
quantum Hilbert positive cone                                      SUPPLIED / C
quantum tensor composite                                           C/D from QM Core 004
ACE-QM arbitrary-ancilla extension requirement                     C  TARGET_SPECIALIZATION_SELECTOR
CP conclusion                                                      CONDITIONAL STANDARD-MATH CONSEQUENCE
```

Therefore this step does not count as an independent DSD derivation of complete positivity.

It does show that a pre-existing DSD rule — the requirement that the complete declared state remain admissible — naturally rejects a merely positive local map once the standard quantum composite structure is supplied.

## 7. Trace preservation remains separate

The transpose example is already trace-preserving, so its failure demonstrates that

\[
\boxed{
\text{positivity + trace preservation}\not\Rightarrow\text{CPTP}.
}
\]

Complete positivity and normalization preservation must therefore be audited separately.

QM Core 005B should test the conditions under which deterministic normalized-state evolution forces trace preservation and how selective operations/instruments require trace-nonincreasing branches whose sum is trace-preserving.

## 8. Reproducibility

```bash
python audits/science/2026-09-08_qm_core_005a_positive_vs_complete_positivity_gate.py --mode all
```

The script uses exact rational arithmetic for the Bell-state partial-transpose witness.

Expected summary:

```text
Bell projector has unit trace                                        PASS
partial transpose preserves trace                                    PASS
partial transpose has eigenvalue -1/2                                PASS
partial transpose is not positive semidefinite                       PASS
transpose Choi witness is negative                                   PASS
identity extension remains positive on control vector                PASS

OVERALL: PASS_WITH_REFINEMENT
```

## 9. Verdict

**PASS_WITH_REFINEMENT**

The isolated-system positivity criterion is strictly too weak for standard quantum composite dynamics. The transpose map gives an exact finite counterexample. Generic DSD does not supply complete positivity, but its pre-existing complete-state admissibility discipline combines cleanly with the supplied quantum composite/ancilla interface to recover CP as the correct conditional admissibility requirement.
