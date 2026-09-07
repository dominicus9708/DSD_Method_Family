# DSD-AUDIT-20260908-MATH-023 — Collatz lifespan phase-descriptor saturation

Date: 2026-09-08

Verdict:

`CONFIRMED / FINITE DIAGNOSTIC / STRATEGY SATURATION`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Within the exact MATH-022 domain of 17,745 right offsets surviving through depth 61, can the finite metric

\[
L_{\max}(r)=\max_b L(b,r)
\]

be represented by a materially smaller phase descriptor

\[
(q_{61},T^{61}(r)\bmod2^m)?
\]

## DSD tuple

### D — Definition

The object being compressed is **only the finite output metric `L_max`** on `0<=r<=10^7`.

This is not a claim that the descriptor represents the full Collatz trajectory or full Hensel state.

### R — Resolution

The audit varies the retained endpoint phase resolution `m` exactly and measures both:

1. aliasing errors — same descriptor, different lifespan;
2. state-count reduction.

Selected results:

| m | classes | conflicting classes | conflicting states |
|---:|---:|---:|---:|
|11|8,910|4,818|13,605|
|20|17,702|41|82|
|24|17,742|2|4|
|25|17,743|1|2|
|26|17,744|0|0|

### S — Selection

The input states are exactly the 17,745 MATH-022 depth-61 survivors.  Their `L_max` values are recomputed over all 339 internal boundaries with the same exact candidate prefix gate.

No sampling is used.

### E — Exclusion / counterexample

At `m=25`, two exact states share

\[
(q_{61},y\bmod2^{25})=(41,11,114,030)
\]

but have different output lifespans:

\[
r=702,631:\ L_{\max}=210,
\]

\[
r=7,066,623:\ L_{\max}=177.
\]

Therefore 25-bit phase truncation is not a legal exact descriptor even for the limited lifespan metric.

This is a direct finite-state aliasing witness.

### T — Transition

At `m=26` the finite lifespan metric has no aliasing in the audited domain, but the state count is still

\[
17,744/17,745.
\]

Hence raising phase resolution removes error only by restoring essentially all original state information.

No useful computational transition/merge follows.

### C — Consistency

The result is consistent with earlier MATH-007 right-congruence barriers: endpoint phase information cannot be coarsened freely when downstream survival behavior is sensitive to the parity continuation.

MATH-023 does not strengthen MATH-007 to a new universal modulus theorem; it is a separate finite lifespan diagnostic.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / STRATEGY SATURATION`

The no-conflict observation at `m=26` is not promoted beyond the finite MATH-022 dataset.

### O — Outcome

Closed:

- simple `(q61, y mod 2^m)` compression of `L_max` is not worth pursuing on this domain;
- `m<=25` is demonstrably unsafe;
- `m=26` has negligible compression.

Open:

- structural upper bounds for lifespan;
- dominance/monotone descriptors not requiring near-full phase information;
- right offsets above `10^7`;
- first cell / Collatz.

## Prohibited upgrades

Do not infer:

\[
\text{same finite }L_{\max}\Rightarrow\text{same full state}.
\]

Do not infer `m=26` is a universal exact quotient.

Do not infer strategy saturation of this descriptor invalidates MATH-021 or MATH-022.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_lifespan_phase_descriptor_saturation_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-lifespan-phase-descriptor-saturation.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-023`
