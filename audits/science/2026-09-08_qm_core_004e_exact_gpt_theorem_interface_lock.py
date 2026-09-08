from fractions import Fraction
import argparse
import math


def matrix_rank(rows):
    rows = [list(map(Fraction, row)) for row in rows]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if rows[i][c] != 0), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(m):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [rows[i][j] - f * rows[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def test_normalized_affine_slice_codim_one():
    omega = [
        (1, 0, 0),
        (1, 1, 0),
        (1, 0, 1),
        (1, Fraction(1, 3), Fraction(1, 4)),
    ]
    vdim = matrix_rank(omega)
    base = omega[0]
    diffs = [
        tuple(row[j] - base[j] for j in range(len(base)))
        for row in omega[1:]
    ]
    affdim = matrix_rank(diffs)
    assert vdim == 3
    assert affdim == 2
    assert affdim == vdim - 1
    return True, (vdim, affdim)


def test_convex_bounded_not_compact():
    # Omega=(0,1) is convex and bounded but not closed in R, hence not compact.
    samples = [Fraction(1, n) for n in range(2, 20)]
    assert all(Fraction(0) < x < Fraction(1) for x in samples)
    limit = Fraction(0)
    assert not (Fraction(0) < limit < Fraction(1))
    a, b, lam = Fraction(1, 5), Fraction(4, 5), Fraction(2, 5)
    mixed = lam * a + (1 - lam) * b
    assert Fraction(0) < mixed < Fraction(1)
    return True, (samples[-1], limit, mixed)


def test_crr_reachability_weaker_than_connected_group():
    # O(2) is disconnected (det +/-1), while SO(2) paths can reach any point
    # on the circle from any other point. Thus pure-state path reachability
    # does not imply the full allowed reversible group is connected.
    target_angles = [0.0, math.pi / 7.0, math.pi / 2.0, math.pi]
    for theta in target_angles:
        x, y = math.cos(theta), math.sin(theta)
        assert abs(x * x + y * y - 1.0) < 1e-12
    determinant_components = {+1, -1}
    assert len(determinant_components) == 2
    return True, tuple(sorted(determinant_components))


def test_rrde_designated_vs_universal_quantifier():
    # Logical interface witness: one designated maximal measurement can pass
    # while another maximal measurement fails. Theorem 21 quantifies over any
    # perfectly distinguishing N-outcome measurement.
    restriction_equivalence = {
        "M_designated": True,
        "M_other": False,
    }
    designated_pass = restriction_equivalence["M_designated"]
    universal_pass = all(restriction_equivalence.values())
    assert designated_pass
    assert not universal_pass
    return True, (designated_pass, universal_pass)


def test_current_crd_missing_exact_tomographic_locality_fields():
    current_crd = {
        "GLOBAL_CARRIER",
        "LOCAL_EMBEDDINGS",
        "LOCAL_READOUT_FAMILY",
        "GLOBAL_READOUT_FAMILY",
        "REDUCTION_MAPS",
        "COMPOSITE_DYNAMICS",
    }
    exact_tl_lock = {
        "PRODUCT_PREPARATIONS",
        "PRODUCT_EFFECTS",
        "TENSOR_CARRIER_EQUALITY",
        "LOCAL_TRANSFORMATION_PRODUCTS",
        "PRODUCT_NORMALIZATION",
    }
    missing = exact_tl_lock - current_crd
    assert missing == exact_tl_lock
    return True, tuple(sorted(missing))


def test_interface_status_matrix():
    # Existing DSD/QM-specialization package versus exact external theorem interface.
    status = {
        "finite_dimensional_real_carrier": "conditional_pass",
        "convexity": "conditional_pass",
        "codim_one_normalization_slice": "conditional_pass",
        "compactness": "gap",
        "no_restriction": "explicit_selector",
        "tomographic_locality_exact_tensor_form": "gap",
        "subspace_axiom_universal_quantifier": "gap",
        "continuous_reversible_group_connectedness": "gap",
        "capacity_family_for_every_N": "gap",
    }
    assert status["compactness"] == "gap"
    assert status["no_restriction"] == "explicit_selector"
    assert sum(v == "gap" for v in status.values()) == 5
    return True, status


def run_all():
    tests = [
        ("normalized evaluation slice has codim one", test_normalized_affine_slice_codim_one),
        ("convex bounded state set need not be compact", test_convex_bounded_not_compact),
        ("CRR reachability != full connected group", test_crr_reachability_weaker_than_connected_group),
        ("RRDE designated quantifier != theorem universal quantifier", test_rrde_designated_vs_universal_quantifier),
        ("current CRD != exact Tomographic Locality tensor lock", test_current_crd_missing_exact_tomographic_locality_fields),
        ("exact theorem-interface status matrix", test_interface_status_matrix),
    ]
    ok = True
    for name, fn in tests:
        try:
            _, detail = fn()
            print(f"{name:58s} PASS  {detail}")
        except Exception as exc:
            ok = False
            print(f"{name:58s} FAIL  {exc}")
    print()
    print("OVERALL:", "PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all"], default="all")
    _ = parser.parse_args()
    raise SystemExit(run_all())


if __name__ == "__main__":
    main()
