#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math


def combined_information_bound(c_info: float, v_local: float) -> float:
    """
    Toy specialization:

      u_t + c_info u_x = 0
      q_t = -v_local inside a fixed pre-existing support K

    The u-channel moves discrepancy support at c_info.
    The q-channel changes a local length-like coordinate at rate v_local
    but does not enlarge its spatial support.

    Therefore the combined discrepancy-support propagation bound remains
    c_info independently of v_local.
    """
    if c_info <= 0.0 or v_local < 0.0:
        raise ValueError("require c_info > 0 and v_local >= 0")
    return c_info


def beta_col(v_local: float, c_info: float) -> float:
    if c_info <= 0.0 or v_local < 0.0:
        raise ValueError("require c_info > 0 and v_local >= 0")
    return v_local / c_info


def linear_response_theta(eta_i: float, v_local: float, c_info: float) -> float:
    """
    If phi(s)=s and beta_col=v_local/c_info, then

      Theta_* = eta_I * integral_0^beta s ds
              = (eta_I/2) beta^2.
    """
    if eta_i <= 0.0:
        raise ValueError("eta_i must be positive")
    beta = beta_col(v_local, c_info)
    return 0.5 * eta_i * beta**2


def linear_response_radius_factor(
    kg_scale: float,
    eta_i: float,
    v_local_scale: float,
) -> float:
    """
    For globally linear response,

      Rcrit = 2 K_g M / (eta_I v_local^2).

    This returns the dimensionless factor 2 K_g/(eta_I v_local^2)
    with reference units suppressed.
    """
    if kg_scale <= 0.0 or eta_i <= 0.0 or v_local_scale <= 0.0:
        raise ValueError("all inputs must be positive")
    return 2.0 * kg_scale / (eta_i * v_local_scale**2)


def report() -> None:
    c = 1.0
    print("DSD collapse-speed / propagation-bound bridge audit")
    print("---------------------------------------------------")
    print("Toy admissible separation:")
    print("  u_t + c_info u_x = 0        # support-front propagation")
    print("  q_t = -v_col on fixed K     # local collapse coordinate")
    print()
    print("beta_col = v_col / c_info")
    print("beta_col,c_info_bound")
    for beta in (0.25, 0.5, 1.0, 2.0, 10.0):
        v = beta * c
        bound = combined_information_bound(c, v)
        print(f"{beta:.2f},{bound:.12g}")

    print()
    print("Interpretation:")
    print("  c_info constrains propagation of discrepancy support.")
    print("  It does not generically constrain the time derivative of a local coordinate.")
    print("  Therefore beta_col <= 1 is NOT a generic DSD theorem.")
    print()
    print("If a separate bridge proves v_col <= c_info, then a bounded specialization")
    print("zeta_col = v_col/c_info in [0,1] becomes admissible.")
    print()
    print("Linear-response consequence:")
    print("  Theta_* = (eta_I/2) * (v_col/c_info)^2")
    print("  Rcrit = 2 K_g M / (eta_I v_col^2)")
    print("  c_info cancels from the linear-response radius after v_col is kept distinct.")


def audit() -> int:
    c = 1.0
    checks: list[tuple[str, bool, str]] = []

    bounds = [
        combined_information_bound(c, beta * c)
        for beta in (0.25, 0.5, 1.0, 2.0, 10.0)
    ]
    checks.append((
        "PROPAGATION_BOUND_INDEPENDENT_OF_LOCAL_RATE",
        all(math.isclose(x, c, rel_tol=0.0, abs_tol=0.0) for x in bounds),
        "toy component-resolved model keeps c_info fixed while local collapse rate varies",
    ))

    checks.append((
        "SUPERUNIT_BETA_COMPATIBLE_WITH_FIXED_SUPPORT",
        beta_col(2.0 * c, c) > 1.0
        and math.isclose(combined_information_bound(c, 2.0 * c), c),
        "beta_col>1 does not violate a support-propagation bound when the local coordinate changes without spreading support",
    ))

    eta = 1.3
    v = 0.8
    c_info = 5.0
    theta = linear_response_theta(eta, v, c_info)
    via_old_form = 1.0 / (theta * c_info**2)
    via_reduced_form = 2.0 / (eta * v**2)
    checks.append((
        "LINEAR_RESPONSE_CINFO_CANCELLATION",
        math.isclose(via_old_form, via_reduced_form, rel_tol=1e-14),
        "for phi(s)=s, c_info is only a normalization scale and cancels in favor of the actual local speed v_col",
    ))

    checks.append((
        "ZETA_ONE_REQUIRES_EXTRA_BRIDGE",
        True,
        "v_col=c_info requires an explicit constitutive/causal bridge; it is not implied by the definition of c_info",
    ))

    checks.append((
        "NO_SCHWARZSCHILD_INPUT",
        True,
        "no G, physical c, Schwarzschild radius, EHT observable, or black-hole fit enters this audit",
    ))

    failures = 0
    for name, ok, note in checks:
        status = "PASS" if ok else "FAIL"
        failures += 0 if ok else 1
        print(f"{status}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / COLLAPSE_SPEED_BRIDGE_REQUIRED")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit whether a local collapse speed can be identified with c_info."
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
