# Structural-Gravity \(\nu_{\rm kin}\) Constitutive Audit
# 구조적 중력 \(\nu_{\rm kin}\) 구성법칙 감사

```text
AUDIT_ID: DSD-AUDIT-20260911-PHYSICS-BH-003
STATUS: PASS_WITH_BOUNDARY / CONSTITUTIVE_FUNCTION_REFINEMENT
DOMAIN: structural gravity / black-hole critical radius
DATE: 2026-09-11
PARENT_AUDIT: audits/science/2026-09-11_structural-gravity-support-threshold-factorization-audit.md
RELATED_CODE: audits/science/2026-09-11_structural_gravity_nu_kin_constitutive_audit.py
```

## 1. Audit question / 감사 질문

Can the first open bridge factor

\[
\nu_{\rm kin}=\frac12
\]

be justified independently of the Schwarzschild coefficient, or is the previously used globally quadratic support law too strong?

The answer is split into two levels:

1. a quadratic **leading low-speed term** can be justified under explicit regularity and reversal-symmetry assumptions;
2. the coefficient \(1/2\) and the extension of that quadratic law up to \(v\sim c_{\rm info}\) require additional constitutive physics.

## 2. DSD boundary carried forward / 계승 경계

The current Structural Reorganization Dynamics paper defines \(c_{\rm info}\) as an infimal finite propagation bound for a declared model class and discrepancy convention. Its numerical value and saturation are not consequences of the word information.

The same paper also states that equality with a characteristic upper bound requires a sharp or saturating propagation mode and is not implied by hyperbolicity alone.

Therefore \(c_{\rm info}\) is not by itself an energy normalization, inertia law, work law, or kinetic constitutive relation.

## 3. General support-capacity function / 일반 지지용량 함수

Replace the globally quadratic ansatz by the more general downstream specialization

\[
\boxed{
E_{\rm sup}(v)
=
\mu_I c_{\rm info}^2\,
\Phi\!\left(\frac{v}{c_{\rm info}}\right)
}
\]

with

\[
\beta\equiv\frac{v}{c_{\rm info}}.
\]

This form only says that \(\mu_I\) supplies the inertial scale and \(c_{\rm info}\) supplies a velocity scale. The dimensionless constitutive function \(\Phi\) remains downstream data.

For a support state with

\[
v_{\rm sup}=\zeta c_{\rm info},
\]

the capacity per source-coupled carrier is

\[
C_{\rm sup}
=
\eta_I c_{\rm info}^2\Phi(\zeta),
\qquad
\eta_I\equiv\frac{\mu_I}{\mu_g}.
\]

Hence the general threshold factor is

\[
\boxed{
\Theta_*=\eta_I\Phi(\zeta)
}
\]

and the candidate radius becomes

\[
\boxed{
R_{\rm crit}
=
\frac{K_gM}
{\eta_I\Phi(\zeta)c_{\rm info}^2}
}.
\]

The previous relation

\[
\Theta_*=\nu_{\rm kin}\eta_I\zeta^2
\]

is therefore a special case obtained only when

\[
\Phi(\zeta)=\nu_{\rm kin}\zeta^2
\]

holds over the entire relevant interval.

## 4. What smooth reversal symmetry actually gives / 매끄러운 반전대칭이 주는 것

Assume locally near \(v=0\):

1. \(E_{\rm sup}(0)=0\);
2. the constitutive law is smooth enough for an even expansion;
3. reversing the support/reorganization direction does not change the scalar support energy,
   \(E_{\rm sup}(-v)=E_{\rm sup}(v)\).

Then

\[
\Phi(\beta)
=
\nu_2\beta^2
+
\nu_4\beta^4
+
\nu_6\beta^6
+\cdots.
\]

Thus a quadratic leading term is natural in this local smooth-even specialization.

But these assumptions do **not** determine \(\nu_2\).

Equivalently, when \(\Phi\) is twice differentiable,

\[
\nu_2=\frac12\Phi''(0),
\]

and generic DSD does not currently fix \(\Phi''(0)\).

## 5. Conditional origin of the factor \(1/2\) / \(1/2\)의 조건부 기원

Add a separate low-speed work/momentum bridge

\[
\frac{dE_{\rm sup}}{dv}=p_{\rm eff}(v)
\]

and an inertial response law

\[
p_{\rm eff}(v)
=
\mu_Iv
+
O\!\left(\frac{v^3}{c_{\rm info}^2}\right).
\]

Then

\[
\frac{dE_{\rm sup}}{dv}
=
\mu_Iv+O(v^3/c_{\rm info}^2).
\]

With \(E_{\rm sup}(0)=0\), integration gives

\[
E_{\rm sup}(v)
=
\frac12\mu_Iv^2
+
O\!\left(\frac{\mu_Iv^4}{c_{\rm info}^2}\right),
\]

or

\[
\boxed{
\Phi(\beta)
=
\frac12\beta^2+O(\beta^4)
}.
\]

Therefore

\[
\boxed{\nu_2=\frac12}
\]

is conditionally recoverable as a **leading low-speed coefficient** once that inertial work/momentum bridge is supplied.

It is not yet a theorem of generic DSD or of the present structural-gravity sector.

## 6. Why this does not justify global \(\nu_{\rm kin}=1/2\) / 전구간 이차법칙이 되지 않는 이유

Three constitutive examples can share the same low-speed coefficient \(1/2\) while differing strongly near the propagation bound:

\[
\Phi_A(\zeta)=\frac12\zeta^2,
\]

\[
\Phi_B(\zeta)=\frac12\zeta^2+0.1\zeta^4,
\]

and, as a non-polynomial comparison law,

\[
\Phi_C(\zeta)
=
\frac{1}{\sqrt{1-\zeta^2}}-1,
\qquad 0\le\zeta<1.
\]

All have

\[
\Phi(\zeta)=\frac12\zeta^2+O(\zeta^4)
\]

near zero, but at \(\zeta=0.9\),

```text
Phi_A = 0.405000
Phi_B = 0.470610
Phi_C = 1.294157
```

and at \(\zeta=0.99\),

```text
Phi_A = 0.490050
Phi_B = 0.586110
Phi_C = 6.088812
```

Thus

\[
\boxed{
\text{low-speed coefficient }1/2
\not\Rightarrow
\text{global quadratic capacity up to }\zeta\approx1
}
\]

is an explicit countermodel result.

## 7. Independent nonuniqueness of \(\nu_{\rm kin}\) / 계수 비유일성

Even if one insists on a pure quadratic family

\[
\Phi(\zeta)=\nu\zeta^2,
\]

the same \(c_{\rm info}\) is compatible with, for example,

\[
\nu=0.3,\quad0.5,\quad0.8.
\]

At \(\zeta=0.9\), these give

```text
nu = 0.3 -> Phi = 0.243
nu = 0.5 -> Phi = 0.405
nu = 0.8 -> Phi = 0.648
```

so \(c_{\rm info}\) alone does not determine the coefficient.

## 8. Updated Schwarzschild comparator / 갱신된 외부 비교식

Only after the DSD-side constitutive function is frozen should the external Schwarzschild comparator be opened.

The generalized ratio is

\[
\boxed{
\frac{R_{\rm crit}}{R_S}
=
\frac{1}{2\eta_I\Phi(\zeta)}
\frac{K_g}{G}
\left(\frac{c}{c_{\rm info}}\right)^2
}.
\]

The old quadratic expression is recovered only under

\[
\Phi(\zeta)=\nu_{\rm kin}\zeta^2.
\]

No black-hole observable is used here to choose \(\Phi\), \(\nu_2\), or any higher-order coefficient.

## 9. Reproducibility / 재현성

Run

```bash
python audits/science/2026-09-11_structural_gravity_nu_kin_constitutive_audit.py --mode all
```

Current result:

```text
8/8 checks passed
STATUS: PASS_WITH_BOUNDARY / CONSTITUTIVE_FUNCTION_REFINEMENT
```

## 10. Verdict / 판정

```text
VERDICT:
PASS_WITH_BOUNDARY / CONSTITUTIVE_FUNCTION_REFINEMENT

SUPPORTED:
- a smooth reversal-symmetric support-energy specialization has an even local expansion;
- its first nonzero regular term may be quadratic;
- nu_2 = 1/2 follows conditionally from an independent low-speed work/momentum bridge;
- the general critical coefficient is Theta_* = eta_I Phi(zeta).

NOT DERIVED:
- a global pure-quadratic law Phi(zeta)=1/2 zeta^2;
- validity of the low-speed expansion at zeta=1;
- eta_I = 1;
- zeta = 1;
- K_g = G;
- c_info = c;
- R_crit = R_S.
```

## 11. Consequence for the previous factorization / 이전 분해식에 대한 결과

The BH-002 factorization remains valid as the **globally quadratic special case**, but its general form must now be written

\[
\boxed{\Theta_*=\eta_I\Phi(\zeta)}.
\]

Accordingly, \(\nu_{\rm kin}\) should be treated as either:

1. the leading local coefficient \(\nu_2\), or
2. a global constant only after a separate constitutive audit establishes a pure quadratic law over the relevant regime.

## 12. Next target / 다음 대상

The next independent factor is

\[
\eta_I=\frac{\mu_I}{\mu_g}.
\]

Audit whether structural inertial response and source-coupled strength can be identified, related by a constant, or must remain independent property channels. This must be decided without importing the equivalence principle or setting \(\eta_I=1\) to recover Schwarzschild.
