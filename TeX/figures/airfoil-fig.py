import aerosandbox as asb
import aerosandbox.numpy as np

a = asb.Airfoil("dae11").repanel(20)

from aerosandbox.tools.pretty_plots import plt, sns, mpl, show_plot

color = "#64ACBE"

fig, ax = plt.subplots(figsize=(4, 2))
plt.plot(a.x(), a.y(), ".-", zorder=11, color=color)
plt.fill(a.x(), a.y(), zorder=10, color=color, alpha=0.2)
plt.axis('equal')
from matplotlib import ticker

ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=0.1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(base=0.1))
show_plot(
    title="DAE11 Airfoil",
    xlabel="$x/c$",
    ylabel="$y/c$",
    show=False
)
plt.savefig(r"C:\Users\User\Dropbox (MIT)\School\Grad School\2021 Spring\Thesis\TeX\figures\airfoil-fig.pgf")
plt.show()
