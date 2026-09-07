#!/usr/bin/env python3
"""
Track-3 aggregate-dynamics closure gate.

Purpose
-------
Test whether a typed product aggregate A:S->U_Q x U_R can carry an autonomous
induced dynamics Gamma_A satisfying A o Gamma = Gamma_A o A.

The script provides:
1. a closure-failure witness: two distinct component-resolved states have the
   same aggregate but evolve to different future aggregates;
2. a positive control: a supplied componentwise scaling transition preserves
   aggregate fibers and induces Gamma_A(q,r)=(2q,r/2).

All numbers are exact Fractions and bookkeeping-only.
Python standard library only.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Iterable


Aggregate = tuple[Fraction, Fraction]


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


def witness_states() -> tuple[TypedState, TypedState]:
    s_pm = TypedState(
        "support_plus_minus",
        (
            Term("q_plus", Fraction(1)),
            Term("q_minus", Fraction(-1)),
        ),
        (Term("r_fixed", Fraction(2)),),
    )
    s_zero = TypedState(
        "support_zero",
        (Term("q_zero", Fraction(0)),),
        (Term("r_fixed", Fraction(2)),),
    )
    return s_pm, s_zero


def gamma_hidden_support(state: TypedState) -> TypedState:
    q_rules = {
        "q_plus": Fraction(2),
        "q_minus": Fraction(0),
        "q_zero": Fraction(0),
    }
    r_rules = {"r_fixed": Fraction(2)}

    return TypedState(
        state.name + "_next_hidden",
        tuple(
            Term(term.label, q_rules.get(term.label, term.value))
            for term in state.q_terms
        ),
        tuple(
            Term(term.label, r_rules.get(term.label, term.value))
            for term in state.r_terms
        ),
    )


def gamma_scaling(state: TypedState) -> TypedState:
    return TypedState(
        state.name + "_next_scaling",
        tuple(Term(term.label, 2 * term.value) for term in state.q_terms),
        tuple(
            Term(term.label, Fraction(1, 2) * term.value)
            for term in state.r_terms
        ),
    )


def gamma_aggregate_scaling(value: Aggregate) -> Aggregate:
    q, r = value
    return (2 * q, Fraction(1, 2) * r)


def closure_classes(
    states: Iterable[TypedState],
    transition: Callable[[TypedState], TypedState],
) -> dict[Aggregate, set[Aggregate]]:
    grouped: defaultdict[Aggregate, set[Aggregate]] = defaultdict(set)
    for state in states:
        grouped[aggregate(state)].add(aggregate(transition(state)))
    return dict(grouped)


def closure_holds_on_family(
    states: Iterable[TypedState],
    transition: Callable[[TypedState], TypedState],
) -> bool:
    return all(
        len(outputs) == 1
        for outputs in closure_classes(states, transition).values()
    )


def run_failure() -> None:
    s1, s2 = witness_states()
    a1 = aggregate(s1)
    a2 = aggregate(s2)
    n1 = aggregate(gamma_hidden_support(s1))
    n2 = aggregate(gamma_hidden_support(s2))

    print("CLOSURE-FAILURE WITNESS")
    print(f"A(s1) = {a1}")
    print(f"A(s2) = {a2}")
    print(f"same initial aggregate: {a1 == a2}")
    print(f"A(Gamma(s1)) = {n1}")
    print(f"A(Gamma(s2)) = {n2}")
    print(f"future aggregates differ: {n1 != n2}")
    print(
        "induced aggregate dynamics exists on witness fiber: "
        f"{closure_holds_on_family((s1, s2), gamma_hidden_support)}"
    )


def run_positive() -> None:
    s1, s2 = witness_states()
    states = (
        s1,
        s2,
        TypedState(
            "extra",
            (
                Term("qa", Fraction(3)),
                Term("qb", Fraction(-1)),
            ),
            (Term("ra", Fraction(4)),),
        ),
    )

    print("POSITIVE CONTROL")
    print(
        "aggregate-fiber closure on finite family: "
        f"{closure_holds_on_family(states, gamma_scaling)}"
    )

    for state in states:
        lhs = aggregate(gamma_scaling(state))
        rhs = gamma_aggregate_scaling(aggregate(state))
        print(
            f"{state.name}: A(Gamma(s))={lhs} "
            f"Gamma_A(A(s))={rhs} commute={lhs == rhs}"
        )


def run_classes() -> None:
    s1, s2 = witness_states()

    print("FIBER OUTPUT CLASSES — FAILURE")
    for source_agg, future_aggs in closure_classes(
        (s1, s2), gamma_hidden_support
    ).items():
        print(f"{source_agg} -> {sorted(future_aggs)}")

    print("FIBER OUTPUT CLASSES — POSITIVE")
    for source_agg, future_aggs in closure_classes(
        (s1, s2), gamma_scaling
    ).items():
        print(f"{source_agg} -> {sorted(future_aggs)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("failure", "positive", "classes", "all"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("failure", "all"):
        run_failure()
    if args.mode in ("positive", "all"):
        run_positive()
    if args.mode in ("classes", "all"):
        run_classes()


if __name__ == "__main__":
    main()
