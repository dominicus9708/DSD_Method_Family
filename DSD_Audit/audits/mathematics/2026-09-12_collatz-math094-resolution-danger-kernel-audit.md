# DSD Audit — Collatz MATH-094 resolution-indexed danger kernel

Date: 2026-09-12

Status: `PASS / EXACT NEGATIVE RESULT / (R,PHASE) ALONE IS INSUFFICIENT`

## 1. Scope

MATH-094 replaces macro-depth indexing by the MATH-093 dyadic-envelope resolution `R` and computes the address-forgotten phase danger set `D_R`.

## 2. Exact result

The executable exact interval recursion gives

\[
\boxed{D_R=(1/2,1)\quad\text{for every }R=0,\ldots,69.}
\]

Thus the phase-only danger kernel saturates completely.

## 3. DSD interpretation

This is not a mathematical failure of the one-paid program.  It is an **insufficient-state result**.

The abstraction discarded both:

1. exact dyadic address/carry compatibility;
2. accumulated positive penalty from earlier multi-edges.

Because both omissions enlarge the language, saturation means only that `(R,phase)` cannot distinguish safe actual paths from fictitious low-cost paths.

`PASS`.

## 4. Cross-check with MATH-088

MATH-088 already demonstrates that a phase-danger corridor can be entirely fictitious: at depth 17, 5,330,013 phase-danger edge attempts yield zero address-compatible danger edges.

Therefore MATH-094 saturation is consistent with, rather than contradictory to, the exact address results.

## 5. State-minimality consequence

A depth-free quotient must retain at least one additional state channel beyond `(R,Omega)`.
Current exact candidates are:

- accumulated current-phase penalty credit;
- MATH-090 carry valuation;
- MATH-092 normalized 2-adic address word.

A quotient that drops all three is now explicitly rejected by counterexample/saturation.

## 6. Prohibited upgrades

Do not infer:

- `D_R` full `=>` actual danger exists for every phase;
- phase-only saturation `=>` Bellman strategy fails;
- exact address is necessarily required in full uncompressed form;
- MATH-094 `=>` any Collatz counterexample.

## 7. Verdict

`PASS AS A NEGATIVE MODEL-SELECTION RESULT`.

The bare `(R,phase)` abstraction should be retired.  The next route is a product quotient coupling resolution with carry/address credit and, where useful, accumulated penalty.
