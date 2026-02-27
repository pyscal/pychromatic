=================
Palette Reference
=================

All 22 built-in palettes available through ``Palette("name")``.


Qualitative Palettes
--------------------

Best for categorical data where no natural order exists.

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Name
     - Colors
     - Color Names
   * - ``default``
     - 15
     - blue, red, green, orange, purple, bluegrey, lightblue, pink,
       lightgreen, yellow, teal, grey, brown, lime, cyan
   * - ``pastels``
     - 12
     - color1–color12
   * - ``basics``
     - 9
     - color1–color9
   * - ``set1_dark``
     - 8
     - color1–color8
   * - ``set1_pastel``
     - 8
     - color1–color8
   * - ``excel``
     - 7
     - color1–color7
   * - ``set2``
     - 5
     - color1–color5
   * - ``google``
     - 5
     - color1–color5
   * - ``set3``
     - 5
     - color1–color5
   * - ``set4``
     - 5
     - color1–color5
   * - ``dark``
     - 5
     - color1–color5
   * - ``earth``
     - 5
     - color1–color5
   * - ``set6``
     - 5
     - color1–color5
   * - ``set7``
     - 5
     - color1–color5
   * - ``accent``
     - 15
     - lred, lyellow, lgreen, lblue, lgrey, dred, dyellow, dgreen,
       dblue, dgrey, pred, pyellow, pgreen, pblue, pgrey


Sequential Palettes
-------------------

Best for data with a natural order or gradient.

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Name
     - Colors
     - Color Names
   * - ``set5``
     - 5
     - color1–color5
   * - ``rainbow``
     - 5
     - color1–color5


Colorblind-Friendly Palettes
-----------------------------

Designed to be distinguishable by viewers with common forms of
color-vision deficiency.

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Name
     - Colors
     - Color Names
   * - ``okabe_ito``
     - 8
     - orange, sky, green, yellow, blue, vermilion, purple, black
   * - ``tableau10``
     - 10
     - blue, orange, red, teal, green, yellow, purple, pink, brown, grey
   * - ``tol_bright``
     - 7
     - blue, pink, green, yellow, cyan, purple, grey
   * - ``tol_muted``
     - 9
     - indigo, sky, teal, green, olive, sand, rose, wine, violet


Using a Palette
---------------

.. code-block:: python

    from pychromatic import Palette

    # Load any palette by name
    p = Palette("rainbow")
    print(len(p))             # 5
    print(p[0])               # Color object for first color

    # List all available palette names
    from pychromatic.colors import color_palettes
    print(list(color_palettes.keys()))


Standalone Colorblind Dicts
---------------------------

The four colorblind palettes are also available as plain dicts:

.. code-block:: python

    from pychromatic import okabe_ito, tableau10, tol_bright, tol_muted

    # Access colors by name
    okabe_ito["sky"]       # '#56B4E9'
    tableau10["teal"]      # '#76B7B2'
    tol_bright["cyan"]     # '#66CCEE'
    tol_muted["wine"]      # '#882255'
