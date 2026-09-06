# PHY-QM-015 — POVM readout vs instrument dynamics obstruction

Date: 2026-09-06

## Question
Does the POVM effect data of a measurement determine the postmeasurement dynamics strongly enough to determine later sequential statistics?

## External quantum specialization
Use the same first-step Z POVM

\[
E_{\pm}=P^Z_{\pm}.
\]

Compare two instruments implementing that same POVM.

Instrument L (Lüders):

\[
\mathcal I^{L}_{z}(\rho)=P^Z_z\rho P^Z_z.
\]

Instrument R (measure and reprepare in the X basis):

\[
\mathcal I^{R}_{+}(\rho)=\operatorname{Tr}(P^Z_+\rho)|+\rangle\langle+|,
\]

\[
\mathcal I^{R}_{-}(\rho)=\operatorname{Tr}(P^Z_-\rho)|-\rangle\langle-|.
\]

Both induce the same first-step outcome probabilities

\[
P(z)=\operatorname{Tr}(E_z\rho).
\]

## Exact finite witness
For initial state \(\rho_0=|0\rangle\langle0|\), both instruments give

\[
P(z=+1)=1,
\qquad P(z=-1)=0.
\]

Now perform an X projective measurement afterward.

For Instrument L:

\[
P(z=+1,x=+1)=P(z=+1,x=-1)=1/2.
\]

For Instrument R:

\[
P(z=+1,x=+1)=1,
\qquad
P(z=+1,x=-1)=0.
\]

Thus identical POVM readout at step one does not determine the sequential behavior.

## DSD interpretation
Let \(\Phi_{\rm POVM}\) be the one-step probability readout and \(\Phi_{\rm seq}\) the later sequential readout. Then there exist two measurement realizations \(I_L,I_R\) such that

\[
\Phi_{\rm POVM}(I_L)=\Phi_{\rm POVM}(I_R)
\]

but

\[
\Phi_{\rm seq}(I_L)\neq\Phi_{\rm seq}(I_R).
\]

Therefore no factorization

\[
\Phi_{\rm seq}=g\circ\Phi_{\rm POVM}
\]

exists over this realization family.

This is a direct compression obstruction: effect-level readout forgets state-update information required by later dynamics.

## Audit verdict
- POVM effects determine all later sequential statistics: **FAIL**.
- Same one-shot measurement statistics imply same measurement transition: **FAIL**.
- A dynamic quantum specialization needs quantum-instrument data, not only POVM effects, when postmeasurement state matters: **PASS**.
- DSD Property core must be changed: **NO**; the instrument is a downstream dynamic/physical specialization.

## DSD consequence
A safe bridge is

\[
\boxed{\text{measurement property/readout}\neq\text{measurement transition instrument}.}
\]

The Property Axiom System may type the observable/context/readout, while Structural Reorganization Dynamics or a quantum-specific dynamic extension carries the outcome-indexed transition maps.

## Reproducibility

```bash
python audits/science/2026-09-06_sequential_quantum_instrument_dsd_order.py
```
