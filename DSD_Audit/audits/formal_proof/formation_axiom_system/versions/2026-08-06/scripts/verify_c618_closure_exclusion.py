#!/usr/bin/env python3
r"""Finite C6.18 audit: enumerate stage-set profiles, then reuse T6.16 witnesses.

This program verifies only finite implications and stored prior finite cases.
The general Corollary 6.18 proof depends on source Theorem 6.17(ii).
Run from the DSD_Method_Family repository root on Windows:
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c618_closure_exclusion.py
Optional first argument selects output JSON. Standard library only.
"""
from itertools import product
import json
import sys
from pathlib import Path

CASE_ID = "FAS-F2-C6.18-001"
SOURCE_SHA = "8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a"
# One candidate's first failing stage, with -1 denoting survival through I7.
DROP_OPTIONS = (-1, 0, 1, 2, 3, 4, 5, 6, 7)


def stage_sets(labels):
    """The SAME candidate identities are filtered at every stage."""
    return tuple(frozenset(i for i, drop in enumerate(labels)
                           if drop == -1 or k < drop)
                 for k in range(8))


def branching_index(stages):
    if stages[-1]:
        return None  # The strict-isomorphic case: b is not defined.
    return next(k for k, stage in enumerate(stages) if not stage)


def check():
    profile_count = 0
    source_compatible = 0
    excluded_four = 0
    abstract_four = 0
    observed = set()
    count_by_ambient = {}
    first_four_witness = None
    for n in range(4):
        count_by_ambient[str(n)] = {"total": 0, "i3_equals_i4": 0,
                                    "nested_only_first_b4": 0}
        for labels in product(DROP_OPTIONS, repeat=n):
            stages = stage_sets(labels)
            b = branching_index(stages)
            profile_count += 1
            count_by_ambient[str(n)]["total"] += 1
            assert all(stages[k + 1] <= stages[k] for k in range(7))
            if b is not None:
                assert stages[b] == frozenset()
                assert all(stages[j] for j in range(b))
                assert all(not stages[k] for k in range(b, 8))
            else:
                assert stages[-1]
            if stages[3] == stages[4]:
                source_compatible += 1
                count_by_ambient[str(n)]["i3_equals_i4"] += 1
                # The exact corollary's finite-set consequence.
                assert b != 4
                excluded_four += 1
                observed.add(b)
            elif b == 4:
                # Nestedness ALONE permits b=4, but equality I3=I4 fails.
                abstract_four += 1
                count_by_ambient[str(n)]["nested_only_first_b4"] += 1
                if first_four_witness is None:
                    first_four_witness = {"drop_labels": list(labels),
                                          "stage_counts": [len(x) for x in stages]}
    assert profile_count == 820, profile_count
    assert source_compatible == 585, source_compatible
    assert abstract_four == 71, abstract_four
    assert observed == {None, 0, 1, 2, 3, 5, 6, 7}, observed
    assert first_four_witness is not None
    assert first_four_witness["stage_counts"] == [1, 1, 1, 1, 0, 0, 0, 0]

    # Reuse earlier stored genuine source-typed finite comparisons rather
    # than pretending abstract chains are full Formation models.
    results_dir = Path(__file__).resolve().parent.parent / "results"
    previous = results_dir / "t616_first_branching.json"
    previous_data = json.loads(previous.read_text(encoding="utf-8"))
    assert previous_data["audit_id"] == "FAS-F2-T6.16-001"
    assert previous_data["source_sha256"] == SOURCE_SHA
    fixtures = previous_data["typed_selected_cases"]
    assert len(fixtures) == 8
    first_indices = {}
    for label, record in fixtures.items():
        counts = record["stage_counts"]
        b = record["b"]
        assert len(counts) == 8 and all(counts[k + 1] <= counts[k]
                                        for k in range(7))
        assert counts[3] == counts[4]
        if b is None:
            assert counts[7] > 0
        else:
            assert b in range(8) and counts[b] == 0
            assert all(counts[j] > 0 for j in range(b))
            assert b != 4
        first_indices[label] = b
    assert set(first_indices.values()) == {None, 0, 1, 2, 3, 5, 6, 7}

    return {
        "audit_id": CASE_ID,
        "source_sha256": SOURCE_SHA,
        "all_checks_passed": True,
        "ambient_cardinalities_exhausted": [0, 1, 2, 3],
        "all_abstract_nested_profiles": profile_count,
        "profiles_with_I3_equal_I4": source_compatible,
        "profiles_with_I3_equal_I4_and_b4": 0,
        "profiles_with_nestedness_only_and_b4": abstract_four,
        "countercase_to_nestedness_alone": first_four_witness,
        "source_compatible_branch_values": [
            "undefined" if b is None else b
            for b in sorted(observed, key=lambda x: (-1 if x is None else x))
        ],
        "by_ambient_cardinality": count_by_ambient,
        "earlier_t616_source_typed_fixture_cases": len(fixtures),
        "earlier_t616_fixture_first_branch_indices": first_indices,
        "earlier_t616_all_satisfy_I3_equal_I4": True,
        "nestedness_alone_is_insufficient": True,
        "no_circular_use_of_corollary_6_18": True,
        "finite_computation_not_general_proof": True,
        "independent_external_validation": False,
    }


def main():
    data = check()
    outfile = (Path(sys.argv[1]) if len(sys.argv) > 1 else
               Path(__file__).resolve().parent.parent / "results" /
               "c618_closure_exclusion.json")
    outfile.parent.mkdir(parents=True, exist_ok=True)
    outfile.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n",
                       encoding="utf-8")
    print("C6.18 finite checks PASS:", data["all_abstract_nested_profiles"],
          "abstract profiles,", data["earlier_t616_source_typed_fixture_cases"],
          "earlier source-typed model pairs")
    print("OUTPUT:", outfile)


if __name__ == "__main__":
    main()
