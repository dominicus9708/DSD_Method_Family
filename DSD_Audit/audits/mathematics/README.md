# Mathematics audit index / 수학 감사 인덱스

이 디렉터리는 DSD Audit의 수학 분야 감사 기록을 보존합니다.

현재 기록의 대부분은 Collatz 추측에 대한 proof-architecture, 외부문헌, exact calculation 감사입니다. 개별 파일은 역사 기록과 판정을 보존하며, 이 README는 **현재 탐색용 인덱스**입니다.

## Current Collatz status

- **Collatz conjecture:** `OPEN`
- **First universal Farey cell:** `OPEN`
- **Proof architecture:** `PARTIALLY_CONFIRMED`
- **Current start window:**

\[
2^{71}<N<\frac{1364}{1024}2^{71}
\]

- **Current top-address labels:** `340` (`1024..1363`)
- **Current frontier:** lower-61 reachable endpoint phases

\[
\operatorname{Reach}_{61}\subset\{(q_{61},y\bmod2048)\}.
\]

## Canonical Collatz audit sequence

| Audit ID | Record | Outcome / role |
|---|---|---|
| `DSD-AUDIT-20260907-MATH-001` | [`2026-09-07_collatz-proof-architecture-full-audit.md`](2026-09-07_collatz-proof-architecture-full-audit.md) | Full proof-architecture audit; global result `PARTIALLY_CONFIRMED`, Collatz remains `OPEN` |
| `DSD-AUDIT-20260907-MATH-002` | [`2026-09-07_collatz-external-literature-citation-audit.md`](2026-09-07_collatz-external-literature-citation-audit.md) | Claim-level external literature audit and `A/B/C/D/FINITE ONLY` citation policy |
| `DSD-AUDIT-20260907-MATH-003` | [`2026-09-07_collatz-denjoy-koksma-first-cell-audit.md`](2026-09-07_collatz-denjoy-koksma-first-cell-audit.md) | Denjoy–Koksma/Ostrowski input audited; first-cell top-address count `341 → 340`; scalar-only route boundary fixed |
| `DSD-AUDIT-20260907-MATH-004` | [`2026-09-07_collatz-first-cell-endpoint-q-lock-audit.md`](2026-09-07_collatz-first-cell-endpoint-q-lock-audit.md) | Endpoint q-lock/address-faithful Hensel interpretation; revised to candidate-language first crossing scope |
| `DSD-AUDIT-20260907-MATH-005` | [`2026-09-07_collatz-340block-endpoint-halo-audit.md`](2026-09-07_collatz-340block-endpoint-halo-audit.md) | Same-endpoint coupling localized to adjacent-block halos |
| `DSD-AUDIT-20260907-MATH-006` | [`2026-09-07_collatz-block-label-11bit-transducer-audit.md`](2026-09-07_collatz-block-label-11bit-transducer-audit.md) | Exact 61+11 block-label transducer; low-surplus pointwise label caps |
| `DSD-AUDIT-20260907-MATH-007` | [`2026-09-07_collatz-block-label-right-congruence-audit.md`](2026-09-07_collatz-block-label-right-congruence-audit.md) | Exact right-congruence barrier; `q61=39..43` requires all 2048 endpoint phases |

## Reading order

For the present proof attempt, read in this order:

1. `MATH-001` — global dependency/status map.
2. `MATH-002` — what external results may legally enter the proof line.
3. `MATH-003` — why the first-cell candidate window has 340 top blocks and why scalar correction alone stops there.
4. `MATH-004` — same-endpoint ordinary-integer lineage and non-independent Hensel interpretation.
5. `MATH-005` — block coupling locality.
6. `MATH-006` — exact block-label transducer.
7. `MATH-007` — why endpoint phase cannot be coarsened away in the strongest range.

## Audit discipline

### SAFE does not mean global proof

A `CONFIRMED` or `SAFE` local audit applies only to the locked claim and scope. It must not be upgraded to Collatz without the missing universal bridges.

### Computation does not become a theorem by scale

Finite scans and exact finite tables may establish the finite statement they actually enumerate, but

\[
\text{finite computation}\not\Rightarrow\text{universal theorem}.
\]

### Measure/density language is not emptiness

\[
\text{almost all}\not\Rightarrow\text{all},
\qquad
\mu(S)=0\not\Rightarrow S=\varnothing.
\]

### Preserve ordinary-integer lineage

A residue, quotient state, endpoint class, or symbolic path may be used only when the bridge back to the same ordinary integer is explicit at the required resolution.

## External literature citation classes

- `A` — positive prior art
- `B` — conditional prior art
- `C` — partial absorption: surviving content + failed/open hinge separated
- `D` — audited anti-pattern / negative methodological prior art
- `FINITE ONLY` — finite evidence only

A failed global proof mechanism is not summarized as “the entire paper is wrong.” The audit records the exact failed bridge and separately preserves valid definitions, lemmas, or computations.

## Revision policy

- Do not silently rewrite an older reasonable verdict as though it never existed.
- When scope or evidence changes, revise the current file explicitly or add a linked revision/migration record.
- Preserve old commits and paths for traceability.
- Use this README to identify the current audit sequence rather than reorganizing historical files merely for appearance.

## Related repository

Current calculation/proof index:

`dominicus9708/Math-verification/collatz/README.md`
