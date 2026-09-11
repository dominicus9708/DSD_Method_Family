# Black-Hole Spectral Universality-Class Protocol
# 블랙홀 스펙트럼 보편성 클래스 프로토콜

```text
METHOD_ID: DSD-METHOD-20260911-BH-SPECTRAL-UNIV-001
STATUS: ACTIVE_REFINEMENT
DOMAIN: structural gravity / black-hole critical-radius benchmark
DATE: 2026-09-11
```

## 1. Purpose / 목적

This protocol defines the minimum tests required before one spectral support coefficient may be treated as universal across different black-hole progenitors or mass scales.

The protocol does not assume Schwarzschild or Kerr as the target geometry.

## 2. Canonical normalized pencil / 정본 정규화 pencil

For a conservative/quasi-static support specialization with positive-definite load operator \(L(S)\), define

\[
B(S)=L(S)^{-1/2}H_0(S)L(S)^{-1/2}
\]

and

\[
\Psi_*(S)=\lambda_{\min}B(S).
\]

The current critical-radius candidate is

\[
R_{\rm crit}(S)
=\frac{K_{\rm eff}M}{c_{\rm info}^2\Psi_*(S)}.
\]

Therefore one universal \(R/M\) coefficient requires the normalized factors \(K_{\rm eff}/c_{\rm info}^2\) and \(\Psi_*\) to be universal in the declared regime.

## 3. Equivalence classes / 등가 클래스

### Class U0 — common scaling/congruence

Treat two pencils as threshold-equivalent when

\[
H_0'=sA^TH_0A,
\qquad
L'=sA^TLA,
\qquad s>0,
\]

with \(A\) invertible.

This preserves all generalized eigenvalues.

### Class U1 — coefficient equivalence

Require only

\[
\lambda_{\min}B(S_1)
=
\lambda_{\min}B(S_2).
\]

This is enough for the same spectral threshold coefficient but does not imply the full operators are equivalent.

### Class U2 — full normalized spectral equivalence

A stronger sufficient condition is

\[
B(S)=U(S)^TB_*U(S)
\]

with \(U(S)\) orthogonal.

### Class U3 — dynamical attractor universality

For collapse trajectories \(S(t)\), require

\[
B(S,t)\to B_*
\]

for a declared family of distinct initial states.

This is the strongest current target and remains unproved.

## 4. Approximate universality / 근사 보편성

Use operator norm to quantify approach to a common class:

\[
\epsilon_B(S)=\|B(S)-B_*\|_2.
\]

For symmetric \(B\), Weyl's inequality gives

\[
|\Psi_*(S)-\Psi_*|
\le\epsilon_B(S).
\]

Hence a predeclared tolerance \(\epsilon_B\le\epsilon_{\rm max}\) provides a rigorous coefficient-error bound within this specialization.

## 5. Source-detail firewall / source detail 방화벽

Do not infer universal \(\Psi_*\) from total mass equality alone.

Density profile, bounded-component structure, relation structure, or other typed detail may survive in \(H_0\) or \(L\).

Before claiming universality, test whether the support map factors through the intended coarse source descriptor.

In particular, if two sources satisfy

\[
M_1=M_2
\]

but

\[
B(S_1)\neq B(S_2),
\]

then total mass is not yet a sufficient descriptor for the support threshold.

## 6. Anti-circularity / 순환검증 방지

Do not:

- choose \(B_*\) so that \(\lambda_{\min}B_*=1/2\) because Schwarzschild requires it;
- use a GR endpoint to justify collapse toward that same endpoint;
- erase density/profile dependence by definition and later count universality as a prediction;
- treat no-hair simplicity as proof of an internal support-operator attractor;
- identify an EHT image ring with a horizon boundary.

## 7. Required benchmark sequence / 필수 벤치마크 순서

1. **Synthetic invariance control** — verify common scaling and congruence invariance.
2. **Same-mass structural countercontrol** — vary density/internal detail at fixed coarse mass.
3. **Detail-suppression control** — test whether a declared physical bridge actually reduces normalized operator differences.
4. **Cross-mass freeze** — freeze all dimensionless bridge parameters and apply the same normalized rule across stellar and supermassive scales.
5. **Only then open GR comparators** — compare the frozen result with Schwarzschild/Kerr observables in the same regime.

## 8. Decision labels / 판정표

- `U0_SCALE_EQUIVALENT`: common scaling/basis change only.
- `U1_COEFFICIENT_EQUIVALENT`: same \(\Psi_*\) but full spectral equivalence not shown.
- `U2_SPECTRALLY_EQUIVALENT`: normalized spectra coincide.
- `U3_ATTRACTOR_CANDIDATE`: multiple trajectories approach one \(B_*\) under an explicit dynamical law.
- `PROFILE_DEPENDENCE_REMAINS`: source-detail dependence survives.
- `UNIVERSALITY_NOT_DERIVED`: no law establishes convergence.
- `FAIL`: same declared observable/regime gives incompatible frozen predictions.

## 9. Current status / 현재 상태

The current synthetic audit establishes U0 mathematically and demonstrates that U1 fails when normalized profile detail is deliberately retained.

It also demonstrates that a detail-erasure limit can produce U1/U2 behavior, but generic DSD does not currently provide the strong-field dynamical law required for U3.

```text
CURRENT_STATE:
U0_SCALE_EQUIVALENT / PROFILE_DEPENDENCE_REMAINS / U3_UNRESOLVED
```

## 10. Reproducibility / 재현성

```bash
python audits/science/2026-09-11_structural_gravity_spectral_universality_class_audit.py --mode all
```

Related audit:

```text
audits/science/2026-09-11_structural-gravity-spectral-universality-class-audit.md
```
