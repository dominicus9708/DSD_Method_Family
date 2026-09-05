#!/usr/bin/env python3
"""Continuum ell_A=0 boundary audit for the reciprocal/common-action DSD-gravity branch.

Historical repository path retains `structural_gravity_logs` for continuity.

For ell_A=0 the axis equation is algebraic:
    a = 2 beta chi exp(-2 beta a/3) U_s^2.

Writing
    z = 2 beta a/3,
    A = 4 beta^2 chi/3,
gives the exact principal-branch elimination
    z = W(A U_s^2),
    a = 3 W(A U_s^2)/(2 beta).

With q = p U_s, p=exp(-z), the monotone local branch has
    q^2 = z exp(-z)/A,
and loses local flux monotonicity at z=1, hence a=3/(2 beta).

The radial uniform-source field equation is integrated in continuum form using
w=-q >= 0:
    U_s = -sqrt(z exp(z)/A),
    w_s + 2w/s = (3 epsilon/2) U,
with the exterior normalization U(1)-w(1)=1.

The endpoint can be parameterized by the boundary axis amplitude a_b. For a
given (beta, chi, a_b), the script solves for (U(0), epsilon). Finite
differences in a_b then diagnose whether epsilon(a_b) is still increasing when
a_b reaches the admissibility wall a_b=1.

This is a reproducibility/control calculation for a conditional specialization,
not a universal gravity law.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, root
from scipy.special import lambertw


def endpoint_solution(beta: float, chi: float, a_b: float,
                      guess=(2.0, 0.65), s0=1.0e-6):
    if beta <= 0 or chi <= 0:
        raise ValueError("beta and chi must be positive")
    if not (0.0 <= a_b <= 1.0):
        raise ValueError("a_b must lie in [0,1]")

    A = 4.0 * beta * beta * chi / 3.0
    z_b = 2.0 * beta * a_b / 3.0
    if z_b > 1.0 + 1.0e-12:
        raise ValueError(
            "a_b lies beyond the principal monotone local branch (z_b>1)"
        )

    w_b = math.sqrt(z_b * math.exp(-z_b) / A) if a_b > 0 else 0.0
    U_b = 1.0 + w_b

    def v_from_w(w: float) -> float:
        x = A * w * w
        if x > 1.0 / math.e * (1.0 + 1.0e-8):
            return float("nan")
        x = min(x, 1.0 / math.e)
        z = float((-lambertw(-x, 0)).real)
        return math.sqrt(max(0.0, z * math.exp(z) / A))

    def residual(y):
        U0, epsilon = y
        lam = 1.5 * epsilon
        U_init = U0 - lam * U0 * s0 * s0 / 6.0
        w_init = lam * U0 * s0 / 3.0

        def rhs(s, state):
            U, w = state
            v = v_from_w(float(w))
            if not np.isfinite(v):
                return [1.0e6, 1.0e6]
            return [-v, lam * U - 2.0 * w / s]

        sol = solve_ivp(
            rhs, (s0, 1.0), (U_init, w_init),
            rtol=2.0e-9, atol=1.0e-11, max_step=0.01,
        )
        if not sol.success:
            return [1.0e3, 1.0e3]
        U1, w1 = sol.y[:, -1]
        return [U1 - U_b, w1 - w_b]

    ans = root(residual, guess, method="hybr", options={"xtol": 1.0e-10})
    if not ans.success:
        raise RuntimeError(ans.message)
    return float(ans.x[0]), float(ans.x[1]), w_b, z_b


def endpoint_derivative(beta: float, chi: float, h=0.002,
                        guess=(2.0, 0.65)):
    """Second-order backward estimate of d epsilon / d a_b at a_b=1."""
    U0, e0, _, _ = endpoint_solution(beta, chi, 1.0, guess=guess)
    U1, e1, _, _ = endpoint_solution(beta, chi, 1.0-h, guess=(U0, e0))
    U2, e2, _, _ = endpoint_solution(beta, chi, 1.0-2.0*h, guess=(U1, e1))
    derivative = (3.0*e0 - 4.0*e1 + e2) / (2.0*h)
    return derivative, e0, U0


def first_global_boundary(chi: float, beta_lo: float, beta_hi: float,
                          h=0.002):
    cache = {}

    def f(beta):
        key = round(float(beta), 12)
        if key in cache:
            return cache[key][0]
        if cache:
            nearest = min(cache, key=lambda b: abs(b-beta))
            guess = (cache[nearest][2], cache[nearest][1])
        else:
            guess = (2.5, 0.8)
        out = endpoint_derivative(float(beta), chi, h=h, guess=guess)
        cache[key] = out
        print(
            f"beta={beta:.9f} d_eps_da={out[0]:.9e} "
            f"epsilon_at_a1={out[1]:.9f}"
        )
        return out[0]

    vlo = f(beta_lo)
    vhi = f(beta_hi)
    if vlo * vhi > 0:
        raise RuntimeError("beta bracket does not straddle the global boundary")

    beta_star = brentq(f, beta_lo, beta_hi, xtol=2.0e-5)
    _ = f(beta_star)
    der, epsilon, U0 = cache[round(float(beta_star), 12)]
    return beta_star, epsilon, der, U0


def local_fold(beta: float, chi: float):
    a_fold = 3.0 / (2.0 * beta)
    Us2_fold = 3.0 * math.e / (4.0 * beta * beta * chi)
    return a_fold, Us2_fold


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=("endpoint", "derivative", "boundary", "local"),
                   default="derivative")
    p.add_argument("--beta", type=float, default=1.4)
    p.add_argument("--chi", type=float, default=0.5)
    p.add_argument("--a", type=float, default=1.0)
    p.add_argument("--h", type=float, default=0.002)
    p.add_argument("--beta-lo", type=float, default=1.35)
    p.add_argument("--beta-hi", type=float, default=1.40)
    args = p.parse_args()

    if args.mode == "local":
        a_fold, us2 = local_fold(args.beta, args.chi)
        print(f"beta={args.beta:.12g}")
        print(f"chi={args.chi:.12g}")
        print(f"local_a_fold={a_fold:.12g}")
        print(f"local_Us2_fold={us2:.12g}")
        print("exact_local_fold_saturation_beta=1.5")
        return

    if args.mode == "endpoint":
        U0, epsilon, wb, zb = endpoint_solution(args.beta, args.chi, args.a)
        print(f"beta={args.beta:.12g} chi={args.chi:.12g} a_b={args.a:.12g}")
        print(f"U0={U0:.12f}")
        print(f"epsilon={epsilon:.12f}")
        print(f"w_boundary={wb:.12f}")
        print(f"z_boundary={zb:.12f}")
        return

    if args.mode == "derivative":
        der, epsilon, U0 = endpoint_derivative(
            args.beta, args.chi, h=args.h
        )
        print(f"beta={args.beta:.12g} chi={args.chi:.12g}")
        print(f"d_epsilon_da_at_a1={der:.12e}")
        print(f"epsilon_at_a1={epsilon:.12f}")
        print(f"U0_at_a1={U0:.12f}")
        return

    beta_star, epsilon, der, U0 = first_global_boundary(
        args.chi, args.beta_lo, args.beta_hi, h=args.h
    )
    print(f"chi={args.chi:.12g}")
    print(f"beta_global_star={beta_star:.12f}")
    print(f"epsilon_star={epsilon:.12f}")
    print(f"d_epsilon_da={der:.3e}")
    print(f"U0_star={U0:.12f}")


if __name__ == "__main__":
    main()
