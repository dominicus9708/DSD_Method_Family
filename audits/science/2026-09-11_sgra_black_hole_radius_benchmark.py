#!/usr/bin/env python3
"""
Sgr A* structural-gravity black-hole critical-radius benchmark.

Purpose
-------
Keep four layers separate:

1. independent external inference:
   stellar-orbit mass and distance for Sgr A*;
2. direct horizon-scale observable:
   EHT bright-ring angular diameter;
3. standard-GR comparator:
   r_g = GM/c^2 and R_S = 2GM/c^2;
4. DSD candidate layer:
   R_crit = K_g M / (Theta_* c_info^2).

The script does NOT fit K_g, Theta_*, or c_info to Schwarzschild.
It only exposes the dimensionless closure relation that a later
independent DSD derivation would have to satisfy.

Default numerical inputs:
- GRAVITY Collaboration (2022):
  M = (4.297 ± 0.012 stat ± 0.040 sys) x 10^6 M_sun
  D = 8277 ± 9 stat ± 30 sys pc
- EHT Collaboration (2022):
  bright ring diameter = 51.8 ± 2.3 microarcsec
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass


# SI constants. The numerical benchmark is insensitive to the final few
# significant figures at the current astrophysical error level.
G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30
PARSEC = 3.085677581491367e16
RAD_TO_UAS = 206_264_806_247.09636


@dataclass(frozen=True)
class Inputs:
    mass_msun: float = 4.297e6
    mass_stat_msun: float = 0.012e6
    mass_sys_msun: float = 0.040e6
    distance_pc: float = 8277.0
    distance_stat_pc: float = 9.0
    distance_sys_pc: float = 30.0
    ring_diameter_uas: float = 51.8
    ring_diameter_err_uas: float = 2.3


def quadrature(*values: float) -> float:
    return math.sqrt(sum(v * v for v in values))


def gravitational_radius_m(mass_msun: float) -> float:
    return G * mass_msun * M_SUN / C**2


def angle_uas(length_m: float, distance_pc: float) -> float:
    return length_m / (distance_pc * PARSEC) * RAD_TO_UAS


def physical_length_m(angle_uas_value: float, distance_pc: float) -> float:
    return angle_uas_value / RAD_TO_UAS * distance_pc * PARSEC


def ratio_uncertainty(
    ratio: float,
    numerator: float,
    numerator_err: float,
    mass: float,
    mass_err: float,
    distance: float,
    distance_err: float,
) -> float:
    """
    For ring/theta_g where theta_g ∝ M/D:
      ratio ∝ ring * D / M.
    """
    rel = quadrature(
        numerator_err / numerator,
        mass_err / mass,
        distance_err / distance,
    )
    return abs(ratio) * rel


def dsd_to_schwarzschild_ratio(
    theta_star: float,
    kg_over_g: float,
    cinfo_over_c: float,
) -> float:
    """
    Candidate DSD critical radius:
        R_crit = K_g M / (Theta_* c_info^2)

    Standard comparator:
        R_S = 2 G M / c^2

    Hence:
        R_crit / R_S
        = [1 / (2 Theta_*)] (K_g/G) (c/c_info)^2.
    """
    if theta_star <= 0:
        raise ValueError("theta_star must be positive")
    if cinfo_over_c <= 0:
        raise ValueError("cinfo_over_c must be positive")
    return (kg_over_g / (2.0 * theta_star)) / (cinfo_over_c**2)


def compute(inputs: Inputs) -> dict:
    rg_m = gravitational_radius_m(inputs.mass_msun)
    rs_m = 2.0 * rg_m

    theta_g_uas = angle_uas(rg_m, inputs.distance_pc)
    theta_rs_radius_uas = 2.0 * theta_g_uas
    theta_horizon_diameter_uas = 4.0 * theta_g_uas

    ring_physical_diameter_m = physical_length_m(
        inputs.ring_diameter_uas, inputs.distance_pc
    )

    ring_over_rg = inputs.ring_diameter_uas / theta_g_uas
    ring_over_horizon_diameter = (
        inputs.ring_diameter_uas / theta_horizon_diameter_uas
    )

    ring_over_rg_stat_err = ratio_uncertainty(
        ring_over_rg,
        inputs.ring_diameter_uas,
        inputs.ring_diameter_err_uas,
        inputs.mass_msun,
        inputs.mass_stat_msun,
        inputs.distance_pc,
        inputs.distance_stat_pc,
    )
    ring_over_rg_sys_err = ring_over_rg * quadrature(
        inputs.mass_sys_msun / inputs.mass_msun,
        inputs.distance_sys_pc / inputs.distance_pc,
    )
    ring_over_rg_total_err = quadrature(
        ring_over_rg_stat_err, ring_over_rg_sys_err
    )

    theta_g_stat_err = theta_g_uas * quadrature(
        inputs.mass_stat_msun / inputs.mass_msun,
        inputs.distance_stat_pc / inputs.distance_pc,
    )
    theta_g_sys_err = theta_g_uas * quadrature(
        inputs.mass_sys_msun / inputs.mass_msun,
        inputs.distance_sys_pc / inputs.distance_pc,
    )

    return {
        "inputs": asdict(inputs),
        "independent_scale": {
            "r_g_km": rg_m / 1e3,
            "R_S_km": rs_m / 1e3,
            "theta_g_uas": theta_g_uas,
            "theta_g_stat_err_uas": theta_g_stat_err,
            "theta_g_sys_err_uas": theta_g_sys_err,
            "theta_Rs_radius_uas": theta_rs_radius_uas,
            "theta_horizon_diameter_uas": theta_horizon_diameter_uas,
        },
        "eht_readout_without_shadow_calibration": {
            "ring_physical_diameter_km": ring_physical_diameter_m / 1e3,
            "ring_diameter_over_r_g": ring_over_rg,
            "ring_diameter_over_r_g_total_err": ring_over_rg_total_err,
            "ring_diameter_over_schwarzschild_horizon_diameter": (
                ring_over_horizon_diameter
            ),
        },
        "dsd_candidate_relation": {
            "definition": "R_crit = K_g M / (Theta_* c_info^2)",
            "comparison_identity": (
                "R_crit/R_S = (K_g/G) / "
                "[2 Theta_* (c_info/c)^2]"
            ),
            "closure_if_Kg_eq_G_and_cinfo_eq_c": (
                "Theta_* = 1/2 is required for R_crit = R_S"
            ),
            "status": (
                "OPEN: K_g, Theta_*, and c_info/c are not fixed by this benchmark"
            ),
        },
    }


def format_report(result: dict) -> str:
    s = result["independent_scale"]
    e = result["eht_readout_without_shadow_calibration"]
    d = result["dsd_candidate_relation"]

    lines = [
        "Sgr A* DSD structural-gravity radius benchmark",
        "================================================",
        f"r_g = {s['r_g_km']:.6e} km",
        f"R_S = {s['R_S_km']:.6e} km",
        (
            "theta_g(independent orbit M/D) = "
            f"{s['theta_g_uas']:.6f} uas "
            f"± {s['theta_g_stat_err_uas']:.6f} stat "
            f"± {s['theta_g_sys_err_uas']:.6f} sys"
        ),
        f"Schwarzschild horizon angular diameter = {s['theta_horizon_diameter_uas']:.6f} uas",
        f"EHT bright-ring physical diameter = {e['ring_physical_diameter_km']:.6e} km",
        (
            "EHT bright-ring diameter / r_g = "
            f"{e['ring_diameter_over_r_g']:.6f} "
            f"± {e['ring_diameter_over_r_g_total_err']:.6f}"
        ),
        (
            "EHT bright-ring diameter / Schwarzschild horizon diameter = "
            f"{e['ring_diameter_over_schwarzschild_horizon_diameter']:.6f}"
        ),
        "",
        "DSD candidate closure",
        "---------------------",
        d["definition"],
        d["comparison_identity"],
        d["closure_if_Kg_eq_G_and_cinfo_eq_c"],
        d["status"],
    ]
    return "\n".join(lines)


def self_test(result: dict) -> None:
    s = result["independent_scale"]
    e = result["eht_readout_without_shadow_calibration"]

    assert 6.2e6 < s["r_g_km"] < 6.5e6
    assert 1.24e7 < s["R_S_km"] < 1.30e7
    assert 5.0 < s["theta_g_uas"] < 5.3
    assert 9.5 < e["ring_diameter_over_r_g"] < 10.7

    # Algebraic closure check only; this does not derive these values.
    ratio = dsd_to_schwarzschild_ratio(
        theta_star=0.5,
        kg_over_g=1.0,
        cinfo_over_c=1.0,
    )
    assert abs(ratio - 1.0) < 1e-15


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "json", "test"),
        default="all",
    )
    parser.add_argument(
        "--json-out",
        default=None,
        help="Optional path for machine-readable benchmark output.",
    )
    args = parser.parse_args()

    result = compute(Inputs())
    self_test(result)

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

    if args.mode == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif args.mode == "test":
        print("PASS: all benchmark self-tests")
    else:
        print(format_report(result))
        print("\nPASS: all benchmark self-tests")


if __name__ == "__main__":
    main()
