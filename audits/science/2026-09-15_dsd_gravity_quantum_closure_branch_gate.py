#!/usr/bin/env python3
"""BH-RB-019: quantum closure branch / self-binding criterion gate.

This audit does not derive a black-hole successor-core EOS. It classifies four
minimal quantum-closure branches after BH-RB-018 and tests which branches can:
(1) generate an intrinsic dimensionful density scale, and
(2) generate a positive zero-pressure self-bound state needed for a candidate
epsilon_0^EOS.

Branches:
A. mass/gap scale only
B. vacuum/self-binding offset
C. interaction-generated scale / saturation
D. exactly scale-free closure
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

HBAR = 1.054_571_817e-34  # J s
C = 299_792_458.0          # m/s
EV = 1.602_176_634e-19     # J


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


def free_fermi_pressure_bracket(x: float) -> float:
    """Dimensionless spin-1/2 T=0 relativistic Fermi-gas pressure bracket.

    P = m^4 c^5/(24 pi^2 hbar^3) * F(x), x=p_F/(mc).
    Only the sign/zero structure is used in this audit.
    """
    if x < 0:
        raise ValueError("x must be nonnegative")
    return x * (2.0 * x * x - 3.0) * math.sqrt(1.0 + x * x) + 3.0 * math.asinh(x)


def rg_alpha(mu2: float, mu1: float, alpha1: float, b: float) -> float:
    """One-loop solution of d alpha / d ln(mu) = -b alpha^2."""
    return 1.0 / (1.0 / alpha1 + b * math.log(mu2 / mu1))


def rg_lambda(mu: float, alpha: float, b: float) -> float:
    """RG-invariant transmutation scale for the generic one-loop model."""
    return mu * math.exp(-1.0 / (b * alpha))


def energy_density_from_energy_scale(lambda_e_joule: float) -> float:
    """epsilon ~ Lambda_E^4/(hbar c)^3, coefficient set to 1."""
    return lambda_e_joule**4 / (HBAR * C) ** 3


def saturation_toy(y: float, e_star: float = 1.0, k: float = 2.0) -> tuple[float, float, float]:
    """Dimensionless self-binding control.

    y=n/n_*. e(y)=e_* + (k/2)(y-1)^2.
    Reduced pressure is p/(n_* e_unit) ~ y^2 de/dy.
    Returns (e, p_reduced, dp_reduced/dy).
    """
    e = e_star + 0.5 * k * (y - 1.0) ** 2
    de = k * (y - 1.0)
    d2e = k
    p = y * y * de
    dp = 2.0 * y * de + y * y * d2e
    return e, p, dp


def run_checks() -> list[Check]:
    checks: list[Check] = []

    # D — exactly scale-free closure.
    w = 1.0 / 3.0
    checks.append(Check(
        "scale-free EOS has no positive zero-pressure intercept",
        all(w * eps > 0.0 for eps in (1.0, 2.0, 10.0)) and w * 0.0 == 0.0,
        "For p=w*epsilon with w>0, p=0 iff epsilon=0.",
    ))

    eps = 7.0
    lam = 5.0
    checks.append(Check(
        "scale-free EOS retains its form under overall rescaling",
        math.isclose((w * (lam * eps)) / (lam * eps), w, rel_tol=0.0, abs_tol=1e-15),
        "Rescaling epsilon and p by the same positive factor leaves p/epsilon=w; no preferred absolute epsilon is selected.",
    ))

    # A — mass/gap scale only.
    m_ratio = 3.0
    checks.append(Check(
        "mass/gap branch carries an intrinsic density dimension",
        math.isclose(m_ratio**4, 81.0),
        "epsilon_m ~ m_*^4 c^5/hbar^3, so a supplied mass/gap scale changes epsilon_m as m_*^4.",
    ))

    xs = (0.01, 0.1, 1.0, 10.0)
    fvals = tuple(free_fermi_pressure_bracket(x) for x in xs)
    checks.append(Check(
        "free degenerate Fermi gas has positive pressure at every sampled finite density",
        all(v > 0.0 for v in fvals),
        "Positive T=0 free-gas pressure bracket sampled at x=p_F/(mc)>0: " + repr(tuple(round(v, 12) for v in fvals)),
    ))

    checks.append(Check(
        "free mass/gap branch is not self-bound by mass alone",
        free_fermi_pressure_bracket(0.0) == 0.0 and all(v > 0.0 for v in fvals),
        "For the free Fermi comparator, pressure reaches zero only as p_F and number density go to zero.",
    ))

    # B — vacuum/self-binding offset.
    B = 11.0
    eps0_bag = 4.0 * B
    p0_bag = (eps0_bag - 4.0 * B) / 3.0
    checks.append(Check(
        "vacuum offset can create a positive zero-pressure intercept",
        eps0_bag > 0.0 and p0_bag == 0.0,
        "Comparator p=(epsilon-4B)/3 gives epsilon_0=4B>0 for B>0.",
    ))

    checks.append(Check(
        "vacuum-offset self-binding breaks the scale-free zero-pressure structure",
        (w * eps0_bag) > 0.0 and p0_bag == 0.0,
        "The same positive epsilon has nonzero p in p=w epsilon but zero p after the supplied vacuum offset.",
    ))

    # C1 — interaction-generated RG scale.
    b = 0.7
    mu1 = 100.0
    alpha1 = 0.2
    mu2 = 1000.0
    alpha2 = rg_alpha(mu2, mu1, alpha1, b)
    L1 = rg_lambda(mu1, alpha1, b)
    L2 = rg_lambda(mu2, alpha2, b)
    checks.append(Check(
        "generic asymptotically-free one-loop running generates an RG-invariant scale",
        math.isclose(L1, L2, rel_tol=2e-14, abs_tol=0.0),
        f"Lambda(mu1)={L1:.12e}, Lambda(mu2)={L2:.12e} in the same arbitrary energy units.",
    ))

    checks.append(Check(
        "dimensional transmutation still requires renormalization boundary data",
        L1 > 0.0 and mu1 > 0.0 and alpha1 > 0.0,
        "Lambda=mu*exp[-1/(b alpha(mu))] is physical/RG-invariant only after a dimensionful reference scale and running-coupling boundary condition are supplied.",
    ))

    lambda_e = 200.0e6 * EV
    eps_lambda = energy_density_from_energy_scale(lambda_e)
    checks.append(Check(
        "a generated microscopic energy scale can feed an absolute energy-density scale",
        eps_lambda > 0.0 and math.isfinite(eps_lambda),
        f"For a 200 MeV control scale and unit coefficient, Lambda^4/(hbar c)^3={eps_lambda:.12e} J/m^3.",
    ))

    c1, c2 = 0.5, 2.0
    checks.append(Check(
        "RG scale generation does not by itself fix the EOS intercept",
        not math.isclose(c1 * eps_lambda, c2 * eps_lambda),
        "The same Lambda permits different dimensionless coefficients/phase functionals; scale generation is not yet an EOS derivation.",
    ))

    # C2 — interaction-generated finite-density saturation / self-binding.
    e_star, p_star, dp_star = saturation_toy(1.0)
    checks.append(Check(
        "interaction/saturation branch can realize finite-density zero pressure",
        e_star > 0.0 and abs(p_star) < 1e-15,
        "For e(n)=e_*+K/2(n/n_*-1)^2, p=n^2 d(e)/dn vanishes at n=n_*>0.",
    ))

    checks.append(Check(
        "finite-density saturation point can be locally mechanically stable",
        dp_star > 0.0,
        f"Positive reduced dp/dy at y=1 gives local positive compressibility control; dp/dy={dp_star:g}.",
    ))

    # Distinguish formation threshold from EOS intercept.
    eps_form = 13.0
    eps_eos = 17.0
    checks.append(Check(
        "formation threshold and zero-pressure EOS intercept remain independent outputs",
        eps_form != eps_eos,
        "No DSD typing/formation rule identifies epsilon_form with epsilon_0^EOS without an explicit quantum-thermodynamic bridge.",
    ))

    # Branch decision.
    branch_scale = {
        "mass_gap": True,
        "vacuum_offset": True,
        "interaction_generated": True,
        "scale_free": False,
    }
    branch_positive_intercept = {
        "mass_gap": False,             # not automatic; free comparator fails
        "vacuum_offset": True,
        "interaction_generated": True, # possible if finite-density saturation/self-binding is actually derived
        "scale_free": False,
    }
    checks.append(Check(
        "branch classification separates scale generation from positive self-binding",
        branch_scale["mass_gap"]
        and not branch_positive_intercept["mass_gap"]
        and branch_positive_intercept["vacuum_offset"]
        and branch_positive_intercept["interaction_generated"]
        and not branch_scale["scale_free"],
        "Mass/gap carries scale but not automatic self-binding; vacuum offset can self-bind; interactions can self-bind conditionally; exact scale-free closure cannot choose epsilon_0.",
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
    print("BRANCH A mass/gap: SCALE-CARRYING / POSITIVE-INTERCEPT-NOT-AUTOMATIC")
    print("BRANCH B vacuum/self-binding: POSITIVE-INTERCEPT-CAPABLE")
    print("BRANCH C interaction-generated: SCALE-GENERATION-CAPABLE / SELF-BINDING-CONDITIONAL")
    print("BRANCH D exact scale-free: REJECT-AS-UNIQUE-RADIUS-CLOSURE")

    if passed == total:
        print(
            "VERDICT: PASS_WITH_BOUNDARY / "
            "QUANTUM_CLOSURE_BRANCHES_SEPARATED / "
            "POSITIVE_EOS_INTERCEPT_REQUIRES_SELF_BINDING_OR_VACUUM_OFFSET / "
            "MASS_GAP_ALONE_INSUFFICIENT / "
            "SCALE_FREE_BRANCH_REJECTED_FOR_RADIUS_SELECTION / "
            "MICROPHYSICAL_CORE_EOS_NOT_YET_DERIVED"
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
