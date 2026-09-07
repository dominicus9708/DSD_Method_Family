# DSD-AUDIT-20260908-MATH-030 — Collatz cut-10 parallel-memory Pareto point

Date: 2026-09-08

Verdict:

`CONFIRMED / EXACT SCHEDULING OPTIMIZATION / COMPUTATIONAL ONLY`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

For the exact MATH-028/029 `RMAX=10^9` bounded-lift tree and a 16-worker execution model, what is the earliest cut depth that both supplies enough independent tasks and avoids a single DFS subtree whose exact work already exceeds the ideal total-tail/16 share?

## DSD tuple

### D — Definition

A cut-depth task is one exact coefficient-surviving prefix state at that depth.  Tail work is measured by exact bounded-lift branch attempts from that cut state through depth 61.

This is an algorithmic scheduling metric, not a Collatz invariant.

### R — Resolution

No mathematical state is coarsened.  Each task retains the full exact bounded-lift state and expands the same descendants as MATH-028/029.

Cuts 0..10 are audited at exact branch-attempt resolution.

### S — Selection

Cuts 0..7 expose fewer than 16 tasks.

The first candidate cuts with at least 16 tasks are:

| cut | tasks | maximum exact tail-subtree work |
|---:|---:|---:|
|8|19|27,928,598|
|9|38|17,725,864|
|10|64|10,943,447|

The total post-cut-10 tail work is

\[
187,063,811.
\]

### E — Exclusion

For 16 workers, the ideal equal tail share is

\[
187,063,811/16=11,691,488.1875.
\]

Thus cuts 8 and 9 retain a single task larger than the ideal share, while cut 10 does not:

\[
10,943,447<11,691,488.1875.
\]

Cuts below 8 do not expose 16 tasks at all.

Therefore cut 10 is the first audited cut removing this specific single-subtree lower-bound obstruction while maintaining at least 16 tasks.

### T — Transition

The cut-10 traversal performs `180` branch attempts before the cut and `187,063,811` after it, totaling

\[
\boxed{187,063,991},
\]

identical to MATH-028/029.

It reaches exactly

\[
\boxed{1,796,718}
\]

depth-61 leaves.

No mathematical pruning is introduced.

### C — Consistency

Maximum local DFS stack at cut 10 is `20`.  Therefore 16-worker algorithmic live-prefix storage is

\[
64+16\cdot20=384.
\]

Comparisons:

\[
286,693/384\approx746.60
\]

versus MATH-029 cut 24, and

\[
11,894,128/384\approx30,974.29
\]

versus the MATH-028 breadth-first peak.

These are state-storage ratios only.  They do not imply equal wall-clock speedups.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / COMPUTATIONAL SCHEDULING OPTIMIZATION`.

No new Collatz exclusion follows from the cut-depth choice itself.

### O — Outcome

Established:

- cut 10 is the first audited 16-worker cut satisfying the stated task-granularity criterion;
- exact branch-attempt total and depth-61 leaf count are preserved;
- algorithmic live-prefix storage is reduced to 384 states under the audited 16-worker model.

Still open:

- optimal cut for other worker counts or larger `RMAX`;
- address-label continuation bottleneck;
- right offsets above `10^9`;
- first-cell emptiness;
- Collatz.

## AP-2 / information-loss check

No quotient or state alias is used.  The optimization changes only task partition and traversal order.

## Prohibited upgrades

Do not infer:

- cut-10 scheduling optimum ⇒ universal optimum;
- state-storage reduction ⇒ Collatz candidate pruning;
- theoretical load criterion ⇒ exact wall-clock scaling;
- computational scheduling improvement ⇒ stronger first-cell theorem.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_cut10_parallel_memory_pareto_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-cut10-parallel-memory-pareto.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-030`
