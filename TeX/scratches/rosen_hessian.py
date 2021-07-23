def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

import sympy as s

x, y, lamb = s.symbols("x y lambda")

f = rosenbrock(x, y)

g = x ** 2 + y ** 2 - 1

gradf = s.Matrix([s.diff(f, x), s.diff(f, y)])
gradg = s.Matrix([s.diff(g, x), s.diff(g, y)])

hess = s.hessian(f, [x, y])

import numpy as np
hess_opt = np.array(hess.subs(x, 0).subs(y, 1), "f8")

vals, vecs = np.linalg.eig(hess_opt)

# print(vals)

# print(np.linalg.cond(hess_opt))

lagrangian = gradf + lamb * gradg

ans = s.nsolve(
    [*lagrangian, g],
    [x, y, lamb],
    [1,2,3]
)
xo, yo, lambo = ans

hesso = hess.subs(x, xo).subs(y, yo).subs(lamb, lambo)

np.linalg.cond(np.array(hesso,float))