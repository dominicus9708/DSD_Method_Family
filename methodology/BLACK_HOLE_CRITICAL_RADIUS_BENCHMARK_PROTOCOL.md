# Black-Hole Critical-Radius Benchmark Protocol
# 블랙홀 구조적 임계반지름 벤치마크 프로토콜

```text
PROTOCOL_ID: DSD-METHOD-20260911-BH-RADIUS-001
STATUS: ACTIVE_DRAFT
DOMAIN: structural gravity / black-hole benchmark
DATE: 2026-09-11
```

## 1. Purpose / 목적

This protocol tests whether a structural-gravity critical-radius relation can be obtained without inserting the Schwarzschild radius as a premise.

The standard Schwarzschild/Kerr relations are external comparators, not target equations to be fitted.

The first benchmark target is Sgr A* because its mass-to-distance scale is constrained independently by stellar orbits while EHT supplies a separate horizon-scale image observable.

## 2. Provenance layers / 출처 층위

Keep four layers separate.

### O — external observational/inference inputs

Examples:

- stellar-orbit mass and distance;
- EHT bright-ring angular diameter;
- later direct timing or orbital observables.

### B — external bridge

Examples:

- small-angle conversion;
- SI constants;
- GRMHD calibration from image ring to geometric shadow, when explicitly invoked.

### C — standard-GR comparator

Examples:

\[
r_g=\frac{GM}{c^2},
\qquad
R_S=\frac{2GM}{c^2}.
\]

These are never counted as DSD derivations.

### D — DSD candidate layer

The structural-gravity audit currently supports only conditional far-field source linearity and inverse-square shape while leaving the absolute response normalization unresolved.

For the benchmark, write

\[
K_g\equiv\frac{\chi_*}{4\pi}
\]

as a notation for the still-unresolved source-independent normalization in the coarse far-field sector.

If the conditional far-field relation is specialized as

\[
a_X(r)\simeq K_g\frac{M}{r^2},
\]

and if a static radial potential-like descriptor is additionally supplied by

\[
a_X=-\frac{dX}{dr},
\qquad
X(\infty)=0,
\]

then

\[
X(r)=K_g\frac{M}{r}.
\]

This step is conditional on the supplied response bridge; it is not a Formation/Property theorem.

## 3. Candidate structural compactness / 구조적 압축도 후보

Define, as a benchmark candidate only,

\[
\Theta_X(r)
\equiv
\frac{|X(r)|}{c_{\rm info}^2}
=
\frac{K_gM}{c_{\rm info}^2r}.
\]

The use of \(c_{\rm info}\) here is a hypothesis to form a dimensionless criticality descriptor. It does not mean that \(c_{\rm info}\) has already been identified with the physical speed of light, nor that it is an amplitude normalization.

If a later independently justified black-hole critical condition supplies

\[
\Theta_X(R_{\rm crit})=\Theta_*,
\]

then

\[
\boxed{
R_{\rm crit}
=
\frac{K_gM}{\Theta_*c_{\rm info}^2}
}.
\]

Thus the present architecture can conditionally recover linear mass scaling,

\[
R_{\rm crit}\propto M,
\]

but it does not yet determine the coefficient.

## 4. Comparator identity / 비교식

Against the external Schwarzschild comparator

\[
R_S=\frac{2GM}{c^2},
\]

the exact ratio is

\[
\boxed{
\frac{R_{\rm crit}}{R_S}
=
\frac{1}{2\Theta_*}
\frac{K_g}{G}
\left(\frac{c}{c_{\rm info}}\right)^2
}.
\]

This equation is a comparison identity, not a DSD derivation of Schwarzschild.

If future independent work were to yield

\[
K_g=G,
\qquad
c_{\rm info}=c,
\qquad
\Theta_*=\frac12,
\]

then the candidate would close exactly to Schwarzschild. Those three equalities must not be inserted as fit conditions in the derivation stage.

## 5. Anti-circularity rules / 순환검증 방지

1. Do not infer \(K_g\), \(c_{\rm info}\), or \(\Theta_*\) from \(R_S\) and later claim Schwarzschild recovery.
2. Do not identify EHT bright-ring diameter with horizon diameter.
3. Do not use an EHT shadow-calibrated mass to validate a radius relation with the same EHT shadow.
4. Prefer masses from independent stellar/binary dynamics for the first benchmark layer.
5. Freeze one DSD parameter set before applying it to additional black-hole masses.
6. Treat rotation as a later correction sector; first stabilize the low-spin/nonrotating limit.
7. Record all bridge assumptions in the provenance ledger.

## 6. Sgr A* benchmark observables / Sgr A* 기준값

Use the following current frozen inputs for benchmark version 1:

```text
GRAVITY stellar-orbit inference:
M = (4.297 ± 0.012 stat ± 0.040 sys) × 10^6 M_sun
D = 8277 ± 9 stat ± 30 sys pc

EHT image observable:
bright-ring diameter = 51.8 ± 2.3 microarcsec
```

The EHT ring is an image observable, not a horizon radius.

## 7. Reproducible calculator / 재현 계산

Repository command:

```bash
python audits/science/2026-09-11_sgra_black_hole_radius_benchmark.py --mode all
```

Optional machine-readable output:

```bash
python audits/science/2026-09-11_sgra_black_hole_radius_benchmark.py --mode json
```

## 8. Decision states / 판정 상태

Use the following labels.

- `OPEN`: coefficient or bridge not independently determined.
- `CONDITIONAL_SCALING_RECOVERY`: \(R\propto M\) follows only after explicit candidate bridges.
- `CROSS_TARGET_STABLE`: one frozen parameter set survives multiple mass scales without retuning.
- `SCHWARZSCHILD_SCALE_RECOVERED`: the full coefficient closes to \(2GM/c^2\) without using that relation as an input.
- `FAIL_BOUNDARY`: mismatch is traced to different observable/regime rather than a failed same-observable prediction.
- `FAIL`: same observable, same regime, same assumptions, statistically incompatible result.

## 9. Next targets / 다음 대상

After Sgr A*:

1. LMC X-3 and A0620-00 for low-spin stellar-mass scaling;
2. M87* for supermassive-scale extrapolation and mass-systematic stress testing;
3. Cygnus X-1 for a high-spin correction sector;
4. GW150914 remnant for flux/balance and dynamical-horizon bookkeeping rather than static radius validation.

## 10. Current maximum supported claim / 현재 최대 주장

The existing structural-gravity architecture plus an explicit potential/criticality specialization can produce a candidate radius of the form

\[
R_{\rm crit}=\frac{K_gM}{\Theta_*c_{\rm info}^2}.
\]

This conditionally recovers the linear mass scaling required by Schwarzschild, but the absolute normalization, the critical threshold, and the relation between \(c_{\rm info}\) and \(c\) remain open.

Therefore no independent Schwarzschild-radius derivation has yet been achieved.
