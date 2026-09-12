# DSD Audit — Collatz MATH-090 dyadic carry valuation

Date: 2026-09-12

Status: `PASS / EXACT HENSEL-LIFT COMPATIBILITY FORM / NOT A GLOBAL CARRY THEOREM`

## 1. Scope

MATH-090 rewrites exact dyadic macro compatibility as a low-resolution residue test plus a 2-adic carry-divisibility test.

## 2. Low-resolution residue

For `R=ceil(log2 M)`, solving

\[
r_R\equiv(A-B)(3^Q)^{-1}\pmod{2^R}
\]

is exact because `3^Q` is odd.  If `r_R>=M`, no parameter in `0<=s<M` can satisfy the full edge congruence.

`PASS`.

## 3. Carry valuation

Define

\[
C_R=(A-B-3^Qr_R)/2^R.
\]

A zero Hensel lift from bit `R` through bit `h-1` requires each successive carry parity to be zero.  This is equivalent to

\[
2^{h-R}\mid C_R
\]

or

\[
\nu_2(C_R)\ge h-R.
\]

The finite synthetic regression in the certificate agrees with the direct full-residue test. `PASS`.

## 4. Information separation

The result preserves the DSD separation:

- `r_R<M` checks whether the low-resolution address lies inside the finite source family;
- `nu_2(C_R)>=z` checks whether that address can be extended through all additional dyadic bits without changing the source parameter;
- the phase inequality checks Bellman cost.

No one component is substituted for another. `PASS`.

## 5. Relation to depth-41 bounded carry

The new compatibility carry and the depth-41 dominance carry are not asserted to be the same numerical variable.
They are instances of the same finite-lifting mechanism, but they answer different questions.

This distinction is required. `PASS`.

## 6. Prohibited upgrades

Do not infer:

- high carry valuation is probabilistically rare;
- carry compatibility alone implies Bellman danger;
- the depth-41 dominance carry can directly replace the macro compatibility carry;
- MATH-090 closes depths 7--16;
- one-paid closure implies first-cell or Collatz closure.

## 7. Verdict

`PASS` as an exact compatibility compression.  The recommended next calculation is to classify remaining phase-danger terminal edges first by `(R,z)` and then apply the low-residue/carry test, rather than carrying full source integers through the whole tree.
