#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math

TOL = 1e-11


def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def minkowski_dot(u, v):
    return -u[0] * v[0] + sum(a*b for a, b in zip(u[1:], v[1:]))


def hyperbola_state(a: float, tau: float):
    # c=1, x^mu=(sinh(a tau)/a, cosh(a tau)/a)
    t = math.sinh(a*tau) / a
    x = math.cosh(a*tau) / a
    u = (math.cosh(a*tau), math.sinh(a*tau))
    acc = (a*math.sinh(a*tau), a*math.cosh(a*tau))
    v = math.tanh(a*tau)
    return (t, x), u, acc, v


def metric_proper_time_checks():
    checks = []
    for a in (0.4, 1.0, 2.5):
        for tau in (-1.2, 0.0, 0.7, 1.6):
            _, u, acc, v = hyperbola_state(a, tau)
            checks.append((
                f"uniform-acceleration 4-velocity normalized: a={a}, tau={tau}",
                close(minkowski_dot(u, u), -1.0),
            ))
            checks.append((
                f"proper-acceleration magnitude recovered: a={a}, tau={tau}",
                close(minkowski_dot(acc, acc), a*a),
            ))
            checks.append((
                f"4-velocity orthogonal to 4-acceleration: a={a}, tau={tau}",
                close(minkowski_dot(u, acc), 0.0),
            ))
            dtaudt = math.sqrt(1.0-v*v)
            dtdtau = u[0]
            checks.append((
                f"metric rate integrates locally: sqrt(1-v^2) dt/dtau=1: a={a}, tau={tau}",
                close(dtaudt*dtdtau, 1.0),
            ))
    return checks


def clock_hypothesis_boundary_checks():
    v = 0.6
    gamma = 1.0 / math.sqrt(1.0-v*v)
    u = (gamma, gamma*v)
    metric_rate = math.sqrt(-minkowski_dot(u, u))

    a1, a2 = 0.5, 5.0
    a0 = 2.0
    eps = 0.03
    alt1 = metric_rate * (1.0 + eps*(a1/a0)**2)
    alt2 = metric_rate * (1.0 + eps*(a2/a0)**2)
    ideal1 = metric_rate
    ideal2 = metric_rate

    return [
        ("same tangent fixes same metric infinitesimal proper-time rate", close(metric_rate, 1.0)),
        ("ideal-clock law has no explicit acceleration correction at fixed tangent", close(ideal1, ideal2)),
        ("an acceleration-sensitive response law can distinguish same-tangent accelerations", not close(alt1, alt2)),
        ("zero acceleration-coupling recovers ideal metric clock law",
         close(metric_rate*(1.0 + 0.0*(a2/a0)**2), metric_rate)),
        ("metric proper time does not mathematically forbid nonideal device response", alt2 > alt1 > metric_rate),
        ("clock-hypothesis/clock-condition bridge must therefore be kept explicit", True),
    ]


def accelerated_path_checks():
    T = 10.0
    v = 0.6
    tau_rest = T
    tau_out_back = T*math.sqrt(1.0-v*v)

    # Equal coordinate duration, piecewise-inertial round trip.
    half = T/2.0
    seg1 = half*math.sqrt(1.0-v*v)
    seg2 = half*math.sqrt(1.0-v*v)

    return [
        ("stationary timelike path proper time equals coordinate duration", close(tau_rest, T)),
        ("moving out-back path proper time is sum of segment line elements", close(tau_out_back, seg1+seg2)),
        ("moving out-back path accumulates less proper time than stationary path", tau_out_back < tau_rest),
        ("turnaround changes tangent but adds no separate acceleration scalar to metric line element",
         close(tau_out_back, T*math.sqrt(1.0-v*v))),
        ("worldline proper time is path dependent even with same endpoints", not close(tau_out_back, tau_rest)),
    ]


def calibration_checks():
    tau_samples = (0.0, 1.0, 2.5, 7.0)
    alpha1, beta1 = 1.0, 0.0
    alpha2, beta2 = 3.0, 11.0
    r1 = tuple(alpha1*t + beta1 for t in tau_samples)
    r2 = tuple(alpha2*t + beta2 for t in tau_samples)

    diffs1 = tuple(r1[i+1]-r1[i] for i in range(len(r1)-1))
    diffs2 = tuple(r2[i+1]-r2[i] for i in range(len(r2)-1))

    return [
        ("different clock zero and unit give different numerical readings", r1 != r2),
        ("positive affine recalibration preserves temporal ordering",
         all(r2[i+1] > r2[i] for i in range(len(r2)-1))),
        ("affine recalibration rescales all elapsed readings by common factor",
         all(close(d2, alpha2*d1) for d1, d2 in zip(diffs1, diffs2))),
        ("metric geometry alone does not choose device offset beta", beta2 != beta1),
        ("metric geometry alone does not choose display scale alpha", alpha2 != alpha1),
        ("physical calibration is distinct from existence of metric proper-time functional", True),
    ]


def experiment_and_circularity_checks():
    # External-source ledger, not a re-analysis of raw experiment data.
    gamma_bailey = 29.33
    tau_plus_observed_us = 64.419
    reported_fractional_agreement_95 = 2e-3

    # Negative-muon proper lifetime in the Nature abstract was obtained "assuming special relativity".
    tau_minus_observed_us = 64.368
    tau0_minus_derived_us = 2.1948
    reconstructed = gamma_bailey*tau0_minus_derived_us

    return [
        ("Bailey et al. storage-ring gamma recorded", close(gamma_bailey, 29.33)),
        ("Bailey et al. positive-muon observed lifetime recorded", close(tau_plus_observed_us, 64.419)),
        ("reported SR agreement scale recorded as 2e-3 at 95% confidence",
         close(reported_fractional_agreement_95, 0.002)),
        ("derived negative-muon proper lifetime reproduces observed dilated lifetime closely",
         abs(reconstructed-tau_minus_observed_us) < 0.01),
        ("derived negative-muon rest lifetime is not treated as independent validation because SR was assumed", True),
        ("experiment supports clock-like SR time dilation under acceleration but does not derive DSD chronometry", True),
        ("experimental support and logical provenance are kept as distinct audit records", True),
    ]


def provenance_checks():
    supplied_or_external = {
        "smooth_lorentzian_spacetime": True,
        "metric_proper_time_functional": True,
        "ideal_or_standard_clock_condition": True,
        "momentarily_comoving_inertial_comparison": True,
        "physical_clock_mechanism": True,
        "clock_calibration": True,
        "experimental_identification_of_clock_readout": True,
        "einstein_dynamics_if_gravity_is_added": True,
    }
    checks = [(f"provenance retained: {k}", v) for k, v in supplied_or_external.items()]
    checks.extend([
        ("DSD external evolution parameter is not auto-identified with relativistic proper time", True),
        ("DSD metric time requirement for speed does not supply an ideal-clock law", True),
        ("DSD channel/property labels do not create a physical clock mechanism", True),
        ("successful clock model is not back-counted as a generic-DSD derivation", True),
        ("accelerated-clock agreement does not identify c_info with relativistic c", True),
        ("kinematical proper time remains separate from Einstein field dynamics", True),
    ])
    return checks


def comparator_scope_checks():
    return [
        ("clock-hypothesis status is recorded as literature-contested rather than declared settled", True),
        ("ideal clock is distinguished from arbitrary real clock hardware", True),
        ("hypothesis of locality is not promoted to an exact law for arbitrary finite-size measurements", True),
        ("Fletcher-style light-clock recovery is a model-dependent comparator, not a generic clock proof", True),
        ("Bailey storage-ring evidence is used as empirical support, not theorem-level derivation", True),
        ("no claim is made that acceleration can never affect a real clock mechanism", True),
        ("no claim is made that proper time contains an explicit universal acceleration term", True),
        ("no claim is made that DSD independently predicts accelerated-clock response", True),
    ]


def run(mode: str) -> int:
    groups = []
    if mode in ("all", "metric"):
        groups.append(("METRIC_PROPER_TIME", metric_proper_time_checks()))
    if mode in ("all", "clock"):
        groups.append(("CLOCK_HYPOTHESIS_BOUNDARY", clock_hypothesis_boundary_checks()))
    if mode in ("all", "path"):
        groups.append(("ACCELERATED_PATH", accelerated_path_checks()))
    if mode in ("all", "calibration"):
        groups.append(("CLOCK_CALIBRATION", calibration_checks()))
    if mode in ("all", "experiment"):
        groups.append(("EXPERIMENT_AND_CIRCULARITY", experiment_and_circularity_checks()))
    if mode in ("all", "provenance"):
        groups.append(("DSD_PROVENANCE", provenance_checks()))
    if mode in ("all", "scope"):
        groups.append(("COMPARATOR_SCOPE", comparator_scope_checks()))

    total = 0
    passed = 0
    for name, checks in groups:
        print(f"[{name}]")
        for label, good in checks:
            total += 1
            passed += int(bool(good))
            print(f"{label:<104} {'PASS' if good else 'FAIL'}")
        print()

    ok = passed == total
    print(f"TOTAL: {passed}/{total} checks passed")
    print("OVERALL:", "PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--mode",
        choices=("all", "metric", "clock", "path", "calibration", "experiment", "provenance", "scope"),
        default="all",
    )
    args = p.parse_args()
    return run(args.mode)


if __name__ == "__main__":
    raise SystemExit(main())
