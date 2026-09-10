# REL Core 007 — Horizon / Coordinate-Singularity / Curvature-Singularity / Causal-Boundary Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Track**

## 1. Purpose

REL Core 001R–006 separated standard-relativity provenance, Lorentzian geometry, geodesic/curvature response, Einstein evolution, diffeomorphism/gauge equivalence, and the linearized radiative sector.

REL Core 007 audits the black-hole boundary/singularity layer:

```text
Schwarzschild-coordinate breakdown
-> regular horizon chart
-> invariant curvature
-> local null-cone behavior
-> global event-horizon status
-> genuine curvature singularity
-> causal geodesic incompleteness
-> descriptive-access restriction
```

The principal firewall is

\[
\boxed{
\text{coordinate singularity}
\neq
\text{event horizon}
\neq
\text{curvature singularity}
\neq
\text{geodesic incompleteness}
\neq
\text{DSD descriptive inaccessibility}
}
\]

This gate uses the standard positive-mass Schwarzschild solution as an explicitly supplied relativity specialization. It does not derive Schwarzschild geometry from generic DSD.

---

## 2. Supplied Schwarzschild specialization

In geometric units \(G=c=1\), supply

\[
 ds^2
 =
 -\left(1-\frac{2M}{r}\right)dt^2
 +\left(1-\frac{2M}{r}\right)^{-1}dr^2
 +r^2d\Omega^2,
 \qquad M>0.
\]

Write

\[
 f(r)=1-\frac{2M}{r}.
\]

Then

```text
r > 2M : f(r) > 0
r = 2M : f(r) = 0
r < 2M : f(r) < 0
```

The Schwarzschild-coordinate coefficient \(g_{rr}=f^{-1}\) diverges at \(r=2M\). This is not yet a coordinate-independent singularity statement.

---

## 3. Coordinate failure versus regular horizon geometry

Introduce ingoing Eddington–Finkelstein time

\[
 v=t+r_*,
 \qquad
 \frac{dr_*}{dr}=f^{-1}.
\]

The metric becomes

\[
 ds^2=-f(r)dv^2+2\,dv\,dr+r^2d\Omega^2.
\]

The \((v,r)\) block is

\[
\begin{pmatrix}
-f & 1\\
1 & 0
\end{pmatrix},
\]

whose determinant is exactly

\[
\boxed{-1}.
\]

Hence the metric remains nondegenerate at \(r=2M\). At the equator,

\[
\det g=-r^4,
\]

so at \(r=2M\) it is finite and nonzero.

Therefore

\[
\boxed{
\text{Schwarzschild chart breakdown at }r=2M
\not\Rightarrow
\text{geometric singularity there}.
}
\]

This matches the standard role of Eddington–Finkelstein or Kruskal coordinates: they extend smoothly through the Schwarzschild-coordinate horizon.

---

## 4. Invariant curvature gate

For Schwarzschild,

\[
K
:=
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
=
\frac{48M^2}{r^6}.
\]

At the horizon,

\[
K(2M)=\frac{3}{4M^4},
\]

which is finite for \(M>0\).

At \(r\to0^+\),

\[
K(r)\to+\infty.
\]

Thus the supplied Schwarzschild solution exhibits the explicit separation

\[
\boxed{
 r=2M:
 \text{coordinate failure in Schwarzschild coordinates, finite curvature}
}
\]

versus

\[
\boxed{
 r=0:
 \text{curvature blow-up}.
}
\]

Curvature blow-up is a strong invariant witness in Schwarzschild, but this audit does **not** redefine every spacetime singularity as curvature divergence.

---

## 5. Local causal one-way structure

For radial null curves in ingoing Eddington–Finkelstein coordinates,

\[
0=-f\,dv^2+2\,dv\,dr.
\]

The nontrivial outgoing branch satisfies

\[
\frac{dr}{dv}=\frac12f(r).
\]

Therefore

```text
outside r>2M : dr/dv > 0
horizon r=2M : dr/dv = 0
inside  r<2M : dr/dv < 0
```

Once the standard future time orientation and Schwarzschild extension are supplied, the outgoing radial branch cannot increase \(r\) inside the horizon.

However, the **event horizon** is not defined merely by \(g_{tt}=0\), by the sign of one coordinate coefficient, or by one local finite check. Its classification is a global causal/asymptotic statement. This gate therefore records the local null-cone witness as R3 and keeps the global horizon identification dependent on the supplied Schwarzschild spacetime and its asymptotic structure.

---

## 6. Curvature singularity versus geodesic incompleteness

For a radial timelike geodesic dropped from rest at infinity, \(E=1\),

\[
\frac{dr}{d\tau}
=-\sqrt{\frac{2M}{r}}.
\]

The proper time from the horizon \(r=2M\) to \(r=0\) is

\[
\Delta\tau
=
\int_0^{2M}\sqrt{\frac{r}{2M}}\,dr
=
\boxed{\frac{4M}{3}}.
\]

Hence this causal geodesic reaches the Schwarzschild curvature singularity in finite proper time.

That supports geodesic incompleteness of the maximal Schwarzschild spacetime, but the logical notions remain distinct. A separate counterexample is the restricted flat region of Minkowski spacetime with an omitted boundary: its curvature is zero, yet a straight causal geodesic can hit the omitted boundary at finite affine/proper parameter.

Therefore

\[
\boxed{
\text{geodesic incompleteness}
\not\Rightarrow
\text{curvature blow-up in every spacetime}.
}
\]

and this audit does not use curvature divergence as the universal definition of singularity.

---

## 7. DSD descriptive-access firewall

The current DSD Dynamics defines a descriptive projection

\[
\Pi_O:X\to X_O
\]

for a declared descriptive-accessibility specification \(O\), and explicitly does not assume that this projection is injective. Therefore two distinct structural states can become equivalent under one restricted descriptive regime without becoming identical as full states.

This produces a useful compatibility rule for black-hole applications:

\[
\boxed{
\text{restricted descriptive access}
\neq
\text{underlying structural nonexistence}.
}
\]

But the same formal distinction does **not** authorize the converse identification

\[
\boxed{
\text{DSD descriptive projection}
\neq
\text{GR event horizon}.
}
\]

A GR event horizon is fixed by the supplied Lorentzian causal structure and global asymptotics. A DSD descriptive projection is a declared information/readout interface. Connecting them would require an explicit application bridge and proof of compatibility.

Similarly,

\[
\boxed{
\text{causal inaccessibility}
\neq
\text{DSD undefined assignment}
}
\]

because Formation's undefined-assignment status is a typed domain statement, not a synonym for an observer's inability to receive a signal.

No current result permits importing the internal structural-gravity notions of local-collapse convergence or support limits and calling them Schwarzschild horizons without a separate derivation.

---

## 8. Provenance ledger

```text
R0 PRE_EXISTING_DSD
  typed status / domain distinctions
  descriptive-access projection discipline
  reduced-readout noninjectivity firewall
  explicit-bridge requirement

R1 GENERAL_MATHEMATICAL_STRUCTURAL
  coordinate-invariant scalar comparison
  chart regularity / nondegeneracy distinction
  geodesic incompleteness as affine/proper-parameter criterion

R2 RELATIVITY_SPECIALIZATION
  positive-mass Schwarzschild vacuum solution
  mass parameter M
  asymptotically flat Schwarzschild interpretation
  maximal extension / future time orientation
  event-horizon global causal setting

R3 STANDARD_THEOREM_CONSEQUENCE
  Schwarzschild-coordinate failure at r=2M
  Eddington-Finkelstein regularity there
  K=48M^2/r^6
  finite K at r=2M
  curvature blow-up at r=0
  radial-null one-way sign structure
  E=1 finite proper time 4M/3 from horizon to r=0

R4 REMAINS_EXTERNAL_NOT_DERIVED
  generic DSD -> Schwarzschild solution
  generic DSD -> event horizon
  DSD descriptive projection = event horizon
  DSD undefined assignment = causal inaccessibility
  structural-gravity local collapse = Schwarzschild black hole
  uniqueness of astrophysical interior/source from exterior Schwarzschild data
```

No R3 consequence is counted retroactively as evidence that generic DSD supplied the R2 black-hole geometry.

---

## 9. Reproducibility

GitHub files:

```text
audits/science/2026-09-10_rel_core_007_horizon_coordinate_curvature_causal_boundary_gate.py
audits/science/2026-09-10_rel-core-007-horizon-coordinate-curvature-causal-boundary-gate-audit.md
methodology/RELATIVITY_HORIZON_SINGULARITY_CAUSAL_BOUNDARY_INTERFACE.md
```

Run from repository root:

```bash
python audits/science/2026-09-10_rel_core_007_horizon_coordinate_curvature_causal_boundary_gate.py --mode all
```

Actual result:

```text
SCHWARZSCHILD: 9/9 PASS
EF_HORIZON: 7/7 PASS
GEODESIC: 6/6 PASS
PROVENANCE: 17/17 PASS

TOTAL: 39/39 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

The script uses the Python standard library only.

---

## 10. External standard-theory checks

Primary cross-checks used for this gate:

- David Tong, *General Relativity*, Sec. 6.1.3: ingoing Eddington–Finkelstein coordinates and horizon regularity.
  https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S6.html
- Cambridge GR II notes, Appendix F: coordinate versus physical singularities, Schwarzschild Kretschmann scalar, and geodesic incompleteness.
  https://www.damtp.cam.ac.uk/user/us248/Lectures/Notes/grII.pdf

These references support the standard-relativity side of the bridge. They are not treated as DSD-derived results.

---

## 11. Final verdict

**PASS_WITH_BOUNDARY**.

The supplied Schwarzschild geometry cleanly supports

\[
\boxed{
\text{coordinate breakdown at }2M
\neq
\text{curvature singularity}
}
\]

and, after supplying the global Schwarzschild causal structure,

\[
\boxed{
\text{regular horizon}
\neq
\text{central curvature singularity}.
}
\]

The specific \(E=1\) radial geodesic reaches \(r=0\) in finite proper time, while the flat restricted-manifold counterexample prevents equating geodesic incompleteness with curvature blow-up in general.

For DSD, the valid conclusion is only that its typed accessibility/readout discipline can keep causal access, chart access, assignment status, and full structural existence distinct.

It does **not** establish

\[
\boxed{
\text{generic DSD}
\Longrightarrow
\text{Schwarzschild black-hole causal structure}.
}
\]

No DSD core-paper revision is required by this gate.

Next target:

```text
REL Core 008 — Integrated Standard-Relativity Reconstruction Synthesis / Provenance Closure Gate
```

The next gate should synthesize REL Core 001R–007 into one provenance/dependency ledger, classify which parts are supplied relativity structure versus theorem consequences, and close the ordinary standard-relativity track before any QFT/quantum-gravity or structural-gravity bridge is reopened.
