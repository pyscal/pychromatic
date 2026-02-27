Welcome to pychromatic's documentation!
========================================

**pychromatic** is a color palette manager and matplotlib plotting utility for
Python. It provides 22 curated color palettes (including 4 colorblind-friendly
sets), color manipulation tools, and opinionated matplotlib plot templates.

.. code-block:: python

   from pychromatic import Color, Palette, get_color, palette_cmap

   p = Palette('okabe_ito')
   c = Color('#1976d2', name='blue')
   hex_val = get_color(0.5, 'viridis')
   cmap = palette_cmap('rainbow')


.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   quickstart

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   examples/colors
   examples/palettes
   examples/colormaps
   examples/colorblind
   examples/plotting
   examples/utilities

.. toctree::
   :maxdepth: 2
   :caption: Reference

   api
   palette_reference

.. toctree::
   :maxdepth: 1
   :caption: Project

   contributing
   history
   authors


Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
