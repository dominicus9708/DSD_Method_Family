# DSD-AUDIT-20260908-MATH-021 — Collatz depth-local linear collision halo / depth-2109 internal-boundary exclusion

Date: 2026-09-08

Verdict:

`CONFIRMED / ESTABLISHED_WITHIN_SCOPE / COMPUTATIONAL-STRUCTURAL ACCELERATION`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Claim under audit

For candidate-language internal adjacent-block starts sharing a depth-`k` endpoint, MATH-004 implies a same-`Q` correction identity.  Writing the start displacement as

\[
d=N_R-N_L>0,
\]

the normalized corrections satisfy

\[
d=S_L-S_R.
\]

Universal-spine correction control gives

\[
0<S_R,
\qquad S_L\le Q/3,
\]

hence

\[
\boxed{0<d<Q/3\le k/3}.
\]

Therefore a collision-complete depth-local search needs only

\[
\boxed{d\le\lfloor(k-1)/3\rfloor}.
\]

For a right start near an internal boundary,

\[
N_R=b2^{61}+r,
\]

the first 61 parity decisions depend only on `r`.  Exact finite prefix audit at the frozen published floor finds

\[
\boxed{r_{\min}^{(61)}=703},
\]

meaning all right offsets `0..702` fail the candidate coefficient prefix by or before depth 61, while `r=703` is the first survivor.

Combining the two facts yields

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate pair for }61\le k\le2109.
}
\]

## DSD tuple

### D — Definition

The audited object is narrowly defined:

- internal boundaries `b=1025..1363` between the 340 current top-address blocks;
- candidate-language universal-spine starts;
- equality of a common depth-`k` endpoint;
- ordinary positive integer lineage preserved.

This does not audit all possible candidate states or outer-window competitors.

### R — Resolution

Earlier finite calculations used an arithmetic-credit halo such as

\[
2^{k-q_{\min}(k)}-1.
\]

That resolution is safe but unnecessarily fine for the equality event under audit.

The exact collision variable is the ordinary start displacement `d`, and MATH-004 reduces the required resolution to

\[
\lfloor(k-1)/3\rfloor.
\]

This is an exact reduction, not a heuristic truncation.

### S — Selection

A state enters the collision search only if it remains in the audited coefficient-survival candidate language.

For the first 61 steps, the exact published-floor threshold

\[
(3+2^{-71})^q>2^k
\]

was compared by integer arithmetic with the simpler `3^q>=2^k` threshold.  Their minimum integer `q` agrees at every depth `1..61` used by the finite obstruction.

### E — Exclusion

Exhaustive finite scan gives:

- no `r=0..702` survives every required prefix through depth 61;
- `r=703` does survive.

Prefix failure is irreversible for candidate-language membership, so these excluded states cannot re-enter at later depth.

### T — Transition

For `61<=k<=2109`, any collision would require

\[
r\le d<k/3\le703.
\]

At the upper endpoint the inequality is strict, so `r<=702`.

The depth-61 exclusion therefore transfers legally to every depth in the interval.

At depth 2110 the linear halo first permits `r=703`; the transfer stops there.  No extrapolation beyond that boundary is made.

### C — Consistency

The result is consistent with MATH-015–020.

Those audits scanned much larger halos and found no internal endpoint collision through depth 81.  MATH-021 explains that equality could only have occurred in a tiny subset of those halos, where the right candidate side is already empty.

No previous correct result is invalidated; the computational architecture is sharpened.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE`

The algebraic reduction is exact in the audited candidate endpoint-fiber scope.  The `r_min=703` component is exact finite computation.  The composed depth interval is an exact logical consequence of these two inputs.

It is not promoted to a proof of the Collatz conjecture or of first-cell emptiness.

### O — Outcome

Closed in scope:

1. exponential-sized depth-local endpoint collision halos are unnecessary;
2. collision search radius is linear in depth;
3. internal adjacent-block same-endpoint coupling is excluded for every depth `61..2109`;
4. the next new right-offset shell begins exactly at depth 2110 with `r=703`.

Open:

1. same-block candidate structure;
2. outer-window competitors;
3. internal-boundary behavior from depth 2110 onward;
4. first universal cell;
5. Collatz conjecture.

## Prohibited upgrades

Do not infer:

\[
\text{no internal endpoint coupling}\Rightarrow\text{no candidate integers}.
\]

Do not infer:

\[
61\le k\le2109\text{ exclusion}\Rightarrow\text{all depths}.
\]

Do not transfer the linear endpoint halo automatically to unrelated full-Hensel or terminal-correction constraints.

Do not use the result to exclude outer-window competitors.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_depth_local_linear_collision_halo_certificate.py`

Math-verification explanatory note:

`collatz/notes/2026-09-08-depth-local-linear-collision-halo-and-2109-exclusion.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-021`
