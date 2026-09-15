# BH-GC-002 — Dynamic Multi-Core Lineage / Causality Firewall Gate

**Date:** 2026-09-16  
**Project:** DSD gravity rebaseline  
**Branch:** side audit; canonical BH-RB-025 transport audit remains unchanged  
**Status:** PASS_WITH_BOUNDARY

## Question

BH-GC-001 replaced a permanent material-ball core with a dynamic gravitational-core descriptor based on local tidal-strength maxima, while retaining the maximum-acceleration radius only as a characteristic shell in sufficiently radial states.

The next problem is causality.

If a descriptor maximum moves, splits, merges, disappears, or becomes dominant elsewhere, does that motion have to satisfy the same speed bound as matter and information?

The answer is **no** unless the moving maximum is being used as a physical continuation worldline.

A descriptor maximum can move superluminally as a pattern, or the global argmax can jump discontinuously, without any material or information transport exceeding \(c\).

Therefore the lineage model must type these notions separately.

## 1. Four distinct motions

The following must not be identified:

\[
\boxed{
\text{material/component motion}
\neq
\text{signal/transport propagation}
\neq
\text{local descriptor-maximum continuation}
\neq
\text{global/pattern maximum motion}.
}
\]

For a physical material or signal continuation edge in a local relativistic chart, the separation must be future causal:

\[
c^2\Delta t^2-\Delta x^2\ge0,
\qquad
\Delta t\ge0.
\]

A descriptor-successor relation does not automatically carry this requirement because it may encode only a change in which feature is largest, rather than a transported entity.

## 2. Causal split control

Use units \(c=1\).

A parent event at

\[
O=(t,x)=(0,0)
\]

produces two child components with

\[
x_\pm(t)=\pm0.6t.
\]

At \(t=3\),

\[
x_\pm=\pm1.8.
\]

For either branch,

\[
\Delta t^2-\Delta x^2
=9-3.24
=5.76>0.
\]

Thus both physical continuation branches are timelike and causal.

This supplies a minimal lineage control for

\[
K_0\longrightarrow K_+\cup K_-.
\]

The split does not require a superluminal separation of matter.

## 3. Causal merger control

Conversely, two components starting at

\[
x_\pm(0)=\pm2.8
\]

and moving toward the origin with

\[
|v|=0.7c
\]

meet at \(t=4\).

For either branch,

\[
\Delta t^2-\Delta x^2
=16-7.84
=8.16>0.
\]

Hence

\[
K_1\cup K_2\longrightarrow K_3
\]

is compatible with causal component motion when the physical branches themselves remain inside the light cone.

## 4. Superluminal descriptor-pattern witness

Now consider two ordinary luminal scalar modes,

\[
\phi(x,t)
=
\cos[k_1(x-t)]
+
\cos[k_2(x+t)].
\]

Using the sum identity,

\[
\phi
=2
\cos\left[
\frac{k_1+k_2}{2}x
-
\frac{k_1-k_2}{2}t
\right]
\cos\left[
\frac{k_1-k_2}{2}x
-
\frac{k_1+k_2}{2}t
\right].
\]

The two factor-pattern velocities are

\[
v_{\rm slow}
=
\frac{k_1-k_2}{k_1+k_2}c,
\]

and

\[
\boxed{
v_{\rm fast}
=
\frac{k_1+k_2}{k_1-k_2}c.
}
\]

For

\[
k_1=1,
\qquad
k_2=0.8,
\]

this gives

\[
v_{\rm slow}=\frac19c,
\]

and

\[
\boxed{v_{\rm fast}=9c.}
\]

The underlying modes themselves still propagate only at \(\pm c\).

Therefore the motion of an interference fringe is not a material or information-carrying worldline.

This is a purely mathematical pattern-speed witness. It is not a claim that a black-hole tidal maximum actually follows this particular wave model.

Its role is narrower:

\[
\boxed{
\text{causal underlying fields}
\not\Rightarrow
\text{every derived extremum pattern moves at }\le c.
}
\]

## 5. Global argmax can jump without anything moving

Take two stationary local maxima at

\[
x_A=-10,
\qquad
x_B=+10.
\]

Let their amplitudes be

\[
A_A(t)=1-0.1t,
\qquad
A_B(t)=1+0.1t.
\]

Then

\[
t<0:
\operatorname{ArgMax}=\{A\},
\]

\[
t=0:
\operatorname{ArgMax}=\{A,B\},
\]

\[
t>0:
\operatorname{ArgMax}=\{B\}.
\]

No peak has travelled from \(A\) to \(B\).

If one nevertheless divides their separation by a very short comparison interval, e.g.

\[
\Delta t=0.02,
\qquad
\Delta x=20,
\]

then the apparent argmax-hop speed is

\[
\boxed{v_{\rm hop}=1000c.}
\]

The corresponding separation is spacelike:

\[
\Delta t^2-\Delta x^2
=0.0004-400<0.
\]

Therefore this hop must **not** be inserted into the lineage graph as a material or signal continuation edge.

It is a change in dominance of two already existing local features.

## 6. Common-past synchronization firewall

The amplitude crossing above does not require superluminal A-to-B communication.

A common event

\[
O=(-10,0)
\]

can send null signals to both

\[
A=(0,-10),
\qquad
B=(0,+10),
\]

because

\[
\Delta t^2-\Delta x^2
=100-100=0
\]

for both paths.

Thus two distant local structures can change in a coordinated way because of shared past data, without either being the causal source of the other at the moment their descriptor ranking changes.

This is exactly why a global maximum switch is not a propagation speed measurement.

## 7. Typed DSD lineage rule

The dynamic gravitational-core branch should therefore use typed lineage edges.

A minimal distinction is

\[
\Lambda_{\rm mat}
:
\text{material/component continuation},
\]

\[
\Lambda_{\rm sig}
:
\text{signal/transport continuation},
\]

\[
\Lambda_{\rm desc}
:
\text{descriptor-successor relation},
\]

\[
\Lambda_{\rm dom}
:
\text{dominance/argmax change}.
\]

Require

\[
\boxed{
\Lambda_{\rm mat},\Lambda_{\rm sig}
\Rightarrow
\text{future-causal edge}.
}
\]

Do **not** require a global argmax or pattern relation to define a causal worldline unless an independent physical transport identification has been supplied.

Therefore

\[
\boxed{
\Lambda_{\rm desc},\Lambda_{\rm dom}
\not\Rightarrow
\Lambda_{\rm mat}\text{ or }\Lambda_{\rm sig}.
}
\]

This prevents the DSD lineage record from accidentally turning a bookkeeping succession into superluminal matter or information transfer.

## 8. Consequence for the gravitational-core descriptor

BH-GC-001 defined, for a chosen admissible timelike flow \(u^\mu\),

\[
\mathfrak M_u(\tau)
=
\operatorname{LocMax}_x\mathcal T_u(x,\tau).
\]

BH-GC-002 now requires that this be treated as a **set-valued instantaneous descriptor**, not automatically as a collection of particle-like worldlines.

Between successive slices, one must separately ask:

1. does a local maximum admit a nearby causal continuation;
2. did one maximum bifurcate into two through a local causal event;
3. did two branches merge through a causal event;
4. did an unrelated maximum merely become dominant;
5. did an interference or descriptor pattern shift without carrying energy or information.

Thus a dynamic state can pass through

\[
\text{single core seed}
\rightarrow
\text{two causal descendant seeds}
\rightarrow
\text{fluid-like weak-maxima phase}
\rightarrow
\text{new dominant seed}
\]

without assigning one permanent material identity to the entire sequence.

## 9. Relevance to the black-hole interior hypothesis

The user's current hypothesis allows

\[
\text{condensed core}
\leftrightarrow
\text{multi-core state}
\leftrightarrow
\text{fluid-like state}
\leftrightarrow
\text{fragmented/re-formed state}.
\]

BH-GC-002 shows that this description is not automatically in conflict with the relativistic speed limit merely because the **location of a descriptor maximum** appears to move or jump faster than \(c\).

The causal requirement applies to the physical mechanisms underneath the descriptor:

\[
\boxed{
|v_{\rm matter}|<c,
\qquad
|v_{\rm signal}|\le c,
}
\]

while

\[
\boxed{
v_{\rm pattern}\text{ or argmax-hop speed need not obey the same bound.}
}
\]

This does not derive a black-hole interior multi-core state from GR or DSD. It only closes one logical causality loophole in the proposed descriptor language.

## 10. Firewalls

The following remain forbidden:

\[
\text{descriptor maximum motion}
=
\text{material motion},
\]

\[
\text{global argmax switch}
=
\text{signal propagation},
\]

\[
\text{superluminal pattern speed}
=
\text{superluminal information transfer},
\]

\[
\text{split/merge of maxima}
=
\text{physical split/merge without a causal constitutive solution}.
\]

Likewise, this side audit does not alter the separate BH-RB compactness, trapped-region, EOS, or transport results.

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
&\text{CAUSAL\_COMPONENT\_SPLIT\_AND\_MERGER\_ADMISSIBLE /}\\
&\text{DESCRIPTOR\_MAXIMUM\_OR\_INTERFERENCE\_PATTERN\_MAY\_MOVE\_SUPERLUMINALLY\_WITHOUT\_TRANSPORT /}\\
&\text{GLOBAL\_ARGMAX\_SWITCH\_IS\_NOT\_A\_PHYSICAL\_WORLDLINE /}\\
&\text{LINEAGE\_MUST\_TYPE\_CAUSAL\_CONTINUATION\_SEPARATELY\_FROM\_DESCRIPTOR\_SUCCESSION /}\\
&\text{BLACK\_HOLE\_INTERIOR\_MULTICORE\_DYNAMICS\_NOT\_DERIVED}.
\end{aligned}
}
\]

## Next side audit — BH-GC-003

A point maximum is still too fragile to serve as the complete physical core.

The next side audit should replace point seeds by finite connected **superlevel core regions**, for example

\[
\mathcal K_\lambda(\tau)
=
\left\{
x:\mathcal T_u(x,\tau)\ge\lambda(\tau)
\right\},
\]

and test whether connected components of \(\mathcal K_\lambda\) can provide a stable finite-support descriptor through motion, split, merger, temporary flattening, and small perturbations.

The audit should keep the threshold-selection rule non-circular and distinguish genuine component birth/death from noise-induced local extrema.

The canonical BH-RB-025 finite-relaxation transport audit remains a separate mainline task.

## Reproducibility

From the repository root:

```powershell
python audits/science/2026-09-16_dsd_gravity_dynamic_multicore_lineage_causality_gate.py --mode all
```
