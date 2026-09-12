# DSD Audit — Collatz MATH-092 normalized 2-adic address transducer

Date: 2026-09-12

Status: `PASS / EXACT COORDINATE CHANGE / FINITE-PRECISION SAFE`

MATH-092 replaces the current target intercept `B` by the normalized 2-adic coordinate

\[
X=3^{-Q}B.
\]

Because `3^Q` is a 2-adic unit, this is an invertible coordinate change at every finite dyadic precision.

The edge compatibility residue becomes

\[
r=(3^{-Q}A_e-X)\bmod2^h,
\]

and the child update is

\[
X'=(X+r-3^{-Q}A_e)/2^h+3^{-(Q+q_e)}B_e.
\]

The numerator is divisible by `2^h` by construction, so the right shift is exact.  If `P` future bits are retained before the transition, `P-h` bits are sufficient afterward.  No future-compatible address distinction inside those retained bits is lost.

`PASS`.

DSD interpretation: the large integer intercept is not itself the proof-facing state.  The proof-facing address state is a finite 2-adic word undergoing low-bit selection, carry division, and edge-dependent addition.  This is structurally comparable to the bounded-carry finite-state machinery used in the depth-41 Hensel calculation, while remaining a distinct compatibility channel.

Prohibited upgrades: coordinate compression does not itself prove Bellman safety, ordinary descent, first-cell emptiness, or the Collatz conjecture.
