#!/usr/bin/env python3
"""
QM Core 004C — operational capacity and effect-completeness gate.

Standard-library-only finite witnesses for:
1. pairwise perfect distinguishability != joint distinguishability/capacity,
2. capacity invariance under readout-preserving relabeling,
3. declared product measurements give a supermultiplicative capacity witness,
4. operational capacity does not imply no-restriction/effect completeness,
5. tomographic spanning does not imply no-restriction.

Run:
    python audits/science/2026-09-08_qm_core_004c_capacity_effect_completeness_gate.py --mode all
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations, permutations, product


def rank_rational(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = c = 0
    while r < m and c < n:
        pivot = next((i for i in range(r, m) if a[i][c] != 0), None)
        if pivot is None:
            c += 1
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                f = a[i][c]
                a[i] = [a[i][j] - f * a[r][j] for j in range(n)]
        r += 1
        c += 1
    return r


def measurement_normalized(states, measurement):
    return all(
        sum(effect.get(s, Fraction(0)) for effect in measurement.values()) == 1
        for s in states
    )


def jointly_distinguishable(subset, measurements):
    subset = tuple(subset)
    n = len(subset)
    if n <= 1:
        return True
    for measurement in measurements.values():
        outcomes = tuple(measurement)
        if len(outcomes) < n:
            continue
        for chosen in permutations(outcomes, n):
            ok = True
            for i, state_i in enumerate(subset):
                for j, state_j in enumerate(subset):
                    target = Fraction(1 if i == j else 0)
                    if measurement[chosen[i]].get(state_j, Fraction(0)) != target:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return True
    return False


def operational_capacity(states, measurements):
    states = tuple(states)
    cap = 1 if states else 0
    for n in range(2, len(states) + 1):
        if any(jointly_distinguishable(ss, measurements) for ss in combinations(states, n)):
            cap = n
    return cap


def pairwise_vs_joint_witness():
    states = ("A", "B", "C")
    measurements = {
        "M_AB": {
            "a": {"A": Fraction(1), "B": Fraction(0), "C": Fraction(1, 2)},
            "b": {"A": Fraction(0), "B": Fraction(1), "C": Fraction(1, 2)},
        },
        "M_AC": {
            "a": {"A": Fraction(1), "C": Fraction(0), "B": Fraction(1, 2)},
            "c": {"A": Fraction(0), "C": Fraction(1), "B": Fraction(1, 2)},
        },
        "M_BC": {
            "b": {"B": Fraction(1), "C": Fraction(0), "A": Fraction(1, 2)},
            "c": {"B": Fraction(0), "C": Fraction(1), "A": Fraction(1, 2)},
        },
    }
    normalized = all(measurement_normalized(states, m) for m in measurements.values())
    pairwise = all(jointly_distinguishable(pair, measurements) for pair in combinations(states, 2))
    triple = jointly_distinguishable(states, measurements)
    cap = operational_capacity(states, measurements)
    return normalized and pairwise and not triple and cap == 2, cap


def relabel_model(states, measurements):
    state_map = {s: f"s{i}" for i, s in enumerate(states)}
    new_states = tuple(state_map[s] for s in states)
    new_measurements = {}
    for mk, measurement in measurements.items():
        new_m = {}
        for ok, effect in measurement.items():
            new_m[f"o_{ok}"] = {state_map[s]: p for s, p in effect.items()}
        new_measurements[f"R_{mk}"] = new_m
    return new_states, new_measurements


def capacity_invariance_witness():
    states = ("A", "B", "C")
    measurements = {
        "M_AB": {
            "a": {"A": Fraction(1), "B": Fraction(0), "C": Fraction(1, 2)},
            "b": {"A": Fraction(0), "B": Fraction(1), "C": Fraction(1, 2)},
        },
        "M_AC": {
            "a": {"A": Fraction(1), "C": Fraction(0), "B": Fraction(1, 2)},
            "c": {"A": Fraction(0), "C": Fraction(1), "B": Fraction(1, 2)},
        },
        "M_BC": {
            "b": {"B": Fraction(1), "C": Fraction(0), "A": Fraction(1, 2)},
            "c": {"B": Fraction(0), "C": Fraction(1), "A": Fraction(1, 2)},
        },
    }
    c0 = operational_capacity(states, measurements)
    rs, rm = relabel_model(states, measurements)
    c1 = operational_capacity(rs, rm)
    return c0 == c1 == 2, (c0, c1)


def product_capacity_witness():
    local_states = (0, 1)
    local_measurement = {
        "0": {0: Fraction(1), 1: Fraction(0)},
        "1": {0: Fraction(0), 1: Fraction(1)},
    }
    local_measurements = {"Z": local_measurement}
    cap_local = operational_capacity(local_states, local_measurements)

    global_states = tuple(product(local_states, local_states))
    global_effects = {}
    for oa, ob in product(("0", "1"), repeat=2):
        global_effects[(oa, ob)] = {
            (a, b): local_measurement[oa][a] * local_measurement[ob][b]
            for a, b in global_states
        }
    global_measurements = {"ZxZ": global_effects}
    cap_global = operational_capacity(global_states, global_measurements)
    return cap_local == 2 and cap_global == 4, (cap_local, cap_global)


def capacity_not_effect_completeness_witness():
    grid = (Fraction(0), Fraction(1, 2), Fraction(1))
    emax_grid = {(a, b) for a in grid for b in grid}
    ephys = {
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(1)),
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    }
    strict_subset = ephys < emax_grid

    states = ("0", "1")
    measurement = {
        "0": {"0": Fraction(1), "1": Fraction(0)},
        "1": {"0": Fraction(0), "1": Fraction(1)},
    }
    cap = operational_capacity(states, {"Z": measurement})
    return strict_subset and cap == 2, (len(ephys), len(emax_grid), cap)


def tomography_not_no_restriction_witness():
    allowed = [
        (Fraction(1), 0, 0, 0),
        (Fraction(1, 2), Fraction(1, 2), 0, 0),
        (Fraction(1, 2), Fraction(-1, 2), 0, 0),
        (Fraction(1, 2), 0, Fraction(1, 2), 0),
        (Fraction(1, 2), 0, Fraction(-1, 2), 0),
        (Fraction(1, 2), 0, 0, Fraction(1, 2)),
        (Fraction(1, 2), 0, 0, Fraction(-1, 2)),
    ]
    span_rank = rank_rational(allowed)

    extra = (Fraction(1, 2), Fraction(1, 5), Fraction(1, 5), 0)
    a, bx, by, bz = extra
    b2 = bx * bx + by * by + bz * bz
    valid_effect = b2 <= a * a and b2 <= (1 - a) * (1 - a)
    absent = extra not in set(allowed)
    return span_rank == 4 and valid_effect and absent, (span_rank, extra)


def run_all():
    checks = []

    ok, detail = pairwise_vs_joint_witness()
    checks.append(("pairwise != joint capacity", ok, detail))

    ok, detail = capacity_invariance_witness()
    checks.append(("capacity invariant under typed relabeling", ok, detail))

    ok, detail = product_capacity_witness()
    checks.append(("declared product capacity witness", ok, detail))

    ok, detail = capacity_not_effect_completeness_witness()
    checks.append(("capacity != effect completeness", ok, detail))

    ok, detail = tomography_not_no_restriction_witness()
    checks.append(("tomography != no-restriction", ok, detail))

    for name, ok, detail in checks:
        print(f"{name:<42} {'PASS' if ok else 'FAIL'}  {detail}")

    overall = all(ok for _, ok, _ in checks)
    print()
    print("OVERALL:", "PASS_WITH_REFINEMENT" if overall else "FAIL")
    return 0 if overall else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    args = parser.parse_args()
    if args.mode == "all":
        raise SystemExit(run_all())


if __name__ == "__main__":
    main()
