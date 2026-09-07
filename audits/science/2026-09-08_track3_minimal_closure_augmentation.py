#!/usr/bin/env python3
"""
Track-3 minimal closure augmentation / sufficient-state gate.

Purpose
-------
Given a full finite state family S, aggregate A:S->U, and deterministic
transition Gamma:S->S, test which reduced augmentations eta make
A_tilde=(A, eta) dynamically closed.

The script also computes the coarsest Gamma-stable refinement of aggregate
fibers by finite partition refinement. This quotient is relative to the
declared (S, A, Gamma) family; it is not a universal physical state.

Python standard library only. All numeric bookkeeping uses Fraction.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Hashable


Aggregate = tuple[Fraction, Fraction]
Descriptor = Hashable


@dataclass(frozen=True)
class Term:
    label: str
    value: Fraction


@dataclass(frozen=True)
class State:
    name: str
    q_terms: tuple[Term, ...]
    r_terms: tuple[Term, ...]
    outgoing_cause: tuple[str, ...]


def build_family() -> tuple[dict[str, State], dict[str, str]]:
    regular = ("REGULAR_VALUE_OR_FIELD_CHANGE",)
    none: tuple[str, ...] = ()

    states = {
        "s_pm": State(
            "s_pm",
            (Term("q_plus", Fraction(1)), Term("q_minus", Fraction(-1))),
            (Term("r_fixed", Fraction(2)),),
            regular,
        ),
        "s_uv": State(
            "s_uv",
            (Term("q_u", Fraction(2)), Term("q_v", Fraction(-2))),
            (Term("r_fixed", Fraction(2)),),
            regular,
        ),
        "s_alt": State(
            "s_alt",
            (Term("q_a", Fraction(1)), Term("q_b", Fraction(-1))),
            (Term("r_fixed", Fraction(2)),),
            regular,
        ),
        "s_zero": State(
            "s_zero",
            (Term("q_zero", Fraction(0)),),
            (Term("r_fixed", Fraction(2)),),
            regular,
        ),
        "h": State(
            "h",
            (Term("q_high", Fraction(2)),),
            (Term("r_fixed", Fraction(2)),),
            none,
        ),
        "l": State(
            "l",
            (Term("q_zero", Fraction(0)),),
            (Term("r_fixed", Fraction(2)),),
            none,
        ),
    }

    gamma = {
        "s_pm": "h",
        "s_uv": "h",
        "s_alt": "l",
        "s_zero": "l",
        "h": "h",
        "l": "l",
    }
    return states, gamma


def aggregate(state: State) -> Aggregate:
    return (
        sum((term.value for term in state.q_terms), Fraction(0)),
        sum((term.value for term in state.r_terms), Fraction(0)),
    )


def q_term_count(state: State) -> int:
    return len(state.q_terms)


def outgoing_cause_signature(state: State) -> tuple[str, ...]:
    return state.outgoing_cause


ACTIVE_SUPPORT_LABELS = frozenset({"q_plus", "q_u", "q_high"})


def active_support_bit(state: State) -> int:
    return int(any(term.label in ACTIVE_SUPPORT_LABELS for term in state.q_terms))


def transition(state: State, states: dict[str, State], gamma: dict[str, str]) -> State:
    return states[gamma[state.name]]


def reduced_descriptor(
    state: State,
    eta: Callable[[State], Hashable] | None = None,
) -> Descriptor:
    a = aggregate(state)
    if eta is None:
        return a
    return (a, eta(state))


def closure_failures(
    states: dict[str, State],
    gamma: dict[str, str],
    eta: Callable[[State], Hashable] | None = None,
) -> list[tuple[Descriptor, tuple[str, ...], tuple[Descriptor, ...]]]:
    groups: defaultdict[Descriptor, list[State]] = defaultdict(list)
    for state in states.values():
        groups[reduced_descriptor(state, eta)].append(state)

    failures = []
    for source_descriptor, group in groups.items():
        outputs = {
            reduced_descriptor(transition(state, states, gamma), eta)
            for state in group
        }
        if len(outputs) > 1:
            failures.append(
                (
                    source_descriptor,
                    tuple(sorted(state.name for state in group)),
                    tuple(sorted(outputs, key=repr)),
                )
            )
    return sorted(failures, key=repr)


def closure_holds(
    states: dict[str, State],
    gamma: dict[str, str],
    eta: Callable[[State], Hashable] | None = None,
) -> bool:
    return not closure_failures(states, gamma, eta)


def canonicalize(signatures: dict[str, Hashable]) -> dict[str, int]:
    classes: dict[Hashable, int] = {}
    result: dict[str, int] = {}
    next_id = 0

    for name in sorted(signatures):
        signature = signatures[name]
        if signature not in classes:
            classes[signature] = next_id
            next_id += 1
        result[name] = classes[signature]

    return result


def partition_groups(class_map: dict[str, int]) -> tuple[tuple[str, ...], ...]:
    grouped: defaultdict[int, list[str]] = defaultdict(list)
    for name, class_id in class_map.items():
        grouped[class_id].append(name)
    return tuple(
        sorted(
            (tuple(sorted(names)) for names in grouped.values()),
            key=repr,
        )
    )


def stable_dynamic_partition(
    states: dict[str, State],
    gamma: dict[str, str],
) -> list[dict[str, int]]:
    current = canonicalize(
        {name: aggregate(state) for name, state in states.items()}
    )
    history = [current.copy()]

    while True:
        signatures = {
            name: (aggregate(states[name]), current[gamma[name]])
            for name in states
        }
        refined = canonicalize(signatures)
        history.append(refined.copy())

        if all(refined[name] == current[name] for name in states):
            return history

        current = refined


def descriptor_partition(
    states: dict[str, State],
    eta: Callable[[State], Hashable] | None,
) -> tuple[tuple[str, ...], ...]:
    grouped: defaultdict[Descriptor, list[str]] = defaultdict(list)
    for state in states.values():
        grouped[reduced_descriptor(state, eta)].append(state.name)
    return tuple(
        sorted(
            (tuple(sorted(names)) for names in grouped.values()),
            key=repr,
        )
    )


def run_candidates() -> None:
    states, gamma = build_family()

    candidates = (
        ("aggregate_only", None),
        ("aggregate_plus_cause_signature", outgoing_cause_signature),
        ("aggregate_plus_q_term_count", q_term_count),
        ("aggregate_plus_active_support_bit", active_support_bit),
    )

    print("CANDIDATE CLOSURE TESTS")
    for label, eta in candidates:
        print(f"{label}: closure={closure_holds(states, gamma, eta)}")
        failures = closure_failures(states, gamma, eta)
        for source, names, outputs in failures:
            print(f"  source={source}")
            print(f"  states={names}")
            print(f"  future_descriptors={outputs}")

    print("ACTIVE-SUPPORT POSITIVE CONTROL")
    for name in sorted(states):
        state = states[name]
        nxt = transition(state, states, gamma)
        print(
            f"{name:7s}: "
            f"{reduced_descriptor(state, active_support_bit)} -> "
            f"{reduced_descriptor(nxt, active_support_bit)}"
        )


def run_partition() -> None:
    states, gamma = build_family()
    history = stable_dynamic_partition(states, gamma)

    print("DYNAMIC PARTITION REFINEMENT")
    for step, class_map in enumerate(history):
        print(f"P{step}: {partition_groups(class_map)}")

    stable = partition_groups(history[-1])
    active = descriptor_partition(states, active_support_bit)

    print(f"stable_dynamic_partition={stable}")
    print(f"aggregate_plus_active_support_partition={active}")
    print(f"partitions_match={stable == active}")


def run_histories() -> None:
    states, gamma = build_family()

    print("AGGREGATE OUTPUT HISTORIES")
    for name in sorted(states):
        current = states[name]
        history = []
        for _ in range(4):
            history.append(aggregate(current))
            current = transition(current, states, gamma)
        print(f"{name:7s}: {tuple(history)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("candidates", "partition", "histories", "all"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("candidates", "all"):
        run_candidates()
    if args.mode in ("partition", "all"):
        run_partition()
    if args.mode in ("histories", "all"):
        run_histories()


if __name__ == "__main__":
    main()
