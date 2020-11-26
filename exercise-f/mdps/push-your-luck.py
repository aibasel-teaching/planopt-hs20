#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import itertools
import operator
import os
from functools import reduce
from pyscipopt import Model


def powerset(iterable):
    """ powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3) """
    s = list(iterable)
    return itertools.chain.from_iterable(
        (frozenset(elem) for elem in itertools.combinations(s, r))
        for r in range(len(s)+1))


_emptyset = frozenset()  # Just for convenience

class PushYourLuckMDP(object):
    """ A push-your-luck MDP with variable discount factor """

    def __init__(self, N, gamma):
        self._die_sides = set(range(1, N + 1))
        self._states = sorted(powerset(self._die_sides))
        self._actions = ["roll", "collect"]
        self._gamma = gamma

    def discount_factor(self):
        return self._gamma

    def states(self):
        return self._states

    def actions(self):
        return self._actions

    def reward(self, s, a):
        # TODO: add your code here
        return 0

    def transitions(self, s, a):
        """ Return a list of pairs (s', p), one pair per each state s'
            such that the probability p of the transition (s, a, s')
            in the MDP is non-zero.
        """
        # TODO: add your code here
        return []

    def state_name(self, s):
        if not s:
            return "empty"
        return "_".join(str(num) for num in sorted(s))

    def variable_name(self, s):
        return "v_" + self.state_name(s)

    def constraint_name(self, s, a):
        return "{}_{}".format(self.state_name(s), a)


def compute_state_values(mdp):
    """Generate LP model for MDP."""
    gamma = mdp.discount_factor()
    model = Model("MDP")

    # Variables
    state_to_var = {s: model.addVar(mdp.variable_name(s)) for s in mdp.states()}

    # Objective function
    # TODO: add your code here

    # Constraints
    # TODO: add your code here

    model.hideOutput()
    model.optimize()
    solution = {s: model.getVal(state_to_var[s]) for s in mdp.states()}
    return solution


def action_values(mdp, state_values, state):
    """Return a list of pairs (q, a) such that q = Q(state, a)"""
    # TODO: add your code here
    return []


def print_solution(mdp, state_values):
    for s in mdp.states():
        _, a = max(action_values(mdp, state_values, s))
        print("{}: {} ({})".format(mdp.variable_name(s), state_values[s], a))


def main(n, gamma):
    mdp = PushYourLuckMDP(n, gamma)
    state_values = compute_state_values(mdp)
    print_solution(mdp, state_values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("N", type=int, default=6)
    parser.add_argument("gamma", type=float, default=0.9)
    args = parser.parse_args()
    main(args.N, args.gamma)
