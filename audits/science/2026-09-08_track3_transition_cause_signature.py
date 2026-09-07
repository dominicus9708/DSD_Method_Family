#!/usr/bin/env python3
"""
Track-3 finite witness: typed transition-cause signatures for describability-regime motion.

Purpose
-------
Show that the same observed sector transition can arise from distinct DSD-layer changes,
and refine the earlier sector-flux bookkeeping by an exact cause-signature partition.

No quantum-gravity premise is used. The numerical weights are bookkeeping-only.
Python standard library only.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class SideProfile:
    formation: bool = True
    property_applicable: bool = True
    prerequisite_satisfied: bool = True
    access_allowed: bool = True
    readout_defined: bool = True
    representation: str = "rep0"
    value: float = 0.0


@dataclass(frozen=True)
class Record:
    name: str
    q: SideProfile
    r: SideProfile
    weight: float = 1.0


def side_describable(profile: SideProfile) -> bool:
    return (
        profile.formation
        and profile.property_applicable
        and profile.prerequisite_satisfied
        and profile.access_allowed
        and profile.readout_defined
    )


def sector(record: Record) -> str:
    key = (side_describable(record.q), side_describable(record.r))
    return {
        (False, False): "NEITHER",
        (True, False): "Q_ONLY",
        (False, True): "R_ONLY",
        (True, True): "OVERLAP",
    }[key]


def side_cause_labels(old: SideProfile, new: SideProfile) -> set[str]:
    labels: set[str] = set()

    if old.formation != new.formation:
        labels.add("FORMATION_CHANGE")

    if (
        old.property_applicable != new.property_applicable
        or old.prerequisite_satisfied != new.prerequisite_satisfied
    ):
        labels.add("PROPERTY_STATUS_CHANGE")

    if old.access_allowed != new.access_allowed:
        labels.add("ACCESS_DOMAIN_CHANGE")

    if old.readout_defined != new.readout_defined:
        labels.add("READOUT_OR_RESOLUTION_CHANGE")

    if old.representation != new.representation:
        labels.add("PASSIVE_REPRESENTATION_CHANGE")

    if old.value != new.value:
        labels.add("REGULAR_VALUE_OR_FIELD_CHANGE")

    return labels


def cause_signature(old: Record, new: Record) -> tuple[str, ...]:
    labels = side_cause_labels(old.q, new.q) | side_cause_labels(old.r, new.r)
    return tuple(sorted(labels))


def build_membership_cases() -> tuple[list[Record], list[Record]]:
    q_ok = SideProfile()
    r_ok = SideProfile()

    old_records = [
        Record("access_case", q_ok, SideProfile(access_allowed=False), 1.0),
        Record(
            "prereq_case",
            q_ok,
            SideProfile(prerequisite_satisfied=False),
            1.5,
        ),
        Record("formation_case", q_ok, SideProfile(formation=False), 2.0),
        Record("readout_case", q_ok, SideProfile(readout_defined=False), 2.5),
        Record(
            "multi_case",
            q_ok,
            SideProfile(prerequisite_satisfied=False, access_allowed=False),
            3.0,
        ),
    ]

    new_records = [
        Record(record.name, q_ok, r_ok, record.weight) for record in old_records
    ]
    return old_records, new_records


def cause_resolved_flux(
    old_records: list[Record], new_records: list[Record]
) -> tuple[dict[tuple[str, str], float], dict[tuple[str, str, tuple[str, ...]], float]]:
    if len(old_records) != len(new_records):
        raise ValueError("old/new record lists must have the same length")

    total_flux: defaultdict[tuple[str, str], float] = defaultdict(float)
    signature_flux: defaultdict[tuple[str, str, tuple[str, ...]], float] = defaultdict(float)

    for old, new in zip(old_records, new_records):
        if old.name != new.name:
            raise ValueError("record names must align across the transition")

        a = sector(old)
        b = sector(new)
        signature = cause_signature(old, new)

        total_flux[(a, b)] += old.weight
        signature_flux[(a, b, signature)] += old.weight

    return dict(total_flux), dict(signature_flux)


def check_signature_partition(
    total_flux: dict[tuple[str, str], float],
    signature_flux: dict[tuple[str, str, tuple[str, ...]], float],
) -> bool:
    reconstructed: defaultdict[tuple[str, str], float] = defaultdict(float)
    for (a, b, _signature), weight in signature_flux.items():
        reconstructed[(a, b)] += weight
    return dict(reconstructed) == total_flux


def representation_control() -> dict[str, object]:
    q_ok = SideProfile()
    old = Record(
        "representation_only",
        q_ok,
        SideProfile(access_allowed=False, representation="rep0"),
    )
    new = Record(
        "representation_only",
        q_ok,
        SideProfile(access_allowed=False, representation="rep1"),
    )

    return {
        "old_sector": sector(old),
        "new_sector": sector(new),
        "cause_signature": cause_signature(old, new),
        "membership_preserved": sector(old) == sector(new),
    }


def run_cases() -> None:
    old_records, new_records = build_membership_cases()

    print("CAUSE CASES")
    for old, new in zip(old_records, new_records):
        print(
            f"{old.name:14s}: {sector(old):8s} -> {sector(new):8s} "
            f"cause={cause_signature(old, new)} weight={old.weight}"
        )

    same_observed_motion = all(
        sector(old) == "Q_ONLY" and sector(new) == "OVERLAP"
        for old, new in zip(old_records, new_records)
    )
    distinct_signatures = len(
        {cause_signature(old, new) for old, new in zip(old_records, new_records)}
    )

    print(f"same observed Q_ONLY->OVERLAP motion: {same_observed_motion}")
    print(f"distinct cause signatures: {distinct_signatures}")

    rep = representation_control()
    print("REPRESENTATION CONTROL")
    for key, value in rep.items():
        print(f"{key}: {value}")


def run_flux() -> None:
    old_records, new_records = build_membership_cases()
    total_flux, signature_flux = cause_resolved_flux(old_records, new_records)

    print("TOTAL FLUX")
    for key in sorted(total_flux):
        print(f"{key}: {total_flux[key]}")

    print("CAUSE-SIGNATURE FLUX")
    for key in sorted(signature_flux, key=str):
        print(f"{key}: {signature_flux[key]}")

    print(f"signature partition reconstructs total flux: {check_signature_partition(total_flux, signature_flux)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("cases", "flux", "all"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("cases", "all"):
        run_cases()
    if args.mode in ("flux", "all"):
        run_flux()


if __name__ == "__main__":
    main()
