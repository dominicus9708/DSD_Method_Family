# PHY-QM-026 — Heterogeneous environment record-weight audit

## Status
PASS_WITH_BOUNDARY

## Scope
This audit does not identify DSD with Quantum Darwinism and does not claim a universal redundancy formula. It studies one explicit binary cq pointer-record specialization with conditionally pure product environment records.

Let the two pointer values be equiprobable and let environment unit i carry conditional pure states with overlap

\[
c_i=|\langle e_i^{(0)}|e_i^{(1)}\rangle|\in[0,1].
\]

For a fragment F whose conditional records factorize,

\[
C_F=\prod_{i\in F}c_i.
\]

For the cq state

\[
\rho_{SF}=\frac12\sum_{s=0,1}|s\rangle\langle s|\otimes|e_s^F\rangle\langle e_s^F|,
\]

the fragment mutual information is

\[
I_{QMI}(S:F)=H_2\!\left(\frac{1+C_F}{2}\right).
\]

The Helstrom minimum-error probability is

\[
e_F=\frac{1-\sqrt{1-C_F^2}}{2},
\]

and the corresponding binary accessible information in this symmetric specialization is

\[
I_{acc}(F)=1-H_2(e_F).
\]

## Additive record weight
Define

\[
w_i:=-\ln c_i.
\]

Then

\[
W_F:=\sum_{i\in F}w_i=-\ln C_F.
\]

Thus any fragment-overlap threshold C_F <= tau_delta becomes the additive threshold

\[
W_F\ge W_\delta,
\qquad
W_\delta=-\ln\tau_\delta.
\]

At delta=0.1 the solver gives

```text
QMI threshold overlap       tau_QMI = 0.367961307352785
QMI additive threshold      W_QMI   = 0.999777489404211
accessible threshold overlap tau_acc = 0.226435010274195
accessible additive threshold W_acc   = 1.485297305588193
```

The numerical closeness W_QMI ~ 1 at delta=0.1 is contingent and is not promoted to a DSD constant.

## DSD interpretation
The environment is no longer summarized by one fragment size m. The retained record is naturally support tagged:

\[
\{(i,w_i):i\in E\}.
\]

A fragment is sufficient only relative to a declared diagnostic and threshold. Therefore a safe downstream diagnostic is

```text
SUFFICIENT_FRAGMENT(F, diagnostic, delta)
```

rather than a universal statement that all fragments of a given cardinality are equivalent.

This matches the existing DSD rule that aggregate values do not reconstruct support-tagged component structure without an injectivity/reconstruction condition.

## Boundary
The additive reduction relies on conditional product records and the overlap product law. Correlated environment records, mixed conditional records, interacting fragments, or alternative objectivity diagnostics need separate bridges.

## Reproducibility

```bash
python audits/science/2026-09-06_quantum_darwinism_heterogeneous_fragments.py \
  --mode threshold --delta 0.1
```
