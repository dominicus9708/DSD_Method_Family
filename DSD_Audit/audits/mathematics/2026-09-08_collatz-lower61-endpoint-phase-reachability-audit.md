# DSD-AUDIT-20260908-MATH-008 — Collatz lower-61 endpoint-phase reachability saturation

Date: 2026-09-08
Domain: Mathematics / Collatz
Primary repository: `dominicus9708/Math-verification`

## Outcome

**Verdict: CONFIRMED exact constructive reachability / STRATEGY SATURATION.**

For the lower-61 universal coefficient-spine language, every endpoint phase modulo `2048` is actually realized for each odd count

\[
q_{61}=39,\ldots,58.
\]

The exact reachable-phase cardinalities are

\[
\#\operatorname{Reach}_{61}(q)=
\begin{cases}
2048,&39\le q\le58,\\
1166,&q=59,\\
58,&q=60,\\
1,&q=61.
\end{cases}
\]

Therefore every `q61` range in which MATH-006 has a nontrivial coefficient-only 340-label sieve (`q61=39,...,45`) already reaches the entire ambient endpoint-phase space. The proposed refinement "restrict MATH-006/007 to actually reachable lower-61 phases" yields no additional label elimination.

This is a negative strategy result, not a negative verdict on MATH-006 or MATH-007.

## Scope lock

Let

\[
T(n)=
\begin{cases}
 n/2,&n\text{ even},\\
 (3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For `0<=x<2^61`, define `q_k(x)` as the odd-step count in the first `k` shortcut steps.

The audited candidate language is exactly

\[
3^{q_k(x)}\ge2^k
\qquad(1\le k\le61).
\]

For fixed `q=q61(x)`, define

\[
\operatorname{Reach}_{61}(q)
=
\{T^{61}(x)\bmod2048:\ x\text{ satisfies the locked language and }q_{61}(x)=q\}.
\]

No later-block Hensel assumption is inserted into this calculation.

## Exact construction

For a valid length-`k` parity prefix, let `x_k` be its unique canonical representative in `[0,2^k)`, let `y_k=T^k(x_k)`, and let `q_k` be its odd count.

The two lifts to one extra address bit are

\[
x_k,
\qquad x_k+2^k,
\]

whose depth-`k` endpoints differ by exactly

\[
3^{q_k}.
\]

Since this difference is odd, the two endpoints have opposite parity. Hence a prescribed next parity bit selects exactly one lift.

This gives an exact integer recurrence that reconstructs the same ordinary start rather than replacing it by a coarse representative.

## Evidence mode

### q61=39,...,58

The certificate deterministically enumerates valid parity words in lexicographic order. For each newly observed endpoint phase it stores an ordinary-integer witness and reruns that witness directly under `T`.

The scan stops only after all `2048` phases have independently verified witnesses.

Since `2048` is the entire ambient residue space, explicit witnesses prove exact equality

\[
\operatorname{Reach}_{61}(q)=\mathbb Z/2048\mathbb Z.
\]

No probabilistic inference is used.

### q61=59,60,61

The valid languages are exhaustively enumerated:

- `q61=59`: 1,708 valid words -> 1,166 phases;
- `q61=60`: 59 valid words -> 58 phases;
- `q61=61`: 1 valid word -> 1 phase.

For `q61=61`, the unique canonical start is

\[
2^{61}-1,
\]

and its endpoint phase is `274`.

## Eight-axis audit

### D — Describability

PASS.

Ordinary start, parity word, cumulative odd count, universal-spine prefix condition, exact endpoint, and endpoint phase are all explicit.

### R — Resolution

PASS.

The calculation is performed at ordinary-integer witness resolution. The modulo-2048 projection is applied only to the final observable being audited.

### S — Selection

PASS.

Only lower-61 words satisfying the already-audited coefficient-survival prefix language are admitted.

### E — Exclusion

PASS AS STRATEGY EXCLUSION.

For `q61=39,...,45`, no endpoint phase can be excluded as unreachable, because all 2048 phases have explicit witnesses. Therefore phase-sparsity cannot be used to strengthen the coefficient-only label sieve.

### T — Transition / lineage

PASS.

The parity-word lift reconstructs a unique `x<2^61`, and each retained witness is independently rerun under the shortcut map. No residue representative is substituted for a different ordinary integer.

### C — Consistency

PASS.

The result is consistent with MATH-006/007:

- MATH-006 gives strong pointwise label caps at low `q61`;
- MATH-007 shows the phase masks are maximally distinguishable there;
- MATH-008 now shows all those distinguishable phases actually occur.

Thus the three audits together identify a genuine information barrier rather than an artifact of including unreachable ambient states.

### N — Norm

PASS.

Constructive witnesses and exhaustive finite enumeration are used only for the finite reachability statement actually claimed.

### O — Outcome

CONFIRMED / STRATEGY SATURATION.

The lower-61 phase-restriction branch is closed as a source of further coefficient-only pruning. A next refinement must add a new same-integer observable.

## Critical consequence

For every `q61` at which MATH-006 can reject at least one of the 340 block labels,

\[
q_{61}=39,\ldots,45,
\]

we have

\[
\operatorname{Reach}_{61}(q)=\mathbb Z/2048\mathbb Z.
\]

Hence

\[
\text{MATH-006 pointwise mask}
+\text{actual phase reachability}
\]

does not produce a fixed globally excluded block set.

The restricted reachability for `q61=59,60,61` is irrelevant to this particular sieve because MATH-006 already has one trivial all-340-survive mask for every `q61>=46`.

## Required prohibited upgrades

- do not interpret witness-completion scan lengths as probabilities or densities;
- do not infer that the witness subset exhausts all ordinary starts for `q39..58`;
- do not invalidate the correct pointwise MATH-006 caps merely because the proposed reachability refinement saturates;
- do not use the restricted high-q phase sets as an exclusion when the coefficient-only mask is already trivial;
- do not count endpoint quotient and root-Hensel maximality as independent filters;
- do not infer first-cell closure or Collatz closure.

## Evidence

Math-verification certificate:

`collatz/src/2026_09_08_lower61_endpoint_phase_reachability_certificate.py`

Certificate commit:

`764696d443c10cfbebd610893f0e517182a08512`

Math-verification explanatory note:

`collatz/notes/2026-09-08-lower61-endpoint-phase-reachability-and-route-saturation.md`

Note commit:

`77522e531f297558315af2dc94b6cb58c066e4dc`

No new external theorem is imported by this audit.

## Next audited transition

Do not further coarsen or restrict `(q61,y mod2048)` as the main refinement. The next candidate state must preserve the same ordinary integer while adding information not already present in the coefficient-only transducer. Priority candidates are:

1. correction/address order within an endpoint phase;
2. endpoint/Hensel eligibility beyond depth72, preserving the previously audited non-independence rule;
3. an exact address-local invariant inside the `<2^35` adjacent-block halos.
