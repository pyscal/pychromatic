"""
Main file containing the Palette class
"""
import pychromatic.colors as colorlist
from pychromatic.cutils import Color_utils
import random

class Palette(Color_utils):
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
            self.colors = colorlist.color_palettes[palette_name]['colors']
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


    def plot_colors(self, limit=None, minimal=False):
        """
        Wrap around inherited plot function
        """
        if limit is None:
            Color_utils.plot_colors(self, self.colors, minimal=minimal)
        else:
            Color_utils.plot_colors(self, self.colors[:limit+1], minimal=minimal)
