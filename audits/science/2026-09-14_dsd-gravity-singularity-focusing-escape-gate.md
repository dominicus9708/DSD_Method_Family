# BH-RB-010 — Singularity focusing / finite-core escape-condition gate

**Date:** 2026-09-14  
**Project:** DSD gravity rebaseline  
**Author:** Kwon Dominicus  
**Verdict:** `PASS_WITH_BOUNDARY / FOCUSING_GATE_IDENTIFIED / FINITE_CORE_NOT_DERIVED`

## 1. Scope

This audit continues BH-RB-009 without restoring any discarded structural-gravity equation or coefficient.

The question is narrowed to standard general relativity:

> After a finite three-dimensional material support has entered a trapped region with positive areal radius, what does classical GR actually force, and which hypothesis must change if a future-complete finite-radius core or a trapped-to-untrapped bounce is to occur?

This is not yet a constitutive model for the hypothesized re-formed black-hole core.

## 2. Central distinction

The modern Penrose singularity theorem does **not** conclude that a material body becomes a zero-dimensional point or that its support radius obeys `R -> 0`.

Under its standard hypotheses — null convergence, a non-compact Cauchy hypersurface, and a closed future-trapped surface — it concludes the existence of future-incomplete null geodesics.

Therefore the following implication is forbidden:

\[
\text{null geodesic incompleteness}
\not\Rightarrow
\text{material support radius }R=0.
\]

The singularity theorem is an incompleteness theorem, not a theorem of zero-dimensional matter ontology.

## 3. Null Raychaudhuri gate

For an affinely parametrized, hypersurface-orthogonal null congruence in 3+1 dimensions,

\[
\frac{d\theta}{d\lambda}
=
-\frac12\theta^2
-\sigma_{ab}\sigma^{ab}
-R_{ab}k^ak^b.
\]

For null normals generated orthogonally from a spacelike two-surface, the twist vanishes.

If the null convergence condition holds,

\[
R_{ab}k^ak^b\ge0,
\]

then, because \(\sigma_{ab}\sigma^{ab}\ge0\),

\[
\frac{d\theta}{d\lambda}
\le
-\frac12\theta^2.
\]

For an initially negative expansion \(\theta_0<0\), focusing occurs no later than

\[
\Delta\lambda_{\rm focus}
\le
\frac{2}{|\theta_0|}.
\]

The audit script checks the dimensionless examples

\[
\theta_0=-0.5,-1,-2
\quad\Rightarrow\quad
\Delta\lambda_{\rm focus}\le4,2,1.
\]

## 4. Direct trapped-to-untrapped bounce

A local reversal of the same outgoing null congruence from trapped to untrapped requires its negative expansion eventually to increase toward and through zero.

For the twist-free Raychaudhuri equation, null convergence forbids this local defocusing because all terms on the right-hand side are non-positive.

For example, with

\[
\theta=-1,
\qquad
\sigma_{ab}\sigma^{ab}=0.04,
\]

a target

\[
\frac{d\theta}{d\lambda}=+0.1
\]

requires

\[
R_{ab}k^ak^b=-0.64<0.
\]

Within Einstein GR, contraction with a null vector removes both the trace term and the cosmological-constant term, so

\[
R_{ab}k^ak^b
=
\frac{8\pi G}{c^4}T_{ab}k^ak^b.
\]

Hence direct local null defocusing of this type requires violation of the null convergence condition and, under the Einstein equation, the corresponding null energy condition, unless one of the congruence assumptions being used no longer applies.

This conclusion must not be confused with a reversal of the material worldlines themselves.

## 5. Matter bounce is not causal untrapping

Pressure gradients can accelerate matter worldlines and can, in principle, reverse contraction of matter variables.

That statement is logically weaker than saying that the surrounding outgoing null expansion becomes positive.

Thus

\[
\boxed{
\text{matter bounce}
\neq
\text{trapped-to-untrapped null defocusing}
}
\]

and the two gates must be audited separately.

A known singularity-free perfect-fluid GR example reviewed by Senovilla contracts, rebounds and re-expands because of pressure-gradient acceleration while satisfying strong curvature/energy conditions; it avoids the relevant singularity theorem because another theorem hypothesis fails. This is a useful proof-of-principle that 'bounce' and 'energy-condition violation' are not universal synonyms. It is not a black-hole interior model and is not imported as the DSD core solution.

## 6. Branch classification after BH-RB-009

### A. Continued trapped collapse

If all Penrose hypotheses remain in force,

\[
\text{NCC}
+
\text{non-compact Cauchy hypersurface}
+
\text{closed future-trapped surface},
\]

then future null geodesic incompleteness follows.

This branch remains compatible with `R -> 0` models such as the idealized Oppenheimer-Snyder endpoint, but the theorem itself does not derive `R -> 0`.

### B. Matter-radius bounce at \(R_{\min}>0\)

A reversal of the material support radius

\[
\dot R<0
\to
\dot R=0
\to
\dot R>0
\]

is not ruled out solely by the null Raychaudhuri inequality because matter worldlines need not be null geodesics and may be accelerated by pressure/stress gradients.

However, such a bounce does not automatically remove the trapped causal structure.

### C. Trapped-to-untrapped bounce

For the same twist-free null congruence, a local increase of negative null expansion is blocked by the NCC Raychaudhuri gate.

A genuine causal untrapping branch therefore needs at least one relevant assumption to fail or change. In Einstein GR the most direct local route is `T_ab k^a k^b < 0`, i.e. NEC violation; other routes concern the global/causal hypotheses rather than a local positive-energy defocusing force.

### D. Future-complete finite trapped core

A core may be hypothesized to retain

\[
R_{\rm core}\ge R_{\min}>0
\]

while remaining inside a trapped region.

But a future-complete nonsingular realization cannot simultaneously retain every Penrose hypothesis. At least one of the following must fail or cease to apply:

1. null convergence / corresponding NEC under Einstein dynamics;
2. existence of the relevant non-compact Cauchy hypersurface / global-hyperbolic structure;
3. persistence of the closed future-trapped-surface hypothesis in the required form;
4. another technical hypothesis of the theorem formulation being invoked.

If none fails, the finite-radius core can still coexist with geodesic incompleteness, but then it has not resolved the classical singularity problem.

## 7. Standard-GR regular black-hole comparator

The literature contains nonsingular or regular-center black-hole geometries constructed within Einstein GR with special matter sectors. They are not generic and their energy conditions and global causal structures differ model by model.

A 2021 review by Maeda emphasizes this non-generic status and shows that some candidate geometries fail standard energy-condition criteria while some other spherical examples can satisfy the dominant energy condition. This is evidence only that Einstein equations do not algebraically identify 'black hole' with 'zero-dimensional material point'. It is **not** evidence that the present finite-support successor core has been physically derived or that realistic stellar collapse forms one.

## 8. DSD provenance firewall

The results in Sections 2–7 are external standard-GR results and theorem logic (`R2–R4` in the active provenance ladder).

No DSD structural entropy, rank law, old `K_g`, support threshold, or discarded structural-gravity coefficient is used.

DSD contributes only the bookkeeping distinction that must be preserved later:

\[
\text{formation transition}
\neq
\text{spatial-dimensional collapse}
\neq
\text{describability collapse}.
\]

No new gravitational law is inferred from that distinction here.

## 9. Audit result

The executable gate performs 12 algebraic/logical checks:

- three focusing-bound checks;
- four monotonic-focusing checks under NCC;
- two positive-defocusing / negative-`R_kk` checks;
- three Penrose-hypothesis logic checks.

Expected result:

```text
checks: 12/12 PASS
VERDICT: PASS_WITH_BOUNDARY / FOCUSING_GATE_IDENTIFIED / FINITE_CORE_NOT_DERIVED
```

## 10. Consequence for the next stage

The search has narrowed to two distinct unknowns rather than one:

\[
\boxed{
\text{(i) Can the re-formed material support reach }R_{\min}>0?
}
\]

and

\[
\boxed{
\text{(ii) If yes, does the spacetime remain trapped/incomplete, or which standard-GR theorem hypothesis changes?}
}
\]

The next audit should therefore build the weakest possible constitutive stress model for the successor core, without assuming a desired minimum radius, and test separately:

- material support bounce;
- energy conditions;
- causality / characteristic speeds;
- null-expansion behavior;
- global completeness status.

## References

- J. M. M. Senovilla, *A critical appraisal of the singularity theorems*, Phil. Trans. R. Soc. A 380 (2022), DOI: 10.1098/rsta.2021.0174, arXiv:2108.07296.
- S. Kar and S. SenGupta, *The Raychaudhuri equations: a brief review*, Pramana 69 (2007), arXiv:gr-qc/0611123.
- H. Maeda, *Quest for realistic non-singular black-hole geometries: Regular-center type*, arXiv:2107.04791.
