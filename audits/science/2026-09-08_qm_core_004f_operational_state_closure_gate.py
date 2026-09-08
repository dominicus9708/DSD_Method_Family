from fractions import Fraction
import argparse


def in_open_unit(x: Fraction) -> bool:
    return Fraction(0) < x < Fraction(1)


def test_open_interval_convexity():
    samples = [
        (Fraction(1, 5), Fraction(4, 5), Fraction(2, 5)),
        (Fraction(1, 10), Fraction(9, 10), Fraction(1, 2)),
        (Fraction(1, 3), Fraction(2, 3), Fraction(0)),
        (Fraction(1, 3), Fraction(2, 3), Fraction(1)),
    ]
    for x, y, lam in samples:
        z = lam * x + (1 - lam) * y
        assert in_open_unit(z)
    return True, samples


def test_bounded_convex_not_closed():
    seq = [Fraction(1, n) for n in range(2, 12)]
    assert all(in_open_unit(x) for x in seq)
    limit = Fraction(0)
    assert not in_open_unit(limit)
    return True, (seq[-1], limit)


def test_banach_codomain_does_not_close_image():
    # The codomain may be complete while the realized physical image is not closed.
    seq = [Fraction(1, n) for n in range(2, 12)]
    image = tuple(seq)
    assert all(in_open_unit(v) for v in image)
    assert Fraction(0) not in image
    return True, (image[-1], Fraction(0))


def test_logical_completion_does_not_add_limit_state():
    def descriptor(x: Fraction):
        assert in_open_unit(x)
        return ("FORMED", "PROPERTY_DEFINED", "READOUT_DEFINED", x)

    descriptors = [descriptor(Fraction(1, n)) for n in range(2, 12)]
    assert all(len(d) == 4 for d in descriptors)
    zero_admitted = in_open_unit(Fraction(0))
    assert not zero_admitted
    return True, (len(descriptors), zero_admitted)


def test_limit_admission_repairs_sequence():
    original = lambda x: Fraction(0) < x < Fraction(1)
    completed = lambda x: Fraction(0) <= x <= Fraction(1)

    seq = [Fraction(1, n) for n in range(2, 12)]
    assert all(original(x) for x in seq)
    limit = Fraction(0)
    assert not original(limit)
    assert completed(limit)
    return True, limit


def test_closure_changes_state_carrier():
    test_points = (Fraction(0), Fraction(1, 2), Fraction(1))
    open_membership = tuple(in_open_unit(x) for x in test_points)
    closed_membership = tuple(Fraction(0) <= x <= Fraction(1) for x in test_points)
    assert open_membership == (False, True, False)
    assert closed_membership == (True, True, True)
    assert open_membership != closed_membership
    return True, (open_membership, closed_membership)


def run_all():
    tests = [
        ("open state image remains convex under mixing", test_open_interval_convexity),
        ("bounded + convex does not imply closed", test_bounded_convex_not_closed),
        ("Banach codomain does not close physical image", test_banach_codomain_does_not_close_image),
        ("logical descriptor completion != topological closure", test_logical_completion_does_not_add_limit_state),
        ("explicit limit admission repairs witness sequence", test_limit_admission_repairs_sequence),
        ("closure augmentation changes physical carrier", test_closure_changes_state_carrier),
    ]

    ok = True
    for name, fn in tests:
        try:
            _, detail = fn()
            print(f"{name:52s} PASS  {detail}")
        except Exception as exc:
            ok = False
            print(f"{name:52s} FAIL  {exc}")

    print("\nOVERALL:", "PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all"], default="all")
    _ = parser.parse_args()
    raise SystemExit(run_all())


if __name__ == "__main__":
    main()
