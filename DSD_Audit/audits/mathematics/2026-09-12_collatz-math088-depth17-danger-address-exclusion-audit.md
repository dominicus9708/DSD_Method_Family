# DSD Audit — Collatz MATH-088 depth-17 danger-address exclusion

Date: 2026-09-12

Status: `PASS / FINITE EXACT DEPTH-17 BELLMAN EXCLUSION / NO GLOBAL CLOSURE CLAIM`

## 1. Scope

This audit reviews the one-paid macro-depth-17 result obtained by phase-only danger localization followed by exact dyadic address restoration.

The audit distinguishes:

- phase lower-envelope danger;
- actual same-integer address compatibility;
- Bellman reduced-cost safety;
- ordinary Collatz descent.

Only the first three enter MATH-088.

## 2. Phase-only over-approximation

Removing dyadic address conditions enlarges the admissible language.  Therefore using the phase-only lower envelope to identify all cells that can still have negative Bellman margin is safe as a first filter.

A phase cell with a nonnegative lower-envelope margin cannot contain a more dangerous actual address-compatible path.

`PASS`.

A negative phase-only cell is not a counterexample and must not be discarded without restoring address compatibility.

## 3. Exact address restoration

For each retained parent and canonical edge, actual composition requires

\[
s\equiv(A_e-B)(3^Q)^{-1}\pmod{2^{h_e}},
\qquad 0\le s<M.
\]

Because `3^Q` is odd, the inverse modulo `2^{h_e}` exists and the residue class is unique.

The complete depth-17 replay checks 5,330,013 phase-danger attempts from 595,738 exact parent states and finds zero residues inside the corresponding source ranges.

`PASS`.

## 4. Address-gap diagnostic

The frozen replay summary gives

\[
M_{\max}=4,239,
\qquad
s_{\min}=9,498,993,710,400.
\]

Therefore

\[
s_{\min}>M_{\max},
\]

which independently explains the zero compatibility count for this finite corridor.

This numerical gap must not be promoted to a universal asymptotic theorem without a separate symbolic proof.

## 5. Same-integer lineage

No probabilistic independence or density inference is used.  The phase stage only enlarges the language.  The final exclusion is performed with the exact dyadic congruence inherited from the canonical MATH-061 cylinder composition.

`PASS`.

## 6. Claim hierarchy

Safe claim:

\[
\boxed{\text{one-paid macro depth }17\text{ has no negative actual Bellman terminal}}
\]

Unsafe upgrades include:

- depth 17 safety `=>` depths 7--16 safety;
- Bellman safety `=>` ordinary descent for every represented integer;
- zero address-compatible danger edges `=>` a universal residue-gap law;
- one-paid depth closure `=>` first-cell emptiness;
- first-cell work `=>` the Collatz conjecture.

## 7. Verdict

MATH-088 passes the DSD audit.  Its strongest structural lesson is that the remaining Bellman obstruction can disappear not because the phase penalty becomes large enough, but because the phase-danger path has no compatible dyadic source address.

The next task should therefore search for a reusable address-gap descriptor, rather than simply extending raw macro depth.
