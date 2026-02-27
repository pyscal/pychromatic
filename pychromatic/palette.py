"""
Main file containing the Palette class
"""

from __future__ import annotations

import random
from collections.abc import Iterator

import matplotlib.colors as mc
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

import pychromatic.colors as colorlist
import pychromatic.cutils as cutils
from pychromatic.colorclass import Color


class Palette:
    """
    Palette class is the main class of pychromatic that is initialised

    """

    def __init__(self, palette: str = "default", palette_type: str = "") -> None:

        self.colors: list[Color] | None = None
        self._palette = palette

        # if palette name is provided, assign the palette directly
        if palette == "default" and palette_type == "":
            self.assign_palette("default")

        # if random is selected - give a random palette
        elif palette == "random":
            self.random_palette()

        # if a type choice is provided, select accordingly
        elif palette_type != "":
            self.random_palette(palette_type=palette_type)

        # or maybe just a name
        else:
            self.assign_palette(palette)

    def __repr__(self) -> str:
        """
        String representation of the palette
        """
        n_colors = len(self.colors) if self.colors else 0
        return f"Palette('{self._palette}', {n_colors} colors)"

    def __len__(self) -> int:
        """Return the number of colors in the palette."""
        return len(self.colors) if self.colors else 0

    def __iter__(self) -> Iterator[Color]:
        """Iterate over the colors in the palette."""
        return iter(self.colors) if self.colors else iter([])

    def __getitem__(self, index: int | str) -> Color:
        """Access a color by integer index or name."""
        if isinstance(index, int):
            return self.colors[index]
        if isinstance(index, str):
            for c in self.colors:
                if c.name == index:
                    return c
            raise KeyError(f"No color named '{index}' in palette")
        raise TypeError(f"Index must be int or str, got {type(index).__name__}")

    @property
    def palette(self) -> str:
        return self._palette

    @palette.setter
    def palette(self, palette_name: str) -> None:
        """
        A property for palette
        """
        # if palette name is provided, assign the palette directly
        self._palette = palette_name
        if palette_name == "default":
            self.assign_palette("default")

        # if random is selected - give a random palette
        elif palette_name == "random":
            self.random_palette()

        # or maybe just a name
        else:
            self.assign_palette(palette_name)

    def reset(self) -> None:
        for c in self.colors:
            c.reset()

    def add_color(self, clr: str | Color, name: str | None = None, pos: int | None = None) -> None:
        if pos is None:
            pos = len(self.colors) + 1

        if isinstance(clr, str):
            if name is None:
                name = f"color{len(self.colors)}"
            c = Color(clr, name=name)
            setattr(self, name, c)
            self.colors[pos:pos] = [c]
        else:
            setattr(self, clr.name, clr)
            self.colors[pos:pos] = [clr]

    def remove_color(self, clr: str) -> None:
        delattr(self, clr)
        pos = [i for i, c in enumerate(self.colors) if c.name == clr]
        for p in reversed(pos):
            del self.colors[p]

    def brighten(self, clr: str, fraction: float = 0.05, name: str | None = None) -> None:
        if name is None:
            name = f"color{len(self.colors)}"
        hexv = cutils.brighten(getattr(self, clr).hex, fraction=fraction)
        c = Color(hexv, name=name)
        setattr(self, name, c)
        self.colors.append(c)

    def darken(self, clr: str, fraction: float = 0.05, name: str | None = None) -> None:
        self.brighten(clr, fraction=-1 * fraction, name=name)

    def mix(self, clr1: str, clr2: str, ratio: float = 0.5, name: str | None = None) -> None:
        if name is None:
            name = f"color{len(self.colors)}"

        color1 = getattr(self, clr1)
        color2 = getattr(self, clr2)
        rgb1 = cutils.hex_to_rgb(color1.hex)
        rgb2 = cutils.hex_to_rgb(color2.hex)

        rgb = [ratio * rgb1[x] + (1 - ratio) * rgb2[x] for x in range(3)]
        hexv = cutils.rgb_to_hex(rgb)
        c = Color(hexv, name=name)
        setattr(self, name, c)
        self.colors.append(c)
        self.show(color_list=[color1, c, color2])

    def get_cmap(self) -> mc.LinearSegmentedColormap:
        """Create a ``LinearSegmentedColormap`` from the palette colors."""
        cmap = cutils.create_colormap([color.hex for color in self.colors])
        return cmap

    def get_intermediate_colors(
        self, clr1: str, clr2: str, num_colors: int = 1, names: list[str] | None = None
    ) -> None:
        if names is None:
            names = [f"color{len(self.colors) + x}" for x in range(num_colors)]

        color1 = getattr(self, clr1)
        color2 = getattr(self, clr2)
        clrlist = cutils.find_intermediate_colors(
            color1.hex, color2.hex, colors=num_colors, ignore_edges=True
        )
        clrobjlist = [Color(hexv, name=names[count]) for count, hexv in enumerate(clrlist)]
        for c in clrobjlist:
            self.colors.append(c)

    def assign_palette(self, palette_name: str) -> None:
        """
        Assign a palatte to the class

        Parameters
        ----------
        palette_name : string
            name of the palette

        Returns
        -------
        None
        """
        # try to get the list of colors
        try:
            clrs = colorlist.color_palettes[palette_name]
            clist = []
            for i in range(len(clrs["colors"])):
                c = Color(clrs["colors"][i], name=clrs["names"][i])
                setattr(self, clrs["names"][i], c)
                clist.append(c)
            self.colors = clist
        except KeyError:
            raise KeyError(f"Palette '{palette_name}' not found!") from None

    def random_palette(self, palette_type: str | None = None) -> None:
        """
        Assign a random palette

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if palette_type is None:
            keys = colorlist.color_palettes.keys()

            # pick a random key
            random_plt = random.choice(list(keys))
            self.assign_palette(random_plt)

        else:
            # if a type is provided, pick a random palette that satisfies the type
            filtered_list = [
                key
                for key in colorlist.color_palettes
                if colorlist.color_palettes[key]["type"] == palette_type
            ]
            random_plt = random.choice(filtered_list)
            self.assign_palette(random_plt)

    def show(
        self,
        color_list: list[Color] | None = None,
        minimal: bool = True,
        title: str | None = None,
        scale: float = 0.5,
    ) -> None:
        """
        Wrap around inherited plot function
        """
        if color_list is None:
            color_list = self.colors

        colors = [c.hex for c in color_list]
        names = [c.name for c in color_list]

        if not minimal:
            fig, axs = plt.subplots(1, 3, figsize=(12, 5))
            for count, color in enumerate(colors):
                x = np.arange(11)
                y = np.sin(x / (1.75 * np.pi))
                axs[0].plot(x, y + count / 3.0, color=color, label=f"{color}", linewidth=4)
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
                # plt.axis("off")
                ax2 = fig.add_subplot(spec[1, count])
                ax2.plot([0, 1], [0.25, 0.25], color=color, linewidth=3)
                ax2.set_ylim(0, 0.5)
                ax2.set_xlim(0, 0.5)

                ax1.spines["right"].set_visible(False)
                ax1.spines["left"].set_visible(False)
                ax1.spines["top"].set_visible(False)
                ax1.spines["bottom"].set_visible(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([])
                ax1.xaxis.set_ticks_position("none")
                ax1.yaxis.set_ticks_position("none")

                ax2.spines["right"].set_visible(False)
                ax2.spines["left"].set_visible(False)
                ax2.spines["top"].set_visible(False)
                ax2.spines["bottom"].set_visible(False)
                ax2.set_xticklabels([])
                ax2.set_yticklabels([])
                ax2.xaxis.set_ticks_position("none")
                ax2.yaxis.set_ticks_position("none")
                ax2.set_xlabel(names[count], fontsize=10, rotation=90, color="#37474F")

            plt.subplots_adjust(wspace=0, hspace=0)
            plt.show()
