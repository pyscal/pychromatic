"""
Main file containing the Palette class
"""
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.colors as mc

import pychromatic.colors as colorlist
import random
from pychromatic.colorclass import Color
from pychromatic.cutils import Color_utils
import colorsys
import numpy as np

class Palette():
    """
    Palette class is the main class of pychromatic that is initialised

    """
    def __init__(self, palette='default', type=''):

        self.colors = None
        self._palette = palette


        #if palette name is provided, assign the palette directly
        if palette == 'default' and type == '':
            self.assign_palette('default')

        #if random is selected - give a random palette
        elif palette == 'random':
            self.random_palette()

        #if a type choice is provided, select accordingly
        elif type != '':
            self.random_palette(type=type)

        #or maybe just a name
        else:
            self.assign_palette(palette)

        self.utils = Color_utils()

    def __repr__(self):
        """
        String of the class
        """
        self.show()
        return self._palette

    @property
    def palette(self):
        return self._palette

    @palette.setter
    def palette(self, palette_name):
        """
        A property for palette
        """
        #if palette name is provided, assign the palette directly
        self._palette = palette_name
        if palette_name == 'default':
            self.assign_palette('default')

        #if random is selected - give a random palette
        elif palette_name == 'random':
            self.random_palette()

        #or maybe just a name
        else:
            self.assign_palette(palette_name)

    def reset(self):
        for c in self.colors:
            c.reset()

    def add_color(self, clr, name=None, pos=None):
        if pos is None:
            pos = len(self.colors)+1

        if isinstance(clr, str):
            if name is None:
                name = "color%d"%len(self.colors)
            c = Color(clr, name=name)
            setattr(self, name, c)
            self.colors[pos:pos] = [c]
        else:
            setattr(self, clr.name, clr)
            self.colors[pos:pos] = [c]      


    def remove_color(self, clr):
        delattr(self, clr)
        pos = [i for i, c in enumerate(self.colors) if c.name==clr]
        for p in pos:
            del self.colors[p]

    def brighten(self, clr, fraction=0.05, name=None):
        if name is None:
            name = "color%d"%len(self.colors)
        hexv = self.utils.brighten(getattr(self, clr).hex, fraction=fraction)
        c = Color(hexv, name=name)
        setattr(self, name, c)
        self.colors.append(c)
        self.show(color_list=[getattr(self, clr), c])

    def darken(self, clr, fraction=0.05, name=None):
        self.brighten(clr, fraction=-1*fraction, name=name)        

    def mix(self, clr1, clr2, ratio=0.5, name=None):
        if name is None:
            name = "color%d"%len(self.colors)

        color1 = getattr(self, clr1)
        color2 = getattr(self, clr2)
        rgb1 = self.utils.hex_to_rgb(color1.hex)
        rgb2 = self.utils.hex_to_rgb(color2.hex)
        
        rgb = [ratio*rgb1[x] + (1-ratio)*rgb2[x] for x in range(3)]
        hexv = self.utils.rgb_to_hex(rgb)
        c = Color(hexv, name=name)
        setattr(self, name, c)
        self.colors.append(c)
        self.show(color_list=[color1, c, color2])

    def get_cmap(self):
        cmap = self.utils.create_colormap([color.hex for color in self.colors])
        return cmap
    
    def get_intermediate_colors(self, clr1, clr2, num_colors=1, names=None):
        if names is None:
            names = ["color%d"%(len(self.colors)+x) for x in range(num_colors)]

        color1 = getattr(self, clr1)
        color2 = getattr(self, clr2)        
        clrlist = self.utils.find_intermediate_colors(color1.hex, color2.hex, colors=num_colors, ignore_edges=True)
        clrobjlist = [Color(hexv, name=names[count]) for hexv, count in enumerate(clrlist)]
        for c in clrobjlist:
            self.colors.append(c)
        self.show(color_list=clrobjlist)

    
    def assign_palette(self, palette_name):
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
        #try to get the list of colors
        try:
            clrs = colorlist.color_palettes[palette_name]
            clist = []
            for i in range(len(clrs["colors"])):
                c = Color(clrs["colors"][i], name=clrs["names"][i])
                setattr(self, clrs["names"][i], c)
                clist.append(c)
            self.colors = clist
        except:
            raise KeyError("Palette %s not found!"%palette_name)

    def random_palette(self, type=None):
        """
        Assign a random palette

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if type is None:
            keys = colorlist.color_palettes.keys()

            #pick a random key
            random_plt = random.choice(list(keys))
            self.assign_palette(random_plt)

        else:
            #if a type is provided, pick a random palette that satisfies the type
            filtered_list = [ key for key in colorlist.color_palettes.keys() if colorlist.color_palettes[key]['type'] == type]
            random_plt = random.choice(filtered_list)
            self.assign_palette(random_plt)


    def show(self, color_list=None, minimal=True, title=None, scale=0.5):
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
                    y = np.sin(x/(1.75*np.pi))
                    axs[0].plot(x, y+count/3., color=color, label="%s"%color, linewidth=4)
            axs[1].pie((np.random.dirichlet(np.ones(len(colors)),size=1)*100)[0], colors=colors, autopct='%1.1f%%', startangle=90)
            axs[1].axis('equal')
            axs[1].set_title(title)
            axs[2].bar(np.arange(len(colors)), np.arange(len(colors))+1,color=colors,linewidth=0)
            axs[2].set_xticks(np.arange(len(colors))+0.4)
            plt.show()
        else:
            fig = plt.figure(figsize=[scale*len(colors), scale])
            spec = gridspec.GridSpec(ncols=len(colors), nrows=2, figure=fig)
            for count, color in enumerate(colors):
                ax1 = fig.add_subplot(spec[0, count])
                ax1.fill([0,1,1,0],[0,0,1,1], color=color)
                ax1.set_ylim(0,1)
                ax1.set_xlim(0,1)
                #plt.axis("off")
                ax2 = fig.add_subplot(spec[1, count])
                ax2.plot([0,1],[0.25,0.25], color=color, linewidth=3)
                ax2.set_ylim(0,0.5)
                ax2.set_xlim(0,0.5)

                ax1.spines['right'].set_visible(False)
                ax1.spines['left'].set_visible(False)
                ax1.spines['top'].set_visible(False)
                ax1.spines['bottom'].set_visible(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([])
                ax1.xaxis.set_ticks_position('none')
                ax1.yaxis.set_ticks_position('none')
                
                ax2.spines['right'].set_visible(False)
                ax2.spines['left'].set_visible(False)
                ax2.spines['top'].set_visible(False)
                ax2.spines['bottom'].set_visible(False)
                ax2.set_xticklabels([])
                ax2.set_yticklabels([])
                ax2.xaxis.set_ticks_position('none')
                ax2.yaxis.set_ticks_position('none')
                ax2.set_xlabel(names[count], fontsize=10, rotation=90, color="#37474F")

            plt.subplots_adjust(wspace=0, hspace=0)
            plt.show()        