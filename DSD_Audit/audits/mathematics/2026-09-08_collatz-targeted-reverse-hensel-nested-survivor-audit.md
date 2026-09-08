# DSD-AUDIT-20260908-MATH-041 — targeted reverse-Hensel nested survivor engine

## Verdict

`CONFIRMED / EXACT TARGETED CLASS-MAX ORACLE / NESTED ONE-SIDED PRUNING THROUGH DEPTH 31 / COMPUTATIONAL ACCELERATION`

Collatz conjecture remains `OPEN`.

The first universal Farey cell remains `OPEN`.

## Audited claim

After the MATH-040 selection correction, the root-Hensel competitor is arbitrary.  Instead of constructing the complete unrestricted Hensel class table, MATH-041 reconstructs only the class requested by an actual coefficient-surviving candidate.

The resulting targeted class maximum agrees with the earlier one-sided counts through depth 26 and extends the nested all-prefix Hensel filter exactly through depth 31.

## Reverse-Hensel oracle

For odd positions

\[
p_1<\cdots<p_q<k,
\]

write the correction recursively as

\[
C=3C_{q-1}+2^{p_q}.
\]

Given `r=C mod 3^q`, each possible last odd position satisfies

\[
2^{p_q}\equiv r\pmod3,
\]

and yields the exact previous residue

\[
r_{q-1}\equiv\frac{r-2^{p_q}}3\pmod{3^{q-1}}.
\]

Recursive enumeration with decreasing position bounds enumerates precisely the arbitrary words in the queried Hensel class.  The maximum reconstructed correction is therefore the exact unrestricted class maximum.

## Downstream-stable exclusion

MATH-013 proves that lower `h` in a Hensel class remains lower under either common child transition.  Hence a prefix that fails class maximality can never become maximal later.

This licenses immediate pruning:

\[
\boxed{\text{non-maximal prefix}\Rightarrow\text{do not expand descendants}.}
\]

## Exact finite result

At depth 31:

\[
\#\mathcal L_{\rm coeff}=23{,}642{,}078,
\]

while candidates satisfying coefficient survival and all-prefix one-sided Hensel maximality are

\[
\boxed{19{,}347{,}686}.
\]

Thus the cumulative Hensel removal inside the coefficient language is

\[
\boxed{4{,}294{,}392}
\]

low-31-bit candidate residue classes.

The current first-cell window contains each nonzero residue modulo `2^31` exactly `340*2^30` times, so the corresponding finite ordinary-start count is

\[
\boxed{7{,}063{,}302{,}682{,}978{,}549{,}760}
\]

remaining after these two prefix conditions through depth 31.

This is not a terminal first-cell survivor count; later prefix, address, first-crossing, and correction conditions remain.

## Selected nested rows

| depth | full coefficient | generated from previous Hensel survivors | final survivors | newly pruned |
|---:|---:|---:|---:|---:|
| 24 | 286,581 | 234,332 | 234,156 | 176 |
| 26 | 1,037,374 | 848,189 | 847,493 | 696 |
| 27 | 1,762,293 | 1,443,156 | 1,442,349 | 807 |
| 28 | 3,524,586 | 2,884,698 | 2,882,872 | 1,826 |
| 29 | 6,385,637 | 5,230,056 | 5,226,985 | 3,071 |
| 30 | 12,771,274 | 10,453,970 | 10,446,423 | 7,547 |
| 31 | 23,642,078 | 19,359,254 | 19,347,686 | 11,568 |

## DSD tuple

### D — Describability

Objects are separated into candidate prefix, Hensel class residue, and arbitrary competitor class members.

### R — Resolution

Exact finite depths through 31 and exact ternary class residue.  No phase truncation is used.

### S — Selection

- descendants are generated only from candidates that survived every earlier coefficient and Hensel gate;
- arbitrary competitors are generated only inside a queried candidate class.

### E — Exclusion

Candidate prefix is removed iff its correction is strictly below the exact unrestricted class maximum.  MATH-012 guarantees the relevant credit mechanism is uniformly safe in this shallow-depth regime.

### T — Transition

MATH-013 downstream dominance proves deleted lower-`h` representatives cannot recover after a common suffix.

### C — Consistency

- targeted oracle reproduces MATH-040 one-sided results through depth 26;
- exact survivor regressions are fixed through depth 31;
- first one-sided event remains `(k,q,C,Cmax)=(6,4,65,146)`.

### N — Norm

`ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.

### O — Outcome

The unrestricted global class table is no longer required for shallow continuation.  Candidate-requested reverse-Hensel reconstruction is the preferred Hensel oracle.

Depth 32 remains computationally unresolved in the current single-run implementation and is the next partition target.

## Prohibited upgrades

- 19,347,686 low-31-bit classes ⇒ complete first-cell survivor set — **PROHIBITED**;
- depth31 ⇒ depth195 — **PROHIBITED**;
- finite class-count fraction ⇒ density theorem — **PROHIBITED**;
- targeted computation ⇒ universal proof — **PROHIBITED**.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_targeted_reverse_hensel_nested_survivor_certificate.cpp`

Certificate commit:

`4c3a914c00efdb394866c9242a0d32f7272e5f08`

Explanatory note:

`collatz/notes/2026-09-08-targeted-reverse-hensel-nested-survivor-engine.md`

Note commit:

`390bf8511592cb77635d39597782649d4969ace6`

Controlling scope correction: MATH-040.
