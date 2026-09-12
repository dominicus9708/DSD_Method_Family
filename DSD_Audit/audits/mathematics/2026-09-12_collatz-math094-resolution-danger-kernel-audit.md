# DSD Audit — Collatz MATH-094 resolution-indexed danger kernel

Date: 2026-09-12

Status: `PASS AS SAFE OVER-APPROXIMATION / NUMERICAL KERNEL EXECUTION STILL TO BE FROZEN`

## 1. Scope

MATH-094 replaces macro-depth indexing by dyadic envelope resolution `R` and defines an address-forgotten phase danger set `D_R`.

## 2. Resolution DAG

Under MATH-093 every multi-edge updates `R'=R-h` exactly, with `h>=3`.  Therefore recursion in `R` is acyclic.  The first unresolved one-paid envelope satisfies `R<=69` from the first-cell source-window width and the minimum first-edge resolution.

`PASS`.

## 3. Danger recursion

The recursion includes:

- preimages of `D_(R-h)` through every multi-edge `h<=R`;
- terminal phase regions satisfying `c*rho*Omega < lambda(h-R)` for `h>R`.

This is the correct phase-only necessary language after the dyadic envelope abstraction. `PASS`.

## 4. One-sided information loss

Two pieces of information are deliberately dropped:

1. exact dyadic address compatibility;
2. positive penalties already paid on earlier multi-edges.

Both omissions can only add danger candidates, not remove actual ones.  Therefore exclusion of a phase from `D_R` is safe, while inclusion in `D_R` is not itself evidence of an actual dangerous path.

`PASS`.

## 5. Claim boundary

MATH-094 currently provides the exact recursion and executable generator, but the complete numerical interval table for `R=0..69` has not yet been frozen into a canonical certificate summary.

Therefore the correct status is structural reduction, not completed one-paid closure.

## 6. Verdict

`PASS AS SAFE OVER-APPROXIMATION`.

The next calculation should freeze the exact `D_R` interval table and intersect it with the actual first-macro states before restoring the MATH-092/090 address-carry channel.
