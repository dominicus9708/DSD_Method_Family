#!/usr/bin/env python3
"""
Track-2 B5 finite witness: composition of reductions/readouts vs order dependence.

Purpose
-------
Test four distinct questions that must not be conflated:

1. Are two maps even typed-composable in a requested order?
2. If both are endomaps, do they commute?
3. Do compatible standard-QM reductions commute in a supplied specialization?
4. Do domain restriction and passive Lorentz re-expression commute when the
   semantic domain is transported covariantly?

The script also provides exact counterexamples showing that individually valid,
idempotent reductions/channels need not commute.

No quantum-gravity premise is used. Python standard library only.
"""

from __future__ import annotations

import argparse
import math

TOL = 1e-12


# ---------------------------------------------------------------------
# Generic finite maps
# ---------------------------------------------------------------------

def generic_witness():
    domain = (0, 1, 2)

    # Both maps are idempotent endomaps on the same carrier.
    r1 = {0: 0, 1: 0, 2: 2}
    r2 = {0: 0, 1: 1, 2: 1}

    def compose(f, g):
        return {x: f[g[x]] for x in domain}

    r2_r1 = compose(r2, r1)
    r1_r2 = compose(r1, r2)

    idempotent_r1 = all(r1[r1[x]] == r1[x] for x in domain)
    idempotent_r2 = all(r2[r2[x]] == r2[x] for x in domain)

    return {
        "r1_idempotent": idempotent_r1,
        "r2_idempotent": idempotent_r2,
        "r2_after_r1": r2_r1,
        "r1_after_r2": r1_r2,
        "commute": r2_r1 == r1_r2,
    }


# ---------------------------------------------------------------------
# Small matrix helpers
# ---------------------------------------------------------------------

def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matadd(a, b):
    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def matscale(c, a):
    return [[c * a[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def outer(v):
    return [[v[i] * v[j].conjugate() for j in range(len(v))] for i in range(len(v))]


def maxdiff(a, b):
    return max(
        abs(a[i][j] - b[i][j])
        for i in range(len(a))
        for j in range(len(a[0]))
    )


# ---------------------------------------------------------------------
# Standard-QM witnesses
# ---------------------------------------------------------------------

def idx3(a, b, c):
    return 4 * a + 2 * b + c


def trace_b_from_abc(rho):
    # ABC -> AC
    out = [[0j] * 4 for _ in range(4)]
    for a in range(2):
        for c in range(2):
            for ap in range(2):
                for cp in range(2):
                    out[2 * a + c][2 * ap + cp] = sum(
                        rho[idx3(a, b, c)][idx3(ap, b, cp)]
                        for b in range(2)
                    )
    return out


def trace_c_from_abc(rho):
    # ABC -> AB
    out = [[0j] * 4 for _ in range(4)]
    for a in range(2):
        for b in range(2):
            for ap in range(2):
                for bp in range(2):
                    out[2 * a + b][2 * ap + bp] = sum(
                        rho[idx3(a, b, c)][idx3(ap, bp, c)]
                        for c in range(2)
                    )
    return out


def trace_second_qubit(rho):
    # Two-qubit carrier XY -> X.
    return [
        [
            sum(rho[2 * a + b][2 * ap + b] for b in range(2))
            for ap in range(2)
        ]
        for a in range(2)
    ]


def dephase_axis(rho, nx, ny, nz):
    ident = [[1 + 0j, 0j], [0j, 1 + 0j]]
    pauli_x = [[0j, 1 + 0j], [1 + 0j, 0j]]
    pauli_y = [[0j, -1j], [1j, 0j]]
    pauli_z = [[1 + 0j, 0j], [0j, -1 + 0j]]

    axis = matadd(
        matadd(matscale(nx, pauli_x), matscale(ny, pauli_y)),
        matscale(nz, pauli_z),
    )
    p_plus = matscale(0.5, matadd(ident, axis))
    p_minus = matscale(0.5, matadd(ident, matscale(-1.0, axis)))

    return matadd(
        matmul(matmul(p_plus, rho), p_plus),
        matmul(matmul(p_minus, rho), p_minus),
    )


def qm_witness():
    # Arbitrary normalized pure three-qubit state for the partial-trace order test.
    amplitudes = [complex(k, ((-1) ** k) * 0.3 * k) for k in range(1, 9)]
    norm = math.sqrt(sum(abs(z) ** 2 for z in amplitudes))
    psi = [z / norm for z in amplitudes]
    rho_abc = outer(psi)

    # Trace B then C, versus C then B. Both should reduce ABC -> A.
    a_after_b_then_c = trace_second_qubit(trace_b_from_abc(rho_abc))
    a_after_c_then_b = trace_second_qubit(trace_c_from_abc(rho_abc))
    disjoint_partial_traces_commute = maxdiff(
        a_after_b_then_c, a_after_c_then_b
    ) < TOL

    # Order-sensitive idempotent pinching/dephasing channels.
    rho0 = outer([1 + 0j, 0j])
    s = 1 / math.sqrt(2)

    delta_z = lambda r: dephase_axis(r, 0.0, 0.0, 1.0)
    delta_m = lambda r: dephase_axis(r, s, 0.0, s)

    z_once = delta_z(rho0)
    m_once = delta_m(rho0)

    z_idempotent = maxdiff(delta_z(z_once), z_once) < TOL
    m_idempotent = maxdiff(delta_m(m_once), m_once) < 1e-10

    m_after_z = delta_m(delta_z(rho0))
    z_after_m = delta_z(delta_m(rho0))
    dephasings_commute_on_witness = maxdiff(m_after_z, z_after_m) < TOL

    return {
        "disjoint_partial_traces_commute": disjoint_partial_traces_commute,
        "A_after_trace_B_then_C": a_after_b_then_c,
        "A_after_trace_C_then_B": a_after_c_then_b,
        "Delta_Z_idempotent": z_idempotent,
        "Delta_m_idempotent": m_idempotent,
        "Delta_m_after_Delta_Z": m_after_z,
        "Delta_Z_after_Delta_m": z_after_m,
        "nonorthogonal_dephasings_commute_on_witness": dephasings_commute_on_witness,
    }


# ---------------------------------------------------------------------
# Relativity / typed domain restriction witnesses
# ---------------------------------------------------------------------

def typed_restrict(record, target_domain):
    missing = set(target_domain) - set(record)
    if missing:
        raise ValueError(
            "restriction is ill-typed: target domain contains points absent "
            "from the current record"
        )
    return {point: record[point] for point in target_domain}


def boost_event(event, beta):
    t, x = event
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    return (
        round(gamma * (t - beta * x), 12),
        round(gamma * (x - beta * t), 12),
    )


def boost_record(record, beta):
    return {boost_event(point, beta): value for point, value in record.items()}


def in_causal_past(event, observer_event):
    t, x = event
    to, xo = observer_event
    dt = to - t
    dx = xo - x
    return dt >= -TOL and dt * dt - dx * dx >= -TOL


def relativity_witness():
    events = (
        (0.0, 0.0),
        (1.0, 0.5),
        (1.0, 2.0),
        (3.0, 0.0),
    )
    record = {event: i for i, event in enumerate(events)}

    # Nested restrictions: D2 subset D1 subset X.
    d1 = set(events[:3])
    d2 = set(events[:2])

    nested = typed_restrict(typed_restrict(record, d1), d2)
    direct = typed_restrict(record, d2)
    nested_absorption_holds = nested == direct

    reverse_is_typed = True
    try:
        typed_restrict(typed_restrict(record, d2), d1)
    except ValueError:
        reverse_is_typed = False

    # Covariant access/representation control using a causal domain.
    observer = (2.0, 0.0)
    causal_domain = {e for e in record if in_causal_past(e, observer)}
    beta = 0.6

    restrict_then_boost = boost_record(
        typed_restrict(record, causal_domain), beta
    )

    boosted_record = boost_record(record, beta)
    boosted_observer = boost_event(observer, beta)
    boosted_causal_domain = {
        e for e in boosted_record if in_causal_past(e, boosted_observer)
    }
    boost_then_restrict = typed_restrict(
        boosted_record, boosted_causal_domain
    )

    covariant_square_commutes = restrict_then_boost == boost_then_restrict

    return {
        "nested_restriction_absorption_holds": nested_absorption_holds,
        "reverse_nested_order_is_typed_without_extension": reverse_is_typed,
        "causal_domain_original": sorted(causal_domain),
        "causal_domain_boosted": sorted(boosted_causal_domain),
        "restrict_then_boost": restrict_then_boost,
        "boost_then_restrict_transported_domain": boost_then_restrict,
        "covariant_restriction_representation_square_commutes": covariant_square_commutes,
    }


def print_block(title, data):
    print(f"\n[{title}]")
    for key, value in data.items():
        print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "generic", "qm", "rel"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("all", "generic"):
        g = generic_witness()
        assert g["r1_idempotent"] is True
        assert g["r2_idempotent"] is True
        assert g["commute"] is False
        print_block("GENERIC IDEMPOTENT REDUCTIONS", g)

    if args.mode in ("all", "qm"):
        q = qm_witness()
        assert q["disjoint_partial_traces_commute"] is True
        assert q["Delta_Z_idempotent"] is True
        assert q["Delta_m_idempotent"] is True
        assert q["nonorthogonal_dephasings_commute_on_witness"] is False
        print_block("STANDARD-QM COMPOSITION / ORDER", q)

    if args.mode in ("all", "rel"):
        r = relativity_witness()
        assert r["nested_restriction_absorption_holds"] is True
        assert r["reverse_nested_order_is_typed_without_extension"] is False
        assert r["covariant_restriction_representation_square_commutes"] is True
        print_block("RELATIVITY / DOMAIN TYPING", r)

    print("\nVERDICT: PASS_WITH_BOUNDARY")
    print(
        "COMMON: composability is typed first; commutation is an additional property, "
        "not a consequence of both maps being valid reductions."
    )


if __name__ == "__main__":
    main()
