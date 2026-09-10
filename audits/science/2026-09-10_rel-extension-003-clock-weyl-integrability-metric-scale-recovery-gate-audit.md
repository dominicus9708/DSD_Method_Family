# REL Extension 003 — Clock / Weyl Integrability / Metric-Scale Recovery Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Extension Track**

## 1. Purpose

REL Extension 002 separated conformal light-cone information, projective free-fall information, Weyl compatibility, metric scale, and Einstein dynamics.

This gate asks the next chronometric question:

> What additional assumptions are required to pass from a Weyl-compatible geometry to a pseudo-Riemannian representative usable by physical clock readings, without assuming a clock standard first and then back-counting that standard as an independent derivation of metric scale?

The audit therefore separates:

```text
conformal class
Weyl scale connection
closed vs exact Weyl one-form
local vs global integrability
standard-clock rule
proper-time parametrization
second-clock-effect criterion
constant scale / clock-zero ambiguity
physical clock calibration
Einstein dynamics
```

---

## 2. DSD baseline

The current DSD dynamics paper treats numerical time as an external evolution parameter when metric time is required. A purely ordered history can be represented without numerical metric time, while a speed interpretation requires metric time. This is a typing/scope rule, not a theorem that the supplied time is relativistic proper time.

Likewise, the static and dynamic DSD layers require explicit downstream bridges for physical constitutive interpretation. Therefore no clock law, Lorentzian proper-time rule, Weyl one-form, or Einstein equation is silently identified with generic DSD structure.

---

## 3. Standard theorem lock: Weyl structure and gauge

Use the standard Weyl comparator in the convention adopted by Avalos, Dahia, and Romero:

\[
\nabla g = g\otimes\omega,
\]

with gauge transformation

\[
\bar g=e^{-f}g,
\qquad
\bar\omega=\omega-df.
\]

The affine connection is unchanged by this representative change.

If

\[
\omega=d\phi,
\]

then choosing \(f=\phi\) yields

\[
\bar\omega=0,
\]

so an exact Weyl one-form permits reduction to a pseudo-Riemannian representative on that domain.

This is an external geometrical comparator, not a generic DSD theorem.

---

## 4. Standard-clock gate

In the EPS/Perlick/Avalos route, a timelike parametrized curve is a standard clock when its covariant acceleration is orthogonal to its tangent in the relevant Weyl geometry. Locally, an appropriate reparametrization exists under the stated assumptions.

The resulting standard-clock parameter is not an absolute numerical clock unit. The admissible parameter is unique only up to

\[
\widetilde\tau=a\tau+b,
\qquad a>0,
\]

where \(a\) fixes clock scale and \(b\) fixes the zero.

A finite regression witness uses

\[
\tau(t)=3t+5,
\qquad
\widetilde\tau=7\tau-11.
\]

Elapsed times obey

\[
\Delta\widetilde\tau=7\,\Delta\tau.
\]

Hence

\[
\boxed{\text{standard-clock parametrization}\not\Rightarrow\text{absolute numerical clock unit}.}
\]

---

## 5. Exact path-independence witness

Take

\[
\omega=d\phi,
\qquad
\phi(x,y)=x+2y,
\]

between \(A=(0,0)\) and \(B=(1,1)\).

For the two piecewise paths

```text
HV: horizontal, then vertical
VH: vertical, then horizontal
```

both line integrals are

\[
\int_{HV}\omega=3,
\qquad
\int_{VH}\omega=3.
\]

Therefore the corresponding closed-loop integral vanishes.

In the Perlick/Avalos second-clock comparison factor,

\[
\exp\!\left[\frac12\left(\int_{\Gamma_1}\omega-\int_{\Gamma_2}\omega\right)\right],
\]

these two histories give unity.

This is the finite control for an exact, path-independent case.

---

## 6. Nonclosed second-clock-effect witness

Take instead

\[
\omega=x\,dy,
\qquad
 d\omega=dx\wedge dy\neq0.
\]

Between the same endpoints,

\[
\int_{HV}\omega=1,
\qquad
\int_{VH}\omega=0.
\]

Thus the same-endpoint history difference is nonzero and the unit-square loop satisfies

\[
\oint\omega=1.
\]

Under the adopted EPS/Perlick/Avalos clock comparison law, the rate factor becomes

\[
\exp(1/2)\neq1.
\]

Hence this comparator gives a history-dependent clock-rate witness.

The scope statement is essential:

\[
\boxed{d\omega\neq0\Rightarrow\text{SCE witness}}
\]

is being used only inside this specific proper-time/transport convention. It is not promoted to an assumption-free theorem about every possible non-metric transport prescription.

---

## 7. Closed versus globally exact topology gate

Local closedness does not imply a single global Weyl potential on an arbitrary domain.

On

\[
\mathbb R^2\setminus\{0\},
\]

use

\[
\omega=
-\frac{y}{x^2+y^2}\,dx
+
\frac{x}{x^2+y^2}\,dy.
\]

Away from the origin,

\[
d\omega=0.
\]

But on the unit circle,

\[
\oint\omega=2\pi\neq0.
\]

Therefore the form is closed but not globally exact on the punctured plane.

So the audit keeps

\[
\boxed{\text{local closedness}\neq\text{global exactness}}
\]

and treats simple connectedness/cohomological information as an additional global premise.

---

## 8. No-second-clock-effect reconstruction boundary

In the Avalos–Dahia–Romero reconstruction, if the adopted standard-clock comparison has no second clock effect for arbitrary same-endpoint timelike histories, the relevant Weyl integrals are path independent. Under their assumptions this yields local closedness of \(\omega\); on a simply connected domain it gives global exactness and therefore an integrable Weyl geometry.

The provenance is therefore conditional:

```text
Weyl geometry
+ standard-clock definition
+ adopted clock transport/proper-time law
+ empirical no-SCE selector
+ global topology assumptions
-> integrable Weyl / pseudo-Riemannian representative
```

The clock premise is not erased after the reconstruction succeeds.

---

## 9. Residual global metric-scale gate

Even when

\[
\omega=d\phi
\]

and the gauge choice \(f=\phi\) sets \(\bar\omega=0\), the potential is only fixed by its derivative up to

\[
\phi\mapsto\phi+C.
\]

The corresponding zero-Weyl metric representatives differ by a constant factor:

\[
\bar g_{\phi+C}=e^{-C}\bar g_{\phi}.
\]

For

\[
C=\ln4,
\]

the factor is \(1/4\).

Thus integrability can eliminate the local Weyl scale connection while leaving a global numerical scale convention to clock calibration or another physical standard.

Hence

\[
\boxed{
\text{integrable Weyl reduction}
\not\Rightarrow
\text{absolute physical clock calibration}.
}
\]

---

## 10. Comparator-scope firewall

The EPS/Perlick/Avalos chronometric route is retained as a valid conditional comparator under its explicit assumptions.

The audit also records that alternative Weyl-covariant or nonmetric transport prescriptions have been proposed in which the second-clock conclusion can differ. Therefore the implication from nonintegrability to an observable second clock effect is not universalized beyond the clock/transport convention used here.

This avoids turning one physically motivated chronometric rule into a generic theorem of Weyl geometry or DSD.

---

## 11. DSD provenance ledger

### R0 — PRE_EXISTING_DSD

```text
typed applicability/status discipline
explicit downstream bridge discipline
state / relation / transition separation
ordered history versus metric-time separation
metric time required before interpreting a quantity as speed
```

### R1 — GENERAL_MATHEMATICAL_STRUCTURAL

```text
closed versus exact differential form
local versus global integrability
topological obstruction
path independence
affine reparametrization ambiguity
```

### R2 — RELATIVITY / CHRONOMETRY SPECIALIZATION

```text
smooth spacetime domain
Lorentzian/Weyl geometric specialization
Weyl one-form and gauge rule
timelike curve family
Perlick/EPS standard-clock definition
second-clock comparison rule
```

### R3 — STANDARD THEOREM CONSEQUENCE

```text
local standard-clock reparametrization under stated hypotheses
exact Weyl one-form -> gauge with omega=0
no-SCE -> local path independence / closedness in the cited framework
closed + simply connected -> global exactness
integrable Weyl -> pseudo-Riemannian representative
```

### R4 — REMAINS EXTERNAL / NOT INDEPENDENTLY DERIVED

```text
empirical absence or experimental bound on second clock effect
physical clock construction and calibration
absolute numerical unit of proper time
actual global spacetime topology
physical spacetime dimension/signature/time orientation
Einstein field equation and coupling constants
actual matter/initial/boundary data
```

Only R0/R1 count as target-independent DSD evidence.

---

## 12. Deterministic regression result

Run from repository root:

```bash
python audits/science/2026-09-10_rel_extension_003_clock_weyl_integrability_metric_scale_recovery_gate.py --mode all
```

Observed result:

```text
EXACT_PATH_INDEPENDENCE: PASS
NONCLOSED_SECOND_CLOCK: PASS
CLOSED_NOT_GLOBAL_EXACT: PASS
GAUGE_REDUCTION_RESIDUAL_SCALE: PASS
STANDARD_CLOCK_AFFINE_AMBIGUITY: PASS
DSD_PROVENANCE: PASS
COMPARATOR_SCOPE: PASS
TOTAL: 57/57 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

These tests are finite algebraic/topological/provenance witnesses. They do not constitute an empirical test of relativistic chronometry and do not prove the full external differential-geometric results from first principles.

---

## 13. Verdict

**PASS_WITH_BOUNDARY**.

The chronometric reconstruction route remains viable in conditional form:

\[
\text{Weyl structure}
+
\text{standard-clock rule}
+
\text{no-SCE selector}
+
\text{global topology premise}
\leadsto
\text{integrable Weyl / pseudo-Riemannian representative}.
\]

But the following identifications are rejected:

\[
\boxed{
\text{pseudo-Riemannian representative}
\neq
\text{absolute physical clock calibration}
}
\]

and

\[
\boxed{
\text{DSD metric time}
\neq
\text{relativistic proper time}
}
\]

unless an explicit physical bridge is supplied.

No contradiction requiring revision of the present DSD core papers was found.

---

## 14. External references

- J. Ehlers, F. A. E. Pirani, A. Schild, *The Geometry of Free Fall and Light Propagation* (1972; republication, General Relativity and Gravitation 44, 1587–1609, 2012), DOI: 10.1007/s10714-012-1353-4.
- V. Perlick, *Characterization of standard clocks by means of light rays and freely falling particles*, General Relativity and Gravitation 19, 1059–1073 (1987), DOI: 10.1007/BF00759142.
- R. Avalos, F. Dahia, C. Romero, *A note on the problem of proper time in Weyl space-time*, Foundations of Physics 48, 253–270 (2018), arXiv:1611.10198, DOI: 10.1007/s10701-017-0134-z.
- C. Pala, O. Sert, M. Adak, *Weyl covariance, second clock effect and proper time in theories of symmetric teleparallel gravity*, European Physical Journal C 83 (2023), DOI: 10.1140/epjc/s10052-023-11171-0.

These are external comparators and are not counted as DSD-derived evidence.

---

## 15. Next target

**REL Extension 004 — Clock Hypothesis / Accelerated Proper-Time / Operational Calibration Gate**.

The next gate will separate:

```text
metric proper time
ideal-clock hypothesis
worldline acceleration
clock mechanism / finite-size effects
local rate law
initial calibration
coordinate time
observer readout
DSD external evolution parameter
Einstein dynamics
```

The central circularity test is whether the physical validity of metric proper time is being inferred merely by defining an ideal clock to measure it.
