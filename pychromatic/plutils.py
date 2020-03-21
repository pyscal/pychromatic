import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mc
from pychromatic.palette import Palette

class Multiplot:
    """
    A class to easily create multiplots and return the objects for further modification
    """
    def __init__(self, width=510, **kwargs):
        """
        Add things
        """
        #asssign a palette, things can be changed later
        self.width = width
        #plot dimensions
        self.fraction = kwargs.get('fraction',1)
        self.ration = kwargs.get('ration', ((5**.5 - 1) / 2.0))
        #palette specs
        self.palette = Palette(palette=kwargs.get('palette', 'default'))
        #number of plots
        self.columns = kwargs.get('columns',1)
        self.rows = kwargs.get('rows',1)

        self.make_plot()

    def make_plot(self):
        """
        Make plot of the required dimensions using GridSpec
        """
        self.fig = plt.figure(figsize=self.set_size())
        self.spec = gridspec.GridSpec(ncols=self.columns, nrows=self.rows, figure=self.fig)
        self.axes = []
        #now create a set of axes
        for i in range(len(self.rows)):
            axdummy = []
            for j in range(len(self.columns)):
                ax = self.fig.add_subplot(self.spec[i, j])
                axdummy.append(ax)
            self.axes.append(axdummy)

    def set_size(self):
        """
        Set aesthetic figure dimensions to avoid scaling in latex.

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
        fig_width_pt = self.width * self.fraction

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
