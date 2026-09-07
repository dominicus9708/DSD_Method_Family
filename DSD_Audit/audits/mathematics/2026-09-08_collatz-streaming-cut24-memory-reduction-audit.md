# DSD-AUDIT-20260908-MATH-029 — Collatz streaming cut-24 memory reduction

Date: 2026-09-08

Verdict:

`CONFIRMED / EXACT REORDERING / COMPUTATIONAL MEMORY REDUCTION / FINITE ONLY`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Can the exact MATH-028 `r<=10^9` combined lifting + rolling computation be reordered so that the same finite state tree and the same terminal outputs are preserved while simultaneous prefix storage is substantially reduced?

## DSD tuple

### D — Definition

The finite domain, coefficient-survival predicate, 339 internal boundaries, and exact endpoint transitions are exactly those of MATH-028.

MATH-029 changes only the enumeration schedule.

### R — Resolution

Every prefix state retains the full exact tuple needed downstream:

\[
(r,T^k(r),q_k,k).
\]

At depth 61 the exact ordinary endpoint is address-lifted and continued by the previously audited exact 11-step rolling operator.

No phase-only or truncated state replaces an exact propagated endpoint.

### S — Selection

The bounded-lift tree is first generated breadth-first through

\[
K_{\rm cut}=24.
\]

This produces exactly

\[
286,581
\]

surviving cut-frontier states after `735,398` branch attempts.

Each cut state is then expanded independently by DFS through depth 61.  No candidate is dropped merely because another state appears similar.

### E — Exclusion

MATH-029 makes no new mathematical exclusion.

It reproduces the existing MATH-028 finite outputs:

- depth-61 survivors: `1,796,718`;
- first right offset: `703`;
- last right offset: `999,999,207`;
- deepest failing rolling-window base: `545`;
- first witness at that base: `(r,b)=(378,620,799,1183)`;
- zero states survive the audited rolling continuation through depth 1029.

Thus the inherited finite same-endpoint coupling exclusion remains

\[
61\le k\le3,000,000,003.
\]

### T — Transition

The post-cut DFS performs

\[
186,328,593
\]

bounded-lift branch attempts. Hence

\[
735,398+186,328,593
=187,063,991,
\]

exactly matching the total MATH-028 bounded-lift branch count.

This equality, together with the complete terminal-output regression, confirms that the operation is an enumeration-order change rather than state pruning.

### C — Consistency

The breadth-first MATH-028 peak live prefix count was

\[
11,894,128.
\]

MATH-029 has cut frontier `286,581` and audited maximum local DFS stack `7`.

For 16 workers, algorithmic simultaneous prefix storage is therefore

\[
286,581+16\cdot7=286,693,
\]

for an exact live-state-count reduction factor

\[
\frac{11,894,128}{286,693}\approx41.49.
\]

Machine-specific resident-memory measurements are diagnostic only; the stable claim is the algorithmic live-state count.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / COMPUTATIONAL MEMORY REDUCTION / FINITE ONLY`.

This is not a new Collatz pruning theorem.

### O — Outcome

Established:

- exact cut-frontier + DFS streaming decomposition;
- identical bounded-lift branch-attempt total to MATH-028;
- identical finite depth-61 survivor set statistics and rolling-continuation frontier;
- approximately `41.49x` reduction in 16-worker algorithmic live-prefix storage.

Still open:

- optimal cut depth for larger right-offset domains;
- right offsets above `10^9`;
- mathematical compression of the remaining exact state tree;
- first-cell emptiness;
- Collatz.

## AP-2 / aliasing check

No state aliasing or quotient merge occurs. The reduced memory comes solely from consuming subtrees before generating unrelated subtrees.

Therefore AP-2 finite-state aliasing is not invoked.

## Prohibited upgrades

Do not infer:

- storage reduction ⇒ mathematical state exclusion;
- observed RSS ratio ⇒ portable theorem-facing speed/memory ratio;
- exact finite reordering at `r<=10^9` ⇒ arbitrary-domain numerical result;
- inherited endpoint-coupling exclusion ⇒ first-cell or Collatz closure.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_streaming_cut24_lifting_rolling_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-streaming-cut24-lifting-rolling-memory-reduction.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-029`
