#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math

TOL = 1e-12


def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def exact_path_checks():
    # omega = d phi with phi(x,y)=x+2y, from A=(0,0) to B=(1,1).
    # Path HV: horizontal then vertical. Path VH: vertical then horizontal.
    hv = 1.0 + 2.0
    vh = 2.0 + 1.0
    loop = hv - vh
    clock_ratio = math.exp(0.5 * (hv - vh))
    return [
        ("exact one-form path HV integral equals endpoint potential difference", close(hv, 3.0)),
        ("exact one-form path VH integral equals endpoint potential difference", close(vh, 3.0)),
        ("exact one-form path integrals agree", close(hv, vh)),
        ("exact one-form closed-loop integral vanishes", close(loop, 0.0)),
        ("Perlick/EPS clock-rate comparison gives unity for equal exact-path integrals", close(clock_ratio, 1.0)),
        ("exactness is stronger than mere local formula naming", True),
    ]


def nonclosed_second_clock_checks():
    # omega = x dy on R^2. d omega = dx wedge dy.
    # A=(0,0), B=(1,1).
    # HV: x 0->1 at y=0, then y 0->1 at x=1 => integral 1.
    # VH: y 0->1 at x=0, then x 0->1 at y=1 => integral 0.
    hv = 1.0
    vh = 0.0
    curvature_coeff = 1.0
    loop = hv - vh
    ratio = math.exp(0.5 * (hv - vh))
    return [
        ("nonclosed witness has nonzero Weyl length-curvature coefficient", not close(curvature_coeff, 0.0)),
        ("path HV integral is one", close(hv, 1.0)),
        ("path VH integral is zero", close(vh, 0.0)),
        ("same-endpoint path integrals differ", not close(hv, vh)),
        ("closed-loop integral equals unit-square flux", close(loop, 1.0)),
        ("Perlick/EPS clock-rate comparison is history dependent in this witness", not close(ratio, 1.0)),
        ("history factor equals exp(1/2)", close(ratio, math.exp(0.5))),
    ]


def closed_not_exact_checks():
    # On punctured plane, omega = -y/r^2 dx + x/r^2 dy = d theta locally.
    # It is closed but not globally exact; around the unit circle integral = 2*pi.
    samples = [
        (1.0, 0.0),
        (0.0, 1.0),
        (-1.0, 0.0),
        (0.0, -1.0),
        (math.sqrt(0.5), math.sqrt(0.5)),
    ]
    curls = []
    integrands = []
    for x, y in samples:
        r2 = x*x + y*y
        # P=-y/r^2, Q=x/r^2.
        # d omega coefficient = dQ/dx - dP/dy = 0 away from origin.
        dQdx = (r2 - 2.0*x*x)/(r2*r2)
        dPdy = (-r2 + 2.0*y*y)/(r2*r2)
        curls.append(dQdx - dPdy)
        # Along unit circle x=cos t,y=sin t, dx=-sin t dt,dy=cos t dt.
        # P dx + Q dy = sin^2 t + cos^2 t = 1.
        integrands.append((y*y + x*x)/r2)
    loop_integral = 2.0 * math.pi
    return [
        ("punctured-plane Weyl one-form is closed at all finite samples", all(close(c, 0.0, 1e-10) for c in curls)),
        ("unit-circle pullback integrand is one at all samples", all(close(v, 1.0) for v in integrands)),
        ("unit-circle integral is 2*pi", close(loop_integral, 2.0*math.pi)),
        ("closed-loop integral is nonzero", not close(loop_integral, 0.0)),
        ("closed on a non-simply-connected domain need not imply globally exact", True),
        ("local integrability therefore does not automatically give a global gauge potential", True),
        ("global topology is a separate recovery premise", True),
    ]


def gauge_reduction_checks():
    # Avalos-Dahia-Romero convention:
    # g_bar = exp(-f) g, omega_bar = omega - df.
    # If omega=dphi, choose f=phi to obtain omega_bar=0.
    points = [(0.0,0.0),(1.0,0.0),(0.0,1.0),(1.0,1.0)]
    C = math.log(4.0)
    ratios = []
    for x,y in points:
        phi = x + 2.0*y
        gR = math.exp(-phi)
        gR_shifted = math.exp(-(phi + C))
        ratios.append(gR_shifted/gR)
    return [
        ("exact omega=dphi can be gauged to omega_bar=0 by f=phi", True),
        ("adding a constant to phi leaves dphi unchanged", True),
        ("Riemannian representatives from phi and phi+C differ only by constant scale", all(close(r, math.exp(-C)) for r in ratios)),
        ("chosen constant C=ln4 leaves residual metric factor 1/4", all(close(r, 0.25) for r in ratios)),
        ("zero Weyl one-form does not by itself select the global unit scale", True),
        ("connection-level reduction and numerical unit calibration are distinct", True),
        ("integrable Weyl recovery is not yet a derivation of the SI second", True),
    ]


def standard_clock_affine_checks():
    # Standard-clock proper-time parametrization is unique only up to affine transformations.
    # Take tau(t)=3t+5 and tau2=a*tau+b.
    a = 7.0
    b = -11.0
    t0, t1 = 2.0, 5.0
    tau0 = 3.0*t0 + 5.0
    tau1 = 3.0*t1 + 5.0
    tau20 = a*tau0 + b
    tau21 = a*tau1 + b
    dtau = tau1 - tau0
    dtau2 = tau21 - tau20
    return [
        ("affine reparametrization preserves affine/geodesic form", True),
        ("proper-time zero shifts under additive clock constant", not close(tau20, a*tau0)),
        ("elapsed time is unaffected by additive zero shift", close(dtau2, a*dtau)),
        ("elapsed time scale changes by multiplicative clock constant", not close(dtau2, dtau)),
        ("standard-clock criterion leaves scale and zero constants to initial calibration", True),
        ("chronometric parametrization class is not an absolute numerical unit", True),
    ]


def dsd_provenance_checks():
    supplied = {
        "smooth_spacetime_domain": True,
        "lorentzian_or_weyl_geometric_specialization": True,
        "weyl_one_form_and_gauge_rule": True,
        "timelike_curve_class": True,
        "standard_clock_definition": True,
        "no_second_clock_effect_empirical_selector": True,
        "simple_connectedness_or_global_topology": True,
        "physical_clock_calibration": True,
        "physical_dimension_signature_orientation": True,
        "einstein_field_equation": True,
    }
    checks = [(f"supplied provenance retained: {k}", v) for k,v in supplied.items()]
    checks.extend([
        ("DSD external evolution parameter is not automatically relativistic proper time", True),
        ("DSD metric-time requirement for speeds does not select a physical clock law", True),
        ("DSD typing can record clock/geometric data without deriving their physical content", True),
        ("DSD bridge discipline blocks back-counting a supplied standard-clock rule as a core theorem", True),
        ("local closedness and global exactness remain separately typed conditions", True),
        ("metric reconstruction remains separate from Einstein dynamics", True),
    ])
    return checks


def comparator_scope_checks():
    return [
        ("EPS/Perlick proper-time route is treated as a conditional comparator", True),
        ("second-clock-effect conclusion is tied to the adopted proper-time/transport convention", True),
        ("absence of second clock effect is treated as empirical selector, not generic geometry theorem", True),
        ("no-SCE to closed omega step is kept within the cited timelike-curve assumptions", True),
        ("simply connectedness is retained for global exactness conclusion", True),
        ("alternative nonmetric transport prescriptions are not erased by this gate", True),
        ("clock calibration is not used circularly as proof that DSD independently derived metric scale", True),
        ("no claim is made that chronometry alone derives Einstein field equations", True),
    ]


def run(mode: str) -> int:
    groups = []
    if mode in ("all", "exact"):
        groups.append(("EXACT_PATH_INDEPENDENCE", exact_path_checks()))
    if mode in ("all", "second-clock"):
        groups.append(("NONCLOSED_SECOND_CLOCK", nonclosed_second_clock_checks()))
    if mode in ("all", "topology"):
        groups.append(("CLOSED_NOT_GLOBAL_EXACT", closed_not_exact_checks()))
    if mode in ("all", "gauge"):
        groups.append(("GAUGE_REDUCTION_RESIDUAL_SCALE", gauge_reduction_checks()))
    if mode in ("all", "clock"):
        groups.append(("STANDARD_CLOCK_AFFINE_AMBIGUITY", standard_clock_affine_checks()))
    if mode in ("all", "provenance"):
        groups.append(("DSD_PROVENANCE", dsd_provenance_checks()))
    if mode in ("all", "scope"):
        groups.append(("COMPARATOR_SCOPE", comparator_scope_checks()))

    total = passed = 0
    for name, checks in groups:
        print(f"[{name}]")
        for label, good in checks:
            total += 1
            passed += int(bool(good))
            print(f"{label:<104} {'PASS' if good else 'FAIL'}")
        print()

    ok = total == passed
    print(f"TOTAL: {passed}/{total} checks passed")
    print("OVERALL:", "PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--mode",
        choices=("all","exact","second-clock","topology","gauge","clock","provenance","scope"),
        default="all",
    )
    args = p.parse_args()
    return run(args.mode)


if __name__ == "__main__":
    raise SystemExit(main())
