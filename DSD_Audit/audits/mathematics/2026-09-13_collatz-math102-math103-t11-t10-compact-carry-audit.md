# DSD Audit — Collatz MATH-102/103 one-paid t=11 and t=10 compact-carry closures

Date: 2026-09-13

Status: `PASS AS EXACT FINITE t=11,t=10 CLOSURES / NOT FIRST-CELL CLOSURE`

Both certificates use the already-audited architecture:

1. address-forgotten phase lower-envelope to define a safe danger superset;
2. restoration of every actual first-macro state intersecting that superset;
3. exact normalized 2-adic compact carry propagation;
4. terminal testing only after the universal `p>1/9` overshoot bound is applied.

For `t=11`, any negative terminal must have `z>=33`; complete replay over 254 roots yields `991,302,455` danger-edge attempts, `0` address-compatible danger edges, and strict minimum residue gap `514`.

For `t=10`, any negative terminal must have `z>=30`; complete replay over 300 roots yields `882,659,777` danger-edge attempts, `0` address-compatible danger edges, and strict minimum residue gap `548`.

Independent root sharding does not merge cross-root duplicates and therefore cannot delete a candidate. The compact precision `73+R` remains future-complete for all remaining multi-edge resolution plus one terminal edge.

Verdict:

\[
\boxed{t=11\text{ CLOSED}},\qquad
\boxed{t=10\text{ CLOSED}}.
\]

The detailed unresolved one-paid frontier is

\[
\boxed{7\le t\le9}.
\]

Do not infer paid-count `r=10/11` closure, first-cell emptiness, or the Collatz conjecture.
