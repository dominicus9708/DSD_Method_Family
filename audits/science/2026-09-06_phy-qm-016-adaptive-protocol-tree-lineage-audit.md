# PHY-QM-016 — Adaptive protocol tree and branch-lineage audit

Date: 2026-09-06

## Question
Is an ordered list of measurements sufficient when a later operation is chosen conditionally from earlier classical outcomes?

## External quantum specialization
Initial state:

\[
\rho_0=|0\rangle\langle0|.
\]

Step 1: projective X measurement.

Step 2 policy:

- if the first outcome is \(+1\), measure Z;
- if the first outcome is \(-1\), measure X again.

Thus the second instrument is a function of the preceding history.

## Exact branch weights
The finite tree has nonzero histories

\[
(+1,Z,+1),\quad(+1,Z,-1),\quad(-1,X,-1)
\]

with probabilities

\[
1/4,\quad1/4,\quad1/2,
\]

respectively. The branch weights sum to one.

## Protocol representation
For an n-step adaptive quantum protocol, a compact representation is

\[
h_k=(x_1,a_1;\ldots;x_k,a_k),
\]

with policy

\[
x_{k+1}=\pi_{k+1}(h_k).
\]

If \(\mathcal I^{(k)}_{a_k|h_{k-1}}\) is the chosen outcome-indexed quantum instrument, then the unnormalized branch state is

\[
\widetilde\rho_{h_n}
=
\mathcal I^{(n)}_{a_n|h_{n-1}}
\circ\cdots\circ
\mathcal I^{(1)}_{a_1}(\rho_0),
\]

and

\[
p(h_n)=\operatorname{Tr}\widetilde\rho_{h_n}.
\]

## DSD interpretation
An adaptive protocol is not faithfully represented by

\[
\{\mathcal I_1,\ldots,\mathcal I_n\}
\]

or even by one fixed ordered list. It requires a history-indexed branching relation or decision tree.

This matches the current Structural Reorganization Dynamics, where a hybrid transition is relation-valued, branching is allowed, and lineage data are retained whenever identity succession is claimed.

## Audit verdict
- Unordered operation set is sufficient: **FAIL**.
- One fixed ordered list is sufficient for adaptive protocols: **FAIL**.
- History-indexed protocol tree is sufficient for the finite witness: **PASS**.
- DSD core dynamics must be rewritten: **NO**; its relation-valued transitions and lineage structure already admit this specialization.

## Consequence for the quantum DSD interface
A safer protocol coordinate is

\[
\boxed{
\mathfrak P
=
(\text{root state},\text{history set},\text{policy},\text{instrument family},\text{conditioning rules})
}
\]

rather than a measurement-name list.

## Reproducibility

```bash
python audits/science/2026-09-06_sequential_quantum_instrument_dsd_order.py
```
