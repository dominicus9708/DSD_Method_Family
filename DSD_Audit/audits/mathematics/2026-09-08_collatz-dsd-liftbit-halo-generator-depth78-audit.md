# DSD Audit — Collatz lift-bit halo generator and internal-boundary exclusion through depth 78

- **Audit ID:** `DSD-AUDIT-20260908-MATH-017`
- **Date:** 2026-09-08
- **Target:** exact generation of fixed-depth internal-boundary halos and continuation of MATH-016
- **Verdict:** `CONFIRMED COMPUTATIONAL ACCELERATION / FINITE ONLY DEPTH-78 INTERNAL-BOUNDARY EXCLUSION`
- **Collatz status:** `OPEN`

## Claim under audit

Can the complete `2^m-1` boundary halo be generated without scanning every ordinary integer offset, while preserving exactly the lower-61 universal-spine states needed for the endpoint calculation? If so, does the resulting exact state set contain any internal adjacent-block endpoint merger through depth 78?

## Exact lift-bit descriptor

At depth `k`, let the canonical lower residue be `x_k`, with

\[
y=T^k(x_k),\qquad q=q_k.
\]

Choose the next binary lift bit

\[
e\in\{0,1\},\qquad x_{k+1}=x_k+e2^k.
\]

After the first `k` shortcut steps the lifted endpoint is exactly

\[
\boxed{z=y+e3^q.}
\]

Hence the next parity bit and state are

\[
\boxed{b=z\bmod2},
\]

\[
y'=T(z),\qquad q'=q+b.
\]

This state transition is exact and uses only the information required by the next step.

## Boundary halo constraints

For

\[
D=2^m-1,
\]

the right local offsets satisfy

\[
0\le r<D,
\]

so binary lift bits `e_m,...,e_60` are fixed to zero.

For the left side, with

\[
x=2^{61}-\ell,\qquad1\le\ell\le D,
\]

the same high lift bits are fixed to one.

Therefore only the first `m` lift bits branch; after that the lower-61 construction is deterministic. Coefficient-survival failure is applied immediately, so failed states are never expanded.

## Regression against prior exhaustive scans

The generator reproduces the already audited brute-force lower-61 halo counts exactly:

| `m` | right survivors | left survivors |
|---:|---:|---:|
| 22 | 7,376 | 7,741 |
| 26 | 120,566 | 120,071 |
| 27 | 241,066 | 240,441 |

Status: `ESTABLISHED_WITHIN_SCOPE`.

## New `m=28` complete halo

For depth 76 through 78,

\[
D=2^{28}-1=268{,}435{,}455.
\]

The exact generated lower-61 state counts are

\[
\boxed{481{,}570\text{ right}},
\qquad
\boxed{481{,}645\text{ left}}.
\]

This replaces an ambient scan of roughly `2^28` offsets per side by the exact surviving state set. The reduction is computational pruning, not a density theorem.

## Exact depth-78 endpoint audit

At depth 78,

\[
q_{\min}(78)=50,
\qquad
78-q_{\min}=28,
\]

so the `m=28` halo is complete for the same-endpoint displacement question.

All 339 internal block boundaries were scanned with the exact address lift and the tail propagated from depth 61 to 78.

Exact surviving evaluations:

- right: `64,370,400`;
- left: `64,259,236`.

Exact same-q endpoint intersections:

\[
\boxed{0}.
\]

MATH-004 supplies equal q for candidate states that share an endpoint. Since the shortcut map is deterministic, a common-depth merger at any earlier depth `k<=78` would persist to depth 78. Therefore

\[
\boxed{\text{no internal adjacent-block endpoint merger occurs through depth 78}.}
\]

## Depth-79 planning state

At depth79,

\[
q_{\min}(79)=50,
\qquad
D_{79}=2^{29}-1.
\]

The same exact generator gives the local lower-61 state counts

\[
964{,}227\text{ right},
\qquad
963{,}422\text{ left}.
\]

These are **planning counts only**. No depth-79 endpoint verdict is included in this audit.

## DSD tuple

### D — Describability

The raw integer offset is replaced by the exact transition state `(k,y,q,e)` plus the fixed halo-side high-bit rule.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### R — Resolution

The full `2^m-1` finite halo is represented exactly; no sampling or coarse residue substitution is used.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### S — Selection

Universal-spine coefficient survival is applied before expansion, so only states still relevant to the candidate language are retained.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### E — Exclusion

Failed lift states are discarded immediately. All internal adjacent-block endpoint equalities through depth78 are excluded in the complete finite envelope.

Status: `ESTABLISHED_WITHIN_SCOPE / FINITE ONLY`.

### T — Transition

The exact lift transition is `y -> y+e3^q` followed by one ordinary shortcut-map step. The block-dependent tail uses the exact affine address lift.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### C — Consistency

The generator reproduces prior brute-force counts at `m=22,26,27` before being used at the new `m=28` resolution. The depth78 endpoint intersection is exact integer arithmetic.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### N — Norm

The generator is an exact computational acceleration. The endpoint conclusion is finite in depth and must not be promoted to an asymptotic or universal statement.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### O — Outcome

`CONFIRMED COMPUTATIONAL ACCELERATION / FINITE ONLY DEPTH-78 INTERNAL-BOUNDARY EXCLUSION`.

The state-generation bottleneck is materially reduced. The next bottleneck is repeated block-dependent tail endpoint-set construction across 339 boundaries.

## Prohibited upgrades

- Do not read the state-count reduction as a Collatz density theorem.
- Do not infer zero collisions at depth79 from the planning counts.
- Do not infer no merger at arbitrary depth from no merger through78.
- Do not infer full MATH-005 halo emptiness.
- Do not infer first-cell or Collatz closure.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_dsd_liftbit_halo_generator_depth78_certificate.cpp`

Certificate commit:

`a39c5b6ce7b00aeea37bc33a8e978b8f86874760`

Explanatory note:

`collatz/notes/2026-09-08-dsd-liftbit-halo-generator-and-depth78-exclusion.md`

Note commit:

`a79012d505d82f66db7679a6c8fa2d6658edd9f6`
