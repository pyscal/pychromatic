==================
Utility Functions
==================

The ``pychromatic.cutils`` module contains low-level color utility functions
that can be used independently of the ``Color`` and ``Palette`` classes.


Color Conversions
-----------------

Hex to RGB
~~~~~~~~~~

.. code-block:: python

    from pychromatic.cutils import hex_to_rgb

    hex_to_rgb('#ff5722')        # [255, 87, 34]
    hex_to_rgb('#000000')        # [0, 0, 0]
    hex_to_rgb('#ffffff')        # [255, 255, 255]

    # Also works without the '#' prefix
    hex_to_rgb('1976d2')         # [25, 118, 210]


RGB to Hex
~~~~~~~~~~

.. code-block:: python

    from pychromatic.cutils import rgb_to_hex

    rgb_to_hex([255, 0, 0])      # '#ff0000'
    rgb_to_hex([25, 118, 210])   # '#1976d2'

    # Float inputs (0.0–1.0) are auto-converted
    rgb_to_hex([1.0, 0.0, 0.0])  # '#ff0000'


RGB to HLS
~~~~~~~~~~

.. code-block:: python

    from pychromatic.cutils import rgb_to_hls

    rgb_to_hls([255, 0, 0])      # [0.0, 0.5, 1.0]
    rgb_to_hls([25, 118, 210])   # [0.565..., 0.460..., 0.786...]


HLS to RGB
~~~~~~~~~~

.. code-block:: python

    from pychromatic.cutils import hls_to_rgb

    hls_to_rgb([0.0, 0.5, 1.0])  # [255, 0, 0]


Color Manipulation
------------------

Brighten / Darken
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from pychromatic.cutils import brighten

    brighten('#1976d2', fraction=0.2)    # lighter shade
    brighten('#1976d2', fraction=-0.2)   # darker shade

    # Even pure black can be brightened
    brighten('#000000', fraction=0.5)    # mid-grey


Mix Colors
~~~~~~~~~~

Blend two colors at a given ratio:

.. code-block:: python

    from pychromatic.cutils import mix_colors

    mix_colors('#ff0000', '#0000ff', ratio=0.5)   # equal blend
    mix_colors('#ff0000', '#0000ff', ratio=1.0)   # 100% first color
    mix_colors('#ff0000', '#0000ff', ratio=0.0)   # 100% second color


Find Intermediate Colors
~~~~~~~~~~~~~~~~~~~~~~~~~

Generate evenly-spaced colors between two endpoints:

.. code-block:: python

    from pychromatic.cutils import find_intermediate_colors

    # 3 colors between red and blue (excluding endpoints)
    colors = find_intermediate_colors('#ff0000', '#0000ff', colors=3, ignore_edges=True)
    print(len(colors))           # 3

    # Include endpoints
    colors = find_intermediate_colors('#ff0000', '#0000ff', colors=3, ignore_edges=False)
    print(len(colors))           # 5 (3 intermediates + 2 edges)


Colormap Creation
~~~~~~~~~~~~~~~~~

Create a ``LinearSegmentedColormap`` from a list of hex colors:

.. code-block:: python

    from pychromatic.cutils import create_colormap

    cmap = create_colormap(['#ff0000', '#ffffff', '#0000ff'])
    # Red → White → Blue diverging colormap

    # Requires at least 2 colors
    create_colormap(['#ff0000'])  # ValueError


Colormap Sampling
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from pychromatic.cutils import get_color

    get_color(0.5, 'viridis')    # sample midpoint
    get_color(0.0, 'plasma')     # sample start
    get_color(1.0, 'inferno')    # sample end


Palette Colormap
~~~~~~~~~~~~~~~~

.. code-block:: python

    from pychromatic.cutils import palette_cmap

    cmap = palette_cmap('rainbow')
    print(cmap.name)             # 'rainbow'


Plotting Colors
~~~~~~~~~~~~~~~

Visualize a list of colors:

.. code-block:: python

    from pychromatic.cutils import plot_colors

    plot_colors(['#ff0000', '#00ff00', '#0000ff'], minimal=True)
    plot_colors(['#ff0000', '#00ff00', '#0000ff'], minimal=False)


Deprecated: ``Color_utils``
----------------------------

The ``Color_utils`` class is a backward-compatibility shim. Use module-level
functions directly:

.. code-block:: python

    # Old (deprecated, emits warning):
    from pychromatic.cutils import Color_utils
    cu = Color_utils()
    cu.hex_to_rgb('#ff0000')

    # New (preferred):
    from pychromatic.cutils import hex_to_rgb
    hex_to_rgb('#ff0000')
