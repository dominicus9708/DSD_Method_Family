# DSD Audit — Collatz MATH-089 terminal phase-address wedge

Date: 2026-09-12

Status: `PASS / EXACT LOCAL PHASE-ADDRESS COUPLING / NOT GLOBAL CLOSURE`

## 1. Scope

This audit reviews the exact local coupling between source-family resolution, terminal Bellman overshoot, and dyadic address zero-extension for one-paid edges.

## 2. Resolution/address equivalence

For a parent family with `M` source parameters and

\[
R_{res}=\lceil\log_2M\rceil,
\]

an edge of resolution `h>R_res` selects one residue `s_h mod 2^h`.
Writing

\[
s_h=s_R+2^{R_{res}}\zeta
\]

gives

\[
s_h<M
\iff
\zeta=0\ \text{and}\ s_R<M.
\]

This is elementary exact integer arithmetic. `PASS`.

The number

\[
z=h-R_{res}
\]

is therefore both:

1. the resolution overshoot left after the MATH-074 source-resolution potential;
2. the number of extra high dyadic residue bits that must all be zero for the terminal edge to exist.

This identification is exact and not probabilistic. `PASS`.

## 3. Phase law

MATH-083/085 current-phase coordinates give

\[
p=c\Omega_{out},
\qquad c\in\{1/4,1/8\},
\]

with exact output-phase branch ranges `(1/2,2/3)` and `(8/9,1)` respectively.
Hence `p>1/9` globally. `PASS`.

## 4. Danger conjunction

A locally negative terminal contribution requires

\[
c\Omega_{out}<\lambda z,
\qquad\lambda=19/503,
\]

and actual address compatibility simultaneously.
Therefore the MATH-089 conjunction

\[
\zeta=0,
\quad s_R<M,
\quad c\Omega_{out}<\lambda z
\]

is a safe necessary condition for terminal danger. `PASS`.

It is not a sufficient condition for a global counterexample.

## 5. Universal pruning consequences

Because `1/9>2 lambda`, every terminal with `z<=2` is automatically safe.
For `z=3`, the `c=1/4` branch is automatically safe since `1/8>3 lambda`; only the `c=1/8` branch below `456/503` can remain locally dangerous.

These are exact arithmetic consequences. `PASS`.

## 6. DSD interpretation

MATH-089 provides the clearest current bridge between two previously separate descriptors:

- analytic/phase deficit;
- dyadic address resolution.

The same integer `z` measures both the uncancelled Bellman length charge and the number of high address bits whose zero-extension is required.

This supports using `(R_res,z,Omega_out,address residue)` as a common state interface across depth, one-paid macro, and AP-resolution analyses.

## 7. Prohibited upgrades

Do not infer:

- zero-extension requirement `=>` probabilistic rarity;
- `z<=2` safety `=>` every terminal has `z<=2`;
- phase-address wedge `=>` all macro depths are closed;
- Bellman safety `=>` ordinary descent;
- one-paid closure `=>` first-cell emptiness or the Collatz conjecture.

## 8. Verdict

`PASS` as an exact reusable terminal pruning lemma.  The next calculation should classify the remaining depth-16 and lower danger corridor by `z` first, then perform exact address lifting only for the small phase subregions that survive the local wedge.
