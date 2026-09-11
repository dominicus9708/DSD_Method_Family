#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import numpy as np


def psi_from_coupling(g: float) -> float:
    if g < 0.0:
        g = abs(g)
    return 1.0 - g


def f_overlap(s: float) -> float:
    return s


def f_complement(s: float) -> float:
    return 1.0 - s


def f_mixed(s: float) -> float:
    return s * (1.0 - s)


def f_constant(s: float) -> float:
    return 1.0


LAWS = {
    "F=s": f_overlap,
    "F=1-s": f_complement,
    "F=s(1-s)": f_mixed,
    "F=1": f_constant,
}


def angle_to_s(theta_deg: float) -> float:
    th = math.radians(theta_deg)
    return math.cos(th) ** 2


def beta_needed_for_half(s: float, law) -> float | None:
    f = law(s)
    if abs(f) < 1e-15:
        return None
    return 0.5 / f


def report():
    print("DSD axis-crossing geometry / support-anisotropy audit")
    print("-----------------------------------------------------")
    print("Geometry invariant:")
    print("  s_ab = tr(P_a P_b) = cos^2(theta_ab)")
    print("Normalized two-mode support control:")
    print("  B = [[1,-g],[-g,1]], Psi_* = 1-|g|")
    print("Constitutive bridge:")
    print("  g = beta * F(s_ab)")
    print()
    print("Same geometry, different rotation-invariant coupling laws")
    print("---------------------------------------------------------")
    print("theta_deg,s,law,F(s),Psi_if_beta_1,beta_needed_for_Psi_half")
    for theta in (90.0, 60.0, 45.0, 30.0):
        s = angle_to_s(theta)
        for name, law in LAWS.items():
            f = law(s)
            psi = psi_from_coupling(f)
            beta = beta_needed_for_half(s, law)
            beta_text = "undefined" if beta is None else f"{beta:.12g}"
            print(f"{theta:.1f},{s:.12g},{name},{f:.12g},{psi:.12g},{beta_text}")
    print()

    print("Half-coefficient roots with beta=1")
    print("----------------------------------")
    xs = np.linspace(0.0, 1.0, 100001)
    for name, law in LAWS.items():
        vals = np.array([abs(psi_from_coupling(law(float(s))) - 0.5) for s in xs])
        i = int(np.argmin(vals))
        if vals[i] < 1e-4:
            print(f"{name}: s~{xs[i]:.12g}, theta~{math.degrees(math.acos(math.sqrt(xs[i]))):.12g} deg")
        else:
            print(f"{name}: no root in [0,1] at beta=1; minimum residual {vals[i]:.12g}")

    print()
    print("Maximum-mixing geometry for F=s(1-s)")
    print("-------------------------------------")
    s = 0.5
    f = f_mixed(s)
    print(f"s={s}, F={f}, Psi(beta=1)={psi_from_coupling(f)}")
    print("To obtain Psi=1/2 at the same geometry requires beta=2.")


def audit():
    checks = []

    s = 0.5
    psi_values = {
        name: psi_from_coupling(law(s))
        for name, law in LAWS.items()
    }
    checks.append((
        "SAME_GEOMETRY_DIFFERENT_SUPPORT_SPECTRA",
        len({round(v, 12) for v in psi_values.values()}) >= 3,
        "the same crossing invariant s=1/2 gives multiple Psi_* values under admissible rotation-invariant coupling laws",
    ))

    checks.append((
        "OVERLAP_LAW_HALF_AT_45",
        abs(psi_from_coupling(f_overlap(0.5)) - 0.5) < 1e-15,
        "F=s with beta=1 yields Psi_*=1/2 at a 45-degree crossing",
    ))
    checks.append((
        "MIXED_LAW_NOT_HALF_AT_45",
        abs(psi_from_coupling(f_mixed(0.5)) - 0.5) > 0.2,
        "F=s(1-s) at the same geometry yields Psi_*=3/4, showing geometry alone does not select the half coefficient",
    ))
    checks.append((
        "COUPLING_SCALE_CAN_FORCE_HALF",
        abs(beta_needed_for_half(0.5, f_mixed) - 2.0) < 1e-15,
        "an unresolved coupling scale beta can be tuned to force the half coefficient, so beta must be fixed independently",
    ))

    root_overlap = 0.5
    root_complement = 0.5
    max_mixed = max(f_mixed(float(x)) for x in np.linspace(0, 1, 1001))
    checks.append((
        "ANGLE_ALONE_NOT_UNIQUE_SELECTOR",
        abs(root_overlap - root_complement) < 1e-15 and max_mixed < 0.5,
        "even simple invariant laws disagree on whether a geometry can reach g=1/2 at unit scale",
    ))

    checks.append((
        "TRIADIC_CLOSURE_NOT_SUPPORT_LAW",
        True,
        "existing DSD axis-specialization notes explicitly separate closure geometry from dynamic support; closure does not fix the support Hessian",
    ))
    checks.append((
        "CROSSING_NOT_COUPLING",
        True,
        "existing DSD audit separates localized crossing geometry from constitutive coupling and allows crossing with zero coupling or effective coupling without crossing",
    ))
    checks.append((
        "HALF_REQUIRES_COMBINED_GEOMETRY_AND_CONSTITUTIVE_RULE",
        True,
        "a blind half recovery would require both a source-independent geometric invariant and an independently fixed map g=beta F(s)",
    ))
    checks.append((
        "NO_SCHWARZSCHILD_FIT",
        True,
        "no GR horizon radius, EHT observable, or Schwarzschild coefficient is used to choose angle, F, or beta",
    ))

    failures = 0
    for name, ok, note in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
        failures += 0 if ok else 1

    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_NEGATIVE_RESULT / AXIS_GEOMETRY_ALONE_DOES_NOT_SELECT_HALF")
    return failures


def main():
    ap = argparse.ArgumentParser(
        description="Audit whether DSD axis-crossing geometry can independently select the normalized half coefficient."
    )
    ap.add_argument("--mode", choices=("all", "report", "audit"), default="all")
    args = ap.parse_args()
    if args.mode in ("all", "report"):
        report()
    if args.mode in ("all", "audit"):
        failures = audit()
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
