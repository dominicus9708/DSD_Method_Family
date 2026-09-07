# DSD Audit — Collatz depth-72 internal-boundary endpoint exclusion

- **Audit ID:** `DSD-AUDIT-20260908-MATH-015`
- **Date:** 2026-09-08
- **Target:** MATH-005 internal boundary halos inside the current 61+11 window
- **Verdict:** `FINITE ONLY / EXACT DEPTH-72 INTERNAL-BOUNDARY EXCLUSION`
- **Collatz status:** `OPEN`

## Claim under audit

Do any two universal-spine candidate starts lying on opposite sides of one of the 339 internal `2^61` block boundaries reach the same shortcut-map endpoint at a common depth `k<=72`?

## Complete finite search envelope

For a length-k word with q odd bits,

\[
T^k(N)=\frac{3^qN+C}{2^k}
\]

and the normalized correction satisfies

\[
\frac{C}{3^q}<2^{k-q}\left(1-\left(\frac23\right)^q\right)<2^{k-q}.
\]

MATH-004 supplies equal q for same-endpoint candidate states. Coefficient survival at depth72 gives

\[
q\ge46.
\]

Therefore every positive integer start displacement of a possible same-endpoint pair at depth72 obeys

\[
\boxed{d\le2^{26}-1=67{,}108{,}863.}
\]

This supplies a complete finite halo for the depth-72 question.

## Boundary coordinates

With

\[
W=2^{61},\qquad B=bW,
\]

write

\[
N_-=B-\ell=(b-1)W+(W-\ell),
\]

\[
N_+=B+r=bW+r.
\]

The first 61 steps depend only on `W-l` and `r`. The final 11 steps are evaluated with the exact address lifts `(b-1)3^q` and `b3^q` for every internal boundary

\[
b=1025,\ldots,1363.
\]

## Exact results

Within the complete `2^26-1` local halo:

- lower-61 right universal-spine survivors: `120,566`;
- lower-61 left universal-spine survivors: `120,071`;
- internal boundaries scanned: `339`;
- depth-72 surviving right evaluations across all boundaries: `22,527,308`;
- depth-72 surviving left evaluations across all boundaries: `22,306,426`;
- exact cross-boundary endpoint equalities at depth72: `0`.

The lookup compared exact depth-72 endpoints even without requiring equal q in the key.

Because the shortcut map is deterministic, a merger at any earlier common depth `k<=72` would persist to depth72. Hence

\[
\boxed{\text{no internal adjacent-block endpoint merger occurs through depth72}.}
\]

## DSD tuple

### D — Describability

Block address, signed boundary offset, lower-61 endpoint, odd count, lifted endpoint, and final endpoint are represented separately.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### R — Resolution

All integer offsets in the complete fixed-depth halo and all 339 internal boundaries are covered exactly. Every prefix-survival condition through depth72 is checked.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### S — Selection

Only universal-spine candidate states survive the prefix coefficient gate.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### E — Exclusion

All internal cross-boundary endpoint mergers through depth72 are excluded by exact exhaustive intersection.

Status: `ESTABLISHED_WITHIN_SCOPE / FINITE ONLY`.

### T — Transition

The first 61 steps are evaluated in boundary-local lower-residue coordinates. The address-dependent 11-step tail uses the exact affine lift.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### C — Consistency

The certificate uses exact integer arithmetic only. The displacement halo follows from the already audited same-q endpoint lock plus the elementary correction envelope.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### N — Norm

The conclusion is finite in depth. No extrapolation past 72 is licensed.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### O — Outcome

`FINITE ONLY / EXACT DEPTH-72 INTERNAL-BOUNDARY EXCLUSION`.

MATH-005's internal halo synchronization is unnecessary for endpoint merging inside the present 61+11 window. Deeper halo coupling remains open.

## Prohibited upgrades

- No merge through depth72 does not imply no merge later.
- Do not mark the full MATH-005 first-cell halo problem closed.
- Endpoint block-locality does not imply every other proof condition is block-local.
- No first-cell or Collatz closure follows.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_depth72_internal_boundary_endpoint_exclusion_certificate.cpp`

Certificate commit:

`656509a9ad6eb83ca7fb3f97174d0d12096e8855`

Explanatory note:

`collatz/notes/2026-09-08-depth72-internal-boundary-endpoint-exclusion.md`

Note commit:

`06def339d2983260a7a6587de4c2cb4eeb7eaba5`
