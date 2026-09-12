# DSD Audit — Collatz MATH-082 one-paid resolution-bit Bellman wedge

Date: 2026-09-12

Status: `PASS AS SUFFICIENT PRUNING RULE / NOT A DESCENT THEOREM / LONGER CHAIN COVERAGE OPEN`

## 1. Scope

This audit reviews MATH-082's use of the audited `Y<2^73` source-anchor ceiling to construct a coarse source-resolution Bellman potential for composed one-paid chains.

The audit distinguishes three claims that must not be conflated:

1. Bellman/reduced-cost safety;
2. singleton source resolution;
3. ordinary Collatz descent to the frozen floor.

The Collatz conjecture and first universal Farey cell remain `OPEN`. Paid-count layers `2<=r<=13` are outside scope.

## 2. Coarse bit budget is exact as a ceiling-based potential

For accumulated exact source modulus depth `H`, define

\[
B(H)=\max(0,73-H).
\]

Under the audited source bound `Y<2^73`, reaching `H>=73` leaves at most one ordinary source anchor. Hence `B` is a valid coarse unresolved-address-bit budget.

It is **not** the same object as actual multiplicity resolution

\[
R_{res}=\lceil\log_2 M\rceil.
\]

`PASS`, subject to keeping the notation and semantics separate.

## 3. Bellman potential calculation

With `lambda=19/503`, MATH-082 sets

\[
H_{bit}=-\lambda B.
\]

For a path from accumulated depth 0 to `H`, exact telescoping gives

\[
J_{bit}=\mathcal P-\lambda H+H_{bit}(H)-H_{bit}(0).
\]

Therefore

\[
J_{bit}=\mathcal P
\quad(H\le73)
\]

and

\[
J_{bit}=\mathcal P-\lambda(H-73)
\quad(H>73).
\]

No probabilistic assumption enters this identity. `PASS`.

## 4. One-paid universal wedge

Each one-paid macro has one paid event at `u=1` and therefore penalty

\[
p=\Omega/6.
\]

On the audited boundary phase domain,

\[
1/2<\Omega\le1,
\]

so

\[
p>1/12.
\]

A `t`-macro chain has

\[
\mathcal P>t/12.
\]

Consequently the sufficient phase-free terminal condition

\[
228(H-73)\le503t
\]

for `H>73` is algebraically valid. `H<=73` is automatically safe for this reduced-cost comparison because the bit potential cancels the entire length charge.

`PASS AS A SUFFICIENT CONDITION`.

It is not a necessary condition; failing it does not imply a low-cost survivor.

## 5. Exact phase-infimum strengthening

A composed PathCylinder stores

\[
\mathcal P=\beta\Omega_0
\]

on an exact phase interval. Using `beta*Omega_lo` as the infimum is safe for proving a lower bound. The stronger test may certify a cylinder that the phase-free `t/12` bound does not.

`PASS`.

## 6. Depth-2 regression

Exact composition from multi-source first macros produces:

- new singleton handoffs: `1,137`;
- multi-source survivors: `11,389`.

The universal wedge certifies `1,136` handoffs.

The sole universal exception has `t=2`, `H=78`; its exact phase-infimum margin is strictly positive, so all `1,137` are reduced-cost safe.

This means ordinary trajectory continuation is unnecessary **for this penalty/Bellman pruning purpose**. It does not invalidate or replace MATH-061's independent same-integer descent audit.

## 7. Depth-3 regression

Exact composition gives:

- new singleton handoffs: `11,511`;
- multi-source survivors: `85,803`.

The universal wedge certifies `11,489`.

Exact phase-infimum bounds certify 20 of the remaining 22, leaving two cylinders, both with `t=3`, `H=84`.

Those two are not discarded analytically. They are handed to exact ordinary continuation and reach the frozen floor in 1 and 10 shortcut steps.

This respects the claim hierarchy:

\[
\text{failed sufficient cost test}
\not\Rightarrow
\text{failed descent}.
\]

`PASS`.

## 8. State reduction consequence

The new result gives an exact pruning order for future one-paid searches:

1. preserve exact source/address compatibility under cylinder composition;
2. when a singleton handoff appears, apply the universal bit/penalty wedge;
3. if needed, apply the exact phase-infimum test;
4. only then materialize the small residual set as ordinary integers.

This is preferable to materializing every singleton at creation time.

## 9. Interaction with MATH-060 additive allowance

The coarse bit potential spans 73 shortcut-step equivalents, while MATH-060 retained an 89-step additive allowance. Arithmetic therefore leaves 16 step-equivalents outside this potential.

This is compatible with the current architecture but does **not** prove that every other future potential/address endpoint term fits into the remaining 16.

No global Bellman closure is claimed.

## 10. Prohibited upgrades

Do not infer:

- Bellman-safe terminal `=>` ordinary descent has been proved for that integer;
- failure of the wedge `=>` a mathematical obstruction;
- depth-2/3 pruning efficiency `=>` identical efficiency through macro depth 24;
- 73-bit bit budget `=>` exact multiplicity equals `2^(73-H)`;
- MATH-082 `=>` one-paid aperiodic chains are closed;
- one-paid pruning `=>` first-cell emptiness.

## 11. Verdict

MATH-082 passes the DSD audit as an **exact sufficient pruning layer** that couples accumulated penalty to exact source-resolution depth.

Its most important methodological result is that the vast majority of early singleton handoffs need not be sent to ordinary continuation in the low-cost Bellman search.

The next high-value target is macro depth 4 and beyond using pruning at state creation, not post-hoc brute terminal continuation.
