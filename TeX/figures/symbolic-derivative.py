from aerosandbox.tools.sympy_interactive import *

rho, V, CL, S = s.symbols(r"\rho V C_L S")
f = 0.5 * rho * V ** 2 * CL * S
grad_f = s.Matrix([
    s.diff(f, rho),
    s.diff(f, V),
    s.diff(f, CL),
    s.diff(f, S),
])

print(grad_f.__repr__())
