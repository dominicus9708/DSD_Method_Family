# Structural-Gravity Support-Response Interface
# 구조적 중력 지지응답 인터페이스

```text
INTERFACE_ID: DSD-METHOD-20260911-BH-SUPPORT-001
STATUS: ACTIVE_DRAFT
DOMAIN: structural gravity / support failure / black-hole critical radius
DATE: 2026-09-11
PARENT_PROTOCOL: methodology/BLACK_HOLE_CRITICAL_RADIUS_BENCHMARK_PROTOCOL.md
```

## 1. Purpose / 목적

This interface replaces an opaque critical coefficient with explicit downstream constitutive quantities before any Schwarzschild comparison is opened.

It is not part of generic Formation, Property, static aggregation, or generic Structural Reorganization Dynamics.

## 2. Structural-load candidate / 구조 하중 후보

In the coarse spherical structural-gravity specialization,

\[
U_X(R)=K_g\frac{M}{R}.
\]

This is inherited as a downstream candidate from the conditional far-field response sector.

## 3. General support response / 일반 지지응답

Supply

\[
\frac{dE_{\rm sup}}{dv}=P_I(v),
\qquad
E_{\rm sup}(0)=0,
\]

and represent the inertial response by

\[
P_I(v)=\mu_Ic_{\rm info}\phi(v/c_{\rm info}).
\]

Let

\[
\eta_I=\frac{\mu_I}{\mu_g}.
\]

The local support/collapse speed \(v_{\rm col}\) is **not** generically identified with the propagation bound \(c_{\rm info}\).

When both quantities are finite, positive, and metric-speed quantities in the chosen specialization, define only the comparison ratio

\[
\boxed{
\beta_{\rm col}:=\frac{v_{\rm col}}{c_{\rm info}}>0
}.
\]

Generic DSD does not imply \(\beta_{\rm col}\le1\).

Then

\[
C_{\rm sup}
=\frac{E_{\rm sup,max}}{\mu_g}
=\eta_Ic_{\rm info}^2
\int_0^{\beta_{\rm col}}\phi(s)\,ds.
\]

The support-failure threshold

\[
U_X(R_{\rm crit})=C_{\rm sup}
\]

gives

\[
\boxed{
R_{\rm crit}
=\frac{K_gM}
{\eta_Ic_{\rm info}^2I_\phi(\beta_{\rm col})}
},
\qquad
I_\phi(\beta):=\int_0^\beta\phi(s)\,ds.
\]

### 3.1 Bounded collapse-to-propagation specialization / 유계 붕괴-전파 특수화

Only if an additional constitutive or causal bridge independently proves

\[
v_{\rm col}\le c_{\rm info}
\]

may one introduce

\[
\zeta_{\rm col}
:=\frac{v_{\rm col}}{c_{\rm info}}
\in(0,1].
\]

The earlier notation \(v_{\rm sup}=\zeta c_{\rm info}\), \(0<\zeta\le1\), is retained only as this extra specialization.

The equality

\[
\zeta_{\rm col}=1
\]

requires a further saturation theorem and is not implied by the definition of \(c_{\rm info}\).

## 4. Linear-response specialization / 선형응답 특수화

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

Hence

\[
\boxed{
R_{\rm crit}
=\frac{2K_gM}
{\eta_Iv_{\rm col}^2}
}.
\]

Thus the factor \(1/2\) comes from global linear response, while \(c_{\rm info}\) cancels from the linear-response radius after the actual local collapse/support speed is kept distinct.

The previous bounded formula

\[
R_{\rm crit}
=\frac{2K_gM}
{\eta_I\zeta_{\rm col}^2c_{\rm info}^2}
\]

is recovered only inside the additional bridge \(v_{\rm col}=\zeta_{\rm col}c_{\rm info}\).

## 5. Identification firewall / 식별 방화벽

The generic candidate radius depends on

\[
\frac{K_g}{\eta_II_\phi(\beta_{\rm col})c_{\rm info}^2}.
\]

Consequently:

- \(K_g\) and \(\eta_I\) have a common-rescaling degeneracy in the radius sector;
- \(\eta_I=1\) requires an explicit identification of \(\mu_I\) and \(\mu_g\);
- low-speed linearity does not establish global linearity through the critical interval;
- \(c_{\rm info}\) constrains discrepancy-support propagation, not automatically the rate of a local collapse coordinate;
- \(v_{\rm col}\le c_{\rm info}\) requires a separate constitutive or causal bridge;
- \(v_{\rm col}=c_{\rm info}\) requires a further saturation result;
- physical identification with relativistic \(c\) remains a separate calibration question.

## 6. Required independent audits / 필요한 독립 감사

Before opening the Schwarzschild comparator, independently audit:

1. response law \(\phi\);
2. inertial/source measure ratio \(\eta_I\);
3. local collapse/support speed \(v_{\rm col}\);
4. any bridge between \(v_{\rm col}\) and \(c_{\rm info}\);
5. source normalization \(K_g\);
6. physical interpretation and calibration of \(c_{\rm info}\) and/or \(v_{\rm col}\).

Do not fit any of these quantities to one black-hole radius and then reuse that target as validation.

## 7. Related audits / 관련 감사

```text
audits/science/2026-09-11_structural-gravity-support-threshold-factorization-audit.md
audits/science/2026-09-11_structural-gravity-inertial-response-integral-audit.md
audits/science/2026-09-11_structural-gravity-inertial-source-identifiability-audit.md
audits/science/2026-09-11_structural-gravity-collapse-speed-bridge-audit.md
```

Reproduction commands:

```bash
python audits/science/2026-09-11_structural_gravity_support_threshold_factorization.py --mode all
python audits/science/2026-09-11_structural_gravity_inertial_response_integral_audit.py --mode all
python audits/science/2026-09-11_structural_gravity_inertial_source_identifiability_audit.py --mode all
python audits/science/2026-09-11_structural_gravity_collapse_speed_bridge_audit.py --mode all
```
