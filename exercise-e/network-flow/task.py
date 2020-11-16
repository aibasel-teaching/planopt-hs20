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
    variables=[a, b, c]
    operators = [
        Operator("o1",  preconditions={a: 1            }, effects={a: 2            }, cost=1),
        Operator("o2",  preconditions={a: 2, b: 1      }, effects={a: 1, b: 3      }, cost=1),
        Operator("o3",  preconditions={      b: 4, c: 1}, effects={      b: 2, c: 2}, cost=1),
        Operator("o4",  preconditions={      b: 3      }, effects={      b: 4      }, cost=1),
        Operator("o5",  preconditions={      b: 2      }, effects={      b: 4      }, cost=1),
        Operator("o6",  preconditions={      b: 4      }, effects={      b: 3      }, cost=1),
        Operator("o7",  preconditions={      b: 3, c: 2}, effects={      b: 6, c: 4}, cost=1),
        Operator("o8",  preconditions={a: 2, b: 3      }, effects={a: 3, b: 5      }, cost=1),
        Operator("o9",  preconditions={a: 2,       c: 2}, effects={a: 4,       c: 3}, cost=1),
        Operator("o10", preconditions={            c: 4}, effects={            c: 2}, cost=1),
        Operator("o11", preconditions={a: 3, b: 5, c: 4}, effects={a: 5, b: 7, c: 5}, cost=1),
        Operator("o12", preconditions={a: 4, b: 6, c: 3}, effects={a: 5, b: 7, c: 5}, cost=1),
    ]
    init = {a: 1, b: 1, c: 1}
    goal = {a: 5, b: 7, c: 5}
    return Task(variables=variables, operators=operators, init=init, goal=goal)


