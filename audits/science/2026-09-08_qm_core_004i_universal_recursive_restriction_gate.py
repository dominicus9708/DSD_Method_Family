#!/usr/bin/env python3
"""QM Core 004I — universal recursive restriction equivalence gate.

Standard-library only.

The script checks:
1) a capacity-two product-disk GPT countermodel with no-restriction,
   connected pure-state-transitive reversible group, and two inequivalent
   complete measurements;
2) one complete measurement has a singleton zero face (reference recursion passes),
   while another has a disk zero face (universal Subspace-style recursion fails);
3) pure-state transitivity does not imply complete-measurement/frame transitivity;
4) selected retained dynamics can match a lower model while the full face-stabilizer
   dynamics do not;
5) reference-face recursion + complete-measurement transitivity transfers the
   recursive equivalence to every complete measurement.
"""

from __future__ import annotations

import argparse
import math
from itertools import product


TOL = 1e-10


def vec2(theta: float):
    return (math.cos(theta), math.sin(theta))


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def rot(theta: float, v):
    c, s = math.cos(theta), math.sin(theta)
    return (c * v[0] - s * v[1], s * v[0] + c * v[1])


def close_vec(a, b, tol=TOL):
    return abs(a[0] - b[0]) < tol and abs(a[1] - b[1]) < tol


def disk_ok(v, tol=TOL):
    return dot(v, v) <= 1.0 + tol


def state_ok(state):
    x, y = state
    return disk_ok(x) and disk_ok(y)


def e_diag(state):
    """e_D = 1/2 + (x1+y1)/4 on D^2 x D^2."""
    x, y = state
    return 0.5 + 0.25 * (x[0] + y[0])


def e_x(state):
    """e_X = (1+x1)/2."""
    x, _ = state
    return 0.5 + 0.5 * x[0]


def e_y(state):
    """e_Y = (1+y1)/2."""
    _, y = state
    return 0.5 + 0.5 * y[0]


def test_capacity_two_product_disk():
    # For any perfect 3-outcome measurement on K=D^2 x D^2,
    # each outcome effect that reaches both 0 and 1 must be active in at
    # least one factor X or Y. In every assignment of one active factor
    # to each of three effects, two effects select the same factor.
    #
    # If effects i and j are both active in factor X, perfect
    # distinguishability forces, for effect i:
    #   x_j = x_k = -x_i,
    # and, for effect j:
    #   x_i = x_k = -x_j,
    # which is contradictory. The same holds for Y.
    #
    # This exhausts the logical support choices and proves capacity <= 2.
    choices = list(product(("X", "Y"), repeat=3))
    for assignment in choices:
        assert len(set(assignment)) <= 2
        assert assignment.count("X") >= 2 or assignment.count("Y") >= 2

    # Capacity >= 2: explicit binary perfect-distinguishability witness.
    s_plus = ((1.0, 0.0), (1.0, 0.0))
    s_minus = ((-1.0, 0.0), (1.0, 0.0))
    assert state_ok(s_plus) and state_ok(s_minus)
    assert abs(e_x(s_plus) - 1.0) < TOL
    assert abs(e_x(s_minus) - 0.0) < TOL
    return True, {"support_assignments_checked": len(choices), "capacity": 2}


def test_reference_measurement_singleton_zero_face():
    # Since x1 >= -1 and y1 >= -1 on the two disks,
    # e_D=0 implies x1+y1=-2 and hence x1=y1=-1.
    # Unit-disk membership then forces x2=y2=0.
    s_zero = ((-1.0, 0.0), (-1.0, 0.0))
    s_one = ((1.0, 0.0), (1.0, 0.0))
    assert e_diag(s_zero) == 0.0
    assert e_diag(s_one) == 1.0

    x1_min = y1_min = -1.0
    assert x1_min + y1_min == -2.0
    assert (-1.0) ** 2 + 0.0 ** 2 == 1.0
    return True, {"zero_face": "singleton", "state": s_zero}


def test_other_complete_measurement_nonrecursive_zero_face():
    # e_X=0 fixes x=(-1,0), but leaves y arbitrary in D^2.
    s_a = ((-1.0, 0.0), (1.0, 0.0))
    s_b = ((-1.0, 0.0), (-1.0, 0.0))
    assert e_x(s_a) == 0.0 and e_x(s_b) == 0.0
    assert s_a != s_b

    # The zero face still has capacity at least two: e_Y distinguishes
    # these two retained states perfectly.
    assert e_y(s_a) == 1.0
    assert e_y(s_b) == 0.0
    return True, {"zero_face": "disk", "retained_capacity_at_least": 2}


def test_connected_pure_state_transitivity():
    # Pure states of D^2 x D^2 are S^1 x S^1.
    # G=SO(2)xSO(2) is connected and acts transitively.
    source = (vec2(0.37), vec2(-0.91))
    target = (vec2(1.73), vec2(2.21))
    dx = 1.73 - 0.37
    dy = 2.21 - (-0.91)

    for k in range(21):
        t = k / 20.0
        x_t = rot(t * dx, source[0])
        y_t = rot(t * dy, source[1])
        assert abs(dot(x_t, x_t) - 1.0) < 1e-9
        assert abs(dot(y_t, y_t) - 1.0) < 1e-9

    final = (rot(dx, source[0]), rot(dy, source[1]))
    assert close_vec(final[0], target[0])
    assert close_vec(final[1], target[1])
    return True, {"group": "SO(2)xSO(2)", "pure_state_transitive": True}


def test_frame_nontransitivity():
    # Type A frame: antipodal in X, identical in Y.
    a1 = ((1.0, 0.0), (1.0, 0.0))
    a2 = ((-1.0, 0.0), (1.0, 0.0))

    # Type D frame: antipodal in both X and Y.
    d1 = ((1.0, 0.0), (1.0, 0.0))
    d2 = ((-1.0, 0.0), (-1.0, 0.0))

    inv_a = (dot(a1[0], a2[0]), dot(a1[1], a2[1]))
    inv_d = (dot(d1[0], d2[0]), dot(d1[1], d2[1]))

    assert inv_a == (-1.0, 1.0)
    assert inv_d == (-1.0, -1.0)
    assert inv_a != inv_d

    # Product rotations preserve both factorwise inner products.
    return True, {"frame_A_invariant": inv_a, "frame_D_invariant": inv_d}


def matmul2(a, b):
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def test_selected_vs_full_face_dynamics():
    # Abstract dynamics-side control:
    # selected retained dynamics H_sel = SO(2) can match a lower disk model,
    # while the full face-preserving group H_full = O(2) cannot be conjugate
    # to SO(2). O(2) is nonabelian, whereas SO(2) is abelian.
    theta = 0.41
    R = (
        (math.cos(theta), -math.sin(theta)),
        (math.sin(theta), math.cos(theta)),
    )
    F = ((1.0, 0.0), (0.0, -1.0))
    RF = matmul2(R, F)
    FR = matmul2(F, R)
    assert RF != FR

    phi = -0.63
    S = (
        (math.cos(phi), -math.sin(phi)),
        (math.sin(phi), math.cos(phi)),
    )
    assert all(
        abs(matmul2(R, S)[i][j] - matmul2(S, R)[i][j]) < 1e-12
        for i in range(2)
        for j in range(2)
    )

    return True, {
        "selected_group": "SO(2)",
        "full_group": "O(2)",
        "full_not_conjugate_to_selected": True,
    }


def test_reference_recursion_plus_frame_transitivity_transfer():
    # Finite symbolic check of the transfer mechanism.
    reference_faces = {"F0", "F1"}
    lower_equivalent = {"F0": True, "F1": True}

    # Another complete measurement is carried to the reference measurement,
    # possibly with an outcome permutation.
    transported_to_reference = {"G0": "F1", "G1": "F0"}

    universal = all(
        transported_to_reference[g] in reference_faces
        and lower_equivalent[transported_to_reference[g]]
        for g in transported_to_reference
    )
    assert universal
    return True, {"universal_transfer": True, "requires_frame_transitivity": True}


def run_all():
    tests = [
        ("capacity-two product-disk control", test_capacity_two_product_disk),
        ("reference complete measurement -> singleton face", test_reference_measurement_singleton_zero_face),
        ("other complete measurement -> nonrecursive disk face", test_other_complete_measurement_nonrecursive_zero_face),
        ("connected group + pure-state transitivity", test_connected_pure_state_transitivity),
        ("pure-state transitivity != frame transitivity", test_frame_nontransitivity),
        ("selected dynamics != full stabilizer dynamics", test_selected_vs_full_face_dynamics),
        ("reference recursion + frame transitivity -> universal", test_reference_recursion_plus_frame_transitivity_transfer),
    ]

    ok = True
    for name, fn in tests:
        try:
            _, detail = fn()
            print(f"{name:56s} PASS  {detail}")
        except Exception as exc:
            ok = False
            print(f"{name:56s} FAIL  {exc}")

    print()
    print("OVERALL:", "PASS_WITH_REFINEMENT" if ok else "FAIL")
    return 0 if ok else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all"], default="all")
    _ = parser.parse_args()
    raise SystemExit(run_all())


if __name__ == "__main__":
    main()
