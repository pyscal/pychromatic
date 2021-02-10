import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mc
from pychromatic.palette import Palette
from cycler import cycler
import pychromatic.colors as pc

class PlotTemplate(Palette):
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
        fig_height_in = fig_width_in * self.ratio

        fig_dim = (fig_width_in, fig_height_in)

        return fig_dim

    def show(self):
        return self.fig

                    
class Multiplot(PlotTemplate):
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
        self.ratio = kwargs.get('ratio', ((5**.5 - 1) / 2.0))
        #palette specs
        #self.palette = Palette(palette=kwargs.get('palette', 'default'))
        self.palette = kwargs.get('palette', 'default')
        #number of plots
        self.columns = kwargs.get('columns',1)
        self.rows = kwargs.get('rows',1)
        self.rows = kwargs.get('rows',1)

        self.make_plot()
                

    def make_plot(self):
        """
        Make plot of the required dimensions using GridSpec
        """
        self.fig = plt.figure(figsize=self.set_size(), edgecolor=pc.darkgrey)
        self.spec = gridspec.GridSpec(ncols=self.columns, nrows=self.rows, figure=self.fig)
        self.axes = []
        self.subaxes = []
        custom_cycler = (cycler(color=self.colors))
        #now create a set of axes
        for i in range(self.rows):
            axdummy = []
            saxdummy = []
            for j in range(self.columns):
                ax = self.fig.add_subplot(self.spec[i, j])
                ax.set_prop_cycle(custom_cycler)

                #set ticks
                ax.tick_params(which='major', length=4, width=1, 
                          direction='in', bottom=True, top=False, 
                          right=False, color=pc.accent["dgrey"])

                axdummy.append(ax)
                saxdummy.append([])
            self.axes.append(np.array(axdummy))
            self.subaxes.append(np.array(saxdummy))
        self.axes = np.array(self.axes)
        self.subaxes = np.array(self.subaxes)


    def add_subplot(self, index, rows=1, columns=1, hide_axes=True):
        """
        make subplots
        """
        if len(index) != 2:
            raise TypeError("Index should be of length 2")
        if index[0] >= self.rows:
            raise ValueError("index should be less than set rows")
        if index[1] >= self.columns:
            raise ValueError("index should be less than set columns")


        gs = gridspec.GridSpecFromSubplotSpec(rows, columns, subplot_spec=self.spec[index[0], index[1]])
        for r in range(rows):
            for c in range(columns):
                ax = self.fig.add_subplot(gs[r, c])
                #set ticks
                ax.tick_params(which='major', length=4, width=1, 
                          direction='in', bottom=True, top=False, 
                          right=False, color=pc.accent["dgrey"])

                subx = list(self.subaxes)
                subx[index[0]][index[1]]  = np.append(subx[index[0]][index[1]], ax)
                self.subaxes = subx

        if hide_axes:
            self.turn_off_axes(index)

    #now turn off main axes
    def turn_off_axes(self, index, subindex=None):
        """
        Turn off axes
        """
        if subindex is None:
            self.axes[index[0], index[1]].spines['right'].set_visible(False)
            self.axes[index[0], index[1]].spines['left'].set_visible(False)
            self.axes[index[0], index[1]].spines['top'].set_visible(False)
            self.axes[index[0], index[1]].spines['bottom'].set_visible(False)
            self.axes[index[0], index[1]].set_xticklabels([])
            self.axes[index[0], index[1]].set_yticklabels([])
            self.axes[index[0], index[1]].xaxis.set_ticks_position('none')
            self.axes[index[0], index[1]].yaxis.set_ticks_position('none')
            self.axes[index[0], index[1]].set_ylabel(" ")
            self.axes[index[0], index[1]].set_xlabel(" ")
        else:
            self.axes[index[0], index[1]][subindex].spines['right'].set_visible(False)
            self.axes[index[0], index[1]][subindex].spines['left'].set_visible(False)
            self.axes[index[0], index[1]][subindex].spines['top'].set_visible(False)
            self.axes[index[0], index[1]][subindex].spines['bottom'].set_visible(False)
            self.axes[index[0], index[1]][subindex].set_xticklabels([])
            self.axes[index[0], index[1]][subindex].set_yticklabels([])
            self.axes[index[0], index[1]][subindex].xaxis.set_ticks_position('none')
            self.axes[index[0], index[1]][subindex].yaxis.set_ticks_position('none')
            self.axes[index[0], index[1]][subindex].set_ylabel(" ")
            self.axes[index[0], index[1]][subindex].set_xlabel(" ")




class BrokenAxes(PlotTemplate):
    """
    Broken axes plot object
    """
    def __init__(self, x, y, width=510, fig=None, spec=None, specx=0, specy=0, **kwargs):
        """
        Add things
        """
        #asssign a palette, things can be changed later
        self.x = x
        self.y = y
        self.width = width
        self.fig = fig
        self.spec = spec
        self.specx = specx
        self.specy = specy

        self.d = kwargs.get('d',0.06)
        self.tilt = kwargs.get('tilt',0.01)
        #plot dimensions
        self.fraction = kwargs.get('fraction',1)
        self.ratio = kwargs.get('ratio', ((5**.5 - 1) / 2.0))
        #palette specs
        #self.palette = Palette(palette=kwargs.get('palette', 'default'))
        self.palette = kwargs.get('palette', 'default')
        #number of plots
        self.columns = kwargs.get('columns',1)
        self.rows = kwargs.get('rows',1)

        self.make_plot()

    def make_plot(self):

        self.axes = []
        if self.fig is None:
            self.fig = plt.figure(figsize=self.set_size(), edgecolor=pc.darkgrey)
        
        if self.spec is None:
            self.spec = gridspec.GridSpec(ncols=1, nrows=1, wspace=0.2)

        if len(self.x)==4:
            seg1 = self.x[1]-self.x[0]
            seg2 = self.x[3]-self.x[2]
            xlo1 = self.x[0]
            xlo2 = self.x[2]
            xhi1 = self.x[1]
            xhi2 = self.x[3]
            ylo = self.y[0]
            yhi = self.y[1]
            widths = [seg1, seg2]
            ax = self.spec[self.specx, self.specy].subgridspec(1, 2, width_ratios=widths, wspace=0.2)
            ax2m = self.fig.add_subplot(ax[0, :])
            ax2a = self.fig.add_subplot(ax[0, 0], sharey=ax2m)
            ax2b = self.fig.add_subplot(ax[0, 1], sharey=ax2a)
            ax2a.set_xlim(xlo1, xhi1)
            ax2b.set_xlim(xlo2, xhi2)
            ax2a.set_ylim(ylo, yhi)
            ax2b.set_ylim(ylo, yhi)
            ax2m.set_ylim(ylo, yhi)

            norm1 = (widths[0]/sum(widths))
            norm2 = (widths[1]/sum(widths))

            ax2m.tick_params(which='major', length=3, width=1, direction='in', 
                             bottom=False, top=False, right=False, left=False, 
                             labelbottom=False, labelleft=False, 
                             color=pc.darkgrey,zorder=1000)

            ax2a.tick_params(which='major', length=3, width=1, direction='in', 
                             bottom=True, top=False, right=False, color=pc.darkgrey)
            ax2b.tick_params(which='major', length=3, width=1, direction='in', 
                             bottom=True, top=False, right=False, left=False, 
                             labelleft=False, color=pc.darkgrey)    

            ax2m.spines['right'].set_visible(False)
            ax2m.spines['left'].set_visible(False)
            ax2m.spines['top'].set_visible(False)
            ax2m.spines['bottom'].set_visible(False)
            ax2a.spines['right'].set_visible(False)
            ax2b.spines['left'].set_visible(False)


            ax2a.plot([xhi1-self.tilt*norm1, xhi1+self.tilt*norm1], [ylo-self.d/2, ylo+self.d/2], color=pc.darkgrey)[0].set_clip_on(False)
            ax2a.plot([xhi1-self.tilt*norm1, xhi1+self.tilt*norm1], [yhi-self.d/2, yhi+self.d/2], color=pc.darkgrey)[0].set_clip_on(False)
            ax2b.plot([xlo2-self.tilt*norm2, xlo2+self.tilt*norm2], [ylo-self.d/2, ylo+self.d/2], color=pc.darkgrey)[0].set_clip_on(False)
            ax2b.plot([xlo2-self.tilt*norm2, xlo2+self.tilt*norm2], [yhi-self.d/2, yhi+self.d/2], color=pc.darkgrey)[0].set_clip_on(False)

        elif len(self.y)==4:
            seg1 = self.y[1]-self.y[0]
            seg2 = self.y[3]-self.y[2]
            ylo1 = self.y[0]
            ylo2 = self.y[2]
            yhi1 = self.y[1]
            yhi2 = self.y[3]
            xlo = self.x[0]
            xhi = self.x[1]
            widths = [seg1, seg2]
            ax = self.spec[self.specx, self.specy].subgridspec(2, 1, height_ratios=widths, wspace=0.2)
            ax2m = self.fig.add_subplot(ax[:, 0])
            ax2a = self.fig.add_subplot(ax[1, 0], sharex=ax2m)
            ax2b = self.fig.add_subplot(ax[0, 0], sharex=ax2a)
            ax2a.set_ylim(ylo1, yhi1)
            ax2b.set_ylim(ylo2, yhi2)
            ax2a.set_xlim(xlo, xhi)
            ax2b.set_xlim(xlo, xhi)
            ax2m.set_xlim(xlo, xhi)

            norm1 = (widths[0]/sum(widths))
            norm2 = (widths[1]/sum(widths))

            ax2m.tick_params(which='major', length=3, width=1, direction='in', 
                             bottom=False, top=False, right=False, left=False, 
                             labelbottom=False, labelleft=False, 
                             color=pc.darkgrey,zorder=1000)

            ax2a.tick_params(which='major', length=3, width=1, direction='in', 
                             bottom=True, top=False, right=False, labeltop=False, color=pc.darkgrey)
            ax2b.tick_params(which='major', length=3, width=1, direction='in', 
                             bottom=False, top=True, right=False, left=True, 
                             labelbottom=False, color=pc.darkgrey)    

            ax2m.spines['right'].set_visible(False)
            ax2m.spines['left'].set_visible(False)
            ax2m.spines['top'].set_visible(False)
            ax2m.spines['bottom'].set_visible(False)
            ax2a.spines['top'].set_visible(False)
            ax2b.spines['bottom'].set_visible(False)


            ax2a.plot([xlo-self.d/2, xlo+self.d/2], [yhi1-self.tilt*norm1, yhi1+self.tilt*norm1],  color=pc.darkgrey)[0].set_clip_on(False)
            ax2a.plot([xhi-self.d/2, xhi+self.d/2], [yhi1-self.tilt*norm1, yhi1+self.tilt*norm1], color=pc.darkgrey)[0].set_clip_on(False)
            ax2b.plot([xlo-self.d/2, xlo+self.d/2], [ylo2-self.tilt*norm2, ylo2+self.tilt*norm2], color=pc.darkgrey)[0].set_clip_on(False)
            ax2b.plot([xhi-self.d/2, xhi+self.d/2], [ylo2-self.tilt*norm2, ylo2+self.tilt*norm2], color=pc.darkgrey)[0].set_clip_on(False)

        custom_cycler = (cycler(color=self.colors))
        ax2m.set_prop_cycle(custom_cycler)
        ax2a.set_prop_cycle(custom_cycler)
        ax2b.set_prop_cycle(custom_cycler)

        self.axes = [ax2m, ax2a, ax2b]

