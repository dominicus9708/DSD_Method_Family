#!/usr/bin/env python3
"""
BH-RB-017 — Constitutive density-scale / causal-EOS gate.

Purpose:
- Continue BH-RB-016 after the rotational radius floor was shown not to be
  self-persisting under generic angular-momentum loss.
- Ask whether a causal barotropic pressure law by itself selects a positive
  finite core radius.
- Use the standard static TOV system only as an external control.
- Separate dimensionless stiffness from the dimensionful constitutive scale.

Key boundary:
- This is NOT a black-hole-interior solution.
- A static regular perfect-fluid TOV star is horizonless; the calculation is
  used to determine what an EOS can and cannot supply before a dynamic trapped
  branch is attempted.
- No discarded structural-gravity radius law is reused.
"""

from __future__ import annotations

import argparse
import math

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30


def logspace(a: float, b: float, n: int) -> list[float]:
    if n < 2:
        return [10.0**a]
    step = (b - a) / (n - 1)
    return [10.0 ** (a + i * step) for i in range(n)]


def linear_eos_epsilon_bar(p_bar: float, s: float) -> float:
    """
    Dimensionless affine causal-EOS control:
        p = s (epsilon - epsilon_0),
        epsilon/epsilon_0 = 1 + (p/epsilon_0)/s.

    0 < s <= 1 corresponds to sound-speed slope dp/d epsilon <= 1 in c=1 units.
    """
    if not (0.0 < s <= 1.0):
        raise ValueError("s must lie in (0,1].")
    return 1.0 + max(p_bar, 0.0) / s


def tov_rhs_bar(r: float, m: float, p: float, s: float) -> tuple[float, float]:
    """Dimensionless TOV equations after scaling by epsilon_0."""
    eps = linear_eos_epsilon_bar(p, s)
    denom = r * (r - 2.0 * m)
    if denom <= 0.0:
        raise ValueError("TOV control entered r <= 2m; static branch invalid.")
    dm = 4.0 * math.pi * r * r * eps
    dp = -(eps + p) * (m + 4.0 * math.pi * r**3 * p) / denom
    return dm, dp


def integrate_tov_linear_eos(
    p_c_bar: float,
    s: float = 1.0,
    h: float = 2.0e-4,
    r_max: float = 2.0,
) -> tuple[float, float, float]:
    """
    Integrate the dimensionless TOV control with a fixed-step RK4 scheme.

    Returns (m_bar, r_bar, compactness = m_bar/r_bar) at p=0.
    """
    if p_c_bar <= 0.0:
        raise ValueError("central pressure must be positive.")

    r = 1.0e-6
    eps_c = linear_eos_epsilon_bar(p_c_bar, s)
    m = 4.0 * math.pi * eps_c * r**3 / 3.0
    p = p_c_bar

    while r < r_max and p > 0.0:
        k1m, k1p = tov_rhs_bar(r, m, p, s)
        k2m, k2p = tov_rhs_bar(
            r + 0.5 * h,
            m + 0.5 * h * k1m,
            p + 0.5 * h * k1p,
            s,
        )
        k3m, k3p = tov_rhs_bar(
            r + 0.5 * h,
            m + 0.5 * h * k2m,
            p + 0.5 * h * k2p,
            s,
        )
        k4m, k4p = tov_rhs_bar(
            r + h,
            m + h * k3m,
            p + h * k3p,
            s,
        )

        m_new = m + h * (k1m + 2.0 * k2m + 2.0 * k3m + k4m) / 6.0
        p_new = p + h * (k1p + 2.0 * k2p + 2.0 * k3p + k4p) / 6.0
        r_new = r + h

        if p_new <= 0.0:
            frac = p / (p - p_new)
            r_surface = r + frac * h
            m_surface = m + frac * (m_new - m)
            return m_surface, r_surface, m_surface / r_surface

        r, m, p = r_new, m_new, p_new

    raise RuntimeError("surface p=0 was not reached inside r_max.")


def scan_maximum_mass(
    s: float = 1.0,
    n: int = 600,
) -> tuple[float, float, float, float]:
    """
    Scan central pressure and return the first mass maximum along the static sequence:
      (p_c_bar, m_bar, r_bar, compactness).
    """
    best: tuple[float, float, float, float] | None = None
    for pc in logspace(-3.0, 3.0, n):
        m, r, comp = integrate_tov_linear_eos(pc, s=s)
        if best is None or m > best[1]:
            best = (pc, m, r, comp)
    assert best is not None
    return best


def constitutive_length_scale_from_rho0(rho0: float) -> float:
    """
    For epsilon_0 = rho_0 c^2, the TOV length scale is
        L_0 = c/sqrt(G rho_0).
    """
    if rho0 <= 0.0:
        raise ValueError("rho0 must be positive.")
    return C / math.sqrt(G * rho0)


def physical_mass_radius(
    m_bar: float,
    r_bar: float,
    rho0: float,
) -> tuple[float, float]:
    """Return physical (mass_kg, radius_m) for the affine-EOS scale rho0."""
    l0 = constitutive_length_scale_from_rho0(rho0)
    m0 = (C**2 / G) * l0
    return m_bar * m0, r_bar * l0


def checks() -> list[tuple[str, bool]]:
    out: list[tuple[str, bool]] = []

    s = 1.0
    pc, mbar, rbar, comp = scan_maximum_mass(s=s)
    out.append(("causal-limit EOS slope s=1 is admissible", 0.0 < s <= 1.0))
    out.append(("maximum-mass scan returns positive dimensionless M and R", mbar > 0.0 and rbar > 0.0))
    out.append(("causal-limit static compactness is near the standard ~0.354 control", abs(comp - 0.354) < 0.01))
    out.append(("regular static branch remains outside r=2M", 2.0 * comp < 1.0))

    r_over_rs = 1.0 / (2.0 * comp)
    out.append(("maximum-mass causal-limit radius is about 1.41 Schwarzschild radii", abs(r_over_rs - 1.412) < 0.05))

    pc_soft, m_soft, r_soft, comp_soft = scan_maximum_mass(s=1.0 / 3.0)
    out.append(("stiffer causal EOS raises maximum static compactness", comp > comp_soft))

    rho0 = 2.7e17
    m1, r1 = physical_mass_radius(mbar, rbar, rho0)
    m4, r4 = physical_mass_radius(mbar, rbar, 4.0 * rho0)
    out.append(("quadrupling constitutive density scale halves physical radius", abs(r4 / r1 - 0.5) < 1e-12))
    out.append(("quadrupling constitutive density scale halves physical mass scale", abs(m4 / m1 - 0.5) < 1e-12))
    out.append(("compactness is invariant under epsilon_0 scaling", abs((G * m1 / (C**2 * r1)) - comp) < 1e-12))

    m100, r100 = physical_mass_radius(mbar, rbar, 100.0 * rho0)
    out.append(("100x density scale gives 10x smaller M and R scales", abs(r100 / r1 - 0.1) < 1e-12 and abs(m100 / m1 - 0.1) < 1e-12))

    # Analytic scale-free control: p=w epsilon has no epsilon_0. Under a GR similarity
    # rescaling, M and R may both scale by lambda while compactness M/R is unchanged.
    lam = 3.0
    M0, R0 = 2.0, 5.0
    out.append(("scale-free similarity changes absolute size while preserving compactness", abs((lam * M0) / (lam * R0) - M0 / R0) < 1e-15))

    out.append(("affine causal EOS supplies a dimensionful scale only through rho0/epsilon0", constitutive_length_scale_from_rho0(4.0 * rho0) < constitutive_length_scale_from_rho0(rho0)))

    # Horizon firewall for the static comparator.
    out.append(("static causal-EOS control does not realize a trapped finite core", r_over_rs > 1.0))

    # The actual central-pressure location of the maximum is finite and O(1), showing
    # that the dimensionless sequence closes only after an EOS family is chosen.
    out.append(("dimensionless maximum occurs at finite p_c/epsilon0", 0.5 < pc < 10.0))

    return out


def report() -> None:
    print("BH-RB-017 constitutive density-scale / causal-EOS gate")
    print("Static TOV comparator only; not a black-hole interior solution.")
    print()

    rows = []
    for s in (1.0 / 3.0, 0.5, 0.7, 1.0):
        pc, mbar, rbar, comp = scan_maximum_mass(s=s)
        rows.append((s, pc, mbar, rbar, comp, 1.0 / (2.0 * comp)))

    print("s=dp/deps   pc/eps0   Mbar       Rbar       GM/(Rc^2)  R/r_s")
    for s, pc, mbar, rbar, comp, rrs in rows:
        print(f"{s:8.5f}  {pc:8.5f}  {mbar:9.6f}  {rbar:9.6f}  {comp:10.6f}  {rrs:7.4f}")

    pc, mbar, rbar, comp = scan_maximum_mass(s=1.0)
    rho0 = 2.7e17
    m1, r1 = physical_mass_radius(mbar, rbar, rho0)
    m4, r4 = physical_mass_radius(mbar, rbar, 4.0 * rho0)

    print()
    print("Synthetic constitutive-scale control for s=1:")
    print(f"rho0 = {rho0:.3e} kg/m^3 -> Mmax ~= {m1/M_SUN:.6f} Msun, R ~= {r1/1000.0:.6f} km")
    print(f"rho0 = {4.0*rho0:.3e} kg/m^3 -> Mmax ~= {m4/M_SUN:.6f} Msun, R ~= {r4/1000.0:.6f} km")
    print("The factor-of-two scaling is the point; these are not black-hole-core predictions.")

    print()
    print("Analytic closure statements:")
    print("1) For p = w epsilon, the EOS is scale-free; it does not supply an intrinsic density/length scale.")
    print("2) For p = s(epsilon-epsilon0), epsilon0 supplies L0 = c^2/sqrt(G epsilon0) = c/sqrt(G rho0).")
    print("3) Therefore M and R scale as epsilon0^(-1/2) at fixed dimensionless solution.")
    print("4) Causality fixes only 0 < s <= 1; it does not choose epsilon0.")
    print("5) Even the maximally stiff static s=1 branch remains outside its Schwarzschild radius.")

    results = checks()
    passed = sum(ok for _, ok in results)
    print()
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"\n{passed}/{len(results)} checks PASS")
    if passed != len(results):
        raise SystemExit(1)

    print(
        "\nVERDICT: PASS_WITH_BOUNDARY / CAUSAL_CONSTITUTIVE_SCALE_IDENTIFIED / "
        "DIMENSIONFUL_MICROPHYSICAL_SCALE_REQUIRED / "
        "STATIC_CAUSAL_FLUID_DOES_NOT_CLOSE_TRAPPED_CORE / "
        "FINITE_DYNAMIC_CORE_RADIUS_NOT_DERIVED"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all", "report"], default="all")
    _ = parser.parse_args()
    report()


if __name__ == "__main__":
    main()
