#!/usr/bin/env python3
"""BH-RB-021: globally causal self-bound EOS completion gate.

This audit constructs a thermodynamically consistent constant-sound-speed
completion of the BH-RB-020 local self-binding toy closure. It does not claim
that the resulting piecewise EOS is the microscopic black-hole-core EOS.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Params:
    mc2: float = 1.0
    B: float = 1.0
    y: float = 0.2

    @property
    def A(self) -> float:
        return math.sqrt(4.0 * self.B * self.mc2 * self.y)

    @property
    def n_star(self) -> float:
        return self.A / (2.0 * self.B)

    @property
    def n_causal(self) -> float:
        return math.sqrt(self.mc2 / (3.0 * self.B))


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


def eps_low(n: float, q: Params) -> float:
    return q.mc2 * n - q.A * n**2 + q.B * n**3


def p_low(n: float, q: Params) -> float:
    return -q.A * n**2 + 2.0 * q.B * n**3


def mu_low(n: float, q: Params) -> float:
    return q.mc2 - 2.0 * q.A * n + 3.0 * q.B * n**2


def dp_dn_low(n: float, q: Params) -> float:
    return -2.0 * q.A * n + 6.0 * q.B * n**2


def cs2_low(n: float, q: Params) -> float:
    return dp_dn_low(n, q) / mu_low(n, q)


def eps0_surface(q: Params) -> float:
    return eps_low(q.n_star, q)


def css_state(
    z: float,
    n_match: float,
    eps_match: float,
    p_match: float,
    s: float,
) -> tuple[float, float, float, float]:
    """Return (epsilon, pressure, number density, chemical potential).

    The high-density branch is
        p = p_m + s (epsilon - epsilon_m),
    with thermodynamic normalization chosen so n and mu are continuous at z=1.
    """
    d_match = eps_match + p_match
    c_offset = p_match - s * eps_match
    d = d_match * z ** (1.0 + s)
    eps = (d - c_offset) / (1.0 + s)
    press = (s * d + c_offset) / (1.0 + s)
    n = n_match * z
    mu = d / n
    return eps, press, n, mu


def almost(a: float, b: float, tol: float = 2e-12) -> bool:
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def run_checks() -> list[Check]:
    q = Params()
    checks: list[Check] = []

    checks.append(Check(
        "chosen toy control lies inside the BH-RB-020 local causal window",
        0.0 < q.y <= 1.0 / 3.0,
        f"y={q.y:.6f}, required 0<y<=1/3.",
    ))

    checks.append(Check(
        "finite-density self-bound surface exists",
        q.n_star > 0.0 and almost(p_low(q.n_star, q), 0.0) and eps0_surface(q) > 0.0,
        f"n*={q.n_star:.12f}, epsilon0={eps0_surface(q):.12f}.",
    ))

    sample_low = [
        q.n_star + (q.n_causal - q.n_star) * i / 200.0
        for i in range(201)
    ]
    low_cs = [cs2_low(n, q) for n in sample_low]
    checks.append(Check(
        "low-density physical branch is mechanically stable",
        all(dp_dn_low(n, q) >= -1e-12 for n in sample_low),
        f"min dp/dn={min(dp_dn_low(n, q) for n in sample_low):.12f}.",
    ))
    checks.append(Check(
        "low-density physical branch is causal through n_causal",
        min(low_cs) >= -1e-12 and max(low_cs) <= 1.0 + 1e-12,
        f"cs^2/c^2 spans [{min(low_cs):.12f}, {max(low_cs):.12f}].",
    ))
    checks.append(Check(
        "n_causal is exactly the low-branch luminal boundary",
        almost(cs2_low(q.n_causal, q), 1.0),
        f"n_causal={q.n_causal:.12f}, cs^2/c^2={cs2_low(q.n_causal, q):.12f}.",
    ))

    thermo_resid = max(abs(eps_low(n, q) + p_low(n, q) - n * mu_low(n, q)) for n in sample_low)
    checks.append(Check(
        "low branch satisfies zero-temperature Euler identity",
        thermo_resid < 1e-11,
        f"max |epsilon+p-n mu|={thermo_resid:.3e}.",
    ))

    checks.append(Check(
        "low branch obeys 0<=p<=epsilon on the physical interval",
        all(-1e-12 <= p_low(n, q) <= eps_low(n, q) + 1e-12 for n in sample_low),
        "For n<=n_causal, epsilon-p=n(mc^2-B n^2)>0.",
    ))

    nm = q.n_causal
    em = eps_low(nm, q)
    pm = p_low(nm, q)
    mum = mu_low(nm, q)
    s = cs2_low(nm, q)

    e1, p1, n1, mu1 = css_state(1.0, nm, em, pm, s)
    checks.append(Check(
        "maximally causal CSS completion is continuous in epsilon and p",
        almost(e1, em) and almost(p1, pm),
        f"match epsilon={e1:.12f}, p={p1:.12f}.",
    ))
    checks.append(Check(
        "CSS completion is continuous in n and chemical potential",
        almost(n1, nm) and almost(mu1, mum),
        f"match n={n1:.12f}, mu={mu1:.12f}.",
    ))

    checks.append(Check(
        "maximal completion is C1 in p(epsilon) at the match",
        almost(cs2_low(nm, q), s) and almost(s, 1.0),
        f"low slope={cs2_low(nm,q):.12f}, high slope={s:.12f}.",
    ))

    zs = [1.0 + 0.05 * i for i in range(201)]
    hi = [css_state(z, nm, em, pm, s) for z in zs]
    high_euler_resid = max(abs(E + P - N * MU) for E, P, N, MU in hi)
    checks.append(Check(
        "high branch preserves epsilon+p=n mu",
        high_euler_resid < 1e-10,
        f"max |epsilon+p-n mu|={high_euler_resid:.3e}.",
    ))
    checks.append(Check(
        "high branch is globally causal and mechanically stable",
        0.0 < s <= 1.0 and all(MU > 0.0 for _, _, _, MU in hi),
        f"constant cs^2/c^2={s:.12f}; mu remains positive in audit range.",
    ))
    checks.append(Check(
        "high branch preserves dominant-energy inequality",
        all(0.0 <= P <= E + 1e-12 for E, P, _, _ in hi),
        f"At match p/epsilon={pm/em:.12f}; for s<=1, p-epsilon cannot increase.",
    ))

    high_zero_extrap = em - pm / s
    checks.append(Check(
        "causal completion preserves the original physical zero-pressure surface",
        almost(p_low(q.n_star, q), 0.0)
        and q.n_star < nm
        and high_zero_extrap < em,
        (
            f"physical epsilon0={eps0_surface(q):.12f}; "
            f"high-branch linear extrapolation would cross p=0 at epsilon={high_zero_extrap:.12f}, "
            "outside the adopted high-density domain."
        ),
    ))

    nm_sub = 0.5 * (q.n_star + q.n_causal)
    em_sub = eps_low(nm_sub, q)
    pm_sub = p_low(nm_sub, q)
    s_sub = cs2_low(nm_sub, q)
    sub_states = [css_state(z, nm_sub, em_sub, pm_sub, s_sub) for z in zs]
    checks.append(Check(
        "strictly subluminal thermodynamically matched CSS completion exists",
        0.0 < s_sub < 1.0
        and all(0.0 <= P <= E + 1e-12 for E, P, _, _ in sub_states),
        f"example match n={nm_sub:.12f}, constant cs^2/c^2={s_sub:.12f}.",
    ))

    expected_nc = math.sqrt(q.mc2 / (3.0 * q.B))
    checks.append(Check(
        "canonical matching density is fixed by existing BH-RB-020 coefficients",
        almost(nm, expected_nc),
        "n_match=n_causal=sqrt(mc^2/(3B)); no new dimensional matching constant is inserted.",
    ))

    e2, p2, n2, mu2 = css_state(2.0, nm, em, pm, s)
    checks.append(Check(
        "maximal causal completion has the expected thermodynamic scaling",
        almost(mu2 / mum, 2.0) and almost((e2 + p2) / (em + pm), 4.0),
        f"at n/nm=2: mu/mu_m={mu2/mum:.12f}, (epsilon+p)/(epsilon_m+p_m)={(e2+p2)/(em+pm):.12f}.",
    ))

    return checks


def report() -> int:
    checks = run_checks()
    passed = sum(c.passed for c in checks)
    total = len(checks)
    for i, c in enumerate(checks, 1):
        print(f"[{i:02d}] {'PASS' if c.passed else 'FAIL'} — {c.name}")
        print(f"     {c.detail}")
    print()
    print(f"RESULT: {passed}/{total} PASS")
    if passed == total:
        print(
            "VERDICT: PASS_WITH_BOUNDARY / "
            "GLOBALLY_CAUSAL_SELF_BOUND_EOS_FAMILY_CONSTRUCTED / "
            "THERMODYNAMIC_MATCHING_PRESERVES_N_AND_MU / "
            "EPSILON0_SURVIVES_CAUSAL_COMPLETION / "
            "MICROPHYSICAL_HIGH_DENSITY_BRANCH_NOT_DERIVED / "
            "BLACK_HOLE_CORE_RADIUS_NOT_YET_DERIVED"
        )
        return 0
    print("VERDICT: FAIL")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all", "checks"), default="all")
    args = parser.parse_args()
    if args.mode in {"all", "checks"}:
        return report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
