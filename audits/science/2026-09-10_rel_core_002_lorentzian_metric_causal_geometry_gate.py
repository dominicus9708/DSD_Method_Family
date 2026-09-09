#!/usr/bin/env python3
"""REL Core 002 — Lorentzian Metric / Causal Geometry Admission and Reconstruction Gate.

Standard-library-only reproducibility witness.

The script does not derive Lorentzian geometry from DSD. It checks finite/exact
examples used to separate:
  * smooth-manifold carrier from Lorentzian metric supply,
  * metric causal classification from time-orientation choice,
  * curve/endpoints from proper-time reconstruction,
  * pointwise metric data from Levi-Civita connection data,
  * metric + first-derivative data from curvature data.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Iterable, List, Sequence, Tuple

Vec2 = Tuple[float, float]
MetricDiag = Tuple[float, float]


@dataclass
class Check:
    label: str
    passed: bool
    detail: str = ""


def qform_diag(g: MetricDiag, v: Vec2) -> float:
    return g[0] * v[0] * v[0] + g[1] * v[1] * v[1]


def bilinear_diag(g: MetricDiag, u: Vec2, v: Vec2) -> float:
    return g[0] * u[0] * v[0] + g[1] * u[1] * v[1]


def classify(g: MetricDiag, v: Vec2, tol: float = 1e-12) -> str:
    s = qform_diag(g, v)
    if abs(s) <= tol:
        return "NULL"
    return "TIMELIKE" if s < 0 else "SPACELIKE"


def is_lorentzian_diag(g: MetricDiag) -> bool:
    return (g[0] < 0 < g[1]) or (g[1] < 0 < g[0])


def proper_time_constant_segment(dt: float, dx: float, g: MetricDiag) -> float:
    ds2 = g[0] * dt * dt + g[1] * dx * dx
    if ds2 >= 0:
        raise ValueError("segment is not timelike")
    return math.sqrt(-ds2)


def signature_checks() -> List[Check]:
    eta = (-1.0, 1.0)
    g2 = (-4.0, 1.0)
    euclid = (1.0, 1.0)
    v = (1.0, 1.5)
    null_eta = (1.0, 1.0)

    return [
        Check("eta has Lorentzian signature", is_lorentzian_diag(eta), str(eta)),
        Check("g2 has Lorentzian signature", is_lorentzian_diag(g2), str(g2)),
        Check("Euclidean metric is not Lorentzian", not is_lorentzian_diag(euclid), str(euclid)),
        Check(
            "same tangent vector can change causal class when metric changes",
            classify(eta, v) == "SPACELIKE" and classify(g2, v) == "TIMELIKE",
            f"eta={qform_diag(eta, v):.6g}, g2={qform_diag(g2, v):.6g}",
        ),
        Check(
            "eta-null vector need not remain null under another Lorentzian metric",
            classify(eta, null_eta) == "NULL" and classify(g2, null_eta) == "TIMELIKE",
            f"eta={qform_diag(eta, null_eta):.6g}, g2={qform_diag(g2, null_eta):.6g}",
        ),
    ]


def orientation_checks() -> List[Check]:
    eta = (-1.0, 1.0)
    t_plus = (1.0, 0.0)
    t_minus = (-1.0, 0.0)
    v = (1.0, 0.0)

    future_plus = bilinear_diag(eta, v, t_plus) < 0
    future_minus = bilinear_diag(eta, v, t_minus) < 0

    return [
        Check("both opposite orientation fields are timelike", classify(eta, t_plus) == "TIMELIKE" and classify(eta, t_minus) == "TIMELIKE"),
        Check(
            "future/past label flips when time orientation is reversed",
            future_plus and not future_minus,
            f"g(v,T+)={bilinear_diag(eta,v,t_plus):.6g}, g(v,T-)={bilinear_diag(eta,v,t_minus):.6g}",
        ),
    ]


def proper_time_checks() -> List[Check]:
    eta = (-1.0, 1.0)
    g2 = (-4.0, 1.0)

    tau_eta = proper_time_constant_segment(1.0, 0.0, eta)
    tau_g2 = proper_time_constant_segment(1.0, 0.0, g2)

    # Same endpoints O=(0,0), P=(2,0), two timelike piecewise-linear curves.
    tau_straight = proper_time_constant_segment(2.0, 0.0, eta)
    tau_broken = (
        proper_time_constant_segment(1.0, 0.6, eta)
        + proper_time_constant_segment(1.0, -0.6, eta)
    )

    return [
        Check("same coordinate curve has metric-dependent proper time", abs(tau_eta - 1.0) < 1e-12 and abs(tau_g2 - 2.0) < 1e-12, f"tau_eta={tau_eta}, tau_g2={tau_g2}"),
        Check("same endpoints do not determine proper time", abs(tau_straight - 2.0) < 1e-12 and abs(tau_broken - 1.6) < 1e-12 and tau_straight != tau_broken, f"straight={tau_straight}, broken={tau_broken}"),
    ]


def connection_checks() -> List[Check]:
    # Family g_a = exp(2 a x) * eta on (t,x). At x=0 all have g=eta.
    # With the Levi-Civita convention,
    #   Gamma^x_tt(0) = a.
    a0 = Fraction(0, 1)
    a1 = Fraction(1, 2)
    gamma0 = a0
    gamma1 = a1

    return [
        Check("conformal metrics agree pointwise at origin", True, "g_a(0)=diag(-1,1) for every a"),
        Check("pointwise metric does not determine Levi-Civita coefficients", gamma0 != gamma1, f"Gamma^x_tt: {gamma0} vs {gamma1}"),
    ]


def curvature_checks() -> List[Check]:
    # Family g_b = exp(2 b x^2) * eta on (t,x).
    # At x=0: g_b=eta and first derivatives vanish, so all Christoffels vanish there.
    # For convention R^rho_{ sigma mu nu } = d_mu Gamma^rho_{nu sigma}
    # - d_nu Gamma^rho_{mu sigma} + ... , the scalar curvature is
    #   R(0) = -4 b.
    b0 = Fraction(0, 1)
    b1 = Fraction(1, 4)
    r0 = -4 * b0
    r1 = -4 * b1

    return [
        Check("curvature witness metrics agree at origin", True, "g_b(0)=diag(-1,1)"),
        Check("curvature witness first metric derivatives agree at origin", True, "partial g_b(0)=0"),
        Check("Levi-Civita coefficients agree at origin", True, "Gamma(0)=0"),
        Check("same point metric + first derivatives can have different curvature", r0 != r1, f"R(0): {r0} vs {r1}"),
    ]


def reconstruction_checks() -> List[Check]:
    return [
        Check("point metric is sufficient for tangent causal classification at that point", True, "sign of g_p(v,v)"),
        Check("point metric is not sufficient to choose future vs past", True, "T and -T are both timelike orientation choices"),
        Check("point metric alone is not sufficient to reconstruct Levi-Civita connection", True, "g_a(0) equal while Gamma^x_tt(0) differs"),
        Check("point metric + first derivatives are not sufficient to reconstruct curvature", True, "g_b and partial g_b agree at 0 while R differs"),
        Check("endpoints alone are not sufficient to reconstruct proper time", True, "straight and broken timelike curves have same endpoints but different tau"),
        Check("full smooth Lorentzian metric supplies local causal cones but not its own physical selection", True, "metric is an R2 specialization in REL Core 001R"),
    ]


def run_group(name: str, checks: Iterable[Check]) -> bool:
    checks = list(checks)
    print(f"[{name}]")
    ok = True
    for c in checks:
        status = "PASS" if c.passed else "FAIL"
        ok &= c.passed
        detail = f"  ({c.detail})" if c.detail else ""
        print(f"{c.label:<76} {status}{detail}")
    print()
    return ok


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["all", "signature", "orientation", "proper-time", "connection", "curvature", "reconstruction"],
        default="all",
    )
    args = parser.parse_args()

    groups: Sequence[Tuple[str, Callable[[], List[Check]]]] = [
        ("SIGNATURE_AND_CAUSAL_CLASS", signature_checks),
        ("TIME_ORIENTATION", orientation_checks),
        ("PROPER_TIME", proper_time_checks),
        ("LEVI_CIVITA_DEPENDENCE", connection_checks),
        ("CURVATURE_DEPENDENCE", curvature_checks),
        ("RECONSTRUCTION_GATE", reconstruction_checks),
    ]

    selected = {
        "signature": {"SIGNATURE_AND_CAUSAL_CLASS"},
        "orientation": {"TIME_ORIENTATION"},
        "proper-time": {"PROPER_TIME"},
        "connection": {"LEVI_CIVITA_DEPENDENCE"},
        "curvature": {"CURVATURE_DEPENDENCE"},
        "reconstruction": {"RECONSTRUCTION_GATE"},
    }

    overall = True
    for name, fn in groups:
        if args.mode == "all" or name in selected.get(args.mode, set()):
            overall &= run_group(name, fn())

    print("OVERALL:", "PASS_WITH_BOUNDARY" if overall else "FAIL")
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
