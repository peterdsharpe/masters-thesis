"""
An illustration of the various types of norms that can be used during function regression, and what they look like.
"""

import aerosandbox as asb
import aerosandbox.numpy as np
from aerosandbox.tools.pretty_plots import plt, sns, mpl, show_plot, set_ticks, palettes
from dataset_temperature import time, measured_temperature


def model(x, p):
    return p["1"] * x + p["0"]  # Linear regression


def fit_model_with_norm(residual_norm_type):
    return asb.FittedModel(
        model=model,
        x_data=time,
        y_data=measured_temperature,
        parameter_guesses={
            "1": 0,
            "0": 0,
        },
        residual_norm_type=residual_norm_type,
        verbose=False
    )


L1_model = fit_model_with_norm("L1")
L2_model = fit_model_with_norm("L2")
LInf_model = fit_model_with_norm("LInf")

x = np.linspace(0, 100)

fig, ax = plt.subplots(figsize=(5, 4))
plt.plot(time, measured_temperature, ".k", label="Data")

fits = []

for sn, ln in zip(
        ["L1", "L2", "LInf"],
        ["$L_1$", "$L_2$", "$L_\infty$"]
):
    fit = fit_model_with_norm(sn)
    fits.append(fit)

    plt.plot(
        x,
        fit(x),
        # label=f"{ln} Fit",
        alpha=0.8
    )

c = mpl.colors.ColorConverter()


def darken(color, frac):
    ncolor = c.to_rgba_array(color).flatten()
    return (1 - frac) * np.array(ncolor) + frac * np.array([0, 0, 0, 1])


def text(lineid, s, x, offset=12, **kwargs):
    y = fits[lineid](x) + offset

    dydx = (fits[lineid](x + 10) - fits[lineid](x)) / 10
    yxscale = 4.55
    angle = np.arctan(dydx / yxscale) * 180 / np.pi
    plt.text(
        x, y, s,
        rotation=angle,
        color=darken(palettes["categorical"][lineid], 0.1),

        alpha=0.9,
        fontsize=10,
        **kwargs
    )


text(0, "$L_1$ fit (best outlier rejection)", 2)
text(1, "$L_2$ fit (least-squares)", 4, offset=-17)
text(2, "$L_\infty$ fit (minimizes peak error)", 2)

set_ticks(
    10, 5, 50, 25
)
plt.subplots_adjust(
    top=0.93,
    bottom=0.13,
    left=0.15,
    right=0.98
)
plt.xlim(0, 100)
plt.ylim(-100, 250)
show_plot(
    r"Impact of Norm Choice for Outlier Treatment",
    r"$x$",
    r"$f(x)$",
    tight_layout=False,
    legend=False,
    show=False
)
plt.savefig(r"C:\Users\User\Dropbox (MIT)\School\Grad School\2021 Spring\Thesis\TeX\figures\fitting-norm.pgf")
plt.show()