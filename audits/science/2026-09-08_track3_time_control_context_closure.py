#!/usr/bin/env python3
"""
Track-3 time/control-context closure and robust sufficient-state refinement.

Purpose
-------
Extend the previous autonomous reduced-dynamics closure gate from one supplied
transition Gamma:S->S to a finite family {Gamma_c}_{c in C} of explicitly
supplied control/context-dependent transitions.

The script demonstrates:
1. the same reduced state can evolve differently under different supplied
   transition contexts;
2. aggregate + context is still insufficient when one context splits an
   aggregate fiber;
3. an explicitly retained active-support role bit closes the controlled
   reduced dynamics on the declared finite family;
4. robust partition refinement across all allowed contexts recovers the same
   coarsest control-closed partition;
5. a restricted control family may admit a coarser reduced state.

All numerical values are exact Fractions and bookkeeping-only.
Python standard library only.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Hashable, Iterable


Aggregate = tuple[Fraction, Fraction]
Descriptor = tuple[Aggregate, int]


@dataclass(frozen=True)
class Term:
    label: str
    value: Fraction


@dataclass(frozen=True)
class TypedState:
    name: str
    q_terms: tuple[Term, ...]
    r_terms: tuple[Term, ...]


def aggregate(state: TypedState) -> Aggregate:
    return (
        sum((term.value for term in state.q_terms), Fraction(0)),
        sum((term.value for term in state.r_terms), Fraction(0)),
    )


def build_states() -> dict[str, TypedState]:
    r_fixed = (Term("r_fixed", Fraction(2)),)
    return {
        "h": TypedState(
            "h",
            (Term("q_high", Fraction(2)),),
            r_fixed,
        ),
        "l": TypedState(
            "l",
            (Term("q_zero", Fraction(0)),),
            r_fixed,
        ),
        "s_pm": TypedState(
            "s_pm",
            (
                Term("q_plus", Fraction(1)),
                Term("q_minus", Fraction(-1)),
            ),
            r_fixed,
        ),
        "s_uv": TypedState(
            "s_uv",
            (
                Term("q_u", Fraction(2)),
                Term("q_v", Fraction(-2)),
            ),
            r_fixed,
        ),
        "s_alt": TypedState(
            "s_alt",
            (
                Term("q_a", Fraction(1)),
                Term("q_b", Fraction(-1)),
            ),
            r_fixed,
        ),
        "s_zero": TypedState(
            "s_zero",
            (Term("q_zero", Fraction(0)),),
            r_fixed,
        ),
    }


TRANSITIONS: dict[str, dict[str, str]] = {
    "probe": {
        "h": "h",
        "l": "l",
        "s_pm": "h",
        "s_uv": "h",
        "s_alt": "l",
        "s_zero": "l",
    },
    "reset": {
        "h": "h",
        "l": "l",
        "s_pm": "l",
        "s_uv": "l",
        "s_alt": "l",
        "s_zero": "l",
    },
}


ACTIVE_SUPPORT_LABELS = {"q_plus", "q_u", "q_high"}


def gamma(
    state: TypedState,
    context: str,
    states: dict[str, TypedState],
) -> TypedState:
    return states[TRANSITIONS[context][state.name]]


def active_support_bit(state: TypedState) -> int:
    return int(
        any(term.label in ACTIVE_SUPPORT_LABELS for term in state.q_terms)
    )


def augmented_descriptor(state: TypedState) -> Descriptor:
    return (aggregate(state), active_support_bit(state))


def output_classes(
    states: Iterable[TypedState],
    readout: Callable[[TypedState], Hashable],
    context: str,
    state_table: dict[str, TypedState],
) -> dict[Hashable, set[Hashable]]:
    grouped: defaultdict[Hashable, set[Hashable]] = defaultdict(set)
    for state in states:
        grouped[readout(state)].add(
            readout(gamma(state, context, state_table))
        )
    return dict(grouped)


def closure_holds_for_context(
    states: Iterable[TypedState],
    readout: Callable[[TypedState], Hashable],
    context: str,
    state_table: dict[str, TypedState],
) -> bool:
    return all(
        len(outputs) == 1
        for outputs in output_classes(
            states, readout, context, state_table
        ).values()
    )


def controlled_closure_holds(
    states: Iterable[TypedState],
    readout: Callable[[TypedState], Hashable],
    contexts: Iterable[str],
    state_table: dict[str, TypedState],
) -> bool:
    return all(
        closure_holds_for_context(
            states, readout, context, state_table
        )
        for context in contexts
    )


def canonical_partition(
    signatures: dict[str, Hashable],
) -> dict[str, int]:
    label_for_signature: dict[Hashable, int] = {}
    partition: dict[str, int] = {}
    next_label = 0

    for name in sorted(signatures):
        signature = signatures[name]
        if signature not in label_for_signature:
            label_for_signature[signature] = next_label
            next_label += 1
        partition[name] = label_for_signature[signature]

    return partition


def robust_partition_refinement(
    state_table: dict[str, TypedState],
    contexts: tuple[str, ...],
) -> list[dict[str, int]]:
    states = tuple(state_table.values())
    partition = canonical_partition(
        {state.name: aggregate(state) for state in states}
    )
    history = [partition]

    while True:
        signatures: dict[str, Hashable] = {}
        for state in states:
            future_classes = tuple(
                (
                    context,
                    partition[
                        gamma(state, context, state_table).name
                    ],
                )
                for context in contexts
            )
            signatures[state.name] = (
                aggregate(state),
                future_classes,
            )

        refined = canonical_partition(signatures)
        history.append(refined)
        if refined == partition:
            return history
        partition = refined


def partition_classes(
    partition: dict[str, int],
) -> list[tuple[str, ...]]:
    classes: defaultdict[int, list[str]] = defaultdict(list)
    for name, label in partition.items():
        classes[label].append(name)
    return [
        tuple(sorted(names))
        for _, names in sorted(classes.items())
    ]


def run_context_witness() -> None:
    states = build_states()
    source = states["s_pm"]

    probe_future = aggregate(gamma(source, "probe", states))
    reset_future = aggregate(gamma(source, "reset", states))

    print("TIME/CONTROL-CONTEXT WITNESS")
    print(f"initial aggregate: {aggregate(source)}")
    print(f"probe future aggregate: {probe_future}")
    print(f"reset future aggregate: {reset_future}")
    print(
        "same reduced state + different supplied context -> "
        f"different future aggregate: {probe_future != reset_future}"
    )


def run_closure_gate() -> None:
    state_table = build_states()
    states = tuple(state_table.values())
    contexts = tuple(sorted(TRANSITIONS))

    print("CONTROLLED CLOSURE GATE")
    for context in contexts:
        print(
            f"aggregate closure under {context}: "
            f"{closure_holds_for_context(states, aggregate, context, state_table)}"
        )
        print(
            f"augmented closure under {context}: "
            f"{closure_holds_for_context(states, augmented_descriptor, context, state_table)}"
        )

    print(
        "aggregate closes for all contexts: "
        f"{controlled_closure_holds(states, aggregate, contexts, state_table)}"
    )
    print(
        "augmented descriptor closes for all contexts: "
        f"{controlled_closure_holds(states, augmented_descriptor, contexts, state_table)}"
    )

    print("AGGREGATE OUTPUT CLASSES")
    for context in contexts:
        for source_key, outputs in sorted(
            output_classes(
                states, aggregate, context, state_table
            ).items(),
            key=str,
        ):
            print(f"{context}: {source_key} -> {sorted(outputs)}")


def run_refinement() -> None:
    state_table = build_states()
    contexts = tuple(sorted(TRANSITIONS))
    history = robust_partition_refinement(state_table, contexts)

    print("ROBUST CONTROL-FAMILY PARTITION REFINEMENT")
    for index, partition in enumerate(history):
        print(f"P{index}: {partition_classes(partition)}")

    stable = history[-1]
    active_partition = canonical_partition(
        {
            state.name: augmented_descriptor(state)
            for state in state_table.values()
        }
    )

    print(
        "stable robust partition equals (A, active_support_bit) partition: "
        f"{stable == active_partition}"
    )

    reset_only = ("reset",)
    reset_history = robust_partition_refinement(
        state_table, reset_only
    )
    print(
        "reset-only stable partition: "
        f"{partition_classes(reset_history[-1])}"
    )
    print(
        "aggregate alone closes for reset-only family: "
        f"{closure_holds_for_context(tuple(state_table.values()), aggregate, 'reset', state_table)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("context", "closure", "refinement", "all"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("context", "all"):
        run_context_witness()
    if args.mode in ("closure", "all"):
        run_closure_gate()
    if args.mode in ("refinement", "all"):
        run_refinement()


if __name__ == "__main__":
    main()
