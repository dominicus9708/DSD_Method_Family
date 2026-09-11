# Black-Hole Critical-Radius Threshold Interface Refinement
# 블랙홀 임계반지름 임계 인터페이스 정교화

```text
METHOD_ID: DSD-METHOD-20260911-BH-RADIUS-THRESHOLD-REFINE-001
STATUS: ACTIVE_REFINEMENT
DOMAIN: structural gravity / black-hole benchmark
DATE: 2026-09-11
PARENT_PROTOCOL: methodology/BLACK_HOLE_CRITICAL_RADIUS_BENCHMARK_PROTOCOL.md
```

## 1. Purpose / 목적

This document records the current canonical refinement of the support-threshold portion of the black-hole critical-radius benchmark.

It is intended to supersede the older support-factorization assumptions **where they conflict** with the eta_I identifiability and zeta saturation/interface audits. The parent benchmark protocol remains the general provenance/anti-circularity framework.

## 2. Starting coarse structural-gravity form / 시작 coarse 형식

Retain the conditional far-field candidate

\[
a_X(r)\simeq K_g\frac{M}{r^2},
\]

and, when the explicit potential bridge is supplied,

\[
X(r)=K_g\frac{M}{r}.
\]

No Schwarzschild relation is used to fix \(K_g\), \(c_{\rm info}\), or any threshold coefficient.

## 3. eta_I reduction / eta_I 축약

If a downstream physical specialization distinguishes a source-coupled carrier \(\mu_g\) and an inertial/support carrier \(\mu_I\), define

\[
\eta_I=\frac{\mu_I}{\mu_g}.
\]

Generic DSD does not derive \(\eta_I=1\).

Under an explicit weak-field universality bridge,

\[
\eta_I(S)=\eta_0
\]

for all admitted test-body states in that regime. Then the observable normalization depends on

\[
\boxed{K_{\rm eff}\equiv\frac{K_g}{\eta_0}}.
\]

A universal \(\eta_0\) is therefore degenerate with \(K_g\) and should not be counted as a separately identifiable black-hole coefficient.

Writing \(\eta_0=1\) after this reduction is a normalization convention only.

If \(\eta_I(S)\) is non-universal, keep it explicitly as a separate state-dependent physical sector.

## 4. c_info / local-support carrier firewall / c_info와 local-support carrier 방화벽

The dynamic foundation defines \(c_{\rm info}\) as an infimal upper bound on expansion of declared component-resolved distinguishability support.

It does not follow that every local reorganization or support-capacity rate is a metric propagation-front speed.

Therefore the generic support capacity must not be written as though a local rate automatically satisfies

\[
v_{\rm sup}=\zeta c_{\rm info}.
\]

That specialization is admissible only after an explicit support-propagation interface is supplied.

## 5. Canonical support-capacity interface / 정본 지지용량 인터페이스

Use a typed support-state carrier

\[
S_{\rm sup}
\]

and a dimensionless downstream constitutive functional

\[
\Psi:S_{\rm sup}\to\mathbb R_{>0}.
\]

Define the support capacity per universal source-coupled normalization by

\[
\boxed{
C_{\rm sup}
=c_{\rm info}^2\Psi(S_{\rm sup})
}.
\]

Matching the structural load scale

\[
U_X(R)=K_{\rm eff}\frac{M}{R}
\]

to the declared support capacity gives

\[
\boxed{
R_{\rm crit}
=
\frac{K_{\rm eff}M}
{c_{\rm info}^2\Psi(S_{\rm sup})}
}.
\]

This is the current preferred generic candidate form.

It remains a downstream physical specialization, not a Formation/Property theorem.

## 6. Optional front specialization / 선택적 front 특수화

If the model supplies all of the following:

1. a metric localization carrier;
2. a physically identified support-failure front;
3. a proof/interface that failure at a target cannot precede arrival of the relevant distinguishability support;
4. finite propagation in the required discrepancy convention;

then define

\[
\zeta_{\rm front}
=
\frac{v_{\rm front}}{c_{\rm info}}.
\]

The propagation theorem can then support

\[
0\le\zeta_{\rm front}\le1.
\]

Equality

\[
\zeta_{\rm front}=1
\]

requires a saturating perturbation/mode and is not automatic.

A constitutive special model may set

\[
\Psi(S_{\rm sup})=\Phi(\zeta_{\rm front}),
\]

but neither \(\Phi\) nor saturation is supplied by generic DSD.

## 7. Low-speed constitutive coefficient / 저속 구성계수

If a support-energy specialization uses

\[
E_{\rm sup}(v)
=
\mu_Ic_{\rm info}^2\Phi(v/c_{\rm info})
\]

and separately supplies

\[
\frac{dE_{\rm sup}}{dv}=p_{\rm eff}(v),
\qquad
p_{\rm eff}(v)=\mu_Iv+O(v^3/c_{\rm info}^2),
\]

then

\[
\Phi(\beta)=\frac12\beta^2+O(\beta^4).
\]

This fixes only the leading low-speed coefficient. It does not imply the global law

\[
\Phi(\beta)=\frac12\beta^2
\]

near a critical or saturating regime.

## 8. Current comparator identity / 현재 비교식

Against the external Schwarzschild comparator

\[
R_S=\frac{2GM}{c^2},
\]

the current generic candidate gives

\[
\boxed{
\frac{R_{\rm crit}}{R_S}
=
\frac{1}{2\Psi(S_{\rm sup})}
\frac{K_{\rm eff}}{G}
\left(\frac{c}{c_{\rm info}}\right)^2
}.
\]

This is only a comparison identity.

The following quantities remain independently unresolved:

- \(K_{\rm eff}/G\);
- \(c_{\rm info}/c\);
- the critical support-state readout \(\Psi(S_{\rm sup})\);
- possible strong-field nonuniversality of \(\eta_I(S)\).

## 9. Anti-fitting rules / 피팅 방지 규칙

Do not:

- set \(\Psi=1/2\) because Schwarzschild requires it under other unit identifications;
- set a front saturation parameter to 1 merely because \(c_{\rm info}\) is an upper bound;
- infer \(K_{\rm eff}\) from \(R_S\) and reuse it as an independent DSD prediction;
- identify weak-field universality with strong-field state independence without a bridge;
- identify an EHT bright ring with a horizon radius.

## 10. Current verdict / 현재 판정

```text
CURRENT_STATE:
CONDITIONAL_SCALING_RECOVERY / THRESHOLD_FUNCTION_OPEN

SURVIVES:
R_crit proportional to M under the explicit coarse structural-gravity and support-capacity bridges.

REMOVED_AS_GENERIC_ASSUMPTIONS:
eta_I = 1
zeta = 1
v_sup = zeta c_info without a carrier/interface declaration
purely quadratic Phi up to the critical regime

NEXT_TARGET:
derive, constrain, or falsify candidate forms of Psi(S_sup) from the structural-support state itself while Schwarzschild remains sealed as a comparator.
```

## 11. Related reproducibility commands / 관련 재현 명령

```bash
python audits/science/2026-09-11_structural_gravity_eta_i_identifiability_audit.py --mode all
python audits/science/2026-09-11_structural_gravity_zeta_saturation_interface_audit.py --mode all
```
