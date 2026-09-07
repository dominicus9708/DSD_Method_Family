# DSD-AUDIT-20260908-MATH-034 — Collatz base-independent 22-step full continuation

Date: 2026-09-08

Verdict:

`CONFIRMED / EXACT CONTINUATION ACCELERATION / FINITE ONLY`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Can the MATH-033 base-independent 22-step critical-prefix gate replace the depth-83+ 11-step threshold sequence in the complete finite `RMAX=10^9` continuation while preserving the exact ordinary endpoint and reproducing the MATH-028/032 result?

## DSD tuple

### D — Definition

The finite domain, depth-61 survivor set, 339 internal address labels, MATH-031 prefilter, and final candidate predicate are unchanged.

Only the depth-83+ threshold evaluation is regrouped from 11-step blocks to 22-step blocks.

### R — Resolution

Each 22-bit residue stores the MATH-033 critical threshold descriptor

\[
(j_*,s_*).
\]

The threshold at base `K` is exactly

\[
q_{\rm pub}(K+j_*)-s_*.
\]

The propagated endpoint is **not** reduced to this descriptor.  It remains exact.

### S — Selection

The MATH-031 cyclic prefilter leaves exactly

\[
189,767,400
\]

depth-83 exact address states from the `1,796,718` depth-61 right-offset survivors.

All of those states enter the MATH-034 continuation.

### E — Exclusion

At each base `K=83,105,127,...`, a state is rejected exactly when its current odd-count is below the base-independent critical threshold.

No heuristic or approximate threshold is used.

### T — Transition

A one-shot 22-step affine numerator can overflow a 128-bit intermediate.  That implementation route was identified during audit and rejected.

The final engine therefore performs endpoint arithmetic as two already-audited exact 11-step affine updates after a successful 22-step threshold gate.

This yields:

- depth-83 instantiations: `189,767,400`;
- depth-83+ 22-step threshold gates: `294,223,428`;
- endpoint overflow: `0`;
- audited-end survivors: `0`.

### C — Consistency

The final finite output matches MATH-028 and MATH-032 exactly:

- deepest failing base `545`;
- first witness `(r,b)=(378,620,799,1183)`;
- inherited finite internal adjacent-block same-endpoint exclusion through

\[
3,000,000,003.
\]

MATH-032 used `467,202,551` 11-step threshold checks from base 83 onward. MATH-034 uses `294,223,428` 22-step gates, a reduction of

\[
172,979,123
\]

checks, approximately `37.02%`.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / COMPUTATIONAL ACCELERATION / FINITE ONLY`.

The mathematical finite exclusion is unchanged; the exact evaluation path is improved.

### O — Outcome

Established:

- MATH-033 descriptor functions as an actual arbitrary-base rolling gate;
- safe exact endpoint propagation by sequential audited 11-step updates;
- complete finite regression against MATH-028/032;
- depth-83+ threshold-gate count reduced by about 37.02%.

Still open:

- larger right-offset domains;
- further exact compression of the surviving continuation;
- full first-cell halo;
- first-cell emptiness;
- Collatz.

## AP-2 / implementation audit

The threshold descriptor and propagated exact state are kept distinct.  No truncated residue is treated as a complete downstream state.

The discarded one-shot 128-bit 22-step arithmetic is an implementation anti-pattern, not evidence against the mathematical descriptor.

## Prohibited upgrades

Do not infer:

- fewer threshold gates ⇒ stronger theorem;
- threshold-count reduction ⇒ equal wall-clock speedup;
- base-independent local gate ⇒ base-independent complete Collatz state;
- finite same-endpoint exclusion ⇒ first-cell or Collatz closure.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_base_independent_tail22_full_continuation_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-base-independent-tail22-full-continuation.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-034`
