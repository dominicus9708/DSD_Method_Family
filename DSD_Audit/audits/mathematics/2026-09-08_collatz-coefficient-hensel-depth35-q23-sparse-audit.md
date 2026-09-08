# DSD-AUDIT-20260908-MATH-038 — depth-35 q=23 sparse Hensel-event audit

## Verdict

`CONFIRMED WITHIN q=23 LAYER / SPARSE EVENT STRUCTURE / FULL DEPTH-35 SET OPEN`

Collatz conjecture remains `OPEN`.

The first universal Farey cell remains `OPEN`.

## Audited claim

At depth 35, restricted to the coefficient-surviving `q=23` layer:

- five collision classes are inherited from the five depth-34 `q=22` classes of MATH-037 via the odd-child transition;
- exactly fifteen genuinely new q=23 classes arise from even-child q=23 / odd-child q=22 cross-branch intersections;
- the inherited and new sets are disjoint.

Thus the audited q=23 layer contains exactly twenty collision classes.

No statement is made here about possible depth-35 collision classes with `q>23`.

## DSD tuple

### D — Describability

The object is the **event set of Hensel class mergers** at one exact q layer, not the full candidate-word population.

### R — Resolution

Exact depth 35, exact q=23, exact class residues modulo `3^23`.

### S — Selection

Parents must satisfy the coefficient-survival gate through depth 34. The transition is split into inherited same-class events and genuinely new even/odd cross-branch intersections.

### E — Exclusion

Event counting alone is not candidate exclusion. Any downstream ordinary-start exclusion still requires an exact positive Hensel credit and same-integer translation. MATH-037 supplies this for its five primitive depth-34 classes; newly formed q=23 events require their own credit audit before being promoted to candidate elimination.

### T — Transition

For class residue `r`:

- even child: `r` unchanged at the same q;
- odd child: `(3r+2^k) mod 3^(q+1)`.

Same-bit maps preserve an existing collision. Therefore genuinely new class mergers can only appear in an even/odd cross-branch intersection.

### C — Consistency

The exact targeted scan verifies:

- `47,993,022` depth-34 q=23 parent classes, with no internal duplicate class residue;
- `39,993,895` depth-34 q=22 words;
- `15` new q=23 cross-branch target classes;
- `0` overlaps between those new classes and the `5` inherited q=23 collision images.

### N — Norm

`ESTABLISHED_WITHIN q=23 FINITE SCOPE`.

The full depth-35 collision set remains `OPEN` because higher-q layers are not closed by this certificate.

### O — Outcome

The sparse event representation is computationally justified at the minimal q layer: a population of tens of millions of parent words produces only twenty known q=23 collision events after inheritance plus new cross intersections.

The next target is a partitioned/external-memory q=24 cross-branch scan at depth 36. A monolithic sort attempt exceeded the session execution limit and is explicitly excluded from evidence.

## Prohibited upgrades

- twenty q=23 classes ⇒ twenty total depth-35 collisions — **PROHIBITED**;
- sparse q=23 event set ⇒ asymptotically sparse Hensel structure — **PROHIBITED**;
- timed-out depth-36 computation ⇒ mathematical evidence — **PROHIBITED**;
- class merger without positive-credit verification ⇒ ordinary-start exclusion — **PROHIBITED**.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_coefficient_hensel_depth35_q23_sparse_certificate.cpp`

Certificate commit:

`edd96c6688def6733646ad1347620f057db5ead4`

Explanatory note:

`collatz/notes/2026-09-08-coefficient-hensel-depth35-q23-sparse-events.md`

Note commit:

`f6765f066da0f1893dc763eeb24eedf8135e568e`
