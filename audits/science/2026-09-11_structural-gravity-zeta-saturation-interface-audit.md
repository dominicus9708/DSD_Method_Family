# Structural Gravity — zeta Saturation / Interface Audit
# 구조적 중력 — zeta 포화·인터페이스 감사

```text
AUDIT_ID: DSD-AUDIT-20260911-BH-RADIUS-ZETA-001
STATUS: COMPLETED_WITH_CORRECTION
DOMAIN: structural gravity / black-hole critical-radius benchmark
DATE: 2026-09-11
RELATED_PROTOCOL: methodology/BLACK_HOLE_CRITICAL_RADIUS_BENCHMARK_PROTOCOL.md
RELATED_CODE: audits/science/2026-09-11_structural_gravity_zeta_saturation_interface_audit.py
```

## 1. Audit question / 감사 질문

The previous support-threshold candidate used

\[
v_{\rm sup}=\zeta c_{\rm info},
\qquad 0<\zeta\le1.
\]

This audit asks whether that substitution is actually justified by the Structural Reorganization Dynamics, and in particular whether

\[
\boxed{\zeta=1}
\]

can be derived without importing the Schwarzschild coefficient or another external target.

## 2. Generic DSD propagation result / 일반 DSD 전파 결과

The dynamic foundation defines \(c_{\rm info}\) as the infimum of admissible finite propagation bounds for component-resolved distinguishability support under a fixed discrepancy convention.

Therefore \(c_{\rm info}\) is an upper-bound object. It is not, by definition, the speed of every propagating mode.

For hyperbolic specializations, a characteristic upper bound can be admissible, but equality with the component-resolved infimal bound requires a sharp or saturating propagation mode and does not follow from hyperbolicity alone.

The same separation appears in the identity-front result:

\[
c_{\rm id,front}\le c_{\rm info},
\]

while equality requires a saturating perturbation and is not automatic.

Hence

\[
\boxed{\text{upper propagation bound}\not\Rightarrow\text{actual mode speed}=c_{\rm info}}.
\]

## 3. Carrier mismatch correction / carrier 불일치 교정

A more important problem is that the earlier symbol \(v_{\rm sup}\) was introduced inside a local support-capacity ansatz,

\[
E_{\rm sup}=\mu_Ic_{\rm info}^2\Phi(v_{\rm sup}/c_{\rm info}),
\]

whereas \(c_{\rm info}\) is defined for metric expansion of distinguishability support.

These are not automatically the same data type.

A local constitutive support-rate parameter may describe local reorganization, deformation, relaxation, or another capacity variable without being the speed of a propagation front across the localization carrier.

Therefore even the inequality

\[
0\le\frac{v_{\rm sup}}{c_{\rm info}}\le1
\]

is not a generic DSD consequence unless an explicit **support-propagation interface** identifies \(v_{\rm sup}\) with a front rate to which the finite-propagation theorem applies.

This is a correction to the previous factorization.

## 4. Conditional front specialization / 조건부 front 특수화

If a later physical specialization supplies a metric localization length, a support-failure front, and an interface proving that failure at the target cannot precede arrival of the relevant distinguishability front, then define

\[
\zeta_{\rm front}
\equiv
\frac{v_{\rm front}}{c_{\rm info}}.
\]

Under the finite-propagation hypotheses,

\[
0\le\zeta_{\rm front}\le1.
\]

But

\[
\boxed{\zeta_{\rm front}=1}
\]

requires a saturating perturbation/mode. It is an additional sharpness condition, not an implication of the existence of \(c_{\rm info}\).

## 5. Critical-radius consequence / 임계반지름 결과

After the eta_I audit, the universal branch is written with

\[
K_{\rm eff}=K_g/\eta_0.
\]

The most conservative radius candidate is now

\[
\boxed{
R_{\rm crit}
=
\frac{K_{\rm eff}M}
{\Phi(\xi)c_{\rm info}^2}
}
\]

where \(\xi\) is a declared dimensionless support-state variable whose physical carrier must be specified by the downstream constitutive model.

Only when a valid support-propagation interface is supplied may one specialize

\[
\xi=\zeta_{\rm front}=v_{\rm front}/c_{\rm info}.
\]

Thus the generic black-hole threshold should **not** assume \(\zeta=1\).

## 6. Sensitivity control / 민감도 통제

For sensitivity only, take the special quadratic law

\[
\Phi(\zeta)=\frac12\zeta^2.
\]

Relative to the saturated value \(\zeta=1\), the candidate radius scales as

\[
\frac{R_{\rm crit}(\zeta)}{R_{\rm crit}(1)}
=\frac1{\zeta^2}.
\]

Examples:

| \(\zeta\) | quadratic relative radius |
|---:|---:|
| 1.0 | 1.0000 |
| 0.99 | 1.0203 |
| 0.9 | 1.2346 |
| 0.8 | 1.5625 |
| 0.5 | 4.0000 |

A quartic-corrected constitutive law with the same low-speed quadratic coefficient produces different sensitivities. Therefore uncertainty in the constitutive shape \(\Phi\) and uncertainty in the saturation/front parameter are separate.

This table is not a black-hole prediction; it is a coefficient-sensitivity control.

## 7. What survives / 살아남은 구조

The following chain survives:

\[
\text{source}
\to K_{\rm eff}M/r
\to\text{declared support capacity}
\to R_{\rm crit}.
\]

But the capacity bridge must now be written without silently identifying a local support rate with the propagation bound.

The safe general form is

\[
C_{\rm sup}=c_{\rm info}^2\Psi(S_{\rm sup}),
\]

where \(S_{\rm sup}\) is the declared support-state data and \(\Psi\) is a downstream constitutive readout.

Then

\[
\boxed{
R_{\rm crit}
=
\frac{K_{\rm eff}M}
{c_{\rm info}^2\Psi(S_{\rm sup})}
}.
\]

A one-parameter front specialization may later set

\[
\Psi(S_{\rm sup})=\Phi(\zeta_{\rm front}),
\]

but this is no longer part of the generic core.

## 8. Numerical audit / 수치 감사

The reproducibility script checks:

1. a valid front can remain strictly below \(c_{\rm info}\);
2. saturation is an extra condition;
3. a local support rate needs an interface before comparison with \(c_{\rm info}\);
4. the radius coefficient is sensitive to sub-saturation values;
5. constitutive shape and saturation are separate uncertainties;
6. no Schwarzschild/EHT datum sets \(\zeta\);
7. the old substitution requires refinement;
8. \(\zeta=1\) is not derived.

Result:

```text
8/8 PASS
STATUS: PASS_WITH_CORRECTION / SATURATION_NOT_DERIVED
```

Repository command:

```bash
python audits/science/2026-09-11_structural_gravity_zeta_saturation_interface_audit.py --mode all
```

## 9. Verdict / 판정

```text
VERDICT:
PASS_WITH_CORRECTION / SATURATION_NOT_DERIVED

MAXIMUM_SUPPORTED_CLAIM:
DSD supplies c_info as an infimal propagation upper bound. A front rate governed by the same distinguishability-support propagation can be bounded by c_info under explicit localization and interface assumptions, but equality requires a saturating mode. A local constitutive support rate is not automatically such a front rate. Therefore zeta=1 is not a generic DSD result, and even the parametrization v_sup=zeta*c_info must be restricted to a declared support-propagation specialization.

CORRECTION:
Replace the generic threshold Theta_*=eta_I Phi(zeta) by a carrier-explicit downstream capacity Psi(S_sup). In the universal eta branch, absorb eta_0 into K_eff and write R_crit=K_eff M/[c_info^2 Psi(S_sup)]. Recover Phi(zeta_front) only after a valid front interface is supplied.

UNSUPPORTED:
- zeta=1 from the definition of c_info
- identification of every local support/reorganization rate with c_info
- use of the Schwarzschild coefficient to choose saturation
```

## 10. Next audit / 다음 감사

The remaining coefficient problem is now better posed. Audit the dimensionless support-capacity functional

\[
\boxed{\Psi(S_{\rm sup})}
\]

itself, rather than trying to force \(\zeta=1\).

The next question is whether structural support failure supplies a dimensionless critical value from DSD-internal state relations, or whether an additional physical constitutive law remains unavoidable. The Schwarzschild value must remain sealed during this audit.
