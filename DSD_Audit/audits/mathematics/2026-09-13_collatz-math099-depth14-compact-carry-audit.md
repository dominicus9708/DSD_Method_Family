# DSD Audit — Collatz MATH-099 root-sharded compact-carry depth-14 closure

Date: 2026-09-13

Status: `PASS / t=14 BELLMAN-SAFE / 7<=t<=13 OPEN`

## 1. Scope

MATH-099 applies the already-audited MATH-096/098 compact carry architecture to macro depth 14.  The claim is Bellman/reduced-cost safety of every singleton handoff at this macro depth.

## 2. Phase over-approximation

The backward phase corridor is constructed after forgetting exact dyadic address and retaining the minimum penalty on each phase cell.  This enlarges the possible danger language.  Restoring only actual states whose exact phase interval intersects the corridor cannot omit an actual negative path.

`PASS`.

## 3. Independent root shards

All 125 actual first-macro danger roots are processed separately.  No assumption of disjointness or independence is made.  Downstream overlap produces duplicate work only.

`PASS`.

## 4. Exact address state

Each shard retains exact `M,H,phase-id` and

\[
X=3^{-Q}B\bmod2^{73+R},\qquad
G=3^{-Q}\bmod2^{73+R},
\]

with `R=ceil(log2 M)`.  MATH-096 proves this precision sufficient and MATH-092 supplies the exact transition.

`PASS`.

## 5. Terminal necessary condition

Since every one-paid macro pays strictly more than `1/9`, any negative depth-14 terminal must satisfy

\[
z=h-R\ge42.
\]

MATH-099 uses this only to discard analytically safe terminal edges.

`PASS`.

## 6. Complete result

Across all root shards, 343,241,144 phase-compatible terminal attempts satisfy `z>=42`.  Exact carry/address testing finds zero with `r<M`.

The smallest residue gap is

\[
r-M=4,352,816>0.
\]

Therefore no boundary equality or integer-rounding ambiguity is present.

`PASS`.

## 7. Claim boundary

The valid conclusion is

\[
\boxed{t=14\text{ Bellman-safe}.}
\]

Do not infer ordinary descent of every represented integer, full one-paid closure, first-cell emptiness, or the Collatz conjecture.

The unresolved detailed one-paid band is

\[
\boxed{7\le t\le13.}
\]

## 8. Verdict

`PASS`.

MATH-099 supplies an independent second application of the MATH-096 compact carry state at a larger phase-danger workload, with exact same-integer compatibility eliminating every surviving terminal danger edge.
