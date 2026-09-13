#!/usr/bin/env python3
"""BH-RB-011 — finite-core turning-point / trapping compatibility gate.

This audit uses standard spherically symmetric Misner–Sharp relations in
geometrized units G=c=1. It does not derive a DSD gravity law.

Core identities:
    Gamma^2 = 1 + U^2 - 2m/R
    U = D_T R

For a material-shell turning point U=0:
    Gamma^2 = 1 - 2m/R
so a strictly trapped shell (2m/R > 1) cannot be at an areal-radius
turning point while Gamma is real.

For a nondissipative anisotropic fluid, the standard dynamical equation is
used in the form
    (mu+p_r) D_T U
      = -(mu+p_r)(m/R^2 + 4*pi*p_r*R)
        - Gamma^2 [D_R p_r + 2(p_r-p_t)/R].

The toy values below are dimensionless geometrized controls only.
"""

from __future__ import annotations

import argparse
import math

TOL = 1.0e-12


def gamma_sq(U: float, compactness: float) -> float:
    """Return Gamma^2 = 1 + U^2 - C, with C=2m/R."""
    return 1.0 + U * U - compactness


def min_abs_U_for_real_gamma(compactness: float) -> float:
    """Minimum |U| compatible with Gamma^2>=0 at a given C."""
    return math.sqrt(max(compactness - 1.0, 0.0))


def turning_point_allowed(compactness: float) -> bool:
    """At U=0, a regular turning point requires C<=1."""
    return 1.0 - compactness >= -TOL


def turning_acceleration(
    mu: float,
    p_r: float,
    p_t: float,
    radius: float,
    compactness: float,
    dpr_dR: float,
):
    """Evaluate the nondissipative anisotropic shell acceleration at U=0.

    Returns None when the turning point is kinematically incompatible with
    Gamma^2>=0.
    """
    gsq = 1.0 - compactness
    if gsq < -TOL:
        return None
    if radius <= 0.0:
        raise ValueError("radius must be positive")
    if abs(mu + p_r) <= TOL:
        raise ValueError("mu+p_r must be nonzero for this reduced equation")

    m = 0.5 * compactness * radius
    inertial_density = mu + p_r
    grav = inertial_density * (m / radius**2 + 4.0 * math.pi * p_r * radius)
    stress_bracket = dpr_dR + 2.0 * (p_r - p_t) / radius
    hydro = -gsq * stress_bracket
    acceleration = (hydro - grav) / inertial_density
    return {
        "Gamma2": gsq,
        "grav_term": grav,
        "stress_bracket": stress_bracket,
        "hydro_term": hydro,
        "D_T_U": acceleration,
    }


def required_stress_bracket_threshold(
    mu: float, p_r: float, radius: float, compactness: float
) -> float:
    """Threshold B such that B < threshold is needed for D_T U>0.

    B = D_R p_r + 2(p_r-p_t)/R.
    Assumes 0<=C<1 and mu+p_r>0.
    """
    gsq = 1.0 - compactness
    if gsq <= 0.0:
        raise ValueError("threshold is defined here only for C<1")
    m = 0.5 * compactness * radius
    grav = (mu + p_r) * (m / radius**2 + 4.0 * math.pi * p_r * radius)
    return -grav / gsq


def run_checks() -> list[tuple[str, bool]]:
    checks: list[tuple[str, bool]] = []

    checks.append(("untrapped U=0 gives Gamma^2>0", abs(gamma_sq(0.0, 0.8) - 0.2) < TOL))
    checks.append(("marginal U=0 gives Gamma^2=0", abs(gamma_sq(0.0, 1.0)) < TOL))
    checks.append(("strictly trapped U=0 is incompatible", gamma_sq(0.0, 1.2) < 0.0))
    checks.append(("C=1.2 needs |U|>=sqrt(0.2)", abs(gamma_sq(-math.sqrt(0.2), 1.2)) < TOL))
    checks.append(("larger |U| restores Gamma^2>=0", gamma_sq(-0.6, 1.2) >= 0.0))
    checks.append(("turning point gate is exactly C<=1", turning_point_allowed(0.99) and turning_point_allowed(1.0) and not turning_point_allowed(1.01)))

    toy_08 = turning_acceleration(1.0, 0.1, 0.5, 1.0, 0.80, -20.0)
    toy_095 = turning_acceleration(1.0, 0.1, 0.5, 1.0, 0.95, -20.0)
    toy_099 = turning_acceleration(1.0, 0.1, 0.5, 1.0, 0.99, -20.0)
    toy_100 = turning_acceleration(1.0, 0.1, 0.5, 1.0, 1.00, -20.0)

    checks.append(("finite stress can yield a bounce away from C=1", toy_08 is not None and toy_08["D_T_U"] > 0.0))
    checks.append(("same finite stress loses against gravity near C=1", toy_095 is not None and toy_099 is not None and toy_095["D_T_U"] < 0.0 and toy_099["D_T_U"] < 0.0))
    checks.append(("at C=1 finite hydro term is suppressed by Gamma^2", toy_100 is not None and abs(toy_100["hydro_term"]) < TOL and toy_100["grav_term"] > 0.0 and toy_100["D_T_U"] < 0.0))

    thr_08 = required_stress_bracket_threshold(1.0, 0.1, 1.0, 0.80)
    thr_099 = required_stress_bracket_threshold(1.0, 0.1, 1.0, 0.99)
    checks.append(("required finite stress magnitude diverges as C->1-", abs(thr_099) > abs(thr_08)))

    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all", "checks", "toy"], default="all")
    args = parser.parse_args()

    if args.mode in ("all", "checks"):
        checks = run_checks()
        passed = sum(ok for _, ok in checks)
        for name, ok in checks:
            print(f"{'PASS' if ok else 'FAIL'}  {name}")
        print(f"\n{passed}/{len(checks)} checks passed")
        if passed != len(checks):
            return 1

    if args.mode in ("all", "toy"):
        print("\nToy turning-point controls (G=c=R=mu=1 units where applicable)")
        for C in (0.80, 0.95, 0.99, 1.00, 1.20):
            print(f"C={C:.2f}: Gamma^2(U=0)={1-C:+.6f}, min|U|={min_abs_U_for_real_gamma(C):.6f}")
        for C in (0.80, 0.95, 0.99, 1.00):
            res = turning_acceleration(1.0, 0.1, 0.5, 1.0, C, -20.0)
            print(f"C={C:.2f}: {res}")

    print("\nVERDICT: PASS_WITH_BOUNDARY / TURNING_POINT_REQUIRES_NONTRAPPED_OR_MARGINAL_STATE / FINITE_CORE_NOT_DERIVED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
