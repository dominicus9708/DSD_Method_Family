# DSD-AUDIT-20260908-MATH-013 — Collatz Hensel class-max dominance quotient

## Verdict

`CONFIRMED / EXACT DOMINANCE QUOTIENT / COMPUTATIONAL ACCELERATION / RESIDUAL TERNARY-STATE BARRIER`

Collatz conjecture remains `OPEN`.

The first universal Farey cell remains `OPEN`.

## Audited claim

For a length-`k` parity word with odd-count `q` and correction `C`, write

\[
C=h3^q+r,
\qquad0\le r<3^q.
\]

The root-Hensel translation-class key is

\[
\kappa=(q,r)=(q,C\bmod3^q).
\]

Within one exact class, larger `h` permanently dominates smaller `h` for the class-maximum computation. This dominance is preserved under both possible next parity-bit transitions, so one may retain only the maximum `h` representative per class before expansion.

This is an exact computational quotient. Candidate exclusion still requires the corresponding positive ordinary-start credit to be legal; MATH-012 supplies a uniform arithmetic-credit gate only in its stated scope.

## DSD tuple

### D — Describability

The audited object is not the full Collatz state. It is the root-Hensel **translation class plus class-max score**:

\[
(q,r;h).
\]

The class and the dominance coordinate are explicitly separated.

### R — Resolution

The finite regression covers symbolic parity-word depths through `L=26`. The class residue is exact modulo `3^q`; no binary-phase or coarse quotient is substituted for it.

### S — Selection

For each exact class `(q,r)`, keep only the largest observed `h`.

### E — Exclusion

A smaller-`h` state in the same class is excluded from **future class-maximum computation**, because it can never overtake the larger state under either child transition.

This does not by itself exclude the corresponding ordinary Collatz candidate unless a valid positive-start credit argument is also available.

### T — Transition

If the next bit is even, `(q,r,h)` is unchanged.

If the next bit is odd at position `k`,

\[
C'=3C+2^k
=h3^{q+1}+(3r+2^k).
\]

Writing

\[
3r+2^k=t3^{q+1}+r',
\]

gives

\[
r'=(3r+2^k)\bmod3^{q+1},
\qquad
h'=h+t.
\]

The child class key depends only on `(q,r,k)`, and the child score is the parent `h` plus the same class-dependent constant. Therefore strict `h` order is preserved.

### C — Consistency

A known exact L=24 collision provides the information-loss witness:

\[
(k,q,d)=(24,15,9)
\]

for both words, but

\[
C_w=5\cdot3^{15}+3{,}169{,}280,
\qquad
C_u=1\cdot3^{15}+3{,}169{,}280.
\]

Thus they share the same exact class residue but have `h=5` and `h=1`, respectively, with credit difference 4. This proves that the MATH-012 scalar `(k-q)` does not contain the remaining Hensel class/maximality information.

The new quotient DP reproduces exact class counts through L=26.

### N — Norm

`ESTABLISHED_WITHIN_SCOPE`.

Finite state-reduction ratios are not asymptotic estimates. Wall-clock measurements are diagnostic only.

### O — Outcome

A downstream-stable dominance quotient is available and materially reduces the finite symbolic state space, but exact ternary residue information survives as a necessary state component.

## Exact finite compression

Excluding the all-zero word:

| L | full nonzero words | class-max states | state reduction |
|---:|---:|---:|---:|
| 24 | 16,777,215 | 3,213,594 | 5.220701495× |
| 25 | 33,554,431 | 6,116,463 | 5.485920703× |
| 26 | 67,108,863 | 11,650,325 | 5.760256731× |

Cumulative child transitions:

| L | full binary transitions | quotient transitions | reduction |
|---:|---:|---:|---:|
| 24 | 33,554,430 | 7,141,552 | 4.698478706× |
| 25 | 67,108,862 | 13,568,742 | 4.945842584× |
| 26 | 134,217,726 | 25,801,670 | 5.201900730× |

These are exact finite operation/state counts for the quotient computation.

## Information-loss conclusion

The following quotient is unsafe for residual Hensel structure:

\[
(k,q,d),\qquad d=k-q.
\]

The exact class residue

\[
r=C\bmod3^q
\]

cannot be discarded merely because the MATH-012 arithmetic-credit predicate depends only on `d`.

Therefore MATH-012 and MATH-013 have different roles:

- `d=k-q` is complete for the **credit envelope**;
- `(q,r)` plus class-max `h` is needed for the **translation-class maximality calculation**.

## Safe acceleration rule

For root-Hensel class-max enumeration:

1. represent each state by exact `(q,r,h)`;
2. merge equal `(q,r)` keys immediately;
3. retain only maximal `h`;
4. expand only those representatives.

Because dominance is transition-stable, a removed state never needs to be restored later.

## Prohibited upgrades

- same `(k,q,d)` ⇒ same Hensel class — **PROHIBITED**.
- same `d` ⇒ same full-Hensel eligibility — **PROHIBITED**.
- same `(q,r)` ⇒ same complete Collatz trajectory — **PROHIBITED**.
- lower `h` ⇒ impossible Collatz candidate without a legal positive-start credit — **PROHIBITED**.
- finite 24–26 compression ratio ⇒ asymptotic compression exponent — **PROHIBITED**.
- class-max computational pruning ⇒ first-cell closure — **PROHIBITED**.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_dsd_hensel_classmax_dominance_quotient.cpp`

Certificate commit:

`098fddb5565b0a9849ce51c50a9c4660c81855be`

Explanatory note:

`collatz/notes/2026-09-08-hensel-classmax-dominance-quotient.md`

Historical L=24 singleton/collision anchor:

`collatz/src/no00_root_hensel_max_audit.cpp`

Historical commit:

`414169e3fa272265b08850dbd447eb70fb9a482e`

## Next decision gate

Test whether the current first-cell/bounded-credit setting permits a smaller exact quotient of the ternary class residue. If no such quotient is available without losing class identity, stop deepening this Hensel-compression branch and move primary effort to the `<2^35` adjacent-block halo invariant.

Global status remains `OPEN`.
