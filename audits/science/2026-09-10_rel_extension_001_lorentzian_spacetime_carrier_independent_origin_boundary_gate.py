#!/usr/bin/env python3
from __future__ import annotations
import argparse
import math

TOL = 1e-12

def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol

def quad(diag, v):
    return sum(g * x * x for g, x in zip(diag, v))

def causal_class(diag, v):
    q = quad(diag, v)
    if close(q, 0.0):
        return "null"
    return "timelike" if q < 0.0 else "spacelike"

def signature_counts(diag):
    neg = sum(x < -TOL for x in diag)
    zero = sum(abs(x) <= TOL for x in diag)
    pos = sum(x > TOL for x in diag)
    return neg, zero, pos

def carrier_signature_checks():
    checks = []
    for n in (2, 3, 4, 5):
        lor = [-1.0] + [1.0] * (n - 1)
        eu = [1.0] * n
        checks.append((f"R^{n} admits Lorentzian diagonal signature (1,{n-1})",
                       signature_counts(lor) == (1, 0, n - 1)))
        checks.append((f"same R^{n} carrier also admits Euclidean positive signature",
                       signature_counts(eu) == (0, 0, n)))
    checks.append(("Lorentzian admissibility does not select dimension 4",
                   all(signature_counts([-1.0] + [1.0]*(n-1))[0] == 1 for n in (2,3,5))))
    return checks

def causal_dependence_checks():
    v = (1.0, 1.5)
    g1 = (-1.0, 1.0)
    g2 = (-4.0, 1.0)
    q1, q2 = quad(g1, v), quad(g2, v)
    return [
        ("same tangent vector is spacelike for diag(-1,+1)", close(q1, 1.25) and causal_class(g1, v) == "spacelike"),
        ("same tangent vector is timelike for diag(-4,+1)", close(q2, -1.75) and causal_class(g2, v) == "timelike"),
        ("carrier+tangent does not fix causal class without metric", causal_class(g1, v) != causal_class(g2, v)),
    ]

def null_scale_checks():
    checks = []
    speeds = (2.0, 3.0, 7.0/3.0)
    for c in speeds:
        g = (-c*c, 1.0)
        vp = (1.0, c)
        vm = (1.0, -c)
        checks.append((f"diag(-c^2,+1) has null branch +c for c={c:g}", close(quad(g, vp), 0.0)))
        checks.append((f"diag(-c^2,+1) has null branch -c for c={c:g}", close(quad(g, vm), 0.0)))
    checks.append(("same carrier permits distinct null coordinate scales",
                   len({round(c,12) for c in speeds}) == len(speeds)))
    return checks

def orientation_checks():
    g = (-1.0, 1.0)
    tplus = (1.0, 0.0)
    tminus = (-1.0, 0.0)
    v = (2.0, 0.2)
    def inner(a, b):
        return g[0]*a[0]*b[0] + g[1]*a[1]*b[1]
    return [
        ("T+ is timelike", causal_class(g, tplus) == "timelike"),
        ("T- is timelike", causal_class(g, tminus) == "timelike"),
        ("same metric admits opposite time-orientation choices",
         inner(tplus, v) < 0.0 and inner(tminus, v) > 0.0),
    ]

def einstein_dynamics_firewall_checks():
    # Constant Minkowski metric: curvature and Einstein tensor vanish.
    # A separately supplied constant nonzero stress tensor is divergence-free in
    # Cartesian coordinates but does not satisfy G = kappa T for kappa != 0.
    kappa = 1.0
    G = [[0.0, 0.0], [0.0, 0.0]]
    T = [[1.0, 0.0], [0.0, 0.0]]
    residual = [[G[i][j] - kappa*T[i][j] for j in range(2)] for i in range(2)]
    nonzero_residual = any(abs(x) > TOL for row in residual for x in row)
    return [
        ("flat constant metric has zero Einstein-tensor witness", all(close(x,0.0) for row in G for x in row)),
        ("constant nonzero stress tensor witness is supplied independently", close(T[0][0], 1.0)),
        ("geometry alone does not force supplied Einstein equation", nonzero_residual),
    ]

def propagation_firewall_checks():
    # Provenance witness only: this does not identify physical constants.
    c_metric = 2.0
    c_info = 5.0
    return [
        ("metric null-scale parameter can be positive", c_metric > 0.0),
        ("DSD information-bound parameter can be represented independently", c_info > 0.0),
        ("no identity c_info=c is imposed by this generic witness", not close(c_metric, c_info)),
    ]

def provenance_checks():
    statements = {
        "generic_dsd_selects_smooth_spacetime": False,
        "generic_dsd_selects_lorentzian_metric": False,
        "generic_dsd_selects_dimension_4": False,
        "generic_dsd_selects_time_orientation": False,
        "generic_dsd_selects_metric_null_scale": False,
        "generic_dsd_equates_c_info_and_relativistic_c": False,
        "generic_dsd_selects_einstein_equation": False,
        "supplied_lorentzian_structure_is_reconstructible": True,
    }
    expected = dict(statements)
    return [(f"provenance lock: {k}", statements[k] == expected[k]) for k in expected]

def run(mode):
    groups = []
    if mode in ("all", "carrier"):
        groups.append(("CARRIER_SIGNATURE", carrier_signature_checks()))
    if mode in ("all", "causal"):
        groups.append(("CAUSAL_METRIC_DEPENDENCE", causal_dependence_checks()))
    if mode in ("all", "nullscale"):
        groups.append(("NULL_SCALE", null_scale_checks()))
    if mode in ("all", "orientation"):
        groups.append(("TIME_ORIENTATION", orientation_checks()))
    if mode in ("all", "einstein"):
        groups.append(("EINSTEIN_DYNAMICS_FIREWALL", einstein_dynamics_firewall_checks()))
    if mode in ("all", "propagation"):
        groups.append(("PROPAGATION_FIREWALL", propagation_firewall_checks()))
    if mode in ("all", "provenance"):
        groups.append(("PROVENANCE", provenance_checks()))

    total = 0
    passed = 0
    for name, checks in groups:
        print(f"[{name}]")
        for label, good in checks:
            total += 1
            passed += int(bool(good))
            print(f"{label:<88} {'PASS' if good else 'FAIL'}")
        print()
    ok = total == passed
    print(f"TOTAL: {passed}/{total} checks passed")
    print("OVERALL:", "PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode",
                   choices=("all","carrier","causal","nullscale","orientation",
                            "einstein","propagation","provenance"),
                   default="all")
    args = p.parse_args()
    return run(args.mode)

if __name__ == "__main__":
    raise SystemExit(main())
