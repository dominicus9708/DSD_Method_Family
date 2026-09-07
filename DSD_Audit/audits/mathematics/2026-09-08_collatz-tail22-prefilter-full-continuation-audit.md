# DSD-AUDIT-20260908-MATH-032 — Collatz 22-step prefilter full-continuation regression

Date: 2026-09-08

Verdict:

`CONFIRMED / EXACT CONTINUATION ACCELERATION / FINITE ONLY`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Can the MATH-031 exact 22-step cyclic-window prefilter replace the first two address-level 11-step rolling windows of MATH-028, instantiate only depth-83 survivors, and still reproduce the complete finite continuation result on `0<=r<=10^9`?

## DSD tuple

### D — Definition

The finite domain and candidate predicate are unchanged from MATH-028.

The only algorithmic substitution is

\[
(61\to72)+(72\to83)
\]

as two separate per-address rolling checks versus one exact local 22-step descriptor plus cyclic address aggregation.

### R — Resolution

The 22-step local decision uses `n mod 2^22`, but every surviving state reconstructs and propagates the full exact endpoint

\[
T^{83}(N)
=\frac{3^{s_{22}(u)}T^{61}(N)+c_{22}(u)}{2^{22}}.
\]

No residue-only state is propagated beyond depth 83.

### S — Selection

Exact finite counts:

- depth-61 right-offset survivors: `1,796,718`;
- raw internal address states: `609,087,402`;
- states surviving the first legacy 11-step window: `333,913,383`;
- states surviving both first windows / 22-step gate: `189,767,400`.

Only the last set is instantiated as exact depth-83 endpoints.

### E — Exclusion

All states failing either of the first two coefficient-survival windows are excluded from deeper continuation by the exact complete local predicate.

The remaining `189,767,400` exact depth-83 states are continued without approximation.

### T — Transition

From base depth 83 onward, the existing audited 11-step rolling operator executes

\[
\boxed{467,202,551}
\]

window checks.

The final finite output exactly matches MATH-028:

- zero states survive through the audited end;
- zero fixed-width endpoint overflows;
- deepest failing base `545`;
- first witness `(r,b)=(378,620,799,1183)`.

Thus the inherited finite internal adjacent-block same-endpoint coupling exclusion remains

\[
61\le k\le3,000,000,003.
\]

### C — Consistency

The legacy rolling engine would perform

\[
609,087,402+333,913,383+467,202,551
=1,410,203,336
\]

address-level 11-step window checks.

The first two windows alone account for

\[
\boxed{943,000,785}
\]

per-address checks.

MATH-032 replaces those by one cyclic range query per depth-61 leaf and exact endpoint creation only for the depth-83 survivors.

This is not stated as an equal wall-clock speedup because table construction, range-query, bitset extraction, and endpoint reconstruction also cost work.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / COMPUTATIONAL ACCELERATION / FINITE ONLY`.

The mathematical finite exclusion is unchanged from MATH-028; only the exact evaluation path is improved.

### O — Outcome

Established:

- exact substitution of the first two rolling windows by MATH-031;
- exact depth-83 endpoint reconstruction;
- complete finite output regression against MATH-028;
- `943,000,785` legacy per-address first-two-window checks removed from the continuation path;
- post-depth-83 continuation reduced to `467,202,551` exact rolling-window checks.

Still open:

- compression of the depth-83+ continuation;
- larger right-offset domains;
- full first-cell halo;
- first-cell emptiness;
- Collatz.

## AP-2 / representation audit

The residue descriptor selects only the exact local predicate and affine update. The exact ordinary endpoint is reconstructed before any deeper continuation. Therefore no finite residue alias is promoted to a global state equivalence.

## Prohibited upgrades

Do not infer:

- fewer finite threshold checks ⇒ stronger theorem;
- operation-count reduction ⇒ identical wall-clock ratio;
- 22-step local completeness ⇒ arbitrary-depth completeness;
- finite endpoint-coupling exclusion ⇒ candidate emptiness;
- computational acceleration ⇒ Collatz proof.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_tail22_prefilter_full_continuation_regression.cpp`

Math-verification note:

`collatz/notes/2026-09-08-tail22-prefilter-full-continuation-regression.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-032`
