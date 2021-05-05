import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import colorsys
import numpy as np
import matplotlib.colors as mc
import pychromatic.cutils as pcut
from rich.console import Console

class Color:
    """
    A class which holds the info about color

    To implement
    - Mix
    - Colormap
    """
    def __init__(self, colorstr, name=None):
        self.colorstr = colorstr
        self.original = colorstr
        self.originalname = name
        self.name = name
        self.util = pcut.Color_utils()
        self.console = Console()
        self.update()

    #other utility functions
    def __repr__(self):
        if self.name is not None:
            cstr = self.name
        else:
            cstr = self.colorstr
        self.console.print(cstr, style="bold %s"%self.colorstr)
        return self.colorstr

    def __mul__(self, fraction):
        if fraction < 1:
            self.brighten(fraction=fraction)
        else:
            self.darken(fraction=(1-fraction))
        return self

    def __rmul__(self, fraction):
        if fraction < 1:
            self.brighten(fraction=fraction)
        else:
            self.darken(fraction=(1-fraction))
        return self

    def update(self):
        self.hex = self.colorstr
        self.rgb = self.util.hex_to_rgb(self.hex)
        self.hls = self.util.rgb_to_hls(self.rgb)       

    def reset(self):
        self.colorstr = self.original
        self.name = self.originalname
        self.update()
    
    def brighten(self, fraction=0.05):
        self.colorstr = self.util.brighten(self.colorstr, fraction=fraction)
        if self.name is not None:
            self.name = "-".join(["light", self.name.split("-")[-1]])
        self.update()

    def darken(self, fraction=0.05):
        self.colorstr = self.util.brighten(self.colorstr, fraction=-1*fraction)
        if self.name is not None:
            self.name = "-".join(["dark", self.name.split("-")[-1]])
        self.update()

    def show(self, minimal=True, title=None, scale=0.5):
        self.util.plot_colors([self.colorstr], minimal=minimal, title=title,
            scale=scale)


    def mix(self, colorobj, ratio=0.5):
        self.colorstr = self.util.mix_colors(self.hex, colorobj.hex, ratio=(1-ratio))
        if (self.name is not None) and (colorobj.name is not None):
            self.name = "-".join([self.name.split("-")[-1], colorobj.name])
        self.update() 







