# DSD-AUDIT-20260908-MATH-012 — Collatz Hensel even-budget complete descriptor

## Verdict

`CONFIRMED / EXACT ARITHMETIC-CREDIT DESCRIPTOR / COMPUTATIONAL ACCELERATION / NO NEW COLLATZ EXCLUSION`

Collatz conjecture remains `OPEN`.

The first universal Farey cell remains `OPEN`.

## Audited claim

At the frozen theorem-facing verification floor

\[
B_{\rm pub}=2^{71},
\]

the existing arbitrary-competitor root-Hensel arithmetic-credit predicate

\[
2^{k-q}\left(1-\left(\frac23\right)^q\right)<2^{71}
\]

is, for `q>=2`, exactly equivalent to

\[
\boxed{k-q\le71.}
\]

Thus `d=k-q`, the number of even shortcut steps in the prefix, is a complete descriptor for this **credit-eligibility predicate only**.

## DSD tuple

### D — Describability

The target object is precisely the root-Hensel arithmetic-credit condition. It is not the whole Hensel maximality argument and not Collatz-candidate survival.

### R — Resolution

State resolution is exact integer `(k,q)` under the frozen `2^71` theorem-facing floor. The descriptor is `d=k-q`.

### S — Selection

The exact equivalence is claimed for `q>=2`, which contains the present coefficient-surviving regime near and beyond the historical depth-195 boundary.

### E — Exclusion

`d>71` means only:

`ROOT_HENSEL_ARITHMETIC_CREDIT_UNAVAILABLE`.

It does **not** mean:

`COLLATZ_CANDIDATE_EXCLUDED`.

### T — Transition

For `d=k-q`:

- if `d<=71`, then `1-(2/3)^q<1`, hence the legacy credit is `<2^d<=2^71`;
- if `d>=72` and `q>=2`, then `1-(2/3)^q>=5/9>1/2`, hence the legacy credit is `>2^(d-1)>=2^71`.

The transition from the large exact inequality to `d<=71` is therefore exact in scope.

### C — Consistency

The certificate performs exact integer regression for all

\[
2\le q\le k\le512,
\]

covering `130,816` states, with no mismatch.

It also verifies:

- `(195,124)` credit-safe;
- `(196,124)` credit-unsafe;
- `(196,125)` credit-safe.

This refines rather than contradicts the historical “uniform safe through 195; first failure at `(196,124)`” statement.

### N — Norm

`ESTABLISHED_WITHIN_SCOPE`.

Runtime benchmarks are diagnostic only. Finite symbolic word counts are not density or emptiness claims.

### O — Outcome

A complete one-scalar descriptor is available for the arithmetic-credit subproblem, replacing repeated large-power comparisons by the exact integer gate

\[
k-q\le71.
\]

This is a computational acceleration and a cleaner branchwise eligibility classifier.

## Combined threshold with coefficient survival

Coefficient survival requires

\[
q\ge q_{\min}(k),
\]

while the audited root-credit gate requires

\[
q\ge k-71.
\]

Hence the combined threshold is

\[
\boxed{Q_*(k)=\max\{q_{\min}(k),k-71\}.}
\]

The first strict tightening occurs at

\[
\boxed{k=196},
\]

where

\[
q_{\min}(196)=124,
\qquad
196-71=125.
\]

Therefore `(196,124)` survives the coefficient boundary but loses this Hensel credit, while `(196,125)` retains the arithmetic credit.

## Interpretation of the historical depth-195 boundary

Safe statement:

> Through depth 195, coefficient survival automatically implies the audited arithmetic-credit inequality.

Safe refined statement:

> Beginning at depth 196, the lowest coefficient-surviving q branches can lose arithmetic-credit eligibility, while higher-q branches may retain it.

Prohibited upgrade:

> “Full arbitrary-word Hensel maximality is automatically valid beyond 195 whenever `k-q<=71`.”

The descriptor audits only the credit inequality. Any other assumptions of the Hensel mechanism remain separately required.

## Symbolic-prefix diagnostic

The certificate also counts parity words obeying the coefficient boundary at every prefix and the subset that additionally preserves `k-q<=71` at every prefix.

The counts agree through depth 195 and first separate at 196.

This quantifies the coverage of the proof mechanism, not candidate impossibility.

## Computational consequence

For this subproblem, all states with the same `d=k-q` are equivalent **only with respect to the arithmetic-credit predicate**.

This permits safe computational merging for the gate itself and removes repeated large exact power evaluations.

It does not permit merging of complete Collatz, endpoint, correction, parity, or Hensel states.

## Prohibited upgrades

- `d>71` ⇒ Collatz candidate excluded — **PROHIBITED**.
- same `d` ⇒ same full Collatz state — **PROHIBITED**.
- arithmetic credit safe ⇒ every Hensel assumption safe — **PROHIBITED**.
- finite symbolic coverage ratio ⇒ density theorem — **PROHIBITED**.
- computational acceleration ⇒ stronger global theorem — **PROHIBITED**.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_dsd_hensel_even_budget_descriptor.py`

Certificate commit:

`6c7ffb083f37989907a690c303b3f99adb43f7b0`

Explanatory note:

`collatz/notes/2026-09-08-hensel-even-budget-complete-descriptor.md`

The global Collatz status remains `OPEN`.
