==========================
Colormaps & Color Sampling
==========================

pychromatic makes it easy to work with matplotlib colormaps — both sampling
from existing ones and creating new ones from any palette.


Sampling a Colormap: ``get_color()``
------------------------------------

Sample any matplotlib colormap at a position between 0 and 1 to get a hex
color:

.. code-block:: python

    from pychromatic import get_color

    # Sample the viridis colormap at the midpoint
    hex_val = get_color(0.5, 'viridis')
    print(hex_val)               # '#21918c'

    # Endpoints
    start = get_color(0.0, 'viridis')   # dark purple
    end   = get_color(1.0, 'viridis')   # bright yellow

    # Works with any matplotlib cmap
    get_color(0.3, 'plasma')
    get_color(0.7, 'coolwarm')
    get_color(0.5, 'RdYlBu')

The default colormap is ``'viridis'``:

.. code-block:: python

    get_color(0.5)               # same as get_color(0.5, 'viridis')

Values outside [0, 1] raise ``ValueError``:

.. code-block:: python

    get_color(1.5)               # ValueError: value must be between 0 and 1


Building a Gradient
~~~~~~~~~~~~~~~~~~~~

Sample many points to build a discrete gradient:

.. code-block:: python

    import numpy as np

    gradient = [get_color(v, 'inferno') for v in np.linspace(0, 1, 10)]
    print(gradient)              # list of 10 hex strings


Creating a Colormap from a Palette: ``palette_cmap()``
------------------------------------------------------

Turn any pychromatic palette into a matplotlib
``LinearSegmentedColormap``:

.. code-block:: python

    from pychromatic import palette_cmap

    cmap = palette_cmap('rainbow')
    print(cmap.name)             # 'rainbow'

    # Use with matplotlib
    import matplotlib.pyplot as plt
    import numpy as np

    data = np.random.rand(10, 10)
    plt.imshow(data, cmap=cmap)
    plt.colorbar()
    plt.title('rainbow palette as cmap')
    plt.show()

All 22 palettes work:

.. code-block:: python

    palette_cmap('okabe_ito')
    palette_cmap('earth')
    palette_cmap('set1_dark')
    palette_cmap('tol_muted')

Invalid palette names raise ``KeyError`` with a helpful message:

.. code-block:: python

    palette_cmap('nonexistent')
    # KeyError: "Palette 'nonexistent' not found. Available: accent, basics, ..."


Creating Colormaps from Color Lists
------------------------------------

For ad-hoc colormaps from arbitrary colors:

.. code-block:: python

    from pychromatic.cutils import create_colormap

    cmap = create_colormap(['#ff0000', '#ffffff', '#0000ff'])
    # Red → White → Blue diverging colormap

At least 2 colors are required:

.. code-block:: python

    create_colormap(['#ff0000'])   # ValueError


Colormap from a Palette Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also use a ``Palette`` instance directly:

.. code-block:: python

    from pychromatic import Palette

    p = Palette('earth')
    cmap = p.get_cmap()
    # Equivalent to palette_cmap('earth')


Combining Techniques
--------------------

Sample your own palette-based colormap:

.. code-block:: python

    from pychromatic import palette_cmap, get_color
    from pychromatic.cutils import create_colormap

    # Create a cmap from 'dark' palette, then sample it
    cmap = palette_cmap('dark')

    # Get 5 evenly-spaced colors from the cmap
    sampled = [get_color(v, cmap.name) for v in [0.0, 0.25, 0.5, 0.75, 1.0]]

    # Or register it so matplotlib knows it by name
    import matplotlib.pyplot as plt
    plt.colormaps.register(cmap, name='pychromatic_dark')
    # Now usable as: plt.scatter(x, y, c=z, cmap='pychromatic_dark')
