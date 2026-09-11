# DSD Audit — Collatz MATH-071 r=14 adaptive AP-union closure

Date: 2026-09-12

Status: `SAFE FINITE CLOSURE OF r=14 / CLAIM BOUNDARY LOCKED`

## Audit target

MATH-071 claims only the following:

\[
\boxed{r=14\text{ is closed in the current first-cell multi-paid calculation}.}
\]

Together with earlier certificates:

\[
\boxed{r\ge14\text{ is closed}.}
\]

It does **not** claim closure of `2<=r<=13`, the first universal Farey cell, later Farey cells, or the Collatz conjecture.

## Exact workload

The unchanged MATH-065 source-lineage calculation gives

\[
1035=175\text{ cost-safe}+507\text{ singleton-resolution}+353\text{ critical}
\]

phase/address cells.

The lower-cost completed-cylinder workload is exactly

\[
\boxed{24,614,018\text{ branch nodes}},
\]

\[
\boxed{2,599,692\text{ negative-candidate AP cylinders}},
\]

\[
\boxed{10,691,937,078\text{ raw target occurrences}}.
\]

Maximum initial cylinder multiplicity:

\[
\boxed{171,785,639}.
\]

## Describability decomposition

MATH-071 must distinguish five different objects.

### A. Source cylinder

One exact dyadic same-integer source class produced by MATH-065.

### B. Ordinary-target AP representation

\[
P(a,b,m)=\{a+bk:0\le k<m\},\qquad b\text{ odd}.
\]

This is a finite exact representation of ordinary integers, not a density statement.

### C. AP-union normalization

Only APs on the identical

\[
(b,a\bmod b)
\]

grid may be merged, and only when parameter intervals overlap or are adjacent.

### D. Resource shard

A computational partition of the original source representation.  A shard is not a new mathematical hypothesis and carries no pruning meaning.

### E. Floor closure

A represented ordinary integer is closed only after its exact shortcut lineage reaches

\[
\le2^{71}.
\]

These five levels must never be conflated.

## Coverage audit

The exact source stream occupies only these five initial multiplicity regions:

| region | multiplicity support | cylinders | raw occurrences |
|---:|---:|---:|---:|
| A | `1..767077` | 2,598,422 | 5,455,767,618 |
| B | `1526617..2385912` | 856 | 1,673,761,049 |
| C | `4579851..7157735` | 344 | 1,968,444,716 |
| D | `13739556..16283918` | 20 | 311,052,788 |
| E | `17155074..171785639` | 50 | 1,282,910,907 |

Their cylinder counts and occurrence sums reproduce the complete exact workload with zero remainder.

Therefore the apparent gaps between these support regions contain no r=14 source cylinder.
They are not unsearched intervals.

## Transition audit

Because `b` is odd, writing

\[
k=\rho+2s
\]

fixes endpoint parity.

For an even base,

\[
T(a+b(\rho+2s))
=\frac{a+b\rho}{2}+bs.
\]

For an odd base,

\[
T(a+b(\rho+2s))
=\frac{3(a+b\rho)+1}{2}+3bs.
\]

Hence every parity child remains an exact AP.

Floor trimming is safe because `b>0`, so values already `<=2^71` form an initial parameter interval.

## Resource-shard audit

When a state representation becomes too large, MATH-071 bisects the original source set and audits both halves.

For a single AP it uses the exact identity

\[
P(a,b,m)
=P(a,b,m_1)\cup P(a+bm_1,b,m-m_1).
\]

Therefore:

- no target is discarded;
- no statistical independence is assumed;
- cross-shard overlap is harmless duplication;
- success of one shard is never extrapolated to another shard.

This is a computational resolution change only.

## Arithmetic audit

The upper-tail experiment exposed a fixed-width implementation issue: an intermediate affine coefficient can exceed unsigned 128-bit range.

The canonical MATH-071 verifier therefore uses arbitrary-precision integer arithmetic.

This repair is important:

\[
\text{fixed-width overflow}\neq\text{mathematical failure}.
\]

Wrapping, clipping, or silently dropping the state would be invalid.  Exact integer promotion is the accepted repair.

## Closure audit

The low/middle occupied regions close under exact AP-union propagation with refined source shards.
The largest certified closure sweep there is

\[
\boxed{479}.
\]

The newly completed upper regions give:

- region D: 20/20 source APs closed; maximum observed depth 438;
- region E: 50/50 source APs closed; maximum observed depth 421;
- largest multiplicity `171785639`: closed after exact parameter sharding.

No upper-tail result exceeds the lower/middle bound 479.

Therefore every negative-candidate r=14 source cylinder is closed to the frozen floor.

## Claim classification

### SAFE

\[
\boxed{r=14\text{ closed}}
\]

and, after combination with earlier certificates,

\[
\boxed{r\ge14\text{ closed}}.
\]

### OPEN

\[
\boxed{2\le r\le13}.
\]

Also OPEN:

- common depth/paid-count potential;
- mixed one-paid / multi-paid Bellman closure;
- genuinely aperiodic low-cost path;
- first universal Farey cell emptiness;
- later Farey cells;
- full Collatz conjecture.

### PROHIBITED UPGRADES

The following implications are invalid:

\[
r\ge14\text{ closed}\Rightarrow\text{all multi-paid layers closed},
\]

\[
\text{finite AP-family closure}\Rightarrow\text{universal Collatz descent},
\]

\[
\text{resource sharding works}\Rightarrow\text{multiplicity itself is a Lyapunov variable},
\]

\[
\text{paid-count frontier reduced}\Rightarrow\text{first-cell emptiness}.
\]

## Next DSD target

The intended comparison sample is now complete:

\[
\boxed{r=14,15,16,17}
\]

plus the earlier depth-41 finite-state calculation.

The next audit should compare what information each representation preserves and seek a common future-relevant state quantity linking at least:

\[
(k,q,r,u,\Omega,S,\text{dyadic resolution},\text{AP multiplicity}).
\]

Priority should be given to the hardest surviving/late-closing states rather than average states, because a common potential must control the extremal low-cost paths.
