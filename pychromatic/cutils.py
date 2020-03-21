import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import colorsys
import numpy as np
import matplotlib.colors as mc

class Color_utils:
    """
    A class which holds the utility functions for modifying a class.
    """
    def __init__(self):
        self.a = 1

    def hex_to_rgb(self, hexval):
        """
        Convert a hex color value to rgb

        Parameters
        ----------
        hexval : string
            hex color code starting with #

        Returns
        -------
        rgb : list of int
            A list of rgb values between 0-255
        """
        d = hexval.strip('#')
        rgb = [int(d[x:x+2], 16) for x in range(0, len(d), 2)]
        return rgb

    def rgb_to_hex(self, rgb):
        """
        Convert a rgb color value to hex color code

        Parameters
        ----------
        rgb : list
            a list consisting of three rgb values. It can either be from 0 to 255
            or from 0 to 1.

        Returns
        -------
        string
            the hex code

        """
        #decide if rgbs are floating points between 0 or 1
        if all((val >= 0) and (val<=1) and isinstance(val, float) for val in rgb):
            #convert to values within 255
            rgb = [int(x*255) for x in rgb]
        if all((val >= 0) and (val<=255) for val in rgb):
            return "#{:02x}{:02x}{:02x}".format(int(rgb[0]),int(rgb[1]),int(rgb[2]))
        else:
            raise ValueError("rgb values should be within 0-255")


    def rgb_to_hls(self, rgbval):
        """
        Convert a rgb value to equivalent hls value

        Parameters
        ----------
        rgbval : list
            A list of three values containing rgb for the color

        Returns
        -------
        hls : list
            A list of hls values

        Notes
        -----
        rgb values should be between 0-255

        """
        h, l, s = colorsys.rgb_to_hls(rgbval[0]/float(255), rgbval[1]/float(255), rgbval[2]/float(255))
        return [h, l, s]


    def hls_to_rgb(self, hls):
        """
        Convert hls value to rgb

        Parameters
        ----------
        hls : list
            A list of hls values

        Returns
        -------
        rgb : list
            list of rgb values between 0-255

        """
        rgb = colorsys.hls_to_rgb(hls[0], hls[1], hls[2])
        rgb = [int(x*255) for x in rgb]
        return rgb


    def brighten(self, color, fraction=0.05):
        """
        Brighten or darken a color

        Parameters
        ----------
        color : string
            the hex value of input color

        fraction : float
            the amount by which to brighten the color

        Returns
        -------
        hexv : string
            the hex value of the modified color

        Notes
        -----
        Colors can also be darkened by providing a negative value for `fraction`

        """
        rgbval = self.hex_to_rgb(color)
        hls = self.rgb_to_hls(rgbval)

        #now adjust luminescence -
        hls[1] =min((1+fraction)*hls[1], 1)

        rgb = colorsys.hls_to_rgb(hls[0], hls[1], hls[2])
        hexv = self.rgb_to_hex(rgb)
        return hexv


    def mix_colors(self, color1, color2, ratio=0.5):
        """
        Mix two colors to get an intermediate color

        Parameters
        ----------
        color1 : string
            hex code of the first color

        color2 : string
            hex code of the second color

        ratio : float
            ratio between `color1` and `color2`

        Returns
        -------
        hexv : string
            hex code of the intermediate color

        Notes
        -----
        if `ratio` is `r`, then the new color would be r*color1 + (1-r)*color2
        """

        rgb1 = self.hex_to_rgb(color1)
        rgb2 = self.hex_to_rgb(color2)

        rgb = [ratio*rgb1[x] + (1-ratio)*rgb2[x] for x in range(3)]
        hexv = self.rgb_to_hex(rgb)

        return hexv


    def find_intermediate_colors(self, color1, color2, colors=1, ignore_edges=False):
        """
        Find a given number of intermediate colors between two input colors

        Parameters
        ----------
        color1 : string
            hex code of the first input color

        color2 : string
            hex code of the second input color

        colors : int, optional
            number of intermediate colors required, default 1

        ignore_edges : bool, optional
            If True, the input colors are not included in the return list.
            Default False.

        Returns
        -------
        hexvals : list
            list of intermediate colors


        """

        rgb1 = self.hex_to_rgb(color1)
        rgb2 = self.hex_to_rgb(color2)

        #now find intermediate points
        rpoints = np.linspace(rgb1[0], rgb2[0], colors+2)
        gpoints = np.linspace(rgb1[1], rgb2[1], colors+2)
        bpoints = np.linspace(rgb1[2], rgb2[2], colors+2)

        #stack to pairs
        if ignore_edges:
            new_rgbs = np.stack((rpoints[1:-1], gpoints[1:-1], bpoints[1:-1]), axis=-1)
        else:
            new_rgbs = np.stack((rpoints, gpoints, bpoints), axis=-1)

        #convert to hexvals
        hexvals = [self.rgb_to_hex(rgb) for rgb in new_rgbs]
        return hexvals


    def create_colormap(self, colors):
        """
        Create a color map from a list of colors

        Parameters
        ----------
        colors : list
            a list of input colors. Atleast 2 colors are required.

        Returns
        -------
        cmap : color map

        """
        if not len(colors)>1:
            raise ValueError("length of colors should be atleast 2")

        cmap = mc.LinearSegmentedColormap.from_list("", colors)
        return cmap

    def plot_colors(self, colors, minimal=False):
        """
        Show plot to illustrate the colors

        Parameters
        ----------
        colors : list
            list of colors to plot in hex values

        minimal : bool, optional
            if True, plot a minimal bar
            default False

        Returns
        -------
        None

        """
        if not minimal:
            fig, axs = plt.subplots(1, 3, figsize=(12, 5))
            for count, color in enumerate(colors):
                    x = np.arange(11)
                    y = np.sin(x/(1.75*np.pi))
                    axs[0].plot(x, y+count/3., color=color, label="%s"%color, linewidth=4)
            axs[1].pie((np.random.dirichlet(np.ones(len(colors)),size=1)*100)[0], colors=colors, autopct='%1.1f%%', startangle=90)
            axs[1].axis('equal')
            axs[2].bar(np.arange(len(colors)), np.arange(len(colors))+1,color=colors,linewidth=0)
            axs[2].set_xticks(np.arange(len(colors))+0.4)
            plt.show()
        else:
            fig = plt.figure(figsize=[len(colors), 1.5])
            spec = gridspec.GridSpec(ncols=len(colors), nrows=2, figure=fig)
            for count, color in enumerate(colors):
                ax1 = fig.add_subplot(spec[0, count])
                ax1.fill([0,1,1,0],[0,0,1,1], color=color)
                ax1.set_ylim(0,1)
                ax1.set_xlim(0,1)
                plt.axis("off")
                ax2 = fig.add_subplot(spec[1, count])
                ax2.plot([0,1],[0.25,0.25], color=color, linewidth=3)
                ax2.set_ylim(0,0.5)
                ax2.set_xlim(0,0.5)
                plt.axis("off")
            plt.subplots_adjust(wspace=0, hspace=0)
            plt.show()
