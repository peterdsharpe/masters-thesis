import aerosandbox as asb
import aerosandbox.numpy as np
from aerosandbox.tools.pretty_plots import plt, sns, mpl, show_plot

fig, ax = plt.subplots()

data = asb.XFoil(
    airfoil=asb.Airfoil("dae11").repanel(50),
    Re=3e5,
).alpha(np.linspace(0, 15, 80))
a = data["alpha"]
cd = data["CD"]

plt.plot(
    a, cd,
    "-",
    alpha=0.8
)

skip=10
asamp, cdsamp = a[::skip], cd[::skip]
plt.plot(
    asamp, cdsamp,
    ".k"
)

im = asb.InterpolatedModel(asamp, cdsamp, method="bspline")
ap = np.linspace(0, 15, 500)
plt.plot(
    ap, im(ap),
    "-",
    alpha=0.8,
)

plt.xlim(0, 15)
plt.ylim(0, 4e-2)
show_plot()
