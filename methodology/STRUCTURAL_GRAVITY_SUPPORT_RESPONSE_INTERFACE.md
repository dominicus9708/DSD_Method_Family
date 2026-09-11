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
v_{\rm sup}=\zeta c_{\rm info},
\qquad
0<\zeta\le1,
\qquad
\eta_I=\frac{\mu_I}{\mu_g}.
\]

Then

\[
C_{\rm sup}
=\frac{E_{\rm sup,max}}{\mu_g}
=\eta_Ic_{\rm info}^2
\int_0^\zeta\phi(s)\,ds.
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
{\eta_Ic_{\rm info}^2I_\phi(\zeta)}
},
\qquad
I_\phi(\zeta):=\int_0^\zeta\phi(s)\,ds.
\]

## 4. Linear-response specialization / 선형응답 특수화

If

\[
\phi(s)=s
\]

throughout the relevant interval, then

\[
I_\phi(\zeta)=\frac12\zeta^2
\]

and

\[
R_{\rm crit}
=\frac{2K_gM}
{\eta_I\zeta^2c_{\rm info}^2}.
\]

The factor \(1/2\) therefore comes from global linear response, not from \(c_{\rm info}\) alone.

## 5. Identification firewall / 식별 방화벽

The candidate radius depends on

\[
\frac{K_g}{\eta_II_\phi(\zeta)c_{\rm info}^2}.
\]

Consequently:

- \(K_g\) and \(\eta_I\) have a common-rescaling degeneracy in the radius sector;
- \(\eta_I=1\) requires an explicit identification of \(\mu_I\) and \(\mu_g\);
- low-speed linearity does not establish global linearity up to \(\zeta\simeq1\);
- \(\zeta=1\) cannot be inferred merely because \(c_{\rm info}\) is an upper bound.

## 6. Required independent audits / 필요한 독립 감사

Before opening the Schwarzschild comparator, independently audit:

1. response law \(\phi\);
2. inertial/source measure ratio \(\eta_I\);
3. saturation factor \(\zeta\);
4. source normalization \(K_g\);
5. physical interpretation and calibration of \(c_{\rm info}\).

Do not fit any of these quantities to one black-hole radius and then reuse that target as validation.

## 7. Related audits / 관련 감사

```text
audits/science/2026-09-11_structural-gravity-support-threshold-factorization-audit.md
audits/science/2026-09-11_structural-gravity-inertial-response-integral-audit.md
audits/science/2026-09-11_structural-gravity-inertial-source-identifiability-audit.md
```

Reproduction commands:

```bash
python audits/science/2026-09-11_structural_gravity_support_threshold_factorization.py --mode all
python audits/science/2026-09-11_structural_gravity_inertial_response_integral_audit.py --mode all
python audits/science/2026-09-11_structural_gravity_inertial_source_identifiability_audit.py --mode all
```
