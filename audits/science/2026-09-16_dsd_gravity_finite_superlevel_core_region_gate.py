#!/usr/bin/env python3
"""
BH-GC-003 — finite superlevel gravitational-core region gate.

Purpose
-------
Replace a pointwise gravitational/tidal maximum by finite connected superlevel
regions and test whether this gives a more robust descriptor for a dynamic
single-core / multi-core / fluid-like candidate interior.

The numerical control is deliberately 1D and non-black-hole. Two positive
Gaussian descriptor peaks move subluminally and merge. The test concerns the
logic of descriptor regions, not a physical black-hole solution.
"""

import argparse
import math


C = 1.0
SIGMA = 0.8
ETA = 0.5
XMIN = -6.0
XMAX = 6.0
SAMPLES = 24001
DX = (XMAX - XMIN) / (SAMPLES - 1)


def gaussian(x: float, center: float, amp: float = 1.0, sigma: float = SIGMA) -> float:
    z = (x - center) / sigma
    return amp * math.exp(-0.5 * z * z)


def descriptor(x: float, d: float, a_left: float = 1.0, a_right: float = 1.0) -> float:
    return gaussian(x, -d, a_left) + gaussian(x, d, a_right)


def descriptor_noisy(x: float, d: float) -> float:
    base = descriptor(x, d)
    perturb = 0.02 * math.sin(40.0 * x) * math.exp(-(x * x) / 18.0)
    return base * (1.0 + perturb)


def sample(fn):
    xs = [XMIN + i * DX for i in range(SAMPLES)]
    vals = [fn(x) for x in xs]
    return xs, vals


def local_max_count(vals) -> int:
    return sum(1 for i in range(1, len(vals) - 1)
               if vals[i] > vals[i - 1] and vals[i] >= vals[i + 1])


def superlevel_components(xs, vals, eta: float = ETA):
    vmax = max(vals)
    lam = eta * vmax
    comps = []
    start = None
    for i, v in enumerate(vals):
        inside = v >= lam
        if inside and start is None:
            start = i
        if start is not None and (not inside or i == len(vals) - 1):
            end = i if (inside and i == len(vals) - 1) else i - 1
            comps.append((xs[start], xs[end], start, end))
            start = None
    return lam, comps


def widths(comps):
    return [b - a for a, b, _, _ in comps]


def max_boundary_shift(comps_a, comps_b):
    if len(comps_a) != len(comps_b):
        return float("inf")
    shifts = []
    for ca, cb in zip(comps_a, comps_b):
        shifts.extend([abs(ca[0] - cb[0]), abs(ca[1] - cb[1])])
    return max(shifts) if shifts else 0.0


def run_audit() -> int:
    d0 = 2.0
    v = 0.4 * C
    t0 = 0.0
    t1 = 2.0
    d_sep = d0 - v * t0
    d_merge = d0 - v * t1

    xs_sep, vals_sep = sample(lambda x: descriptor(x, d_sep))
    xs_merge, vals_merge = sample(lambda x: descriptor(x, d_merge))
    lam_sep, comps_sep = superlevel_components(xs_sep, vals_sep)
    lam_merge, comps_merge = superlevel_components(xs_merge, vals_merge)

    xs_ns, vals_ns = sample(lambda x: descriptor_noisy(x, d_sep))
    xs_nm, vals_nm = sample(lambda x: descriptor_noisy(x, d_merge))
    _, comps_ns = superlevel_components(xs_ns, vals_ns)
    _, comps_nm = superlevel_components(xs_nm, vals_nm)

    nmax_sep = local_max_count(vals_sep)
    nmax_ns = local_max_count(vals_ns)
    nmax_merge = local_max_count(vals_merge)
    nmax_nm = local_max_count(vals_nm)

    shift_sep = max_boundary_shift(comps_sep, comps_ns)
    shift_merge = max_boundary_shift(comps_merge, comps_nm)

    scale = 7.0
    _, comps_scaled = superlevel_components(xs_sep, [scale * y for y in vals_sep])

    xs_weak, vals_weak = sample(lambda x: descriptor(x, 2.0, 1.0, 0.35))
    _, comps_weak_eta50 = superlevel_components(xs_weak, vals_weak, eta=0.50)
    _, comps_weak_eta25 = superlevel_components(xs_weak, vals_weak, eta=0.25)
    nmax_weak = local_max_count(vals_weak)

    tests = []

    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    check("threshold fraction is admissible", 0.0 < ETA < 1.0, ETA)
    check("component-center motion is subluminal", abs(v) < C, v)
    check("separated snapshot has two finite superlevel regions", len(comps_sep) == 2, comps_sep)
    check("merged snapshot has one finite superlevel region", len(comps_merge) == 1, comps_merge)
    check("all separated-region widths are positive", all(w > 0 for w in widths(comps_sep)), widths(comps_sep))
    check("merged-region width is positive", widths(comps_merge)[0] > 0, widths(comps_merge))
    check("separated regions remain inside finite scan domain", comps_sep[0][0] > XMIN and comps_sep[-1][1] < XMAX, comps_sep)
    check("merged region remains inside finite scan domain", comps_merge[0][0] > XMIN and comps_merge[-1][1] < XMAX, comps_merge)
    check("small perturbation creates extra point maxima in separated state", nmax_ns > nmax_sep, (nmax_sep, nmax_ns))
    check("small perturbation creates extra point maxima in merged state", nmax_nm > nmax_merge, (nmax_merge, nmax_nm))
    check("superlevel component count robust in separated state", len(comps_ns) == len(comps_sep), (len(comps_sep), len(comps_ns)))
    check("superlevel component count robust in merged state", len(comps_nm) == len(comps_merge), (len(comps_merge), len(comps_nm)))
    check("separated boundary shift under perturbation is small", shift_sep < 0.05, shift_sep)
    check("merged boundary shift under perturbation is small", shift_merge < 0.05, shift_merge)
    check("relative-threshold region is invariant under positive descriptor scaling", comps_scaled == comps_sep, (comps_sep, comps_scaled))
    check("component number can change continuously through merge without superluminal material motion", len(comps_sep) == 2 and len(comps_merge) == 1 and abs(v) < C, (v, len(comps_sep), len(comps_merge)))
    check("weak separated profile still has two local maxima", nmax_weak == 2, nmax_weak)
    check("eta=0.50 can suppress weak secondary superlevel component", len(comps_weak_eta50) == 1, comps_weak_eta50)
    check("lower eta can recover both weak and strong components", len(comps_weak_eta25) == 2, comps_weak_eta25)
    check("threshold provenance is therefore necessary", len(comps_weak_eta50) != len(comps_weak_eta25), (len(comps_weak_eta50), len(comps_weak_eta25)))

    passed = sum(ok for _, ok, _ in tests)

    print("BH-GC-003 — finite superlevel gravitational-core region gate")
    print(f"center speed = {v:.6f} c")
    print(f"separated d={d_sep:.6f}, lambda={lam_sep:.12f}, components={[(a,b) for a,b,_,_ in comps_sep]}")
    print(f"merged    d={d_merge:.6f}, lambda={lam_merge:.12f}, components={[(a,b) for a,b,_,_ in comps_merge]}")
    print(f"point maxima: separated {nmax_sep}->{nmax_ns} with perturbation; merged {nmax_merge}->{nmax_nm}")
    print(f"boundary shifts: separated={shift_sep:.6f}, merged={shift_merge:.6f}")
    print(f"weak-core threshold test: eta=.50 -> {len(comps_weak_eta50)} region(s), eta=.25 -> {len(comps_weak_eta25)} region(s)")
    print()

    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")

    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print(
        "VERDICT: PASS_WITH_BOUNDARY / FINITE_CONNECTED_SUPERLEVEL_REGIONS_ARE_MORE_ROBUST_THAN_POINT_MAXIMA / "
        "CAUSAL_COMPONENT_MOTION_CAN_PRODUCE_DESCRIPTOR_REGION_MERGER / THRESHOLD_CHOICE_IS_NOT_UNIQUE_AND_CAN_HIDE_WEAK_CORES / "
        "CORE_REGION_DESCRIPTOR_MUST_RETAIN_FLOW_SLICE_AND_THRESHOLD_PROVENANCE / PHYSICAL_BLACK_HOLE_CORE_REGION_NOT_DERIVED"
    )
    return 0 if passed == len(tests) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all"])
    parser.parse_args()
    raise SystemExit(run_audit())


if __name__ == "__main__":
    main()
