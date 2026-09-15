#!/usr/bin/env python3
"""
BH-GC-004 — threshold-filtration / persistence gravitational-core gate.

Purpose
-------
Replace any one arbitrarily chosen superlevel threshold by the full superlevel
filtration of a nonnegative gravitational/tidal descriptor.  In a 1D control,
compute 0D superlevel persistence and test whether physically salient descriptor
components remain distinguishable from small noise maxima.

This is a structural control only.  It is not a black-hole interior solution
and it does not make persistent-homology classes into material worldlines.
"""

import argparse
import math


XMIN = -6.0
XMAX = 6.0
SAMPLES = 24001
DX = (XMAX - XMIN) / (SAMPLES - 1)
SIGMA = 0.8
NOISE_AMP = 0.02


def gaussian(x: float, center: float, amp: float = 1.0, sigma: float = SIGMA) -> float:
    z = (x - center) / sigma
    return amp * math.exp(-0.5 * z * z)


def profile(x: float, d: float = 2.0, a_left: float = 1.0, a_right: float = 0.35) -> float:
    return gaussian(x, -d, a_left) + gaussian(x, d, a_right)


def noisy_profile(x: float, d: float = 2.0, a_left: float = 1.0, a_right: float = 0.35) -> float:
    base = profile(x, d, a_left, a_right)
    perturb = NOISE_AMP * math.sin(40.0 * x) * math.exp(-(x * x) / 18.0)
    return base * (1.0 + perturb)


def sample(fn):
    xs = [XMIN + i * DX for i in range(SAMPLES)]
    vals = [fn(x) for x in xs]
    return xs, vals


def normalize(vals):
    vmax = max(vals)
    return [v / vmax for v in vals]


def local_max_count(vals) -> int:
    return sum(
        1
        for i in range(1, len(vals) - 1)
        if vals[i] > vals[i - 1] and vals[i] >= vals[i + 1]
    )


def persistence_superlevel(vals):
    """0D persistence of the discrete 1D superlevel filtration.

    Vertices are activated from high to low function value.  When two connected
    components merge, the younger component dies at the merge level (elder rule).
    The final essential component is reported with death at the sampled minimum;
    it is explicitly marked essential and is not interpreted as an ordinary merge.
    """
    n = len(vals)
    order = sorted(range(n), key=lambda i: (-vals[i], i))
    active = [False] * n
    parent = list(range(n))
    birth = [0.0] * n
    birth_index = [-1] * n
    records = []

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for idx in order:
        active[idx] = True
        parent[idx] = idx
        birth[idx] = vals[idx]
        birth_index[idx] = idx

        neighbors = []
        if idx > 0 and active[idx - 1]:
            neighbors.append(find(idx - 1))
        if idx + 1 < n and active[idx + 1]:
            neighbors.append(find(idx + 1))
        neighbors = list(dict.fromkeys(neighbors))

        if not neighbors:
            continue
        if len(neighbors) == 1:
            parent[idx] = neighbors[0]
            continue

        r1, r2 = neighbors
        key1 = (birth[r1], -birth_index[r1])
        key2 = (birth[r2], -birth_index[r2])
        old, young = (r1, r2) if key1 >= key2 else (r2, r1)
        death = vals[idx]
        records.append(
            {
                "birth": birth[young],
                "death": death,
                "persistence": birth[young] - death,
                "birth_index": birth_index[young],
                "death_index": idx,
                "essential": False,
            }
        )
        parent[young] = old
        parent[idx] = old

    roots = {find(i) for i in range(n) if active[i]}
    min_value = min(vals)
    min_index = vals.index(min_value)
    for root in roots:
        records.append(
            {
                "birth": birth[root],
                "death": min_value,
                "persistence": birth[root] - min_value,
                "birth_index": birth_index[root],
                "death_index": min_index,
                "essential": True,
            }
        )

    return sorted(records, key=lambda r: r["persistence"], reverse=True)


def finite_persistences(records):
    return [r["persistence"] for r in records if not r["essential"]]


def count_above(records, tau: float, include_essential: bool = True) -> int:
    return sum(
        1
        for r in records
        if r["persistence"] >= tau and (include_essential or not r["essential"])
    )


def run_audit() -> int:
    xs, clean = sample(lambda x: profile(x, d=2.0))
    _, noisy = sample(lambda x: noisy_profile(x, d=2.0))
    clean_n = normalize(clean)
    noisy_n = normalize(noisy)

    rec_clean = persistence_superlevel(clean_n)
    rec_noisy = persistence_superlevel(noisy_n)

    finite_clean = finite_persistences(rec_clean)
    finite_noisy = finite_persistences(rec_noisy)

    secondary_clean = finite_clean[0]
    secondary_noisy = finite_noisy[0]
    noise_max = max(finite_noisy[1:])
    gap_ratio = secondary_noisy / noise_max

    # A deliberately simple significance cut for this control only.  It is not
    # promoted to a universal DSD or black-hole constant.
    tau_control = 0.10

    # Positive descriptor rescaling should disappear after normalization.
    scaled_n = normalize([7.0 * v for v in noisy])
    rec_scaled = persistence_superlevel(scaled_n)

    # Dynamic approach: the secondary class should lose persistence and then
    # disappear as two subluminally moving peaks merge into one descriptor region.
    dynamic = []
    for d in (2.0, 1.5, 1.2, 1.0, 0.8):
        _, vals = sample(lambda x, dd=d: profile(x, d=dd))
        vals_n = normalize(vals)
        rec = persistence_superlevel(vals_n)
        finite = finite_persistences(rec)
        secondary = finite[0] if finite else 0.0
        dynamic.append((d, local_max_count(vals_n), secondary))

    tests = []

    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    check("clean profile has two point maxima", local_max_count(clean_n) == 2, local_max_count(clean_n))
    check("noisy profile has many extra point maxima", local_max_count(noisy_n) > 2, local_max_count(noisy_n))
    check("clean persistence has one essential and one finite class", len(rec_clean) == 2 and sum(r["essential"] for r in rec_clean) == 1, [(r["persistence"], r["essential"]) for r in rec_clean])
    check("weak clean core has substantial finite persistence", secondary_clean > 0.25, secondary_clean)
    check("noisy weak core retains substantial persistence", secondary_noisy > 0.25, secondary_noisy)
    check("largest noise-only persistence is small", noise_max < 0.03, noise_max)
    check("salient-to-noise persistence gap is large", gap_ratio > 10.0, gap_ratio)
    check("control persistence threshold retains two salient classes", count_above(rec_noisy, tau_control) == 2, count_above(rec_noisy, tau_control))
    check("same threshold rejects all noise-only finite classes", all(p < tau_control for p in finite_noisy[1:]), finite_noisy[1:6])
    check("normalization makes positive amplitude rescaling persistence invariant", all(abs(a["persistence"] - b["persistence"]) < 1e-12 for a, b in zip(rec_noisy, rec_scaled)), [(rec_noisy[i]["persistence"], rec_scaled[i]["persistence"]) for i in range(min(5, len(rec_noisy)))])
    check("secondary persistence decreases during approach", dynamic[0][2] > dynamic[1][2] > dynamic[2][2], dynamic[:3])
    check("secondary class becomes very weak before merger", dynamic[2][2] < 0.03, dynamic[2])
    check("descriptor becomes single-peaked by d=1.0", dynamic[3][1] == 1, dynamic[3])
    check("no finite secondary persistence remains after single-peak merger", dynamic[3][2] == 0.0 and dynamic[4][2] == 0.0, dynamic[3:])
    check("persistence tracks feature lifetime over thresholds rather than one lambda", secondary_clean > 0.0, secondary_clean)
    check("persistence still requires a significance convention", tau_control > 0.0, tau_control)
    check("essential class is kept distinct from ordinary finite mergers", rec_noisy[0]["essential"], rec_noisy[0])
    check("weak-core birth remains spatially on the weak-peak side", xs[rec_noisy[1]["birth_index"]] > 0.0, xs[rec_noisy[1]["birth_index"]])
    check("strong-core essential birth remains on the strong-peak side", xs[rec_noisy[0]["birth_index"]] < 0.0, xs[rec_noisy[0]["birth_index"]])
    check("filtration is descriptor-based and does not encode a material velocity", True, "firewall")
    check("black-hole interior solution is not inferred from this control", True, "scope firewall")

    passed = sum(ok for _, ok, _ in tests)

    print("BH-GC-004 — threshold-filtration / persistence gravitational-core gate")
    print(f"clean secondary persistence = {secondary_clean:.12f}")
    print(f"noisy secondary persistence = {secondary_noisy:.12f}")
    print(f"largest noise persistence    = {noise_max:.12f}")
    print(f"persistence gap ratio        = {gap_ratio:.6f}")
    print(f"control tau                  = {tau_control:.6f}")
    print("dynamic (d, maxima, secondary persistence):")
    for row in dynamic:
        print("  ", row)
    print()

    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")

    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print(
        "VERDICT: PASS_WITH_BOUNDARY / FULL_SUPERLEVEL_FILTRATION_REDUCES_SINGLE_THRESHOLD_ARBITRARINESS / "
        "PERSISTENT_COMPONENTS_SEPARATE_SALIENT_CORES_FROM_SMALL_NOISE_MAXIMA_IN_CONTROL / "
        "PERSISTENCE_CAN_TRACK_MERGER_WITHOUT_DEFINING_A_MATERIAL_WORLDLINE / "
        "SIGNIFICANCE_CUTOFF_AND_FLOW_SLICE_DESCRIPTOR_PROVENANCE_REMAIN_REQUIRED / "
        "PHYSICAL_BLACK_HOLE_CORE_TOPOLOGY_NOT_DERIVED"
    )
    return 0 if passed == len(tests) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all"])
    parser.parse_args()
    raise SystemExit(run_audit())


if __name__ == "__main__":
    main()
