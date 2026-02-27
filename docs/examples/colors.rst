=====================
Working with Colors
=====================

The :class:`~pychromatic.colorclass.Color` class is the fundamental building
block of pychromatic. It wraps a hex color string and provides conversion,
manipulation, and display features.

Creating a Color
----------------

.. code-block:: python

    from pychromatic import Color

    c = Color('#1976d2', name='blue')
    print(c)          # Color('#1976d2', name='blue')
    print(c.hex)      # '#1976d2'
    print(c.rgb)      # [25, 118, 210]
    print(c.hls)      # [0.565..., 0.460..., 0.786...]

The ``name`` parameter is optional:

.. code-block:: python

    c = Color('#ff5722')
    print(c)          # Color('#ff5722')

Input validation
~~~~~~~~~~~~~~~~

``Color`` validates hex input on construction. Invalid values raise
``ValueError``:

.. code-block:: python

    Color('#gggggg')   # ValueError: Invalid hex color '#gggggg'
    Color('ff5722')    # ValueError (missing '#' prefix)
    Color('#fff')      # ValueError (must be 7-char #rrggbb)


Brighten & Darken
-----------------

Adjust luminance in HLS color space:

.. code-block:: python

    c = Color('#1976d2', name='blue')

    c.brighten(0.2)
    print(c.hex)       # lighter shade
    print(c.name)      # 'light-blue'

    c.reset()          # back to original
    c.darken(0.15)
    print(c.name)      # 'dark-blue'

Even pure black can be brightened (the zero-luminance edge case is handled):

.. code-block:: python

    black = Color('#000000', name='black')
    black.brighten(0.5)
    print(black.hex)   # no longer '#000000'


Multiply Operator
-----------------

Use ``*`` to create a **new** Color — the original is unchanged:

.. code-block:: python

    c = Color('#1976d2', name='blue')
    lighter = c * 0.3         # brightened copy
    darker  = c * 1.5         # darkened copy
    print(c.hex)              # still '#1976d2'


Mixing Colors
-------------

Blend two colors in-place:

.. code-block:: python

    c1 = Color('#ff0000', name='red')
    c2 = Color('#0000ff', name='blue')
    c1.mix(c2, ratio=0.5)
    print(c1.hex)      # purple-ish blend
    print(c1.name)     # 'red-blue'


Unpacking & Iteration
---------------------

``Color`` is iterable — you can unpack into ``r, g, b``:

.. code-block:: python

    c = Color('#ff5722')
    r, g, b = c
    print(r, g, b)     # 255 87 34

    # Or convert to list/tuple
    print(list(c))     # [255, 87, 34]
    print(tuple(c))    # (255, 87, 34)


Equality & Hashing
-------------------

Colors compare by hex value (case-insensitive) and are hashable:

.. code-block:: python

    a = Color('#FF5722', name='orange')
    b = Color('#ff5722', name='different')
    print(a == b)       # True

    # Use in sets and as dict keys
    s = {a, b}
    print(len(s))       # 1

    d = {a: 'my color'}
    print(d[b])         # 'my color'


Display
-------

Preview colors in the terminal using Rich:

.. code-block:: python

    c = Color('#e91e63', name='pink')
    c.display()        # prints "pink" in bold #e91e63

Or show a matplotlib swatch:

.. code-block:: python

    c.show()
