#!/usr/bin/env python3

class Operator(object):
    def __init__(self, name, preconditions, effects, cost):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects
        self.cost = cost

class Task(object):
    def __init__(self, variables, operators, init, goal):
        self.variables = variables
        self.operators = operators
        self.init = init
        self.goal = goal

def create_example_task():
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    variables=[a, b, c, d]
    operators = [
        Operator("o_1",  preconditions={a: 2, b: 1, c: 1      }, effects={a: 1, b: 2, c: 3      }, cost=3),
        Operator("o_2",  preconditions={a: 1                  }, effects={a: 2                  }, cost=5),
        Operator("o_3",  preconditions={      b: 1,       d: 1}, effects={      b: 2,       d: 2}, cost=3),
        Operator("o_4",  preconditions={            c: 1, d: 1}, effects={            c: 2, d: 3}, cost=3),
        Operator("o_5",  preconditions={            c: 2, d: 3}, effects={            c: 1, d: 4}, cost=1),
        Operator("o_6",  preconditions={            c: 2, d: 2}, effects={            c: 3, d: 4}, cost=1),
    ]
    init = {a: 1, b: 1, c: 1, d: 1}
    goal = {      b: 2, c: 3, d: 4}
    return Task(variables=variables, operators=operators, init=init, goal=goal)


