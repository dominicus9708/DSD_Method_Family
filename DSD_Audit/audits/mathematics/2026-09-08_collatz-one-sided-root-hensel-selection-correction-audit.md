# DSD-AUDIT-20260908-MATH-040 — one-sided root-Hensel selection correction

## Verdict

`CONFIRMED / SELECTION_ERROR CORRECTED / FIRST ONE-SIDED HENSEL PRUNING AT DEPTH 6 / FINITE EXACT`

Collatz conjecture remains `OPEN`.

The first universal Farey cell remains `OPEN`.

## Audited correction

MATH-037–039 selected both members of a Hensel collision from the coefficient-surviving language.  That is valid for the two-sided collision subproblem, but it is too restrictive for the actual root-Hensel maximality obligation.

The correct selection is asymmetric:

\[
\boxed{
\text{candidate}\in\mathcal L_{\rm coeff},
\qquad
\text{competitor}\in\mathcal L_{\rm arbitrary}.
}
\]

The arbitrary competitor need not itself satisfy the minimal-counterexample coefficient spine.

## Exact first event

The corrected audit finds no one-sided domination through depth 5 and exactly one at depth 6.

For that event,

\[
k=6,\qquad q=4,
\]

\[
C_{\rm cand}=65,
\qquad
C_{\max}=146.
\]

Since

\[
146-65=81=3^4,
\]

the ordinary-start credit is

\[
\boxed{d=1}.
\]

The candidate residue is

\[
\boxed{N\equiv15\pmod{64}},
\]

and the competitor residue is `14 mod 64`.

Therefore

\[
T_u^6(N-1)=T_w^6(N),
\]

and root minimality excludes the candidate residue class throughout the current first-cell window.

## Direct finite counts

The certificate audits all coefficient-surviving candidates against unrestricted Hensel class maxima through depth 26.  Selected results:

| depth | candidates | dominated | max credit |
|---:|---:|---:|---:|
| 6 | 8 | 1 | 1 |
| 10 | 64 | 12 | 1 |
| 16 | 2,114 | 394 | 1 |
| 18 | 7,495 | 1,391 | 3 |
| 20 | 27,328 | 5,084 | 7 |
| 24 | 286,581 | 52,425 | 7 |
| 25 | 573,162 | 105,267 | 15 |
| 26 | 1,037,374 | 189,881 | 15 |

Counts at different depths overlap and are not additive exclusions.

## DSD tuple

### D — Describability

Candidate and competitor roles are different objects and are represented separately.

### R — Resolution

Exact finite depth through 26; exact `(q,C mod 3^q)` Hensel class; exact ordinary-start residue modulo `2^k`.

### S — Selection

- Candidate selection: frozen published-floor coefficient-surviving language.
- Competitor selection: unrestricted parity words of the same `(k,q)` Hensel class.

This corrects the prior symmetric selection when interpreting root-Hensel maximality.

### E — Exclusion

A candidate is excluded only if the unrestricted class maximum has larger correction and the resulting positive credit is legal.  At the first event the credit is exactly 1 and is trivially below every first-cell start.

### T — Transition

For correction difference

\[
C_u-C_w=d3^q,
\]

the exact fixed-fiber identity gives

\[
T_u^k(N-d)=T_w^k(N).
\]

No density, probability, or residue-frequency substitution is used.

### C — Consistency

The targeted reverse-Hensel oracle exactly reproduces the complete per-depth one-sided counts through depth 26 and the first witness `(6,4,65,146)`.

### N — Norm

`ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.

MATH-037–039 remain valid only as two-sided coefficient-language collision records.  Their earlier wording as the first non-vacuous Hensel pruning is superseded.

### O — Outcome

The actual root-Hensel route is materially stronger than the symmetric collision route.  One-sided pruning starts at depth 6.

The current preferred computational object is an unrestricted Hensel class-max oracle queried only on coefficient-surviving candidate classes.

## First-cell residue count

The nonzero residue `15 mod64` occurs exactly

\[
340\cdot2^{55}
=12{,}249{,}790{,}986{,}447{,}749{,}120
\]

times in the current open first-cell window.  This is a finite exact count of starts removed by the first one-sided event, not a density theorem.

## Prohibited upgrades

- MATH-037 depth 34 = first actual Hensel pruning — **SUPERSEDED / PROHIBITED**.
- competitor must satisfy coefficient survival — **PROHIBITED**.
- dominated counts across depths may be summed — **PROHIBITED**.
- finite depth-26 result ⇒ depth-195 closure — **PROHIBITED**.
- one residue class removed ⇒ first-cell emptiness — **PROHIBITED**.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_one_sided_root_hensel_selection_correction_certificate.cpp`

Certificate commit:

`487adff3f3451fd549b6168571ff8f66d75cc40d`

Explanatory note:

`collatz/notes/2026-09-08-one-sided-root-hensel-selection-correction.md`

Note commit:

`a2a5c1dd2e9f712fd81b30b327fd17a814c5e792`
