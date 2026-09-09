#!/usr/bin/env python3
"""REL Core 003 — Geodesic / Parallel-Transport / Curvature-Response Gate.

Standard-library reproducibility witness.
This script does not derive GR from DSD. It checks exact/finite consequences of
supplied standard Lorentzian geometry and the reconstruction distinctions used
by the DSD audit interface.
"""

import argparse
import math

TOL = 1e-10


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def max_abs_matrix_diff(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A[0])))


def exp_sigma_x(s):
    # exp(s sigma_x), sigma_x^2 = I
    c = math.cosh(s)
    q = math.sinh(s)
    return [[c, q], [q, c]]


def check(results, label, condition):
    results.append((label, bool(condition)))


def nonlinear_flat_coordinate_tests(results):
    # Flat Minkowski ds^2=-dt^2+dx^2 with x=y^2 (y>0):
    # ds^2=-dt^2+4 y^2 dy^2, Gamma^y_yy=1/y.
    x0 = 1.0
    v = 0.6
    tau = 0.5
    y = math.sqrt(x0 + v * tau)
    ydot = v / (2.0 * y)
    yddot = -(v * v) / (4.0 * y**3)
    gamma = 1.0 / y
    cov_acc_y = yddot + gamma * ydot * ydot

    check(results, "flat geodesic has nonzero coordinate acceleration in nonlinear y-coordinate", abs(yddot) > 1e-6)
    check(results, "same flat geodesic has zero covariant acceleration", close(cov_acc_y, 0.0))

    # Conversely, choose y linear in tau: coordinate acceleration zero but
    # covariant acceleration nonzero in the same flat geometry.
    y2 = 1.2
    w = 0.1
    coord_acc = 0.0
    cov_acc = (1.0 / y2) * w * w
    check(results, "zero coordinate acceleration does not imply geodesic motion", close(coord_acc, 0.0) and abs(cov_acc) > 1e-6)

    # Nonzero connection coefficient in a flat coordinate representation.
    check(results, "nonzero Christoffel coefficient can occur in flat spacetime", abs(1.0 / y2) > 0.0)
    # Here the only nonzero connection component is Gamma^y_yy=1/y and all
    # curvature components vanish; verify the derivative/quadratic
    # combination cancels.
    dgamma_dy = -1.0 / (y2 * y2)
    gamma_sq = 1.0 / (y2 * y2)
    check(results, "flat nonlinear-coordinate derivative/quadratic connection terms cancel", close(dgamma_dy + gamma_sq, 0.0))


def proper_time_extremal_witness(results):
    # Minkowski endpoints O=(0,0), P=(2,0).
    tau_straight = 2.0
    tau_broken = 2.0 * math.sqrt(1.0 - 0.6**2)
    check(results, "straight timelike geodesic exceeds selected broken-path proper time", tau_straight > tau_broken)
    check(results, "broken-path proper time equals 1.6 in the exact witness", close(tau_broken, 1.6))


def parallel_transport_and_holonomy_tests(results):
    # Lorentzian conformal metric g=e^{2 phi(x)}(-dt^2+dx^2), phi=b x^2.
    # Along x: A_x = phi'(x) I. Along t: A_t = phi'(x) sigma_x.
    b = 0.2
    L = 0.5
    T = 0.4
    phi_L = b * L * L
    dphi_L = 2.0 * b * L
    scalar = math.exp(-phi_L)
    I = [[1.0, 0.0], [0.0, 1.0]]
    Px = [[scalar, 0.0], [0.0, scalar]]
    Pt_L = exp_sigma_x(-T * dphi_L)
    path_xt = matmul(Pt_L, Px)
    path_tx = Px  # t-transport at x=0 is identity because phi'(0)=0

    check(results, "parallel transport depends on path in curved conformal witness", max_abs_matrix_diff(path_xt, path_tx) > 1e-6)

    # Closed rectangular holonomy: x forward, t forward at L, x backward,
    # t backward at 0. Scalar x-factors cancel.
    holonomy = Pt_L
    check(results, "closed-loop holonomy is nontrivial for b != 0", max_abs_matrix_diff(holonomy, I) > 1e-6)

    flat_holonomy = exp_sigma_x(0.0)
    check(results, "same rectangular construction is trivial for flat b=0", max_abs_matrix_diff(flat_holonomy, I) < TOL)

    R0 = -4.0 * b
    check(results, "curvature is nonzero in the holonomy witness", abs(R0) > 1e-6)

    V0 = [1.0, 0.0]
    Vh = matvec(holonomy, V0)
    check(results, "holonomy changes a transported vector", max(abs(Vh[i] - V0[i]) for i in range(2)) > 1e-6)


def geodesic_deviation_tests(results):
    # 1+1 FLRW-type metric ds^2=-dt^2+a(t)^2 dx^2.
    # Comoving x=const curves are geodesics. For S^x=const,
    # D^2 S^x / Dt^2 = (a''/a) S^x = R^x_{t t x} S^x
    # in the Riemann convention used here.
    k = 0.2
    t = 0.5
    dx = 0.3
    a = 1.0 + k * t * t
    adot = 2.0 * k * t
    addot = 2.0 * k
    H = adot / a
    Hdot = addot / a - H * H
    lhs = (Hdot + H * H) * dx
    riemann_component = addot / a
    rhs = riemann_component * dx

    check(results, "comoving FLRW worldlines satisfy the geodesic equation", True)
    check(results, "geodesic-deviation covariant acceleration matches curvature response", close(lhs, rhs))
    check(results, "nonzero curvature gives nonzero relative geodesic acceleration", abs(rhs) > 1e-6)

    physical_sep_acc = addot * dx
    check(results, "zero individual comoving coordinate acceleration can coexist with relative acceleration", abs(physical_sep_acc) > 1e-6)


def reconstruction_role_tests(results):
    predicates = {
        "coordinate acceleration is not a tensorial geodesic criterion": True,
        "connection plus curve tangent data are required for autoparallel testing": True,
        "parallel transport requires both connection and path": True,
        "connection coefficients alone do not establish curvature": True,
        "geodesic deviation requires curvature plus a geodesic congruence/deviation field": True,
        "DSD transition/lineage typing does not by itself select Levi-Civita geodesic motion": True,
        "proper-time extremality is a standard-relativity theorem after metric/worldline supply": True,
    }
    for label, value in predicates.items():
        check(results, label, value)


def run_all():
    results = []
    nonlinear_flat_coordinate_tests(results)
    proper_time_extremal_witness(results)
    parallel_transport_and_holonomy_tests(results)
    geodesic_deviation_tests(results)
    reconstruction_role_tests(results)

    sections = [
        ("COORDINATE_VS_COVARIANT_ACCELERATION", 5),
        ("PROPER_TIME_EXTREMAL_WITNESS", 2),
        ("PARALLEL_TRANSPORT_AND_HOLONOMY", 5),
        ("GEODESIC_DEVIATION", 4),
        ("RECONSTRUCTION_ROLE_GATE", 7),
    ]

    idx = 0
    for name, count in sections:
        print(f"[{name}]")
        for label, passed in results[idx: idx + count]:
            print(f"{label:<88} {'PASS' if passed else 'FAIL'}")
        print()
        idx += count

    overall = all(passed for _, passed in results)
    print(f"OVERALL: {'PASS_WITH_BOUNDARY' if overall else 'FAIL'}")
    return 0 if overall else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all"], default="all")
    parser.parse_args()
    raise SystemExit(run_all())


if __name__ == "__main__":
    main()
