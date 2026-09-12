# DSD Audit — Collatz MATH-095 phase-resolution Bellman negative result

Date: 2026-09-13

Status: `PASS AS NEGATIVE STATE-SUFFICIENCY RESULT / ADDRESS-CARRY CHANNEL REQUIRED`

## 1. Scope

This audit checks MATH-095's conclusion that exact phase, resolution, and accumulated positive penalty are still insufficient after exact dyadic address compatibility is forgotten.

The claim under audit is a state-sufficiency claim, not a Collatz-descent claim.

## 2. Safe over-approximation direction

MATH-095 uses the MATH-093 dyadic envelope and removes exact address compatibility. This enlarges the represented path language. Therefore a negative Bellman value in the envelope cannot be promoted to existence of an actual same-integer negative path.

`PASS`.

## 3. Exact Bellman recursion

For current resolution `R` and phase `Omega`, the recursion

\[
V_R(\Omega)=\min_e
\begin{cases}
 c_e\rho_e\Omega-\lambda(h_e-R),&h_e>R,\\
 c_e\rho_e\Omega+V_{R-h_e}(\rho_e\Omega),&h_e\le R
\end{cases}
\]

retains the complete positive penalty inside the address-forgotten envelope. Because every multi-edge satisfies `h>=3`, recursive calls strictly decrease `R`.

`PASS`.

## 4. Finite exact result

All 857 actual multi-source first-macro phase states are evaluated with exact rational arithmetic. Including the first-macro penalty, every lower-envelope value satisfies

\[
-5/2<J_{env}<-2.
\]

The certificate therefore establishes that restoring penalty alone does not repair the address-forgotten abstraction.

`PASS`.

## 5. DSD interpretation

The failure localizes missing information. The following proof-facing state reductions are now rejected:

\[
(R,\Omega)
\]

and

\[
(R,\Omega,\text{penalty}).
\]

The information discarded by both is exact same-integer compatibility. MATH-088 independently demonstrates the same phenomenon: a large phase-danger set can have zero address-compatible realization.

Thus a successful state must retain a channel equivalent to

\[
\boxed{\mathcal C_2=\text{2-adic carry/address compatibility}.}
\]

`PASS`.

## 6. Relation to MATH-090 and MATH-092

MATH-090 expresses terminal compatibility by a low-residue condition and a carry divisibility condition,

\[
r_R<M,\qquad \nu_2(C_R)\ge h-R.
\]

MATH-092 expresses the same address dynamics as a normalized 2-adic transducer. These results provide exact candidate representations for the missing channel but do not yet prove that a bounded quotient is sufficient through the whole remaining frontier.

## 7. Prohibited upgrades

Do not infer:

- negative envelope value `=>` actual bad path;
- failure of address-forgotten Bellman recursion `=>` failure of the `19/503` target;
- carry/address necessity `=>` a particular finite carry truncation is already sufficient;
- MATH-095 `=>` closure or disproof of the first universal cell.

## 8. Verdict

MATH-095 passes as an exact **negative state-minimality result**. It sharply narrows the next search: the remaining quotient must combine phase/resolution with an exact finite 2-adic carry/address channel rather than trying further address-free Bellman refinements.
