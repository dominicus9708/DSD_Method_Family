# DSD-AUDIT-20260908-MATH-037 — two-sided coefficient-language Hensel collision frontier

## Revised verdict

`CONFIRMED / FIRST TWO-SIDED COEFFICIENT-LANGUAGE COLLISION / FINITE EXACT / SCOPE REVISED BY MATH-040`

Collatz conjecture remains `OPEN`.

The first universal Farey cell remains `OPEN`.

## Revision notice

The original MATH-037 arithmetic remains valid, but its former wording as the **first non-vacuous root-Hensel pruning** is superseded by MATH-040.

Reason: MATH-037 selected both collision members from the coefficient-surviving language. Actual root-Hensel maximality has asymmetric selection:

\[
\text{candidate}\in\mathcal L_{\rm coeff},
\qquad
\text{competitor}\in\mathcal L_{\rm arbitrary}.
\]

MATH-040 proves that one-sided pruning begins already at depth 6.

## Audited claim retained from MATH-037

Within the **two-sided coefficient-surviving language**:

1. there is no Hensel class collision through depth 33;
2. exactly five collision classes appear at depth 34;
3. all five have `q=22`;
4. every collision has credit difference exactly 4;
5. the lower-correction member in each class is genuinely excluded by comparison with the start four units smaller.

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

## DSD tuple

### D — Describability

Object: collision of two coefficient-surviving prefixes in the same Hensel translation class.

### R — Resolution

Exact finite depth 34, exact `q=22`, exact modulo `3^22` and modulo `2^34`.

### S — Selection

Symmetric coefficient-survival selection on both members. This is valid for the two-sided collision subproblem but is **not** the full root-Hensel competitor selection.

### E — Exclusion

Each lower-correction member is excluded by exact credit 4. Those exclusions remain valid.

### T — Transition

\[
C_{\rm high}-C_{\rm low}=4\cdot3^{22}
\]

implies

\[
T^{34}_{\rm high}(N-4)=T^{34}_{\rm low}(N).
\]

### C — Consistency

The original targeted q=22 certificate still reproduces all five two-sided collision classes.

### N — Norm

`ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.

The statement “root-Hensel maximality is vacuous through depth 33” is withdrawn. Only the statement “two-sided coefficient-language collision is absent through depth 33” remains.

### O — Outcome

MATH-037 remains a valid structural collision record, but MATH-040 controls actual one-sided root-Hensel pruning.

## Prohibited upgrades

- first two-sided collision ⇒ first actual Hensel pruning — **PROHIBITED**;
- no two-sided collision ⇒ no arbitrary competitor — **PROHIBITED**;
- sparse two-sided event count ⇒ sparse one-sided pruning — **PROHIBITED**;
- five residues excluded ⇒ first-cell emptiness — **PROHIBITED**.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_coefficient_hensel_depth34_collision_certificate.cpp`

Original certificate commit:

`1da66a0245af8b8baa3d2c20ab5ceecf47785593`

Revised explanatory note:

`collatz/notes/2026-09-08-coefficient-language-hensel-singleton-frontier.md`

MATH-040 controlling audit:

`DSD_Audit/audits/mathematics/2026-09-08_collatz-one-sided-root-hensel-selection-correction-audit.md`

MATH-040 audit commit:

`841a3930c3b286d039f521a0f1a679d31d287722`
