#!/usr/bin/env python3
"""
BH-RB-015 — Shape-floor / rotational-instability gate.

Purpose:
- Continue BH-RB-014 by asking whether a positive polar/equatorial aspect-ratio
  floor q = c/a can emerge without inserting q_min by hand.
- Use the classical homogeneous incompressible Maclaurin sequence only as a
  controlled external fluid benchmark.
- Convert the published secular and dynamical instability eccentricities into
  positive aspect-ratio floors for the *stable axisymmetric Maclaurin branch*.
- Combine those conditional q floors with the BH-RB-014 causal equatorial scale
  to obtain conditional 3D volume-equivalent radius floors.

Important boundaries:
- The Maclaurin spheroid is Newtonian, homogeneous, incompressible, uniformly
  rotating, and horizonless. It is NOT a black-hole interior model.
- Instability thresholds mark loss of stability of the axisymmetric branch.
  They do NOT prove that post-instability evolution preserves a positive c.
- In full GR and with differential rotation, the thresholds change and can be
  lower; no universal q_min is derived.
- Kerr r_+ is not identified with the material-core radius.
"""

from __future__ import annotations

import argparse
import math

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30
M_SGRA = 4.297e6 * M_SUN

KAPPA_UNIFORM_SPHEROID = 2.0 / 5.0

# External benchmark values from the classical Maclaurin sequence.
# Literature gives approximately e >= 0.8127 secularly unstable and
# e >= 0.9529 dynamically unstable.
E_SECULAR = 0.8127
E_DYNAMIC = 0.9529


def r_g(mass: float) -> float:
    return G * mass / C**2


def aspect_ratio_from_e(e: float) -> float:
    """For an oblate spheroid, q=c/a=sqrt(1-e^2)."""
    if not (0.0 <= e < 1.0):
        raise ValueError("e must lie in [0,1).")
    return math.sqrt(1.0 - e * e)


def rv_factor_from_q(q: float) -> float:
    """R_V/a = q^(1/3) for an oblate spheroid with c=q a."""
    if q < 0.0:
        raise ValueError("q must be nonnegative.")
    return q ** (1.0 / 3.0)


def causal_equatorial_scale_over_rg(
    chi: float,
    eta: float = 1.0,
    kappa: float = KAPPA_UNIFORM_SPHEROID,
) -> float:
    """
    BH-RB-014 control:
      eta = f_J/f_M
      a_causal/r_g = eta * chi/kappa.
    """
    if not (0.0 <= chi <= 1.0):
        raise ValueError("chi must lie in [0,1].")
    if eta < 0.0:
        raise ValueError("eta must be nonnegative.")
    if kappa <= 0.0:
        raise ValueError("kappa must be positive.")
    return eta * chi / kappa


def conditional_rv_floor_over_rg(
    chi: float,
    q_floor: float,
    eta: float = 1.0,
    kappa: float = KAPPA_UNIFORM_SPHEROID,
) -> float:
    """
    If a >= a_causal and independently q >= q_floor > 0, then
      R_V/r_g >= (eta chi/kappa) q_floor^(1/3).
    """
    return causal_equatorial_scale_over_rg(chi, eta, kappa) * rv_factor_from_q(q_floor)


def checks() -> list[tuple[str, bool]]:
    out: list[tuple[str, bool]] = []

    q_sec = aspect_ratio_from_e(E_SECULAR)
    q_dyn = aspect_ratio_from_e(E_DYNAMIC)

    out.append((
        "published instability eccentricities map to positive aspect ratios",
        q_sec > 0.0 and q_dyn > 0.0,
    ))

    out.append((
        "secular-stability floor is stricter than dynamical-stability floor",
        q_sec > q_dyn,
    ))

    out.append((
        "secular q floor matches benchmark",
        abs(q_sec - 0.582682) < 5e-6,
    ))

    out.append((
        "dynamical q floor matches benchmark",
        abs(q_dyn - 0.30328466825739814) < 1e-12,
    ))

    out.append((
        "finite q floor gives finite volume-radius factor",
        rv_factor_from_q(q_dyn) > 0.0 and rv_factor_from_q(q_sec) > 0.0,
    ))

    out.append((
        "q can approach zero kinematically if stability cutoff is removed",
        aspect_ratio_from_e(0.999999) < 0.002,
    ))

    out.append((
        "therefore positivity comes from branch-stability restriction, not spheroid kinematics alone",
        aspect_ratio_from_e(0.999999) < q_dyn < q_sec,
    ))

    chi = 0.9
    rv_dyn = conditional_rv_floor_over_rg(chi, q_dyn)
    rv_sec = conditional_rv_floor_over_rg(chi, q_sec)

    out.append((
        "conditional dynamic-stability 3D floor is positive",
        rv_dyn > 0.0,
    ))

    out.append((
        "conditional secular-stability 3D floor exceeds dynamic-stability floor",
        rv_sec > rv_dyn,
    ))

    out.append((
        "chi=0.9 dynamic-control coefficient matches benchmark",
        abs(rv_dyn - 1.5117013591221242) < 1e-12,
    ))

    out.append((
        "chi=0.9 secular-control coefficient matches benchmark",
        abs(rv_sec - 1.8791952533688725) < 2e-4,
    ))

    out.append((
        "reducing retained angular momentum fraction lowers the conditional radius floor linearly",
        abs(
            conditional_rv_floor_over_rg(chi, q_dyn, eta=0.5)
            - 0.5 * rv_dyn
        ) < 1e-12,
    ))

    out.append((
        "zero-spin limit removes the BH-RB-014 rotational radius floor",
        conditional_rv_floor_over_rg(0.0, q_dyn) == 0.0,
    ))

    return out


def report() -> None:
    q_sec = aspect_ratio_from_e(E_SECULAR)
    q_dyn = aspect_ratio_from_e(E_DYNAMIC)
    f_sec = rv_factor_from_q(q_sec)
    f_dyn = rv_factor_from_q(q_dyn)

    print("BH-RB-015 shape-floor / rotational-instability gate")
    print("Maclaurin spheroid = external Newtonian control only.")
    print()
    print("Published control thresholds:")
    print(f"e_secular  = {E_SECULAR:.7f} -> q_secular = c/a = {q_sec:.9f}")
    print(f"e_dynamic  = {E_DYNAMIC:.7f} -> q_dynamic = c/a = {q_dyn:.9f}")
    print(f"q_secular^(1/3) = {f_sec:.9f}")
    print(f"q_dynamic^(1/3) = {f_dyn:.9f}")
    print()
    print("Interpretation:")
    print("The stable axisymmetric Maclaurin branch terminates through")
    print("non-axisymmetric instability while c/a is still positive.")
    print("This is a conditional shape floor for that branch, not a universal GR q_min.")
    print()

    chi = 0.9
    rg = r_g(M_SGRA)
    rv_sec = conditional_rv_floor_over_rg(chi, q_sec)
    rv_dyn = conditional_rv_floor_over_rg(chi, q_dyn)
    print("BH-RB-014 + BH-RB-015 conditional control at chi=0.9, eta=1, kappa=2/5:")
    print(f"R_V,min(secular-stable)/r_g = {rv_sec:.9f}")
    print(f"R_V,min(dynamic-stable)/r_g = {rv_dyn:.9f}")
    print(f"Sgr A* scale secular control = {rv_sec*rg/1000:.6f} km")
    print(f"Sgr A* scale dynamic control = {rv_dyn*rg/1000:.6f} km")
    print()
    print("Firewall:")
    print("These numbers are NOT black-hole-core radius predictions.")
    print("They show only that once a positive q-floor is supplied by a specific")
    print("stable-fluid branch, BH-RB-014 converts it into a positive conditional 3D scale.")
    print("The post-instability branch must be evolved separately in GR.")

    results = checks()
    passed = sum(ok for _, ok in results)
    print()
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"\n{passed}/{len(results)} checks PASS")
    if passed != len(results):
        raise SystemExit(1)

    print(
        "\nVERDICT: PASS_WITH_BOUNDARY / "
        "POSITIVE_SHAPE_FLOOR_EXISTS_ON_STABLE_MACLAURIN_CONTROL / "
        "INSTABILITY_PREEMPTS_AXISYMMETRIC_Q_TO_ZERO / "
        "UNIVERSAL_GR_Q_MIN_NOT_DERIVED / "
        "POST_INSTABILITY_DYNAMIC_BRANCH_REQUIRED"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all", "report"], default="all")
    _ = parser.parse_args()
    report()


if __name__ == "__main__":
    main()
