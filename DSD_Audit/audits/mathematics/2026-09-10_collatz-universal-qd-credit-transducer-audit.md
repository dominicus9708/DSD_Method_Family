# DSD-AUDIT-20260910-MATH-013 — Collatz universal q-d credit transducer

Date: 2026-09-10

Verdict: `EXACT REPRESENTATION REDUCTION / FINITE REGRESSION PASS / UNIVERSAL FINITE CLOSURE OPEN`

## 1. Audited claim

The post-MATH-051 one-sided root-Hensel computation was previously implemented as a family of fixed-even-budget (`d`) finite-state solvers. The audited question is whether `d` is genuinely part of the transition law or only part of the initial condition.

Result:

\[
\boxed{\text{the arithmetic transition is universal in }(q,d);\ d\text{ is not an internal transition parameter}.}
\]

This is an exact reparameterization claim, not a Collatz proof claim.

## 2. Universal coefficient boundary

For the j-th even rank with cumulative odd-gap `G_j`, coefficient admissibility is

\[
3^{G_j}>2^{G_j+j+1}.
\]

Hence

\[
\boxed{\ell_j=\left\lceil(j+1)\log_{3/2}2\right\rceil}
\]

and the reverse capacity is

\[
\boxed{m(r)=\left\lfloor r\log_2(3/2)\right\rfloor}.
\]

Therefore

\[
\ell_{a-1}\le r\iff a\le m(r).
\]

The formerly stored deadline vector `L[j]` is a prefix of one universal Beatty/mechanical staircase.

Audit classification: `EXACT`.

## 3. Credit-coordinate reduction

From the previous carry state `(a,b,h)`, define

\[
\boxed{\chi=h+2^b-2^a.}
\]

If the next state has remaining ranks `(a',b')`, then

\[
\boxed{\chi'=\frac{2\chi+2^{b'}-2^{a'}}3},
\]

with exact divisibility by 3 required.

Initial state:

\[
(a,b,\chi)=(d,d,0).
\]

Terminal positive Hensel translation credit is exactly `chi>0`.

Audit classification: `EXACT`.

## 4. Universal viability recurrence

Let `V(r,a,b,chi)` mean that at least one completion through r remaining gap levels ends in positive exact Hensel credit while the candidate obeys the coefficient boundary and the competitor remains unrestricted.

Then

\[
V(r,a,b,\chi)=
\bigvee_{0\le a'\le\min(a,m(r-1))}
\bigvee_{0\le b'\le b}
\left[
3\mid(2\chi+2^{b'}-2^{a'})
\wedge
V\!\left(r-1,a',b',\frac{2\chi+2^{b'}-2^{a'}}3\right)
\right],
\]

with

\[
V(0,a,b,\chi)\iff(a=0\wedge\chi>0).
\]

No original fixed-d parameter occurs inside this transition law.

`q` determines the initial remaining gap level and `d` determines only the initial state `(d,d,0)`.

Audit classification: `EXACT REPARAMETRIZATION`.

## 5. Regression evidence

The independent universal-coordinate certificate in `dominicus9708/Math-verification` reproduces the completed MATH-051 terminal-dominated counts:

| q | d | canonical D | universal-coordinate D |
|---:|---:|---:|---:|
| 30 | 10 | 54,028,926 | 54,028,926 |
| 29 | 11 | 124,678,824 | 124,678,824 |
| 29 | 12 | 361,499,293 | 361,499,293 |
| 28 | 13 | 586,723,760 | 586,723,760 |
| 27 | 14 | 703,863,494 | 703,863,494 |
| 26 | 15 | 355,002,462 | 355,002,462 |

No mismatch occurred.

Audit classification: `FINITE EXACT REGRESSION`.

## 6. Rank normalization

The transition is equivariant under

\[
(a,b,\chi)\mapsto(a+s,b+s,2^s\chi).
\]

Therefore every reachable state from the zero-credit root obeys

\[
\boxed{2^{\min(a,b)}\mid\chi.}
\]

Define

\[
v=b-a,
\qquad
c=\chi/2^{\min(a,b)},
\qquad
u=m(r)-a.
\]

With

\[
\varepsilon_r=m(r)-m(r-1)\in\{0,1\},
\]

and candidate consumption `t=a-a'`,

\[
t=\nu'-\nu+\varepsilon_r.
\]

Writing `p(v)=min(0,v)` and

\[
\Delta(v)=2^{\max(v,0)}-2^{\max(-v,0)},
\]

the normalized arithmetic update is

\[
\boxed{
c'=\frac{2^{1+t+p(v)-p(v')}c+\Delta(v')}{3}}.
\]

The arithmetic core is therefore independent of the absolute ranks and is driven locally by the mechanical boundary bit `epsilon_r`.

Audit classification: `EXACT IDENTITY`; arbitrary normalized-state finiteness remains `OPEN`.

## 7. DSD information-loss audit

The following information has been shown redundant for the Hensel-dominance predicate:

- raw parity-word enumeration;
- absolute even positions once cumulative gaps are retained;
- the fixed-d deadline array as a separate object;
- the old blocksum carry once `chi` is retained;
- common absolute candidate/competitor rank scale once `(v,c)` is retained locally.

The following information is **not** yet removable:

- normalized competitor-excess / credit state as d grows;
- the nonperiodic mechanical coefficient-boundary drive;
- ordinary-integer dyadic address lineage;
- first-crossing/Farey-cell identity;
- terminal endpoint/correction requirement.

## 8. Counting versus final proof obligation

The MATH-051 finite calculation counted dominated candidates. A universal proof requires an emptiness/path-existence statement, not merely a density or count estimate.

The Hensel component can be viewed as a safety game in which the candidate chooses a coefficient-valid continuation and an exact competitor frontier tracks every possible same-Hensel-class dominating word.

The eventual proof object should be the infinite/terminal bad-path set, equivalently a greatest safe fixed point on an exact product state.

Root-Hensel state alone is insufficient. The same ordinary integer must be preserved across dyadic address, Hensel, first-crossing and endpoint conditions.

## 9. Relation to the full-proof architecture

The current first-cell target in `Math-verification` requires the pointwise intersection of:

1. root dyadic address;
2. coefficient survival;
3. nested root-Hensel maximality;
4. first-crossing cell extension;
5. terminal correction/end-point sufficiency.

The correct eventual state is therefore a lineage-preserving product, not an independent multiplication of filter counts.

Eliminating the first universal Farey cell would still leave later strip cells unless a separate uniform strip-coverage theorem is supplied.

## 10. Corrected next target

Because the coefficient boundary is a nonperiodic mechanical/Sturmian word, a single constant matrix and rational generating function must not be assumed without an additional phase quotient.

The natural intermediate target is a two-operator cocycle driven by

\[
\varepsilon_r\in\{0,1\},
\]

provided the normalized state admits a uniform finite quotient:

\[
M_{\varepsilon_q}\cdots M_{\varepsilon_1}.
\]

If no such finite quotient exists, seek a well-founded ranking function on the normalized exact state instead.

## 11. Prohibited upgrades

- universal recurrence `=>` finite universal automaton;
- MATH-051 regression `=>` arbitrary-d theorem;
- two-symbol Sturmian drive `=>` periodicity;
- decreasing survivor density `=>` empty survivor set;
- Hensel component closure `=>` same-integer closure;
- first-cell closure `=>` all Farey strip cells;
- DSD reparameterization `=>` independent novelty claim;
- any result in this audit `=>` Collatz conjecture solved.

## 12. Canonical companion records

In `dominicus9708/Math-verification`:

- `collatz/notes/2026-09-10-math052-universal-qd-credit-transducer-and-final-target.md`
- `collatz/src/2026_09_10_universal_qd_credit_transducer_certificate.cpp`
- `collatz/src/2026_09_10_rank_normalized_bulk_recurrence_certificate.py`
- `collatz/results/2026-09-10-universal-qd-credit-transducer-regression.tsv`
