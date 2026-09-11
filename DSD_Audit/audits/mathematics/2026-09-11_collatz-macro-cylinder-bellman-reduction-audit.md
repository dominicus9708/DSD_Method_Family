# DSD Audit — Collatz macro-cylinder / Bellman reduction

Date: 2026-09-11
Status: `PARTIALLY CONFIRMED / REPRESENTATION REPAIRED / GLOBAL BELLMAN CLOSURE OPEN`

## Audited chain

This audit covers the current Math-verification sequence

- MATH-058R — paid-exit source-cylinder bookkeeping repair;
- MATH-059 — arithmetic-progression one-paid macro cylinders and Bellman target correction;
- MATH-060 — first-cell envelope and sufficient global penalty slope `19/503`;
- MATH-061 — exact cylinder composition and 73-bit ordinary-source handoff;
- MATH-062 — exact consecutive-phase lower bound reducing detailed multi-paid counts to `2..64`.

The mathematical domain norm remains ordinary proof validity. DSD analysis is used only to identify state completeness, duplicate information, lineage loss, invalid quotienting, and scope boundaries.

## 1. MATH-058R bookkeeping repair

### Defect

The original MATH-058 certificate represented the same paid-exit phase/address source more than once: one record was emitted per parity-compatible lift `t`, while the downstream routine ignored that stored `t` and re-enumerated the full lift interval.

### DSD diagnosis

This was a **duplicate-lineage representation error**, not a mathematical contradiction. One source cylinder had been represented by several records which were then each expanded as if independent.

### Repair

Retain one source cylinder

\[
(\text{phase interval},R,E_0,q,[t_{\min},t_{\max}])
\]

and solve the recovery congruence exactly once downstream.

### Verdict

`SAFE AFTER REPAIR`.

The corrected certificate reproduces the intended canonical table

\[
69:(20,1),\quad70:(4,0),\quad71:(4,0),\quad72:(0,0).
\]

## 2. MATH-059 state compression

A one-paid source family is exactly compressible as

\[
Y=A+2^H s
\longmapsto
Y'=B+3^Q s.
\]

The same cylinder carries an exact phase interval, exact phase multiplier, and exact scalar penalty coefficient.

### DSD verdict

`SAFE COMPLETE REPRESENTATION WITHIN THE ONE-PAID MACRO SCOPE`.

The compression removes endpoint-lift enumeration without removing any future-relevant coordinate used by the macro continuation.

## 3. Rejected edgewise optimization

Candidate claim:

\[
\beta_e\Omega-\frac{17}{450}\ell_e>0
\]

for every legal macro edge.

Verdict: `REJECT`.

The unique long `L=69` one-paid edge violates this edgewise condition on its legal phase interval, yet its exact continuation is transient and reaches coefficient failure after the chain

\[
71\text{-step one-paid}
\to3\text{-step one-paid}
\to10\text{-step four-paid}
\to\text{failure}.
\]

### DSD lesson

`locally negative adjusted edge` is not equivalent to `globally sustainable low-mean path`.

The correct object is a Bellman/potential or minimum-mean-cycle inequality on a future-complete state.

## 4. MATH-060 target slope

Using the exact first-cell continued-fraction mediant structure and a two-block Denjoy-Koksma bound, MATH-060 derives a rigorous first-cell penalty ceiling. Relative to the conservative 89-step endpoint overhead, a global lower bound

\[
\mathcal P_K\ge\lambda(K-89)
\]

with

\[
\lambda=\frac{19}{503}
\]

would be sufficient to close the first universal cell.

### Verdict

`SAFE AS A SUFFICIENT TARGET, NOT AS AN ESTABLISHED LOWER BOUND`.

Do not confuse the target inequality with a theorem already proved for Collatz paths.

## 5. MATH-061 composition closure

Exact composition preserves

\[
Y_0=A+2^H s,
\qquad
Y_1=B+3^Q s.
\]

Appending a second macro imposes one dyadic congruence on `s`, hence the composed source remains one residue class modulo the product dyadic modulus. Phase intervals pull back exactly and min-plus coefficients update exactly.

### 73-bit handoff

The audited `u=0` anchor ceiling is below `2^73`. Therefore once accumulated macro length reaches 73 bits, the composed source residue class contains at most one ordinary source anchor.

This is a resolution theorem, not a density statement.

### Finite regression

For the 910 exact one-paid cylinders, all ordered pairs give 12,530 nonempty exact two-macro compositions. 1,141 of those have a singleton ordinary source. Every singleton target descends to `<=2^71` within at most 71 shortcut steps.

### Verdict

`SAFE FINITE SAME-INTEGER CLOSURE FOR THE SINGLETON TWO-MACRO SUBSET`.

## 6. Relation to the periodic negative-ghost theorem

The pre-existing theorem proves that an eventually-periodic coefficient-surviving parity tail has negative rational fixed point

\[
x=\frac{C(p)}{2^H-3^S}<0.
\]

MATH-061 does not replace this theorem. The two results cover different resolution layers:

- periodic infinite symbolic repetition -> negative ghost;
- finite macro composition -> exact dyadic source resolution and direct ordinary-integer handoff.

The genuinely aperiodic symbolic branch remains open.

## 7. MATH-062 phase-sum reduction

Inside one paid cluster, every paid odd has `u>=1`, so

\[
p_j\ge\frac{\Omega_j}{6}.
\]

The paid odd events advance the odd-count phase consecutively even when even steps occur between them. Therefore the cluster penalty is bounded by one consecutive phase sum, not by independent `1/12` minima.

Exact rational phase minimization proves that every multi-paid cluster with

\[
r\ge65
\]

already has positive adjusted cost at target slope `19/503` under the MATH-058 length bound.

Thus detailed negative-edge analysis is required only for

\[
2\le r\le64.
\]

### Verdict

`SAFE FINITE REDUCTION OF AN UNBOUNDED PAID-COUNT CHANNEL`.

## 8. Current future-complete state requirement

The remaining Bellman state must preserve enough information to decide future legal composition. At minimum:

\[
(\text{dyadic source cylinder},
\text{current endpoint affine image},
\text{source phase interval},
\text{phase multiplier},
\text{penalty coefficient},
\text{macro class}).
\]

An exact `S=C/3^q` coordinate may replace redundant exact real/Hensel/dyadic projections only when the replacement remains exact. A scalar real bound on `S` is not a safe substitute for same-integer address lineage.

## 9. Prohibited upgrades

- corrected MATH-058 table `=>` original certificate had no defect;
- one-paid cylinder compression `=>` all multi-paid dynamics compressed;
- negative-ghost periodic closure `=>` aperiodic closure;
- 73-bit singleton resolution `=>` few length-73 cylinders;
- 1,141 singleton descents `=>` all one-paid chains closed;
- `r>=65` automatic safety `=>` all multi-paid clusters safe;
- sufficient target `19/503` `=>` target already proved globally;
- first-cell closure, if later obtained, `=>` all later Farey cells or Collatz.

## 10. Next audited target

Construct the exact mixed macro system containing

1. one-paid cylinders under MATH-061 composition;
2. only the detailed multi-paid cylinders with `2<=r<=64`;
3. already-nonnegative summary transitions for `r>=65` where connectivity information is still needed;
4. exact singleton handoff at 73 accumulated dyadic bits.

Then test a Bellman potential for

\[
\mathcal P_e-\frac{19}{503}\ell_e+H(s')-H(s)\ge0.
\]

The remaining proof-facing obstruction is the genuinely aperiodic low-mean same-integer path.
