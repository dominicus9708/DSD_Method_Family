# REL Extension 008 — Scalar-Invariant / Frame-Classification / Degenerate-Curvature Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Extension Track**

## 1. Purpose

REL Extension 007 separated Ricci curvature, Weyl curvature, vacuum conditions, matter-source attribution, and Einstein dynamics.

This extension asks a different reconstruction question:

1. Do scalar polynomial curvature invariants determine the full local curvature tensor?
2. If two Lorentzian metrics have the same scalar curvature invariants, must they be locally isometric?
3. Can nonflat curvature be hidden from all scalar polynomial curvature invariants?
4. What additional frame-normalized information is required when scalar invariants are degenerate?
5. What, if anything, does this imply for generic DSD?

The principal firewalls are

\[
\text{same scalar polynomial curvature invariants}
\not\Rightarrow
\text{same full curvature},
\]

and

\[
\text{same scalar polynomial curvature invariants}
\not\Rightarrow
\text{local isometry}
\]

without an explicit nondegeneracy theorem or equivalent additional structure.

---

## 2. Standard-relativity comparator locked before DSD interpretation

A four-dimensional pp-wave can locally be written in Brinkmann form

\[
ds^2
=
2\,du\,dv
+
H(u,x,y)\,du^2
+
dx^2+dy^2.
\]

For the vacuum Einstein equation, \(H\) is harmonic in the transverse coordinates.

The deterministic witness uses

\[
H=A(x^2-y^2),
\qquad
A\neq 0,
\]

which is harmonic and gives a nonflat vacuum plane wave.

For the convention used in the audit,

\[
R_{uxux}=-A,
\qquad
R_{uyuy}=+A,
\]

up to the usual Riemann symmetries.

The Ricci tensor vanishes but the Riemann tensor does not.

External comparator:

- C. Roche, A. B. Aazami, C. Cederbaum, *Exact parallel waves in general relativity*, General Relativity and Gravitation 55, 40 (2023), DOI: 10.1007/s10714-023-03083-x.
- The review states the local Brinkmann form, the vacuum harmonic condition, and that all scalar curvature invariants of plane waves vanish.
- V. Pravda, A. Pravdová, A. Coley, R. Milson, *All spacetimes with vanishing curvature invariants*, Class. Quantum Grav. 19 (2002) 6213–6236, DOI: 10.1088/0264-9381/19/23/318.

---

## 3. Deterministic finite scalar witness

At \(x=y=0\), the inverse metric in \((u,v,x,y)\) coordinates is

\[
g^{uv}=g^{vu}=1,
\qquad
g^{xx}=g^{yy}=1,
\qquad
g^{uu}=0.
\]

With \(A=2\), the program constructs the full covariant Riemann tensor from

\[
R_{uxux}=-2,
\qquad
R_{uyuy}=+2
\]

and the algebraic symmetries.

The exact rational computation gives

\[
R_{\mu\nu}=0,
\qquad
R=0,
\qquad
R_{\mu\nu}R^{\mu\nu}=0,
\qquad
R_{\alpha\beta\gamma\delta}
R^{\alpha\beta\gamma\delta}=0.
\]

The Riemann tensor is nevertheless nonzero.

The induced curvature operator on the six-dimensional bivector basis has

\[
\operatorname{rank}=2,
\qquad
\mathcal R^2=0.
\]

Hence its trace powers vanish in the tested family:

\[
\operatorname{tr}(\mathcal R^n)=0,
\qquad
n=1,\ldots,6.
\]

This is a finite algebraic witness, not by itself a proof of the all-orders VSI theorem.

---

## 4. All-orders VSI result is external standard geometry

The all-orders statement is locked to the external literature.

For plane waves, scalar curvature invariants built from the metric, Riemann tensor, and covariant derivatives of the Riemann tensor vanish.

More generally, the VSI literature classifies Lorentzian spacetimes for which all scalar polynomial curvature invariants of all derivative orders vanish.

Therefore the finite program establishes a transparent local countermodel, while the universal all-orders statement remains an external standard-relativity theorem.

This distinction prevents the regression program from silently promoting finite sampling into a theorem.

---

## 5. Minkowski versus nonflat plane wave

Use two metrics on the same local coordinate carrier:

\[
g_{\mathrm{flat}}
=
2\,du\,dv+dx^2+dy^2
\]

and

\[
g_{\mathrm{wave}}
=
2\,du\,dv
+
A(x^2-y^2)du^2
+
dx^2+dy^2.
\]

The flat metric has

\[
R_{\alpha\beta\gamma\delta}=0.
\]

The plane wave has

\[
R_{\alpha\beta\gamma\delta}\neq0.
\]

Yet the complete scalar polynomial curvature-invariant family vanishes for both.

Thus

\[
\boxed{
\text{same complete SPI family}
\not\Rightarrow
\text{same Riemann tensor}
}
\]

and because a local isometry preserves the curvature tensor,

\[
\boxed{
\text{same complete SPI family}
\not\Rightarrow
\text{local isometry}.
}
\]

This is stronger than a statement about a few familiar invariants such as the Ricci scalar or Kretschmann scalar.

---

## 6. Scalar readout as a non-injective reconstruction map

Let

\[
\Phi_{\mathrm{SPI}}(g)
=
\{I_1(g),I_2(g),\ldots\}
\]

denote the supplied family of scalar polynomial curvature readouts.

For the flat metric and the nonflat plane wave,

\[
\Phi_{\mathrm{SPI}}(g_{\mathrm{flat}})
=
\Phi_{\mathrm{SPI}}(g_{\mathrm{wave}})
=
0.
\]

Hence the readout fiber is nontrivial:

\[
\Phi_{\mathrm{SPI}}^{-1}(0)
\]

contains geometrically inequivalent metrics.

This is an application of the DSD analysis tool `readout fiber`; it is not a new DSD axiom and does not derive the pp-wave geometry.

---

## 7. I-nondegenerate versus degenerate Kundt boundary

The failure above is not promoted to the claim that scalar polynomial invariants are always useless.

Coley, Hervik and Pelavas prove in four-dimensional Lorentzian geometry that a metric is either \(\mathcal I\)-non-degenerate, in which case it is locally characterized by its scalar polynomial curvature invariants, or it belongs to the Kundt class; metrics not characterized by the invariants must be of degenerate Kundt form.

External comparator:

- A. Coley, S. Hervik, N. Pelavas, *Spacetimes characterized by their scalar curvature invariants*, Class. Quantum Grav. 26 (2009) 025013, DOI: 10.1088/0264-9381/26/2/025013.

Therefore the correct firewall is

\[
\boxed{
\text{SPI reconstruction requires a nondegeneracy condition;}
}
\]

not

\[
\text{SPIs never characterize Lorentzian geometry}.
\]

---

## 8. Frame-resolution and Cartan/Karlhede boundary

At the origin, choose the pseudo-orthonormal frame

\[
e_0=\frac{\partial_u-\partial_v}{\sqrt2},
\qquad
e_1=\frac{\partial_u+\partial_v}{\sqrt2},
\qquad
e_2=\partial_x,
\qquad
e_3=\partial_y.
\]

The electric tidal matrix is

\[
E_{ij}=R(e_0,e_i,e_0,e_j)
=
\begin{pmatrix}
0&0&0\\
0&-A/2&0\\
0&0&A/2
\end{pmatrix}.
\]

For \(A=2\),

\[
E=
\operatorname{diag}(0,-1,+1),
\]

which directly distinguishes the plane wave from Minkowski space even though the SPI readout is identical.

However, raw frame components are not themselves absolute invariants.

A \(45^\circ\) rotation in the transverse spatial basis changes the nonzero pattern from diagonal to off-diagonal while preserving rotation-invariant properties of that observer's tidal matrix.

Therefore

\[
\boxed{
\text{frame-resolved tensor data}
\neq
\text{arbitrary raw coordinate/frame components}.
}
\]

Vacuum pp-wave equivalence can instead be handled by the Cartan–Karlhede procedure, which normalizes Lorentz-frame freedom and uses the Riemann tensor and its covariant derivatives.

Milson, McNutt and Coley give a complete invariant classification of vacuum pp-waves using Cartan invariants and show that the fourth covariant derivative bound is sharp for that class.

External comparator:

- R. Milson, D. McNutt, A. Coley, *Invariant classification of vacuum PP-waves*, J. Math. Phys. 54 (2013) 022502, DOI: 10.1063/1.4791691, arXiv:1209.5081.

Thus

\[
\text{SPI degeneracy}
\not\Rightarrow
\text{geometry is unclassifiable}.
\]

It means a richer invariant classification procedure is required.

---

## 9. Provenance classification

```text
R0 PRE_EXISTING_DSD
  typed status/applicability
  explicit downstream bridge discipline
  external numerical evolution time is not automatically relativistic proper time
  readout-fiber analysis can represent noninjective observation/reconstruction maps

R1 GENERAL_MATHEMATICAL_STRUCTURAL
  scalar readout map
  injectivity / noninjectivity distinction
  tensor-versus-scalar information loss
  frame normalization versus raw component choice

R2 RELATIVITY SPECIALIZATION
  four-dimensional Lorentzian metric
  Levi-Civita connection
  Riemann tensor
  Brinkmann pp-wave metric
  vacuum Einstein specialization
  scalar polynomial curvature invariants
  Lorentz frame

R3 STANDARD THEOREM CONSEQUENCE
  plane-wave/VSI vanishing-invariant theorem
  I-nondegenerate versus degenerate-Kundt characterization
  Cartan–Karlhede invariant classification of vacuum pp-waves

R4 REMAINS EXTERNAL / NOT INDEPENDENTLY DERIVED
  why physical spacetime is Lorentzian and four-dimensional
  selection of the pp-wave or any actual physical metric
  Einstein field dynamics
  empirical identification of a physical spacetime
  completeness of a chosen scalar/readout family outside theorem hypotheses
  Cartan frame-normalization rules as generic DSD outputs
```

---

## 10. DSD firewall

The current DSD dynamical framework permits supplied metric localization and downstream constitutive structure, but does not identify them automatically with physical spacetime geometry or Einstein dynamics.

Therefore none of the following are licensed:

```text
DSD scalar descriptor = curvature scalar
DSD residual = Weyl/Riemann curvature
DSD property aggregate = scalar polynomial invariant family
DSD channel labels = Lorentz-frame components
DSD c_info = relativistic c
SPI degeneracy = DSD derivation of pp-waves
Cartan/Karlhede classification = generic DSD theorem
```

The valid DSD-level contribution is the provenance and noninjective-readout diagnosis.

---

## 11. Deterministic regression result

```text
BRINKMANN_PLANE_WAVE_GEOMETRY:             PASS (45 checks)
FINITE_SCALAR_INVARIANT_WITNESS:           PASS (47 checks)
MINKOWSKI_VS_VSI_DEGENERACY:               PASS (7 checks)
FRAME_RESOLUTION_AND_NORMALIZATION_FIREWALL: PASS (9 checks)
DSD_PROVENANCE:                            PASS (16 checks)
COMPARATOR_SCOPE:                          PASS (12 checks)

TOTAL: 136/136 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

The 136 checks include repeated tensor-symmetry and matrix-entry checks and are not 136 independent physical results.

---

## 12. Final verdict

**PASS_WITH_BOUNDARY.**

The expected counterexample is real and stronger than the minimal plan required:

\[
\boxed{
\text{nonflat Lorentzian geometry can have the same complete SPI family as flat spacetime}.
}
\]

Therefore scalar curvature invariants alone are not a universal reconstruction interface for Lorentzian geometry.

The failure is controlled rather than universal: \(\mathcal I\)-non-degenerate metrics can be characterized by SPIs, while degenerate Kundt/VSI cases require richer frame-normalized tensorial information such as Cartan–Karlhede data.

No contradiction requiring revision of the current DSD core papers was found.

---

## 13. Reproducibility

Repository-root command:

```bash
python audits/science/2026-09-10_rel_extension_008_scalar_invariant_frame_classification_degenerate_curvature_gate.py --mode all
```

Files:

```text
audits/science/
2026-09-10_rel_extension_008_scalar_invariant_frame_classification_degenerate_curvature_gate.py

audits/science/
2026-09-10_rel-extension-008-scalar-invariant-frame-classification-degenerate-curvature-gate-audit.md

methodology/
RELATIVITY_SCALAR_INVARIANT_FRAME_CLASSIFICATION_DEGENERACY_INTERFACE.md
```

---

## 14. Next target

**REL Extension 009 — Integrated Independent-Origin / Reconstruction Closure Gate**

This is the final synthesis target for the ordinary standard-relativity reconstruction line.

It will combine Extensions 001–008 and ask, with no new physical selector silently inserted:

\[
\text{What exactly is reconstructible from generic DSD?}
\]

and

\[
\text{What remains supplied by standard relativity?}
\]

The closure must not convert successful compatibility into an independent derivation claim.
