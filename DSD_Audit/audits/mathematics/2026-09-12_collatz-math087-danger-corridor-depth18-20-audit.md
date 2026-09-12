# DSD Audit — Collatz MATH-087 danger-corridor closure at depths 18--20

Date: 2026-09-12

Status: `PASS / EXACT FINITE BELLMAN CLOSURE FOR TARGET DEPTHS 18,19,20`

## 1. Scope

MATH-087 does not expand the entire exact-address one-paid tree.  It uses MATH-086's phase-only lower envelope to identify the only phase regions in which a negative Bellman margin is still possible, back-propagates those regions, and restores exact dyadic address only inside that corridor.

The audit must therefore verify that the two-stage reduction cannot discard an actual negative-margin path.

## 2. Positive phase-only cells may be removed safely

The phase-only model forgets dyadic address and retains the smallest accumulated penalty coefficient for an identical `(H, phase interval)` state.  It is therefore a lower-cost over-approximation.

If such a phase-only cell already has nonnegative terminal lower-envelope margin, every actual address-compatible realization beneath it has margin at least as large.

Hence removing phase-positive cells before address restoration is safe. `PASS`.

## 3. Negative cells are not pruned

Every phase-only cell whose lower-envelope margin can be negative is retained.  MATH-087 back-propagates its phase predecessors to depth 1 and then replays exact MATH-085 dyadic congruence transitions forward inside that corridor.

Thus a phase-negative cell is treated as a request for finer resolution, not as evidence of failure and not as a pruning condition. `PASS`.

## 4. Corridor filtering

At every exact forward level MATH-087 retains an exact address state whenever its current phase interval intersects the backward danger region of that depth.

Intersection rather than equality is deliberately conservative: it may retain extra exact states when the phase-only region is coarser than the exact state, but cannot remove a state whose phase lies in the danger corridor.

`PASS`.

## 5. Terminal audit

For target depths 18, 19 and 20, every exact singleton child generated from the final exact corridor parent set is evaluated with

\[
J=\mathcal P_{\inf}-\frac{19}{503}(H-73)
\]

for `H>73`, with the exact current-phase penalty infimum from MATH-085 coordinates.

Certified populations:

- depth 18: `50,133` exact singleton children, zero negative margins;
- depth 19: `2,816` exact singleton children, zero negative margins;
- depth 20: `12` exact singleton children, zero negative margins.

The respective observed minimum margins are approximately `1.9565`, `2.1052`, and `2.6101`, all strictly positive.

`PASS`.

## 6. Coverage consequence

MATH-086 proves that an actual multi-source one-paid chain cannot survive through a 20th macro.  MATH-087 therefore closes the top three possible source-resolution layers, but this does not interpolate over the untreated middle depths.

The detailed one-paid Bellman frontier becomes

\[
7\le t\le17.
\]

`PASS AS CLAIM-SCOPE UPDATE`.

## 7. Prohibited upgrades

Do not infer:

- closure at 18--20 `=>` closure at 7--17;
- phase lower-envelope model `=` exact address dynamics;
- absence of negative Bellman margin `=>` an independent ordinary-descent result;
- one-paid Bellman closure `=>` mixed multi-paid closure;
- first-cell emptiness;
- Collatz.

## 8. Verdict

MATH-087 passes the DSD audit.  Its reduction is monotone in the safe direction: coarse phase analysis only removes regions already certified nonnegative, while every potentially negative region is resolved by exact dyadic same-integer compatibility before a closure claim is made.
