# DSD-AUDIT-20260908-MATH-009

## Subject

Collatz root-Hensel correction ordering versus endpoint/minimum-start ordering.

## Verdict

`CONFIRMED / REDUNDANT / NO NEW PRUNING`

Collatz conjecture: `OPEN`.

## Locked scope

The audit compares candidates only inside a common fixed `(k,q,E)` fiber, where `k` is the shortcut depth, `q` the odd count and `E` the endpoint.

For each candidate,

\[
2^kE=3^qN+R.
\]

For two candidates in the same locked fiber,

\[
R_1-R_2=3^q(N_2-N_1),
\]

so

\[
N_1<N_2\iff R_1>R_2.
\]

The two proposed orderings are therefore one affine relation, not independent evidence.

## Audit tuple

\[
\mathcal A=(D,R,S,E,T,C,N,O).
\]

### D — Describability

`N`, `R`, `q`, `k`, and `E` are explicitly defined in the same endpoint identity.

### R — Resolution

The comparison is valid only after locking the same depth, odd count and endpoint. Comparisons across different fibers are not imported.

### S — Selection

The minimum-start representative and maximum-correction representative coincide inside the locked fiber.

### E — Exclusion

A candidate excluded by this ordering cannot be counted as independently excluded again by relabeling the same ordering as a root-Hensel correction selector.

### T — Transition

The transition from the two affine identities to the difference identity is exact algebra.

### C — Consistency

The result is consistent with the previously audited endpoint q-lock/address-faithful Hensel interpretation.

### N — Norm

This is a local exact identity. It does not upgrade the root-Hensel depth-195 theorem, the first universal cell, or the Collatz conjecture.

### O — Outcome

The attempted additional pruning branch is closed as `REDUNDANT / NO NEW PRUNING`.

## Surviving information

The depth-195 root-Hensel result still has separate value as a same-integer extension/eligibility statement. MATH-009 removes only the invalid interpretation that correction ordering and endpoint ordering are independent filters.

## Prohibited upgrade

\[
\text{same ordering in two coordinate systems}
\not\Rightarrow
\text{two independent pruning credits}.
\]

\[
\text{MATH-009 confirmed}
\not\Rightarrow
\text{first universal cell closed}.
\]
