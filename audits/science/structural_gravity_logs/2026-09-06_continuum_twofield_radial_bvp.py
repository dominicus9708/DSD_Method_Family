#!/usr/bin/env python3
"""Continuum two-field radial BVP audit for reciprocal/common-action DSD gravity.

Historical repository path retains `structural_gravity_logs` for continuity.
This solver treats ell_A > 0 directly in the continuum.

Static equations:
    -s^-2 d/ds[s^2 p(a) U_s] = (3 epsilon/2) U
    -ell^2(a_ss+2 a_s/s-6 a/s^2)+a = 2 beta chi p(a) U_s^2
    p(a)=exp(-2 beta a/3)

Regular variables:
    a=s^2 g, U_s=s r, g_s=s k.

For prescribed a_b, endpoint conditions are
    U(1)+p(a_b)U_s(1)=1, g(1)=a_b, k(1)=-2a_b.
"""

from __future__ import annotations
import argparse, math
from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, least_squares, minimize_scalar

@dataclass
class Solution:
    U0: float
    g0: float
    epsilon: float
    residual: float

def _integrate(beta, chi, ell, x, s0):
    U0, g0, epsilon = map(float, x)
    r0 = -0.5 * epsilon * U0
    k0 = (g0 - 2.0 * beta * chi * r0 * r0) / (7.0 * ell * ell)
    y0 = np.array([U0, r0, g0, k0], dtype=float)
    def rhs(s, y):
        U, r, g, k = y
        a = s*s*g
        p = math.exp(max(-50.0, min(50.0, -2.0*beta*a/3.0)))
        ap = 2.0*s*g + s**3*k
        rp = (-3.0*r - 1.5*epsilon*U/p)/s + (2.0*beta/3.0)*ap*r
        kp = (-7.0*k + (g - 2.0*beta*chi*p*r*r)/(ell*ell))/s
        return np.array([s*r, rp, s*k, kp])
    return solve_ivp(rhs, (s0, 1.0), y0, rtol=5e-8, atol=5e-10, max_step=0.005)

def solve_point(beta, chi, ell, a_boundary, guess=None, s0=1e-5):
    if ell <= 0.0:
        raise ValueError("ell must be positive; use the ell=0 continuum solver for the local branch")
    if guess is None:
        guess = np.array([1.4, 0.2, 0.4], dtype=float)
    def residual(x):
        try:
            sol = _integrate(beta, chi, ell, x, s0)
            if (not sol.success) or sol.t[-1] < 0.999999:
                return np.full(3, 1e3)
            U, r, g, k = sol.y[:, -1]
            p = math.exp(max(-50.0, min(50.0, -2.0*beta*g/3.0)))
            return np.array([U + p*r - 1.0, g - a_boundary, k + 2.0*a_boundary])
        except Exception:
            return np.full(3, 1e3)
    fit = least_squares(residual, np.asarray(guess, dtype=float),
                        bounds=([0.1,-10.0,1e-6],[20.0,20.0,3.0]),
                        xtol=1e-11, ftol=1e-11, gtol=1e-11, max_nfev=400)
    err = float(np.max(np.abs(residual(fit.x))))
    U0, g0, epsilon = map(float, fit.x)
    return Solution(U0,g0,epsilon,err), fit.x

def fold_point(beta, chi, ell, a_lo, a_hi):
    cache = {}
    def eps_of(a):
        guess = cache[min(cache, key=lambda q: abs(q-a))] if cache else None
        sol, x = solve_point(beta, chi, ell, float(a), guess=guess)
        if sol.residual > 1e-6:
            raise RuntimeError(f"BVP residual too large: {sol.residual}")
        cache[float(a)] = x
        return sol.epsilon
    for a in np.linspace(a_lo, a_hi, 7):
        eps_of(float(a))
    opt = minimize_scalar(lambda a: -eps_of(float(a)), bounds=(a_lo,a_hi),
                          method="bounded", options={"xatol":2e-7})
    return float(opt.x), float(-opt.fun), float(eps_of(1.0))

def boundary_derivative(beta, chi, ell, h=0.008):
    lo, xlo = solve_point(beta, chi, ell, 1.0-h)
    hi, _ = solve_point(beta, chi, ell, 1.0+h, guess=xlo)
    return (hi.epsilon-lo.epsilon)/(2.0*h)

def beta_boundary(chi, ell, beta_lo, beta_hi, h):
    f = lambda b: boundary_derivative(float(b), chi, ell, h=h)
    return float(brentq(f, beta_lo, beta_hi, xtol=2e-5))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=("point","fold","beta-boundary"), default="point")
    p.add_argument("--beta", type=float, default=2.0)
    p.add_argument("--chi", type=float, default=0.5)
    p.add_argument("--ell", type=float, default=0.1)
    p.add_argument("--a-boundary", type=float, default=0.5)
    p.add_argument("--a-lo", type=float, default=0.52)
    p.add_argument("--a-hi", type=float, default=0.72)
    p.add_argument("--beta-lo", type=float, default=1.0)
    p.add_argument("--beta-hi", type=float, default=1.12)
    p.add_argument("--h", type=float, default=0.008)
    p.add_argument("--s0", type=float, default=1e-5)
    args = p.parse_args()
    if args.mode == "point":
        sol, _ = solve_point(args.beta,args.chi,args.ell,args.a_boundary,s0=args.s0)
        print(f"epsilon={sol.epsilon:.12f}")
        print(f"U0={sol.U0:.12f}")
        print(f"g0={sol.g0:.12f}")
        print(f"residual={sol.residual:.6e}")
    elif args.mode == "fold":
        af, ef, ec = fold_point(args.beta,args.chi,args.ell,args.a_lo,args.a_hi)
        print(f"a_fold={af:.12f}")
        print(f"epsilon_fold={ef:.12f}")
        print(f"epsilon_a1_contact={ec:.12f}")
    else:
        bs = beta_boundary(args.chi,args.ell,args.beta_lo,args.beta_hi,args.h)
        print(f"beta_fold_saturation_boundary={bs:.12f}")
        print(f"control_derivative={boundary_derivative(bs,args.chi,args.ell,args.h):.6e}")

if __name__ == "__main__":
    main()
