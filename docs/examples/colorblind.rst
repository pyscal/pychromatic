============================
Colorblind-Friendly Palettes
============================

pychromatic ships four accessibility-first palettes designed for readers with
color vision deficiencies. Each is available as both a ``Palette`` object and
an importable Python dictionary.

Available Palettes
------------------

.. list-table::
   :header-rows: 1
   :widths: 20 10 40

   * - Name
     - Colors
     - Source
   * - ``okabe_ito``
     - 8
     - Okabe & Ito (2008) universal palette
   * - ``tableau10``
     - 10
     - Tableau default categorical scheme
   * - ``tol_bright``
     - 7
     - Paul Tol's bright qualitative scheme
   * - ``tol_muted``
     - 9
     - Paul Tol's muted qualitative scheme


Using as Palette Objects
------------------------

.. code-block:: python

    from pychromatic import Palette

    p = Palette('okabe_ito')
    print(len(p))                # 8
    p.show()

    # Access by name
    print(p.orange.hex)          # '#E69F00'
    print(p.sky.hex)             # '#56B4E9'

    # Iterate
    for color in p:
        print(f"{color.name}: {color.hex}")


Using as Dictionaries
---------------------

For simple lookups without creating objects:

.. code-block:: python

    from pychromatic import okabe_ito, tableau10, tol_bright, tol_muted

    # Direct access
    print(okabe_ito['orange'])     # '#E69F00'
    print(tableau10['teal'])       # '#76B7B2'
    print(tol_bright['cyan'])      # '#66CCEE'
    print(tol_muted['indigo'])     # '#332288'

    # Use in matplotlib
    import matplotlib.pyplot as plt

    for name, hex_val in okabe_ito.items():
        plt.bar(name, 1, color=hex_val)
    plt.xticks(rotation=45)
    plt.title('Okabe-Ito palette')
    plt.tight_layout()
    plt.show()


Okabe-Ito
~~~~~~~~~

.. code-block:: python

    from pychromatic import okabe_ito

    # 8 colors designed for universal readability
    print(okabe_ito)
    # {'orange': '#E69F00', 'sky': '#56B4E9', 'green': '#009E73',
    #  'yellow': '#F0E442', 'blue': '#0072B2', 'vermilion': '#D55E00',
    #  'purple': '#CC79A7', 'black': '#000000'}


Tableau 10
~~~~~~~~~~

.. code-block:: python

    from pychromatic import tableau10

    # 10 colors from Tableau's default categorical palette
    print(list(tableau10.keys()))
    # ['blue', 'orange', 'red', 'teal', 'green',
    #  'yellow', 'purple', 'pink', 'brown', 'grey']


Tol Bright
~~~~~~~~~~

.. code-block:: python

    from pychromatic import tol_bright

    # 7 high-contrast colors
    print(list(tol_bright.keys()))
    # ['blue', 'pink', 'green', 'yellow', 'cyan', 'purple', 'grey']


Tol Muted
~~~~~~~~~

.. code-block:: python

    from pychromatic import tol_muted

    # 9 low-chroma colors for dense visualizations
    print(list(tol_muted.keys()))
    # ['indigo', 'sky', 'teal', 'green', 'olive',
    #  'sand', 'rose', 'wine', 'violet']


Generating Colormaps
--------------------

All colorblind palettes work with ``palette_cmap()``:

.. code-block:: python

    from pychromatic import palette_cmap

    cmap = palette_cmap('okabe_ito')

    import matplotlib.pyplot as plt
    import numpy as np

    data = np.random.rand(8, 8)
    plt.imshow(data, cmap=cmap)
    plt.colorbar()
    plt.title('Okabe-Ito as continuous cmap')
    plt.show()
