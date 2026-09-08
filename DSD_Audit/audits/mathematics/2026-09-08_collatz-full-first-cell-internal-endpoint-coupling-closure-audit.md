# DSD-AUDIT-20260908-MATH-036 — full-first-cell internal adjacent-block endpoint-coupling closure

Date: 2026-09-08

Verdict:

`CONFIRMED / FINITE ONLY / MECHANISM CLOSED THROUGH FIRST UNIVERSAL CROSSING`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Can the internal adjacent-block same-endpoint coupling mechanism be excluded throughout the entire first universal crossing, without upgrading that mechanism-specific exclusion into first-cell emptiness?

## DSD tuple

### D — Definition

First coefficient-crossing depth:

\[
A_0=114,208,327,604.
\]

Internal block boundaries are the 339 boundaries between top-address labels `1024..1363`.

The candidate predicate remains prefixwise coefficient survival in the current universal-spine route.

The audited mechanism is specifically:

> a candidate on one side of an internal top-address boundary and a candidate on the adjacent side reach the same endpoint at the same depth.

### R — Resolution

MATH-021 gives the necessary right-offset bound

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor.
\]

Hence the complete right-offset domain relevant through `A0` is

\[
0\le r\le R_*,
\qquad
R_*:=\left\lfloor\frac{A_0-1}{3}\right\rfloor
=\boxed{38,069,442,534}.
\]

This full finite domain was partitioned into contiguous non-overlapping shells and audited with a 64-bit interval-pruned exact generator.

### S — Selection

At prefix depth `k`, a low-prefix state `r0` is expanded only if an exact integer completion

\[
r=r_0+t2^k
\]

can fall in the target shell `[L,U]`.

This is a subtree exclusion by exact interval infeasibility, not a state merge.

Every accepted shell state is then continued exactly to depth 61 and passed into the already audited 22-step cyclic and base-independent continuation engine.

Complete aggregate depth-61 survivor count:

\[
\boxed{68,385,325}.
\]

Cumulative finite q support reaches `q61=54` with two states. This support is recorded as finite data only.

### E — Exclusion

Complete aggregate counts over `0..R*`:

\[
\boxed{7,225,448,447}
\]

exact depth-83 address states and

\[
\boxed{11,202,913,510}
\]

base-83+ 22-step threshold gates.

Every shell satisfies

\[
\boxed{\text{survive to audited end}=0},
\qquad
\boxed{\text{fixed-width endpoint overflow}=0}.
\]

Maximum failing-window base:

\[
\boxed{633}.
\]

After correcting witness bookkeeping so it tracks the current maximum base, the first audited deepest witness is

\[
\boxed{r=8,933,328,767,\qquad b=1251}.
\]

The failure in the gate based at 633 occurs by depth 655 at the latest.

The smallest positive depth-61-surviving right offset is

\[
\boxed{703}.
\]

Its earliest possible linear-halo entry is

\[
3\cdot703+1=\boxed{2110}>655.
\]

Thus every `r>=703` audited candidate loses coefficient survival before it can enter the necessary same-endpoint collision halo. Offsets `r<=702` do not survive through depth 61.

### T — Transition

The transition chain is:

1. exact bounded binary lifting;
2. exact interval-feasibility pruning;
3. deterministic completion to depth 61 after the selected finite bit width;
4. exact address lift;
5. 22-step cyclic coefficient gate;
6. exact endpoint propagation via two audited 11-step affine updates;
7. base-independent 22-step critical-prefix gates thereafter.

No truncated endpoint state is propagated as if it were the full endpoint.

### C — Consistency

The shell partition is exactly contiguous from `0` through `R*`.

Aggregate post-audit checks:

- depth-61 survivors = `68,385,325`;
- depth-83 states = `7,225,448,447`;
- 22-step gates = `11,202,913,510`;
- maximum failing base = `633`;
- maximum observed finite q support = `54`;
- every shell survivor/overflow result = `0/0`.

The aggregate arithmetic satisfies

\[
R_*=\left\lfloor\frac{A_0-1}{3}\right\rfloor.
\]

The post-audit initially contained a wrong final comparison `3R*+1>A0`; this was rejected and corrected to the exact identity

\[
3R_*+1=A_0-1.
\]

That correction changed no shell result or mechanism conclusion.

A separate small-depth certificate checks `k=1..60`. It enumerates exactly `1,352,610` boundary/offset combinations satisfying the necessary displacement range and finds

\[
\boxed{0}
\]

joint coefficient-surviving pairs.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / FINITE ONLY / MECHANISM CLOSED`.

Exact conclusion:

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate coupling for }
1\le k\le A_0
}
\]

within the current universal-spine/coefficient-survival scope.

### O — Outcome

Established:

- complete finite collision-halo domain through the first crossing identified as `R*=38,069,442,534`;
- entire domain audited without gaps;
- 68,385,325 depth-61 right-offset survivors processed;
- all relevant continuation shells terminate before halo entry;
- small depths `1..60` independently contain no joint coefficient-surviving boundary pair;
- internal adjacent-block same-endpoint coupling mechanism closed through the first universal crossing.

Not established:

- first-cell candidate emptiness;
- exclusion of candidates that do not rely on cross-boundary endpoint coupling;
- arbitrary later Farey cells;
- Collatz.

## Implementation audit

Two implementation findings were material and were corrected before this verdict:

1. the finite q support expanded from 52 to 53 and then 54 as the right-offset domain grew, so empirical support was not allowed to become a fixed type bound;
2. shell witness bookkeeping historically recorded base-545 witnesses even when a shell's deepest base was larger. The deepest numeric values were unaffected, but those witness labels were discarded and the tracker was corrected. Both base-633 shells were rerun, yielding the corrected first deepest witness `(8,933,328,767,1251)`.

## Prohibited upgrades

Do not infer:

- mechanism closure ⇒ first-cell emptiness;
- first-crossing mechanism closure ⇒ all later cells;
- finite maximum failing base 633 ⇒ universal lifespan theorem;
- endpoint-coupling exclusion ⇒ Collatz candidate exclusion in general;
- this result ⇒ proof of Collatz.

## Reproducibility

Math-verification:

- `collatz/src/2026_09_08_interval_pruned_64bit_tail22_shell_engine.cpp`
- `collatz/src/2026_09_08_full_first_cell_small_depth_boundary_certificate.cpp`
- `collatz/results/2026-09-08-full-first-cell-internal-boundary-shell-results.csv`
- `collatz/src/2026_09_08_full_first_cell_internal_endpoint_coupling_postaudit.py`
- `collatz/notes/2026-09-08-full-first-cell-internal-endpoint-coupling-closure.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-036`
