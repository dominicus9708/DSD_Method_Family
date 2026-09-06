# PHY-QM-028 — Heterogeneous redundancy as a bin-covering problem

## Status
PASS_WITH_BOUNDARY

## Diagnostic being optimized
For a heterogeneous discrete environment, define the DSD audit diagnostic

\[
R_{\delta}^{\mathrm{disj,opt}}
:=
\max\{k:\exists\text{ pairwise-disjoint }F_1,\dots,F_k,
\;W(F_j)\ge W_\delta\}.
\]

After normalization by W_delta, each environment unit has nonnegative size

\[
a_i=w_i/W_\delta
\]

and each sufficient fragment must satisfy

\[
\sum_{i\in F}a_i\ge1.
\]

Maximizing the number of pairwise-disjoint sufficient fragments is therefore the standard bin-covering optimization form: partition items into as many bins as possible whose total size is at least the threshold.

This equivalence applies to this explicitly declared disjoint-fragment diagnostic. It is not claimed to replace all standard Quantum Darwinism redundancy conventions, which often use typical or averaged fragment information.

## Complexity boundary
Bin covering is the dual of bin packing and is computationally nontrivial/NP-hard in general. Therefore heterogeneous redundancy optimization need not collapse to one average fragment size.

## Exact finite witness
Use normalized weights

```text
[0.14, 0.58, 0.05, 0.18, 0.75, 0.09, 0.13, 0.14, 0.84, 0.21]
```

Total weight:

\[
W_{tot}=3.11,
\]

so the trivial capacity upper bound is

\[
R\le\lfloor3.11\rfloor=3.
\]

The exact bitmask solver finds three disjoint sufficient fragments:

```text
[2,7,8]   weight 1.03
[1,5,6,9] weight 1.01
[0,3,4]   weight 1.07
```

Hence

\[
\boxed{R_{\delta}^{\mathrm{disj,opt}}=3.}
\]

A deliberately simple largest-plus-smallest greedy control produces only two covered fragments:

```text
[8,2,5,6] weight 1.11
[4,0,7]   weight 1.03
```

Thus

\[
\boxed{R_{greedy}=2<R_{opt}=3.}
\]

## DSD interpretation
Once environment channels carry unequal descriptive/record weights, redundancy is not only a scalar aggregation problem. It is a support-aware allocation problem. The support retained by the DSD static layer therefore becomes operationally relevant rather than merely bookkeeping.

A safe record is

```text
ENV_RECORD = {(fragment_id, record_weight, access_metadata, ...)}
```

with any scalar redundancy computed downstream.

## Audit verdict
- `mean fragment size alone determines heterogeneous redundancy`: REJECTED.
- `total record weight always equals usable redundancy times threshold`: REJECTED as an equality; only an upper-bound type statement survives.
- `support allocation can change the exact number of sufficient disjoint fragments`: CONFIRMED.
- `heterogeneous exact redundancy can require combinatorial optimization`: CONFIRMED for the chosen diagnostic.

## Reproducibility

```bash
python audits/science/2026-09-06_quantum_darwinism_heterogeneous_fragments.py \
  --mode heterogeneous
```
