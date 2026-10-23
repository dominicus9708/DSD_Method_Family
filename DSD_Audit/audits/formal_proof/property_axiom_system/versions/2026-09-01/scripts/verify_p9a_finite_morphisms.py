#!/usr/bin/env python3
"""Exhaustive 53-model legal finite Property-core comparison (paper dated 2026-09-01).

This is a finite-model metacheck, NOT a proof of the manuscript's general theorems.
Script usage: python verify_p9a_finite_morphisms.py [output_json]
Default output is ../results/p9a_finite_morphisms.json adjacent to scripts/.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import sys
from dataclasses import dataclass
from pathlib import Path

PAPER_SHA256 = "03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"
PROPERTY_KINDS = ("p", "q")
# Each kind has the typed unary profile (u), one prerequisite d, and value set {0,1}.
# A kind is None (undeclared), "U" (declared but source profile unavailable),
# or (ap,sat,value) with ap,sat in {0,1}, value in {-1 [undefined],0,1}.

@dataclass(frozen=True)
class Core:
    available: bool
    fields: tuple[None | str | tuple[int, int, int], ...]

    def declarations(self) -> frozenset[str]:
        return frozenset(k for k, v in zip(PROPERTY_KINDS, self.fields) if v is not None)

    def serial(self) -> dict:
        def datum(f):
            if f is None:
                return {"state": "undeclared"}
            if f == "U":
                return {"state": "declared_profile_unavailable"}
            a, d, value = f
            return {"state": "declared_profile_available", "ap_x": bool(a),
                    "sat_d_x": bool(d), "assignment_x": None if value == -1 else value}
        return {"available_aux_u": self.available,
                "property_data": {k: datum(v) for k,v in zip(PROPERTY_KINDS, self.fields)}}


def enumerate_cores() -> list[Core]:
    legal_active = [None]
    for ap, sat, val in itertools.product((0, 1), (0, 1), (-1, 0, 1)):
        if val != -1 and not (ap and sat):
            continue
        legal_active.append((ap, sat, val))
    assert len(legal_active) == 7  # one undeclared plus six legal declared possibilities
    unavailable = [Core(False, fs) for fs in itertools.product((None, "U"), repeat=2)]
    available = [Core(True, fs) for fs in itertools.product(legal_active, repeat=2)]
    cores = unavailable + available
    assert len(cores) == 53 and len(set(cores)) == 53
    # Check both primitive axioms in every source-available declared kind.
    for c in cores:
        for f in c.fields:
            if c.available and f is not None:
                ap, sat, val = f
                assert val == -1 or (ap == 1 and sat == 1)
            if not c.available:
                assert f in (None, "U")
    return cores


def forward(a: Core, b: Core) -> bool:
    """Typed F1-F5 with explicit source declared-AND-available guard."""
    if a.available and not b.available:  # F1
        return False
    if not a.declarations() <= b.declarations():  # F2
        return False
    if a.available:
        for fa, fb in zip(a.fields, b.fields):
            if fa is None:
                continue
            assert isinstance(fa, tuple) and isinstance(fb, tuple)
            aa, sa, va = fa
            ab, sb, vb = fb
            if aa > ab or sa > sb:  # F3-F4
                return False
            if va != -1 and va != vb:  # F5 (target defined same value)
                return False
    return True


def embedding(a: Core, b: Core) -> bool:
    if not forward(a, b):
        return False
    # Component maps of present one-element sorts injective. Domain/reflection
    # only on available source-declared kinds as in intended reading of Def.6.3.
    if a.available:
        for fa, fb in zip(a.fields, b.fields):
            if fa is None:
                continue
            assert isinstance(fa, tuple) and isinstance(fb, tuple)
            if fa[:2] != fb[:2] or (fa[2] == -1) != (fb[2] == -1):
                return False
    return True


def componentwise_bijective_embedding(a: Core, b: Core) -> bool:
    # In the one-point source carrier, each defined carrier map is bijective.
    # If no source carrier is available, the entire empty map family is vacuously bijective.
    return embedding(a, b)


def strict(a: Core, b: Core) -> bool:
    """S1-S4: same available-sort/declaration sets and two-way embedding."""
    return (a.available == b.available and a.declarations() == b.declarations()
            and embedding(a, b) and embedding(b, a))


def stages(a: Core, b: Core) -> tuple[bool, bool, bool, bool, bool]:
    i1 = a.available == b.available
    i2 = i1 and a.declarations() == b.declarations()
    i3 = i2 and (not a.available or all(
        fa is None or fa[:2] == fb[:2] for fa, fb in zip(a.fields, b.fields)))
    i4 = i3 and (not a.available or all(
        fa is None or fa[2] == fb[2] for fa, fb in zip(a.fields, b.fields)))
    i5 = i4  # Definition 3.7/C1: explicit completed data uniquely determined
    return i1, i2, i3, i4, i5


def find_case(cores, predicate):
    for a, b in itertools.product(cores, repeat=2):
        if predicate(a, b):
            return {"source": a.serial(), "target": b.serial()}
    raise AssertionError("No requested finite witness in search space")


def audit() -> dict:
    cores = enumerate_cores()
    n = len(cores)
    f = [[forward(a, b) for b in cores] for a in cores]
    e = [[embedding(a, b) for b in cores] for a in cores]
    s = [[strict(a, b) for b in cores] for a in cores]
    comparison = [[stages(a, b) for b in cores] for a in cores]
    # All reported claims genuinely quantified over the entire 53-core family.
    assert all(f[i][i] and e[i][i] and s[i][i] for i in range(n))
    for i, j, k in itertools.product(range(n), repeat=3):
        if f[i][j] and f[j][k]:
            assert f[i][k], ("forward_composition", i, j, k)
        if e[i][j] and e[j][k]:
            assert e[i][k], ("embedding_composition", i, j, k)
        if s[i][j] and s[j][k]:
            assert s[i][k], ("strict_composition", i, j, k)
    assert all(s[i][j] == s[j][i] for i in range(n) for j in range(n))
    assert all(not s[i][j] or (e[i][j] and e[j][i]) for i in range(n) for j in range(n))
    assert all(sum(1 for v in comparison[i][j] if not v) in range(6)
               for i in range(n) for j in range(n))
    assert all(not comparison[i][j][t+1] or comparison[i][j][t]
               for i in range(n) for j in range(n) for t in range(4))
    assert all(comparison[i][j][3] == comparison[i][j][4] == s[i][j]
               for i in range(n) for j in range(n))
    assert all(comparison[i][j] == comparison[j][i]
               for i in range(n) for j in range(n))
    # Strict class invariance: first branch unchanged after replacing models with isomorphic ones.
    strict_classes: dict[tuple, list[int]] = {}
    for i in range(n):
        key = tuple(j for j in range(n) if s[i][j])
        strict_classes.setdefault(key, []).append(i)
    for cls in strict_classes.values():
        representative = cls[0]
        assert all(comparison[representative][j] == comparison[i][j]
                   for i in cls for j in range(n))
        assert all(comparison[j][representative] == comparison[j][i]
                   for i in cls for j in range(n))
    # Demonstrate the assertion "bijective embedding implies strict" is false
    # even for two full typed property cores, without manipulating existing source code.
    bad = find_case(cores, lambda a,b:
                    componentwise_bijective_embedding(a,b)
                    and not strict(a,b)
                    and a.available == b.available
                    and a.declarations() != b.declarations())
    unavailable_identity = next(c for c in cores if not c.available and "p" in c.declarations())
    assert unavailable_identity.fields[0] == "U"
    assert f[cores.index(unavailable_identity)][cores.index(unavailable_identity)]
    counts = {"pairs": n*n,
              "forward": sum(map(sum, f)),
              "embedding": sum(map(sum,e)),
              "carrierwise_bijective_embedding": sum(map(sum,e)),
              "strict": sum(map(sum,s)),
              "strict_equivalence_classes": len(strict_classes),
              "branch_counts": {str(t):0 for t in range(1,5)}}
    for i in range(n):
        for j in range(n):
            st = comparison[i][j]
            if not st[3]:
                k = next(t+1 for t,v in enumerate(st[:4]) if not v)
                counts["branch_counts"][str(k)] += 1
    assert all(v > 0 for v in counts["branch_counts"].values())
    return {
        "case":"PA-P9A-20260901-FINITE-MORPHISM-EXHAUSTIVE-001",
        "source_pdf_sha256":PAPER_SHA256,
        "family":"fixed Formation Stage-VI, one auxiliary sort, two fixed unary property kinds, singleton-or-unavailable sort, prerequisite d, values 0/1",
        "legal_cores":n,
        "core_breakdown":{"aux_u_unavailable":4,"aux_u_singleton":49},
        "counts":counts,
        "assertions":{"all_identity_forward_embedding_strict":True,
                      "all_forward_compositions_well_typed":True,
                      "all_embedding_compositions_well_typed":True,
                      "all_strict_compositions_well_typed":True,
                      "strict_symmetric":True,
                      "stage_nested_all_pairs":True,
                      "stage4_equals_stage5_all_pairs":True,
                      "stage4_nonempty_iff_strict_all_pairs":True,
                      "stage_profiles_symmetric_all_pairs":True,
                      "stage_profiles_invariant_under_strict_all_pairs":True,
                      "first_branch_exists_at_each_of_1_2_3_4_in_family":True},
        "source_literal_F3_illtyped_identity_witness":unavailable_identity.serial(),
        "carrierwise_bijective_embedding_not_strict_witness":bad,
        "reading_boundary":"Guard F3-F5 for source declared AND profile available; interpret S2/S3 as extra to componentwise bijection",
        "general_model_theorem_proved_by_finite_search":False,
        "full_paper_FPA":"OPEN",
        "original_experiment_source_changed":False,
        "manuscript_PDF_or_TEX_changed":False}


def main() -> None:
    assert len(sys.argv) <= 2, "usage: verify_p9a_finite_morphisms.py [output_json]"
    obj = audit()
    out = Path(sys.argv[1]) if len(sys.argv) == 2 else Path(__file__).resolve().parent.parent / "results/p9a_finite_morphisms.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print("P9A finite comparison: PASS", obj["legal_cores"], "cores", obj["counts"])


if __name__ == "__main__":
    main()
