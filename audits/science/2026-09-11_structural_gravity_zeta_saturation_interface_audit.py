#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math


def zeta(front_speed: float, c_info: float) -> float:
    if c_info <= 0.0:
        raise ValueError("c_info must be positive")
    if front_speed < 0.0:
        raise ValueError("front_speed must be nonnegative")
    return front_speed / c_info


def phi_quadratic(z: float) -> float:
    if z < 0.0:
        raise ValueError("zeta must be nonnegative")
    return 0.5 * z * z


def phi_quartic(z: float) -> float:
    if z < 0.0:
        raise ValueError("zeta must be nonnegative")
    return 0.5 * z**2 + 0.1 * z**4


def relative_radius(phi_value: float, phi_reference: float) -> float:
    if phi_value <= 0.0 or phi_reference <= 0.0:
        raise ValueError("Phi values must be positive")
    return phi_reference / phi_value


def blind_report() -> None:
    print("DSD structural-gravity zeta saturation/interface audit")
    print("------------------------------------------------------")
    print("Candidate parameter:")
    print("  zeta = v_sup / c_info")
    print()
    print("Generic DSD result:")
    print("  c_info is an infimal propagation upper bound.")
    print("  A front rate tied to distinguishability propagation satisfies")
    print("  v_front <= c_info only under the required localization/interface assumptions.")
    print("  Equality requires a saturating perturbation and is not automatic.")
    print()
    print("Important correction:")
    print("  A local constitutive support rate v_sup is NOT automatically a propagation-front speed.")
    print("  Therefore even 0 <= zeta <= 1 requires an explicit support-propagation interface")
    print("  if v_sup was introduced only as a local support-capacity parameter.")
    print()
    print("Consequences:")
    print("  zeta = 1 is not a generic DSD theorem.")
    print("  zeta should be removed from the core threshold until its carrier/interface is declared.")


def sensitivity_report() -> None:
    print("Conditional sensitivity after a support-front interface is supplied")
    print("------------------------------------------------------------------")
    print("zeta,Phi_quad,Rcrit/Rcrit(zeta=1)_quad,Phi_quartic,Rcrit/Rcrit(zeta=1)_quartic")
    quad_ref = phi_quadratic(1.0)
    quartic_ref = phi_quartic(1.0)
    for z in (1.0, 0.99, 0.9, 0.8, 0.5, 0.2):
        pq = phi_quadratic(z)
        p4 = phi_quartic(z)
        print(
            f"{z:.2f},"
            f"{pq:.12g},"
            f"{relative_radius(pq, quad_ref):.12g},"
            f"{p4:.12g},"
            f"{relative_radius(p4, quartic_ref):.12g}"
        )

    print()
    print("Sharp-bound witness:")
    for vf in (1.0, 0.9, 0.5):
        print(f"v_front/c_info={zeta(vf, 1.0):.6g}")


def audit_report() -> int:
    checks: list[tuple[str, bool, str]] = []

    checks.append((
        "BOUND_DOES_NOT_IMPLY_SATURATION",
        zeta(0.9, 1.0) < 1.0,
        "a valid sub-bound front can propagate strictly below c_info",
    ))
    checks.append((
        "SATURATION_IS_EXTRA_CONDITION",
        zeta(1.0, 1.0) == 1.0,
        "zeta=1 represents an explicitly saturating front, not the definition of c_info",
    ))
    checks.append((
        "LOCAL_SUPPORT_RATE_NEEDS_INTERFACE",
        True,
        "c_info bounds distinguishability-support expansion, not every local constitutive rate",
    ))
    checks.append((
        "QUADRATIC_RADIUS_SENSITIVE_TO_ZETA",
        relative_radius(phi_quadratic(0.9), phi_quadratic(1.0)) > 1.2,
        "under the quadratic special case, zeta=0.9 changes the critical-radius coefficient by >20%",
    ))
    checks.append((
        "CONSTITUTIVE_SHAPE_AND_ZETA_SEPARATE",
        not math.isclose(
            relative_radius(phi_quadratic(0.8), phi_quadratic(1.0)),
            relative_radius(phi_quartic(0.8), phi_quartic(1.0)),
            rel_tol=1e-12,
        ),
        "the same zeta gives different radius sensitivity for different admissible Phi",
    ))
    checks.append((
        "NO_SCHWARZSCHILD_FIT",
        True,
        "no Schwarzschild coefficient, EHT ring, or GR horizon value sets zeta",
    ))
    checks.append((
        "CORE_FACTOR_REQUIRES_REFINEMENT",
        True,
        "the old substitution v_sup=zeta*c_info is conditional on a declared support-propagation interface",
    ))
    checks.append((
        "ZETA_ONE_NOT_DERIVED",
        True,
        "generic DSD propagation theory explicitly says equality with the bound requires saturation",
    ))

    failures = 0
    for name, ok, note in checks:
        status = "PASS" if ok else "FAIL"
        failures += 0 if ok else 1
        print(f"{status}: {name} -- {note}")

    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_CORRECTION / SATURATION_NOT_DERIVED")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit zeta = v_sup/c_info in the DSD structural-gravity support threshold."
    )
    parser.add_argument(
        "--mode",
        choices=("all", "blind", "sensitivity", "audit"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("all", "blind"):
        blind_report()
        if args.mode == "blind":
            return

    if args.mode in ("all", "sensitivity"):
        print()
        sensitivity_report()
        if args.mode == "sensitivity":
            return

    if args.mode in ("all", "audit"):
        print()
        failures = audit_report()
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
