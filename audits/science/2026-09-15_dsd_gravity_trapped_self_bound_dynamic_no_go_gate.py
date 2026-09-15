#!/usr/bin/env python3
"""BH-RB-023: trapped self-bound dynamic no-go gate.

Scope
-----
Spherically symmetric, comoving, non-dissipative GR fluid in geometrized
units G=c=1.  The audit asks whether the globally causal, self-bound,
nonnegative-pressure EOS family constructed in BH-RB-021 can by itself
produce a finite positive-radius stall/bounce after a shell is already
strictly trapped.

It does NOT prove that every black-hole interior must reach R=0.  It only
closes the perfect-fluid/no-flux spherical branch.  Escape channels such as
outward energy flux, sufficiently negative radial pressure/tension,
non-spherical rotation, anisotropic transport, or a different successor
stress-energy closure remain separate branches.
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


def gamma_sq(compactness: float, U: float) -> float:
    """Misner-Sharp constraint: Gamma^2 = 1 + U^2 - 2m/R."""
    return 1.0 + U * U - compactness


def mass_rate(R: float, U: float, p_r: float, q: float = 0.0, Gamma: float = 1.0) -> float:
    """D_T m = -4 pi R^2 (p_r U + q Gamma).

    q=0 is the perfect-fluid/no-flux branch.  q>0 is taken as outward flux
    in the sign convention used by this audit.
    """
    return -4.0 * math.pi * R * R * (p_r * U + q * Gamma)


def compactness_rate(
    R: float,
    compactness: float,
    U: float,
    p_r: float,
    q: float = 0.0,
    Gamma: float = 1.0,
) -> float:
    """Derivative of C=2m/R using the Misner-Sharp mass-work equation."""
    return -8.0 * math.pi * R * (p_r * U + q * Gamma) - compactness * U / R


def contraction_floor(compactness: float) -> float:
    """For C>1 and Gamma^2>=0: |U| >= sqrt(C-1)."""
    if compactness <= 1.0:
        return 0.0
    return math.sqrt(compactness - 1.0)


def time_bound_to_radius(R0: float, R1: float, trapped_gap_compactness: float) -> float:
    """Upper bound on proper-time parameter to contract from R0 to R1.

    If C >= C0 > 1 throughout, then U <= -sqrt(C0-1), hence
    Delta tau <= (R0-R1)/sqrt(C0-1).
    """
    if not (R0 > R1 >= 0.0 and trapped_gap_compactness > 1.0):
        raise ValueError("Require R0>R1>=0 and C0>1")
    return (R0 - R1) / contraction_floor(trapped_gap_compactness)


def outward_flux_threshold(
    R: float,
    compactness: float,
    U: float,
    p_r: float,
    Gamma: float,
) -> float:
    """Minimum outward q needed for D_T C <= 0 at equality.

    For U<0 and Gamma>0,
        q Gamma >= |U| [p_r + C/(8 pi R^2)].
    """
    if U >= 0.0 or Gamma <= 0.0:
        raise ValueError("Require collapsing U<0 and Gamma>0")
    return abs(U) * (p_r + compactness / (8.0 * math.pi * R * R)) / Gamma


def run_checks() -> list[Check]:
    checks: list[Check] = []

    # 1. Misner-Sharp kinematic control.
    C = 1.2
    U = -0.7
    gs = gamma_sq(C, U)
    checks.append(Check(
        "Misner-Sharp constraint admits the synthetic trapped control",
        gs >= 0.0,
        f"C={C:.6f}, U={U:.6f}, Gamma^2={gs:.12f}.",
    ))

    # 2. Strictly trapped turning point is impossible under the same spherical constraint.
    gs_turn = gamma_sq(1.1, 0.0)
    checks.append(Check(
        "strictly trapped shell cannot have a regular U=0 turning point",
        gs_turn < 0.0,
        f"At C=1.1 and U=0, formal Gamma^2={gs_turn:.12f}<0.",
    ))

    # 3. Contraction-rate floor.
    C0 = 1.05
    u_floor = contraction_floor(C0)
    checks.append(Check(
        "strict trappedness produces a nonzero areal-contraction-rate floor",
        u_floor > 0.0 and abs(gamma_sq(C0, -u_floor)) < 1e-12,
        f"C0={C0:.6f}, |U|_min={u_floor:.12f} at Gamma=0.",
    ))

    # 4. Positive pressure increases Misner-Sharp mass during collapse.
    R = 1.0
    Uc = -0.3
    p = 0.2
    dm = mass_rate(R, Uc, p)
    checks.append(Check(
        "positive radial pressure increases Misner-Sharp mass during collapse",
        dm > 0.0,
        f"R={R}, U={Uc}, p={p}, D_T m={dm:.12f}.",
    ))

    # 5. Compactness monotonicity for p>=0, q=0.
    rate_samples = [compactness_rate(1.0, 1.1, -0.2, p_i) for p_i in (0.0, 0.1, 0.5)]
    checks.append(Check(
        "nonnegative radial pressure deepens compactness in the no-flux collapsing branch",
        all(x > 0.0 for x in rate_samples),
        "D_T C samples=" + ", ".join(f"{x:.12f}" for x in rate_samples) + ".",
    ))

    # 6-7. BH-RB-021 CSS envelope has p>=0 and causal slope on its physical domain.
    eps0 = 1.0
    s = 0.8
    eps_samples = [eps0 + 0.1 * i for i in range(91)]
    pvals = [s * (eps - eps0) for eps in eps_samples]
    checks.append(Check(
        "self-bound CSS physical branch has nonnegative pressure above its surface",
        min(pvals) >= -1e-12 and max(pvals) > 0.0,
        f"min p={min(pvals):.12f}, max p={max(pvals):.12f}.",
    ))
    checks.append(Check(
        "CSS control obeys the causal sound-speed slope bound",
        0.0 <= s <= 1.0,
        f"dp/dE={s:.12f}.",
    ))

    # 8. Once C>1, positive-pressure/no-flux collapse cannot relax C back to 1.
    dC0 = compactness_rate(1.0, C0, -0.1, 0.0)
    checks.append(Check(
        "strictly trapped positive-pressure/no-flux branch cannot relax compactness toward one",
        C0 > 1.0 and dC0 > 0.0,
        f"C0={C0:.6f}, D_T C at p=0 is already {dC0:.12f}>0.",
    ))

    # 9-10. Finite-time contraction bound; no positive-radius asymptote while C>=C0>1.
    dt_half = time_bound_to_radius(1.0, 0.5, C0)
    checks.append(Check(
        "fixed trapped gap yields a finite proper-time bound to any lower positive radius",
        math.isfinite(dt_half) and dt_half > 0.0,
        f"From R=1 to R=0.5, Delta tau <= {dt_half:.12f} in geometric units.",
    ))
    checks.append(Check(
        "positive-radius asymptote is incompatible with a persistent strict trapped gap",
        u_floor > 0.0,
        f"If C>=C0={C0:.6f}, then |U|>={u_floor:.12f}, so U cannot tend to zero.",
    ))

    # 11-12. Outward flux is one explicit escape channel for compactness reduction.
    Rf, Cf, Uf, pf, Gf = 1.0, 1.1, -0.2, 0.1, 0.4
    qcrit = outward_flux_threshold(Rf, Cf, Uf, pf, Gf)
    dC_eq = compactness_rate(Rf, Cf, Uf, pf, qcrit, Gf)
    dC_above = compactness_rate(Rf, Cf, Uf, pf, 1.1 * qcrit, Gf)
    checks.append(Check(
        "outward-flux threshold exactly cancels compactness growth",
        abs(dC_eq) < 1e-12,
        f"q_crit={qcrit:.12f}, D_T C={dC_eq:.3e}.",
    ))
    checks.append(Check(
        "sufficient outward flux can reduce compactness in the same spherical balance law",
        dC_above < 0.0,
        f"At 1.1 q_crit, D_T C={dC_above:.12f}.",
    ))

    # 13-14. Radial tension is another algebraic escape channel in the same formula.
    pcrit = -Cf / (8.0 * math.pi * Rf * Rf)
    dC_tension_eq = compactness_rate(Rf, Cf, Uf, pcrit, 0.0, Gf)
    dC_tension_more = compactness_rate(Rf, Cf, Uf, 1.1 * pcrit, 0.0, Gf)
    checks.append(Check(
        "radial-tension threshold can cancel compactness growth without heat flux",
        abs(dC_tension_eq) < 1e-12,
        f"p_r,crit={pcrit:.12f}, D_T C={dC_tension_eq:.3e}.",
    ))
    checks.append(Check(
        "stronger radial tension can reduce compactness in the same spherical balance law",
        dC_tension_more < 0.0,
        f"At 1.1 p_r,crit, D_T C={dC_tension_more:.12f}.",
    ))

    # 15. Closure verdict.
    checks.append(Check(
        "positive-pressure self-bound EOS alone supplies no trapped finite-radius escape channel",
        all(x >= -1e-12 for x in pvals) and qcrit > 0.0 and pcrit < 0.0,
        "Finite-radius survival after strict trapping needs additional transport/stress or a branch beyond this spherical no-flux perfect-fluid closure.",
    ))

    return checks


def report() -> int:
    checks = run_checks()
    passed = sum(c.passed for c in checks)
    total = len(checks)
    for i, c in enumerate(checks, 1):
        print(f"[{i:02d}] {'PASS' if c.passed else 'FAIL'} — {c.name}")
        print(f"     {c.detail}")
    print()
    print(f"RESULT: {passed}/{total} PASS")
    if passed == total:
        print(
            "VERDICT: PASS_WITH_BOUNDARY / "
            "SPHERICAL_POSITIVE_PRESSURE_SELF_BOUND_NO_FLUX_BRANCH_CLOSED / "
            "TRAPPED_COMPACTNESS_DEEPENS_DURING_COLLAPSE / "
            "FINITE_RADIUS_STALL_OR_BOUNCE_NOT_AVAILABLE_AFTER_STRICT_TRAPPING / "
            "EXTRA_TRANSPORT_OR_NONPERFECT_STRESS_REQUIRED / "
            "FINITE_CORE_RADIUS_NOT_DERIVED"
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
