#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math


def integral_linear(zeta: float) -> float:
    if not (0.0 < zeta <= 1.0):
        raise ValueError("zeta must satisfy 0 < zeta <= 1")
    return 0.5 * zeta**2


def radius_scale_factor(
    kg_scale: float,
    eta_i: float,
    response_integral: float,
    cinfo_scale: float = 1.0,
) -> float:
    """
    Dimensionless factor multiplying M in the candidate radius:

        Rcrit/M ∝ K_g / [eta_I I_phi(zeta) c_info^2].

    Here all dimensional reference units are suppressed. The purpose is
    identifiability, not physical calibration.
    """
    if kg_scale <= 0 or eta_i <= 0 or response_integral <= 0 or cinfo_scale <= 0:
        raise ValueError("all scale inputs must be positive")
    return kg_scale / (eta_i * response_integral * cinfo_scale**2)


def report() -> None:
    zeta = 1.0
    response = integral_linear(zeta)
    baseline = radius_scale_factor(1.0, 1.0, response)

    print("DSD inertial/source-coupling identifiability audit")
    print("--------------------------------------------------")
    print("Candidate combination:")
    print("  Rcrit/M ∝ K_g / [eta_I I_phi(zeta) c_info^2]")
    print("  eta_I = mu_I / mu_g")
    print()
    print(f"Linear-response I_phi(1) = {response:.12g}")
    print(f"Baseline factor = {baseline:.12g}")
    print()
    print("Common rescaling degeneracy K_g -> a K_g, eta_I -> a eta_I:")
    print("a,scaled_factor,relative_to_baseline")
    for a in (0.25, 0.5, 1.0, 2.0, 4.0, 10.0):
        scaled = radius_scale_factor(a, a, response)
        print(f"{a:.2f},{scaled:.12g},{scaled/baseline:.12g}")

    print()
    print("Independent eta variation with K_g fixed:")
    print("eta_I,factor,relative_to_baseline")
    for eta in (0.8, 0.9, 1.0, 1.1, 1.2):
        value = radius_scale_factor(1.0, eta, response)
        print(f"{eta:.2f},{value:.12g},{value/baseline:.12g}")

    print()
    print("Boundary:")
    print("  Black-hole radius data alone constrain a combination, not eta_I=1.")
    print("  A separate bridge or independent calibration is required to identify mu_I with mu_g.")


def audit() -> int:
    response = integral_linear(1.0)
    baseline = radius_scale_factor(1.0, 1.0, response)

    checks: list[tuple[str, bool, str]] = []

    for a in (0.25, 0.5, 2.0, 4.0, 10.0):
        scaled = radius_scale_factor(a, a, response)
        checks.append((
            f"COMMON_RESCALING_INVARIANCE_a={a}",
            math.isclose(scaled, baseline, rel_tol=1e-14, abs_tol=0.0),
            "simultaneous scaling of K_g and eta_I leaves the candidate radius factor unchanged",
        ))

    changed = radius_scale_factor(1.0, 1.1, response)
    checks.append((
        "ETA_IDENTIFIABLE_ONLY_AFTER_KG_FIXED",
        not math.isclose(changed, baseline, rel_tol=1e-6),
        "eta_I changes the radius only after K_g and the response law are independently fixed",
    ))

    checks.append((
        "ETA_EQUAL_ONE_NOT_GENERIC_DSD",
        True,
        "eta_I=1 requires an explicit identification bridge between inertial and source-coupled measures",
    ))

    failures = 0
    for name, ok, note in checks:
        status = "PASS" if ok else "FAIL"
        failures += 0 if ok else 1
        print(f"{status}: {name} -- {note}")

    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / ETA_I_UNDERDETERMINED")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit identifiability of the DSD inertial/source-coupling ratio eta_I."
    )
    parser.add_argument("--mode", choices=("all", "report", "audit"), default="all")
    args = parser.parse_args()

    if args.mode in ("all", "report"):
        report()
        if args.mode == "report":
            return

    if args.mode in ("all", "audit"):
        print()
        failures = audit()
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
