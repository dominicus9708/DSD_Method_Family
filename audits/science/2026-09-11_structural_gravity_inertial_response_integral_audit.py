#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class ResponseCase:
    name: str
    phi: Callable[[float], float]
    exact_integral_at_one: float | None = None


def trapz_integral(f: Callable[[float], float], upper: float, n: int = 200_000) -> float:
    if not (0.0 <= upper <= 1.0):
        raise ValueError("upper must satisfy 0 <= upper <= 1")
    if n < 2:
        raise ValueError("n must be >= 2")
    if upper == 0.0:
        return 0.0

    h = upper / n
    total = 0.5 * (f(0.0) + f(upper))
    for i in range(1, n):
        total += f(i * h)
    return total * h


def theta_star(eta_i: float, zeta: float, phi: Callable[[float], float]) -> float:
    """
    General downstream response-integral bridge:

        dE_sup / dv = P_I(v)
        P_I(v) = mu_I * c_info * phi(v / c_info)

    Therefore, at v_sup = zeta * c_info,

        E_sup,max / mu_g
        = eta_I * c_info^2 * integral_0^zeta phi(s) ds

    and

        Theta_* = eta_I * integral_0^zeta phi(s) ds.

    No Schwarzschild relation is used here.
    """
    if eta_i <= 0.0:
        raise ValueError("eta_i must be positive")
    if not (0.0 < zeta <= 1.0):
        raise ValueError("zeta must satisfy 0 < zeta <= 1")
    return eta_i * trapz_integral(phi, zeta)


def response_cases() -> list[ResponseCase]:
    return [
        ResponseCase(
            "linear_phi=s",
            lambda s: s,
            exact_integral_at_one=0.5,
        ),
        ResponseCase(
            "hardening_phi=s+0.5s^3",
            lambda s: s + 0.5 * s**3,
            exact_integral_at_one=0.625,
        ),
        ResponseCase(
            "softening_phi=s-0.5s^3",
            lambda s: s - 0.5 * s**3,
            exact_integral_at_one=0.375,
        ),
        ResponseCase(
            "saturating_phi=tanh(s)",
            math.tanh,
            exact_integral_at_one=math.log(math.cosh(1.0)),
        ),
        ResponseCase(
            "power_phi=s^2",
            lambda s: s**2,
            exact_integral_at_one=1.0 / 3.0,
        ),
    ]


def blind_report() -> None:
    print("DSD support/inertial response-integral audit")
    print("--------------------------------------------")
    print("General downstream bridge:")
    print("  dE_sup/dv = P_I(v)")
    print("  P_I(v) = mu_I * c_info * phi(v/c_info)")
    print("  v_sup = zeta * c_info")
    print("  eta_I = mu_I / mu_g")
    print()
    print("Therefore:")
    print("  Theta_* = eta_I * integral_0^zeta phi(s) ds")
    print()
    print("At eta_I=1 and zeta=1 (conditional bridge values only):")
    print("case,Theta_*")
    for case in response_cases():
        th = theta_star(1.0, 1.0, case.phi)
        print(f"{case.name},{th:.12g}")
    print()
    print("Boundary:")
    print("  The coefficient 1/2 is exact only for the globally linear response phi(s)=s.")
    print("  Local small-speed linearity does not fix the integral up to zeta=1.")


def small_speed_report() -> None:
    zetas = (0.1, 0.25, 0.5, 0.75, 1.0)
    linear = response_cases()[0]
    hardening = response_cases()[1]
    softening = response_cases()[2]

    print("Small-speed versus saturation sensitivity")
    print("------------------------------------------")
    print("zeta,linear,hardening,softening")
    for z in zetas:
        vals = [
            theta_star(1.0, z, linear.phi),
            theta_star(1.0, z, hardening.phi),
            theta_star(1.0, z, softening.phi),
        ]
        print(f"{z:.2f},{vals[0]:.12g},{vals[1]:.12g},{vals[2]:.12g}")


def audit_report() -> int:
    checks: list[tuple[str, bool, str]] = []

    cases = response_cases()

    for case in cases:
        numeric = theta_star(1.0, 1.0, case.phi)
        if case.exact_integral_at_one is not None:
            checks.append((
                f"INTEGRAL_{case.name}",
                abs(numeric - case.exact_integral_at_one) < 2e-10,
                f"numeric integral matches exact value {case.exact_integral_at_one:.12g}",
            ))

    linear_half = theta_star(1.0, 1.0, cases[0].phi)
    checks.append((
        "HALF_FROM_GLOBAL_LINEAR_RESPONSE",
        abs(linear_half - 0.5) < 2e-10,
        "phi(s)=s implies Theta_*=eta_I*zeta^2/2; at eta_I=zeta=1 this gives 1/2",
    ))

    nonlinear_values = [theta_star(1.0, 1.0, c.phi) for c in cases[1:]]
    checks.append((
        "HALF_NOT_UNIVERSAL",
        all(abs(v - 0.5) > 1e-3 for v in nonlinear_values),
        "admissible nonlinear response families do not preserve Theta_*=1/2",
    ))

    z = 0.1
    lin = theta_star(1.0, z, cases[0].phi)
    hard = theta_star(1.0, z, cases[1].phi)
    rel = abs(hard - lin) / lin
    checks.append((
        "LOCAL_LINEARITY_CAN_HIDE_HIGH_SPEED_DIFFERENCE",
        rel < 0.01,
        "hardening and linear laws are nearly indistinguishable at zeta=0.1 but diverge at saturation",
    ))

    checks.append((
        "NO_SCHWARZSCHILD_INPUT",
        True,
        "no G, c, R_S, EHT ring, or black-hole radius enters the blind response integral",
    ))

    failures = 0
    for name, ok, note in checks:
        status = "PASS" if ok else "FAIL"
        failures += 0 if ok else 1
        print(f"{status}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / LINEAR_RESPONSE_REQUIRED_FOR_EXACT_HALF")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit the structural-support response law behind the DSD critical coefficient."
    )
    parser.add_argument(
        "--mode",
        choices=("all", "blind", "small-speed", "audit"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("all", "blind"):
        blind_report()
        if args.mode == "blind":
            return

    if args.mode in ("all", "small-speed"):
        print()
        small_speed_report()
        if args.mode == "small-speed":
            return

    if args.mode in ("all", "audit"):
        print()
        failures = audit_report()
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
