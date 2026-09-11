# Structural Gravity Normalized-Pencil Invariant Obstruction Audit

```text
AUDIT_ID: DSD-SG-20260911-INVARIANT-001
STATUS: PASS_WITH_BOUNDARY / TARGET_SPECTRUM_UNIQUENESS_OPEN
DATE: 2026-09-11
DOMAIN: structural gravity / black-hole coefficient universality
```

## Question
If a common normalized strong-field target \(B_*\) is required, which invariants can obstruct convergence from source-dependent initial support pencils?

## Source boundary
Structural Reorganization Dynamics does not impose conservation generically. A conservation/redistribution law inside a regular epoch is an additional model condition, and status/domain/formation transitions require separate jump/balance rules when conservation across them is claimed. Therefore invariant preservation must be audited in each structural-gravity specialization rather than assumed.

## Control pencils
Reuse the three previous normalized 2-mode support controls:

\[
B_{\rm uniform}=\begin{pmatrix}1&-0.5\\-0.5&1\end{pmatrix},
\]

with core-heavy and envelope-heavy variants having different off-diagonal couplings.

The resulting invariants are:

| profile | tr \(B\) | det \(B\) | \(\lambda_{\min}\) | \(\lambda_{\max}\) |
|---|---:|---:|---:|---:|
| uniform | 2 | 0.75 | 0.5 | 1.5 |
| core-heavy | 2 | 0.880481632653 | 0.654285714286 | 1.34571428571 |
| envelope-heavy | 2 | 0.718190693878 | 0.469142857143 | 1.53085714286 |

Thus all three controls share the same trace but not determinant, Frobenius norm, or spectrum.

## Obstruction results

### Full-spectrum conservation
If the flow is isospectral, initially different spectra remain different. Therefore pure orthogonal reorientation cannot drive these controls to one common \(B_*\).

### Determinant conservation
A source-dependent conserved determinant partitions the states into different invariant leaves. Exact convergence to one matrix with one determinant is then impossible unless transitions or nonconservative dynamics change that invariant.

### Trace conservation
Trace conservation alone is **not** an obstruction here because all controls already satisfy

\[
\operatorname{tr}B=2.
\]

However, it also does not determine the target spectrum uniquely.

A trace-preserving isotropization gives

\[
B_*^{\rm iso}=I,
\qquad
\Psi_*=1,
\]

whereas a nonisotropic trace-preserving target can have

\[
B_*^{\rm aniso}=\operatorname{diag}(0.5,1.5),
\qquad
\Psi_*=0.5.
\]

Therefore the common trace does not select the earlier \(1/2\) toy value.

## Relaxation implication
A common-target relaxation can erase source-dependent determinant and spectral differences only because those quantities are not conserved by the control flow.

Thus the attractor program must explicitly identify which structural quantities are:

1. strictly conserved;
2. redistributed but globally constrained;
3. dissipative/nonconserved;
4. reset or changed at typed transitions.

## Main conclusion
The existence of a common attractor is not enough. Its **uniqueness and admissibility** depend on the surviving invariant set.

A necessary compatibility condition for a common target is:

\[
C_j[B(S_1,0)]=C_j[B(S_2,0)]
\]

for every invariant \(C_j\) that is exactly preserved throughout the relevant basin and transition chain.

If a source-dependent invariant survives, the basin splits and exact universal \(B_*\) is obstructed.

Generic DSD does not currently force such an obstructing invariant, but it also does not uniquely determine the target spectrum after the obstructions are removed.

## Audit result

```text
11/11 checks passed
PASS_WITH_BOUNDARY / TARGET_SPECTRUM_UNIQUENESS_OPEN
```

## Next target
Determine whether structural-gravity support dynamics supplies an independent target-selection principle after the invariant audit. In particular, test whether relaxation toward isotropy, fixed anisotropy, critical coupling, or transition-selected spectra follows from the actual support/reorganization bridge rather than from Schwarzschild matching.

## Reproduction

```bash
python audits/science/2026-09-11_structural_gravity_normalized_pencil_invariant_audit.py --mode all
```
