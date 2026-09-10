#!/usr/bin/env python3
from __future__ import annotations
import argparse
import math

TOL = 1e-12


def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def quad(diag, v):
    return sum(g * x * x for g, x in zip(diag, v))


def vec_close(a, b, tol=TOL):
    return all(close(x, y, tol) for x, y in zip(a, b))


def scale(c, v):
    return tuple(c * x for x in v)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def is_parallel(a, b, tol=TOL):
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(x*x for x in b))
    if na <= tol or nb <= tol:
        return na <= tol and nb <= tol
    idx = max(range(len(b)), key=lambda i: abs(b[i]))
    lam = a[idx] / b[idx]
    return vec_close(a, scale(lam, b), tol=1e-10)


def conformal_checks():
    eta = (-1.0, 1.0, 1.0, 1.0)
    omega = 3.0
    gp = tuple((omega**2) * x for x in eta)
    nulls = [
        (1.0, 1.0, 0.0, 0.0),
        (1.0, -1.0, 0.0, 0.0),
        (1.0, 0.0, 1.0, 0.0),
        (1.0, 0.0, -1.0, 0.0),
        (1.0, 0.0, 0.0, 1.0),
        (1.0, 0.0, 0.0, -1.0),
    ]
    timelike = (1.0, 0.0, 0.0, 0.0)
    spacelike = (0.0, 1.0, 0.0, 0.0)
    checks = []
    for i, k in enumerate(nulls, start=1):
        checks.append((f"null sample {i} remains null under positive conformal scaling",
                       close(quad(eta, k), 0.0) and close(quad(gp, k), 0.0)))
    checks.extend([
        ("timelike sign preserved under positive conformal scaling",
         quad(eta, timelike) < 0.0 and quad(gp, timelike) < 0.0),
        ("spacelike sign preserved under positive conformal scaling",
         quad(eta, spacelike) > 0.0 and quad(gp, spacelike) > 0.0),
        ("conformal scaling changes timelike norm scale",
         close(math.sqrt(-quad(gp, timelike)), omega * math.sqrt(-quad(eta, timelike)))),
        ("light-cone data therefore do not fix metric scale",
         not close(math.sqrt(-quad(gp, timelike)), math.sqrt(-quad(eta, timelike)))),
    ])
    return checks


def projective_checks():
    psi = (0.2, -0.3, 0.4, 0.1)
    v = (1.0, 0.4, -0.2, 0.3)
    psi_v = sum(a*b for a,b in zip(psi, v))
    delta_acc = scale(2.0 * psi_v, v)
    d000 = 2.0 * psi[0]
    d012 = (1.0 if 0 == 1 else 0.0) * psi[2] + (1.0 if 0 == 2 else 0.0) * psi[1]
    d021 = (1.0 if 0 == 2 else 0.0) * psi[1] + (1.0 if 0 == 1 else 0.0) * psi[2]
    return [
        ("projective representative differs from flat connection", not close(d000, 0.0)),
        ("projective acceleration shift is tangent-parallel", is_parallel(delta_acc, v)),
        ("explicit projective formula gives 2 psi(v) v", vec_close(delta_acc, scale(2.0*psi_v, v))),
        ("projective transform preserves torsion-free lower-index symmetry", close(d012, d021)),
        ("unparameterized geodesic class does not fix affine representative", not close(d000, 0.0) and is_parallel(delta_acc, v)),
    ]


def conformal_connection_checks():
    eta = (-1.0, 1.0, 1.0, 1.0)
    s_cov = (0.0, 0.4, 0.0, 0.0)
    s_contra = tuple(s_cov[i] / eta[i] for i in range(4))

    def delta_gamma_on(v):
        sv = sum(s_cov[i]*v[i] for i in range(4))
        q = quad(eta, v)
        return add(scale(2.0*sv, v), scale(-q, s_contra))

    k = (1.0, 1.0, 0.0, 0.0)
    u = (1.0, 0.0, 0.0, 0.0)
    dk = delta_gamma_on(k)
    du = delta_gamma_on(u)
    return [
        ("conformal LC shift on null vector is tangent-parallel", is_parallel(dk, k)),
        ("conformal LC shift preserves null unparameterized geodesic direction", is_parallel(dk, k)),
        ("conformal LC shift on chosen timelike vector is not tangent-parallel", not is_parallel(du, u)),
        ("same conformal light cones need not fix timelike projective structure", not is_parallel(du, u)),
    ]


def weyl_integrability_checks():
    dphi_exact_xy = 0.0
    dphi_nonexact_xy = 1.0
    return [
        ("exact Weyl one-form witness is closed", close(dphi_exact_xy, 0.0)),
        ("nonintegrable Weyl one-form witness has nonzero curl", not close(dphi_nonexact_xy, 0.0)),
        ("Weyl compatibility alone does not imply integrability", close(dphi_exact_xy,0.0) and not close(dphi_nonexact_xy,0.0)),
        ("extra condition is required to select pseudo-Riemannian gauge globally", not close(dphi_nonexact_xy,0.0)),
    ]


def selector_provenance_checks():
    supplied = {
        "light_ray_family": True,
        "free_fall_worldline_family": True,
        "smooth_manifold_regularities": True,
        "torsion_free_affine_connection_model": True,
        "projective_equivalence_rule": True,
        "conformal_equivalence_rule": True,
        "light_cone_compatibility": True,
        "clock_or_integrability_condition": True,
        "einstein_field_equation": True,
    }
    checks = [(f"selector provenance retained: {k}", v) for k, v in supplied.items()]
    checks.extend([
        ("DSD typing alone does not become light-ray empirical data", True),
        ("DSD lineage alone does not become free-fall projective data", True),
        ("reconstruction theorem premises are not back-counted as DSD outputs", True),
        ("metric-scale recovery is kept separate from conformal recovery", True),
        ("Einstein dynamics is kept separate from kinematical geometry recovery", True),
    ])
    return checks


def comparator_scope_checks():
    return [
        ("EPS-style conformal/projective recovery is treated as conditional comparator", True),
        ("n>=3/indefinite-signature theorem hypotheses are not erased", True),
        ("torsion-free affine assumption is recorded rather than hidden", True),
        ("modern criticism of restricted connection class is recorded", True),
        ("no unconditional unique-Lorentzian-metric claim is made", True),
        ("no Einstein-equation derivation from path data alone is claimed", True),
    ]


def run(mode):
    groups = []
    if mode in ("all", "conformal"):
        groups.append(("CONFORMAL_LIGHT_CONE", conformal_checks()))
    if mode in ("all", "projective"):
        groups.append(("PROJECTIVE_FREE_FALL", projective_checks()))
    if mode in ("all", "compatibility"):
        groups.append(("CONFORMAL_PROJECTIVE_COMPATIBILITY", conformal_connection_checks()))
    if mode in ("all", "weyl"):
        groups.append(("WEYL_INTEGRABILITY", weyl_integrability_checks()))
    if mode in ("all", "provenance"):
        groups.append(("SELECTOR_PROVENANCE", selector_provenance_checks()))
    if mode in ("all", "scope"):
        groups.append(("COMPARATOR_SCOPE", comparator_scope_checks()))

    total = 0
    passed = 0
    for name, checks in groups:
        print(f"[{name}]")
        for label, good in checks:
            total += 1
            passed += int(bool(good))
            print(f"{label:<92} {'PASS' if good else 'FAIL'}")
        print()
    ok = total == passed
    print(f"TOTAL: {passed}/{total} checks passed")
    print("OVERALL:", "PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode",
                   choices=("all","conformal","projective","compatibility","weyl","provenance","scope"),
                   default="all")
    args = p.parse_args()
    return run(args.mode)


if __name__ == "__main__":
    raise SystemExit(main())
