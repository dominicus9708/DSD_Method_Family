# DSD Audit — Collatz Hensel ternary truncation barrier

- **Audit ID:** `DSD-AUDIT-20260908-MATH-014`
- **Date:** 2026-09-08
- **Target:** exact Hensel class descriptor after MATH-013
- **Verdict:** `CONFIRMED / EXACT INFORMATION BARRIER`
- **Collatz status:** `OPEN`

## Claim under audit

Can the exact MATH-013 Hensel translation-class residue

\[
r=C\bmod3^q
\]

be replaced uniformly by a shorter ternary residue

\[
C\bmod3^m,\qquad m<q?
\]

## Exact witness family

For arbitrary

\[
q\ge1,\qquad k\ge q+1,
\]

choose two length-k parity words with odd-position sets

\[
P_w=\{0,2,3,\ldots,q\},
\qquad
P_u=\{1,2,3,\ldots,q\}.
\]

Both have exactly q odd entries. Their correction difference is

\[
\boxed{C(w)-C(u)=-3^{q-1}.}
\]

Hence

\[
C(w)\equiv C(u)\pmod{3^{q-1}}
\]

while

\[
C(w)\not\equiv C(u)\pmod{3^q}.
\]

Every coarser power-of-three residue `3^m`, `m<q`, therefore aliases two distinct exact Hensel classes.

## DSD tuple

### D — Describability

The exact class key `(q,C mod3^q)` and the proposed truncated observations are explicitly distinguished.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### R — Resolution

Scope is the unrestricted finite parity-word language with `q<k`. Zero padding extends the witness to every `k>=q+1`.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### S — Selection

A constructive two-word witness family is selected; no probabilistic or search-based existence step is needed.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### E — Exclusion

Uniform truncations `C mod3^m`, `m<q`, are excluded as complete exact Hensel-class descriptors.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### T — Transition

Padding by zero parity bits leaves q and both corrections unchanged, so the alias persists at all larger depths.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### C — Consistency

The identity follows directly from the correction sum, and the certificate regresses the construction through `q=512` with exact integers.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### N — Norm

This is an information barrier only. It is not a Collatz exclusion theorem.

Status: `ESTABLISHED_WITHIN_SCOPE`.

### O — Outcome

`CONFIRMED / EXACT INFORMATION BARRIER`.

The naive fixed ternary-truncation branch is closed. A smaller descriptor would require additional proven restrictions or a genuinely different quotient.

## Prohibited upgrades

- Do not infer that every possible descriptor must have cardinality `3^q`.
- Do not infer that a restricted downstream language cannot compress further.
- Do not infer Collatz closure from failure of a computational compression route.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_hensel_ternary_truncation_barrier_certificate.py`

Certificate commit:

`74738fa7c875077c2e58aa370185dbe85507c2fc`

Explanatory note:

`collatz/notes/2026-09-08-hensel-ternary-truncation-barrier.md`

Note commit:

`2829c30984cb0db77a75357d6ac850ae51495ed7`
