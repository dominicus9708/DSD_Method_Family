# DSD Gravity M/J/Q Bridge Gate Audit — BH-RB-002

Date: 2026-09-12

Status: **PASS_WITH_BOUNDARY / PHYSICAL_CHARGE_BRIDGE_REQUIRED**

## Purpose

Continue the active QM/relativity-based DSD gravity rebaseline after BH-RB-001.

The question is not yet which black-hole solution is correct. The question is which DSD records can legitimately receive external physical meanings such as mass-energy, momentum, angular momentum, charge, and stress without collapsing the typed structure or importing GR results as DSD primitives.

The discarded 2026-09-11 structural-gravity branch (`K_g`, `Theta_*`, `Psi_*`, normalized support pencils, target selection) is not used.

## Source constraints inherited from current DSD papers

The current DSD Property Axiom System retains the full ordered typed input of every defined property record. A property record may be unary, binary, higher-order, or mixed.

The static aggregation paper requires an explicit application-specific association rule before a multi-input property record can inform one formation channel. Later scalarization, contraction, constitutive interpretation, and empirical readout are additional maps rather than part of the abstract property structure.

The dynamics paper likewise states that a property label does not determine a mathematical coefficient or physical quantity by name alone. A constitutive dynamic bridge is required. Conservation is an additional model condition rather than a generic DSD consequence.

Therefore the physical bridge must be downstream and typed.

## Minimal physical matter bridge

Let the native typed property carrier be

\[
\mathcal R_A^{\rm prop}
=\{(\varpi,x,z):\varpi\in\Pi_A,\ x\in D_{A,\varpi},\ z=\Xi_{A,\varpi}(x)\}.
\]

A candidate physical bridge cannot be written as a bare relabeling `z -> mass`. It must have enough supplied relativistic/physical structure to identify localization, units, representation, and covariance. Schematically,

\[
B_{\rm MAT}^{R2/R4}:
(\mathcal I_{\rm DSD},X_{\rm REL},\mathcal U,\ell)
\rightharpoonup
\mathcal T_{\rm phys},
\]

where `X_REL` contains the supplied relativistic carrier, `ell` is a declared localization/association map, `U` denotes physical unit/interpretation data, and `T_phys` may contain stress-energy, currents, or other physical matter records.

This bridge is not part of generic DSD.

## Bridge admissibility conditions

1. **Defined-status gate** — undefined DSD records are not converted to numerical zero.
2. **Complete-input retention** — the full typed input profile is preserved unless an explicit coarse-graining map is declared.
3. **Explicit localization** — a DSD record is not assigned a spacetime event or slice by name alone.
4. **Unit/dimension declaration** — a dimensionless or abstract DSD value is not silently treated as kg, J, C, or angular momentum.
5. **Representation declaration** — scalar, vector, tensor, current, and density roles are supplied explicitly.
6. **Covariance/locality conditions** — imposed only when the physical specialization uses them.
7. **No hidden conservation** — `nabla_mu T^{mu nu}=0` or charge conservation is an external matter/GR compatibility condition unless separately derived.
8. **No hidden unary ownership** — multi-input properties are not allocated to a single channel without a declared association rule.
9. **No aggregate reconstruction claim** — equality of a reduced scalar aggregate does not reconstruct the component-resolved physical state.

## Scalar-mass collapse witness

After an external position/momentum specialization, consider two two-component states with the same scalar energy aggregate and zero total linear momentum.

State A uses tangential momenta:

\[
r_1=(1,0,0),\quad p_1=(0,1,0),
\]

\[
r_2=(-1,0,0),\quad p_2=(0,-1,0).
\]

Then

\[
P_{\rm tot}=0,\qquad J_z=2.
\]

State B uses radial momenta with the same energy proxy:

\[
r_1=(1,0,0),\quad p_1=(1,0,0),
\]

\[
r_2=(-1,0,0),\quad p_2=(-1,0,0),
\]

so

\[
P_{\rm tot}=0,\qquad J_z=0.
\]

Thus

\[
\boxed{E_{\rm agg}(A)=E_{\rm agg}(B)\;\not\Rightarrow\;J(A)=J(B)}.
\]

A scalar mass/energy readout alone therefore cannot decide whether the correct external comparator should be Schwarzschild-like or Kerr-like.

An analogous charge witness gives equal scalar energy with different total charge, so scalar energy does not determine `Q` either.

## Conservation independence witness

Two fully well-typed externally specialized snapshots can have different scalar energy totals while remaining type-correct. Therefore typing and status correctness alone do not imply a conservation equation.

This agrees with the current Structural Reorganization Dynamics rule that conservation or redistribution laws are additional model conditions.

## Important correction to the T_munu-first route

The active rebaseline had identified the DSD-to-`T_{mu nu}` bridge as the first matter interface to audit. This remains necessary for coupling ordinary matter to GR, but it is **not sufficient as a black-hole identity map**.

In an external vacuum black-hole region,

\[
T_{\mu\nu}=0
\]

can hold while the geometry still carries a nonzero mass and, for Kerr, angular momentum parameter.

Therefore the black-hole pipeline must distinguish local matter data from global geometric charges/boundary data:

\[
\mathcal I_{\rm DSD}
\xrightarrow{B_{\rm MAT}}
(T_{\mu\nu},j^\mu,\ldots)
\xrightarrow{\text{external matter+GR dynamics}}
(g_{\mu\nu},\text{boundary/asymptotic data})
\xrightarrow{Q_{\rm global}}
(M,J,Q,\ldots).
\]

The map `Q_global` is an external relativistic/global-charge construction, not a generic DSD aggregate.

## External black-hole horizon comparator

Once external physical charges are supplied, the Kerr-Newman family provides the parameterized comparator

\[
\chi=\frac{Jc}{GM^2},
\qquad
\hat q=\frac{Q}{\sqrt{4\pi\varepsilon_0G}\,M},
\]

with horizon-existence condition

\[
\chi^2+\hat q^2\le1.
\]

The outer horizon is

\[
r_+
=r_g\left(1+\sqrt{1-\chi^2-\hat q^2}\right),
\qquad
r_g=\frac{GM}{c^2}.
\]

For fixed mass and this external solution family,

\[
\boxed{r_g\le r_+\le2r_g}.
\]

For the Sgr A* mass benchmark used in BH-RB-001,

\[
r_g\approx6.34525\times10^6\ {\rm km},
\]

so the external Kerr-Newman horizon envelope is

\[
\boxed{
6.34525\times10^6\ {\rm km}
\le r_+\le
1.26905\times10^7\ {\rm km}
}.
\]

This interval is **not a DSD prediction**. It is the standard-GR comparator range left after `M` is fixed but `J` and `Q` are not yet supplied.

## Verdict

- property value by name -> physical mass/energy/momentum/charge: **FAIL**.
- explicit typed physical bridge: **REQUIRED**.
- scalar energy/mass aggregate -> angular momentum: **FAIL**.
- scalar energy/mass aggregate -> charge: **FAIL**.
- generic DSD typing -> conservation law: **FAIL**.
- `T_{mu nu}` bridge as matter interface: **NECESSARY BUT NOT SUFFICIENT FOR BLACK-HOLE IDENTITY**.
- separate global charge/boundary map `(g,boundary data) -> (M,J,Q)`: **REQUIRED FOR THE CURRENT BLACK-HOLE ROUTE**.
- external Kerr-Newman horizon envelope at fixed mass: **PASS AS R3/R4 COMPARATOR ONLY**.

## Next step

BH-RB-003 should audit the **mass/energy sector first**, because every Schwarzschild/Kerr/Kerr-Newman radius comparator requires `M`.

The key question is whether a DSD typed matter bridge can distinguish:

1. local matter energy density,
2. integrated matter energy on a supplied slice,
3. conserved total energy under a supplied matter law,
4. relativistic global mass such as an asymptotic/geometric charge,

without identifying these four levels by definition.

Only after this mass hierarchy is separated should `J` and `Q` be closed independently.

Reproduction script:

`audits/science/2026-09-12_dsd_gravity_mjq_bridge_gate_audit.py`
