#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30

DEFINED_ZERO = "defined_zero"
DEFINED_NONZERO = "defined_nonzero"


@dataclass(frozen=True)
class CoreAssumptions:
    ambient_spatial_dimension: int = 3
    support_spatial_dimension: int = 3
    finite_positive_radius: bool = True
    constituent_identity_required: bool = False
    formation_level_successor_allowed: bool = True
    stress_energy_required: bool = True
    eos_supplied: bool = False
    static_equilibrium_claimed: bool = False
    j_status: str = DEFINED_ZERO
    q_status: str = DEFINED_ZERO


def schwarzschild_radius_m(mass_msun: float) -> float:
    if mass_msun <= 0:
        raise ValueError("mass_msun must be positive")
    return 2.0 * G * mass_msun * M_SUN / C**2


def core_radius_m(mass_msun: float, radius_fraction: float) -> float:
    if not (0.0 < radius_fraction <= 1.0):
        raise ValueError("radius_fraction must lie in (0, 1]")
    return radius_fraction * schwarzschild_radius_m(mass_msun)


def mean_mass_density_kg_m3(mass_msun: float, radius_fraction: float) -> float:
    radius = core_radius_m(mass_msun, radius_fraction)
    mass = mass_msun * M_SUN
    return 3.0 * mass / (4.0 * math.pi * radius**3)


def mean_energy_density_j_m3(mass_msun: float, radius_fraction: float) -> float:
    return mean_mass_density_kg_m3(mass_msun, radius_fraction) * C**2


def compactness(radius_fraction: float) -> float:
    if not (0.0 < radius_fraction <= 1.0):
        raise ValueError("radius_fraction must lie in (0, 1]")
    return 1.0 / radius_fraction


def audit(assumptions: CoreAssumptions, mass_msun: float) -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []

    checks.append((
        "AMBIENT_SPACE_REMAINS_3D_BY_WORKING_SPECIALIZATION",
        assumptions.ambient_spatial_dimension == 3,
        "the first branch does not identify compression with dimensional collapse",
    ))
    checks.append((
        "MATERIAL_SUPPORT_REMAINS_FINITE_3D",
        assumptions.support_spatial_dimension == 3 and assumptions.finite_positive_radius,
        "the candidate core is a finite 3D support, not an ontological point object",
    ))
    checks.append((
        "CONSTITUENT_IDENTITY_IS_NOT_REQUIRED",
        not assumptions.constituent_identity_required and assumptions.formation_level_successor_allowed,
        "stellar constituent identity may be lost while a new successor core is formed",
    ))
    checks.append((
        "STRESS_ENERGY_IS_REQUIRED_FOR_PHYSICAL_CLOSURE",
        assumptions.stress_energy_required,
        "mass density alone is not treated as a supporting mechanism",
    ))
    checks.append((
        "J_AND_Q_ZERO_ARE_EXPLICIT_NOT_UNDEFINED",
        assumptions.j_status == DEFINED_ZERO and assumptions.q_status == DEFINED_ZERO,
        "the first spherical comparator branch uses explicit nonrotating and neutral statuses",
    ))

    rho_1 = mean_mass_density_kg_m3(mass_msun, 1.0)
    rho_half = mean_mass_density_kg_m3(mass_msun, 0.5)
    checks.append((
        "MEAN_DENSITY_SCALES_AS_RADIUS_MINUS_THREE",
        math.isclose(rho_half / rho_1, 8.0, rel_tol=1e-12),
        "halving a finite 3D radius at fixed mass raises mean density by a factor of eight",
    ))

    equilibrium_blocked = not assumptions.eos_supplied and not assumptions.static_equilibrium_claimed
    checks.append((
        "NO_EQUILIBRIUM_CLAIM_BEFORE_CONSTITUTIVE_CLOSURE",
        equilibrium_blocked,
        "without an EOS/constitutive stress law this gate permits scale calculations but not a stable-core solution claim",
    ))

    checks.append((
        "POSITIVE_RADIUS_DOMAIN_ONLY",
        core_radius_m(mass_msun, 1.0) > 0.0 and core_radius_m(mass_msun, 0.01) > 0.0,
        "the scan variable is restricted to R_core > 0",
    ))

    return checks


def print_report(mass_msun: float) -> None:
    assumptions = CoreAssumptions()
    rs_m = schwarzschild_radius_m(mass_msun)

    print("DSD gravity finite 3D re-formed core assumption gate -- BH-RB-007")
    print("------------------------------------------------------------------")
    print(f"mass_msun={mass_msun:.12g}")
    print(f"schwarzschild_radius_km={rs_m / 1000.0:.12g}")
    print("model=constituent-agnostic finite 3D successor core")
    print("status=ASSUMPTION_GATE_ONLY; no EOS or equilibrium solution is inferred")
    print()

    print("Scale table")
    print("lambda,R_core_km,compactness,mean_rho_kg_m3,mean_epsilon_J_m3")
    for lam in (1.0, 0.5, 0.1, 0.01):
        print(
            f"{lam:.6g},"
            f"{core_radius_m(mass_msun, lam)/1000.0:.12g},"
            f"{compactness(lam):.12g},"
            f"{mean_mass_density_kg_m3(mass_msun, lam):.12g},"
            f"{mean_energy_density_j_m3(mass_msun, lam):.12g}"
        )

    print()
    checks = audit(assumptions, mass_msun)
    failures = 0
    for name, ok, note in checks:
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")

    print()
    print("Boundary")
    print("The 3D-support and constituent-agnostic successor assumptions are working specializations, not generic DSD theorems.")
    print("The script does not claim that pure mass is a material substance, does not derive an EOS, and does not establish equilibrium inside the horizon.")
    print("Its next required input is a constitutive stress-energy model or dynamical evolution law for the successor core.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit the finite-3D, constituent-agnostic re-formed black-hole core assumptions."
    )
    parser.add_argument("--mass-msun", type=float, default=4.297e6)
    args = parser.parse_args()
    if args.mass_msun <= 0:
        parser.error("--mass-msun must be positive")
    print_report(args.mass_msun)


if __name__ == "__main__":
    main()
