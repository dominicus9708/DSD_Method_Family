# PHY-QM-042~045 — Relative Entropy, Recovery, and Describability Audit

Date: 2026-09-07
Method: DSD analysis + DSD general audit
Status: PASS_WITH_BOUNDARY

## Scope
This batch treats quantum relative entropy and recoverability as externally supplied standard quantum-information structures. DSD does not derive the Umegaki/Araki relative entropy, the data-processing inequality, or Petz recovery.

## PHY-QM-042 — Data processing is a describability-loss witness, not an ontology-loss theorem
For faithful finite-dimensional states, use

D(rho||sigma) = Tr rho (log rho - log sigma).

Under a CPTP map Phi,

D(Phi(rho)||Phi(sigma)) <= D(rho||sigma).

Finite control in `2026-09-07_quantum_qft_modular_qrf_batch.py`:

D(rho||sigma) = 0.157511626439759 bits,
D(Delta rho||Delta sigma) = 0.031163445151860 bits

for Z-dephasing Delta.

Audit verdict:
- distinguishability available to the supplied readout/channel can decrease;
- this does not imply that the underlying global state ceased to exist;
- DSD should classify this as map-relative distinguishability loss unless an additional physical-erasure statement is proven.

## PHY-QM-043 — Recoverability is distinct from identifiability
The prior readout-fiber criterion asks whether Phi is injective on an admissible state class. Recovery instead asks whether, after applying Phi, there exists an allowed recovery map R such that R(Phi(rho)) reconstructs rho exactly or approximately on a specified family.

Therefore:

IDENTIFIABILITY != RECOVERABILITY.

A noninjective map can still be recoverable on a restricted code/model family, while a globally injective descriptive encoding may be operationally unrecoverable under a restricted protocol class.

## PHY-QM-044 — Equality/near-equality in data processing is a stronger condition than small output loss
Standard quantum information links equality in monotonicity to sufficient/recoverable channels (Petz-type recovery), while approximate equality is connected to approximate recovery bounds. DSD should not reduce this to a scalar `information lost` label; the domain family and allowed recovery map class must remain typed.

Recommended downstream profile:

RECOVERABILITY(
  state_family,
  channel,
  recovery_class,
  error_metric,
  tolerance
)

## PHY-QM-045 — Relative entropy is not a universal DSD scalar
Relative entropy depends on an ordered state pair, supplied algebra/representation, and domain conditions. In QFT it can remain meaningful where naive local density-matrix entropy is problematic, but this does not elevate it to a universal DSD measure of describability.

DSD consequence:
- retain relative entropy as a domain-specific diagnostic;
- do not identify `describability` with entropy or relative entropy;
- record whether a diagnostic is state-pair, algebra, region, channel, and observer/protocol dependent.

## General audit candidate extracted
1. Distinguish `compression/readout loss` from `physical destruction`.
2. Distinguish injectivity from recoverability.
3. Any scalar distinguishability measure must keep its domain, map, and comparison pair typed.
4. Equality conditions deserve a separate audit from generic inequalities.

## Reproducibility
Run from repository root:

```bash
python audits/science/2026-09-07_quantum_qft_modular_qrf_batch.py
```
