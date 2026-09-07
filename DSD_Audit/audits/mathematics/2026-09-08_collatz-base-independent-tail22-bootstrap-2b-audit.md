# DSD-AUDIT-20260908-MATH-035 — Collatz base-independent tail22 bootstrap through 2e9

Date: 2026-09-08

Verdict:

`CONFIRMED / FINITE ONLY / EXACT ACCELERATED BOOTSTRAP`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Does the current DSD-native accelerated engine preserve exact ordinary-integer lineage when the finite right-offset domain is enlarged to

\[
0\le r\le2,000,000,000,
\]

and what exact internal adjacent-block same-endpoint exclusion follows from that finite domain?

## DSD tuple

### D — Definition

The starts are

\[
N=b2^{61}+r,
\qquad1025\le b\le1363,
\qquad0\le r\le2\cdot10^9.
\]

The candidate predicate is prefixwise coefficient survival in the current universal-spine route.

The conclusion concerns only internal adjacent-block candidates that could meet at a common endpoint.

### R — Resolution

The engine preserves four exact layers:

1. cut-10 bounded binary prefix state;
2. exact depth-61 state `(r,T^61(r),q61)`;
3. cyclic 22-bit residue lookup used only to decide the first 22-step address-survival gate;
4. exact endpoint state propagated by two audited 11-step affine updates per accepted 22-step block.

No residue-only state is propagated in place of the exact endpoint.

### S — Selection

Exact depth-61 right-offset survivors:

\[
\boxed{3,592,089}.
\]

First and last:

\[
703,\qquad1,999,999,935.
\]

Exact q61 histogram:

`39:771761, 40:987601, 41:794250, 42:514554, 43:285599, 44:140125, 45:61616, 46:24051, 47:8723, 48:2770, 49:745, 50:231, 51:54, 52:8, 53:1`.

The `q61=53` state is retained. Any implementation that freezes the previously observed support `39..52` is therefore invalid on this enlarged domain.

### E — Exclusion

The 22-step cyclic address prefilter leaves

\[
\boxed{379,544,924}
\]

exact depth-83 address states.

The base-83+ computation executes

\[
\boxed{588,381,926}
\]

base-independent 22-step threshold gates.

Results:

\[
\boxed{\text{survive to audited end}=0},
\]

\[
\boxed{\text{overflow}=0}.
\]

Deepest failing base:

\[
\boxed{545},
\]

with first witness

\[
\boxed{r=378,620,799,\quad b=1183}.
\]

### T — Transition

The exact transition chain is

\[
T^k(x+e2^k)=T^k(x)+e3^{q_k}
\]

for bounded lifting,

then

\[
T^{61}(b2^{61}+r)=T^{61}(r)+b3^{q_{61}},
\]

then the 22-step coefficient gate selected by the MATH-033 critical prefix, followed by two exact 11-step affine endpoint updates.

The MATH-033 threshold descriptor is a gate, not a replacement endpoint state.

### C — Consistency

The frozen theorem-facing coefficient threshold is generated with arbitrary-precision integer arithmetic.

The previous `RMAX=10^9` implementation support `q61<=52` is explicitly not reused as a theorem. The enlarged domain exhibits `q61=53`, and the final computation includes it.

MATH-021 supplies the independent necessary collision-halo condition

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor.
\]

Thus `r<=2e9` covers every relevant right offset through

\[
\boxed{k\le6,000,000,003}.
\]

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / FINITE ONLY`.

Exact consequence:

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate coupling for }
61\le k\le6,000,000,003
}
\]

within the audited universal-spine/coefficient-survival scope.

### O — Outcome

Established:

- exact finite domain enlarged to `r<=2e9`;
- 3,592,089 depth-61 survivors;
- exact q61 support through 53 in this domain;
- 379,544,924 depth-83 exact address states after cyclic prefilter;
- 588,381,926 base-83+ 22-step gates;
- zero audited-end survivors and zero endpoint overflows;
- finite internal endpoint-coupling exclusion through depth 6,000,000,003.

Still open:

- right offsets above `2e9`;
- the full first-cell collision-halo domain;
- candidate mechanisms not involving this endpoint coupling;
- first-cell emptiness;
- Collatz.

## Implementation audit

The appearance of one `q61=53` survivor is a positive DSD implementation-audit event: an empirical support bound from a smaller finite domain is not allowed to become an undeclared type invariant.

Future implementations should derive or dynamically accommodate the q-range for the requested domain.

## Prohibited upgrades

Do not infer:

- finite `r<=2e9` implies all halo offsets;
- depth `6,000,000,003` implies ordinary Collatz verification to that depth;
- same-endpoint coupling exclusion implies candidate emptiness;
- repeated deepest failure at 545 implies a universal lifespan bound;
- acceleration or finite exclusion implies a proof of Collatz.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_base_independent_tail22_bootstrap_2b_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-base-independent-tail22-bootstrap-2b.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-035`
