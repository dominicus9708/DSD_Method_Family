# Collatz min-plus value-frontier audit

Date: 2026-09-10
Audit ID: `DSD-AUDIT-20260910-MATH-056`
Status: `EXACT FINITE OBJECTIVE REDUCTION / REGRESSION PASS / UNIVERSAL VALUE LAW OPEN`

## Scope

This audit covers the transition from the MATH-054 slack-event budget scan to the MATH-056 exact min-plus objective and the associated cross-channel Hensel reduction.

The mathematical norm remains ordinary exact proof/certificate validity. DSD is used to identify which information is necessary for the downstream predicate and which histories may be merged without changing the objective.

## 1. Objective replacement

MATH-054 counted positive-slack odd events. MATH-056 instead uses their exact correction penalty.

For an odd event at position `k`, with odd count `q` and slack `u`, the first-72 penalty with common denominator `3^72` has exact integer cost

\[
w_{72}(k,q,u)=(2^u-1)2^k3^{71-q}.
\]

All costs are nonnegative. Hence exact Dijkstra ordering by accumulated integer cost is valid.

DSD verdict:

`SAFE OBJECTIVE COMPRESSION WITHIN THE STATED FINITE LANGUAGE`.

The event count is not a complete descriptor of penalty; replacing it by the exact min-plus cost removes that information loss.

## 2. Same-integer lineage retained

At depth 72 each prefix is mapped to the unique canonical ordinary start

\[
N\equiv-C3^{-q}\pmod{2^{72}}.
\]

Only starts in the current first-cell window are retained, and the same ordinary integer is then continued under the shortcut Collatz map for the coefficient-survival test.

No residue is silently promoted to a different ordinary integer after depth 72.

Verdict:

`LINEAGE PRESERVED`.

## 3. Exact finite values

The Math-verification certificate records

\[
V(195)\approx0.599240626584020691,
\]

\[
V(265)\approx0.825434691651584558,
\]

\[
V(300)\approx0.857630048844662025.
\]

These are exact finite minima represented by integer cost over `3^72`; the decimals are display values only.

Because the feasible sets are nested,

\[
V(K+1)\ge V(K)
\]

is exact. No positive asymptotic slope follows from the three sampled depths.

Verdict:

`FINITE EXACT / ASYMPTOTIC INFERENCE PROHIBITED`.

## 4. Hensel channel separation

The value function above uses address + coefficient survival. Hensel maximality is intentionally not folded into the value unless explicitly checked.

MATH-013 suffix stability permits a first-failure reduction: once the candidate was class-max at depth `k-1`, only an opposite-last-parity competitor can produce a new failure at depth `k`.

The dedicated cross-channel certificate reproduces the previously known Hensel failure of top-address 1133 at depth 56.

Verdict:

`EXACT REDUCTION / HENSEL EVIDENCE NOT DOUBLE-COUNTED`.

## 5. Scratch-result correction

A pre-commit scratch implementation had reported that the MATH-056 `V(195)` minimizer passed the cross-channel Hensel test through depth 140. During canonicalization an unsafe large-exponent implementation in the optimistic pruning bound was found.

That scratch statement is rejected from the canonical record.

The overflow-safe replacement retains only:

- top-address 1133: first Hensel failure at depth 56;
- top-address 1060 (`V(195)` minimizer): no cross-channel failure through depth 90.

This correction does not alter the min-plus frontier values.

DSD verdict:

`SCRATCH CLAIM DOWNGRADED / CANONICAL RANGE NARROWED`.

## 6. Current proof-facing bridge

The useful chain is now

\[
\text{same integer address}
+\text{coefficient survival}
+\text{Hensel state}
\longrightarrow
\text{minimum slack penalty}.
\]

The remaining obligation is not to compute `V(K)` at arbitrarily many depths. It is to find a complete Bellman quotient or a proved lower-bound recurrence for the value function, and then combine it with the first-crossing endpoint/correction requirement.

The candidate form

\[
V(K+\Delta)\ge V(K)+\delta
\]

is a target pattern only. No uniform positive `delta` theorem is established here.

## 7. Prohibited upgrades

- finite exact minima `=>` universal asymptotic growth;
- monotonicity `=>` strict monotonicity;
- coefficient survival `=>` full minimal-counterexample survival;
- cross-channel depth-90 pass `=>` depth-195 or arbitrary-depth Hensel maximality;
- min-plus compression `=>` first-cell closure;
- first-cell progress `=>` later-strip coverage;
- any finite certificate `=>` Collatz conjecture proof.

## Canonical Math-verification records

- `collatz/results/2026-09-10-firstcell-minplus-value-frontier.tsv`
- `collatz/src/2026_09_10_firstcell_minplus_value_frontier_certificate.cpp`
- `collatz/src/2026_09_10_cross_channel_hensel_candidate_certificate.cpp`
- `collatz/notes/2026-09-10-math056-firstcell-minplus-value-frontier.md`
