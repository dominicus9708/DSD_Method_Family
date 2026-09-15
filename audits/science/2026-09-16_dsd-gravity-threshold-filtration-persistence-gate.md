# BH-GC-004 — Threshold-Filtration / Persistence Gravitational-Core Gate

**Date:** 2026-09-16  
**Project:** DSD gravity rebaseline  
**Branch:** side audit; does **not** replace canonical BH-RB-025 finite-relaxation transport audit  
**Status:** PASS_WITH_BOUNDARY

## Question

BH-GC-003 replaced point maxima by finite connected superlevel regions,

\[
\mathcal K_{u,\lambda}(\tau)
=\{x\in\Sigma_\tau:\mathcal T_u(x,\tau)\ge\lambda\},
\]

but showed that a single chosen threshold can hide a weaker core component.

BH-GC-004 therefore asks whether the **full superlevel filtration**

\[
\boxed{
\{\mathcal K_{u,\lambda}(\tau)\}_{\lambda}
}
\]

can provide a more robust gravitational-core descriptor without selecting one preferred \(\lambda\) in advance.

## 1. Superlevel filtration

For a fixed flow/slice pair \((u,\Sigma_\tau)\) and nonnegative descriptor \(\mathcal T_u\), define

\[
\mathcal K_{u,\lambda_2}(\tau)
\subseteq
\mathcal K_{u,\lambda_1}(\tau),
\qquad
\lambda_2>\lambda_1.
\]

As the threshold is lowered, connected components are born at local maxima and merge at lower descriptor levels.

The lifetime of a finite component is measured by

\[
\boxed{
\Pi=b-d
}
\]

where \(b\) is the descriptor value at birth and \(d\) is the merge/death level.

The surviving global component is kept explicitly separate as an **essential** class; it is not silently treated as an ordinary merger.

## 2. Control profile

Use the same deliberately non-black-hole 1D descriptor control as the previous side audit:

\[
\mathcal T(x)
=
\exp\!\left[-\frac{(x+d)^2}{2\sigma^2}\right]
+0.35\exp\!\left[-\frac{(x-d)^2}{2\sigma^2}\right],
\]

with

\[
\sigma=0.8,
\qquad d=2.
\]

A small multiplicative perturbation is added,

\[
\mathcal T_{\rm noisy}(x)
=
\mathcal T(x)
\left[
1+0.02\sin(40x)e^{-x^2/18}
\right].
\]

The descriptor is normalized by its instantaneous maximum before persistence is compared. This makes the control invariant under a positive overall amplitude rescaling while preserving relative shape information.

## 3. Point maxima versus persistent components

The clean profile has two point maxima.

The noisy profile has **13** point maxima, so the pointwise seed count is strongly noise-sensitive.

However, 0D superlevel persistence gives two dominant classes:

\[
\Pi_{\rm strong}\approx0.999999,
\]

for the essential strong component, and

\[
\boxed{
\Pi_{\rm weak}\approx0.298897
}
\]

for the weaker finite component.

The largest noise-only persistence is only

\[
\Pi_{\rm noise,max}\approx0.0195133.
\]

Hence the control has a persistence gap

\[
\boxed{
\frac{\Pi_{\rm weak}}{\Pi_{\rm noise,max}}
\approx15.32.
}
\]

So a weak but coherent gravitational-core feature can remain clearly separated from many small descriptor maxima even when a single high superlevel threshold would miss it.

## 4. No universal persistence cutoff is derived

For this synthetic control only, a demonstration cutoff

\[
\tau_\Pi=0.10
\]

retains the two salient classes and rejects all noise-only finite classes.

This does **not** derive a universal DSD or black-hole constant.

The correct interpretation is

\[
\boxed{
\text{single-}\lambda\text{ arbitrariness is reduced, but a significance convention remains.}
}
\]

Therefore the persistence cutoff, if used, must retain provenance and may need to come from physical resolution, uncertainty, a constitutive scale, or an independently specified model-selection rule.

## 5. Dynamic merger control

The two Gaussian descriptor sources are then brought together while their underlying component-center motion remains subluminal.

The secondary persistence evolves as

\[
\begin{array}{c|c|c}
 d & \text{point maxima} & \Pi_{\rm secondary}\\
\hline
2.0 & 2 & 0.299363\\
1.5 & 2 & 0.157743\\
1.2 & 2 & 0.020291\\
1.0 & 1 & 0\\
0.8 & 1 & 0
\end{array}
\]

Thus the weaker component loses persistence continuously before the descriptor becomes single-peaked.

This supplies a useful description of merger:

\[
\boxed{
\text{two persistent gravitational-core features}
\rightarrow
\text{weakening secondary feature}
\rightarrow
\text{one persistent feature}
}
\]

without making the persistence class into a material worldline.

## 6. DSD lineage refinement

The side-audit lineage vocabulary can now distinguish:

\[
\Lambda_{\rm mat}:
\text{material continuation},
\]

\[
\Lambda_{\rm sig}:
\text{signal/transport continuation},
\]

\[
\Lambda_{\rm desc}:
\text{descriptor succession},
\]

\[
\Lambda_{\rm dom}:
\text{dominance/argmax change},
\]

\[
\Lambda_{\rm reg}:
\text{finite superlevel-region continuation},
\]

and now

\[
\boxed{
\Lambda_{\rm pers}:
\text{persistent-feature continuation across threshold filtrations}.
}
\]

Only \(\Lambda_{\rm mat}\) and \(\Lambda_{\rm sig}\) automatically require a future-causal physical edge. Descriptor-, region-, and persistence-lineage are structural relations until an independent material/transport bridge is supplied.

## 7. Required provenance

A persistence-based gravitational-core description must retain at least

\[
\boxed{
(u,\Sigma_\tau,\mathcal T_u,\text{normalization},\text{filtration rule},\tau_\Pi)
}
\]

where applicable.

Changing the flow field, slice, descriptor, normalization, or significance rule can change the persistence structure. Therefore none may be hidden in an allegedly unique invariant core definition.

## 8. Firewalls

The following implications remain forbidden:

\[
\text{persistent descriptor feature}
\not\Rightarrow
\text{persistent material object},
\]

\[
\text{persistent descriptor feature}
\not\Rightarrow
\text{event horizon or trapped surface},
\]

\[
\text{persistence merger}
\not\Rightarrow
\text{matter merger unless independently bridged},
\]

\[
\text{large persistence}
\not\Rightarrow
\text{physical black-hole core existence}.
\]

The method reduces threshold arbitrariness; it does not derive the physical descriptor \(\mathcal T_u\), preferred flow \(u\), black-hole interior solution, or unique significance scale.

## Result

The reproducibility audit gives

\[
\boxed{21/21\ \mathrm{PASS}}.
\]

Final verdict:

\[
\boxed{
\begin{aligned}
&\text{PASS\_WITH\_BOUNDARY /}\\
&\text{FULL\_SUPERLEVEL\_FILTRATION\_REDUCES\_SINGLE\_THRESHOLD\_ARBITRARINESS /}\\
&\text{PERSISTENT\_COMPONENTS\_SEPARATE\_SALIENT\_CORES\_FROM\_SMALL\_NOISE\_MAXIMA\_IN\_CONTROL /}\\
&\text{PERSISTENCE\_CAN\_TRACK\_MERGER\_WITHOUT\_DEFINING\_A\_MATERIAL\_WORLDLINE /}\\
&\text{SIGNIFICANCE\_CUTOFF\_AND\_FLOW\_SLICE\_DESCRIPTOR\_PROVENANCE\_REMAIN\_REQUIRED /}\\
&\text{PHYSICAL\_BLACK\_HOLE\_CORE\_TOPOLOGY\_NOT\_DERIVED}.
\end{aligned}
}
\]

## Next side audit — BH-GC-005

Test whether the persistence construction remains stable under changes of spatial resolution and finite measurement/coarse-graining scale.

The next gate should distinguish:

\[
\text{physical splitting/merger}
\quad\text{from}\quad
\text{resolution-induced splitting/merger}.
\]

A core descriptor that changes its component count merely because the sampling scale changes is not yet suitable for a physical black-hole interpretation.

## Reproducibility

From the repository root:

```powershell
python audits/science/2026-09-16_dsd_gravity_threshold_filtration_persistence_gate.py --mode all
```
