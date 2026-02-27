=====
Usage
=====

Working with Colors
-------------------

Create a ``Color`` from any hex string:

.. code-block:: python

    from pychromatic import Color

    c = Color('#1976d2', name='blue')
    print(c.hex)        # '#1976d2'
    print(c.rgb)        # [25, 118, 210]
    c.display()          # Rich terminal swatch

Brighten, darken, mix, or multiply:

.. code-block:: python

    c.brighten(0.2)          # lightens in HLS space
    c.darken(0.1)            # darkens in HLS space
    c.reset()                # back to original '#1976d2'

    lighter = c * 1.3        # returns a NEW Color (original unchanged)
    c.mix(Color('#ff0000'), ratio=0.5)  # blend in-place

Working with Palettes
---------------------

Load any built-in palette by name:

.. code-block:: python

    from pychromatic import Palette

    p = Palette('default')      # 15-color sequential palette
    p.show()                     # matplotlib swatch plot
    print(p.colors)              # list of Color objects

    # Access individual colors as attributes
    print(p.blue.hex)

Switch palettes, add, or remove colors:

.. code-block:: python

    p.palette = 'pastels'        # swap to a different palette
    p.add_color('#abcdef', name='custom')
    p.remove_color('custom')
    p.reset()                    # restore original colors

Generate a matplotlib ``LinearSegmentedColormap``:

.. code-block:: python

    cmap = p.get_cmap()
    # Use in any matplotlib call:  ax.scatter(x, y, c=z, cmap=cmap)

Colorblind-Friendly Palettes
-----------------------------

Four accessibility-first palettes are available both as ``Palette`` objects
**and** as importable plain dictionaries:

.. code-block:: python

    from pychromatic import okabe_ito, tableau10, tol_bright, tol_muted

    # Palette object
    p = Palette('okabe_ito')
    p.show()

    # Direct dict access
    print(okabe_ito['orange'])   # '#E69F00'
    print(tol_muted['teal'])     # '#44AA99'

Available colorblind palettes:

* **okabe_ito** — 8 colors, Okabe & Ito (2008)
* **tableau10** — 10 colors, Tableau default
* **tol_bright** — 7 colors, Paul Tol bright
* **tol_muted** — 9 colors, Paul Tol muted

The ``chromatify`` Decorator
----------------------------

Auto-style matplotlib subplots with palette colors:

.. code-block:: python

    from pychromatic import chromatify

    @chromatify
    def my_plot():
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 9])
        return ax

    my_plot()

Color Utilities
---------------

Low-level functions live in ``pychromatic.cutils``:

.. code-block:: python

    from pychromatic.cutils import (
        hex_to_rgb,
        rgb_to_hex,
        brighten,
        mix_colors,
        find_intermediate_colors,
        create_colormap,
    )

    hex_to_rgb('#ff5722')                         # [255, 87, 34]
    rgb_to_hex([25, 118, 210])                    # '#1976d2'
    mix_colors('#ff0000', '#0000ff', ratio=0.5)   # blended hex
    find_intermediate_colors('#ff0000', '#0000ff', colors=5)  # list of hex
