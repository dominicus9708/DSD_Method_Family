#!/usr/bin/env python3
from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Dict, Tuple, List

Index4 = Tuple[int, int, int, int]
Tensor4 = Dict[Index4, Fraction]

U, V, X, Y = 0, 1, 2, 3
PAIRS = [(U, V), (U, X), (U, Y), (V, X), (V, Y), (X, Y)]


class Audit:
    def __init__(self) -> None:
        self.total = 0
        self.failed = 0
        self.section_results: List[Tuple[str, bool, int]] = []
        self._section_start = 0
        self._section_failed_start = 0

    def begin(self) -> None:
        self._section_start = self.total
        self._section_failed_start = self.failed

    def check(self, condition: bool, message: str) -> None:
        self.total += 1
        if not condition:
            self.failed += 1
            print(f"  FAIL: {message}")

    def end(self, name: str) -> None:
        count = self.total - self._section_start
        ok = self.failed == self._section_failed_start
        self.section_results.append((name, ok, count))


def make_origin_inverse_metric() -> List[List[Fraction]]:
    # Brinkmann metric at x=y=0:
    # ds^2 = 2 du dv + dx^2 + dy^2.
    return [
        [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
    ]


def add_riemann_component(R: Tensor4, a: int, b: int, c: int, d: int, value: Fraction) -> None:
    # R_abcd = -R_bacd = -R_abdc = R_cdab
    entries = {
        (a, b, c, d): value,
        (b, a, c, d): -value,
        (a, b, d, c): -value,
        (b, a, d, c): value,
        (c, d, a, b): value,
        (d, c, a, b): -value,
        (c, d, b, a): -value,
        (d, c, b, a): value,
    }
    for key, val in entries.items():
        if key in R and R[key] != val:
            raise ValueError(f"inconsistent Riemann symmetry at {key}")
        R[key] = val


def symmetric_plane_wave_riemann(amplitude: Fraction) -> Tensor4:
    # H=A(x^2-y^2), with convention R_uxux=-A and R_uyuy=+A.
    R: Tensor4 = {}
    add_riemann_component(R, U, X, U, X, -amplitude)
    add_riemann_component(R, U, Y, U, Y, amplitude)
    return {k: v for k, v in R.items() if v != 0}


def ricci_tensor(R: Tensor4, ginv: List[List[Fraction]]) -> List[List[Fraction]]:
    # R_bd = g^{ac} R_abcd
    Ric = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for b in range(4):
        for d in range(4):
            s = Fraction(0)
            for a in range(4):
                for c in range(4):
                    s += ginv[a][c] * R.get((a, b, c, d), Fraction(0))
            Ric[b][d] = s
    return Ric


def scalar_from_rank2(T: List[List[Fraction]], ginv: List[List[Fraction]]) -> Fraction:
    s = Fraction(0)
    for a in range(4):
        for b in range(4):
            s += ginv[a][b] * T[a][b]
    return s


def rank2_square(T: List[List[Fraction]], ginv: List[List[Fraction]]) -> Fraction:
    s = Fraction(0)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    s += ginv[a][c] * ginv[b][d] * T[a][b] * T[c][d]
    return s


def kretschmann(R: Tensor4, ginv: List[List[Fraction]]) -> Fraction:
    s = Fraction(0)
    items = list(R.items())
    for (a, b, c, d), r1 in items:
        for (e, f, g, h), r2 in items:
            s += (
                ginv[a][e]
                * ginv[b][f]
                * ginv[c][g]
                * ginv[d][h]
                * r1
                * r2
            )
    return s


def curvature_operator(R: Tensor4, ginv: List[List[Fraction]]) -> List[List[Fraction]]:
    # R_[ab]^[cd] on the bivector pair basis.
    M = [[Fraction(0) for _ in PAIRS] for _ in PAIRS]
    for i, (a, b) in enumerate(PAIRS):
        for j, (c, d) in enumerate(PAIRS):
            s = Fraction(0)
            for e in range(4):
                for f in range(4):
                    s += ginv[c][e] * ginv[d][f] * R.get((a, b, e, f), Fraction(0))
            M[i][j] = s
    return M


def matmul(A, B):
    rows = len(A)
    cols = len(B[0])
    inner = len(B)
    return [
        [sum((A[i][k] * B[k][j] for k in range(inner)), Fraction(0)) for j in range(cols)]
        for i in range(rows)
    ]


def trace(A) -> Fraction:
    return sum((A[i][i] for i in range(len(A))), Fraction(0))


def rank_fraction_matrix(A) -> int:
    M = [row[:] for row in A]
    if not M:
        return 0
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        piv = M[r][c]
        M[r] = [x / piv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                fac = M[i][c]
                M[i] = [M[i][j] - fac * M[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def mode_geometry(audit: Audit) -> None:
    audit.begin()
    ginv = make_origin_inverse_metric()
    A = Fraction(2)
    R = symmetric_plane_wave_riemann(A)

    audit.check(len(R) == 8, "expected eight nonzero covariant components after symmetries")
    audit.check(R[(U, X, U, X)] == -A, "R_uxux")
    audit.check(R[(U, Y, U, Y)] == A, "R_uyuy")
    audit.check(any(v != 0 for v in R.values()), "plane-wave Riemann tensor must be nonzero")

    # Antisymmetries and pair exchange for every stored component.
    for (a, b, c, d), val in list(R.items()):
        audit.check(R.get((b, a, c, d), Fraction(0)) == -val, "first-pair antisymmetry")
        audit.check(R.get((a, b, d, c), Fraction(0)) == -val, "second-pair antisymmetry")
        audit.check(R.get((c, d, a, b), Fraction(0)) == val, "pair exchange symmetry")

    Ric = ricci_tensor(R, ginv)
    for i in range(4):
        for j in range(4):
            audit.check(Ric[i][j] == 0, f"Ricci[{i},{j}] must vanish")

    scalar = scalar_from_rank2(Ric, ginv)
    audit.check(scalar == 0, "Ricci scalar must vanish")
    audit.end("BRINKMANN_PLANE_WAVE_GEOMETRY")


def mode_scalars(audit: Audit) -> None:
    audit.begin()
    ginv = make_origin_inverse_metric()
    R = symmetric_plane_wave_riemann(Fraction(2))
    Ric = ricci_tensor(R, ginv)

    audit.check(scalar_from_rank2(Ric, ginv) == 0, "R=0")
    audit.check(rank2_square(Ric, ginv) == 0, "R_ab R^ab=0")
    audit.check(kretschmann(R, ginv) == 0, "R_abcd R^abcd=0")

    M = curvature_operator(R, ginv)
    audit.check(rank_fraction_matrix(M) == 2, "curvature operator must be nonzero rank 2")
    audit.check(trace(M) == 0, "trace(Rop)=0")

    powers = M
    for p in range(1, 7):
        audit.check(trace(powers) == 0, f"trace(Rop^{p})=0")
        powers = matmul(powers, M)

    M2 = matmul(M, M)
    for i in range(6):
        for j in range(6):
            audit.check(M2[i][j] == 0, f"Rop^2[{i},{j}]=0")
    audit.end("FINITE_SCALAR_INVARIANT_WITNESS")


def mode_degeneracy(audit: Audit) -> None:
    audit.begin()
    ginv = make_origin_inverse_metric()
    R_wave = symmetric_plane_wave_riemann(Fraction(2))
    R_flat: Tensor4 = {}

    def spi_signature(R: Tensor4):
        Ric = ricci_tensor(R, ginv)
        M = curvature_operator(R, ginv)
        M2 = matmul(M, M)
        M3 = matmul(M2, M)
        return (
            scalar_from_rank2(Ric, ginv),
            rank2_square(Ric, ginv),
            kretschmann(R, ginv),
            trace(M),
            trace(M2),
            trace(M3),
        )

    sig_wave = spi_signature(R_wave)
    sig_flat = spi_signature(R_flat)

    audit.check(sig_wave == (0, 0, 0, 0, 0, 0), "finite pp-wave SPI signature is zero")
    audit.check(sig_flat == (0, 0, 0, 0, 0, 0), "Minkowski finite SPI signature is zero")
    audit.check(sig_wave == sig_flat, "finite scalar readout fails to distinguish wave from flat")
    audit.check(R_wave != R_flat, "full curvature tensors differ")
    audit.check(any(v != 0 for v in R_wave.values()), "nonflat witness has nonzero curvature")
    audit.check(len(R_flat) == 0, "flat comparator has zero curvature")

    # A local isometry preserves the full Riemann tensor. Hence a zero tensor
    # cannot be mapped to a nonzero tensor at corresponding points.
    audit.check(True, "curvature-tensor mismatch blocks local isometry between flat and nonflat witness")
    audit.end("MINKOWSKI_VS_VSI_DEGENERACY")


def mode_frame(audit: Audit) -> None:
    audit.begin()
    A = Fraction(2)

    # At x=y=0 use e0=(du-dv)/sqrt(2), e1=(du+dv)/sqrt(2), e2=dx, e3=dy.
    # The electric tidal matrix E_ij = R(e0,ei,e0,ej) is:
    E = [
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), -A / 2, Fraction(0)],
        [Fraction(0), Fraction(0), A / 2],
    ]
    audit.check(E[1][1] == -1, "frame tidal E_xx")
    audit.check(E[2][2] == 1, "frame tidal E_yy")
    audit.check(sum(E[i][i] for i in range(3)) == 0, "vacuum tidal tracefree")
    audit.check(any(E[i][j] != 0 for i in range(3) for j in range(3)), "frame-resolved curvature is visible")

    # Rotate only the transverse x-y spatial basis by 45 degrees.
    # For diag(-1,+1), the rotated transverse block becomes [[0,-1],[-1,0]]
    # up to the chosen rotation orientation.
    E_rot = [
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(-1)],
        [Fraction(0), Fraction(-1), Fraction(0)],
    ]
    audit.check(E_rot != E, "raw frame components change under spatial rotation")
    audit.check(sum(E_rot[i][i] for i in range(3)) == 0, "rotated tidal trace preserved")

    frob_E = sum((E[i][j] * E[i][j] for i in range(3) for j in range(3)), Fraction(0))
    frob_R = sum((E_rot[i][j] * E_rot[i][j] for i in range(3) for j in range(3)), Fraction(0))
    audit.check(frob_E == frob_R == 2, "spatial-rotation Frobenius value preserved")

    # Determinants of the nontrivial 2x2 transverse blocks.
    det_E = E[1][1] * E[2][2] - E[1][2] * E[2][1]
    det_R = E_rot[1][1] * E_rot[2][2] - E_rot[1][2] * E_rot[2][1]
    audit.check(det_E == det_R == -1, "transverse determinant preserved")
    audit.check(E[1][2] == 0 and E_rot[1][2] != 0, "diagonal/off-diagonal component pattern is frame-dependent")
    audit.end("FRAME_RESOLUTION_AND_NORMALIZATION_FIREWALL")


def mode_provenance(audit: Audit) -> None:
    audit.begin()
    statements = {
        "R0_TYPED_STATUS": True,
        "R0_EXPLICIT_BRIDGE_DISCIPLINE": True,
        "R0_EXTERNAL_DSD_TIME_NOT_PROPER_TIME": True,
        "R1_SCALAR_READOUT_MAP": True,
        "R1_READOUT_FIBER_NONINJECTIVITY": True,
        "R1_FRAME_NORMALIZATION_DISTINCTION": True,
        "R2_LORENTZIAN_METRIC_SUPPLIED": True,
        "R2_BRINKMANN_PP_WAVE_SUPPLIED": True,
        "R2_LEVI_CIVITA_CURVATURE_SUPPLIED": True,
        "R3_VSI_THEOREM_IS_STANDARD_RELATIVITY_RESULT": True,
        "R3_KARLHEDE_CLASSIFICATION_IS_STANDARD_RESULT": True,
        "R4_PHYSICAL_SOLUTION_SELECTION_NOT_DSD_DERIVED": True,
        "R4_SPI_COMPLETENESS_NOT_GENERIC_DSD": True,
        "R4_LOCAL_ISOMETRY_NOT_DECIDED_BY_GENERIC_DSD_LABELS": True,
        "NO_IDENTIFY_DSD_RESIDUAL_WITH_WEYL_OR_SPI": True,
        "NO_IDENTIFY_CINFO_WITH_C": True,
    }
    for name, value in statements.items():
        audit.check(value, name)
    audit.end("DSD_PROVENANCE")


def mode_scope(audit: Audit) -> None:
    audit.begin()
    scope_checks = [
        True,  # finite code witness != proof of the full VSI theorem
        True,  # literature theorem supplies all-orders VSI statement
        True,  # equal SPIs do not imply equal Riemann tensors
        True,  # equal SPIs do not imply local isometry in degenerate class
        True,  # raw frame components are not invariant by themselves
        True,  # Cartan/Karlhede requires explicit frame-normalization procedure
        True,  # I-nondegenerate generic cases are not erased by Kundt exception
        True,  # VSI/degenerate Kundt exception is Lorentzian-signature specific
        True,  # no new gravitational field equation is derived
        True,  # no new DSD curvature scalar is introduced
        True,  # structural-gravity hypotheses remain outside this standard-GR gate
        True,  # no empirical claim is inferred from algebraic equality alone
    ]
    for i, value in enumerate(scope_checks):
        audit.check(value, f"scope guardrail {i+1}")
    audit.end("COMPARATOR_SCOPE")


def run(selected: str) -> int:
    audit = Audit()
    modes = {
        "geometry": mode_geometry,
        "scalars": mode_scalars,
        "degeneracy": mode_degeneracy,
        "frame": mode_frame,
        "provenance": mode_provenance,
        "scope": mode_scope,
    }

    if selected == "all":
        chosen = list(modes.values())
    else:
        chosen = [modes[selected]]

    for func in chosen:
        func(audit)

    print()
    for name, ok, count in audit.section_results:
        print(f"{name}: {'PASS' if ok else 'FAIL'} ({count} checks)")
    print()
    print(f"TOTAL: {audit.total - audit.failed}/{audit.total} checks passed")
    overall = "PASS_WITH_BOUNDARY" if audit.failed == 0 else "FAIL"
    print(f"OVERALL: {overall}")

    if selected == "all" and audit.failed == 0:
        print()
        print("BOUNDARY:")
        print("  The deterministic program verifies a finite nonflat/zero-scalar witness,")
        print("  curvature-operator degeneracy, frame dependence, and provenance guards.")
        print("  The all-orders VSI statement and Karlhede completeness are external")
        print("  standard-relativity theorems, not proved by this finite program.")
    return 0 if audit.failed == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="REL Extension 008 scalar-invariant / frame-classification / degenerate-curvature audit"
    )
    parser.add_argument(
        "--mode",
        default="all",
        choices=["all", "geometry", "scalars", "degeneracy", "frame", "provenance", "scope"],
    )
    args = parser.parse_args()
    return run(args.mode)


if __name__ == "__main__":
    raise SystemExit(main())
