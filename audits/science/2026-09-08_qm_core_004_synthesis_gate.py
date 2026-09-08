#!/usr/bin/env python3
"""QM Core 004 synthesis provenance gate.

This script is an audit ledger, not a proof of quantum theory.  It checks that the
five exact-interface items isolated in QM Core 004E are no longer left as GAP or
NOT_EQUIVALENT, while keeping Class-C/D conditions separate from independent
Class-A/B evidence.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class LedgerItem:
    code: str
    layer: str
    provenance: str
    status: str
    independent_evidence: bool
    note: str


ITEMS = [
    LedgerItem("DSD-TYPING", "Formation/Property", "A", "DERIVED", True,
               "typed identity, status, restriction and equivalence discipline"),
    LedgerItem("DSD-LOSS", "Static/Dynamics", "A", "DERIVED", True,
               "aggregate/readout information-loss and reconstruction discipline"),
    LedgerItem("DSD-LINEAGE", "Dynamics", "A", "DERIVED", True,
               "regular evolution versus formation transition/lineage separation"),
    LedgerItem("ORE", "Operational", "B", "DERIVED", True,
               "randomized preparation induces convex mixture"),
    LedgerItem("AFFINE-READOUT", "Operational", "B", "DERIVED", True,
               "probability readout is affine under operational randomization"),
    LedgerItem("MPT", "Operational", "B", "DERIVED", True,
               "mixture-preserving transformations are affine"),
    LedgerItem("OCD", "Operational", "B", "DERIVED", True,
               "capacity defined by joint perfect distinguishability"),

    LedgerItem("LDC-QM", "Composite", "C", "EXPLICIT_ASSUMPTION", False,
               "local descriptive completeness selector"),
    LedgerItem("RRDE-QM", "Restriction", "C", "EXPLICIT_ASSUMPTION", False,
               "recursive restriction selector"),
    LedgerItem("CRR-QM", "Reversible", "C", "EXPLICIT_ASSUMPTION", False,
               "continuous pure-state reachability selector"),
    LedgerItem("NR-QM", "Effects", "C", "EXPLICIT_ASSUMPTION", False,
               "no-restriction/effect-completeness selector"),

    LedgerItem("OSC/SOLA-QM", "Topology", "D", "EXPLICIT_ASSUMPTION", False,
               "operational closure/compactness exact lock"),
    LedgerItem("CRG/RGPR-QM", "Reversible", "D", "EXPLICIT_ASSUMPTION", False,
               "connected full reversible-group exact lock"),
    LedgerItem("ILPC-QM", "Composite", "D", "EXPLICIT_ASSUMPTION", False,
               "independent local-product composition precursor"),
    LedgerItem("LFRR-QM", "Restriction", "D", "EXPLICIT_ASSUMPTION", False,
               "linear full reference recursion"),
    LedgerItem("CMT-QM", "Restriction", "D", "EXPLICIT_ASSUMPTION", False,
               "complete-measurement transitivity"),
    LedgerItem("IFPC-QM", "Capacity", "D", "EXPLICIT_ASSUMPTION", False,
               "iterated finite product composition"),
    LedgerItem("IDDC-QM", "Capacity", "D", "EXPLICIT_ASSUMPTION", False,
               "intrinsic exact one-step capacity descent"),

    LedgerItem("ETC-QM", "Composite", "C/D", "CONDITIONAL_DERIVATION", False,
               "tensor carrier from ILPC + LDC + finite operational linearization"),
    LedgerItem("ULRRDE-QM", "Restriction", "D", "CONDITIONAL_DERIVATION", False,
               "universal recursion from LFRR + CMT"),
    LedgerItem("CFE-QM", "Capacity", "D", "CONDITIONAL_DERIVATION", False,
               "all finite capacities from nontrivial seed + IFPC + IDDC"),

    LedgerItem("BORN-TRACE", "Probability", "External+C", "CONDITIONAL_DERIVATION", False,
               "generalized Gleason/Busch representation after supplied Hilbert-effect carrier plus gluing/normalization"),
    LedgerItem("HILBERT-CARRIER", "State/effect geometry", "External", "SUPPLIED", False,
               "complex Hilbert/effect carrier is not independently derived by QM Core 004"),
]

EXACT_004 = {
    "OSC/SOLA-QM",
    "CRG/RGPR-QM",
    "ETC-QM",
    "ULRRDE-QM",
    "CFE-QM",
}

BLOCKING = {"GAP", "NOT_EQUIVALENT"}


def run_checks() -> None:
    exact = [item for item in ITEMS if item.code in EXACT_004]
    assert len(exact) == 5, "all five QM Core 004E exact-interface items must be present"
    assert all(item.status not in BLOCKING for item in exact), (
        "an exact-interface item remains unclassified"
    )
    assert next(item for item in ITEMS if item.code == "HILBERT-CARRIER").status == "SUPPLIED"
    assert next(item for item in ITEMS if item.code == "BORN-TRACE").status == "CONDITIONAL_DERIVATION"
    assert all(item.independent_evidence for item in ITEMS if item.provenance in {"A", "B"})
    assert all(not item.independent_evidence for item in ITEMS if item.provenance in {"C", "D", "C/D"})


def print_summary() -> None:
    exact = [item for item in ITEMS if item.code in EXACT_004]
    independent = [item for item in ITEMS if item.independent_evidence]
    target_inputs = [item for item in ITEMS if item.provenance in {"C", "D", "C/D"}]

    print("QM CORE 004 SYNTHESIS LEDGER")
    print(f"exact_004_items: {len(exact)}")
    print(f"exact_unclassified: {sum(item.status in BLOCKING for item in exact)}")
    print(f"independent_A_B_evidence_categories: {len(independent)}")
    print(f"target_or_comparator_categories: {len(target_inputs)}")
    print("hilbert_carrier_status: SUPPLIED")
    print("born_trace_status: CONDITIONAL_DERIVATION")
    print("independent_complex_Hilbert_derivation: NO")
    print("conditional_external_reconstruction_interface: CLASSIFIED")
    print("OVERALL: PASS_WITH_BOUNDARY")


def print_ledger() -> None:
    for item in ITEMS:
        flag = "INDEPENDENT" if item.independent_evidence else "NON-INDEPENDENT"
        print(f"{item.code:18s} {item.provenance:10s} {item.status:24s} {flag:15s} {item.note}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all", "check", "summary", "ledger"), default="all")
    args = parser.parse_args()

    if args.mode in {"all", "check"}:
        run_checks()
        if args.mode == "check":
            print("CHECK: PASS")
            return
    if args.mode in {"all", "summary"}:
        print_summary()
    if args.mode in {"all", "ledger"}:
        print_ledger()


if __name__ == "__main__":
    main()
