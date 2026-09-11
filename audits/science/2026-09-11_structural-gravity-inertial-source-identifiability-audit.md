# Structural-Gravity Inertial/Source Coupling Identifiability Audit
# 구조적 중력 관성량/원천결합량 식별가능성 감사

```text
AUDIT_ID: DSD-AUDIT-20260911-PHYSICS-BH-004
STATUS: PASS_WITH_BOUNDARY / ETA_I_UNDERDETERMINED
DOMAIN: structural gravity / black-hole critical radius
DATE: 2026-09-11
RELATED_METHOD: methodology/BLACK_HOLE_CRITICAL_RADIUS_BENCHMARK_PROTOCOL.md
RELATED_CODE: audits/science/2026-09-11_structural_gravity_inertial_source_identifiability_audit.py
PARENT_AUDIT: audits/science/2026-09-11_structural-gravity-inertial-response-integral-audit.md
```

## 1. Audit question / 감사 질문

Is the ratio

\[
\eta_I=\frac{\mu_I}{\mu_g}
\]

forced to equal one by the current DSD architecture, or is it an independent downstream bridge quantity?

Here \(\mu_I\) is the carrier measure entering the support/inertial response and \(\mu_g\) is the source-coupled carrier used to normalize the structural load.

## 2. Generic DSD boundary / 일반 DSD 경계

The current dynamic framework requires typed properties to affect dynamics only through explicitly supplied constitutive bridges. Realized-axis and property structures are also independent unless an additional law connects them.

The same discipline applies here: equality of two physically interpreted measures cannot be inferred merely because both occur in one downstream model.

Therefore generic DSD does not imply

\[
\mu_I=\mu_g
\]

or

\[
\eta_I=1.
\]

An identification law must be stated separately.

## 3. Updated radius family / 갱신된 반지름 군

From the response-integral audit,

\[
R_{\rm crit}
=
\frac{K_gM}
{\eta_I I_\phi(\zeta)c_{\rm info}^2},
\]

where

\[
I_\phi(\zeta)
:=
\int_0^\zeta\phi(s)\,ds.
\]

The critical radius therefore depends on the combination

\[
\boxed{
\frac{K_g}{\eta_I I_\phi(\zeta)c_{\rm info}^2}
}.
\]

This immediately creates an identifiability issue.

## 4. Common-rescaling degeneracy / 공통 재척도 퇴화

For any \(a>0\), apply

\[
K_g\mapsto aK_g,
\qquad
\eta_I\mapsto a\eta_I.
\]

Then

\[
\frac{aK_g}{a\eta_I I_\phi c_{\rm info}^2}
=
\frac{K_g}{\eta_I I_\phi c_{\rm info}^2}.
\]

Hence the candidate black-hole radius is invariant under this common rescaling.

Therefore a radius measurement alone cannot distinguish \(K_g\) from \(\eta_I\).

## 5. Reproducible calculation / 재현 계산

Run

```bash
python audits/science/2026-09-11_structural_gravity_inertial_source_identifiability_audit.py --mode all
```

Using the globally linear response comparator \(I_\phi(1)=1/2\), the script gives:

```text
Common rescaling degeneracy K_g -> a K_g, eta_I -> a eta_I:
a     scaled factor     relative to baseline
0.25  2.00000000000     1.00000000000
0.50  2.00000000000     1.00000000000
1.00  2.00000000000     1.00000000000
2.00  2.00000000000     1.00000000000
4.00  2.00000000000     1.00000000000
10.0  2.00000000000     1.00000000000
```

All 7/7 checks pass.

The calculation is an identifiability audit only. It does not calibrate \(K_g\), \(\eta_I\), or a black-hole radius.

## 6. Consequence after an independent K_g calibration / K_g 독립 고정 이후의 결과

If \(K_g\) is independently fixed outside the black-hole radius sector, changing \(\eta_I\) does change the predicted critical radius.

For fixed \(K_g\), fixed \(c_{\rm info}\), and the linear response integral:

```text
eta_I   radius factor relative to eta_I=1
0.80    1.250000
0.90    1.111111
1.00    1.000000
1.10    0.909091
1.20    0.833333
```

Thus \(\eta_I\) becomes empirically relevant only after the other coupled factors are frozen independently.

## 7. What would justify eta_I = 1? / eta_I=1의 정당화 조건

The equality

\[
\eta_I=1
\]

would require an explicit downstream identification such as

\[
\boxed{\mu_I\equiv\mu_g}
\]

for the same carrier and regime.

This would play a role analogous to identifying inertial and source-coupled measures, but the audit does not label it as a generic equivalence principle or derive it from standard GR.

It must be separately justified by the structural-gravity specialization, by an independent empirical calibration, or by a stronger theorem not presently in the DSD core.

## 8. Anti-fitting rule / 피팅 방지

Do not determine \(\eta_I\) from the Schwarzschild radius and then use the same radius as evidence that DSD predicted Schwarzschild.

A legitimate route is:

1. determine or bound \(K_g\) outside the black-hole radius sector;
2. determine the response law \(\phi\) outside the black-hole radius sector if possible;
3. determine whether \(\mu_I\) and \(\mu_g\) are identical or related by an independent bridge;
4. freeze \(\eta_I\);
5. only then reopen the black-hole radius comparator.

## 9. Verdict / 판정

```text
VERDICT:
PASS_WITH_BOUNDARY / ETA_I_UNDERDETERMINED

CONFIRMED:
- the candidate radius depends on K_g/eta_I rather than on K_g and eta_I separately;
- common rescaling of K_g and eta_I is an exact degeneracy of this candidate family;
- black-hole radius data alone cannot establish eta_I=1;
- eta_I=1 requires a separate identification bridge.

NOT DERIVED:
- mu_I = mu_g;
- eta_I = 1;
- K_g = G;
- c_info = c;
- zeta = 1;
- R_crit = R_S.
```

## 10. Next target / 다음 대상

The next bridge audit is the saturation factor \(\zeta\):

\[
v_{\rm sup}=\zeta c_{\rm info}.
\]

The task is to determine whether local-collapse convergence is forced to saturate the information-propagation bound, can remain strictly sub-saturating, or requires a separate characteristic speed altogether.
