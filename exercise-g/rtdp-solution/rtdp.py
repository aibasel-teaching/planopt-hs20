#! /usr/bin/env python3

import argparse
import copy
import random
import sys

import instance
from utils import print_values, print_solved, print_policy, wait_for_input


EPSILON = 0.0001


"""
Compute a the Manhattan distance for a state of the example instance, except
for state (2, 3), which is hard-coded to have heuristic value 4.
"""
def heuristic(inst, s):
    # This is a cheat that only works for the specific instance, not for
    # arbitrary cost structure
    if s.x == 2 and s.y == 3:
        return 4.0
    return (inst.width-1-s.x) + (inst.height-1-s.y)


"""
Compute the Q-value for state s and action under the given values.
"""
def compute_q_value(inst, s, action, values):
    if s == inst.goal:
        return 0.0

    assert inst.action_is_applicable(s, action)
    res = inst.costs[s]
    succs = inst.get_successors(s, action)
    for (succ, prob) in succs:
        res += values[succ] * prob
    return res


"""
Compute the greedy action in state s under the given values (None if s is a
goal state) and also return the resulting Q-value of that best action in s.
"""
def compute_greedy_action_and_value(inst, s, values):
    if s == inst.goal:
        return None, 0.0

    min_q = float('inf')
    best_a = None
    for a in inst.get_applicable_actions(s):
        q_val = compute_q_value(inst, s, a, values)
        if q_val < min_q:
            best_a = a
            min_q = q_val
    assert best_a is not None
    return best_a, min_q


"""
Compute a mapping from states to actions that represents the greedy policy.
"""
def get_greedy_policy(inst, values):
    greedy_policy = { s :' ' for s in inst.states }
    for s in inst.states:
        best_a, min_q = compute_greedy_action_and_value(inst, s, values)
        if best_a is None:
            assert s == inst.goal
        else:
            assert inst.action_is_applicable(s, best_a)
            greedy_policy[s] = best_a
    return greedy_policy


"""
Sample a successor state of state s applying action best_a.
"""
def sample_successor(inst, s, best_a):
    succs = inst.get_successors(s, best_a)
    if len(succs) == 1:
        succ, prob = succs[0]
        assert prob == 1.0
        return succ
    else:
        assert len(succs) == 2
        assert succs[0][0] == s
        # There are two successors and we know that the first one is the same
        # state as the current one. We can therefore, with probability of
        # transitioning to the second state, sample this second state, and
        # otherewise just return the previous state.
        succ, prob = succs[1]
        if random.random() <= prob:
            return succ
        else:
            return s


"""
Compute an RTDP trial: starting from the initial state, repeatedly compute
the best available action, update the value of the current state according
to this action, and sample a successor from applying this action. Set the
state to the successor and repated while not reaching a goal state.
"""
def perform_trial(inst, values):
    s = inst.init
    while s != inst.goal:
        best_a, min_q = compute_greedy_action_and_value(inst, s, values)
        values[s] = min_q
        s = sample_successor(inst, s, best_a)
    return values


"""
For two dicts with the same keys, compute the maximum difference of values.
"""
def compute_max_difference(values, other_values):
    assert values.keys() == other_values.keys()
    return max([abs(values[s] - other_values[s]) for s in values.keys()])


"""
Run the RTDP algorithm until the change in values is below some epsilon.
"""
def rtdp(inst, values):
    iteration = 1
    while True:
        wait_for_input("Press enter for another iteration of RTDP...")
        old_values = dict(values)
        values = perform_trial(inst, values)

        print("Values after iteration {}: ".format(iteration))
        print_values(inst, values)

        change = compute_max_difference(old_values, values)
        if change < EPSILON:
            print("Converged in iteration {}".format(iteration))
            break
        iteration += 1
    return values


"""
Compute the residual of state s under the given values: it is 0 if s is a goal
state and it is the difference to the Q-value of the greedy action in a
otherwise.
"""
def residual(inst, s, values):
    if s == inst.goal:
        return 0.0

    best_a, min_q = compute_greedy_action_and_value(inst, s, values)

    return abs(values[s] - min_q)


"""
Compute the residual of all states reachable under the greedy policy. If the
residual is smaller than some epsilon for all reachable states, then mark them
as solved. Otherwise, update their values.
"""
def check_solved(inst, given_s, solved, values):
    assert given_s != inst.goal

    all_solved = True
    open_list = []
    closed = []

    if not solved[given_s]:
        open_list.append(given_s)
    while len(open_list):
        s = open_list.pop()
        closed.append(s)
        if residual(inst, s, values) > EPSILON:
            all_solved = False
        else:
            # TODO: this does not match the algorithm!
            if s == inst.goal:
                continue
            best_a, min_q = compute_greedy_action_and_value(inst, s, values)

            succs = inst.get_successors(s, best_a)
            for succ, prob in succs:
                if not solved[succ] and succ not in open_list and succ not in closed:
                    open_list.append(succ)

    if all_solved:
        for s in closed:
            solved[s] = True
    else:
        for s in closed:
            best_a, min_q = compute_greedy_action_and_value(inst, s, values)
            values[s] = min_q
    return (solved, values)


"""
Compute the best available action, update the value of the current state
according to this action, and sample a successor from applying this action
(this mimics trial of RTDP). Recursively visit the sampled successor and
after returning from recursion, call check_solved on originally given state s.
"""
def visit(inst, s, solved, values):
    if solved[s] or s == inst.goal:
        return (solved, values)

    best_a, min_q = compute_greedy_action_and_value(inst, s, values)
    values[s] = min_q
    sprime = sample_successor(inst, s, best_a)
    solved, values = visit(inst, sprime, solved, values)
    solved, values = check_solved(inst, s, solved, values)
    return (solved, values)


"""
Run the LRTDP algorithm until it converges.
"""
def lrtdp(inst, values):
    solved = { s: False for s in inst.states }
    iteration = 1
    while not solved[inst.init]:
        wait_for_input("Press enter for another iteration of LRTDP...".format(iteration))
        solved, values = visit(inst, inst.init, solved, values)
        print("Values after iteration {}: ".format(iteration))
        print_values(inst, values)
        print("Solved after iteration {}: ".format(iteration))
        print_solved(inst, solved)
        iteration += 1
    return values


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'algorithm', choices=['rtdp', 'lrtdp'],
        help="Choose the algorithm."
    )
    args = parser.parse_args()

    inst = instance.get_example_instance()
    print(inst)

    values = { s : heuristic(inst, s) for s in inst.states }

    print("")
    print("Initial state-values:")
    print_values(inst, values)

    if args.algorithm == 'rtdp':
        values = rtdp(inst, values)
    elif args.algorithm == 'lrtdp':
        values = lrtdp(inst, values)
    else:
        sys.exit("Unknown algorithm")
    print("")

    print("Final values:")
    print_values(inst, values)

    policy = get_greedy_policy(inst, values)
    print("Corresponding final policy:")
    print_policy(inst, policy)
