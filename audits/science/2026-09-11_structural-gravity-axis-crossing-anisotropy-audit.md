# Structural Gravity Axis-Crossing Anisotropy Audit

```text
AUDIT_ID: DSD-SG-20260911-BH-AXIS-CROSSING-ANISO-001
STATUS: PASS_WITH_NEGATIVE_RESULT / AXIS_GEOMETRY_ALONE_DOES_NOT_SELECT_HALF
DATE: 2026-09-11
DOMAIN: structural gravity / axis specialization / black-hole critical-radius benchmark
```

## 1. Question

Can the axis-crossing geometry retained by the DSD axis specialization independently select the normalized support anisotropy required for

\[
\Psi_*=\frac12
\]

without using the Schwarzschild coefficient?

## 2. Geometric input and support control

For two realized lines with projectors \(P_a,P_b\), use the unoriented rotation-invariant overlap

\[
s_{ab}=\operatorname{tr}(P_aP_b)=\cos^2\theta_{ab}.
\]

The normalized two-mode support control is

\[
B=
\begin{pmatrix}
1&-g\\
-g&1
\end{pmatrix},
\qquad
\Psi_*=1-|g|.
\]

A constitutive bridge is still required:

\[
g=\beta F(s_{ab}).
\]

The DSD axis-specialization notes already separate crossing geometry from dynamic coupling. Therefore neither \(F\) nor \(\beta\) is fixed by the geometric label alone.

## 3. Same geometry, different coupling laws

The following rotation-invariant controls are all admissible as mathematical maps of \(s\):

\[
F(s)=s,
\qquad
F(s)=1-s,
\qquad
F(s)=s(1-s),
\qquad
F(s)=1.
\]

At the same geometry

\[
s=\frac12
\quad(\theta=45^\circ),
\]

with \(\beta=1\), they give respectively

\[
\Psi_*=rac12,
\qquad
\frac12,
\qquad
\frac34,
\qquad
0.
\]

Hence

\[
\boxed{\text{same crossing geometry}\not\Rightarrow\text{same support spectrum}}.
\]

## 4. Coupling-scale degeneracy

For any geometry with \(F(s)\neq0\), the half coefficient can be forced by choosing

\[
\beta=\frac{1}{2F(s)}.
\]

For example, the symmetric mixing function \(F=s(1-s)\) is maximal at \(s=1/2\), but gives

\[
F=\frac14,
\qquad
\Psi_*=\frac34
\]

when \(\beta=1\).

Obtaining \(\Psi_*=1/2\) at the same geometry requires

\[
\beta=2.
\]

Therefore an unresolved coupling normalization can always manufacture the desired coefficient and must be determined independently.

## 5. Triadic closure boundary

The current axis-specialization record treats cyclic triadic closure as a geometric condition and explicitly separates closure satisfaction from dynamic support. The same closure geometry can receive stable or unstable constitutive bridges.

Therefore triadic closure or realized-axis rank cannot be used by itself to fix the normalized support Hessian or \(\Psi_*\).

## 6. Verdict

```text
PASS WITH NEGATIVE RESULT

CONFIRMED:
- s_ab is a legitimate rotation-invariant geometric input after the axis specialization is supplied;
- a geometry-to-coupling bridge can feed the support pencil;
- some explicit bridge choices can yield Psi_*=1/2.

REJECTED AS AN INDEPENDENT HALF SELECTOR:
- crossing geometry alone;
- a 45-degree crossing alone;
- triadic closure alone;
- realized-axis rank alone.

OPEN:
- an independently derived, source-independent map g=beta F(s);
- an independently derived geometry or state that fixes its input s;
- whether a multi-axis constitutive law produces a universal normalized anisotropy ratio.
```

## 7. Reproducibility

```bash
python audits/science/2026-09-11_structural_gravity_axis_crossing_anisotropy_audit.py --mode all
```

The audit returns 9/9 passing checks.

## 8. Next target

Search for a combined constitutive invariant rather than a purely geometric one. The next candidate should relate at least two of the following in one independently declared law:

- axis-crossing geometry;
- axial tension/prestress;
- restoration/stiffness block;
- load-direction operator;
- normalized generalized spectrum.

A successful blind half recovery requires the combined law to determine both the geometry-sensitive coupling and its normalization without referring to GR.