
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from matplotlib.patches import Patch
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage, AnnotationBbox)
from matplotlib.cbook import get_sample_data


#color libraries------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

class colors():
    """
    Class which consists of color properties
    """
    def __init__(self):
        
        self.lred = '#d7191c'
        self.lyellow = '#fdae61'
        self.lgreen = '#abdda4'
        self.lblue = '#2b83ba'
        self.lgrey = "#455A64"
        self.dred = '#C62828'
        self.dyellow = '#FFA000'
        self.dgreen = '#008F68'
        self.dblue = '#006899'
        self.dgrey = "#424242"

    def make_colormap(self, seq):
        """
        Return a LinearSegmentedColormap
        seq: a sequence of floats and RGB-tuples. The floats should be increasing
        and in the interval (0,1).
        """
        seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
        cdict = {'red': [], 'green': [], 'blue': []}
        for i, item in enumerate(seq):
            if isinstance(item, float):
                r1, g1, b1 = seq[i - 1]
                r2, g2, b2 = seq[i + 1]
                cdict['red'].append([item, r1, r2])
                cdict['green'].append([item, g1, g2])
                cdict['blue'].append([item, b1, b2])
        return mcolors.LinearSegmentedColormap('CustomMap', cdict)

    def make_map(self):        
        c = mcolors.ColorConverter().to_rgb

        self.yellowmap = self.make_colormap(
            [c('#FFECB3'),c('#FFE082'), 0.20, c('#FFE082'), c('#FFD54F'), 0.40, c('#FFD54F'), c('#FFCA28'), 0.60, c('#FFCA28'), c('#FFC107'), 0.80, c('#FFC107'), c(self.dyellow) ])
        self.redmap = self.make_colormap(
            [c('#FFCDD2'),c('#EF9A9A'), 0.20, c('#EF9A9A'), c('#EF5350'), 0.40, c('#EF5350'), c('#F44336'), 0.60, c('#F44336'), c('#E53935'), 0.80, c('#E53935'), c(self.dred) ])
        self.greenmap = self.make_colormap(
            [c('#C8E6C9'),c('#A5D6A7'), 0.20, c('#A5D6A7'), c('#81C784'), 0.40, c('#81C784'), c('#66BB6A'), 0.60, c('#66BB6A'), c('#4CAF50'), 0.80, c('#4CAF50'), c(self.dgreen) ])
        self.bluemap = self.make_colormap(
            [c('#B3E5FC'),c('#29B6F6'), 0.20, c('#29B6F6'), c('#039BE5'), 0.40, c('#039BE5'), c('#0288D1'), 0.60, c('#0288D1'), c('#0277BD'), 0.80, c('#0277BD'), c(self.dblue) ])
        self.greymap = self.make_colormap(
            [c('#CFD8DC'),c('#90A4AE'), 0.20, c('#90A4AE'), c('#607D8B'), 0.40, c('#607D8B'), c('#455A64'), 0.60, c('#455A64'), c('#37474F'), 0.80, c('#37474F'), c('#263238') ])


def set_size(width, fraction=1, ratio=((5**.5 - 1) / 2.0)):
    """ Set aesthetic figure dimensions to avoid scaling in latex.

    Parameters
    ----------
    width: float
            Width in pts
    fraction: float
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    #golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches/home/users/menonsqr/Documents/BCC-Mo/EAM_Zhou
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * ratio

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim    