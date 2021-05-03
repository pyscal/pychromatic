import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import colorsys
import numpy as np
import matplotlib.colors as mc
import pychromatic.cutils as pcut

class Color_obj:
    """
    A class which holds the info about color

    To implement
    - Mix
    - Colormap
    """
    def __init__(self, colorstr):
        self.colorstr = colorstr
        self.original = colorstr
        self.util = pcut.Color_utils()
        self.update()

    #other utility functions
    def __repr__(self):
        self.show(minimal=True, title="red", scale=0.5)
        return self.colorstr

    def __add__(self, colorobj):
        self.colorstr = self.util.mix_colors(self.hex, colorobj.hex, ratio=0.5)
        self.update()
        return self

    def __radd__(self, colorobj):
        self.colorstr = self.util.mix_colors(self.hex, colorobj.hex, ratio=0.5)
        self.update()       
        return self

    def __mul__(self, fraction):
        if fraction < 1:
            self.darken(fraction=fraction)
        else:
            self.brighten(fraction=(1-fraction))
        return self

    def __rmul__(self, fraction):
        if fraction < 1:
            self.darken(fraction=fraction)
        else:
            self.brighten(fraction=(1-fraction))        
        return self

    def update(self):
        self.hex = self.colorstr
        self.rgb = self.util.hex_to_rgb(self.hex)
        self.hls = self.util.rgb_to_hls(self.rgb)       

    def reset(self):
        self.colorstr = self.original
        self.update()
    
    def brighten(self, fraction=0.05):
        self.colorstr = self.util.brighten(self.colorstr, fraction=fraction)
        self.update()

    def darken(self, fraction=0.05):
        self.colorstr = self.util.brighten(self.colorstr, fraction=-1*fraction)
        self.update()

    def show(self, minimal=False, title=None, scale=1):
        self.util.plot_colors([self.colorstr], minimal=minimal, title=title,
            scale=scale)










