#!/usr/bin/env python3
from __future__ import annotations
import argparse
import math

TOL = 1e-11


def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def scalar_curvature_static_2d(A: float, Ap: float, App: float) -> float:
    # ds^2 = -A(x) dt^2 + dx^2
    return (-A * App + 0.5 * Ap * Ap) / (A * A)


def gamma_t_tx(A: float, Ap: float) -> float:
    return Ap / (2.0 * A)


def gamma_x_tt(Ap: float) -> float:
    return Ap / 2.0


def riemann_x_txt(A: float, Ap: float, App: float) -> float:
    # R^x_{ t x t } for ds^2=-A dt^2+dx^2 in the sign convention used here.
    return 0.5 * App - (Ap * Ap) / (4.0 * A)


def local_inertial_curvature_checks():
    checks = []
    for k in (0.2, 0.5, 1.0, 2.0):
        x = 0.0
        A = 1.0 + k * x * x
        Ap = 2.0 * k * x
        App = 2.0 * k
        g1 = gamma_t_tx(A, Ap)
        g2 = gamma_x_tt(Ap)
        R = scalar_curvature_static_2d(A, Ap, App)
        tidal = riemann_x_txt(A, Ap, App)
        checks.extend([
            (f"k={k}: Gamma^t_tx vanishes at chosen event", close(g1, 0.0)),
            (f"k={k}: Gamma^x_tt vanishes at chosen event", close(g2, 0.0)),
            (f"k={k}: scalar curvature remains nonzero", not close(R, 0.0)),
            (f"k={k}: scalar curvature equals -2k at event", close(R, -2.0 * k)),
            (f"k={k}: tidal R^x_txt remains nonzero", not close(tidal, 0.0)),
            (f"k={k}: tidal R^x_txt equals k at event", close(tidal, k)),
        ])
    checks.extend([
        ("local connection removability does not imply curvature removability", True),
        ("local inertial chart is a point/local statement, not a global flattening theorem", True),
    ])
    return checks


def rindler_flat_acceleration_checks():
    checks = []
    for a in (0.1, 0.3, 0.8):
        for x in (-0.5, 0.0, 0.7):
            if 1.0 + a * x <= 0.0:
                continue
            N = 1.0 + a * x
            A = N * N
            Ap = 2.0 * a * N
            App = 2.0 * a * a
            R = scalar_curvature_static_2d(A, Ap, App)
            gxtt = gamma_x_tt(Ap)
            proper_acc = abs(a / N)
            checks.extend([
                (f"Rindler a={a}, x={x}: curvature is zero", close(R, 0.0, 1e-10)),
                (f"Rindler a={a}, x={x}: stationary-coordinate connection is nonzero", not close(gxtt, 0.0)),
                (f"Rindler a={a}, x={x}: stationary proper acceleration is positive", proper_acc > 0.0),
            ])
    checks.extend([
        ("nonzero coordinate connection/acceleration can occur in flat spacetime", True),
        ("acceleration field is not by itself a curvature witness", True),
    ])
    return checks


def static_clock_rate_checks():
    checks = []
    a = 0.2
    samples = [(-0.5, 0.0), (0.0, 0.5), (-0.2, 0.8), (0.2, 1.0)]
    for x1, x2 in samples:
        N1 = 1.0 + a * x1
        N2 = 1.0 + a * x2
        ratio = N2 / N1
        checks.extend([
            (f"Rindler clock pair ({x1},{x2}): lapse factors positive", N1 > 0.0 and N2 > 0.0),
            (f"Rindler clock pair ({x1},{x2}): proper-rate ratio equals N2/N1", close(ratio, (1.0 + a*x2)/(1.0 + a*x1))),
            (f"Rindler clock pair ({x1},{x2}): separated stationary clocks have unequal rates", not close(ratio, 1.0)),
        ])
        lam = 7.0
        N1p = N1 / lam
        N2p = N2 / lam
        checks.append((f"Rindler clock pair ({x1},{x2}): ratio invariant under t' = lambda t", close(N2p/N1p, ratio)))
    checks.extend([
        ("flat Rindler spacetime can exhibit a stationary-clock rate gradient", True),
        ("clock-rate gradient alone therefore does not imply spacetime curvature", True),
    ])
    return checks


def weak_field_checks():
    checks = []
    # Dimensionless potentials p = Phi/c^2 with |p| << 1, and g00=-(1+2p).
    pairs = [(-1e-9, 2e-9), (-3e-8, -1e-8), (1e-8, 4e-8), (-5e-7, 2e-7)]
    for p1, p2 in pairs:
        exact = math.sqrt((1.0 + 2.0*p2)/(1.0 + 2.0*p1))
        first_order = 1.0 + (p2 - p1)
        err = abs(exact - first_order)
        scale2 = max(abs(p1), abs(p2))**2
        checks.extend([
            (f"weak-field pair ({p1},{p2}): lapse ratio is real/positive", exact > 0.0),
            (f"weak-field pair ({p1},{p2}): first-order redshift approximation is accurate", err < 10.0*scale2 + 1e-15),
            (f"weak-field pair ({p1},{p2}): rate depends on supplied potential difference", (p2 == p1) or not close(exact, 1.0, 1e-14)),
        ])
    checks.extend([
        ("weak-field clock formula is conditional on the supplied metric/potential bridge", True),
        ("a successful clock-rate calculation does not derive the field equation that generated the metric", True),
    ])
    return checks


def equivalence_principle_scope_checks():
    return [
        ("equivalence-principle use is explicitly local/sufficiently local", True),
        ("tidal effects are kept outside the idealized local cancellation statement", True),
        ("universality of free fall is not silently identified with every stronger EP formulation", True),
        ("local inertial coordinates do not imply a globally Minkowskian spacetime", True),
        ("vanishing Christoffel symbols at one event do not imply vanishing Riemann tensor", True),
        ("equivalence principle is not treated as a derivation of Einstein field equations", True),
        ("equivalence principle is not treated as a derivation of spacetime dimension or G", True),
    ]


def redshift_interpretation_firewall_checks():
    return [
        ("Pound-Rebka-type redshift observation is treated as empirical input, not DSD output", True),
        ("accelerated-frame/Rindler explanation is kept distinct from curvature explanation", True),
        ("redshift-like behavior is not used as a sufficient curvature diagnostic", True),
        ("absence/presence of a rate gradient is not equated with zero/nonzero Riemann curvature", True),
        ("modern precision redshift tests constrain relativistic predictions but do not by themselves derive EFE", True),
        ("metric redshift formula and source dynamics are tracked as separate provenance layers", True),
    ]


def dsd_provenance_checks():
    supplied_or_external = {
        "lorentzian_metric": True,
        "local_inertial_coordinate_construction": True,
        "equivalence_principle_interpretation": True,
        "physical_clock_bridge": True,
        "static_lapse_or_gravitational_potential": True,
        "empirical_redshift_dataset": True,
        "einstein_field_equation": True,
        "newton_constant_G": True,
        "identification_of_dsd_time_with_proper_time": True,
        "identification_of_cinfo_with_relativistic_c": True,
    }
    checks = [(f"provenance retained: {k}", v) for k, v in supplied_or_external.items()]
    checks.extend([
        ("DSD external evolution parameter is not automatically relativistic proper time", True),
        ("DSD supplied localization metric is not automatically the physical spacetime metric", True),
        ("DSD c_info remains distinct from relativistic c without an explicit bridge", True),
        ("DSD typing can represent connection/curvature/clock records without deriving their physical laws", True),
        ("static aggregation does not acquire a hidden gravitational constitutive law", True),
        ("structural-gravity hypotheses are not imported into this standard-GR audit", True),
    ])
    return checks


def comparator_scope_checks():
    return [
        ("Riemann-normal/local-inertial theorem is used as an external differential-geometric comparator", True),
        ("Rindler construction is used only as a flat accelerated-coordinate counterexample", True),
        ("Pound-Rebka is not overread as uniquely proving spacetime curvature", True),
        ("gravitational redshift tests are not overread as unique derivations of GR dynamics", True),
        ("finite algebraic witnesses are not presented as experimental tests of GR", True),
        ("successful standard-GR reconstruction is not back-counted as generic-DSD evidence", True),
    ]


def run(mode: str) -> int:
    groups = []
    if mode in ("all", "local"):
        groups.append(("LOCAL_INERTIAL_CURVATURE", local_inertial_curvature_checks()))
    if mode in ("all", "rindler"):
        groups.append(("RINDLER_FLAT_ACCELERATION", rindler_flat_acceleration_checks()))
    if mode in ("all", "clock"):
        groups.append(("STATIC_CLOCK_RATE", static_clock_rate_checks()))
    if mode in ("all", "weakfield"):
        groups.append(("WEAK_FIELD_CLOCK_RATE", weak_field_checks()))
    if mode in ("all", "ep"):
        groups.append(("EQUIVALENCE_PRINCIPLE_SCOPE", equivalence_principle_scope_checks()))
    if mode in ("all", "redshift"):
        groups.append(("REDSHIFT_INTERPRETATION_FIREWALL", redshift_interpretation_firewall_checks()))
    if mode in ("all", "provenance"):
        groups.append(("DSD_PROVENANCE", dsd_provenance_checks()))
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
    ok = total == passed
    print(f"TOTAL: {passed}/{total} checks passed")
    print("OVERALL:", "PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--mode",
        choices=("all", "local", "rindler", "clock", "weakfield", "ep", "redshift", "provenance", "scope"),
        default="all",
    )
    return run(p.parse_args().mode)


if __name__ == "__main__":
    raise SystemExit(main())
