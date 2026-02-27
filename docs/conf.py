"""Sphinx configuration for pychromatic documentation."""

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import pychromatic

# -- Project information ---------------------------------------------------

project = "pychromatic"
copyright = "2019-2026, Sarath Menon"
author = "Sarath Menon"
version = pychromatic.__version__
release = pychromatic.__version__

# -- General configuration -------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
source_suffix = ".rst"
root_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "friendly"

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True

# Autodoc settings
autodoc_member_order = "bysource"
autodoc_typehints = "description"

# Intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "numpy": ("https://numpy.org/doc/stable", None),
}

# -- Options for HTML output -----------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "style_nav_header_background": "#1976d2",
}
html_static_path = ["_static"]
html_title = f"pychromatic {version}"
html_short_title = "pychromatic"
html_show_sourcelink = True
html_baseurl = "https://pyscal.github.io/pychromatic/"

# -- Extension configuration -----------------------------------------------

htmlhelp_basename = "pychromaticdoc"
