#!/usr/bin/env python3
"""MF-REG-20261025-002. Source-locked finite compatibility fixtures, not full protocol proofs.
Author: Kwon Dominicus. Frozen expected outcomes are loaded from a prior Git commit.
"""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import fitz

PROJECTION_CASES = {
    "Comparison": ["J0", "J1", "J2", "B0", "B1"],
    "Analysis": ["Z0", "Z1", "Z2", "A0"],
    "Specification": ["Z0", "Z1", "Z2"],
    "Aggregation": ["A0", "Z0", "Z1"],
    "Compression": ["A0", "Z2"],
    "Reconstruction": ["A0", "Z0", "Z2"],
    "Measurement": ["Z0", "Z1", "B0", "B1"],
    "Computation": ["P0", "B0", "B1", "Z1"],
    "Synthesis": ["S0", "A0"],
    "Audit": ["Z0", "A0", "J0", "B1", "S0"],
}

def source_lock(path, meta):
    b = Path(path).read_bytes()
    h = hashlib.sha256(b).hexdigest()
    with fitz.open(path) as doc:
        count = len(doc)
        full_text = "\n".join(page.get_text() for page in doc)
    return {"sha256": h, "pages": count, "hash_and_pages_match": h == meta["sha256"] and count == meta["pages"]}, full_text

def evaluate(case):
    kind = case["kind"]
    if kind in ("zero_extension", "zero_extension_sidecar"):
        universe, admitted = case["universe"], set(case["admitted"])
        terms = case["terms"]
        assert all(c in universe for c in admitted) and set(terms) == admitted
        values = {x: terms[x] if x in admitted else 0 for x in universe}
        pairs = [(a, b) for i, a in enumerate(universe) for b in universe[i + 1:]]
        collision = any(values[a] == values[b] and (a in admitted) != (b in admitted) for a, b in pairs)
        result = {"values": values, "collision_with_membership_difference": collision}
        if kind == "zero_extension":
            result["output_membership_discriminates"] = not collision
        else:
            result["extended_status_discriminates"] = all((values[a], a in admitted) != (values[b], b in admitted) for a,b in pairs if (a in admitted) != (b in admitted))
        return result
    if kind == "finite_aggregate_fibers":
        channels, families = case["channels"], case["families"]
        assert all(set(f) <= set(channels) for f in families)
        outputs = [sum(channels[c] for c in f) for f in families]
        supports = [frozenset(f) for f in families]
        counts = Counter(outputs)
        return {"outputs": outputs, "support_difference": len(set(supports)) > 1,
                "noninjective_on_declared_class": any(outputs[i] == outputs[j] and supports[i] != supports[j]
                                                        for i in range(len(families)) for j in range(i + 1, len(families))),
                "inverse_fiber_cardinality_at_zero": counts[0], "unique_source_from_output_only": counts[0] == 1,
                "support_sidecar_unique": len(set(zip(outputs, supports))) == len(families)}
    if kind == "strict_identity_with_prescribed_j":
        assert case["strict_identity"] is True and case["j_multiplier"] != 0
        mapped = case["j_multiplier"] * case["source_total"]
        return {"mapped_source": mapped, "j_composite_coincidence": mapped == case["target_total"],
                "strict_identity": case["strict_identity"]}
    if kind == "unequal_channel_cardinality":
        assert case["j_multiplier"] != 0
        ls, rs = sum(case["source_channels"].values()), sum(case["target_channels"].values())
        return {"source_composite": ls, "target_composite": rs,
                "j_composite_coincidence": case["j_multiplier"] * ls == rs,
                "strict_formation_isomorphism_possible": len(case["source_channels"]) == len(case["target_channels"])}
    if kind == "nested_stage_first_branch":
        stages = {int(k): v for k, v in case["stage_nonempty"].items()}
        assert sorted(stages) == list(range(8))
        # I_(k+1) subset I_k; verified nonempty after verified emptiness would violate nesting.
        for i in range(7):
            assert not (stages[i] is False and stages[i + 1] is True)
        # Determine a *justified* first empty index, not merely first inspected empty index.
        first = next((i for i in range(8) if stages[i] is False and all(stages[j] is True for j in range(i))), None)
        return {"first_justified_branch": first, "stage_three_empty": stages[3] is False,
                "closure_exclusion_at_stage_four": stages[3] == stages[4] and first != 4}
    if kind == "formation_sum_vs_domain_synthesis":
        assert all(c in case["channels"] for c in case["family"])
        val = sum(case["channels"][c] for c in case["family"])
        return {"formation_composite": val, "formation_composite_defined": True,
                "domain_synthesis_terminal": "READY_FOR_DOMAIN_VALIDATION" if case["domain_composition_bridge_supplied"] else "BLOCKED"}
    if kind == "zero_term_pruning":
        c = case["candidate_channel"]
        val = case["channels"][c]
        retain = "channel_membership" in case["required_output"] and c in case["channels"]
        return {"raw_value": val, "prune_as_irrelevant": val == 0 and not retain}
    raise ValueError("Unknown frozen kind " + kind)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixtures", required=True)
    for k in ("formation", "property", "aggregation", "dynamics"):
        parser.add_argument("--" + k, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    packet = json.loads(Path(args.fixtures).read_text(encoding="utf-8"))
    assert packet["case_id"] == "MF-REG-20261025-002"
    assert len(packet["cases"]) == 11 and len(set(c["id"] for c in packet["cases"])) == 11
    assert packet["methods_in_scope"] == list(PROJECTION_CASES)
    sources, raw = {}, {}
    for name, lock in packet["source_locks"].items():
        sources[name], raw[name] = source_lock(getattr(args, name), lock)
    s = re.sub(r"\s+", " ", raw["formation"])
    anchors = {
        "T4.7_residual_independence": all(t in s for t in ("Theorem 4.7", "six residual primitive constraints", "not asserted to remain true")),
        "P5.13_conditional_zero_extension": all(t in s for t in ("Proposition 5.13", "absent candidate", "admitted channel", "This loss is not asserted for every formation model")),
        "P5.14_noninjective_finite_composition": all(t in s for t in ("Proposition 5.14", "Non-injective composition is permitted")),
        "P6.22_6.26_cardinality_obstruction": all(t in s for t in ("Proposition 6.22", "Corollary 6.26", "Channel-cardinality obstruction")),
        "D2_supplied_material_boundary": all(t in s for t in ("fifty-seven material items", "six exposed", "supplied material-record input")),
        "D2_arithmetic_57_9_6": 9 + 12 + 36 == 57 and 2 + 1 + 6 == 9 and 8 - 2 == 6,
        "S6.15_6.16_nestedness": all(t in s for t in ("Definition 6.15", "Theorem 6.16", "nestedness")),
        "discussion_fixed_J_nonimplication": all(t in s for t in ("independently prescribed J", "no unconditional implication ordering")),
    }
    results = {}
    assertions = []
    for case in packet["cases"]:
        observed = evaluate(case)
        expected = case["expected"]
        checks = {k: observed.get(k, "<NOT_EMITTED>") == v for k, v in expected.items()}
        results[case["id"]] = {"kind": case["kind"], "actual": observed, "expected": expected,
                                "field_checks": checks, "pass": all(checks.values()) and set(observed) == set(expected)}
        assertions.extend(checks.values())
        assertions.append(set(observed) == set(expected))
    projections = {method: {"fixture_ids": ids, "bounded_guard_retrace_pass": all(results[c]["pass"] for c in ids)}
                   for method, ids in PROJECTION_CASES.items()}
    output = {"audit_id": packet["case_id"], "author": packet["author"],
              "frozen_fixture_commit": "07bcf6e70333a0e5862d4e271b99f90ef0ee163f",
              "frozen_precommit": packet["precommit"], "preexecution_correction": packet["correction"],
              "sources": sources, "source_anchors": anchors, "case_results": results,
              "method_guard_projections": projections,
              "counts": {"source_locks_pass": sum(v["hash_and_pages_match"] for v in sources.values()),
                         "source_anchors_pass": sum(anchors.values()), "case_families": len(results),
                         "case_families_pass": sum(v["pass"] for v in results.values()),
                         "expected_fields_checked": sum(len(x["field_checks"]) for x in results.values()),
                         "expected_fields_pass": sum(sum(x["field_checks"].values()) for x in results.values()),
                         "exact_output_keyset_checks_pass": sum(set(x["actual"]) == set(x["expected"]) for x in results.values()),
                         "method_guard_projections_pass": sum(x["bounded_guard_retrace_pass"] for x in projections.values()),
                         "method_guard_projections_total": len(projections)},
              "caveats": ["not original old-version run: 2026-08-06 source PDF not mounted",
                          "projections are finite logical guards, not full frozen method-protocol execution",
                          "no construction or independent audit of full D2 57-element witness",
                          "source text anchoring is not a theorem proof",
                          "none of these cases is independent evaluator or new real-world evidence"]}
    ok = (len(sources) == 4 and all(x["hash_and_pages_match"] for x in sources.values())
          and all(anchors.values()) and all(assertions)
          and all(x["bounded_guard_retrace_pass"] for x in projections.values()))
    output["verdict"] = "PASS_WITH_BOUNDARY" if ok else "FAIL_WITH_EVIDENCE"
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": output["verdict"], **output["counts"]}, sort_keys=True))
    if not ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
