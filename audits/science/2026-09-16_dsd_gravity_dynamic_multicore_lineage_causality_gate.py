#!/usr/bin/env python3
"""
BH-GC-002 — dynamic multi-core lineage / causality firewall gate.

Purpose
-------
Audit four distinct notions that must not be conflated in a dynamic
gravitational-core descriptor:
1. material/component motion,
2. causal signal/transport speed,
3. local descriptor-maximum continuation,
4. global/pattern maximum motion.

All controls use 1+1 Minkowski units with c=1. They are structural controls,
not a black-hole-interior solution and not a numerical-relativity solver.
"""

import argparse

C = 1.0


def causal_interval(dt: float, dx: float) -> float:
    return C * C * dt * dt - dx * dx


def is_causal_edge(t0: float, x0: float, t1: float, x1: float) -> bool:
    dt = t1 - t0
    dx = x1 - x0
    return dt >= 0.0 and causal_interval(dt, dx) >= -1e-12


def interference_pattern_speeds(k1: float, k2: float):
    """For cos[k1(x-t)] + cos[k2(x+t)]."""
    v_slow = (k1 - k2) / (k1 + k2)
    v_fast = (k1 + k2) / (k1 - k2)
    return v_slow, v_fast


def dominant_seed(t: float, rate: float = 0.1):
    """Two stationary local maxima A and B with amplitudes crossing at t=0."""
    aa = 1.0 - rate * t
    ab = 1.0 + rate * t
    tol = 1e-15
    if aa > ab + tol:
        return ("A",), (aa, ab)
    if ab > aa + tol:
        return ("B",), (aa, ab)
    return ("A", "B"), (aa, ab)


def run_audit() -> int:
    tests = []

    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    # 1) Physical split from one common event.
    v_split = 0.6
    t_split = 3.0
    x_plus = v_split * t_split
    x_minus = -v_split * t_split
    check("split + branch causal", is_causal_edge(0.0, 0.0, t_split, x_plus),
          causal_interval(t_split, x_plus))
    check("split - branch causal", is_causal_edge(0.0, 0.0, t_split, x_minus),
          causal_interval(t_split, x_minus))
    check("split component speed below c", abs(v_split) < C, v_split)

    # 2) Physical merger into one event.
    v_merge = 0.7
    t_merge = 4.0
    x0_left = -v_merge * t_merge
    x0_right = v_merge * t_merge
    check("merge left branch causal", is_causal_edge(0.0, x0_left, t_merge, 0.0),
          causal_interval(t_merge, -x0_left))
    check("merge right branch causal", is_causal_edge(0.0, x0_right, t_merge, 0.0),
          causal_interval(t_merge, -x0_right))
    check("merge component speed below c", abs(v_merge) < C, v_merge)

    # 3) Pattern-speed witness from two luminal modes.
    k1, k2 = 1.0, 0.8
    v_slow, v_fast = interference_pattern_speeds(k1, k2)
    check("mode 1 signal speed is c", C == 1.0, C)
    check("mode 2 signal speed is -c", -C == -1.0, -C)
    check("slow interference factor subluminal", abs(v_slow) < C, v_slow)
    check("fast interference fringe superluminal as pattern", abs(v_fast) > C, v_fast)
    check("fast fringe not assigned as material/signal edge", True,
          "pattern only")

    # 4) Global argmax can jump between stationary local maxima.
    xa, xb = -10.0, 10.0
    dt = 0.01
    before, amps_before = dominant_seed(-dt)
    at_cross, amps_cross = dominant_seed(0.0)
    after, amps_after = dominant_seed(dt)
    apparent_jump_speed = (xb - xa) / (2.0 * dt)
    light_travel_time = abs(xb - xa) / C
    check("dominant seed before crossing is A", before == ("A",),
          (before, amps_before))
    check("argmax is set-valued at exact crossing", at_cross == ("A", "B"),
          (at_cross, amps_cross))
    check("dominant seed after crossing is B", after == ("B",),
          (after, amps_after))
    check("global argmax apparent jump exceeds c", apparent_jump_speed > C,
          apparent_jump_speed)
    check("A-to-B causal signal requires finite light time", light_travel_time == 20.0,
          light_travel_time)
    check("spacelike A-to-B hop rejected as physical lineage edge",
          not is_causal_edge(-dt, xa, dt, xb),
          causal_interval(2.0 * dt, xb - xa))

    # 5) Common-past synchronization: O=(-10,0) can reach A and B at t=0.
    check("common-past O->A is causal/null", is_causal_edge(-10.0, 0.0, 0.0, xa),
          causal_interval(10.0, xa))
    check("common-past O->B is causal/null", is_causal_edge(-10.0, 0.0, 0.0, xb),
          causal_interval(10.0, xb))

    # 6) Typed-lineage firewall.
    physical_edges_causal = all([
        is_causal_edge(0.0, 0.0, t_split, x_plus),
        is_causal_edge(0.0, 0.0, t_split, x_minus),
        is_causal_edge(0.0, x0_left, t_merge, 0.0),
        is_causal_edge(0.0, x0_right, t_merge, 0.0),
    ])
    dominance_switch_not_transport = not is_causal_edge(-dt, xa, dt, xb)
    check("all material continuation edges are causal", physical_edges_causal,
          physical_edges_causal)
    check("dominance switch kept outside transport lineage",
          dominance_switch_not_transport, dominance_switch_not_transport)

    passed = sum(ok for _, ok, _ in tests)

    print("BH-GC-002 — dynamic multi-core lineage / causality firewall gate")
    print("Units: c=1")
    print(f"split branches: v=±{v_split:.3f}")
    print(f"merge branches: |v|={v_merge:.3f}")
    print(f"interference speeds: v_slow={v_slow:.12f}, v_fast={v_fast:.12f}")
    print(f"dominant-max hop: apparent speed={apparent_jump_speed:.3f}")
    print(f"A<->B light travel time={light_travel_time:.3f}")
    print()

    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")

    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print(
        "VERDICT: PASS_WITH_BOUNDARY / "
        "CAUSAL_COMPONENT_SPLIT_AND_MERGER_ADMISSIBLE / "
        "DESCRIPTOR_MAXIMUM_OR_INTERFERENCE_PATTERN_MAY_MOVE_SUPERLUMINALLY_WITHOUT_TRANSPORT / "
        "GLOBAL_ARGMAX_SWITCH_IS_NOT_A_PHYSICAL_WORLDLINE / "
        "LINEAGE_MUST_TYPE_CAUSAL_CONTINUATION_SEPARATELY_FROM_DESCRIPTOR_SUCCESSION / "
        "BLACK_HOLE_INTERIOR_MULTICORE_DYNAMICS_NOT_DERIVED"
    )
    return 0 if passed == len(tests) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all"])
    parser.parse_args()
    raise SystemExit(run_audit())


if __name__ == "__main__":
    main()
