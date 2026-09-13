#!/usr/bin/env python3
"""
BH-RB-013 — Polar-support closure gate for a rotating successor-core branch.

Purpose:
- Correct the over-strong inference that spatial/flow anisotropy from rotation
  automatically requires anisotropic material stress.
- Verify that direct centrifugal support vanishes on the rotation axis.
- Use the exact stationary-axisymmetric perfect-fluid Euler equation only as a
  standard-GR structural comparator.
- Use the Newtonian uniform-density Maclaurin spheroid as an analytic control
  showing that isotropic pressure can close the polar balance while rotation
  produces an oblate spatial configuration.

Important boundaries:
- The Maclaurin spheroid is a Newtonian control, NOT a black-hole interior model.
- Stationary rotating-star equilibrium is NOT assumed to extend through a trapped
  region or event horizon.
- This audit does not derive a finite black-hole core or its radius.

References used for the analytic controls:
- Paschalidis & Stergioulas, Living Reviews in Relativity 20, 7 (2017),
  "Rotating Stars in Relativity".
- Braviner & Ogilvie, MNRAS 441, 2321 (2014), Maclaurin-spheroid equilibrium.
- FLASH User's Guide, Maclaurin gravity test, for A1/A3 interior-potential
  coefficients (ultimately tracing to Chandrasekhar's ellipsoidal figures).
"""

from __future__ import annotations

import argparse
import math


SECULAR_MACLAURIN_LIMIT = 0.81267


def a1(e: float) -> float:
    """Maclaurin oblate-spheroid coefficient A1=A2."""
    if e == 0.0:
        return 2.0 / 3.0
    root = math.sqrt(1.0 - e * e)
    return root * math.asin(e) / e**3 - (1.0 - e * e) / e**2


def a3(e: float) -> float:
    """Maclaurin oblate-spheroid coefficient A3."""
    if e == 0.0:
        return 2.0 / 3.0
    root = math.sqrt(1.0 - e * e)
    return 2.0 / e**2 - 2.0 * root * math.asin(e) / e**3


def omega2_over_pi_g_rho(e: float) -> float:
    """Maclaurin equilibrium rotation law Omega^2/(pi G rho)."""
    if e == 0.0:
        return 0.0
    root = math.sqrt(1.0 - e * e)
    return (
        2.0 * root * (3.0 - 2.0 * e * e) * math.asin(e) / e**3
        - 6.0 * (1.0 - e * e) / e**2
    )


def polar_pressure_coeff(e: float) -> float:
    """
    Dimensionless central polar pressure load
      p_c / (pi G rho^2 a^2) = A3 * (c/a)^2 = A3(1-e^2)
    for the homogeneous Maclaurin control.
    """
    return a3(e) * (1.0 - e * e)


def equatorial_pressure_coeff(e: float) -> float:
    """
    Dimensionless central equatorial pressure load after centrifugal support:
      p_c/(pi G rho^2 a^2) = A1 - 1/2 Omega^2/(pi G rho).
    In Maclaurin equilibrium this equals the polar expression exactly.
    """
    return a1(e) - 0.5 * omega2_over_pi_g_rho(e)


def directional_rotation_fraction(q: float, theta_deg: float) -> float:
    """Newtonian directional control q sin^2(theta)."""
    th = math.radians(theta_deg)
    return q * math.sin(th) ** 2


def checks() -> list[tuple[str, bool]]:
    out: list[tuple[str, bool]] = []
    samples = (0.05, 0.10, 0.30, 0.60, 0.80, SECULAR_MACLAURIN_LIMIT, 0.90)

    out.append((
        "ellipsoid coefficients satisfy 2*A1 + A3 = 2",
        all(abs(2.0 * a1(e) + a3(e) - 2.0) < 1e-11 for e in samples),
    ))

    out.append((
        "Maclaurin rotation law equals 2[A1-(1-e^2)A3]",
        all(
            abs(
                omega2_over_pi_g_rho(e)
                - 2.0 * (a1(e) - (1.0 - e * e) * a3(e))
            ) < 1e-11
            for e in samples
        ),
    ))

    out.append((
        "isotropic central pressure closes polar/equatorial balance",
        all(
            abs(polar_pressure_coeff(e) - equatorial_pressure_coeff(e)) < 1e-11
            for e in samples
        ),
    ))

    out.append((
        "direct centrifugal support vanishes on the rotation axis",
        all(abs(directional_rotation_fraction(q, 0.0)) < 1e-15 for q in (0.1, 0.5, 1.0, 10.0)),
    ))

    out.append((
        "direct centrifugal support is nonzero away from the axis",
        directional_rotation_fraction(0.5, 45.0) > 0.0
        and directional_rotation_fraction(0.5, 90.0) > directional_rotation_fraction(0.5, 45.0),
    ))

    out.append((
        "polar pressure load remains positive through secularly stable Maclaurin branch",
        all(polar_pressure_coeff(e) > 0.0 for e in (0.0, 0.3, 0.6, 0.8, SECULAR_MACLAURIN_LIMIT)),
    ))

    out.append((
        "rotation can coexist with isotropic pressure and oblate geometry",
        omega2_over_pi_g_rho(0.8) > 0.0
        and math.sqrt(1.0 - 0.8**2) < 1.0
        and abs(polar_pressure_coeff(0.8) - equatorial_pressure_coeff(0.8)) < 1e-11,
    ))

    out.append((
        "nonrotating spherical limit recovered",
        abs(a1(0.0) - 2.0 / 3.0) < 1e-15
        and abs(a3(0.0) - 2.0 / 3.0) < 1e-15
        and omega2_over_pi_g_rho(0.0) == 0.0,
    ))

    return out


def report() -> None:
    print("BH-RB-013 polar-support closure gate")
    print("Newtonian Maclaurin control only; not a black-hole interior solution.")
    print()
    print("e       c/a       A1        A3        Omega^2/(piGrho)   Pc/(piG rho^2 a^2)")
    for e in (0.0, 0.3, 0.6, 0.8, SECULAR_MACLAURIN_LIMIT, 0.9, 0.92996):
        c_over_a = math.sqrt(1.0 - e * e)
        print(
            f"{e:0.5f}  {c_over_a:0.6f}  {a1(e):0.6f}  {a3(e):0.6f}  "
            f"{omega2_over_pi_g_rho(e):0.9f}         {polar_pressure_coeff(e):0.9f}"
        )

    e = SECULAR_MACLAURIN_LIMIT
    print()
    print("At the Maclaurin secular-instability threshold control e=0.81267:")
    print(f"c/a = {math.sqrt(1.0 - e*e):.9f}")
    print(f"Omega^2/(pi G rho) = {omega2_over_pi_g_rho(e):.9f}")
    print(f"polar central-pressure coefficient = {polar_pressure_coeff(e):.9f}")
    print("direct centrifugal polar term = 0 by axis regularity / sin^2(theta) control")

    results = checks()
    passed = sum(ok for _, ok in results)
    print()
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"\n{passed}/{len(results)} checks PASS")
    if passed != len(results):
        raise SystemExit(1)

    print(
        "\nVERDICT: PASS_WITH_BOUNDARY / DIRECT_POLAR_ROTATION_SUPPORT_ZERO / "
        "ISOTROPIC_PRESSURE_CAN_CLOSE_POLAR_BALANCE_IN_STATIONARY_CONTROL / "
        "TRAPPED_DYNAMIC_CORE_STILL_UNCLOSED"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all", "report"], default="all")
    _ = parser.parse_args()
    report()


if __name__ == "__main__":
    main()
