#!/usr/bin/env python3
"""BH-RB-020: minimal self-binding quantum-closure / epsilon0 derivation gate.

This audit does not claim a black-hole-core EOS. It tests whether a minimal
effective many-body closure with competing attractive and repulsive terms can
generate a finite-density zero-pressure energy-density intercept without
fitting a target radius, and it audits local stability and causality.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


def energy_per_particle(n: float, mc2: float, A: float, B: float) -> float:
    return mc2 - A * n + B * n * n


def energy_density(n: float, mc2: float, A: float, B: float) -> float:
    return n * energy_per_particle(n, mc2, A, B)


def pressure(n: float, A: float, B: float) -> float:
    # p = n^2 de/dn
    return -A * n * n + 2.0 * B * n**3


def denergy_density_dn(n: float, mc2: float, A: float, B: float) -> float:
    return mc2 - 2.0 * A * n + 3.0 * B * n * n


def dpressure_dn(n: float, A: float, B: float) -> float:
    return -2.0 * A * n + 6.0 * B * n * n


def cs2_over_c2(n: float, mc2: float, A: float, B: float) -> float:
    return dpressure_dn(n, A, B) / denergy_density_dn(n, mc2, A, B)


def saturation_density(A: float, B: float) -> float:
    return A / (2.0 * B)


def y_binding(mc2: float, A: float, B: float) -> float:
    return A * A / (4.0 * B * mc2)


def epsilon0(mc2: float, A: float, B: float) -> float:
    ns = saturation_density(A, B)
    return energy_density(ns, mc2, A, B)


def causal_density_cap(mc2: float, B: float) -> float:
    # cs^2/c^2 <= 1 for this toy requires 3 B n^2 <= m c^2.
    return math.sqrt(mc2 / (3.0 * B))


def run_checks() -> list[Check]:
    checks: list[Check] = []

    # Dimensionless normalized control point; no physical BH radius is fitted.
    mc2 = 2.0
    A = 1.0
    B = 1.0
    ns = saturation_density(A, B)
    y = y_binding(mc2, A, B)
    e_star = energy_per_particle(ns, mc2, A, B)
    eps0 = epsilon0(mc2, A, B)
    cs_star = cs2_over_c2(ns, mc2, A, B)
    n_causal = causal_density_cap(mc2, B)

    checks.append(Check(
        "positive attraction/repulsion coefficients generate a positive finite stationary density",
        A > 0.0 and B > 0.0 and ns > 0.0,
        f"n_* = A/(2B) = {ns:.12g}.",
    ))

    dedn_star = -A + 2.0 * B * ns
    checks.append(Check(
        "energy per constituent is stationary at n_*",
        math.isclose(dedn_star, 0.0, abs_tol=1e-14),
        f"de/dn|_* = {dedn_star:.3e}.",
    ))

    checks.append(Check(
        "the stationary point is a strict local minimum",
        2.0 * B > 0.0,
        f"d2e/dn2 = 2B = {2.0*B:.12g}.",
    ))

    checks.append(Check(
        "pressure vanishes at the same finite density",
        math.isclose(pressure(ns, A, B), 0.0, abs_tol=1e-14),
        f"p(n_*) = {pressure(ns, A, B):.3e}.",
    ))

    expected_e_star = mc2 - A*A/(4.0*B)
    checks.append(Check(
        "finite-density energy per constituent matches the analytic minimum",
        math.isclose(e_star, expected_e_star, rel_tol=1e-14),
        f"e_*={e_star:.12g}, analytic={expected_e_star:.12g}.",
    ))

    expected_eps0 = A/(2.0*B) * (mc2 - A*A/(4.0*B))
    checks.append(Check(
        "epsilon_0 is derived from m,A,B rather than supplied independently",
        math.isclose(eps0, expected_eps0, rel_tol=1e-14) and eps0 > 0.0,
        f"epsilon_0={eps0:.12g}.",
    ))

    checks.append(Check(
        "the finite-density state is bound relative to the dilute rest-energy reference",
        0.0 < e_star < mc2,
        f"e_*/mc2={e_star/mc2:.12g}.",
    ))

    expected_cs_star = 2.0*y/(1.0-y)
    checks.append(Check(
        "sound-speed ratio at saturation has the analytic form 2y/(1-y)",
        math.isclose(cs_star, expected_cs_star, rel_tol=1e-14),
        f"y={y:.12g}, cs2/c2={cs_star:.12g}.",
    ))

    checks.append(Check(
        "the chosen control point is locally stable and causal at saturation",
        0.0 < cs_star <= 1.0,
        f"0 < cs2/c2={cs_star:.12g} <= 1.",
    ))

    checks.append(Check(
        "causality at saturation is equivalent to y <= 1/3 for this toy closure",
        (y <= 1.0/3.0) == (cs_star <= 1.0),
        f"y={y:.12g}; threshold=1/3.",
    ))

    checks.append(Check(
        "the same condition places n_* below the toy causal-density cap",
        (y <= 1.0/3.0) == (ns <= n_causal),
        f"n_*={ns:.12g}, n_causal={n_causal:.12g}.",
    ))

    n_high = 10.0 * n_causal
    cs_high = cs2_over_c2(n_high, mc2, A, B)
    checks.append(Check(
        "the polynomial toy is not a globally causal high-density EOS",
        cs_high > 1.0,
        f"at n=10 n_causal, cs2/c2={cs_high:.12g} > 1.",
    ))

    n_very_high = 1.0e8
    cs_asym = cs2_over_c2(n_very_high, mc2, A, B)
    checks.append(Check(
        "the high-density sound-speed ratio approaches the superluminal limit 2",
        math.isclose(cs_asym, 2.0, rel_tol=2e-8),
        f"cs2/c2 at large n={cs_asym:.12g}.",
    ))

    mc2_b = 1.0
    B_b = 1.0
    A_b = math.sqrt(4.0 * B_b * mc2_b * 0.5)  # y=0.5
    ns_b = saturation_density(A_b, B_b)
    cs_b = cs2_over_c2(ns_b, mc2_b, A_b, B_b)
    checks.append(Check(
        "too-strong binding can fail causality even though a finite-density minimum exists",
        ns_b > 0.0 and cs_b > 1.0,
        f"y=0.5 gives cs2/c2={cs_b:.12g}.",
    ))

    A2 = 2.0*A
    B2 = 4.0*B
    ns2 = saturation_density(A2, B2)
    checks.append(Check(
        "changing microscopic interaction coefficients changes the derived saturation density",
        not math.isclose(ns2, ns, rel_tol=1e-14),
        f"n_*(A,B)={ns:.12g}; n_*(2A,4B)={ns2:.12g}.",
    ))

    return checks


def report() -> int:
    checks = run_checks()
    passed = sum(c.passed for c in checks)
    total = len(checks)
    for idx, c in enumerate(checks, 1):
        print(f"[{idx:02d}] {'PASS' if c.passed else 'FAIL'} — {c.name}")
        print(f"     {c.detail}")
    print()
    print(f"RESULT: {passed}/{total} PASS")
    if passed == total:
        print(
            "VERDICT: PASS_WITH_BOUNDARY / "
            "FINITE_DENSITY_SELF_BINDING_SCALE_CONSTRUCTED / "
            "EPSILON0_DERIVABLE_FROM_MICRO_COEFFICIENTS_IN_TOY_CLOSURE / "
            "LOCAL_CAUSALITY_CONDITION_IDENTIFIED / "
            "GLOBAL_CAUSAL_COMPLETION_REQUIRED / "
            "BLACK_HOLE_CORE_EOS_AND_RADIUS_NOT_DERIVED"
        )
        return 0
    print("VERDICT: FAIL")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all", "checks"), default="all")
    args = parser.parse_args()
    if args.mode in {"all", "checks"}:
        return report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
