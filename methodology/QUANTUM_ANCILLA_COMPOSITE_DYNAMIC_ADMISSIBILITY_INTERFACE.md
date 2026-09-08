# Quantum Ancilla / Composite Dynamic Admissibility Interface

Status: **methodology / target-specialization interface**  
Applies to: finite-dimensional quantum reconstruction audits after QM Core 004.

## 1. Purpose

This interface prevents an isolated-system positivity check from being mistaken for admissibility of a local quantum dynamics on declared composites.

## 2. Required declarations

```text
LOCAL_STATE_CARRIER
LOCAL_MAP
ANCILLA_FAMILY
COMPOSITE_CARRIER_RULE
LOCAL_EXTENSION_RULE
JOINT_ADMISSIBILITY_CONDITION
NORMALIZATION_STATUS
SELECTIVITY_STATUS
```

## 3. ACE-QM — Ancilla-Compatible Extension

For every admitted ancilla `B`, every admitted joint state `rho_AB`, and every declared local map `Phi_A`, require the declared local extension to act as

\[
\Phi_A\otimes\operatorname{id}_B
\]

and require the output to remain inside the admitted joint-state carrier.

Within the standard finite-dimensional Hilbert/tensor specialization, positivity of all such extensions is complete positivity.

## 4. Choi test

For a linear map

\[
\Phi:M_d(\mathbb C)\to M_{d'}(\mathbb C),
\]

the Choi operator is

\[
J(\Phi)
=(\Phi\otimes\operatorname{id}_d)(|\Omega\rangle\langle\Omega|).
\]

The standard Choi theorem gives

\[
\boxed{
\Phi\text{ completely positive}
\Longleftrightarrow
J(\Phi)\ge0.
}
\]

Thus a same-dimension ancilla is sufficient for the finite-dimensional exact test.

## 5. DSD provenance discipline

The following must not be conflated:

```text
A  DSD trajectory slices remain admissible
C  quantum positive-cone specialization
C/D quantum composite/tensor specialization
C  ACE-QM arbitrary-ancilla compatibility
```

The CP conclusion is a conditional consequence after the quantum-specific composite structure is supplied. It is not evidence that generic DSD independently derived quantum complete positivity.

## 6. Counterexample rule

When a candidate map is positive on isolated states, test it on at least one entangled composite before treating it as a quantum local dynamics.

The canonical finite witness is matrix transposition:

```text
T(X) = X^T
positive                       yes
trace-preserving               yes
completely positive            no
Bell-state partial transpose   negative eigenvalue -1/2
```

This witness rejects the implication

\[
\text{positive + trace preserving}\Rightarrow\text{CPTP}.
\]

## 7. Next dynamic gates

After ACE-QM, separate:

```text
DNP-QM  deterministic normalization preservation
SBN-QM  selective branch normalization / trace nonincrease
ISC-QM  instrument sum closure
REV-QM  reversible-channel specialization
SEM-QM  continuous-time semigroup specialization
```

Complete positivity and normalization preservation are logically distinct and should be audited in separate steps.
