# Structural-Gravity Support-Threshold Factorization Audit
# 구조적 중력 지지 임계계수 분해 감사

```text
AUDIT_ID: DSD-AUDIT-20260911-PHYSICS-BH-002
STATUS: PASS_WITH_BOUNDARY / OPEN_COEFFICIENT
DOMAIN: structural gravity / black-hole critical radius
DATE: 2026-09-11
RELATED_METHOD: methodology/BLACK_HOLE_CRITICAL_RADIUS_BENCHMARK_PROTOCOL.md
RELATED_CODE: audits/science/2026-09-11_structural_gravity_support_threshold_factorization.py
PARENT_AUDIT: audits/science/2026-09-11_sgra-structural-gravity-radius-benchmark-audit.md
```

## 1. Audit question / 감사 질문

Can the previously open critical coefficient \(\Theta_*\) be obtained from the current DSD propagation bound \(c_{\rm info}\) alone, or must the structural-support threshold contain additional downstream constitutive factors?

The target is not to fit the Schwarzschild coefficient. The target is to decompose the missing coefficient before any comparison is opened.

## 2. Core firewall / 핵심 경계

The current Structural Reorganization Dynamics paper gives \(c_{\rm info}\) the role of a finite propagation-speed upper bound. It does not by itself fix amplitudes, inertia, stiffness, restoring terms, damping, or constitutive couplings.

Therefore the quotient

\[
\Theta_X(r)=\frac{|X(r)|}{c_{\rm info}^2}
\]

may be used as a dimensionless diagnostic candidate, but \(c_{\rm info}^2\) must not be silently interpreted as a universal structural-support energy or capacity.

This corrects an ambiguity in the first Sgr A* benchmark: the dimensionless quotient is admissible as a diagnostic, while the physical threshold normalization remains a separate downstream bridge.

## 3. Carried-forward structural-gravity candidate / 계승 후보

In the coarse spherical benchmark sector,

\[
a_X(r)\simeq K_g\frac{M}{r^2}
\]

and, after the explicit static bridge

\[
a_X=-\frac{dX}{dr},\qquad X(\infty)=0,
\]

one obtains

\[
|X(r)|=K_g\frac{M}{r}.
\]

Call this candidate structural load per source unit

\[
U_X(R)\equiv |X(R)|=K_g\frac{M}{R}.
\]

No Schwarzschild relation is used here.

## 4. Explicit support-capacity bridge / 명시적 지지용량 교량

Introduce, as a downstream physical specialization rather than a generic DSD theorem,

\[
E_{\rm sup,max}
=\nu_{\rm kin}\,\mu_I\,v_{\rm sup}^2.
\]

Here:

- \(\nu_{\rm kin}>0\) is the constitutive normalization of the support-energy law;
- \(\mu_I\) is the structural inertial measure relevant to the support sector;
- \(v_{\rm sup}=\zeta c_{\rm info}\), with \(0<\zeta\le1\), is the actually saturated support/reorganization speed relative to the propagation bound;
- \(\mu_g\) is the source-coupled carrier used to normalize the structural load;
- \(\eta_I\equiv\mu_I/\mu_g\).

Then the support capacity per source unit is

\[
C_{\rm sup}
=\frac{E_{\rm sup,max}}{\mu_g}
=\nu_{\rm kin}\eta_I\zeta^2c_{\rm info}^2.
\]

The threshold condition

\[
U_X(R_{\rm crit})=C_{\rm sup}
\]

therefore gives

\[
\boxed{
\Theta_*
=\nu_{\rm kin}\eta_I\zeta^2
}
\]

and

\[
\boxed{
R_{\rm crit}
=\frac{K_gM}
{\nu_{\rm kin}\eta_I\zeta^2c_{\rm info}^2}
}.
\]

This is the main result of the factorization audit.

## 5. Conditional half recovery / 조건부 1/2 복원

If, and only if, the downstream specialization additionally supplies

\[
\nu_{\rm kin}=\frac12,
\qquad
\eta_I=1,
\qquad
\zeta=1,
\]

then

\[
\boxed{\Theta_*=\frac12}.
\]

The three assumptions have distinct provenance:

1. \(\nu_{\rm kin}=1/2\): quadratic kinetic/support-energy normalization;
2. \(\eta_I=1\): equivalence between the inertial support measure and the source-coupled carrier;
3. \(\zeta=1\): exact saturation of the propagation bound by the support/reorganization process.

None of these three equalities is currently implied by generic DSD.

Hence the value \(1/2\) is conditionally reconstructible, but not yet independently derived.

## 6. Schwarzschild comparator opened only after factorization / 분해 후 비교

With the external comparator

\[
R_S=\frac{2GM}{c^2},
\]

the factorized ratio is

\[
\boxed{
\frac{R_{\rm crit}}{R_S}
=
\frac{1}{2\nu_{\rm kin}\eta_I\zeta^2}
\frac{K_g}{G}
\left(\frac{c}{c_{\rm info}}\right)^2
}.
\]

For the quadratic specialization \(\nu_{\rm kin}=1/2\), this reduces to

\[
\boxed{
\frac{R_{\rm crit}}{R_S}
=
\frac{K_g}{G}
\left(\frac{c}{c_{\rm info}}\right)^2
\frac{1}{\eta_I\zeta^2}
}.
\]

Exact Schwarzschild closure in that specialization would require

\[
\boxed{
\frac{K_g}{G}
\left(\frac{c}{c_{\rm info}}\right)^2
=\eta_I\zeta^2
}.
\]

This is a closure condition, not a derived identity.

## 7. Sensitivity / 민감도

The reproducible script gives the following comparator sensitivity when the Schwarzschild comparator is opened only after the blind factorization:

```text
case                         Theta_*    Rcrit/Rs
nominal conditional          0.500      1.000000
zeta = 0.9                   0.405      1.234568
eta_I = 1.1                  0.550      0.909091
nu_kin = 1                   1.000      0.500000
K_g/G = 0.95                 0.500      0.950000
c_info/c = 1.05              0.500      0.907029
```

Thus a Schwarzschild match is not forced by the dimensional form alone. Small changes in downstream factors change the radius ratio in distinct, testable ways.

## 8. Equivalent escape-style route / 동등한 탈출형 경로

If one separately supplies a quadratic balance law

\[
\frac12\mu_Iv^2
\leftrightarrow
\mu_g\frac{K_gM}{R},
\]

then

\[
v^2
=\frac{2}{\eta_I}\frac{K_gM}{R}.
\]

Setting \(v=\zeta c_{\rm info}\) reproduces the same threshold family.

For \(\eta_I=1\) and \(\zeta=1\),

\[
\frac{K_gM}{Rc_{\rm info}^2}=\frac12.
\]

This route explains where the familiar factor \(1/2\) would come from, but it also makes clear that it comes from a quadratic energy/balance specialization, not from \(c_{\rm info}\) alone.

## 9. Provenance ledger / 출처 장부

```text
R0 / PRE-EXISTING DSD:
- explicit downstream-bridge discipline
- c_info as propagation upper bound rather than automatic physical c
- distinction among transport, property, formation, and rank transitions

R1 / GENERAL STRUCTURAL-MATHEMATICAL:
- dimensionless quotient construction
- factorization of independent positive coefficients
- sensitivity analysis

DOWNSTREAM STRUCTURAL-GRAVITY SPECIALIZATION:
- U_X = K_g M / R as structural-load candidate
- support-capacity law E_sup,max = nu_kin mu_I v_sup^2
- eta_I = mu_I / mu_g
- v_sup = zeta c_info

EXTERNAL COMPARATOR ONLY:
- G
- c
- R_S = 2GM/c^2
```

## 10. Reproducibility / 재현성

Repository command:

```bash
python audits/science/2026-09-11_structural_gravity_support_threshold_factorization.py --mode all
```

The current script passes 6/6 internal checks.

No EHT ring or shadow observable is used to choose \(\nu_{\rm kin}\), \(\eta_I\), \(\zeta\), \(K_g/G\), or \(c_{\rm info}/c\).

## 11. Verdict / 판정

```text
VERDICT:
PASS_WITH_BOUNDARY / OPEN_COEFFICIENT

ADVANCE:
- Theta_* is no longer a single opaque free symbol;
- it factorizes into explicit downstream quantities:
  Theta_* = nu_kin eta_I zeta^2;
- the conditional origin of Theta_*=1/2 is identified;
- the coefficient-2 problem is converted into independently auditable bridge questions.

NOT DERIVED:
- nu_kin = 1/2;
- eta_I = 1;
- zeta = 1;
- K_g = G;
- c_info = c;
- R_crit = R_S.
```

## 12. Next target / 다음 대상

Before using another black hole to fit the coefficient, audit the three internal bridge factors independently:

1. whether the structural-support/inertia sector has a justified quadratic normalization \(\nu_{\rm kin}\);
2. whether the relevant support inertial measure and source-coupled measure justify \(\eta_I=1\) or another fixed value;
3. whether local-collapse convergence saturates the propagation bound, i.e. whether \(\zeta=1\), or remains strictly sub-saturating.

Only after those factors are frozen independently should the Schwarzschild comparator be reopened and the same parameter set applied to Sgr A*, low-spin stellar-mass candidates, and M87* without retuning.
