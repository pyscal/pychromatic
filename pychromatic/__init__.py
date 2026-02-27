__version__ = "0.6.0"

from pychromatic.colorclass import Color
from pychromatic.colors import okabe_ito, tableau10, tol_bright, tol_muted
from pychromatic.decors import chromatify
from pychromatic.palette import Palette
from pychromatic.plutils import BrokenAxes, Multiplot

__all__ = [
    "Color",
    "Palette",
    "Multiplot",
    "BrokenAxes",
    "chromatify",
    "okabe_ito",
    "tableau10",
    "tol_bright",
    "tol_muted",
]
