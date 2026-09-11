# Sgr A* Structural-Gravity Critical-Radius Benchmark Audit
# Sgr A* 구조적 중력 임계반지름 벤치마크 감사

```text
AUDIT_ID: DSD-AUDIT-20260911-PHYSICS-BH-001
STATUS: OPEN / CONDITIONAL_SCALING_RECOVERY
DOMAIN: structural gravity / black-hole benchmark
DATE: 2026-09-11
TARGET: Sagittarius A*
RELATED_METHOD: methodology/BLACK_HOLE_CRITICAL_RADIUS_BENCHMARK_PROTOCOL.md
RELATED_CODE: audits/science/2026-09-11_sgra_black_hole_radius_benchmark.py
```

## 1. Audit question / 감사 질문

Can the current structural-gravity architecture produce a black-hole critical-radius candidate whose mass scaling and numerical scale can later be compared with the Schwarzschild radius, without putting the Schwarzschild radius into the DSD derivation?

The first target is Sgr A* because stellar-orbit dynamics constrain the central mass and distance independently of the EHT bright-ring size.

## 2. DSD basis carried forward / 계승되는 DSD 근거

The current structural-gravity audit already separates:

- internal mass structure;
- exterior coarse source;
- structural detail sectors;
- distortion descriptor \(X\);
- distortion gradient / acceleration-like sector;
- finite propagation upper bound \(c_{\rm info}\);
- unresolved source-independent response normalization.

It conditionally allows a coarse far-field form

\[
a_X(r;S)
=
\frac{\chi_*}{4\pi}
\frac{M_{\rm coarse}}{r^2}
[1+\delta F(S,r)],
\]

with \(\delta F\to0\) only as a conditional far-field target.

The normalization \(\chi_*\) is explicitly unresolved.

For benchmark notation define

\[
K_g\equiv\frac{\chi_*}{4\pi}.
\]

This is a notation change inside the benchmark, not a numerical determination of \(K_g\).

## 3. Candidate criticality chain / 임계성 후보 사슬

In the coarse static spherical limit, add the explicit bridge

\[
a_X=-\frac{dX}{dr},
\qquad X(\infty)=0.
\]

Then

\[
X(r)=K_g\frac{M}{r}.
\]

Define a candidate dimensionless structural compactness

\[
\Theta_X(r)
=
\frac{|X(r)|}{c_{\rm info}^2}
=
\frac{K_gM}{c_{\rm info}^2r}.
\]

If an independently justified critical condition later supplies

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

Therefore

\[
\boxed{R_{\rm crit}\propto M}
\]

is recoverable conditionally.

However, \(K_g\), \(\Theta_*\), and \(c_{\rm info}/c\) remain open.

## 4. External observational ledger / 외부 관측 장부

### O1 — stellar-orbit mass and distance

GRAVITY Collaboration (A&A 657, L12, 2022) reports

\[
M_\bullet
=(4.297\pm0.012)\times10^6M_\odot
\]

and

\[
R_0=8277\pm9\,\mathrm{pc}
\]

as statistical errors, with quoted systematics of approximately

\[
\Delta M_{\rm sys}\simeq4.0\times10^4M_\odot,
\qquad
\Delta R_{0,\rm sys}\simeq30\,\mathrm{pc}.
\]

Source:
https://www.aanda.org/articles/aa/full_html/2022/01/aa42465-21/aa42465-21.html

This is an external GR stellar-orbit inference, not a DSD output.

### O2 — EHT bright-ring diameter

EHT Collaboration (ApJL 930, L12/L15, 2022) reports a bright-ring angular diameter

\[
d_{\rm ring}=51.8\pm2.3\,\mu\mathrm{as}.
\]

Sources:
https://eventhorizontelescope.org/publications/first-sagittarius-event-horizon-telescope-results-i-shadow-supermassive-black-hole
https://eventhorizontelescope.org/publications/first-sagittarius-event-horizon-telescope-results-iv-variability-morphology-and

The observed bright ring is not identified with the horizon diameter.

## 5. Reproducible calculation / 재현 계산

Run

```bash
python audits/science/2026-09-11_sgra_black_hole_radius_benchmark.py --mode all
```

with the frozen inputs above.

The script returns

```text
r_g = 6.345250e+06 km
R_S = 1.269050e+07 km
theta_g(independent orbit M/D) = 5.124486 uas ± 0.015357 stat ± 0.051191 sys
Schwarzschild horizon angular diameter = 20.497946 uas
EHT bright-ring physical diameter = 6.413988e+07 km
EHT bright-ring diameter / r_g = 10.108330 ± 0.461041
EHT bright-ring diameter / Schwarzschild horizon diameter = 2.527083
```

All self-tests pass.

## 6. Immediate observational consequence / 즉시 관측 결과

Using only the independent orbital \(M/D\) scale plus the directly measured EHT ring angle,

\[
\boxed{
\frac{d_{\rm ring}}{r_g}
=10.108\pm0.461
}
\]

for the frozen input set.

This does not require identifying the EHT ring with the event horizon.

The same calculation gives

\[
\frac{d_{\rm ring}}
{d_{\rm horizon}^{\rm Schw}}
\simeq2.527.
\]

Therefore

\[
\boxed{
\text{EHT bright-ring diameter}
\neq
\text{Schwarzschild horizon diameter}
}
\]

is numerically explicit in this benchmark.

## 7. Standard comparator / 표준 비교식

The external Schwarzschild comparator is

\[
R_S=\frac{2GM}{c^2}.
\]

For the GRAVITY mass input,

\[
R_S\simeq1.26905\times10^7\,\mathrm{km}.
\]

This value is stored only as a comparator.

The EHT metric-test paper reports that the observed Sgr A* image size is within approximately 10% of Kerr predictions after calibrating the observed image size to the geometrically defined shadow using Kerr and non-Kerr simulation libraries.

Source:
https://eventhorizontelescope.org/publications/first-sagittarius-event-horizon-telescope-results-vi-testing-black-hole-metric

That calibration is not used as a DSD derivation input here.

## 8. DSD-to-Schwarzschild closure identity / 폐쇄 비교식

The candidate DSD relation and standard comparator give

\[
\boxed{
\frac{R_{\rm crit}}{R_S}
=
\frac{1}{2\Theta_*}
\frac{K_g}{G}
\left(\frac{c}{c_{\rm info}}\right)^2
}.
\]

Hence exact closure would require the product condition

\[
\boxed{
\frac{K_g}{G}
\left(\frac{c}{c_{\rm info}}\right)^2
=2\Theta_*
}.
\]

A special case is

\[
K_g=G,
\qquad
c_{\rm info}=c,
\qquad
\Theta_*=\frac12,
\]

but none of those equalities is currently derived by DSD.

Therefore this benchmark does not recover the Schwarzschild coefficient yet.

## 9. Anti-fitting boundary / 피팅 경계

The following procedures are prohibited for a future positive claim:

- choose \(K_g\) from \(G\) solely to fit Sgr A*;
- set \(c_{\rm info}=c\) solely because Schwarzschild requires it;
- set \(\Theta_*=1/2\) solely to recover the factor 2;
- use EHT ring diameter as the horizon diameter;
- derive mass from the EHT shadow and reuse the same shadow as an independent radius confirmation;
- retune any of the above parameters separately for stellar-mass and supermassive targets.

## 10. Current verdict / 현재 판정

```text
VERDICT:
OPEN / CONDITIONAL_SCALING_RECOVERY

CONFIRMED:
- current structural-gravity architecture can support a conditional mass-linear critical-radius form;
- Sgr A* provides a clean independent M/D vs horizon-scale image benchmark;
- EHT bright ring and horizon diameter must remain separate readouts;
- the frozen Sgr A* numerical benchmark is reproducible.

NOT YET CONFIRMED:
- K_g = G;
- c_info = c;
- Theta_* = 1/2;
- R_crit = R_S;
- any independent DSD derivation of the Schwarzschild coefficient 2.
```

## 11. Next calculation / 다음 계산

1. Derive or reject a DSD-internal candidate for \(\Theta_*\) from structural-support failure / local-collapse convergence without importing black-hole compactness.
2. Audit whether \(K_g\) can be fixed outside the black-hole sector.
3. Audit whether \(c_{\rm info}\) can be physically identified with \(c\) independently of the black-hole radius problem.
4. Freeze the resulting parameter set.
5. Apply without retuning to LMC X-3 / A0620-00 and then to M87*.
6. Only after cross-target stability, compare the recovered radius scale with Schwarzschild.
