# PHY-QM-034~037 — Error Correction, Pointer Selection, Observer Access, and Local Causality

Date: 2026-09-06

Status: PASS_WITH_BOUNDARY

## PHY-QM-034 — Physical error versus logical information loss

Use the three-qubit repetition code for a single bit-flip error only:

`|psi_L> = alpha|000> + beta|111>`.

The stabilizers `Z1 Z2` and `Z2 Z3` distinguish the four relevant error classes:

- no error: `(+1,+1)`
- `X1`: `(-1,+1)`
- `X2`: `(-1,-1)`
- `X3`: `(+1,-1)`

Applying the corresponding correction recovers the encoded state with fidelity 1 in the exact control.

DSD verdict:

`local physical corruption` does not imply `logical property loss` when the retained code/support structure and a valid recovery map are supplied.

The code is deliberately narrow: it corrects one Pauli-X error. It is not a universal one-qubit error or erasure code. Hence the result is a witness for layered recoverability, not a universal protection theorem.

This supplies an external quantum example of a distinction already important in DSD: reduced/local failure and complete-structure failure are not identical.

## PHY-QM-035 — Pointer basis is dynamically selected, not named into existence

Use the dephasing channel

`rho_01 -> gamma rho_01`, `rho_10 -> gamma rho_10`,

with diagonal entries unchanged. On the Pauli operator basis its eigenvalues are

- `I -> 1`
- `Z -> 1`
- `X -> gamma`
- `Y -> gamma`.

For `gamma=0.3`:

- `D(|0><0|, E(|0><0|)) = 0`
- `D(|+><+|, E(|+><+|)) = 0.35`.

Thus the Z eigenstates are stable under this supplied environment interaction, while phase-sensitive X/Y components decay.

DSD verdict:

A property label such as `pointer`, `stable`, or `classical` does not determine the selected basis. The basis emerges only after a quantum dynamical bridge is supplied.

This agrees with the general DSD Property boundary: names and typed property declarations do not by themselves determine constitutive/dynamical laws.

## PHY-QM-036 — Wigner-friend-style local/global distinguishability without interpretation claims

Compare

`rho_coh = |Phi+><Phi+|`,

where `|Phi+>=(|00>+|11>)/sqrt(2)`, with the incoherent record mixture

`rho_mix = 1/2 |00><00| + 1/2 |11><11|`.

The local reduced record state is identical:

`D(rho_F^coh, rho_F^mix)=0` up to floating-point error.

But globally

`D(rho_coh, rho_mix)=1/2`.

A global Bell-coherence test gives

- coherent case: `P(Phi+)=1`, `P(Phi-)=0`
- mixture: `P(Phi+)=1/2`, `P(Phi-)=1/2`.

DSD verdict:

`same observer-local description` does not imply `same complete structural state`.

The example is intentionally interpretation-neutral. It does not decide whether collapse is fundamental or effective. It only demonstrates that an observer-accessible reduced algebra/projection can identify states that remain distinguishable by a larger allowed operation class.

This is a direct quantum witness for DSD descriptive projection / latent structural distinction.

## PHY-QM-037 — Local CPTP operation and operational no-signalling

Take a Bell pair and apply an amplitude-damping CPTP map on subsystem A only. For `gamma=0.3`, the reproducibility control gives

`rho_B(before)=I/2`,

`rho_B(after)=I/2`,

with trace distance 0.

This is the standard unconditioned local-channel no-signalling structure: a trace-preserving local operation on A cannot by itself change the reduced state seen at B.

Conditional/postselected branches remain a different object and may change Bob's conditional state once the branch information is supplied; this does not make the unconditioned channel a superluminal signalling protocol.

DSD verdict:

Do not identify any of the following:

- entanglement,
- conditional remote-state update,
- no-signalling,
- finite propagation speed,
- `c_info`.

The first three are quantum-statistical/operational structures; `c_info` belongs only to a DSD dynamical specialization that also supplies localization, metric time, discrepancy support, and an evolution law.

## Combined methodological result

PHY-QM-034~037 adds four independent axes to the DSD quantum interface:

1. recoverability under an explicit error model;
2. dynamical selection of a stable property basis;
3. dependence on the allowed observer/readout algebra;
4. operational no-signalling under local trace-preserving operations.

None of these is reducible to readout injectivity alone.

## Reproducibility

```bash
python audits/science/2026-09-06_quantum_relativistic_expansion_batch.py --mode qec
python audits/science/2026-09-06_quantum_relativistic_expansion_batch.py --mode pointer --gamma 0.3
python audits/science/2026-09-06_quantum_relativistic_expansion_batch.py --mode wigner
python audits/science/2026-09-06_quantum_relativistic_expansion_batch.py --mode nosignal --gamma 0.3
```

## External references

- Knill, E. & Laflamme, R. (1997), *Theory of quantum error-correcting codes*, Phys. Rev. A 55, 900.
- Zurek, W. H. (1981), *Pointer basis of quantum apparatus*, Phys. Rev. D 24, 1516.
- Zurek, W. H. (2003), *Decoherence, einselection, and the quantum origins of the classical*, Rev. Mod. Phys. 75, 715.
