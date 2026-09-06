# PHY-QM-020 — Continuous decoherence factor, distinguishability, and recoverability

Date: 2026-09-06

## Question

Can the difference between coherent, partially decohered, and fully decohered measurement-lineage states be quantified continuously rather than treated as a binary status?

## One-parameter family

Use the reduced `SR` family

\[
\rho_{SR}(\gamma)=\frac12
\begin{pmatrix}
1&0&0&\gamma\\
0&0&0&0\\
0&0&0&0\\
\gamma^*&0&0&1
\end{pmatrix},
\qquad |\gamma|\le1.
\]

For a pure environment-marking model, `gamma` is the overlap of the two environmental marker states:

\[
\gamma=\langle e_1|e_0\rangle.
\]

The two extreme controls are

\[
|\gamma|=1 \Rightarrow \text{coherent premeasurement},
\]

\[
|\gamma|=0 \Rightarrow \text{fully dephased reduced state}.
\]

## Visibility and which-way distinguishability

For this symmetric pure-marker control,

\[
V=|\gamma|,
\qquad
D=\sqrt{1-|\gamma|^2},
\]

so

\[
V^2+D^2=1.
\]

This is the saturated two-path complementarity relation for the chosen pure marker model; it is standard quantum mechanics, not a DSD-derived law.

## Recovery fidelity

For real nonnegative `gamma`, applying the inverse premeasurement CNOT and testing against the initial state `|+>|0>` gives

\[
\boxed{F_{\rm rec}(\gamma)=\frac{1+\gamma}{2}.}
\]

The joint mutual information is

\[
\boxed{
I(S:R)=2-H_2\!\left(\frac{1+|\gamma|}{2}\right)
}
\]

in bits.

Numerical controls:

| gamma | visibility | distinguishability | recovery fidelity | I(S:R) bits |
|---:|---:|---:|---:|---:|
| 1.0 | 1.000000 | 0.000000 | 1.000000 | 2.000000 |
| 0.8 | 0.800000 | 0.600000 | 0.900000 | 1.531004 |
| 0.5 | 0.500000 | 0.866025 | 0.750000 | 1.188722 |
| 0.2 | 0.200000 | 0.979796 | 0.600000 | 1.029049 |
| 0.0 | 0.000000 | 1.000000 | 0.500000 | 1.000000 |

## Conditional eraser response

If `R` is measured in the X basis, the conditional system state has off-diagonal magnitude

\[
\boxed{|(\rho_{S|R_X})_{01}|=\frac{|\gamma|}{2}.}
\]

Thus the later protocol response directly tracks the residual coherence parameter while the individual `S` and `R` marginals remain `I/2` for the whole family.

## DSD implication

This provides a useful separation between:

```text
carrier existence
carrier accessibility
coherence retained in the joint state
which-way distinguishability
future protocol recoverability
```

These are not one binary DSD status.

A coarse descriptor containing only local marginals has the entire gamma-family in one fiber, while a later conditional/reversal protocol distinguishes the family continuously. Hence the reduced descriptor fails the DSD factorization test for that downstream response.

## Audit verdict

- `coherent/decohered` should be represented only as a binary universal DSD status: **FAIL**.
- a downstream quantum specialization may attach a continuous coherence/recoverability coordinate: **PASS**.
- standard visibility/distinguishability relations are DSD axioms: **FAIL**.
- reduced marginals alone reconstruct recoverability: **FAIL**.

Verdict: **PASS_WITH_BOUNDARY**.

## External references

- B.-G. Englert, Phys. Rev. Lett. 77, 2154 (1996), fringe visibility and which-way information.
- W. H. Zurek, Rev. Mod. Phys. 75, 715 (2003), decoherence and environment-induced monitoring.
- M. O. Scully and K. Drühl, Phys. Rev. A 25, 2208 (1982), quantum eraser.

## Reproducibility

```bash
python audits/science/2026-09-06_quantum_record_decoherence_dsd.py \
  --mode gamma --gamma 1 0.8 0.5 0.2 0
```
