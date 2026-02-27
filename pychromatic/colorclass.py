"""
Color class for representing and manipulating individual colors.
"""
from __future__ import annotations

import pychromatic.cutils as cutils
from rich.console import Console


class Color:
    """
    A class representing a single color with conversion, manipulation and display capabilities.

    Parameters
    ----------
    colorstr : str
        Hex color code (e.g. '#ff5722')
    name : str or None
        Optional human-readable name for the color
    """

    def __init__(self, colorstr: str, name: str | None = None) -> None:
        self.colorstr: str = colorstr
        self.original: str = colorstr
        self.originalname: str | None = name
        self.name: str | None = name
        self.console = Console()
        self.update()

    def __repr__(self) -> str:
        name_part = f", name='{self.name}'" if self.name is not None else ""
        return f"Color('{self.colorstr}'{name_part})"

    def display(self) -> None:
        """Display the color with rich formatting in the terminal."""
        cstr = self.name if self.name is not None else self.colorstr
        self.console.print(cstr, style=f"bold {self.colorstr}")

    def __mul__(self, fraction: float) -> Color:
        new_color = Color(self.colorstr, name=self.name)
        if fraction < 1:
            new_color.brighten(fraction=fraction)
        else:
            new_color.darken(fraction=(fraction - 1))
        return new_color

    def __rmul__(self, fraction: float) -> Color:
        return self.__mul__(fraction)

    def update(self) -> None:
        """Re-derive hex, rgb, and hls attributes from the current colorstr."""
        self.hex: str = self.colorstr
        self.rgb: list[int] = cutils.hex_to_rgb(self.hex)
        self.hls: list[float] = cutils.rgb_to_hls(self.rgb)

    def reset(self) -> None:
        """Reset color to its original value."""
        self.colorstr = self.original
        self.name = self.originalname
        self.update()

    def brighten(self, fraction: float = 0.05) -> None:
        """Brighten the color by the given fraction."""
        self.colorstr = cutils.brighten(self.colorstr, fraction=fraction)
        if self.name is not None:
            self.name = f"light-{self.name.split('-')[-1]}"
        self.update()

    def darken(self, fraction: float = 0.05) -> None:
        """Darken the color by the given fraction."""
        self.colorstr = cutils.brighten(self.colorstr, fraction=-1 * fraction)
        if self.name is not None:
            self.name = f"dark-{self.name.split('-')[-1]}"
        self.update()

    def show(
        self, minimal: bool = True, title: str | None = None, scale: float = 0.5
    ) -> None:
        """Display a color swatch plot."""
        cutils.plot_colors([self.colorstr], minimal=minimal, title=title, scale=scale)

    def mix(self, colorobj: Color, ratio: float = 0.5) -> None:
        """Mix this color with another color in-place."""
        self.colorstr = cutils.mix_colors(self.hex, colorobj.hex, ratio=(1 - ratio))
        if (self.name is not None) and (colorobj.name is not None):
            self.name = f"{self.name.split('-')[-1]}-{colorobj.name}"
        self.update()







