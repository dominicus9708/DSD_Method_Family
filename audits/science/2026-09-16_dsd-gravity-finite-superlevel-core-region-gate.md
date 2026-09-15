# BH-GC-003 — Finite Superlevel Gravitational-Core Region Gate

**Date:** 2026-09-16  
**Project:** DSD gravity rebaseline  
**Branch:** side audit; does **not** replace canonical BH-RB-025  
**Status:** PASS_WITH_BOUNDARY

## Question

BH-GC-001 separated a tidal-core seed from the maximum-acceleration shell, and BH-GC-002 separated causal material/signal motion from descriptor-maximum motion.

This gate asks whether a **finite connected high-gravity region** is a better working gravitational-core descriptor than an isolated point maximum.

For an admitted observer/flow field \(u^\mu\) on an admitted spatial slice \(\Sigma_\tau\), let the local tidal-strength descriptor be \(\mathcal T_u(x,\tau)\). Define

\[
\boxed{
\mathcal K_{u,\lambda}(\tau)
=
\left\{
 x\in\Sigma_\tau:
 \mathcal T_u(x,\tau)\ge\lambda(\tau)
\right\}.
}
\]

The instantaneous gravitational-core candidates are the **connected components** of \(\mathcal K_{u,\lambda}\), not the point set of all local maxima alone.

## 1. Why a finite region is useful

A pointwise maximum can move, exchange dominance, split numerically under a small perturbation, or disappear during a temporarily flat/fluid-like state.

A connected superlevel component records a finite neighborhood in which the gravitational descriptor remains large.

Therefore the descriptor can represent

\[
K_1\cup K_2
\longrightarrow
K_3
\]

for merger and

\[
K_1
\longrightarrow
K_{1a}\cup K_{1b}
\]

for splitting without assuming a permanently preserved material ball.

This remains a **descriptor operation** until a causal material/signal lineage is independently supplied.

## 2. Numerical structural control

Use a positive 1D descriptor field made from two Gaussian peaks,

\[
\mathcal T(x,t)
=
\exp\!\left[-\frac{(x+d(t))^2}{2\sigma^2}\right]
+
\exp\!\left[-\frac{(x-d(t))^2}{2\sigma^2}\right],
\]

with

\[
\sigma=0.8,
\qquad
 d(t)=d_0-vt,
\qquad
 d_0=2,
\qquad
 v=0.4c.
\]

The underlying peak centers therefore move subluminally.

Choose the relative threshold

\[
\lambda(t)=\eta\max_x\mathcal T(x,t),
\qquad
\eta=0.5.
\]

At the separated snapshot \(d=2\), the superlevel set has two finite connected components,

\[
\mathcal K_{0.5}
\approx
[-2.9415,-1.0575]
\cup
[1.0575,2.9415].
\]

At the later snapshot \(d=1.2\), while the underlying center speed is still only \(0.4c\), the two regions have merged into

\[
\mathcal K_{0.5}
\approx
[-2.134,2.134].
\]

Thus a change in the number of connected gravitational-core regions is compatible with causal component motion.

## 3. Point-maxima noise test

Apply the bounded perturbation

\[
\mathcal T_{\rm pert}(x)
=
\mathcal T(x)
\left[1+0.02\sin(40x)e^{-x^2/18}\right].
\]

For the separated snapshot, the number of pointwise local maxima changes from

\[
2\to13,
\]

and for the merged snapshot from

\[
2\to21.
\]

Nevertheless, the number of connected \(\eta=0.5\) superlevel regions remains

\[
2\to2
\]

for the separated state and

\[
1\to1
\]

for the merged state.

The maximum numerical boundary shifts are only

\[
\Delta x_{\partial K}^{\rm sep}=0.021,
\qquad
\Delta x_{\partial K}^{\rm merge}=0.0125.
\]

Therefore the finite-region descriptor is substantially more robust than raw point-maxima counting in this control.

## 4. Positive-rescaling property

Because the threshold is defined as a fraction of the instantaneous maximum,

\[
\lambda=\eta\max\mathcal T,
\]

a positive overall rescaling

\[
\mathcal T\mapsto a\mathcal T,
\qquad a>0
\]

leaves \(\mathcal K_{u,\lambda}\) unchanged.

This is useful when only the relative shape of the admitted descriptor is intended to define the region.

It does **not** make the construction unique.

## 5. Threshold non-uniqueness firewall

A global relative threshold can hide a real but weaker separated component.

In the control

\[
\mathcal T(x)
=
G(x;-2,1.0)+G(x;+2,0.35),
\]

there are still two local maxima.

However,

\[
\eta=0.50
\]

produces only one connected superlevel component, whereas

\[
\eta=0.25
\]

recovers both components.

Therefore

\[
\boxed{
\text{connected superlevel core}
\text{ is more robust than a point maximum, but it is threshold-dependent.}
}
\]

The tuple

\[
\boxed{
(u,\Sigma_\tau,\mathcal T_u,\lambda)
}
\]

must remain part of the descriptor provenance.

## 6. Relativistic dynamic-core interpretation

The current working gravitational-core object is therefore not a unique point or a permanent solid sphere.

For each admitted \((u,\Sigma_\tau,\lambda)\), write

\[
\mathcal K_{u,\lambda}(\tau)
=
\bigsqcup_i K_i(\tau),
\]

where each \(K_i\) is a connected component.

The instantaneous state may have

\[
N_K(\tau)=0,1,2,\ldots
\]

components.

A DSD lineage record can then type separately:

\[
\Lambda_{\rm mat},
\quad
\Lambda_{\rm sig},
\quad
\Lambda_{\rm desc},
\quad
\Lambda_{\rm dom},
\quad
\Lambda_{\rm reg},
\]

where \(\Lambda_{\rm reg}\) records succession of finite descriptor regions.

Only material and signal continuations are required to form future-causal worldline/worldtube relations. Region-boundary motion or topology changes are not automatically matter or information transport.

## 7. Firewalls

The following identifications remain forbidden:

\[
\mathcal K_{u,\lambda}
\neq
\text{material support},
\]

\[
\partial\mathcal K_{u,\lambda}
\neq
\text{event horizon},
\]

\[
\mathcal K_{u,\lambda}
\neq
\{\mathcal C>1\},
\]

\[
\text{region merger/split}
\neq
\text{superluminal transport}.
\]

Also, the threshold \(\lambda\) must not be chosen after the fact to force a desired number or radius of cores.

## Result

The reproducibility script gives

\[
\boxed{20/20\ \mathrm{PASS}}.
\]

Final verdict:

\[
\boxed{
\begin{aligned}
&\text{PASS\_WITH\_BOUNDARY /}\\
&\text{FINITE\_CONNECTED\_SUPERLEVEL\_REGIONS\_ARE\_MORE\_ROBUST\_THAN\_POINT\_MAXIMA /}\\
&\text{CAUSAL\_COMPONENT\_MOTION\_CAN\_PRODUCE\_DESCRIPTOR\_REGION\_MERGER /}\\
&\text{THRESHOLD\_CHOICE\_IS\_NOT\_UNIQUE\_AND\_CAN\_HIDE\_WEAK\_CORES /}\\
&\text{CORE\_REGION\_DESCRIPTOR\_MUST\_RETAIN\_FLOW\_SLICE\_AND\_THRESHOLD\_PROVENANCE /}\\
&\text{PHYSICAL\_BLACK\_HOLE\_CORE\_REGION\_NOT\_DERIVED}.
\end{aligned}
}
\]

## Next side audit — BH-GC-004

Replace one arbitrary threshold by a **threshold filtration / persistence test**.

Study

\[
\left\{
\mathcal K_{u,\lambda}
\right\}_{\lambda}
\]

across a range of \(\lambda\), and identify components that persist across a nontrivial threshold interval.

The aim is to distinguish a stable gravitational-core feature from a threshold-specific or noise-specific feature without preselecting one privileged \(\lambda\).

This remains a descriptor audit, not a derivation of black-hole interior matter.

## Reproducibility

From the repository root:

```powershell
python audits/science/2026-09-16_dsd_gravity_finite_superlevel_core_region_gate.py --mode all
```
