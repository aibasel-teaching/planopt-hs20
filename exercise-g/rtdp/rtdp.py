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
    # TODO: add your code here.
    # Return a float (even though heuristic values are integers).


"""
Compute the Q-value for state s and action under the given values.
"""
def compute_q_value(inst, s, action, values):
    # TODO: add your code here.
    # The goal state has Q-value of 0.
    # Return a float.


"""
Compute the greedy action in state s under the given values (None if s is a
goal state) and also return the resulting Q-value of that best action in s.
"""
def compute_greedy_action_and_value(inst, s, values):
    # TODO: add your code here.
    # Make use of compute_q_value to compute Q-values.
    # Return a pair of best action and its Q-value.
    # For the goal state, return no action and 0.


"""
Compute a mapping from states to actions that represents the greedy policy.
"""
def get_greedy_policy(inst, values):
    # TODO: add your code here.
    # Make use of compute_greedy_action_and_value to compute the best action
    # for each state.
    # Return a dictionary from states to strings, where ' ' denotes no action,
    # and otherwise, the action is indicated by 'N', 'E', 'S', or 'W'.


"""
Sample a successor state of state s applying action best_a.
"""
def sample_successor(inst, s, best_a):
    # TODO: add your code here.
    # Return a state - either s or the successor if applying best_a succeeded.

    # Note: get_successors of Instance either returns a single successor in
    # which case we have to pick it (its probability is 1), or it returns
    # exactly two successors and the first one is the same state as the given
    # one. We can therefore, with probability of transitioning to the second
    # state, sample this second state, and otherewise just return the given
    # state.


"""
Compute an RTDP trial: starting from the initial state, repeatedly compute
the best available action, update the value of the current state according
to this action, and sample a successor from applying this action. Set the
state to the successor and repated while not reaching a goal state.
"""
def perform_trial(inst, values):
    # TODO: add your code here.
    # Make use of compute_greedy_action_and_value and sample_successor
    # Return updated value function values.


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
    # TODO: add your code here.
    # Make use of compute_greedy_action_and_value.
    # Return a float.


"""
Compute the residual of all states reachable under the greedy policy. If the
residual is smaller than some epsilon for all reachable states, then mark them
as solved. Otherwise, update their values.
"""
def check_solved(inst, given_s, solved, values):
    assert given_s != inst.goal
    # TODO: add your code here.
    # Make use of compute_greedy_action_and_value.
    # Return updated labeling solved and updated value function values.


"""
Compute the best available action, update the value of the current state
according to this action, and sample a successor from applying this action
(this mimics trial of RTDP). Recursively visit the sampled successor and
after returning from recursion, call check_solved on originally given state s.
"""
def visit(inst, s, solved, values):
    # TODO: add your code here.
    # Make use of compute_greedy_action_and_value, sample_successor, and
    # check_solved.
    # Return updated labeling solved and updated value function values.


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
