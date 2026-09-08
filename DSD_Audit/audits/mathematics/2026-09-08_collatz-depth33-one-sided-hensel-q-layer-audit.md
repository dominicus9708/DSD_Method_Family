# DSD-AUDIT-20260908-MATH-043 — depth-33 one-sided Hensel q-layer audit

## Verdict

`CONFIRMED / ONE-SIDED ROOT-HENSEL PRUNING / FINITE EXACT`

Collatz conjecture remains `OPEN`.

The first universal Farey cell remains `OPEN`.

## Audited claim

At depth 33, the coefficient-surviving candidate language splits exactly by Hensel odd-count q. Within each q-layer, candidates are compared against arbitrary same-class parity words using the exact key `(q, C mod 3^q)`.

The combined exact result is

\[
82{,}694{,}966
\to
67{,}727{,}277.
\]

Thus cumulative Hensel removal through depth 33 is

\[
\boxed{14{,}967{,}689}.
\]

From the exact MATH-042 survivor set, depth 33 admits `67,760,822` coefficient-valid children before the new Hensel comparison, so the newly removed set at depth 33 has size

\[
\boxed{33{,}545}.
\]

## DSD tuple

### D — Describability

The state separates candidate role, competitor role, q-layer, Hensel residue, correction, and prior-prefix survival lineage.

### R — Resolution

Exact finite depth 33; exact q-layers `21..33`; exact residue modulo `3^q`; exact correction maximum.

### S — Selection

Coefficient survival constrains only candidates. Arbitrary parity-word competitors are retained without imposing the candidate coefficient gate.

### E — Exclusion

A candidate is excluded iff a same-q, same-residue arbitrary competitor has strictly larger correction. The audited depth satisfies the existing arithmetic-credit safety requirement.

### T — Transition

MATH-013 downstream dominance makes current-depth non-maximality hereditary under common suffixes. Hence current-depth unrestricted class-max filtering is compatible with the all-prefix one-sided Hensel requirement.

### C — Consistency

- `q=23..33` completed in the descending full run;
- `q=22` independently rerun as a standalone exact layer;
- `q=21` independently rerun with OpenMP partitioning by the smallest zero position;
- the companion post-audit recombines all q-layers and independently checks the transition from the MATH-042 q-distribution.

The exact q-layer survivors sum to `67,727,277`.

### N — Norm

`ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.

Execution partitioning does not change the mathematical state space.

### O — Outcome

Depth 33 is closed for the current one-sided root-Hensel gate. The corrected Hensel route continues to give concrete finite pruning, but it does not prove the first universal cell empty.

## Exact layer totals

The two heaviest layers are:

\[
q=21:\quad13{,}472{,}296\to10{,}907{,}449,
\]

\[
q=22:\quad26{,}521{,}599\to21{,}566{,}825.
\]

Across all q-layers, cumulative removed candidates equal `14,967,689`.

The exact new depth-33 removals from MATH-042 survivors equal `33,545`.

## Prohibited upgrades

- finite depth-33 pruning ⇒ first-cell emptiness — **PROHIBITED**;
- finite layer ratios ⇒ probability or density — **PROHIBITED**;
- Hensel-max prefix ⇒ complete Collatz candidate validity — **PROHIBITED**;
- depth-33 result ⇒ arbitrary-depth Hensel theorem — **PROHIBITED**.

## Reproducibility

Math-verification per-q certificate:

`collatz/src/2026_09_08_depth33_one_sided_hensel_q_layer_certificate.cpp`

Commit:

`a6390f6eb73f9226ab31ece03160d079b94efee7`

Post-audit:

`collatz/src/2026_09_08_depth33_one_sided_hensel_post_audit.cpp`

Commit:

`938be0398c35420c0399fd15c3aa125ee56dd8f2`

Explanatory note:

`collatz/notes/2026-09-08-depth33-one-sided-hensel-q-layer-audit.md`

Commit:

`977344463646095b28a68223dca33087d8b61c67`
