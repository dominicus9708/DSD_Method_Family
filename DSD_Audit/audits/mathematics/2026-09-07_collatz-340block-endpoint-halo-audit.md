# DSD-AUDIT-20260907-MATH-005 — Collatz 340-block endpoint-halo decomposition

Date: 2026-09-07
Domain: Mathematics / Collatz
Primary repository: `dominicus9708/Math-verification`

## Outcome

**Verdict: CONFIRMED address-geometric reduction.**

The 340 surviving top-address blocks are not coupled all-to-all by candidate-language endpoint/Hensel equivalence. Any such fiber can meet at most two adjacent blocks, and every internal cross-block interaction is confined to an exact boundary halo of width below `2^35` on each relevant side.

This is a decomposition theorem, not an emptiness theorem.

## Inputs

Current start partition:

\[
I_a=[a2^{61},(a+1)2^{61}),
\qquad a=1024,\ldots,1363.
\]

Number of blocks:

\[
340.
\]

Full-first-cell endpoint q-lock and candidate correction bound:

\[
q_1=q_2=q,
\qquad
S\le q/3.
\]

Terminal odd count:

\[
q_0=72,057,431,991.
\]

## Derived displacement bound

For same-endpoint candidate states,

\[
|N_1-N_2|=|S_1-S_2|<q/3\le q_0/3.
\]

Since `q0` is divisible by 3, the largest possible positive integer displacement is

\[
H=q_0/3-1=24,019,143,996<2^{35}.
\]

Block width is

\[
W=2^{61}.
\]

Thus

\[
2H<W.
\]

## Eight-axis audit

### D — Describability

PASS.

Blocks, boundaries, ordinary starts, endpoint fibers, and halo width are explicitly defined.

### R — Resolution

PASS.

The decomposition is in exact ordinary integer address space. No measure or statistical quotient replaces the integer geometry.

### S — Selection

PASS.

Only the 340 blocks already surviving the certified first-cell start cap are partitioned. Outer-window states are not silently deleted.

### E — Exclusion

PASS AS A COUPLING EXCLUSION.

An endpoint fiber cannot connect nonadjacent blocks because its total start displacement is `<H<W/2`.

This excludes **long-range block coupling**, not candidate starts themselves.

### T — Transition / lineage

PASS.

The fiber relation is inherited from exact common endpoints with equal odd count. Address displacement is exact and lineage-preserving.

### C — Consistency

PASS.

The halo theorem is consistent with the full-first-cell q-lock audit and with the ordinary start interval.

### N — Norm

PASS.

No new proof norm is introduced. The result reorganizes exact candidate states for later minimal-counterexample quotienting.

### O — Outcome

CONFIRMED.

The 340-block endpoint-coupling graph is nearest-neighbor only.

## Exact finite geometry

Internal boundaries:

\[
339.
\]

Two-sided internal halo integer count:

\[
2H\cdot339
=16,284,979,629,288.
\]

Strict candidate-window integer count:

\[
340\cdot2^{61}-1.
\]

Hence

\[
\frac{16,284,979,629,288}{340\cdot2^{61}-1}
<\frac1{48,140,000}.
\]

The small ratio is recorded only as computational-locality information.

## Required prohibited upgrades

- small halo fraction does not imply empty halos;
- block-local endpoint quotient does not make terminal correction local;
- outer candidate-window boundaries must not be treated as ordinary internal interfaces;
- no block is eliminated by this theorem alone;
- no Collatz conclusion follows from the decomposition alone.

## Evidence

Certificate commit:

`f2774276400f8d4519545d0c43b63c1f3e8a12ea`

Explanatory note commit:

`0f98069e78b7aa06fcbe7560b6564fc652b203dd`

Upstream full-cell q-lock audit:

`DSD-AUDIT-20260907-MATH-004`

## Next audited transition

Normalize each block as

\[
N=a2^{61}+x.
\]

Audit whether any root-prefix/terminal obligations admit a right-congruence in the block label `a`. Only a proved equivalence may group block interiors; otherwise the 340 interiors remain separate exact problems.