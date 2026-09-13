# BH-RB-009 — Dynamic finite-support trapped-region gate

## Verdict

**PASS_WITH_BOUNDARY / FINITE_3D_SUPPORT_CAN_ENTER_TRAPPED_REGION / POSITIVE_MINIMUM_RADIUS_NOT_DERIVED**

## Purpose

This audit continues the active DSD gravity rebaseline without reusing the discarded structural-gravity branch. It tests a narrower question than a black-hole interior equation of state:

> Can a finite three-dimensional matter support enter a trapped region while its areal radius remains strictly positive?

The test does **not** assume that a trapped surface forces matter support to become zero-dimensional, nor does it assume that a positive minimum core radius exists.

## Provenance

- **R0/R1 DSD:** component-resolved dynamic state, lineage/formation transition separation, support-preserving representation, no automatic identification of rank transition with spacetime-dimension change.
- **R2/R3 relativity specialization:** spherical areal radius, Misner–Sharp mass, trapped/marginal/untrapped sphere classification.
- **R4 external physical model:** Einstein dynamics and the Oppenheimer–Snyder homogeneous pressureless-dust collapse witness.

No external GR statement is relabeled as a generic DSD derivation.

## Spherical dynamic gate

For a spherically symmetric spacetime, let `R(t,r)` denote areal radius and `m(t,r)` the Misner–Sharp mass. Restoring `G` and `c`, define the local compactness

\[
\mathcal C_{\rm MS}(t,r)=\frac{2Gm(t,r)}{R(t,r)c^2}.
\]

The standard spherical classification is

\[
\mathcal C_{\rm MS}<1 \Rightarrow \text{untrapped},
\qquad
\mathcal C_{\rm MS}=1 \Rightarrow \text{marginal},
\qquad
\mathcal C_{\rm MS}>1 \Rightarrow \text{trapped}.
\]

The key logical point is that this criterion constrains the causal behavior of two-spheres. It does not contain the implication

\[
\mathcal C_{\rm MS}>1 \Rightarrow R=0.
\]

Therefore a trapped region and a finite positive areal radius are not mutually exclusive at the kinematic level.

Reference: S. A. Hayward, *Gravitational energy in spherical symmetry*, Phys. Rev. D 53, 1938 (1996), DOI: 10.1103/PhysRevD.53.1938.

## Oppenheimer–Snyder crossing witness

Use the standard homogeneous, pressureless dust collapse as a control witness. For the outer surface released from rest at `R0`, a convenient cycloidal parametrization is

\[
R(\eta)=\frac{R_0}{2}(1+\cos\eta),
\]

\[
\tau(\eta)=\sqrt{\frac{R_0^3}{8GM}}\,(\eta+\sin\eta),
\qquad 0\le\eta\le\pi.
\]

The zero-radius endpoint occurs at

\[
\eta=\pi,
\qquad
R(\pi)=0.
\]

The surface crosses the Schwarzschild radius

\[
r_s=\frac{2GM}{c^2}
\]

at an earlier parameter value `eta_h` determined by

\[
\frac{R_0}{2}(1+\cos\eta_h)=r_s.
\]

Thus, for every interval

\[
\eta_h<\eta<\pi,
\]

the outer support radius satisfies

\[
0<R(\eta)<r_s,
\]

while the surface is already inside the trapped regime.

This is a direct counterexample to the automatic identification

\[
\text{horizon/trapped entry}=\text{zero-dimensional matter support}.
\]

References:

- J. R. Oppenheimer and H. Snyder, *On Continued Gravitational Contraction*, Phys. Rev. 56, 455 (1939), DOI: 10.1103/PhysRev.56.455.
- A modern presentation of the cycloidal surface trajectory is also given in discussions of the Oppenheimer–Snyder model, e.g. Frontiers in Astronomy and Space Sciences 3, 29 (2016), DOI: 10.3389/fspas.2016.00029.

## Sgr A* scale control

The same external Sgr A* mass control used in the active branch is retained only as a scale input:

\[
M=4.297\times10^6M_\odot.
\]

Then

\[
r_s\approx1.269049932\times10^7\ \mathrm{km}.
\]

For a deliberately synthetic control initial radius

\[
R_0=4r_s,
\]

one obtains

\[
\eta_h=\frac{2\pi}{3}\approx2.0943951,
\]

\[
\tau_h\approx501.269641\ \mathrm{s},
\]

while the pressureless-dust zero-radius endpoint occurs at

\[
\tau_{0}\approx531.946397\ \mathrm{s}.
\]

Hence the chosen control has a proper-time interval

\[
\Delta\tau\approx30.676756\ \mathrm{s}
\]

between horizon crossing and the dust-model zero-radius endpoint.

At the representative post-crossing value `eta=2.5`,

\[
R\approx0.397712769\,r_s
\approx5.0471736\times10^6\ \mathrm{km},
\]

and

\[
\frac{2GM}{Rc^2}\approx2.514377405>1.
\]

The matter support is therefore still at a strictly positive areal radius while the control sphere is trapped.

The choice `R0=4r_s` is a synthetic audit control, not a reconstruction of the actual formation history of Sgr A*.

## What this proves

The standard GR witness establishes only the following limited result:

\[
\boxed{
\text{finite positive 3D support can cross into a trapped region before }R=0
}
\]

This supports the DSD separation

\[
\text{spatial/support compression}
\neq
\text{dimensional-rank collapse}.
\]

It also shows that the horizon condition by itself cannot be used as evidence that the material support has already become a point or zero-dimensional object.

## What this does not prove

Oppenheimer–Snyder dust continues to `R=0` in finite comoving proper time. Therefore it is **not** a model of the proposed persistent finite black-hole core.

This audit does not derive:

- a positive minimum radius `R_min>0`;
- a bounce or static endpoint;
- a new black-hole equation of state;
- a constituent-agnostic re-formed core stress law;
- a DSD-native replacement for Einstein dynamics;
- avoidance of singularity theorems;
- preservation of all microscopic information.

The result is only a crossing/existence gate: finite support and trapped-region membership can coexist for a nonzero interval.

## Next gate

BH-RB-010 should therefore ask a stronger question:

\[
\boxed{
\text{what constitutive or transition conditions are necessary for }
R_{\rm core}(\tau)\ge R_{\min}>0
\text{ after trapped-region entry?}
}
\]

The next audit should separate at least three possibilities:

1. continuing collapse with no lower bound;
2. finite-radius bounce/re-expansion;
3. asymptotic or dynamically maintained finite-radius successor core.

No branch should be selected in advance. Energy conditions, causal propagation, stress anisotropy, flux, and formation-level successor rules must be audited before assigning a physical interpretation.
