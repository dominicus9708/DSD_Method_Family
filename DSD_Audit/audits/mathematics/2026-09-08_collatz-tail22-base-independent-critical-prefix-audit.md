# DSD-AUDIT-20260908-MATH-033 — Collatz base-independent 22-step critical prefix

Date: 2026-09-08

Verdict:

`CONFIRMED / EXACT LOCAL DESCRIPTOR / COMPUTATIONAL ACCELERATION`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Can the exact 22-step coefficient-survival threshold

\[
H_K(u)=\max_{1\le j\le22}
\left(q_{\rm pub}(K+j)-s_j(u)\right)
\]

be represented at every base depth `K` by one base-independent critical prefix attached to residue `u mod 2^22`?

## DSD tuple

### D — Definition

At the frozen theorem-facing floor,

\[
B=2^{71},\quad A=3B+1,\quad c_0=A/B.
\]

Let

\[
\beta=\log2/\log c_0.
\]

For one local parity residue `u`, `s_j(u)` is the cumulative added odd-count through local prefix `j`.

### R — Resolution

The critical prefix is

\[
j_*(u)=\arg\max_j(\beta j-s_j(u)).
\]

The certificate does not approximate beta numerically.  For positive integer differences `Delta j, Delta s`, score ordering is decided exactly by

\[
2^{\Delta j}B^{\Delta s}
\gtrless
A^{\Delta s}.
\]

All `2^22` residues are processed.

### S — Selection

No residue is sampled or discarded.  The descriptor is constructed for every one of

\[
4,194,304
\]

22-bit residues.

### E — Exact equivalence

Because `A` is odd and greater than 1, the strict coefficient equality `c_0^q=2^k` is impossible for positive integer `q,k`. Hence

\[
q_{\rm pub}(k)=\lceil\beta k\rceil.
\]

For any local prefix `j`, criticality gives

\[
\beta(j_*-j)\ge s_{j_*}-s_j=:m\in\mathbb Z.
\]

Therefore for every base depth `K`,

\[
\lceil\beta(K+j_*)\rceil
\ge
\lceil\beta(K+j)+m\rceil
=
\lceil\beta(K+j)\rceil+m.
\]

Thus

\[
\boxed{
H_K(u)=q_{\rm pub}(K+j_*)-s_{j_*}
}
\]

for every `K`.

### T — Transition

The local threshold calculation can therefore carry `(j_*,s_*)` with each residue and evaluate an arbitrary-base 22-step gate with one `q_pub` lookup and subtraction.

Endpoint propagation is deliberately kept separate.  MATH-033 does not authorize a residue-only propagated state.

### C — Consistency

The certificate explicitly regresses the formula on all `2^22` residues at bases

`0, 61, 83, 127, 545, 1007`,

for a total of

\[
25,165,824
\]

threshold equalities, all passing.

During development, an apparent concern about the ceiling function was audited directly. The integer nature of `s_{j_*}-s_j` is exactly what preserves the ordering after ceiling translation.

A separate implementation issue was also identified: forming a full 22-step affine numerator in one 128-bit multiplication can overflow even when two sequential audited 11-step updates do not. That implementation route is rejected; it does not affect the threshold theorem.

### N — Norm

Evidence status:

`ESTABLISHED / EXACT LOCAL PREDICATE DESCRIPTOR`.

This is not a complete arbitrary-depth Collatz state descriptor.

### O — Outcome

Established:

- one unique critical prefix per 22-bit residue;
- exact base-independent representation of the 22-step coefficient threshold;
- exact integer computation of critical-prefix ordering;
- exhaustive six-base regression over all `2^22` residues.

Still open:

- use of the descriptor in the full depth-83+ continuation;
- larger right-offset domains;
- first-cell emptiness;
- Collatz.

## AP-2 / representation audit

The descriptor compresses only the **local threshold function**.  Exact endpoint information remains required for the next residue and transition.

Therefore the result is not an unsafe finite-state merge.

## Prohibited upgrades

Do not infer:

- base-independent threshold descriptor ⇒ base-independent full Collatz state;
- local 22-step completeness ⇒ arbitrary-depth completeness;
- threshold compression ⇒ candidate exclusion beyond the exact gate;
- computational acceleration ⇒ proof completion.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_tail22_base_independent_critical_prefix_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-tail22-base-independent-critical-prefix.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-033`
