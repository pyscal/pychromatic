===========
Quick Start
===========

Install pychromatic and start using it in three lines:

.. code-block:: console

    $ pip install pychromatic

.. code-block:: python

    from pychromatic import Palette, Color

    p = Palette('okabe_ito')   # colorblind-friendly palette
    p.show()                    # matplotlib swatch

    c = Color('#1976d2', name='blue')
    c.display()                 # Rich terminal preview

That's it! Read on for detailed examples of every feature.

What can pychromatic do?
------------------------

* **22 built-in palettes** — qualitative, sequential, and 4 colorblind-safe sets
* **Color manipulation** — brighten, darken, mix, find intermediates
* **Colormap generation** — from any palette or matplotlib cmap name
* **Plot templates** — ``Multiplot``, ``BrokenAxes``, ``chromatify`` decorator
* **Format conversions** — hex, RGB, HLS

Jump to the :doc:`examples/colors` page for hands-on examples.
