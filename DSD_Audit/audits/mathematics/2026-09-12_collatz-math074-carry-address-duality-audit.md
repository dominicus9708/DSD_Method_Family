# DSD audit — Collatz MATH-074 carry/address duality

Date: 2026-09-12

Status: `SAFE COMPARISON-STATE REDUCTION / ABSOLUTE-STATE MERGE NOT CLAIMED`

## Audited objects

- MATH-051 fixed-d bounded-carry Hensel solver;
- MATH-072 common coordinate `S = 1 + Sigma - rho`;
- MATH-073 absolute dyadic source-resolution height `R`;
- MATH-074 3-adic carry envelope.

## 1. Exact cross-description identity

For fixed `(k,d)`, hence fixed `rho`,

\[
\Delta S=\Delta\Sigma.
\]

If `r` lower gap levels remain and `h_r` is the MATH-051 carry after all higher gap levels have been processed, then

\[
\boxed{
\Delta S_{>r}
=\Delta\Sigma_{>r}
=\left(\frac23\right)^r h_r.
}
\]

Therefore `h_r` is not an independent analytic variable. It is an integer-state encoding of a partial normalized-correction difference.

## 2. 3-adic / 2-adic duality

For two primitive comparison states at equal remaining competitor count `n_B`,

\[
h_2-h_1=c3^r
\]

implies

\[
\Delta S_{>r}^{(2)}-\Delta S_{>r}^{(1)}=c2^r.
\]

Hence equal carry residue modulo `3^r` corresponds exactly, under matched lower completion, to equality of the partial normalized-correction translation modulo `2^r`.

This is a genuine structural bridge between the depth-41 carry description and the dyadic source-resolution description.

## 3. Exact dominance reduction

Under the same lower candidate and competitor block choices, a carry difference `c3^r` evolves as

\[
2^j c3^{r-j}
\]

after `j` lower-level transitions and ends as the positive terminal credit difference

\[
2^r c.
\]

Therefore, for fixed `n_B` and fixed residue `eta mod 3^r`, any smaller carry is future-dominated by the largest carry in that class.

The exact canonical comparison envelope is

\[
\boxed{
\mathcal E_r(n_B,\eta)
=\max\{h:(n_B,h),\ h\equiv\eta\pmod{3^r}\}.
}
\]

Removing non-maximal members preserves the existential question of whether any competitor can complete to positive exact Hensel translation credit.

## 4. Depth-41 regression

The envelope-modified MATH-051 solver reproduces the canonical difficult central dominated counts exactly:

- `D(41,12)=361,499,293`;
- `D(41,13)=586,723,760`;
- `D(41,14)=703,863,494`;
- `D(41,15)=355,002,462`.

The maximum primitive competitor-set sizes decrease from

`33,46,100,147`

to

`23,33,44,68`.

These reductions support the implementation but are not themselves proof claims. The proof-facing point is preservation of the exact dominated counts together with the algebraic envelope lemma.

## 5. Critical DSD separation

### Absolute path state

The Bellman analysis concerns one path and currently uses quantities such as

\[
(S,\rho,\Omega,R).
\]

`R` is an absolute same-integer source-resolution resource.

### Comparison state

The Hensel dominance solver compares a candidate path with possible competitors. Its state contains relative quantities such as

\[
(n_A,n_B,h)
\]

or the canonical envelope `E_r`.

The comparison envelope must not be silently promoted to an independent scalar Bellman potential.

## 6. Safe synthesis

It is safe to say

\[
\boxed{
\text{bounded carry}
\leftrightarrow
\text{scaled partial }\Delta S
\leftrightarrow
\text{finite dyadic address translation}.
}
\]

It is also safe to use the carry envelope as an exact dominance/quotient operator on histories while using `H_R=-lambda R` as an absolute path potential.

## 7. Prohibited upgrades

Do not infer:

- that the carry envelope has depth-independent bounded size;
- that `E_r` itself is a scalar Lyapunov/Bellman potential;
- that `(S,rho,Omega,R)` is already a future-complete finite quotient;
- that fixed-depth Hensel dominance closes the first universal Farey cell;
- that MATH-074 closes any of `2<=r<=13`;
- that Collatz is proved.

## 8. Next audited target

Test whether all address-sensitive pruning needed after MATH-073 can be expressed as:

1. absolute dyadic resolution `R` for pathwise Bellman accounting; and
2. relative carry envelope `E_r` for exact dominance between histories;

without introducing a fifth independent analytic coordinate.

If successful, the common description would reduce to one analytic path state plus one exact comparison operator rather than two unrelated state systems.
