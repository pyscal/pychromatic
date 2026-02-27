===============
Plot Templates
===============

pychromatic provides opinionated matplotlib plot templates that handle
layout, styling, and color cycling automatically.


Multiplot
---------

Create multi-panel figures with automatic grid layout:

.. code-block:: python

    from pychromatic import Multiplot
    import numpy as np

    m = Multiplot(columns=2, rows=2)

    # Access axes by (row, col)
    ax1 = m[0, 0]
    ax2 = m[0, 1]
    ax3 = m[1, 0]
    ax4 = m[1, 1]

    x = np.linspace(0, 2 * np.pi, 100)
    ax1.plot(x, np.sin(x))
    ax1.set_title('sin(x)')

    ax2.plot(x, np.cos(x))
    ax2.set_title('cos(x)')

    ax3.plot(x, np.sin(2 * x))
    ax4.plot(x, np.cos(2 * x))

    m.show()


Custom Sizing
~~~~~~~~~~~~~

Control figure dimensions and grid proportions:

.. code-block:: python

    m = Multiplot(
        columns=3,
        rows=2,
        width=600,
        fraction=1.0,
        ratio=0.5,
        width_ratios=[2, 1, 1],
        height_ratios=[1, 2],
        wspace=0.3,
        hspace=0.4,
    )


GridSpec Keyword Forwarding
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pass any ``GridSpec`` keyword via ``gridspec_kwargs``:

.. code-block:: python

    m = Multiplot(
        columns=2,
        rows=1,
        gridspec_kwargs={'left': 0.1, 'right': 0.9, 'bottom': 0.15},
    )


Subplots Within Subplots
~~~~~~~~~~~~~~~~~~~~~~~~~

Split any panel into a sub-grid:

.. code-block:: python

    m = Multiplot(columns=2, rows=1)

    # Split the left panel into 2×1
    m.add_subplot((0, 0), rows=2, columns=1)

    # Access sub-axes with three-index tuple
    sub_ax_top    = m[0, 0, 0]
    sub_ax_bottom = m[0, 0, 1]

    sub_ax_top.plot([1, 2, 3])
    sub_ax_bottom.bar([1, 2, 3], [1, 4, 9])


Styling Axes
~~~~~~~~~~~~

Convenience method for common axis modifications (labels, limits, spines):

.. code-block:: python

    m = Multiplot(columns=1, rows=1)
    m.style_axes(
        (0, 0),
        xlabel='Time (s)',
        ylabel='Amplitude',
        title='Signal',
        xlim=(0, 10),
        ylim=(-1, 1),
        hide_spines=['top', 'right'],
        labelsize=14,
    )


Inset Axes
~~~~~~~~~~

Add inset plots to any panel:

.. code-block:: python

    m = Multiplot(columns=1, rows=1)
    m.add_inset((0, 0), width='30%', height='30%', loc=1)

    # Access the inset axis
    inset_ax = m[0, 0, 0]
    inset_ax.plot([1, 2, 3], [3, 1, 2])


Tables
~~~~~~

Add data tables to panels:

.. code-block:: python

    m = Multiplot(columns=2, rows=1)

    m.add_table(
        (0, 1),
        columnlist=[[1, 2, 3], [4, 5, 6]],
        header=['A', 'B'],
        fmt=['%d', '%d'],
    )


The ``chromatify`` Decorator
----------------------------

Auto-style any function that returns a matplotlib ``Axes``:

.. code-block:: python

    from pychromatic import chromatify

    @chromatify
    def my_plot():
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 9])
        return ax

    ax = my_plot()
    # Axes now have:
    #   - hidden top/right spines
    #   - custom tick styling
    #   - automatic color cycling from set6 palette

Pass keyword arguments to customize:

.. code-block:: python

    ax = my_plot(
        xlabel='X axis',
        ylabel='Y axis',
        colors=['#ff0000', '#00ff00', '#0000ff'],
        labelfont=14,
    )

The decorator preserves the original function's metadata (name, docstring)
thanks to ``functools.wraps``:

.. code-block:: python

    print(my_plot.__name__)     # 'my_plot'


BrokenAxes
----------

Create plots with broken x- or y-axes:

.. code-block:: python

    from pychromatic import BrokenAxes

    # Broken x-axis: two x-ranges, one y-range
    ba = BrokenAxes(
        x=[0, 5, 20, 30],      # two segments: [0,5] and [20,30]
        y=[0, 10],               # continuous y
    )

    # Plot on the sub-axes
    ax_left  = ba.axes[1]       # left segment
    ax_right = ba.axes[2]       # right segment

    import numpy as np
    x1 = np.linspace(0, 5, 50)
    x2 = np.linspace(20, 30, 50)
    ax_left.plot(x1, np.sin(x1))
    ax_right.plot(x2, np.sin(x2))

.. code-block:: python

    # Broken y-axis: one x-range, two y-ranges
    ba = BrokenAxes(
        x=[0, 10],
        y=[0, 20, 80, 100],     # two segments: [0,20] and [80,100]
    )

BrokenAxes can also be embedded inside a ``Multiplot``:

.. code-block:: python

    from pychromatic import Multiplot

    m = Multiplot(columns=2, rows=1)
    m.add_brokenaxes(
        (0, 0),
        x=[0, 5, 20, 30],
        y=[0, 10],
    )
