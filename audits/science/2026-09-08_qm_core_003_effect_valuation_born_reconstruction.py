#!/usr/bin/env python3
"""
QM Core 003 — Effect valuation / Born representation finite witness.

Standard-library-only reproducibility script for:
1) coarse-graining additivity of the Born valuation,
2) failure of a nonlinear context-normalized quadratic rule,
3) qubit state reconstruction from effect valuations,
4) absorption of any additive probability lift into a changed density-state
   representation in the finite-dimensional effect-valuation setting.

This script is a finite witness. It does not prove Busch/Gleason theorems.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import sqrt
from typing import Dict


def fstr(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def born_refinement_test() -> Dict[str, object]:
    # rho = diag(3/4, 1/4)
    p0 = Fraction(3, 4)
    p1 = Fraction(1, 4)

    # Fine POVM: E1 = 1/2 P0, E2 = 1/2 P0, E3 = P1.
    fine = (
        p0 * Fraction(1, 2),
        p0 * Fraction(1, 2),
        p1,
    )
    coarse_p0 = p0

    fine_sum = sum(fine, Fraction(0, 1))
    coarse_from_fine = fine[0] + fine[1]
    passed = (
        fine_sum == 1
        and coarse_from_fine == coarse_p0
    )
    return {
        "fine": fine,
        "fine_sum": fine_sum,
        "coarse_from_fine": coarse_from_fine,
        "coarse_direct": coarse_p0,
        "passed": passed,
    }


def nonlinear_context_rule_test() -> Dict[str, object]:
    # Same physical state and same effect P0, but compare two POVM refinements.
    p0 = Fraction(3, 4)
    p1 = Fraction(1, 4)

    fine_born = (
        p0 * Fraction(1, 2),
        p0 * Fraction(1, 2),
        p1,
    )
    fine_sq = tuple(v * v for v in fine_born)
    fine_norm = sum(fine_sq, Fraction(0, 1))
    fine_q = tuple(v / fine_norm for v in fine_sq)
    fine_p0_total = fine_q[0] + fine_q[1]

    coarse_born = (p0, p1)
    coarse_sq = tuple(v * v for v in coarse_born)
    coarse_norm = sum(coarse_sq, Fraction(0, 1))
    coarse_q = tuple(v / coarse_norm for v in coarse_sq)
    coarse_p0 = coarse_q[0]

    # A context-independent effect valuation must give the same value to P0
    # whether P0 is represented directly or as the sum of two coexistent effects.
    violates_gluing = fine_p0_total != coarse_p0
    return {
        "fine_q": fine_q,
        "fine_p0_total": fine_p0_total,
        "coarse_q": coarse_q,
        "coarse_p0": coarse_p0,
        "violates_gluing": violates_gluing,
        "passed": violates_gluing,
    }


def qubit_tomography_test() -> Dict[str, object]:
    # Choose a valid qubit Bloch vector r = (1/3, -1/4, 1/2).
    rx = Fraction(1, 3)
    ry = Fraction(-1, 4)
    rz = Fraction(1, 2)

    # For P_k^+ = (I + sigma_k)/2, Born valuation is (1 + r_k)/2.
    fx = (1 + rx) / 2
    fy = (1 + ry) / 2
    fz = (1 + rz) / 2

    # Reconstruct the Bloch vector from the three effect valuations.
    rx_rec = 2 * fx - 1
    ry_rec = 2 * fy - 1
    rz_rec = 2 * fz - 1

    r2 = rx * rx + ry * ry + rz * rz
    rnorm = sqrt(float(r2))
    eig_plus = (1 + rnorm) / 2
    eig_minus = (1 - rnorm) / 2

    passed = (
        (rx_rec, ry_rec, rz_rec) == (rx, ry, rz)
        and rnorm <= 1.0 + 1e-15
        and eig_minus >= -1e-15
    )

    return {
        "effect_values": (fx, fy, fz),
        "reconstructed_bloch": (rx_rec, ry_rec, rz_rec),
        "bloch_norm": rnorm,
        "density_eigenvalues": (eig_plus, eig_minus),
        "passed": passed,
    }


def additive_lift_absorption_test() -> Dict[str, object]:
    # Start from rho = diag(3/4, 1/4).
    rho = (Fraction(3, 4), Fraction(1, 4))

    # An additive normalized change represented by a traceless Hermitian shift.
    delta = Fraction(1, 20)
    rho_prime = (rho[0] + delta, rho[1] - delta)

    # Target effect P0.
    p_before = rho[0]
    p_after = rho_prime[0]
    delta_p = p_after - p_before

    # If rho' remains positive and normalized, the "lift" is not an extra
    # probability term: it is exactly a changed state representation.
    valid_density = (
        rho_prime[0] >= 0
        and rho_prime[1] >= 0
        and sum(rho_prime, Fraction(0, 1)) == 1
    )
    passed = valid_density and delta_p == delta

    return {
        "rho": rho,
        "rho_prime": rho_prime,
        "p_before": p_before,
        "p_after": p_after,
        "delta_p": delta_p,
        "passed": passed,
    }


def run_all() -> bool:
    a = born_refinement_test()
    b = nonlinear_context_rule_test()
    c = qubit_tomography_test()
    d = additive_lift_absorption_test()

    print("QM Core 003 — Effect valuation / Born representation")
    print()
    print("[1] Born coarse-graining consistency")
    print("    fine probabilities       :", tuple(fstr(x) for x in a["fine"]))
    print("    fine sum                 :", fstr(a["fine_sum"]))
    print("    refined P0 total         :", fstr(a["coarse_from_fine"]))
    print("    direct P0 value          :", fstr(a["coarse_direct"]))
    print("    RESULT                   :", "PASS" if a["passed"] else "FAIL")
    print()

    print("[2] Nonlinear context-normalized quadratic rule")
    print("    fine-context q           :", tuple(fstr(x) for x in b["fine_q"]))
    print("    P0 via refined context   :", fstr(b["fine_p0_total"]))
    print("    coarse-context q         :", tuple(fstr(x) for x in b["coarse_q"]))
    print("    P0 via coarse context    :", fstr(b["coarse_p0"]))
    print("    gluing violation         :", b["violates_gluing"])
    print("    RESULT                   :", "PASS" if b["passed"] else "FAIL")
    print()

    print("[3] Qubit valuation tomography")
    print("    f(Px+), f(Py+), f(Pz+)   :", tuple(fstr(x) for x in c["effect_values"]))
    print("    reconstructed Bloch      :", tuple(fstr(x) for x in c["reconstructed_bloch"]))
    print("    Bloch norm               :", f"{c['bloch_norm']:.12f}")
    print("    density eigenvalues      :", tuple(f"{x:.12f}" for x in c["density_eigenvalues"]))
    print("    RESULT                   :", "PASS" if c["passed"] else "FAIL")
    print()

    print("[4] Additive probability lift is a state shift")
    print("    rho                       :", tuple(fstr(x) for x in d["rho"]))
    print("    rho'                      :", tuple(fstr(x) for x in d["rho_prime"]))
    print("    p(P0) before -> after     :", f"{fstr(d['p_before'])} -> {fstr(d['p_after'])}")
    print("    delta p                   :", fstr(d["delta_p"]))
    print("    RESULT                    :", "PASS" if d["passed"] else "FAIL")
    print()

    overall = all(x["passed"] for x in (a, b, c, d))
    print("OVERALL:", "PASS_WITH_REFINEMENT" if overall else "FAIL")
    return overall


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "born", "nonlinear", "tomography", "lift"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode == "all":
        ok = run_all()
    elif args.mode == "born":
        result = born_refinement_test()
        print(result)
        ok = bool(result["passed"])
    elif args.mode == "nonlinear":
        result = nonlinear_context_rule_test()
        print(result)
        ok = bool(result["passed"])
    elif args.mode == "tomography":
        result = qubit_tomography_test()
        print(result)
        ok = bool(result["passed"])
    else:
        result = additive_lift_absorption_test()
        print(result)
        ok = bool(result["passed"])

    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
