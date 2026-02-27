===========
pychromatic
===========

A color palette manager and matplotlib plotting utility for Python.


* Free software: GNU General Public License v3
* Documentation: https://pychromatic.readthedocs.io.


Features
--------

* **20 curated color palettes** including 4 colorblind-friendly sets
  (Okabe–Ito, Tableau 10, Tol Bright, Tol Muted)
* Color manipulation: brighten, darken, mix, find intermediates
* Color format conversions: hex, RGB, HLS
* Generate matplotlib colormaps from any color list
* Opinionated matplotlib plot templates (``Multiplot``, ``BrokenAxes``)
* ``chromatify`` decorator for auto-styling matplotlib subplots
* Rich terminal color preview via ``Color.display()``

Installation
------------

.. code-block:: console

    $ pip install pychromatic

For development:

.. code-block:: console

    $ pip install -e ".[dev]"

Quick Start
-----------

.. code-block:: python

    from pychromatic import Palette, Color

    # Use a built-in palette
    p = Palette('default')
    p.show()

    # Work with individual colors
    c = Color('#1976d2', name='blue')
    c.brighten(0.2)
    c.display()

Colorblind-Friendly Palettes
-----------------------------

pychromatic ships four accessibility-first palettes that can be used as
``Palette`` objects **or** imported directly as plain dictionaries:

.. code-block:: python

    from pychromatic import okabe_ito, tableau10, tol_bright, tol_muted

    # Use as a Palette object
    p = Palette('okabe_ito')
    p.show()

    # Or grab individual hex values from the dict
    print(okabe_ito['orange'])   # '#E69F00'
    print(tableau10['teal'])     # '#76B7B2'

Available colorblind palettes:

* **okabe_ito** — 8 colors from the Okabe & Ito (2008) universal palette
* **tableau10** — 10 colors from Tableau's default categorical palette
* **tol_bright** — 7 high-contrast colors from Paul Tol's bright scheme
* **tol_muted** — 9 low-chroma colors from Paul Tol's muted scheme

Available Palettes
------------------

.. list-table::
   :header-rows: 1

   * - Name
     - Colors
     - Type
   * - ``default``
     - 15
     - sequential
   * - ``pastels``
     - 12
     - qualitative
   * - ``basics``
     - 9
     - qualitative
   * - ``set1_dark``
     - 8
     - qualitative
   * - ``set1_pastel``
     - 8
     - qualitative
   * - ``excel``
     - 7
     - qualitative
   * - ``set2`` – ``set7``
     - 5
     - qualitative
   * - ``google``
     - 5
     - qualitative
   * - ``dark``
     - 5
     - qualitative
   * - ``earth``
     - 5
     - qualitative
   * - ``rainbow``
     - 5
     - qualitative
   * - ``accent``
     - 15
     - qualitative
   * - ``okabe_ito``
     - 8
     - qualitative (colorblind-safe)
   * - ``tableau10``
     - 10
     - qualitative (colorblind-safe)
   * - ``tol_bright``
     - 7
     - qualitative (colorblind-safe)
   * - ``tol_muted``
     - 9
     - qualitative (colorblind-safe)
