from fractions import Fraction
from dataclasses import dataclass
from typing import Tuple
import argparse


@dataclass(frozen=True)
class Prep:
    name: str
    stats: Tuple[Fraction, ...]


def mix_stats(a: Tuple[Fraction, ...], b: Tuple[Fraction, ...], lam: Fraction):
    return tuple(lam*x + (1-lam)*y for x, y in zip(a, b))


def test_randomized_preparation_affinity():
    a = Prep('A', (Fraction(1,4), Fraction(3,4)))
    b = Prep('B', (Fraction(3,4), Fraction(1,4)))
    lam = Fraction(2,5)
    m = mix_stats(a.stats, b.stats, lam)
    expected0 = lam*a.stats[0] + (1-lam)*b.stats[0]
    expected1 = lam*a.stats[1] + (1-lam)*b.stats[1]
    assert m == (expected0, expected1)
    assert m == (Fraction(11,20), Fraction(9,20))
    return True, m


def test_nonaffine_readout_counterexample():
    lam = Fraction(1,2)
    x0, x1 = Fraction(0), Fraction(1)
    xm = lam*x0 + (1-lam)*x1
    lhs = xm*xm
    rhs = lam*(x0*x0) + (1-lam)*(x1*x1)
    assert lhs == Fraction(1,4)
    assert rhs == Fraction(1,2)
    assert lhs != rhs
    return True, (lhs, rhs)


def test_operational_quotient_convexity():
    p1 = Prep('P1', (Fraction(1), Fraction(0)))
    p2 = Prep('P2', (Fraction(0), Fraction(1)))
    p3 = Prep('P3', (Fraction(1,2), Fraction(1,2)))
    mix12 = mix_stats(p1.stats, p2.stats, Fraction(1,2))
    assert mix12 == p3.stats

    quotient = {p.stats for p in (p1, p2, p3)}
    assert len(quotient) == 3
    assert mix12 in quotient

    m = mix_stats(p3.stats, p1.stats, Fraction(1,3))
    assert m == (Fraction(5,6), Fraction(1,6))
    return True, m


def test_ordered_cone_construction():
    s1 = (Fraction(1), Fraction(1), Fraction(0))
    s2 = (Fraction(1), Fraction(0), Fraction(1))
    a, b = Fraction(1,3), Fraction(1,2)
    v = tuple(a*x + b*y for x, y in zip(s1, s2))
    assert v == (Fraction(5,6), Fraction(1,3), Fraction(1,2))
    assert v[0] > 0

    c = Fraction(3,2)
    cv = tuple(c*x for x in v)
    assert cv[0] == Fraction(5,4)

    assert v != (0,0,0)
    assert v[0] > 0
    return True, v


def test_mixture_preserving_transformation_affinity():
    lam = Fraction(2,5)
    x, y = Fraction(1,5), Fraction(4,5)
    xm = lam*x + (1-lam)*y

    lhs = 1 - xm
    rhs = lam*(1-x) + (1-lam)*(1-y)
    assert lhs == rhs

    nlhs = xm*xm
    nrhs = lam*(x*x) + (1-lam)*(y*y)
    assert nlhs != nrhs
    return True, (lhs, nlhs, nrhs)


def test_effect_completeness_independence():
    grid = [Fraction(0), Fraction(1,2), Fraction(1)]
    emax = {(a,b) for a in grid for b in grid}
    ephys = {
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(1)),
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    }
    assert ephys < emax
    assert len(emax) == 9 and len(ephys) == 4
    return True, (len(ephys), len(emax))


def run_all():
    tests = [
        ('randomized preparation -> affine statistics', test_randomized_preparation_affinity),
        ('non-affine readout counterexample', test_nonaffine_readout_counterexample),
        ('operational quotient convexity', test_operational_quotient_convexity),
        ('ordered cone construction', test_ordered_cone_construction),
        ('mixture-preserving transformation -> affine', test_mixture_preserving_transformation_affinity),
        ('ordered carrier != no-restriction', test_effect_completeness_independence),
    ]
    ok = True
    for name, fn in tests:
        try:
            _, detail = fn()
            print(f'{name:44s} PASS  {detail}')
        except Exception as exc:
            ok = False
            print(f'{name:44s} FAIL  {exc}')
    print('\nOVERALL:', 'PASS_WITH_REFINEMENT' if ok else 'FAIL')
    return 0 if ok else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['all'], default='all')
    _ = parser.parse_args()
    raise SystemExit(run_all())


if __name__ == '__main__':
    main()
