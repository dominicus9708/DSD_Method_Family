# DSD-AUDIT-20260907-MATH-007 — Collatz block-label right-congruence barrier

Date: 2026-09-07
Domain: Mathematics / Collatz
Primary repository: `dominicus9708/Math-verification`

## Outcome

**Verdict: CONFIRMED compression barrier.**

For the exact 340-label coefficient-survival task from depth61 to depth72, low-surplus states `q61=39,...,43` admit no nontrivial quotient of `y mod2048` that preserves the complete surviving-label set. All 2048 endpoint residues are pairwise distinguishable by their 340-bit survival masks.

This is a negative but useful audit: it prunes an invalid coarse-state strategy before it is used in the proof line.

## Object under audit

For fixed `q61` and `y mod2048`, define the mask over labels `a=1024,...,1363` whose exact 11-bit continuation keeps coefficient survival through depth72.

A right-congruence class is defined by equality of the full 340-bit mask.

## Exact results

| q61 | exact mask classes |
|---:|---:|
| 39 | 2048 |
| 40 | 2048 |
| 41 | 2048 |
| 42 | 2048 |
| 43 | 2048 |
| 44 | 1838 |
| 45 | 341 |
| 46–61 | 1 |

## Eight-axis audit

### D — Describability

PASS.

The compared state is exactly `(q61,y mod2048)` and the observable is the complete 340-label survival mask.

### R — Resolution

PASS.

All 2048 endpoint residues are retained before quotienting, and quotienting is permitted only under exact mask equality.

### S — Selection

PASS.

The 340 labels are the already-certified current top-address set. No unrelated addresses are inserted.

### E — Exclusion

PASS AS STRATEGY EXCLUSION.

For `q61=39,...,43`, every nontrivial identification of two endpoint residues changes the exact label-survival mask. Therefore such a quotient is excluded as an exact proof state.

### T — Transition / lineage

PASS.

The mask is generated from the same ordinary start through the exact affine endpoint relation. No representative substitution occurs.

### C — Consistency

PASS.

The result is consistent with MATH-006: the strongest label-count pruning occurs exactly where endpoint-phase information is maximally noncompressible.

### N — Norm

PASS.

The criterion is exact preservation of all candidate labels, not approximate accuracy or average behavior.

### O — Outcome

CONFIRMED.

The next compression must exploit **reachability restrictions on endpoint phases** or a richer structural relation; it cannot simply throw away `y mod2048` in the low-surplus branch.

## Critical logical distinction

For fixed `q` and fixed block label `a`, varying `y` translates `y+a3^q` through every residue modulo2048. Therefore

\[
\text{at most 47 labels survive for each }y
\]

does **not** imply

\[
\text{293 labels are globally impossible}.
\]

The identity of the surviving labels depends on the exact endpoint phase.

## Required prohibited upgrades

- do not replace endpoint phase by odd count alone for `q61=39,...,43`;
- do not infer globally bad labels from pointwise mask cardinalities;
- do not read mask-class counts as entropy or probability;
- do not infer first-cell or Collatz closure.

## Evidence

Certificate commit:

`0ab28726a671b9c0e74ddaeded4e39cc6514ba19`

Explanatory note commit:

`420d9158ae294c8e1adaaf78b85a5067b0ef3ac9`

Upstream transducer audit:

`DSD-AUDIT-20260907-MATH-006`

## Next audited transition

Compute the actually reachable subset of `(q61,y mod2048)` produced by lower-61 universal-spine starts. Only that reachability relation can determine whether the endpoint-phase barrier is active in the real candidate language or merely in the ambient residue space.