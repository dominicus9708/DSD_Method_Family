# REL Extension 007 — Ricci / Weyl Decomposition / Matter-Source / Vacuum-Curvature Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Extension Track**

## 1. Purpose

REL Extension 006 established that tidal relative acceleration is a local curvature probe but one observer's tidal matrix does not determine the full local Riemann tensor.

This gate asks what follows after full local curvature data are available. It separates:

```text
full Riemann curvature
Ricci tensor
Ricci scalar
Weyl tensor
Ricci-flat condition
Einstein vacuum with/without Lambda
stress-energy tensor
Einstein field equation
material source interpretation
```

The two principal firewalls are

\[
R_{\mu\nu}=0
\not\Rightarrow
R_{\alpha\beta\gamma\delta}=0,
\]

and

\[
\text{curvature decomposition}
\neq
\text{independent derivation of a material source or Einstein dynamics}.
\]

---

## 2. DSD baseline

The current DSD Structural Reorganization Dynamics paper states that the coefficients/operators of a dynamic realization are outputs of a constitutive dynamic bridge or separately supplied dynamic data; its model family is not a universal DSD physical law. The finite-propagation layer likewise requires a supplied metric localization carrier and metric time.

Accordingly, this gate does not identify

```text
DSD localization metric = physical spacetime metric
DSD property aggregation = Ricci contraction
DSD structural residual = Weyl curvature
DSD dynamic operator = Einstein tensor / Einstein dynamics
DSD c_info = relativistic c
```

without an explicit bridge.

---

## 3. Standard decomposition lock

In four spacetime dimensions, use the standard Weyl/Ricci decomposition

\[
R_{abcd}
=
C_{abcd}
+\frac12\left(
 g_{ac}R_{db}-g_{ad}R_{cb}-g_{bc}R_{da}+g_{bd}R_{ca}
\right)
-\frac{R}{6}
\left(g_{ac}g_{db}-g_{ad}g_{cb}\right).
\]

The Weyl tensor is tracefree. The standard component count in four dimensions is

```text
algebraic Riemann tensor : 20
symmetric Ricci tensor   : 10
Weyl tensor              : 10
```

The regression does not merely enter these dimensions as literals: it reconstructs the exact Ricci contraction map on the 20-dimensional algebraic-curvature basis inherited from REL Extension 006.

---

## 4. Exact Ricci-map rank

Let

\[
\mathcal R_{20}
\longrightarrow
\operatorname{Sym}^2(T^*)
\]

be the contraction

\[
R_{abcd}\mapsto R_{bd}=g^{ac}R_{abcd}.
\]

Using exact rational arithmetic, the map has

\[
\operatorname{rank}=10,
\qquad
\dim\ker=10.
\]

Hence there is a ten-dimensional family of nonzero algebraic curvatures invisible to Ricci contraction.

The Weyl projection itself has rank 10, and every projected basis tensor is verified to be Ricci-tracefree. Since its image lies in the Ricci kernel and both have dimension 10, the regression identifies the algebraic Ricci kernel with the Weyl sector in this four-dimensional setup.

Thus

\[
\boxed{
\text{Ricci data do not determine the full Riemann tensor}.
}
\]

---

## 5. Ricci-flat but curved countermodel

A particularly simple exact kernel element is generated in the bivector representation by a nonzero `M[(01),(23)]` entry together with the Bianchi-related `M[(03),(12)]` entry.

For this tensor,

\[
R_{ab}=0,
\qquad
R=0,
\qquad
C_{abcd}=R_{abcd},
\]

but

\[
R_{abcd}\neq0.
\]

Therefore, independently of any particular spacetime solution,

\[
\boxed{
R_{ab}=0\not\Rightarrow R_{abcd}=0
}
\]

already follows as a finite algebraic countermodel.

---

## 6. Schwarzschild exterior as the standard physical comparator

The Schwarzschild exterior supplies the familiar physical GR realization of the same logical separation. Standard calculations give

\[
R_{\mu\nu}=0
\]

outside the source, while the Kretschmann scalar in geometric units is

\[
K
=
R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta}
=
\frac{48M^2}{r^6}.
\]

For every finite audit sample with \(M\neq0\) and \(r>0\), this invariant is positive, so the exterior is not Riemann-flat even though it is Ricci-flat.

This standard Schwarzschild fact is an external GR comparator. It is not counted as a DSD-derived result.

---

## 7. Weyl-flat but Riemann-curved control

The converse confusion is blocked with a constant-sectional-curvature algebraic tensor

\[
R_{abcd}
=K\left(g_{ac}g_{bd}-g_{ad}g_{bc}\right).
\]

In four dimensions the regression verifies

\[
R_{ab}=3K g_{ab},
\qquad
R=12K,
\qquad
C_{abcd}=0.
\]

For \(K\neq0\), the full Riemann tensor remains nonzero.

Hence

\[
\boxed{
C_{abcd}=0
\not\Rightarrow
R_{abcd}=0.
}
\]

Ricci and Weyl sectors therefore encode distinct pieces of the full local curvature.

---

## 8. Vacuum must declare the cosmological-constant convention

The Einstein equation is treated as a separately supplied physical law,

\[
G_{ab}+\Lambda g_{ab}=\kappa T_{ab}.
\]

For physical vacuum \(T_{ab}=0\), tracing the four-dimensional equation gives

\[
R=4\Lambda,
\]

and therefore

\[
R_{ab}=\Lambda g_{ab}.
\]

Thus the common shorthand

\[
\text{vacuum}\Rightarrow R_{ab}=0
\]

is valid only in the \(\Lambda=0\) convention.

The regression verifies this with constant-curvature controls \(K=\Lambda/3\):

\[
G_{ab}+\Lambda g_{ab}=0
\]

while \(R_{ab}\neq0\) whenever \(\Lambda\neq0\).

The correct firewall is therefore

\[
\boxed{
T_{ab}=0
\not\Rightarrow
R_{ab}=0
\quad\text{unless the Lambda convention is specified.}
}
\]

---

## 9. Vacuum tidal projection

REL Extension 006 found that a general fixed comoving observer accesses a six-dimensional symmetric tidal block \(R_{0i0j}\).

Restricting the present algebraic space to the ten-dimensional Ricci-flat/Weyl kernel, the same fixed-observer tidal map has exact rank 5. Its spatial trace vanishes.

Hence in Ricci-flat vacuum the fixed observer sees the familiar five-dimensional electric/tidal part of the Weyl tensor while five Weyl degrees remain outside that readout.

Therefore

\[
\boxed{
\text{vacuum simplification}
\not\Rightarrow
\text{one-observer full Weyl reconstruction}.
}
\]

This is a direct continuation of the observability boundary established in REL Extension 006.

---

## 10. Matter-source inversion firewall

Suppose full geometry is known. If one **also supplies**

```text
Einstein field equation
Lambda
kappa
```

then the stress-energy tensor follows algebraically as

\[
T_{ab}
=
\frac{1}{\kappa}
\left(G_{ab}+\Lambda g_{ab}\right).
\]

This is a valid theorem consequence of the supplied Einstein equation.

It is not an independent derivation of that equation from curvature alone.

The regression holds one geometry fixed and changes \(\kappa\) or \(\Lambda\). The inferred \(T_{ab}\) changes. Therefore the curvature decomposition by itself does not carry either the coupling normalization or the cosmological-constant choice.

Furthermore, even a fixed stress-energy tensor does not uniquely specify microscopic matter constitution without a separate matter model.

Hence

\[
\boxed{
\text{Riemann/Ricci/Weyl data}
\not\Rightarrow
\text{unique material-source law}.
}
\]

---

## 11. DSD provenance classification

```text
R0 PRE_EXISTING_DSD
  typed status/applicability discipline
  explicit downstream bridge discipline
  external evolution time not automatically relativistic proper time
  supplied localization metric not automatically spacetime metric

R1 GENERAL_MATHEMATICAL_STRUCTURAL
  algebraic tensor symmetries
  contraction map
  rank-nullity / kernel reasoning
  decomposition and reconstruction bookkeeping

R2 RELATIVITY_SPECIALIZATION
  4D Lorentzian metric
  Levi-Civita curvature interpretation
  Riemann/Ricci/Weyl physical spacetime reading
  Schwarzschild solution
  stress-energy interpretation
  Einstein field equation
  Lambda and kappa

R3 STANDARD_THEOREM_CONSEQUENCE
  4D Weyl/Ricci decomposition once R2 geometry is supplied
  Ricci-flat Schwarzschild exterior
  EFE source inversion after EFE, Lambda and kappa are supplied
  Lambda-vacuum relation R_ab = Lambda g_ab in 4D

R4 REMAINS_EXTERNAL_NOT_DERIVED
  why physical spacetime obeys Einstein dynamics
  numerical values of G/c/Lambda
  actual matter content and matter Lagrangian
  unique microscopic source interpretation from T_ab
  structural-gravity dynamics
```

No R2/R3 item is back-counted as target-independent evidence for generic DSD.

---

## 12. Deterministic regression result

Run from repository root:

```bash
python audits/science/2026-09-10_rel_extension_007_ricci_weyl_matter_source_vacuum_curvature_gate.py --mode all
```

Observed result:

```text
ALGEBRAIC_RICCI_MAP:                  PASS
WEYL_DECOMPOSITION:                   PASS
RICCI_FLAT_CURVATURE_COUNTERMODEL:    PASS
CONSTANT_CURVATURE_CONTROL:           PASS
LAMBDA_VACUUM_BOUNDARY:               PASS
VACUUM_TIDAL_PROJECTION:              PASS
SCHWARZSCHILD_VACUUM_COMPARATOR:      PASS
SOURCE_ATTRIBUTION_FIREWALL:          PASS
DSD_PROVENANCE:                       PASS
COMPARATOR_SCOPE:                     PASS

TOTAL: 147/147 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

The 147 checks include repeated basis-by-basis decomposition, trace, and exact-rank consistency tests. They are not 147 independent empirical tests or physical theorems.

---

## 13. Verdict

**PASS_WITH_BOUNDARY**.

The gate establishes three independent separations:

\[
\boxed{R_{ab}=0\not\Rightarrow R_{abcd}=0,}
\]

\[
\boxed{C_{abcd}=0\not\Rightarrow R_{abcd}=0,}
\]

and

\[
\boxed{
\text{curvature decomposition}
\neq
\text{material-source attribution}
\neq
\text{derivation of Einstein dynamics}.
}
\]

The Ricci contraction removes a ten-dimensional Weyl kernel in the general four-dimensional algebraic-curvature space. Conversely, constant-curvature geometry can have vanishing Weyl tensor and nonzero Ricci/Riemann curvature.

No contradiction with the current DSD core papers was found, and no structural-gravity model was used.

---

## 14. External references

- Wolfram MathWorld, *Weyl Tensor*, standard n-dimensional Riemann/Weyl/Ricci decomposition and Weyl component count: https://mathworld.wolfram.com/WeylTensor.html
- Wolfram MathWorld, *Riemann Tensor*, standard curvature decomposition: https://mathworld.wolfram.com/RiemannTensor.html
- Cadabra manual, *Schwarzschild*, explicit symbolic verification of \(R_{\mu\nu}=0\) and \(R_{abcd}R^{abcd}=48M^2/r^6\): https://cadabra.science/notebooks/schwarzschild.html
- Goethe University Frankfurt, *ART mit dem Computer*, Schwarzschild Ricci-flatness and Kretschmann invariant: https://itp.uni-frankfurt.de/~hanauske/VARTC/VARTC2023.html

These are external comparators and are not counted as DSD-derived evidence.

---

## 15. Next target

**REL Extension 008 — Scalar-Invariant / Frame-Classification / Degenerate-Curvature Gate**.

The next audit should separate

```text
full tensor curvature
scalar polynomial curvature invariants
frame/tetrad components
coordinate components
Cartan-type derivative data
local isometry classification
```

with the central firewall

\[
\text{matching a finite set of curvature scalars}
\not\Rightarrow
\text{local metric/isometry equivalence}.
\]

A particularly important comparator class will be nonflat VSI/pp-wave spacetimes, where all scalar polynomial curvature invariants can vanish despite nonzero curvature. This must be verified from primary/authoritative literature before use in the next gate.
