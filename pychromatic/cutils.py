"""
Color utility functions for converting, mixing, and visualizing colors.
"""

from __future__ import annotations

import colorsys

import matplotlib.colors as mc
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np


def hex_to_rgb(hexval: str) -> list[int]:
    """
    Convert a hex color value to rgb.

    Parameters
    ----------
    hexval : str
        hex color code starting with #

    Returns
    -------
    list[int]
        A list of rgb values between 0-255
    """
    d = hexval.strip("#")
    return [int(d[x : x + 2], 16) for x in range(0, len(d), 2)]


def rgb_to_hex(rgb: list[int | float]) -> str:
    """
    Convert an rgb color value to hex color code.

    Parameters
    ----------
    rgb : list
        a list consisting of three rgb values. It can either be from 0 to 255
        or from 0 to 1.

    Returns
    -------
    str
        the hex code
    """
    # decide if rgbs are floating points between 0 and 1
    if all((val >= 0) and (val <= 1) and isinstance(val, float) for val in rgb):
        rgb = [int(x * 255) for x in rgb]
    if all((val >= 0) and (val <= 255) for val in rgb):
        return f"#{int(rgb[0]):02x}{int(rgb[1]):02x}{int(rgb[2]):02x}"
    else:
        raise ValueError("rgb values should be within 0-255")


def rgb_to_hls(rgbval: list[int]) -> list[float]:
    """
    Convert an rgb value to equivalent hls value.

    Parameters
    ----------
    rgbval : list[int]
        A list of three values containing rgb for the color (0-255)

    Returns
    -------
    list[float]
        A list of hls values
    """
    hue, lit, sat = colorsys.rgb_to_hls(rgbval[0] / 255.0, rgbval[1] / 255.0, rgbval[2] / 255.0)
    return [hue, lit, sat]


def hls_to_rgb(hls: list[float]) -> list[int]:
    """
    Convert hls value to rgb.

    Parameters
    ----------
    hls : list[float]
        A list of hls values

    Returns
    -------
    list[int]
        list of rgb values between 0-255
    """
    rgb = colorsys.hls_to_rgb(hls[0], hls[1], hls[2])
    return [int(x * 255) for x in rgb]


def brighten(color: str, fraction: float = 0.05) -> str:
    """
    Brighten or darken a color.

    Parameters
    ----------
    color : str
        the hex value of input color
    fraction : float
        the amount by which to brighten the color

    Returns
    -------
    str
        the hex value of the modified color

    Notes
    -----
    Colors can also be darkened by providing a negative value for ``fraction``.
    """
    rgbval = hex_to_rgb(color)
    hls = rgb_to_hls(rgbval)

    # adjust luminance (handle zero-luminance / pure-black case)
    if hls[1] == 0 and fraction > 0:
        hls[1] = min(fraction, 1.0)
    else:
        hls[1] = min((1 + fraction) * hls[1], 1)

    rgb = colorsys.hls_to_rgb(hls[0], hls[1], hls[2])
    return rgb_to_hex(rgb)


def mix_colors(color1: str, color2: str, ratio: float = 0.5) -> str:
    """
    Mix two colors to get an intermediate color.

    Parameters
    ----------
    color1 : str
        hex code of the first color
    color2 : str
        hex code of the second color
    ratio : float
        ratio between ``color1`` and ``color2``

    Returns
    -------
    str
        hex code of the intermediate color

    Notes
    -----
    If ``ratio`` is ``r``, then the new color would be r*color1 + (1-r)*color2.
    """
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)

    rgb = [ratio * rgb1[x] + (1 - ratio) * rgb2[x] for x in range(3)]
    return rgb_to_hex(rgb)


def find_intermediate_colors(
    color1: str,
    color2: str,
    colors: int = 1,
    ignore_edges: bool = False,
) -> list[str]:
    """
    Find a given number of intermediate colors between two input colors.

    Parameters
    ----------
    color1 : str
        hex code of the first input color
    color2 : str
        hex code of the second input color
    colors : int, optional
        number of intermediate colors required, default 1
    ignore_edges : bool, optional
        If True, the input colors are not included in the return list.
        Default False.

    Returns
    -------
    list[str]
        list of intermediate hex color codes
    """
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)

    # find intermediate points
    rpoints = np.linspace(rgb1[0], rgb2[0], colors + 2)
    gpoints = np.linspace(rgb1[1], rgb2[1], colors + 2)
    bpoints = np.linspace(rgb1[2], rgb2[2], colors + 2)

    # stack to pairs
    if ignore_edges:
        new_rgbs = np.stack((rpoints[1:-1], gpoints[1:-1], bpoints[1:-1]), axis=-1)
    else:
        new_rgbs = np.stack((rpoints, gpoints, bpoints), axis=-1)

    return [rgb_to_hex(rgb) for rgb in new_rgbs]


def create_colormap(colors: list[str]) -> mc.LinearSegmentedColormap:
    """
    Create a color map from a list of colors.

    Parameters
    ----------
    colors : list[str]
        a list of input hex colors. At least 2 colors are required.

    Returns
    -------
    LinearSegmentedColormap
        the generated colormap
    """
    if len(colors) < 2:
        raise ValueError("length of colors should be at least 2")

    return mc.LinearSegmentedColormap.from_list("", colors)


def get_color(value: float, cmap_name: str = "viridis") -> str:
    """
    Sample a color from a matplotlib colormap at a given position.

    Parameters
    ----------
    value : float
        Position to sample, must be between 0 and 1.
    cmap_name : str, optional
        Name of any matplotlib colormap (default ``'viridis'``).

    Returns
    -------
    str
        Hex color code at the requested position.

    Examples
    --------
    >>> get_color(0.5, "viridis")
    '#21918c'
    """
    if not 0 <= value <= 1:
        raise ValueError(f"value must be between 0 and 1, got {value}")
    cmap = plt.get_cmap(cmap_name)
    rgba = cmap(value)
    return rgb_to_hex([rgba[0], rgba[1], rgba[2]])


def palette_cmap(palette_name: str) -> mc.LinearSegmentedColormap:
    """
    Create a matplotlib colormap from a pychromatic palette.

    Parameters
    ----------
    palette_name : str
        Name of a palette defined in ``pychromatic.colors.color_palettes``.

    Returns
    -------
    LinearSegmentedColormap
        A colormap interpolating through all colors in the palette.

    Examples
    --------
    >>> cmap = palette_cmap("rainbow")
    >>> cmap(0.0)  # first color in RGBA
    (...)
    """
    from pychromatic.colors import color_palettes

    if palette_name not in color_palettes:
        raise KeyError(
            f"Palette '{palette_name}' not found. Available: {', '.join(sorted(color_palettes))}"
        )
    hex_colors = color_palettes[palette_name]["colors"]
    return mc.LinearSegmentedColormap.from_list(palette_name, hex_colors)


def plot_colors(
    colors: list[str],
    minimal: bool = False,
    title: str | None = None,
    scale: float = 1,
) -> None:
    """
    Show plot to illustrate the colors.

    Parameters
    ----------
    colors : list[str]
        list of colors to plot in hex values
    minimal : bool, optional
        if True, plot a minimal bar. Default False.
    title : str or None, optional
        title for the plot
    scale : float, optional
        scale factor for figure size
    """
    if not minimal:
        fig, axs = plt.subplots(1, 3, figsize=(12, 5))
        for count, color in enumerate(colors):
            x = np.arange(11)
            y = np.sin(x / (1.75 * np.pi))
            axs[0].plot(x, y + count / 3.0, color=color, label=color, linewidth=4)
        axs[1].pie(
            (np.random.dirichlet(np.ones(len(colors)), size=1) * 100)[0],
            colors=colors,
            autopct="%1.1f%%",
            startangle=90,
        )
        axs[1].axis("equal")
        axs[1].set_title(title)
        axs[2].bar(
            np.arange(len(colors)),
            np.arange(len(colors)) + 1,
            color=colors,
            linewidth=0,
        )
        axs[2].set_xticks(np.arange(len(colors)) + 0.4)
        plt.show()
    else:
        fig = plt.figure(figsize=[scale * len(colors), scale])
        spec = gridspec.GridSpec(ncols=len(colors), nrows=2, figure=fig)
        for count, color in enumerate(colors):
            ax1 = fig.add_subplot(spec[0, count])
            ax1.fill([0, 1, 1, 0], [0, 0, 1, 1], color=color)
            ax1.set_ylim(0, 1)
            ax1.set_xlim(0, 1)
            plt.axis("off")
            ax2 = fig.add_subplot(spec[1, count])
            ax2.plot([0, 1], [0.25, 0.25], color=color, linewidth=3)
            ax2.set_ylim(0, 0.5)
            ax2.set_xlim(0, 0.5)
            plt.axis("off")
        plt.subplots_adjust(wspace=0, hspace=0)
        plt.show()


# Backward compatibility alias
class Color_utils:
    """Deprecated: Use module-level functions directly instead."""

    def __getattr__(self, name: str):
        import warnings

        warnings.warn(
            "Color_utils is deprecated. Use pychromatic.cutils functions directly.",
            DeprecationWarning,
            stacklevel=2,
        )
        func = globals().get(name)
        if func is not None and callable(func):
            return func
        raise AttributeError(f"module 'pychromatic.cutils' has no attribute '{name}'")
