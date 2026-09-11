# Structural Gravity — eta_I Identifiability Audit
# 구조적 중력 — eta_I 식별가능성 감사

```text
AUDIT_ID: DSD-AUDIT-20260911-BH-RADIUS-ETA-I-001
STATUS: COMPLETED_WITH_BOUNDARY
DOMAIN: structural gravity / black-hole critical-radius benchmark
DATE: 2026-09-11
RELATED_PROTOCOL: methodology/BLACK_HOLE_CRITICAL_RADIUS_BENCHMARK_PROTOCOL.md
RELATED_CODE: audits/science/2026-09-11_structural_gravity_eta_i_identifiability_audit.py
```

## 1. Audit question / 감사 질문

The support-threshold factorization introduced

\[
\eta_I\equiv\frac{\mu_I}{\mu_g},
\]

where \(\mu_I\) is the inertial/support carrier used by the downstream support-capacity model and \(\mu_g\) is the source-coupled carrier used by the structural-gravity response bridge.

The audit asks:

1. Does generic DSD imply \(\eta_I=1\)?
2. If weak-field universality makes \(\eta_I\) common to all test bodies, is its absolute value separately identifiable from \(K_g\)?
3. Does black-hole critical-radius benchmarking add an independent constraint on \(\eta_I\)?
4. What remains open in the strong-field regime?

## 2. DSD-source boundary / DSD 소스 경계

The Property Axiom System keeps property kinds, typed profiles, applicability, prerequisites, and assignments distinct. Physical constitutive or geometric specialization is downstream data rather than an automatic consequence of a property label.

The Structural Reorganization Dynamics likewise treats evolution coefficients and typed operators as supplied constitutive data. The finite propagation quantity \(c_{\rm info}\) is a propagation bound and does not identify inertial, source-coupled, or support-capacity coefficients.

Therefore generic DSD does not contain a theorem

\[
\boxed{\mu_I=\mu_g}
\]

and hence does not derive

\[
\boxed{\eta_I=1}.
\]

Any equality or universal proportionality must enter through an explicit downstream physical bridge.

## 3. Minimal response bridge / 최소 응답 bridge

For the identifiability test, introduce only the bookkeeping relations

\[
F_X=\mu_g a_X,
\]

\[
\mu_I a=F_X.
\]

Then

\[
a=\frac{\mu_g}{\mu_I}a_X
=\frac{a_X}{\eta_I}.
\]

If the structural-gravity coarse response is

\[
a_X\simeq K_g\frac{M}{r^2},
\]

the observable acceleration normalization becomes

\[
\boxed{
a\simeq\frac{K_g}{\eta_I}\frac{M}{r^2}
}.
\]

Thus the weak-field response identifies the ratio

\[
\boxed{K_{\rm eff}\equiv\frac{K_g}{\eta_I}},
\]

not \(K_g\) and \(\eta_I\) separately.

## 4. Universal-ratio degeneracy / 보편 비율 퇴화

Suppose a weak-field universality bridge gives

\[
\eta_I(S)=\eta_0
\]

for every admitted test-body state \(S\) in that regime.

Then

\[
K_{\rm eff}=\frac{K_g}{\eta_0}
\]

absorbs the common factor.

For example, the three pairs

\[
(\eta_0,K_g)=(0.5,0.5),(1,1),(2,2)
\]

have the same \(K_g/\eta_0=1\). The calculator confirms that they give the same weak-field normalization and the same normalized critical-radius prediction when all other bridge factors are held fixed.

Therefore

\[
\boxed{
\text{universal }\eta_0\text{ is not separately identifiable from }K_g
}
\]

within the present response architecture.

Choosing \(\eta_0=1\) after universality is imposed is therefore a normalization convention, not an independent DSD derivation.

## 5. Critical-radius consequence / 임계반지름 결과

After the constitutive-function refinement, the support threshold is written

\[
\Theta_*=\eta_I\Phi(\zeta),
\qquad
\zeta=\frac{v_{\rm sup}}{c_{\rm info}}.
\]

The candidate radius is

\[
R_{\rm crit}
=
\frac{K_gM}{\eta_I\Phi(\zeta)c_{\rm info}^2}.
\]

For universal \(\eta_I=\eta_0\), define

\[
K_{\rm eff}=\frac{K_g}{\eta_0}.
\]

Then

\[
\boxed{
R_{\rm crit}
=
\frac{K_{\rm eff}M}{\Phi(\zeta)c_{\rm info}^2}
}.
\]

Hence the present black-hole radius benchmark also does not separately determine \(K_g\) and a universal \(\eta_0\).

This removes one spurious independent coefficient from the universal sector, but it does not determine the remaining normalization.

## 6. Non-universal eta_I is physical / 비보편 eta_I는 물리적으로 구별됨

If

\[
\eta_I=\eta_I(S)
\]

depends on composition, internal state, or physical regime, the absorption into one universal \(K_{\rm eff}\) is impossible.

For two test states,

\[
a_i\propto\frac{1}{\eta_I^{(i)}}.
\]

The differential free-fall signal can be summarized by an Eötvös-type quantity

\[
\eta_{12}^{(E)}
=
2\frac{|a_1-a_2|}{|a_1+a_2|}.
\]

The calculator verifies that a common \(\eta_I\) gives zero differential signal, while any state-dependent difference gives a nonzero signal.

Therefore weak-field universality experiments constrain **variation of the ratio across bodies**, not a separately measurable absolute normalization of \(\mu_I/\mu_g\) once a common factor is absorbed into the coupling convention.

## 7. External empirical comparator / 외부 경험 비교

The MICROSCOPE final Ti/Pt result reports

\[
\eta_{\rm Eotvos}(\mathrm{Ti},\mathrm{Pt})
=
[-1.5\pm2.3(\mathrm{stat})\pm1.5(\mathrm{syst})]\times10^{-15},
\]

consistent with no weak-equivalence-principle violation in that test.

This is used only as an **external weak-field comparator**. It is not imported as a DSD axiom and does not prove that a DSD strong-field support carrier must remain state-independent near a black-hole critical regime.

A recent Living Reviews discussion likewise formulates Newtonian free fall with separate inertial and gravitational masses and notes that universality requires the ratios to be equal across bodies; a common ratio permits the two masses to be chosen equal by normalization.

External sources:

- MICROSCOPE final result: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.129.121102
- Uzan, Living Reviews in Relativity (2025): https://link.springer.com/article/10.1007/s41114-025-00059-y

## 8. Strong-field firewall / 강한장 방화벽

The following implication is not allowed:

\[
\text{weak-field UFF}
\Rightarrow
\eta_I(S)=\text{constant in every strong-field state}.
\]

A strong-field DSD specialization may retain the universal bridge as a hypothesis, or it may introduce a state-dependent \(\eta_I(S)\). The latter would be an additional physical sector requiring independent observational constraints.

Therefore the black-hole program must distinguish:

### Universal branch

\[
\eta_I=\eta_0,
\qquad
K_{\rm eff}=K_g/\eta_0.
\]

Use the reduced radius candidate

\[
R_{\rm crit}
=
\frac{K_{\rm eff}M}{\Phi(\zeta)c_{\rm info}^2}.
\]

### Non-universal branch

\[
\eta_I=\eta_I(S),
\]

which cannot be absorbed globally and must be retained as an explicit state-dependent bridge factor.

## 9. Numerical audit / 수치 감사

The reproducibility script checks:

1. common-ratio degeneracy;
2. the same degeneracy in the critical-radius expression;
3. universal \(\eta_I\) implies zero differential free-fall signal;
4. non-universal \(\eta_I\) produces a nonzero signal;
5. generic DSD does not derive \(\eta_I=1\);
6. a universal ratio can be absorbed into \(K_{\rm eff}\);
7. no Schwarzschild/EHT datum is used to set \(\eta_I\);
8. strong-field extension remains open.

Result:

```text
8/8 PASS
STATUS: PASS_WITH_BOUNDARY / UNIVERSAL_RATIO_DEGENERACY
```

Repository command:

```bash
python audits/science/2026-09-11_structural_gravity_eta_i_identifiability_audit.py --mode all
```

## 10. Verdict / 판정

```text
VERDICT:
PASS_WITH_BOUNDARY / UNIVERSAL_RATIO_DEGENERACY

MAXIMUM_SUPPORTED_CLAIM:
Generic DSD does not derive mu_I = mu_g or eta_I = 1. Under an explicit weak-field universality bridge, eta_I may be common across admitted test bodies, but its common absolute value is degenerate with the structural-gravity normalization K_g. The present weak-field response and black-hole critical-radius candidate depend on K_eff = K_g/eta_I. Setting eta_I = 1 is therefore a normalization convention only after universality has been supplied. State-dependent eta_I remains a separate physical possibility and is not eliminated by weak-field universality tests.

UNSUPPORTED:
- eta_I = 1 as a generic DSD theorem
- use of MICROSCOPE to prove strong-field universality
- use of Schwarzschild or EHT data to fit eta_I
- separate recovery of K_g and a universal eta_I from the current benchmark
```

## 11. Next audit / 다음 감사

Audit the saturation factor

\[
\boxed{\zeta=\frac{v_{\rm sup}}{c_{\rm info}}}
\]

and determine whether

\[
\zeta=1
\]

is derivable, merely a sharp-bound/saturation assumption, or must remain state-dependent.

Because \(c_{\rm info}\) is only an infimal propagation upper bound in the generic dynamic layer, the default expectation is that actual support-failure dynamics need not saturate it. This must be checked without importing the Schwarzschild coefficient.
