# Track-3 Aggregate-Dynamics Closure Gate Audit

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Track: **3 — common-kernel construction after non-QFT Track-2 synthesis**

## 1. Purpose

The current DSD static aggregation layer produces reduced typed aggregates and explicitly does not reconstruct support without an injectivity theorem. The current Structural Reorganization Dynamics layer is component-resolved and likewise states that a reduced aggregate does not replace the full dynamic state without an injectivity or reconstruction result.

The present question is therefore narrower than deriving a new dynamics:

> Given a full structural state space `S`, a typed aggregate `A:S->U`, and a supplied full transition `Gamma:S->S`, when does there exist an autonomous aggregate-level transition `Gamma_A` such that `A o Gamma = Gamma_A o A`?

For the common QM/relativity construction, the aggregate codomain may be the typed product `U_Q x U_R`; no scalar identification of the two sectors is assumed.

No quantum-gravity premise and no new physical coupling law is introduced.

---

## 2. Source-locked boundary

The source papers already impose three relevant constraints:

1. the static layer is static and introduces no evolution law;
2. aggregate equality need not reconstruct channel or property support;
3. structural dynamics are component-resolved, and reduced aggregates do not replace the state without an injectivity/reconstruction result.

Accordingly, any autonomous aggregate dynamics must be proved as an additional factorization property of a supplied full transition. It is not inherited automatically from the existence of the static aggregate.

---

## 3. Exact closure criterion

Let

\[
A:S\to U,
\qquad
\Gamma:S\to S.
\]

An induced map

\[
\Gamma_A:\operatorname{im}A\to\operatorname{im}A
\]

satisfying

\[
\boxed{
A\circ\Gamma
=
\Gamma_A\circ A
}
\]

exists if and only if

\[
\boxed{
A(s)=A(s')
\Longrightarrow
A(\Gamma(s))=A(\Gamma(s'))
}
\]

for all declared source states `s,s'`.

Equivalently, the full transition must map each `A`-fiber into one `A`-fiber.

This is not a fourth independent theorem family. It is the Track-2 fiber-factorization theorem specialized to

\[
f=A,
\qquad
q=A\circ\Gamma.
\]

### Consequence

Two opposite overstatements are rejected:

\[
\boxed{
\text{aggregate exists}
\not\Rightarrow
\text{autonomous aggregate dynamics exists}
}
\]

and

\[
\boxed{
\text{aggregate is noninjective}
\not\Rightarrow
\text{autonomous aggregate dynamics is impossible}.
}
\]

Noninjectivity makes closure nontrivial; failure occurs only when the supplied transition splits an aggregate fiber.

---

## 4. Closure-failure finite witness

Use a typed product aggregate

\[
A(s)
=
\bigl(
\sum q_i,
\sum r_j
\bigr).
\]

The first state retains quantum-side support

```text
q_plus  = +1
q_minus = -1
r_fixed = +2
```

and the second retains

```text
q_zero  = 0
r_fixed = +2
```

so

\[
A(s_{\pm})=(0,2)=A(s_0),
\]

while the component-resolved supports differ.

Supply a deterministic full transition whose update uses the retained support labels:

```text
q_plus  -> 2
q_minus -> 0
q_zero  -> 0
r_fixed -> 2
```

Then

\[
A(\Gamma(s_{\pm}))=(2,2),
\qquad
A(\Gamma(s_0))=(0,2).
\]

Thus

\[
A(s_{\pm})=A(s_0)
\]

but

\[
A(\Gamma(s_{\pm}))\neq A(\Gamma(s_0)).
\]

Therefore no single-valued `Gamma_A` can be defined on the aggregate value `(0,2)` for this witness family.

### Status

**Finite exact closure-failure witness.**

The numbers are bookkeeping values only. They are not quantum observables, metric quantities, stress-energy components, DSD gravity sources, or physical coupling constants.

---

## 5. Positive control — noninjective aggregate with valid closure

Use the same noninjective aggregate and the same two source states, but supply the componentwise full transition

\[
q_i\mapsto 2q_i,
\qquad
r_j\mapsto \frac12 r_j.
\]

Then

\[
A(\Gamma(s))
=
\left(
2A_Q(s),
\frac12 A_R(s)
\right).
\]

Hence the induced aggregate transition

\[
\boxed{
\Gamma_A(q,r)
=
(2q,r/2)
}
\]

is well-defined on `im A`, and

\[
A\circ\Gamma
=
\Gamma_A\circ A.
\]

For both distinct source states with initial aggregate `(0,2)`, the future aggregate is `(0,1)`.

This positive control proves that noninjectivity of `A` alone does not prohibit autonomous reduced dynamics.

---

## 6. Relation to the previous Track-3 cause-signature stage

The previous stage showed

\[
\text{same sector transition}
\not\Rightarrow
\text{same transition cause signature}.
\]

The present stage adds a different reduction boundary:

\[
\text{same static aggregate}
\not\Rightarrow
\text{same future aggregate}.
\]

Both are instances of the same general discipline: reduced records may identify multiple richer states, and a dynamic claim on the reduced record is valid only when the supplied full transition respects the corresponding fibers.

Cause signatures are therefore potential retained coordinates for a later closure refinement, but they are not assumed to be sufficient by themselves.

---

## 7. DSD impact

No change to the Formation Axiom System, Property Axiom System, Channel-Indexed Static Aggregation, or Structural Reorganization Dynamics is required.

The current core already supports the correct interpretation:

```text
static aggregate
!= full component-resolved state

static aggregation law
!= evolution law

same aggregate
!= same lineage / same transition cause / same future aggregate
```

Track 3 should therefore apply the following gate whenever an aggregate-level evolution equation is proposed:

```text
1. declare full source-state carrier S;
2. declare typed aggregate A:S->U;
3. declare supplied full transition Gamma;
4. test every relevant A-fiber for future-aggregate consistency;
5. define Gamma_A only if A Gamma is constant on those fibers;
6. otherwise retain additional state coordinates or restrict the admissible source family.
```

This is an audit/analysis operating rule, not a new DSD axiom.

---

## 8. Verdict

**PASS_WITH_REFINEMENT.**

The Track-3 typed aggregate remains valid, but autonomous aggregate dynamics is conditional rather than automatic.

The exact result is:

\[
\boxed{
\Gamma_A\text{ exists on }\operatorname{im}A
\iff
\Gamma\text{ respects }A\text{-fibers.}
}
\]

The closure-failure witness shows why hidden support retained by the full state can matter dynamically even when the static aggregate agrees. The positive control shows that a noninjective aggregate can nevertheless support closed dynamics when the full transition is fiber-compatible.

No physical quantum-relativistic coupling is derived.

---

## 9. Reproducibility

Run from the repository root:

```bash
python audits/science/2026-09-08_track3_aggregate_dynamics_closure.py --mode all
```

The script uses only the Python standard library and exact `fractions.Fraction` arithmetic.

---

## 10. Next Track-3 target

The next useful construction is a **minimal closure augmentation / sufficient-state gate**.

Given a closure-failing aggregate `A`, seek an explicitly retained typed coordinate `eta` such that

\[
\widetilde A(s)
=
(A(s),\eta(s))
\]

is still reduced relative to the full component state but satisfies

\[
\widetilde A(s)=\widetilde A(s')
\Longrightarrow
\widetilde A(\Gamma(s))=\widetilde A(\Gamma(s')).
\]

The goal is not to assume that cause signature, support identity, or another coordinate is universally sufficient. The next audit should determine which retained information is actually sufficient for the declared transition family and which proposed augmentation remains lossy.
