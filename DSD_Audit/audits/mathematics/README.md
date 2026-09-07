# Mathematics audit index / 수학 감사 인덱스

이 디렉터리는 DSD Audit의 수학 분야 감사 기록을 보존합니다. 개별 감사 파일은 역사 판정과 근거를 보존하며, 이 README는 **현재 탐색용 인덱스**입니다.

## Current Collatz status

- **Collatz conjecture:** `OPEN`
- **First universal Farey cell:** `OPEN`
- **Proof architecture:** `PARTIALLY_CONFIRMED`
- **Current start window:**

\[
2^{71}<N<\frac{1364}{1024}2^{71}
\]

- **Current top-address labels:** `340` (`1024..1363`)
- **MATH-008:** actual lower-61 phase reachability is saturated for the coefficient-only phase route.
- **MATH-009:** Hensel correction ordering and endpoint/minimum-start ordering are redundant within a fixed fiber.
- **MATH-010:** DSD representation-stage gates entered the computation and blocked double address lift.
- **MATH-011:** finite coefficient survival was compressed to `H(r)` and the 340-address aggregation to a cyclic sliding window, producing exact computational acceleration.
- **MATH-012:** the root-Hensel arithmetic-credit inequality was compressed exactly to the even-step descriptor `d=k-q`; the old depth-195 uniform boundary is refined branchwise.
- **Current frontier:** after the cheap gate `k-q<=71`, test whether the remaining non-redundant Hensel/endpoint conditions admit another exact small descriptor.

## Canonical Collatz audit sequence

| Audit ID | Record | Outcome / role |
|---|---|---|
| `DSD-AUDIT-20260907-MATH-001` | [`2026-09-07_collatz-proof-architecture-full-audit.md`](2026-09-07_collatz-proof-architecture-full-audit.md) | Global dependency/status map; `PARTIALLY_CONFIRMED`, Collatz `OPEN` |
| `DSD-AUDIT-20260907-MATH-002` | [`2026-09-07_collatz-external-literature-citation-audit.md`](2026-09-07_collatz-external-literature-citation-audit.md) | Claim-level external literature audit; `A/B/C/D/FINITE ONLY` policy |
| `DSD-AUDIT-20260907-MATH-003` | [`2026-09-07_collatz-denjoy-koksma-first-cell-audit.md`](2026-09-07_collatz-denjoy-koksma-first-cell-audit.md) | DK/Ostrowski input; `341→340` first-cell address frontier |
| `DSD-AUDIT-20260907-MATH-004` | [`2026-09-07_collatz-first-cell-endpoint-q-lock-audit.md`](2026-09-07_collatz-first-cell-endpoint-q-lock-audit.md) | Candidate-language endpoint q-lock and address-faithful interpretation |
| `DSD-AUDIT-20260907-MATH-005` | [`2026-09-07_collatz-340block-endpoint-halo-audit.md`](2026-09-07_collatz-340block-endpoint-halo-audit.md) | Same-endpoint coupling localized to adjacent-block halos |
| `DSD-AUDIT-20260907-MATH-006` | [`2026-09-07_collatz-block-label-11bit-transducer-audit.md`](2026-09-07_collatz-block-label-11bit-transducer-audit.md) | Exact 61+11 block-label transducer; pointwise low-surplus caps |
| `DSD-AUDIT-20260907-MATH-007` | [`2026-09-07_collatz-block-label-right-congruence-audit.md`](2026-09-07_collatz-block-label-right-congruence-audit.md) | Exact phase right-congruence barrier |
| `DSD-AUDIT-20260908-MATH-008` | [`2026-09-08_collatz-lower61-endpoint-phase-reachability-audit.md`](2026-09-08_collatz-lower61-endpoint-phase-reachability-audit.md) | All 2048 phases occur for `q61=39..58`; phase-sparsity route `STRATEGY SATURATION` |
| `DSD-AUDIT-20260908-MATH-009` | [`2026-09-08_collatz-root-hensel-endpoint-ordering-redundancy-audit.md`](2026-09-08_collatz-root-hensel-endpoint-ordering-redundancy-audit.md) | Same-fiber Hensel/endpoint ordering is one affine relation; `REDUNDANT / NO NEW PRUNING` |
| `DSD-AUDIT-20260908-MATH-010` | [`2026-09-08_collatz-dsd-native-61plus11-computation-audit.md`](2026-09-08_collatz-dsd-native-61plus11-computation-audit.md) | DSD-native stage/resolution/exclusion state; double address lift rejected |
| `DSD-AUDIT-20260908-MATH-011` | [`2026-09-08_collatz-dsd-complete-descriptor-cyclic-window-acceleration-audit.md`](2026-09-08_collatz-dsd-complete-descriptor-cyclic-window-acceleration-audit.md) | Complete finite `H(r)` descriptor + exact cyclic-window transform; computational acceleration |
| `DSD-AUDIT-20260908-MATH-012` | [`2026-09-08_collatz-hensel-even-budget-descriptor-audit.md`](2026-09-08_collatz-hensel-even-budget-descriptor-audit.md) | Root-Hensel arithmetic-credit predicate exactly reduced to `k-q<=71`; branchwise refinement of depth-195 boundary |

## Reading order

1. `MATH-001` — global status/dependencies.
2. `MATH-002` — legal external inputs.
3. `MATH-003` — 340-block first-cell window.
4. `MATH-004` — endpoint q-lock.
5. `MATH-005` — adjacent-block locality.
6. `MATH-006` — exact 61+11 transducer.
7. `MATH-007` — phase quotient barrier.
8. `MATH-008` — actual phase reachability saturation.
9. `MATH-009` — Hensel/endpoint ordering redundancy.
10. `MATH-010` — DSD-native representation gates.
11. `MATH-011` — complete descriptor used for exact acceleration.
12. `MATH-012` — depth-72+ Hensel arithmetic-credit complete descriptor.

## MATH-011 computational compression

For lifted residue `r mod2048`,

\[
H(r)=\max_{1\le j\le11}\bigl(q_{\min}(61+j)-s_j(r)\bigr)
\]

is complete for the finite depth-72 coefficient-survival predicate:

\[
r\text{ survives}\iff q_{61}\ge H(r).
\]

With the inverse of `3^q mod2048`, the 340-address aggregation becomes a cyclic contiguous window. The expensive predicate-evaluation layer is reduced from `16,015,360` to `47,104` evaluations while reproducing the full legacy count vectors exactly.

This is computational acceleration, not a stronger Collatz theorem.

## MATH-012 Hensel arithmetic-credit descriptor

At the frozen theorem-facing floor `2^71`, the existing arithmetic-credit predicate

\[
2^{k-q}\left(1-\left(\frac23\right)^q\right)<2^{71}
\]

is, for `q>=2`, exactly equivalent to

\[
\boxed{k-q\le71.}
\]

Thus `d=k-q`, the number of even steps in the prefix, is a complete descriptor for **this credit predicate only**.

Together with coefficient survival:

\[
\boxed{Q_*(k)=\max\{q_{\min}(k),k-71\}.}
\]

The uniform historical boundary is refined by

- `(195,124)` — credit safe;
- `(196,124)` — coefficient-safe / credit-unsafe;
- `(196,125)` — credit safe.

Therefore depth196 is the first depth where the lowest coefficient-surviving q loses this credit. This does not automatically extend full arbitrary-word Hensel maximality on higher-q branches; all other conditions remain separately required.

The certificate exactly regresses `130,816` states with `2<=q<=k<=512` against the legacy big-integer predicate with no mismatch.

## DSD audit discipline

### Exact arithmetic stays primary

DSD may compress or reparameterize a predicate only when exact equivalence is proved or exhaustively regressed within the stated finite scope.

### Complete descriptors are scope-bound

`H(r)` is complete for the finite 61+11 coefficient predicate. `d=k-q` is complete for the root-Hensel arithmetic-credit predicate. Neither is automatically a complete Collatz state.

### Mechanism failure is not candidate exclusion

\[
k-q>71
\]

means the audited Hensel credit is unavailable. It does **not** mean the ordinary Collatz candidate is impossible.

### Preserve ordinary-integer lineage

Residue, endpoint, quotient, parity, and correction states may be merged only when the exact relation needed by the downstream predicate is preserved.

### Redundant evidence is not multiplied

Endpoint ordering and correction ordering remain one affine relation in the fixed-fiber scope.

### Computation does not become a universal theorem by scale

\[
\text{finite computation}\not\Rightarrow\text{universal theorem}.
\]

\[
\text{almost all}\not\Rightarrow\text{all},
\qquad
\mu(S)=0\not\Rightarrow S=\varnothing.
\]

## External literature citation classes

- `A` — positive prior art
- `B` — conditional prior art
- `C` — partial absorption
- `D` — audited anti-pattern / negative methodological prior art
- `FINITE ONLY` — finite evidence only

## Revision policy

- Preserve historical audit files and commits.
- Revise scope explicitly rather than silently replacing earlier verdicts.
- A saturated/failed strategy branch does not invalidate correct upstream mathematics.
- Use this README as the current sequence map rather than moving historical files for cosmetic reasons.

## Related repository

Current calculation/proof index:

`dominicus9708/Math-verification/collatz/README.md`
