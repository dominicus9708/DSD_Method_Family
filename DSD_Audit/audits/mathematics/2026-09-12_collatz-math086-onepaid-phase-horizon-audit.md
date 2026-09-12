# DSD Audit — Collatz MATH-086 one-paid phase-only horizon

Date: 2026-09-12

Status: `PASS AS AN OVER-APPROXIMATE HORIZON CERTIFICATE / NOT BELLMAN CLOSURE`

## 1. Scope

MATH-086 strengthens the one-paid macro analysis in two ways:

1. the universal one-paid penalty floor is improved from `p>1/12` to `p>1/9`;
2. exact dyadic address is deliberately forgotten to build a larger phase-only language, and that larger language is shown to have no possible multi-source state after macro depth 20 when combined with MATH-084's `multi-source => H<=71` theorem.

The first universal cell and the Collatz conjecture remain open.

## 2. Penalty-floor audit

MATH-085 gives the exact current-phase law

\[
p_e=c_e\Omega',
\qquad c_e\in\{1/4,1/8\}.
\]

For the `c_e=1/4` branch its exact image phase domain lies in `(1/2,2/3)`, so

\[
p_e>1/8.
\]

For the `c_e=1/8` branch the exact image phase domain lies in `(8/9,1)`, so

\[
p_e>1/9.
\]

Therefore

\[
\boxed{p_e>1/9}
\]

for every canonical one-paid macro.  `PASS`.

The strengthened phase-free sufficient wedge

\[
171(H-73)\le503t
\]

follows algebraically for `lambda=19/503`.  It remains sufficient, not necessary.

## 3. Address forgetting is an enlargement, not pruning

MATH-086 merges canonical edges only after erasing address and only when they have the identical phase map data `(H,rho,c)` and overlapping phase domains.

This operation can create spurious paths that fail the real dyadic congruence, but it cannot remove an actual phase-compatible edge.

Likewise exact duplicate phase states retain the smallest accumulated penalty coefficient.  This can only make the lower-cost language larger/harder to close.

Therefore the phase-only language is a proof-safe over-approximation for horizon and lower-bound purposes. `PASS`.

## 4. Interaction with MATH-084

MATH-084 independently proves

\[
\text{actual multi-source}\Longrightarrow H\le71.
\]

MATH-086 propagates the larger phase language only inside `H<=71`.  It finds 13 possible phase states at macro depth 19 and zero at macro depth 20.

Because every actual multi-source state is contained in that phase-only language,

\[
\boxed{\text{actual multi-source one-paid chain has at most 19 macros}.}
\]

A compatible 20th macro is necessarily source-resolving. `PASS`.

This is stronger than the MATH-084 length-only bound `t<=23`, but it does not assert that every phase-only terminal crossing is an actual address-compatible state.

## 5. Depth-4--6 consequence

The stronger `1/9` floor and MATH-085 terminal maxima give

\[
H_{max}(4)=84,\quad H_{max}(5)=87,\quad H_{max}(6)=90.
\]

Each satisfies

\[
171(H-73)<503t.
\]

Hence the MATH-085 depth-4--6 terminal sets are now certified by the phase-free wedge alone.  Their earlier exact phase-infimum audit remains a valid independent regression.

`PASS`.

## 6. What phase-only negative margins mean

Some address-forgotten terminal crossings retain a negative lower-envelope margin.  This does not imply an actual low-cost same-integer path.

The correct hierarchy is

\[
\text{phase-only negative cell}
\to
\text{restore exact dyadic address}
\to
\text{re-evaluate actual terminal cylinders}.
\]

This is essential because earlier work already proved that phase/correction credit cannot replace exact compatibility address.

## 7. Prohibited upgrades

Do not infer:

- phase-only language `=` actual Collatz language;
- phase-only negative margin `=>` actual obstruction;
- finite multi-source horizon `=>` every terminal is Bellman-safe;
- Bellman-safe terminal `=>` ordinary descent;
- one-paid horizon closure `=>` first-cell closure;
- MATH-086 `=>` Collatz.

## 8. Verdict

MATH-086 passes the DSD audit as a conservative over-approximate horizon certificate and as a strict strengthening of the one-paid universal penalty floor.

The preferred continuation is not raw depth enumeration.  It is danger-frontier analysis: retain only phase-only cells whose lower-envelope Bellman margin can still be negative, then restore exact dyadic address only on those cells.
