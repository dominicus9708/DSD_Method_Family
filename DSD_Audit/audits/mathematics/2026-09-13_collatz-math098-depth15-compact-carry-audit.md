# DSD Audit — Collatz MATH-098 root-sharded compact-carry depth-15 closure

Date: 2026-09-13

Status: `PASS / t=15 BELLMAN-SAFE / 7<=t<=14 OPEN`

## 1. Scope

MATH-098 applies the MATH-096 finite normalized carry state to macro depth 15, with the phase search restricted by a backward address-forgotten lower-envelope corridor and the exact address computation partitioned into 84 independent first-root shards.

## 2. Phase corridor

The phase corridor is computed after forgetting address and retaining the least accumulated penalty on each phase cell.  It is therefore an over-approximation of actual dangerous same-integer paths.  An actual negative path cannot be lost by intersecting with this corridor.

`PASS`.

## 3. Root sharding

Every actual first-macro compact state intersecting the danger corridor is assigned to one of 84 explicit root shards.  Shards are processed independently and are not assumed disjoint later in the dynamics.

No cross-root deduplication is performed.  Thus overlap causes duplicate verification only; it cannot remove an integer or a future state.

`PASS`.

## 4. Compact address sufficiency

Each shard retains exact `M,H,phase_id` and the MATH-096 finite address pair

\[
X=3^{-Q}B\bmod2^{73+R},\qquad G=3^{-Q}\bmod2^{73+R},
\]

where `R=ceil(log2 M)`.  MATH-096 proves this precision sufficient for all later one-paid compatibility tests, and MATH-092 supplies the exact transition.

`PASS`.

## 5. Terminal danger threshold

The strict one-paid penalty lower bound `p>1/9` implies that at macro depth 15 any Bellman-negative terminal must have

\[
z=h-R\ge45.
\]

MATH-098 uses this as a necessary condition only.  All other terminal edges are analytically safe and need no address test.

`PASS`.

## 6. Exact finite result

Across all 84 shards there are 145,075,745 phase-compatible terminal edge attempts satisfying `z>=45`.  Exact normalized address testing finds zero with `r<M`.

The global minimum residue gap is

\[
r-M=25,366,468>0.
\]

Hence no numerical-boundary ambiguity is involved.

The aggregate parent-occurrence count includes intentional cross-root duplicates and is not promoted to a unique-state count.

`PASS`.

## 7. Claim boundary

The valid conclusion is

\[
\boxed{t=15\text{ Bellman-safe}.}
\]

Do not infer:

- Bellman safety `=>` ordinary descent for every terminal integer;
- root-shard overlap `=>` statistical independence;
- phase-corridor pruning `=>` address information is dispensable;
- `t=15` closure `=>` closure of all one-paid chains or of the first universal cell.

The unresolved detailed one-paid band is

\[
\boxed{7\le t\le14.}
\]

## 8. Verdict

`PASS`.

MATH-098 confirms that the carry/address channel identified by MATH-095 is not merely necessary in principle; when retained in the compact MATH-096 state, it eliminates every phase-danger terminal at macro depth 15.
