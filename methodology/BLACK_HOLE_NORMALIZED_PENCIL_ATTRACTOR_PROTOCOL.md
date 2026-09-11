# Black-Hole Normalized Support-Pencil Attractor Protocol

```text
PROTOCOL_ID: DSD-METHOD-20260911-BH-ATTRACTOR-001
STATUS: ACTIVE_DRAFT
DATE: 2026-09-11
DOMAIN: structural gravity / critical-radius universality
```

## 1. Purpose
The preceding critical-radius work reduced the coefficient-universality problem to the normalized spectral quantity

\[
B(S,t)=L(S,t)^{-1/2}H_0(S,t)L(S,t)^{-1/2},
\qquad
\Psi_*(S,t)=\lambda_{\min}B(S,t).
\]

This protocol tests whether DSD-style dynamics can make distinct source states approach one normalized strong-field class.

## 2. Source discipline
Structural Reorganization Dynamics distinguishes transport, coupling, relaxation/restoration, source terms, transitions, and optional realized-axis reorientation. These mechanisms are not interchangeable and require explicit constitutive bridges. No generic monotonicity or relaxation stability is supplied.

Therefore no mechanism is credited with attractor behavior merely because it changes the state.

## 3. Mechanism classification
- **Transport:** changes location/support; does not by itself contract normalized spectral differences.
- **Axis reorientation:** orthogonal/projector commutator evolution can be isospectral; not an erasure mechanism by itself.
- **Coupling:** mixes components but has no generic dissipative sign.
- **Relaxation/restoration:** the only existing DSD dynamic slot that can directly host a contractive common-target law, provided stability is separately imposed.
- **Source/forcing:** must be tracked separately; persistent source-dependent forcing can obstruct exact universality.
- **Transitions:** may reset domains/status/formation and require separate transition relations; they cannot be hidden inside a regular relaxation equation.

## 4. Canonical attractor candidate
Use

\[
\Delta_B=B-B_*.
\]

A minimal regular-epoch specialization is

\[
\dot\Delta_B=-\mathcal R_B\Delta_B+F_{\rm res}.
\]

For the scalar-rate control

\[
\mathcal R_B=\gamma I,
\qquad \gamma>0,
\qquad F_{\rm res}=0,
\]

one has

\[
\Delta_B(t)=e^{-\gamma(t-t_0)}\Delta_B(t_0).
\]

Hence

\[
\|B(t)-B_*\|_2
\le
 e^{-\gamma(t-t_0)}\|B(t_0)-B_*\|_2
\]

and

\[
|\Psi_*(t)-\Psi_*|
\le
 e^{-\gamma(t-t_0)}\|B(t_0)-B_*\|_2.
\]

## 5. Minimal sufficient bridge package
For exact normalized coefficient universality in this branch, require at least:

1. a common normalized target \(B_*\), or a target orbit with the same generalized spectrum;
2. a uniformly coercive/contractive relaxation operator on the admitted basin;
3. asymptotically vanishing or source-independent normalized forcing/residuals;
4. transition rules that preserve the basin or map all admitted pre-transition states into a common post-transition class;
5. declared norm/carrier and well-posedness conditions.

## 6. Anti-overclaim rules
Do not infer:

- a common target from the existence of relaxation terms;
- stability from a restoration-like property label;
- spectral contraction from transport;
- detail erasure from axis reorientation;
- universality from one source profile;
- \(\Psi_*=1/2\) from Schwarzschild matching.

## 7. Falsification conditions
This attractor route fails for exact coefficient universality if any of the following persists in the normalized strong-field limit:

\[
B_{*,S_1}\neq B_{*,S_2}
\]

with different minimum eigenvalues,

\[
F_{{\rm res},S}(t)\not\to F_*
\]

or the relaxation operator loses coercivity/contractivity on a relevant source class.

## 8. Current result
The control audit shows:

- orthogonal reorientation preserves the initial \(\Psi_*\) differences;
- common-target stable relaxation contracts them exponentially;
- source-dependent targets preserve nonzero asymptotic spread;
- persistent source-dependent forcing produces asymptotic offsets.

Current verdict:

```text
PASS_WITH_BOUNDARY / COMMON_RELAXATION_TARGET_REQUIRED
```

This is a viable specialization path, not yet a physical derivation of the black-hole universal coefficient.

## 9. Invariant compatibility / 불변량 호환성
A common attractor is possible only if every exactly preserved invariant is compatible across all admitted source states.

For an invariant family \(C_j[B]\), exact convergence to one target requires

\[
C_j[B(S_1,0)]=C_j[B(S_2,0)]=C_j[B_*]
\]

for every \(C_j\) preserved through the entire regular epoch and transition chain.

The control audit found:

- the three radial-profile pencils share \(\operatorname{tr}B=2\);
- they have different determinants, Frobenius norms, and spectra;
- therefore exact determinant conservation or isospectral evolution would obstruct one common \(B_*\);
- trace conservation alone does not obstruct a common target, but it does not determine the target spectrum uniquely.

A trace-preserving isotropization of the controls gives

\[
B_*^{\rm iso}=I,
\qquad
\Psi_*=1,
\]

whereas a trace-preserving nonisotropic target can have

\[
B_*^{\rm aniso}=\operatorname{diag}(0.5,1.5),
\qquad
\Psi_*=0.5.
\]

Therefore a common trace or a generic tendency toward isotropy is insufficient to select the earlier \(1/2\) control value.

Structural Reorganization Dynamics supplies no generic conservation law; conservation/redistribution is an additional model condition. The structural-gravity specialization must therefore classify each candidate invariant as conserved, redistributed, dissipative, or transition-reset.

Current invariant-audit verdict:

```text
PASS_WITH_BOUNDARY / TARGET_SPECTRUM_UNIQUENESS_OPEN
```

## 10. Next target
After mechanism and invariant audits, the unresolved problem is target selection itself.

Test whether the actual structural-support/reorganization bridge independently selects:

1. isotropic relaxation;
2. a fixed anisotropic spectrum;
3. a critical-coupling spectrum;
4. a transition-selected spectrum;
5. or no universal spectrum at all.

The target minimum eigenvalue must be obtained without importing the Schwarzschild coefficient.

## 11. Reproduction

```bash
python audits/science/2026-09-11_structural_gravity_normalized_pencil_attractor_audit.py --mode all
python audits/science/2026-09-11_structural_gravity_normalized_pencil_invariant_audit.py --mode all
```
