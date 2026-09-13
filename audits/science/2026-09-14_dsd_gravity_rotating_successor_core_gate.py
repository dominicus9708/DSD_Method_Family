#!/usr/bin/env python3
"""
BH-RB-012 — Rotating successor-core scale / anisotropy gate.

Purpose:
- Open the J != 0 branch without deriving an interior black-hole core.
- Compare the Kerr horizon scale with two angular-momentum diagnostic scales:
    r_j    = j/c
    r_circ = j^2/(GM)
  where j = J/M = chi GM/c = chi r_g c.
- Audit directional centrifugal support with a Newtonian control
  f_rot(theta) = q sin^2(theta), q = r_circ/R.
- Compute the specific-angular-momentum threshold needed for external
  circularization, r_circ > r_+.

Important:
These are scale diagnostics / controls, not a relativistic interior equilibrium
solution and not a derivation of a finite black-hole core.
"""

from __future__ import annotations

import argparse
import math

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30
M_SGRA = 4.297e6 * M_SUN


def r_g(mass: float) -> float:
    return G * mass / C**2


def r_plus(mass: float, chi: float) -> float:
    rg = r_g(mass)
    return rg * (1.0 + math.sqrt(max(0.0, 1.0 - chi**2)))


def j_mean(mass: float, chi: float) -> float:
    return chi * G * mass / C


def r_j(mass: float, chi: float) -> float:
    return j_mean(mass, chi) / C


def r_circ(mass: float, chi: float) -> float:
    j = j_mean(mass, chi)
    return j * j / (G * mass)


def ell_threshold_for_external_circularization(chi_bh: float) -> float:
    """
    Dimensionless accretion specific angular momentum ell = j_acc/(r_g c).
    External circularization requires ell^2 r_g > r_+.
    """
    return math.sqrt(1.0 + math.sqrt(max(0.0, 1.0 - chi_bh**2)))


def directional_rotation_fraction(q: float, theta_deg: float) -> float:
    """
    Newtonian directional control:
      a_rot/a_g ~ q sin^2(theta)
    for a nearly spherical shell at fixed radius.
    theta=0 is the rotation axis; theta=90 deg is the equator.
    """
    th = math.radians(theta_deg)
    return q * math.sin(th) ** 2


def checks() -> list[tuple[str, bool]]:
    out: list[tuple[str, bool]] = []
    grid = [i / 1000 for i in range(1001)]

    identity_ok = True
    for chi in grid:
        s = math.sqrt(max(0.0, 1.0 - chi**2))
        lhs = chi**2 / (1.0 + s)
        rhs = 1.0 - s
        if abs(lhs - rhs) > 1e-12:
            identity_ok = False
            break
    out.append(("Kerr/rotation ratio identity", identity_ok))

    out.append((
        "BH-mean circularization scale never exceeds Kerr horizon",
        all(r_circ(M_SGRA, x) <= r_plus(M_SGRA, x) + 1e-6 for x in grid),
    ))

    out.append((
        "causal angular-momentum scale never exceeds Kerr horizon",
        all(r_j(M_SGRA, x) <= r_plus(M_SGRA, x) + 1e-6 for x in grid),
    ))

    out.append((
        "extremal equality r_circ = r_plus = r_g",
        abs(r_circ(M_SGRA, 1.0) - r_g(M_SGRA)) < 1e-6
        and abs(r_plus(M_SGRA, 1.0) - r_g(M_SGRA)) < 1e-6,
    ))

    out.append((
        "rotation vanishes on the axis in the directional control",
        abs(directional_rotation_fraction(0.8, 0.0)) < 1e-15,
    ))

    out.append((
        "rotation is maximal at the equator in the directional control",
        directional_rotation_fraction(0.8, 90.0)
        >= directional_rotation_fraction(0.8, 60.0)
        >= directional_rotation_fraction(0.8, 30.0)
        >= directional_rotation_fraction(0.8, 0.0),
    ))

    chi = 0.9
    ell_thr = ell_threshold_for_external_circularization(chi)
    rg = r_g(M_SGRA)
    rp = r_plus(M_SGRA, chi)
    out.append((
        "ell just above threshold circularizes outside horizon",
        ((1.01 * ell_thr) ** 2 * rg) > rp,
    ))
    out.append((
        "ell just below threshold circularizes inside horizon scale",
        ((0.99 * ell_thr) ** 2 * rg) < rp,
    ))

    q = r_circ(M_SGRA, chi) / rp
    out.append(("chi=0.9 horizon-scale equatorial q is sub-unity", 0.0 < q < 1.0))
    out.append(("chi=0.9 polar q remains zero", abs(directional_rotation_fraction(q, 0.0)) < 1e-15))

    out.append((
        "spinless limit removes rotational scales",
        r_circ(M_SGRA, 0.0) == 0.0 and r_j(M_SGRA, 0.0) == 0.0,
    ))

    out.append((
        "nonzero spin introduces nonzero angular-momentum scales",
        r_circ(M_SGRA, 0.5) > 0.0 and r_j(M_SGRA, 0.5) > 0.0,
    ))

    return out


def report() -> None:
    rg = r_g(M_SGRA)
    print("BH-RB-012 rotating successor-core scale / anisotropy gate")
    print("M = 4.297e6 Msun")
    print(f"r_g = {rg/1000:.6f} km")
    print()
    print("chi    r_+/r_g   r_j/r_g   r_circ/r_g   r_circ/r_+   ell_ext_threshold")
    for chi in (0.0, 0.3, 0.5, 0.7, 0.9, 0.99, 1.0):
        rp = r_plus(M_SGRA, chi)
        rj = r_j(M_SGRA, chi)
        rc = r_circ(M_SGRA, chi)
        print(
            f"{chi:4.2f}   {rp/rg:9.6f}   {rj/rg:8.6f}   "
            f"{rc/rg:11.6f}   {rc/rp:11.6f}   "
            f"{ell_threshold_for_external_circularization(chi):9.6f}"
        )

    chi = 0.9
    rp = r_plus(M_SGRA, chi)
    q = r_circ(M_SGRA, chi) / rp
    print()
    print("Directional rotation control for chi=0.9 evaluated at R=r_+:")
    print(f"q_equator = r_circ/r_+ = {q:.9f}")
    for theta in (0, 15, 30, 45, 60, 75, 90):
        print(f"theta={theta:2d} deg -> f_rot={directional_rotation_fraction(q, theta):.9f}")

    results = checks()
    passed = sum(ok for _, ok in results)
    print()
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"\n{passed}/{len(results)} checks PASS")
    if passed != len(results):
        raise SystemExit(1)

    print(
        "\nVERDICT: PASS_WITH_BOUNDARY / ROTATION_SCALE_IDENTIFIED / "
        "POLAR_SUPPORT_STILL_REQUIRED / FINITE_CORE_NOT_DERIVED"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all", "report"], default="all")
    _ = parser.parse_args()
    report()


if __name__ == "__main__":
    main()
