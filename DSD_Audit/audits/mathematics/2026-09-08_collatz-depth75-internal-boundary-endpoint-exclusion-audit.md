# DSD Audit — Collatz internal-boundary endpoint exclusion through depth 75

- **Audit ID:** `DSD-AUDIT-20260908-MATH-016`
- **Date:** 2026-09-08
- **Target:** continuation of MATH-015 beyond the 61+11 window
- **Verdict:** `FINITE ONLY / EXACT DEPTH-75 INTERNAL-BOUNDARY EXCLUSION`
- **Collatz status:** `OPEN`

## Claim under audit

Do any universal-spine candidate starts on opposite sides of an internal `2^61` block boundary merge at a common shortcut-map depth `k<=75`?

## Complete displacement envelopes

For same-endpoint candidate states, MATH-004 supplies common q. The exact correction-credit envelope gives

\[
d<2^{k-q}\left(1-\left(\frac23\right)^q\right)<2^{k-q}.
\]

The audited complete halos are therefore:

- depth73: `qmin=47`, `D=2^26-1`;
- depth74: `qmin=47`, `D=2^27-1`;
- depth75: `qmin=48`, `D=2^27-1`.

## Exact checkpoints

### Depth73

- full halo retained;
- all 339 boundaries scanned;
- right surviving evaluations: `20,193,949`;
- left surviving evaluations: `19,985,263`;
- endpoint collisions: `0`.

### Depth74

The halo was doubled and the entire new shell was included.

- `D=134,217,727`;
- right surviving evaluations: `40,290,262`;
- left surviving evaluations: `39,979,477`;
- endpoint collisions: `0`.

### Depth75

- lower-61 right survivors in the complete halo: `241,066`;
- lower-61 left survivors: `240,441`;
- right surviving evaluations across all boundaries: `37,619,431`;
- left surviving evaluations: `37,318,039`;
- endpoint collisions: `0`.

Since the shortcut map is deterministic, any merger at a common earlier depth would persist to depth75. Therefore

\[
\boxed{\text{no internal adjacent-block endpoint merger occurs through depth75}.}
\]

## DSD tuple

### D — Describability

Depth, q-minimum, displacement halo, local lower-61 state, block address, and endpoint remain separate.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### R — Resolution

Every integer offset in the complete fixed-depth halo is covered. All 339 current internal block boundaries are scanned.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### S — Selection

Only states satisfying universal-spine coefficient survival at every prefix are propagated.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### E — Exclusion

All internal cross-boundary endpoint equalities through depth75 are excluded within the complete finite envelope.

Status: `ESTABLISHED_WITHIN_SCOPE / FINITE ONLY`.

### T — Transition

Exact lower-61 local states are lifted by the block address and propagated to the target depth with the ordinary shortcut map.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### C — Consistency

The zero-collision result survives a genuine radius expansion at depth74 from `2^26-1` to `2^27-1`; it is not merely a repeated scan of the old halo.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### N — Norm

The result is finite in depth. The next depth requires a new complete shell.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### O — Outcome

`FINITE ONLY / EXACT DEPTH-75 INTERNAL-BOUNDARY EXCLUSION`.

The endpoint-coupling-free window is extended from depth72 to depth75. The full first-cell halo problem remains open.

## Next boundary

At depth76,

\[
q_{\min}(76)=48,
\qquad
D_{76}=2^{28}-1.
\]

A depth76 claim requires the new shell to be included explicitly.

## Prohibited upgrades

- No merger through75 does not imply no merger later.
- Do not infer full MATH-005 halo emptiness.
- Do not infer a limiting/asymptotic law from the finite zero sequence.
- Do not infer first-cell or Collatz closure.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_depth75_internal_boundary_endpoint_exclusion_certificate.cpp`

Certificate commit:

`76ba15fe7eb9521fa17f554e912c7f6a155e08f0`

Explanatory note:

`collatz/notes/2026-09-08-depth75-internal-boundary-endpoint-exclusion.md`

Note commit:

`6ceffd01489d3d4997abffc0891486866185d47a`
