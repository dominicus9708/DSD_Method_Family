# BH-GC-001 — Gravitational-Core Descriptor Gate

**Date:** 2026-09-16  
**Project:** DSD gravity rebaseline  
**Branch:** side audit; does **not** replace the canonical BH-RB-025 transport audit  
**Status:** PASS_WITH_BOUNDARY

## Question

The working intuition is that a dynamically changing black-hole interior need not preserve one material core. It may pass through single-core, multi-core, fluid-like, fragmented, and re-condensed states.

This audit asks:

> Can the location of maximum gravitational acceleration be promoted to the physical definition of the core?

The answer is:

\[
\boxed{
\text{it is a useful characteristic shell in a spherical Newtonian control, but it is not a unique core definition.}
}
\]

The maximum-acceleration location can differ from the density/tidal center and from the compactness maximum.

## 1. Spherical Newtonian gate

For a spherical mass distribution,

\[
m(r)=4\pi\int_0^r \rho(r')r'^2\,dr',
\]

\[
g(r)=\frac{Gm(r)}{r^2}.
\]

A nonzero-radius extremum of \(g\) satisfies

\[
\frac{dg}{dr}=0.
\]

Using

\[
\frac{dm}{dr}=4\pi r^2\rho,
\]

one obtains

\[
4\pi\rho(r_*)=\frac{2m(r_*)}{r_*^3}.
\]

With the interior mean density

\[
\bar\rho(r)=\frac{3m(r)}{4\pi r^3},
\]

this is

\[
\boxed{
\rho(r_*)=\frac{2}{3}\bar\rho(r_*).
}
\]

Thus the maximum-acceleration radius is not arbitrary. It is the radius at which continued enclosed-mass growth and geometric \(1/r^2\) dilution balance in this spherical Newtonian specialization.

## 2. Smooth Plummer control

Use the smooth Plummer profile only as a logical comparator, not as a black-hole interior model:

\[
\rho(r)=\frac{3M}{4\pi a^3}\left(1+\frac{r^2}{a^2}\right)^{-5/2}.
\]

Define

\[
x=\frac{r}{a}.
\]

Then

\[
m(r)=M\frac{x^3}{(1+x^2)^{3/2}},
\]

and

\[
g(r)=\frac{GM}{a^2}\frac{x}{(1+x^2)^{3/2}}.
\]

The maximum occurs at

\[
\boxed{
x_{g\max}=\frac{1}{\sqrt2}}.
\]

At this radius,

\[
\frac{\rho}{\bar\rho}=\frac{1}{1+x^2}=\frac23,
\]

which reproduces the general spherical condition.

## 3. Acceleration maximum is not compactness maximum

The spherical compactness-like radial shape is proportional to

\[
\frac{m(r)}{r}
\propto
\frac{x^2}{(1+x^2)^{3/2}}.
\]

Its maximum is at

\[
\boxed{
x_{\mathcal C\max}=\sqrt2}.
\]

Therefore

\[
\boxed{
r_{g\max}\neq r_{\mathcal C\max}}.
\]

For this control,

\[
r_{\mathcal C\max}=2r_{g\max}.
\]

So a maximum-acceleration shell cannot be silently identified with a \(\mathcal C=2Gm/(Rc^2)\) maximum or trapped-surface location.

## 4. Acceleration maximum is not tidal maximum

For a spherical Newtonian field, the tidal operator has one radial and two tangential eigen-directions. A Frobenius-norm control is

\[
\|\mathsf T\|^2
=
\left(\frac{dg}{dr}\right)^2
+2\left(\frac{g}{r}\right)^2.
\]

For the Plummer profile,

\[
\frac{a^3}{GM}\|\mathsf T\|
=
\sqrt{
\frac{3(1+2x^4)}{(1+x^2)^5}
}.
\]

This is maximal at

\[
\boxed{x_{T\max}=0}.
\]

Meanwhile

\[
g(0)=0.
\]

Hence

\[
\boxed{
\text{zero acceleration at the symmetry center}
\quad\text{can coexist with}\quad
\text{maximum tidal strength there}.
}
\]

The three characteristic locations are therefore distinct in one smooth control:

\[
\boxed{
0=x_{T\max}
<
\frac{1}{\sqrt2}=x_{g\max}
<
\sqrt2=x_{\mathcal C\max}.
}
\]

## 5. Revised core interpretation

The original maximum-acceleration intuition survives, but in a narrower role.

For a sufficiently spherical, quasi-Newtonian component, define a **characteristic gravitational shell** by

\[
R_{g\max}(t)
=
\operatorname*{arg\,max}_{r}|g(r,t)|.
\]

It can act as a useful radial marker of where the inward field changes from increasing to decreasing.

It should **not** be promoted to the unique center, unique material boundary, compactness maximum, curvature maximum, or trapped-surface radius.

## 6. Relativistic replacement

In general relativity, a local gravitational acceleration field is not observer-independent. A freely falling observer can have zero proper acceleration while still measuring strong tidal curvature.

For a specified timelike observer/flow field \(u^\mu\), define the spatial projector

\[
h_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu
\]

for signature \((-+++ )\), and the flow-conditioned tidal operator

\[
\mathcal E_{\mu\nu}[u]
=
h_\mu{}^\alpha h_\nu{}^\beta
R_{\alpha\rho\beta\sigma}
 u^\rho u^\sigma.
\]

A positive local tidal-strength descriptor is

\[
\boxed{
\mathcal T_u
=
\sqrt{\mathcal E_{\mu\nu}\mathcal E^{\mu\nu}}.
}
\]

In a local orthonormal frame this is the Frobenius norm of the geodesic-deviation matrix \(R_{\hat i\hat0\hat j\hat0}\).

This is not fully observer-independent: the choice of \(u^\mu\) remains part of the descriptor.

### Preferred flow when available

If the stress-energy tensor has a unique future-directed timelike Landau eigenvector,

\[
T^\mu{}_{\nu}u^\nu=-\varepsilon u^\mu,
\qquad
u^\mu u_\mu=-1,
\]

that flow can provide a physically motivated frame for the descriptor.

If no unique timelike energy frame exists, the model must retain the observer/flow index explicitly; it may not claim a unique invariant core from \(\mathcal T_u\) alone.

## 7. Dynamic multi-core definition

For a chosen admissible flow \(u\), define the instantaneous gravitational-core seeds by the local maxima of tidal strength:

\[
\boxed{
\mathfrak M_u(\tau)
=
\operatorname{LocMax}_{x}\mathcal T_u(x,\tau).
}
\]

There may be one, several, or no isolated maxima.

This permits:

\[
K_1
\longrightarrow
K_{1a}\cup K_{1b}
\]

for splitting and

\[
K_1\cup K_2
\longrightarrow
K_3
\]

for merger without requiring persistent constituent identity.

The DSD lineage record should track predecessor-successor relations among these gravitational-core components rather than presuming that one material object persists.

## 8. Core center versus characteristic shell

The audit therefore separates two objects:

\[
\boxed{
\text{gravitational-core seed/center}
\sim
\operatorname{LocMax}\mathcal T_u
}
\]

and, only where an approximately radial component exists,

\[
\boxed{
\text{characteristic acceleration shell}
\sim
\operatorname*{arg\,max}|g|.
}
\]

The acceleration shell can surround a tidal core seed; it need not coincide with it.

For a non-spherical or rapidly time-dependent state, a single shell radius may not exist at all.

## 9. Relation to the active black-hole branch

This refinement fits the current successor-core hypothesis better than a permanent solid-like sphere.

The interior state may cycle through

\[
\text{single condensed component}
\leftrightarrow
\text{multi-component state}
\leftrightarrow
\text{fluid-like state}
\leftrightarrow
\text{fragmented/re-formed state}.
\]

The persistent object of study is then not a fixed material ball but a causal, finite-support, time-dependent stress-energy structure together with its gravitational-core descriptor and lineage.

This does **not** derive such an interior from GR or DSD. It only supplies a non-circular way to describe the candidate structure if a physical solution exists.

## 10. Firewalls

The following identifications remain forbidden:

\[
\text{maximum acceleration}
\neq
\text{maximum tidal curvature}
\neq
\text{maximum compactness}
\neq
\text{event horizon}
\neq
\text{material-core boundary}.
\]

Also,

\[
\mathcal T_u\text{ maximum}
\neq
\text{observer-independent unique core}
\]

unless a physically preferred flow has independently been supplied.

The compactness

\[
\mathcal C=\frac{2Gm}{Rc^2}
\]

remains a separate spherical Misner-Sharp/GR specialization and must not be inferred from the tidal descriptor alone.

## Result

The reproducibility script gives

\[
\boxed{17/17\ \mathrm{PASS}}.
\]

Final verdict:

\[
\boxed{
\begin{aligned}
&\text{PASS\_WITH\_BOUNDARY /}\\
&\text{MAXIMUM\_ACCELERATION\_IS\_A\_USEFUL\_CHARACTERISTIC\_SHELL /}\\
&\text{IT\_IS\_NOT\_A\_UNIQUE\_CORE\_CENTER /}\\
&\text{TIDAL\_AND\_COMPACTNESS\_MAXIMA\_ARE\_DISTINCT /}\\
&\text{DYNAMIC\_MULTICORE\_DESCRIPTOR\_IS\_ADMISSIBLE /}\\
&\text{PHYSICAL\_BLACK\_HOLE\_INTERIOR\_CORE\_NOT\_DERIVED}.
\end{aligned}
}
\]

## Next side audit — BH-GC-002

Construct a dynamic multi-core lineage control in which local tidal maxima can move, split, merge, and disappear while every signal/transport channel remains causal.

The audit should distinguish:

\[
\text{component motion},\quad
\text{descriptor-maximum motion},\quad
\text{material transport},\quad
\text{causal signal speed}.
\]

A maximum of a field may move faster than \(c\) as a pattern without carrying matter or information; this must not be confused with a causal transport speed. BH-GC-002 should therefore establish an explicit lineage/causality firewall before the descriptor is used in the black-hole dynamics branch.

## Reproducibility

From the repository root:

```powershell
python audits/science/2026-09-16_dsd_gravity_gravitational_core_descriptor_gate.py --mode all
```
