# Structural-Gravity Collapse-Speed Bridge Audit
# 구조적 중력 붕괴속도 교량 감사

```text
AUDIT_ID: DSD-AUDIT-20260911-PHYSICS-BH-005
STATUS: PASS_WITH_BOUNDARY / COLLAPSE_SPEED_BRIDGE_REQUIRED
DOMAIN: structural gravity / support failure / black-hole critical radius
DATE: 2026-09-11
RELATED_METHOD: methodology/STRUCTURAL_GRAVITY_SUPPORT_RESPONSE_INTERFACE.md
RELATED_CODE: audits/science/2026-09-11_structural_gravity_collapse_speed_bridge_audit.py
PARENT_AUDIT: audits/science/2026-09-11_structural-gravity-inertial-response-integral-audit.md
```

## 1. Audit question / 감사 질문

Does the current DSD propagation bound \(c_{\rm info}\) generically imply that a local collapse or support-failure speed satisfies

\[
0\le v_{\rm col}\le c_{\rm info},
\]

and in particular does local-collapse convergence justify

\[
v_{\rm col}=c_{\rm info}?
\]

The answer is no at the generic DSD level.

## 2. Foundation boundary / 기초 경계

Structural Reorganization Dynamics defines \(c_{\rm info}\) from the propagation of distinguishability support. It is an infimal finite propagation bound for admissible perturbations under a declared discrepancy convention.

The same paper explicitly separates the existence of a finite propagation bound from its numerical value and states that a finite \(c_{\rm info}\) is a theorem or model condition rather than a consequence of the word “information.”

In the symmetric-hyperbolic specialization, the characteristic estimate supplies an admissible bound \(c_*\), while equality with the infimal \(c_{\rm info}\) requires a sharp or saturating propagation mode. Hyperbolicity alone does not imply equality.

The time parameter is also not automatically metric time. A quantity interpreted as a speed requires a supplied metric-time structure.

Therefore three notions must remain distinct:

1. support-front propagation speed;
2. characteristic speed of a supplied represented evolution law;
3. time derivative of a local collapse/support coordinate.

## 3. Counterexample specialization / 반례 특수화

Consider a component-resolved downstream toy model with two sectors:

\[
\partial_tu+c_{\rm info}\partial_xu=0,
\]

and, on a fixed pre-existing support \(K\),

\[
\partial_tq=-v_{\rm col}.
\]

Let \(q\) be a length-like local structural coordinate.

The \(u\)-sector transports discrepancy support at speed \(c_{\rm info}\).

The \(q\)-sector changes locally at rate \(v_{\rm col}\), but its support does not expand beyond \(K\). Therefore its support-propagation speed is zero even if \(|\partial_tq|\) is arbitrarily large.

The combined information-propagation bound remains

\[
c_{\rm info}
\]

for any positive \(v_{\rm col}\).

Consequently, defining

\[
\beta_{\rm col}:=\frac{v_{\rm col}}{c_{\rm info}}
\]

for finite positive \(c_{\rm info}\), generic DSD does not imply

\[
\beta_{\rm col}\le1.
\]

This is not a claim that a physically relativistic collapse may be superluminal. It is a typing/provenance result: the generic DSD propagation theorem alone is insufficient to impose that physical restriction on a different local coordinate.

## 4. Correction to the previous saturation notation / 이전 포화기호 교정

The previous support-response interface used

\[
v_{\rm sup}=\zeta c_{\rm info},
\qquad 0<\zeta\le1.
\]

That bounded form is now reclassified as an additional **collapse-to-propagation bridge specialization**, not a generic DSD consequence.

The generic dimensionless ratio, when both quantities are defined, is

\[
\boxed{
\beta_{\rm col}=\frac{v_{\rm col}}{c_{\rm info}}>0
}
\]

with no generic upper bound supplied by the current foundation.

Only after an independent constitutive or causal theorem proves

\[
v_{\rm col}\le c_{\rm info}
\]

may one define the bounded specialization

\[
\zeta_{\rm col}:=\frac{v_{\rm col}}{c_{\rm info}}
\in(0,1].
\]

And only a further saturation theorem would justify

\[
\zeta_{\rm col}=1.
\]

## 5. General response formula with the corrected ratio / 교정된 일반 응답식

For a supplied inertial/support response

\[
P_I(v)=\mu_Ic_{\rm info}\phi(v/c_{\rm info}),
\]

let

\[
\eta_I=\frac{\mu_I}{\mu_g}.
\]

At a selected local support-failure speed \(v_{\rm col}\), the capacity per source unit is

\[
C_{\rm sup}
=
\eta_Ic_{\rm info}^2
\int_0^{\beta_{\rm col}}\phi(s)\,ds.
\]

Hence the candidate radius becomes

\[
\boxed{
R_{\rm crit}
=
\frac{K_gM}
{\eta_Ic_{\rm info}^2 I_\phi(\beta_{\rm col})}
},
\qquad
I_\phi(\beta):=\int_0^\beta\phi(s)\,ds.
\]

This is still a downstream structural-gravity specialization, not a generic DSD theorem.

## 6. Linear-response simplification / 선형응답 단순화

If

\[
\phi(s)=s
\]

throughout the relevant interval, then

\[
I_\phi(\beta_{\rm col})
=
\frac12\beta_{\rm col}^2
=
\frac12\frac{v_{\rm col}^2}{c_{\rm info}^2}.
\]

Therefore

\[
\boxed{
R_{\rm crit}
=
\frac{2K_gM}
{\eta_Iv_{\rm col}^2}
}.
\]

The normalization scale \(c_{\rm info}\) cancels exactly.

This is an important correction: in the globally linear-response specialization, the candidate critical radius depends on the **actual supplied local collapse/support speed** \(v_{\rm col}\), not directly on the information-propagation bound.

Thus the route to a Schwarzschild-scale comparator would require independent bridges such as

\[
K_g\leftrightarrow G,
\qquad
\eta_I\leftrightarrow1,
\qquad
v_{\rm col}\leftrightarrow c,
\]

rather than obtaining the result merely from \(c_{\rm info}\).

## 7. Reproducible witness / 재현 가능한 증인

Run from the repository root:

```bash
python audits/science/2026-09-11_structural_gravity_collapse_speed_bridge_audit.py --mode all
```

The script varies

\[
\beta_{\rm col}
=0.25,0.5,1,2,10
\]

while keeping the combined discrepancy-support propagation bound fixed.

It passes 5/5 checks.

## 8. Provenance ledger / 출처 장부

```text
R0 / PRE-EXISTING DSD:
- c_info is defined through distinguishability-support propagation.
- finite c_info and its numerical value require a model theorem/condition.
- metric speed requires metric time.
- characteristic equality/saturation is not generic.

R1 / GENERAL STRUCTURAL-MATHEMATICAL:
- support propagation and local coordinate rate are mathematically distinct.
- a fixed-support local coordinate can change arbitrarily quickly without enlarging support.
- dimensionless ratio beta_col = v_col/c_info is a valid comparison only after both speeds are defined.

DOWNSTREAM STRUCTURAL-GRAVITY SPECIALIZATION:
- q as a collapse/support coordinate.
- P_I(v) as support/inertial response.
- v_col as the selected support-failure speed.

NOT DERIVED:
- v_col <= c_info;
- v_col = c_info;
- c_info = physical c;
- v_col = physical c;
- Schwarzschild radius.
```

## 9. Verdict / 판정

```text
VERDICT:
PASS_WITH_BOUNDARY / COLLAPSE_SPEED_BRIDGE_REQUIRED

ADVANCE:
- the previous single saturation factor is split into propagation and collapse notions;
- zeta<=1 is no longer treated as generic;
- beta_col=v_col/c_info is the generic comparison ratio when both speeds exist;
- for globally linear response, c_info cancels and Rcrit=2 K_g M/(eta_I v_col^2).

OPEN:
- physical law for v_col;
- proof or rejection of v_col<=c_info;
- proof or rejection of saturation v_col=c_info;
- relation of v_col or c_info to relativistic c.
```

## 10. Next target / 다음 대상

The next audit should determine whether a physically admissible black-hole specialization can obtain a **causal collapse-speed bridge** without importing the Schwarzschild radius or horizon condition itself.

In particular, separate the following candidate routes:

1. causal-cone restriction on a realized-axis or local geometric carrier;
2. characteristic collapse mode of an explicit hyperbolic constitutive system;
3. support-failure front speed versus local material/contraction speed;
4. observational or weak-field calibration of the relevant speed scale outside the black-hole-radius target.

Only after one route independently fixes \(v_{\rm col}\) should the Schwarzschild comparator be reopened.
