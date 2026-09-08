# DSD-AUDIT-20260908-MATH-042 — depth-32 one-sided Hensel flat class-max

## Verdict

`CONFIRMED / ONE-SIDED ROOT-HENSEL PRUNING / FINITE EXACT`

Collatz conjecture remains `OPEN`.

The first universal Farey cell remains `OPEN`.

## Audited claim

At depth 32, compare every coefficient-surviving candidate parity word against every arbitrary parity word in the same root-Hensel class `(q, C mod 3^q)`. Using MATH-013 downstream dominance, current-depth unrestricted class-maximality is sufficient for the all-prefix Hensel-max requirement within the audited finite range.

Exact result:

\[
41{,}347{,}483
\to
33{,}880{,}411.
\]

Thus

\[
\boxed{7{,}467{,}072}
\]

coefficient-surviving depth-32 prefixes are cumulatively excluded by one-sided root-Hensel maximality.

Relative to the exact MATH-041 nested depth-32 prefilter count `33,894,412`, the new depth-32 Hensel comparison excludes exactly

\[
\boxed{14{,}001}
\]

additional prefixes.

## DSD tuple

### D — Describability

Candidate and competitor are separate roles. Candidate belongs to the frozen coefficient-surviving language; competitor is arbitrary except for matching the same Hensel class.

### R — Resolution

Exact finite depth 32; exact q-layers `21..32`; exact residue modulo `3^q`; exact correction maxima.

### S — Selection

Coefficient survival constrains only the candidate. No coefficient-survival requirement is imposed on the competitor.

### E — Exclusion

A candidate is removed iff an arbitrary same-class competitor has strictly larger correction. At depth 32 all audited q-layers satisfy the previously established arithmetic-credit budget `k-q<=71`.

### T — Transition

MATH-013 downstream dominance is retained: once a prefix is non-maximal, appending the same suffix to the better competitor preserves a positive correction advantage, so the candidate cannot recover at a later current-depth maximum.

### C — Consistency

An independent flat-class-max regression at depth 31 reproduced the MATH-041 result exactly:

\[
23{,}642{,}078\to19{,}347{,}686.
\]

At depth 32, the q-layer survivor sum is exactly `33,880,411`, and the unrestricted competitor enumeration covers exactly `236,618,693` words.

### N — Norm

`ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.

No probability, density, or arbitrary-depth interpretation is used.

### O — Outcome

The one-sided Hensel route remains computationally effective after correcting the earlier two-sided selection mistake. Depth 32 is closed exactly, but neither the first universal cell nor Collatz is closed.

## Calculation method

Because depth-32 candidate q is at least 21, arbitrary competitors have at most 11 zero positions. The certificate enumerates arbitrary words by zero-position combinations and retains flat hash entries only for class residues actually queried by coefficient-surviving candidates.

This is a calculation acceleration, not a stronger theorem.

## Prohibited upgrades

- `7,467,072` excluded prefixes ⇒ first cell empty — **PROHIBITED**;
- exact finite depth 32 ⇒ arbitrary-depth Hensel maximality theorem — **PROHIBITED**;
- one-sided Hensel-max prefix ⇒ complete Collatz candidate validity — **PROHIBITED**;
- finite q-layer proportions ⇒ probabilistic or density claim — **PROHIBITED**.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_depth32_one_sided_hensel_flat_classmax_certificate.cpp`

Certificate commit:

`e3592b987e065d376b260b3921919bce58869088`

Explanatory note:

`collatz/notes/2026-09-08-depth32-one-sided-hensel-flat-classmax.md`

Note commit:

`00be19bc73e989be8f99ac66ad8d9dd414aea521`
