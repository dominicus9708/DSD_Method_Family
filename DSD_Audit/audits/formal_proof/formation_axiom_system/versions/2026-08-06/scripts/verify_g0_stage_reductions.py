#!/usr/bin/env python3
"""Formation F2 G0: deterministic check of Definition 2.4 / Proposition 2.5.

Models the eight *record coordinate sets*, not actual Formation axioms.
The general identity and composition laws follow from coordinate erasure,
not from this finite test alone. Standard library; Python 3.10+.

Windows 11 / repository root:
py -3.11 DSD_Audit\\audits\\formal_proof\\formation_axiom_system\\scripts\\verify_g0_stage_reductions.py --output DSD_Audit\\audits\\formal_proof\\formation_axiom_system\\results\\g0_stage_reductions.json
"""
import argparse
import json
from itertools import combinations_with_replacement
from pathlib import Path

STAGES = (
    ("B", "F", "M_B", "E_B", "P_B", "mat", "act", "anchors_E", "anchors_P",
     "Lambda", "V_pointed", "R_carrier"),
    ("Adm_expr", "Des_expr"),
    ("Res",),
    ("Realize", "Adm_cfg", "LC", "BC"),
    ("Psi", "A_star", "Des_cfg", "Kdes", "Ades"),
    ("Lambda_delta", "Q", "q", "Gamma", "size", "delta"),
    ("Role_relation", "U", "Chan", "C"),
    ("W", "T", "Dcomp", "Comp"),
)


def record(k):
    assert 0 <= k <= 7
    return tuple(tuple((s, field) for field in STAGES[s]) for s in range(k + 1))


def projection(j, i, x):
    assert 0 <= i <= j <= 7 and len(x) == j + 1
    return x[: i + 1]


def run():
    triple_count = 0
    for i, j, k in combinations_with_replacement(range(8), 3):
        assert projection(k, k, record(k)) == record(k)
        assert projection(j, i, projection(k, j, record(k))) == projection(k, i, record(k))
        triple_count += 1
    truncation_count = 0
    for j in range(8):
        for i in range(j + 1):
            assert projection(j, i, record(j)) == record(i)
            truncation_count += 1
    assert triple_count == 120 and truncation_count == 36
    assert "R_carrier" in STAGES[0] and "Role_relation" not in STAGES[0]
    assert "Role_relation" in STAGES[6]
    return {
        "audit_id": "FAS-F2-G0-001",
        "source_pdf_sha256": "8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a",
        "test_type": "coordinate-record combinatorial smoke test",
        "general_mathematical_proof": False,
        "independent_external_replication": False,
        "stage_count_including_bookkeeping_zero": 8,
        "formation_stage_count": 7,
        "reduction_composition_triples_verified": triple_count,
        "truncation_pairs_verified": truncation_count,
        "roles_carrier_in_stage_zero": True,
        "role_relation_in_stage_six": True,
        "all_assertions_passed": True,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: 120 reduction-composition triples, 36 full-truncation projections")
    print("Output:", args.output)


if __name__ == "__main__":
    main()
