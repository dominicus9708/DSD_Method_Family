#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

G = 6.67430e-11                 # m^3 kg^-1 s^-2
C = 299_792_458.0              # m s^-1
M_SUN = 1.98847e30             # kg
PC = 3.085677581491367e16      # m
UAS_TO_RAD = math.pi / (180.0 * 3600.0 * 1e6)


@dataclass(frozen=True)
class SgrAInputs:
    mass_msun: float = 4.297e6
    mass_stat_msun: float = 0.012e6
    distance_pc: float = 8277.0
    distance_stat_pc: float = 9.0
    eht_ring_diameter_uas: float = 51.8
    eht_ring_diameter_err_uas: float = 2.3


def angular_uas(length_m: float, distance_m: float) -> float:
    return (length_m / distance_m) / UAS_TO_RAD


def compute(inputs: SgrAInputs) -> dict[str, float]:
    mass_kg = inputs.mass_msun * M_SUN
    distance_m = inputs.distance_pc * PC

    r_g = G * mass_kg / C**2
    r_s = 2.0 * r_g

    theta_g = angular_uas(r_g, distance_m)
    theta_rs_radius = 2.0 * theta_g
    theta_rs_diameter = 4.0 * theta_g

    # Schwarzschild shadow diameter comparator: 2 * (3 sqrt(3) r_g)
    theta_shadow_diameter = 6.0 * math.sqrt(3.0) * theta_g

    # Effective coefficient that would be required only if the observed EHT
    # ring diameter were (incorrectly) equated to a horizon diameter:
    # d_ring = 2 * lambda_eff * theta_g.
    lambda_eff_if_ring_equals_horizon = (
        inputs.eht_ring_diameter_uas / (2.0 * theta_g)
    )

    # Readout ratio between observed ring diameter and Schwarzschild horizon diameter.
    ring_to_schwarzschild_horizon_diameter = (
        inputs.eht_ring_diameter_uas / theta_rs_diameter
    )

    ring_to_schwarzschild_shadow_diameter = (
        inputs.eht_ring_diameter_uas / theta_shadow_diameter
    )

    # First-order independent statistical uncertainty in theta_g from M and D.
    rel_mass = inputs.mass_stat_msun / inputs.mass_msun
    rel_distance = inputs.distance_stat_pc / inputs.distance_pc
    rel_theta_g = math.sqrt(rel_mass**2 + rel_distance**2)
    theta_g_stat = theta_g * rel_theta_g

    return {
        "r_g_km": r_g / 1000.0,
        "r_s_km": r_s / 1000.0,
        "theta_g_uas": theta_g,
        "theta_g_stat_uas": theta_g_stat,
        "theta_rs_radius_uas": theta_rs_radius,
        "theta_rs_diameter_uas": theta_rs_diameter,
        "theta_shadow_diameter_uas": theta_shadow_diameter,
        "eht_ring_diameter_uas": inputs.eht_ring_diameter_uas,
        "ring_to_schwarzschild_horizon_diameter": ring_to_schwarzschild_horizon_diameter,
        "ring_to_schwarzschild_shadow_diameter": ring_to_schwarzschild_shadow_diameter,
        "lambda_eff_if_ring_equals_horizon": lambda_eff_if_ring_equals_horizon,
    }


def audit(result: dict[str, float]) -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []

    checks.append((
        "SCHWARZSCHILD_SCALE_IDENTITY",
        math.isclose(result["r_s_km"], 2.0 * result["r_g_km"], rel_tol=1e-12),
        "R_S = 2 r_g"
    ))

    checks.append((
        "ANGULAR_SCALE_IDENTITY",
        math.isclose(
            result["theta_rs_diameter_uas"],
            4.0 * result["theta_g_uas"],
            rel_tol=1e-12,
        ),
        "Schwarzschild horizon angular diameter = 4 theta_g"
    ))

    checks.append((
        "RING_NOT_HORIZON_DIAMETER",
        abs(result["ring_to_schwarzschild_horizon_diameter"] - 1.0) > 0.5,
        "EHT ring diameter must not be identified with the horizon diameter"
    ))

    checks.append((
        "RING_NEAR_STANDARD_SHADOW_SCALE",
        abs(result["ring_to_schwarzschild_shadow_diameter"] - 1.0) < 0.10,
        "Observed ring scale is near the standard Schwarzschild shadow comparator"
    ))

    checks.append((
        "DSD_COEFFICIENT_REMAINS_UNDERDETERMINED",
        True,
        "lambda_DSD, K_g/G, and c_info/c are not fixed by this benchmark"
    ))

    return checks


def print_report(result: dict[str, float], checks: list[tuple[str, bool, str]]) -> None:
    print("Sgr A* DSD/GR provenance benchmark")
    print("----------------------------------")
    for key, value in result.items():
        print(f"{key}: {value:.12g}")

    print()
    print("Audit")
    failures = 0
    for name, ok, note in checks:
        status = "PASS" if ok else "FAIL"
        failures += 0 if ok else 1
        print(f"{status}: {name} -- {note}")

    print()
    print("Boundary")
    print(
        "R_DSD = lambda_DSD * (K_g/G) * (c/c_info)^2 * r_g "
        "is only a candidate scaling form."
    )
    print(
        "This script does not fit lambda_DSD to 2 and does not infer a DSD "
        "horizon radius from the EHT ring."
    )
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sgr A* DSD structural-gravity / Schwarzschild-scale benchmark"
    )
    parser.add_argument(
        "--mode",
        choices=("all", "values", "audit"),
        default="all",
    )
    args = parser.parse_args()

    result = compute(SgrAInputs())
    checks = audit(result)

    if args.mode == "values":
        for key, value in result.items():
            print(f"{key}={value:.12g}")
    elif args.mode == "audit":
        failures = 0
        for name, ok, note in checks:
            status = "PASS" if ok else "FAIL"
            failures += 0 if ok else 1
            print(f"{status}: {name} -- {note}")
        print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    else:
        print_report(result, checks)


if __name__ == "__main__":
    main()
