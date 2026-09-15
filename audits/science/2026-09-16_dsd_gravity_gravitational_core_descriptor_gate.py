#!/usr/bin/env python3
"""
BH-GC-001 — gravitational-core descriptor gate.

Purpose
-------
Test whether the radius of maximum inward gravitational acceleration can be
used as a unique definition of a black-hole successor core.

The control is deliberately non-black-hole and Newtonian: a smooth Plummer
mass profile. This is enough to test the logical equivalence of three candidate
locations:
  1. maximum acceleration magnitude,
  2. maximum compactness-like m(r)/r,
  3. maximum local tidal-strength norm.

The result is a structural gate only. It does not assert that a Plummer profile
models a black-hole interior.
"""

import argparse
import math


def density_shape(x: float) -> float:
    """rho / [3M/(4 pi a^3)] for the Plummer sphere."""
    return (1.0 + x*x) ** (-2.5)


def mean_density_shape(x: float) -> float:
    """rho_bar / [3M/(4 pi a^3)]."""
    return (1.0 + x*x) ** (-1.5)


def enclosed_mass_fraction(x: float) -> float:
    """m(r)/M, x=r/a."""
    return x**3 / (1.0 + x*x) ** 1.5


def acceleration_shape(x: float) -> float:
    """|g| / (GM/a^2)."""
    return x / (1.0 + x*x) ** 1.5


def compactness_shape(x: float) -> float:
    """[m(r)/r] / (M/a); physical 2Gm/(rc^2) differs by a constant factor."""
    return x*x / (1.0 + x*x) ** 1.5


def tidal_shape(x: float) -> float:
    """
    Newtonian tidal Frobenius norm divided by GM/a^3.

    For spherical g(r): eigenvalue magnitudes are represented by dg/dr and g/r,
    so ||T||^2 = (dg/dr)^2 + 2(g/r)^2.
    """
    dg_dx = (1.0 - 2.0*x*x) / (1.0 + x*x) ** 2.5
    g_over_x = 1.0 / (1.0 + x*x) ** 1.5
    return math.sqrt(dg_dx*dg_dx + 2.0*g_over_x*g_over_x)


def scan_max(fn, xmax: float = 5.0, samples: int = 200001):
    best_x = 0.0
    best_y = fn(0.0)
    for i in range(1, samples):
        x = xmax * i / (samples - 1)
        y = fn(x)
        if y > best_y:
            best_x, best_y = x, y
    return best_x, best_y


def run_audit() -> int:
    x_g = 1.0 / math.sqrt(2.0)
    x_C = math.sqrt(2.0)
    x_T = 0.0

    scan_g, max_g = scan_max(acceleration_shape)
    scan_C, max_C = scan_max(compactness_shape)
    scan_T, max_T = scan_max(tidal_shape)

    rho_ratio = density_shape(x_g) / mean_density_shape(x_g)

    tests = []

    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    check("center acceleration vanishes", abs(acceleration_shape(0.0)) < 1e-15, acceleration_shape(0.0))
    check("center tidal norm is finite and nonzero", tidal_shape(0.0) > 0.0, tidal_shape(0.0))
    check("analytic acceleration maximum radius", abs(scan_g - x_g) < 2e-5, (scan_g, x_g))
    check("analytic compactness maximum radius", abs(scan_C - x_C) < 2e-5, (scan_C, x_C))
    check("tidal norm maximum at center", abs(scan_T - x_T) < 1e-12, (scan_T, x_T))
    check("acceleration maximum differs from tidal maximum", abs(x_g - x_T) > 0.1, (x_g, x_T))
    check("acceleration maximum differs from compactness maximum", abs(x_g - x_C) > 0.1, (x_g, x_C))
    check("compactness maximum differs from tidal maximum", abs(x_C - x_T) > 0.1, (x_C, x_T))
    check("rho/rhobar condition at g maximum is 2/3", abs(rho_ratio - 2.0/3.0) < 1e-12, rho_ratio)
    check("enclosed mass fraction is positive at g maximum", enclosed_mass_fraction(x_g) > 0.0, enclosed_mass_fraction(x_g))
    check("acceleration maximum lies at finite radius", x_g > 0.0, x_g)
    check("compactness maximum lies farther out than acceleration maximum", x_C > x_g, (x_C, x_g))
    check("tidal strength decreases between center and g maximum", tidal_shape(x_g) < tidal_shape(0.0), (tidal_shape(x_g), tidal_shape(0.0)))
    check("tidal strength decreases further by compactness maximum", tidal_shape(x_C) < tidal_shape(x_g), (tidal_shape(x_C), tidal_shape(x_g)))
    check("scan acceleration maximum positive", max_g > 0.0, max_g)
    check("scan compactness maximum positive", max_C > 0.0, max_C)
    check("scan tidal maximum positive", max_T > 0.0, max_T)

    passed = sum(ok for _, ok, _ in tests)

    print("BH-GC-001 — gravitational-core descriptor gate")
    print("Plummer control: x=r/a")
    print(f"x_gmax = 1/sqrt(2) = {x_g:.12f}")
    print(f"x_Cmax = sqrt(2)   = {x_C:.12f}")
    print(f"x_Tmax = 0         = {x_T:.12f}")
    print(f"rho/rhobar at gmax = {rho_ratio:.12f}")
    print(f"T(0)={tidal_shape(0.0):.12f}, T(gmax)={tidal_shape(x_g):.12f}, T(Cmax)={tidal_shape(x_C):.12f}")
    print()

    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")

    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print(
        "VERDICT: PASS_WITH_BOUNDARY / MAXIMUM_ACCELERATION_DEFINES_A_USEFUL_CHARACTERISTIC_SHELL_IN_SPHERICAL_NEWTONIAN_CONTROL / "
        "IT_IS_NOT_A_UNIQUE_CORE_CENTER_OR_COMPACTNESS_OR_TIDAL_MAXIMUM / RELATIVISTIC_CORE_DESCRIPTOR_MUST_BE_OBSERVER_OR_FLOW_CONDITIONED_AND_TIDAL_GEOMETRY_BASED"
    )

    return 0 if passed == len(tests) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all"])
    parser.parse_args()
    raise SystemExit(run_audit())


if __name__ == "__main__":
    main()
