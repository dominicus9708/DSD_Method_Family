# DSD-AUDIT-20260908-MATH-037 — coefficient-language Hensel collision frontier

## Verdict

`CONFIRMED / FIRST NON-VACUOUS HENSEL PRUNING IN COEFFICIENT LANGUAGE / FINITE EXACT`

Collatz conjecture remains `OPEN`.

The first universal Farey cell remains `OPEN`.

## Audited claim

Within the frozen published-floor coefficient-surviving parity language:

1. the previously completed full finite scan found no root-Hensel class collision through depth 33 and exactly five collision classes at depth 34;
2. an independent targeted certificate re-extracts all five depth-34 classes in the minimal `q=22` layer;
3. every one of the five has correction-credit difference exactly `4`;
4. therefore the lower-correction representative excludes one concrete ordinary-start residue class modulo `2^34` by comparison with the start four units smaller.

## Exact data

All five collisions have

\[
q=22,
\qquad
C_{\rm high}-C_{\rm low}=4\cdot3^{22}.
\]

The exact Hensel residues are

\[
4{,}015{,}726{,}592,
4{,}559{,}922{,}176,
5{,}240{,}166{,}656,
8{,}585{,}544{,}704,
9{,}875{,}489{,}792.
\]

The excluded ordinary-start residue classes modulo `2^34` are

\[
5{,}348{,}744{,}191,
7{,}435{,}082{,}751,
11{,}843{,}133{,}439,
15{,}231{,}450{,}879,
15{,}257{,}926{,}655.
\]

For each class, the competing start residue is exactly four smaller.

## DSD tuple

### D — Describability

The object is a root-Hensel translation-class collision among parity prefixes that also satisfy the coefficient-survival gate at every prefix. This is narrower than unrestricted symbolic Hensel collision and narrower than complete Collatz candidate elimination.

### R — Resolution

Exact finite depth 34; exact `q=22`; exact correction modulo `3^22`; exact ordinary-start residue modulo `2^34`.

### S — Selection

Only coefficient-surviving prefixes under the frozen published-floor minimal-counterexample spine are selected. Unrestricted symbolic words are not mixed into the candidate-language count.

### E — Exclusion

Within each of the five classes, the lower-correction representative is excluded because the higher-correction representative at ordinary start `N-4` reaches the same endpoint. Since all first-cell starts are greater than `2^71`, the positive credit 4 is safely smaller than the candidate start.

### T — Transition

The exact fixed-fiber identity is

\[
C_{\rm high}-C_{\rm low}=4\cdot3^{22}.
\]

Therefore

\[
T^{34}_{\rm high}(N-4)=T^{34}_{\rm low}(N).
\]

The Hensel-class statement is thus transferred back to an actual smaller ordinary integer without dropping the same-integer lineage.

### C — Consistency

The targeted certificate counts

- `26,521,599` coefficient-surviving depth-33 `q=22` parents;
- `13,472,296` coefficient-surviving depth-33 `q=21` parents;
- exactly five q=22 cross-branch collision classes at depth 34.

These five coincide with the five total depth-34 classes found by the earlier full external-partition scan.

### N — Norm

`ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.

Sparse event counts are not treated as probabilities or asymptotic densities.

### O — Outcome

Root-Hensel maximality is vacuous on the coefficient-surviving language through depth 33 and becomes non-vacuous at depth 34. Five concrete low-34-bit ordinary-start residue classes are excluded.

The first universal cell is not proved empty.

## Calculation-direction consequence

The coefficient-surviving class-max DP remains too large for a direct depth-195 expansion, while actual collision events are initially extremely sparse. The preferred route is therefore a sparse Hensel-event engine:

1. propagate already-existing collision classes under valid child transitions;
2. search only for genuinely new even/odd class intersections;
3. translate every event back to ordinary-start credit before candidate exclusion.

## Prohibited upgrades

- five residue classes excluded ⇒ first cell empty — **PROHIBITED**;
- sparse at depth 34 ⇒ sparse for all depths — **PROHIBITED**;
- unrestricted Hensel collision ⇒ coefficient-language collision — **PROHIBITED**;
- class collision without legal positive credit ⇒ candidate excluded — **PROHIBITED**;
- finite absence through depth 33 ⇒ universal injectivity — **PROHIBITED**.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_coefficient_hensel_depth34_collision_certificate.cpp`

Certificate commit:

`1da66a0245af8b8baa3d2c20ab5ceecf47785593`

Explanatory note:

`collatz/notes/2026-09-08-coefficient-language-hensel-singleton-frontier.md`

Note commit:

`c613866fb66893f169bdc0ef662d70cbb16b324f`
