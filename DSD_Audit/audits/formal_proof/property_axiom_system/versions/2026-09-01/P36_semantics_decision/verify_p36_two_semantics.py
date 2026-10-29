#!/usr/bin/env python3
"""PA-P36: independent bounded checks for active vs surplus raw typed property data.
Author: Kwon Dominicus (research manuscript); verification script companion.
Usage from DSD_Method_Family root:
 python DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/P36_semantics_decision/verify_p36_two_semantics.py --out <path>
No external dependencies. Does NOT edit manuscript, reproduce a general ZFC proof, or assert a chosen semantic convention.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

P27_SHA = {
    "EN": "51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb",
    "KR": "a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb",
}

@dataclass(frozen=True)
class Primitive:
    declared: frozenset[str]
    supplied_sorts: frozenset[str]
    app: tuple[tuple[str, frozenset[tuple[str, ...]]], ...]
    sat: tuple[tuple[str, str, frozenset[tuple[str, ...]]], ...]
    xi: tuple[tuple[str, tuple[tuple[tuple[str, ...], int], ...]], ...]


def p(*, declared=(), supplied_sorts=(), app=(), sat=(), xi=()) -> Primitive:
    return Primitive(frozenset(declared), frozenset(supplied_sorts), tuple(app), tuple(sat), tuple(xi))


def active_kinds(a: Primitive) -> frozenset[str]:
    # Shared test signature has candidates p:(h), no prerequisites; q:(h), prerequisite {d}.
    return a.declared & {"p", "q"}


def normal(a: Primitive) -> Primitive:
    act = active_kinds(a)
    return Primitive(a.declared, a.supplied_sorts,
        tuple(k for k in a.app if k[0] in act),
        tuple(k for k in a.sat if k[0] in act),
        tuple(k for k in a.xi if k[0] in act))


def derived(a: Primitive) -> tuple:
    c = normal(a)
    domains = tuple((kind, tuple(x for x, _ in assignments)) for kind, assignments in c.xi)
    records = tuple((kind, x, z) for kind, assignments in c.xi for x, z in assignments)
    return (domains, records)


def complete_raw(a: Primitive) -> tuple[Primitive, tuple]:
    return a, derived(a)


def reduce_raw(full: tuple[Primitive, tuple]) -> Primitive:
    return full[0]


def complete_norm(a: Primitive) -> tuple[Primitive, tuple]:
    return normal(a), derived(a)


def raw_descriptor(a: Primitive) -> tuple:
    return a, derived(a)


def active_equiv(a: Primitive, b: Primitive) -> bool:
    # A deliberately small fixed inherited h carrier: no auxiliary maps and identity on h.
    return normal(a) == normal(b)


def raw_equiv(a: Primitive, b: Primitive) -> bool:
    return a == b


def run() -> dict:
    left = p()
    right = p(app=(("p", frozenset({("a",)})),))  # surplus for UNDECLARED p
    extra_empty = p(app=(("p", frozenset()),))
    extra_value = p(xi=(("p", ((("a",), 0),)),))
    canonical_on = p(declared=("p",), app=(("p", frozenset({("a",)})),),
                     xi=(("p", ((("a",), 0),)),))
    surplus_on = p(declared=("p",), app=(("p", frozenset({("a",)})),),
                   xi=(("p", ((("a",), 0),)),), sat=(("q", "d", frozenset()),))
    cases = {
        "A_canonical_no_surplus": normal(left) == left and normal(canonical_on) == canonical_on,
        "B_surplus_well_typed_example_requires_extra_convention": right != left and right.app[0][1] <= frozenset({("a",), ("b",)}),
        "B_can_keep_distinct_raw_presentation": raw_descriptor(right) != raw_descriptor(left),
        "N_forgets_inactive_unlabelled_extra": normal(right) == normal(left),
        "N_forgets_explicit_empty_surplus": extra_empty != left and normal(extra_empty) == normal(left),
        "N_forgets_extra_value": extra_value != left and normal(extra_value) == normal(left),
        "N_idempotent": all(normal(normal(a)) == normal(a) for a in [left,right,extra_empty,extra_value,canonical_on,surplus_on]),
        "N_has_section_by_empty_surplus": all(normal(a) == a for a in [left,canonical_on]),
        "N_not_injective_on_B": right != left and normal(right) == normal(left),
        "derived_depends_only_on_active": all(derived(a) == derived(normal(a)) for a in [left,right,extra_empty,extra_value,canonical_on,surplus_on]),
        "C1_raw_left_inverse": all(reduce_raw(complete_raw(a)) == a for a in [left,right,extra_empty,extra_value,canonical_on,surplus_on]),
        "C1_raw_right_inverse_on_actual_full": all(complete_raw(reduce_raw(complete_raw(a))) == complete_raw(a) for a in [left,right,extra_empty,extra_value,canonical_on,surplus_on]),
        "C1_normalizing_breaks_raw_exact_inverse": reduce_raw(complete_norm(right)) != right,
        "strict_active_iso_not_raw_iso": active_equiv(left,right) and not raw_equiv(left,right),
        "raw_identity_iso_implies_active": all(not raw_equiv(a,b) or active_equiv(a,b) for a in [left,right,extra_empty,extra_value,canonical_on] for b in [left,right,extra_empty,extra_value,canonical_on]),
        "raw_stage3_not_stage3_active": left.app != right.app and normal(left).app == normal(right).app,
        "surplus_sat_independent_of_active_C1": normal(canonical_on) == normal(surplus_on) and derived(canonical_on) == derived(surplus_on),
        "availability_vs_explicit_empty_distinct": p() != p(supplied_sorts=("u",)),
    }
    assert all(cases.values()), {k:v for k,v in cases.items() if not v}
    return {
        "audit_id": "PA-P36-20261029-SEMANTIC-A-B-DECISION-AUDIT",
        "source_frozen_sha256": P27_SHA,
        "checked": len(cases),
        "passed": sum(cases.values()),
        "checks": cases,
        "scope": "Inherited carrier h={a,b}, candidate p:(h), delta(p)=empty and candidate q:(h), delta(q)={d}; no tested model declares q. Raw examples are CONDITIONAL on presentation B; all maps here identity. Derived() models only assignment domains and records (not full C1 status).",
        "mathematical_scope": "ZFC arguments in accompanying audit report; this code merely checks finite witness separation.",
        "decision": "A = least additional machinery for active-core FPA; B = possible with raw-presentation/core quotient split. Author choice not asserted.",
        "revision": "Deferred; no P27 manuscript or Zenodo edits",
        "whole_property_fpa": "OPEN",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    result = run()
    data = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(data, encoding="utf-8")
    print(data, end="")


if __name__ == "__main__":
    main()