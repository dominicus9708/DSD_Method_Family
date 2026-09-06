#!/usr/bin/env python3
import argparse
import math


def h2(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def qmi(c: float, m: int) -> float:
    # Equal-prior classical pointer variable correlated with two pure
    # fragment states whose overlap is c**m.
    return h2((1.0 + c ** m) / 2.0)


def helstrom_error(c: float, m: int) -> float:
    return (1.0 - math.sqrt(max(0.0, 1.0 - c ** (2 * m)))) / 2.0


def accessible_info(c: float, m: int) -> float:
    # Equal-prior binary pure-state ensemble.
    e = helstrom_error(c, m)
    return 1.0 - h2(e)


def success_opt(c: float, m: int) -> float:
    return 1.0 - helstrom_error(c, m)


def success_z_restricted(c: float, m: int) -> float:
    # |e0>=|0>, |e1>=c|0>+sqrt(1-c^2)|1>.
    # Local Z measurement on each copy; infer 1 iff any result is 1.
    return 1.0 - 0.5 * c ** (2 * m)


def pair_agreement(c: float, m: int) -> float:
    e = helstrom_error(c, m)
    return (1.0 - e) ** 2 + e ** 2


def min_fragment(c: float, delta: float, mode: str, max_m: int = 100000):
    fn = qmi if mode == "qmi" else accessible_info
    target = 1.0 - delta
    for m in range(1, max_m + 1):
        if fn(c, m) >= target:
            return m
    return None


def redundancy(N: int, m):
    if m is None or m > N:
        return 0
    return N // m


def print_thresholds(N: int, delta: float, overlaps):
    print(f"# threshold map: N={N}, delta={delta}")
    print("c,m_qmi,R_qmi,m_acc,R_acc")
    for c in overlaps:
        mq = min_fragment(c, delta, "qmi")
        ma = min_fragment(c, delta, "acc")
        print(f"{c:.5f},{mq},{redundancy(N,mq)},{ma},{redundancy(N,ma)}")


def print_access(delta: float, overlaps):
    print(f"# access map at QMI threshold, delta={delta}")
    print("c,m_qmi,I_qmi,P_opt,I_acc,P_Z,pair_agree,overlap_sq")
    for c in overlaps:
        m = min_fragment(c, delta, "qmi")
        print(
            f"{c:.5f},{m},{qmi(c,m):.12f},{success_opt(c,m):.12f},"
            f"{accessible_info(c,m):.12f},{success_z_restricted(c,m):.12f},"
            f"{pair_agreement(c,m):.12f},{c**(2*m):.12f}"
        )


def print_perfect(N: int):
    print("# perfect record control")
    print("localized_record_global_MI_bits=1")
    print("perfect_broadcast_global_MI_bits=1")
    print("localized_record_redundancy=1")
    print(f"perfect_broadcast_redundancy={N}")
    print("factorization_obstruction=global_MI_does_not_determine_redundancy")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["all", "perfect", "threshold", "access"], default="all")
    p.add_argument("--N", type=int, default=100)
    p.add_argument("--delta", type=float, default=0.1)
    p.add_argument(
        "--overlaps",
        type=float,
        nargs="*",
        default=[0.0, 0.5, 0.8, 0.9, 0.95, 0.99],
    )
    args = p.parse_args()

    if args.mode in ("all", "perfect"):
        print_perfect(args.N)
    if args.mode in ("all", "threshold"):
        print_thresholds(args.N, args.delta, args.overlaps)
    if args.mode in ("all", "access"):
        print_access(args.delta, [c for c in args.overlaps if c < 1.0])


if __name__ == "__main__":
    main()
