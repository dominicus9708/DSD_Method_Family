# PHY-QM-019 — Local erasure, environment transfer, and accessibility scope

Date: 2026-09-06

## Question

If an outcome carrier is reset locally, has the information itself been physically destroyed?

## Explicit unitary control

Start from

\[
|\Phi^+\rangle_{SR}|0\rangle_E
=\frac{|000\rangle+|110\rangle}{\sqrt2}.
\]

Apply a SWAP between `R` and `E`. The result is

\[
|\Psi\rangle_{SRE}
=\frac{|000\rangle+|101\rangle}{\sqrt2}
=|0\rangle_R\otimes|\Phi^+\rangle_{SE}.
\]

The original carrier `R` has been reset to

\[
\rho_R=|0\rangle\langle0|.
\]

But the correlation has moved to the environment carrier `E`.

## Correlation transfer

The numerical control gives

\[
I(S:R)=0,
\qquad
I(S:E)=2\ \text{bits}.
\]

Applying the same SWAP again restores the original global state with fidelity

\[
F_{\rm reverse}=1.
\]

Therefore

\[
\boxed{\text{local carrier reset}\neq\text{global information destruction}.}
\]

## Reduced-description view

If `E` is not included in the accessible descriptor, the accessible `SR` state is

\[
\rho_{SR}
=\frac{I_S}{2}\otimes|0\rangle\langle0|_R.
\]

From that reduced viewpoint the original correlation appears absent. In the full `SRE` state it remains exactly recoverable.

This provides a sharp distinction among:

```text
carrier-local reset
correlation transfer
environment inaccessibility
global state destruction
```

Only the first two occur in the explicit unitary witness.

## Decoherence boundary

Standard decoherence theory models apparent loss of phase coherence through entanglement with environmental degrees of freedom and reduction to an accessible subsystem. Environment-induced decoherence can make reversal operationally infeasible while the larger closed-state model retains correlations. This audit does not promote practical recoverability to guaranteed global recoverability in every physical situation; the full dynamical model and accessible carrier set must be stated.

## DSD interpretation

For a DSD quantum specialization, accessibility is not one of the Property Axiom System's primitive assignment statuses. It is additional downstream data describing which carriers or lineage coordinates are available to a readout/protocol.

Thus one should distinguish

\[
\text{state/carrier existence}
\]

from

\[
\text{carrier included in current readout support}.
\]

A reduced projection that omits `E` is a descriptive coarse-graining. The SWAP itself is a physical transition. These are different operations and must not share one label such as `erasure` without qualification.

## Audit verdict

- `carrier reset => global information destruction`: **FAIL**.
- `inaccessible environment => information undefined`: **FAIL** as a general DSD-core identification.
- reduction/coarse-graining and physical transition can be represented separately: **PASS**.
- a claim of physical erasure must declare the subsystem/environment scope: **PASS**.

Verdict: **PASS_WITH_BOUNDARY**.

## External references

- W. H. Zurek, Rev. Mod. Phys. 75, 715 (2003).
- M. Schlosshauer, Rev. Mod. Phys. 76, 1267 (2005).

## Reproducibility

```bash
python audits/science/2026-09-06_quantum_record_decoherence_dsd.py --mode core
```
