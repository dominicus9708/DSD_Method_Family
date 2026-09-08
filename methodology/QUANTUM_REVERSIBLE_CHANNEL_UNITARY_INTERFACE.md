# Quantum Reversible Channel / Unitary Interface

Date: 2026-09-08

## Purpose

This interface prevents three different notions from being conflated in DSD quantum specializations:

```text
ALGEBRAIC_INVERSE
STATE_SPACE_BIJECTION
PHYSICAL_CHANNEL_INVERSE
```

Only the last notion is sufficient for the standard finite-dimensional reversible-channel theorem.

## PCR-QM — Physical Channel Reversibility

For a deterministic quantum specialization on a fixed finite-dimensional system, declare a map

\[
\Phi:M_d(\mathbb C)\to M_d(\mathbb C)
\]

physically reversible only if:

```text
1. Phi is an admitted deterministic quantum channel.
2. There exists another admitted deterministic quantum channel Psi.
3. Psi o Phi = id on the complete declared state carrier.
4. Phi o Psi = id on the complete declared state carrier.
5. Both directions satisfy the same composite/ancilla admissibility discipline.
```

With the Hilbert/CPTP specialization supplied, the standard finite-dimensional theorem gives

\[
\boxed{
\mathrm{PCR\!-\!QM}
\Longrightarrow
\Phi(X)=UXU^\dagger
}
\]

for a unitary \(U\) when input and output system dimensions agree.

## Non-implications

Do not infer:

\[
\text{algebraic invertibility}
\Rightarrow
\text{physical reversibility},
\]

or

\[
\text{continuous DSD trajectory}
\Rightarrow
\text{unitary quantum dynamics}.
\]

A depolarizing channel with nonzero depolarizing parameter is a standard control: its linear superoperator is algebraically invertible, but the inverse need not be positive.

Likewise temporal lineage in DSD states succession but does not provide inverse dynamics.

## Distinguishability audit

If \(\Phi\) and \(\Psi\) are mutually inverse CPTP maps, contractivity in both directions forces

\[
\|\Phi(\rho)-\Phi(\sigma)\|_1
=
\|\rho-\sigma\|_1
\]

for every pair of states. Any strict distinguishability contraction is therefore sufficient to reject PCR-QM.

## Provenance

```text
transition/equivalence separation         A  PRE_EXISTING_DSD
normalization-functional preservation     B  GENERAL_OPERATIONAL_RESULT
Hilbert/CPTP carrier                      C  TARGET/SUPPLIED
PCR-QM                                    C  TARGET_SPECIALIZATION_SELECTOR
unitary conclusion                        CONDITIONAL STANDARD-QM THEOREM
```

This provenance must be retained in audits and synthesis documents so that a conditional unitary conclusion is not counted as an independent DSD derivation.
