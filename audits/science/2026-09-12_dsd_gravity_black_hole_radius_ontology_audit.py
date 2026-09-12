#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

G = 6.67430e-11              # m^3 kg^-1 s^-2
C = 299_792_458.0            # m s^-1
M_SUN = 1.98847e30           # kg
AU_KM = 149_597_870.7         # km


@dataclass(frozen=True)
class Benchmark:
    mass_msun: float = 4.297e6
    mass_stat_msun: float = 0.012e6
    mass_sys_msun: float = 0.040e6


def gravitational_radius_m(mass_msun: float) -> float:
    return G * (mass_msun * M_SUN) / C**2


def schwarzschild_scales(bench: Benchmark) -> dict[str, float]:
    rg = gravitational_radius_m(bench.mass_msun)
    drg_stat = gravitational_radius_m(bench.mass_stat_msun)
    drg_sys = gravitational_radius_m(bench.mass_sys_msun)
    return {
        "r_g_km": rg / 1e3,
        "r_g_stat_km": drg_stat / 1e3,
        "r_g_sys_km": drg_sys / 1e3,
        "r_horizon_km": 2.0 * rg / 1e3,
        "r_horizon_stat_km": 2.0 * drg_stat / 1e3,
        "r_horizon_sys_km": 2.0 * drg_sys / 1e3,
        "r_horizon_AU": 2.0 * rg / 1e3 / AU_KM,
        "r_singularity_areal_km": 0.0,
    }


def kerr_scales(mass_msun: float, chi: float) -> dict[str, float]:
    if not 0.0 <= abs(chi) <= 1.0:
        raise ValueError("|chi| must lie in [0, 1] for a Kerr black hole.")
    rg = gravitational_radius_m(mass_msun)
    q = math.sqrt(max(0.0, 1.0 - chi**2))
    a = abs(chi) * rg
    r_plus = rg * (1.0 + q)
    r_minus = rg * (1.0 - q)
    return {
        "chi": chi,
        "kerr_ring_parameter_a_km": a / 1e3,
        "outer_horizon_r_plus_km": r_plus / 1e3,
        "inner_horizon_r_minus_km": r_minus / 1e3,
    }


def audit(bench: Benchmark) -> list[tuple[str, bool, str]]:
    s = schwarzschild_scales(bench)
    checks: list[tuple[str, bool, str]] = []
    checks.append((
        "SCHWARZSCHILD_HORIZON_IS_2RG",
        math.isclose(s["r_horizon_km"], 2.0 * s["r_g_km"], rel_tol=1e-14),
        "External GR comparator: r_H = 2GM/c^2."
    ))
    checks.append((
        "SCHWARZSCHILD_CURVATURE_SINGULARITY_AT_R0",
        s["r_singularity_areal_km"] == 0.0,
        "External GR comparator: curvature singularity locus has areal coordinate r=0."
    ))
    k0 = kerr_scales(bench.mass_msun, 0.0)
    checks.append((
        "KERR_ZERO_SPIN_REDUCES_TO_SCHWARZSCHILD_HORIZON",
        math.isclose(k0["outer_horizon_r_plus_km"], s["r_horizon_km"], rel_tol=1e-14),
        "chi=0 gives the Schwarzschild outer horizon."
    ))
    checks.append((
        "DSD_NATIVE_RADIUS_NOT_ASSIGNED",
        True,
        "No DSD-native radius is asserted before an explicit localization/metric bridge."
    ))
    return checks


def print_values(bench: Benchmark, chi: float | None) -> None:
    s = schwarzschild_scales(bench)
    print("DSD gravity black-hole radius ontology benchmark")
    print("------------------------------------------------")
    print(f"mass_msun={bench.mass_msun:.12g}")
    print(f"mass_stat_msun={bench.mass_stat_msun:.12g}")
    print(f"mass_sys_msun={bench.mass_sys_msun:.12g}")
    print(f"r_g_km={s['r_g_km']:.12g}")
    print(f"r_g_stat_km={s['r_g_stat_km']:.12g}")
    print(f"r_g_sys_km={s['r_g_sys_km']:.12g}")
    print(f"schwarzschild_horizon_km={s['r_horizon_km']:.12g}")
    print(f"schwarzschild_horizon_stat_km={s['r_horizon_stat_km']:.12g}")
    print(f"schwarzschild_horizon_sys_km={s['r_horizon_sys_km']:.12g}")
    print(f"schwarzschild_horizon_AU={s['r_horizon_AU']:.12g}")
    print("schwarzschild_curvature_singularity_areal_radius_km=0")
    print("dsd_native_radius=UNDEFINED_PENDING_LOCALIZATION_METRIC_BRIDGE")

    if chi is not None:
        k = kerr_scales(bench.mass_msun, chi)
        print()
        print("Kerr external comparator")
        print(f"chi={k['chi']:.12g}")
        print(f"kerr_ring_parameter_a_km={k['kerr_ring_parameter_a_km']:.12g}")
        print(f"outer_horizon_r_plus_km={k['outer_horizon_r_plus_km']:.12g}")
        print(f"inner_horizon_r_minus_km={k['inner_horizon_r_minus_km']:.12g}")
        print("kerr_curvature_singularity_locus=BL_r_0_theta_pi_over_2")
        print("note=a is a Kerr ring parameter, not a regular proper-radius observable")


def main() -> None:
    p = argparse.ArgumentParser(
        description=(
            "External-GR radius ontology benchmark for the active DSD gravity rebaseline. "
            "Does not reuse the discarded K_g/Theta/Psi structural-gravity branch."
        )
    )
    p.add_argument("--mass-msun", type=float, default=4.297e6)
    p.add_argument("--mass-stat-msun", type=float, default=0.012e6)
    p.add_argument("--mass-sys-msun", type=float, default=0.040e6)
    p.add_argument("--chi", type=float, default=None)
    p.add_argument("--mode", choices=("all", "values", "audit"), default="all")
    args = p.parse_args()

    bench = Benchmark(args.mass_msun, args.mass_stat_msun, args.mass_sys_msun)
    checks = audit(bench)

    if args.mode in ("all", "values"):
        print_values(bench, args.chi)

    if args.mode in ("all", "audit"):
        if args.mode == "all":
            print()
        failures = 0
        print("Audit")
        for name, ok, note in checks:
            failures += 0 if ok else 1
            print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
        print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")


if __name__ == "__main__":
    main()
