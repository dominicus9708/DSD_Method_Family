# Structural-Gravity Support-Capacity Constitutive Interface
# 구조적 중력 지지용량 구성법칙 인터페이스

```text
INTERFACE_ID: DSD-METHOD-20260911-SG-SUPPORT-001
STATUS: ACTIVE_DRAFT
DOMAIN: structural gravity / black-hole critical radius
DATE: 2026-09-11
RELATED_AUDIT: audits/science/2026-09-11_structural-gravity-nu-kin-constitutive-audit.md
```

## 1. Purpose / 목적

This interface prevents a propagation-speed bound from being silently promoted into an energy, inertia, or support-capacity law.

The structural-gravity black-hole benchmark may use \(c_{\rm info}\) as a velocity scale, but any physical support-failure threshold must supply a separate constitutive function.

## 2. General constitutive form / 일반 구성법칙형

Write

\[
E_{\rm sup}(v)
=
\mu_Ic_{\rm info}^2\Phi(\beta),
\qquad
\beta=\frac{v}{c_{\rm info}}.
\]

The symbols have separate roles:

- \(c_{\rm info}\): propagation-speed upper bound of the chosen dynamic model;
- \(\mu_I\): structural inertial scale of the support sector;
- \(\Phi\): dimensionless constitutive support-capacity function;
- \(v\): realized support/reorganization rate in the supplied physical specialization.

None of these identifications is supplied automatically by Formation, Property, or generic Structural Reorganization Dynamics.

## 3. Threshold readout / 임계 readout

Let

\[
v_{\rm sup}=\zeta c_{\rm info},
\qquad 0<\zeta\le1,
\]

and let

\[
\eta_I=\frac{\mu_I}{\mu_g}
\]

compare the support-inertial carrier with the source-coupled carrier.

Then

\[
C_{\rm sup}
=
\eta_Ic_{\rm info}^2\Phi(\zeta).
\]

When the structural-load candidate

\[
U_X(R)=K_g\frac{M}{R}
\]

is equated with that capacity, the threshold family is

\[
\boxed{\Theta_*=\eta_I\Phi(\zeta)}
\]

and

\[
\boxed{
R_{\rm crit}
=
\frac{K_gM}
{\eta_I\Phi(\zeta)c_{\rm info}^2}
}.
\]

## 4. Quadratic special case / 이차형 특수 경우

A global quadratic specialization is

\[
\Phi(\beta)=\nu_{\rm kin}\beta^2.
\]

Only in that case does

\[
\Theta_*=\nu_{\rm kin}\eta_I\zeta^2
\]

hold globally.

For a smooth reversal-symmetric local law,

\[
\Phi(\beta)
=
\nu_2\beta^2+\nu_4\beta^4+\cdots.
\]

Thus the notation \(\nu_{\rm kin}\) must not be used ambiguously. It means either:

1. the local leading coefficient \(\nu_2\); or
2. a global coefficient only after a separate audit establishes \(\nu_4=\nu_6=\cdots=0\) over the relevant regime.

## 5. Conditional low-speed half / 조건부 저속 \(1/2\)

If a downstream inertial work/momentum bridge supplies

\[
\frac{dE_{\rm sup}}{dv}=p_{\rm eff}(v),
\qquad
p_{\rm eff}(v)=\mu_Iv+O(v^3/c_{\rm info}^2),
\]

then

\[
\Phi(\beta)=\frac12\beta^2+O(\beta^4).
\]

Therefore \(1/2\) may be recovered as the leading low-speed coefficient, but this does not establish

\[
\Phi(1)=\frac12.
\]

## 6. Saturation firewall / 포화 방화벽

A finite propagation bound does not imply that every structural process reaches that bound.

Consequently

\[
\zeta=1
\]

must remain a separate physical statement.

Likewise, even when the low-speed coefficient is \(1/2\), higher-order terms in \(\Phi\) may dominate as \(\zeta\to1\).

The two questions

```text
Does the process saturate c_info?
What is the constitutive capacity at that rate?
```

must remain separate.

## 7. Comparator firewall / 비교식 방화벽

Only after \(\Phi\), \(\eta_I\), \(\zeta\), \(K_g\), and the physical interpretation of \(c_{\rm info}\) are fixed independently may the external Schwarzschild comparator be opened.

Then

\[
\boxed{
\frac{R_{\rm crit}}{R_S}
=
\frac{1}{2\eta_I\Phi(\zeta)}
\frac{K_g}{G}
\left(\frac{c}{c_{\rm info}}\right)^2
}.
\]

Do not choose \(\Phi\) or its coefficients from this identity.

## 8. Provenance labels / 출처 표기

```text
R0 / PRE-EXISTING DSD:
- c_info as an infimal propagation bound under declared model assumptions
- downstream-bridge discipline
- separation of transport, property, formation, and rank transitions

R1 / GENERAL STRUCTURAL-MATHEMATICAL:
- dimensionless constitutive-function representation
- even local expansion under smooth reversal symmetry

DOWNSTREAM PHYSICAL SPECIALIZATION:
- mu_I
- mu_g
- eta_I
- Phi
- zeta
- work/momentum bridge
- support-failure equation

EXTERNAL COMPARATOR ONLY:
- G
- c
- Schwarzschild/Kerr relations
```

## 9. Current decision / 현재 판정

```text
GENERAL FORM:
Theta_* = eta_I Phi(zeta)

QUADRATIC FORM:
Theta_* = nu_kin eta_I zeta^2
only if Phi(zeta)=nu_kin zeta^2 is independently established.

LOW-SPEED RESULT:
nu_2 = 1/2 is conditionally recoverable from an inertial work/momentum bridge.

OPEN:
eta_I
zeta
higher-order constitutive terms
K_g/G
c_info/c
```

## 10. Audit order / 감사 순서

1. \(\eta_I\): determine whether support inertia and source coupling are independent, proportional, or identical.
2. \(\zeta\): determine whether local-collapse convergence saturates \(c_{\rm info}\).
3. \(\Phi\) at high \(\zeta\): establish or reject global quadraticity.
4. Only then reopen black-hole comparators and perform no-retuning cross-target tests.
