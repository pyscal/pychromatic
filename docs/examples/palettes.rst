=======================
Working with Palettes
=======================

The :class:`~pychromatic.palette.Palette` class manages collections of
:class:`~pychromatic.colorclass.Color` objects and provides manipulation,
colormap generation, and visualization features.

Creating a Palette
------------------

Load any of the 22 built-in palettes by name:

.. code-block:: python

    from pychromatic import Palette

    p = Palette('default')       # 15-color qualitative palette
    p = Palette('okabe_ito')     # 8-color colorblind-safe
    p = Palette('rainbow')       # 5-color sequential
    p = Palette('random')        # surprise me!

.. code-block:: python

    print(p)                     # Palette('rainbow', 5 colors)

See :doc:`/palette_reference` for the full list.


Container Protocol
------------------

Palettes support ``len()``, iteration, and indexing:

.. code-block:: python

    p = Palette('set2')

    # Length
    print(len(p))                # 5

    # Iterate
    for color in p:
        print(color.hex, color.name)

    # Index by position
    first = p[0]
    last  = p[-1]

    # Index by name
    p = Palette('default')
    blue = p['blue']
    print(blue.hex)              # '#1976d2'


Accessing Colors as Attributes
------------------------------

Every color is also set as an attribute on the palette:

.. code-block:: python

    p = Palette('default')
    print(p.blue.hex)            # '#1976d2'
    print(p.red.hex)             # '#d32f2f'
    print(p.green.rgb)           # [56, 142, 60]


Switching Palettes
------------------

.. code-block:: python

    p = Palette('default')
    p.palette = 'pastels'        # swap to a different palette
    print(len(p))                # 12


Adding & Removing Colors
------------------------

.. code-block:: python

    p = Palette('set2')
    p.add_color('#abcdef', name='custom')
    print(len(p))                # 6
    print(p.custom.hex)          # '#abcdef'

    # Add a Color object
    from pychromatic import Color
    p.add_color(Color('#fedcba', name='warm'))

    # Remove by name
    p.remove_color('custom')
    print(len(p))                # 6


Brighten & Darken Palette Colors
--------------------------------

Create a brightened/darkened copy of a palette color and add it to the palette:

.. code-block:: python

    p = Palette('set2')
    p.brighten('color1', fraction=0.3, name='light_c1')
    print(p.light_c1.hex)

    p.darken('color2', fraction=0.2, name='dark_c2')
    print(p.dark_c2.hex)

.. note::

   ``brighten()`` and ``darken()`` no longer call ``show()`` automatically,
   so they can be used in scripts without opening plot windows.


Mixing Colors
-------------

Mix two palette colors to create an intermediate:

.. code-block:: python

    p = Palette('default')
    p.mix('blue', 'red', ratio=0.5, name='purple')
    print(p.purple.hex)


Finding Intermediate Colors
----------------------------

Generate evenly-spaced intermediates between two palette colors:

.. code-block:: python

    p = Palette('default')
    p.get_intermediate_colors('blue', 'red', num_colors=3,
                               names=['step1', 'step2', 'step3'])
    print(p.step1.hex, p.step2.hex, p.step3.hex)


Generating a Colormap
---------------------

Convert a palette into a matplotlib ``LinearSegmentedColormap``:

.. code-block:: python

    p = Palette('rainbow')
    cmap = p.get_cmap()

    # Use in any matplotlib call
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.random.randn(100)
    y = np.random.randn(100)
    c = np.random.rand(100)

    plt.scatter(x, y, c=c, cmap=cmap)
    plt.colorbar()
    plt.show()


Reset
-----

Restore all colors to their original values:

.. code-block:: python

    p = Palette('default')
    p.colors[0].brighten(0.5)    # modify first color
    p.reset()                     # back to original
    print(p.colors[0].hex)        # original hex


Displaying Palettes
-------------------

.. code-block:: python

    p = Palette('okabe_ito')
    p.show()                     # compact swatch
    p.show(minimal=False)        # full plot with line, pie, and bar charts
