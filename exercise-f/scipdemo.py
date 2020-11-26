#!/usr/bin/env python3

from pyscipopt import Model

model = Model("Example")
x = model.addVar("x")
y = model.addVar("y")
z = model.addVar("z")

model.setObjective(2*x - 3*y + z, "maximize")
c1 = model.addCons(x + 2*y + z <= 10, name="Some constraint")
model.addCons(x - z <= 0, name="another constraint")

model.hideOutput()
model.optimize()
print(model.getObjVal())
print(model.getVal(x))
print(model.getVal(y))
print(model.getVal(z))

