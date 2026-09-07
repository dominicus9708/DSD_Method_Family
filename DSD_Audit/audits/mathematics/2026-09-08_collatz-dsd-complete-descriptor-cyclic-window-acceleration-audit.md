# DSD Audit — Collatz DSD complete-descriptor cyclic-window acceleration

- **Audit ID:** `DSD-AUDIT-20260908-MATH-011`
- **Date:** 2026-09-08
- **Subject:** finite 61+11 Collatz coefficient-survival computation
- **Global Collatz status:** `OPEN`
- **Audit verdict:** `CONFIRMED WITHIN SCOPE / COMPUTATIONAL ACCELERATION`

## Claim under audit

For the exact finite MATH-006 transducer, the 11-bit tail survival predicate can be replaced by a complete residue descriptor

\[
H(r)=\max_{1\le j\le11}\bigl(q_{\min}(61+j)-s_j(r)\bigr),
\]

so that

\[
r\text{ survives to depth }72\iff q_{61}\ge H(r).
\]

Furthermore, for fixed `q61`, the 340-address count over all base phases can be transformed exactly into a cyclic length-340 sliding-window computation using the invertibility of `3^q mod 2048`.

The accelerated implementation must reproduce the full legacy count vector, not merely the min/max summary.

## D — Describability

**ESTABLISHED_WITHIN_SCOPE.**

Objects are explicit:

- `r in Z/2048Z`: address-lifted tail residue;
- `s_j(r)`: odd-count accumulated in the first `j` of the 11 tail steps;
- `q_min(k)`: minimum coefficient-surviving odd count at depth `k`;
- `H(r)`: exact threshold needed from the incoming `q61`;
- `C_q(y)`: number of the current 340 top-address labels that survive through depth 72 for base endpoint phase `y`.

The scope is finite and does not include arbitrary deeper continuation.

## R — Resolution

**ESTABLISHED_WITHIN_SCOPE.**

Resolution is exactly:

- 61 lower/root bits;
- 11 continuation bits;
- modulo `2^11=2048` endpoint phase;
- 340 addresses `1024..1363`;
- `q61=39..61`.

No result is silently extended beyond this resolution.

## S — Selection

The original MATH-006 condition is

\[
q_{61}+s_j(r)\ge q_{\min}(61+j)
\quad\text{for every }j=1,\dots,11.
\]

Taking the maximum of the rearranged lower bounds gives

\[
q_{61}\ge
\max_j\bigl(q_{\min}(61+j)-s_j(r)\bigr)=H(r).
\]

Therefore `q61 >= H(r)` is necessary and sufficient for exactly the same finite selection predicate.

## E — Exclusion

No candidate is excluded by a weaker or probabilistic criterion.

The accelerated algorithm excludes exactly the residues excluded by the original stepwise coefficient-survival test.

The full count vectors are asserted equal for every `q61=39..61` and every `y mod 2048`.

## T — Transition

Let

\[
m=3^{q_{61}}\pmod{2048}.
\]

Since `m` is odd, it is a unit modulo 2048.

For `z=m^{-1}y` and

\[
g_q(t)=\mathbf1[H(mt)\le q],
\]

one has exactly

\[
C_q(y)
=
\sum_{a=1024}^{1363}
\mathbf1[H(y+am)\le q]
=
\sum_{a=1024}^{1363}g_q(z+a).
\]

Thus the 340-address arithmetic progression is converted to a cyclic contiguous window. This is a bijective coordinate change, not a loss of state information.

## C — Consistency

**CONFIRMED.**

The accelerated implementation reproduces the complete legacy MATH-006 count vector for all audited `q61` values.

The resulting min/max table remains:

| `q61` | min | max |
|---:|---:|---:|
| 39 | 36 | 47 |
| 40 | 124 | 141 |
| 41 | 221 | 235 |
| 42 | 288 | 303 |
| 43 | 320 | 333 |
| 44 | 336 | 340 |
| 45 | 339 | 340 |
| 46–61 | 340 | 340 |

The exact `H` distribution is:

| `H` | count |
|---:|---:|
| 39 | 247 |
| 40 | 554 |
| 41 | 570 |
| 42 | 406 |
| 43 | 195 |
| 44 | 63 |
| 45 | 12 |
| 46 | 1 |

which sums to 2048 and explains why all residues survive for `q61>=46` under this finite predicate.

## N — Norm

- Exact finite equivalence: `ESTABLISHED_WITHIN_SCOPE`
- Computational acceleration: `CONFIRMED`
- New theorem-level pruning: `NO`
- First-cell closure: `OPEN`
- Collatz closure: `OPEN`

Wall-clock benchmark ratios are diagnostic only because they depend on interpreter and hardware.

The invariant deterministic work statement is preferred: the all-phase/all-address layer uses

\[
23\cdot2048\cdot340=16{,}015{,}360
\]

address-survival predicate lookups in the legacy scan, whereas descriptor construction followed by threshold arrays needs

\[
23\cdot2048=47{,}104
\]

threshold evaluations at that layer, a factor `340` reduction in predicate evaluations, plus inexpensive sliding sums and a one-time `2048*11` descriptor construction.

## O — Outcome

**CONFIRMED WITHIN SCOPE / COMPUTATIONAL ACCELERATION.**

This is the first current Collatz case in which DSD contributes directly to computation by identifying a complete finite descriptor and a safe exact coordinate transform that avoid repeated work.

It does not strengthen the mathematical survivor bounds and must not be presented as new progress toward universal closure by itself.

## Prohibited upgrades

- computational speedup `=>` stronger Collatz theorem;
- finite complete descriptor at depth 72 `=>` complete descriptor at arbitrary depth;
- exact min/max regression `=>` fixed globally excluded labels;
- runtime benchmark ratio `=>` machine-independent complexity theorem;
- current first-cell computation `=>` Collatz proof.

## Evidence

Math-verification certificate:

`collatz/src/2026_09_08_dsd_complete_descriptor_cyclic_window_acceleration.py`

Certificate commit:

`03f4c5bc86bbea3a27dbdf509da79d15dd70492d`

Explanatory note:

`collatz/notes/2026-09-08-dsd-complete-descriptor-and-cyclic-window-acceleration.md`

Note commit:

`2d0e75d9c07a01b531bc572e695ad779094ebd8f`

## Next audit target

Test whether the depth-72+ same-integer continuation/Hensel eligibility predicate admits an analogous complete descriptor. The next descriptor is worth keeping in the computation engine only if it yields safe pruning, safe merging, or fewer exact state expansions.
