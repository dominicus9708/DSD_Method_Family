#!/usr/bin/env python3
"""
DSD structural-support threshold interface audit.

Purpose
-------
Test what the already-recorded DSD structural-support criterion

    m_sup = lambda_min(H_full)

actually determines for a black-hole critical-radius program.

For a two-sector toy Hessian

    H = [[k_U, g],
         [g,   k_A]]

with positive diagonal stiffnesses, the support limit is

    lambda_min(H) = 0  <=>  g^2 = k_U k_A.

This yields a dimensionless marginality ratio

    eta = g^2/(k_U k_A)

with eta_* = 1.

Crucially, this does NOT determine the radial compactness threshold Theta_* in

    Theta_X = K_g M/(c_info^2 r).

An additional constitutive bridge eta = F(Theta_X) is required.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class HessianCase:
    k_u: float
    k_a: float
    g: float


def eigenvalues_2x2(case: HessianCase) -> tuple[float, float]:
    ku, ka, g = case.k_u, case.k_a, case.g
    trace = ku + ka
    disc = math.sqrt((ku - ka) ** 2 + 4.0 * g * g)
    return ((trace - disc) / 2.0, (trace + disc) / 2.0)


def support_margin(case: HessianCase) -> float:
    return eigenvalues_2x2(case)[0]


def eta(case: HessianCase) -> float:
    if case.k_u <= 0 or case.k_a <= 0:
        raise ValueError("k_u and k_a must be positive")
    return case.g * case.g / (case.k_u * case.k_a)


def critical_g(k_u: float, k_a: float) -> float:
    if k_u <= 0 or k_a <= 0:
        raise ValueError("k_u and k_a must be positive")
    return math.sqrt(k_u * k_a)


def theta_star_power_bridge(alpha: float, power: float) -> float:
    """
    Bridge family eta = alpha * Theta^power.
    eta_* = 1 implies Theta_* = alpha^(-1/power).
    """
    if alpha <= 0 or power <= 0:
        raise ValueError("alpha and power must be positive")
    return alpha ** (-1.0 / power)


def compute() -> dict:
    cases = []
    for ku, ka in [(1.0, 1.0), (2.0, 8.0), (0.5, 4.5), (3.0, 7.0)]:
        gc = critical_g(ku, ka)
        for factor in (0.8, 1.0, 1.2):
            case = HessianCase(ku, ka, factor * gc)
            lmin, lmax = eigenvalues_2x2(case)
            cases.append({
                **asdict(case),
                "g_over_gcrit": factor,
                "eta": eta(case),
                "lambda_min": lmin,
                "lambda_max": lmax,
            })

    bridge_examples = []
    for alpha, power in [
        (1.0, 1.0),
        (2.0, 1.0),
        (4.0, 2.0),
        (8.0, 3.0),
        (0.5, 1.0),
    ]:
        bridge_examples.append({
            "bridge": f"eta = {alpha:g} * Theta^{power:g}",
            "alpha": alpha,
            "power": power,
            "Theta_star_from_eta_eq_1": theta_star_power_bridge(alpha, power),
        })

    return {
        "support_definition": "m_sup = lambda_min(H_full)",
        "two_mode_threshold": "eta = g^2/(k_U k_A); support limit eta_* = 1",
        "cases": cases,
        "bridge_examples": bridge_examples,
        "conclusion": (
            "The spectral support criterion fixes eta_*=1, but Theta_* is "
            "underdetermined until an independent constitutive map "
            "eta=F(Theta_X) is supplied."
        ),
    }


def self_test(data: dict) -> None:
    threshold_cases = [
        x for x in data["cases"] if abs(x["g_over_gcrit"] - 1.0) < 1e-12
    ]
    assert threshold_cases
    for x in threshold_cases:
        assert abs(x["eta"] - 1.0) < 1e-12
        assert abs(x["lambda_min"]) < 1e-12

    for x in data["cases"]:
        if x["g_over_gcrit"] < 1.0:
            assert x["lambda_min"] > 0
        elif x["g_over_gcrit"] > 1.0:
            assert x["lambda_min"] < 0

    theta_values = {
        round(x["Theta_star_from_eta_eq_1"], 12)
        for x in data["bridge_examples"]
    }
    assert len(theta_values) > 1

    half = theta_star_power_bridge(alpha=2.0, power=1.0)
    assert abs(half - 0.5) < 1e-15


def report(data: dict) -> str:
    lines = [
        "DSD structural-support threshold interface audit",
        "================================================",
        "m_sup = lambda_min(H_full)",
        "Two-mode H = [[k_U,g],[g,k_A]]",
        "For k_U,k_A>0: lambda_min=0 iff g^2=k_U*k_A",
        "Define eta=g^2/(k_U*k_A): eta_*=1",
        "",
        "Representative checks:",
    ]
    for x in data["cases"]:
        lines.append(
            f"k_U={x['k_u']:g}, k_A={x['k_a']:g}, "
            f"g/gcrit={x['g_over_gcrit']:.1f}, "
            f"eta={x['eta']:.3f}, lambda_min={x['lambda_min']:.6g}"
        )
    lines += ["", "Constitutive bridge non-uniqueness:"]
    for x in data["bridge_examples"]:
        lines.append(
            f"{x['bridge']} -> Theta_*={x['Theta_star_from_eta_eq_1']:.6g}"
        )
    lines += [
        "",
        "RESULT:",
        "eta_*=1 is independently supported by the existing spectral support definition.",
        "Theta_* is NOT determined by that criterion alone.",
        "Theta_*=1/2 appears only if an additional bridge such as eta=2*Theta is supplied.",
        "Therefore the Schwarzschild coefficient 2 has not been independently recovered.",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all", "json", "test"), default="all")
    parser.add_argument("--json-out")
    args = parser.parse_args()

    data = compute()
    self_test(data)

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    if args.mode == "json":
        print(json.dumps(data, indent=2, ensure_ascii=False))
    elif args.mode == "test":
        print("PASS: all threshold-interface self-tests")
    else:
        print(report(data))
        print("\nPASS: all threshold-interface self-tests")


if __name__ == "__main__":
    main()
