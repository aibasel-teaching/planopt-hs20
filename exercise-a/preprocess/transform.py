#!/usr/bin/env python

import sys, os
from collections import defaultdict

from parser import parse_domain_file
from pddl_types import *
from pddl_printer import save_domain, generate_effect_pddl

# Use TRUE_CONDITION to represent "T" and FALSE_CONDITION for "F".

def simplify_condition(condition):
    """
    returns a condition that is equivalent to the given condition but
    does not contain constants TRUE_CONDITION or FALSE_CONDITION.
    """
    # TODO: add your code here.
    raise NotImplementedError


def get_effcond(literal, effect):
    """
    returns the condition under which the given effect sets the given
    literal in the successor state.
    """
    # TODO: add your code here.
    raise NotImplementedError


def transform_effect(effect, variables):
    """
    returns a new effect that is equivalent to the given effect and in
    conflict-free effect normal form.
    """
    # TODO: add your code here.
    raise NotImplementedError


def transform_action(action, variables):
    transformed_action = Action(action.name)
    transformed_action.parameters = action.parameters
    transformed_action.precondition = action.precondition
    transformed_action.effect = transform_effect(action.effect, variables)
#   We only verify that the given effect is in effect normal form and
#   omit the coNP-hard check that it is also conflict-free.
    verify_effect_normal_form(transformed_action.effect)
    return transformed_action


def transform_domain(domain):
    for p in domain.predicates:
        if len(p) > 1:
            print("The domain has predicates with parameters. Please "
                "run ground.py first to get a grounded domain and then "
                "call transform.py on the generated pddl file.")
            sys.exit(1)
    transformed_domain = Domain()
    transformed_domain.name = domain.name
    transformed_domain.requirements = domain.requirements
    transformed_domain.predicates = domain.predicates
    for action in domain.actions:
        transformed_domain.actions.append(transform_action(action, domain.predicates))
    return transformed_domain


def verify_effect_normal_form(effect):
    def fail(msg):
        print >> sys.stderr, msg
        print >> sys.stderr, "First violating effect: "
        for line in generate_effect_pddl(effect, indent=0):
            print >> sys.stderr, line
        sys.exit(1)

    atomic_effects = set()
    if isinstance(effect, ConjunctiveEffect):
        for c in effect.conjuncts:
            if not isinstance(c, ConditionalEffect):
                fail("The effect is a conjunctive effect but at least "
                    "one of its conjuncts is not a conditional effect. "
                    "(Type of conjunct %s)" % type(c).__name__)
        for c in effect.conjuncts:
            if not isinstance(c.subeffect, (AtomicEffect, NegatedAtomicEffect)):
                fail("The effect is a conjunctive effect with only "
                    "conditional effects as conjuncts but one of the "
                    "conditional effect has a subeffect which is not "
                    "atomic. (Type of subeffect %s)" % type(c.subeffect).__name__)
        for c in effect.conjuncts:
            if c.subeffect in atomic_effects:
                fail("The effect is a conjunctive effect with only "
                    "conditional effects as conjuncts which have atomic "
                    "subeffects. However, a subeffect occurs more than "
                    "once.")
            atomic_effects.add(c.subeffect)
    elif isinstance(effect, ConditionalEffect):
        if not isinstance(effect.subeffect, (AtomicEffect, NegatedAtomicEffect)):
            fail("The effect is a conditional effect but its subeffect "
                "is not atomic. (Type of subeffect %s)" % type(effect.subeffect).__name__)
    else:
        fail("The effect is not in effect normal form because it is "
            "neither a conjunctive effect nor a conditional effect. "
            "(Type of effect %s)" % type(effect.subeffect).__name__)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "expected domain filename as the only parameter."
        sys.exit(1)
    domain_filename = sys.argv[1]
    domain = parse_domain_file(domain_filename)
    transformed_domain = transform_domain(domain)

    domain_path, domain_ext = os.path.splitext(domain_filename)
    transformed_domain_filename = domain_path + "_normalized" + domain_ext
    save_domain(transformed_domain, transformed_domain_filename)
