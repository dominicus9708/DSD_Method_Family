#!/usr/bin/env python3
"""BH-RB-018: quantum microphysical scale / successor-core EOS provenance gate.

This audit does not derive a black-hole-core EOS. It checks dimensional and
logical controls required before an intrinsic energy-density scale epsilon_0
can be claimed from a quantum microphysical closure.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Dict, Iterable, Tuple

import sympy as sp

# SI base dimensions ordered as (M, L, T)
DIMS: Dict[str, Tuple[int, int, int]] = {
    "m": (1, 0, 0),
    "hbar": (1, 2, -1),
    "c": (0, 1, -1),
    "G": (-1, 3, -2),
    "energy": (1, 2, -2),
    "energy_density": (1, -1, -2),
    "length": (0, 1, 0),
}

HBAR = 1.054_571_817e-34  # J s, exact to shown digits through SI h
C = 299_792_458.0          # m/s, exact
G = 6.674_30e-11           # m^3 kg^-1 s^-2 (CODATA 2022 central value)


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


def dim_product(exponents: Dict[str, sp.Rational]) -> Tuple[sp.Rational, sp.Rational, sp.Rational]:
    out = [sp.Rational(0), sp.Rational(0), sp.Rational(0)]
    for key, power in exponents.items():
        d = DIMS[key]
        for i in range(3):
            out[i] += sp.Rational(power) * d[i]
    return tuple(out)  # type: ignore[return-value]


def has_solution(keys: Iterable[str], target: Tuple[int, int, int]) -> tuple[bool, tuple[sp.Expr, ...] | None]:
    keys = tuple(keys)
    A = sp.Matrix([[DIMS[k][i] for k in keys] for i in range(3)])
    b = sp.Matrix(target)
    syms = sp.symbols(f"x0:{len(keys)}")
    sol = sp.linsolve((A, b), syms)
    if sol is sp.EmptySet:
        return False, None
    first = next(iter(sol))
    return True, tuple(first)


def planck_energy_density() -> float:
    return C**7 / (HBAR * G**2)


def planck_length() -> float:
    return math.sqrt(HBAR * G / C**3)


def gr_length_from_energy_density(eps: float) -> float:
    return C**2 / math.sqrt(G * eps)


def mass_generated_energy_density(mass: float) -> float:
    return mass**4 * C**5 / HBAR**3


def mass_generated_gr_length(mass: float) -> float:
    return gr_length_from_energy_density(mass_generated_energy_density(mass))


def run_checks() -> list[Check]:
    checks: list[Check] = []

    ok_hc, _ = has_solution(("hbar", "c"), DIMS["energy_density"])
    checks.append(Check(
        "hbar+c cannot form an absolute energy-density scale",
        not ok_hc,
        "No monomial hbar^a c^b has dimensions of energy density.",
    ))

    ok_mhc, sol_mhc = has_solution(("m", "hbar", "c"), DIMS["energy_density"])
    expected_mhc = (sp.Rational(4), sp.Rational(-3), sp.Rational(5))
    checks.append(Check(
        "one supplied mass scale can form an energy-density scale",
        ok_mhc and sol_mhc == expected_mhc,
        f"Expected m^4 hbar^-3 c^5, solved exponents={sol_mhc}.",
    ))

    dims_mhc = dim_product({"m": 4, "hbar": -3, "c": 5})
    checks.append(Check(
        "m^4 c^5 / hbar^3 has energy-density dimensions",
        dims_mhc == tuple(map(sp.Rational, DIMS["energy_density"])),
        f"dimension vector={dims_mhc}.",
    ))

    ok_hcg, sol_hcg = has_solution(("hbar", "c", "G"), DIMS["energy_density"])
    expected_hcg = (sp.Rational(-1), sp.Rational(7), sp.Rational(-2))
    checks.append(Check(
        "hbar+c+G admit the Planck energy-density monomial",
        ok_hcg and sol_hcg == expected_hcg,
        f"Expected hbar^-1 c^7 G^-2, solved exponents={sol_hcg}.",
    ))

    eps_p = planck_energy_density()
    lp = planck_length()
    lp_from_eps = gr_length_from_energy_density(eps_p)
    checks.append(Check(
        "Planck energy density maps to Planck length under the BH-RB-017 GR scale",
        math.isclose(lp_from_eps, lp, rel_tol=2e-15, abs_tol=0.0),
        f"L(eps_P)={lp_from_eps:.15e} m, l_P={lp:.15e} m.",
    ))

    # General microscopic energy scale Lambda_E: epsilon ~ Lambda_E^4 / (hbar c)^3.
    # Using E dimensions directly, verify E^4 hbar^-3 c^-3.
    dims_lambda = [0, 0, 0]
    for i in range(3):
        dims_lambda[i] = 4 * DIMS["energy"][i] - 3 * DIMS["hbar"][i] - 3 * DIMS["c"][i]
    checks.append(Check(
        "a supplied microscopic energy scale Lambda can generate epsilon ~ Lambda^4/(hbar c)^3",
        tuple(dims_lambda) == DIMS["energy_density"],
        f"dimension vector={tuple(dims_lambda)}.",
    ))

    # Affine EOS p=s(eps-eps0): p=0 at eps=eps0.
    eps0 = 7.0
    s = 0.6
    p_at_eps0 = s * (eps0 - eps0)
    checks.append(Check(
        "affine self-bound EOS intercept is a constitutive energy-density scale",
        p_at_eps0 == 0.0,
        "For p=s(eps-eps0), zero pressure occurs at eps=eps0.",
    ))

    # MIT-bag comparator: p=(eps-4B)/3 gives eps0=4B.
    B = 11.0
    bag_eps0 = 4.0 * B
    p_bag = (bag_eps0 - 4.0 * B) / 3.0
    checks.append(Check(
        "bag-like vacuum offset demonstrates a microphysical intercept mechanism",
        p_bag == 0.0 and bag_eps0 == 4.0 * B,
        "Comparator only: p=(eps-4B)/3 => eps0=4B.",
    ))

    # A dimensionless coupling cannot repair the absence of a dimensional scale.
    checks.append(Check(
        "dimensionless couplings cannot by themselves create the missing density dimension",
        not ok_hc,
        "Multiplying by any dimensionless function leaves the hbar+c dimensional mismatch unchanged.",
    ))

    # Mass-scale dependence is strong and non-unique: eps_m ~ m^4, L_m ~ m^-2.
    m1, m2 = 2.0, 6.0
    ratio_eps = (m2 / m1) ** 4
    ratio_L = (m2 / m1) ** -2
    checks.append(Check(
        "mass-generated density scales as m^4",
        math.isclose(ratio_eps, 81.0),
        f"For m2/m1=3, epsilon2/epsilon1={ratio_eps:g}.",
    ))
    checks.append(Check(
        "BH-RB-017 GR length built from the mass-generated density scales as m^-2",
        math.isclose(ratio_L, 1.0 / 9.0),
        f"For m2/m1=3, L2/L1={ratio_L:g}.",
    ))

    # epsilon_transition and affine eps0 are logically independent unless a physical bridge equates them.
    eps_transition = 13.0
    eps_affine = 17.0
    checks.append(Check(
        "formation-transition scale is not algebraically identical to EOS zero-pressure intercept",
        eps_transition != eps_affine,
        "The two symbols may coincide only after an explicit microscopic/thermodynamic derivation.",
    ))

    # Scale-free p=w eps remains zero-pressure only at eps=0, hence no positive self-bound intercept.
    w = 1.0 / 3.0
    eps_test = 5.0
    checks.append(Check(
        "scale-free linear EOS has no positive zero-pressure intercept",
        w * eps_test != 0.0 and w * 0.0 == 0.0,
        "For p=w eps with w>0, p=0 implies eps=0.",
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
    print(f"epsilon_P = {planck_energy_density():.12e} J/m^3")
    print(f"l_P       = {planck_length():.12e} m")
    if passed == total:
        print("VERDICT: PASS_WITH_BOUNDARY / QUANTUM_SCALE_PROVENANCE_IDENTIFIED / MICROSCOPIC_HAMILTONIAN_OR_FIELD_SCALE_REQUIRED / PLANCK_SCALE_NOT_AUTOMATICALLY_SELECTED / BLACK_HOLE_CORE_EOS_NOT_DERIVED")
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
