import aerosandbox as asb
import aerosandbox.numpy as np

N = 5000

opti = asb.Opti()

x = opti.variable(init_guess=4 * np.ones(shape=N))

x1 = x[:-1]
x2 = x[1:]

f = np.sum(100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2)

opti.minimize(f)

sol = opti.solve()
