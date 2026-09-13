#!/usr/bin/env python3
"""BH-RB-010 — Standard-GR singularity focusing / escape-condition gate.

This audit deliberately uses only the algebraic consequences of the null
Raychaudhuri equation and the logical hypothesis structure of the Penrose
singularity theorem.  It does not import any discarded structural-gravity law.

Author: Kwon Dominicus
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isclose


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    detail: str


def raychaudhuri_rhs(theta: float, shear_sq: float = 0.0, rkk: float = 0.0) -> float:
    """Null, twist-free Raychaudhuri RHS in 3+1 dimensions.

    dtheta/dlambda = -1/2 theta^2 - sigma_ab sigma^ab - R_ab k^a k^b.
    """
    if shear_sq < 0:
        raise ValueError("shear_sq must be non-negative")
    return -0.5 * theta * theta - shear_sq - rkk


def focusing_bound(theta0: float) -> float:
    """Affine-parameter upper bound 2/|theta0| for theta0 < 0 under NCC."""
    if theta0 >= 0:
        raise ValueError("theta0 must be negative for the trapped/focusing gate")
    return 2.0 / abs(theta0)


def required_rkk_for_derivative(theta: float, shear_sq: float, target_dtheta: float) -> float:
    """R_kk required to obtain a requested local dtheta/dlambda."""
    if shear_sq < 0:
        raise ValueError("shear_sq must be non-negative")
    return -0.5 * theta * theta - shear_sq - target_dtheta


def penrose_gate(ncc: bool, noncompact_cauchy: bool, closed_future_trapped: bool) -> bool:
    """Return True when the modern Penrose theorem hypotheses used here are all present.

    True means: the theorem forces future null geodesic incompleteness.
    It does NOT mean that a material core has zero radius.
    """
    return ncc and noncompact_cauchy and closed_future_trapped


def run_checks() -> list[Check]:
    checks: list[Check] = []

    for theta0, expected in [(-0.5, 4.0), (-1.0, 2.0), (-2.0, 1.0)]:
        got = focusing_bound(theta0)
        checks.append(
            Check(
                f"focusing_bound_theta0_{theta0:g}",
                isclose(got, expected, rel_tol=0.0, abs_tol=1e-12),
                f"lambda_focus <= {got:g} (dimensionless affine units)",
            )
        )

    for i, (theta, shear_sq, rkk) in enumerate(
        [(-1.0, 0.0, 0.0), (-1.0, 0.2, 0.0), (-0.3, 0.1, 0.05), (-2.0, 1.0, 3.0)],
        start=1,
    ):
        rhs = raychaudhuri_rhs(theta, shear_sq, rkk)
        checks.append(
            Check(
                f"ncc_monotone_case_{i}",
                rhs < 0.0,
                f"dtheta/dlambda={rhs:.6g} <= 0 under theta<0, shear^2>=0, R_kk>=0",
            )
        )

    theta = -1.0
    shear_sq = 0.04
    target = 0.1
    required_rkk = required_rkk_for_derivative(theta, shear_sq, target)
    checks.append(
        Check(
            "local_defocusing_requires_negative_Rkk",
            required_rkk < 0.0,
            f"for theta={theta}, shear^2={shear_sq}, target dtheta/dlambda={target}, R_kk={required_rkk}",
        )
    )
    checks.append(
        Check(
            "local_defocusing_target_reproduced",
            isclose(raychaudhuri_rhs(theta, shear_sq, required_rkk), target, abs_tol=1e-12),
            "Raychaudhuri substitution reproduces the requested positive derivative",
        )
    )

    checks.append(
        Check(
            "penrose_all_hypotheses_force_incompleteness",
            penrose_gate(True, True, True),
            "NCC + noncompact Cauchy hypersurface + closed future-trapped surface",
        )
    )
    checks.append(
        Check(
            "penrose_escape_if_ncc_fails",
            not penrose_gate(False, True, True),
            "the theorem no longer follows when null convergence is not supplied",
        )
    )
    checks.append(
        Check(
            "penrose_escape_if_global_cauchy_hypothesis_fails",
            not penrose_gate(True, False, True),
            "the theorem no longer follows when the noncompact Cauchy hypothesis is not supplied",
        )
    )

    return checks


def print_branch_summary() -> None:
    print("\nBranch classification")
    print("A. Continued trapped collapse + NCC + noncompact Cauchy surface -> null geodesic incompleteness is forced.")
    print("   This is NOT a theorem that the material support radius becomes zero.")
    print("B. Trapped -> untrapped local null defocusing -> impossible along the same twist-free null congruence while NCC holds.")
    print("   In Einstein GR, direct local defocusing therefore requires NEC/NCC violation or failure of the congruence assumptions.")
    print("C. Finite R_min > 0 core that remains trapped can be posited, but if it is also future-complete, then at least one Penrose hypothesis must fail.")
    print("D. Matter-worldline bounce and causal untrapping are distinct questions; pressure acceleration can reverse matter motion without by itself reversing null expansion.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all", "checks", "summary"], default="all")
    args = parser.parse_args()

    if args.mode in {"all", "checks"}:
        checks = run_checks()
        passed = sum(c.passed for c in checks)
        for c in checks:
            status = "PASS" if c.passed else "FAIL"
            print(f"[{status}] {c.name}: {c.detail}")
        print(f"\nchecks: {passed}/{len(checks)} PASS")
        if passed != len(checks):
            return 1

    if args.mode in {"all", "summary"}:
        print_branch_summary()
        print("\nVERDICT: PASS_WITH_BOUNDARY / FOCUSING_GATE_IDENTIFIED / FINITE_CORE_NOT_DERIVED")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
