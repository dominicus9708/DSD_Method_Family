# Structural-Gravity Inertial-Response Integral Audit
# 구조적 중력 관성응답 적분 감사

```text
AUDIT_ID: DSD-AUDIT-20260911-PHYSICS-BH-003
STATUS: PASS_WITH_BOUNDARY / LINEAR_RESPONSE_REQUIRED_FOR_EXACT_HALF
DOMAIN: structural gravity / black-hole critical radius
DATE: 2026-09-11
RELATED_METHOD: methodology/BLACK_HOLE_CRITICAL_RADIUS_BENCHMARK_PROTOCOL.md
RELATED_CODE: audits/science/2026-09-11_structural_gravity_inertial_response_integral_audit.py
PARENT_AUDIT: audits/science/2026-09-11_structural-gravity-support-threshold-factorization-audit.md
```

## 1. Audit question / 감사 질문

Can the previously introduced support coefficient \(\nu_{\rm kin}=1/2\) be reduced from an arbitrary normalization to a more explicit constitutive condition, without importing the Schwarzschild radius or fitting a black-hole observable?

The target is not to prove the value \(1/2\) from generic DSD. The target is to identify exactly what downstream response law would make \(1/2\) follow.

## 2. Foundational boundary / 기초 경계

The Structural Reorganization Dynamics paper treats \(c_{\rm info}\) as a finite structural-information propagation bound. It does not by itself choose an inertia law, an energy functional, a restoring law, or a constitutive coupling.

Therefore an exact support-energy coefficient cannot be inferred from \(c_{\rm info}\) alone.

The static aggregation layer likewise introduces no physical constitutive law; such laws require downstream specialization.

## 3. Response-integral bridge / 응답 적분 교량

Introduce an explicit downstream support/inertial response law.

Let \(v\ge0\) be the magnitude of the support/reorganization response speed and let \(P_I(v)\) be its conjugate inertial-response quantity. Supply the work-like bridge

\[
\frac{dE_{\rm sup}}{dv}=P_I(v),
\qquad E_{\rm sup}(0)=0.
\]

Write the response in dimensionless form

\[
P_I(v)
=\mu_I c_{\rm info}\,
\phi\!\left(\frac{v}{c_{\rm info}}\right),
\]

where \(\phi\) is a supplied dimensionless constitutive response function.

Let

\[
v_{\rm sup}=\zeta c_{\rm info},
\qquad 0<\zeta\le1,
\]

and

\[
\eta_I=\frac{\mu_I}{\mu_g}.
\]

Then

\[
E_{\rm sup,max}
=
\mu_I c_{\rm info}^2
\int_0^\zeta \phi(s)\,ds,
\]

so the support capacity per source-coupled carrier becomes

\[
C_{\rm sup}
=
\eta_I c_{\rm info}^2
\int_0^\zeta \phi(s)\,ds.
\]

Hence the critical coefficient is more generally

\[
\boxed{
\Theta_*
=
\eta_I
\int_0^\zeta \phi(s)\,ds
}.
\]

This replaces the earlier opaque product \(\nu_{\rm kin}\eta_I\zeta^2\) by an explicit response integral.

## 4. Exact origin of the factor 1/2 / 1/2 계수의 정확한 기원

If the downstream response is globally linear over the full relevant interval,

\[
\phi(s)=s,
\]

then

\[
\Theta_*
=
\eta_I\int_0^\zeta s\,ds
=
\frac12\eta_I\zeta^2.
\]

Thus the earlier quadratic normalization

\[
\nu_{\rm kin}=\frac12
\]

is not an independent coefficient in this specialization. It is the integral consequence of the stronger constitutive statement

\[
P_I(v)=\mu_I v
\]

throughout the response range used by the threshold calculation.

For the additional conditional values

\[
\eta_I=1,
\qquad
\zeta=1,
\]

one obtains

\[
\Theta_*=\frac12.
\]

This remains conditional because generic DSD does not currently derive the globally linear response law, \(\eta_I=1\), or saturation \(\zeta=1\).

## 5. Why low-speed linearity is insufficient / 저속 선형성만으로 부족한 이유

Suppose only the small-speed behavior is known,

\[
\phi(s)=s+O(s^3)
\qquad (s\to0).
\]

Then

\[
\Theta_*
=
\frac12\eta_I\zeta^2
+O(\zeta^4)
\]

for small \(\zeta\).

However, a black-hole support threshold would be evaluated near the upper end of the allowed response range if \(\zeta\) is close to one. Therefore the low-speed expansion cannot by itself justify the exact coefficient \(1/2\) at saturation.

The full response curve must be fixed or bounded.

## 6. Reproducible response-family calculation / 재현 가능한 응답군 계산

Run

```bash
python audits/science/2026-09-11_structural_gravity_inertial_response_integral_audit.py --mode all
```

For \(\eta_I=1\) and \(\zeta=1\), the blind response integral gives:

```text
phi(s) = s                    -> Theta_* = 0.500000000000
phi(s) = s + 0.5 s^3          -> Theta_* = 0.625000000003
phi(s) = s - 0.5 s^3          -> Theta_* = 0.374999999997
phi(s) = tanh(s)               -> Theta_* = 0.433780830482
phi(s) = s^2                   -> Theta_* = 0.333333333338
```

All 9/9 checks pass.

No \(G\), physical \(c\), Schwarzschild radius, EHT ring, or black-hole radius is used by this blind response calculation.

## 7. Small-speed masking / 저속 구간의 은폐 효과

For the linear, hardening, and softening response laws:

```text
zeta   linear       hardening     softening
0.10   0.005000     0.0050125     0.0049875
0.25   0.031250     0.0317383     0.0307617
0.50   0.125000     0.1328125     0.1171875
0.75   0.281250     0.3208008     0.2416992
1.00   0.500000     0.6250000     0.3750000
```

At small \(\zeta\), nonlinear response laws can mimic the linear law closely. Near saturation they produce materially different critical coefficients.

Therefore a low-field or low-speed calibration is not enough to fix the strong-collapse threshold.

## 8. Updated critical-radius family / 갱신된 임계반지름 군

Matching the structural load candidate

\[
U_X(R)=K_g\frac{M}{R}
\]

to the response-integral support capacity gives

\[
\boxed{
R_{\rm crit}
=
\frac{K_gM}
{\eta_I c_{\rm info}^2\int_0^\zeta\phi(s)\,ds}
}.
\]

The earlier formula with \(\nu_{\rm kin}\) is recovered only when the response family has the corresponding quadratic form.

In the globally linear specialization,

\[
R_{\rm crit}
=
\frac{2K_gM}
{\eta_I\zeta^2c_{\rm info}^2}.
\]

This is still a DSD downstream candidate family, not a Schwarzschild derivation.

## 9. Provenance ledger / 출처 장부

```text
R0 / PRE-EXISTING DSD:
- downstream constitutive bridges must be explicit;
- c_info is a propagation bound, not an automatic physical energy normalization;
- no universal physical constitutive law is supplied by the static or generic dynamic layer.

R1 / GENERAL MATHEMATICAL STRUCTURE:
- define a response function phi;
- integrate dE/dv = P(v);
- exact linear response gives an exact 1/2 integral coefficient.

DOWNSTREAM STRUCTURAL-GRAVITY SPECIALIZATION:
- dE_sup/dv = P_I(v);
- P_I(v) = mu_I c_info phi(v/c_info);
- eta_I = mu_I/mu_g;
- v_sup = zeta c_info;
- U_X(R) = K_g M/R.

EXTERNAL COMPARATOR:
- none used in the blind response audit.
```

## 10. Verdict / 판정

```text
VERDICT:
PASS_WITH_BOUNDARY / LINEAR_RESPONSE_REQUIRED_FOR_EXACT_HALF

ADVANCE:
- the factor 1/2 is no longer merely an arbitrary nu_kin choice;
- it is exactly generated by a globally linear inertial-response law;
- the general threshold becomes an integral over a constitutive response function;
- the strong-collapse regime can now be distinguished from low-speed calibration.

NOT DERIVED:
- global phi(s)=s up to saturation;
- eta_I = 1;
- zeta = 1;
- K_g = G;
- c_info = c;
- R_crit = R_S.
```

## 11. Next target / 다음 대상

The next independent bridge audit is \(\eta_I=\mu_I/\mu_g\).

The question is whether the structural inertial measure controlling support response and the source-coupled measure entering \(U_X\) are forced to coincide, are related by a fixed bridge, or must remain independent parameters.

Only after that audit should the saturation factor \(\zeta\) be tested.
