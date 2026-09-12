# DSD Audit — Collatz MATH-093 dyadic resolution envelope

Date: 2026-09-12

Status: `PASS / SAFE SUPERSET ENVELOPE / EXACT RESOLUTION POTENTIAL INSIDE ENVELOPE`

## 1. Scope

MATH-093 replaces an exact finite source family `0<=s<M` by the larger dyadic family `0<=s<2^R`, where `R=ceil(log2 M)`.

## 2. Superset direction

Because `M<=2^R`, every actual source parameter is retained.  The envelope only adds fictitious source parameters.

Therefore:

- proving safety for the envelope implies safety for the actual family;
- finding a dangerous envelope path does not imply an actual dangerous path.

`PASS`.

## 3. Exact multi-edge resolution

For edge resolution `h<=R`, every residue modulo `2^h` occurs in the enlarged family and the child envelope has exactly `2^(R-h)` parameters.
Hence `R'=R-h` exactly. `PASS`.

## 4. Exact terminal overshoot

For `h>R`, the envelope contains at most one member of the selected residue class.  The remaining resolution overshoot is `z=h-R`, matching MATH-089's zero-extension bit count. `PASS`.

## 5. Potential identity

With `H_R=-lambda R`, multi-edge reduced cost simplifies exactly to the edge penalty `p`, while a terminal edge contributes `p-lambda z`.

Thus all possible negative reduced cost can be localized to the terminal edge **within the envelope model**. `PASS`.

## 6. DSD information-loss audit

The replacement `M -> 2^R` deliberately loses the exact upper cutoff of the source interval.  This loss enlarges the admissible language and therefore is one-sided safe for exclusion/safety proofs.

No density or independence interpretation is permitted.

## 7. Prohibited upgrades

Do not infer:

- envelope compatibility `=>` actual compatibility;
- envelope danger `=>` actual danger;
- terminal localization `=>` phase alone closes the problem;
- MATH-093 `=>` remaining macro depths are already closed;
- one-paid Bellman safety `=>` ordinary descent or Collatz closure.

## 8. Verdict

`PASS`.  MATH-093 is the preferred proof-facing abstraction for the remaining one-paid Bellman search because it makes the source-resolution potential exact and removes macro-depth accumulation from the multi-edge part of the argument.
