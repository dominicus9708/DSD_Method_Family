#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30


def schwarzschild_radius_km(mass_msun: float) -> float:
    return 2.0 * G * mass_msun * M_SUN / C**2 / 1000.0


def buchdahl_min_lambda() -> float:
    """R/r_s lower bound for the standard Buchdahl perfect-fluid assumptions."""
    return 9.0 / 8.0


def andreasson_u_bound(omega: float) -> float:
    """Sharp static anisotropic bound u=2GM/(Rc^2) under p_r+2p_t <= omega*rho."""
    if omega <= 0.0:
        raise ValueError("omega must be positive")
    x = 1.0 + 2.0 * omega
    return (x * x - 1.0) / (x * x)


def lambda_from_u(u: float) -> float:
    if not (0.0 < u < 1.0):
        raise ValueError("u must lie in (0,1)")
    return 1.0 / u


def uniform_density_pc_over_rho_c2(lambda_r: float) -> float:
    """Interior-Schwarzschild central-pressure ratio for R/r_s > 9/8."""
    u = 1.0 / lambda_r
    if not (0.0 < u < 8.0 / 9.0):
        raise ValueError("finite positive central pressure requires R/r_s > 9/8")
    root = math.sqrt(1.0 - u)
    return (1.0 - root) / (3.0 * root - 1.0)


def audit(mass_msun: float) -> list[tuple[str, bool, str]]:
    rs = schwarzschild_radius_km(mass_msun)
    lam_b = buchdahl_min_lambda()
    u_dec = andreasson_u_bound(3.0)
    lam_dec = lambda_from_u(u_dec)

    checks: list[tuple[str, bool, str]] = []
    checks.append((
        "BUCHDAHL_BOUND_IS_9_OVER_8_RS",
        math.isclose(lam_b, 1.125, rel_tol=0.0, abs_tol=1e-15),
        "standard isotropic monotone-density static branch requires R/r_s >= 9/8",
    ))
    checks.append((
        "UNIFORM_DENSITY_PRESSURE_GROWS_TOWARD_BUCHDAHL_LIMIT",
        uniform_density_pc_over_rho_c2(1.13) > uniform_density_pc_over_rho_c2(1.25) > 0.0,
        "the constant-density interior witness shows rapidly increasing central pressure near 9/8 r_s",
    ))
    checks.append((
        "UNIFORM_DENSITY_PRESSURE_DIVERGENCE_WITNESS",
        uniform_density_pc_over_rho_c2(1.1251) > 1000.0,
        "central pressure diverges as R/r_s approaches 9/8 from above",
    ))
    checks.append((
        "TARGET_INTERVAL_EXCLUDED_BY_STANDARD_ISOTROPIC_STATIC_BRANCH",
        lam_b > 1.0,
        "the target finite-core interval 0 < R <= r_s lies below the Buchdahl static perfect-fluid domain",
    ))
    checks.append((
        "ANDREASSON_DEC_BOUND_IS_48_OVER_49",
        math.isclose(u_dec, 48.0 / 49.0, rel_tol=0.0, abs_tol=1e-15),
        "with nonnegative pressures plus DEC, p_r+2p_t <= 3 rho gives u <= 48/49",
    ))
    checks.append((
        "ANISOTROPY_RELAXES_BUT_DOES_NOT_REACH_HORIZON_UNDER_DEC_BOUND",
        1.0 < lam_dec < lam_b,
        "the broad static anisotropic DEC bound permits more compact states than Buchdahl but still keeps R > r_s",
    ))
    checks.append((
        "TARGET_INTERVAL_EXCLUDED_BY_STATIC_ANISOTROPIC_DEC_BRANCH",
        lam_dec > 1.0,
        "under the Andreasson hypotheses the target interval 0 < R <= r_s remains excluded",
    ))
    checks.append((
        "STATIC_EXCLUSION_DOES_NOT_PROVE_NO_FINITE_CORE",
        rs > 0.0 and lam_b > lam_dec > 1.0,
        "the result only closes specified static matter branches; dynamic or assumption-violating branches remain logically open",
    ))
    return checks


def print_report(mass_msun: float) -> None:
    rs = schwarzschild_radius_km(mass_msun)
    lam_b = buchdahl_min_lambda()
    u_dec = andreasson_u_bound(3.0)
    lam_dec = lambda_from_u(u_dec)

    print("DSD gravity static stress support gate -- BH-RB-008")
    print("---------------------------------------------------")
    print(f"mass_msun={mass_msun:.12g}")
    print(f"r_s_km={rs:.12g}")
    print(f"buchdahl_lambda_min={lam_b:.12g}")
    print(f"buchdahl_R_min_km={lam_b * rs:.12g}")
    print(f"andreasson_DEC_u_max={u_dec:.12g}")
    print(f"andreasson_DEC_lambda_min={lam_dec:.12g}")
    print(f"andreasson_DEC_R_min_km={lam_dec * rs:.12g}")
    print()

    print("Uniform-density interior-Schwarzschild pressure witness")
    for lam in (2.0, 1.5, 1.25, 1.13, 1.126, 1.1251):
        ratio = uniform_density_pc_over_rho_c2(lam)
        print(f"R/r_s={lam:.7g}: p_c/(rho c^2)={ratio:.12g}")
    print()

    failures = 0
    checks = audit(mass_msun)
    print("Audit")
    for name, ok, note in checks:
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print()
    print("Boundary")
    print("This audit does not prove that a finite 3D black-hole core is impossible.")
    print("It excludes the target R<=r_s interval only for the stated static GR matter branches.")
    print("The next admissible branch is dynamical support/evolution, unless one explicitly relaxes the matter assumptions.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit static isotropic and anisotropic stress-support bounds for the DSD finite-3D core branch."
    )
    parser.add_argument("--mass-msun", type=float, default=4.297e6)
    args = parser.parse_args()
    if args.mass_msun <= 0.0:
        parser.error("--mass-msun must be positive")
    print_report(args.mass_msun)


if __name__ == "__main__":
    main()
