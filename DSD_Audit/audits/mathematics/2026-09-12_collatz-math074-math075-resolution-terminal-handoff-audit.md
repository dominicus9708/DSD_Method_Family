# DSD audit — Collatz MATH-074/075 resolution and terminal handoff structure

Date: 2026-09-12

## Scope

Audit the combination of:

- MATH-072 analytic bridge between `S`, `Sigma`, `rho`, `u`, and `Omega`;
- MATH-073/074 dyadic source-resolution Bellman potential;
- MATH-075 finite one-paid terminal handoff audit through macro depth 4;
- MATH-051 bounded-carry Hensel dominance state;
- MATH-061 exact one-paid compatibility/address composition.

## 1. State-role separation

The address-like information must be split into two logically distinct channels:

\[
\mathcal A=(\mathcal A_{\rm compat},\mathcal A_{\rm dom}).
\]

`A_compat` is the exact dyadic endpoint/source information needed to decide whether a future macro congruence is legal.

`A_dom` is the relative Hensel-dominance information used to decide whether another fixed-d word can dominate a candidate. MATH-051 compresses this part by bounded carry and viable competitor subsets.

These channels are related but not interchangeable.

### Audit verdict

✅ Exact future macro legality requires `A_compat`.

✅ Bounded-carry state can compress `A_dom` within the MATH-051 audited fixed-d scope.

❌ It is not valid to discard `A_compat` merely because two candidate histories have identical carry subsets.

## 2. Resolution potential

For an exact source cylinder with `M` ordinary anchors define

\[
R(M)=\lceil\log_2 M\rceil.
\]

Appending `ell` exact shortcut bits leaves

\[
M'\le\left\lceil M/2^\ell\right\rceil,
\]

hence

\[
R'\le\max(0,R-\ell).
\]

With

\[
H_R=-\frac{19}{503}R,
\]

one obtains

\[
p-\frac{19}{503}\ell+H_R'-H_R
\ge
p-\frac{19}{503}(\ell-R)_+.
\]

### Audit verdict

✅ Every multi-source refinement with `ell<=R` is automatically Bellman-safe because `p>=0`.

✅ Any remaining negative reduced cost is localized to a terminal edge whose length exceeds the remaining resolution budget.

❌ This does not prove the terminal singleton descends.

## 3. Finite symbolic one-paid horizon

The one-paid catalogue has macro shortcut length at least 3. The audited pre-first-cell source range reaches singleton resolution by accumulated dyadic length 73.

Therefore a symbolic multi-source one-paid chain can contain at most

\[
\left\lfloor72/3\right\rfloor=24
\]

macros before the next compatible extension is singleton-resolved.

### Audit verdict

✅ The formerly described arbitrary-length symbolic one-paid problem has a finite symbolic horizon under the MATH-061 source ceiling.

❌ The ordinary integer trajectory after singleton handoff can still be arbitrarily longer; the 24-macro bound is not a Collatz trajectory-length bound.

## 4. Terminal audit through macro depth 4

Exact one-paid composition gives:

| depth | new singleton handoffs | multi-source survivors | unique terminal integers | max direct descent |
|---:|---:|---:|---:|---:|
| 2 | 1,137 | 11,389 | 576 | 71 |
| 3 | 11,511 | 85,803 | 6,562 | 202 |
| 4 | 76,585 | 442,957 | 46,845 | 185 |

Every audited terminal integer reaches the frozen floor `2^71`.

### Audit verdict

✅ Same-integer closure through the enumerated terminal sets is exact finite evidence.

❌ Depth-4 closure must not be upgraded to all one-paid chains.

## 5. Representation-growth diagnosis

Raw exact symbolic representations grow rapidly by macro depth 4 even though terminal states continually leave the symbolic system.

This is analogous to the representation-growth problem repaired in MATH-070 by banded AP union.

The correct next move is not deeper Cartesian composition. It is quotienting by future-complete compatibility coordinates and unioning phase intervals only where all exact future-relevant data agree.

### SAFE merge requirements

A merge may preserve:

- exact accumulated shortcut length/resolution;
- exact odd-count information needed for `3^Q mod 2^h` compatibility;
- exact dyadic target address needed for every admissible next macro;
- exact source information sufficient to reconstruct a terminal ordinary target;
- exact phase interval union within a compatibility-equivalent class;
- resolution height `R`;
- optional bounded-carry dominance data when used for exact pruning.

### PROHIBITED merges

- merge by phase interval alone;
- merge by the same `R` alone;
- merge by bounded carry while dropping dyadic compatibility address;
- merge AP multiplicity with source-anchor multiplicity as if they were the same quantity.

## 6. Current structural picture

The most promising future-complete factorization is

\[
\boxed{
\text{analytic }(S,\rho,\Omega)
\times
\text{resolution }R
\times
\text{dyadic compatibility}
\times
\text{Hensel dominance}.
}
\]

MATH-072 shows that the analytic coordinates are not independent:

\[
S=1+\Sigma-\rho,
\qquad
\rho=2^{-u}\Omega.
\]

MATH-074 shows that `R` supplies an exact Bellman potential component.

The unresolved design problem is therefore the smallest exact quotient for dyadic compatibility plus whatever Hensel-dominance state is genuinely necessary.

## 7. Current theorem boundary

✅ `r>=14` multi-paid layers are closed in the current first-cell paid-count calculation.

✅ one-paid terminal handoffs are directly closed through macro depth 4.

✅ symbolic one-paid horizon is finite at at most 24 macros under the audited source ceiling.

❌ macro depths 5..24 are not yet terminally exhausted.

❌ mixed one-paid/multi-paid compatibility is not globally closed.

❌ first universal Farey cell is still OPEN.

❌ Collatz conjecture is still OPEN.
