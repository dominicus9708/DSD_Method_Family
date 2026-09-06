# PHY-QM-027 — Global overlap versus redundancy obstruction

## Status
PASS — explicit counterexample

## Question
Does a global decoherence/record-overlap summary determine how many independently sufficient environment fragments exist?

## Normalized construction
Normalize the sufficient-fragment threshold to

\[
W_\delta=1.
\]

Consider two eight-unit environments with additive record weights.

### Distributed record

\[
w^{(A)}=(0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5).
\]

Then

\[
\sum_i w_i^{(A)}=4.
\]

The environment can be partitioned into four disjoint pairs, each with total weight 1, so

\[
R_{opt}^{(A)}=4.
\]

### Concentrated record

\[
w^{(B)}=(3.5,0.5,0,0,0,0,0,0).
\]

Again

\[
\sum_i w_i^{(B)}=4.
\]

Hence both environments have the same total conditional-overlap product,

\[
C_E=e^{-4}=0.0183156388887\ldots
\]

but only the first unit of B is individually sufficient and the residual weight is below threshold. Thus

\[
R_{opt}^{(B)}=1.
\]

## Result

\[
\boxed{
C_E^{(A)}=C_E^{(B)}
\quad\text{but}\quad
R_{opt}^{(A)}=4\ne1=R_{opt}^{(B)}.
}
\]

Therefore

\[
\boxed{
\text{global record/decoherence strength}
\not\Rightarrow
\text{redundancy distribution}.
}
\]

This is a support-distribution factorization obstruction: a scalar total cannot reconstruct where the record weight resides.

## DSD impact
The result is directly analogous to DSD static aggregation collisions: equal aggregates can arise from different support-tagged records. For Quantum Darwinism specialization, the environment support and per-fragment record strengths must be retained whenever redundancy or multi-observer accessibility matters.

This does not show that standard Quantum Darwinism uses the global overlap as its sole redundancy definition. It is a negative control against making that reduction inside the DSD specialization.

## Reproducibility

```bash
python audits/science/2026-09-06_quantum_darwinism_heterogeneous_fragments.py \
  --mode counterexample
```
