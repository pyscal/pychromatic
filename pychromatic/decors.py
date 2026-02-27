"""
Decorators for auto-styling matplotlib plots.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from cycler import cycler

import pychromatic.colors as colorlist


def chromatify(add_subplot: Callable) -> Callable:
    """
    Decorator that auto-applies opinionated matplotlib styling to subplot functions.

    The decorated function should return a matplotlib Axes object.
    """

    def modify_plot(*args: Any, **kwargs: Any) -> Any:
        """Apply chromatify styling to the subplot."""
        # Process def args

        labelsize = kwargs.get("labelsize", 12)
        color = kwargs.get("color", "#37474F")
        colors = kwargs.get("colors", colorlist.color_palettes["set6"]["colors"])
        xlabel = kwargs.get("xlabel", "ax.set_xlabel()")
        ylabel = kwargs.get("ylabel", "ax.set_ylabel()")
        labelfont = kwargs.get("labelfont", 12)

        # Params and splines
        ax = add_subplot(*args, **kwargs)
        ax.tick_params(
            which="major",
            length=0,
            width=1,
            direction="in",
            bottom=True,
            top=False,
            right=False,
            color=color,
            labelsize=labelsize,
        )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_color("#37474F")
        ax.spines["left"].set_color("#37474F")

        ax.xaxis.label.set_color("#37474F")
        ax.yaxis.label.set_color("#37474F")
        # Change custom plot colors
        custom_cycler = cycler(color=colors)
        ax.set_prop_cycle(custom_cycler)

        # labels
        ax.set_xlabel(xlabel, fontsize=labelfont)
        ax.set_ylabel(ylabel, fontsize=labelfont)

        return ax

    return modify_plot
